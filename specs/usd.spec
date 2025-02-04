# We hard-code the ABI version here, even though it can be derived from the
# package version, as a reminder of the need to rebuild dependent packages on
# every update. See additional notes near the downstream ABI versioning patch.
# It should be 0.MAJOR.MINOR without leading zeros, e.g. 22.03 → 0.22.3.
%global downstream_so_version 0.25.2

%bcond alembic       1
%bcond draco         1
%bcond embree        1
%bcond jemalloc      0
# Not yet packaged: https://github.com/AcademySoftwareFoundation/MaterialX
# https://bugzilla.redhat.com/show_bug.cgi?id=2262694
%bcond materialx     0
# Default "UNIX Makefiles" backend for CMake would also work fine; ninja is a
# bit faster. We conditionalize it just in case there are backend-specific
# issues in the future.
%bcond ninja         1
%bcond openshading   1
%bcond openvdb       1
%bcond ocio          1
%bcond oiio          1
%bcond ptex          1
%bcond usdview       1
# TODO: Figure out how to re-enable the tests. Currently these want to install
# into /usr/tests, and there are issues with the launchers finding the
# command-line tools in the buildroot.
%bcond test          0

Name:           usd
Version:        25.02
Release:        %autorelease
Summary:        3D VFX pipeline interchange file format

# The entire source is Pixar except:
#
# Apache-2.0:
#   - pxr/imaging/hgiVulkan/spirv_reflect.{cpp,h}
# BSD-3-Clause:
#   - pxr/base/gf/ilmbase_*
#   - pxr/base/js/rapidjson/msinttypes/ (removed in %%prep)
#   - pxr/base/tf/pxrCLI11/ (removed in %%prep)
#   - pxr/base/tf/pxrDoubleConversion/ (removed in %%prep)
#   - pxr/imaging/hio/OpenEXR/OpenEXRCore/
#   - pxr/imaging/plugin/hioAvif/AVIF/src/src-libyuv/
# BSD-2-Clause:
#   - pxr/base/tf/pxrLZ4/ (removed in %%prep)
#   - pxr/imaging/plugin/hioAvif/AVIF/, except
#     pxr/imaging/plugin/hioAvif/AVIF/src/src-libyuv/;
#     pxr/imaging/plugin/hioAvif/AVIF/src/avif_obu.c has a different copyright
#   - pxr/imaging/plugin/hioAvif/aom/
# BSL-1.0:
#   - pxr/external/boost/
# MIT:
#   - docs/doxygen/doxygen-awesome-css/ (removed in %%prep)
#   - pxr/base/js/rapidjson/, except pxr/base/js/rapidjson/msinttypes/ (both
#     removed in %%prep)
#   - pxr/base/pegtl/
#   - pxr/base/tf/pxrTslRobinMap/
#   - pxr/imaging/garch/khrplatform.h
#   - pxr/imaging/hgiVulkan/vk_mem_alloc.h
#   - pxr/imaging/hio/OpenEXR/deflate/ (removed in %%prep)
#   - third_party/renderman-26/plugin/rmanArgsParser/pugixml/ (removed in %%prep)
# MIT OR Unlicense:
#   - pxr/imaging/hio/stb/
# Pixar AND GPL-3.0-or-later WITH Bison-exception-2.2:
#   - pxr/usd/sdf/path.tab.{cpp,h}
#   - pxr/usd/sdf/textFileFormat.tab.{cpp,h}
#   - third_party/renderman-26/plugin/hdPrman/virtualStructConditionalGrammar.tab.{cpp,h}
#
# Additionally, the following would be listed above but are removed in %%prep:
#
# Apache-2.0:
#   - pxr/usdImaging/usdviewq/fonts/Roboto_Mono/
#   - pxr/usdImaging/usdviewq/fonts/Roboto/
# MIT:
#   - docs/doxygen/doxygen-awesome-css/ (except doxygen-awesome-darkmode-toggle.js)
# MIT AND Apache-2.0:
#   - docs/doxygen/doxygen-awesome-css/doxygen-awesome-darkmode-toggle.js
#
# (Certain build system files are also under licenses other than Apache-2.0, but
# do not contribute their license terms to the built RPMs.)
#
# Note that the license assigned the SPDX identifier Pixar was later officially
# named Tomorrow Open Source Technology License 1.0, TOST-1.0, with no change
# to its terms.
License:        %{shrink:
                Pixar AND
                Apache-2.0 AND
                BSD-3-Clause AND
                BSD-2-Clause AND
                BSL-1.0 AND
                MIT AND
                (MIT OR Unlicense) AND
                (Pixar AND GPL-3.0-or-later WITH Bison-exception-2.2)
                }
