%bcond_without python

# time of tests on s390x is too long, disable it for now
%ifarch s390x
%bcond_with check
%else
%bcond_without check
%endif

%bcond_with all_tests
%global usd 0

%global forgeurl https://github.com/f3d-app/f3d
Version:        3.0.0
%forgemeta

Name:           f3d
Release:        %autorelease
Summary:        Fast and minimalist 3D viewer

License:        BSD-3-Clause
URL:            %{forgeurl}
Source0:        %{forgesource}
# Backport fix for building with assimp-6.x
# https://github.com/f3d-app/f3d/commit/9bed68ef2b5425c9600c81a7245f13ed2d4079b8.patch
Patch:          f3d-assimp6.patch

# https://fedoraproject.org/wiki/Changes/EncourageI686LeafRemoval
ExcludeArch: %{ix86}

BuildRequires:  gcc-c++
BuildRequires:  cmake
BuildRequires:  ninja-build
BuildRequires:  json-devel
BuildRequires:  cxxopts-devel
BuildRequires:  vtk-devel
BuildRequires:  lapack-devel
BuildRequires:  assimp-devel
BuildRequires:  cmake(draco)
# fedora 39 do not ship draco-static package
%if 0%{?fedora} != 39
BuildRequires:  draco-static
%endif
BuildRequires:  alembic-devel
BuildRequires:  opencascade-devel

%if %{usd}
BuildRequires:  cmake(pxr)
BuildRequires:  openshadinglanguage-devel
BuildRequires:  OpenImageIO-devel
BuildRequires:  opensubdiv-devel
BuildRequires:  openvdb-devel
BuildRequires:  ptex-devel
BuildRequires:  OpenColorIO-devel
BuildRequires:  embree-devel
%endif

BuildRequires:  imath-devel
BuildRequires:  help2man

%if %{with check}
BuildRequires:  xorg-x11-drv-dummy
BuildRequires:  mesa-dri-drivers
# provides /usr/bin/xvfb-run
BuildRequires:  xorg-x11-server-Xvfb
BuildRequires:  python3-pytest
%endif

BuildRequires:  desktop-file-utils
BuildRequires:  libappstream-glib

Requires:       hicolor-icon-theme
Requires:       shared-mime-info

%description
F3D is a fast and minimalist 3D viewer desktop application. It supports many
file formats, from digital content to scientific datasets (including glTF, USD,
STL, STEP, PLY, OBJ, FBX, Alembic), can show animations and support thumbnails
and many rendering and texturing options including real time physically based
rendering and raytracing.

It is fully controllable from the command line and support configuration files.
It can provide thumbnails, support interactive hotkeys, drag&drop and
integration into file managers.

F3D also contains the libf3d, a simple library to render meshes, with C++ and
Python Bindings, as well as experimental Java and Javascript bindings.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
This package contains development files for %{name}.

%if %{with python}
%package        python3
Summary:        Python 3 bindings for the %{name}
BuildRequires:  python3-devel
BuildRequires:  python3-pybind11
Requires:       %{name}%{?_isa} = %{version}-%{release}
Provides:       python3-%{name} = %{version}-%{release}

%description    python3
This package contains Python 3 bindings for %{name}.
%endif

%ifarch %{java_arches}
%package        java
Summary:        Java bindings for the %{name}
BuildRequires:  javapackages-tools
BuildRequires:  java-25-devel
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    java
This package contains Java bindings for %{name}.
%endif

%prep
%forgeautosetup -p1
# remove bundled libraries of cxxopts and nlohmann_json
rm -rf external/{cxxopts,nlohmann_json}
# fix install location for -java sub-package
sed -i 's|${CMAKE_INSTALL_LIBDIR}|${CMAKE_INSTALL_LIBDIR}/f3d|' java/CMakeLists.txt
sed -i 's|share/java|%{_jnidir}|' java/CMakeLists.txt

%build
%cmake \
    -GNinja \
    -DCMAKE_BUILD_TYPE=RelWithDebInfo \
    -DF3D_PLUGINS_STATIC_BUILD=OFF \
    -DF3D_PLUGINS_INSTALL_DIR=%{_libdir}/f3d/plugins \
    -DF3D_USE_EXTERNAL_CXXOPTS=ON \
    -DF3D_USE_EXTERNAL_NLOHMANN_JSON=ON \
    -DF3D_LINUX_INSTALL_DEFAULT_CONFIGURATION_FILE_IN_PREFIX=ON \
    -DF3D_LINUX_GENERATE_MAN=ON \
    -DF3D_MODULE_RAYTRACING=OFF \
    -DF3D_MODULE_EXTERNAL_RENDERING=OFF \
    -DF3D_PLUGIN_BUILD_ALEMBIC=ON \
    -DF3D_PLUGIN_BUILD_ASSIMP=ON \
    -DF3D_PLUGIN_BUILD_DRACO=ON \
    -DF3D_PLUGIN_BUILD_EXODUS=ON \
    -DF3D_PLUGIN_BUILD_OCCT=ON \
