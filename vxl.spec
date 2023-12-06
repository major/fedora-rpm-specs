%undefine __cmake_in_source_build

Name:       vxl
Version:    2.0.2
Release:    %autorelease
Summary:    C++ Libraries for Computer Vision Research and Implementation
License:    BSD
URL:        https://vxl.github.io/
# Need to remove the non-free lena image from the sources
# tar xf vxl-%%{version}.tar.gz
# rm -rf vxl-%%{version}/contrib/prip/vdtop/tests/lena.org.pgm
# tar cfz vxl-%%{version}-clean.tar.gz vxl-%%{version}/
# Source0:  https://github.com/vxl/vxl/archive/v%%{version}/%%{name}-%%{version}.tar.gz
Source0:    %{name}-%{version}-clean.tar.gz

# Patches generated from tree here:
# https://github.com/sanjayankur31/vxl/tree/fedora-v2.0.2-f32
# use system rply and don't use mpeg2
Patch1:     0001-v2.0.2-unbundle-rply.patch
Patch2:     0002-v2.0.2-Use-Fedora-expat-and-expatpp.patch
Patch3:     0003-v2.0.2-Use-Fedora-minizip.patch
# Submitted upstream https://github.com/vxl/vxl/pull/626
Patch4:     0004-v2.0.2-Version-shared-objects.patch
Patch5:     0005-v2.0.2-Add-cmake-module-to-find-RPLY.patch
Patch6:     0006-v2.0.2-bbas-baio-Update-function-arguments-in-declar.patch
Patch7:     0007-v2.0.2-fix-bkml-test.patch
Patch8:     0008-v2.0.2-Correct-rply-includedir.patch

# Fixes https://github.com/vxl/vxl/issues/638
# Thanks jjames@fedoraproject.org for pointing it out
Patch9:     0001-BUG-Logic-for-conditional-compilation-was-exactly-wr.patch

# Remove obsolete boxm library that fails to build on ARM
# https://github.com/vxl/vxl/commit/cdf414000606af4bad322f7ff4c1fcdeaaa286ad
Patch10:    0009-removed-the-obsolete-octree-library-boxm.patch

# Fix missing #include caught by gcc-11
Patch11:     0010-gcc11.patch

BuildRequires:  cmake
BuildRequires:  Coin2-devel
BuildRequires:  doxygen
BuildRequires:  expat-devel
BuildRequires:  expatpp-devel
BuildRequires:  freeglut-devel
BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  git
# Use bundled dcmtk until upstream updates their code to use newer dcmtk
# https://github.com/vxl/vxl/issues/550
# BuildRequires:  dcmtk-devel
BuildRequires:  libpng-devel
BuildRequires:  libtiff-devel
BuildRequires:  libXmu-devel
BuildRequires:  libXi-devel
BuildRequires:  libjpeg-devel
%ifnarch s390 s390x
BuildRequires:  libdc1394-devel
%endif
BuildRequires:  libgeotiff-devel
BuildRequires:  libjpeg-turbo-devel
BuildRequires:  minizip-ng-compat-devel
# Does not build with latest version
# https://github.com/vxl/vxl/issues/627
# BuildRequires:  openjpeg2-devel

# Py2 only from the looks of it
# BuildRequires:  python3-devel

BuildRequires:  rply-devel
BuildRequires:  SIMVoleon-devel
BuildRequires:  shapelib-devel
BuildRequires:  texi2html
BuildRequires:  zlib-devel

# Bundled
Provides:  bundled(libopenjpeg2) = 2.0.0

#GUI needs wx, a desktop file and an icon

%description
VXL (the Vision-something-Libraries) is a collection of C++ libraries designed
for computer vision research and implementation. It was created from TargetJr
and the IUE with the aim of making a light, fast and consistent system.
VXL is written in ANSI/ISO C++ and is designed to be portable over many
platforms.


%package    doc
Summary:    Documentation for VXL library
BuildArch:  noarch

%description doc

You should install this package if you would like to
have all the documentation

%package    devel
Summary:    Headers and development libraries for VXL
Requires:   %{name}%{?_isa} = %{version}-%{release}

%description devel

You should install this package if you would like to
develop code based on VXL.

%prep
%autosetup -S git

# Remove bundled library (let's use FEDORA's ones)
# v3p/netlib (made by f2c) dependency not removed because of heavily modifications
# QV is a Silicon Graphics' VRML parser from the 90s. Now unmantained.

# Bundled: dcmtk
# Requires VXL_FORCE_V3P_DCMTK:BOOL=ON

# Also bundled: openjpeg2
# Requires VXL_FORCE_V3P_OPENJPEG2:BOOL=ON \
# Also may be needed
# -DOPENJPEG2_INCLUDE_DIR:PATH=%%{_includedir}/openjpeg-2.3 \
# -DOPENJPEG2_LIBRARIES:PATH=%%{_libdir}/libopenjp2.so \


# for l in jpeg png zlib tiff geotiff rply dcmtk bzlib openjpeg2
for l in jpeg png zlib tiff geotiff bzlib
do
    find v3p/$l -type f ! -name 'CMakeLists.txt' -execdir rm {} +
done

