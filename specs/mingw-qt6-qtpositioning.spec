%{?mingw_package_header}

%global qt_module qtpositioning
#global pre rc2

#global commit a73dfa7c63b82e25f93e44ed6386664373aaca74
#global shortcommit %(c=%{commit}; echo ${c:0:7})

%if 0%{?commit:1}
%global source_folder %{qt_module}-%{commit}
%else
%global source_folder %{qt_module}-everywhere-src-%{version}%{?pre:-%{pre}}
%endif

# first two digits of version
%global release_version %(echo %{version} | awk -F. '{print $1"."$2}')

Name:           mingw-qt6-%{qt_module}
Version:        6.8.1
Release:        2%{?dist}
Summary:        Qt6 for Windows - Qt Positioning component

# Base license is LGPLv3 or GPLv2
# 3rdparty/clip2tri is MIT, see ./src/3rdparty/clip2tri/LICENSE
# 3rdparty/poly2tri is BSD, see ./src/3rdparty/poly2tri/LICENSE
# 3rdparty/clipper ist Boost, see ./src/3rdparty/clipper/LICENSE
License:        LGPL-3.0-only OR GPL-3.0-only WITH Qt-GPL-exception-1.0
URL:            http://qt.io/

%if 0%{?commit:1}
Source0:        https://github.com/qt/%{qt_module}/archive/%{commit}/%{qt_module}-everywhere-src-%{commit}.tar.gz
%else
Source0:        http://download.qt.io/%{?pre:development}%{?!pre:official}_releases/qt/%{release_version}/%{version}%{?pre:-%pre}/submodules/%{qt_module}-everywhere-src-%{version}%{?pre:-%pre}.tar.xz
%endif

BuildArch:      noarch

BuildRequires:  cmake
BuildRequires:  ninja-build

BuildRequires:  mingw32-filesystem >= 96
BuildRequires:  mingw32-gcc-c++
BuildRequires:  mingw32-qt6-qtbase = %{version}
BuildRequires:  mingw32-qt6-qtdeclarative = %{version}
BuildRequires:  mingw32-qt6-qtserialport = %{version}

BuildRequires:  mingw64-filesystem >= 96
BuildRequires:  mingw64-gcc-c++
BuildRequires:  mingw64-qt6-qtbase = %{version}
BuildRequires:  mingw64-qt6-qtdeclarative = %{version}
BuildRequires:  mingw64-qt6-qtserialport = %{version}

Provides:       bundled(clip2tri)
Provides:       bundled(poly2tri)
Provides:       bundled(clipper)


%description
This package contains the Qt software toolkit for developing
cross-platform applications.

This is the Windows version of Qt, for use in conjunction with the
Fedora Windows cross-compiler.


# Win32
%package -n mingw32-qt6-%{qt_module}
Summary:        Qt6 for Windows - Qt Positioning component

%description -n mingw32-qt6-%{qt_module}
This package contains the Qt software toolkit for developing
cross-platform applications.

This is the 32-bit Windows version of Qt, for use in conjunction with the
Fedora Windows cross-compiler.


# Win64
%package -n mingw64-qt6-%{qt_module}
Summary:        Qt6 for Windows - Qt Positioning component

%description -n mingw64-qt6-%{qt_module}
This package contains the Qt software toolkit for developing
cross-platform applications.

This is the 64-bit Windows version of Qt, for use in conjunction with the
Fedora Windows cross-compiler.


%{?mingw_debug_package}


%prep
%autosetup -p1 -n %{source_folder}

# Postfix licenses of bundled libraries with name of library
cp -a src/3rdparty/clip2tri/LICENSE LICENSE.clip2tri
cp -a src/3rdparty/poly2tri/LICENSE LICENSE.poly2tri
cp -a src/3rdparty/clipper/LICENSE LICENSE.clipper


%build
export MINGW32_CXXFLAGS="%{mingw32_cflags} -msse2"
export MINGW64_CXXFLAGS="%{mingw64_cflags} -msse2"
%mingw_cmake -G Ninja -DCMAKE_BUILD_TYPE=RelWithDebInfo
%mingw_ninja


