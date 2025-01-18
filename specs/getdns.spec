# Stubby has its own package now
%bcond_with stubby
#%%global extraver rc1
%global upstream_version %{version}%{?extraver:-%{extraver}}
%global stubby_version 0.4.2

%undefine __cmake_in_source_build

Summary: Modern asynchronous API to the DNS
Name: getdns
Version: 1.7.3
Release: 7%{?extraver:.%{extraver}}%{?dist}
License: BSD-3-Clause
Url: http://www.getdnsapi.net
Source: http://www.getdnsapi.net/dist/%{name}-%{upstream_version}.tar.gz
Source1: http://www.getdnsapi.net/dist/%{name}-%{upstream_version}.tar.gz.asc
Source2: http://keys.gnupg.net/pks/lookup?op=get&search=0xE5F8F8212F77A498#/willem.nlnetlabs.nl
BuildRequires:  gcc
BuildRequires: libidn2-devel unbound-devel doxygen libevent-devel
BuildRequires: pkgconfig openssl-devel libyaml-devel
BuildRequires: systemd-rpm-macros
BuildRequires: libuv-devel libev-devel check-devel
BuildRequires: cmake
BuildRequires: gnupg2
Requires: unbound-libs

%if %{with stubby}
Source2: stubby.service
%endif

#Patch0:

%description
getdns is a modern asynchronous DNS API. It implements DNS entry points
from a design developed and vetted by application developers, in an API
specification edited by Paul Hoffman. With the development of this API,
we intend to offer application developers a modernized and flexible way
to access DNS security (DNSSEC) and other powerful new DNS features; a
particular hope is to inspire application developers towards innovative
security solutions in their applications.

%package devel
Summary: Development package that includes getdns header files
Requires: %{name}%{?_isa} = %{version}-%{release}

%description devel
The devel package contains the getdns library and the include files and
some example C code.

%package utils
Summary: getdns utilities
Requires: %{name}%{?_isa} = %{version}-%{release}

%description utils
The %{name}-utils package contains utilities using getdns library,
getdns_query and getdns_query_mon utilities. They can be used to analyze
responses from DNS servers over UDP, TCP and TLS, including support for
DNS security.

getdns_query can be used for fetching details of DNS responses in json format.
getdns_query_mon is great for automated monitoring of DNS server replies.

%if %{with stubby}
%package stubby
Summary: DNS Privacy Daemon - Stubby
Requires: %{name}%{?_isa} = %{version}-%{release}
Provides: stubby%{?_isa} = stubby-%{stubby_version}

%description stubby 
Stubby is an application that acts as a local DNS Privacy stub resolver (using DNS-over-TLS). Stubby encrypts DNS queries sent from a client machine (desktop or laptop) to a DNS Privacy resolver increasing end user privacy. Stubby is in the early stages of development but is suitable for technical/advanced users. A more generally user-friendly version is on the way!
%end
%endif

%prep
%{?gpgverify:%gpgverify -k 2 -s 1 -d 0}
%autosetup -p1 -n %{name}-%{upstream_version}

%build
%cmake -DCMAKE_BUILD_TYPE=RelWithDebInfo -DENABLE_STATIC=OFF \
  -DPATH_TRUST_ANCHOR_FILE=%{_sharedstatedir}/unbound/root.key \
%if %{with stubby}
  -DBUILD_STUBBY=ON \
%endif

%cmake_build

%check
# make test needs a network connection - so disabled per default
# make test

%install
%cmake_install

%if %{with stubby}
mkdir -p %{buildroot}%{_unitdir}
install -m 644 %{SOURCE2} %{buildroot}%{_unitdir}/stubby.service
install -d -m 0750 %{buildroot}%{_localstatedir}/cache/stubby
install -d -m 0755 %{buildroot}%{_sysconfdir}/stubby
install -d %__cmake_builddir/stubby/stubby.yml %{buildroot}%{_sysconfdir}/stubby/stubby.yml
rm -rf %{buildroot}%{_docdir}/stubby
%endif