find contrib/brl/b3p/shapelib -type f ! -name 'CMakeLists.txt' -execdir rm {} +
find contrib/brl/b3p/minizip -type f ! -name 'CMakeLists.txt' -execdir rm {} +
find contrib/brl/b3p/expat -type f ! -name 'CMakeLists.txt' -execdir rm {} +
find contrib/brl/b3p/expatpp -type f ! -name 'CMakeLists.txt' -execdir rm {} +

# v3p/mpeg2 lib in fedora is not enough to build the target. Moreover it is in rpmfusion repo

# Fix executable permissions on source file
# not using "." for find since it sometimes crashes within the .git folder
for f in config contrib core scripts v3p vcl; do
    find $f -name "*.h" -execdir chmod -x '{}' \;
    find $f -name "*.cxx" -execdir chmod -x '{}' \;
    find $f -name "*.txx" -execdir chmod -x '{}' \;
done

# Do not use bundled minizip
sed -i '/add_subdirectory(minizip)/ d' contrib/brl/b3p/CMakeLists.txt

%build
%cmake -DVXL_INSTALL_LIBRARY_DIR:PATH=%{_lib} \
    -DBUILD_SHARED_LIBS:BOOL=ON \
    -DVXL_USE_GEOTIFF:BOOL=ON \
    -DVXL_FORCE_B3P_EXPAT:BOOL=OFF \
    -DVXL_FORCE_V3P_DCMTK:BOOL=ON \
    -DVXL_FORCE_V3P_GEOTIFF:BOOL=OFF \
    -DVXL_FORCE_V3P_JPEG:BOOL=OFF \
    -DVXL_FORCE_V3P_PNG:BOOL=OFF \
    -DVXL_FORCE_V3P_TIFF:BOOL=OFF \
    -DVXL_FORCE_V3P_ZLIB:BOOL=OFF \
    -DVXL_FORCE_V3P_RPLY:BOOL=OFF \
    -DVXL_FORCE_V3P_OPENJPEG2:BOOL=ON \
    -DVXL_USING_NATIVE_ZLIB:BOOL=ON \
    -DVXL_USING_NATIVE_JPEG:BOOL=ON \
    -DVXL_USING_NATIVE_PNG:BOOL=ON \
    -DVXL_USING_NATIVE_TIFF:BOOL=ON \
    -DVXL_USING_NATIVE_GEOTIFF:BOOL=ON \
    -DVXL_USING_NATIVE_EXPAT:BOOL=ON \
    -DVXL_USING_NATIVE_EXPATPP:BOOL=ON \
    -DVXL_USING_NATIVE_SHAPELIB:BOOL=ON \
    -DVXL_USING_NATIVE_BZLIB2:BOOL=ON \
    -DVXL_BUILD_VGUI:BOOL=OFF \
    -DVXL_BUILD_BGUI3D:BOOL=OFF \
    -DVXL_BUILD_OXL:BOOL=ON \
    -DVXL_BUILD_BRL:BOOL=ON \
    -DVXL_BUILD_BRL_PYTHON:BOOL=OFF \
    -DVXL_BUILD_GEL:BOOL=ON \
    -DVXL_BUILD_PRIP:BOOL=ON \
    -DVXL_BUILD_CONVERSIONS:BOOL=ON \
    -DVXL_BUILD_CUL:BOOL=ON \
    -DVXL_BUILD_RPL:BOOL=ON \
    -DVXL_BUILD_CONTRIB:BOOL=ON \
    -DVXL_BUILD_CORE_SERIALISATION:BOOL=ON \
    -DVXL_BUILD_CORE_GEOMETRY:BOOL=ON \
    -DVXL_BUILD_CORE_IMAGING:BOOL=ON \
    -DVXL_BUILD_CORE_NUMERICS:BOOL=ON \
    -DVXL_BUILD_CORE_PROBABILITY:BOOL=ON \
    -DVXL_BUILD_CORE_UTILITIES:BOOL=ON \
    -DVXL_BUILD_CORE_VIDEO:BOOL=ON \
    -DVXL_BUILD_EXAMPLES:BOOL=OFF \
    -DBUILD_TESTING:BOOL=ON \
    -DVXL_BUILD_DOCUMENTATION:BOOL=ON \
    -DCMAKE_BUILD_TYPE:STRING="RelWithDebInfo" \
    -DCMAKE_CXX_FLAGS:STRING="$RPM_OPT_FLAGS -fpermissive" \
    -DVNL_CONFIG_LEGACY_METHODS:BOOL=ON

# Other stuff
# -DEXPATPP_INCLUDE_DIR:PATH=%%{_includedir} \
# -DEXPATPP_LIBRARY:PATH=%%{_libdir}/libexpatpp.so \
# -DPYTHON_LIBRARY=/usr/lib64/libpython2.7.so \

# These comments from older spec versions need verification:
#BUILD_VGUI? NO, it depends on box2m which in turns relies on OPENCL which is not available in FEDORA
#wxwidgets seems to be found
#Multiple versions of QT found please set DESIRED_QT_VERSION

%cmake_build

%install
%cmake_install

# Stray file installed in a random location
rm -fv %{buildroot}/usr/contrib/brl/bseg/boxm2/ocl/boxm2_ocl_where_root_dir.h

