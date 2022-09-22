%global pkg_name pyqt6-sip
%global pypi_name PyQt6_sip
%global _sip_api_major 13
%global _sip_api_minor 4
%global _sip_api %{_sip_api_major}.%{_sip_api_minor}

Name:           python-%{pkg_name}
Version:        13.4.0
Release:        1%{?dist}
Summary:        The sip module support for PyQt6

License:        GPLv2 or GPLv3
URL:            https://www.riverbankcomputing.com/software/sip/
Source0:        %{pypi_source}

BuildRequires:  gcc
BuildRequires:  python3-devel
BuildRequires:  %{py3_dist setuptools} >= 30.3
BuildRequires:  %{py3_dist wheel}

%global _description %{expand:
The sip extension module provides support for the PyQt6 package.
}

%description %_description

%package -n     python3-%{pkg_name}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{pkg_name}}
Provides: python3-pyqt6-sip-api(%{_sip_api_major}) = %{_sip_api}
Provides: python3-pyqt6-sip-api(%{_sip_api_major})%{?_isa} = %{_sip_api}

%description -n python3-%{pkg_name} %_description
%prep
%autosetup -n %{pypi_name}-%{version}


%build
%py3_build


%install
%py3_install


%files -n python3-%{pkg_name}
%doc README
%license LICENSE LICENSE-GPL3
%{python3_sitearch}/PyQt6_sip*
%{python3_sitearch}/PyQt6/


%changelog
* Mon Sep 05 2022 Onuralp Sezer <thunderbirdtr@fedoraproject.org> - 13.4.0-1
- 13.4.0

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 13.3.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon Jun 13 2022 Python Maint <python-maint@redhat.com> - 13.3.0-2
- Rebuilt for Python 3.11

* Wed Apr 13 2022 Onuralp Sezer <thunderbirdtr@fedoraproject.org> - 13.3.0-1
- Initial Package
