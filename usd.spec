# We hard-code the ABI version here, even though it can be derived from the
# package version, as a reminder of the need to rebuild dependent packages on
# every update. See additional notes near the downstream ABI versioning patch.
# It should be 0.MAJOR.MINOR without leading zeros, e.g. 22.03 → 0.22.3.
%global downstream_so_version 0.22.5

%bcond_without  alembic
%bcond_with     documentation
%bcond_without  embree
%bcond_without  imaging
%bcond_with     jemalloc
%bcond_with     openshading
%bcond_with     openvdb
%bcond_without  ocio
%bcond_without  oiio
%bcond_without  python3
%bcond_without  usdview
# TODO: Figure out how to re-enable the tests. Currently these want to install
# into /usr/tests and, and there are issues with the launchers finding the
# command-line tools in the buildroot.
%bcond_with  test

Name:           usd
Version:        22.05b
Release:        %autorelease -b 9
Summary:        3D VFX pipeline interchange file format

# The entire source is ASL 2.0 except:
#
# BSD:
#   - pxr/base/gf/ilmbase_*
#   - pxr/base/js/rapidjson/msinttypes/
#   - pxr/base/tf/pxrDoubleConversion/
#   - pxr/base/tf/pxrLZ4/
# MIT:
#   - pxr/imaging/garch/khrplatform.h
#   - pxr/base/js/rapidjson/, except pxr/base/js/rapidjson/msinttypes/
#   - third_party/renderman-24/plugin/rmanArgsParser/pugixml/
#   - pxr/base/tf/pxrTslRobinMap/
#   - pxr/imaging/hgiVulkan/vk_mem_alloc.h
# MIT or Unlicense:
#   - pxr/imaging/hio/stb/
#
# (Certain build system files are also under licenses other than ASL 2.0, but
# do not contribute their license terms to the built RPMs.)
#
# The following files mention GPLv3+, but are distributed under ASL 2.0 due to
# the special exception for Bison parser skeletons. See the comments in their
# headers for details.
#
#   - pxr/usd/sdf/path.tab.{cpp,h}
#   - pxr/usd/sdf/textFileFormat.tab.{cpp,h}
#   - third_party/renderman-24/plugin/hdPrman/virtualStructConditionalGrammar.tab.{cpp,h}
License:        ASL 2.0 and BSD and MIT and (MIT or Unlicense)
URL:            http://www.openusd.org/
%global forgeurl https://github.com/PixarAnimationStudios/%{name}
Source0:        %{forgeurl}/archive/v%{version}/%{name}-%{version}.tar.gz
Source1:        org.open%{name}.%{name}view.desktop

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
Patch:          USD-22.05-soversion.patch

# Support OpenEXR 3
# https://github.com/PixarAnimationStudios/USD/issues/1591
#
# See also:
# Support compiling against imath
# https://github.com/PixarAnimationStudios/USD/pull/1829
# Support OpenVDB without depending on OpenEXR
# https://github.com/PixarAnimationStudios/USD/pull/1728
Patch:          USD-22.05-OpenEXR3.patch

# Allow building against recent glibc with no malloc hooks (>= 2.34)
# https://github.com/PixarAnimationStudios/USD/pull/1830
Patch:          %{forgeurl}/pull/1830.patch

# Do not access PyFrameObject fields directly on Python 3.10+
#
# Fixes a Python 3.11 incompatibility. Still accesses PyCodeObject fields
# directly.
# https://github.com/PixarAnimationStudios/USD/pull/1928
Patch:          %{forgeurl}/pull/1928.patch

# Base
BuildRequires:  boost-devel
BuildRequires:  boost-program-options
BuildRequires:  cmake
BuildRequires:  dos2unix
BuildRequires:  gcc-c++
BuildRequires:  pkgconfig(blosc)
BuildRequires:  pkgconfig(tbb)

# Documentation
%if %{with documentation}
BuildRequires:  doxygen
BuildRequires:  graphviz
%endif

