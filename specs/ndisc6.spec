Name:		ndisc6
Version:	1.0.8
Release:	3%{?dist}
Summary:	IPv6 diagnostic tools

License:	GPL-2.0-only OR GPL-3.0-only
URL:		https://www.remlab.net/ndisc6/
Source0:	https://www.remlab.net/files/ndisc6/ndisc6-%{version}.tar.bz2
Source1:	https://www.remlab.net/files/ndisc6/ndisc6-%{version}.tar.bz2.asc
# gpg2 --recv-key 0x772D56C80CA8ABF9C475FCA34E3557690BEE0224
# gpg2 --export --export-options export-minimal 0x772D56C80CA8ABF9C475FCA34E3557690BEE0224 > 772D56C80CA8ABF9C475FCA34E3557690BEE0224.gpg
Source2:	772D56C80CA8ABF9C475FCA34E3557690BEE0224.gpg
BuildRequires: make
BuildRequires:  gcc
BuildRequires:	gnupg2
BuildRequires:	perl-generators

%description
This package gathers a few diagnostic tools for IPv6 networks:
- ndisc6, which performs ICMPv6 Neighbor Discovery in user-land,
- rdisc6, which performs ICMPv6 Router Discovery in user-land,
- rltraceroute6, yet another IPv6 implementation of traceroute,
- tcptraceroute6, a TCP/IPv6-based traceroute implementation,
- tracert6, a ICMPv6 Echo Request based traceroute,
- tcpspray6, a TCP/IP Discard/Echo bandwidth meter.

%prep
%{gpgverify} --keyring='%{S:2}' --signature='%{S:1}' --data='%{S:0}'
%setup -q

%build
%configure --disable-suid-install
%make_build

%install
%make_install

%find_lang %{name}

%files -f %{name}.lang
%license COPYING 
%doc README
%{_sysconfdir}/rdnssd
%{_bindir}/addr2name
%{_bindir}/dnssort
%{_bindir}/name2addr
%{_bindir}/tcpspray
%{_bindir}/tcpspray6
%{_sbindir}/ndisc6
%{_sbindir}/rdisc6
%{_sbindir}/rdnssd
%{_sbindir}/rltraceroute6
%{_sbindir}/tcptraceroute6
%{_sbindir}/tracert6
%doc %{_mandir}/man1/addr2name.1.gz
%doc %{_mandir}/man1/dnssort.1.gz
%doc %{_mandir}/man1/name2addr.1.gz
%doc %{_mandir}/man1/tcpspray.1.gz
%doc %{_mandir}/man1/tcpspray6.1.gz
%doc %{_mandir}/man8/ndisc6.8.gz
%doc %{_mandir}/man8/rdisc6.8.gz
%doc %{_mandir}/man8/rdnssd.8.gz
%doc %{_mandir}/man8/rltraceroute6.8.gz
%doc %{_mandir}/man8/tcptraceroute6.8.gz
%doc %{_mandir}/man8/tracert6.8.gz

%changelog
* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.8-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.8-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Mon Apr 15 2024 Michele Baldessari <michele@acksyn.org> - 1.0.8-1
- New upstream

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.7-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.7-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Mon Nov 20 2023 Dominik Mierzejewski <dominik@greysector.net> - 1.0.7-3
- Switch to HTTPS URLs
- Enable tarball signature verification
- Drop unused patch
- Sort file list alphabetically
- Use SPDX identifiers in License: field

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.7-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Tue Jun 6 2023 Michele Baldessari <michele@acksyn.org> - 1.0.7-1
- New upstream

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Tue Aug 16 2022 Michele Baldessari <michele@acksyn.org> - 1.0.6-1
- New upstream

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Fri Feb 25 2022 Michele Baldessari <michele@acksyn.org> - 1.0.5-1
- New upstream

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.4-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Dec 01 2020 Michele Baldessari <michele@acksyn.org> - 1.0.4-1
- New upstream release

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.3-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.3-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.3-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.3-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.3-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.3-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.3-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri Nov 04 2016 Michele Baldessari <michele@acksyn.org> - 1.0.3-2
- Fix dnssort tool patch by Dominik 'Rathann' Mierzejewski. Fixes BZ#1361815

* Fri May 27 2016 Michele Baldessari <michele@acksyn.org> - 1.0.3-1
- New upstream version

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Fri Aug 22 2014 Stjepan Gros <stjepan.gros@gmail.com> - 1.0.2-1
- Bumped to a new upstream version

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.1-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Jul 17 2013 Petr Pisar <ppisar@redhat.com> - 1.0.1-5
- Perl 5.18 rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Mar 15 2011 Stjepan Gros <stjepan.gros@gmail.com> - 1.0.1-1
- Bumped to a new upstream version
- Removed references to isatap daemon as it is deprecated

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Thu Dec  2 2010 Stjepan Gros <stjepan.gros@gmail.com> - 1.0.0-1
- Bumped to a new upstream version

* Mon Nov 16 2009 Stjepan Gros <stjepan.gros@gmail.com> - 0.9.9-1
- Bumped to a new upstream version

* Mon Dec 29 2008 Stjepan Gros <stjepan.gros@gmail.com> - 0.9.8-2
- Escaped unintentional macro in changelog section

* Sun May  4 2008 Stjepan Gros <stjepan.gros@gmail.com> - 0.9.8-1
- Bumped version

* Sat Mar 15 2008 Stjepan Gros <stjepan.gros@gmail.com> - 0.9.7-1
- Bumped version
- Removed patches

* Tue Jan 22 2008 Stjepan Gros <stjepan.gros@gmail.com> - 0.9.5-1
- Synced with upstream version
- Restricted license to GPLv2 or GPLv3
- Use %%find_lang macro
- Rebased and cleaned up patch to exclude absolute paths
- Added patch to avoid duplicate netlink definition

* Sat Dec 22 2007 Stjepan Gros <stjepan.gros@gmail.com> - 0.9.3-2
- Changed license to GPLv2+
- Removed absolute symlinks for manual pages
- Removed setuid bits on binaries
- Fixed changelog entries to include version

* Sat Dec 8 2007 Stjepan Gros <stjepan.gros@gmail.com> - 0.9.3-1
- Initial Release
