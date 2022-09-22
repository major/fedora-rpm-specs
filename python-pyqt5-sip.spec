%global pkg_name pyqt5-sip
%global pypi_name PyQt5_sip
%global _sip_api_major 12
%global _sip_api_minor 11
%global _sip_api %{_sip_api_major}.%{_sip_api_minor}

Name:           python-%{pkg_name}
Version:        12.11.0
Release:        2%{?dist}
Summary:        The sip module support for PyQt5

License:        GPLv2 or GPLv3
URL:            https://www.riverbankcomputing.com/software/sip/
Source0:        %{pypi_source}

BuildRequires:  gcc
BuildRequires:  python3-devel
BuildRequires:  %{py3_dist setuptools} >= 30.3
BuildRequires:  %{py3_dist wheel}

%global _description %{expand:
The sip extension module provides support for the PyQt5 package.
}

%description %_description

%package -n     python3-%{pkg_name}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{pkg_name}}
Provides: python3-pyqt5-sip-api(%{_sip_api_major}) = %{_sip_api}
Provides: python3-pyqt5-sip-api(%{_sip_api_major})%{?_isa} = %{_sip_api}

%description -n python3-%{pkg_name} %_description

%prep
%autosetup -n %{pypi_name}-%{version}

%build
%py3_build

%install
%py3_install

%files -n python3-%{pkg_name}
%doc README
%{python3_sitearch}/PyQt5_sip*
%{python3_sitearch}/PyQt5/

%changelog
* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 12.11.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed Jul 20 2022 Scott Talbert <swt@techie.net> - 12.11.0-1
- Update to new upstream release 12.11.0 (#2074708)

* Mon Jun 13 2022 Python Maint <python-maint@redhat.com> - 12.9.1-3
- Rebuilt for Python 3.11

* Sat Mar 12 2022 Scott Talbert <swt@techie.net> - 12.9.1-2
- Fix FTBFS with Python 3.11.0a6 (#2062145)

* Fri Feb 18 2022 Scott Talbert <swt@techie.net> - 12.9.1-1
- Update to new upstream release 12.9.1 (#2049165)

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 12.9.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 12.9.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Sat Jul 10 2021 Scott Talbert <swt@techie.net> - 12.9.0-1
- Update to latest upstream release for sip 6

* Tue Jul 06 2021 Scott Talbert <swt@techie.net> - 12.8.1-2
- Correct sip-api provides (#1979409)

* Mon May 24 2021 Scott Talbert <swt@techie.net> - 12.8.1-1
- Initial package
