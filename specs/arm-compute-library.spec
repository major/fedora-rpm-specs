%global majorver 42
%global releasever 42.0.0
%global desc %{expand: \
The Compute Library is a collection of low-level machine learning functions
optimized for Arm Cortex-A, Arm Neoverse and Arm Mali GPUs architectures.

The library provides superior performance to other open source alternatives
and immediate support for new Arm technologies e.g. SVE2.}

Name:		arm-compute-library
Version:	24.09
Release:	%autorelease
Summary:	ARM compute library

License:	MIT AND Apache-2.0
URL:		https://github.com/arm-software/ComputeLibrary
Source0:	%{url}/archive/v%{version}/%{name}-%{version}.tar.gz
Source1:	arm_compute.pc.in
Source2:	arm_compute_graph.pc.in

Patch0:		mathjax-doc.patch
Patch1:		disable-doxygen-timestamp.patch

BuildRequires:	doxygen
BuildRequires:	gcc-c++
BuildRequires:	python3-scons
BuildRequires:	libglvnd-devel

# arm-compute-library is not available on these architectures
# https://github.com/ARM-software/ComputeLibrary?tab=readme-ov-file#supported-architecturestechnologies
ExcludeArch:	i686 ppc64le s390x

%description
%{desc}
	
%package devel
Summary:	Development files for %{name}
Requires:	%{name}%{?_isa} = %{version}-%{release}
Provides:	bundle(opencl-headers) = 3.0
Provides:	bundle(stb_image-devel) = 2.19
Provides:	bundle(half-devel) = 1.12.0
Provides:	bundle(libnpy) = 0.1.0

%description devel
%{desc}

%package doc
Summary:	Documentations and examples for %{name}
Requires:	%{name}-devel%{?_isa} = %{version}-%{release}
Requires:	mathjax

%description doc
Contains documentations and examples for %{name}.

%prep
%autosetup -p1 -n ComputeLibrary-%{version} 

# remove .bazel files
find . -name *.bazel -exec rm -f '{}' \;

# gcc 15 include cstdint
sed -i '/#include <memory>.*/a#include <cstdint>' arm_compute/core/CPP/CPPTypes.h
sed -i '/#include <cstddef>.*/a#include <cstdint>' arm_compute/runtime/MemoryRegion.h
sed -i '1i #include <cstdint>' tests/framework/instruments/hwc_names.hpp

%build
scons %{?_smp_mflags} os=linux \
	build=native \
	install_dir=install \
	set_soname=1 \
	opencl=1 \
	asserts=1 \
	embed_kernels=1 \
	benchmark_tests=0 \
	validation_tests=1 \
	examples=0 \
%ifarch aarch64
	neon=1 arch=arm64-v8a \
%else
	neon=0 arch=x86_64 \
%endif
	Werror=0 extra_cxx_flags="%{optflags}" extra_link_flags="%{build_ldflags}"

# Build documentation
doxygen docs/Doxyfile

# pkgconfig files
cat %{SOURCE1} | sed -e "s,%%prefix%%,%{_prefix},g" \
	-e "s,%%exec_prefix%%,%{_prefix},g" \
	-e "s,%%libdir%%,%{_libdir},g" \
	-e "s,%%includedir%%,%{_includedir},g" \
	-e "s,%%VERSION%%,%{version},g" \
	> build/install/arm_compute.pc
cat %{SOURCE2} | sed -e "s,%%prefix%%,%{_prefix},g" \
	-e "s,%%exec_prefix%%,%{_prefix},g" \
	-e "s,%%libdir%%,%{_libdir},g" \
	-e "s,%%includedir%%,%{_includedir},g" \
	-e "s,%%VERSION%%,%{version},g" \
	> build/install/arm_compute_graph.pc

%install
mkdir -p %{buildroot}%{_includedir}/ArmCompute
cp -a build/install/include/* %{buildroot}%{_includedir}/ArmCompute/
mkdir -p %{buildroot}%{_libdir}
rm -f build/*.a
cp -a build/libarm_compute* %{buildroot}%{_libdir}
mkdir -p %{buildroot}%{_libdir}/pkgconfig
install -m 0644 build/install/arm_compute.pc %{buildroot}%{_libdir}/pkgconfig
install -m 0644 build/install/arm_compute_graph.pc %{buildroot}%{_libdir}/pkgconfig
mkdir -p %{buildroot}%{_docdir}/%{name}
cp -a build/docs/html %{buildroot}%{_docdir}/%{name} 

%check
# CL_DEVICE_VERSION = Unavailable
# ERROR: in generate_build_options src/core/CL/CLCompileContext.cpp:284: Non uniform workgroup size is not supported!!
# by-passing the CL tests
LD_LIBRARY_PATH=%{buildroot}%{_libdir}:$LD_LIBRARY_PATH ./build/tests/arm_compute_validation --filter='^(?!CL).*'

%files
%license LICENSE include/half/LICENSE.txt
%doc README.md
%{_libdir}/libarm_compute.so.%{releasever}
%{_libdir}/libarm_compute.so.%{majorver}
%{_libdir}/libarm_compute_graph.so.%{releasever}
%{_libdir}/libarm_compute_graph.so.%{majorver}

%files devel
%doc CONTRIBUTING.md
%{_includedir}/ArmCompute/*
%{_libdir}/libarm_compute.so
%{_libdir}/libarm_compute_graph.so
%{_libdir}/pkgconfig/arm_compute.pc
%{_libdir}/pkgconfig/arm_compute_graph.pc

%files doc
%{_docdir}/%{name}

%changelog
%autochangelog
