%{?mingw_package_header}

%global pkgname qtkeychain

Name:           mingw-%{pkgname}
Version:        0.14.3
Release:        3%{?dist}
Summary:        MinGW Windows %{pkgname} library
BuildArch:      noarch

License:        BSD-3-Clause
Url:            https://github.com/frankosterfeld/%{pkgname}
Source0:        https://github.com/frankosterfeld/%{pkgname}/archive/%{version}/%{pkgname}-%{version}.tar.gz

BuildRequires: make
BuildRequires:  cmake

BuildRequires:  mingw32-filesystem >= 95
BuildRequires:  mingw32-gcc-c++
BuildRequires:  mingw32-qt5-qtbase
BuildRequires:  mingw32-qt5-qttools
BuildRequires:  mingw32-qt5-qttools-tools

BuildRequires:  mingw64-filesystem >= 95
BuildRequires:  mingw64-gcc-c++
BuildRequires:  mingw64-qt5-qtbase
BuildRequires:  mingw64-qt5-qttools
BuildRequires:  mingw64-qt5-qttools-tools


%description
MinGW Windows %{pkgname} library.


%package -n mingw32-%{pkgname}-qt5
Summary:       MinGW Windows %{pkgname} library

%description -n mingw32-%{pkgname}-qt5
MinGW Windows %{pkgname} library.


%package -n mingw64-%{pkgname}-qt5
Summary:       MinGW Windows %{pkgname} library

%description -n mingw64-%{pkgname}-qt5
MinGW Windows %{pkgname} library.


%{?mingw_debug_package}


%prep
%autosetup -p1 -n %{pkgname}-%{version}


%build
%mingw_cmake \
    -DBUILD_WITH_QT4:BOOL=OFF
%mingw_make_build


%install
%mingw_make_install

%find_lang %{pkgname} --with-qt
grep %{mingw32_datadir}/qt5keychain/translations %{pkgname}.lang > mingw32_%{pkgname}-qt5.lang
grep %{mingw64_datadir}/qt5keychain/translations %{pkgname}.lang > mingw64_%{pkgname}-qt5.lang



%files -n mingw32-%{pkgname}-qt5 -f mingw32_%{pkgname}-qt5.lang
%license COPYING
%{mingw32_bindir}/libqt5keychain.dll
%{mingw32_includedir}/qt5keychain/
%{mingw32_libdir}/libqt5keychain.dll.a
%{mingw32_libdir}/cmake/Qt5Keychain
%{mingw32_datadir}/qt5/mkspecs/modules/qt_Qt5Keychain.pri

%files -n mingw64-%{pkgname}-qt5 -f mingw64_%{pkgname}-qt5.lang
%license COPYING
%{mingw64_bindir}/libqt5keychain.dll
%{mingw64_includedir}/qt5keychain/
%{mingw64_libdir}/libqt5keychain.dll.a
%{mingw64_libdir}/cmake/Qt5Keychain
%{mingw64_datadir}/qt5/mkspecs/modules/qt_Qt5Keychain.pri

%changelog
* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.14.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.14.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Tue Jun 04 2024 Sandro Mani <manisandro@gmail.com> - 0.14.3-1
- Update to 0.14.3

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.14.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.14.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Dec 24 2023 Sandro Mani <manisandro@gmail.com> - 0.14.0-1
- Update to 0.14.0

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.13.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.13.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Tue Aug 30 2022 Sandro Mani <manisandro@gmail.com> - 0.13.2-1
- Update to 0.13.2

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.11.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Fri Mar 25 2022 Sandro Mani <manisandro@gmail.com> - 0.11.1-5
- Rebuild with mingw-gcc-12

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.11.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.11.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.11.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Sep 15 2020 Sandro Mani <manisandro@gmail.com> - 0.11.1-1
- Update to 0.11.1

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.10.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Jun 19 2020 Sandro Mani <manisandro@gmail.com> - 0.10.0-1
- Update to 0.10.0

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Tue Oct 08 2019 Sandro Mani <manisandro@gmail.com> - 0.9.1-3
- Rebuild (Changes/Mingw32GccDwarf2)

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Tue May 14 2019 Sandro Mani <manisandro@gmail.com> - 0.9.1-1
- Update to 0.9.1

* Thu Apr 25 2019 Sandro Mani <manisandro@gmail.com> - 0.7.0-1
- Initial package
