%{?mingw_package_header}

%global qt_module qtsvg
#global pre rc2

#global commit 45483bfae4f59ab92be22007cf49d9d7eee8a16c
#global shortcommit %(c=%{commit}; echo ${c:0:7})

%if 0%{?commit:1}
%global source_folder %{qt_module}-%{commit}
%else
%global source_folder %{qt_module}-everywhere-src-%{version}%{?pre:-%{pre}}
%endif

# first two digits of version
%global release_version %(echo %{version} | awk -F. '{print $1"."$2}')

Name:           mingw-qt6-%{qt_module}
Version:        6.3.1
Release:        2%{?dist}
Summary:        Qt6 for Windows - QtSvg component

License:        LGPLv3 or GPLv2
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

BuildRequires:  mingw64-filesystem >= 96
BuildRequires:  mingw64-gcc-c++
BuildRequires:  mingw64-qt6-qtbase = %{version}


%description
This package contains the Qt software toolkit for developing
cross-platform applications.

This is the Windows version of Qt, for use in conjunction with the
Fedora Windows cross-compiler.


# Win32
%package -n mingw32-qt6-%{qt_module}
Summary:        Qt6 for Windows - QtSvg component

%description -n mingw32-qt6-%{qt_module}
This package contains the Qt software toolkit for developing
cross-platform applications.

This is the 32-bit Windows version of Qt, for use in conjunction with the
Fedora Windows cross-compiler.


# Win64
%package -n mingw64-qt6-%{qt_module}
Summary:        Qt6 for Windows - QtSvg component

%description -n mingw64-qt6-%{qt_module}
This package contains the Qt software toolkit for developing
cross-platform applications.

This is the 64-bit Windows version of Qt, for use in conjunction with the
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
%license LICENSE.LGPL* LICENSE.GPL*
%{mingw32_bindir}/Qt6Svg.dll
%{mingw32_bindir}/Qt6SvgWidgets.dll
%{mingw32_includedir}/qt6/QtSvg/
%{mingw32_includedir}/qt6/QtSvgWidgets/
%{mingw32_libdir}/libQt6Svg.dll.a
%{mingw32_libdir}/libQt6SvgWidgets.dll.a
%{mingw32_libdir}/Qt6Svg.prl
%{mingw32_libdir}/Qt6SvgWidgets.prl
%{mingw32_libdir}/cmake/Qt6BuildInternals/StandaloneTests/QtSvgTestsConfig.cmake
%{mingw32_libdir}/cmake/Qt6Gui/Qt6QSvgPlugin*.cmake
%{mingw32_libdir}/cmake/Qt6Gui/Qt6QSvgIconPlugin*.cmake
%{mingw32_libdir}/cmake/Qt6Svg/
%{mingw32_libdir}/cmake/Qt6SvgWidgets/
%{mingw32_libdir}/pkgconfig/Qt6Svg.pc
%{mingw32_libdir}/pkgconfig/Qt6SvgWidgets.pc
%{mingw32_libdir}/metatypes/qt6svg_relwithdebinfo_metatypes.json
%{mingw32_libdir}/metatypes/qt6svgwidgets_relwithdebinfo_metatypes.json
%{mingw32_libdir}/qt6/mkspecs/modules/qt_lib_svg.pri
%{mingw32_libdir}/qt6/mkspecs/modules/qt_lib_svg_private.pri
%{mingw32_libdir}/qt6/mkspecs/modules/qt_lib_svgwidgets.pri
%{mingw32_libdir}/qt6/mkspecs/modules/qt_lib_svgwidgets_private.pri
%dir %{mingw32_libdir}/qt6/plugins/iconengines/
%{mingw32_libdir}/qt6/plugins/iconengines/qsvgicon.dll
%{mingw32_libdir}/qt6/plugins/imageformats/qsvg.dll
%{mingw32_datadir}/qt6/modules/Svg.json
%{mingw32_datadir}/qt6/modules/SvgWidgets.json

# Win64
%files -n mingw64-qt6-%{qt_module}
%license LICENSE.LGPL* LICENSE.GPL*
%{mingw64_bindir}/Qt6Svg.dll
%{mingw64_bindir}/Qt6SvgWidgets.dll
%{mingw64_includedir}/qt6/QtSvg/
%{mingw64_includedir}/qt6/QtSvgWidgets/
%{mingw64_libdir}/libQt6Svg.dll.a
%{mingw64_libdir}/libQt6SvgWidgets.dll.a
%{mingw64_libdir}/Qt6Svg.prl
%{mingw64_libdir}/Qt6SvgWidgets.prl
%{mingw64_libdir}/cmake/Qt6BuildInternals/StandaloneTests/QtSvgTestsConfig.cmake
%{mingw64_libdir}/cmake/Qt6Gui/Qt6QSvgPlugin*.cmake
%{mingw64_libdir}/cmake/Qt6Gui/Qt6QSvgIconPlugin*.cmake
%{mingw64_libdir}/cmake/Qt6Svg/
%{mingw64_libdir}/cmake/Qt6SvgWidgets/
%{mingw64_libdir}/pkgconfig/Qt6Svg.pc
%{mingw64_libdir}/pkgconfig/Qt6SvgWidgets.pc
%{mingw64_libdir}/metatypes/qt6svg_relwithdebinfo_metatypes.json
%{mingw64_libdir}/metatypes/qt6svgwidgets_relwithdebinfo_metatypes.json
%{mingw64_libdir}/qt6/mkspecs/modules/qt_lib_svg.pri
%{mingw64_libdir}/qt6/mkspecs/modules/qt_lib_svg_private.pri
%{mingw64_libdir}/qt6/mkspecs/modules/qt_lib_svgwidgets.pri
%{mingw64_libdir}/qt6/mkspecs/modules/qt_lib_svgwidgets_private.pri
%dir %{mingw64_libdir}/qt6/plugins/iconengines/
%{mingw64_libdir}/qt6/plugins/iconengines/qsvgicon.dll
%{mingw64_libdir}/qt6/plugins/imageformats/qsvg.dll
%{mingw64_datadir}/qt6/modules/Svg.json
%{mingw64_datadir}/qt6/modules/SvgWidgets.json


%changelog
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

* Mon Nov 01 2021 Sandro Mani <manisandro@gmail.com> - 6.2.1-1
- Update to 6.2.1

* Sun Oct 03 2021 Sandro Mani <manisandro@gmail.com> - 6.2.0-1
- Update to 6.2.0

* Mon Sep 27 2021 Sandro Mani <manisandro@gmail.com> - 6.2.0-0.2.rc2
- Update to 6.2.0-rc2

* Wed Sep 22 2021 Sandro Mani <manisandro@gmail.com> - 6.2.0-0.1.rc
- Update to 6.2.0-rc

* Sat Aug 14 2021 Sandro Mani <manisandro@gmail.com> - 6.1.2-1
- Update to 6.1.2

* Thu Jul 08 2021 Sandro Mani <manisandro@gmail.com> - 6.1.1-1
- Initial package
