# Adapted from
# https://build.opensuse.org/package/view_file/home:bruno_friedmann:branches:Application:Geo/cloudcompare/cloudcompare.spec
#
# Copyright (c) 2016 SUSE LINUX GmbH, Nuernberg, Germany.
# Copyright (c) 2016 Ioda-Net Sàrl, Charmoille, Switzerland. Bruno Friedmann
# Copyright (c) 2017 Miro Hrončok and possibly others
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.


%global edition Release
%global cname   CloudCompare
Name:           cloudcompare
Version:        2.11.3
Release:        %autorelease
Summary:        3D point cloud and mesh processing software

# Main part is GPLv2+
# CCLib is LGPLv2+
# Plugin from Source1 is MIT
# Plugin from Source2 is Boost
# dxflib is GPLv2+
# shapelib is (LGPLv2+ or MIT)
# as the result is compiled into one piece, it should be:
# Automatically converted from old format: GPLv2+ - review is highly recommended.
License:        GPL-2.0-or-later

URL:            http://www.cloudcompare.org/

# https://fedoraproject.org/wiki/Changes/EncourageI686LeafRemoval
%if 0%{?fedora} >= 37 || 0%{?rhel} >= 10
ExcludeArch:    %{ix86}
%endif

Source0:        https://github.com/%{cname}/%{cname}/archive/v%{version}/%{cname}-%{version}.tar.gz

# git submodules
%global pr_commit 134fb831764dd5ebd53616e83992f0060e4b09ce
Source1:        https://github.com/%{cname}/PoissonRecon/archive/%{pr_commit}/PoissonRecon-%{pr_commit}.tar.gz

%global lE57F_commit 14f6a67cf98485189cfd154bc42081d38e480b9d
Source2:        https://github.com/asmaloney/libE57Format/archive/%{lE57F_commit}/libE57Format-%{lE57F_commit}.tar.gz

# desktop files
Source3:        %{name}.desktop
Source4:        ccviewer.desktop

# https://github.com/CloudCompare/CloudCompare/pull/1310
Patch:          %{name}-pcl1.11.patch

# https://github.com/CloudCompare/CloudCompare/commit/5bc453a08a
# https://github.com/CloudCompare/CloudCompare/commit/1b5f2a710e
# https://github.com/CloudCompare/CloudCompare/commit/535c501760
# https://github.com/CloudCompare/CloudCompare/issues/1504
Patch:          %{name}-pcl1.12.patch

# https://github.com/qcad/qcad/commit/1eeffc5daf
Patch:          %{name}-CVE-2021-21897.patch

# Change required CMake version to 3.10
# https://github.com/CloudCompare/CloudCompare/commit/ffd19dccb7
# Fixes FTBFS with cmake 4 https://bugzilla.redhat.com/2380504
Patch:          %{name}-cmake3.10.patch

BuildRequires:  boost-devel
BuildRequires:  desktop-file-utils
BuildRequires:  cmake >= 3
BuildRequires:  fdupes
BuildRequires:  gcc-c++
BuildRequires:  laszip-devel
BuildRequires:  libgomp
BuildRequires:  libusb1-devel
BuildRequires:  make
BuildRequires:  pcl-devel
BuildRequires:  pkgconfig(gdal)
BuildRequires:  pkgconfig(cunit)
BuildRequires:  pkgconfig(dri)
BuildRequires:  pkgconfig(eigen3)
BuildRequires:  pkgconfig(gl)
BuildRequires:  pkgconfig(glew)
BuildRequires:  pkgconfig(glu)
BuildRequires:  pkgconfig(pkg-config)
BuildRequires:  pkgconfig(shapelib)
BuildRequires:  pkgconfig(Qt3Support)
BuildRequires:  pkgconfig(Qt5Concurrent)
BuildRequires:  pkgconfig(Qt5Core)
BuildRequires:  pkgconfig(Qt5DBus)
BuildRequires:  pkgconfig(Qt5Designer)
BuildRequires:  pkgconfig(Qt5Gui)
BuildRequires:  pkgconfig(Qt5Help)
BuildRequires:  pkgconfig(Qt5Multimedia)
BuildRequires:  pkgconfig(Qt5Network)
BuildRequires:  pkgconfig(Qt5OpenGL)
BuildRequires:  pkgconfig(Qt5OpenGLExtensions)
BuildRequires:  pkgconfig(Qt5PrintSupport)
BuildRequires:  pkgconfig(Qt5Script)
BuildRequires:  pkgconfig(Qt5ScriptTools)
BuildRequires:  pkgconfig(Qt5Sql)
BuildRequires:  pkgconfig(Qt5Svg)
BuildRequires:  pkgconfig(Qt5Test)
BuildRequires:  pkgconfig(Qt5UiTools)
BuildRequires:  pkgconfig(Qt5Widgets)
BuildRequires:  pkgconfig(Qt5Xml)
BuildRequires:  pkgconfig(Qt5XmlPatterns)
BuildRequires:  pkgconfig(xerces-c)
BuildRequires:  pkgconfig(zlib)

