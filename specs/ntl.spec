Name:           ntl
Version:        11.6.0
Release:        %autorelease
Summary:        High-performance algorithms for vectors, matrices, and polynomials

# LGPL-2.1-or-later: the project as a whole
# BSD-2-Clause: src/FFT.cpp
License:        LGPL-2.1-or-later AND BSD-2-Clause
URL:            https://libntl.org/
VCS:            git:https://github.com/libntl/ntl.git

Source:         https://libntl.org/%{name}-%{version}.tar.gz
# Detect CPU at load time, optionally use PCLMUL, AVX, FMA, and AVX2 features.
# This patch was sent upstream, but upstream prefers that the entire library
# be built for a specific CPU, which we cannot do in Fedora.
Patch:          %{name}-loadtime-cpu.patch

# See https://fedoraproject.org/wiki/Changes/EncourageI686LeafRemoval
ExcludeArch:    %{ix86}

BuildRequires:  gcc-c++
BuildRequires:  gf2x-devel
BuildRequires:  gmp-devel
BuildRequires:  libtool
BuildRequires:  make
BuildRequires:  perl-interpreter

%description
NTL is a high-performance, portable C++ library providing data structures and
algorithms for arbitrary length integers; for vectors, matrices, and
polynomials over the integers and over finite fields; and for arbitrary
precision floating point arithmetic.

NTL provides high quality implementations of state-of-the-art algorithms for:
* arbitrary length integer arithmetic and arbitrary precision floating point
  arithmetic;
* polynomial arithmetic over the integers and finite fields including basic
  arithmetic, polynomial factorization, irreducibility testing, computation
  of minimal polynomials, traces, norms, and more;
* lattice basis reduction, including very robust and fast implementations of
  Schnorr-Euchner, block Korkin-Zolotarev reduction, and the new
  Schnorr-Horner pruning heuristic for block Korkin-Zolotarev;
* basic linear algebra over the integers, finite fields, and arbitrary
  precision floating point numbers.

%package devel 
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description devel 
%{summary}.

%prep
%autosetup -p1

# Remove an unused file with an unacceptable license (CC-BY-3.0)
rm src/GetTime0.cpp

%build
# TODO: Once we can assume z15, add TUNE=linux-s390x to the flags for s390x
cd src
./configure \
  CXX="${CXX-g++}" \
  CXXFLAGS='%{build_cxxflags} -fPIC' \
  LDFLAGS='%{build_ldflags}' \
  DOCDIR=%{_docdir} \
  ENABLE_RPATH=off \
  LIBDIR=%{_libdir} \
  NATIVE=off \
  NTL_GF2X_LIB=on \
  NTL_STD_CXX14=on \
%ifarch %{x86_64}
  NTL_LOADTIME_CPU=on \
  TUNE=x86 \
%else
  TUNE=generic \
%endif
  PKGDIR=%{_libdir}/pkgconfig \
  SHARED=on \
  SYS_PREFIX=%{_prefix}
cd -

# not smp-safe
make -C src V=1

%install
make -C src install \
  DESTDIR=%{buildroot} \
  PREFIX=%{_prefix} \
  DOCDIR=%{_docdir} \
  INCLUDEDIR=%{_includedir} \
  LIBDIR=%{_libdir} 

# Unpackaged files
rm -rfv %{buildroot}%{_docdir}/NTL
rm -fv  %{buildroot}%{_libdir}/libntl.a

%check
make -C src check

%files
%doc README
%license doc/copying.txt
%{_libdir}/libntl.so.45{,.*}

%files devel 
%doc doc/*
%{_includedir}/NTL/
%{_libdir}/libntl.so
%{_libdir}/pkgconfig/ntl.pc

%changelog
%autochangelog
