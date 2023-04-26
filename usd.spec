# We hard-code the ABI version here, even though it can be derived from the
# package version, as a reminder of the need to rebuild dependent packages on
# every update. See additional notes near the downstream ABI versioning patch.
# It should be 0.MAJOR.MINOR without leading zeros, e.g. 22.03 → 0.22.3.
%global downstream_so_version 0.23.05

%bcond_without  alembic
%bcond_with     documentation
%bcond_without  draco
%bcond_without  embree
%bcond_with     jemalloc
# Not yet packaged: https://github.com/AcademySoftwareFoundation/MaterialX
%bcond_with     materialx
# Default "UNIX Makefiles" backend for CMake would also work fine; ninja is a
# bit faster. We conditionalize it just in case there are backend-specific
# issues in the future.
%bcond_without  ninja
%bcond_without  openshading
%bcond_without  openvdb
%bcond_without  ocio
%bcond_without  oiio
%bcond_without  ptex
# Not yet packaged
%bcond_with     pyside6
%bcond_without  usdview
# TODO: Figure out how to re-enable the tests. Currently these want to install
# into /usr/tests and, and there are issues with the launchers finding the
# command-line tools in the buildroot.
%bcond_with  test

Name:           usd
Version:        23.05
Release:        %autorelease
Summary:        3D VFX pipeline interchange file format

# The entire source is Apache-2.0 except:
#
# BSD-3-Clause:
#   - pxr/base/gf/ilmbase_*
#   - pxr/base/js/rapidjson/msinttypes/
#   - pxr/base/tf/pxrDoubleConversion/
#   - pxr/base/tf/pxrCLI11/
# BSD-2-Clause:
#   - pxr/base/tf/pxrLZ4/
# MIT:
#   - pxr/imaging/garch/khrplatform.h
#   - pxr/base/js/rapidjson/, except pxr/base/js/rapidjson/msinttypes/
#   - third_party/renderman-24/plugin/rmanArgsParser/pugixml/
#   - pxr/base/tf/pxrTslRobinMap/
#   - pxr/imaging/hgiVulkan/vk_mem_alloc.h
# MIT OR Unlicense:
#   - pxr/imaging/hio/stb/
# Apache-2.0 AND GPL-3.0-or-later WITH Bison-exception-2.2:
#   - pxr/usd/sdf/path.tab.{cpp,h}
#   - pxr/usd/sdf/textFileFormat.tab.{cpp,h}
#   - third_party/renderman-24/plugin/hdPrman/virtualStructConditionalGrammar.tab.{cpp,h}
#
# (Certain build system files are also under licenses other than Apache-2.0, but
# do not contribute their license terms to the built RPMs.)
License:        Apache-2.0 AND BSD-3-Clause AND BSD-2-Clause AND MIT AND (MIT OR Unlicense) AND (Apache-2.0 AND GPL-3.0-or-later WITH Bison-exception-2.2)
URL:            http://www.openusd.org/
%global forgeurl https://github.com/PixarAnimationStudios/usd
Source0:        %{forgeurl}/archive/v%{version}/usd-%{version}.tar.gz
Source1:        org.openusd.usdview.desktop
# Latest stb_image.patch that applies cleanly against 2.27:
#   %%{forgeurl}/raw/8f9bb9563980b41e7695148b63bf09f7abd38a41/pxr/imaging/hio/stb/stb_image.patch
# We treat this as a source file because it is applied separately during
# unbundling. It has been hand-edited to apply to 2.28, where
# stbi__unpremultiply_on_load_thread is already renamed to
# stbi_set_unpremultiply_on_load_thread.
Source2:        stb_image.patch

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
Patch:          USD-23.05-soversion.patch

# Port to Embree 4.x
# https://github.com/PixarAnimationStudios/USD/pull/2266
Patch:          %{forgeurl}/pull/2266.patch

# Base
BuildRequires:  gcc-c++

BuildRequires:  cmake
%if %{with ninja}
BuildRequires:  ninja-build
%endif

BuildRequires:  dos2unix
BuildRequires:  help2man

