%global upstream_name level-zero-raytracing-support

Name: intel-level-zero-gpu-raytracing
Version: 1.1.0
Release: %autorelease
Summary: oneAPI Level Zero Ray Tracing Support library

License: Apache-2.0
URL: https://github.com/intel/level-zero-raytracing-support
Source0: %{url}/archive/v%{version}.tar.gz

BuildRequires: cmake
BuildRequires: gcc gcc-c++
BuildRequires: git
BuildRequires: ninja-build
BuildRequires: pkg-config
BuildRequires: tbb-devel

Requires: tbb
Requires: oneapi-level-zero

# Upstream only supports x86_64
ExclusiveArch:  x86_64

%description
The oneAPI Level Zero Ray Tracing Support library implements high performance
CPU based construction algorithms for 3D acceleration structures that are
compatible with the ray tracing hardware of Intel GPUs.

This library is used by Intel oneAPI Level Zero to implement part of the
RTAS builder extension.

This library should not get used directly but only through Level Zero.

%prep
%autosetup -n %{upstream_name}-%{version}

%build
%cmake \
   -DCMAKE_BUILD_TYPE=Release \
   -DCMAKE_INSTALL_PREFIX=/usr \
   -DZE_RAYTRACING_TBB_STATIC=OFF
%cmake_build

%install
%cmake_install

%files
%license LICENSE.txt
%{_libdir}/libze_intel_gpu_raytracing.so


%doc

%changelog
%autochangelog
