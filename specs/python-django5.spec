# Main Django, i.e. whether this is the main Django version in the distribution
# that owns /usr/bin/django-admin and other unique paths
# based on Python packaging, see e.g. python3.13
%if 0%{?fedora} >= 42
%bcond_without main_django
%else
%bcond_with main_django
%endif

%global major_ver 5

Name:           python-django%{major_ver}
Version:        5.1.6
Release:        %autorelease
Summary:        A high-level Python Web framework

# Django: BSD-3-Clause
# Bundled Python code: PSF-2.0
# Font Awesome font: OFL-1.1
# Font Awesome icons: MIT
# jquery, select2, xregexp: MIT
# gis/gdal: BSD-3-Clause
# gis/geos: BSD-3-Clause
License:        BSD-3-Clause AND PSF-2.0 AND MIT AND OFL-1.1
URL:            https://www.djangoproject.com/
Source:         %{pypi_source Django}
Source:         %{name}.rpmlintrc

Patch:          Django-allow-setuptools-74.diff
# these tests would sometimes trigger the following exception
# UnicodeEncodeError: 'utf-8' codec can't encode characters in position 12-13: surrogates not allowed
Patch:          Django-skip-flaky-unicode-tests.diff

# This allows to build the package without tests, e.g. when bootstrapping new Python version
%bcond tests    1

BuildArch:      noarch

%global _description %{expand:
Django is a high-level Python Web framework that encourages rapid
development and a clean, pragmatic design. It focuses on automating as
much as possible and adhering to the DRY (Don't Repeat Yourself)
principle.}

%description %_description


%if %{with main_django}
%global pkgname python3-django
%else
%global pkgname python3-django%{major_ver}
%endif

%package -n %{pkgname}-bash-completion
Summary:        Bash completion files for Django
BuildRequires:  bash-completion
Requires:       bash-completion

# Make sure this replaces any other Django bash-completion package
Provides:       python-django-bash-completion-impl
Conflicts:      python-django-bash-completion-impl

%description -n %{pkgname}-bash-completion
This package contains the Bash completion files form Django high-level
Python Web framework.


%package -n %{pkgname}-doc
Summary:        Documentation for Django
# Font Awesome: CC-BY-4.0, OFL-1.1, MIT
License:        BSD-3-Clause AND CC-BY-4.0 AND OFL-1.1 AND MIT
Suggests:       %{pkgname} = %{version}-%{release}
BuildRequires:  make

# Make sure this replaces any other Django doc package
Provides:       python-django-doc-impl
Conflicts:      python-django-doc-impl

%description -n %{pkgname}-doc
This package contains the documentation for the Django high-level
Python Web framework.


%package -n %{pkgname}
Summary:        A high-level Python Web framework

Recommends:     (%{pkgname}-bash-completion = %{version}-%{release} if bash-completion)

BuildRequires:  python3-devel
BuildRequires:  python3-asgiref

# see django/contrib/admin/static/admin/js/vendor/
Provides:       bundled(jquery) = 3.6.4
Provides:       bundled(select2) = 4.0.13
Provides:       bundled(xregexp) = 3.2.0

# Make sure this replaces any other Django package
Provides:       python-django-impl
Conflicts:      python-django-impl

%description -n %{pkgname} %_description

%prep
%autosetup -p1 -n Django-%{version}

# hard-code python3 in django-admin
pushd django
for file in conf/project_template/manage.py-tpl ; do
    sed -i "s/\/env python/\/python3/" $file ;
done
popd

# Use non optimised psycopg for tests
# Not available in Fedora
sed -i 's/psycopg\[binary\]>=3\.1\.8/psycopg>=3.1.8/' tests/requirements/postgres.txt

# Remove unnecessary test BRs
sed -i '/^pywatchman\b/d' tests/requirements/py3.txt
sed -i '/^tzdata$/d' tests/requirements/py3.txt

# Remove deps on code checkers/linters
sed -i '/^black\b/d' tests/requirements/py3.txt
sed -i '/^black\b/d' docs/requirements.txt
sed -i '/^blacken-docs\b/d' docs/requirements.txt

%generate_buildrequires
%pyproject_buildrequires -r %{?with_tests:tests/requirements/{py3,postgres,mysql,oracle}.txt} docs/requirements.txt

%build
%pyproject_wheel


%install
%pyproject_install
%pyproject_save_files django

# build documentation
(cd docs && mkdir djangohtml && mkdir -p _build/{doctrees,html} && make html)
mkdir -p %{buildroot}%{_docdir}/python3-django-doc
cp -ar docs/_build/html/* %{buildroot}%{_docdir}/python3-django-doc/

# install man pages (for the main executable only)
mkdir -p %{buildroot}%{_mandir}/man1/
cp -p docs/man/* %{buildroot}%{_mandir}/man1/

# install bash completion script
mkdir -p %{buildroot}%{bash_completions_dir}
install -m 0644 -p extras/django_bash_completion \
  %{buildroot}%{bash_completions_dir}/django-admin.py

for file in django-admin django-admin-3 django-admin-%{python3_version} python3-django-admin manage.py ; do
   ln -s django-admin.py %{buildroot}%{bash_completions_dir}/$file
done

# Add backward compatible links to %%{_bindir}
ln -s ./django-admin %{buildroot}%{_bindir}/django-admin-3
ln -s ./django-admin %{buildroot}%{_bindir}/django-admin-%{python3_version}
ln -s ./django-admin %{buildroot}%{_bindir}/python3-django-admin

# remove .po files
find %{buildroot} -name "*.po" | xargs rm -f
sed -i '/.po$/d' %{pyproject_files}

%check
# many contrib modules assume a configured app, "Requested setting INSTALLED_APPS..."
# the rest needs optional dependencies
%{pyproject_check_import \
    -e 'django.contrib.*' \
    -e 'django.core.serializers.pyyaml' \
    -e 'django.db.backends.mysql*' \
    -e 'django.db.backends.oracle*' \
    -e 'django.db.backends.postgresql*'}

%if %{with tests}
cd %{_builddir}/Django-%{version}
export PYTHONPATH=$(pwd)
cd tests

%{python3} runtests.py --settings=test_sqlite --verbosity=2
%endif

%files -n %{pkgname}-bash-completion
%{bash_completions_dir}/*

%files -n %{pkgname}-doc
%doc %{_docdir}/python3-django-doc/*
%license LICENSE
%license %{_docdir}/python3-django-doc/_static/fontawesome/LICENSE.txt

%files -n %{pkgname} -f %{pyproject_files}
%doc AUTHORS README.rst
%doc %{python3_sitelib}/django/contrib/admin/static/admin/img/README.txt
%license %{python3_sitelib}/django/contrib/admin/static/admin/css/vendor/select2/LICENSE-SELECT2.md
%license %{python3_sitelib}/django/contrib/admin/static/admin/img/LICENSE
%license %{python3_sitelib}/django/contrib/admin/static/admin/js/vendor/jquery/LICENSE.txt
%license %{python3_sitelib}/django/contrib/admin/static/admin/js/vendor/select2/LICENSE.md
%license %{python3_sitelib}/django/contrib/admin/static/admin/js/vendor/xregexp/LICENSE.txt
%license %{python3_sitelib}/django/contrib/gis/gdal/LICENSE
%license %{python3_sitelib}/django/contrib/gis/geos/LICENSE
%{_bindir}/django-admin
%{_bindir}/django-admin-3
%{_bindir}/django-admin-%{python3_version}
%{_bindir}/python3-django-admin
%{_mandir}/man1/django-admin.1*


%changelog
%autochangelog
