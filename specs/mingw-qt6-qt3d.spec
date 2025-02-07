%{?mingw_package_header}

%global qt_module qt3d
#global pre rc2

#global commit bdb98baf8253c69949a8c259369203da9ffb269c
#global shortcommit %(c=%{commit}; echo ${c:0:7})

%if 0%{?commit:1}
%global source_folder %{qt_module}-%{commit}
%else
%global source_folder %{qt_module}-everywhere-src-%{version}%{?pre:-%{pre}}
%endif

# first two digits of version
%define release_version %(echo %{version} | awk -F. '{print $1"."$2}')

Name:           mingw-qt6-%{qt_module}
Version:        6.8.2
Release:        1%{?dist}
Summary:        Qt6 for Windows - Qt3d component

License:        LGPL-3.0-only OR GPL-3.0-only WITH Qt-GPL-exception-1.0
URL:            http://qt.io/

BuildArch:      noarch

%if 0%{?commit:1}
Source0:        https://github.com/qt/%{qt_module}/archive/%{commit}/%{qt_module}-everywhere-src-%{commit}.tar.gz
%else
Source0:        http://download.qt.io/%{?pre:development}%{?!pre:official}_releases/qt/%{release_version}/%{version}%{?pre:-%pre}/submodules/%{qt_module}-everywhere-src-%{version}%{?pre:-%pre}.tar.xz
%endif

BuildRequires:  cmake
BuildRequires:  ninja-build

BuildRequires:  mingw32-filesystem >= 96
BuildRequires:  mingw32-gcc-c++
BuildRequires:  mingw32-qt6-qtbase = %{version}
BuildRequires:  mingw32-qt6-qtdeclarative = %{version}
BuildRequires:  mingw32-qt6-qtshadertools = %{version}

BuildRequires:  mingw64-filesystem >= 96
BuildRequires:  mingw64-gcc-c++
BuildRequires:  mingw64-qt6-qtbase = %{version}
BuildRequires:  mingw64-qt6-qtdeclarative = %{version}
BuildRequires:  mingw64-qt6-qtshadertools = %{version}


%description
This package contains the Qt software toolkit for developing
cross-platform applications.

This is the Windows version of Qt, for use in conjunction with the
Fedora Windows cross-compiler.


# Win32
%package -n mingw32-qt6-%{qt_module}
Summary:        Qt6 for Windows - Qt3d component

%description -n mingw32-qt6-%{qt_module}
This package contains the Qt software toolkit for developing
cross-platform applications.

This is the 32-bit Windows version of Qt, for use in conjunction with the
Fedora Windows cross-compiler.


