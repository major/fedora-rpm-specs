%global shortname adwaita-qt

%{?mingw_package_header}

Name:           mingw-adwaita-qt
Version:        1.4.2
Release:        8%{?dist}
Summary:        Adwaita theme for Qt-based applications

License:        LGPL-2.0-or-later AND GPL-2.0-or-later
Url:            https://github.com/FedoraQt/adwaita-qt
Source0:        https://github.com/FedoraQt/adwaita-qt/archive/%{version}/adwaita-qt-%{version}.tar.gz

BuildArch:      noarch
BuildRequires:  cmake
BuildRequires:  make

BuildRequires:  mingw32-filesystem >= 95
BuildRequires:  mingw32-gcc
BuildRequires:  mingw32-gcc-c++
BuildRequires:  mingw32-qt5-qtbase
BuildRequires:  mingw32-qt6-qtbase

BuildRequires:  mingw64-filesystem >= 95
BuildRequires:  mingw64-gcc
BuildRequires:  mingw64-gcc-c++
BuildRequires:  mingw64-qt5-qtbase
BuildRequires:  mingw64-qt6-qtbase

%description
Theme to let Qt applications fit nicely into Fedora Workstation

# Win32
%package -n mingw32-adwaita-qt5
Summary:        Adwaita Qt5 theme
Requires:       mingw32-libadwaita-qt5 = %{version}-%{release}

%description -n mingw32-adwaita-qt5
Adwaita theme variant for applications utilizing Qt5.

%package -n mingw32-libadwaita-qt5
Summary:        Adwaita Qt5 library

%description -n mingw32-libadwaita-qt5
%{summary}.

%package -n mingw32-libadwaita-qt5-static
Summary:        Development files for mingw32-libadwaita-qt5
Requires:       mingw32-libadwaita-qt5 = %{version}-%{release}

%description -n mingw32-libadwaita-qt5-static
Static version of the mingw32-libadwaita-qt5 library.

# Win64
%package -n mingw64-adwaita-qt5
Summary:        Adwaita Qt5 theme
Requires:       mingw64-libadwaita-qt5 = %{version}-%{release}
BuildArch:      noarch

%description -n mingw64-adwaita-qt5
Adwaita theme variant for applications utilizing Qt5.

%package -n mingw64-libadwaita-qt5
Summary:        Adwaita Qt5 library

%description -n mingw64-libadwaita-qt5
%{summary}.

%package -n mingw64-libadwaita-qt5-static
Summary:        Development files for mingw64-libadwaita-qt5
Requires:       mingw64-libadwaita-qt5 = %{version}-%{release}

%description -n mingw64-libadwaita-qt5-static
Static version of the mingw64-libadwaita-qt5 library.

# Win32
%package -n mingw32-adwaita-qt6
Summary:        Adwaita Qt6 theme
Requires:       mingw32-libadwaita-qt6 = %{version}-%{release}

%description -n mingw32-adwaita-qt6
Adwaita theme variant for applications utilizing Qt6.

%package -n mingw32-libadwaita-qt6
Summary:        Adwaita Qt6 library

%description -n mingw32-libadwaita-qt6
%{summary}.

%package -n mingw32-libadwaita-qt6-static
Summary:        Development files for mingw32-libadwaita-qt6
Requires:       mingw32-libadwaita-qt6 = %{version}-%{release}

%description -n mingw32-libadwaita-qt6-static
Static version of the mingw32-libadwaita-qt6 library.

# Win64
%package -n mingw64-adwaita-qt6
Summary:        Adwaita Qt6 theme
Requires:       mingw64-libadwaita-qt6 = %{version}-%{release}
BuildArch:      noarch

%description -n mingw64-adwaita-qt6
Adwaita theme variant for applications utilizing Qt6.

%package -n mingw64-libadwaita-qt6
Summary:        Adwaita Qt6 library

%description -n mingw64-libadwaita-qt6
%{summary}.

%package -n mingw64-libadwaita-qt6-static
Summary:        Development files for mingw64-libadwaita-qt6
Requires:       mingw64-libadwaita-qt6 = %{version}-%{release}

%description -n mingw64-libadwaita-qt6-static
Static version of the mingw64-libadwaita-qt6 library.

%{?mingw_debug_package}

%prep
%autosetup -p1 -n adwaita-qt-%{version}

%build
mkdir %{_target_platform}-qt5
pushd %{_target_platform}-qt5

%mingw_cmake ../..

%mingw_make_build

popd

