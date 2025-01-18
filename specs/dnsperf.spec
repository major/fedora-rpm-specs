%if 0%{?fedora} >= 29 || 0%{?rhel} > 7
%bcond_without python3
%bcond_with    python2
%else
%bcond_with    python3
%bcond_without python2
%endif

%global forgeurl0 https://github.com/DNS-OARC/dnsperf

Summary: Benchmarking authorative and recursing DNS servers
Name: dnsperf
Version: 2.12.0
Release: 7%{?dist}
# New page was found, but on github is also project, that seems to be official.
#
# Github project has different license and so far is the only one with any
# license mentioned. Unfortunately, project seems to be dead.
# It changed license text to Apache License 2.0
# Url: https://github.com/akamai/dnsperf
# License: ASL 2.0
#
# Another fork was maintained by ISC in contrib,
# now split into separate repository. This repository comes exactly from
# original nominum tarball, great source of patches.
# Url: https://gitlab.isc.org/isc-projects/dnsperf
#
# It seems DNS-OARC taken over the project, it has github page
# https://github.com/DNS-OARC/dnsperf

# Automatically converted from old format: ASL 2.0 - review is highly recommended.
License: Apache-2.0
Url: https://www.dns-oarc.net/tools/dnsperf
Vcs: git:%{forgeurl0}

# Deactivate GitHub sources, make web server official. Should be the same, but GitHub does not match checksums.
#Source: https://github.com/DNS-OARC/dnsperf/archive/v%%{version}/%%{name}-%%{version}.tar.gz
Source0: https://www.dns-oarc.net/files/dnsperf/%{name}-%{version}.tar.gz
Source2: dnsperf-data

BuildRequires: gcc, make
BuildRequires: autoconf automake libtool
BuildRequires: ldns-devel
BuildRequires: openssl-devel
BuildRequires: ck-devel
BuildRequires: libnghttp2-devel

%if %{with python3}
BuildRequires: python3-devel
%endif

%if 0%{?fedora} >= 27 || 0%{?rhel} >= 8
# resperf-report requires it, but not dnsperf itself
# do not force it always
Recommends: gnuplot
%else
Requires:   gnuplot
%endif
%if %{with python3}
BuildRequires: python3-devel
%endif

%if %{with python2}
BuildRequires: python2-devel
%endif

Provides: %{name}-data = %{version}-%{release}
Obsoletes: %{name}-data < 2.5.1-2

%description
This is dnsperf, a collection of DNS server performance testing tools.
For more information, see the dnsperf(1) and resperf(1) man pages.

%if %{with python2} || %{with python3}
%package queryparse
Summary: Pcap dns query extraction utility
BuildArch: noarch
# Required for license file
Requires: %{name} = %{version}-%{release}
%if %{with python3}
Requires: python3-pcapy python3-dns
%endif
%if %{with python2}
Requires: pcapy python2-dns
%endif

%description queryparse
This is dnsperf, a collection of DNS server performance testing tools.

Provides queryparse, python utility extracting queries from pcap files,
such as recorded by tcpdump or wireshark. Prints output in format
useable by dnsperf and resperf.

%endif

%prep
%autosetup -p1

%build
autoreconf -fi
%configure
%make_build

%if %{with python2}
%{__python3} %{_rpmconfigdir}/redhat/pathfix.py -i %{__python2} -p -n contrib/queryparse/queryparse
%endif
%if %{with python3}
%{__python3} %{_rpmconfigdir}/redhat/pathfix.py -i %{__python3} -p -n contrib/queryparse/queryparse
%endif

%install
%make_install dist_doc_DATA=''
%if %{with python2} || %{with python3}
install -p contrib/queryparse/queryparse %{buildroot}/%{_bindir}
install -D -m 644 -p contrib/queryparse/queryparse.1 %{buildroot}/%{_mandir}/man1/queryparse.1
gzip %{buildroot}/%{_mandir}/man1/queryparse.1
%endif

mkdir -p %{buildroot}%{_datadir}/%{name}
touch %{buildroot}%{_datadir}/%{name}/queryfile-example-current
install -m 755 -p %{SOURCE2} %{buildroot}%{_bindir}/dnsperf-data

%check
%make_build check

%files 
%doc README.md CHANGES
%license LICENSE
%{_bindir}/*perf*
%{_mandir}/man*/*perf*
%dir %{_datadir}/dnsperf
%ghost %{_datadir}/dnsperf/queryfile-example-current

%if %{with python2} || %{with python3}
%files queryparse
%{_bindir}/queryparse
%{_mandir}/man1/queryparse.1*
%endif

