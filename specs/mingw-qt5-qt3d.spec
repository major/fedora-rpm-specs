%{?mingw_package_header}

# Disable debuginfo subpackages and debugsource packages for now to use old logic
%undefine _debugsource_packages
%undefine _debuginfo_subpackages

# Override the __debug_install_post argument as this package
# contains both native as well as cross compiled binaries
%global __debug_install_post %%{mingw_debug_install_post}; %{_bindir}/find-debuginfo.sh %{?_missing_build_ids_terminate_build:--strict-build-id} %{?_find_debuginfo_opts} "%{_builddir}/%%{?buildsubdir}" %{nil}

%global qt_module qt3d
#global pre beta

#global commit bdb98baf8253c69949a8c259369203da9ffb269c
#global shortcommit %(c=%{commit}; echo ${c:0:7})

%if 0%{?commit:1}
%global source_folder %{qt_module}-%{commit}
%else
%global source_folder %{qt_module}-everywhere-src-%{version}%{?pre:-%{pre}}
%endif

# first two digits of version
%define release_version %(echo %{version} | awk -F. '{print $1"."$2}')

Name:           mingw-qt5-%{qt_module}
Version:        5.15.16
Release:        1%{?dist}
Summary:        Qt5 for Windows - Qt3d component

# Automatically converted from old format: GPLv3 with exceptions or LGPLv2 with exceptions - review is highly recommended.
License:        LicenseRef-Callaway-GPLv3-with-exceptions OR LGPL-2.0-or-later WITH FLTK-exception
URL:            http://qt.io/

%if 0%{?commit:1}
Source0:        https://github.com/qt/%{qt_module}/archive/%{commit}/%{qt_module}-everywhere-src-%{commit}.tar.gz
%else
Source0:        http://download.qt.io/%{?pre:development}%{?!pre:official}_releases/qt/%{release_version}/%{version}%{?pre:-%pre}/submodules/%{qt_module}-everywhere-opensource-src-%{version}%{?pre:-%pre}.tar.xz
%endif

# Make sure -lz is added to the LDFLAGS
Patch0:         qt3d-fix-zlib-linker-flags.patch

BuildRequires:  gcc-c++
BuildRequires:  make
BuildRequires:  zlib-devel

BuildRequires:  mingw32-filesystem >= 96
BuildRequires:  mingw32-gcc-c++
BuildRequires:  mingw32-qt5-qtbase = %{version}
BuildRequires:  mingw32-qt5-qtbase-devel = %{version}
BuildRequires:  mingw32-qt5-qtdeclarative = %{version}

BuildRequires:  mingw64-filesystem >= 96
BuildRequires:  mingw64-gcc-c++
BuildRequires:  mingw64-qt5-qtbase = %{version}
BuildRequires:  mingw64-qt5-qtbase-devel = %{version}
BuildRequires:  mingw64-qt5-qtdeclarative = %{version}

# This package depends on QtOpenGLExtensions which is only available as a static library
# See http://code.qt.io/cgit/qt/qtbase.git/commit/?id=a2ddf3dfe066bb4e58de1d11b1800efcd05fb3a0
BuildRequires:  mingw32-qt5-qtbase-static = %{version}
BuildRequires:  mingw64-qt5-qtbase-static = %{version}

%description
This package contains the Qt software toolkit for developing
cross-platform applications.

This is the Windows version of Qt, for use in conjunction with the
Fedora Windows cross-compiler.


# Win32
%package -n mingw32-qt5-%{qt_module}
Summary:        Qt5 for Windows - Qt3d component
BuildArch:      noarch

%description -n mingw32-qt5-%{qt_module}
This package contains the Qt software toolkit for developing
cross-platform applications.

This is the Windows version of Qt, for use in conjunction with the
Fedora Windows cross-compiler.

%package -n mingw32-qt5-%{qt_module}-tools
Summary:        Qt5 for Windows - Native tools for the Qt3d component
Requires:       mingw32-qt5-%{qt_module} = %{version}-%{release}

%description -n mingw32-qt5-%{qt_module}-tools
This package contains the Qt software toolkit for developing
cross-platform applications.

This is the Windows version of Qt, for use in conjunction with the
Fedora Windows cross-compiler.


# Win64
%package -n mingw64-qt5-%{qt_module}
Summary:        Qt5 for Windows - Qt3d component
BuildArch:      noarch

