Name:		meshlab
Summary:	A system for processing and editing unstructured 3D triangular meshes
Version:	2023.12
Release:	%autorelease
URL:		https://github.com/cnr-isti-vclab/meshlab
# Bundled e57 is Boost-licensed
# bundled glew is BSD-3-Clause
# bundled picojson is BSD-2-Clause
License:	GPL-2.0-or-later AND BSD-2-Clause AND BSD-3-Clause AND LicenseRef-Fedora-Public-Domain AND Apache-2.0 AND BSL-1.0
Source0:	https://github.com/cnr-isti-vclab/meshlab/archive/MeshLab-%{version}/%{name}-%{version}.tar.gz
# Matches 2023.12:
%global vcglibver 88c881d
# Probably belongs in its own package, but nothing else seems to depend on it.
Source2:	https://github.com/cnr-isti-vclab/vcglib/archive/%{vcglibver}/vcglib-%{vcglibver}.tar.gz
# Notes for Fedora users (around issues with Wayland)
Source3:	README.Fedora
# Upstream doesn't bundle some things anymore, it looks for a system copy and downloads it if not found
# We should consider packaging libE57Format separately, but I don't think anything else needs it
Source4:	https://github.com/asmaloney/libE57Format/archive/refs/tags/v2.3.0.zip
# I know there is at least one other consumer of libigl, but as a header only library... bundle here too.
Source5:	https://github.com/libigl/libigl/archive/refs/tags/v2.4.0.zip
# This nexus is not the same as the nexus package in Fedora.
# This nexus is a c++/javascript library for creation and visualization of a batched multiresolution
# 3D model structure
Source6:	https://www.meshlab.net/data/libs/nexus-master.zip
# It also needs corto, a library for compression and decompression meshes and point clouds (C++/Javascript)
Source7:	https://www.meshlab.net/data/libs/corto-master.zip
# Long bundled, now pulled out of the source tarball, it's OpenCTM!
# Could be made into it's own package, but A) it is very old and B) unlikely anything else needs it
Source8:	https://www.meshlab.net/data/libs/OpenCTM-1.0.3-src.zip
# Meshlab's fork of StructureSynth, the original is very old
Source9:	https://github.com/alemuntoni/StructureSynth/archive/refs/tags/1.5.1.zip
# Meshlab depends on tinygltf 2.6.3, which is not current.
# tinygltf is a header-only library, so bundle party fun time
Source10:	https://github.com/syoyo/tinygltf/archive/refs/tags/v2.6.3.zip
# Meshlab depends on u3d 1.5.1, which is slightly better than when it depended on a fork of u3d.
Source11:	https://www.meshlab.net/data/libs/u3d-1.5.1.zip


Provides:	bundled(vcglib) = %{vcglibver}

# Properly install u3d IDTFConverter library
# Patch0:         meshlab-2020.07-u3d-install-fix.patch
# Adjust MESHLAB_LIB_INSTALL_DIR to not have a meshlab/ subdir
# and adjust MESHLAB_PLUGIN_INSTALL_DIR to have it
Patch1:         meshlab-2021.07-MESHLAB_LIB_INSTALL_DIR-fix.patch
# Allow system levmar
Patch2:		meshlab-2023.12-system-levmar.patch
# Fix FTBFS with GCC 13+ by adding include <cstdint>
# Upstream already added that in https://github.com/asmaloney/libE57Format/pull/176
Patch3:         meshlab-2023.12-e57-gcc13.patch
# Include cstdint when corto uses uint32_t
Patch4:		meshlab-2023.12-corto-cstdint.patch
# Cmake fix
Patch5:		meshlab-2023.12-cmake-fix.patch
# Comment out LoadCamera (it is broken and unused)
Patch6:		meshlab-2023.12-vcglib-no-LoadCamera.patch
# This struct doesn't define "value". I think it actually wants to use "point" in the - operator, like it does in the + operator, but... who knows.
Patch7:		meshlab-2023.12-fix-nonexistent-value.patch
# There are also undefined variables in a function that does not seem to be called. :/
Patch8:		meshlab-2023.12-fix-invalid-vars.patch

# Bundled things
Provides:	bundled(u3d) = 1.5.1
Provides:	bundled(e57) = 2.3.0
Provides:	bundled(libigl) = 2.4.0
Provides:	bundled(OpenCTM) = 1.0.3
Provides:	bundled(StructureSynth) = 1.5.1-meshlab
Provides:	bundled(tinygltf) = 2.6.3

# Meshlab now depends on embree, which only builds on these arches
# If you want to change this, go fix embree first.
ExclusiveArch:  aarch64 x86_64

BuildRequires:	bzip2-devel
BuildRequires:	CGAL-devel
BuildRequires:	eigen3-devel
BuildRequires:	embree-devel
BuildRequires:	glew-devel
BuildRequires:  gmp-devel
BuildRequires:	levmar-devel
BuildRequires:	lib3ds-devel
BuildRequires:	muParser-devel
BuildRequires:	qhull-devel
BuildRequires:	qt5-qtbase-devel qt5-qtdeclarative-devel qt5-qtxmlpatterns-devel qt5-qtscript-devel
BuildRequires:  tbb-devel
BuildRequires:	desktop-file-utils
BuildRequires:	ImageMagick
BuildRequires:	xerces-c-devel

# https://fedoraproject.org/wiki/Changes/EncourageI686LeafRemoval
%if 0%{?fedora} >= 37 || 0%{?rhel} >= 10
ExcludeArch:	%{ix86}
%endif

# Get Fedora 33++ behavior on anything older
%undefine __cmake_in_source_build

