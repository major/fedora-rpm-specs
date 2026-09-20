%bcond_without opencl

%global blend_version 2.11.0

Name:           luxcorerender
Version:        2.11.2
Release:        %autorelease
Summary:        Physically based unbiased rendering system

License:        Apache-2.0
URL:            https://luxcorerender.org/
Source0:        https://github.com/LuxCoreRender/LuxCore/archive/wheels-v%{version}/LuxCore-%{version}.tar.gz
# BlendLuxCore has an independent release cadence.
Source1:        https://github.com/LuxCoreRender/BlendLuxCore/archive/v%{blend_version}/BlendLuxCore-%{blend_version}.tar.gz
Source3:        org.%{name}.blendluxcore.metainfo.xml

ExclusiveArch:  x86_64

BuildRequires:  cmake >= 3.29
BuildRequires:  gcc-c++
BuildRequires:  appstream
BuildRequires:  blender-rpm-macros
BuildRequires:  bison
BuildRequires:  flex
BuildRequires:  python3-devel

BuildRequires:  boost-devel
BuildRequires:  boost-iostreams
BuildRequires:  boost-serialization
BuildRequires:  cmake(Blosc2)
BuildRequires:  cmake(Eigen3)
BuildRequires:  cmake(Imath)
BuildRequires:  cmake(OpenColorIO)
BuildRequires:  cmake(OpenEXR)
BuildRequires:  cmake(OpenImageIO)
BuildRequires:  cmake(OpenImageDenoise)
BuildRequires:  cmake(OpenJPEG)
BuildRequires:  cmake(nlohmann_json)
BuildRequires:  cmake(OpenSubdiv)
BuildRequires:  cmake(pybind11)
BuildRequires:  cmake(spdlog)
BuildRequires:  cmake(TBB)
BuildRequires:  cmake(tsl-robin-map)
BuildRequires:  cmake(zlib-ng)
BuildRequires:  embree-devel
BuildRequires:  openvdb-devel
BuildRequires:  pkgconfig(bzip2)
BuildRequires:  pkgconfig(liblzma)
BuildRequires:  pkgconfig(libzstd)
BuildRequires:  pkgconfig(minizip)
BuildRequires:  pkgconfig(libpng)
BuildRequires:  pkgconfig(openjph)
BuildRequires:  pkgconfig(openssl)
BuildRequires:  pkgconfig(zlib)

# Optional OpenCL
%if %{with opencl}
BuildRequires:  pkgconfig(OpenCL)
%global opencl_flags -DLUXRAYS_ENABLE_OPENCL=ON -DLUXRAYS_DISABLE_OPENCL=OFF
%else
%global opencl_flags -DLUXRAYS_ENABLE_OPENCL=OFF -DLUXRAYS_DISABLE_OPENCL=ON
%endif

# CUDA disabled (not in Fedora)
%global cuda_flags -DLUXRAYS_ENABLE_CUDA=OFF -DLUXRAYS_ENABLE_OPTIX=OFF -DLUXRAYS_DISABLE_CUDA=ON

Obsoletes:      LuxRender < 2.0
Provides:       LuxRender = %{version}-%{release}
Obsoletes:      LuxRender-core < 2.0
Provides:       LuxRender-core = %{version}-%{release}
Obsoletes:      %{name}-core < %{version}-%{release}
Provides:       %{name}-core = %{version}-%{release}

%description
LuxCoreRender implements state-of-the-art light transport algorithms for
photorealistic rendering. Features hybrid CPU/GPU acceleration,
spectral rendering, and advanced material modeling.

%package -n blender-%{name}
Summary:        Blender 4.2+ integration extension
License:        GPL-3.0-or-later
BuildArch:      noarch
Requires:       %{name} = %{version}-%{release}
Obsoletes:      %{name}-blender < %{blend_version}
Provides:       %{name}-blender = %{blend_version}-%{release}

%description -n blender-%{name}
Blender extension for exporting scenes and materials to LuxCore Renderer.
Supports Cycles material conversion and interactive rendering.

