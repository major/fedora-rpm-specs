# EL8 and EL9 require `gcc-toolset-13` as build dependency.
# * On EL8, Binutils 2.30 do not support the `vmovdqu` AVX-512 instruction.
# * On EL8 and EL9, GCC 8.5.0/11.4.1 generates ultra-slow test code for aarch64.
# * When building with `gcc-toolset-12`, the `gcc-annobin` plugin is not found.
%global needs_gcc_toolset 0%{?el8} || 0%{?el9}

%if 0%{?fedora} >= 40 || 0%{?rhel} >= 10
%bcond_without tbb
%else
%bcond_with tbb
%endif

Name:           blake3
Version:        1.8.1
Release:        %autorelease
Summary:        Official C implementation of the BLAKE3 cryptographic hash function

License:        Apache-2.0
URL:            https://github.com/BLAKE3-team/BLAKE3/
Source0:        %{url}/archive/%{version}/%{name}-%{version}.tar.gz

BuildRequires:  cmake
%if %{needs_gcc_toolset}
BuildRequires:  gcc-toolset-13
BuildRequires:  gcc-toolset-13-libasan-devel
BuildRequires:  gcc-toolset-13-libubsan-devel
%else
BuildRequires:  gcc
BuildRequires:  libasan
BuildRequires:  libubsan
%endif
%if %{with tbb}
BuildRequires:  gcc-c++
BuildRequires:  tbb-devel >= 2021.11
%endif
BuildRequires:  python3

%description
BLAKE3 is a cryptographic hash function that is:
- Much faster than MD5, SHA-1, SHA-2, SHA-3, and BLAKE2.
- Secure, unlike MD5 and SHA-1. And secure against length extension, unlike
  SHA-2.
- Highly parallelizable across any number of threads and SIMD lanes, because
  it's a Merkle tree on the inside.
- Capable of verified streaming and incremental updates, again because it's a
  Merkle tree.
- A PRF, MAC, KDF, and XOF, as well as a regular hash.
- One algorithm with no variants, which is fast on x86-64 and also on smaller
  architectures.


%package devel
Summary: %{summary} - development files
Requires: %{name}%{?_isa} = %{version}-%{release}

%description devel
Development files for the %{name} library.


%prep
%autosetup -p1 -n BLAKE3-%{version}


%build
%if %{needs_gcc_toolset}
. /opt/rh/gcc-toolset-13/enable
%endif
cd c
%cmake \
%if 0%{with tbb}
  -DBLAKE3_USE_TBB=ON
%endif
%cmake_build


%check
# These make-flag definitions are only used locally
%ifnarch x86_64
%define non_x86_64_flags BLAKE3_NO_SSE2=1 BLAKE3_NO_SSE41=1 BLAKE3_NO_AVX2=1 BLAKE3_NO_AVX512=1
%else
%if %{needs_gcc_toolset}
# Do not run the AVX-512 test because it segfaults when instrumented with ASAN
# (https://gcc.gnu.org/bugzilla/show_bug.cgi?id=110027 - fixed upstream, but
# `gcc-toolset-13` does not include the fix)
%define non_x86_64_flags BLAKE3_NO_AVX512=1
%endif
%endif
%ifarch %{arm32} aarch64
%define arm_flags %{?flags} BLAKE3_USE_NEON=1
%endif

%if %{needs_gcc_toolset}
. /opt/rh/gcc-toolset-13/enable
%endif
cd c
%make_build %{?non_x86_64_flags} %{?arm_flags} -f Makefile.testing test

# There is no NEON assembly implementation
%make_build %{?non_x86_64_flags} BLAKE3_NO_NEON=1 -f Makefile.testing test_asm


%install
cd c
%cmake_install


%files
%license LICENSE_A2
%{_libdir}/lib%{name}.so.0
%{_libdir}/lib%{name}.so.%{version}

%files devel
%doc c/example.c
%doc c/README.md
%{_includedir}/%{name}.h
%{_libdir}/lib%{name}.so
%{_libdir}/cmake/%{name}/
%{_libdir}/pkgconfig/lib%{name}.pc


%changelog
%autochangelog
