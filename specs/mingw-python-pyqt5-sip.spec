%{?mingw_package_header}

%global mod_name pyqt5-sip
%global pypi_name pyqt5_sip

Name:           mingw-python-%{mod_name}
Summary:        MinGW Python %{pypi_name} library
Version:        12.16.1
Release:        1%{?dist}
BuildArch:      noarch

License:        GPL-2.0-only OR GPL-3.0-only
Url:            https://www.riverbankcomputing.com/software/sip/
Source0:        %{pypi_source}


BuildRequires:  mingw32-filesystem >= 102
BuildRequires:  mingw32-dlfcn
BuildRequires:  mingw32-gcc
BuildRequires:  mingw32-python3
BuildRequires:  mingw32-python3-build

BuildRequires:  mingw64-filesystem >= 102
BuildRequires:  mingw64-dlfcn
BuildRequires:  mingw64-gcc
BuildRequires:  mingw64-python3
BuildRequires:  mingw64-python3-build


%description
MinGW Python %{pypi_name} library.


%package -n mingw32-python3-%{mod_name}
Summary:       MinGW Python 3 %{mod_name} library
Obsoletes:     mingw32-python3-%{pypi_name} < 12.11.0-2
Provides:      mingw32-python3-%{pypi_name} = %{version}-%{release}

%description -n mingw32-python3-%{mod_name}
MinGW Python 3 %{pypi_name} library.


%package -n mingw64-python3-%{mod_name}
Summary:       MinGW Python 3 %{pypi_name} library
Obsoletes:     mingw64-python3-%{pypi_name} < 12.11.0-2
Provides:      mingw64-python3-%{pypi_name} = %{version}-%{release}

%description -n mingw64-python3-%{mod_name}
MinGW Python 3 %{pypi_name} library.


%{?mingw_debug_package}


%prep
%autosetup -p1 -n %{pypi_name}-%{version}


%build
%mingw32_py3_build_wheel
%mingw64_py3_build_wheel


%install
%mingw32_py3_install_wheel
%mingw64_py3_install_wheel


%files -n mingw32-python3-%{mod_name}
%dir %{mingw32_python3_sitearch}/PyQt5/
%{mingw32_python3_sitearch}/PyQt5/sip*
%{mingw32_python3_sitearch}/PyQt5_sip-%{version}.dist-info/

%files -n mingw64-python3-%{mod_name}
%dir %{mingw64_python3_sitearch}/PyQt5/
%{mingw64_python3_sitearch}/PyQt5/sip*
%{mingw64_python3_sitearch}/PyQt5_sip-%{version}.dist-info/


%changelog
* Wed Dec 25 2024 Sandro Mani <manisandro@gmail.com> - 12.16.1-1
- Update to 12.16.1

* Sun Dec 08 2024 Sandro Mani <manisandro@gmail.com> - 12.16.0-1
- Update to 12.16.0

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 12.15.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Tue Jul 16 2024 Sandro Mani <manisandro@gmail.com> - 12.15.0-1
- Update to 12.15.0

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 12.13.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 12.13.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Oct 19 2023 Sandro Mani <manisandro@gmail.com> - 12.13.0-2
- Bump

* Thu Oct 19 2023 Sandro Mani <manisandro@gmail.com> - 12.13.0-1
- Update to 12.13.0

* Sat Aug 12 2023 Sandro Mani <manisandro@gmail.com> - 12.12.2-2
- Rebuild (sip)

* Sat Jul 29 2023 Sandro Mani <manisandro@gmail.com> - 12.12.2-1
- Update to 12.12.2

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 12.12.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Wed Apr 26 2023 Sandro Mani <manisandro@gmail.com> - 12.12.1-1
- Update to 12.12.1

* Thu Feb 02 2023 Sandro Mani <manisandro@gmail.com> - 12.11.1-1
- Update to 12.11.1

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 12.11.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Wed Oct 19 2022 Sandro Mani <manisandro@gmail.com> - 12.11.0-2
- Switch to python3-build

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