mkdir %{_target_platform}-qt6
pushd %{_target_platform}-qt6

%mingw_cmake -DUSE_QT6=ON ../..

%mingw_make_build

popd

%install
pushd %{_target_platform}-qt5
%mingw_make_install
popd

pushd %{_target_platform}-qt6
%mingw_make_install
popd

# Win32
%files -n mingw32-adwaita-qt5
%{mingw32_libdir}/qt5/plugins/styles/libadwaita-qt.dll

%files -n mingw32-libadwaita-qt5
%{mingw32_bindir}/libadwaitaqt-1.dll
%{mingw32_bindir}/libadwaitaqtpriv-1.dll
%{mingw32_includedir}/AdwaitaQt/
%{mingw32_libdir}/cmake/AdwaitaQt/
%{mingw32_libdir}/pkgconfig/adwaita-qt.pc

%files -n mingw32-libadwaita-qt5-static
%{mingw32_libdir}/libadwaitaqt.dll.a
%{mingw32_libdir}/libadwaitaqtpriv.dll.a

# Win64
%files -n mingw64-adwaita-qt5
%{mingw64_libdir}/qt5/plugins/styles/libadwaita-qt.dll

%files -n mingw64-libadwaita-qt5
%{mingw64_bindir}/libadwaitaqt-1.dll
%{mingw64_bindir}/libadwaitaqtpriv-1.dll
%{mingw64_includedir}/AdwaitaQt/
%{mingw64_libdir}/cmake/AdwaitaQt/
%{mingw64_libdir}/pkgconfig/adwaita-qt.pc

%files -n mingw64-libadwaita-qt5-static
%{mingw64_libdir}/libadwaitaqt.dll.a
%{mingw64_libdir}/libadwaitaqtpriv.dll.a

%files -n mingw32-adwaita-qt6
%{mingw32_libdir}/qt6/plugins/styles/libadwaita-qt.dll

%files -n mingw32-libadwaita-qt6
%{mingw32_bindir}/libadwaitaqt6-1.dll
%{mingw32_bindir}/libadwaitaqt6priv-1.dll
%{mingw32_includedir}/AdwaitaQt6/
%{mingw32_libdir}/cmake/AdwaitaQt6/
%{mingw32_libdir}/pkgconfig/adwaita-qt6.pc

%files -n mingw32-libadwaita-qt6-static
%{mingw32_libdir}/libadwaitaqt6.dll.a
%{mingw32_libdir}/libadwaitaqt6priv.dll.a

# Win64
%files -n mingw64-adwaita-qt6
%{mingw64_libdir}/qt6/plugins/styles/libadwaita-qt.dll

%files -n mingw64-libadwaita-qt6
%{mingw64_bindir}/libadwaitaqt6-1.dll
%{mingw64_bindir}/libadwaitaqt6priv-1.dll
%{mingw64_includedir}/AdwaitaQt6/
%{mingw64_libdir}/cmake/AdwaitaQt6/
%{mingw64_libdir}/pkgconfig/adwaita-qt6.pc

%files -n mingw64-libadwaita-qt6-static
%{mingw64_libdir}/libadwaitaqt6.dll.a
%{mingw64_libdir}/libadwaitaqt6priv.dll.a

%changelog
* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.2-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.2-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Tue Jan 31 2023 Jan Grulich <jgrulich@redhat.com> - 1.4.2-3
- migrated to SPDX license

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Wed Sep 21 2022 Jan Grulich <jgrulich@redhat.com> - 1.4.2-1
- 1.4.2

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Fri Mar 25 2022 Sandro Mani <manisandro@gmail.com> - 1.4.1-2
- Rebuild with mingw-gcc-12

* Fri Feb 04 2022 Jan Grulich <jgrulich@redhat.com> - 1.4.1-1
- 1.4.1

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Mon Aug 30 2021 Jan Grulich <jgrulich@redhat.com> - 1.4.0-1
- 1.4.0

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Mon Mar 22 2021 Jan Grulich <jgrulich@redhat.com> - 1.2.1-1
- 1.2.1

* Tue Mar 09 2021 Jan Grulich <jgrulich@redhat.com> - 1.2.0-3
- Fix adwaita-qt library to be properly linked using CMake

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Fri Dec 18 2020 Jan Grulich <jgrulich@redhat.com> - 1.2.0-1
- 1.2.0

* Mon Nov 09 2020 Jan Grulich <jgrulich@redhat.com> - 1.1.91-1
- Initial release
