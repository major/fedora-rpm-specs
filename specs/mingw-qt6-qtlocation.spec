%{?mingw_package_header}

%global qt_module qtlocation
#global pre rc2

#global commit f28408346243cf090326f4738fd838219c21e00f
#global shortcommit %%(c=%%{commit}; echo ${c:0:7})

%if 0%{?commit:1}
%global source_folder %{qt_module}-%{commit}
%else
%global source_folder %{qt_module}-everywhere-src-%{version}%{?pre:-%{pre}}
%endif

# first two digits of version
%define release_version %(echo %{version} | awk -F. '{print $1"."$2}')

Name:           mingw-qt6-%{qt_module}
Version:        6.8.1
Release:        2%{?dist}
Summary:        Qt6 for Windows - QtLocation component

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
BuildRequires:  mingw32-qt6-qtpositioning = %{version}

BuildRequires:  mingw64-filesystem >= 96
BuildRequires:  mingw64-gcc-c++
BuildRequires:  mingw64-qt6-qtbase = %{version}
BuildRequires:  mingw64-qt6-qtdeclarative = %{version}
BuildRequires:  mingw64-qt6-qtpositioning = %{version}


%description
This package contains the Qt software toolkit for developing
cross-platform applications.

This is the Windows version of Qt, for use in conjunction with the
Fedora Windows cross-compiler.


# Win32
%package -n mingw32-qt6-%{qt_module}
Summary:        Qt6 for Windows - QtLocation component

%description -n mingw32-qt6-%{qt_module}
This package contains the Qt software toolkit for developing
cross-platform applications.

This is the Windows version of Qt, for use in conjunction with the
Fedora Windows cross-compiler.


# Win64
%package -n mingw64-qt6-%{qt_module}
Summary:        Qt6 for Windows - QtLocation component

%description -n mingw64-qt6-%{qt_module}
This package contains the Qt software toolkit for developing
cross-platform applications.

This is the Windows version of Qt, for use in conjunction with the
Fedora Windows cross-compiler.


%{?mingw_debug_package}


%prep
%autosetup -p1 -n %{source_folder}


%build
export MINGW32_CXXFLAGS="%{mingw32_cflags} -msse2"
export MINGW64_CXXFLAGS="%{mingw64_cflags} -msse2"
%mingw_cmake -GNinja -DCMAKE_BUILD_TYPE=RelWithDebInfo
%mingw_ninja


%install
%mingw_ninja_install



# Win32
%files -n mingw32-qt6-%{qt_module}
%license LICENSES/GPL* LICENSES/LGPL*
%{mingw32_bindir}/Qt6Location.dll
%{mingw32_libdir}/libQt6Location.dll.a
%{mingw32_libdir}/qt6/metatypes/qt6location_relwithdebinfo_metatypes.json
%{mingw32_libdir}/qt6/modules/Location.json
%{mingw32_libdir}/cmake/Qt6BuildInternals/StandaloneTests/QtLocationTestsConfig.cmake
%{mingw32_libdir}/cmake/Qt6Location/
%{mingw32_libdir}/cmake/Qt6Qml/QmlPlugins/Qt6declarative_locationAdditionalTargetInfo.cmake
%{mingw32_libdir}/cmake/Qt6Qml/QmlPlugins/Qt6declarative_locationConfig.cmake
%{mingw32_libdir}/cmake/Qt6Qml/QmlPlugins/Qt6declarative_locationConfigVersion.cmake
%{mingw32_libdir}/cmake/Qt6Qml/QmlPlugins/Qt6declarative_locationConfigVersionImpl.cmake
%{mingw32_libdir}/cmake/Qt6Qml/QmlPlugins/Qt6declarative_locationTargets.cmake
%{mingw32_libdir}/cmake/Qt6Qml/QmlPlugins/Qt6declarative_locationTargets-relwithdebinfo.cmake
%{mingw32_libdir}/pkgconfig/Qt6Location.pc
%{mingw32_libdir}/qt6/qml/QtLocation/
%{mingw32_libdir}/qt6/mkspecs/modules/qt_lib_location.pri
%{mingw32_libdir}/qt6/mkspecs/modules/qt_lib_location_private.pri
%dir %{mingw32_libdir}/qt6/plugins/geoservices/
%{mingw32_libdir}/qt6/plugins/geoservices/qtgeoservices_itemsoverlay.dll
%{mingw32_libdir}/qt6/plugins/geoservices/qtgeoservices_osm.dll
%{mingw32_libdir}/qt6/sbom/%{qt_module}-%{version}.spdx
%{mingw32_libdir}/Qt6Location.prl
%{mingw32_includedir}/qt6/QtLocation/

