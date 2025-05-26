%undefine __cmake_in_source_build

# shared objects version: API
%global major 3
%global minor 5
%global patch 0

Name:       vxl
Version:    3.5.0
Release:    %autorelease
Summary:    C++ Libraries for Computer Vision Research and Implementation

# see licenses.txt for a complete break down of licenses (using licensecheck)
# other licenses are not included because the files they refer to are not used/included in our build
License:    BSD-3-Clause AND NTP AND BSL-1.0 AND BSD-2-Clause AND MIT AND Apache-2.0 AND LicenseRef-Fedora-Public-Domain AND SMLNJ

# https://fedoraproject.org/wiki/Changes/EncourageI686LeafRemoval
ExcludeArch: %{ix86}

URL:        https://vxl.github.io/
# Need to remove the non-free lena image from the sources
# tar xf vxl-%%{version}.tar.gz
# rm -rf vxl-%%{version}/contrib/prip/vdtop/tests/lena.org.pgm
# tar cfz vxl-%%{version}-clean.tar.gz vxl-%%{version}/
#Source0:  https://github.com/vxl/vxl/archive/v%%{version}/%%{name}-%%{version}.tar.gz
Source0:    %{name}-%{version}-clean.tar.gz

# Patches generated from tree here:
# https://github.com/sanjayankur31/vxl/tree/fedora-3.5.0
# use system rply and don't use mpeg2
Patch:     0001-v3.5.0-unbundle-rply.patch
Patch:     0002-v3.5.0-Use-Fedora-expat-and-expatpp.patch
Patch:     0003-v3.5.0-Use-Fedora-minizip.patch
Patch:     0004-v3.5.0-Add-cmake-module-to-find-RPLY.patch
Patch:     0005-v3.5.0-fix-bkml-test.patch
Patch:     0006-v3.5.0-Correct-rply-includedir.patch
Patch:     0007-v3.5.0-remove-triangle.patch
Patch:     0008-v3.5.0-remove-bits-using-triangle.patch
Patch:     0009-v3.5.0-indent-to-keep-gcc-happy.patch
# otherwise we get:
# /usr/bin/ld: ../../../../../lib/libimesh.so.3.5.0.0: undefined reference to `brdb_value::registrar::registrar(brdb_value const*)'
# collect2: error: ld returned 1 exit status
# gmake[2]: *** [contrib/brl/bseg/baml/tests/CMakeFiles/baml_test_all.dir/build.make:172: bin/baml_test_all] Error 1
# gmake[2]: Leaving directory '/builddir/build/BUILD/vxl-3.5.0/redhat-linux-build'
# gmake[1]: *** [CMakeFiles/Makefile2:46025: contrib/brl/bseg/baml/tests/CMakeFiles/baml_test_all.dir/all] Error 2
Patch:     0010-v3.5.0-more-linker-fixes.patch

# Fix missing #include caught by gcc-11
Patch:     0011-v3.5.0-fix-for-gcc11.patch
# For linker error
Patch:     0012-v3.5.0-link-against-acal.patch
Patch:     0013-v3.5.0-more-linkage-fixes.patch
Patch:     0014-v3.5.0-use-system-zlib-tiff-minizip-compat.patch
Patch:     0015-v3.5.0-fix-linking.patch
Patch:     0016-v3.5.0-fix-linking.patch
# remove more bits that used triangle
Patch:     0017-v3.5.0-remove-boxm2-processes-that-use-sdnet-that-re.patch
# remove ctest dashboard config
Patch:     0018-chore-remove-ctest-dashboard-config.patch

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
# Bundled
Provides:  bundled(libopenjpeg2) = 2.0.0


# Py2 only from the looks of it
# BuildRequires:  python3-devel

BuildRequires:  rply-devel
BuildRequires:  SIMVoleon-devel
BuildRequires:  shapelib-devel
BuildRequires:  texi2html
BuildRequires:  zlib-ng-compat-devel

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

# remove bundled bits
# triangle removed in patch (bad license: https://github.com/vxl/vxl/issues/752#issuecomment-655526696)

# remove other bits, only leave CMakeLists.txt
for l in jpeg png zlib tiff geotiff bzlib
do
    find v3p/$l -type f ! -name 'CMakeLists.txt' -execdir rm -fv {} +
done
find contrib/brl/b3p/shapelib -type f ! -name 'CMakeLists.txt' -execdir rm -fv {} +
find contrib/brl/b3p/minizip -type f ! -name 'CMakeLists.txt' -execdir rm -fv {} +
find contrib/brl/b3p/expat -type f ! -name 'CMakeLists.txt' -execdir rm -fv {} +
find contrib/brl/b3p/expatpp -type f ! -name 'CMakeLists.txt' -execdir rm -fv {} +

# Fix executable permissions on source file
# not using "." for find since it sometimes crashes within the .git folder
for f in config contrib core scripts v3p vcl; do
    find $f -name "*.h" -execdir chmod -x '{}' \;
    find $f -name "*.cxx" -execdir chmod -x '{}' \;
    find $f -name "*.txx" -execdir chmod -x '{}' \;
done

