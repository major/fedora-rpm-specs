%if ! 0%{?rhel} || 0%{?rhel} >= 10
%bcond_without testcoverage
%bcond_with setup_py
%else
%bcond_with testcoverage
%bcond_without setup_py
%endif

%if ! 0%{?rhel} || 0%{?rhel} >= 9
%bcond_with compatbuild
%else
%bcond_without compatbuild
%endif

%if 0%{undefined pyproject_files}
%global pyproject_files %{_builddir}/%{name}-%{version}-%{release}.%{_arch}-pyproject-files
%endif

%global srcname rpmautospec_core
%global canonicalname %{py_dist_name %{srcname}}

Name: python-%{canonicalname}
Version: 0.1.1
Release: %autorelease
Summary: Minimum functionality for rpmautospec

License: MIT
URL: https://github.com/fedora-infra/%{canonicalname}
Source0: %{pypi_source %{srcname}}
BuildArch: noarch
BuildRequires: python3-devel >= 3.6.0
# The dependencies needed for testing don’t get auto-generated.
BuildRequires: python3dist(pytest)
%if %{with testcoverage}
BuildRequires: python3dist(pytest-cov)
%endif
BuildRequires: sed

%if %{without compatbuild}
%generate_buildrequires
%if %{without setup.py}
%{pyproject_buildrequires}
%else
( %{pyproject_buildrequires} ) | grep -v poetry
echo 'python3dist(setuptools)'
%endif
%else
BuildRequires: python3dist(setuptools)
%endif

%global _description %{expand:
This package contains minimum functionality to determine if an RPM spec file
uses rpmautospec features.}

%description %_description

%package -n python3-%{canonicalname}
Summary: %{summary}
%if %{with compatbuild}
%py_provides python3-%{canonicalname}
%endif

%description -n python3-%{canonicalname} %_description

%prep
%autosetup -n %{srcname}-%{version}

%if %{without testcoverage}
cat << PYTESTINI > pytest.ini
[pytest]
addopts =
PYTESTINI
%endif

%if %{with setup_py}
cat << SETUPPY > setup.py
from setuptools import setup

setup(name="%{canonicalname}", version="%{version}")
SETUPPY
%endif

%build
%if %{without compatbuild}
%pyproject_wheel
%else
%py3_build
%endif

%install
%if %{without compatbuild}
%pyproject_install
%pyproject_save_files %{srcname}
# Work around poetry not listing license files as such in package metadata.
sed -i -e 's|^\(.*/LICENSE\)|%%license \1|g' %{pyproject_files}
%else
%py3_install
echo '%{python3_sitelib}/%{srcname}*' > %{pyproject_files}
%endif

%check
%pytest

%files -n python3-%{canonicalname} -f %{pyproject_files}
%doc README.md
%if %{with compatbuild}
%license LICENSE
%endif

%changelog
%autochangelog