# For imaging and usd imaging
%if %{with imaging}
%if %{with embree}
BuildRequires:  embree-devel
%endif
%if %{with openshading}
BuildRequires:  openshadinglanguage
BuildRequires:  pkgconfig(oslexec)
%endif
BuildRequires:  opensubdiv-devel
%if %{with openvdb}
BuildRequires:  openvdb-devel
%endif
BuildRequires:  pkgconfig(dri)
%if %{with jemalloc}
BuildRequires:  pkgconfig(jemalloc)
%endif
%if %{with ocio}
# usd is not yet compatible with OpenColorIO 2 so use compat package.
BuildRequires:  pkgconfig(OpenColorIO) < 2
%endif
%if %{with oiio}
BuildRequires:  pkgconfig(OpenImageIO)
%endif
BuildRequires:  cmake(OpenEXR)
%if 0%{?fedora} < 35
BuildRequires:  pkgconfig(IlmBase) >= 2.0
%else
BuildRequires:  cmake(Imath) >= 2.0
%endif
BuildRequires:  pkgconfig(Ptex)
%endif
%if %{with alembic}
BuildRequires:  cmake(Alembic)
BuildRequires:  hdf5-devel
%endif

# Header-only library: -static is for tracking per guidelines
#
# stb_image 2.27^20210910gitaf1a5bc-0.2 is the minimum EVR to contain fixes for
# all of CVE-2021-28021, CVE-2021-42715, CVE-2021-42716, and CVE-2022-28041.
BuildRequires:  stb_image-devel >= 2.27^20210910gitaf1a5bc-0.2
BuildRequires:  stb_image-static
BuildRequires:  stb_image_write-devel
BuildRequires:  stb_image_write-static
BuildRequires:  stb_image_resize-devel
BuildRequires:  stb_image_resize-static

Requires:       %{name}-libs%{?_isa} = %{version}-%{release}
%if %{with python3}
Requires:       python3-%{name}%{?_isa} = %{version}-%{release}
%endif

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
# Version from:
# third_party/renderman-24/plugin/rmanArgsParser/pugixml/pugiconfig.hpp
# (header comment)
Provides:       bundled(pugixml) = 1.9
# Version from: pxr/base/js/rapidjson/rapidjson.h
# (RAPIDJSON_{MAJOR,MINOR,PATCH}_VERSION)
Provides:       bundled(rapidjson) = 1.0.2
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
Requires:       cmake-filesystem
Requires:       %{name}-libs%{?_isa} = %{version}-%{release}

%description devel
This package contains the C++ header files and symbolic links to the shared
libraries for %{name}. If you would like to develop programs using %{name},
you will need to install %{name}-devel.

# For usdview
%if %{with python3}
%package -n python3-%{name}
Summary: %{summary}

BuildRequires:  pkgconfig(python3)
BuildRequires:  pkgconfig(Qt5)
BuildRequires:  python3dist(jinja2)
%if %{with usdview}
BuildRequires:  desktop-file-utils
BuildRequires:  python3dist(pyside2)
%endif
BuildRequires:  python3dist(pyopengl)
Requires:       font(roboto)
Requires:       font(robotoblack)
Requires:       font(robotolight)
Requires:       font(robotomono)
Requires:       python3dist(jinja2)
%if %{with usdview}
Requires:       python3dist(pyside2)
%endif
Requires:       python3dist(pyopengl)
%py_provides    python3-pxr

%description -n python3-%{name}
Python language bindings for the Universal Scene Description (USD) C++ API
%endif

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

%if %{with python3}
# Fix all Python shebangs recursively in .
%py3_shebang_fix .
%endif

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
cp -p %{_includedir}/stb_image.h %{_includedir}/stb_image_write.h .
cat stb_image.patch stb_image_write.patch | patch -p1
ln -svf %{_includedir}/stb_image_resize.h ./
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

%build
# Fix uic-qt5 use
cat > uic-wrapper <<'EOF'
#!/bin/sh
exec uic-qt5 -g python "$@"
EOF
chmod +x uic-wrapper

# Fix python3 support
# https://github.com/PixarAnimationStudios/USD/issues/1419

flags="%{optflags} -Wl,--as-needed -DTBB_SUPPRESS_DEPRECATED_MESSAGES=1" \
# Patch2 was not good enough to get the include path for Imath everywhere it
# was needed. Add it globally.
# https://github.com/PixarAnimationStudios/USD/issues/1591
flags="${flags} $(pkgconf --cflags Imath)"

%cmake \
     -DCMAKE_CXX_FLAGS_RELEASE="${flags}" \
     -DCMAKE_C_FLAGS_RELEASE="${flags}" \
     -DCMAKE_CXX_STANDARD=17 \
     -DCMAKE_EXE_LINKER_FLAGS="-pie" \
     -DCMAKE_SKIP_RPATH=ON \
     -DCMAKE_SKIP_INSTALL_RPATH=ON \
     -DCMAKE_VERBOSE_MAKEFILE=ON \
     -DPXR_BUILD_USDVIEW=%{?with_usdview:ON}%{?!with_usdview:OFF} \
