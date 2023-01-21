%{?mingw_package_header}

%global qt_module qtwebsockets
#global pre rc2

#global commit e5133f4f0bb7c01d7bd7fc499d8c148c03a5b500
#global shortcommit %(c=%{commit}; echo ${c:0:7})

%if 0%{?commit:1}
%global source_folder %{qt_module}-%{commit}
%else
%global source_folder %{qt_module}-everywhere-src-%{version}%{?pre:-%{pre}}
%endif

# first two digits of version
%define release_version %(echo %{version} | awk -F. '{print $1"."$2}')

Name:           mingw-qt6-%{qt_module}
Version:        6.4.2
Release:        2%{?dist}
Summary:        Qt6 for Windows - QtWebsockets component

License:        LGPL-3.0-only OR GPL-2.0-only
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
Summary:        Qt6 for Windows - QtWebsockets component

%description -n mingw32-qt6-%{qt_module}
This package contains the Qt software toolkit for developing
cross-platform applications.

This is the Windows version of Qt, for use in conjunction with the
Fedora Windows cross-compiler.


# Win64
%package -n mingw64-qt6-%{qt_module}
Summary:        Qt6 for Windows - QtWebsockets component

%description -n mingw64-qt6-%{qt_module}
This package contains the Qt software toolkit for developing
cross-platform applications.

This is the Windows version of Qt, for use in conjunction with the
Fedora Windows cross-compiler.


%{?mingw_debug_package}


%prep
%autosetup -p1 -n %{source_folder}


%build
%mingw_cmake -G Ninja -DCMAKE_BUILD_TYPE=RelWithDebInfo
%mingw_ninja


%install
%mingw_ninja_install


# Win32
%files -n mingw32-qt6-%{qt_module}
%license LICENSES/*GPL*
%{mingw32_bindir}/Qt6WebSockets.dll
%{mingw32_includedir}/qt6/QtWebSockets/
%{mingw32_libdir}/cmake/Qt6WebSockets/
%{mingw32_libdir}/cmake/Qt6BuildInternals/StandaloneTests/QtWebSocketsTestsConfig.cmake
%{mingw32_libdir}/cmake/Qt6Qml/QmlPlugins/Qt6qmlwebsockets*
%{mingw32_libdir}/pkgconfig/Qt6WebSockets.pc
%{mingw32_libdir}/libQt6WebSockets.dll.a
%{mingw32_libdir}/metatypes/qt6websockets_relwithdebinfo_metatypes.json
%{mingw32_libdir}/Qt6WebSockets.prl
%{mingw32_libdir}/qt6/mkspecs/modules/qt_lib_websockets.pri
%{mingw32_libdir}/qt6/mkspecs/modules/qt_lib_websockets_private.pri
%{mingw32_libdir}/qt6/qml/QtWebSockets/
%{mingw32_datadir}/qt6/modules/WebSockets.json


# Win64
%files -n mingw64-qt6-%{qt_module}
%license LICENSES/*GPL*
%{mingw64_bindir}/Qt6WebSockets.dll
%{mingw64_includedir}/qt6/QtWebSockets/
%{mingw64_libdir}/cmake/Qt6WebSockets/
%{mingw64_libdir}/cmake/Qt6BuildInternals/StandaloneTests/QtWebSocketsTestsConfig.cmake
%{mingw64_libdir}/cmake/Qt6Qml/QmlPlugins/Qt6qmlwebsockets*
%{mingw64_libdir}/pkgconfig/Qt6WebSockets.pc
%{mingw64_libdir}/libQt6WebSockets.dll.a
%{mingw64_libdir}/metatypes/qt6websockets_relwithdebinfo_metatypes.json
%{mingw64_libdir}/Qt6WebSockets.prl
%{mingw64_libdir}/qt6/mkspecs/modules/qt_lib_websockets.pri
%{mingw64_libdir}/qt6/mkspecs/modules/qt_lib_websockets_private.pri
%{mingw64_libdir}/qt6/qml/QtWebSockets/
%{mingw64_datadir}/qt6/modules/WebSockets.json


%changelog
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

* Sun Oct 03 2021 Sandro Mani <manisandro@gmail.com> - 6.2.0-1
- Update to 6.2.0

* Wed Sep 29 2021 Sandro Mani <manisandro@gmail.com> - 6.2.0-0.2.rc2
- Initial package