%check
# 5/985 fail:
# 713 - bil_algo_test_detect_ridges (SEGFAULT)
# 781 - bkml_test_bkml (Child aborted)
# 801 - volm_test_candidate_region_parser (Child aborted)
# 967 - vifa_test_int_faces_attr (Child aborted)
# 968 - vifa_test_int_faces_adj_attr (Child aborted)
ctest %{_vpath_builddir} || exit 0

%ldconfig_scriptlets

%files
%doc core/vxl_copyright.h
%{_bindir}/octree
%{_libdir}/libclipper.so.2.0
%{_libdir}/libtestlib.so.2.0
%{_libdir}/libvcl.so.2.0
%{_libdir}/libvgl.so.2.0
%{_libdir}/libvidl.so.2.0
%{_libdir}/libvil_io.so.2.0
%{_libdir}/libvnl.so.2.0
%{_libdir}/libvpgl_file_formats.so.2.0
%{_libdir}/libvpl.so.2.0
%{_libdir}/libclipper.so.2.0.2
%{_libdir}/libtestlib.so.2.0.2
%{_libdir}/libvcl.so.2.0.2
%{_libdir}/libvgl.so.2.0.2
%{_libdir}/libvidl.so.2.0.2
%{_libdir}/libvil_io.so.2.0.2
%{_libdir}/libvnl.so.2.0.2
%{_libdir}/libvpgl_file_formats.so.2.0.2
%{_libdir}/libvpl.so.2.0.2
%{_libdir}/libnetlib.so.2.0
%{_libdir}/libv3p_netlib.so.2.0
%{_libdir}/libvcsl.so.2.0
%{_libdir}/libvgl_xio.so.2.0
%{_libdir}/libvil.so.2.0
%{_libdir}/libvnl_xio.so.2.0
%{_libdir}/libvpgl_io.so.2.0
%{_libdir}/libvsl.so.2.0
%{_libdir}/libnetlib.so.2.0.2
%{_libdir}/libv3p_netlib.so.2.0.2
%{_libdir}/libvcsl.so.2.0.2
%{_libdir}/libvgl_xio.so.2.0.2
%{_libdir}/libvil.so.2.0.2
%{_libdir}/libvnl_xio.so.2.0.2
%{_libdir}/libvpgl_io.so.2.0.2
%{_libdir}/libvsl.so.2.0.2
%{_libdir}/libvbl_io.so.2.0
%{_libdir}/libvgl_algo.so.2.0
%{_libdir}/libvil1.so.2.0
%{_libdir}/libvnl_algo.so.2.0
%{_libdir}/libvpdl.so.2.0
%{_libdir}/libvpgl.so.2.0
%{_libdir}/libvul_io.so.2.0
%{_libdir}/libvbl_io.so.2.0.2
%{_libdir}/libvgl_algo.so.2.0.2
%{_libdir}/libvil1.so.2.0.2
%{_libdir}/libvnl_algo.so.2.0.2
%{_libdir}/libvpdl.so.2.0.2
%{_libdir}/libvpgl.so.2.0.2
%{_libdir}/libvul_io.so.2.0.2
%{_libdir}/libvbl.so.2.0
%{_libdir}/libvgl_io.so.2.0
%{_libdir}/libvil_algo.so.2.0
%{_libdir}/libvnl_io.so.2.0
%{_libdir}/libvpgl_algo.so.2.0
%{_libdir}/libvpgl_xio.so.2.0
%{_libdir}/libvul.so.2.0
%{_libdir}/libvbl.so.2.0.2
%{_libdir}/libvgl_io.so.2.0.2
%{_libdir}/libvil_algo.so.2.0.2
%{_libdir}/libvnl_io.so.2.0.2
%{_libdir}/libvpgl_algo.so.2.0.2
%{_libdir}/libvpgl_xio.so.2.0.2
%{_libdir}/libvul.so.2.0.2
%{_libdir}/libbaio.so.2.0
%{_libdir}/libbaio.so.2.0.2
%{_libdir}/libbaml.so.2.0
%{_libdir}/libbaml.so.2.0.2
%{_libdir}/libbapl.so.2.0
%{_libdir}/libbapl.so.2.0.2
%{_libdir}/libbapl_io.so.2.0
%{_libdir}/libbapl_io.so.2.0.2
%{_libdir}/libbapl_pro.so.2.0
%{_libdir}/libbapl_pro.so.2.0.2
%{_libdir}/libbbas_pro.so.2.0
%{_libdir}/libbbas_pro.so.2.0.2
%{_libdir}/libbbgm.so.2.0
%{_libdir}/libbbgm.so.2.0.2
%{_libdir}/libbbgm_pro.so.2.0
%{_libdir}/libbbgm_pro.so.2.0.2
%{_libdir}/libbcvr.so.2.0
%{_libdir}/libbcvr.so.2.0.2
%{_libdir}/libbdgl.so.2.0
%{_libdir}/libbdgl.so.2.0.2
%{_libdir}/libbdpg.so.2.0
%{_libdir}/libbdpg.so.2.0.2
%{_libdir}/libbetr.so.2.0
%{_libdir}/libbetr.so.2.0.2
%{_libdir}/libbetr_pro.so.2.0
%{_libdir}/libbetr_pro.so.2.0.2
%{_libdir}/libbgrl.so.2.0
%{_libdir}/libbgrl.so.2.0.2
%{_libdir}/libbgrl2.so.2.0
%{_libdir}/libbgrl2.so.2.0.2
%{_libdir}/libbgrl2_algo.so.2.0
%{_libdir}/libbgrl2_algo.so.2.0.2
%{_libdir}/libbil.so.2.0
%{_libdir}/libbil.so.2.0.2
%{_libdir}/libbil_algo.so.2.0
%{_libdir}/libbil_algo.so.2.0.2
%{_libdir}/libbjson.so.2.0
%{_libdir}/libbjson.so.2.0.2
%{_libdir}/libbkml.so.2.0
%{_libdir}/libbkml.so.2.0.2
%{_libdir}/libbmdl.so.2.0
%{_libdir}/libbmdl.so.2.0.2
%{_libdir}/libbmdl_pro.so.2.0
%{_libdir}/libbmdl_pro.so.2.0.2
%{_libdir}/libbmsh3d.so.2.0
%{_libdir}/libbmsh3d.so.2.0.2
%{_libdir}/libbmsh3d_algo.so.2.0
%{_libdir}/libbmsh3d_algo.so.2.0.2
%{_libdir}/libbmsh3d_pro.so.2.0
%{_libdir}/libbmsh3d_pro.so.2.0.2
%{_libdir}/libbnabo.so.2.0
%{_libdir}/libbnabo.so.2.0.2
%{_libdir}/libbnl.so.2.0
%{_libdir}/libbnl.so.2.0.2
%{_libdir}/libbnl_algo.so.2.0
%{_libdir}/libbnl_algo.so.2.0.2
%{_libdir}/libboct.so.2.0
%{_libdir}/libboct.so.2.0.2
%{_libdir}/libboxm2.so.2.0
%{_libdir}/libboxm2.so.2.0.2
%{_libdir}/libboxm2_basic.so.2.0
%{_libdir}/libboxm2_basic.so.2.0.2
%{_libdir}/libboxm2_class.so.2.0
%{_libdir}/libboxm2_class.so.2.0.2
%{_libdir}/libboxm2_cpp.so.2.0
%{_libdir}/libboxm2_cpp.so.2.0.2
%{_libdir}/libboxm2_cpp_algo.so.2.0
%{_libdir}/libboxm2_cpp_algo.so.2.0.2
%{_libdir}/libboxm2_cpp_pro.so.2.0
%{_libdir}/libboxm2_cpp_pro.so.2.0.2
%{_libdir}/libboxm2_io.so.2.0
%{_libdir}/libboxm2_io.so.2.0.2
%{_libdir}/libboxm2_pro.so.2.0
%{_libdir}/libboxm2_pro.so.2.0.2
%{_libdir}/libboxm2_util.so.2.0
%{_libdir}/libboxm2_util.so.2.0.2
%{_libdir}/libboxm2_vecf.so.2.0
%{_libdir}/libboxm2_vecf.so.2.0.2
%{_libdir}/libboxm2_volm.so.2.0
%{_libdir}/libboxm2_volm.so.2.0.2
%{_libdir}/libboxm2_volm_conf.so.2.0
%{_libdir}/libboxm2_volm_conf.so.2.0.2
%{_libdir}/libboxm2_volm_desc.so.2.0
%{_libdir}/libboxm2_volm_desc.so.2.0.2
%{_libdir}/libboxm2_volm_io.so.2.0
%{_libdir}/libboxm2_volm_io.so.2.0.2
%{_libdir}/libboxm2_volm_pro.so.2.0
%{_libdir}/libboxm2_volm_pro.so.2.0.2
%{_libdir}/libbpgl.so.2.0
%{_libdir}/libbpgl.so.2.0.2
%{_libdir}/libbpgl_algo.so.2.0
%{_libdir}/libbpgl_algo.so.2.0.2
%{_libdir}/libbprb.so.2.0
%{_libdir}/libbprb.so.2.0.2
%{_libdir}/libbrad.so.2.0
%{_libdir}/libbrad.so.2.0.2
%{_libdir}/libbrad_io.so.2.0
%{_libdir}/libbrad_io.so.2.0.2
%{_libdir}/libbrad_pro.so.2.0
%{_libdir}/libbrad_pro.so.2.0.2
%{_libdir}/libbrdb.so.2.0
%{_libdir}/libbrdb.so.2.0.2
%{_libdir}/libbrec.so.2.0
%{_libdir}/libbrec.so.2.0.2
%{_libdir}/libbrec_pro.so.2.0
%{_libdir}/libbrec_pro.so.2.0.2
%{_libdir}/libbreg3d.so.2.0
%{_libdir}/libbreg3d.so.2.0.2
%{_libdir}/libbreg3d_pro.so.2.0
%{_libdir}/libbreg3d_pro.so.2.0.2
%{_libdir}/libbrip.so.2.0
%{_libdir}/libbrip.so.2.0.2
%{_libdir}/libbrip_pro.so.2.0
%{_libdir}/libbrip_pro.so.2.0.2
%{_libdir}/libbsgm.so.2.0
%{_libdir}/libbsgm.so.2.0.2
%{_libdir}/libbsgm_pro.so.2.0
%{_libdir}/libbsgm_pro.so.2.0.2
%{_libdir}/libbsl.so.2.0
%{_libdir}/libbsl.so.2.0.2
%{_libdir}/libbsol.so.2.0
%{_libdir}/libbsol.so.2.0.2
%{_libdir}/libbsta.so.2.0
%{_libdir}/libbsta.so.2.0.2
%{_libdir}/libbsta_algo.so.2.0
%{_libdir}/libbsta_algo.so.2.0.2
%{_libdir}/libbsta_io.so.2.0
%{_libdir}/libbsta_io.so.2.0.2
%{_libdir}/libbsta_pro.so.2.0
%{_libdir}/libbsta_pro.so.2.0.2
%{_libdir}/libbsta_vis.so.2.0
%{_libdir}/libbsta_vis.so.2.0.2
%{_libdir}/libbstm.so.2.0
%{_libdir}/libbstm.so.2.0.2
%{_libdir}/libbstm_basic.so.2.0
%{_libdir}/libbstm_basic.so.2.0.2
%{_libdir}/libbstm_cpp_algo.so.2.0
%{_libdir}/libbstm_cpp_algo.so.2.0.2
%{_libdir}/libbstm_cpp_pro.so.2.0
%{_libdir}/libbstm_cpp_pro.so.2.0.2
%{_libdir}/libbstm_io.so.2.0
%{_libdir}/libbstm_io.so.2.0.2
%{_libdir}/libbstm_multi.so.2.0
%{_libdir}/libbstm_multi.so.2.0.2
%{_libdir}/libbstm_multi_basic.so.2.0
%{_libdir}/libbstm_multi_basic.so.2.0.2
%{_libdir}/libbstm_multi_io.so.2.0
%{_libdir}/libbstm_multi_io.so.2.0.2
%{_libdir}/libbstm_pro.so.2.0
%{_libdir}/libbstm_pro.so.2.0.2
%{_libdir}/libbstm_util.so.2.0
%{_libdir}/libbstm_util.so.2.0.2
%{_libdir}/libbsvg.so.2.0
%{_libdir}/libbsvg.so.2.0.2
%{_libdir}/libbsvg_pro.so.2.0
%{_libdir}/libbsvg_pro.so.2.0.2
%{_libdir}/libbtol.so.2.0
%{_libdir}/libbtol.so.2.0.2
%{_libdir}/libbugl.so.2.0
%{_libdir}/libbugl.so.2.0.2
%{_libdir}/libbundler.so.2.0
%{_libdir}/libbundler.so.2.0.2
%{_libdir}/libbvgl.so.2.0
%{_libdir}/libbvgl.so.2.0.2
%{_libdir}/libbvgl_algo.so.2.0
%{_libdir}/libbvgl_algo.so.2.0.2
%{_libdir}/libbvgl_pro.so.2.0
%{_libdir}/libbvgl_pro.so.2.0.2
%{_libdir}/libbvpl.so.2.0
%{_libdir}/libbvpl.so.2.0.2
%{_libdir}/libbvpl_functors.so.2.0
%{_libdir}/libbvpl_functors.so.2.0.2
%{_libdir}/libbvpl_kernels.so.2.0
%{_libdir}/libbvpl_kernels.so.2.0.2
%{_libdir}/libbvpl_kernels_io.so.2.0
%{_libdir}/libbvpl_kernels_io.so.2.0.2
%{_libdir}/libbvpl_kernels_pro.so.2.0
%{_libdir}/libbvpl_kernels_pro.so.2.0.2
%{_libdir}/libbvpl_pro.so.2.0
%{_libdir}/libbvpl_pro.so.2.0.2
%{_libdir}/libbvpl_util.so.2.0
%{_libdir}/libbvpl_util.so.2.0.2
%{_libdir}/libbvpl_util_io.so.2.0
%{_libdir}/libbvpl_util_io.so.2.0.2
%{_libdir}/libbvrml.so.2.0
%{_libdir}/libbvrml.so.2.0.2
%{_libdir}/libbvrml_pro.so.2.0
%{_libdir}/libbvrml_pro.so.2.0.2
%{_libdir}/libbvxm.so.2.0
%{_libdir}/libbvxm.so.2.0.2
%{_libdir}/libbvxm_algo.so.2.0
%{_libdir}/libbvxm_algo.so.2.0.2
%{_libdir}/libbvxm_algo_pro.so.2.0
%{_libdir}/libbvxm_algo_pro.so.2.0.2
%{_libdir}/libbvxm_grid.so.2.0
%{_libdir}/libbvxm_grid.so.2.0.2
%{_libdir}/libbvxm_grid_io.so.2.0
%{_libdir}/libbvxm_grid_io.so.2.0.2
%{_libdir}/libbvxm_grid_pro.so.2.0
%{_libdir}/libbvxm_grid_pro.so.2.0.2
%{_libdir}/libbvxm_io.so.2.0
%{_libdir}/libbvxm_io.so.2.0.2
%{_libdir}/libbvxm_pro.so.2.0
%{_libdir}/libbvxm_pro.so.2.0.2
%{_libdir}/libbwm_video.so.2.0
%{_libdir}/libbwm_video.so.2.0.2
%{_libdir}/libbxml.so.2.0
%{_libdir}/libbxml.so.2.0.2
%{_libdir}/libclsfy.so.2.0
%{_libdir}/libclsfy.so.2.0.2
%{_libdir}/libdepth_map.so.2.0
%{_libdir}/libdepth_map.so.2.0.2
%{_libdir}/libfhs.so.2.0
%{_libdir}/libfhs.so.2.0.2
%{_libdir}/libgeml.so.2.0
%{_libdir}/libgeml.so.2.0.2
%{_libdir}/libgevd.so.2.0
%{_libdir}/libgevd.so.2.0.2
%{_libdir}/libgmvl.so.2.0
%{_libdir}/libgmvl.so.2.0.2
%{_libdir}/libgst.so.2.0
%{_libdir}/libgst.so.2.0.2
%{_libdir}/libgtrl.so.2.0
%{_libdir}/libgtrl.so.2.0.2
%{_libdir}/libicam.so.2.0
%{_libdir}/libicam.so.2.0.2
%{_libdir}/libicam_pro.so.2.0
%{_libdir}/libicam_pro.so.2.0.2
%{_libdir}/libihog.so.2.0
%{_libdir}/libihog.so.2.0.2
%{_libdir}/libihog_pro.so.2.0
%{_libdir}/libihog_pro.so.2.0.2
%{_libdir}/libimesh.so.2.0
%{_libdir}/libimesh.so.2.0.2
%{_libdir}/libimesh_algo.so.2.0
%{_libdir}/libimesh_algo.so.2.0.2
%{_libdir}/libipts.so.2.0
%{_libdir}/libipts.so.2.0.2
%{_libdir}/libm23d.so.2.0
%{_libdir}/libm23d.so.2.0.2
%{_libdir}/libmbl.so.2.0
%{_libdir}/libmbl.so.2.0.2
%{_libdir}/libmcal.so.2.0
%{_libdir}/libmcal.so.2.0.2
%{_libdir}/libmfpf.so.2.0
%{_libdir}/libmfpf.so.2.0.2
%{_libdir}/libmipa.so.2.0
%{_libdir}/libmipa.so.2.0.2
%{_libdir}/libmmn.so.2.0
%{_libdir}/libmmn.so.2.0.2
%{_libdir}/libmsdi.so.2.0
%{_libdir}/libmsdi.so.2.0.2
%{_libdir}/libmsm.so.2.0
%{_libdir}/libmsm.so.2.0.2
%{_libdir}/libmsm_utils.so.2.0
%{_libdir}/libmsm_utils.so.2.0.2
%{_libdir}/libmvl.so.2.0
%{_libdir}/libmvl.so.2.0.2
%{_libdir}/libmvl2.so.2.0
%{_libdir}/libmvl2.so.2.0.2
%{_libdir}/libosl.so.2.0
%{_libdir}/libosl.so.2.0.2
%{_libdir}/libouel.so.2.0
%{_libdir}/libouel.so.2.0.2
%{_libdir}/libouml.so.2.0
%{_libdir}/libouml.so.2.0.2
%{_libdir}/liboxl_vrml.so.2.0
%{_libdir}/liboxl_vrml.so.2.0.2
%{_libdir}/libpdf1d.so.2.0
%{_libdir}/libpdf1d.so.2.0.2
%{_libdir}/librgrl.so.2.0
%{_libdir}/librgrl.so.2.0.2
%{_libdir}/librrel.so.2.0
%{_libdir}/librrel.so.2.0.2
%{_libdir}/librsdl.so.2.0
%{_libdir}/librsdl.so.2.0.2
%{_libdir}/libsdet.so.2.0
%{_libdir}/libsdet.so.2.0.2
%{_libdir}/libsdet_pro.so.2.0
%{_libdir}/libsdet_pro.so.2.0.2
%{_libdir}/libvcon_pro.so.2.0
%{_libdir}/libvcon_pro.so.2.0.2
%{_libdir}/libvdgl.so.2.0
%{_libdir}/libvdgl.so.2.0.2
%{_libdir}/libvdtop.so.2.0
%{_libdir}/libvdtop.so.2.0.2
%{_libdir}/libvepl.so.2.0
%{_libdir}/libvepl.so.2.0.2
%{_libdir}/libvidl_pro.so.2.0
%{_libdir}/libvidl_pro.so.2.0.2
%{_libdir}/libvifa.so.2.0
%{_libdir}/libvifa.so.2.0.2
%{_libdir}/libvil3d.so.2.0
%{_libdir}/libvil3d.so.2.0.2
%{_libdir}/libvil3d_algo.so.2.0
%{_libdir}/libvil3d_algo.so.2.0.2
%{_libdir}/libvil3d_io.so.2.0
%{_libdir}/libvil3d_io.so.2.0.2
%{_libdir}/libvil_pro.so.2.0
%{_libdir}/libvil_pro.so.2.0.2
%{_libdir}/libvimt.so.2.0
%{_libdir}/libvimt.so.2.0.2
%{_libdir}/libvimt3d.so.2.0
%{_libdir}/libvimt3d.so.2.0.2
%{_libdir}/libvimt_algo.so.2.0
%{_libdir}/libvimt_algo.so.2.0.2
%{_libdir}/libvipl.so.2.0
%{_libdir}/libvipl.so.2.0.2
%{_libdir}/libvmal.so.2.0
%{_libdir}/libvmal.so.2.0.2
%{_libdir}/libvmap.so.2.0
%{_libdir}/libvmap.so.2.0.2
%{_libdir}/libvolm.so.2.0
%{_libdir}/libvolm.so.2.0.2
%{_libdir}/libvolm_conf.so.2.0
%{_libdir}/libvolm_conf.so.2.0.2
%{_libdir}/libvolm_desc.so.2.0
%{_libdir}/libvolm_desc.so.2.0.2
%{_libdir}/libvolm_pro.so.2.0
%{_libdir}/libvolm_pro.so.2.0.2
%{_libdir}/libvpdfl.so.2.0
%{_libdir}/libvpdfl.so.2.0.2
%{_libdir}/libvpgl_pro.so.2.0
%{_libdir}/libvpgl_pro.so.2.0.2
%{_libdir}/libvpyr.so.2.0
%{_libdir}/libvpyr.so.2.0.2
%{_libdir}/libvsol.so.2.0
%{_libdir}/libvsol.so.2.0.2
%{_libdir}/libvsph.so.2.0
%{_libdir}/libvsph.so.2.0.2
%{_libdir}/libvtol.so.2.0
%{_libdir}/libvtol.so.2.0.2
%{_libdir}/libvtol_algo.so.2.0
%{_libdir}/libvtol_algo.so.2.0.2
# Bundles
%{_libdir}/libopenjpeg2.so.2.0
%{_libdir}/libopenjpeg2.so.2.0.0