%description
MeshLab is an open source, portable, and extensible system for the
processing and editing of unstructured 3D triangular meshes.  The
system is aimed to help the processing of the typical not-so-small
unstructured models arising in 3D scanning, providing a set of tools
for editing, cleaning, healing, inspecting, rendering and converting
these kinds of meshes.

%prep
%setup -q -n meshlab-MeshLab-%{version} -a 2
# %%patch0 -p1 -b .installfix
%patch -P 1 -p1 -b .libdirfix
%patch -P 2 -p1 -b .system-levmar
cp %{SOURCE3} .
rmdir src/vcglib && mv vcglib-%{vcglibver}* src/vcglib

pushd src/external
mkdir -p downloads
cd downloads
unzip %{SOURCE4}
unzip %{SOURCE5}
unzip %{SOURCE6}
unzip %{SOURCE8}
unzip %{SOURCE9}
unzip %{SOURCE10}
unzip %{SOURCE11}
pushd nexus-master/src
rm -rf corto
unzip %{SOURCE7}
mv corto-master corto
popd
popd

# These patches need to apply after we build the bundled tree
%patch -P 3 -p1 -b .e57-gcc13
%patch -P 4 -p1 -b .cstdint

%patch -P 5 -p1 -b .cmake-fix
%patch -P 6 -p1 -b .no-LoadCamera
%patch -P 7 -p1 -b .fix-nonexistent-value
%patch -P 8 -p1 -b .fix-invalid-vars


# remove some bundles
%if 0
rm -rf src/external/glew*
rm -rf src/external/qhull*
rm -rf src/external/levmar*
rm -rf src/external/lib3ds*
rm -rf src/external/muparser*
%endif

# plugin path
sed -i -e 's|"lib"|"%{_lib}"|g' src/common/globals.cpp
# sed -i -e 's|"lib"|"%{_lib}"|g' src/meshlab/plugindialog.cpp

# icon path, see https://github.com/cnr-isti-vclab/meshlab/pull/752
# sed -i -e 's|/icons/pixmaps|/pixmaps|g' src/CMakeLists.txt

%build
export CXXFLAGS=`echo %{optflags} -std=c++14 -fopenmp -DSYSTEM_QHULL -I/usr/include/libqhull`

%global _vpath_srcdir src
%cmake \
	-DMESHLAB_USE_DEFAULT_BUILD_AND_INSTALL_DIRS=ON \
	-DCMAKE_SKIP_RPATH=ON \
	-DCMAKE_VERBOSE_MAKEFILE=OFF \
	-DCMAKE_BUILD_TYPE=RelWithDebInfo \
	-DALLOW_BUNDLED_EIGEN=OFF \
	-DALLOW_BUNDLED_GLEW=OFF \
	-DALLOW_BUNDLED_LEVMAR=ON \
	-DALLOW_BUNDLED_LIB3DS=OFF \
	-DALLOW_BUNDLED_MUPARSER=OFF \
	-DALLOW_BUNDLED_NEWUOA=ON \
	-DALLOW_BUNDLED_OPENCTM=ON \
	-DALLOW_BUNDLED_QHULL=OFF \
	-DALLOW_BUNDLED_SSYNTH=ON \
	-DALLOW_BUNDLED_XERCES=OFF \
	-DALLOW_SYSTEM_EIGEN=ON \
	-DALLOW_SYSTEM_GLEW=ON \
	-DALLOW_SYSTEM_GMP=ON \
	-DALLOW_SYSTEM_LIB3DS=ON \
	-DALLOW_SYSTEM_MUPARSER=ON \
	-DALLOW_SYSTEM_OPENCTM=ON \
	-DALLOW_SYSTEM_QHULL=ON \
	-DALLOW_SYSTEM_XERCES=ON \
	-DEigen3_DIR=usr/include/eigen3 \
	-DGlew_DIR=/usr/include/GL \
	-DQhull_DIR=/usr/include/libqhull

%cmake_build

# create desktop file
cat <<EOF >meshlab.desktop
[Desktop Entry]
Name=meshlab
GenericName=MeshLab 3D triangular mesh processing and editing
Exec=env QT_QPA_PLATFORM=xcb meshlab
Icon=meshlab
Terminal=false
Type=Application
Categories=Graphics;
EOF

%install
%cmake_install

mkdir -p %{buildroot}%{_datadir}/pixmaps/
cp -a meshlab.png %{buildroot}%{_datadir}/pixmaps/

# add desktop link
install -d -m 755 %{buildroot}%{_datadir}/applications
install -p -m 644 meshlab.desktop %{buildroot}%{_datadir}/applications
desktop-file-validate %{buildroot}%{_datadir}/applications/meshlab.desktop

%files
%doc README.md README.Fedora
%doc docs/readme.txt
%doc docs/privacy.txt
%license LICENSE.txt
%license src/external/downloads/u3d-*/COPYING
%{_bindir}/meshlab
# unsupported in 2021
# %%{_bindir}/meshlabserver
%{_libdir}/*.so*
%{_libdir}/meshlab/
%{_datadir}/meshlab/
%{_datadir}/applications/meshlab.desktop
%{_datadir}/icons/hicolor/512x512/apps/meshlab.png
%{_datadir}/pixmaps/meshlab.png
%license resources/shaders/3Dlabs-license.txt
%license resources/shaders/LightworkDesign-license.txt
# %%license unsupported/plugins_experimental/filter_segmentation/license.txt
# %%license unsupported/plugins_unsupported/filter_poisson/license.txt

%changelog
%autochangelog
