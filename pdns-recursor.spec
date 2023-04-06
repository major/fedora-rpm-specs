%ifarch %{ix86} armv7hl
%global _lto_cflags %{nil}
%endif

Name: pdns-recursor
Version: 4.8.4
Release: 1%{?dist}
Summary: Modern, advanced and high performance recursing/non authoritative name server
License: GPLv2
URL: https://powerdns.com
Source0: https://downloads.powerdns.com/releases/%{name}-%{version}.tar.bz2
ExcludeArch: %{arm} %{ix86}

Provides: powerdns-recursor = %{version}-%{release}
BuildRequires: make
BuildRequires: boost-devel
BuildRequires: gcc-c++
%ifarch %{arm} %{ix86} x86_64 %{mips} aarch64
BuildRequires: luajit-devel
%else
BuildRequires: lua-devel
%endif
%ifarch ppc64 ppc64le
BuildRequires: libatomic
%endif
BuildRequires: libcap-devel
BuildRequires: fstrm-devel
BuildRequires: openssl-devel
BuildRequires: systemd
BuildRequires: systemd-devel
BuildRequires: protobuf-devel
BuildRequires: hostname
BuildRequires: libsodium-devel
BuildRequires: autoconf
BuildRequires: automake
BuildRequires: libtool

Requires(pre): shadow-utils
Requires(post): systemd
Requires(preun): systemd
Requires(postun): systemd


%description
PowerDNS Recursor is a non authoritative/recursing DNS server. Use this
package if you need a dns cache for your network.


%prep
%autosetup -n %{name}-%{version}

%build
%configure \
    --sysconfdir=%{_sysconfdir}/%{name} \
    --with-libsodium \
    --enable-reproducible \
    --enable-dnstap \
    --enable-dns-over-tls \
%ifarch %{arm} %{ix86} x86_64 %{mips} aarch64
    --with-lua=luajit \
%else
    --with-lua \
%endif
    --with-socketdir=%{_rundir}

make %{?_smp_mflags}


%install
make install DESTDIR=%{buildroot}

%{__mv} %{buildroot}%{_sysconfdir}/%{name}/recursor.conf{-dist,}

# add directories for newly-observed-domains/unique-domain-response
install -p -d -m 0755 %{buildroot}/%{_sharedstatedir}/%{name}/nod
install -p -d -m 0755 %{buildroot}/%{_sharedstatedir}/%{name}/udr

# change user and group to pdns-recursor
sed -i \
    -e 's/# setuid=/setuid=pdns-recursor/' \
    -e 's/# setgid=/setgid=pdns-recursor/' \
    -e 's/# security-poll-suffix=secpoll\.powerdns\.com\./security-poll-suffix=/' \
    %{buildroot}%{_sysconfdir}/%{name}/recursor.conf


%pre
getent group pdns-recursor > /dev/null || groupadd -r pdns-recursor
getent passwd pdns-recursor > /dev/null || \
    useradd -r -g pdns-recursor -d / -s /sbin/nologin \
    -c "PowerDNS Recursor user" pdns-recursor
exit 0


%post
%systemd_post pdns-recursor.service


%preun
%systemd_preun pdns-recursor.service


%postun
%systemd_postun_with_restart pdns-recursor.service


%files
%{_bindir}/rec_control
%{_sbindir}/pdns_recursor
%{_mandir}/man1/pdns_recursor.1.gz
%{_mandir}/man1/rec_control.1.gz
%{_unitdir}/pdns-recursor.service
%{_unitdir}/pdns-recursor@.service
%dir %{_sysconfdir}/%{name}
%config(noreplace) %{_sysconfdir}/%{name}/recursor.conf
%dir %attr(0755,pdns-recursor,pdns-recursor) %{_sharedstatedir}/%{name}
%dir %attr(0755,pdns-recursor,pdns-recursor) %{_sharedstatedir}/%{name}/nod
%dir %attr(0755,pdns-recursor,pdns-recursor) %{_sharedstatedir}/%{name}/udr
%doc README
%license COPYING


%changelog
* Tue Apr 04 2023 Morten Stevens <mstevens@fedoraproject.org> - 4.8.4-1
- Update to 4.8.4

