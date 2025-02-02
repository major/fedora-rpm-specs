# Build doc by default
%bcond_without doc

%global srcname django-extensions
%global modname django_extensions

Name:           python-%{srcname}
Version:        3.2.3
Release:        %autorelease
Summary:        Extensions for Django

License:        GPL-3.0-or-later
URL:            https://github.com/django-extensions/django-extensions
# PyPI tarball doesn't contain some requirements files
# Source0:        %%{pypi_source %%{srcname}}
Source0:        %{url}/archive/%{version}/%{srcname}-%{version}.tar.gz

BuildArch:      noarch

BuildRequires:	make
BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  python%{python3_pkgversion}-setuptools

%if %{with doc}
BuildRequires:  python%{python3_pkgversion}-sphinx
BuildRequires:  make
%endif

%global _description %{expand:
Django Extensions is a collection of custom extensions for the Django
Framework.}

%description %{_description}


%package -n python%{python3_pkgversion}-%{srcname}
Summary:        %{summary}

%description -n python%{python3_pkgversion}-%{srcname} %{_description}


%package -n python%{python3_pkgversion}-%{srcname}-doc
Summary:        Documentation for %{srcname}
Suggests:       python%{python3_pkgversion}-%{srcname} = %{version}-%{release}

%description -n python%{python3_pkgversion}-%{srcname}-doc %{_description}
This package contains the documentation for %{srcname}.


%prep
%autosetup -p1 -n %{srcname}-%{version}
# Remove commands incompatible with Python 3.12
%if 0%{?python3_version_nodots} >= 312
# https://github.com/django-extensions/django-extensions/issues/1831
rm django_extensions/management/commands/mail_debug.py
rm tests/management/commands/test_mail_debug.py
# https://github.com/django-extensions/django-extensions/issues/1832
rm django_extensions/management/commands/shell_plus.py
rm -r tests/management/commands/shell_plus_tests/
%endif
# Remove coverage
sed -i /pytest-cov/d requirements-dev.txt
sed -Ei 's/--cov[^ =]*[ =][^ =]+//g' setup.cfg

%generate_buildrequires
%pyproject_buildrequires -t


%build
%pyproject_wheel

%if %{with doc}
(cd docs && make html)
%endif


%install
%pyproject_install
%pyproject_save_files %{modname}


%check
# tox.ini invokes make invokes pytest
# call directly so we can disable tests that require network
SELECTOR="not PipCheckerTests"
%if 0%{?el9}
# minor differences in generated HTML
# E   - </span><span class="s2">
# E   + </span><span class="w"><span class="s2">
# E   ?              ++++++++++++++++
SELECTOR+=" and not test_should_highlight_bash_syntax_without_name"
%endif
%pytest -v django_extensions tests \
  -k "${SELECTOR}" \
  --ignore tests/test_dumpscript.py
# run this separately, see https://github.com/django-extensions/django-extensions/issues/1871
%pytest -v tests/test_dumpscript.py


%files -n python%{python3_pkgversion}-%{srcname} -f %{pyproject_files}
%doc CHANGELOG.md CONTRIBUTING.md README.rst

%if %{with doc}
%files -n python%{python3_pkgversion}-%{srcname}-doc
%license LICENSE
%doc docs/_build/html/*
%endif


%changelog
%autochangelog