The extension uses the system-provided LuxCore Python bindings.

%package devel
Summary:        Development headers and libraries
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description devel
Header files and build configuration for developing LuxCore-based applications.

%prep
%autosetup -p1 -a1 -n LuxCore-wheels-v%{version}

# Fedora provides the Python bindings as part of the main package.  Do not let
# the Blender extension download and install a second copy from PyPI at runtime.
sed -i 's/luxloader\.ensure_pyluxcore()/# Use the system-provided Python bindings./' \
    BlendLuxCore-%{blend_version}/__init__.py

# Fix detection for Blosc2 and OIDN (upstream naming mismatches)
sed -i 's/c-blosc/Blosc2/g' CMakeLists.txt
sed -i 's/oidn/OpenImageDenoise/g' CMakeLists.txt
sed -i 's/find_package(robin_hood REQUIRED)/find_package(tsl-robin-map REQUIRED)/' \
    CMakeLists.txt
sed -i 's/find_package(Boost REQUIRED)/find_package(Boost REQUIRED COMPONENTS iostreams serialization)/' \
    CMakeLists.txt

# Map Fedora's system-library targets to the Conan-style names used upstream.
sed -i '/find_package(embree REQUIRED)/c\
find_path(EMBREE_INCLUDE_DIR embree4/rtcore.h REQUIRED)\
find_library(EMBREE_LIBRARY NAMES embree4 REQUIRED)\
add_library(embree::embree SHARED IMPORTED)\
set_target_properties(embree::embree PROPERTIES IMPORTED_LOCATION "${EMBREE_LIBRARY}" INTERFACE_INCLUDE_DIRECTORIES "${EMBREE_INCLUDE_DIR}")' \
    CMakeLists.txt
sed -i '/find_package(tsl-robin-map REQUIRED)/a\
add_library(onetbb::onetbb INTERFACE IMPORTED)\
set_target_properties(onetbb::onetbb PROPERTIES INTERFACE_LINK_LIBRARIES "TBB::tbb;TBB::tbbmalloc")\
add_library(robin_hood::robin_hood INTERFACE IMPORTED)\
set_target_properties(robin_hood::robin_hood PROPERTIES INTERFACE_LINK_LIBRARIES tsl::robin_map)\
add_library(openexr::openexr INTERFACE IMPORTED)\
set_target_properties(openexr::openexr PROPERTIES INTERFACE_LINK_LIBRARIES OpenEXR::OpenEXR)\
add_library(opensubdiv::opensubdiv INTERFACE IMPORTED)\
set_target_properties(opensubdiv::opensubdiv PROPERTIES INTERFACE_LINK_LIBRARIES OpenSubdiv::osdCPU)\
add_library(openimageio::openimageio INTERFACE IMPORTED)\
set_target_properties(openimageio::openimageio PROPERTIES INTERFACE_LINK_LIBRARIES "OpenImageIO::OpenImageIO;OpenImageIO::OpenImageIO_Util")\
find_path(OIDN_INCLUDE_DIR OpenImageDenoise/oidn.hpp REQUIRED)\
find_library(OIDN_LIBRARY NAMES OpenImageDenoise REQUIRED)\
add_library(oidn::oidn SHARED IMPORTED)\
set_target_properties(oidn::oidn PROPERTIES IMPORTED_LOCATION "${OIDN_LIBRARY}" INTERFACE_INCLUDE_DIRECTORIES "${OIDN_INCLUDE_DIR}")\
find_path(OPENJPH_INCLUDE_DIR openjph/ojph_codestream.h REQUIRED)\
find_library(OPENJPH_LIBRARY NAMES openjph REQUIRED)\
add_library(openjph::openjph SHARED IMPORTED)\
set_target_properties(openjph::openjph PROPERTIES IMPORTED_LOCATION "${OPENJPH_LIBRARY}" INTERFACE_INCLUDE_DIRECTORIES "${OPENJPH_INCLUDE_DIR}")' \
    CMakeLists.txt