# Win64
%files -n mingw64-qt6-%{qt_module}
%license LICENSES/GPL* LICENSES/LGPL*
%{mingw64_bindir}/Qt6Location.dll
%{mingw64_libdir}/libQt6Location.dll.a
%{mingw64_libdir}/qt6/metatypes/qt6location_relwithdebinfo_metatypes.json
%{mingw64_libdir}/qt6/modules/Location.json
%{mingw64_libdir}/cmake/Qt6BuildInternals/StandaloneTests/QtLocationTestsConfig.cmake
%{mingw64_libdir}/cmake/Qt6Location/
%{mingw64_libdir}/cmake/Qt6Qml/QmlPlugins/Qt6declarative_locationAdditionalTargetInfo.cmake
%{mingw64_libdir}/cmake/Qt6Qml/QmlPlugins/Qt6declarative_locationConfig.cmake
%{mingw64_libdir}/cmake/Qt6Qml/QmlPlugins/Qt6declarative_locationConfigVersion.cmake
%{mingw64_libdir}/cmake/Qt6Qml/QmlPlugins/Qt6declarative_locationConfigVersionImpl.cmake
%{mingw64_libdir}/cmake/Qt6Qml/QmlPlugins/Qt6declarative_locationTargets.cmake
%{mingw64_libdir}/cmake/Qt6Qml/QmlPlugins/Qt6declarative_locationTargets-relwithdebinfo.cmake
%{mingw64_libdir}/pkgconfig/Qt6Location.pc
%{mingw64_libdir}/qt6/qml/QtLocation/
%{mingw64_libdir}/qt6/mkspecs/modules/qt_lib_location.pri
%{mingw64_libdir}/qt6/mkspecs/modules/qt_lib_location_private.pri
%dir %{mingw64_libdir}/qt6/plugins/geoservices/
%{mingw64_libdir}/qt6/plugins/geoservices/qtgeoservices_itemsoverlay.dll
%{mingw64_libdir}/qt6/plugins/geoservices/qtgeoservices_osm.dll
%{mingw64_libdir}/qt6/sbom/%{qt_module}-%{version}.spdx
%{mingw64_libdir}/Qt6Location.prl
%{mingw64_includedir}/qt6/QtLocation/


%changelog
* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 6.8.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Sat Dec 07 2024 Sandro Mani <manisandro@gmail.com> - 6.8.1-1
- Update to 6.8.1

* Wed Oct 23 2024 Sandro Mani <manisandro@gmail.com> - 6.8.0-1
- Update to 6.8.0

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 6.7.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Wed Jul 03 2024 Sandro Mani <manisandro@gmail.com> - 6.7.2-1
- Update to 6.7.2

* Mon May 27 2024 Sandro Mani <manisandro@gmail.com> - 6.7.1-1
- Update to 6.7.1

* Sat Apr 13 2024 Sandro Mani <manisandro@gmail.com> - 6.7.0-1
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

* Mon Jul 31 2023 Sandro Mani <manisandro@gmail.com> - 6.5.2-1
- Update to 6.5.2

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 6.5.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Fri Jun 16 2023 Sandro Mani <manisandro@gmail.com> - 6.5.1-3
- Fix license
- Fix %%{mingwXX_libdir}/qt6/plugins/geoservices/ dir ownership

* Wed Jun 07 2023 Sandro Mani <manisandro@gmail.com> - 6.5.1-2
- Fix license

* Fri Jun 02 2023 Sandro Mani <manisandro@gmail.com> - 6.5.1-1
- Update to 6.5.1

* Wed Nov 03 2021 Sandro Mani <manisandro@gmail.com> - 6.2.1-1
- Update to 6.2.1

* Tue Oct 26 2021 Sandro Mani <manisandro@gmail.com> - 6.2.0-3
- Base license is LGPLv3 or GPLv2

* Fri Oct 08 2021 Sandro Mani <manisandro@gmail.com> - 6.2.0-2
- Remove unused bundled libraries
- Clarify license

* Sun Oct 03 2021 Sandro Mani <manisandro@gmail.com> - 6.2.0-1
- Update to 6.2.0

* Wed Sep 29 2021 Sandro Mani <manisandro@gmail.com> - 6.2.0-0.2.rc2
- Update to 6.2.0-rc2

* Thu Sep 23 2021 Sandro Mani <manisandro@gmail.com> - 6.2.0-0.1.rc
- Inital package
