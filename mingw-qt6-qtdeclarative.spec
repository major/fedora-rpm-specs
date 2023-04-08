%{?mingw_package_header}

# Disable debuginfo subpackages
%undefine _debugsource_packages

%global qt_module qtdeclarative
#global pre rc2

#global commit dd1d6b56271caf3f90e536b3ad9dab58c873f202
#global shortcommit %(c=%{commit}; echo ${c:0:7})

%if 0%{?commit:1}
%global source_folder %{qt_module}-%{commit}
%else
%global source_folder %{qt_module}-everywhere-src-%{version}%{?pre:-%{pre}}
%endif

# first two digits of version
%define release_version %(echo %{version} | awk -F. '{print $1"."$2}')

Name:           mingw-qt6-%{qt_module}
Version:        6.5.0
Release:        1%{?dist}
Summary:        Qt6 for Windows - QtDeclarative component

License:        LGPL-3.0-only OR GPL-2.0-only
URL:            http://qt.io/

%if 0%{?commit:1}
Source0:        https://github.com/qt/%{qt_module}/archive/%{commit}/%{qt_module}-everywhere-src-%{commit}.tar.gz
%else
Source0:        http://download.qt.io/%{?pre:development}%{?!pre:official}_releases/qt/%{release_version}/%{version}%{?pre:-%pre}/submodules/%{qt_module}-everywhere-src-%{version}%{?pre:-%pre}.tar.xz
%endif

# Add qt6 suffix to tools to avoid collision with qt5 tools
Patch0:         qtdeclarative-qt6-suffix.patch

# Upstream patches
Patch50:        d3d-retry-with-dxgi-adapter-flag-software-adapter-if-failed.patch

BuildRequires:  cmake
BuildRequires:  ninja-build
BuildRequires:  perl-interpreter
BuildRequires:  qt6-qtdeclarative-devel = %{version}%{?pre:~%pre}

BuildRequires:  mingw32-filesystem >= 96
BuildRequires:  mingw32-gcc-c++
BuildRequires:  mingw32-qt6-qtbase = %{version}
BuildRequires:  mingw32-qt6-qtshadertools = %{version}

BuildRequires:  mingw64-filesystem >= 96
BuildRequires:  mingw64-gcc-c++
BuildRequires:  mingw64-qt6-qtbase = %{version}
BuildRequires:  mingw64-qt6-qtshadertools = %{version}

%description
This package contains the Qt software toolkit for developing
cross-platform applications.

This is the Windows version of Qt, for use in conjunction with the
Fedora Windows cross-compiler.


# Win32
%package -n mingw32-qt6-%{qt_module}
Summary:        Qt6 for Windows - QtDeclarative component
# Dependency for host tools
Requires:       qt6-qtdeclarative-devel = %{version}%{?pre:~%pre}
Obsoletes:      mingw32-qt6-qtquickcontrols2 < 6.2.0-0.1.rc
Provides:       mingw32-qt6-qtquickcontrols2 = %{version}-%{release}
BuildArch:      noarch

%description -n mingw32-qt6-%{qt_module}
This package contains the Qt software toolkit for developing
cross-platform applications.

This is the 32-bit Windows version of Qt, for use in conjunction with the
Fedora Windows cross-compiler.


# Win64
%package -n mingw64-qt6-%{qt_module}
Summary:        Qt for Windows - QtDeclarative component
# Dependency for host tools
Requires:       qt6-qtdeclarative-devel = %{version}%{?pre:~%pre}
Obsoletes:      mingw64-qt6-qtquickcontrols2 < 6.2.0-0.1.rc
Provides:       mingw64-qt6-qtquickcontrols2 = %{version}-%{release}
BuildArch:      noarch

%description -n mingw64-qt6-%{qt_module}
This package contains the Qt software toolkit for developing
cross-platform applications.

This is the 64-bit Windows version of Qt, for use in conjunction with the
Fedora Windows cross-compiler.


%{?mingw_debug_package}


%prep
%autosetup -p1 -n %{source_folder}


%build
%ifarch ppc64le
# FIXME: ICE
export MINGW32_CFLAGS="%(echo %mingw32_cflags | sed 's/-O2/-O1/')"
export MINGW32_CXXFLAGS="%(echo %mingw32_cflags | sed 's/-O2/-O1/')"
export MINGW64_CFLAGS="%(echo %mingw64_cflags | sed 's/-O2/-O1/')"
export MINGW64_CXXFLAGS="%(echo %mingw64_cflags | sed 's/-O2/-O1/')"
%endif

%mingw_cmake -G Ninja -DCMAKE_BUILD_TYPE=RelWithDebInfo
%mingw_ninja


%install
%mingw_ninja_install

# Drop files which should probably have not been installed
rm -rf %{buildroot}%{mingw32_libdir}/objects-RelWithDebInfo/
rm -rf %{buildroot}%{mingw64_libdir}/objects-RelWithDebInfo/


