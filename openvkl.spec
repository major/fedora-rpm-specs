Name:		openvkl
Version:	2.0.1
Release:	%autorelease
Summary:	Intel Open Volume Kernel Library

# Most of the source code is Apache-2.0, with the following exceptions:
# vklTests uses those headers during the compilation
# testing/external/catch.hpp is BSL-1.0
# testing/external/half.hpp is MIT
License:	Apache-2.0 AND BSL-1.0 AND MIT
URL:		https://github.com/OpenVKL/openvkl
Source0:	%{url}/archive/v%{version}/%{name}-%{version}.tar.gz

BuildRequires:	boost-devel
BuildRequires:	blosc-devel
BuildRequires:	cmake >= 3.1
BuildRequires:	embree-devel >= 4.0.0
BuildRequires:	gcc-c++
BuildRequires:	glfw-devel
BuildRequires:	imath-devel
BuildRequires:	ispc-static >= 1.19.0
BuildRequires:	openvdb-devel >= 7.0.0
BuildRequires:	rkcommon-devel >= 1.11.0

# Upstream only supports x86_64 and ARM64 architectures
ExclusiveArch:	aarch64 x86_64

%description
Intel Open Volume Kernel Library (Open VKL) is a collection of high-performance
volume computation kernels, developed at Intel. The target users of Open VKL 
are graphics application engineers who want to improve the performance of their
volume rendering applications by leveraging Open VKL’s performance-optimized 
kernels, which include volume traversal and sampling functionality for a 
variety of volumetric data formats.

Open VKL contains kernels optimized for the latest x86 processors with support
for SSE, AVX, AVX2, and AVX-512 instructions, and for ARM processors with 
support for NEON instructions. Open VKL supports Intel GPUs based on the Xe HPG
microarchitecture and Xe HPC microarchitecture under Linux.

%package devel
Summary:	Development files for %{name}
License:	Apache-2.0
Requires:	%{name}%{?_isa} = %{version}-%{release}
Requires:	openvdb-devel >= 7.0.0
Requires:	rkcommon-devel >= 1.11.0

%description devel
The %{name}-devel package contains libraries and header files for
applications that use %{name}.

%prep
%autosetup -p1

# do not install LICENSE.txt
sed -i '/LICENSE.txt/d' openvkl/CMakeLists.txt
sed -i '/third-party-programs/d' openvkl/CMakeLists.txt
# lib64 path fix 
sed -i 's/lib\/cmake/%{_lib}\/cmake/g' utility/vdb/CMakeLists.txt
# bypass vdb_volume_dense test for now
sed -i '/vdb_volume_dense.cpp/d' testing/apps/CMakeLists.txt

%build
%cmake \
	-DBUILD_EXAMPLES=OFF \
	-DBUILD_OPENVKL_TESTING=ON \
	-DBUILD_BENCHMARKS=OFF \
	-DOpenVDB_ROOT=%{_prefix}
%cmake_build

%install
%cmake_install

%check
%ctest

%files
%license LICENSE.txt third-party-programs*.txt
%doc CHANGELOG.md README.md SECURITY.md
%{_bindir}/vklTestsCPU
%{_libdir}/lib%{name}.so.2
%{_libdir}/lib%{name}.so.%{version}
%{_libdir}/lib%{name}_module_cpu_device.so.2
%{_libdir}/lib%{name}_module_cpu_device.so.%{version}
%{_libdir}/lib%{name}_module_cpu_device_{4,8,16}.so.2
%{_libdir}/lib%{name}_module_cpu_device_{4,8,16}.so.%{version}

%files devel
%{_includedir}/%{name}
%{_libdir}/lib%{name}.so
%{_libdir}/lib%{name}_module_cpu_device.so
%{_libdir}/lib%{name}_module_cpu_device_{4,8,16}.so
%{_libdir}/cmake/%{name}-%{version}/

%changelog
%autochangelog