# Win64
%package -n mingw64-qt6-%{qt_module}
Summary:        Qt6 for Windows - Qt3d component

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
%{mingw32_bindir}/Qt63DAnimation.dll
%{mingw32_bindir}/Qt63DCore.dll
%{mingw32_bindir}/Qt63DExtras.dll
%{mingw32_bindir}/Qt63DInput.dll
%{mingw32_bindir}/Qt63DLogic.dll
%{mingw32_bindir}/Qt63DRender.dll
%{mingw32_bindir}/Qt63DQuick.dll
%{mingw32_bindir}/Qt63DQuickAnimation.dll
%{mingw32_bindir}/Qt63DQuickExtras.dll
%{mingw32_bindir}/Qt63DQuickInput.dll
%{mingw32_bindir}/Qt63DQuickRender.dll
%{mingw32_bindir}/Qt63DQuickScene2D.dll
%{mingw32_bindir}/Qt63DQuickScene3D.dll
%{mingw32_libdir}/cmake/Qt63DQuickScene3D/Qt63DQuickScene3DAdditionalTargetInfo.cmake
%{mingw32_libdir}/cmake/Qt63DQuickScene3D/Qt63DQuickScene3DConfig.cmake
%{mingw32_libdir}/cmake/Qt63DQuickScene3D/Qt63DQuickScene3DConfigVersion.cmake
%{mingw32_libdir}/cmake/Qt63DQuickScene3D/Qt63DQuickScene3DConfigVersionImpl.cmake
%{mingw32_libdir}/cmake/Qt63DQuickScene3D/Qt63DQuickScene3DDependencies.cmake
%{mingw32_libdir}/cmake/Qt63DQuickScene3D/Qt63DQuickScene3DTargets-relwithdebinfo.cmake
%{mingw32_libdir}/cmake/Qt63DQuickScene3D/Qt63DQuickScene3DTargets.cmake
%{mingw32_libdir}/cmake/Qt63DQuickScene3D/Qt63DQuickScene3DVersionlessAliasTargets.cmake
%{mingw32_libdir}/cmake/Qt63DQuickScene3D/Qt63DQuickScene3DVersionlessTargets.cmake
%{mingw32_includedir}/qt6/Qt3DAnimation/
%{mingw32_includedir}/qt6/Qt3DCore/
%{mingw32_includedir}/qt6/Qt3DExtras/
%{mingw32_includedir}/qt6/Qt3DInput/
%{mingw32_includedir}/qt6/Qt3DLogic/
%{mingw32_includedir}/qt6/Qt3DQuick/
%{mingw32_includedir}/qt6/Qt3DRender/
%{mingw32_includedir}/qt6/Qt3DQuickAnimation/
%{mingw32_includedir}/qt6/Qt3DQuickExtras/
%{mingw32_includedir}/qt6/Qt3DQuickInput
%{mingw32_includedir}/qt6/Qt3DQuickRender/
%{mingw32_includedir}/qt6/Qt3DQuickScene2D/
%{mingw32_includedir}/qt6/Qt3DQuickScene3D/
%{mingw32_libdir}/cmake/Qt63DAnimation/
%{mingw32_libdir}/cmake/Qt63DCore/
%{mingw32_libdir}/cmake/Qt63DExtras/
%{mingw32_libdir}/cmake/Qt63DInput/
%{mingw32_libdir}/cmake/Qt63DLogic/
%{mingw32_libdir}/cmake/Qt63DRender/
%{mingw32_libdir}/cmake/Qt63DQuick/
%{mingw32_libdir}/cmake/Qt63DQuickAnimation/
%{mingw32_libdir}/cmake/Qt63DQuickExtras/
%{mingw32_libdir}/cmake/Qt63DQuickInput/
%{mingw32_libdir}/cmake/Qt63DQuickRender/
%{mingw32_libdir}/cmake/Qt63DQuickScene2D/
%{mingw32_libdir}/cmake/Qt63DQuickScene3D/
%{mingw32_libdir}/cmake/Qt6BuildInternals/StandaloneTests/Qt3DTestsConfig.cmake
%{mingw32_libdir}/cmake/Qt6Qml/QmlPlugins/Qt6qtquickscene2dplugin*
%{mingw32_libdir}/cmake/Qt6Qml/QmlPlugins/Qt6qtquickscene3dplugi*
%{mingw32_libdir}/cmake/Qt6Qml/QmlPlugins/Qt6quick3danimationplugin*
%{mingw32_libdir}/cmake/Qt6Qml/QmlPlugins/Qt6quick3dcoreplugin*
%{mingw32_libdir}/cmake/Qt6Qml/QmlPlugins/Qt6quick3dextrasplugin*
%{mingw32_libdir}/cmake/Qt6Qml/QmlPlugins/Qt6quick3dinputplugin*
%{mingw32_libdir}/cmake/Qt6Qml/QmlPlugins/Qt6quick3dlogicplugin*
%{mingw32_libdir}/cmake/Qt6Qml/QmlPlugins/Qt6quick3drenderplugin*
%{mingw32_libdir}/cmake/Qt6/FindWrapQt3DAssimp.cmake
%{mingw32_libdir}/pkgconfig/Qt63DAnimation.pc
%{mingw32_libdir}/pkgconfig/Qt63DCore.pc
%{mingw32_libdir}/pkgconfig/Qt63DExtras.pc
%{mingw32_libdir}/pkgconfig/Qt63DInput.pc
%{mingw32_libdir}/pkgconfig/Qt63DLogic.pc
%{mingw32_libdir}/pkgconfig/Qt63DRender.pc
%{mingw32_libdir}/pkgconfig/Qt63DQuick.pc
%{mingw32_libdir}/pkgconfig/Qt63DQuickAnimation.pc
%{mingw32_libdir}/pkgconfig/Qt63DQuickExtras.pc
%{mingw32_libdir}/pkgconfig/Qt63DQuickInput.pc
%{mingw32_libdir}/pkgconfig/Qt63DQuickRender.pc
%{mingw32_libdir}/pkgconfig/Qt63DQuickScene2D.pc
%{mingw32_libdir}/pkgconfig/Qt63DQuickScene3D.pc
%{mingw32_libdir}/libQt63DAnimation.dll.a
%{mingw32_libdir}/libQt63DCore.dll.a
%{mingw32_libdir}/libQt63DExtras.dll.a
%{mingw32_libdir}/libQt63DInput.dll.a
%{mingw32_libdir}/libQt63DLogic.dll.a
%{mingw32_libdir}/libQt63DRender.dll.a
%{mingw32_libdir}/libQt63DQuick.dll.a
%{mingw32_libdir}/libQt63DQuickAnimation.dll.a
%{mingw32_libdir}/libQt63DQuickExtras.dll.a
%{mingw32_libdir}/libQt63DQuickInput.dll.a
%{mingw32_libdir}/libQt63DQuickRender.dll.a
%{mingw32_libdir}/libQt63DQuickScene2D.dll.a
%{mingw32_libdir}/libQt63DQuickScene3D.dll.a
%{mingw32_libdir}/Qt63DAnimation.prl
%{mingw32_libdir}/Qt63DCore.prl
%{mingw32_libdir}/Qt63DExtras.prl
%{mingw32_libdir}/Qt63DInput.prl
%{mingw32_libdir}/Qt63DLogic.prl
%{mingw32_libdir}/Qt63DRender.prl
%{mingw32_libdir}/Qt63DQuick.prl
%{mingw32_libdir}/Qt63DQuickAnimation.prl
%{mingw32_libdir}/Qt63DQuickExtras.prl
%{mingw32_libdir}/Qt63DQuickInput.prl
%{mingw32_libdir}/Qt63DQuickRender.prl
%{mingw32_libdir}/Qt63DQuickScene2D.prl
%{mingw32_libdir}/Qt63DQuickScene3D.prl
%{mingw32_libdir}/qt6/metatypes/qt63danimation_relwithdebinfo_metatypes.json
%{mingw32_libdir}/qt6/metatypes/qt63dcore_relwithdebinfo_metatypes.json
%{mingw32_libdir}/qt6/metatypes/qt63dextras_relwithdebinfo_metatypes.json
%{mingw32_libdir}/qt6/metatypes/qt63dinput_relwithdebinfo_metatypes.json
%{mingw32_libdir}/qt6/metatypes/qt63dlogic_relwithdebinfo_metatypes.json
%{mingw32_libdir}/qt6/metatypes/qt63drender_relwithdebinfo_metatypes.json
%{mingw32_libdir}/qt6/metatypes/qt63dquick_relwithdebinfo_metatypes.json
%{mingw32_libdir}/qt6/metatypes/qt63dquickanimation_relwithdebinfo_metatypes.json
%{mingw32_libdir}/qt6/metatypes/qt63dquickextras_relwithdebinfo_metatypes.json
%{mingw32_libdir}/qt6/metatypes/qt63dquickinput_relwithdebinfo_metatypes.json
%{mingw32_libdir}/qt6/metatypes/qt63dquickrender_relwithdebinfo_metatypes.json
%{mingw32_libdir}/qt6/metatypes/qt63dquickscene2d_relwithdebinfo_metatypes.json
%{mingw32_libdir}/qt6/metatypes/qt63dquickscene3d_relwithdebinfo_metatypes.json
%{mingw32_libdir}/qt6/mkspecs/modules/qt_lib_3dquick.pri
%{mingw32_libdir}/qt6/mkspecs/modules/qt_lib_3danimation.pri
%{mingw32_libdir}/qt6/mkspecs/modules/qt_lib_3danimation_private.pri
%{mingw32_libdir}/qt6/mkspecs/modules/qt_lib_3dcore.pri
%{mingw32_libdir}/qt6/mkspecs/modules/qt_lib_3dcore_private.pri
%{mingw32_libdir}/qt6/mkspecs/modules/qt_lib_3dextras.pri
%{mingw32_libdir}/qt6/mkspecs/modules/qt_lib_3dextras_private.pri
%{mingw32_libdir}/qt6/mkspecs/modules/qt_lib_3dinput.pri
%{mingw32_libdir}/qt6/mkspecs/modules/qt_lib_3dinput_private.pri
%{mingw32_libdir}/qt6/mkspecs/modules/qt_lib_3dlogic.pri
%{mingw32_libdir}/qt6/mkspecs/modules/qt_lib_3dlogic_private.pri
%{mingw32_libdir}/qt6/mkspecs/modules/qt_lib_3drender.pri
%{mingw32_libdir}/qt6/mkspecs/modules/qt_lib_3drender_private.pri
%{mingw32_libdir}/qt6/mkspecs/modules/qt_lib_3dquick_private.pri
%{mingw32_libdir}/qt6/mkspecs/modules/qt_lib_3dquickanimation.pri
%{mingw32_libdir}/qt6/mkspecs/modules/qt_lib_3dquickanimation_private.pri
%{mingw32_libdir}/qt6/mkspecs/modules/qt_lib_3dquickextras.pri
%{mingw32_libdir}/qt6/mkspecs/modules/qt_lib_3dquickextras_private.pri
%{mingw32_libdir}/qt6/mkspecs/modules/qt_lib_3dquickinput.pri
%{mingw32_libdir}/qt6/mkspecs/modules/qt_lib_3dquickinput_private.pri
%{mingw32_libdir}/qt6/mkspecs/modules/qt_lib_3dquickrender.pri
%{mingw32_libdir}/qt6/mkspecs/modules/qt_lib_3dquickrender_private.pri
%{mingw32_libdir}/qt6/mkspecs/modules/qt_lib_3dquickscene2d.pri
%{mingw32_libdir}/qt6/mkspecs/modules/qt_lib_3dquickscene2d_private.pri
%{mingw32_libdir}/qt6/mkspecs/modules/qt_lib_3dquickscene3d.pri
%{mingw32_libdir}/qt6/mkspecs/modules/qt_lib_3dquickscene3d_private.pri
%dir %{mingw32_libdir}/qt6/plugins/geometryloaders/
%{mingw32_libdir}/qt6/plugins/geometryloaders/defaultgeometryloader.dll
%{mingw32_libdir}/qt6/plugins/geometryloaders/gltfgeometryloader.dll
%dir %{mingw32_libdir}/qt6/plugins/renderers/
%{mingw32_libdir}/qt6/plugins/renderers/openglrenderer.dll
%{mingw32_libdir}/qt6/plugins/renderers/rhirenderer.dll
%dir %{mingw32_libdir}/qt6/plugins/renderplugins/
%{mingw32_libdir}/qt6/plugins/renderplugins/scene2d.dll
%dir %{mingw32_libdir}/qt6/plugins/sceneparsers/
%{mingw32_libdir}/qt6/plugins/sceneparsers/assimpsceneimport.dll
%{mingw32_libdir}/qt6/plugins/sceneparsers/gltfsceneexport.dll
%{mingw32_libdir}/qt6/plugins/sceneparsers/gltfsceneimport.dll
%{mingw32_libdir}/qt6/qml/Qt3D/
%{mingw32_libdir}/qt6/qml/QtQuick/Scene2D/
%{mingw32_libdir}/qt6/qml/QtQuick/Scene3D/
%{mingw32_libdir}/qt6/modules/3DAnimation.json
%{mingw32_libdir}/qt6/modules/3DCore.json
%{mingw32_libdir}/qt6/modules/3DExtras.json
%{mingw32_libdir}/qt6/modules/3DInput.json
%{mingw32_libdir}/qt6/modules/3DLogic.json
%{mingw32_libdir}/qt6/modules/3DRender.json
%{mingw32_libdir}/qt6/modules/3DQuick.json
%{mingw32_libdir}/qt6/modules/3DQuickAnimation.json
%{mingw32_libdir}/qt6/modules/3DQuickExtras.json
%{mingw32_libdir}/qt6/modules/3DQuickInput.json
%{mingw32_libdir}/qt6/modules/3DQuickRender.json
%{mingw32_libdir}/qt6/modules/3DQuickScene2D.json
%{mingw32_libdir}/qt6/modules/3DQuickScene3D.json
%{mingw32_libdir}/qt6/sbom/%{qt_module}-%{version}.spdx


