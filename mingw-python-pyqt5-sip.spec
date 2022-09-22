%{?mingw_package_header}

%global pypi_name PyQt5_sip

Name:           mingw-python-pyqt5-sip
Summary:        MinGW Python pyqt5-sip
Version:        12.11.0
Release:        1%{?dist}
BuildArch:      noarch

License:        GPLv2 or GPLv3
Url:            https://www.riverbankcomputing.com/software/sip/
Source0:        %{pypi_source}


BuildRequires:  mingw32-filesystem >= 102
BuildRequires:  mingw32-gcc
BuildRequires:  mingw32-python3
BuildRequires:  mingw32-python3-setuptools

BuildRequires:  mingw64-filesystem >= 102
BuildRequires:  mingw64-gcc
BuildRequires:  mingw64-python3
BuildRequires:  mingw64-python3-setuptools


%description
MinGW Python %{pypi_name}.


%package -n mingw32-python3-%{pypi_name}
Summary:       MinGW Python 3 %{pypi_name}

%description -n mingw32-python3-%{pypi_name}
MinGW Python 3 %{pypi_name}.


%package -n mingw64-python3-%{pypi_name}
Summary:       MinGW Python 3 %{pypi_name}

%description -n mingw64-python3-%{pypi_name}
MinGW Python 3 %{pypi_name}.


%{?mingw_debug_package}


%prep
%autosetup -p1 -n %{pypi_name}-%{version}


%build
%{mingw32_py3_build}
%{mingw64_py3_build}


%install
%{mingw32_py3_install}
%{mingw64_py3_install}


%files -n mingw32-python3-%{pypi_name}
%dir %{mingw32_python3_sitearch}/PyQt5/
%{mingw32_python3_sitearch}/PyQt5/sip*
%{mingw32_python3_sitearch}/%{pypi_name}-%{version}*-py%{mingw32_python3_version}.egg-info/

%files -n mingw64-python3-%{pypi_name}
%dir %{mingw64_python3_sitearch}/PyQt5/
%{mingw64_python3_sitearch}/PyQt5/sip*
%{mingw64_python3_sitearch}/%{pypi_name}-%{version}*-py%{mingw32_python3_version}.egg-info/


%changelog
* Fri Jul 22 2022 Sandro Mani <manisandro@gmail.com> - 12.11.0-1
- Update to 12.11.0

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 12.9.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Fri Feb 18 2022 Sandro Mani <manisandro@gmail.com> - 12.9.1-1
- Update to 12.9.1

* Thu Feb 10 2022 Sandro Mani <manisandro@gmail.com> - 12.9.0-4
- Rebuild for new python dependency generator (take two)

* Thu Feb 10 2022 Sandro Mani <manisandro@gmail.com> - 12.9.0-3
- Rebuild for new python dependency generator

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 12.9.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Tue Sep 28 2021 Sandro Mani <manisandro@gmail.com> - 12.9.0-1
- Initial package