%description -n mingw64-qt5-%{qt_module}
This package contains the Qt software toolkit for developing
cross-platform applications.

This is the Windows version of Qt, for use in conjunction with the
Fedora Windows cross-compiler.

%package -n mingw64-qt5-%{qt_module}-tools
Summary:        Qt5 for Windows - Native tools for the Qt3d component
Requires:       mingw64-qt5-%{qt_module} = %{version}-%{release}

%description -n mingw64-qt5-%{qt_module}-tools
This package contains the Qt software toolkit for developing
cross-platform applications.

This is the Windows version of Qt, for use in conjunction with the
Fedora Windows cross-compiler.


%{?mingw_debug_package}


%prep
%autosetup -p1 -n %{source_folder}
%if 0%{?commit:1}
# Make sure the syncqt tool is run when using a git snapshot
mkdir .git
%endif


%build
%mingw_qmake_qt5 ../%{qt_module}.pro
%mingw_make_build


%install
%mingw_make install INSTALL_ROOT=%{buildroot}

# .prl files aren't interesting for us

# Exclude debug files from the main files (note: the debug files are only created after %%install, so we can't search for them directly)
find %{buildroot}%{mingw32_prefix} | grep -E '.(exe|dll|pyd)$' | sed 's|^%{buildroot}\(.*\)$|%%exclude \1.debug|' > mingw32-qt5-%{qt_module}.debugfiles
find %{buildroot}%{mingw64_prefix} | grep -E '.(exe|dll|pyd)$' | sed 's|^%{buildroot}\(.*\)$|%%exclude \1.debug|' > mingw64-qt5-%{qt_module}.debugfiles


