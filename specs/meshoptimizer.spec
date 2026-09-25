Name:           meshoptimizer
Version:        1.2
Release:        %autorelease
Summary:        Mesh optimization library

License:        MIT AND (MIT OR Unlicense)
URL:            https://meshoptimizer.org/
Source0:        https://github.com/zeux/%{name}/archive/v%{version}/%{name}-%{version}.tar.gz

BuildRequires:  cmake
BuildRequires:  gcc-c++

# Header-only libraries bundled in the upstream source archive
Provides:       bundled(cgltf-devel) = 1.15
Provides:       bundled(fast_obj-devel) = 1.3
Provides:       bundled(sdefl-devel)

%description
meshoptimizer is a library that provides algorithms for optimizing meshes for
rendering efficiency. It includes vertex-cache, overdraw, and vertex-fetch
optimization, mesh simplification, generation of small mesh clusters, and
vertex and index buffer codecs.


%package devel
Summary:        Development files for meshoptimizer
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description devel
This package contains the C++ header and CMake package files needed to build
software against meshoptimizer.


%prep
%autosetup


%build
%cmake \
    -DMESHOPT_BUILD_DEMO:BOOL=ON \
    -DMESHOPT_BUILD_GLTFPACK:BOOL=OFF \
    -DMESHOPT_BUILD_SHARED_LIBS:BOOL=ON \
    -DMESHOPT_INSTALL:BOOL=ON \
    -DMESHOPT_SOVERSION:STRING=1 \
    -DMESHOPT_WERROR:BOOL=OFF
%cmake_build


%install
%cmake_install


%check
# Upstream's fixed codec fixtures assume a little-endian in-memory layout.
# s390x is big-endian, so the demo suite reports false byte-comparison failures.
%ifnarch s390x
%{_vpath_builddir}/meshoptdemo
%endif


%files
%license LICENSE.md
%doc README.md
%{_libdir}/libmeshoptimizer.so.1
%{_libdir}/libmeshoptimizer.so.%{version}


%files devel
%{_includedir}/meshoptimizer.h
%{_libdir}/libmeshoptimizer.so
%{_libdir}/cmake/meshoptimizer/


%changelog
%autochangelog
