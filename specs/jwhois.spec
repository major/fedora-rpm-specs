%{?!with_cache: %global with_cache 0}

Name: jwhois
Version: 4.0
Release: 80%{?dist}
URL: http://www.gnu.org/software/jwhois/
Source0: ftp://ftp.gnu.org/gnu/jwhois/jwhois-%{version}.tar.gz
Source1: https://raw.githubusercontent.com/robert-scheck/jwhois/2bd561e06ca37cf6c2ef9f0a2e957e09f58e6972/example/jwhois.conf
Patch0: jwhois-4.0-connect.patch
Patch1: jwhois-4.0-ipv6match.patch
Patch2: jwhois-4.0-fclose.patch
Patch3: jwhois-4.0-select.patch
Patch5: jwhois-4.0-multi-homed.patch
Patch6: jwhois-4.0-libidn2.patch
Patch7: jwhois-4.0-idna.patch
Patch8: jwhois-4.0-idnfail.patch
# Patch9: adds options to force querying on ipv4 or ipv6, see rhbz#1551215
Patch9: jwhois-4.0-ipv4_ipv6.patch
Patch10: jwhois-configure-c99.patch
Patch11: jwhois-c99.patch
Patch12: jwhois-4.0-gcc15-fix.patch
License: GPL-3.0-only
Summary: Internet whois/nicname client
BuildRequires: gcc, libidn2-devel, autoconf, automake
%if %{with_cache}
BuildRequires: gdbm-devel
%endif
BuildRequires: make
%if 0%{?rhel} && 0%{?rhel} <= 7
Requires(post): /sbin/install-info
Requires(preun): /sbin/install-info
%endif
Requires(post): %{_sbindir}/update-alternatives
Requires(preun): %{_sbindir}/update-alternatives

%global genname whois
%global alternative jwhois

%description
A whois client that accepts both traditional and finger-style queries.

%prep
%setup -q
%autopatch -p1

iconv -f iso-8859-1 -t utf-8 < doc/sv/jwhois.1 > doc/sv/jwhois.1_
mv doc/sv/jwhois.1_ doc/sv/jwhois.1

cp -pf %{SOURCE1} example/jwhois.conf

autoreconf

%build
%if %{with_cache}
%configure --enable-sgid --localstatedir=%{_localstatedir}/cache/jwhois
%else
%configure
%endif
make %{?_smp_mflags}

%install
rm -fr $RPM_BUILD_ROOT
make install DESTDIR="$RPM_BUILD_ROOT"

%if %{with_cache}
echo 'cachefile = "/var/cache/jwhois/jwhois.db";' >> $RPM_BUILD_ROOT/etc/jwhois.conf
install -m0775 -d $RPM_BUILD_ROOT/%{_localstatedir}/cache/jwhois
touch $RPM_BUILD_ROOT/%{_localstatedir}/cache/jwhois/jwhois.db
%endif

rm -f "$RPM_BUILD_ROOT"%{_infodir}/dir
%find_lang jwhois

# Make "whois.{%%alternative}" jwhois (because of localized manual pages).
echo .so man1/jwhois.1 > $RPM_BUILD_ROOT/%{_mandir}/man1/whois.%{alternative}.1

# Rename to alternative names
touch $RPM_BUILD_ROOT%{_bindir}/whois
chmod 755 $RPM_BUILD_ROOT%{_bindir}/whois
touch $RPM_BUILD_ROOT%{_mandir}/man1/whois.1

%files -f %{name}.lang
%doc AUTHORS COPYING ChangeLog NEWS README TODO
%if %{with_cache}
%attr(2755,root,jwhois) %{_bindir}/jwhois
%attr(2775,root,jwhois) %{_localstatedir}/cache/jwhois/jwhois.db
%else
%attr(0755,root,root) %{_bindir}/jwhois
%endif
%ghost %verify(not md5 size mtime) %{_bindir}/whois
%{_mandir}/man1/jwhois.1*
%lang(sv) %{_mandir}/sv/man1/jwhois.1*
%{_mandir}/man1/whois.%{alternative}.*
%ghost %verify(not md5 size mtime) %{_mandir}/man1/whois.1.gz
%{_infodir}/jwhois.info.*
%config(noreplace) %{_sysconfdir}/jwhois.conf

%if %{with_cache}
%pre
getent group jwhois >/dev/null || groupadd -r jwhois || :
%endif

%post
%if 0%{?rhel} && 0%{?rhel} <= 7
if [ -f %{_infodir}/jwhois.info ]; then # --excludedocs?
    /sbin/install-info %{_infodir}/jwhois.info %{_infodir}/dir || :
