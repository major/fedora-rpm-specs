%if 0%{?fedora} >= 37
%bcond_without doc
%else
# need Sphinx >= 3.5.0
# c9s has 3.4.3
# f36 has 3.4.0
%bcond_with doc
%endif

Name:           python-django3
%global         pkgname Django
%global         ver 3.2.18
#global         pre ...
%global         real_version %{ver}%{?pre:%{pre}}
Version:        %{ver}%{?pre:~%{pre}}
Release:        %autorelease
Summary:        A high-level Python Web framework

License:        BSD-3-Clause
URL:            https://www.djangoproject.com/
Source0:        %{pypi_source %{pkgname} %{real_version}}

# skip tests requiring network connectivity
Patch:          Django-skip-net-tests.patch
# tag failing tests
Patch:          Django-tag-failing-tests.patch

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
Conflicts:      python-django-bash-completion

%description bash-completion
This package contains the Bash completion files form Django high-level
Python Web framework.


%if %{with doc}
%package -n python3-django3-doc
Summary:        Documentation for Django
Suggests:       python3-django3 = %{version}-%{release}
BuildRequires:  make
BuildRequires:  python3-sphinx
BuildRequires:  python3-psycopg2

%description -n python3-django3-doc
This package contains the documentation for the Django high-level
Python Web framework.
%endif


%package -n python3-django3
Summary:        A high-level Python Web framework

Recommends:     (%{name}-bash-completion = %{version}-%{release} if bash)

BuildRequires:  python3-devel

Provides:       bundled(jquery) = 2.2.3
Provides:       bundled(xregexp) = 2.0.0

Conflicts:      python3-django

%description -n python3-django3 %_description

%prep
%autosetup -p1 -n %{pkgname}-%{real_version}

# hard-code python3 in django-admin
pushd django
for file in bin/django-admin.py conf/project_template/manage.py-tpl ; do
    sed -i "s/\/env python/\/python3/" $file ;
done
popd

# Remove unnecessary test BRs
sed -i '/^pywatchman\b/d' tests/requirements/py3.txt
sed -i '/^tzdata$/d' tests/requirements/py3.txt

%generate_buildrequires
%pyproject_buildrequires -r tests/requirements/py3.txt

%build
%pyproject_wheel


%install
%pyproject_install
%pyproject_save_files django

%if %{with doc}
# build documentation
(cd docs && mkdir djangohtml && mkdir -p _build/{doctrees,html} && make html)
cp -ar docs ..
%endif

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

%{python3} runtests.py --settings=test_sqlite --verbosity=2 --exclude-tag failed


%files bash-completion
%{_datadir}/bash-completion

%if %{with doc}
%files -n python3-django3-doc
%doc docs/_build/html/*
%endif

%files -n python3-django3 -f %{pyproject_files}
%doc AUTHORS README.rst
%license LICENSE
%{_bindir}/django-admin.py
%{_bindir}/django-admin
%{_bindir}/django-admin-3
%{_bindir}/django-admin-%{python3_version}
%{_bindir}/python3-django-admin
%{_mandir}/man1/django-admin.1*


%changelog
%autochangelog