BuildRequires:  pkgconfig(blosc)
BuildRequires:  boost-devel
BuildRequires:  pkgconfig(dri)
BuildRequires:  hdf5-devel
BuildRequires:  opensubdiv-devel
BuildRequires:  pkgconfig(tbb)

BuildRequires:  cmake(OpenEXR) >= 3.0
BuildRequires:  cmake(Imath) >= 3.0

%if %{with alembic}
BuildRequires:  cmake(Alembic)
%endif

%if %{with documentation}
BuildRequires:  doxygen
BuildRequires:  graphviz
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
BuildRequires:  pkgconfig(OpenImageIO)
%endif

%if %{with openshading}
BuildRequires:  openshadinglanguage
BuildRequires:  pkgconfig(oslexec)
%endif

%if %{with openvdb}
BuildRequires:  openvdb-devel
%endif

%if %{with ptex}
BuildRequires:  pkgconfig(Ptex)
%endif


# Header-only library: -static is for tracking per guidelines
#
# Enforce the the minimum EVR to contain fixes for all of CVE-2021-28021,
# CVE-2021-42715, CVE-2021-42716, and CVE-2022-28041, plus the null-pointer
# dereference bug https://github.com/nothings/stb/issues/1452.
BuildRequires:  stb_image-devel >= 2.28^20230129git5736b15-0.2
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

# Upstream bundles
# Filed ticket to convince upstream to use system libraries
# https://github.com/PixarAnimationStudios/USD/issues/1490
# Version from: pxr/base/tf/pxrDoubleConversion/README
Provides:       bundled(double-conversion) = 2.0.0
# Version from: pxr/base/gf/ilmbase_half.README
Provides:       bundled(ilmbase) = 2.5.3
# Version from: pxr/base/tf/pxrLZ4/lz4.h (LZ4_VERSION_{MAJOR,MINOR_PATCH})
Provides:       bundled(lz4) = 1.9.2
# Version from: pxr/base/tf/pxrCLI11/README.md
Provides:       bundled(cli11) = 2.3.1
# Version from:
# third_party/renderman-24/plugin/rmanArgsParser/pugixml/pugiconfig.hpp
# (header comment)
Provides:       bundled(pugixml) = 1.9
# Version from: pxr/base/js/rapidjson/rapidjson.h
# (RAPIDJSON_{MAJOR,MINOR,PATCH}_VERSION)
Provides:       bundled(rapidjson) = 1.1.0
# Version from: pxr/imaging/hgiVulkan/spirv_reflect.h (header comment)
Provides:       bundled(SPIRV-Reflect) = 1.0
# Version from: pxr/imaging/hgiVulkan/vk_mem_alloc.h (header comment)
Provides:       bundled(VulkanMemoryAllocator) = 3.0.0~development
# Forked from an unknown version:
# pxr/base/tf/pxrTslRobinMap/
Provides:       bundled(robin-map)

%description libs
Universal Scene Description (USD) is an efficient, scalable system for
authoring, reading, and streaming time-sampled scene description for
interchange between graphics applications.

%package        devel
Summary:        Development files for USD
Requires:       usd-libs%{?_isa} = %{version}-%{release}

%description devel
This package contains the C++ header files and symbolic links to the shared
libraries for usd. If you would like to develop programs using usd,
you will need to install usd-devel.

# For usdview, usdcompress
%package -n python3-usd
Summary: %{summary}

BuildRequires:  pkgconfig(python3)
BuildRequires:  pkgconfig(Qt5)
BuildRequires:  python3dist(jinja2)
%if %{with usdview}
BuildRequires:  desktop-file-utils
%if %{with pyside6}
BuildRequires:  python3dist(pyside6)
%else
BuildRequires:  python3dist(pyside2)
%endif
%endif
BuildRequires:  python3dist(pyopengl)
Requires:       font(roboto)
Requires:       font(robotoblack)
Requires:       font(robotolight)
Requires:       font(robotomono)
Requires:       python3dist(jinja2)
%if %{with usdview}
%if %{with pyside6}
Requires:       python3dist(pyside6)
%else
Requires:       python3dist(pyside2)
%endif
%endif
Requires:       python3dist(pyopengl)
%py_provides    python3-pxr

%description -n python3-usd
Python language bindings for the Universal Scene Description (USD) C++ API


