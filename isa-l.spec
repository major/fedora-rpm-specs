Name:		isa-l
Version:	2.30.0
Release:	1%{?dist}
Summary:	Intel(R) Intelligent Storage Acceleration Library

License:	BSD-3-Clause
URL:		https://github.com/intel/isa-l
Source0:	%{url}/archive/v%{version}/isa-l-%{version}.tar.gz

# Patches from upstream:
# https://github.com/intel/isa-l/commit/d3cfb2fb772e375cf2007e484e0a6ec0c6a7c993
Patch0:		s390x-compat.patch
# https://github.com/intel/isa-l/commit/bee5180a1517f8b5e70b02fcd66790c623536c5d
Patch1:		aarch64-relocation.patch

ExcludeArch:	%{ix86}

BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libtool
BuildRequires:	make
BuildRequires:	gcc
%if %{?rhel}%{!?rhel:0} == 7
BuildRequires:	yasm
%else
BuildRequires:	nasm
%endif

%description
Collection of low-level functions used in storage applications.
Contains fast erasure codes that implement a general Reed-Solomon type
encoding for blocks of data that helps protect against erasure of
whole blocks. The general ISA-L library contains an expanded set of
functions used for data protection, hashing, encryption, etc.

This package contains the shared library.

%package devel
Summary:	Intel(R) Intelligent Storage Acceleration Library - devel files
Requires:	%{name}%{?_isa} = %{version}-%{release}

%description devel
Collection of low-level functions used in storage applications.
Contains fast erasure codes that implement a general Reed-Solomon type
encoding for blocks of data that helps protect against erasure of
whole blocks. The general ISA-L library contains an expanded set of
functions used for data protection, hashing, encryption, etc.

This package contains the development files needed to build against
the shared library.

%package tools
Summary:	Intel(R) Intelligent Storage Acceleration Library - tool
Requires:	%{name}%{?_isa} = %{version}-%{release}

%description tools
Collection of low-level functions used in storage applications.
Contains fast erasure codes that implement a general Reed-Solomon type
encoding for blocks of data that helps protect against erasure of
whole blocks. The general ISA-L library contains an expanded set of
functions used for data protection, hashing, encryption, etc.

This package contains CLI tools.

%prep
%setup -q
%patch -P 0 -p1
%patch -P 1 -p1

%build
autoreconf -v -f -i
%configure --disable-static
%make_build

%install
%make_install
rm %{buildroot}%{_libdir}/*.la

%check
%make_build check

%ldconfig_scriptlets

%files
%{_libdir}/libisal.so.2*
%license LICENSE

%files devel
%{_includedir}/isa-l.h
%{_includedir}/isa-l
%{_libdir}/libisal.so
%{_libdir}/pkgconfig/libisal.pc
%doc examples

%files tools
%{_bindir}/igzip
%{_mandir}/man1/igzip.1*

%changelog
* Sat Nov 11 2023 Mattias Ellert <mattias.ellert@physics.uu.se> - 2.30.0-1
- Initial package for Fedora