# Win32
%files -n mingw32-qt5-%{qt_module} -f mingw32-qt5-%{qt_module}.debugfiles
%license LICENSE.LGPL* LICENSE.GPL*
%{mingw32_bindir}/Qt53DAnimation.dll
%{mingw32_bindir}/Qt53DCore.dll
%{mingw32_bindir}/Qt53DExtras.dll
%{mingw32_bindir}/Qt53DInput.dll
%{mingw32_bindir}/Qt53DLogic.dll
%{mingw32_bindir}/Qt53DQuick.dll
%{mingw32_bindir}/Qt53DQuickAnimation.dll
%{mingw32_bindir}/Qt53DQuickExtras.dll
%{mingw32_bindir}/Qt53DQuickInput.dll
%{mingw32_bindir}/Qt53DQuickRender.dll
%{mingw32_bindir}/Qt53DQuickScene2D.dll
%{mingw32_bindir}/Qt53DRender.dll
%{mingw32_includedir}/qt5/Qt3DAnimation/
%{mingw32_includedir}/qt5/Qt3DCore/
%{mingw32_includedir}/qt5/Qt3DExtras/
%{mingw32_includedir}/qt5/Qt3DInput/
%{mingw32_includedir}/qt5/Qt3DLogic/
%{mingw32_includedir}/qt5/Qt3DQuick/
%{mingw32_includedir}/qt5/Qt3DQuickAnimation/
%{mingw32_includedir}/qt5/Qt3DQuickExtras/
%{mingw32_includedir}/qt5/Qt3DQuickInput/
%{mingw32_includedir}/qt5/Qt3DQuickRender/
%{mingw32_includedir}/qt5/Qt3DQuickScene2D/
%{mingw32_includedir}/qt5/Qt3DRender/
%{mingw32_libdir}/*.prl
%{mingw32_libdir}/libQt53DAnimation.dll.a
%{mingw32_libdir}/libQt53DCore.dll.a
%{mingw32_libdir}/libQt53DExtras.dll.a
%{mingw32_libdir}/libQt53DInput.dll.a
%{mingw32_libdir}/libQt53DLogic.dll.a
%{mingw32_libdir}/libQt53DQuick.dll.a
%{mingw32_libdir}/libQt53DQuickAnimation.dll.a
%{mingw32_libdir}/libQt53DQuickExtras.dll.a
%{mingw32_libdir}/libQt53DQuickInput.dll.a
%{mingw32_libdir}/libQt53DQuickRender.dll.a
%{mingw32_libdir}/libQt53DQuickScene2D.dll.a
%{mingw32_libdir}/libQt53DRender.dll.a
%{mingw32_libdir}/qt5/plugins/geometryloaders/
%{mingw32_libdir}/qt5/plugins/renderers/
%{mingw32_libdir}/qt5/plugins/renderplugins/
%{mingw32_libdir}/qt5/plugins/sceneparsers/
%{mingw32_libdir}/cmake/Qt53DAnimation/
%{mingw32_libdir}/cmake/Qt53DCore/
%{mingw32_libdir}/cmake/Qt53DExtras/
%{mingw32_libdir}/cmake/Qt53DInput/
%{mingw32_libdir}/cmake/Qt53DLogic/
%{mingw32_libdir}/cmake/Qt53DQuick/
%{mingw32_libdir}/cmake/Qt53DQuickAnimation/
%{mingw32_libdir}/cmake/Qt53DQuickExtras/
%{mingw32_libdir}/cmake/Qt53DQuickInput/
%{mingw32_libdir}/cmake/Qt53DQuickRender/
%{mingw32_libdir}/cmake/Qt53DQuickScene2D/
%{mingw32_libdir}/cmake/Qt53DRender/
%{mingw32_libdir}/pkgconfig/Qt53DAnimation.pc
%{mingw32_libdir}/pkgconfig/Qt53DCore.pc
%{mingw32_libdir}/pkgconfig/Qt53DExtras.pc
%{mingw32_libdir}/pkgconfig/Qt53DInput.pc
%{mingw32_libdir}/pkgconfig/Qt53DLogic.pc
%{mingw32_libdir}/pkgconfig/Qt53DQuick.pc
%{mingw32_libdir}/pkgconfig/Qt53DQuickAnimation.pc
%{mingw32_libdir}/pkgconfig/Qt53DQuickExtras.pc
%{mingw32_libdir}/pkgconfig/Qt53DQuickInput.pc
%{mingw32_libdir}/pkgconfig/Qt53DQuickRender.pc
%{mingw32_libdir}/pkgconfig/Qt53DQuickScene2D.pc
%{mingw32_libdir}/pkgconfig/Qt53DRender.pc
%{mingw32_datadir}/qt5/mkspecs/modules/qt_lib_3danimation.pri
%{mingw32_datadir}/qt5/mkspecs/modules/qt_lib_3danimation_private.pri
%{mingw32_datadir}/qt5/mkspecs/modules/qt_lib_3dcore.pri
%{mingw32_datadir}/qt5/mkspecs/modules/qt_lib_3dcore_private.pri
%{mingw32_datadir}/qt5/mkspecs/modules/qt_lib_3dextras.pri
%{mingw32_datadir}/qt5/mkspecs/modules/qt_lib_3dextras_private.pri
%{mingw32_datadir}/qt5/mkspecs/modules/qt_lib_3dinput.pri
%{mingw32_datadir}/qt5/mkspecs/modules/qt_lib_3dinput_private.pri
%{mingw32_datadir}/qt5/mkspecs/modules/qt_lib_3dlogic.pri
%{mingw32_datadir}/qt5/mkspecs/modules/qt_lib_3dlogic_private.pri
%{mingw32_datadir}/qt5/mkspecs/modules/qt_lib_3dquick.pri
%{mingw32_datadir}/qt5/mkspecs/modules/qt_lib_3dquick_private.pri
%{mingw32_datadir}/qt5/mkspecs/modules/qt_lib_3dquickanimation.pri
%{mingw32_datadir}/qt5/mkspecs/modules/qt_lib_3dquickanimation_private.pri
%{mingw32_datadir}/qt5/mkspecs/modules/qt_lib_3dquickextras.pri
%{mingw32_datadir}/qt5/mkspecs/modules/qt_lib_3dquickextras_private.pri
%{mingw32_datadir}/qt5/mkspecs/modules/qt_lib_3dquickinput.pri
%{mingw32_datadir}/qt5/mkspecs/modules/qt_lib_3dquickinput_private.pri
%{mingw32_datadir}/qt5/mkspecs/modules/qt_lib_3dquickrender.pri
%{mingw32_datadir}/qt5/mkspecs/modules/qt_lib_3dquickrender_private.pri
%{mingw32_datadir}/qt5/mkspecs/modules/qt_lib_3dquickscene2d.pri
%{mingw32_datadir}/qt5/mkspecs/modules/qt_lib_3dquickscene2d_private.pri
%{mingw32_datadir}/qt5/mkspecs/modules/qt_lib_3drender.pri
%{mingw32_datadir}/qt5/mkspecs/modules/qt_lib_3drender_private.pri
%{mingw32_libdir}/qt5/qml/Qt3D/
%dir %{mingw32_libdir}/qt5/qml/QtQuick/
%{mingw32_libdir}/qt5/qml/QtQuick/Scene2D/
%{mingw32_libdir}/qt5/qml/QtQuick/Scene3D/

%files -n mingw32-qt5-%{qt_module}-tools
%{_prefix}/%{mingw32_target}/bin/qt5/qgltf


# Win64
%files -n mingw64-qt5-%{qt_module} -f mingw64-qt5-%{qt_module}.debugfiles
%license LICENSE.LGPL* LICENSE.GPL*
%{mingw64_bindir}/Qt53DAnimation.dll
%{mingw64_bindir}/Qt53DCore.dll
%{mingw64_bindir}/Qt53DExtras.dll
%{mingw64_bindir}/Qt53DInput.dll
%{mingw64_bindir}/Qt53DLogic.dll
%{mingw64_bindir}/Qt53DQuick.dll
%{mingw64_bindir}/Qt53DQuickAnimation.dll
%{mingw64_bindir}/Qt53DQuickExtras.dll
%{mingw64_bindir}/Qt53DQuickInput.dll
%{mingw64_bindir}/Qt53DQuickRender.dll
%{mingw64_bindir}/Qt53DQuickScene2D.dll
%{mingw64_bindir}/Qt53DRender.dll
%{mingw64_includedir}/qt5/Qt3DAnimation/
%{mingw64_includedir}/qt5/Qt3DCore/
%{mingw64_includedir}/qt5/Qt3DExtras/
%{mingw64_includedir}/qt5/Qt3DInput/
%{mingw64_includedir}/qt5/Qt3DLogic/
%{mingw64_includedir}/qt5/Qt3DQuick/
%{mingw64_includedir}/qt5/Qt3DQuickAnimation/
%{mingw64_includedir}/qt5/Qt3DQuickExtras/
%{mingw64_includedir}/qt5/Qt3DQuickInput/
%{mingw64_includedir}/qt5/Qt3DQuickRender/
%{mingw64_includedir}/qt5/Qt3DQuickScene2D/
%{mingw64_includedir}/qt5/Qt3DRender/
%{mingw64_libdir}/*.prl
%{mingw64_libdir}/libQt53DAnimation.dll.a
%{mingw64_libdir}/libQt53DCore.dll.a
%{mingw64_libdir}/libQt53DExtras.dll.a
%{mingw64_libdir}/libQt53DInput.dll.a
%{mingw64_libdir}/libQt53DLogic.dll.a
%{mingw64_libdir}/libQt53DQuick.dll.a
%{mingw64_libdir}/libQt53DQuickAnimation.dll.a
%{mingw64_libdir}/libQt53DQuickExtras.dll.a
%{mingw64_libdir}/libQt53DQuickInput.dll.a
%{mingw64_libdir}/libQt53DQuickRender.dll.a
%{mingw64_libdir}/libQt53DQuickScene2D.dll.a
%{mingw64_libdir}/libQt53DRender.dll.a
%{mingw64_libdir}/qt5/plugins/geometryloaders/
%{mingw64_libdir}/qt5/plugins/renderers/
%{mingw64_libdir}/qt5/plugins/renderplugins/
%{mingw64_libdir}/qt5/plugins/sceneparsers/
%{mingw64_libdir}/cmake/Qt53DAnimation/
%{mingw64_libdir}/cmake/Qt53DCore/
%{mingw64_libdir}/cmake/Qt53DExtras/
%{mingw64_libdir}/cmake/Qt53DInput/
%{mingw64_libdir}/cmake/Qt53DLogic/
%{mingw64_libdir}/cmake/Qt53DQuick/
%{mingw64_libdir}/cmake/Qt53DQuickAnimation/
%{mingw64_libdir}/cmake/Qt53DQuickExtras/
%{mingw64_libdir}/cmake/Qt53DQuickInput/
%{mingw64_libdir}/cmake/Qt53DQuickRender/
%{mingw64_libdir}/cmake/Qt53DQuickScene2D/
%{mingw64_libdir}/cmake/Qt53DRender/
%{mingw64_libdir}/pkgconfig/Qt53DAnimation.pc
%{mingw64_libdir}/pkgconfig/Qt53DCore.pc
%{mingw64_libdir}/pkgconfig/Qt53DExtras.pc
%{mingw64_libdir}/pkgconfig/Qt53DInput.pc
%{mingw64_libdir}/pkgconfig/Qt53DLogic.pc
%{mingw64_libdir}/pkgconfig/Qt53DQuick.pc
%{mingw64_libdir}/pkgconfig/Qt53DQuickAnimation.pc
%{mingw64_libdir}/pkgconfig/Qt53DQuickExtras.pc
%{mingw64_libdir}/pkgconfig/Qt53DQuickInput.pc
%{mingw64_libdir}/pkgconfig/Qt53DQuickRender.pc
%{mingw64_libdir}/pkgconfig/Qt53DQuickScene2D.pc
%{mingw64_libdir}/pkgconfig/Qt53DRender.pc
%{mingw64_datadir}/qt5/mkspecs/modules/qt_lib_3danimation.pri
%{mingw64_datadir}/qt5/mkspecs/modules/qt_lib_3danimation_private.pri
%{mingw64_datadir}/qt5/mkspecs/modules/qt_lib_3dcore.pri
%{mingw64_datadir}/qt5/mkspecs/modules/qt_lib_3dcore_private.pri
%{mingw64_datadir}/qt5/mkspecs/modules/qt_lib_3dextras.pri
%{mingw64_datadir}/qt5/mkspecs/modules/qt_lib_3dextras_private.pri
%{mingw64_datadir}/qt5/mkspecs/modules/qt_lib_3dinput.pri
%{mingw64_datadir}/qt5/mkspecs/modules/qt_lib_3dinput_private.pri
%{mingw64_datadir}/qt5/mkspecs/modules/qt_lib_3dlogic.pri
%{mingw64_datadir}/qt5/mkspecs/modules/qt_lib_3dlogic_private.pri
%{mingw64_datadir}/qt5/mkspecs/modules/qt_lib_3dquick.pri
%{mingw64_datadir}/qt5/mkspecs/modules/qt_lib_3dquick_private.pri
%{mingw64_datadir}/qt5/mkspecs/modules/qt_lib_3dquickanimation.pri
%{mingw64_datadir}/qt5/mkspecs/modules/qt_lib_3dquickanimation_private.pri
%{mingw64_datadir}/qt5/mkspecs/modules/qt_lib_3dquickextras.pri
%{mingw64_datadir}/qt5/mkspecs/modules/qt_lib_3dquickextras_private.pri
%{mingw64_datadir}/qt5/mkspecs/modules/qt_lib_3dquickinput.pri
%{mingw64_datadir}/qt5/mkspecs/modules/qt_lib_3dquickinput_private.pri
%{mingw64_datadir}/qt5/mkspecs/modules/qt_lib_3dquickrender.pri
%{mingw64_datadir}/qt5/mkspecs/modules/qt_lib_3dquickrender_private.pri
%{mingw64_datadir}/qt5/mkspecs/modules/qt_lib_3dquickscene2d.pri
%{mingw64_datadir}/qt5/mkspecs/modules/qt_lib_3dquickscene2d_private.pri
%{mingw64_datadir}/qt5/mkspecs/modules/qt_lib_3drender.pri
%{mingw64_datadir}/qt5/mkspecs/modules/qt_lib_3drender_private.pri
%{mingw64_libdir}/qt5/qml/Qt3D/
%dir %{mingw64_libdir}/qt5/qml/QtQuick/
%{mingw64_libdir}/qt5/qml/QtQuick/Scene2D/
%{mingw64_libdir}/qt5/qml/QtQuick/Scene3D/

%files -n mingw64-qt5-%{qt_module}-tools
%{_prefix}/%{mingw64_target}/bin/qt5/qgltf


%changelog
* Wed Jan 22 2025 Sandro Mani <manisandro@gmail.com> - 5.15.16-1
- Update to 5.15.16

* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 5.15.15-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Fri Sep 06 2024 Sandro Mani <manisandro@gmail.com> - 5.15.15-1
- Update to 5.15.15

* Mon Sep 02 2024 Miroslav Suchý <msuchy@redhat.com> - 5.15.14-3
- convert license to SPDX

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 5.15.14-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Tue Jun 11 2024 Sandro Mani <manisandro@gmail.com> - 5.15.14-1
- Update to 5.15.14

* Wed May 01 2024 Sandro Mani <manisandro@gmail.com> - 5.15.13-1
- Update to 5.15.13

* Thu Feb 15 2024 Sandro Mani <manisandro@gmail.com> - 5.15.12-1
- Update to 5.15.12

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 5.15.11-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 5.15.11-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sat Oct 14 2023 Sandro Mani <manisandro@gmail.com> - 5.15.11-1
- Update to 5.15.11

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 5.15.10-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jun 15 2023 Sandro Mani <manisandro@gmail.com> - 5.15.10-1
- Update to 5.15.10

* Thu Apr 13 2023 Sandro Mani <manisandro@gmail.com> - 5.15.9-1
- Update to 5.15.9

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 5.15.8-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Mon Jan 09 2023 Sandro Mani <manisandro@gmail.com> - 5.15.8-1
- Update to 5.15.8

* Fri Nov 04 2022 Sandro Mani <manisandro@gmail.com> - 5.15.7-1
- Update to 5.15.7

* Thu Sep 22 2022 Sandro Mani <manisandro@gmail.com> - 5.15.6-1
- Update to 5.15.6

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 5.15.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jul 14 2022 Sandro Mani <manisandro@gmail.com> - 5.15.5-1
- Update to 5.15.5

* Sat May 21 2022 Sandro Mani <manisandro@gmail.com> - 5.15.4-1
- Update to 5.15.4

* Mon Mar 28 2022 Sandro Mani <manisandro@gmail.com> - 5.15.3-2
- BR: mingw-gcc-c++

* Tue Mar 15 2022 Sandro Mani <manisandro@gmail.com> - 5.15.3-1
- Update to 5.15.3

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 5.15.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 5.15.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Thu Apr 22 2021 Jan Blackquill <uhhadd@gmail.com> - 5.15.2-3
- Don't strip .prl files from build

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 5.15.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Nov 23 18:33:00 CET 2020 Sandro Mani <manisandro@gmail.com> - 5.15.2-1
- Update to 5.15.2

* Wed Oct  7 11:13:32 CEST 2020 Sandro Mani <manisandro@gmail.com> - 5.15.1-1
- Update to 5.15.1

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 5.14.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Apr 08 2020 Sandro Mani <manisandro@gmail.com> - 5.14.2-1
- Update to 5.14.2

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 5.13.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Mon Dec 16 2019 Sandro Mani <manisandro@gmail.com> - 5.13.2-1
- Update to 5.13.2

* Tue Oct 08 2019 Sandro Mani <manisandro@gmail.com> - 5.12.5-2
- Rebuild (Changes/Mingw32GccDwarf2)

* Thu Sep 26 2019 Sandro Mani <manisandro@gmail.com> - 5.12.5-1
- Update to 5.12.5

* Tue Aug 27 2019 Sandro Mani <manisandro@gmail.com> - 5.12.4-3
- Rebuild to fix pkg-config files (#1745257)

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 5.12.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jul 18 2019 Sandro Mani <manisandro@gmail.com> - 5.12.4-1
- Update to 5.12.4

* Thu Apr 18 2019 Sandro Mani <manisandro@gmail.com> - 5.12.3-1
- Update to 5.12.3

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 5.11.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Mon Jan 14 2019 Sandro Mani <manisandro@gmail.com> - 5.11.3-1
- Update to 5.11.3

* Sun Sep 23 2018 Sandro Mani <manisandro@gmail.com> - 5.11.2-1
- Update to 5.11.2

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 5.11.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Jun 20 2018 Sandro Mani <manisandro@gmail.com> - 5.11.1-1
- Update to 5.11.1

* Wed May 30 2018 Sandro Mani <manisandro@gmail.com> - 5.11.0-1
- Update to 5.11.0

* Wed Mar 07 2018 Sandro Mani <manisandro@gmail.com> - 5.10.1-2
- Add missing BR: gcc-c++, make

* Fri Feb 16 2018 Sandro Mani <manisandro@gmail.com> - 5.10.1-1
- Update to 5.10.1

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 5.10.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Dec 20 2017 Sandro Mani <manisandro@gmail.com> - 5.10.0-1
- Update to 5.10.0

* Mon Nov 27 2017 Sandro Mani <manisandro@gmail.com> - 5.9.3-1
- Update to 5.9.3

* Wed Oct 11 2017 Sandro Mani <manisandro@gmail.com> - 5.9.2-1
- Update to 5.9.2

* Sat Sep 09 2017 Sandro Mani <manisandro@gmail.com> - 5.9.1-5
- Fix debug files in main package

* Wed Aug 09 2017 Sandro Mani <manisandro@gmail.com> - 5.9.1-4
- Force old debuginfo package logic for now

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 5.9.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 5.9.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Jun 30 2017 Sandro Mani <manisandro@gmail.com> - 5.9.1-1
- Update to 5.9.1

* Wed Jun 28 2017 Sandro Mani <manisandro@gmail.com> - 5.9.0-1
- Update to 5.9.0

* Tue May 09 2017 Sandro Mani <manisandro@gmail.com> - 5.8.0-2
- Rebuild for dropped 0022-Allow-usage-of-static-version-with-CMake.patch in qtbase

* Thu May 04 2017 Sandro Mani <manisandro@gmail.com> - 5.8.0-1
- Update to 5.8.0

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 5.7.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Sat Feb 04 2017 Sandro Mani <manisandro@gmail.com> - 5.7.1-1
- Update to 5.7.1

* Sat May  7 2016 Erik van Pienbroek <epienbro@fedoraproject.org> - 5.6.0-2
- Add BR: mingw{32,64}-qt5-qtbase-devel

* Sun Apr 10 2016 Erik van Pienbroek <epienbro@fedoraproject.org> - 5.6.0-1
- Update to 5.6.0

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 5.5.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Aug  7 2015 Erik van Pienbroek <epienbro@fedoraproject.org> - 5.5.0-1
- Update to 5.5.0
- Added BR: mingw{32,64}-qt5-qtbase-static as this package depends
  on QtOpenGLExtensions which is only available as a static library

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 5.0.0-0.13.git20140525.bdb98ba
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 5.0.0-0.12.git20140525.bdb98ba
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun May 25 2014 Erik van Pienbroek <epienbro@fedoraproject.org> - 5.0.0-0.11.git20140525.bdb98ba
- Update to 20140525 snapshot (rev bdb98ba)

* Sun Jan 12 2014 Erik van Pienbroek <epienbro@fedoraproject.org> - 5.0.0-0.10.git20130923.7433868
- Don't carry .dll.debug files in main package

* Wed Jan  8 2014 Erik van Pienbroek <epienbro@fedoraproject.org> - 5.0.0-0.9.git20130923.7433868
- Dropped manual rename of import libraries

* Sun Jan  5 2014 Erik van Pienbroek <epienbro@fedoraproject.org> - 5.0.0-0.8.git20130923.7433868
- Update to 20130923 snapshot (rev 7433868)
  This is the last Qt 5.2 based revision

* Sun Dec 01 2013 Erik van Pienbroek <epienbro@fedoraproject.org> - 5.0.0-0.7.git20130510.0158ce78
- Fix FTBFS against Qt 5.2

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 5.0.0-0.6.git20130510.0158ce78
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Jul 18 2013 Erik van Pienbroek <epienbro@fedoraproject.org> - 5.0.0-0.5.git20130510.0158ce78
- Make sure the syncqt tool is run because we're using a git snapshot

* Fri May 10 2013 Erik van Pienbroek <epienbro@fedoraproject.org> - 5.0.0-0.4.git20130510.0158ce78
- Update to 20130510 snapshot (rev 0158ce78)

* Sat Jan 12 2013 Erik van Pienbroek <epienbro@fedoraproject.org> - 5.0.0-0.3.git20121111.e4d3ccac
- Fix filelist

* Sun Nov 11 2012 Erik van Pienbroek <epienbro@fedoraproject.org> - 5.0.0-0.2.beta1.git20121111.e4d3ccac
- Update to 20121111 snapshot (rev e4d3ccac)
- Rebuild against latest mingw-qt5-qtbase
- Dropped pkg-config rename hack as it's unneeded now

* Wed Sep 12 2012 Erik van Pienbroek <epienbro@fedoraproject.org> - 5.0.0-0.1.beta1
- Initial release