%install
%mingw_ninja_install


# Win32
%files -n mingw32-qt6-%{qt_module}
%license LICENSES/*GPL*
%{mingw32_bindir}/Qt6Positioning.dll
%{mingw32_bindir}/Qt6PositioningQuick.dll
%{mingw32_includedir}/qt6/QtPositioning/
%{mingw32_includedir}/qt6/QtPositioningQuick/
%{mingw32_libdir}/Qt6Positioning.prl
%{mingw32_libdir}/Qt6PositioningQuick.prl
%{mingw32_libdir}/cmake/Qt6/FindGconf.cmake
%{mingw32_libdir}/cmake/Qt6/FindGypsy.cmake
%{mingw32_libdir}/cmake/Qt6BuildInternals/StandaloneTests/QtPositioningTestsConfig.cmake
%{mingw32_libdir}/cmake/Qt6Bundled_Clip2Tri/
%{mingw32_libdir}/cmake/Qt6Positioning/
%{mingw32_libdir}/cmake/Qt6PositioningQuick/
%{mingw32_libdir}/cmake/Qt6Qml/QmlPlugins/
%{mingw32_libdir}/pkgconfig/Qt6Positioning.pc
%{mingw32_libdir}/pkgconfig/Qt6PositioningQuick.pc
%{mingw32_libdir}/libQt6Positioning.dll.a
%{mingw32_libdir}/libQt6PositioningQuick.dll.a
%{mingw32_libdir}/qt6/metatypes/qt6positioning_relwithdebinfo_metatypes.json
%{mingw32_libdir}/qt6/metatypes/qt6positioningquick_relwithdebinfo_metatypes.json
%{mingw32_libdir}/qt6/mkspecs/modules/qt_lib_positioning.pri
%{mingw32_libdir}/qt6/mkspecs/modules/qt_lib_positioning_private.pri
%{mingw32_libdir}/qt6/mkspecs/modules/qt_lib_positioningquick.pri
%{mingw32_libdir}/qt6/mkspecs/modules/qt_lib_positioningquick_private.pri
%{mingw32_libdir}/qt6/plugins/position/
%{mingw32_libdir}/qt6/modules/Positioning.json
%{mingw32_libdir}/qt6/modules/PositioningQuick.json
%{mingw32_libdir}/qt6/qml/QtPositioning/
%{mingw32_libdir}/qt6/sbom/%{qt_module}-%{version}.spdx

# Win64
%files -n mingw64-qt6-%{qt_module}
%license LICENSES/*GPL*
%{mingw64_bindir}/Qt6Positioning.dll
%{mingw64_bindir}/Qt6PositioningQuick.dll
%{mingw64_includedir}/qt6/QtPositioning/
%{mingw64_includedir}/qt6/QtPositioningQuick/
%{mingw64_libdir}/Qt6Positioning.prl
%{mingw64_libdir}/Qt6PositioningQuick.prl
%{mingw64_libdir}/cmake/Qt6/FindGconf.cmake
%{mingw64_libdir}/cmake/Qt6/FindGypsy.cmake
%{mingw64_libdir}/cmake/Qt6BuildInternals/StandaloneTests/QtPositioningTestsConfig.cmake
%{mingw64_libdir}/cmake/Qt6Bundled_Clip2Tri/
%{mingw64_libdir}/cmake/Qt6Positioning/
%{mingw64_libdir}/cmake/Qt6PositioningQuick/
%{mingw64_libdir}/cmake/Qt6Qml/QmlPlugins/
%{mingw64_libdir}/pkgconfig/Qt6Positioning.pc
%{mingw64_libdir}/pkgconfig/Qt6PositioningQuick.pc
%{mingw64_libdir}/libQt6Positioning.dll.a
%{mingw64_libdir}/libQt6PositioningQuick.dll.a
%{mingw64_libdir}/qt6/metatypes/qt6positioning_relwithdebinfo_metatypes.json
%{mingw64_libdir}/qt6/metatypes/qt6positioningquick_relwithdebinfo_metatypes.json
%{mingw64_libdir}/qt6/mkspecs/modules/qt_lib_positioning.pri
%{mingw64_libdir}/qt6/mkspecs/modules/qt_lib_positioning_private.pri
%{mingw64_libdir}/qt6/mkspecs/modules/qt_lib_positioningquick.pri
%{mingw64_libdir}/qt6/mkspecs/modules/qt_lib_positioningquick_private.pri
%{mingw64_libdir}/qt6/plugins/position/
%{mingw64_libdir}/qt6/modules/Positioning.json
%{mingw64_libdir}/qt6/modules/PositioningQuick.json
%{mingw64_libdir}/qt6/qml/QtPositioning/
%{mingw64_libdir}/qt6/sbom/%{qt_module}-%{version}.spdx


%changelog
* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 6.8.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Sat Dec 07 2024 Sandro Mani <manisandro@gmail.com> - 6.8.1-1
- Update to 6.8.1

* Tue Oct 22 2024 Sandro Mani <manisandro@gmail.com> - 6.8.0-1
- Update to 6.8.0

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 6.7.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Wed Jul 03 2024 Sandro Mani <manisandro@gmail.com> - 6.7.2-1
- Update to 6.7.2

* Sun May 26 2024 Sandro Mani <manisandro@gmail.com> - 6.7.1-1
- Update to 6.7.1

* Tue Apr 09 2024 Sandro Mani <manisandro@gmail.com> - 6.7.0-1
- Update to 6.7.0

* Sun Feb 18 2024 Sandro Mani <manisandro@gmail.com> - 6.6.2-1
- Update to 6.6.2

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 6.6.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 6.6.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Dec 03 2023 Sandro Mani <manisandro@gmail.com> - 6.6.1-1
- Update to 6.6.1

* Wed Oct 18 2023 Sandro Mani <manisandro@gmail.com> - 6.6.0-1
- Update to 6.6.0

* Wed Oct 04 2023 Sandro Mani <manisandro@gmail.com> - 6.5.3-1
- Update to 6.5.3

* Sun Jul 30 2023 Sandro Mani <manisandro@gmail.com> - 6.5.2-1
- Update to 6.5.2

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 6.5.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Tue May 30 2023 Sandro Mani <manisandro@gmail.com> - 6.5.1-1
- Update to 6.5.1

* Fri Apr 7 2023 Marie Loise Nolden <loise@kde.org> - 6.5.0-2
- fix missing quick/serialport modules

* Fri Apr 07 2023 Sandro Mani <manisandro@gmail.com> - 6.5.0-1
- Update to 6.5.0

* Wed Mar 29 2023 Sandro Mani <manisandro@gmail.com> - 6.4.3-1
- Update to 6.4.3

* Tue Mar 28 2023 Sandro Mani <manisandro@gmail.com> - 6.4.2-1
- Update to 6.4.2

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 6.4.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Wed Jan 18 2023 Sandro Mani <manisandro@gmail.com> - 6.4.2-1
- Update to 6.4.2

* Sat Nov 26 2022 Sandro Mani <manisandro@gmail.com> - 6.4.1-1
- Update to 6.4.1

* Fri Nov 04 2022 Sandro Mani <manisandro@gmail.com> - 6.4.0-1
- Update to 6.4.0

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 6.3.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Tue Jul 19 2022 Sandro Mani <manisandro@gmail.com> - 6.3.1-1
- Update to 6.3.1

* Fri Apr 29 2022 Sandro Mani <manisandro@gmail.com> - 6.3.0-1
- Update to 6.3.0

* Fri Mar 25 2022 Sandro Mani <manisandro@gmail.com> - 6.2.3-3
- Rebuild with mingw-gcc-12

* Sun Mar 06 2022 Sandro Mani <manisandro@gmail.com> - 6.2.3-2
- Re-enable s390x build

* Tue Feb 08 2022 Sandro Mani <manisandro@gmail.com> - 6.2.3-1
- Update to 6.2.3

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 6.2.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Dec 17 2021 Sandro Mani <manisandro@gmail.com> - 6.2.2-2
- Fix dir ownership

* Thu Dec 16 2021 Sandro Mani <manisandro@gmail.com> - 6.2.2-1
- Initial package