URL:            http://www.openusd.org/
%global forgeurl https://github.com/PixarAnimationStudios/OpenUSD
Source0:        %{forgeurl}/archive/v%{version}/OpenUSD-%{version}.tar.gz
Source1:        org.openusd.usdview.desktop

# Downstream-only: add an SONAME version
#
# Upstream was asked about .so versioning and setting SONAME properly and
# seemed unprepared to handle the request:
# https://github.com/PixarAnimationStudios/USD/issues/1259#issuecomment-657120216
#
# A patch was offered:
# https://github.com/PixarAnimationStudios/USD/issues/1387
# but it was not sufficient for the general case, since (1) it only handled the
# monolithic build, and (2) it derived the .so version from PXR_MAJOR_VERSION,
# which is *not* reliably bumped on API or ABI changes, and currently is still
# zero.
#
# We will therefore probably need to keep doing downstream .so versioning for
# the foreseeable future. Currently we are assuming that the ABI is likely to
# change on every release (an appropriate assumption for a large C++ project
# with no ABI stability policy), so we build the .so version from the project
# version. Note that the “hidden” major version is zero, so this complies with
# the “0.” prefix recommended in the packaging guidelines.
#
# https://docs.fedoraproject.org/en-US/packaging-guidelines/#_downstream_so_name_versioning
#
# A known defect of this patch is that it causes the hdTiny.so example plugin
# to be versioned as well, which is undesired. This is not a serious problem
# because we do not want to package the built plugin anyway. (It should not be
# built with -DPXR_BUILD_EXAMPLES=OFF, but it is.)
Patch:          0001-Downstream-only-add-an-SONAME-version.patch

# Port to Embree 4.x
# https://github.com/PixarAnimationStudios/OpenUSD/pull/2266
# See also:
# hdEmbree: add support for building against embree4
# https://github.com/PixarAnimationStudios/USD/pull/2266
Patch:          %{forgeurl}/pull/2266.patch

# Downstream-only: use the system double-conversion library
Patch:          0001-Downstream-only-use-the-system-double-conversion-lib.patch
# Downstream-only: use the system lz4 library
Patch:          0002-Downstream-only-use-the-system-lz4-library.patch
# Downstream-only: use the system pugixml library
Patch:          0003-Downstream-only-use-the-system-pugixml-library.patch
# Downstream-only: use the system rapidjson library
Patch:          0004-Downstream-only-use-the-system-rapidjson-library.patch
# Downstream-only: use the system libdeflate library
Patch:          0005-Downstream-only-use-the-system-libdeflate.patch
# Downstream-only: use the system libavif library
Patch:          0006-Downstream-only-use-the-system-libavif.patch

# work: account for task_group_base interface change in oneTBB 2022.0.0
# https://github.com/PixarAnimationStudios/OpenUSD/pull/3392
# Merged as commit 534b22c12dc18203ab5b233792debca8bf843b2e.
Patch:          %{forgeurl}/commit/534b22c12dc18203ab5b233792debca8bf843b2e.patch

# Add missing #include <cstdint>
# https://github.com/PixarAnimationStudios/OpenUSD/pull/3487
# Fixes failure to compile with GCC 15
Patch:          %{forgeurl}/pull/3487.patch

# Base
BuildRequires:  gcc-c++

BuildRequires:  cmake
%if %{with ninja}
BuildRequires:  ninja-build
%endif

BuildRequires:  dos2unix
BuildRequires:  help2man