%changelog
* Thu Jan 16 2025 Fedora Release Engineering <releng@fedoraproject.org> - 2.12.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Wed Jul 24 2024 Miroslav Suchý <msuchy@redhat.com> - 2.12.0-6
- convert license to SPDX

* Wed Jul 17 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.12.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Wed Jan 24 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.12.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.12.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.12.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Tue May 23 2023 Petr Menšík <pemensik@redhat.com> - 2.12.0-1
- Update to 2.12.0

* Fri Mar 17 2023 Petr Menšík <pemensik@redhat.com> - 2.11.2-1
- Update to 2.11.2

* Sat Mar 11 2023 Petr Menšík <pemensik@redhat.com> - 2.11.1-1
- Update to 2.11.1

* Mon Feb 13 2023 Petr Menšík <pemensik@redhat.com> - 2.11.0-1
- Update 2.11.0

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.10.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Tue Jan 17 2023 Paul Wouters <paul.wouters@aiven.io - 2.10.0-2
- pathfix by Lumír Balhar (https://src.fedoraproject.org/rpms/dnsperf/pull-request/2)

* Fri Nov 11 2022 Petr Menšík <pemensik@redhat.com> - 2.10.0-1
- Update to 2.10.0

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.9.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.9.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Dec 22 2021 Petr Menšík <pemensik@redhat.com> - 2.9.0-1
- Update to 2.9.0
- Add tests during build

* Tue Nov 02 2021 Petr Menšík <pemensik@redhat.com> - 2.8.0-1
- Update to 2.8.0

* Sat Sep 18 2021 Petr Menšík <pemensik@redhat.com> - 2.7.1-1
- Update to 2.7.1

* Tue Sep 14 2021 Sahana Prasad <sahana@redhat.com> - 2.7.0-2
- Rebuilt with OpenSSL 3.0.0

* Mon Aug 09 2021 Petr Menšík <pemensik@redhat.com> - 2.7.0-1
- Update to 2.7.0, add DNS over HTTPS support

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.6.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Jun 02 2021 Petr Menšík <pemensik@redhat.com> - 2.6.0-1
- Update to 2.6.0

* Thu Mar 25 2021 Petr Menšík <pemensik@redhat.com> - 2.5.2-1
- Update to 2.5.2

* Tue Mar 23 2021 Petr Menšík <pemensik@redhat.com> - 2.5.1-2
- Remove dnsperf-data package. Provide dnsperf-data command to download sample
  instead.

* Tue Mar 23 2021 Petr Menšík <pemensik@redhat.com> - 2.5.1-1
- Update to 2.5.1

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Fri Jan 22 2021 Petr Menšík <pemensik@redhat.com> - 2.4.0-5
- Correct python3 issues in queryparse

* Fri Jan 22 2021 Petr Menšík <pemensik@redhat.com> - 2.4.0-4
- Move queryparse to separate subpackage
- Recommend only gnuplot for resperf-report

* Sat Dec 19 2020 Adam Williamson <awilliam@redhat.com> - 2.4.0-3
- Rebuild for libldns soname bump

* Thu Dec 10 2020 Petr Menšík <pemensik@redhat.com> - 2.4.0-2
- Update requirements of example queries

* Wed Dec 09 2020 Petr Menšík <pemensik@redhat.com> - 2.4.0-1
- Update to 2.4.0
- bind-libs dependency removed
- dnsperf-data has own version

* Fri Oct 23 2020 Petr Menšík <pemensik@redhat.com> - 2.3.4-7
- Rebuilt for bind 9.11.24

* Tue Sep 01 2020 Petr Menšík <pemensik@redhat.com> - 2.3.4-6
- Stop demanding GeoIP-devel where not required

* Fri Aug 21 2020 Petr Menšík <pemensik@redhat.com> - 2.3.4-5
- Rebuilt for bind 9.11.22

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.4-4
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Jun 25 2020 Petr Menšík <pemensik@redhat.com> - 2.3.4-2
- Add manual include for bind 9.16 support

* Mon May 25 2020 Petr Menšík <pemensik@redhat.com> - 2.3.4-1
- Update to 2.3.4

* Tue Mar 31 2020 Petr Menšík <pemensik@redhat.com> - 2.3.2-4
- Rebuilt for bind 9.11.17

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Mon Nov 25 2019 Petr Menšík <pemensik@redhat.com> - 2.3.2-2
- Rebuilt for bind 9.11.13

* Tue Aug 27 2019 Petr Menšík <pemensik@redhat.com> - 2.3.2-1
- Update to 2.3.2

* Mon Jul 29 2019 Petr Menšík <pemensik@redhat.com> - 2.3.1-1
- Update to 2.3.1

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Wed Jul 17 2019 Petr Menšík <pemensik@redhat.com> - 2.3.0-1
- Update to 2.3.0, support TCP mode

* Tue Jun 11 2019 Petr Menšík <pemensik@redhat.com> - 2.2.1-5
- Rebuilt for BIND 9.11.7

* Fri May 03 2019 Petr Menšík <pemensik@redhat.com> - 2.2.1-4
- Rebuilt for bind 9.11.6

* Tue Apr 09 2019 Petr Menšík <pemensik@redhat.com> - 2.2.1-3
- Move large query file into separate package

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Mon Jan 28 2019 Petr Menšík <pemensik@redhat.com> - 2.2.1-1
- Remove visible u after numbers

* Sun Jan 27 2019 Petr Menšík <pemensik@redhat.com> - 2.2.0-1
- Update to DNS-OARC 2.2.0 release

* Tue Nov 06 2018 Petr Menšík <pemensik@redhat.com> - 2.1.0.0-18
- Update to standard types, required by bind 9.11.5 update
- Changed project URL

* Fri Jul 13 2018 Petr Menšík <pemensik@redhat.com> - 2.1.0.0-17
- Update to bind 9.11.4

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.0.0-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Apr 26 2018 Tomas Hozza <thozza@redhat.com> - 2.1.0.0-15
- Added gcc as an explicit BuildRequires

* Thu Mar 01 2018 Petr Menšík <pemensik@redhat.com> - 2.1.0.0-14
- Define value to USEINLINE macro, rebuild for bind 9.11.3
- Cleanup spec file

* Thu Mar 01 2018 Iryna Shcherbina <ishcherb@redhat.com> - 2.1.0.0-13
- Update Python 2 dependency declarations to new packaging standards
  (See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3)

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.0.0-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Fri Jan 19 2018 Petr Menšík <pemensik@redhat.com> - 2.1.0.0-11
- Rebuild again against bind-9.11.2-P1

* Tue Jan 09 2018 Petr Menšík <pemensik@redhat.com> - 2.1.0.0-10
- Rebuild for bind 9.11.2

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.0.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.0.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Mon Jul 03 2017 Paul Wouters <pwouters@redhat.com> - 2.1.0.0-7
- Rebuild against 9.11.1-P2

* Thu Jun 29 2017 Petr Menšík <pemensik@redhat.com> - 2.1.0.0-6
- Rebuild against bind-9.11.1-P1

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.0.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Nov 21 2016 Paul Wouters <pwouters@redhat.com> - 2.1.0.0-4
- rebuilt for new version of bind

* Sat Nov 19 2016 Peter Robinson <pbrobinson@fedoraproject.org> 2.1.0.0-3
- Rebuild (bind)

* Thu May 26 2016 Tomas Hozza <thozza@redhat.com> - 2.1.0.0-2
- Rebuild against bind-9.10.4-P1

* Wed Apr 20 2016 Paul Wouters <pwouters@redhat.com> - 2.1.0.0-1
- Updated to 2.1.0.0 (rhbz#1305929)
- Remove incorporated patches
- Updated example query file with upstream
- Fixup bad changelog dates
- Use gunzip not bunzip2 as upstream query file is only gzipped

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.0.0-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Dec 16 2015 Tomas Hozza <thozza@redhat.com> - 2.0.0.0-19
- Rebuild against bind-9.10.3-P2

* Fri Sep 04 2015 Tomas Hozza <thozza@redhat.com> - 2.0.0.0-18
- Rebuild against bind 9.10.3rc1

* Wed Jun 24 2015 Tomas Hozza <thozza@redhat.com> - 2.0.0.0-17
- rebuild against bind-9.10.2-P1
- add Build dependency on GeoIP-devel since bind is built with it

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0.0.0-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Fri Mar 13 2015 Tomas Hozza <thozza@redhat.com> - 2.0.0.0-15
- rebuild against bind-9.10.2

* Wed Feb 25 2015 Tomas Hozza <thozza@redhat.com> - 2.0.0.0-14
- Rebuild against bind-9.10.2rc2

* Mon Feb 02 2015 Tomas Hozza <thozza@redhat.com> - 2.0.0.0-13
- rebuild against bind-9.10.2rc1

* Wed Jan 14 2015 Tomas Hozza <thozza@redhat.com> - 2.0.0.0-12
- rebuild against bind-9.10.1-P1

* Fri Oct 03 2014 Tomas Hozza <thozza@redhat.com> - 2.0.0.0-11
- rebuild against bind-9.9.6

* Sat Aug 16 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0.0.0-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0.0.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0.0.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Mon Jul 15 2013 Tomas Hozza <thozza@redhat.com> - 2.0.0.0-7
- Rebuild against bind 9.9.4b1

* Tue May 14 2013 Paul Wouters <pwouters@redhat.com> - 2.0.0.0-6
- Rebuild against bind 9.9.3-0.6.rc2
- Fix url, nominum changed their website

* Tue Apr 16 2013 Adam Tkac <atkac redhat com> - 2.0.0.0-5
- rebuild against new bind

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0.0.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Thu Oct 11 2012 Adam TKac <atkac redhat com> - 2.0.0.0-3
- rebuild against new bind-libs
- pack sample query file with bz2

* Wed Jul 18 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0.0.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Wed Apr 18 2012 Paul Wouters <pwouters@redhat.com> - 2.0.0.0-1
- Upgraded to 2.0.0.0
- Fixup of URLs
- Add pointer to sample query file in usage info
- Added current query sample file as old example has been removed
- Pulled in missing bind-9.8.x/9.9.x version of hmacsha.h
- Removed doc/*pdf files, as their license might mean non-free

* Wed Feb  1 2012 Adam Williamson <awilliam@redhat.com> - 1.0.1.0-28
- rebuild against new bind

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.1.0-27
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Mon Nov 14 2011 Adam Tkac <atkac redhat com> - 1.0.1.0-26
- rebuild against new bind

* Fri Sep 09 2011 Adam Tkac <atkac redhat com> - 1.0.1.0-25
- rebuild against new bind

* Tue May 24 2011 Paul Wouters <paul@xelerance.com> - 1.0.1.0-24
- rebuilt for newer bind

* Mon Feb 21 2011 Adam Tkac <atkac redhat com> - 1.0.1.0-23
- rebuild against new bind

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.1.0-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Thu Sep 30 2010 Adam Tkac <atkac@redhat.com> - 1.0.1.0-21
- rebuild against new bind

* Fri Aug 27 2010 Adam Tkac <atkac redhat com> - 1.0.1.0-20
- rebuild against new bind

* Tue Aug 03 2010 Adam Tkac <atkac redhat com> - 1.0.1.0-19
- rebuild against new bind

* Fri Jul 02 2010 Adam Tkac <atkac redhat com> - 1.0.1.0-18
- rebuild to ensure devel branch doesn't have lower NVR than stable branch

* Mon May 31 2010 Adam Tkac <atkac redhat com> - 1.0.1.0-17
- rebuild against new bind

* Thu Jan 28 2010 Adam Tkac <atkac redhat com> - 1.0.1.0-16
- rebuild against new bind

* Tue Dec 15 2009 Adam Tkac <atkac redhat com> - 1.0.1.0-15
- rebuild against new bind

* Tue Dec 01 2009 Adam Tkac <atkac redhat com> - 1.0.1.0-14
- rebuild against new bind

* Thu Nov 26 2009 Adam Tkac <atkac redhat com> - 1.0.1.0-13
- rebuild against new bind

* Fri Aug 21 2009 Tomas Mraz <tmraz@redhat.com> - 1.0.1.0-12
- rebuilt with new openssl

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.1.0-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Fri Jun 19 2009 Adam Tkac <atkac redhat com> - 1.0.1.0-10
- rebuild again

* Wed Jun 17 2009 Adam Tkac <atkac redhat com> - 1.0.1.0-9
- rebuild against new bind-libs

* Mon Mar 30 2009 Adam Tkac <atkac redhat com> - 1.0.1.0-8
- rebuild against new bind-libs

* Tue Feb 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.1.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Thu Jan 15 2009 Tomas Mraz <tmraz@redhat.com> - 1.0.1.0-6
- rebuild with new openssl
- seems to require libxml2-devel to build now

* Mon Nov 10 2008 Adam Tkac <atkac redhat com> - 1.0.1.0-5
- rebuild against new bind-libs

* Fri Oct 31 2008 Paul Wouters <paul@xelerance.com> - 1.0.1.0-4
- Changed license from BSD to MIT

* Wed Oct 22 2008 Paul Wouters <paul@xelerance.com> - 1.0.1.0-3
- Fixed missing buildrequires
- Pass proper CFLAGS to gcc
- Fix Group

* Tue Oct 21 2008 Paul Wouters <paul@xelerance.com> - 1.0.1.0-2
- Fixed libpcap vs libcap confusion

* Mon Oct 20 2008 Paul Wouters <paul@xelerance.com> - 1.0.1.0-1
- Initial Fedora package
