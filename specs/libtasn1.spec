Summary:	The ASN.1 library used in GNUTLS
Name:		libtasn1
Version:	4.20.0
Release:	%autorelease

# The libtasn1 library is LGPLv2+, utilities are GPLv3+
License:	GPL-3.0-or-later AND LGPL-2.1-or-later
URL:		http://www.gnu.org/software/libtasn1/
Source0:	http://ftp.gnu.org/gnu/libtasn1/%name-%version.tar.gz
Source1:	http://ftp.gnu.org/gnu/libtasn1/%name-%version.tar.gz.sig
#Source2:	gpgkey-1F42418905D8206AA754CCDC29EE58B996865171.gpg
#Source2:	gpgkey-99415CE1905D0E55A9F88026860B7FBB32F8119D.gpg
Source2:        gpgkey-B1D2BD1375BECB784CF4F8C4D73CF638C53C06BE.gpg
Patch1:		libtasn1-3.4-rpath.patch

BuildRequires:	gnupg2
BuildRequires:	gcc
BuildRequires:	bison, pkgconfig, help2man
BuildRequires:	autoconf, automake, libtool
%ifarch %{valgrind_arches}
BuildRequires:	valgrind-devel
%endif
BuildRequires:  make
BuildRequires:  gtk-doc
# Wildcard bundling exception https://fedorahosted.org/fpc/ticket/174
Provides: bundled(gnulib) = 20130324

%package devel
Summary:	Files for development of applications which will use libtasn1
Requires:	%{name}%{?_isa} = %{version}-%{release}

Requires:	%name = %version-%release
Requires:	%{name}-tools = %{version}-%{release}
Requires:	pkgconfig


%package tools
Summary:	Some ASN.1 tools
# Automatically converted from old format: GPLv3+ - review is highly recommended.
License:	GPL-3.0-or-later
Requires:	%{name}%{?_isa} = %{version}-%{release}


%description
A library that provides Abstract Syntax Notation One (ASN.1, as specified
by the X.680 ITU-T recommendation) parsing and structures management, and
Distinguished Encoding Rules (DER, as per X.690) encoding and decoding functions.

%description devel
This package contains files for development of applications which will
use libtasn1.


%description tools
This package contains simple tools that can decode and encode ASN.1
data.


%prep
gpgv2 --keyring %{SOURCE2} %{SOURCE1} %{SOURCE0}
%setup -q

%patch -P1 -p1 -b .rpath

%build
autoreconf -v -f --install
%configure --disable-static --disable-silent-rules
# libtasn1 likes to regenerate docs
touch doc/stamp_docs

%make_build


%install
%make_install

rm -f $RPM_BUILD_ROOT{%_libdir/*.la,%_infodir/dir}


%check
make check

%files
%license COPYING COPYING.LESSERv2
%doc AUTHORS NEWS README.md
%{_libdir}/*.so.6*

%files tools
%{_bindir}/asn1*
%{_mandir}/man1/asn1*

%files devel
%{_libdir}/*.so
%{_libdir}/pkgconfig/*.pc
%{_includedir}/*
%{_infodir}/*.info.*
%{_mandir}/man3/*asn1*


%changelog
%autochangelog