# Win64
%files -n mingw64-qt6-%{qt_module}
%license LICENSES/*GPL*
%{mingw64_bindir}/Qt63DAnimation.dll
%{mingw64_bindir}/Qt63DCore.dll
%{mingw64_bindir}/Qt63DExtras.dll
%{mingw64_bindir}/Qt63DInput.dll
%{mingw64_bindir}/Qt63DLogic.dll
%{mingw64_bindir}/Qt63DRender.dll
%{mingw64_bindir}/Qt63DQuick.dll
%{mingw64_bindir}/Qt63DQuickAnimation.dll
%{mingw64_bindir}/Qt63DQuickExtras.dll
%{mingw64_bindir}/Qt63DQuickInput.dll
%{mingw64_bindir}/Qt63DQuickRender.dll
%{mingw64_bindir}/Qt63DQuickScene2D.dll
%{mingw64_bindir}/Qt63DQuickScene3D.dll
%{mingw64_libdir}/cmake/Qt63DQuickScene3D/Qt63DQuickScene3DAdditionalTargetInfo.cmake
%{mingw64_libdir}/cmake/Qt63DQuickScene3D/Qt63DQuickScene3DConfig.cmake
%{mingw64_libdir}/cmake/Qt63DQuickScene3D/Qt63DQuickScene3DConfigVersion.cmake
%{mingw64_libdir}/cmake/Qt63DQuickScene3D/Qt63DQuickScene3DConfigVersionImpl.cmake
%{mingw64_libdir}/cmake/Qt63DQuickScene3D/Qt63DQuickScene3DDependencies.cmake
%{mingw64_libdir}/cmake/Qt63DQuickScene3D/Qt63DQuickScene3DTargets-relwithdebinfo.cmake
%{mingw64_libdir}/cmake/Qt63DQuickScene3D/Qt63DQuickScene3DTargets.cmake
%{mingw64_libdir}/cmake/Qt63DQuickScene3D/Qt63DQuickScene3DVersionlessAliasTargets.cmake
%{mingw64_libdir}/cmake/Qt63DQuickScene3D/Qt63DQuickScene3DVersionlessTargets.cmake
%{mingw64_includedir}/qt6/Qt3DAnimation/
%{mingw64_includedir}/qt6/Qt3DCore/
%{mingw64_includedir}/qt6/Qt3DExtras/
%{mingw64_includedir}/qt6/Qt3DInput/
%{mingw64_includedir}/qt6/Qt3DLogic/
%{mingw64_includedir}/qt6/Qt3DQuick/
%{mingw64_includedir}/qt6/Qt3DRender/
%{mingw64_includedir}/qt6/Qt3DQuickAnimation/
%{mingw64_includedir}/qt6/Qt3DQuickExtras/
%{mingw64_includedir}/qt6/Qt3DQuickInput
%{mingw64_includedir}/qt6/Qt3DQuickRender/
%{mingw64_includedir}/qt6/Qt3DQuickScene2D/
%{mingw64_includedir}/qt6/Qt3DQuickScene3D/
%{mingw64_libdir}/cmake/Qt63DAnimation/
%{mingw64_libdir}/cmake/Qt63DCore/
%{mingw64_libdir}/cmake/Qt63DExtras/
%{mingw64_libdir}/cmake/Qt63DInput/
%{mingw64_libdir}/cmake/Qt63DLogic/
%{mingw64_libdir}/cmake/Qt63DRender/
%{mingw64_libdir}/cmake/Qt63DQuick/
%{mingw64_libdir}/cmake/Qt63DQuickAnimation/
%{mingw64_libdir}/cmake/Qt63DQuickExtras/
%{mingw64_libdir}/cmake/Qt63DQuickInput/
%{mingw64_libdir}/cmake/Qt63DQuickRender/
%{mingw64_libdir}/cmake/Qt63DQuickScene2D/
%{mingw64_libdir}/cmake/Qt63DQuickScene3D/
%{mingw64_libdir}/cmake/Qt6BuildInternals/StandaloneTests/Qt3DTestsConfig.cmake
%{mingw64_libdir}/cmake/Qt6Qml/QmlPlugins/Qt6qtquickscene2dplugin*
%{mingw64_libdir}/cmake/Qt6Qml/QmlPlugins/Qt6qtquickscene3dplugi*
%{mingw64_libdir}/cmake/Qt6Qml/QmlPlugins/Qt6quick3danimationplugin*
%{mingw64_libdir}/cmake/Qt6Qml/QmlPlugins/Qt6quick3dcoreplugin*
%{mingw64_libdir}/cmake/Qt6Qml/QmlPlugins/Qt6quick3dextrasplugin*
%{mingw64_libdir}/cmake/Qt6Qml/QmlPlugins/Qt6quick3dinputplugin*
%{mingw64_libdir}/cmake/Qt6Qml/QmlPlugins/Qt6quick3dlogicplugin*
%{mingw64_libdir}/cmake/Qt6Qml/QmlPlugins/Qt6quick3drenderplugin*
%{mingw64_libdir}/cmake/Qt6/FindWrapQt3DAssimp.cmake
%{mingw64_libdir}/pkgconfig/Qt63DAnimation.pc
%{mingw64_libdir}/pkgconfig/Qt63DCore.pc
%{mingw64_libdir}/pkgconfig/Qt63DExtras.pc
%{mingw64_libdir}/pkgconfig/Qt63DInput.pc
%{mingw64_libdir}/pkgconfig/Qt63DLogic.pc
%{mingw64_libdir}/pkgconfig/Qt63DRender.pc
%{mingw64_libdir}/pkgconfig/Qt63DQuick.pc
%{mingw64_libdir}/pkgconfig/Qt63DQuickAnimation.pc
%{mingw64_libdir}/pkgconfig/Qt63DQuickExtras.pc
%{mingw64_libdir}/pkgconfig/Qt63DQuickInput.pc
%{mingw64_libdir}/pkgconfig/Qt63DQuickRender.pc
%{mingw64_libdir}/pkgconfig/Qt63DQuickScene2D.pc
%{mingw64_libdir}/pkgconfig/Qt63DQuickScene3D.pc
%{mingw64_libdir}/libQt63DAnimation.dll.a
%{mingw64_libdir}/libQt63DCore.dll.a
%{mingw64_libdir}/libQt63DExtras.dll.a
%{mingw64_libdir}/libQt63DInput.dll.a
%{mingw64_libdir}/libQt63DLogic.dll.a
%{mingw64_libdir}/libQt63DRender.dll.a
%{mingw64_libdir}/libQt63DQuick.dll.a
%{mingw64_libdir}/libQt63DQuickAnimation.dll.a
%{mingw64_libdir}/libQt63DQuickExtras.dll.a
%{mingw64_libdir}/libQt63DQuickInput.dll.a
%{mingw64_libdir}/libQt63DQuickRender.dll.a
%{mingw64_libdir}/libQt63DQuickScene2D.dll.a
%{mingw64_libdir}/libQt63DQuickScene3D.dll.a
%{mingw64_libdir}/Qt63DAnimation.prl
%{mingw64_libdir}/Qt63DCore.prl
%{mingw64_libdir}/Qt63DExtras.prl
%{mingw64_libdir}/Qt63DInput.prl
%{mingw64_libdir}/Qt63DLogic.prl
%{mingw64_libdir}/Qt63DRender.prl
%{mingw64_libdir}/Qt63DQuick.prl
%{mingw64_libdir}/Qt63DQuickAnimation.prl
%{mingw64_libdir}/Qt63DQuickExtras.prl
%{mingw64_libdir}/Qt63DQuickInput.prl
%{mingw64_libdir}/Qt63DQuickRender.prl
%{mingw64_libdir}/Qt63DQuickScene2D.prl
%{mingw64_libdir}/Qt63DQuickScene3D.prl
%{mingw64_libdir}/qt6/metatypes/qt63danimation_relwithdebinfo_metatypes.json
%{mingw64_libdir}/qt6/metatypes/qt63dcore_relwithdebinfo_metatypes.json
%{mingw64_libdir}/qt6/metatypes/qt63dextras_relwithdebinfo_metatypes.json
%{mingw64_libdir}/qt6/metatypes/qt63dinput_relwithdebinfo_metatypes.json
%{mingw64_libdir}/qt6/metatypes/qt63dlogic_relwithdebinfo_metatypes.json
%{mingw64_libdir}/qt6/metatypes/qt63drender_relwithdebinfo_metatypes.json
%{mingw64_libdir}/qt6/metatypes/qt63dquick_relwithdebinfo_metatypes.json
%{mingw64_libdir}/qt6/metatypes/qt63dquickanimation_relwithdebinfo_metatypes.json
%{mingw64_libdir}/qt6/metatypes/qt63dquickextras_relwithdebinfo_metatypes.json
%{mingw64_libdir}/qt6/metatypes/qt63dquickinput_relwithdebinfo_metatypes.json
%{mingw64_libdir}/qt6/metatypes/qt63dquickrender_relwithdebinfo_metatypes.json
%{mingw64_libdir}/qt6/metatypes/qt63dquickscene2d_relwithdebinfo_metatypes.json
%{mingw64_libdir}/qt6/metatypes/qt63dquickscene3d_relwithdebinfo_metatypes.json
%{mingw64_libdir}/qt6/mkspecs/modules/qt_lib_3dquick.pri
%{mingw64_libdir}/qt6/mkspecs/modules/qt_lib_3danimation.pri
%{mingw64_libdir}/qt6/mkspecs/modules/qt_lib_3danimation_private.pri
%{mingw64_libdir}/qt6/mkspecs/modules/qt_lib_3dcore.pri
%{mingw64_libdir}/qt6/mkspecs/modules/qt_lib_3dcore_private.pri
%{mingw64_libdir}/qt6/mkspecs/modules/qt_lib_3dextras.pri
%{mingw64_libdir}/qt6/mkspecs/modules/qt_lib_3dextras_private.pri
%{mingw64_libdir}/qt6/mkspecs/modules/qt_lib_3dinput.pri
%{mingw64_libdir}/qt6/mkspecs/modules/qt_lib_3dinput_private.pri
%{mingw64_libdir}/qt6/mkspecs/modules/qt_lib_3dlogic.pri
%{mingw64_libdir}/qt6/mkspecs/modules/qt_lib_3dlogic_private.pri
%{mingw64_libdir}/qt6/mkspecs/modules/qt_lib_3drender.pri
%{mingw64_libdir}/qt6/mkspecs/modules/qt_lib_3drender_private.pri
%{mingw64_libdir}/qt6/mkspecs/modules/qt_lib_3dquick_private.pri
%{mingw64_libdir}/qt6/mkspecs/modules/qt_lib_3dquickanimation.pri
%{mingw64_libdir}/qt6/mkspecs/modules/qt_lib_3dquickanimation_private.pri
%{mingw64_libdir}/qt6/mkspecs/modules/qt_lib_3dquickextras.pri
%{mingw64_libdir}/qt6/mkspecs/modules/qt_lib_3dquickextras_private.pri
%{mingw64_libdir}/qt6/mkspecs/modules/qt_lib_3dquickinput.pri
%{mingw64_libdir}/qt6/mkspecs/modules/qt_lib_3dquickinput_private.pri
%{mingw64_libdir}/qt6/mkspecs/modules/qt_lib_3dquickrender.pri
%{mingw64_libdir}/qt6/mkspecs/modules/qt_lib_3dquickrender_private.pri
%{mingw64_libdir}/qt6/mkspecs/modules/qt_lib_3dquickscene2d.pri
%{mingw64_libdir}/qt6/mkspecs/modules/qt_lib_3dquickscene2d_private.pri
%{mingw64_libdir}/qt6/mkspecs/modules/qt_lib_3dquickscene3d.pri
%{mingw64_libdir}/qt6/mkspecs/modules/qt_lib_3dquickscene3d_private.pri
%dir %{mingw64_libdir}/qt6/plugins/geometryloaders/
%{mingw64_libdir}/qt6/plugins/geometryloaders/defaultgeometryloader.dll
%{mingw64_libdir}/qt6/plugins/geometryloaders/gltfgeometryloader.dll
%dir %{mingw64_libdir}/qt6/plugins/renderers/
%{mingw64_libdir}/qt6/plugins/renderers/openglrenderer.dll
%{mingw64_libdir}/qt6/plugins/renderers/rhirenderer.dll
%dir %{mingw64_libdir}/qt6/plugins/renderplugins/
%{mingw64_libdir}/qt6/plugins/renderplugins/scene2d.dll
%dir %{mingw64_libdir}/qt6/plugins/sceneparsers/
%{mingw64_libdir}/qt6/plugins/sceneparsers/assimpsceneimport.dll
%{mingw64_libdir}/qt6/plugins/sceneparsers/gltfsceneexport.dll
%{mingw64_libdir}/qt6/plugins/sceneparsers/gltfsceneimport.dll
%{mingw64_libdir}/qt6/qml/Qt3D/
%{mingw64_libdir}/qt6/qml/QtQuick/Scene2D/
%{mingw64_libdir}/qt6/qml/QtQuick/Scene3D/
%{mingw64_libdir}/qt6/modules/3DAnimation.json
%{mingw64_libdir}/qt6/modules/3DCore.json
%{mingw64_libdir}/qt6/modules/3DExtras.json
%{mingw64_libdir}/qt6/modules/3DInput.json
%{mingw64_libdir}/qt6/modules/3DLogic.json
%{mingw64_libdir}/qt6/modules/3DRender.json
%{mingw64_libdir}/qt6/modules/3DQuick.json
%{mingw64_libdir}/qt6/modules/3DQuickAnimation.json
%{mingw64_libdir}/qt6/modules/3DQuickExtras.json
%{mingw64_libdir}/qt6/modules/3DQuickInput.json
%{mingw64_libdir}/qt6/modules/3DQuickRender.json
%{mingw64_libdir}/qt6/modules/3DQuickScene2D.json
%{mingw64_libdir}/qt6/modules/3DQuickScene3D.json
%{mingw64_libdir}/qt6/sbom/%{qt_module}-%{version}.spdx


%changelog
* Wed Feb 05 2025 Sandro Mani <manisandro@gmail.com> - 6.8.2-1
- Update to 6.8.2

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

* Mon Nov 01 2021 Sandro Mani <manisandro@gmail.com> - 6.2.1-1
- Update to 6.2.1

* Sun Oct 03 2021 Sandro Mani <manisandro@gmail.com> - 6.2.0-1
- Update to 6.2.0

* Mon Sep 27 2021 Sandro Mani <manisandro@gmail.com> - 6.2.0-0.2.rc2
- Update to 6.2.0-rc2

* Wed Sep 22 2021 Sandro Mani <manisandro@gmail.com> - 6.2.0-0.1.rc
- Update to 6.2.0-rc

* Fri Aug 27 2021 Sandro Mani <manisandro@gmail.com> - 6.1.2-1
- Update to 6.1.2

* Sun Jul 11 2021 Sandro Mani <manisandro@gmail.com> - 6.1.1-1
- Initial package
