Name:           sofia-sip
Version:        1.13.16
Release:        %autorelease
Summary:        Sofia SIP User-Agent library

License:        LGPL-2.1-or-later
URL:            http://sofia-sip.sourceforge.net/
Source0:        https://github.com/freeswitch/%{name}/archive/refs/tags/v%{version}.tar.gz

# https://github.com/freeswitch/sofia-sip/pull/249
Patch0:         0001-Fix-incompatible-pointer-type-in-sip_basic.c.patch

BuildRequires:  make
BuildRequires:  gcc-c++
BuildRequires:  openssl-devel
BuildRequires:  glib2-devel
BuildRequires:  lksctp-tools-devel
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:  libtool >= 1.5.17

%description
Sofia SIP is a RFC-3261-compliant library for SIP user agents and
other network elements.  The Session Initiation Protocol (SIP) is an
application-layer control (signaling) protocol for creating,
modifying, and terminating sessions with one or more
participants. These sessions include Internet telephone calls,
multimedia distribution, and multimedia conferences.

%package devel
Summary:        Sofia-SIP Development Package
Requires:       sofia-sip = %{version}-%{release}
Requires:       pkgconfig

%description devel
Development package for Sofia SIP UA library.

%package glib
Summary:        Glib bindings for Sofia-SIP
Requires:       sofia-sip = %{version}-%{release}

%description glib
GLib interface to Sofia SIP User Agent library.

%package glib-devel
Summary:        Glib bindings for Sofia SIP development files
Requires:       sofia-sip-glib = %{version}-%{release}
Requires:       sofia-sip-devel = %{version}-%{release}
Requires:       pkgconfig

%description  glib-devel
Development package for Sofia SIP UA Glib library. This package
includes libraries and include files for developing glib programs
using Sofia SIP.

%package utils
Summary:        Sofia-SIP Command Line Utilities
Requires:       sofia-sip = %{version}-%{release}

%description utils
Command line utilities for the Sofia SIP UA library.


%prep
%autosetup -p1

%build
sh autogen.sh
%configure --disable-rpath --disable-static --without-doxygen --disable-stun
make %{?_smp_mflags}

%install
%make_install
find %{buildroot} -name \*.la -delete
find %{buildroot} -name \*.h.in -delete
find . -name installdox -delete

%ldconfig_scriptlets
%ldconfig_scriptlets glib

%files
%doc AUTHORS ChangeLog ChangeLog.ext-trees COPYING COPYRIGHTS
%doc README README.developers RELEASE TODO
%{_libdir}/libsofia-sip-ua.so.*

%files devel
#%doc libsofia-sip-ua/docs/html
%dir %{_includedir}/sofia-sip-1.13
%dir %{_includedir}/sofia-sip-1.13/sofia-sip
%{_includedir}/sofia-sip-1.13/sofia-sip/*.h
%exclude %{_includedir}/sofia-sip-1.13/sofia-sip/su_source.h
%dir %{_includedir}/sofia-sip-1.13/sofia-resolv
%{_includedir}/sofia-sip-1.13/sofia-resolv/*.h
%{_libdir}/libsofia-sip-ua.so
%{_libdir}/pkgconfig/sofia-sip-ua.pc
%{_datadir}/sofia-sip

%files glib
%{_libdir}/libsofia-sip-ua-glib.so.*

%files glib-devel
%{_includedir}/sofia-sip-1.13/sofia-sip/su_source.h
%{_libdir}/libsofia-sip-ua-glib.so
%{_libdir}/pkgconfig/sofia-sip-ua-glib.pc

%files utils
%{_bindir}/addrinfo
%{_bindir}/localinfo
%{_bindir}/sip-date
%{_bindir}/sip-dig
%{_bindir}/sip-options


%changelog
%autochangelog