Provides:       bundled(dxflib) = 3.17.0
Provides:       %{cname} = %{version}-%{release}
%{?_isa:Provides:       %{cname}%{_isa} = %{version}-%{release}}

Requires:       hicolor-icon-theme

# Do not RPM provide .so files only used internally:
%global __provides_exclude_from ^%{_libdir}/%{name}/.*$
%global __requires_exclude ^lib(Q)?CC_.*$

# Get pre-Fedora 33 behavior of cmake
%define __cmake_in_source_build 1

%description
CloudCompare is a 3D point cloud (and triangular mesh) processing software.
It has been originally designed to perform comparison between two 3D points
clouds (such as the ones obtained with a laser scanner) or between a point
cloud and a triangular mesh.
It relies on a specific octree structure that enables great performances in
this particular function. It was also meant to deal with huge point clouds
(typically more than 10 millions points, and up to 120 millions with 2 Gb of
memory).

Afterwards, it has been extended to a more generic point cloud processing
software, including many advanced algorithms (registration, resampling,
color/normal/scalar fields handling, statistics computation, sensor
management, interactive or automatic segmentation, display enhancement...).


%package doc
Summary:        Documentation for %{cname}
Requires:       %{name} == %{version}-%{release}
BuildArch:      noarch

%description doc
CloudCompare is a 3D point cloud (and triangular mesh) processing software.
This is the documentation.


%prep
%autosetup -n %{cname}-%{version} -N

rmdir plugins/core/Standard/qPoissonRecon/PoissonReconLib
tar -xf %{SOURCE1}
mv PoissonRecon-%{pr_commit} plugins/core/Standard/qPoissonRecon/PoissonReconLib

rmdir plugins/core/IO/qE57IO/extern/libE57Format
tar -xf %{SOURCE2}
mv libE57Format-%{lE57F_commit} plugins/core/IO/qE57IO/extern/libE57Format

%autopatch -p1

# On 64bits, change /usr/lib/cloudcompare to /usr/lib64/cloudcompare
sed -i 's|lib/%{name}|%{_lib}/%{name}|g' $(grep -r lib/%{name} -l)

# Remove french TeX docs
rm -rf doc/fr*

# Remove bundled shapelib https://github.com/CloudCompare/CloudCompare/issues/497
rm -rf contrib/shapelib
sed -i 's/add_subdirectory.*//' contrib/ShapeLibSupport.cmake
sed -i 's/ SHAPELIB / shp /g' plugins/core/Standard/qFacets/CMakeLists.txt contrib/ShapeLibSupport.cmake

# For PCL 1.15+
sed -i 's/-std=c++14/-std=c++17/' cmake/CMakeSetCompilerOptions.cmake

%build
mkdir build
pushd build

%cmake .. \
   -DCMAKE_BUILD_TYPE=%{edition} \
   -DCMAKE_INSTALL_RPATH=%{_libdir}/%{name} \
   -DEIGEN_ROOT_DIR=%{_includedir}/eigen3 \
   -DGDAL_INCLUDE_DIR=%{_includedir}/gdal \
   -DDLIB_ROOT=%{_includedir}/dlib \
   -DPLUGIN_STANDARD_QANIMATION=ON \
   -DPLUGIN_STANDARD_QBROOM=ON \
   -DPLUGIN_STANDARD_QCSF=ON \
   -DPLUGIN_STANDARD_QCOMPASS=ON \
   -DPLUGIN_STANDARD_QHPR=ON \
   -DPLUGIN_STANDARD_QHOUGH_NORMALS=ON \
   -DPLUGIN_STANDARD_QM3C2=ON \
   -DPLUGIN_STANDARD_QPCL=ON \
   -DPLUGIN_STANDARD_QPCV=ON \
   -DPLUGIN_STANDARD_QCSF=ON \
   -DPLUGIN_STANDARD_QPOISSON_RECON=ON \
   -DPLUGIN_STANDARD_QSRA=ON \
   -DPLUGIN_GL_QEDL=ON \
   -DPLUGIN_GL_QSSAO=ON \
   -DPLUGIN_IO_QADDITIONAL=ON \
   -DPLUGIN_IO_QCSV_MATRIX=ON \
   -DPLUGIN_IO_QCORE=ON \
   -DPLUGIN_IO_QPHOTOSCAN=ON \
   -DOPTION_SUPPORT_3DCONNEXION_DEVICES=OFF \
   -DOPTION_USE_DXF_LIB=ON \
   -DOPTION_USE_GDAL=ON \
   -DOPTION_USE_SHAPE_LIB=ON \
   -DSHAPELIB_SOURCE_DIR=%{_includedir} \
   -DPLUGIN_STANDARD_QFACETS=ON \
