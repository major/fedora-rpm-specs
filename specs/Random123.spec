%global debug_package %{nil}

Name:       Random123
Version:    1.14.0
Release:    %autorelease
Summary:    Library of random number generators

License:    BSD-3-Clause
URL:        https://github.com/DEShawResearch/random123/
Source0:    %{url}/archive/v%{version}/%{name}-%{version}.tar.gz
Patch:      0001-add-missing-headers.patch
# https://github.com/DEShawResearch/random123/pull/12
Patch:      enable-riscv.patch

# gccfeatures.h mentions what arches are supported
# these aren't on the list
ExcludeArch:    mips64r2 mips32r2 s390

BuildRequires:  make
BuildRequires:  doxygen
# For tests
BuildRequires:  gcc gcc-c++
BuildRequires:  patch

%description
Random123 is a library of "counter-based" random number generators (CBRNGs), in
which the Nth random number can be obtained by applying a stateless mixing
function to N instead of the conventional approach of using N iterations of a
stateful transformation. CBRNGs were originally developed for use in MD
applications on Anton, but they are ideal for a wide range of applications on
modern multi-core CPUs, GPUs, clusters, and special-purpose hardware. Three
families of non-cryptographic CBRNGs are described in a paper presented at the
SC11 conference: ARS (based on the Advanced Encryption System (AES)), Threefry
(based on the Threefish encryption function), and Philox (based on integer
multiplication). They all satisfy rigorous statistical testing (passing
BigCrush in TestU01), vectorize and parallelize well (each generator can
produce at least 264 independent streams), have long periods (the period of
each stream is at least 2128), require little or no memory or state, and have
excellent performance (a few clock cycles per byte of random output). The
Random123 library can be used with CPU (C and C++) and GPU (CUDA and OpenCL)
applications.

%package devel
Summary:   Development files for %{name}
Provides:  %{name} = %{version}-%{release}

%description devel
Development files for %{name}.

%package doc
Summary:    Documentation for %{name}

%description doc
Documentation for %{name}.

%prep
%autosetup -n random123-%{version} -S patch -p1


%build
# Header only library
pushd docs
    doxygen Doxyfile
popd

%install
mkdir -p -m 0755 $RPM_BUILD_ROOT/%{_includedir}/%{name}/
cp -a include/Random123/*  $RPM_BUILD_ROOT/%{_includedir}/%{name}/

%check
pushd tests
    cp GNUmakefile Makefile
    %set_build_flags
    make
popd

%files devel
%license LICENSE
%{_includedir}/%{name}/

%files doc
%doc examples

%changelog
%autochangelog
