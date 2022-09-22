%global commit  9b5946822a5c9c617d937245fdc9049c5740ae09
%global shortcommit  %(c=%{commit}; echo ${c:0:7})

Name:           ngrep
Version:        1.47
Release:        9.1.20180101git%{shortcommit}%{?dist}
Summary:        Network layer grep tool
License:        BSD with advertising
URL:            https://github.com/jpr5/ngrep
Source0:        https://github.com/jpr5/ngrep/archive/%{commit}/%{name}-%{shortcommit}.tar.gz
BuildRequires: make
BuildRequires:  gcc
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  libpcap-devel
BuildRequires:  pcre-devel
BuildRequires:  libnet-devel

%description
ngrep strives to provide most of GNU grep's common features, applying them
to the network layer. ngrep is a pcap-aware tool that will allow you to
specify extended regular or hexadecimal expressions to match against data
payloads of packets. It currently recognizes TCP, UDP, ICMP, IGMP and Raw
protocols across Ethernet, PPP, SLIP, FDDI, Token Ring, 802.11 and null
interfaces, and understands bpf filter logic in the same fashion as more
common packet sniffing tools, such as tcpdump and snoop.

%prep
%setup -qn %{name}-%{commit}
# Make sure not to be using bundled libs
rm -r regex-0.12

%build
autoreconf -fiv
# Note: building with PCRE instead of GNU regex because of license
# incompatibilities (this one's basically a BSD with advertising clause).
%configure --enable-pcre \
           --enable-ipv6 \
           --with-pcap-includes=%{_includedir}/pcap \
           --enable-tcpkill
make %{?_smp_mflags} STRIPFLAG=

%install
make install DESTDIR=%{buildroot} BINDIR_INSTALL=%{_sbindir}

%files
%license LICENSE
%doc CHANGES CREDITS EXAMPLES.md README.md
%{_sbindir}/ngrep
%{_mandir}/man8/ngrep.8*

%changelog
* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.47-9.1.20180101git9b59468
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.47-8.1.20180101git9b59468
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.47-7.1.20180101git9b59468
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.47-6.1.20180101git9b59468
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.47-5.1.20180101git9b59468
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.47-4.1.20180101git9b59468
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.47-3.1.20180101git9b59468
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.47-2.1.20180101git9b59468
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Sep  1 2018 Robin Lee <cheeselee@fedoraproject.org> - 1.47-1.1.20180101git9b59468
- Update to latest snapshot (1.47 with build fix) (BZ#1528728, BZ#1401152)

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.47-0.6.a39256b
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.47-0.5.a39256b
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.47-0.4.a39256b
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.47-0.3.a39256b
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.47-0.2.a39256b
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Sat Oct 29 2016 Fabio Alessandro Locati <fale@fedoraproject.org> - 1.47-0.1.a39256b7
- Rebase on current master branch
- Remove patches

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.45-20.git20131221.16ba99a
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Tue Jul 07 2015 Ralf Corsépius <corsepiu@fedoraproject.org> - 1.45-19.git20131221.16ba99a
- Let configure honor CFLAGS (Fix F23FTBFS RHBZ#1239717).
- Make sure not to be using bundled libs.

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.45-18.git20131221.16ba99a
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.45-17.git20131221.16ba99a
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.45-16.git20131221.16ba99a
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Dec 21 2013 Christopher Meng <rpm@cicku.me> - 1.45-15.git20131221.16ba99a
- Checkout from official repo(BZ#1044630).
- Remove patch for system pcre as configure script can handle it now.
- Add format security check fix due to dumb GCC.

* Mon Aug 26 2013 Christopher Meng <rpm@cicku.me> - 1.45-14
- SPEC Cleanup.
- AArch64 support(BZ#926232).

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.45-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.45-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.45-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Feb 10 2012 Petr Pisar <ppisar@redhat.com> - 1.45-10
- Rebuild against PCRE 8.30

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.45-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.45-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Tue Mar 16 2010 Oliver Falk <oliver@linux-kernel.at> 1.45-7
- pcap has moved to /usr/include/pcap, instead of /usr/include :-/

* Sat Jul 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.45-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.45-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Wed Feb 13 2008 Patrick "Jima" Laughton <jima@beer.tclug.org> 1.45-4
- Bump-n-build for GCC 4.3

* Wed Aug 22 2007 Patrick "Jima" Laughton <jima@beer.tclug.org> 1.45-3
- License clarification

* Tue Aug 21 2007 Patrick "Jima" Laughton <jima@beer.tclug.org> 1.45-2
- Rebuild for BuildID

* Wed Nov 29 2006 Patrick "Jima" Laughton <jima@beer.tclug.org> 1.45-1
- Upgrade to 1.45
- Enable IPv6 support
- Rebuild due to libpcap upgrade

* Wed Oct 04 2006 Patrick "Jima" Laughton <jima@beer.tclug.org> 1.44-7
- Bump-n-build

* Tue Sep 19 2006 Patrick "Jima" Laughton <jima@beer.tclug.org> - 1.44-6
- Bump for FC6 rebuild

* Fri Sep 08 2006 Oliver Falk <oliver@linux-kernel.at> - 1.44-5
- Fix BR

* Tue Oct 18 2005 Oliver Falk <oliver@linux-kernel.at> - 1.44-4
- Bug #170967, useless debuginfo was generated

* Wed Aug 24 2005 Oliver Falk <oliver@linux-kernel.at> - 1.44-3
- Bugs from #166481

* Mon Aug 22 2005 Oliver Falk <oliver@linux-kernel.at> - 1.44-2
- Bug #165963
- Merge with package from Ville
  See also https://www.redhat.com/archives/fedora-extras-list/2005-July/msg01009.html

* Thu Aug 11 2005 Oliver Falk <oliver@linux-kernel.at> - 1.44-1
- Initial build for Fedora Extras