fi
%endif
rm -f /usr/share/man/man1/whois.1.gz
%{_sbindir}/update-alternatives \
    --install %{_bindir}/whois \
        %{genname} %{_bindir}/jwhois 60 \
    --slave %{_mandir}/man1/whois.1.gz \
        %{genname}-man %{_mandir}/man1/whois.%{alternative}.1.gz

%preun
if [ $1 = 0 ]; then
%if 0%{?rhel} && 0%{?rhel} <= 7
    if [ -f %{_infodir}/jwhois.info ]; then # --excludedocs?
        /sbin/install-info --delete %{_infodir}/jwhois.info %{_infodir}/dir || :
    fi
%endif
    %{_sbindir}/update-alternatives --remove \
            %{genname} %{_bindir}/jwhois
fi

%changelog
* Tue Jan 21 2025 Vitezlsav Crhonek <vcrhonek@redhat.com> - 4.0-80
- Fix FTBFS with GCC 15

* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 4.0-79
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 4.0-78
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Wed Jan 24 2024 Fedora Release Engineering <releng@fedoraproject.org> - 4.0-77
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sat Jan 20 2024 Fedora Release Engineering <releng@fedoraproject.org> - 4.0-76
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 4.0-75
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu May 25 2023 Vitezslav Crhonek <vcrhonek@redhat.com> - 4.0-74
- SPDX migration

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 4.0-73
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Tue Jan 10 2023 Florian Weimer <fweimer@redhat.com> - 4.0-72
- C99 compatibility fixes

* Thu Dec 29 2022 Tommy Surbakti <tommy@surbakti.net> - 4.0-71
- Update jwhois.conf for .id ccTLD

* Fri Nov 25 2022 Vitezslav Crhonek <vcrhonek@redhat.com> - 4.0-70
- Fix incorrectly provided whois server for gov.uk in Jisc UK jwhois.conf update

* Mon Nov 21 2022 Vitezslav Crhonek <vcrhonek@redhat.com> - 4.0-69
- Jisc UK jwhois.conf updates

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 4.0-68
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 4.0-67
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Nov 03 2021 Vitezslav Crhonek <vcrhonek@redhat.com> - 4.0-66
- Update jwhois.conf for gov.wales, gov.scot and llyw.cymru (patch by Alex Dutton)
  Resolves: #2018000

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 4.0-65
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 4.0-64
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 4.0-63
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 4.0-62
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Tue Jan 21 2020 Vitezslav Crhonek <vcrhonek@redhat.com> - 4.0-61
- Update jwhois.conf for 151.0.0.0/8
  Resolves: #1683613

* Mon Sep 16 2019 Vitezslav Crhonek <vcrhonek@redhat.com> - 4.0-60
- Update jwhois.conf for .in (patch by William E Little Jr)
  Resolves: #1740284

* Mon Sep 16 2019 Vitezslav Crhonek <vcrhonek@redhat.com> - 4.0-59
- Update jwhois.conf for .ai (patch by Steeve McCauley)
  Resolves: #1751306

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 4.0-58
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Wed Apr 24 2019 Björn Esser <besser82@fedoraproject.org> - 4.0-57
- Remove hardcoded gzip suffix from GNU info pages

* Thu Feb 21 2019 Vitezslav Crhonek <vcrhonek@redhat.com> - 4.0-56
- Fix jwhois freezes on some requests
  Resolves: #1641563

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 4.0-55
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 4.0-54
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Mar 15 2018 Vitezslav Crhonek <vcrhonek@redhat.com> - 4.0-53
- Add options to to force querying on ipv4 or ipv6 (patch by John Fawcett)

* Wed Feb 21 2018 Vitezslav Crhonek <vcrhonek@redhat.com> - 4.0-52
- Add BuildRequires gcc
- Escape macro in comment, remove Group tag

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 4.0-51
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 4.0-50
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 4.0-49
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 4.0-48
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Aug 08 2016 Vitezslav Crhonek <vcrhonek@redhat.com> - 4.0-47
- Fix segfault when /etc/jwhois.conf is not accessible (patch by Christopher Arnold)

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 4.0-46
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Tue Jan 26 2016 Vitezslav Crhonek <vcrhonek@redhat.com> - 4.0-45
- Replace 'define' with 'global'
- Fix jwhois updates complain "failed to link ..." (patch by Michal Jaegermann)
  Resolves: #1298383

* Tue Dec 29 2015 Robert Scheck <robert@fedoraproject.org> - 4.0-44
- Update jwhois.conf from GitHub

* Sat Sep 12 2015 Robert Scheck <robert@fedoraproject.org> - 4.0-43
- Update jwhois.conf from GitHub
- Fixed IDNA 2008 support by running autoreconf

