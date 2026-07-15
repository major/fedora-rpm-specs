Name:           libcanlock
Version:        3.3.3
Release:        %autorelease
Summary:        Create and verify RFC 8315 Netnews Cancel-Locks
# BSD licensed:
# include/base64.h
# include/sha.h
# include/sha-private.h
# src/base64.c
# src/hmac.c
# src/sha1.c
# src/sha224-256.c
# src/sha384-512.c
# src/usha.c
# test/hkdf.c
# test/shatest.c
# NLPL licensed:
# ChangeLog
# README
# ICU licensed:
# include/canlock-private.h
# include/canlock.h
# src/canlock.c
# src/secret.c
# util/canlock.c
# hp/include/hfp_lexer.h
# hp/include/hfp_parser_external.h
# hp/include/package_name.h
# hp/src/parser.c
# hp/src/unfold.c
# hp/util/canlock-hfp.c
# hp/util/canlock-mhp.c
# hp/util/hfp_lexer.l
# hp/util/hfp_parser.y
# hp/util/package_name.c
License:        BSD-3-Clause AND NLPL AND ICU
URL:            https://micha.freeshell.org/libcanlock
Source0:        %{url}/src/%{name}-%{version}.tar.bz2
BuildRequires:  byacc
BuildRequires:  dos2unix
BuildRequires:  flex
BuildRequires:  gcc
BuildRequires:  grep
BuildRequires:  make
BuildRequires:  sed

%description
A library for creating and verifying RFC 8315 Netnews Cancel-Locks.
This implementation uses the recommended algorithm from Section 4 with HMAC
based on the same hash function as <scheme>.

%package devel
Summary:        Development files for libcanlock
Requires:       libcanlock%{?_isa} = %{version}-%{release}

%description devel
This package holds the development files for libcanlock.

%package -n canlock
Summary:        Command line utilities for Netnews Cancel-Lock authentication scheme
Requires:       libcanlock%{?_isa} = %{version}-%{release}

%description -n canlock
Command line utilities for Netnews Cancel-Lock authentication scheme.

canlock can be used to create <c-lock> and <c-key> elements according to
RFC 8315.  The secret data is read from standard input (using EOF for
termination).

canlock also provides a verify interface with the -c option.  An external
header parser is required to extract the <c-key> and <c-lock> elements
from the article headers. The command line utilities canlock-mhp(1) and
canlock-hfp(1) can be used for this purpose.

%prep
%autosetup
dos2unix -k hp/examples/{supersede,target}.txt
cp -p hp/COPYING COPYING.hp

%build
%configure --enable-pc-files
%make_build

%install
%make_install
rm -v %{buildroot}%{_libdir}/libcanlock{,-hp}.a

%check
%make_build check

%files
%doc ChangeLog README doc/sec_review.txt
%license COPYING COPYING.hp
%{_libdir}/libcanlock.so.3{,.*}
%{_libdir}/libcanlock-hp.so.3{,.*}

%files devel
%doc TODO examples/* hp/examples/*
%{_libdir}/libcanlock.so
%{_libdir}/libcanlock-hp.so
%{_includedir}/libcanlock-3/
%{_libdir}/pkgconfig/libcanlock-3.pc
%{_libdir}/pkgconfig/libcanlock-hp-3.pc
%{_mandir}/man3/cl_clear_secret.3*
%{_mandir}/man3/cl_get_key.3*
%{_mandir}/man3/cl_get_lock.3*
%{_mandir}/man3/cl_hp_get_field.3*
%{_mandir}/man3/cl_hp_parse_field.3*
%{_mandir}/man3/cl_hp_unfold_field.3*
%{_mandir}/man3/cl_split.3*
%{_mandir}/man3/cl_verify.3*
%{_mandir}/man3/cl_verify_multi.3*

%files -n canlock
%{_bindir}/canlock
%{_bindir}/canlock-hfp
%{_bindir}/canlock-mhp
%{_mandir}/man1/canlock.1*
%{_mandir}/man1/canlock-hfp.1*
%{_mandir}/man1/canlock-mhp.1*

%changelog
%autochangelog
