%bcond_with testcoverage

# Only use poetry-core on Fedora and new EPEL releases because
# it is missing elsewhere. Fall back to using setuptools instead.
%if ! 0%{?rhel} || 0%{?epel} >= 10
%bcond_without poetry_core
%else
%bcond_with poetry_core
%endif

%global srcname rpmautospec_core
%global canonicalname rpmautospec-core

Name: python-%{canonicalname}
Version: 0.1.5
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

%global _description %{expand:
This package contains minimum functionality to determine if an RPM spec file
uses rpmautospec features.}

%description %_description

%package -n python3-%{canonicalname}
Summary: %{summary}
%if %{without pyproject_build}
%py_provides python3-%{canonicalname}
%endif

%description -n python3-%{canonicalname} %_description

%prep
%autosetup -n %{srcname}-%{version}
%if %{without poetry_core}
# by renaming the [build-system] section we fallback to setuptools (default per PEP 517)
# this only works because there is also a setup.py file in the sdist
test -f setup.py
sed -i 's/\[build-system\]/[ignore-this]/' pyproject.toml
%endif

%if %{without testcoverage}
cat << PYTESTINI > pytest.ini
[pytest]
addopts =
PYTESTINI
%endif

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files %{srcname}
%if %{with poetry_core}
# Work around poetry not listing license files as such in package metadata.
sed -i -e 's|^\(.*/LICENSE\)|%%license \1|g' %{pyproject_files}
%endif

%check
%pytest

%files -n python3-%{canonicalname} -f %{pyproject_files}
%doc README.md

%changelog
%autochangelog
