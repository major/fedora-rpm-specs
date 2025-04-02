%global pypi_name pytest-cid
%global common_description %{expand:
This module is a plugin for the popular Python testing framework pytest. It
compares data structures containing matching CIDs of different versions and
encoding.}

Name:          python-%{pypi_name}
Version:       1.1.2
Release:       %autorelease
BuildArch:     noarch
Summary:       Pytest plugin to compare CIDs
License:       MPL-2.0
URL:           https://github.com/ntninja/pytest-cid
Source0:       %{pypi_source pytest_cid}
# https://github.com/ntninja/pytest-cid/pull/3
Patch1:        python-pytest-cid-0001-Relax-dependencies.patch
BuildRequires: python3-pytest
BuildRequires: python3-pytest-cov
BuildSystem:   pyproject
BuildOption(prep): -n pytest_cid-%{version}
BuildOption(generate_buildrequires): -t
BuildOption(install): pytest_cid

%description %{common_description}

%package -n python3-%{pypi_name}
Summary: %{summary}

%description -n python3-%{pypi_name} %{common_description}

%check -a
%pytest

%files -n python3-%{pypi_name} -f %{pyproject_files}
%doc README.md
%license LICENSE

%changelog
%autochangelog