BuildRequires:  pkgconfig(blosc)
BuildRequires:  pkgconfig(dri)
BuildRequires:  hdf5-devel
BuildRequires:  opensubdiv-devel >= 3.6.0
BuildRequires:  pkgconfig(tbb)
# Unbundled:
BuildRequires:  cmake(double-conversion)
BuildRequires:  pkgconfig(liblz4)
BuildRequires:  cli11-devel cli11-static
BuildRequires:  cmake(pugixml)
BuildRequires:  rapidjson-devel rapidjson-static
BuildRequires:  robin-map-devel robin-map-static
BuildRequires:  pkgconfig(libdeflate)
# Unbundling this means we also use external versions of libaom and libyuv.
BuildRequires:  pkgconfig(libavif)

BuildRequires:  cmake(Imath) >= 3.0

%if %{with alembic}
BuildRequires:  cmake(Alembic)
%endif

%if %{with draco}
BuildRequires:  draco-devel
%endif

%if %{with embree}
BuildRequires:  embree-devel
%endif

%if %{with jemalloc}
BuildRequires:  pkgconfig(jemalloc)
%endif

%if %{with ocio}
BuildRequires:  cmake(OpenColorIO)
%endif

%if %{with oiio}
BuildRequires:  cmake(OpenImageIO)
%endif

%if %{with openshading}
BuildRequires:  openshadinglanguage
BuildRequires:  pkgconfig(oslexec)
%endif

%if %{with openvdb}
BuildRequires:  openvdb-devel
%endif

%if %{with ptex}
BuildRequires:  pkgconfig(ptex)
%endif

# Header-only library: -static is for tracking per guidelines
#
# Enforce the the minimum EVR to contain fixes for all of:
# CVE-2021-28021
# CVE-2021-42715
# CVE-2021-42716
# CVE-2022-28041
# CVE-2023-43898
# CVE-2023-45661
# CVE-2023-45662
# CVE-2023-45663
# CVE-2023-45664
# CVE-2023-45666
# CVE-2023-45667
BuildRequires:  stb_image-devel >= 2.28^20231011gitbeebb24-12
BuildRequires:  stb_image-static
BuildRequires:  stb_image_write-devel >= 1.16
BuildRequires:  stb_image_write-static
BuildRequires:  stb_image_resize-devel >= 0.97
BuildRequires:  stb_image_resize-static

Requires:       usd-libs%{?_isa} = %{version}-%{release}
Requires:       python3-usd%{?_isa} = %{version}-%{release}

# This package is only available for x86_64 and aarch64
# Will fail to build on other architectures
# https://bugzilla.redhat.com/show_bug.cgi?id=1960848
#
# Note that pxr/base/arch/assumptions.cpp explicitly tests the machine is not
# big-endian, and pxr/base/arch/defines.h explicitly enforces x86_64 or ARM64.
ExclusiveArch:  aarch64 x86_64

%description
Universal Scene Description (USD) is a time-sampled scene
description for interchange between graphics applications.

%package        libs
Summary:        Universal Scene Description library