%files devel
%{_datadir}/%{name}
%{_includedir}/%{name}
%{_libdir}/libclipper.so
%{_libdir}/libvbl_io.so
%{_libdir}/libvcsl.so
%{_libdir}/libvgl.so
%{_libdir}/libvil_algo.so
%{_libdir}/libvnl_algo.so
%{_libdir}/libvnl_xio.so
%{_libdir}/libvpgl_file_formats.so
%{_libdir}/libvpgl_xio.so
%{_libdir}/libvul_io.so
%{_libdir}/libnetlib.so
%{_libdir}/libtestlib.so
%{_libdir}/libvbl.so
%{_libdir}/libvgl_algo.so
%{_libdir}/libvgl_xio.so
%{_libdir}/libvil_io.so
%{_libdir}/libvnl_io.so
%{_libdir}/libvpdl.so
%{_libdir}/libvpgl_io.so
%{_libdir}/libvpl.so
%{_libdir}/libvul.so
%{_libdir}/libopenjpeg2.so
%{_libdir}/libv3p_netlib.so
%{_libdir}/libvcl.so
%{_libdir}/libvgl_io.so
%{_libdir}/libvidl.so
%{_libdir}/libvil1.so
%{_libdir}/libvil.so
%{_libdir}/libvnl.so
%{_libdir}/libvpgl_algo.so
%{_libdir}/libvpgl.so
%{_libdir}/libmipa.so
%{_libdir}/libmfpf.so
%{_libdir}/libmcal.so
%{_libdir}/libmbl.so
%{_libdir}/libm23d.so
%{_libdir}/libipts.so
%{_libdir}/libimesh_algo.so
%{_libdir}/libimesh.so
%{_libdir}/libihog_pro.so
%{_libdir}/libihog.so
%{_libdir}/libicam_pro.so
%{_libdir}/libicam.so
%{_libdir}/libgst.so
%{_libdir}/libgmvl.so
%{_libdir}/libgevd.so
%{_libdir}/libgtrl.so
%{_libdir}/libgeml.so
%{_libdir}/libfhs.so
%{_libdir}/libdepth_map.so
%{_libdir}/libclsfy.so
%{_libdir}/libbxml.so
%{_libdir}/libbwm_video.so
%{_libdir}/libbvxm_pro.so
%{_libdir}/libbvxm_io.so
%{_libdir}/libbvxm_grid_pro.so
%{_libdir}/libbvxm_grid_io.so
%{_libdir}/libbvxm_grid.so
%{_libdir}/libbvxm_algo_pro.so
%{_libdir}/libbvxm_algo.so
%{_libdir}/libbvxm.so
%{_libdir}/libbvrml_pro.so
%{_libdir}/libbvrml.so
%{_libdir}/libbvpl_util_io.so
%{_libdir}/libbvpl_util.so
%{_libdir}/libbvpl_pro.so
%{_libdir}/libbvpl_kernels_pro.so
%{_libdir}/libbvpl_kernels_io.so
%{_libdir}/libbvpl_kernels.so
%{_libdir}/libbvpl_functors.so
%{_libdir}/libbvpl.so
%{_libdir}/libvsl.so
%{_libdir}/libbvgl_pro.so
%{_libdir}/libbvgl_algo.so
%{_libdir}/libbvgl.so
%{_libdir}/libbundler.so
%{_libdir}/libbugl.so
%{_libdir}/libbtol.so
%{_libdir}/libbsvg_pro.so
%{_libdir}/libbsvg.so
%{_libdir}/libbstm_util.so
%{_libdir}/libbstm_pro.so
%{_libdir}/libbstm_multi_io.so
%{_libdir}/libbstm_multi_basic.so
%{_libdir}/libbstm_multi.so
%{_libdir}/libbstm_io.so
%{_libdir}/libbstm_cpp_pro.so
%{_libdir}/libbstm_cpp_algo.so
%{_libdir}/libbstm_basic.so
%{_libdir}/libbstm.so
%{_libdir}/libbsta_vis.so
%{_libdir}/libbsta_pro.so
%{_libdir}/libbsta_io.so
%{_libdir}/libbsta_algo.so
%{_libdir}/libbsta.so
%{_libdir}/libbsol.so
%{_libdir}/libbsl.so
%{_libdir}/libbsgm_pro.so
%{_libdir}/libbsgm.so
%{_libdir}/libbrip_pro.so
%{_libdir}/libbrip.so
%{_libdir}/libbreg3d_pro.so
%{_libdir}/libbreg3d.so
%{_libdir}/libbrec_pro.so
%{_libdir}/libbrec.so
%{_libdir}/libbrdb.so
%{_libdir}/libbrad_pro.so
%{_libdir}/libbrad_io.so
%{_libdir}/libbrad.so
%{_libdir}/libbprb.so
%{_libdir}/libbpgl_algo.so
%{_libdir}/libbpgl.so
%{_libdir}/libboxm2_volm_pro.so
%{_libdir}/libboxm2_volm_io.so
%{_libdir}/libboxm2_volm_conf.so
%{_libdir}/libboxm2_volm.so
%{_libdir}/libboxm2_vecf.so
%{_libdir}/libboxm2_util.so
%{_libdir}/libboxm2_pro.so
%{_libdir}/libboxm2_io.so
%{_libdir}/libboxm2_cpp_pro.so
%{_libdir}/libboxm2_cpp_algo.so
%{_libdir}/libboxm2_cpp.so
%{_libdir}/libboxm2_class.so
%{_libdir}/libboxm2_basic.so
%{_libdir}/libboxm2.so
%{_libdir}/libboct.so
%{_libdir}/libbnl_algo.so
%{_libdir}/libbnl.so
%{_libdir}/libbnabo.so
%{_libdir}/libbmsh3d_pro.so
%{_libdir}/libbmsh3d_algo.so
%{_libdir}/libboxm2_volm_desc.so
%{_libdir}/libbmsh3d.so
%{_libdir}/libbmdl_pro.so
%{_libdir}/libbmdl.so
%{_libdir}/libbkml.so
%{_libdir}/libbjson.so
%{_libdir}/libbil_algo.so
%{_libdir}/libbil.so
%{_libdir}/libbgrl2_algo.so
%{_libdir}/libbgrl2.so
%{_libdir}/libbgrl.so
%{_libdir}/libbetr_pro.so
%{_libdir}/libbetr.so
%{_libdir}/libbdpg.so
%{_libdir}/libbdgl.so
%{_libdir}/libbcvr.so
%{_libdir}/libbbgm_pro.so
%{_libdir}/libbbgm.so
%{_libdir}/libbbas_pro.so
%{_libdir}/libbapl_pro.so
%{_libdir}/libbapl_io.so
%{_libdir}/libbapl.so
%{_libdir}/libbaml.so
%{_libdir}/libbaio.so
%{_libdir}/libmmn.so
%{_libdir}/libmsdi.so
%{_libdir}/libmsm.so
%{_libdir}/libmsm_utils.so
%{_libdir}/libmvl.so
%{_libdir}/libmvl2.so
%{_libdir}/libosl.so
%{_libdir}/libouel.so
%{_libdir}/libouml.so
%{_libdir}/liboxl_vrml.so
%{_libdir}/libpdf1d.so
%{_libdir}/librgrl.so
%{_libdir}/librrel.so
%{_libdir}/librsdl.so
%{_libdir}/libsdet.so
%{_libdir}/libsdet_pro.so
%{_libdir}/libvcon_pro.so
%{_libdir}/libvdgl.so
%{_libdir}/libvdtop.so
%{_libdir}/libvepl.so
%{_libdir}/libvidl_pro.so
%{_libdir}/libvifa.so
%{_libdir}/libvil3d.so
%{_libdir}/libvil3d_algo.so
%{_libdir}/libvil3d_io.so
%{_libdir}/libvil_pro.so
%{_libdir}/libvimt.so
%{_libdir}/libvimt3d.so
%{_libdir}/libvimt_algo.so
%{_libdir}/libvipl.so
%{_libdir}/libvmal.so
%{_libdir}/libvmap.so
%{_libdir}/libvolm.so
%{_libdir}/libvolm_conf.so
%{_libdir}/libvolm_desc.so
%{_libdir}/libvolm_pro.so
%{_libdir}/libvpdfl.so
%{_libdir}/libvpgl_pro.so
%{_libdir}/libvpyr.so
%{_libdir}/libvsol.so
%{_libdir}/libvsph.so
%{_libdir}/libvtol.so
%{_libdir}/libvtol_algo.so

%files doc
%doc core/vxl_copyright.h
%doc %{_docdir}/*

%changelog
%autochangelog
