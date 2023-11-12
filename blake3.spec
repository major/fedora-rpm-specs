# Use Clang to avoid https://gcc.gnu.org/bugzilla/show_bug.cgi?id=110027
%global toolchain clang

Name:           blake3
Version:        1.5.0
Release:        1%{?dist}
Summary:        Official C implementation of the BLAKE3 cryptographic hash function

License:        Apache-2.0
URL:            https://github.com/BLAKE3-team/BLAKE3/
Source0:        %{url}/archive/%{version}/%{name}-%{version}.tar.gz

# Tests fail on i686 due to missing `libclang_rt.asan{,_static}-i386.a`
%if 0%{?fedora} >= 39
ExcludeArch:    %{ix86}
%endif

BuildRequires:  cmake
BuildRequires:  clang
BuildRequires:  compiler-rt
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
cd c
%cmake
%cmake_build


%check
# These make-flag definitions are only used locally
%ifnarch x86_64
%define non_x86_64_flags BLAKE3_NO_SSE2=1 BLAKE3_NO_SSE41=1 BLAKE3_NO_AVX2=1 BLAKE3_NO_AVX512=1
%endif
%ifarch %{arm32} aarch64
%define arm_flags %{?flags} BLAKE3_USE_NEON=1
%endif

cd c
%make_build CC=clang %{?non_x86_64_flags} %{?arm_flags} -f Makefile.testing test

# There is no NEON assembly implementation
%make_build CC=clang %{?non_x86_64_flags} BLAKE3_NO_NEON=1 -f Makefile.testing test_asm


%install
cd c
%cmake_install


%files
%license LICENSE
%doc c/README.md
%{_libdir}/lib%{name}.so.0
%{_libdir}/lib%{name}.so.1.5.0

%files devel
%doc c/example.c
%{_includedir}/%{name}.h
%{_libdir}/lib%{name}.so
%{_libdir}/cmake/%{name}/
%{_libdir}/pkgconfig/lib%{name}.pc


%changelog
%autochangelog