# Filed ticket to convince upstream to use system libraries
#   Use system libraries instead of bundling them when possible
#   https://github.com/PixarAnimationStudios/USD/issues/1490
# See also:
#   Path to using external/system copies of OpenEXRCore and libdeflate?
#   https://github.com/PixarAnimationStudios/OpenUSD/issues/2619
# Version from: pxr/base/gf/ilmbase_half.README
#
# This is difficult to unbundle even in the manner of double-conversion: code
# that uses the half type is compatible with ilmbase version 2 (as packaged in
# openexr2) rather than version 3 (as packaged in the ilmbase package).
# Unfortunately, we need cmake(Imath) elsewhere in the package, and this comes
# from the imath package (version 3), which conflicts with the imath version 2
# libraries included with openexr2. So this will not be possible until the
# surrounding code is patched (upstream or downstream) for compatibility with
# ilmbase version 3, something we’re currently not willing to attempt.
Provides:       bundled(ilmbase) = 2.5.3
# Version from: pxr/base/pegtl/pegtl/version.hpp
# Currently, Fedora’s PEGTL is too old:
# https://bugzilla.redhat.com/show_bug.cgi?id=1902427
Provides:       bundled(PEGTL) = 3.2.7
# Version from pxr/imaging/hio/OpenEXR/OpenEXRCore/openexr_version.h
# From pxr/imaging/hio/OpenEXR/README.md:
#   A few changes are still in progress to upstreamed to the OpenEXR project,
#   but these are minor, and otherwise, almost all differences between the
#   interred OpenEXRCore and the official OpenEXR repo are consolidated to the
#   openexr_conf.h header. The remaining differences are removing an extern
#   marking from the few global data tables.
# This suggests that it may not be entirely safe to unbundle this.
Provides:       bundled(openexr) = 3.2.0
# Version from the message for the commit
# e7a8d718c7c113e1c653ee31dc52421f17e09b42 that introduced pxr/external/boost/:
#
#   python: Initial import of boost::python from boost 1.85.0
#   This change just brings boost::python into the tree as a starting point for
#   the pxr_boost::python implementation. The src/ and test/ directories are
#   placed next to the public headers since we don't have separate
#   public/private directory hierarchies like boost, but the code itself is
#   unchanged and not included in the build.
#
#   We use boost 1.85.0 as the starting point even though we're currently on
#   VFX Reference Platform 2022, which specifies boost 1.76.0. This is because
#   later versions of boost are needed for other platforms and versions of
#   Python that OpenUSD supports. For example Python 3.11 requires boost
#   1.82.0+.
#
# This is not a candidate for unbundling because upstream has explicitly forked
# boost::python and modified it to work without the rest of Boost as part of an
# effort to remove the Boost dependency. While pxr_boost::python is derived
# from boost::python, it is not intended to remain compatible with it.
Provides:       bundled(boost) = 1.85.0

# We are currently able to unbundle these and use system libraries, but we
# retain the virtual Provides, commented out, as documentation and in case we
# ever have to switch back to the bundled versions.
#
# Version from: pxr/base/tf/pxrDoubleConversion/README
# Provides:       bundled(double-conversion) = 3.3.0
# Version from: pxr/base/tf/pxrLZ4/lz4.h (LZ4_VERSION_{MAJOR,MINOR_PATCH})
# Provides:       bundled(lz4) = 1.9.2
# Version from: pxr/base/tf/pxrCLI11/README.md
# Provides:       bundled(cli11) = 2.3.1
# Version from:
# third_party/renderman-26/plugin/rmanArgsParser/pugixml/pugiconfig.hpp
# (header comment)
# Provides:       bundled(pugixml) = 1.9
# Version from: pxr/base/js/rapidjson/rapidjson.h
# (RAPIDJSON_{MAJOR,MINOR,PATCH}_VERSION)
# Provides:       bundled(rapidjson) = 1.1.0
# Version from: pxr/base/tf/pxrTslRobinMap/robin_growth_policy.h
# (PXR_TSL_RH_VERSION_{MAJOR,MINOR,PATCH})
# Provides:       bundled(robin-map) = 1.3.0
# Version from pxr/imaging/hio/OpenEXR/deflate/libdeflate.h
# Provides:       bundled(libdeflate) = 1.18
# Version from pxr/imaging/plugin/hioAvif/AVIF/src/avif/avif.h
#   We actually have a post-release snapshot of libavif, because
#   AVIF_VERSION_DEVEL is nonzero, but it’s not easy to determine which commit
#   hash it was copied from.
# Provides:       bundled(libavif) = 1.0.1
# Version from pxr/imaging/plugin/hioAvif/AVIF/src/src-libyuv/libyuv/version.h
# LIBYUV_VERSION is a “serial number” version, e.g. 1895, that gets incremented
# every time changes are dumped into git from an internal VCS; the libyuv
# package in Fedora is considered to have version 0 and uses snapshot
# versioning. We can dig through
# https://chromium.googlesource.com/libyuv/libyuv and find the commit hash that
# corresponds to a particular serial number.
# LIBYUV_VERSION 1895 = commit a97746349b244efd54ab1eb0c0a7366717b33f39
# Provides:       bundled(libyuv) = 0^20240812gita977463
# Version from pxr/imaging/plugin/hioAvif/aom/config/aom_version.h
# Provides:       bundled(aom) = 3.0.0

