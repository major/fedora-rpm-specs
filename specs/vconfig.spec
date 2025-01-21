Name:       vconfig
Version:    1.9
Release:    39%{?dist}
Summary:    Linux 802.1q VLAN configuration utility
# Automatically converted from old format: GPLv2+ - review is highly recommended.
License:    GPL-2.0-or-later
URL:        http://www.candelatech.com/~greear/vlan.html
Source:     http://www.candelatech.com/~greear/vlan/vlan.%{version}.tar.gz
# Fix a security warning by compiler, bug #1037376
Patch0:     %{name}-1.9-Pass-compilation-with-Werror-format-security.patch
BuildRequires:  coreutils
BuildRequires:  gcc
BuildRequires:  make

%description 
The vconfig program configures and adjusts 802.1q VLAN parameters.
This tool is deprecated in favor of "ip link" command.

%prep
%setup -q -n vlan
%patch -P0 -p1 -b .warning

%build
make clean
rm -f vconfig
make CCFLAGS="%{optflags}" LDFLAGS="%{build_ldflags}" STRIP=/bin/true vconfig

%install
install -D -m755 vconfig ${RPM_BUILD_ROOT}%{_sbindir}/vconfig
install -D -m644 vconfig.8 ${RPM_BUILD_ROOT}%{_mandir}/man8/vconfig.8

%files 
%doc CHANGELOG README vlan.html vlan_test.pl
%{_sbindir}/vconfig
%{_mandir}/man8/vconfig.8*

%changelog
* Sun Jan 19 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.9-39
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Fri Jul 26 2024 Miroslav Suchý <msuchy@redhat.com> - 1.9-38
- convert license to SPDX

* Sat Jul 20 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.9-37
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Sat Jan 27 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.9-36
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sat Jul 22 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.9-35
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Sat Jan 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.9-34
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.9-33
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Sat Jan 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.9-32
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Tue Jul 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.9-31
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.9-30
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.9-29
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Jan 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.9-28
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sat Jul 27 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.9-27
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.9-26
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.9-25
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Mar 07 2018 Petr Pisar <ppisar@redhat.com> - 1.9-24
- Modernize spec file

* Fri Feb 23 2018 Florian Weimer <fweimer@redhat.com> - 1.9-23
- Use LDFLAGS from redhat-rpm-config

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.9-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.9-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.9-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.9-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri Feb 05 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.9-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Jun 19 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.9-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Mon Aug 18 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.9-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.9-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Tue Dec 03 2013 Petr Pisar <ppisar@redhat.com> - 1.9-14
- Fix a security warning by compiler (bug #1037376)
- Move the executable to /usr/sbin
- Modernize the spec file

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.9-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Fri Feb 15 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.9-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sun Jul 22 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.9-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.9-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Mon Feb 07 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.9-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.9-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.9-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Wed Mar 19 2008 Roman Rakus <rrakus@redhat.cz> - 1.9-6
- added STRIP=/bin/true for useful debuginfo

* Tue Feb 19 2008 Fedora Release Engineering <rel-eng@fedoraproject.org> - 1.9-5
- Autorebuild for GCC 4.3

* Thu Aug 16 2007 Phil Knirsch <pknirsch@redhat.com> - 1.9-4
- License review and update

* Wed Jan 10 2007 Phil Knirsch <pknirsch@redhat.com> - 1.9-3
- Removed CVS cruft from documentation (#221161)
- Tiny specfile cleanups.

* Wed Jul 12 2006 Jesse Keating <jkeating@redhat.com> - 1.9-2.1
- rebuild

* Fri Feb 17 2006 Phil Knirsch <pknirsch@redhat.com> - 1.9-2
- Fix build problems and cleaned up files in archive properly

* Fri Feb 10 2006 Jesse Keating <jkeating@redhat.com> - 1.9-1.1
- bump again for double-long bug on ppc(64)

* Fri Feb 10 2006 Phil Knirsch <pknirsch@redhat.com> - 1.9-1
- Updated to vconfig-1.9

* Tue Feb 07 2006 Jesse Keating <jkeating@redhat.com> - 1.8-7.2
- rebuilt for new gcc4.1 snapshot and glibc changes

* Fri Dec 09 2005 Jesse Keating <jkeating@redhat.com> - 1.8-7.1
- rebuilt

* Mon Aug 15 2005 Phil Knirsch <pknirsch@redhat.com>
- Fixed license from LGPL to GPL (#163998)

* Wed Mar 02 2005 Phil Knirsch <pknirsch@redhat.com> 1.8-7
- bump release and rebuild with gcc 4

* Fri Feb 18 2005 Phil Knirsch <pknirsch@redhat.com> 1.8-6
- rebuilt

* Sun Feb 13 2005 Florian La Roche <laroche@redhat.com> 1.8-5
- remove kernel dep, kernel runtime deps should go into apps, #146151

* Mon Sep 27 2004 Phil Knirsch <pknirsch@redhat.com> 1.8-4
- Small specfile changes (#131487)

* Tue Jun 15 2004 Elliot Lee <sopwith@redhat.com>
- rebuilt

* Fri Feb 13 2004 Elliot Lee <sopwith@redhat.com>
- rebuilt

* Wed Oct 22 2003 Bill Nottingham <notting@redhat.com> 1.8-1
- update to 1.8 (#107761)

* Wed Jun 04 2003 Elliot Lee <sopwith@redhat.com>
- rebuilt

* Thu May 22 2003 Jeremy Katz <katzj@redhat.com> 1.6-3
- fix to build with gcc 3.3

* Fri Jan 31 2003 Bill Nottingham <notting@redhat.com> 1.6-2
- adapt upstream package
- add patch for license

* Thu Jan 23 2003 Tuomo Soini <tis@foobar.fi> 1.6-6foo
- changes for new initscripts package

* Sun Sep 15 2002 Tuomo Soini <tis@foobar.fi> 1.6-5foo
- foobarize

* Tue Aug 06 2002 Tuomo Soini <tis@foobar.fi> 1.6-t4
- fix ifup-vlan to be able to set default route

* Tue Jun 25 2002 Tuomo Soini <tis@foobar.fi> 1.6-t3
- pgp sign, foobarize spec-file

* Thu May 30 2002 Tuomo Soini <tis@foobar.fi> 1.6-t2
- fix typo in ifup-vlan

* Thu May 30 2002 Tuomo Soini <tis@foobar.fi> 1.6-t1
- updated for redhat 7.3
- build doesn't require kernel-sources

* Fri Apr 05 2002 Dale Bewley <dale@bewley.net>
- update to 1.6
- add ifup scripts

* Tue Dec 11 2001 Dale Bewley <dale@bewley.net>
- initial specfile

# EOF