* Mon Feb 20 2023 Jonathan Wakely <jwakely@redhat.com> - 4.7.2-3
- Rebuilt for Boost 1.81

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 4.7.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Tue Aug 23 2022 Sander Hoentjen <sander@hoentjen.eu> - 4.7.2-1
- Update to 4.7.2 (#2120543)

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 4.7.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Sat Jul 09 2022 Sander Hoentjen <sander@hoentjen.eu> - 4.7.1-1
- Update to 4.7.1 (#2105225)

* Mon May 30 2022 Sander Hoentjen <sander@hoentjen.eu> - 4.7.0-1
- Update to 4.7.0

* Thu May 12 2022 Sander Hoentjen <sander@hoentjen.eu> - 4.7.0~rc1-1
- Update to 4.7.0-rc1
- enable DoT (DNS over TLS)

* Wed May 04 2022 Thomas Rodgers <trodgers@redhat.com> - 4.7.0~beta1-2
- Rebuilt for Boost 1.78

* Sat Apr 30 2022 Sander Hoentjen <sander@hoentjen.eu> - 4.7.0~beta1-1
- Update to 4.7.0-beta1

* Sun Apr 10 2022 Morten Stevens <mstevens@fedoraproject.org> - 4.6.2-1
- Update to 4.6.2

* Thu Feb 10 2022 Morten Stevens <mstevens@fedoraproject.org> - 4.6.0-1
- Update to 4.6.0

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 4.5.4-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Tue Sep 14 2021 Sahana Prasad <sahana@redhat.com> - 4.5.4-4
- Rebuilt with OpenSSL 3.0.0

* Sat Aug 07 2021 Jonathan Wakely <jwakely@redhat.com> - 4.5.4-3
- Rebuilt for Boost 1.76

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 4.5.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 25 2021 Ruben Kerkhof <ruben@rubenkerkhof.com> - 4.5.4-1
- Upstream released new version
  See https://doc.powerdns.com/recursor/changelog/4.5.html#change-4.5.4 for more details

* Thu Jun 24 2021 Ruben Kerkhof <ruben@rubenkerkhof.com> - 4.5.2-1
- Upstream released new version
  See https://doc.powerdns.com/recursor/changelog/4.5.html#change-4.5.2 for more details
- Disable builds on 32-bit arches as announced in https://mailman.powerdns.com/pipermail/pdns-users/2021-May/027218.html

* Tue Mar 02 2021 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 4.4.2-6
- Rebuilt for updated systemd-rpm-macros
  See https://pagure.io/fesco/issue/2583.

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 4.4.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Fri Jan 22 2021 Jonathan Wakely <jwakely@redhat.com> - 4.4.2-4
- Rebuilt for Boost 1.75

* Wed Jan 13 16:40:52 CET 2021 Adrian Reber <adrian@lisas.de> - 4.4.2-3
- Rebuilt for protobuf 3.14

* Sun Dec 27 2020 Ruben Kerkhof <ruben@rubenkerkhof.com> - 4.4.2-2
- Disable LTO on i686 and armv7hl to work around build failure

* Sat Dec 26 2020 Ruben Kerkhof <ruben@rubenkerkhof.com> - 4.4.2-1
- Upstream released new version
  See https://doc.powerdns.com/recursor/changelog/4.4.html#change-4.4.2 for more details

* Mon Oct 19 2020 Morten Stevens <mstevens@fedoraproject.org> - 4.3.5-1
- Update to 4.3.5
- Fixes CVE-2020-25829

* Thu Sep 24 2020 Adrian Reber <adrian@lisas.de> - 4.3.4-2
- Rebuilt for protobuf 3.13

* Tue Sep 08 2020 Morten Stevens <mstevens@fedoraproject.org> - 4.3.4-1
- Update to 4.3.4

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 4.3.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Sun Jun 14 2020 Adrian Reber <adrian@lisas.de> - 4.3.1-2
- Rebuilt for protobuf 3.12

* Wed Jun 03 2020 Ruben Kerkhof <ruben@rubenkerkhof.com> - 4.3.1-1
- Upstream released new version
  Fixes CVE-2020-10995, CVE-2020-12244 and CVE-2020-10030
  See https://doc.powerdns.com/recursor/changelog/4.3.html#change-4.3.1 for more details

* Tue Mar 03 2020 Ruben Kerkhof <ruben@rubenkerkhof.com> - 4.3.0-0.5
- Upstream released new version
  See https://blog.powerdns.com/2020/03/03/powerdns-recursor-4-3-0-released/ for more details

* Fri Feb 21 2020 Ruben Kerkhof <ruben@rubenkerkhof.com> - 4.3.0-0.4rc2
- Update to 4.3.0 rc2
- Fix build with gcc 10

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 4.3.0-0.3beta2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Mon Jan 20 2020 Ruben Kerkhof <ruben@rubenkerkhof.com> - 4.3.0-0.2beta2
- Update to 4.3.0 beta2

* Tue Dec 31 2019 Ruben Kerkhof <ruben@rubenkerkhof.com> - 4.3.0-0.2beta1
- Update to 4.3.0 beta1

* Thu Dec 19 2019 Orion Poplawski <orion@nwra.com> - 4.3.0-0.2alpha3
- Rebuild for protobuf 3.11

* Wed Oct 30 2019 Ruben Kerkhof <ruben@rubenkerkhof.com> - 4.3.0-0.1alpha3
- Update to 4.3.0 alpha3
- Newly observed domains support enabled by default (#1748887)
- Add support for dnstap

* Fri Aug 02 2019 Morten Stevens <mstevens@fedoraproject.org> - 4.2.0-3
- Fix for s390x (https://github.com/PowerDNS/pdns/pull/7951)

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 4.2.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Jul 20 2019 Morten Stevens <mstevens@fedoraproject.org> - 4.2.0-1
- Update to 4.2.0

* Mon May 13 2019 Ruben Kerkhof <ruben@rubenkerkhof.com> - 4.1.12-1
- Upstream released new version
  See https://doc.powerdns.com/recursor/changelog/4.1.html#change-4.1.12 for changes

* Thu Feb 28 2019 Ruben Kerkhof <ruben@rubenkerkhof.com> - 4.1.11-1
- Upstream released new version

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 4.1.9-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jan 25 2019 Jonathan Wakely <jwakely@redhat.com> - 4.1.9-2
- Rebuilt for Boost 1.69

* Thu Jan 24 2019 Ruben Kerkhof <ruben@rubenkerkhof.com> - 4.1.9-1
- Update to new upstream
- Fixes CVE-2019-3807 and CVE-2019-3806

* Wed Nov 28 2018 Ruben Kerkhof <ruben@rubenkerkhof.com> - 4.1.8-1
- Update to new upstream
- Fixes CVE-2018-16855

* Tue Nov 13 2018 Sander Hoentjen <sander@hoentjen.eu> - 4.1.7-1
- Update to new upstream
- Fixes CVE-2018-10851, CVE-2018-14626 and CVE-2018-14644

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 4.1.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu May 24 2018 Ruben Kerkhof <ruben@rubenkerkhof.com> - 4.1.3-2
- Fix sigabort (#1578732)

* Wed May 23 2018 Ruben Kerkhof <ruben@rubenkerkhof.com> - 4.1.3-1
- Upstream released new version
- Enable support for ed25519

* Mon Feb 19 2018 Ruben Kerkhof <ruben@rubenkerkhof.com> - 4.1.1-4
- BuildRequire gcc-c++ (https://fedoraproject.org/wiki/Packaging:C_and_C%2B%2B#BuildRequire)

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 4.1.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Tue Jan 23 2018 Jonathan Wakely <jwakely@redhat.com> - 4.1.1-2
- Rebuilt for Boost 1.66

* Tue Jan 23 2018 Ruben Kerkhof <ruben@rubenkerkhof.com> - 4.1.1-1
- New upstream release
- Fixes CVE-2018-1000003

* Wed Nov 29 2017 Sander Hoentjen <sander@hoentjen.eu> - 4.0.7-1
- New upstream release
- fixes CVE-2017-15090, CVE-2017-15092, CVE-2017-15093 and CVE-2017-15094

* Wed Nov 29 2017 Igor Gnatenko <ignatenko@redhat.com> - 4.0.6-6
- Rebuild for protobuf 3.5

* Mon Nov 13 2017 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 4.0.6-5
- Rebuild for protobuf 3.4

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 4.0.6-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 4.0.6-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Jul 21 2017 Kalev Lember <klember@redhat.com> - 4.0.6-2
- Rebuilt for Boost 1.64

* Thu Jul 06 2017 Sander Hoentjen <sander@hoentjen.eu> - 4.0.6-1
- New upstream release

* Thu Jun 15 2017 Sander Hoentjen <sander@hoentjen.eu> - 4.0.5-3
- Fix building on ppc64* (patch is already upstream)

* Wed Jun 14 2017 Orion Poplawski <orion@cora.nwra.com> - 4.0.5-2
- Rebuild for protobuf 3.3.1

* Wed Jun 14 2017 Sander Hoentjen <sander@hoentjen.eu> - 4.0.5-1
- New upstream release

* Mon May 15 2017 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.0.4-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_27_Mass_Rebuild

* Mon Feb 06 2017 Kalev Lember <klember@redhat.com> - 4.0.4-4
- Rebuilt for Boost 1.63

* Tue Jan 31 2017 Sander Hoentjen <sander@hoentjen.eu> - 4.0.4-3
- Rebuild for protobuf 3.2.0

* Fri Jan 27 2017 Jonathan Wakely <jwakely@redhat.com> - 4.0.4-2
- Rebuilt for Boost 1.63

* Mon Jan 16 2017 Sander Hoentjen <sander@hoentjen.eu> - 4.0.4-1
- New upstream release
- Security fix for CVE-2016-2120, CVE-2016-7068, CVE-2016-7072, CVE-2016-7073, CVE-2016-7074

* Mon Nov 21 2016 Sander Hoentjen <sander@hoentjen.eu> - 4.0.3-2
- Rebuild for protobuf 3.1.0

* Wed Sep 07 2016 Ruben Kerkhof <ruben@rubenkerkhof.com> - 4.0.3-1
- Upstream released new version

* Tue Aug 30 2016 Sander Hoentjen <sander@hoentjen.eu> - 4.0.2-3
- luajit is now also available for aarch64 and MIPS

* Mon Aug 29 2016 Igor Gnatenko <ignatenko@redhat.com> - 4.0.2-2
- Rebuild for LuaJIT 2.1.0

* Sat Aug 27 2016 Sander Hoentjen <sander@hoentjen.eu> - 4.0.2-1
- New upstream release

* Tue Aug 23 2016 Dan Horák <dan[at]danny.cz> - 4.0.1-2
- luajit is available only on selected arches

* Fri Aug 19 2016 Ruben Kerkhof <ruben@rubenkerkhof.com> - 4.0.1-1
- Upstream released new version

* Thu Jul 14 2016 Sander Hoentjen <sander@hoentjen.eu> - 4.0.0-1
- Update to GA release
- enable systemd integration (BR: systemd-devel)
- add protobuf

* Sat Mar 12 2016 Sander Hoentjen <sander@hoentjen.eu> 4.0.0-0.5.alpha2
- Fix group in configuration
- disable secpoll
- with luajit

* Wed Mar 09 2016 Ruben Kerkhof <ruben@rubenkerkhof.com> - 4.0.0-0.4.alpha2
- Upstream released new version:
  http://blog.powerdns.com/2016/03/09/powerdns-recursor-4-0-0-alpha-2-released/
- Drop obsolete patches
- Cleanup the spec a bit

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 4.0.0-0.3.alpha1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Jan 15 2016 Jonathan Wakely <jwakely@redhat.com> - 4.0.0-0.2.alpha1
- Rebuilt for Boost 1.60

* Sun Dec 27 2015 Morten Stevens <mstevens@fedoraproject.org> - 4.0.0-0.1.alpha1
- Update to 4.0.0 (Technical Preview)
- Support for DNSSEC

* Thu Aug 27 2015 Jonathan Wakely <jwakely@redhat.com> - 3.7.3-5
- Rebuilt for Boost 1.59

* Wed Jul 29 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.7.3-4
- Rebuilt for https://fedoraproject.org/wiki/Changes/F23Boost159

* Wed Jul 22 2015 David Tardon <dtardon@redhat.com> - 3.7.3-3
- rebuild for Boost 1.58

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.7.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Wed Jun 10 2015 Morten Stevens <mstevens@fedoraproject.org> - 3.7.3-1
- Update to 3.7.3

* Mon Apr 27 2015 Morten Stevens <mstevens@fedoraproject.org> - 3.7.2-1
- Update to 3.7.2
- CVE-2015-1868

* Thu Feb 12 2015 Morten Stevens <mstevens@fedoraproject.org> - 3.7.1-1
- Update to 3.7.1
- Disable security status polling by default

* Tue Jan 27 2015 Petr Machata <pmachata@redhat.com> - 3.7.0-0.2.rc1
- Rebuild for boost 1.57.0

* Thu Jan 22 2015 Morten Stevens <mstevens@fedoraproject.org> - 3.7.0-0.1.rc1
- Update to 3.7.0-rc1

* Fri Oct 31 2014 Morten Stevens <mstevens@fedoraproject.org> - 3.6.2-1
- Update to 3.6.2
- Enable security status polling

* Wed Sep 10 2014 Morten Stevens <mstevens@fedoraproject.org> - 3.6.1-1
- Update to 3.6.1
- CVE-2014-3614 (#1139251)

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.6.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Fri Jun 20 2014 Morten Stevens <mstevens@fedoraproject.org> - 3.6.0-1
- Update to 3.6.0

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.6.0-0.2.rc1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Fri May 30 2014 Morten Stevens <mstevens@fedoraproject.org> - 3.6.0-0.1.rc1
- Update to 3.6.0-rc1

* Fri May 23 2014 Petr Machata <pmachata@redhat.com> - 3.5.3-3
- Rebuild for boost 1.55.0

* Mon Feb 10 2014 Morten Stevens <mstevens@fedoraproject.org> - 3.5.3-2
- Add upstream patch to fix rhbz#1063305

* Tue Sep 17 2013 Morten Stevens <mstevens@fedoraproject.org> - 3.5.3-1
- Update to 3.5.3

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.5.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Tue Jul 30 2013 Petr Machata <pmachata@redhat.com> - 3.5.2-3
- Rebuild for boost 1.54.0

* Mon Jun 17 2013 Morten Stevens <mstevens@fedoraproject.org> - 3.5.2-2
- Added support for lua 5.2

* Mon Jun 10 2013 Morten Stevens <mstevens@fedoraproject.org> - 3.5.2-1
- Update to 3.5.2

* Fri May 03 2013 Morten Stevens <mstevens@fedoraproject.org> - 3.5.1-1
- Update to 3.5.1

* Mon Apr 22 2013 Morten Stevens <mstevens@fedoraproject.org> - 3.5-2
- Disarm dead code that causes gcc crashes on ARM (rhbz#954192)

* Mon Apr 15 2013 Morten Stevens <mstevens@fedoraproject.org> - 3.5-1
- Update to 3.5
- Fixes CVE-2012-1193 and another variant of the attack (rhbz#794965)
- D.ROOT-SERVERS.NET has a new IP (rhbz#917347)

* Tue Apr 09 2013 Morten Stevens <mstevens@fedoraproject.org> - 3.5-0.3.rc5
- Update to 3.5-rc5

* Fri Apr 05 2013 Morten Stevens <mstevens@fedoraproject.org> - 3.5-0.2.rc4
- Update to 3.5-rc4

* Tue Mar 05 2013 Morten Stevens <mstevens@fedoraproject.org> - 3.5-0.1.rc2
- Update to 3.5-rc2

* Tue Mar 05 2013 Ruben Kerkhof <ruben@rubenkerkhof.com> - 3.3-10
- Enable hardened build as per http://fedoraproject.org/wiki/Packaging:Guidelines#PIE
- Fix bogus date in changelog
- Fix typo in gecos field
- Some rpmlint fixes

* Mon Feb 11 2013 Morten Stevens <mstevens@fedoraproject.org> - 3.3-9
- Enable PrivateTmp as per http://fedoraproject.org/wiki/Features/ServicesPrivateTmp

* Thu Sep 27 2012 Morten Stevens <mstevens@fedoraproject.org> - 3.3-8
- use new systemd rpm macros (rhbz#850267)
- Update systemd unit file

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.3-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Tue Feb 28 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.3-6
- Rebuilt for c++ ABI breakage

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.3-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Mon Sep 12 2011 Tom Callaway <spot@fedoraproject.org> - 3.3-4
- convert to systemd

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Wed Sep 29 2010 jkeating - 3.3-2
- Rebuilt for gcc bug 634757

* Sat Sep 25 2010 Ruben Kerkhof <ruben@rubenkerkhof.com> 3.3-1
- Upstream released new version: http://doc.powerdns.com/changelog.html

* Thu May 13 2010 Ruben Kerkhof <ruben@rubenkerkhof.com> 3.2-2
- Correct group name (bz #591214)

* Sun Mar 14 2010 Ruben Kerkhof <ruben@rubenkerkhof.com> 3.2-1
- Upstream released new version
- Adjust scriptlets to packaging guidelines

* Mon Mar 01 2010 Ruben Kerkhof <ruben@rubenkerkhof.com> 3.2-0.1.rc2
- Upstream released new version

* Wed Jan 06 2010 Ruben Kerkhof <ruben@rubenkerkhof.com> 3.1.7.2-1
- Upstream released new version
- Fixes CVE-2009-4009 and CVE-2009-4010

* Tue Nov 24 2009 Ruben Kerkhof <ruben@rubenkerkhof.com> 3.1.7.1-3
- Start recursor earlier in the boot process (#540428)

* Mon Aug 10 2009 Ruben Kerkhof <ruben@rubenkerkhof.com> - 3.1.7.1-2
- Re-add accidently dropped patch (#516562)

* Mon Aug 03 2009 Ruben Kerkhof <ruben@rubenkerkhof.com> - 3.1.7.1-1
- Upstream released new version
- Drop patches included upstream

* Sat Jul 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.1.7-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Fri Feb 27 2009 Ruben Kerkhof <ruben@rubenkerkhof.com> - 3.1.7-4
- Fix errors with newer Boost
- Fix build with gcc4.4

* Thu Feb 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.1.7-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Thu Jul 24 2008 Ruben Kerkhof <ruben@rubenkerkhof.com> - 3.1.7-2
- Use OPTFLAGS because CXXFLAGS overrides the defaults

* Thu Jul 24 2008 Ruben Kerkhof <ruben@rubenkerkhof.com> - 3.1.7-1
- Upstream released new version, now with Lua support

* Sun May 11 2008 Ruben Kerkhof <ruben@rubenkerkhof.com> - 3.1.6
- Upstream released new version

* Wed Apr 02 2008 Ruben Kerkhof <ruben@rubenkerkhof.com> - 3.1.5
- Upstream released new version

* Sat Feb 16 2008 Ruben Kerkhof <ruben@rubenkerkhof.com> - 3.1.5-0.1.snapshot4
- Snapshot 4
- Drop gcc 4.3 patch, fixed upstream

* Sat Feb 09 2008 Ruben Kerkhof <ruben@rubenkerkhof.com> - 3.1.5-0.1.snapshot3
- Sync with upstream
- Compile fixes for gcc43

* Sat Jan 27 2007 <ruben@rubenkerkhof.com> 3.1.4-4
- Now really fix the description in init script

* Sat Jan 27 2007 <ruben@rubenkerkhof.com> 3.1.4-3
- Fixed Description in init script

* Wed Jan 24 2007 <ruben@rubenkerkhof.com> 3.1.4-2
- Fixes per bz review 221188:
- Changed user to pdns-recursor
- Patched the Makefile to not strip debugsymbols
- Skipped the configure step, it didn't do much
- Added a more Fedora-centric initscript
- Use condrestart instead of restart in %%postun

* Sun Dec 31 2006 <ruben@rubenkerkhof.com> 3.1.4-1
- Initial import
