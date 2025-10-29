%global upstream_name level-zero-raytracing-support
%global tbb_version 2021.6.0

Name: intel-level-zero-gpu-raytracing
Version: 1.2.0
Release: %autorelease
Summary: oneAPI Level Zero Ray Tracing Support library

License: Apache-2.0
URL: https://github.com/intel/level-zero-raytracing-support
Source0: %{url}/archive/v%{version}.tar.gz
Source1: https://github.com/uxlfoundation/oneTBB/archive/v%{tbb_version}.tar.gz

BuildRequires: cmake
BuildRequires: gcc gcc-c++
BuildRequires: git
BuildRequires: ninja-build
BuildRequires: pkg-config

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

# Needs a specific name for static linking
tar xf %{SOURCE1}
mv oneTBB-%{tbb_version} tbb

%build
%cmake \
   -DCMAKE_BUILD_TYPE=Release \
   -DCMAKE_INSTALL_PREFIX=/usr
%cmake_build

%install
%cmake_install

%files
%license LICENSE.txt third-party-programs-TBB.txt
%{_libdir}/libze_intel_gpu_raytracing.so


%doc

%changelog
%autochangelog