%if %{usd}
    -DF3D_PLUGIN_BUILD_USD=ON \
%endif
    -DF3D_PLUGIN_OCCT_COLORING_SUPPORT=ON \
    -DF3D_PLUGIN_BUILD_VDB=OFF \
%if %{with python}
    -DF3D_BINDINGS_PYTHON=ON \
%endif
%ifarch %{java_arches}
    -DF3D_BINDINGS_JAVA=ON \
%endif
%if %{with check}
    -DBUILD_TESTING=ON \
    -DF3D_TESTING_ENABLE_OSMESA_TESTS=OFF \
%endif
    -DCMAKE_SKIP_INSTALL_RPATH=ON \

%cmake_build

%install
%cmake_install

%cmake_install --component mimetypes
%cmake_install --component sdk
%cmake_install --component configuration

rm -r %{buildroot}%{_datadir}/doc/F3D

%check
%if %{with check}
export MESA_DEBUG=silent
export LIBGL_ALWAYS_SOFTWARE=true
export MESA_LOADER_DRIVER_OVERRIDE=llvmpipe
%if %{with all_tests}
xvfb-run -a bash -c "%ctest"
%else
skip_tests=
skip_tests+="libf3d::TestSDKCompareWithFile|libf3d::TestSDKMultiColoring|libf3d::TestSDKMultiOptions|"
skip_tests+="libf3d::TestSDKDynamicBackgroundColor|libf3d::TestSDKDynamicFontFile|libf3d::TestSDKDynamicLightIntensity|"
skip_tests+="libf3d::TestSDKDynamicProperties|f3d::TestVTP|f3d::TestVTR|f3d::TestVTM|f3d::TestGridAbsolute|"
skip_tests+="f3d::TestPointCloud|f3d::TestPointCloudBar|f3d::TestPointCloudDefaultScene|f3d::TestMultiblockMetaData|"
skip_tests+="f3d::TestLightIntensityBrighter|f3d::TestLightIntensityDarker|f3d::TestUTF8|f3d::TestComponentName|"
skip_tests+="f3d::TestGroupGeometries|f3d::TestGroupGeometriesColoring|f3d::TestScalarsCell|f3d::TestMetaData|"
skip_tests+="f3d::TestNoBackground|f3d::TestInteractionGroupGeometriesDrop|f3d::TestInteractionDropSameFiles|"
skip_tests+="f3d::TestVerboseWarning|f3d::TestTensorsDirect|f3d::TestTensorsVolumeDirect|pyf3d::TestPython_deprecated|"
skip_tests+="pyf3d::TestPython_image_compare|f3d::TestCameraOrthographic|f3d::TestWatch|"
xvfb-run -a bash -c "%ctest -E '$skip_tests'"
%endif
%endif

desktop-file-validate %{buildroot}%{_datadir}/applications/*.desktop
appstream-util validate-relax --nonet %{buildroot}%{_metainfodir}/*.metainfo.xml

%files
%license LICENSE.md
%doc README.md
%{_bindir}/f3d
%{bash_completions_dir}/f3d
%{zsh_completions_dir}/_f3d
%{fish_completions_dir}/f3d.fish
%{_datadir}/icons/hicolor/*/apps/f3d.png
%{_datadir}/icons/hicolor/scalable/apps/f3d.svg
%{_datadir}/icons/HighContrast/
%{_datadir}/applications/f3d-plugin-*.desktop
%{_datadir}/applications/f3d.desktop
%{_datadir}/mime/packages/f3d-*.xml
%dir %{_datadir}/f3d
%dir %{_datadir}/f3d/configs
%dir %{_datadir}/f3d/configs/config.d
%dir %{_datadir}/f3d/configs/thumbnail.d
%dir %{_datadir}/f3d/plugins
%{_datadir}/f3d/configs/config.d/*.json
%{_datadir}/f3d/configs/thumbnail.d/*.json
%{_datadir}/f3d/plugins/*.json
%{_datadir}/thumbnailers/f3d-plugin-*.thumbnailer
%{_mandir}/man1/f3d.1*
%{_metainfodir}/app.f3d.F3D.metainfo.xml

%{_libdir}/libf3d.so.3*
%{_libdir}/libvtkext.so
%dir %{_libdir}/f3d
%dir %{_libdir}/f3d/plugins
%{_libdir}/f3d/plugins/libf3d-plugin-*.so

%files devel
%{_libdir}/libf3d.so
%dir %{_includedir}/f3d
%{_includedir}/f3d/*.h
%{_libdir}/cmake/f3d/

%if %{with python}
%files python3
%{python3_sitearch}/f3d/
%endif

%ifarch %{java_arches}
%files java
%{_libdir}/f3d/libf3d-java.so
%{_jnidir}/f3d.jar
%endif

%changelog
%autochangelog
