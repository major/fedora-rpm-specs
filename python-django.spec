Name:           python-django
%global         pkgname Django
%global         ver 4.2.6
#global         pre ...
%global         real_version %{ver}%{?pre:%{pre}}
Version:        %{ver}%{?pre:~%{pre}}
Release:        %autorelease
Summary:        A high-level Python Web framework

License:        BSD-3-Clause
URL:            https://www.djangoproject.com/
Source0:        %{pypi_source %{pkgname} %{real_version}}

# FAIL: test_complex_override_warning (settings_tests.tests.TestComplexSettingOverride.test_complex_override_warning)
# Regression test for #19031
# ----------------------------------------------------------------------
# Traceback (most recent call last):
#   File "/builddir/build/BUILD/Django-4.2.1/tests/settings_tests/tests.py", line 400, in test_complex_override_warning
#     self.assertEqual(cm.filename, __file__)
# AssertionError: '/usr/lib64/python3.12/unittest/case.py' != '/builddir/build/BUILD/Django-4.2.1/tests/settings_tests/tests.py'
# - /usr/lib64/python3.12/unittest/case.py
# + /builddir/build/BUILD/Django-4.2.1/tests/settings_tests/tests.py
Patch:          dirty-hack-remove-assert.patch

BuildArch:      noarch

%global _description %{expand:
Django is a high-level Python Web framework that encourages rapid
development and a clean, pragmatic design. It focuses on automating as
much as possible and adhering to the DRY (Don't Repeat Yourself)
principle.}

%description %_description


%package bash-completion
Summary:        Bash completion files for Django
BuildRequires:  bash-completion
Requires:       bash-completion

%description bash-completion
This package contains the Bash completion files form Django high-level
Python Web framework.


%package -n python3-django-doc
Summary:        Documentation for Django
Suggests:       python3-django = %{version}-%{release}
BuildRequires:  make

%description -n python3-django-doc
This package contains the documentation for the Django high-level
Python Web framework.


%package -n python3-django
Summary:        A high-level Python Web framework

Recommends:     (%{name}-bash-completion = %{version}-%{release} if bash)

BuildRequires:  python3-devel
BuildRequires:  python3-asgiref

Provides: bundled(jquery) = 2.2.3
Provides: bundled(xregexp) = 2.0.0

%description -n python3-django %_description

%prep
%autosetup -p1 -n %{pkgname}-%{real_version}

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
sed -i '/^blacken-docs\b/d' docs/requirements.txt

%generate_buildrequires
%pyproject_buildrequires -r tests/requirements/{py3,postgres,mysql,oracle}.txt docs/requirements.txt

%build
%pyproject_wheel


%install
%pyproject_install
%pyproject_save_files django


# build documentation
(cd docs && mkdir djangohtml && mkdir -p _build/{doctrees,html} && make html)
cp -ar docs ..

# install man pages (for the main executable only)
mkdir -p %{buildroot}%{_mandir}/man1/
cp -p docs/man/* %{buildroot}%{_mandir}/man1/

# install bash completion script
bashcompdir=$(pkg-config --variable=completionsdir bash-completion)
mkdir -p %{buildroot}$bashcompdir
install -m 0644 -p extras/django_bash_completion \
  %{buildroot}$bashcompdir/django-admin.py

for file in django-admin django-admin-3 django-admin-%{python3_version} python3-django-admin manage.py ; do
   ln -s django-admin.py %{buildroot}$bashcompdir/$file
done

# Add backward compatible links to %%{_bindir}
ln -s ./django-admin %{buildroot}%{_bindir}/django-admin-3
ln -s ./django-admin %{buildroot}%{_bindir}/django-admin-%{python3_version}
ln -s ./django-admin %{buildroot}%{_bindir}/python3-django-admin

# remove .po files
find %{buildroot} -name "*.po" | xargs rm -f
sed -i '/.po$/d' %{pyproject_files}

%check
cd %{_builddir}/%{pkgname}-%{real_version}
export PYTHONPATH=$(pwd)
cd tests

# disable two tests due to regression in 3.12b4:
# https://github.com/python/cpython/issues/106669
%{python3} runtests.py --settings=test_sqlite --verbosity=2 --parallel 1 \
%if v"%{python3_version}" >= v"3.12"
  -k "not test_safe_mime_multipart and not test_unicode_address_header"
%endif

%files bash-completion
%{_datadir}/bash-completion

%files -n python3-django-doc
%doc docs/_build/html/*

%files -n python3-django -f %{pyproject_files}
%doc AUTHORS README.rst
%license LICENSE
%{_bindir}/django-admin
%{_bindir}/django-admin-3
%{_bindir}/django-admin-%{python3_version}
%{_bindir}/python3-django-admin
%{_mandir}/man1/django-admin.1*


%changelog
%autochangelog