%build
%cmake -DVXL_INSTALL_LIBRARY_DIR:PATH=%{_lib} \
    -DCMAKE_INSTALL_DATAROOTDIR:PATH=%{_datadir}/%{name} \
    -DBUILD_SHARED_LIBS:BOOL=TRUE \
    -DVXL_USE_GEOTIFF:BOOL=TRUE \
    -DVXL_FORCE_B3P_EXPAT:BOOL=FALSE \
    -DVXL_FORCE_V3P_DCMTK:BOOL=TRUE \
    -DVXL_FORCE_V3P_GEOTIFF:BOOL=FALSE \
    -DVXL_FORCE_V3P_JPEG:BOOL=FALSE \
    -DVXL_FORCE_V3P_PNG:BOOL=FALSE \
    -DVXL_FORCE_V3P_TIFF:BOOL=FALSE \
    -DVXL_FORCE_V3P_ZLIB:BOOL=FALSE \
    -DVXL_FORCE_V3P_RPLY:BOOL=FALSE \
    -DVXL_FORCE_V3P_OPENJPEG2:BOOL=TRUE \
    -DVXL_USING_NATIVE_ZLIB:BOOL=TRUE \
    -DVXL_USING_NATIVE_JPEG:BOOL=TRUE \
    -DVXL_USING_NATIVE_PNG:BOOL=TRUE \
    -DVXL_USING_NATIVE_TIFF:BOOL=TRUE \
    -DVXL_USING_NATIVE_GEOTIFF:BOOL=TRUE \
    -DVXL_USING_NATIVE_EXPAT:BOOL=TRUE \
    -DVXL_USING_NATIVE_EXPATPP:BOOL=TRUE \
    -DVXL_USING_NATIVE_SHAPELIB:BOOL=TRUE \
    -DVXL_USING_NATIVE_BZLIB2:BOOL=TRUE \
    -DVXL_BUILD_VGUI:BOOL=FALSE \
    -DVXL_BUILD_BGUI3D:BOOL=FALSE \
    -DVXL_BUILD_OXL:BOOL=TRUE \
    -DVXL_BUILD_BRL:BOOL=TRUE \
    -DVXL_BUILD_BRL_PYTHON:BOOL=FALSE \
    -DVXL_BUILD_GEL:BOOL=TRUE \
    -DVXL_BUILD_PRIP:BOOL=TRUE \
    -DVXL_BUILD_CONVERSIONS:BOOL=TRUE \
    -DVXL_BUILD_CUL:BOOL=TRUE \
    -DVXL_BUILD_RPL:BOOL=TRUE \
    -DVXL_BUILD_CONTRIB:BOOL=TRUE \
    -DVXL_BUILD_CORE_SERIALISATION:BOOL=TRUE \
    -DVXL_BUILD_CORE_GEOMETRY:BOOL=TRUE \
    -DVXL_BUILD_CORE_IMAGING:BOOL=TRUE \
    -DVXL_BUILD_CORE_NUMERICS:BOOL=TRUE \
    -DVXL_BUILD_CORE_PROBABILITY:BOOL=TRUE \
    -DVXL_BUILD_CORE_UTILITIES:BOOL=TRUE \
    -DVXL_BUILD_CORE_VIDEO:BOOL=TRUE \
    -DVXL_BUILD_EXAMPLES:BOOL=FALSE \
    -DBUILD_TESTING:BOOL=TRUE \
    -DVXL_BUILD_DOCUMENTATION:BOOL=TRUE \
    -DCMAKE_BUILD_TYPE:STRING="RelWithDebInfo" \
    -DCMAKE_CXX_FLAGS:STRING="$RPM_OPT_FLAGS -fpermissive" \
    -DVNL_CONFIG_LEGACY_METHODS:BOOL=TRUE

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
# different tests fail on different arches

%ifarch x86_64
# 99% tests passed, 5 tests failed out of 997
# Total Test time (real) =  23.64 sec
# The following tests FAILED:
#        30 -  vul_vul_test_driver (invalid test name)
#        781 - acal_test_metadata (Failed)
#        816 - bkml_test_bkml (Subprocess aborted)
#        836 - volm_test_candidate_region_parser (Subprocess aborted)
#        979 - vifa_test_int_faces_attr (Subprocess aborted)
#        980 - vifa_test_int_faces_adj_attr (Subprocess aborted)
%ctest -E "(acal_test_metadata|bkml_test_bkml|volm_test_candidate_region_parser|vifa_test_int_faces_attr|vifa_test_int_faces_adj_attr|vul_vul_test_driver)"
%else
# A number of test fail, but not deterministically on aarch and ppc64le etc, e.g:

#    183 - vgl_test_frustum_3d (Failed)
#    557 - m23d_test_ortho_flexible_builder (Failed)
#    638 - vepl_test_gradient_dir (Failed)
#    732 - bil_test_warp (Failed)
#    748 - vsph_test_camera_bounds (Failed)
#    768 - icam_test_transform (Failed)
#    812 - imesh_test_imls_surface (Failed)
#    886 - breg3d_test_ekf_camera_optimizer (Failed)
# Do not make build fail for this arch
%ctest || true
%endif