rm -rf %{buildroot}%{_libdir}/*.la
rm -rf %{buildroot}%{_docdir}/%{name}

%files
%{_libdir}/libgetdns*so.10*
%doc README.md NEWS AUTHORS ChangeLog
%license LICENSE

%files utils
%{_bindir}/getdns_query
%{_bindir}/getdns_server_mon

%if %{with stubby}
%files stubby
%{_bindir}/stubby
%{_mandir}/*/stubby.1*
%dir %attr(0755,root,root) %{_sysconfdir}/stubby
%config(noreplace) %{_sysconfdir}/stubby/stubby.yml
%attr(0644,root,root) %{_unitdir}/stubby.service
%dir %attr(0750,stubby,stubby) %{_localstatedir}/cache/stubby
%doc stubby/README.md stubby/AUTHORS stubby/NEWS stubby/ChangeLog
%endif

%files devel
%{_libdir}/libgetdns*.so
%{_includedir}/getdns/
%{_libdir}/pkgconfig/*.pc
%{_mandir}/*/*.3*
%doc spec

%post
%{?ldconfig}

%postun
%{?ldconfig}
%end

%if %{with stubby}
%pre stubby
getent group stubby >/dev/null || groupadd -r stubby
getent passwd stubby >/dev/null || \
useradd -r -g stubby -d %{_sysconfdir}/stubby -s /sbin/nologin \
    -c "stubby DNS daemon account" stubby
exit 0

%post stubby
%systemd_post stubby.service

%preun stubby
%systemd_preun stubby.service

%postun stubby
%systemd_postun_with_restart stubby.service
%end
%endif

