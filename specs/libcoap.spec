#global candidate rc1

Name:     libcoap
Version:  4.3.5a
Release:  %autorelease
Summary:  C library implementation of CoAP
URL:      https://libcoap.net/
# If build against gnutls the license is BSD + LGPL 2.1
# Automatically converted from old format: BSD - review is highly recommended.
License:  LicenseRef-Callaway-BSD

Source0:  https://github.com/obgm/libcoap/archive/v%{version}.tar.gz#/%{name}-%{version}%{?candidate:-%{candidate}}.tar.gz

BuildRequires: autoconf
BuildRequires: automake
BuildRequires: gcc
BuildRequires: libtool
BuildRequires: openssl-devel
BuildRequires: openssl-devel-engine
BuildRequires: asciidoc
BuildRequires: ctags
BuildRequires: doxygen
BuildRequires: graphviz
BuildRequires: make

%description
The Constrained Application Protocol (CoAP) is a specialized web transfer 
protocol for use with constrained nodes and constrained networks in the Internet 
of Things. The protocol is designed for machine-to-machine (M2M) applications 
such as smart energy and building automation.

libcoap implements a lightweight application-protocol for devices with 
constrained resources such as computing power, RF range, memory, bandwidth,
or network packet sizes. This protocol, CoAP, was standardized in the IETF
working group "CoRE" as RFC 7252.

%package  utils
Summary:  Client and server CoAP utilities
Requires: %{name}%{?_isa} = %{version}-%{release}

%description utils
Utilities for working with %{name}.

%package  devel
Summary:  Development package for %{name}
Requires: %{name}%{?_isa} = %{version}-%{release}

%description devel
Files for development with %{name}.

%package  doc
Summary:  Documentation package for %{name}
BuildArch: noarch

%description doc
Documentation for development with %{name}.

%prep
%autosetup -p1 -n %{name}-%{version}%{?candidate:-%{candidate}}

%build
autoreconf -vif
%configure --without-debug CFLAGS="$RPM_OPT_FLAGS -D COAP_DEBUG_FD=stderr" \
           --enable-examples --enable-documentation --enable-doxygen --enable-manpages \
           --enable-dtls --with-openssl --disable-static

%make_build

%install
%make_install

#Remove libtool archives
find %{buildroot} -name '*.la' -delete
find %{buildroot} -name '*.a' -delete
rm -rf %{buildroot}/%{_datadir}/%{name}

%check
make check

%ldconfig_scriptlets

%files
%license LICENSE COPYING
%doc AUTHORS
%{_libdir}/libcoap-3-openssl.so.3*

%files utils
%{_bindir}/coap*
%{_mandir}/man5/coap*

%files doc
%{_mandir}/man7/coap*
%{_datadir}/doc/libcoap/

%files devel
%{_mandir}/man3/coap*
%{_includedir}/coap3/
%{_libdir}/pkgconfig/libcoap-3*.pc
%{_libdir}/libcoap-3*.so

%changelog
%autochangelog