# Win32
%files -n mingw32-qt6-%{qt_module}
%license LICENSES/*GPL*
%{mingw32_bindir}/qml-qt6.exe
%{mingw32_bindir}/qmleasing-qt6.exe
%{mingw32_bindir}/qmlpreview-qt6.exe
%{mingw32_bindir}/qmlscene-qt6.exe
%{mingw32_bindir}/Qt6LabsAnimation.dll
%{mingw32_bindir}/Qt6LabsFolderListModel.dll
%{mingw32_bindir}/Qt6LabsQmlModels.dll
%{mingw32_bindir}/Qt6LabsSettings.dll
%{mingw32_bindir}/Qt6LabsSharedImage.dll
%{mingw32_bindir}/Qt6LabsWavefrontMesh.dll
%{mingw32_bindir}/Qt6Qml.dll
%{mingw32_bindir}/Qt6QmlCompiler.dll
%{mingw32_bindir}/Qt6QmlCore.dll
%{mingw32_bindir}/Qt6QmlLocalStorage.dll
%{mingw32_bindir}/Qt6QmlModels.dll
%{mingw32_bindir}/Qt6QmlWorkerScript.dll
%{mingw32_bindir}/Qt6QmlXmlListModel.dll
%{mingw32_bindir}/Qt6Quick.dll
%{mingw32_bindir}/Qt6QuickControls2.dll
%{mingw32_bindir}/Qt6QuickControls2Impl.dll
%{mingw32_bindir}/Qt6QuickDialogs2.dll
%{mingw32_bindir}/Qt6QuickDialogs2QuickImpl.dll
%{mingw32_bindir}/Qt6QuickDialogs2Utils.dll
%{mingw32_bindir}/Qt6QuickEffects.dll
%{mingw32_bindir}/Qt6QuickLayouts.dll
%{mingw32_bindir}/Qt6QuickParticles.dll
%{mingw32_bindir}/Qt6QuickShapes.dll
%{mingw32_bindir}/Qt6QuickTemplates2.dll
%{mingw32_bindir}/Qt6QuickTest.dll
%{mingw32_bindir}/Qt6QuickWidgets.dll

%{mingw32_includedir}/qt6/QtLabsAnimation/
%{mingw32_includedir}/qt6/QtLabsFolderListModel/
%{mingw32_includedir}/qt6/QtLabsQmlModels/
%{mingw32_includedir}/qt6/QtLabsSettings/
%{mingw32_includedir}/qt6/QtLabsSharedImage/
%{mingw32_includedir}/qt6/QtLabsWavefrontMesh/
%{mingw32_includedir}/qt6/QtPacketProtocol/
%{mingw32_includedir}/qt6/QtQml/
%{mingw32_includedir}/qt6/QtQmlCompiler/
%{mingw32_includedir}/qt6/QtQmlCore/
%{mingw32_includedir}/qt6/QtQmlDebug/
%{mingw32_includedir}/qt6/QtQmlDom/
%{mingw32_includedir}/qt6/QtQmlIntegration/
%{mingw32_includedir}/qt6/QtQmlLocalStorage/
%{mingw32_includedir}/qt6/QtQmlModels/
%{mingw32_includedir}/qt6/QtQmlTypeRegistrar/
%{mingw32_includedir}/qt6/QtQmlWorkerScript/
%{mingw32_includedir}/qt6/QtQmlXmlListModel/
%{mingw32_includedir}/qt6/QtQuick/
%{mingw32_includedir}/qt6/QtQuickControls2/
%{mingw32_includedir}/qt6/QtQuickControls2Impl/
%{mingw32_includedir}/qt6/QtQuickControlsTestUtils
%{mingw32_includedir}/qt6/QtQuickDialogs2/
%{mingw32_includedir}/qt6/QtQuickDialogs2QuickImpl/
%{mingw32_includedir}/qt6/QtQuickDialogs2Utils/
%{mingw32_includedir}/qt6/QtQuickEffects/
%{mingw32_includedir}/qt6/QtQuickLayouts/
%{mingw32_includedir}/qt6/QtQuickParticles/
%{mingw32_includedir}/qt6/QtQuickShapes/
%{mingw32_includedir}/qt6/QtQuickTemplates2/
%{mingw32_includedir}/qt6/QtQuickTest/
%{mingw32_includedir}/qt6/QtQuickTestUtils/
%{mingw32_includedir}/qt6/QtQuickWidgets/

%{mingw32_libdir}/cmake/Qt6BuildInternals/StandaloneTests/QtDeclarativeTestsConfig.cmake
%{mingw32_libdir}/cmake/Qt6LabsAnimation/
%{mingw32_libdir}/cmake/Qt6LabsFolderListModel/
%{mingw32_libdir}/cmake/Qt6LabsQmlModels/
%{mingw32_libdir}/cmake/Qt6LabsSettings/
%{mingw32_libdir}/cmake/Qt6LabsSharedImage/
%{mingw32_libdir}/cmake/Qt6LabsWavefrontMesh/
%{mingw32_libdir}/cmake/Qt6PacketProtocolPrivate/
%{mingw32_libdir}/cmake/Qt6Qml/
%{mingw32_libdir}/cmake/Qt6QmlCompilerPrivate/
%{mingw32_libdir}/cmake/Qt6QmlCore/
%{mingw32_libdir}/cmake/Qt6QmlDebugPrivate/
%{mingw32_libdir}/cmake/Qt6QmlIntegration/
%{mingw32_libdir}/cmake/Qt6QmlDomPrivate/
%{mingw32_libdir}/cmake/Qt6QmlLocalStorage/
%{mingw32_libdir}/cmake/Qt6QmlModels/
%{mingw32_libdir}/cmake/Qt6QmlTypeRegistrarPrivate/
%{mingw32_libdir}/cmake/Qt6QmlWorkerScript/
%{mingw32_libdir}/cmake/Qt6QmlXmlListModel/
%{mingw32_libdir}/cmake/Qt6Quick/
%{mingw32_libdir}/cmake/Qt6QuickControls2/
%{mingw32_libdir}/cmake/Qt6QuickControls2Impl/
%{mingw32_libdir}/cmake/Qt6QuickControlsTestUtilsPrivate/
%{mingw32_libdir}/cmake/Qt6QuickDialogs2/
%{mingw32_libdir}/cmake/Qt6QuickDialogs2QuickImpl/
%{mingw32_libdir}/cmake/Qt6QuickDialogs2Utils/
%{mingw32_libdir}/cmake/Qt6QuickEffectsPrivate/
%{mingw32_libdir}/cmake/Qt6QuickLayouts/
%{mingw32_libdir}/cmake/Qt6QuickParticlesPrivate/
%{mingw32_libdir}/cmake/Qt6QuickShapesPrivate/
%{mingw32_libdir}/cmake/Qt6QuickTemplates2/
%{mingw32_libdir}/cmake/Qt6QuickTest/
%{mingw32_libdir}/cmake/Qt6QuickTestUtilsPrivate/
%{mingw32_libdir}/cmake/Qt6QuickWidgets/

%{mingw32_libdir}/pkgconfig/Qt6LabsAnimation.pc
%{mingw32_libdir}/pkgconfig/Qt6LabsFolderListModel.pc
%{mingw32_libdir}/pkgconfig/Qt6LabsQmlModels.pc
%{mingw32_libdir}/pkgconfig/Qt6LabsSettings.pc
%{mingw32_libdir}/pkgconfig/Qt6LabsSharedImage.pc
%{mingw32_libdir}/pkgconfig/Qt6LabsWavefrontMesh.pc
%{mingw32_libdir}/pkgconfig/Qt6Qml.pc
%{mingw32_libdir}/pkgconfig/Qt6QmlCore.pc
%{mingw32_libdir}/pkgconfig/Qt6QmlIntegration.pc
%{mingw32_libdir}/pkgconfig/Qt6QmlLocalStorage.pc
%{mingw32_libdir}/pkgconfig/Qt6QmlModels.pc
%{mingw32_libdir}/pkgconfig/Qt6QmlWorkerScript.pc
%{mingw32_libdir}/pkgconfig/Qt6QmlXmlListModel.pc
%{mingw32_libdir}/pkgconfig/Qt6Quick.pc
%{mingw32_libdir}/pkgconfig/Qt6QuickControls2.pc
%{mingw32_libdir}/pkgconfig/Qt6QuickControls2Impl.pc
%{mingw32_libdir}/pkgconfig/Qt6QuickDialogs2.pc
%{mingw32_libdir}/pkgconfig/Qt6QuickDialogs2QuickImpl.pc
%{mingw32_libdir}/pkgconfig/Qt6QuickDialogs2Utils.pc
%{mingw32_libdir}/pkgconfig/Qt6QuickLayouts.pc
%{mingw32_libdir}/pkgconfig/Qt6QuickTemplates2.pc
%{mingw32_libdir}/pkgconfig/Qt6QuickTest.pc
%{mingw32_libdir}/pkgconfig/Qt6QuickWidgets.pc

%{mingw32_libdir}/libQt6LabsAnimation.dll.a
%{mingw32_libdir}/libQt6LabsFolderListModel.dll.a
%{mingw32_libdir}/libQt6LabsQmlModels.dll.a
%{mingw32_libdir}/libQt6LabsSettings.dll.a
%{mingw32_libdir}/libQt6LabsSharedImage.dll.a
%{mingw32_libdir}/libQt6LabsWavefrontMesh.dll.a
%{mingw32_libdir}/libQt6PacketProtocol.a
%{mingw32_libdir}/libQt6QmlDebug.a
%{mingw32_libdir}/libQt6Qml.dll.a
%{mingw32_libdir}/libQt6QmlCompiler.dll.a
%{mingw32_libdir}/libQt6QmlCore.dll.a
%{mingw32_libdir}/libQt6QmlDom.a
%{mingw32_libdir}/libQt6QmlLocalStorage.dll.a
%{mingw32_libdir}/libQt6QmlModels.dll.a
%{mingw32_libdir}/libQt6QmlTypeRegistrar.a
%{mingw32_libdir}/libQt6QmlWorkerScript.dll.a
%{mingw32_libdir}/libQt6QmlXmlListModel.dll.a
%{mingw32_libdir}/libQt6Quick.dll.a
%{mingw32_libdir}/libQt6QuickControls2.dll.a
%{mingw32_libdir}/libQt6QuickControls2Impl.dll.a
%{mingw32_libdir}/libQt6QuickControlsTestUtils.a
%{mingw32_libdir}/libQt6QuickDialogs2.dll.a
%{mingw32_libdir}/libQt6QuickDialogs2QuickImpl.dll.a
%{mingw32_libdir}/libQt6QuickDialogs2Utils.dll.a
%{mingw32_libdir}/libQt6QuickEffects.dll.a
%{mingw32_libdir}/libQt6QuickLayouts.dll.a
%{mingw32_libdir}/libQt6QuickParticles.dll.a
%{mingw32_libdir}/libQt6QuickShapes.dll.a
%{mingw32_libdir}/libQt6QuickTemplates2.dll.a
%{mingw32_libdir}/libQt6QuickTest.dll.a
%{mingw32_libdir}/libQt6QuickTestUtils.a
%{mingw32_libdir}/libQt6QuickWidgets.dll.a

%{mingw32_libdir}/qt6/metatypes/qt6labsanimation_relwithdebinfo_metatypes.json
%{mingw32_libdir}/qt6/metatypes/qt6labsfolderlistmodel_relwithdebinfo_metatypes.json
%{mingw32_libdir}/qt6/metatypes/qt6labsqmlmodels_relwithdebinfo_metatypes.json
%{mingw32_libdir}/qt6/metatypes/qt6labssettings_relwithdebinfo_metatypes.json
%{mingw32_libdir}/qt6/metatypes/qt6labssharedimage_relwithdebinfo_metatypes.json
%{mingw32_libdir}/qt6/metatypes/qt6labswavefrontmesh_relwithdebinfo_metatypes.json
%{mingw32_libdir}/qt6/metatypes/qt6packetprotocolprivate_relwithdebinfo_metatypes.json
%{mingw32_libdir}/qt6/metatypes/qt6qml_relwithdebinfo_metatypes.json
%{mingw32_libdir}/qt6/metatypes/qt6qmlcompilerprivate_relwithdebinfo_metatypes.json
%{mingw32_libdir}/qt6/metatypes/qt6qmlcore_relwithdebinfo_metatypes.json
%{mingw32_libdir}/qt6/metatypes/qt6qmldebugprivate_relwithdebinfo_metatypes.json
%{mingw32_libdir}/qt6/metatypes/qt6qmldomprivate_relwithdebinfo_metatypes.json
%{mingw32_libdir}/qt6/metatypes/qt6qmllocalstorage_relwithdebinfo_metatypes.json
%{mingw32_libdir}/qt6/metatypes/qt6qmlmodels_relwithdebinfo_metatypes.json
%{mingw32_libdir}/qt6/metatypes/qt6qmltyperegistrarprivate_relwithdebinfo_metatypes.json
%{mingw32_libdir}/qt6/metatypes/qt6qmlworkerscript_relwithdebinfo_metatypes.json
%{mingw32_libdir}/qt6/metatypes/qt6qmlxmllistmodel_relwithdebinfo_metatypes.json
%{mingw32_libdir}/qt6/metatypes/qt6quick_relwithdebinfo_metatypes.json
%{mingw32_libdir}/qt6/metatypes/qt6quickcontrols2_relwithdebinfo_metatypes.json
%{mingw32_libdir}/qt6/metatypes/qt6quickcontrols2impl_relwithdebinfo_metatypes.json
%{mingw32_libdir}/qt6/metatypes/qt6quickcontrolstestutilsprivate_relwithdebinfo_metatypes.json
%{mingw32_libdir}/qt6/metatypes/qt6quickdialogs2_relwithdebinfo_metatypes.json
%{mingw32_libdir}/qt6/metatypes/qt6quickdialogs2quickimpl_relwithdebinfo_metatypes.json
%{mingw32_libdir}/qt6/metatypes/qt6quickdialogs2utils_relwithdebinfo_metatypes.json
%{mingw32_libdir}/qt6/metatypes/qt6quickeffectsprivate_relwithdebinfo_metatypes.json
%{mingw32_libdir}/qt6/metatypes/qt6quicklayouts_relwithdebinfo_metatypes.json
%{mingw32_libdir}/qt6/metatypes/qt6quickparticlesprivate_relwithdebinfo_metatypes.json
%{mingw32_libdir}/qt6/metatypes/qt6quickshapesprivate_relwithdebinfo_metatypes.json
%{mingw32_libdir}/qt6/metatypes/qt6quicktemplates2_relwithdebinfo_metatypes.json
%{mingw32_libdir}/qt6/metatypes/qt6quicktest_relwithdebinfo_metatypes.json
%{mingw32_libdir}/qt6/metatypes/qt6quicktestutilsprivate_relwithdebinfo_metatypes.json
%{mingw32_libdir}/qt6/metatypes/qt6quickwidgets_relwithdebinfo_metatypes.json

%{mingw32_libdir}/Qt6LabsAnimation.prl
%{mingw32_libdir}/Qt6LabsFolderListModel.prl
%{mingw32_libdir}/Qt6LabsQmlModels.prl
%{mingw32_libdir}/Qt6LabsSettings.prl
%{mingw32_libdir}/Qt6LabsSharedImage.prl
%{mingw32_libdir}/Qt6LabsWavefrontMesh.prl
%{mingw32_libdir}/Qt6Qml.prl
%{mingw32_libdir}/Qt6QmlCompiler.prl
%{mingw32_libdir}/Qt6QmlCore.prl
%{mingw32_libdir}/Qt6QmlDebug.prl
%{mingw32_libdir}/Qt6QmlDom.prl
%{mingw32_libdir}/Qt6QmlLocalStorage.prl
%{mingw32_libdir}/Qt6QmlModels.prl
%{mingw32_libdir}/Qt6QmlTypeRegistrar.prl
%{mingw32_libdir}/Qt6QmlWorkerScript.prl
%{mingw32_libdir}/Qt6QmlXmlListModel.prl
%{mingw32_libdir}/Qt6Quick.prl
%{mingw32_libdir}/Qt6QuickControls2.prl
%{mingw32_libdir}/Qt6QuickControls2Impl.prl
%{mingw32_libdir}/Qt6QuickControlsTestUtils.prl
%{mingw32_libdir}/Qt6QuickDialogs2.prl
%{mingw32_libdir}/Qt6QuickDialogs2QuickImpl.prl
%{mingw32_libdir}/Qt6QuickDialogs2Utils.prl
%{mingw32_libdir}/Qt6QuickEffects.prl
%{mingw32_libdir}/Qt6QuickLayouts.prl
%{mingw32_libdir}/Qt6QuickParticles.prl
%{mingw32_libdir}/Qt6QuickShapes.prl
%{mingw32_libdir}/Qt6QuickTemplates2.prl
%{mingw32_libdir}/Qt6QuickTest.prl
%{mingw32_libdir}/Qt6QuickTestUtils.prl
%{mingw32_libdir}/Qt6QuickWidgets.prl

%{mingw32_libdir}/Qt6PacketProtocol.prl
%{mingw32_libdir}/qt6/mkspecs/features/qmltypes.prf
%{mingw32_libdir}/qt6/mkspecs/modules/qt_lib_labsanimation.pri
%{mingw32_libdir}/qt6/mkspecs/modules/qt_lib_labsanimation_private.pri
%{mingw32_libdir}/qt6/mkspecs/modules/qt_lib_labsfolderlistmodel.pri
%{mingw32_libdir}/qt6/mkspecs/modules/qt_lib_labsfolderlistmodel_private.pri
%{mingw32_libdir}/qt6/mkspecs/modules/qt_lib_labsqmlmodels.pri
%{mingw32_libdir}/qt6/mkspecs/modules/qt_lib_labsqmlmodels_private.pri
%{mingw32_libdir}/qt6/mkspecs/modules/qt_lib_labssettings.pri
%{mingw32_libdir}/qt6/mkspecs/modules/qt_lib_labssettings_private.pri
%{mingw32_libdir}/qt6/mkspecs/modules/qt_lib_labssharedimage.pri
%{mingw32_libdir}/qt6/mkspecs/modules/qt_lib_labssharedimage_private.pri
%{mingw32_libdir}/qt6/mkspecs/modules/qt_lib_labswavefrontmesh.pri
%{mingw32_libdir}/qt6/mkspecs/modules/qt_lib_labswavefrontmesh_private.pri
%{mingw32_libdir}/qt6/mkspecs/modules/qt_lib_packetprotocol_private.pri
%{mingw32_libdir}/qt6/mkspecs/modules/qt_lib_qml.pri
%{mingw32_libdir}/qt6/mkspecs/modules/qt_lib_qml_private.pri
%{mingw32_libdir}/qt6/mkspecs/modules/qt_lib_qmlcompiler_private.pri
%{mingw32_libdir}/qt6/mkspecs/modules/qt_lib_qmlcore.pri
%{mingw32_libdir}/qt6/mkspecs/modules/qt_lib_qmlcore_private.pri
%{mingw32_libdir}/qt6/mkspecs/modules/qt_lib_qmldebug_private.pri
%{mingw32_libdir}/qt6/mkspecs/modules/qt_lib_qmldom_private.pri
%{mingw32_libdir}/qt6/mkspecs/modules/qt_lib_qmlintegration.pri
%{mingw32_libdir}/qt6/mkspecs/modules/qt_lib_qmlintegration_private.pri
%{mingw32_libdir}/qt6/mkspecs/modules/qt_lib_qmllocalstorage.pri
%{mingw32_libdir}/qt6/mkspecs/modules/qt_lib_qmllocalstorage_private.pri
%{mingw32_libdir}/qt6/mkspecs/modules/qt_lib_qmlmodels.pri
%{mingw32_libdir}/qt6/mkspecs/modules/qt_lib_qmlmodels_private.pri
%{mingw32_libdir}/qt6/mkspecs/modules/qt_lib_qmltest.pri
%{mingw32_libdir}/qt6/mkspecs/modules/qt_lib_qmltest_private.pri
%{mingw32_libdir}/qt6/mkspecs/modules/qt_lib_qmltyperegistrar_private.pri
%{mingw32_libdir}/qt6/mkspecs/modules/qt_lib_qmlworkerscript.pri
%{mingw32_libdir}/qt6/mkspecs/modules/qt_lib_qmlworkerscript_private.pri
%{mingw32_libdir}/qt6/mkspecs/modules/qt_lib_qmlxmllistmodel.pri
%{mingw32_libdir}/qt6/mkspecs/modules/qt_lib_qmlxmllistmodel_private.pri
%{mingw32_libdir}/qt6/mkspecs/modules/qt_lib_quick.pri
%{mingw32_libdir}/qt6/mkspecs/modules/qt_lib_quick_private.pri
%{mingw32_libdir}/qt6/mkspecs/modules/qt_lib_quickcontrols2.pri
%{mingw32_libdir}/qt6/mkspecs/modules/qt_lib_quickcontrols2_private.pri
%{mingw32_libdir}/qt6/mkspecs/modules/qt_lib_quickcontrols2impl.pri
%{mingw32_libdir}/qt6/mkspecs/modules/qt_lib_quickcontrols2impl_private.pri
%{mingw32_libdir}/qt6/mkspecs/modules/qt_lib_quickcontrolstestutilsprivate_private.pri
%{mingw32_libdir}/qt6/mkspecs/modules/qt_lib_quickdialogs2.pri
%{mingw32_libdir}/qt6/mkspecs/modules/qt_lib_quickdialogs2_private.pri
%{mingw32_libdir}/qt6/mkspecs/modules/qt_lib_quickdialogs2quickimpl.pri
%{mingw32_libdir}/qt6/mkspecs/modules/qt_lib_quickdialogs2quickimpl_private.pri
%{mingw32_libdir}/qt6/mkspecs/modules/qt_lib_quickdialogs2utils.pri
%{mingw32_libdir}/qt6/mkspecs/modules/qt_lib_quickdialogs2utils_private.pri
%{mingw32_libdir}/qt6/mkspecs/modules/qt_lib_quickeffects_private.pri
%{mingw32_libdir}/qt6/mkspecs/modules/qt_lib_quicklayouts.pri
%{mingw32_libdir}/qt6/mkspecs/modules/qt_lib_quicklayouts_private.pri
%{mingw32_libdir}/qt6/mkspecs/modules/qt_lib_quickparticles_private.pri
%{mingw32_libdir}/qt6/mkspecs/modules/qt_lib_quickshapes_private.pri
%{mingw32_libdir}/qt6/mkspecs/modules/qt_lib_quicktemplates2.pri
%{mingw32_libdir}/qt6/mkspecs/modules/qt_lib_quicktemplates2_private.pri
%{mingw32_libdir}/qt6/mkspecs/modules/qt_lib_quicktestutilsprivate_private.pri
%{mingw32_libdir}/qt6/mkspecs/modules/qt_lib_quickwidgets.pri
%{mingw32_libdir}/qt6/mkspecs/modules/qt_lib_quickwidgets_private.pri

%{mingw32_libdir}/qt6/plugins/qmllint/
%{mingw32_libdir}/qt6/plugins/qmltooling/

%dir %{mingw32_libdir}/qt6/qml/
%{mingw32_libdir}/qt6/qml/builtins.qmltypes
%{mingw32_libdir}/qt6/qml/jsroot.qmltypes
%dir %{mingw32_libdir}/qt6/qml/Qt/
%dir %{mingw32_libdir}/qt6/qml/Qt/labs/
%{mingw32_libdir}/qt6/qml/Qt/labs/animation/
%{mingw32_libdir}/qt6/qml/Qt/labs/folderlistmodel
%{mingw32_libdir}/qt6/qml/Qt/labs/platform/
%{mingw32_libdir}/qt6/qml/Qt/labs/qmlmodels
%{mingw32_libdir}/qt6/qml/Qt/labs/settings
%{mingw32_libdir}/qt6/qml/Qt/labs/sharedimage/
%{mingw32_libdir}/qt6/qml/Qt/labs/wavefrontmesh/
%dir %{mingw32_libdir}/qt6/qml/Qt/test/
%{mingw32_libdir}/qt6/qml/Qt/test/controls/
%{mingw32_libdir}/qt6/qml/QtCore/
%{mingw32_libdir}/qt6/qml/QtQml/
%{mingw32_libdir}/qt6/qml/QtQuick/
%{mingw32_libdir}/qt6/qml/QtTest/

%{mingw32_libdir}/qt6/modules/LabsAnimation.json
%{mingw32_libdir}/qt6/modules/LabsFolderListModel.json
%{mingw32_libdir}/qt6/modules/LabsQmlModels.json
%{mingw32_libdir}/qt6/modules/LabsSettings.json
%{mingw32_libdir}/qt6/modules/LabsSharedImage.json
%{mingw32_libdir}/qt6/modules/LabsWavefrontMesh.json
%{mingw32_libdir}/qt6/modules/PacketProtocolPrivate.json
%{mingw32_libdir}/qt6/modules/Qml.json
%{mingw32_libdir}/qt6/modules/QmlCompilerPrivate.json
%{mingw32_libdir}/qt6/modules/QmlCore.json
%{mingw32_libdir}/qt6/modules/QmlDebugPrivate.json
%{mingw32_libdir}/qt6/modules/QmlDomPrivate.json
%{mingw32_libdir}/qt6/modules/QmlIntegration.json
%{mingw32_libdir}/qt6/modules/QmlLocalStorage.json
%{mingw32_libdir}/qt6/modules/QmlModels.json
%{mingw32_libdir}/qt6/modules/QmlTypeRegistrarPrivate.json
%{mingw32_libdir}/qt6/modules/QmlWorkerScript.json
%{mingw32_libdir}/qt6/modules/QmlXmlListModel.json
%{mingw32_libdir}/qt6/modules/Quick.json
%{mingw32_libdir}/qt6/modules/QuickControls2.json
%{mingw32_libdir}/qt6/modules/QuickControls2Impl.json
%{mingw32_libdir}/qt6/modules/QuickControlsTestUtilsPrivate.json
%{mingw32_libdir}/qt6/modules/QuickDialogs2.json
%{mingw32_libdir}/qt6/modules/QuickDialogs2QuickImpl.json
%{mingw32_libdir}/qt6/modules/QuickDialogs2Utils.json
%{mingw32_libdir}/qt6/modules/QuickEffectsPrivate.json
%{mingw32_libdir}/qt6/modules/QuickLayouts.json
%{mingw32_libdir}/qt6/modules/QuickParticlesPrivate.json
%{mingw32_libdir}/qt6/modules/QuickShapesPrivate.json
%{mingw32_libdir}/qt6/modules/QuickTemplates2.json
%{mingw32_libdir}/qt6/modules/QuickTest.json
%{mingw32_libdir}/qt6/modules/QuickTestUtilsPrivate.json
%{mingw32_libdir}/qt6/modules/QuickWidgets.json


# Win64
%files -n mingw64-qt6-%{qt_module}
%license LICENSES/*GPL*
%{mingw64_bindir}/qml-qt6.exe
%{mingw64_bindir}/qmleasing-qt6.exe
%{mingw64_bindir}/qmlpreview-qt6.exe
%{mingw64_bindir}/qmlscene-qt6.exe
%{mingw64_bindir}/Qt6LabsAnimation.dll
%{mingw64_bindir}/Qt6LabsFolderListModel.dll
%{mingw64_bindir}/Qt6LabsQmlModels.dll
%{mingw64_bindir}/Qt6LabsSettings.dll
%{mingw64_bindir}/Qt6LabsSharedImage.dll
%{mingw64_bindir}/Qt6LabsWavefrontMesh.dll
%{mingw64_bindir}/Qt6Qml.dll
%{mingw64_bindir}/Qt6QmlCompiler.dll
%{mingw64_bindir}/Qt6QmlCore.dll
%{mingw64_bindir}/Qt6QmlLocalStorage.dll
%{mingw64_bindir}/Qt6QmlModels.dll
%{mingw64_bindir}/Qt6QmlWorkerScript.dll
%{mingw64_bindir}/Qt6QmlXmlListModel.dll
%{mingw64_bindir}/Qt6Quick.dll
%{mingw64_bindir}/Qt6QuickControls2.dll
%{mingw64_bindir}/Qt6QuickControls2Impl.dll
%{mingw64_bindir}/Qt6QuickDialogs2.dll
%{mingw64_bindir}/Qt6QuickDialogs2QuickImpl.dll
%{mingw64_bindir}/Qt6QuickDialogs2Utils.dll
%{mingw64_bindir}/Qt6QuickEffects.dll
%{mingw64_bindir}/Qt6QuickLayouts.dll
%{mingw64_bindir}/Qt6QuickParticles.dll
%{mingw64_bindir}/Qt6QuickShapes.dll
%{mingw64_bindir}/Qt6QuickTemplates2.dll
%{mingw64_bindir}/Qt6QuickTest.dll
%{mingw64_bindir}/Qt6QuickWidgets.dll

%{mingw64_includedir}/qt6/QtLabsAnimation/
%{mingw64_includedir}/qt6/QtLabsFolderListModel/
%{mingw64_includedir}/qt6/QtLabsQmlModels/
%{mingw64_includedir}/qt6/QtLabsSettings/
%{mingw64_includedir}/qt6/QtLabsSharedImage/
%{mingw64_includedir}/qt6/QtLabsWavefrontMesh/
%{mingw64_includedir}/qt6/QtPacketProtocol/
%{mingw64_includedir}/qt6/QtQml/
%{mingw64_includedir}/qt6/QtQmlCompiler/
%{mingw64_includedir}/qt6/QtQmlCore/
%{mingw64_includedir}/qt6/QtQmlDebug/
%{mingw64_includedir}/qt6/QtQmlDom/
%{mingw64_includedir}/qt6/QtQmlIntegration/
%{mingw64_includedir}/qt6/QtQmlLocalStorage/
%{mingw64_includedir}/qt6/QtQmlModels/
%{mingw64_includedir}/qt6/QtQmlTypeRegistrar/
%{mingw64_includedir}/qt6/QtQmlWorkerScript/
%{mingw64_includedir}/qt6/QtQmlXmlListModel/
%{mingw64_includedir}/qt6/QtQuick/
%{mingw64_includedir}/qt6/QtQuickControls2/
%{mingw64_includedir}/qt6/QtQuickControls2Impl/
%{mingw64_includedir}/qt6/QtQuickControlsTestUtils
%{mingw64_includedir}/qt6/QtQuickDialogs2/
%{mingw64_includedir}/qt6/QtQuickDialogs2QuickImpl/
%{mingw64_includedir}/qt6/QtQuickDialogs2Utils/
%{mingw64_includedir}/qt6/QtQuickEffects/
%{mingw64_includedir}/qt6/QtQuickLayouts/
%{mingw64_includedir}/qt6/QtQuickParticles/
%{mingw64_includedir}/qt6/QtQuickShapes/
%{mingw64_includedir}/qt6/QtQuickTemplates2/
%{mingw64_includedir}/qt6/QtQuickTest/
%{mingw64_includedir}/qt6/QtQuickTestUtils/
%{mingw64_includedir}/qt6/QtQuickWidgets/

%{mingw64_libdir}/cmake/Qt6BuildInternals/StandaloneTests/QtDeclarativeTestsConfig.cmake
%{mingw64_libdir}/cmake/Qt6LabsAnimation/
%{mingw64_libdir}/cmake/Qt6LabsFolderListModel/
%{mingw64_libdir}/cmake/Qt6LabsQmlModels/
%{mingw64_libdir}/cmake/Qt6LabsSettings/
%{mingw64_libdir}/cmake/Qt6LabsSharedImage/
%{mingw64_libdir}/cmake/Qt6LabsWavefrontMesh/
%{mingw64_libdir}/cmake/Qt6PacketProtocolPrivate/
%{mingw64_libdir}/cmake/Qt6Qml/
%{mingw64_libdir}/cmake/Qt6QmlCompilerPrivate/
%{mingw64_libdir}/cmake/Qt6QmlCore/
%{mingw64_libdir}/cmake/Qt6QmlDebugPrivate/
%{mingw64_libdir}/cmake/Qt6QmlIntegration/
%{mingw64_libdir}/cmake/Qt6QmlDomPrivate/
%{mingw64_libdir}/cmake/Qt6QmlLocalStorage/
%{mingw64_libdir}/cmake/Qt6QmlModels/
%{mingw64_libdir}/cmake/Qt6QmlTypeRegistrarPrivate/
%{mingw64_libdir}/cmake/Qt6QmlWorkerScript/
%{mingw64_libdir}/cmake/Qt6QmlXmlListModel/
%{mingw64_libdir}/cmake/Qt6Quick/
%{mingw64_libdir}/cmake/Qt6QuickControls2/
%{mingw64_libdir}/cmake/Qt6QuickControls2Impl/
%{mingw64_libdir}/cmake/Qt6QuickControlsTestUtilsPrivate/
%{mingw64_libdir}/cmake/Qt6QuickDialogs2/
%{mingw64_libdir}/cmake/Qt6QuickDialogs2QuickImpl/
%{mingw64_libdir}/cmake/Qt6QuickDialogs2Utils/
%{mingw64_libdir}/cmake/Qt6QuickEffectsPrivate/
%{mingw64_libdir}/cmake/Qt6QuickLayouts/
%{mingw64_libdir}/cmake/Qt6QuickParticlesPrivate/
%{mingw64_libdir}/cmake/Qt6QuickShapesPrivate/
%{mingw64_libdir}/cmake/Qt6QuickTemplates2/
%{mingw64_libdir}/cmake/Qt6QuickTest/
%{mingw64_libdir}/cmake/Qt6QuickTestUtilsPrivate/
%{mingw64_libdir}/cmake/Qt6QuickWidgets/

%{mingw64_libdir}/pkgconfig/Qt6LabsAnimation.pc
%{mingw64_libdir}/pkgconfig/Qt6LabsFolderListModel.pc
%{mingw64_libdir}/pkgconfig/Qt6LabsQmlModels.pc
%{mingw64_libdir}/pkgconfig/Qt6LabsSettings.pc
%{mingw64_libdir}/pkgconfig/Qt6LabsSharedImage.pc
%{mingw64_libdir}/pkgconfig/Qt6LabsWavefrontMesh.pc
%{mingw64_libdir}/pkgconfig/Qt6Qml.pc
%{mingw64_libdir}/pkgconfig/Qt6QmlCore.pc
%{mingw64_libdir}/pkgconfig/Qt6QmlIntegration.pc
%{mingw64_libdir}/pkgconfig/Qt6QmlLocalStorage.pc
%{mingw64_libdir}/pkgconfig/Qt6QmlModels.pc
%{mingw64_libdir}/pkgconfig/Qt6QmlWorkerScript.pc
%{mingw64_libdir}/pkgconfig/Qt6QmlXmlListModel.pc
%{mingw64_libdir}/pkgconfig/Qt6Quick.pc
%{mingw64_libdir}/pkgconfig/Qt6QuickControls2.pc
%{mingw64_libdir}/pkgconfig/Qt6QuickControls2Impl.pc
%{mingw64_libdir}/pkgconfig/Qt6QuickDialogs2.pc
%{mingw64_libdir}/pkgconfig/Qt6QuickDialogs2QuickImpl.pc
%{mingw64_libdir}/pkgconfig/Qt6QuickDialogs2Utils.pc
%{mingw64_libdir}/pkgconfig/Qt6QuickLayouts.pc
%{mingw64_libdir}/pkgconfig/Qt6QuickTemplates2.pc
%{mingw64_libdir}/pkgconfig/Qt6QuickTest.pc
%{mingw64_libdir}/pkgconfig/Qt6QuickWidgets.pc

%{mingw64_libdir}/libQt6LabsAnimation.dll.a
%{mingw64_libdir}/libQt6LabsFolderListModel.dll.a
%{mingw64_libdir}/libQt6LabsQmlModels.dll.a
%{mingw64_libdir}/libQt6LabsSettings.dll.a
%{mingw64_libdir}/libQt6LabsSharedImage.dll.a
%{mingw64_libdir}/libQt6LabsWavefrontMesh.dll.a
%{mingw64_libdir}/libQt6PacketProtocol.a
%{mingw64_libdir}/libQt6QmlDebug.a
%{mingw64_libdir}/libQt6Qml.dll.a
%{mingw64_libdir}/libQt6QmlCompiler.dll.a
%{mingw64_libdir}/libQt6QmlCore.dll.a
%{mingw64_libdir}/libQt6QmlDom.a
%{mingw64_libdir}/libQt6QmlLocalStorage.dll.a
%{mingw64_libdir}/libQt6QmlModels.dll.a
%{mingw64_libdir}/libQt6QmlTypeRegistrar.a
%{mingw64_libdir}/libQt6QmlWorkerScript.dll.a
%{mingw64_libdir}/libQt6QmlXmlListModel.dll.a
%{mingw64_libdir}/libQt6Quick.dll.a
%{mingw64_libdir}/libQt6QuickControls2.dll.a
%{mingw64_libdir}/libQt6QuickControls2Impl.dll.a
%{mingw64_libdir}/libQt6QuickControlsTestUtils.a
%{mingw64_libdir}/libQt6QuickDialogs2.dll.a
%{mingw64_libdir}/libQt6QuickDialogs2QuickImpl.dll.a
%{mingw64_libdir}/libQt6QuickDialogs2Utils.dll.a
%{mingw64_libdir}/libQt6QuickEffects.dll.a
%{mingw64_libdir}/libQt6QuickLayouts.dll.a
%{mingw64_libdir}/libQt6QuickParticles.dll.a
%{mingw64_libdir}/libQt6QuickShapes.dll.a
%{mingw64_libdir}/libQt6QuickTemplates2.dll.a
%{mingw64_libdir}/libQt6QuickTest.dll.a
%{mingw64_libdir}/libQt6QuickTestUtils.a
%{mingw64_libdir}/libQt6QuickWidgets.dll.a

%{mingw64_libdir}/qt6/metatypes/qt6labsanimation_relwithdebinfo_metatypes.json
%{mingw64_libdir}/qt6/metatypes/qt6labsfolderlistmodel_relwithdebinfo_metatypes.json
%{mingw64_libdir}/qt6/metatypes/qt6labsqmlmodels_relwithdebinfo_metatypes.json
%{mingw64_libdir}/qt6/metatypes/qt6labssettings_relwithdebinfo_metatypes.json
%{mingw64_libdir}/qt6/metatypes/qt6labssharedimage_relwithdebinfo_metatypes.json
%{mingw64_libdir}/qt6/metatypes/qt6labswavefrontmesh_relwithdebinfo_metatypes.json
%{mingw64_libdir}/qt6/metatypes/qt6packetprotocolprivate_relwithdebinfo_metatypes.json
%{mingw64_libdir}/qt6/metatypes/qt6qml_relwithdebinfo_metatypes.json
%{mingw64_libdir}/qt6/metatypes/qt6qmlcompilerprivate_relwithdebinfo_metatypes.json
%{mingw64_libdir}/qt6/metatypes/qt6qmlcore_relwithdebinfo_metatypes.json
%{mingw64_libdir}/qt6/metatypes/qt6qmldebugprivate_relwithdebinfo_metatypes.json
%{mingw64_libdir}/qt6/metatypes/qt6qmldomprivate_relwithdebinfo_metatypes.json
%{mingw64_libdir}/qt6/metatypes/qt6qmllocalstorage_relwithdebinfo_metatypes.json
%{mingw64_libdir}/qt6/metatypes/qt6qmlmodels_relwithdebinfo_metatypes.json
%{mingw64_libdir}/qt6/metatypes/qt6qmltyperegistrarprivate_relwithdebinfo_metatypes.json
%{mingw64_libdir}/qt6/metatypes/qt6qmlworkerscript_relwithdebinfo_metatypes.json
%{mingw64_libdir}/qt6/metatypes/qt6qmlxmllistmodel_relwithdebinfo_metatypes.json
%{mingw64_libdir}/qt6/metatypes/qt6quick_relwithdebinfo_metatypes.json
%{mingw64_libdir}/qt6/metatypes/qt6quickcontrols2_relwithdebinfo_metatypes.json
%{mingw64_libdir}/qt6/metatypes/qt6quickcontrols2impl_relwithdebinfo_metatypes.json
%{mingw64_libdir}/qt6/metatypes/qt6quickcontrolstestutilsprivate_relwithdebinfo_metatypes.json
%{mingw64_libdir}/qt6/metatypes/qt6quickdialogs2_relwithdebinfo_metatypes.json
%{mingw64_libdir}/qt6/metatypes/qt6quickdialogs2quickimpl_relwithdebinfo_metatypes.json
%{mingw64_libdir}/qt6/metatypes/qt6quickdialogs2utils_relwithdebinfo_metatypes.json
%{mingw64_libdir}/qt6/metatypes/qt6quickeffectsprivate_relwithdebinfo_metatypes.json
%{mingw64_libdir}/qt6/metatypes/qt6quicklayouts_relwithdebinfo_metatypes.json
%{mingw64_libdir}/qt6/metatypes/qt6quickparticlesprivate_relwithdebinfo_metatypes.json
%{mingw64_libdir}/qt6/metatypes/qt6quickshapesprivate_relwithdebinfo_metatypes.json
%{mingw64_libdir}/qt6/metatypes/qt6quicktemplates2_relwithdebinfo_metatypes.json
%{mingw64_libdir}/qt6/metatypes/qt6quicktest_relwithdebinfo_metatypes.json
%{mingw64_libdir}/qt6/metatypes/qt6quicktestutilsprivate_relwithdebinfo_metatypes.json
%{mingw64_libdir}/qt6/metatypes/qt6quickwidgets_relwithdebinfo_metatypes.json

%{mingw64_libdir}/Qt6LabsAnimation.prl
%{mingw64_libdir}/Qt6LabsFolderListModel.prl
%{mingw64_libdir}/Qt6LabsQmlModels.prl
%{mingw64_libdir}/Qt6LabsSettings.prl
%{mingw64_libdir}/Qt6LabsSharedImage.prl
%{mingw64_libdir}/Qt6LabsWavefrontMesh.prl
%{mingw64_libdir}/Qt6Qml.prl
%{mingw64_libdir}/Qt6QmlCompiler.prl
%{mingw64_libdir}/Qt6QmlCore.prl
%{mingw64_libdir}/Qt6QmlDebug.prl
%{mingw64_libdir}/Qt6QmlDom.prl
%{mingw64_libdir}/Qt6QmlLocalStorage.prl
%{mingw64_libdir}/Qt6QmlModels.prl
%{mingw64_libdir}/Qt6QmlTypeRegistrar.prl
%{mingw64_libdir}/Qt6QmlWorkerScript.prl
%{mingw64_libdir}/Qt6QmlXmlListModel.prl
%{mingw64_libdir}/Qt6Quick.prl
%{mingw64_libdir}/Qt6QuickControls2.prl
%{mingw64_libdir}/Qt6QuickControls2Impl.prl
%{mingw64_libdir}/Qt6QuickControlsTestUtils.prl
%{mingw64_libdir}/Qt6QuickDialogs2.prl
%{mingw64_libdir}/Qt6QuickDialogs2QuickImpl.prl
%{mingw64_libdir}/Qt6QuickDialogs2Utils.prl
%{mingw64_libdir}/Qt6QuickEffects.prl
%{mingw64_libdir}/Qt6QuickLayouts.prl
%{mingw64_libdir}/Qt6QuickParticles.prl
%{mingw64_libdir}/Qt6QuickShapes.prl
%{mingw64_libdir}/Qt6QuickTemplates2.prl
%{mingw64_libdir}/Qt6QuickTest.prl
%{mingw64_libdir}/Qt6QuickTestUtils.prl
%{mingw64_libdir}/Qt6QuickWidgets.prl

%{mingw64_libdir}/Qt6PacketProtocol.prl
%{mingw64_libdir}/qt6/mkspecs/features/qmltypes.prf
%{mingw64_libdir}/qt6/mkspecs/modules/qt_lib_labsanimation.pri
%{mingw64_libdir}/qt6/mkspecs/modules/qt_lib_labsanimation_private.pri
%{mingw64_libdir}/qt6/mkspecs/modules/qt_lib_labsfolderlistmodel.pri
%{mingw64_libdir}/qt6/mkspecs/modules/qt_lib_labsfolderlistmodel_private.pri
%{mingw64_libdir}/qt6/mkspecs/modules/qt_lib_labsqmlmodels.pri
%{mingw64_libdir}/qt6/mkspecs/modules/qt_lib_labsqmlmodels_private.pri
%{mingw64_libdir}/qt6/mkspecs/modules/qt_lib_labssettings.pri
%{mingw64_libdir}/qt6/mkspecs/modules/qt_lib_labssettings_private.pri
%{mingw64_libdir}/qt6/mkspecs/modules/qt_lib_labssharedimage.pri
%{mingw64_libdir}/qt6/mkspecs/modules/qt_lib_labssharedimage_private.pri
%{mingw64_libdir}/qt6/mkspecs/modules/qt_lib_labswavefrontmesh.pri
%{mingw64_libdir}/qt6/mkspecs/modules/qt_lib_labswavefrontmesh_private.pri
%{mingw64_libdir}/qt6/mkspecs/modules/qt_lib_packetprotocol_private.pri
%{mingw64_libdir}/qt6/mkspecs/modules/qt_lib_qml.pri
%{mingw64_libdir}/qt6/mkspecs/modules/qt_lib_qml_private.pri
%{mingw64_libdir}/qt6/mkspecs/modules/qt_lib_qmlcompiler_private.pri
%{mingw64_libdir}/qt6/mkspecs/modules/qt_lib_qmlcore.pri
%{mingw64_libdir}/qt6/mkspecs/modules/qt_lib_qmlcore_private.pri
%{mingw64_libdir}/qt6/mkspecs/modules/qt_lib_qmldebug_private.pri
%{mingw64_libdir}/qt6/mkspecs/modules/qt_lib_qmldom_private.pri
%{mingw64_libdir}/qt6/mkspecs/modules/qt_lib_qmlintegration.pri
%{mingw64_libdir}/qt6/mkspecs/modules/qt_lib_qmlintegration_private.pri
%{mingw64_libdir}/qt6/mkspecs/modules/qt_lib_qmllocalstorage.pri
%{mingw64_libdir}/qt6/mkspecs/modules/qt_lib_qmllocalstorage_private.pri
%{mingw64_libdir}/qt6/mkspecs/modules/qt_lib_qmlmodels.pri
%{mingw64_libdir}/qt6/mkspecs/modules/qt_lib_qmlmodels_private.pri
%{mingw64_libdir}/qt6/mkspecs/modules/qt_lib_qmltest.pri
%{mingw64_libdir}/qt6/mkspecs/modules/qt_lib_qmltest_private.pri
%{mingw64_libdir}/qt6/mkspecs/modules/qt_lib_qmltyperegistrar_private.pri
%{mingw64_libdir}/qt6/mkspecs/modules/qt_lib_qmlworkerscript.pri
%{mingw64_libdir}/qt6/mkspecs/modules/qt_lib_qmlworkerscript_private.pri
%{mingw64_libdir}/qt6/mkspecs/modules/qt_lib_qmlxmllistmodel.pri
%{mingw64_libdir}/qt6/mkspecs/modules/qt_lib_qmlxmllistmodel_private.pri
%{mingw64_libdir}/qt6/mkspecs/modules/qt_lib_quick.pri
%{mingw64_libdir}/qt6/mkspecs/modules/qt_lib_quick_private.pri
%{mingw64_libdir}/qt6/mkspecs/modules/qt_lib_quickcontrols2.pri
%{mingw64_libdir}/qt6/mkspecs/modules/qt_lib_quickcontrols2_private.pri
%{mingw64_libdir}/qt6/mkspecs/modules/qt_lib_quickcontrols2impl.pri
%{mingw64_libdir}/qt6/mkspecs/modules/qt_lib_quickcontrols2impl_private.pri
%{mingw64_libdir}/qt6/mkspecs/modules/qt_lib_quickcontrolstestutilsprivate_private.pri
%{mingw64_libdir}/qt6/mkspecs/modules/qt_lib_quickdialogs2.pri
%{mingw64_libdir}/qt6/mkspecs/modules/qt_lib_quickdialogs2_private.pri
%{mingw64_libdir}/qt6/mkspecs/modules/qt_lib_quickdialogs2quickimpl.pri
%{mingw64_libdir}/qt6/mkspecs/modules/qt_lib_quickdialogs2quickimpl_private.pri
%{mingw64_libdir}/qt6/mkspecs/modules/qt_lib_quickdialogs2utils.pri
%{mingw64_libdir}/qt6/mkspecs/modules/qt_lib_quickdialogs2utils_private.pri
%{mingw64_libdir}/qt6/mkspecs/modules/qt_lib_quickeffects_private.pri
%{mingw64_libdir}/qt6/mkspecs/modules/qt_lib_quicklayouts.pri
%{mingw64_libdir}/qt6/mkspecs/modules/qt_lib_quicklayouts_private.pri
%{mingw64_libdir}/qt6/mkspecs/modules/qt_lib_quickparticles_private.pri
%{mingw64_libdir}/qt6/mkspecs/modules/qt_lib_quickshapes_private.pri
%{mingw64_libdir}/qt6/mkspecs/modules/qt_lib_quicktemplates2.pri
%{mingw64_libdir}/qt6/mkspecs/modules/qt_lib_quicktemplates2_private.pri
%{mingw64_libdir}/qt6/mkspecs/modules/qt_lib_quicktestutilsprivate_private.pri
%{mingw64_libdir}/qt6/mkspecs/modules/qt_lib_quickwidgets.pri
%{mingw64_libdir}/qt6/mkspecs/modules/qt_lib_quickwidgets_private.pri

%{mingw64_libdir}/qt6/plugins/qmllint/
%{mingw64_libdir}/qt6/plugins/qmltooling/

%dir %{mingw64_libdir}/qt6/qml/
%{mingw64_libdir}/qt6/qml/builtins.qmltypes
%{mingw64_libdir}/qt6/qml/jsroot.qmltypes
%dir %{mingw64_libdir}/qt6/qml/Qt/
%dir %{mingw64_libdir}/qt6/qml/Qt/labs/
%{mingw64_libdir}/qt6/qml/Qt/labs/animation/
%{mingw64_libdir}/qt6/qml/Qt/labs/folderlistmodel
%{mingw64_libdir}/qt6/qml/Qt/labs/platform/
%{mingw64_libdir}/qt6/qml/Qt/labs/qmlmodels
%{mingw64_libdir}/qt6/qml/Qt/labs/settings
%{mingw64_libdir}/qt6/qml/Qt/labs/sharedimage/
%{mingw64_libdir}/qt6/qml/Qt/labs/wavefrontmesh/
%dir %{mingw64_libdir}/qt6/qml/Qt/test/
%{mingw64_libdir}/qt6/qml/Qt/test/controls/
%{mingw64_libdir}/qt6/qml/QtCore/
%{mingw64_libdir}/qt6/qml/QtQml/
%{mingw64_libdir}/qt6/qml/QtQuick/
%{mingw64_libdir}/qt6/qml/QtTest/

%{mingw64_libdir}/qt6/modules/LabsAnimation.json
%{mingw64_libdir}/qt6/modules/LabsFolderListModel.json
%{mingw64_libdir}/qt6/modules/LabsQmlModels.json
%{mingw64_libdir}/qt6/modules/LabsSettings.json
%{mingw64_libdir}/qt6/modules/LabsSharedImage.json
%{mingw64_libdir}/qt6/modules/LabsWavefrontMesh.json
%{mingw64_libdir}/qt6/modules/PacketProtocolPrivate.json
%{mingw64_libdir}/qt6/modules/Qml.json
%{mingw64_libdir}/qt6/modules/QmlCompilerPrivate.json
%{mingw64_libdir}/qt6/modules/QmlCore.json
%{mingw64_libdir}/qt6/modules/QmlDebugPrivate.json
%{mingw64_libdir}/qt6/modules/QmlDomPrivate.json
%{mingw64_libdir}/qt6/modules/QmlIntegration.json
%{mingw64_libdir}/qt6/modules/QmlLocalStorage.json
%{mingw64_libdir}/qt6/modules/QmlModels.json
%{mingw64_libdir}/qt6/modules/QmlTypeRegistrarPrivate.json
%{mingw64_libdir}/qt6/modules/QmlWorkerScript.json
%{mingw64_libdir}/qt6/modules/QmlXmlListModel.json
%{mingw64_libdir}/qt6/modules/Quick.json
%{mingw64_libdir}/qt6/modules/QuickControls2.json
%{mingw64_libdir}/qt6/modules/QuickControls2Impl.json
%{mingw64_libdir}/qt6/modules/QuickControlsTestUtilsPrivate.json
%{mingw64_libdir}/qt6/modules/QuickDialogs2.json
%{mingw64_libdir}/qt6/modules/QuickDialogs2QuickImpl.json
%{mingw64_libdir}/qt6/modules/QuickDialogs2Utils.json
%{mingw64_libdir}/qt6/modules/QuickEffectsPrivate.json
%{mingw64_libdir}/qt6/modules/QuickLayouts.json
%{mingw64_libdir}/qt6/modules/QuickParticlesPrivate.json
%{mingw64_libdir}/qt6/modules/QuickShapesPrivate.json
%{mingw64_libdir}/qt6/modules/QuickTemplates2.json
%{mingw64_libdir}/qt6/modules/QuickTest.json
%{mingw64_libdir}/qt6/modules/QuickTestUtilsPrivate.json
%{mingw64_libdir}/qt6/modules/QuickWidgets.json


%changelog
* Thu Apr 06 2023 Sandro Mani <manisandro@gmail.com> - 6.5.0-1
- Update to 6.5.0

* Wed Mar 29 2023 Sandro Mani <manisandro@gmail.com> - 6.4.3-1
- Update to 6.4.3

* Tue Mar 28 2023 Sandro Mani <manisandro@gmail.com> - 6.4.2-1
- Update to 6.4.2

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 6.4.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Wed Jan 18 2023 Sandro Mani <manisandro@gmail.com> - 6.4.2-1
- Update to 6.4.2

* Fri Nov 25 2022 Sandro Mani <manisandro@gmail.com> - 6.4.1-1
- Update to 6.4.1

* Mon Aug 08 2022 Jan Grulich <jgrulich@redhat.com> - 6.3.1-4
- Backport upstream fix needed for Fedora MediaWriter on Windows

* Sat Jul 23 2022 Sandro Mani <manisandro@gmail.com> - 6.3.1-3
- Add version suffix to qmleasing to avoid conflict with qt5-qtdeclarative

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 6.3.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon Jul 18 2022 Sandro Mani <manisandro@gmail.com> - 6.3.1-1
- Update to 6.3.1

* Thu Apr 28 2022 Sandro Mani <manisandro@gmail.com> - 6.3.0-1
- Update to 6.3.0

* Wed Mar 30 2022 Sandro Mani <manisandro@gmail.com> - 6.2.3-3
- Add qt6 suffix to tools to avoid collision with qt5 tools

* Fri Mar 25 2022 Sandro Mani <manisandro@gmail.com> - 6.2.3-3
- Rebuild with mingw-gcc-12

* Sat Mar 05 2022 Sandro Mani <manisandro@gmail.com> - 6.2.3-2
- Re-enable s390x build

* Tue Feb 08 2022 Sandro Mani <manisandro@gmail.com> - 6.2.3-1
- Update to 6.2.3

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 6.2.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Tue Dec 14 2021 Sandro Mani <manisandro@gmail.com> - 6.2.2-1
- Update to 6.2.2

* Mon Nov 01 2021 Sandro Mani <manisandro@gmail.com> - 6.2.1-1
- Update to 6.2.1

* Sun Oct 03 2021 Sandro Mani <manisandro@gmail.com> - 6.2.0-1
- Update to 6.2.0

* Mon Sep 27 2021 Sandro Mani <manisandro@gmail.com> - 6.2.0-0.3.rc2
- Update to 6.2.0-rc2

* Wed Sep 22 2021 Sandro Mani <manisandro@gmail.com> - 6.2.0-0.2.rc
- Obsolete/provide mingw-qt6-qtquickcontrols2

* Wed Sep 22 2021 Sandro Mani <manisandro@gmail.com> - 6.2.0-0.1.rc
- Update to 6.2.0-rc

* Fri Aug 13 2021 Sandro Mani <manisandro@gmail.com> - 6.1.2-1
- Update to 6.1.2

* Mon Aug 09 2021 Sandro Mani <manisandro@gmail.com> - 6.1.1-2
- More detailed %%files

* Sat Jul 10 2021 Sandro Mani <manisandro@gmail.com> - 6.1.1-1
- Update to 6.1.1