* Sun Aug 02 2015 Robert Scheck <robert@fedoraproject.org> - 4.0-42
- Update jwhois.conf from GitHub

* Tue Jul 14 2015 Robert Scheck <robert@fedoraproject.org> - 4.0-41
- Update jwhois.conf from GitHub (#1239078)

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.0-40
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Feb 21 2015 Till Maas <opensource@till.name> - 4.0-39
- Rebuilt for Fedora 23 Change
  https://fedoraproject.org/wiki/Changes/Harden_all_packages_with_position-independent_code

* Mon Sep 08 2014 Vitezslav Crhonek <vcrhonek@redhat.com> - 4.0-38
- Update jwhois.conf for .brussels and .vlaanderen

* Sat Aug 16 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.0-37
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Mon Jul 21 2014 Vitezslav Crhonek <vcrhonek@redhat.com> - 4.0-36
- Fix whois server for the 43.0.0.0/8 block
  Resolves: #1121512

* Tue Jun 10 2014 Vitezslav Crhonek <vcrhonek@redhat.com> - 4.0-35
- Add IDNA 2008 support (patch by Robert Scheck)
  Resolves: #1098785
- Update whois server for .id domain
  Resolves: #1106460
- Add whois servers for .tips and .guru domains
- Merge all config file updates into one patch
- Fix patch adding fallback to original text if IDN conversion fails
  because label is longer than 63 characters

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.0-34
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Tue Apr 29 2014 Vitezslav Crhonek <vcrhonek@redhat.com> - 4.0-33
- Fix jwhois does not fallback to original text if IDN conversion fails
  (patch by Martin Poole)

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.0-32
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.0-31
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.0-30
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.0-29
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue May 24 2011 Vitezslav Crhonek <vcrhonek@redhat.com> - 4.0-28
- Minor fix in IDN encoding patch
  Resolves: #682841
- Update jwhois.conf (various IDN TLDs missing, some changed ccTLD whois
  servers and charsets, patch by Robert Scheck)
  Resolves: #706771

* Tue Mar 29 2011 Vitezslav Crhonek <vcrhonek@redhat.com> - 4.0-27
- Fix /usr/bin/jwhois to be non-writable by group
  Resolves: #690604

* Tue Mar 15 2011 Vitezslav Crhonek <vcrhonek@redhat.com> - 4.0-26
- Fix IDN encoding failed with error code 5
  Resolves: #682841

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.0-25
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Mon Dec 20 2010 Vitezslav Crhonek <vcrhonek@redhat.com> - 4.0-24
- Update jwhois.conf for .ae domains and dotEmarat extension

* Tue Nov  9 2010 Petr Pisar <ppisar@redhat.com> - 4.0-23
- Alternate jwhois as whois
- Disable cache (it was accidentally enabled by default)

* Wed Sep 29 2010 Vitezslav Crhonek <vcrhonek@redhat.com> - 4.0-22
- Fix jwhois does not handle multi-homed server
  Resolves: #624608

* Tue Jun 22 2010 Vitezslav Crhonek <vcrhonek@redhat.com> - 4.0-21
- Update server options for whois.1api.net
  Resolves: #600096
- Merge all jwhois.conf updates into one patch

* Thu Apr 22 2010 Vitezslav Crhonek <vcrhonek@redhat.com> - 4.0-20
- Modify spec file to make easy possible to enable cache
  Resolves: #551131

* Tue Jan 26 2010 Vitezslav Crhonek <vcrhonek@redhat.com> - 4.0-19
- Use select to wait for input (patch by Joshua Roys <joshua.roys@gtri.gatech.edu>)
  Resolves: #469412

* Thu Sep  3 2009 Vitezslav Crhonek <vcrhonek@redhat.com> - 4.0-18
- Fix errors installing jwhois with --excludedocs
  Resolves: #515940

* Sun Aug 16 2009 Robert Scheck <robert@fedoraproject.org> - 4.0-17
- Update jwhois.conf for .edu.ar, .bs, .by, .dk, .name, .ng, .ps,
  .sg, .sl, .sv, .co.zw domains and handles from .name and .aero

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.0-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Sun May 03 2009 Robert Scheck <robert@fedoraproject.org> - 4.0-15
- Update jwhois.conf for .al, .cu, .my and .so domains

* Thu Apr 23 2009 Vitezslav Crhonek <vcrhonek@redhat.com> - 4.0-14
- Update jwhois.conf to expect UTF-8 answer charset from whois.dotster.com
  Resolves: #496015

* Fri Mar 13 2009 Vitezslav Crhonek <vcrhonek@redhat.com> - 4.0-13
- jwhois.conf update for another few domains
  Resolves: #489161

* Fri Feb 27 2009 Vitezslav Crhonek <vcrhonek@redhat.com> - 4.0-12
- Large jwhois.conf update
  Resolves: #48677{3,4,5,6,8}, #48678{0,2-9}, #48679{0-9}
  Resolves: #48680{0-3}, #48682{2,3,7}, #48683{0,2-5,7-9}
  Resolves: #48684{0,2,3,5,7,8}, #48685{0,3,7}, #486862

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.0-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Wed Feb  4 2009 Vitezslav Crhonek <vcrhonek@redhat.com> - 4.0-10
- Close config file descriptor when finished reading the config file
- Add support for ENUM domains into jwhois.conf
  Resolves: #465182

* Fri Jan 23 2009 Vitezslav Crhonek <vcrhonek@redhat.com> - 4.0-9
- Change the server used for .gi domains

* Mon Oct 13 2008 Vitezslav Crhonek <vcrhonek@redhat.com> - 4.0-8
- Update to latest upstream config
  Resolves: #463972

* Mon Feb 11 2008 Vitezslav Crhonek <vcrhonek@redhat.com> - 4.0-7
- Rebuild

* Thu Dec  6 2007 Vitezslav Crhonek <vcrhonek@redhat.com> - 4.0-6
- Fix buildroot
- Fix matching of cidr-ipv6 network addressed (patch by Lubomir
  Kundrak <lkundrak@redhat.com>)
  Resolves: #280941

* Wed Nov 28 2007 Vitezslav Crhonek <vcrhonek@redhat.com> - 4.0-5
- Merge review: add _smp_mflag, remove RPM_BUILD_ROOT test in istall
  and clean, remove Obsoletes:, fix use of %% in changelog
  Resolves: #225955

* Tue Nov 20 2007 Lubomir Kundrak <lkundrak@redhat.com> - 4.0-4
- Fix connections to IPv4 servers

* Tue Oct  9 2007 Vitezslav Crhonek <vcrhonek@redhat.com> - 4.0-3
- Fix localized man pages not marked with %%lang (patch by Ville
  Skyttä <ville.skytta@iki.fi>)

* Tue Aug 28 2007 Vitezslav Crhonek <vcrhonek@redhat.com> - 4.0-2
- Fix license
- Rebuild

* Mon Jul  2 2007 Vitezslav Crhonek <vcrhonek@redhat.com> - 4.0-1
- Update to 4.0 (#246455)

* Fri Mar 23 2007 Vitezslav Crhonek <vcrhonek@redhat.com> - 3.2.3-11
- Change the server used for .se domains to whois.iis.se (patch by Johan
  Sare <johansare@gmail.com>)
  Resolves: #233207

* Sat Jan  6 2007 Miloslav Trmac <mitr@redhat.com> - 3.2.3-10
- Add automatic redirection for .com and .net domains (patch by Wolfgang
  Rupprecht <wsr+redhatbugzilla@wsrcc.com>)
  Resolves: #221668
- Update to upstream config as of Jan 6 2007

* Fri Jan  5 2007 Miloslav Trmac <mitr@redhat.com> - 3.2.3-9
- Ignore install-info errors in scriptlets
- Remove the trailing dot from Summary:

* Tue Oct 31 2006 Miloslav Trmac <mitr@redhat.com> - 3.2.3-8
- Actually use the new upstream config in non-rawhide branches

* Tue Oct 31 2006 Miloslav Trmac <mitr@redhat.com> - 3.2.3-7
- Backport IDN support
  Resolves: #205033
- Update to upstream config as of Oct 31 2006

* Wed Jul 12 2006 Jesse Keating <jkeating@redhat.com> - 3.2.3-6.1
- rebuild

* Tue May 16 2006 Miloslav Trmac <mitr@redhat.com> - 3.2.3-6
- Fix some uninitialized memory accesses
- Fix a typo in the ipv6 patch

* Mon May 15 2006 Miloslav Trmac <mitr@redhat.com> - 3.2.3-5
- Update to upstream config as of May 15 2006 (#191291)
- Add more IPv6 address ranges (#191290, original patch by Peter Bieringer)

* Wed Apr 19 2006 Miloslav Trmac <mitr@redhat.com> - 3.2.3-4
- Update to upstream config as of Apr 19 2006 (#188366)

* Fri Feb 10 2006 Jesse Keating <jkeating@redhat.com> - 3.2.3-3.2.1
- bump again for double-long bug on ppc(64)

* Tue Feb 07 2006 Jesse Keating <jkeating@redhat.com> - 3.2.3-3.2
- rebuilt for new gcc4.1 snapshot and glibc changes

* Fri Dec 09 2005 Jesse Keating <jkeating@redhat.com>
- rebuilt

* Fri Nov 11 2005 Miloslav Trmac <mitr@redhat.com> - 3.2.3-3
- Ship ChangeLog

* Fri Aug  5 2005 Miloslav Trmac <mitr@redhat.com> - 3.2.3-2
- Don't die on SIGPIPE if a browser is not present, improve the error message
  (#165149)

* Mon Aug  1 2005 Miloslav Trmac <mitr@redhat.com> - 3.2.3-1
- Update to jwhois-3.2.3
- Don't compress jwhois.info manually

* Sun Jun 12 2005 Miloslav Trmac <mitr@redhat.com> - 3.2.2-16
- Remove 'fuzzy' from ru.po header to make charset conversion work (#160165)

* Sat Jun 11 2005 Miloslav Trmac <mitr@redhat.com> - 3.2.2-15
- Update to upstream config as of Jun 11 2005, remove patches accepted upstream

* Sat Apr 30 2005 Miloslav Trmac <mitr@redhat.com> - 3.2.2-14
- Add an AfriNIC range (#156178)

* Mon Apr 11 2005 Miloslav Trmac <mitr@redhat.com> - 3.2.2-13
- Update to upstream config as of Apr 11 2005 (get results in English 
  from whois.nic.ad.jp)

* Wed Mar 23 2005 Miloslav Trmac <mitr@redhat.com> - 3.2.2-12
- Update to upstream CVS config as of Mar 23 2005 (#151900)
  Remove now unnecessary typos.patch

* Fri Mar  4 2005 Miloslav Trmac <mitr@redhat.com> - 3.2.2-11
- Rebuild with gcc 4

* Sun Feb 20 2005 Miloslav Trmac <mitr@redhat.com> - 3.2.2-10
- Update to upstream CVS config as of Feb 10 2005 (#147562);
  Remove now unecessary denic.patch, update update_2004.patch
- Fix .cd, .gi, .io (#146613, patch by Robert Scheck)

* Sun Jan  2 2005 Miloslav Trmac <mitr@redhat.com> - 3.2.2-9
- Add IPv6 address ranges, fix .pro, 223.0.0.0/8 (#143682, patch by Robert
  Scheck)

* Sat Nov 20 2004 Miloslav Trmac <mitr@redhat.com> - 3.2.2-8
- Convert Swedish man page to UTF-8

* Mon Nov  1 2004 Miloslav Trmac <mitr@redhat.com> - 3.2.2-7
- Fix double free (#137693)

* Mon Sep 13 2004 Miloslav Trmac <mitr@redhat.com> - 3.2.2-6
- Recognize more redirections at whois.arin.net (#116423)

* Mon Sep 13 2004 Miloslav Trmac <mitr@redhat.com> - 3.2.2-5
- Update config file for .de (#132362, by Robert Scheck)

* Tue Jun 15 2004 Elliot Lee <sopwith@redhat.com>
- rebuilt

* Fri Feb 13 2004 Elliot Lee <sopwith@redhat.com>
- rebuilt

* Wed Jan  7 2004 Nalin Dahyabhai <nalin@redhat.com> 3.2.2-2
- fix typos in jwhois.conf (#113012)

* Fri Jul 04 2003 Florian La Roche <Florian.LaRoche@redhat.de>
- new upstream version 3.2.2

* Wed Jun 04 2003 Elliot Lee <sopwith@redhat.com>
- rebuilt

* Sun Feb 02 2003 Florian La Roche <Florian.LaRoche@redhat.de>
- update to 3.2.1

* Thu Jan 30 2003 Nalin Dahyabhai <nalin@redhat.com> 3.2.0-6
- search whois.publicinternetregistry.net instead of whois.internic.net for
  all '.org$' domains (#82802).

* Wed Jan 22 2003 Tim Powers <timp@redhat.com> 3.2.0-5
- rebuilt

* Thu Dec 12 2002 Karsten Hopp <karsten@redhat.de> 3.2.0-4
- Requires(post,preun) doesn't seem to work properly

* Wed Nov 20 2002 Florian La Roche <Florian.LaRoche@redhat.de> 3.2.0-3
- require install-info

* Thu Nov 14 2002 Nalin Dahyabhai <nalin@redhat.com> 3.2.0-2
- don't bail out of %%install if make install doesn't create an info top node

* Mon Sep 30 2002 Nalin Dahyabhai <nalin@redhat.com> 3.2.0-1
- initial package