%description libs
Universal Scene Description (USD) is an efficient, scalable system for
authoring, reading, and streaming time-sampled scene description for
interchange between graphics applications.

%package        devel
Summary:        Development files for USD
Requires:       usd-libs%{?_isa} = %{version}-%{release}

# Unbundled, and exposed in the API:
Requires:       cli11-devel cli11-static
Requires:       robin-map-devel robin-map-static

%description devel
This package contains the C++ header files and symbolic links to the shared
libraries for usd. If you would like to develop programs using usd,
you will need to install usd-devel.

# For usdview, usdcompress
%package -n python3-usd
Summary: %{summary}

BuildRequires:  pkgconfig(python3)
BuildRequires:  python3dist(jinja2)
%if %{with usdview}
BuildRequires:  desktop-file-utils
BuildRequires:  python3dist(pyside6)
BuildRequires:  pyside6-tools
%endif
BuildRequires:  python3dist(pyopengl)
Requires:       font(roboto)
Requires:       font(robotoblack)
Requires:       font(robotolight)
Requires:       font(robotomono)
Requires:       python3dist(jinja2)
%if %{with usdview}
Requires:       python3dist(pyside6)
%endif
Requires:       python3dist(pyopengl)

Requires:       usd-libs%{?_isa} = %{version}-%{release}

%py_provides    python3-pxr

%description -n python3-usd
Python language bindings for the Universal Scene Description (USD) C++ API

%prep
%autosetup -p1 -n OpenUSD-%{version}

# Convert NOTICE.txt from CRNL line encoding
dos2unix NOTICE.txt

# Fix all Python shebangs recursively in .
%py3_shebang_fix .

# Further drop shebangs line for some py files
sed -r -i '1{/^#!/d}' \
        pxr/usd/sdr/shaderParserTestUtils.py \
        pxr/usd/usdUtils/updateSchemaWithSdrNode.py \
        pxr/usdImaging/usdviewq/usdviewApi.py

# Unbundle Google Roboto fonts
rm -rvf pxr/usdImaging/usdviewq/fonts/*
ln -s %{_datadir}/fonts/google-roboto pxr/usdImaging/usdviewq/fonts/Roboto
ln -s %{_datadir}/fonts/google-roboto-mono \
    pxr/usdImaging/usdviewq/fonts/Roboto_Mono

# Unbundle stb_image, stb_image_write, stb_image_resize:
pushd pxr/imaging/hio/stb
cp -p %{_usr}/include/stb_image.h .
patch -p1 < stb_image.patch
ln -svf %{_usr}/include/stb_image_resize.h \
    %{_usr}/include/stb_image_write.h ./
popd

# Remove bundled doxygen-awesome-css (CSS and JS files) since we are not
# building Doxygen-generated HTML documentation.
rm -rf docs/doxygen/doxygen-awesome-css/

# Remove the bundled copy of double-conversion.
#
# From pxr/base/tf/pxrDoubleConversion/README, the upstream double-conversion
# is patched with pxr/base/tf/pxrDoubleConversion/pxr-double-conversion.patch;
# examination of that patch shows that it merely adds namespaces and renames
# symbols, rather than making functional changes, so using the system library
# should be safe.
find pxr/base/tf/pxrDoubleConversion -type f ! -name '*.h' -print -delete
for hdr in pxr/base/tf/pxrDoubleConversion/*.h
do
  cat > "${hdr}" <<EOF
#include <double-conversion/$(basename "${hdr}")>
namespace pxr_double_conversion = double_conversion;
EOF
done
# Similarly, remove the bundled copy of lz4. Change in the bundled copy can be
# identified by source-code comments, and appear to be limited to adding
# namespaces and removing C linkage.
rm -v pxr/base/tf/pxrLZ4/*
cat > pxr/base/tf/pxrLZ4/lz4.h <<'EOF'
#include <lz4.h>
// System LZ4 has C linkage; this just allows "using namespace"
namespace pxr_lz4 {}
EOF
# Remove the bundled copy of cli11.
rm -v pxr/base/tf/pxrCLI11/*
cat > pxr/base/tf/pxrCLI11/CLI11.h <<'EOF'
#include <CLI/CLI.hpp>
namespace pxr_CLI = CLI;
EOF
# Remove the bundled copy of pugixml.
find third_party/renderman-*/plugin/rmanArgsParser/pugixml/ \
    -type f ! -name '*.hpp' -print -delete