# Upstream's Conan target hides compiled Boost dependencies behind an
# interface-only compatibility target.  Link Fedora's imported Iostreams and
# Serialization targets directly so they survive static-library composition.
find . -name CMakeLists.txt -exec \
    sed -i 's/boost::boost/Boost::iostreams Boost::serialization/g' {} +

# luxcore_static uses the scalable allocator, but its private link dependencies
# do not propagate to the console executable.  Keep tbbmalloc after the static
# archive on the final link line so Fedora's --as-needed does not discard it.
sed -i 's/Boost::serialization)/Boost::serialization TBB::tbbmalloc)/' \
    samples/luxcoreconsole/CMakeLists.txt

# Adapt the robin_hood-specific API to Fedora's tsl-robin-map implementation.
sed -i \
    -e 's|<robin_hood.h>|<tsl/robin_map.h>|' \
    -e 's/robin_hood::unordered_flat_map/tsl::robin_map/g' \
    include/slg/lights/lightsourcedefs.h
sed -i \
    -e 's/robin_hood::unordered_flat_map/tsl::robin_map/g' \
    -e 's/e->second/e.value()/g' \
    src/slg/lights/lightsourcedefs.cpp
sed -i \
    -e '/#include <cstdlib>/i#include <functional>' \
    -e 's/robin_hood::hash_bytes(prefix.data(), sizeof(char) \* prefix.size())/std::hash<std::string>{}(prefix)/' \
    src/slg/scene/scene.cpp

# Fedora's OIDN uses the standard oidn namespace.  The lux::oidn namespace is
# specific to upstream's private OIDN build configured with OIDN_API_NAMESPACE.
sed -i 's/lux::oidn::/oidn::/g' \
    src/slg/film/imagepipeline/plugins/intel_oidn.cpp

# fmt 12 removed basic_memory_buffer::c_str(); convert the formatted buffer to
# a string before passing it to LuxCore's C-style logging callback.
sed -i 's/formatted\.c_str()/fmt::to_string(formatted).c_str()/' \
    include/luxcore/luxcoresink.h

# fmt 12 no longer formats arbitrary enums implicitly.
sed -i 's/API_RETURN("{}", type);/API_RETURN("{}", static_cast<int>(type));/' \
    src/luxcore/luxcoreimpl.cpp

# Fedora's OpenVDB package does not consistently export a discoverable CMake
# target across releases.  Define the target from the system headers/library.
sed -i '/find_package(OpenVDB REQUIRED)/c\
find_path(OPENVDB_INCLUDE_DIR openvdb/openvdb.h REQUIRED)\
find_library(OPENVDB_LIBRARY NAMES openvdb REQUIRED)\
add_library(OpenVDB::openvdb SHARED IMPORTED)\
set_target_properties(OpenVDB::openvdb PROPERTIES IMPORTED_LOCATION "${OPENVDB_LIBRARY}" INTERFACE_INCLUDE_DIRECTORIES "${OPENVDB_INCLUDE_DIR}")' \
    CMakeLists.txt

# CUDA/OptiX and the standalone ImGui frontend are disabled.  Avoid probing
# their unavailable SDKs and omit the frontend target.
sed -i \
    -e '/find_package(nvrtc REQUIRED)/d' \
    -e '/find_package(imgui)/d' \
    -e '/find_package(glfw3)/d' \
    -e '/find_package(imguifiledialog)/d' \
    -e '/add_subdirectory(samples\/luxcoreui)/d' \
    CMakeLists.txt

# With system OIDN and CUDA disabled, these upstream bundle paths are empty.
# Guard their install rules so CMake is not passed an empty PROGRAMS argument.
sed -i \
    -e '179s/^if(LINUX)$/if(LINUX AND LUX_OIDN_DEVICE_CPU)/' \
    -e '217s/^if(LINUX)$/if(LINUX AND LUX_NVRTC)/' \
    src/luxcore/CMakeLists.txt
