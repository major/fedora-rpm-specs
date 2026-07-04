Name:           python-installer
Version:        1.0.1
Release:        %autorelease
Summary:        A library for installing Python wheels

# SPDX
License:        MIT
URL:            https://github.com/pypa/installer
Source:         %{pypi_source installer}

# Replace deprecated posixpath.commonprefix() usage with path.startswith()
# Fixes tests with Python 3.15
Patch:          https://github.com/pypa/installer/pull/340.patch

BuildArch:      noarch
BuildRequires:  python3-devel

# For tests
BuildRequires:  python3-pytest

%global _description %{expand:
This is a low-level library for installing a Python package from
a wheel distribution. It provides basic functionality and abstractions
for handling wheels and installing packages from wheels.}


%description %_description

%package -n     python3-installer
Summary:        %{summary}

%description -n python3-installer %_description


%prep
%autosetup -p1 -n installer-%{version}

%generate_buildrequires
%pyproject_buildrequires


%build
%pyproject_wheel


%install
%pyproject_install
%pyproject_save_files installer


%check
%pyproject_check_import
%pytest


%files -n python3-installer -f %{pyproject_files}
%license LICENSE
%doc README.md


%changelog
%autochangelog
