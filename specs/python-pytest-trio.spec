%global pypi_name pytest-trio

Name:           python-%{pypi_name}
Version:        0.8.0
Release:        %autorelease
Summary:        Pytest plugin for trio

# Automatically converted from old format: MIT or ASL 2.0 - review is highly recommended.
License:        LicenseRef-Callaway-MIT OR Apache-2.0
URL:            https://github.com/python-trio/pytest-trio
Source0:        https://github.com/python-trio/pytest-trio/archive/v%{version}/%{pypi_name}-%{version}.tar.gz

# Remove trio.tests import causing warnings
# https://github.com/python-trio/pytest-trio/pull/135
# We only backport the fix, not the additional formatting changes.
Patch:          https://github.com/python-trio/pytest-trio/pull/135/commits/9cda20bbb966fe1e4ae51921d566c668654ee5e1.patch
# Backport of https://github.com/python-trio/pytest-trio/pull/145
Patch:          migrate-to-pyproject.patch

BuildArch:      noarch

%description
This is a pytest plugin to help you test projects that use Trio, a friendly
library for concurrency and async I/O in Python.

%package -n     python3-%{pypi_name}
Summary:        %{summary}

BuildRequires:  python3-devel
BuildRequires:  python3-hypothesis

%description -n python3-%{pypi_name}
This is a pytest plugin to help you test projects that use Trio, a friendly
library for concurrency and async I/O in Python.

%prep
%autosetup -n %{pypi_name}-%{version} -p1
sed -i s/--cov// pytest.ini

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files -l pytest_trio

%check
%pytest -v

%files -n python3-%{pypi_name} -f %{pyproject_files}
%doc README.rst

%changelog
%autochangelog
