Summary: A tool for testing TCP connections
Name: ttcp
Version: 1.12
Release: 51%{?dist}
URL:	ftp://ftp.sgi.com/sgi/src/ttcp/
Source0: ftp://ftp.sgi.com/sgi/src/ttcp/ttcp.c
Source1: ftp://ftp.sgi.com/sgi/src/ttcp/ttcp.1
Source2: ftp://ftp.sgi.com/sgi/src/ttcp/README
Patch0: ttcp-big.patch
Patch1: ttcp-malloc.patch
Patch2: ttcp-GNU.patch
Patch3: ttcp-man.patch
BuildRequires: gcc
# Automatically converted from old format: Public Domain - needs further work
License: LicenseRef-Callaway-Public-Domain

%description
ttcp is a tool for testing the throughput of TCP connections.  Unlike other
tools which might be used for this purpose (such as FTP clients), ttcp does
not read or write data from or to a disk while operating, which helps ensure
more accurate results.

%prep
%setup -c -T -q
cp -a %{SOURCE0} %{SOURCE1} %{SOURCE2} .
%patch -P0 -p1 -b .big
%patch -P1 -p1 -b .malloc
%patch -P2 -p1 -b .GNU
%patch -P3 -p1 -b .man

%build
%{__cc} -o ttcp $RPM_OPT_FLAGS ttcp.c

%install
mkdir -p $RPM_BUILD_ROOT{%{_mandir}/man1,%{_bindir}}
install -p -m755 ttcp $RPM_BUILD_ROOT%{_bindir}
install -p -m644 ttcp.1 $RPM_BUILD_ROOT%{_mandir}/man1

%files
%doc README
%{_bindir}/ttcp
%{_mandir}/man1/ttcp.1*

%changelog
* Sun Jan 19 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.12-51
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Sat Jul 20 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.12-50
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Sat Jan 27 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.12-49
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sat Jul 22 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.12-48
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Sat Jan 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.12-47
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.12-46
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Sat Jan 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.12-45
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.12-44
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.12-43
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.12-42
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Jan 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.12-41
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sat Jul 27 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.12-40
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.12-39
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.12-38
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.12-37
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.12-36
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.12-35
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.12-34
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri Feb 05 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.12-33
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Mon Jul 13 2015 Michal Sekletar <msekleta@redhat.com> - 1.12-32
- rebuilt due to changed BuildRequires (#1230502)

* Fri Jun 19 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.12-31
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Mon Aug 18 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.12-30
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.12-29
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.12-28
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Fri Feb 15 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.12-27
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sun Jul 22 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.12-26
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.12-25
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Aug 30 2011 Michal Sekletar <msekleta@redhat.com> - 1.12-24
- fix manpage

* Thu Aug 18 2011 Michal Sekletar <msekleta@redhat.com> - 1.12-23
- spec clean up
- added option to cp and install, thus ownership and timestamps are preserved
- removed BuildRoot tag, clean section and buildroot clean up before install

* Wed Aug 17 2011 Michal Sekletar <msekleta@redhat.com> - 1.12-22
- Minor fixes, source file ttcp.c can be patched successfully
- ttcp-inet.patch no longer needed - removed from repository

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.12-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.12-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.12-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Fri Feb 22 2008 Marcela Maslanova <mmaslano@redhat.com> - 1.12-18
- NI_MAXHOST was fixed, so get rid of the previous patch

* Tue Feb 12 2008 Marcela Maslanova <mmaslano@redhat.com> - 1.12-17
- fix for mass rebuild F-9 alpha
- fix warnings

* Fri Aug 24 2007 Marcela Maslanova <mmaslano@redhat.com> - 1.12-16
- check license, mass rebuild

* Tue Mar 06 2007 Marcela Maslanova <mmaslano@redhat.com> - 1.12-15
- merge review
- rhbz#226505

* Wed Jul 12 2006 Jesse Keating <jkeating@redhat.com> - 1.12-14.1
- rebuild

* Thu Jun 15 2006 Radek Vokal <rvokal@redhat.com> 1.12-14
- rebuilt

* Fri Feb 10 2006 Jesse Keating <jkeating@redhat.com> - 1.12-13.2.1
- bump again for double-long bug on ppc(64)

* Tue Feb 07 2006 Jesse Keating <jkeating@redhat.com> - 1.12-13.2
- rebuilt for new gcc4.1 snapshot and glibc changes

* Fri Dec 09 2005 Jesse Keating <jkeating@redhat.com>
- rebuilt

* Fri Mar 04 2005 Radek Vokal <rvokal@redhat.com> - 1.12-13
- gcc4 rebuilt

* Tue Feb 22 2005 Radek Vokal <rvokal@redhat.com>
- implement full IPv6 support (server uses ipv6 mapped addresses for ipv4)
- fix a few warnings 
- added -I option to specify network interface
- added multicast support
- added -w option to specify microsecond delay between each write
- multiple processes can listen to same port
- previous patch cleaned

* Sun Feb 13 2005 Florian La Roche <laroche@redhat.com>
- add patch from #146012

* Tue Jun 15 2004 Elliot Lee <sopwith@redhat.com>
- rebuilt

* Fri Feb 13 2004 Elliot Lee <sopwith@redhat.com>
- rebuilt

* Tue Oct 21 2003 Florian La Roche <Florian.LaRoche@redhat.de>
- add %%clean specfile target

* Wed Jun 04 2003 Elliot Lee <sopwith@redhat.com>
- rebuilt

* Wed Jan 22 2003 Tim Powers <timp@redhat.com>
- rebuilt

* Thu Dec 12 2002 Tim Powers <timp@redhat.com> 1.12-6
- rebuild on all arches

* Fri Jun 21 2002 Tim Powers <timp@redhat.com>
- automated rebuild

* Sun May 26 2002 Tim Powers <timp@redhat.com>
- automated rebuild

* Fri May 17 2002 Nalin Dahyabhai <nalin@redhat.com> 1.12-3
- rebuild in new environment

* Tue May 15 2001 Nalin Dahyabhai <nalin@redhat.com> 1.12-2
- fix defattr

* Thu May 10 2001 Nalin Dahyabhai <nalin@redhat.com> 1.12-1
- build initial package