%if %{with documentation}
%package        doc
Summary:        Documentation for usd
BuildArch:      noarch

%description doc
Documentation for the Universal Scene Description (USD) C++ API
%endif

%prep
%autosetup -p1 -n USD-%{version}

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
cp -p %{_includedir}/stb_image.h .
patch -p1 < '%{SOURCE2}'
ln -svf %{_includedir}/stb_image_resize.h \
    %{_includedir}/stb_image_write.h ./
popd

# Use c++17 standard otherwise build fails
sed -i 's|set(CMAKE_CXX_STANDARD 14)|set(CMAKE_CXX_STANDARD 17)|g' \
        cmake/defaults/CXXDefaults.cmake

# Fix libdir installation
sed -i 's|lib/usd|%{_libdir}/usd|g' cmake/macros/Private.cmake
sed -i 's|"lib"|%{_libdir}|g' cmake/macros/Private.cmake
sed -i 's|plugin/usd|%{_libdir}/usd/plugin|g' \
        cmake/macros/Private.cmake
sed -i 's|/python|/python%{python3_version}/site-packages|g' \
        cmake/macros/Private.cmake
sed -i 's|lib/usd|%{_libdir}/usd|g' cmake/macros/Public.cmake
sed -i 's|"lib"|%{_libdir}|g' cmake/macros/Public.cmake
sed -i 's|plugin/usd|%{_libdir}/usd/plugin|g' \
        cmake/macros/Public.cmake

# Fix cmake directory destination
sed -i 's|"${CMAKE_INSTALL_PREFIX}"|%{_libdir}/cmake/pxr|g' pxr/CMakeLists.txt

# Use Embree4 instead of Embree3. The find-then-modify pattern preserves mtimes
# on sources that did not need to be modified.
find . -type f -exec gawk '/embree3/ { print FILENAME }' '{}' '+' |
  xargs -r sed -r -i 's/(embree)3/\14/'

# Fix uic-qt5 use
cat > uic-wrapper <<'EOF'
#!/bin/sh
exec uic-qt5 -g python "$@"
EOF
chmod +x uic-wrapper


%build
%set_build_flags

# Although upstream supports OpenEXR3 / Imath now, the necessary include path
# is not set everywhere it’s needed. It’s not immediately clear exactly why
# this is happening here or what should be changed upstream.
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
     -DPXR_BUILD_DOCUMENTATION=%{expr:%{with documentation}?"TRUE":"FALSE"} \
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
     -DPYSIDEUICBINARY:PATH=${PWD}/uic-wrapper \
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

# Remove examples that were built and installed even though we set
# -DPXR_BUILD_EXAMPLES=OFF.
rm -vrf '%{buildroot}%{_datadir}/usd/examples'

# Fix installation path for some files
mv %{buildroot}%{_prefix}/lib/python/pxr/*.* \
        %{buildroot}%{python3_sitearch}/pxr/
%if %{with usdview}
mv %{buildroot}%{_prefix}/lib/python/pxr/Usdviewq/* \
        %{buildroot}%{python3_sitearch}/pxr/Usdviewq/
%endif

# TODO: Can we figure out how to fix the installation path for
# pxrTargets{,-release}.cmake, instead of moving them after the fact? We choose
# to put them in the same directory as pxrConfig.cmake.
find %{buildroot}%{_prefix}/cmake -mindepth 1 -maxdepth 1 -type f \
    -exec mv -v '{}' '%{buildroot}%{_libdir}/cmake/pxr' ';'

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
%{_libdir}/usd/
%exclude %{_libdir}/usd/usd/resources/codegenTemplates

%files devel
%doc BUILDING.md CHANGELOG.md VERSIONS.md
%{_includedir}/pxr/
%{_libdir}/libusd_ms.so
%{_libdir}/usd/usd/resources/codegenTemplates/
%{_libdir}/cmake/pxr/pxrConfig.cmake
%{_libdir}/cmake/pxr/pxrTargets.cmake
%{_libdir}/cmake/pxr/pxrTargets-release.cmake

%if %{with documentation}
%files doc
%license LICENSE.txt
%{_docdir}/usd/
%endif

%changelog
%autochangelog
