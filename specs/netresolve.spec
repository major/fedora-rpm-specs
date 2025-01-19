%global snapshot_suffix .20160317git

Name: netresolve
Version: 0.0.1
Release: 0.42%{?snapshot_suffix}%{?dist}
Summary: Generic name resolution library
# Automatically converted from old format: BSD - review is highly recommended.
License: LicenseRef-Callaway-BSD
# https://github.com/crossdistro/netresolve , possibly?
URL: https://sourceware.org/%{name}/
Source0: %{name}-0.0.1.tar.xz
# Fix a syntax error in a test
# From https://github.com/crossdistro/netresolve/pull/2
Patch0: netresolve-0.0.1-test-equality.patch
Patch1: netresolve-0.0.1-strncpy.patch
# https://github.com/crossdistro/netresolve/issues/3
Patch2: netresolve-0.0.1-hosts.patch
Patch3: netresolve-0.0.1-use-after-free.patch
# https://github.com/crossdistro/netresolve/pull/5
Patch4: netresolve-0.0.1-configure-as-if.patch

BuildRequires: make
BuildRequires: ldns-devel
BuildRequires: pkgconfig(libcares)
%if 0%{?fedora}
BuildRequires: unbound-devel
%endif
BuildRequires: pkgconfig(avahi-client)
BuildRequires: pkgconfig(libasyncns)
# live builds
BuildRequires: autoconf automake libtool
# tests
BuildRequires: valgrind
%if 0%{?rhel}
# https://bugzilla.redhat.com/show_bug.cgi?id=1190724
BuildRequires: openssl-devel
%endif
# subpackages installed by netresolve virtual package
Requires: %{name}-core%{?_isa} = %{version}-%{release}
Requires: %{name}-tools%{?_isa} = %{version}-%{release}
Requires: %{name}-compat%{?_isa} = %{version}-%{release}
Requires: %{name}-backends-compat%{?_isa} = %{version}-%{release}
Requires: %{name}-backends-aresdns%{?_isa} = %{version}-%{release}
Requires: %{name}-backends-avahi%{?_isa} = %{version}-%{release}
%description
Netresolve is a package for non-blocking network name resolution via backends
intended as a replacement for name service switch based name resolution in
glibc as well as a testbed for future glibc improvements.

%package core
Summary: Core netresolve libraries
%description core
This package provides core netresolve library with basic name resolution
capabilities for tools and application.

%package compat
Summary: Compatibility netresolve libraries and tools
Requires: %{name}-core%{?_isa} = %{version}-%{release}
%description compat
This package provides libraries and tools for using netresolve from applications
built against other name resolution libraries.

%package tools
Summary: Command line tools based on core netresolve libraries
Requires: %{name}-core%{?_isa} = %{version}-%{release}
%description tools
This package provides tools that provide netresolve capabilities using the
command line.

%package backends-compat
Summary: Backends for netresolve using existing tools
Requires: %{name}-core%{?_isa} = %{version}-%{release}
%description backends-compat
This package provides backends for querying libc, glibc nsswitch backends,
asyncns and other existing name resolution libraries.

%package backends-aresdns
Summary: DNS backend for netresolve based on aresdns
Requires: %{name}-core%{?_isa} = %{version}-%{release}
%description backends-aresdns
This package provides DNS capabilities including learning DNSSEC validity
from the AD flag for netresolve using c-ares.

%package backends-avahi
Summary: Multicast DNS backend for netresolve based on libavahi
Requires: %{name}-core%{?_isa} = %{version}-%{release}
%description backends-avahi
This package provides Multicast DNS capabilities using Avahi daemon and
libraries.

%if 0%{?fedora}
%package backends-ubdns
Summary: DNS backend for netresolve based on libunbound
Requires: %{name}-core%{?_isa} = %{version}-%{release}
%description backends-ubdns
This package provides DNS capabilities including DNSSEC validation to
netresolve using libunbound.
%endif

%package devel
Summary: Development files for netresolve
Requires: %{name}%{?_isa} = %{version}-%{release}
%description devel
This package contains header files and libraries needed to compile
applications or shared objects that use netresolve.

%prep
%autosetup -p1
NOCONFIGURE=yes ./autogen.sh

# disable some tests for now
sed -i \
    -e '/999999x/d' \
    -e '/x-x-x-x-x-x-x-x-x/d' \
    tests/test-netresolve.sh

%build
%configure \
    --disable-silent-rules