%changelog
* Thu Jan 16 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.3-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.3-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Wed Jan 24 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.3-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Mon Jan 02 2023 Petr Menšík <pemensik@redhat.com> - 1.7.3-1
- Update to 1.7.3 (#2155879)

* Tue Dec  6 2022 Florian Weimer <fweimer@redhat.com> - 1.7.2-2
- Backport patch from upstream to fix pointer truncation

* Thu Oct 13 2022 Petr Menšík <pemensik@redhat.com> - 1.7.2-1
- Update to 1.7.2 (#1974450)

* Fri Sep 30 2022 Petr Menšík <pemensik@redhat.com> - 1.7.0-7
- Update License tag to SPDX identifier

* Tue Aug 02 2022 Petr Menšík <pemensik@redhat.com> - 1.7.0-6
- Build with libidn2 2.3.3 (#2113237)

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Tue Sep 14 2021 Sahana Prasad <sahana@redhat.com> - 1.7.0-3
- Rebuilt with OpenSSL 3.0.0

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Mon Jun 07 2021 Paul Wouters <paul.wouters@aiven.io> - 1.7.0-1
- Resolves: rhbz#1965739 getdns-1.7.0 is available
- Resolves: rhbz#1946537 libgetdns_ex_event.so does not contain getdns_extension_set_libevent_base symbol

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Sep 15 2020 Petr Menšík <pemensik@redhat.com> - 1.6.0-6
- Rebuilt for libevent rebase

* Fri Aug 07 2020 Petr Menšík <pemensik@redhat.com> - 1.6.0-5
- Fix cmake build (#1863610)

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.0-4
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Mar 19 2020 Petr Menšík <pemensik@redhat.com> - 1.6.0-2
- Disable stubby subpackage, it has its own package
- Move getdns_query* utilities into getdns-utils subpackage

* Thu Mar 12 2020 Petr Menšík <pemensik@redhat.com> - 1.6.0-1
- Update to 1.6.0

* Wed Mar 11 2020 Petr Menšík <pemensik@redhat.com> - 1.5.2-5
- Build dependency on systemd macrosw (#1799398)

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Apr 07 2019 Petr Menšík <pemensik@redhat.com> - 1.5.2-2
- Update to 1.5.2 (#1689431)

* Tue Mar 19 2019 Petr Menšík <pemensik@redhat.com> - 1.5.2-1.rc1
- Update to 1.5.2-rc1 (#1689431)

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Tue Oct 09 2018 Petr Menšík <pemensik@redhat.com> - 1.4.2-4
- Rebuilt for unbound 1.8

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jul 03 2018 Petr Menšík <pemensik@redhat.com> - 1.4.2-2
- Use trust anchor managed by unbound-libs
- Prepare directory for Zero-config Trust anchor

* Fri May 11 2018 Paul Wouters <pwouters@redhat.com> - 1.4.2-1
- Resolves: rhbz#1575173 Updated to 1.4.2

* Mon Mar 12 2018 Paul Wouters <pwouters@redhat.com> - 1.4.1-1
- Resolves rhbz#1551810 Updated to 1.4.1

* Thu Feb 22 2018 Paul Wouters <pwouters@redhat.com> - 1.4.0-1
- Updated to 1.4.0 (which includes previous patch)

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Sun Jan 14 2018 Paul Wouters <pwouters@redhat.com> - 1.3.0-4
- Remove WorkingDir from stubby.service, no longer need tmpfiles

* Wed Jan 10 2018 Paul Wouters <pwouters@redhat.com> - 1.3.0-3
- Minor fixup for previous patch
- Add Provides: for stubby

* Fri Jan 05 2018 Paul Wouters <pwouters@redhat.com> - 1.3.0-2
- Resolves: 1449127 getdns: switch to libidn2

* Tue Jan 02 2018 Paul Wouters <pwouters@redhat.com> - 1.3.0-1
- Updated to 1.3.0
- Move stubby from -devel to main package
- Add stubby as systemd service

* Fri Nov 17 2017 Paul Wouters <pwouters@redhat.com> - 1.2.1-1
- Updated to 1.2.1

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Tue Jan 24 2017 Paul Wouters <pwouters@redhat.com> - 1.0.0-1
- Updated to 1.0.0

* Thu Sep 22 2016 Paul Wouters <pwouters@redhat.com> - 1.0.0-0.1.b2
- Updated to 1.0.0b2
- Moved getdns_query from devel to core package
- No longer require ldns

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Sat Jan 30 2016 Paul Wouters <pwouters@redhat.com> - 0.9.0-1
- Updated to 0.9.0
- Support pkgconfig

* Thu Nov 19 2015 Paul Wouters <pwouters@redhat.com> - 0.5.1-1
- Updated to 0.5.1

* Fri Sep 04 2015 Paul Wouters <pwouters@redhat.com> - 0.3.2-2
- Workaround for broken --with-getdns_query option
- Adds the getdns_query tool

* Fri Sep 04 2015 Paul Wouters <pwouters@redhat.com> - 0.3.2-1
- Updated to 0.3.2 with bugfix for fallback handling of stateful transports

* Sun Aug 23 2015 Paul Wouters <pwouters@redhat.com> - 0.3.1-1
- Updated to 0.3.1 Fix repeating rdata fields

* Fri Jul 17 2015 Paul Wouters <pwouters@redhat.com> - 0.3.0-1
- updated to 0.3.0 with bugfixes DNS parameter updates and API update

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Mon May 25 2015 Paul Wouters <pwouters@redhat.com> - 0.2.0-1
- Updated to 0.2.0 which includes full DNS over TLS support
- Updated spurious execute bit fixes
- Added explicit --with-* lines to make dependancies clear

* Mon Jan 19 2015 Paul Wouters <pwouters@redhat.com> - 0.1.6-1
- Updated to 0.1.6 with minor bugfixes
- Remove spurious execute bits from some *.[ch] files

* Fri Oct 31 2014 Paul Wouters <pwouters@redhat.com> - 0.1.5-1
- Updated to 0.1.5 with bugfixes and persistent TCP connections
- Example code moved into spec/

* Sat Aug 16 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Wed Jul 02 2014 Paul Wouters <pwouters@redhat.com> - 0.1.3-1
- Updated to 0.1.3

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Thu May 22 2014 Paul Wouters <pwouters@redhat.com> - 0.1.1-2
- Build with libevent support

* Wed Mar 26 2014 Paul Wouters <pwouters@redhat.com> - 0.1.1-1
- Updated to 0.1.1

* Fri Mar 21 2014 Paul Wouters <pwouters@redhat.com> - 0.1.0-2
- Remove cleaning in install
- Simplify files section and use macro instead of /var/lib

* Thu Feb 27 2014 Paul Wouters <pwouters@redhat.com> - 0.1.0-1
- Initial package