for hdr in third_party/renderman-*/plugin/rmanArgsParser/pugixml/*.hpp
do
  cat > "${hdr}" <<EOF
#include <$(basename "${hdr}")>
EOF
done
# Remove the bundled copy of rapidjson. It does not seem to have been modified
# or forked at all.
rm -rv pxr/base/js/rapidjson/
# Remove the bundled copy of robin-map. There are several macros that are
# renamed from TSL_*/tsl_* to PXR_TSL_*/pxr_tsl_* in the bundled copy, and we
# could “alias” these if necessary to avoid patching call sites, but for now
# are not used outside the library headers and we can get by with merely
# aliasing the namespace.
find pxr/base/tf/pxrTslRobinMap -type f ! -name '*.h' -print -delete
for hdr in pxr/base/tf/pxrTslRobinMap/*.h
do
  cat > "${hdr}" <<EOF
#include <tsl/$(basename "${hdr}")>
namespace pxr_tsl = tsl;
EOF
done
# Remove the bundled copy of libdeflate.
rm -rv pxr/imaging/hio/OpenEXR/deflate/
# Remove the bundled copies of libavif, along with the associated libaom and
# the libyuv that is in the libavif sources.
rm -rv pxr/imaging/plugin/hioAvif/aom/ \
    pxr/imaging/plugin/hioAvif/AVIF/

# Use c++17 standard otherwise build fails
sed -i 's|set(CMAKE_CXX_STANDARD 14)|set(CMAKE_CXX_STANDARD 17)|g' \
        cmake/defaults/CXXDefaults.cmake

# Fix libdir installation
sed -i 's|lib/usd|%{_libdir}/usd|g' \
        cmake/macros/{Private,Public}.cmake
sed -i 's|plugin/usd|%{_libdir}/usd/plugin|g' \
        cmake/macros/{Private,Public}.cmake
sed -i 's|"lib"|%{_libdir}|g' \
        cmake/macros/{Private,Public}.cmake
sed -i 's|/python|/python%{python3_version}/site-packages|g' \
        cmake/macros/{Private,Public}.cmake pxr/usdImaging/usdviewq/CMakeLists.txt
sed -i 's|/pxrConfig.cmake|%{_libdir}/cmake/pxr/pxrConfig.cmake|g' \
        pxr/CMakeLists.txt
sed -i 's|"cmake"|"%{_libdir}/cmake/pxr"|g' \
        pxr/CMakeLists.txt
sed -i 's|${PXR_CMAKE_DIR}/cmake|${PXR_CMAKE_DIR}|g' \
        pxr/pxrConfig.cmake.in
sed -i 's|${PXR_CMAKE_DIR}/include|/usr/include|g' \
        pxr/pxrConfig.cmake.in
sed -i 's|EXACT COMPONENTS|COMPONENTS|g' \
        pxr/pxrConfig.cmake.in

# Fix cmake directory destination
sed -i 's|"${CMAKE_INSTALL_PREFIX}"|%{_libdir}/cmake/pxr|g' pxr/CMakeLists.txt

# Use Embree4 instead of Embree3. The find-then-modify pattern preserves mtimes
# on sources that did not need to be modified.
find . -type f -exec gawk '/embree3/ { print FILENAME }' '{}' '+' |
  xargs -r sed -r -i 's/(embree)3/\14/'


%build
# The necessary include path for Imath is not set everywhere it’s needed. It’s
# not immediately clear exactly why this is happening here or what should be
# changed upstream.
extra_flags="${extra_flags-} $(pkgconf --cflags Imath)"

# Suppress deprecation warnings from TBB; upstream should act on them
# eventually, but they just add noise here.
extra_flags="${extra_flags-} -DTBB_SUPPRESS_DEPRECATED_MESSAGES=1"

%cmake \
%if %{with ninja}
     -GNinja \
%endif
%if %{with jemalloc}
     -DPXR_MALLOC_LIBRARY="%{_libdir}/libjemalloc.so" \
%endif
     \
     -DCMAKE_CXX_FLAGS_RELEASE="${CXXFLAGS-} ${extra_flags}" \
     -DCMAKE_CXX_STANDARD=17 \
     -DCMAKE_C_FLAGS_RELEASE="${CFLAGS-} ${extra_flags}" \
     -DCMAKE_EXE_LINKER_FLAGS="${LDFLAGS}" \
     -DCMAKE_SHARED_LINKER_FLAGS="${LDFLAGS}" \
     -DCMAKE_SKIP_INSTALL_RPATH=ON \
     -DCMAKE_SKIP_RPATH=ON \
     -DCMAKE_VERBOSE_MAKEFILE=ON \
     \
     -DPXR_BUILD_HTML_DOCUMENTATION=FALSE \
     -DPXR_BUILD_PYTHON_DOCUMENTATION=FALSE \
     -DPXR_BUILD_EXAMPLES=OFF \
     -DPXR_BUILD_IMAGING=ON \
     -DPXR_BUILD_MONOLITHIC=ON \
     -DPXR_BUILD_TESTS=%{expr:%{with test}?"ON":"OFF"} \
     -DPXR_BUILD_TUTORIALS=OFF \
     -DPXR_BUILD_USD_IMAGING=ON \
     -DPXR_BUILD_USD_TOOLS=ON \
     -DPXR_BUILD_USDVIEW=%{expr:%{with usdview}?"ON":"OFF"} \
     \
     -DPXR_BUILD_ALEMBIC_PLUGIN=%{expr:%{with alembic}?"ON":"OFF"} \
     -DPXR_BUILD_DRACO_PLUGIN=%{expr:%{with draco}?"ON":"OFF"} \
     -DPXR_BUILD_EMBREE_PLUGIN=%{expr:%{with embree}?"ON":"OFF"} \
     -DPXR_BUILD_MATERIALX_PLUGIN=%{expr:%{with materialx}?"ON":"OFF"} \
     -DPXR_BUILD_OPENCOLORIO_PLUGIN=%{expr:%{with ocio}?"ON":"OFF"} \
     -DPXR_BUILD_OPENIMAGEIO_PLUGIN=%{expr:%{with oiio}?"ON":"OFF"} \
     -DPXR_BUILD_PRMAN_PLUGIN=OFF \
     \
     -DPXR_ENABLE_OPENVDB_SUPPORT=%{expr:%{with openvdb}?"ON":"OFF"} \
     -DPXR_ENABLE_HDF5_SUPPORT=ON \
     -DPXR_ENABLE_PTEX_SUPPORT=%{expr:%{with ptex}?"ON":"OFF"} \
     -DPXR_ENABLE_OSL_SUPPORT=%{expr:%{with openshading}?"ON":"OFF"} \
     -DPXR_ENABLE_MALLOCHOOK_SUPPORT=OFF \
     -DPXR_ENABLE_PYTHON_SUPPORT=ON \
     \
     -DPXR_INSTALL_LOCATION="%{_libdir}/usd/plugin" \
     \
     -DPXR_VALIDATE_GENERATED_CODE=OFF \
     \
     -DPYSIDEUICBINARY:PATH=pyside6-uic \
     -DPYSIDE_AVAILABLE=ON \
     -DPYTHON_EXECUTABLE=%{python3}
%cmake_build

%install
%cmake_install

# Fix python3 files installation
mkdir -p %{buildroot}%{python3_sitearch}
mv %{buildroot}%{python3_sitelib}/* %{buildroot}%{python3_sitearch}

%if %{with usdview}
# Install a desktop icon for usdview
desktop-file-install                                    \
--dir=%{buildroot}%{_datadir}/applications              \
%{SOURCE1}
%endif

# Little hack until this issue is resolved
# https://github.com/PixarAnimationStudios/OpenUSD/issues/3310
sed -i 's|OpenGL::GL|${OPENGL_gl_LIBRARY}|g' \
        %{buildroot}%{_libdir}/cmake/pxr/pxrTargets.cmake

# Remove examples that were built and installed even though we set
# -DPXR_BUILD_EXAMPLES=OFF.
rm -vrf '%{buildroot}%{_datadir}/usd/examples'

# Generate and install man pages. While generating the man pages might more
# properly go in %%build, it is generally much easier to do this here in a
# single step, using the entry points installed into the buildroot. This is
# especially true for the entry points that are Python scripts.
install -d '%{buildroot}%{_mandir}/man1'
for cmd in %{buildroot}%{_bindir}/*
do
  PYTHONPATH='%{buildroot}%{python3_sitearch}' \
  LD_LIBRARY_PATH='%{buildroot}%{_libdir}' \
      help2man \
      --no-info --no-discard-stderr --version-string='%{version}' \
      --output="%{buildroot}%{_mandir}/man1/$(basename "${cmd}").1" \
      "${cmd}"
done

%check
%if %{with usdview}
desktop-file-validate %{buildroot}%{_datadir}/applications/org.openusd.usdview.desktop
%endif
%{?with_test:%ctest}

%files
%doc NOTICE.txt README.md

%{_bindir}/hdGenSchema
%{_bindir}/sdfdump
%{_bindir}/sdffilter
%{_bindir}/usdGenSchema
%{_bindir}/usdcat
%{_bindir}/usdchecker
%if %{with draco}
%{_bindir}/usdcompress
%endif
%{_bindir}/usddiff
%{_bindir}/usddumpcrate
%{_bindir}/usdedit
%{_bindir}/usdfixbrokenpixarschemas
%{_bindir}/usdgenschemafromsdr
%{_bindir}/usdmeasureperformance
%{_bindir}/usdrecord
%{_bindir}/usdresolve
%{_bindir}/usdstitch
%{_bindir}/usdstitchclips
%{_bindir}/usdtree
%{_bindir}/usdzip
%if %{with usdview}
%{_datadir}/applications/org.openusd.usdview.desktop
%{_bindir}/testusdview
%{_bindir}/usdview
%endif

%{_mandir}/man1/hdGenSchema.1*
%{_mandir}/man1/sdfdump.1*
%{_mandir}/man1/sdffilter.1*
%{_mandir}/man1/usdGenSchema.1*
%{_mandir}/man1/usdcat.1*
%{_mandir}/man1/usdchecker.1*
%if %{with draco}
%{_mandir}/man1/usdcompress.1*
%endif
%{_mandir}/man1/usddiff.1*
%{_mandir}/man1/usddumpcrate.1*
%{_mandir}/man1/usdedit.1*
%{_mandir}/man1/usdfixbrokenpixarschemas.1*
%{_mandir}/man1/usdgenschemafromsdr.1*
%{_mandir}/man1/usdmeasureperformance.1*
%{_mandir}/man1/usdrecord.1*
%{_mandir}/man1/usdresolve.1*
%{_mandir}/man1/usdstitch.1*
%{_mandir}/man1/usdstitchclips.1*
%{_mandir}/man1/usdtree.1*
%{_mandir}/man1/usdzip.1*
%if %{with usdview}
%{_mandir}/man1/testusdview.1*
%{_mandir}/man1/usdview.1*
%endif

%files -n python3-usd
%{python3_sitearch}/pxr/

%files libs
%license LICENSE.txt
%doc NOTICE.txt README.md
%{_libdir}/libusd_ms.so.%{downstream_so_version}
# While headers normally go in -devel packages, those in
# %%{_libdir}/usd/usd/resources/codegenTemplates/ are used as data (templates
# for generated code), and it makes sense to package them with the rest of the
# library resources. (Technically, these are currently used only by the
# usdGenSchema command-line tool, so they could be moved to the base package,
# but this is probably too fussy.)
%{_libdir}/usd/

%files devel
%doc BUILDING.md CHANGELOG.md VERSIONS.md
%{_includedir}/pxr/
%{_libdir}/libusd_ms.so
%{_libdir}/cmake/pxr/pxrConfig.cmake
%{_libdir}/cmake/pxr/pxrTargets.cmake
%{_libdir}/cmake/pxr/pxrTargets-release.cmake

%changelog
%autochangelog