make %{?_smp_mflags}

%install
%make_install
find %{buildroot} -name '*.la' -delete

%if 0%{?fedora}
%check
export NETRESOLVE_TEST_COMMAND="libtool execute valgrind --leak-check=full --error-exitcode=1 ./netresolve"
make check || { cat ./test-suite.log; false; }
%endif

%ldconfig_scriptlets

%ldconfig_scriptlets core

%ldconfig_scriptlets compat

%ldconfig_scriptlets backends-compat

%ldconfig_scriptlets backends-aresdns

%if 0%{?fedora}
%ldconfig_scriptlets backends-ubdns
%endif

%ldconfig_scriptlets backends-avahi

%files

%files core
%license COPYING
%doc README TODO NEWS
%{_libdir}/libnetresolve-backend-any.so.0
%{_libdir}/libnetresolve-backend-any.so.0.0.0
%{_libdir}/libnetresolve-backend-exec.so.0
%{_libdir}/libnetresolve-backend-exec.so.0.0.0
%{_libdir}/libnetresolve-backend-hostname.so.0
%{_libdir}/libnetresolve-backend-hostname.so.0.0.0
%{_libdir}/libnetresolve-backend-hosts.so.0
%{_libdir}/libnetresolve-backend-hosts.so.0.0.0
%{_libdir}/libnetresolve-backend-loopback.so.0
%{_libdir}/libnetresolve-backend-loopback.so.0.0.0
%{_libdir}/libnetresolve-backend-numerichost.so.0
%{_libdir}/libnetresolve-backend-numerichost.so.0.0.0
%{_libdir}/libnetresolve-backend-unix.so.0
%{_libdir}/libnetresolve-backend-unix.so.0.0.0
%{_libdir}/libnetresolve.so.0
%{_libdir}/libnetresolve.so.0.0.0
%{_libdir}/libnss_netresolve.so.2
%{_libdir}/libnss_netresolve.so.2.0.0

%files tools
%{_bindir}/getaddrinfo
%{_bindir}/gethostbyaddr
%{_bindir}/gethostbyname
%{_bindir}/getnameinfo
%{_bindir}/netresolve
%{_bindir}/res_query

%files compat
%{_bindir}/wrapresolve
%{_libdir}/libnetresolve-asyncns.so.0
%{_libdir}/libnetresolve-asyncns.so.0.0.0
%{_libdir}/libnetresolve-libc.so.0
%{_libdir}/libnetresolve-libc.so.0.0.0

%files backends-compat
%{_libdir}/libnetresolve-backend-asyncns.so.0
%{_libdir}/libnetresolve-backend-asyncns.so.0.0.0
%{_libdir}/libnetresolve-backend-libc.so.0
%{_libdir}/libnetresolve-backend-libc.so.0.0.0
%{_libdir}/libnetresolve-backend-nss.so.0
%{_libdir}/libnetresolve-backend-nss.so.0.0.0

%files backends-aresdns
%{_libdir}/libnetresolve-backend-aresdns.so.0
%{_libdir}/libnetresolve-backend-aresdns.so.0.0.0

%files backends-avahi
%{_libdir}/libnetresolve-backend-avahi.so.0
%{_libdir}/libnetresolve-backend-avahi.so.0.0.0

%if 0%{?fedora}
%files backends-ubdns
%{_libdir}/libnetresolve-backend-ubdns.so.0
%{_libdir}/libnetresolve-backend-ubdns.so.0.0.0
%endif

%files devel
%{_includedir}/netresolve-epoll.h
%{_includedir}/netresolve-event.h
%{_includedir}/netresolve-glib.h
%{_includedir}/netresolve-nonblock.h
%{_includedir}/netresolve-select.h
%{_includedir}/netresolve.h
%{_libdir}/libnetresolve-asyncns.so
%{_libdir}/libnetresolve-backend-any.so
%{_libdir}/libnetresolve-backend-aresdns.so
%{_libdir}/libnetresolve-backend-asyncns.so
%{_libdir}/libnetresolve-backend-avahi.so
%{_libdir}/libnetresolve-backend-exec.so
%{_libdir}/libnetresolve-backend-hostname.so
%{_libdir}/libnetresolve-backend-hosts.so
%{_libdir}/libnetresolve-backend-libc.so
%{_libdir}/libnetresolve-backend-loopback.so
%{_libdir}/libnetresolve-backend-nss.so
%{_libdir}/libnetresolve-backend-numerichost.so
%if 0%{?fedora}
%{_libdir}/libnetresolve-backend-ubdns.so
%endif
%{_libdir}/libnetresolve-backend-unix.so
%{_libdir}/libnetresolve-libc.so
%{_libdir}/libnetresolve.so
%{_libdir}/libnss_netresolve.so

