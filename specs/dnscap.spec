Name:           dnscap
Version:        141
Release:        19%{?dist}
Summary:        DNS traffic capture utility

License:        ISC
URL:            http://public.oarci.net/tools/dnscap
Source0:        http://dnscap.dns-oarc.net/dnscap-%{version}.tar.gz

BuildRequires:  libpcap-devel, libbind-devel, autoconf, automake, libtool
BuildRequires:  pkgconfig, groff-base

Patch0: dnscap134-installfix.patch

%description
dnscap is a network capture utility designed specifically for DNS traffic. It
produces binary data in pcap(3) format, either on standard output or in
successive dump files. This utility is similar to tcpdump(1), but has finer 
grained packet recognition tailored to DNS transactions and protocol options

%prep
%setup -q

%patch0 -p1 -b .installfix

%build
autoreconf --install
%configure
make %{?_smp_mflags}

%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT

%files
%{_bindir}/dnscap
%{_mandir}/man1/dnscap.1.gz

%changelog
* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 141-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 141-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 141-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 141-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 141-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 141-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 141-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 141-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 141-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 141-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 141-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Aug 16 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 141-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 141-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 141-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Tue Feb 19 2013 Adam Tkac <atkac redhat com> 141-5
- add groff-base to BR

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 141-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Mon Nov 26 2012 Adam Tkac <atkac redhat com> 141-3
- remove groff BR

* Wed Jul 18 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 141-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Tue Apr 24 2012 Adam Tkac <atkac redhat com> 141-1
- update to 141

* Fri Jan 06 2012 Adam Tkac <atkac redhat com> 134-1
- update to 134
- patches merged:
  - dnscap-1.0-isc_list.patch
  - dnscap-1.0-warns.patch
  - dnscap-1.0-system.patch

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0-0.11.20070807cvs
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0-0.10.20070807cvs
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Mon Mar 30 2009 Adam Tkac <atkac redhat com> 1.0-0.9.20070807cvs
- remove hardcoded dependencies on libpcap and bind-libs
- fix building with the latest gcc

* Mon Mar 09 2009 Adam Tkac <atkac redhat com> 1.0-0.8.20070807cvs
- replace bind-devel by libbind-devel

* Tue Feb 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0-0.7.20070807cvs
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Mon Feb 18 2008 Fedora Release Engineering <rel-eng@fedoraproject.org> - 1.0-0.6.20070807cvs
- Autorebuild for GCC 4.3

* Wed Aug 22 2007 Adam Tkac <atkac redhat com> 1.0-0.5.20070807cvs
- rebuild (to get BuildID feature)

* Tue Aug 7 2007 Adam Tkac <atkac redhat com> 1.0-0.4.20070807cvs
- handle return value of system() function

* Tue Aug 7 2007 Adam Tkac <atkac redhat com> 1.0-0.3.20070807cvs
- updated to latest cvs
- use libbind's isc/list API

* Mon Aug 6 2007 Adam Tkac <atkac redhat com> 1.0-0.2.20070516cvs
- changed license to ISC
- fixed release number

* Wed Aug 2 2007 Adam Tkac <atkac redhat com> 1.0-0.1.rc5
- initial package