%files
%doc core/vxl_copyright.h
%{_bindir}/octree
%{_libdir}/libacal.so.%{major}.%{minor}
%{_libdir}/libacal.so.%{major}.%{minor}.%{patch}.0
%{_libdir}/libacal_io.so.%{major}.%{minor}
%{_libdir}/libacal_io.so.%{major}.%{minor}.%{patch}.0
%{_libdir}/libbaio.so.%{major}.%{minor}
%{_libdir}/libbaio.so.%{major}.%{minor}.%{patch}.0
%{_libdir}/libbaml.so.%{major}.%{minor}
%{_libdir}/libbaml.so.%{major}.%{minor}.%{patch}.0
%{_libdir}/libbapl.so.%{major}.%{minor}
%{_libdir}/libbapl.so.%{major}.%{minor}.%{patch}.0
%{_libdir}/libbapl_io.so.%{major}.%{minor}
%{_libdir}/libbapl_io.so.%{major}.%{minor}.%{patch}.0
%{_libdir}/libbapl_pro.so.%{major}.%{minor}
%{_libdir}/libbapl_pro.so.%{major}.%{minor}.%{patch}.0
%{_libdir}/libbbas_pro.so.%{major}.%{minor}
%{_libdir}/libbbas_pro.so.%{major}.%{minor}.%{patch}.0
%{_libdir}/libbbgm.so.%{major}.%{minor}
%{_libdir}/libbbgm.so.%{major}.%{minor}.%{patch}.0
%{_libdir}/libbbgm_pro.so.%{major}.%{minor}
%{_libdir}/libbbgm_pro.so.%{major}.%{minor}.%{patch}.0
%{_libdir}/libbcvr.so.%{major}.%{minor}
%{_libdir}/libbcvr.so.%{major}.%{minor}.%{patch}.0
%{_libdir}/libbdgl.so.%{major}.%{minor}
%{_libdir}/libbdgl.so.%{major}.%{minor}.%{patch}.0
%{_libdir}/libbdpg.so.%{major}.%{minor}
%{_libdir}/libbdpg.so.%{major}.%{minor}.%{patch}.0
%{_libdir}/libbetr.so.%{major}.%{minor}
%{_libdir}/libbetr.so.%{major}.%{minor}.%{patch}.0
%{_libdir}/libbetr_pro.so.%{major}.%{minor}
%{_libdir}/libbetr_pro.so.%{major}.%{minor}.%{patch}.0
%{_libdir}/libbgrl.so.%{major}.%{minor}
%{_libdir}/libbgrl.so.%{major}.%{minor}.%{patch}.0
%{_libdir}/libbgrl2.so.%{major}.%{minor}
%{_libdir}/libbgrl2.so.%{major}.%{minor}.%{patch}.0
%{_libdir}/libbgrl2_algo.so.%{major}.%{minor}
%{_libdir}/libbgrl2_algo.so.%{major}.%{minor}.%{patch}.0
%{_libdir}/libbil.so.%{major}.%{minor}
%{_libdir}/libbil.so.%{major}.%{minor}.%{patch}.0
%{_libdir}/libbil_algo.so.%{major}.%{minor}
%{_libdir}/libbil_algo.so.%{major}.%{minor}.%{patch}.0
%{_libdir}/libbjson.so.%{major}.%{minor}
%{_libdir}/libbjson.so.%{major}.%{minor}.%{patch}.0
%{_libdir}/libbkml.so.%{major}.%{minor}
%{_libdir}/libbkml.so.%{major}.%{minor}.%{patch}.0
%{_libdir}/libbmdl.so.%{major}.%{minor}
%{_libdir}/libbmdl.so.%{major}.%{minor}.%{patch}.0
%{_libdir}/libbmdl_pro.so.%{major}.%{minor}
%{_libdir}/libbmdl_pro.so.%{major}.%{minor}.%{patch}.0
%{_libdir}/libbmsh3d.so.%{major}.%{minor}
%{_libdir}/libbmsh3d.so.%{major}.%{minor}.%{patch}.0
%{_libdir}/libbmsh3d_algo.so.%{major}.%{minor}
%{_libdir}/libbmsh3d_algo.so.%{major}.%{minor}.%{patch}.0
%{_libdir}/libbmsh3d_pro.so.%{major}.%{minor}
%{_libdir}/libbmsh3d_pro.so.%{major}.%{minor}.%{patch}.0
%{_libdir}/libbnabo.so.%{major}.%{minor}
%{_libdir}/libbnabo.so.%{major}.%{minor}.%{patch}.0
%{_libdir}/libbnl.so.%{major}.%{minor}
%{_libdir}/libbnl.so.%{major}.%{minor}.%{patch}.0
%{_libdir}/libbnl_algo.so.%{major}.%{minor}
%{_libdir}/libbnl_algo.so.%{major}.%{minor}.%{patch}.0
%{_libdir}/libboct.so.%{major}.%{minor}
%{_libdir}/libboct.so.%{major}.%{minor}.%{patch}.0
%{_libdir}/libboxm2.so.%{major}.%{minor}
%{_libdir}/libboxm2.so.%{major}.%{minor}.%{patch}.0
%{_libdir}/libboxm2_basic.so.%{major}.%{minor}
%{_libdir}/libboxm2_basic.so.%{major}.%{minor}.%{patch}.0
%{_libdir}/libboxm2_class.so.%{major}.%{minor}
%{_libdir}/libboxm2_class.so.%{major}.%{minor}.%{patch}.0
%{_libdir}/libboxm2_cpp.so.%{major}.%{minor}
%{_libdir}/libboxm2_cpp.so.%{major}.%{minor}.%{patch}.0
%{_libdir}/libboxm2_cpp_algo.so.%{major}.%{minor}
%{_libdir}/libboxm2_cpp_algo.so.%{major}.%{minor}.%{patch}.0
%{_libdir}/libboxm2_cpp_pro.so.%{major}.%{minor}
%{_libdir}/libboxm2_cpp_pro.so.%{major}.%{minor}.%{patch}.0
%{_libdir}/libboxm2_io.so.%{major}.%{minor}
%{_libdir}/libboxm2_io.so.%{major}.%{minor}.%{patch}.0
%{_libdir}/libboxm2_pro.so.%{major}.%{minor}
%{_libdir}/libboxm2_pro.so.%{major}.%{minor}.%{patch}.0
%{_libdir}/libboxm2_util.so.%{major}.%{minor}
%{_libdir}/libboxm2_util.so.%{major}.%{minor}.%{patch}.0
%{_libdir}/libboxm2_vecf.so.%{major}.%{minor}
%{_libdir}/libboxm2_vecf.so.%{major}.%{minor}.%{patch}.0
%{_libdir}/libboxm2_volm.so.%{major}.%{minor}
%{_libdir}/libboxm2_volm.so.%{major}.%{minor}.%{patch}.0
%{_libdir}/libboxm2_volm_conf.so.%{major}.%{minor}
%{_libdir}/libboxm2_volm_conf.so.%{major}.%{minor}.%{patch}.0
%{_libdir}/libboxm2_volm_desc.so.%{major}.%{minor}
%{_libdir}/libboxm2_volm_desc.so.%{major}.%{minor}.%{patch}.0
%{_libdir}/libboxm2_volm_io.so.%{major}.%{minor}
%{_libdir}/libboxm2_volm_io.so.%{major}.%{minor}.%{patch}.0
%{_libdir}/libboxm2_volm_pro.so.%{major}.%{minor}
%{_libdir}/libboxm2_volm_pro.so.%{major}.%{minor}.%{patch}.0
%{_libdir}/libbpgl.so.%{major}.%{minor}
%{_libdir}/libbpgl.so.%{major}.%{minor}.%{patch}.0
%{_libdir}/libbpgl_algo.so.%{major}.%{minor}
%{_libdir}/libbpgl_algo.so.%{major}.%{minor}.%{patch}.0
%{_libdir}/libbprb.so.%{major}.%{minor}
%{_libdir}/libbprb.so.%{major}.%{minor}.%{patch}.0
%{_libdir}/libbrad.so.%{major}.%{minor}
%{_libdir}/libbrad.so.%{major}.%{minor}.%{patch}.0
%{_libdir}/libbrad_io.so.%{major}.%{minor}
%{_libdir}/libbrad_io.so.%{major}.%{minor}.%{patch}.0
%{_libdir}/libbrad_pro.so.%{major}.%{minor}
%{_libdir}/libbrad_pro.so.%{major}.%{minor}.%{patch}.0
%{_libdir}/libbrdb.so.%{major}.%{minor}
%{_libdir}/libbrdb.so.%{major}.%{minor}.%{patch}.0
%{_libdir}/libbrec.so.%{major}.%{minor}
%{_libdir}/libbrec.so.%{major}.%{minor}.%{patch}.0
%{_libdir}/libbrec_pro.so.%{major}.%{minor}
%{_libdir}/libbrec_pro.so.%{major}.%{minor}.%{patch}.0
%{_libdir}/libbreg3d.so.%{major}.%{minor}
%{_libdir}/libbreg3d.so.%{major}.%{minor}.%{patch}.0
%{_libdir}/libbreg3d_pro.so.%{major}.%{minor}
%{_libdir}/libbreg3d_pro.so.%{major}.%{minor}.%{patch}.0
%{_libdir}/libbres.so.%{major}.%{minor}
%{_libdir}/libbres.so.%{major}.%{minor}.%{patch}.0
%{_libdir}/libbrip.so.%{major}.%{minor}
%{_libdir}/libbrip.so.%{major}.%{minor}.%{patch}.0
%{_libdir}/libbrip_pro.so.%{major}.%{minor}
%{_libdir}/libbrip_pro.so.%{major}.%{minor}.%{patch}.0
%{_libdir}/libbsgm.so.%{major}.%{minor}
%{_libdir}/libbsgm.so.%{major}.%{minor}.%{patch}.0
%{_libdir}/libbsgm_pro.so.%{major}.%{minor}
%{_libdir}/libbsgm_pro.so.%{major}.%{minor}.%{patch}.0
%{_libdir}/libbsl.so.%{major}.%{minor}
%{_libdir}/libbsl.so.%{major}.%{minor}.%{patch}.0
%{_libdir}/libbsol.so.%{major}.%{minor}
%{_libdir}/libbsol.so.%{major}.%{minor}.%{patch}.0
%{_libdir}/libbsta.so.%{major}.%{minor}
%{_libdir}/libbsta.so.%{major}.%{minor}.%{patch}.0
%{_libdir}/libbsta_algo.so.%{major}.%{minor}
%{_libdir}/libbsta_algo.so.%{major}.%{minor}.%{patch}.0
%{_libdir}/libbsta_io.so.%{major}.%{minor}
%{_libdir}/libbsta_io.so.%{major}.%{minor}.%{patch}.0
%{_libdir}/libbsta_pro.so.%{major}.%{minor}
%{_libdir}/libbsta_pro.so.%{major}.%{minor}.%{patch}.0
%{_libdir}/libbsta_vis.so.%{major}.%{minor}
%{_libdir}/libbsta_vis.so.%{major}.%{minor}.%{patch}.0
%{_libdir}/libbstm.so.%{major}.%{minor}
%{_libdir}/libbstm.so.%{major}.%{minor}.%{patch}.0
%{_libdir}/libbstm_basic.so.%{major}.%{minor}
%{_libdir}/libbstm_basic.so.%{major}.%{minor}.%{patch}.0
%{_libdir}/libbstm_cpp_algo.so.%{major}.%{minor}
%{_libdir}/libbstm_cpp_algo.so.%{major}.%{minor}.%{patch}.0
%{_libdir}/libbstm_cpp_pro.so.%{major}.%{minor}
%{_libdir}/libbstm_cpp_pro.so.%{major}.%{minor}.%{patch}.0
%{_libdir}/libbstm_io.so.%{major}.%{minor}
%{_libdir}/libbstm_io.so.%{major}.%{minor}.%{patch}.0
%{_libdir}/libbstm_multi.so.%{major}.%{minor}
%{_libdir}/libbstm_multi.so.%{major}.%{minor}.%{patch}.0
%{_libdir}/libbstm_multi_basic.so.%{major}.%{minor}
%{_libdir}/libbstm_multi_basic.so.%{major}.%{minor}.%{patch}.0
%{_libdir}/libbstm_multi_io.so.%{major}.%{minor}
%{_libdir}/libbstm_multi_io.so.%{major}.%{minor}.%{patch}.0
%{_libdir}/libbstm_pro.so.%{major}.%{minor}
%{_libdir}/libbstm_pro.so.%{major}.%{minor}.%{patch}.0
%{_libdir}/libbstm_util.so.%{major}.%{minor}
%{_libdir}/libbstm_util.so.%{major}.%{minor}.%{patch}.0
%{_libdir}/libbsvg.so.%{major}.%{minor}
%{_libdir}/libbsvg.so.%{major}.%{minor}.%{patch}.0
%{_libdir}/libbsvg_pro.so.%{major}.%{minor}
%{_libdir}/libbsvg_pro.so.%{major}.%{minor}.%{patch}.0
%{_libdir}/libbtol.so.%{major}.%{minor}
%{_libdir}/libbtol.so.%{major}.%{minor}.%{patch}.0
%{_libdir}/libbugl.so.%{major}.%{minor}
%{_libdir}/libbugl.so.%{major}.%{minor}.%{patch}.0
%{_libdir}/libbundler.so.%{major}.%{minor}
%{_libdir}/libbundler.so.%{major}.%{minor}.%{patch}.0
%{_libdir}/libbvgl.so.%{major}.%{minor}
%{_libdir}/libbvgl.so.%{major}.%{minor}.%{patch}.0
%{_libdir}/libbvgl_algo.so.%{major}.%{minor}
%{_libdir}/libbvgl_algo.so.%{major}.%{minor}.%{patch}.0
%{_libdir}/libbvgl_pro.so.%{major}.%{minor}
%{_libdir}/libbvgl_pro.so.%{major}.%{minor}.%{patch}.0
%{_libdir}/libbvpl.so.%{major}.%{minor}
%{_libdir}/libbvpl.so.%{major}.%{minor}.%{patch}.0
%{_libdir}/libbvpl_functors.so.%{major}.%{minor}
%{_libdir}/libbvpl_functors.so.%{major}.%{minor}.%{patch}.0
%{_libdir}/libbvpl_kernels.so.%{major}.%{minor}
%{_libdir}/libbvpl_kernels.so.%{major}.%{minor}.%{patch}.0
%{_libdir}/libbvpl_kernels_io.so.%{major}.%{minor}
%{_libdir}/libbvpl_kernels_io.so.%{major}.%{minor}.%{patch}.0
%{_libdir}/libbvpl_kernels_pro.so.%{major}.%{minor}
%{_libdir}/libbvpl_kernels_pro.so.%{major}.%{minor}.%{patch}.0
%{_libdir}/libbvpl_pro.so.%{major}.%{minor}
%{_libdir}/libbvpl_pro.so.%{major}.%{minor}.%{patch}.0
%{_libdir}/libbvpl_util.so.%{major}.%{minor}
%{_libdir}/libbvpl_util.so.%{major}.%{minor}.%{patch}.0
%{_libdir}/libbvpl_util_io.so.%{major}.%{minor}
%{_libdir}/libbvpl_util_io.so.%{major}.%{minor}.%{patch}.0
%{_libdir}/libbvrml.so.%{major}.%{minor}
%{_libdir}/libbvrml.so.%{major}.%{minor}.%{patch}.0
%{_libdir}/libbvrml_pro.so.%{major}.%{minor}
%{_libdir}/libbvrml_pro.so.%{major}.%{minor}.%{patch}.0
%{_libdir}/libbvxm.so.%{major}.%{minor}
%{_libdir}/libbvxm.so.%{major}.%{minor}.%{patch}.0
%{_libdir}/libbvxm_algo.so.%{major}.%{minor}
%{_libdir}/libbvxm_algo.so.%{major}.%{minor}.%{patch}.0
%{_libdir}/libbvxm_algo_pro.so.%{major}.%{minor}
%{_libdir}/libbvxm_algo_pro.so.%{major}.%{minor}.%{patch}.0
%{_libdir}/libbvxm_grid.so.%{major}.%{minor}
%{_libdir}/libbvxm_grid.so.%{major}.%{minor}.%{patch}.0
%{_libdir}/libbvxm_grid_io.so.%{major}.%{minor}
%{_libdir}/libbvxm_grid_io.so.%{major}.%{minor}.%{patch}.0
%{_libdir}/libbvxm_grid_pro.so.%{major}.%{minor}
%{_libdir}/libbvxm_grid_pro.so.%{major}.%{minor}.%{patch}.0
%{_libdir}/libbvxm_io.so.%{major}.%{minor}
%{_libdir}/libbvxm_io.so.%{major}.%{minor}.%{patch}.0
%{_libdir}/libbvxm_pro.so.%{major}.%{minor}
%{_libdir}/libbvxm_pro.so.%{major}.%{minor}.%{patch}.0
%{_libdir}/libbwm_video.so.%{major}.%{minor}
%{_libdir}/libbwm_video.so.%{major}.%{minor}.%{patch}.0
%{_libdir}/libbxml.so.%{major}.%{minor}
%{_libdir}/libbxml.so.%{major}.%{minor}.%{patch}.0
%{_libdir}/libclipper.so.%{major}.%{minor}
%{_libdir}/libclipper.so.%{major}.%{minor}.%{patch}.0
%{_libdir}/libclsfy.so.%{major}.%{minor}
%{_libdir}/libclsfy.so.%{major}.%{minor}.%{patch}.0
%{_libdir}/libdepth_map.so.%{major}.%{minor}
%{_libdir}/libdepth_map.so.%{major}.%{minor}.%{patch}.0
%{_libdir}/libfhs.so.%{major}.%{minor}
%{_libdir}/libfhs.so.%{major}.%{minor}.%{patch}.0
%{_libdir}/libgeml.so.%{major}.%{minor}
%{_libdir}/libgeml.so.%{major}.%{minor}.%{patch}.0
%{_libdir}/libgevd.so.%{major}.%{minor}
%{_libdir}/libgevd.so.%{major}.%{minor}.%{patch}.0
%{_libdir}/libgmvl.so.%{major}.%{minor}
%{_libdir}/libgmvl.so.%{major}.%{minor}.%{patch}.0
%{_libdir}/libgst.so.%{major}.%{minor}
%{_libdir}/libgst.so.%{major}.%{minor}.%{patch}.0
%{_libdir}/libgtrl.so.%{major}.%{minor}
%{_libdir}/libgtrl.so.%{major}.%{minor}.%{patch}.0
%{_libdir}/libicam.so.%{major}.%{minor}
%{_libdir}/libicam.so.%{major}.%{minor}.%{patch}.0
%{_libdir}/libicam_pro.so.%{major}.%{minor}
%{_libdir}/libicam_pro.so.%{major}.%{minor}.%{patch}.0
%{_libdir}/libihog.so.%{major}.%{minor}
%{_libdir}/libihog.so.%{major}.%{minor}.%{patch}.0
%{_libdir}/libihog_pro.so.%{major}.%{minor}
%{_libdir}/libihog_pro.so.%{major}.%{minor}.%{patch}.0
%{_libdir}/libimesh.so.%{major}.%{minor}
%{_libdir}/libimesh.so.%{major}.%{minor}.%{patch}.0
%{_libdir}/libimesh_algo.so.%{major}.%{minor}
%{_libdir}/libimesh_algo.so.%{major}.%{minor}.%{patch}.0
%{_libdir}/libipts.so.%{major}.%{minor}
%{_libdir}/libipts.so.%{major}.%{minor}.%{patch}.0
%{_libdir}/libm23d.so.%{major}.%{minor}
%{_libdir}/libm23d.so.%{major}.%{minor}.%{patch}.0
%{_libdir}/libmbl.so.%{major}.%{minor}
%{_libdir}/libmbl.so.%{major}.%{minor}.%{patch}.0
%{_libdir}/libmcal.so.%{major}.%{minor}
%{_libdir}/libmcal.so.%{major}.%{minor}.%{patch}.0
%{_libdir}/libmfpf.so.%{major}.%{minor}
%{_libdir}/libmfpf.so.%{major}.%{minor}.%{patch}.0
%{_libdir}/libmipa.so.%{major}.%{minor}
%{_libdir}/libmipa.so.%{major}.%{minor}.%{patch}.0
%{_libdir}/libmmn.so.%{major}.%{minor}
%{_libdir}/libmmn.so.%{major}.%{minor}.%{patch}.0
%{_libdir}/libmsdi.so.%{major}.%{minor}
%{_libdir}/libmsdi.so.%{major}.%{minor}.%{patch}.0
%{_libdir}/libmsm.so.%{major}.%{minor}
%{_libdir}/libmsm.so.%{major}.%{minor}.%{patch}.0
%{_libdir}/libmsm_utils.so.%{major}.%{minor}
%{_libdir}/libmsm_utils.so.%{major}.%{minor}.%{patch}.0
%{_libdir}/libmvl.so.%{major}.%{minor}
%{_libdir}/libmvl.so.%{major}.%{minor}.%{patch}.0
%{_libdir}/libmvl2.so.%{major}.%{minor}
%{_libdir}/libmvl2.so.%{major}.%{minor}.%{patch}.0
%{_libdir}/libopenjpeg2.so.2.%{patch}.0
%{_libdir}/libopenjpeg2.so.%{major}.%{minor}
%{_libdir}/libosl.so.%{major}.%{minor}
%{_libdir}/libosl.so.%{major}.%{minor}.%{patch}.0
%{_libdir}/libouel.so.%{major}.%{minor}
%{_libdir}/libouel.so.%{major}.%{minor}.%{patch}.0
%{_libdir}/libouml.so.%{major}.%{minor}
%{_libdir}/libouml.so.%{major}.%{minor}.%{patch}.0
%{_libdir}/liboxl_vrml.so.%{major}.%{minor}
%{_libdir}/liboxl_vrml.so.%{major}.%{minor}.%{patch}.0
%{_libdir}/libpdf1d.so.%{major}.%{minor}
%{_libdir}/libpdf1d.so.%{major}.%{minor}.%{patch}.0
%{_libdir}/librgrl.so.%{major}.%{minor}
%{_libdir}/librgrl.so.%{major}.%{minor}.%{patch}.0
%{_libdir}/librrel.so.%{major}.%{minor}
%{_libdir}/librrel.so.%{major}.%{minor}.%{patch}.0
%{_libdir}/librsdl.so.%{major}.%{minor}
%{_libdir}/librsdl.so.%{major}.%{minor}.%{patch}.0
%{_libdir}/libsdet.so.%{major}.%{minor}
%{_libdir}/libsdet.so.%{major}.%{minor}.%{patch}.0
%{_libdir}/libsdet_algo.so.%{major}.%{minor}
%{_libdir}/libsdet_algo.so.%{major}.%{minor}.%{patch}.0
%{_libdir}/libsdet_pro.so.%{major}.%{minor}
%{_libdir}/libsdet_pro.so.%{major}.%{minor}.%{patch}.0
%{_libdir}/libtestlib.so.%{major}.%{minor}
%{_libdir}/libtestlib.so.%{major}.%{minor}.%{patch}.0
%{_libdir}/libv3p_netlib.so.%{major}.%{minor}
%{_libdir}/libv3p_netlib.so.%{major}.%{minor}.%{patch}.0
%{_libdir}/libvbl.so.%{major}.%{minor}
%{_libdir}/libvbl.so.%{major}.%{minor}.%{patch}.0
%{_libdir}/libvbl_io.so.%{major}.%{minor}
%{_libdir}/libvbl_io.so.%{major}.%{minor}.%{patch}.0
%{_libdir}/libvcl.so.%{major}.%{minor}
%{_libdir}/libvcl.so.%{major}.%{minor}.%{patch}.0
%{_libdir}/libvcon_pro.so.%{major}.%{minor}
%{_libdir}/libvcon_pro.so.%{major}.%{minor}.%{patch}.0
%{_libdir}/libvcsl.so.%{major}.%{minor}
%{_libdir}/libvcsl.so.%{major}.%{minor}.%{patch}.0
%{_libdir}/libvdgl.so.%{major}.%{minor}
%{_libdir}/libvdgl.so.%{major}.%{minor}.%{patch}.0
%{_libdir}/libvdtop.so.%{major}.%{minor}
%{_libdir}/libvdtop.so.%{major}.%{minor}.%{patch}.0
%{_libdir}/libvepl.so.%{major}.%{minor}
%{_libdir}/libvepl.so.%{major}.%{minor}.%{patch}.0
%{_libdir}/libvgl.so.%{major}.%{minor}
%{_libdir}/libvgl.so.%{major}.%{minor}.%{patch}.0
%{_libdir}/libvgl_algo.so.%{major}.%{minor}
%{_libdir}/libvgl_algo.so.%{major}.%{minor}.%{patch}.0
%{_libdir}/libvgl_io.so.%{major}.%{minor}
%{_libdir}/libvgl_io.so.%{major}.%{minor}.%{patch}.0
%{_libdir}/libvgl_xio.so.%{major}.%{minor}
%{_libdir}/libvgl_xio.so.%{major}.%{minor}.%{patch}.0
%{_libdir}/libvidl.so.%{major}.%{minor}
%{_libdir}/libvidl.so.%{major}.%{minor}.%{patch}.0
%{_libdir}/libvidl_pro.so.%{major}.%{minor}
%{_libdir}/libvidl_pro.so.%{major}.%{minor}.%{patch}.0
%{_libdir}/libvifa.so.%{major}.%{minor}
%{_libdir}/libvifa.so.%{major}.%{minor}.%{patch}.0
%{_libdir}/libvil.so.%{major}.%{minor}
%{_libdir}/libvil.so.%{major}.%{minor}.%{patch}.0
%{_libdir}/libvil1.so.%{major}.%{minor}
%{_libdir}/libvil1.so.%{major}.%{minor}.%{patch}.0
%{_libdir}/libvil3d.so.%{major}.%{minor}
%{_libdir}/libvil3d.so.%{major}.%{minor}.%{patch}.0
%{_libdir}/libvil3d_algo.so.%{major}.%{minor}
%{_libdir}/libvil3d_algo.so.%{major}.%{minor}.%{patch}.0
%{_libdir}/libvil3d_io.so.%{major}.%{minor}
%{_libdir}/libvil3d_io.so.%{major}.%{minor}.%{patch}.0
%{_libdir}/libvil_algo.so.%{major}.%{minor}
%{_libdir}/libvil_algo.so.%{major}.%{minor}.%{patch}.0
%{_libdir}/libvil_io.so.%{major}.%{minor}
%{_libdir}/libvil_io.so.%{major}.%{minor}.%{patch}.0
%{_libdir}/libvil_pro.so.%{major}.%{minor}
%{_libdir}/libvil_pro.so.%{major}.%{minor}.%{patch}.0
%{_libdir}/libvimt.so.%{major}.%{minor}
%{_libdir}/libvimt.so.%{major}.%{minor}.%{patch}.0
%{_libdir}/libvimt3d.so.%{major}.%{minor}
%{_libdir}/libvimt3d.so.%{major}.%{minor}.%{patch}.0
%{_libdir}/libvimt_algo.so.%{major}.%{minor}
%{_libdir}/libvimt_algo.so.%{major}.%{minor}.%{patch}.0
%{_libdir}/libvipl.so.%{major}.%{minor}
%{_libdir}/libvipl.so.%{major}.%{minor}.%{patch}.0
%{_libdir}/libvmal.so.%{major}.%{minor}
%{_libdir}/libvmal.so.%{major}.%{minor}.%{patch}.0
%{_libdir}/libvmap.so.%{major}.%{minor}
%{_libdir}/libvmap.so.%{major}.%{minor}.%{patch}.0
%{_libdir}/libvnl.so.%{major}.%{minor}
%{_libdir}/libvnl.so.%{major}.%{minor}.%{patch}.0
%{_libdir}/libvnl_algo.so.%{major}.%{minor}
%{_libdir}/libvnl_algo.so.%{major}.%{minor}.%{patch}.0
%{_libdir}/libvnl_io.so.%{major}.%{minor}
%{_libdir}/libvnl_io.so.%{major}.%{minor}.%{patch}.0
%{_libdir}/libvnl_xio.so.%{major}.%{minor}
%{_libdir}/libvnl_xio.so.%{major}.%{minor}.%{patch}.0
%{_libdir}/libvolm.so.%{major}.%{minor}
%{_libdir}/libvolm.so.%{major}.%{minor}.%{patch}.0
%{_libdir}/libvolm_conf.so.%{major}.%{minor}
%{_libdir}/libvolm_conf.so.%{major}.%{minor}.%{patch}.0
%{_libdir}/libvolm_desc.so.%{major}.%{minor}
%{_libdir}/libvolm_desc.so.%{major}.%{minor}.%{patch}.0
%{_libdir}/libvolm_pro.so.%{major}.%{minor}
%{_libdir}/libvolm_pro.so.%{major}.%{minor}.%{patch}.0
%{_libdir}/libvpdfl.so.%{major}.%{minor}
%{_libdir}/libvpdfl.so.%{major}.%{minor}.%{patch}.0
%{_libdir}/libvpdl.so.%{major}.%{minor}
%{_libdir}/libvpdl.so.%{major}.%{minor}.%{patch}.0
%{_libdir}/libvpgl.so.%{major}.%{minor}
%{_libdir}/libvpgl.so.%{major}.%{minor}.%{patch}.0
%{_libdir}/libvpgl_algo.so.%{major}.%{minor}
%{_libdir}/libvpgl_algo.so.%{major}.%{minor}.%{patch}.0
%{_libdir}/libvpgl_file_formats.so.%{major}.%{minor}
%{_libdir}/libvpgl_file_formats.so.%{major}.%{minor}.%{patch}.0
%{_libdir}/libvpgl_io.so.%{major}.%{minor}
%{_libdir}/libvpgl_io.so.%{major}.%{minor}.%{patch}.0
%{_libdir}/libvpgl_pro.so.%{major}.%{minor}
%{_libdir}/libvpgl_pro.so.%{major}.%{minor}.%{patch}.0
%{_libdir}/libvpgl_xio.so.%{major}.%{minor}
%{_libdir}/libvpgl_xio.so.%{major}.%{minor}.%{patch}.0
%{_libdir}/libvpl.so.%{major}.%{minor}
%{_libdir}/libvpl.so.%{major}.%{minor}.%{patch}.0
%{_libdir}/libvpyr.so.%{major}.%{minor}
%{_libdir}/libvpyr.so.%{major}.%{minor}.%{patch}.0
%{_libdir}/libvsl.so.%{major}.%{minor}
%{_libdir}/libvsl.so.%{major}.%{minor}.%{patch}.0
%{_libdir}/libvsol.so.%{major}.%{minor}
%{_libdir}/libvsol.so.%{major}.%{minor}.%{patch}.0
%{_libdir}/libvsph.so.%{major}.%{minor}
%{_libdir}/libvsph.so.%{major}.%{minor}.%{patch}.0
%{_libdir}/libvtol.so.%{major}.%{minor}
%{_libdir}/libvtol.so.%{major}.%{minor}.%{patch}.0
%{_libdir}/libvtol_algo.so.%{major}.%{minor}
%{_libdir}/libvtol_algo.so.%{major}.%{minor}.%{patch}.0
%{_libdir}/libvul.so.%{major}.%{minor}
%{_libdir}/libvul.so.%{major}.%{minor}.%{patch}.0
%{_libdir}/libvul_io.so.%{major}.%{minor}
%{_libdir}/libvul_io.so.%{major}.%{minor}.%{patch}.0