%changelog
* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.1-0.42.20160317git
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Mon Sep 02 2024 Miroslav Suchý <msuchy@redhat.com> - 0.0.1-0.41.20160317git
- convert license to SPDX

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.1-0.40.20160317git
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.1-0.39.20160317git
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.1-0.38.20160317git
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.1-0.37.20160317git
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.1-0.36.20160317git
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Dec 02 2022 Petr Menšík <pemensik@redhat.com> - 0.0.1-0.35.20160317git
- Remove duplicate file entries
- Build with Autoconf 2.72 (#2144836)

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.1-0.34.20160317git
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Sat Jan 22 2022 Petr Menšík <pemensik@redhat.com> - 0.0.1-0.33.20160317git
- Correct compilation issues

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.1-0.32.20160317git
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.1-0.31.20160317git
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.1-0.30.20160317git
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Sat Dec 19 2020 Adam Williamson <awilliam@redhat.com> - 0.0.1-0.29.20160317git
- Rebuild for libldns soname bump

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.1-0.28.20160317git
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.1-0.27.20160317git
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Tue Sep 10 2019 Petr Menšík <pemensik@redhat.com> - 0.0.1-0.26.20160317git
- Pass tests even without trailing newline in hosts (#1736166)

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.1-0.25.20160317git
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Tue Feb 19 2019 Petr Menšík <pemensik@redhat.com> - 0.0.1-0.24.20160317git
- Fix build under new gcc (#1675450)

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.1-0.23.20160317git
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Mon Oct 08 2018 Petr Menšík <pemensik@redhat.com> - 0.0.1-0.22.20160317git
- Rebuilt for unbound 1.8

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.1-0.21.20160317git
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.1-0.20.20160317git
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.1-0.19.20160317git
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.1-0.18.20160317git
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Thu Mar 09 2017 Adam Williamson <awilliam@redhat.com> - 0.0.1-0.17.20160317git
- Fix a syntax error in a test which broke compilation (pemensik)

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.1-0.16.20160317git
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Mar 14 2016 Pavel Šimerda <psimerda@redhat.com> - 0.0.1-0.15.20160314git
- buildable on rhel, updated from git master

* Mon Mar 07 2016 Pavel Šimerda <psimerda@redhat.com> - 0.0.1-0.14.20160307git
- update from git master

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.1-0.13.20160121git
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Jan 21 2016 Pavel Šimerda <psimerda@redhat.com> - 0.0.1-0.12.20160121git
- updated live source

* Tue Jan 05 2016 Pavel Šimerda <psimerda@redhat.com> - 0.0.1-0.11.20151111git
- rebuilt

* Mon Jan 04 2016 Pavel Šimerda <psimerda@redhat.com> - 0.0.1-0.10.20151111git
- rebuilt

* Wed Dec 16 2015 Pavel Šimerda <psimerda@redhat.com> - 0.0.1-0.9.20151111git
- rebuilt

* Tue Nov 24 2015 Pavel Šimerda <psimerda@redhat.com> - 0.0.1-0.8.20151111git
- applied feedback

* Mon Nov 09 2015 Pavel Šimerda <psimerda@redhat.com> - 0.0.1-0.7.20151109git
- updated live source, incorporated feedback

* Thu Oct 15 2015 Pavel Šimerda <psimerda@redhat.com> - 0.0.1-0.6.20151015git
- updated live source, incorporated feedback

* Thu Sep 17 2015 Pavel Šimerda <psimerda@redhat.com> - 0.0.1-0.5.20150923git
- lots of changes upstream since the last time

* Sun Nov 02 2014 Pavel Šimerda <psimerda@redhat.com> - 0.0.1-0.4.20141102git
- rebuilt

* Wed May 21 2014 Pavel Šimerda <psimerda@redhat.com> - 0.0.1-0.3.20140422git
- avoid running the tests

* Thu Apr 24 2014 Pavel Šimerda <psimerda@redhat.com> - 0.0.1-0.2.20140422git
- incorporate review feedback

* Wed Apr 23 2014 Pavel Šimerda <psimerda@redhat.com> - 0.0.1-0.1.20140422git
- initial build
