%{?mingw_package_header}

%global qt_module qtsensors
#global pre rc2

#global commit a73dfa7c63b82e25f93e44ed6386664373aaca74
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
Summary:        Qt6 for Windows - QtSensors component

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

BuildRequires:  mingw64-filesystem >= 96
BuildRequires:  mingw64-gcc-c++
BuildRequires:  mingw64-qt6-qtbase = %{version}
BuildRequires:  mingw64-qt6-qtdeclarative = %{version}


%description
This package contains the Qt software toolkit for developing
cross-platform applications.

This is the Windows version of Qt, for use in conjunction with the
Fedora Windows cross-compiler.


# Win32
%package -n mingw32-qt6-%{qt_module}
Summary:        Qt6 for Windows - QtSensors component

%description -n mingw32-qt6-%{qt_module}
This package contains the Qt software toolkit for developing
cross-platform applications.

This is the 32-bit Windows version of Qt, for use in conjunction with the
Fedora Windows cross-compiler.


# Win64
%package -n mingw64-qt6-%{qt_module}
Summary:        Qt6 for Windows - QtSensors component

%description -n mingw64-qt6-%{qt_module}
This package contains the Qt software toolkit for developing
cross-platform applications.

This is the 64-bit Windows version of Qt, for use in conjunction with the
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
%license LICENSES/*GPL*
%{mingw32_bindir}/Qt6Sensors.dll
%{mingw32_bindir}/Qt6SensorsQuick.dll
%{mingw32_includedir}/qt6/QtSensors/
%{mingw32_includedir}/qt6/QtSensorsQuick/
%{mingw32_libdir}/cmake/Qt6/FindSensorfw.cmake
%{mingw32_libdir}/cmake/Qt6BuildInternals/StandaloneTests/QtSensorsTestsConfig.cmake
%{mingw32_libdir}/cmake/Qt6Sensors/
%{mingw32_libdir}/cmake/Qt6SensorsQuick/
%{mingw32_libdir}/cmake/Qt6Qml/QmlPlugins/Qt6SensorsQuickplugin*
%{mingw32_libdir}/pkgconfig/Qt6Sensors.pc
%{mingw32_libdir}/pkgconfig/Qt6SensorsQuick.pc
%{mingw32_libdir}/libQt6Sensors.dll.a
%{mingw32_libdir}/libQt6SensorsQuick.dll.a
%{mingw32_libdir}/qt6/metatypes/qt6sensors_relwithdebinfo_metatypes.json
%{mingw32_libdir}/qt6/metatypes/qt6sensorsquick_relwithdebinfo_metatypes.json
%{mingw32_libdir}/qt6/sbom/%{qt_module}-%{version}.spdx
%{mingw32_libdir}/Qt6Sensors.prl
%{mingw32_libdir}/Qt6SensorsQuick.prl
%dir %{mingw32_libdir}/qt6/plugins/sensors/
%{mingw32_libdir}/qt6/plugins/sensors/qtsensors_generic.dll
%{mingw32_libdir}/qt6/mkspecs/modules/qt_lib_sensors.pri
%{mingw32_libdir}/qt6/mkspecs/modules/qt_lib_sensors_private.pri
%{mingw32_libdir}/qt6/mkspecs/modules/qt_lib_sensorsquick.pri
%{mingw32_libdir}/qt6/mkspecs/modules/qt_lib_sensorsquick_private.pri
%{mingw32_libdir}/qt6/qml/QtSensors/
%{mingw32_libdir}/qt6/modules/Sensors.json
%{mingw32_libdir}/qt6/modules/SensorsQuick.json

# Win64
%files -n mingw64-qt6-%{qt_module}
%license LICENSES/*GPL*
%{mingw64_bindir}/Qt6Sensors.dll
%{mingw64_bindir}/Qt6SensorsQuick.dll
%{mingw64_includedir}/qt6/QtSensors/
%{mingw64_includedir}/qt6/QtSensorsQuick/
%{mingw64_libdir}/cmake/Qt6/FindSensorfw.cmake
%{mingw64_libdir}/cmake/Qt6BuildInternals/StandaloneTests/QtSensorsTestsConfig.cmake
%{mingw64_libdir}/cmake/Qt6Sensors/
%{mingw64_libdir}/cmake/Qt6SensorsQuick/
%{mingw64_libdir}/cmake/Qt6Qml/QmlPlugins/Qt6SensorsQuickplugin*
%{mingw64_libdir}/pkgconfig/Qt6Sensors.pc
%{mingw64_libdir}/pkgconfig/Qt6SensorsQuick.pc
%{mingw64_libdir}/libQt6Sensors.dll.a
%{mingw64_libdir}/libQt6SensorsQuick.dll.a
%{mingw64_libdir}/qt6/metatypes/qt6sensors_relwithdebinfo_metatypes.json
%{mingw64_libdir}/qt6/metatypes/qt6sensorsquick_relwithdebinfo_metatypes.json
%{mingw64_libdir}/qt6/sbom/%{qt_module}-%{version}.spdx
%{mingw64_libdir}/Qt6Sensors.prl
%{mingw64_libdir}/Qt6SensorsQuick.prl
%dir %{mingw64_libdir}/qt6/plugins/sensors/
%{mingw64_libdir}/qt6/plugins/sensors/qtsensors_generic.dll
%{mingw64_libdir}/qt6/mkspecs/modules/qt_lib_sensors.pri
%{mingw64_libdir}/qt6/mkspecs/modules/qt_lib_sensors_private.pri
%{mingw64_libdir}/qt6/mkspecs/modules/qt_lib_sensorsquick.pri
%{mingw64_libdir}/qt6/mkspecs/modules/qt_lib_sensorsquick_private.pri
%{mingw64_libdir}/qt6/qml/QtSensors/
%{mingw64_libdir}/qt6/modules/Sensors.json
%{mingw64_libdir}/qt6/modules/SensorsQuick.json


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

* Mon Apr 08 2024 Sandro Mani <manisandro@gmail.com> - 6.7.0-1
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

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 6.2.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Dec 16 2021 Sandro Mani <manisandro@gmail.com> - 6.2.2-1
- Update to 6.2.2

* Tue Nov 09 2021 Sandro Mani <manisandro@gmail.com> - 6.2.1-1
- Update to 6.2.1

* Sun Oct 31 2021 Sandro Mani <manisandro@gmail.com> - 6.2.0-2
- Own %%{mingw32,64_libdir}/qt6/plugins/sensors/
- Enhance description

* Sun Oct 03 2021 Sandro Mani <manisandro@gmail.com> - 6.2.0-1
- Update to 6.2.0

* Wed Sep 29 2021 Sandro Mani <manisandro@gmail.com> - 6.2.0-0.2.rc2
- Initial package