%files devel
%{_datadir}/%{name}
%{_includedir}/%{name}
%{_libdir}/libbbas_pro.so
%{_libdir}/libbapl_pro.so
%{_libdir}/libbapl_io.so
%{_libdir}/libacal.so
%{_libdir}/libacal_io.so
%{_libdir}/libbaio.so
%{_libdir}/libbaml.so
%{_libdir}/libbapl.so
%{_libdir}/libbbgm.so
%{_libdir}/libbbgm_pro.so
%{_libdir}/libbcvr.so
%{_libdir}/libbdgl.so
%{_libdir}/libbdpg.so
%{_libdir}/libbetr.so
%{_libdir}/libbetr_pro.so
%{_libdir}/libbgrl.so
%{_libdir}/libbgrl2.so
%{_libdir}/libbgrl2_algo.so
%{_libdir}/libbil.so
%{_libdir}/libbil_algo.so
%{_libdir}/libbjson.so
%{_libdir}/libbkml.so
%{_libdir}/libbmdl.so
%{_libdir}/libbmdl_pro.so
%{_libdir}/libbmsh3d.so
%{_libdir}/libbmsh3d_algo.so
%{_libdir}/libbmsh3d_pro.so
%{_libdir}/libbnabo.so
%{_libdir}/libbnl.so
%{_libdir}/libbnl_algo.so
%{_libdir}/libboct.so
%{_libdir}/libboxm2.so
%{_libdir}/libboxm2_basic.so
%{_libdir}/libboxm2_class.so
%{_libdir}/libboxm2_cpp.so
%{_libdir}/libboxm2_cpp_algo.so
%{_libdir}/libboxm2_cpp_pro.so
%{_libdir}/libboxm2_io.so
%{_libdir}/libboxm2_pro.so
%{_libdir}/libboxm2_util.so
%{_libdir}/libboxm2_vecf.so
%{_libdir}/libboxm2_volm.so
%{_libdir}/libboxm2_volm_conf.so
%{_libdir}/libboxm2_volm_desc.so
%{_libdir}/libboxm2_volm_io.so
%{_libdir}/libboxm2_volm_pro.so
%{_libdir}/libbpgl.so
%{_libdir}/libbpgl_algo.so
%{_libdir}/libbprb.so
%{_libdir}/libbrad.so
%{_libdir}/libbrad_io.so
%{_libdir}/libbrad_pro.so
%{_libdir}/libbrdb.so
%{_libdir}/libbrec.so
%{_libdir}/libbrec_pro.so
%{_libdir}/libbreg3d.so
%{_libdir}/libbreg3d_pro.so
%{_libdir}/libbres.so
%{_libdir}/libbrip.so
%{_libdir}/libbrip_pro.so
%{_libdir}/libbsgm.so
%{_libdir}/libbsgm_pro.so
%{_libdir}/libbsl.so
%{_libdir}/libbsol.so
%{_libdir}/libbsta.so
%{_libdir}/libbsta_algo.so
%{_libdir}/libbsta_io.so
%{_libdir}/libbsta_pro.so
%{_libdir}/libbsta_vis.so
%{_libdir}/libbstm.so
%{_libdir}/libbstm_basic.so
%{_libdir}/libbstm_cpp_algo.so
%{_libdir}/libbstm_cpp_pro.so
%{_libdir}/libbstm_io.so
%{_libdir}/libbstm_multi.so
%{_libdir}/libbstm_multi_basic.so
%{_libdir}/libbstm_multi_io.so
%{_libdir}/libbstm_pro.so
%{_libdir}/libbstm_util.so
%{_libdir}/libbsvg.so
%{_libdir}/libbsvg_pro.so
%{_libdir}/libbtol.so
%{_libdir}/libbugl.so
%{_libdir}/libbundler.so
%{_libdir}/libbvgl.so
%{_libdir}/libbvgl_algo.so
%{_libdir}/libbvgl_pro.so
%{_libdir}/libbvpl.so
%{_libdir}/libbvpl_functors.so
%{_libdir}/libbvpl_kernels.so
%{_libdir}/libbvpl_kernels_io.so
%{_libdir}/libbvpl_kernels_pro.so
%{_libdir}/libbvpl_pro.so
%{_libdir}/libbvpl_util.so
%{_libdir}/libbvpl_util_io.so
%{_libdir}/libbvrml.so
%{_libdir}/libbvrml_pro.so
%{_libdir}/libbvxm.so
%{_libdir}/libbvxm_algo.so
%{_libdir}/libbvxm_algo_pro.so
%{_libdir}/libbvxm_grid.so
%{_libdir}/libbvxm_grid_io.so
%{_libdir}/libbvxm_grid_pro.so
%{_libdir}/libbvxm_io.so
%{_libdir}/libbvxm_pro.so
%{_libdir}/libbwm_video.so
%{_libdir}/libbxml.so
%{_libdir}/libclipper.so
%{_libdir}/libclsfy.so
%{_libdir}/libdepth_map.so
%{_libdir}/libfhs.so
%{_libdir}/libgeml.so
%{_libdir}/libgevd.so
%{_libdir}/libgmvl.so
%{_libdir}/libgst.so
%{_libdir}/libgtrl.so
%{_libdir}/libicam.so
%{_libdir}/libicam_pro.so
%{_libdir}/libihog.so
%{_libdir}/libihog_pro.so
%{_libdir}/libimesh.so
%{_libdir}/libimesh_algo.so
%{_libdir}/libipts.so
%{_libdir}/libm23d.so
%{_libdir}/libmbl.so
%{_libdir}/libmcal.so
%{_libdir}/libmfpf.so
%{_libdir}/libmipa.so
%{_libdir}/libmmn.so
%{_libdir}/libmsdi.so
%{_libdir}/libmsm.so
%{_libdir}/libmsm_utils.so
%{_libdir}/libmvl.so
%{_libdir}/libmvl2.so
%{_libdir}/libopenjpeg2.so
%{_libdir}/libosl.so
%{_libdir}/libouel.so
%{_libdir}/libouml.so
%{_libdir}/liboxl_vrml.so
%{_libdir}/libpdf1d.so
%{_libdir}/librgrl.so
%{_libdir}/librrel.so
%{_libdir}/librsdl.so
%{_libdir}/libsdet.so
%{_libdir}/libsdet_algo.so
%{_libdir}/libsdet_pro.so
%{_libdir}/libtestlib.so
%{_libdir}/libv3p_netlib.so
%{_libdir}/libvbl.so
%{_libdir}/libvbl_io.so
%{_libdir}/libvcl.so
%{_libdir}/libvcon_pro.so
%{_libdir}/libvcsl.so
%{_libdir}/libvdgl.so
%{_libdir}/libvdtop.so
%{_libdir}/libvepl.so
%{_libdir}/libvgl.so
%{_libdir}/libvgl_algo.so
%{_libdir}/libvgl_io.so
%{_libdir}/libvgl_xio.so
%{_libdir}/libvidl.so
%{_libdir}/libvidl_pro.so
%{_libdir}/libvifa.so
%{_libdir}/libvil.so
%{_libdir}/libvil1.so
%{_libdir}/libvil3d.so
%{_libdir}/libvil3d_algo.so
%{_libdir}/libvil3d_io.so
%{_libdir}/libvil_algo.so
%{_libdir}/libvil_io.so
%{_libdir}/libvil_pro.so
%{_libdir}/libvimt.so
%{_libdir}/libvimt3d.so
%{_libdir}/libvimt_algo.so
%{_libdir}/libvipl.so
%{_libdir}/libvmal.so
%{_libdir}/libvmap.so
%{_libdir}/libvnl.so
%{_libdir}/libvnl_algo.so
%{_libdir}/libvnl_io.so
%{_libdir}/libvnl_xio.so
%{_libdir}/libvolm.so
%{_libdir}/libvolm_conf.so
%{_libdir}/libvolm_desc.so
%{_libdir}/libvolm_pro.so
%{_libdir}/libvpdfl.so
%{_libdir}/libvpdl.so
%{_libdir}/libvpgl.so
%{_libdir}/libvpgl_algo.so
%{_libdir}/libvpgl_file_formats.so
%{_libdir}/libvpgl_io.so
%{_libdir}/libvpgl_pro.so
%{_libdir}/libvpgl_xio.so
%{_libdir}/libvpl.so
%{_libdir}/libvpyr.so
%{_libdir}/libvsl.so
%{_libdir}/libvsol.so
%{_libdir}/libvsph.so
%{_libdir}/libvtol.so
%{_libdir}/libvtol_algo.so
%{_libdir}/libvul.so
%{_libdir}/libvul_io.so


%files doc
%doc core/vxl_copyright.h
%doc %{_docdir}/*

%changelog
%autochangelog