sed -i '107s/^if(LINUX)$/if(LINUX AND LUX_OIDN_DEVICE_CPU)/' \
    src/pyluxcore/CMakeLists.txt
sed -i '117s/^endif(LINUX)$/endif()/' src/pyluxcore/CMakeLists.txt

# Never copy system runtime dependencies into the package buildroot.  Fedora's
# dependency generator records the required shared libraries from their owning
# packages; bundling CMake's resolved dependency set would duplicate them.
sed -i \
    '/^[[:space:]]*RUNTIME_DEPENDENCIES$/,/^[[:space:]]*DIRECTORIES .*CONAN_RUNTIME_LIB_DIRS/d' \
    src/luxcore/CMakeLists.txt
sed -i '/^install(RUNTIME_DEPENDENCY_SET LUXCONSOLE_DEPS$/,/^)/d' \
    samples/luxcoreconsole/CMakeLists.txt
sed -i '/^[[:space:]]*RUNTIME_DEPENDENCY_SET LUXCONSOLE_DEPS$/d' \
    samples/luxcoreconsole/CMakeLists.txt

# Give the public library a proper ABI-versioned SONAME.
sed -i '/set_target_properties(luxcore PROPERTIES WINDOWS_EXPORT_ALL_SYMBOLS ON)/a\
set_target_properties(luxcore PROPERTIES VERSION %{version} SOVERSION 2)' \
    src/luxcore/CMakeLists.txt

# Install the Python extension in Fedora's architecture-specific site directory.
sed -i 's|DESTINATION pyluxcore|DESTINATION %{python3_sitearch}|' \
    src/pyluxcore/CMakeLists.txt

%build
# Build the main LuxCore library
%cmake \
    -DCMAKE_SKIP_INSTALL_RPATH=ON \
    -DLUXCORE_VERSION=%{version} \
    -DLUXCOREDEPS_VERSION=2.2.3 \
    %{opencl_flags} \
    %{cuda_flags}
%cmake_build

# Build the BlendLuxCore Blender extension
pushd BlendLuxCore-%{blend_version}
%{_bindir}/blender --command extension build --source-dir . \
    --output-filepath ./BlendLuxCore.zip
popd

%install
# Install the main LuxCore libraries
%cmake_install

# Upstream does not install its public C++ headers yet.
install -d %{buildroot}%{_includedir}
cp -a include/{luxcore,luxrays,slg} %{buildroot}%{_includedir}/
install -Dpm 0644 %{__cmake_builddir}/generated/include/luxcore/cfg.h \
    %{buildroot}%{_includedir}/luxcore/cfg.h
install -Dpm 0644 %{__cmake_builddir}/generated/include/luxrays/cfg.h \
    %{buildroot}%{_includedir}/luxrays/cfg.h

# Install the Blender extension system-wide
mkdir -p %{buildroot}%{blender_extensions}
install -Dpm 0644 BlendLuxCore-%{blend_version}/BlendLuxCore.zip \
    %{buildroot}%{blender_extensions}/BlendLuxCore.zip

# Install the AppStream metadata
install -Dpm 644 %{SOURCE3} %{buildroot}%{_metainfodir}/org.%{name}.blendluxcore.metainfo.xml

%check
appstreamcli validate --no-net %{buildroot}%{_metainfodir}/*.xml

%files
%license COPYING.txt
%doc README.md AUTHORS.txt
%{_bindir}/luxcore*
%{_libdir}/liblux*.so.*
%{python3_sitearch}/pyluxcore*.so

%files -n blender-%{name}
%license BlendLuxCore-%{blend_version}/LICENSE
%doc BlendLuxCore-%{blend_version}/{AUTHORS.txt,readme.md}
%{_metainfodir}/org.%{name}.*.xml
%{blender_extensions}/BlendLuxCore.zip

%files devel
%doc README.md
%{_includedir}/{luxcore,luxrays,slg}
%{_libdir}/libluxcore.so

%changelog
%autochangelog