%ifarch %ix86 x86_64
   -DPLUGIN_STANDARD_QRANSAC_SD=ON \
%else
   -DPLUGIN_STANDARD_QRANSAC_SD=OFF \
%endif

# PLUGIN_STANDARD_QRANSAC_SD on other arches: fatal error: xmmintrin.h: No such file or directory


%make_build VERBOSE=1
popd

%install
pushd build
%make_install VERBOSE=1
popd

# lower-case symblinks
ln -s ./%{cname} %{buildroot}%{_bindir}/%{name}
ln -s ./ccViewer %{buildroot}%{_bindir}/ccviewer

# icons
for RES in 16 32 64 256; do
  mkdir -p %{buildroot}%{_datadir}/icons/hicolor/${RES}x${RES}/apps/
  cp qCC/images/icon/cc_icon_${RES}.png %{buildroot}%{_datadir}/icons/hicolor/${RES}x${RES}/apps/%{name}.png
  cp qCC/images/icon/cc_viewer_icon_${RES}.png %{buildroot}%{_datadir}/icons/hicolor/${RES}x${RES}/apps/ccviewer.png
done

# desktop files
desktop-file-install --dir=%{buildroot}%{_datadir}/applications %{SOURCE3}
desktop-file-install --dir=%{buildroot}%{_datadir}/applications %{SOURCE4}


%files
%doc README.md CONTRIBUTING.md
%{_bindir}/%{name}
%{_bindir}/%{cname}
%{_bindir}/ccviewer
%{_bindir}/ccViewer

%dir %{_libdir}/%{name}/
%{_libdir}/%{name}/lib*.so
%dir %{_libdir}/%{name}/plugins/
%{_libdir}/%{name}/plugins/libQADDITIONAL_IO_PLUGIN.so
%{_libdir}/%{name}/plugins/libQANIMATION_PLUGIN.so
%{_libdir}/%{name}/plugins/libQBROOM_PLUGIN.so
%{_libdir}/%{name}/plugins/libQCOMPASS_PLUGIN.so
%{_libdir}/%{name}/plugins/libQCORE_IO_PLUGIN.so
%{_libdir}/%{name}/plugins/libQCSF_PLUGIN.so
%{_libdir}/%{name}/plugins/libQCSV_MATRIX_IO_PLUGIN.so
%{_libdir}/%{name}/plugins/libQEDL_GL_PLUGIN.so
%{_libdir}/%{name}/plugins/libQFACETS_PLUGIN.so
%{_libdir}/%{name}/plugins/libQHOUGH_NORMALS_PLUGIN.so
%{_libdir}/%{name}/plugins/libQHPR_PLUGIN.so
%{_libdir}/%{name}/plugins/libQM3C2_PLUGIN.so
%{_libdir}/%{name}/plugins/libQPCL_IO_PLUGIN.so
%{_libdir}/%{name}/plugins/libQPCL_PLUGIN.so
%{_libdir}/%{name}/plugins/libQPCV_PLUGIN.so
%{_libdir}/%{name}/plugins/libQPHOTOSCAN_IO_PLUGIN.so
%{_libdir}/%{name}/plugins/libQPOISSON_RECON_PLUGIN.so
%{_libdir}/%{name}/plugins/libQSRA_PLUGIN.so
%{_libdir}/%{name}/plugins/libQSSAO_GL_PLUGIN.so
%ifarch %ix86 x86_64
%{_libdir}/%{name}/plugins/libQRANSAC_SD_PLUGIN.so
%endif

%dir %{_datadir}/%{name}/
%{_datadir}/%{name}/global_shift_list_template.txt
%{_datadir}/%{name}/shaders/
%dir %{_datadir}/%{name}/translations/
%lang(es) %{_datadir}/%{name}/translations/*_es_AR.qm
%lang(fr) %{_datadir}/%{name}/translations/*_fr.qm
%lang(ja) %{_datadir}/%{name}/translations/*_ja.qm
%lang(pt) %{_datadir}/%{name}/translations/*_pt.qm
%lang(ru) %{_datadir}/%{name}/translations/*_ru.qm
%doc %{_datadir}/%{name}/CHANGELOG.md
%license %{_datadir}/%{name}/license.txt

%{_datadir}/icons/hicolor/*/apps/*.png
%{_datadir}/applications/*.desktop

%files doc
%doc doc

%changelog
%autochangelog
