%global srcname environs

%global _description %{expand: \
Environs is a Python library for parsing environment variables.
It allows you to store configuration separate from your code, as per
The Twelve-Factor App (https://12factor.net/config) methodology.}

Name:       python-%{srcname}
Version:    9.5.0
Release:    6%{?dist}
Summary:    Python library for parsing environment variables
License:    MIT
URL:        https://github.com/sloria/%{srcname}
Source0:    %{url}/archive/%{version}/%{srcname}-%{version}.tar.gz

BuildArch:  noarch

BuildRequires:  python3-devel
BuildRequires:  pyproject-rpm-macros

%description %{_description}

%generate_buildrequires
%pyproject_buildrequires -x tests

%package -n python3-%{srcname}
Summary:    Python library for parsing environment variables

%description -n python3-%{srcname}
%{_description}

%pyproject_extras_subpkg -n python3-%{srcname} django

%package -n python3-%{srcname}-examples
Summary:    Example files for Environs
BuildArch:  noarch
%description -n python3-%{srcname}-examples
%{_description}

%prep
%autosetup -n %{srcname}-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files %{srcname}

%check
%pytest

%files -n python3-%{srcname} -f %{pyproject_files}
%license LICENSE
%doc README.md CHANGELOG.md CONTRIBUTING.md

%files -n python3-%{srcname}-examples
%license LICENSE
%doc README.md CHANGELOG.md CONTRIBUTING.md examples


%changelog
* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 9.5.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Fri Jun 30 2023 Python Maint <python-maint@redhat.com> - 9.5.0-5
- Rebuilt for Python 3.12

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 9.5.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 9.5.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Tue Jun 14 2022 Python Maint <python-maint@redhat.com> - 9.5.0-2
- Rebuilt for Python 3.11

* Sat Feb 05 2022 Antonio Trande <sagitter@fedoraproject.org> - 9.5.0-1
- Release 9.5.0

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 9.4.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Sat Jan 08 2022 Antonio Trande <sagitter@fedoraproject.org> - 9.4.0-1
- Release 9.4.0

* Tue Nov 23 2021 Antonio Trande <sagitter@fedoraproject.org> - 9.3.5-1
- Release 9.3.5

* Wed Oct 06 2021 Antonio Trande <sagitter@fedoraproject.org> - 9.3.4-1
- Release 9.3.4

* Sat Aug 14 2021 Antonio Trande <sagitter@fedoraproject.org> - 9.3.3-1
- Release 9.3.3

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 9.3.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Jun 23 2021 Antonio Trande <sagitter@fedoraproject.org> - 9.3.2-3
- Include the sub-package for example files

* Tue Jun 22 2021 Benjamin A. Beasley <code@musicinmybrain.net> - 9.3.2-2
- Switch to pyproject-rpm-macros and add metapackage for django extra

* Sun Jun 20 2021 Antonio Trande <sagitter@fedoraproject.org> - 9.3.2-1
- Release 9.3.2
