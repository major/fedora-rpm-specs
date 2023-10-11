Name:           python-installer
Version:        0.7.0
Release:        3%{?dist}
Summary:        A library for installing Python wheels

# SPDX
License:        MIT
URL:            https://github.com/pypa/installer
Source:         %{pypi_source installer}

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
%doc CONTRIBUTING.md README.md


%changelog
* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Tue Jun 13 2023 Python Maint <python-maint@redhat.com> - 0.7.0-2
- Rebuilt for Python 3.12

* Wed Mar 22 2023 Tomáš Hrnčiar <thrnciar@redhat.com> - 0.7.0-1
- Update to 0.7.0

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Jul 28 2022 Charalampos Stratakis <cstratak@redhat.com> - 0.5.1-1
- Initial package (rhbz#2111707)