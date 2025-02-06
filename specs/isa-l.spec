Name:		isa-l
Version:	2.31.1
Release:	4%{?dist}
Summary:	Intel(R) Intelligent Storage Acceleration Library

License:	BSD-3-Clause
URL:		https://github.com/intel/isa-l
Source0:	%{url}/archive/v%{version}/isa-l-%{version}.tar.gz
#		https://github.com/intel/isa-l/pull/310
Patch0:		0001-Address-compiler-warnings-on-ppc64le-and-s390x.patch
#		https://github.com/intel/isa-l/issues/311
Patch1:		0001-igzip-fix-header-construction-in-Big-Endian-systems.patch

ExcludeArch:	%{ix86}

BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libtool
BuildRequires:	make
BuildRequires:	gcc
BuildRequires:	nasm

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
%patch -P0 -p1
%patch -P1 -p1

%build
autoreconf -v -f -i
%configure --disable-static
%make_build

%install
%make_install
rm %{buildroot}%{_libdir}/*.la

%check
%make_build check
%make_build test
%make_build perf

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
* Tue Feb 04 2025 Mattias Ellert <mattias.ellert@physics.uu.se> - 2.31.1-4
- Backport fix for big endian block header bug

* Sat Jan 18 2025 Mattias Ellert <mattias.ellert@physics.uu.se> - 2.31.1-3
- Adderss compiler warnings on ppc64le and s390x

* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 2.31.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Tue Jan 07 2025 Mattias Ellert <mattias.ellert@physics.uu.se> - 2.31.1-1
- Update to version 2.31.1

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.31.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Wed Jan 24 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.31.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sat Jan 20 2024 Mattias Ellert <mattias.ellert@physics.uu.se> - 2.31.0-1
- Update to version 2.31.0
- Drop EPEL 7 support
- Run more tests

* Sat Nov 11 2023 Mattias Ellert <mattias.ellert@physics.uu.se> - 2.30.0-1
- Initial package for Fedora