%if %{with documentation}
     -DPXR_BUILD_DOCUMENTATION=TRUE \
%endif
     -DPXR_BUILD_EXAMPLES=OFF \
     -DPXR_BUILD_TUTORIALS=OFF \
     -DPXR_BUILD_TESTS=%{?with_test:ON}%{!?with_test:OFF} \
%if %{with openvdb}
     -DPXR_ENABLE_OPENVDB_SUPPORT=ON \
%endif
     -DPXR_INSTALL_LOCATION="%{_libdir}/%{name}/plugin" \
%if %{with jemalloc}
     -DPXR_MALLOC_LIBRARY="%{_libdir}/libjemalloc.so" \
%endif
%if %{with alembic}
     -DOPENEXR_LOCATION=%{_includedir} \
     -DPXR_BUILD_ALEMBIC_PLUGIN=ON \
%endif
%if %{with embree}
     -DPXR_BUILD_EMBREE_PLUGIN=ON \
     -DEMBREE_LOCATION=%{_prefix} \
%endif
%if %{with ocio}
     -DPXR_BUILD_OPENCOLORIO_PLUGIN=ON \
%endif
%if %{with oiio}
     -DPXR_BUILD_OPENIMAGEIO_PLUGIN=ON \
%endif
%if %{with openshading}
     -DPXR_ENABLE_OSL_SUPPORT=ON \
%endif
     -DPYTHON_EXECUTABLE=%{python3} \
%if %{with python3}
     -DPXR_USE_PYTHON_3=ON \
     -DPYSIDE_AVAILABLE=ON \
     -DPYSIDEUICBINARY:PATH=${PWD}/uic-wrapper \
%else
     -DPXR_ENABLE_PYTHON_SUPPORT=OFF \
%endif
     -DPXR_BUILD_MONOLITHIC=ON \
     -DPXR_ENABLE_MALLOCHOOK_SUPPORT=OFF
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
rm -vrf '%{buildroot}%{_datadir}/%{name}/examples'

# Fix installation path for some files
mv %{buildroot}%{_prefix}/lib/python/pxr/*.* \
        %{buildroot}%{python3_sitearch}/pxr/
%if %{with usdview}
mv %{buildroot}%{_prefix}/lib/python/pxr/Usdviewq/* \
        %{buildroot}%{python3_sitearch}/pxr/Usdviewq/
%endif

# Currently, the pxrConfig.cmake that is installed is not correct for
# monolithic builds (and we must do a monolithic build in order to be usable as
# a dependency for Blender). It relies on the libraries that would be in
# pxrTargets.cmake, which is not generated for monolithic builds.
# https://bugzilla.redhat.com/show_bug.cgi?id=2055414
# https://github.com/PixarAnimationStudios/USD/issues/1088
rm -vrf '%{buildroot}%{_libdir}/cmake'

%check
%if %{with usdview}
desktop-file-validate %{buildroot}%{_datadir}/applications/org.open%{name}.%{name}view.desktop
%endif
%{?with_test:%ctest}

%files
%doc NOTICE.txt README.md
%{_bindir}/sdfdump
%{_bindir}/sdffilter
%{_bindir}/usdGenSchema
%{_bindir}/usdcat
%{_bindir}/usdchecker
%{_bindir}/usddiff
%{_bindir}/usddumpcrate
%{_bindir}/usdedit
%{_bindir}/usdgenschemafromsdr
%{_bindir}/usdrecord
%{_bindir}/usdresolve
%{_bindir}/usdstitch
%{_bindir}/usdstitchclips
%{_bindir}/usdtree
%{_bindir}/usdzip

%if %{with python3}
%files -n python3-%{name}
%{python3_sitearch}/pxr
%if %{with usdview}
%{_datadir}/applications/org.open%{name}.%{name}view.desktop
%{_bindir}/testusdview
%{_bindir}/usdview
%endif
%endif

%files libs
%license LICENSE.txt
%doc NOTICE.txt README.md
%{_libdir}/lib%{name}_%{name}_ms.so.%{downstream_so_version}
%{_libdir}/%{name}
%exclude %{_libdir}/%{name}/%{name}/resources/codegenTemplates

%files devel
%doc BUILDING.md CHANGELOG.md VERSIONS.md
%{_includedir}/pxr/
%{_libdir}/lib%{name}_%{name}_ms.so
%{_libdir}/%{name}/%{name}/resources/codegenTemplates/

%if %{with documentation}
%files doc
%license LICENSE.txt
%{_docdir}/%{name}
%endif

%changelog
%autochangelog
