Summary:       List or change SCSI/SATA disk parameters
Name:          sdparm
Version:       1.12
Release:       12%{?dist}

# This software is primarily BSD-2-Clause, except for the following files:
# - BSD-2-Clause AND GPL-2.0-or-later
#     - lib/sg_pt_linux_nvme.c
# - BSD-4-Clause-UC
#     - src/getopt_long.c
#     - src/port_getopt.h
# There is also a BSD-3-Clause COPYING file, but as best I can tell no software
# files are actually covered by that license.  Headers in other files reference
# the BSD_LICENSE instead.
# Automatically converted from old format: BSD-2-Clause AND GPL-2.0-or-later AND BSD-4-Clause-UC - review is highly recommended.
License:       BSD-2-Clause AND GPL-2.0-or-later AND BSD-4-Clause-UC

URL:           http://sg.danny.cz/sg/sdparm.html
Source0:       http://sg.danny.cz/sg/p/sdparm-%{version}.tgz

# extracted from the header of lib/sg_pt_linux_nvme.c
Source1:       GPL-2.0-or-later.txt

# extracted from the header of src/getopt_long.c
Source2:       BSD-4-Clause-UC.txt

BuildRequires: make
BuildRequires: gcc
BuildRequires: sg3_utils-devel

%description 
SCSI disk parameters are held in mode pages. This utility lists or
changes those parameters. Other SCSI devices (or devices that use the
SCSI command set e.g. some SATA devices) such as CD/DVD and tape
drives may also find parts of sdparm useful.

Fetches Vital Product Data pages. Can send commands to start or stop
the media and load or unload removable media.

Warning: It is possible (but unlikely) to change SCSI disk settings
such that the disk stops operating or is slowed down. Use with care.

%prep
%setup -q
cp %{S:1} %{S:2} .

%build
%configure --disable-libsgutils
%make_build

%install
%make_install

%files
%license BSD_LICENSE GPL-2.0-or-later.txt BSD-4-Clause-UC.txt
%doc ChangeLog README CREDITS AUTHORS notes.txt
%{_bindir}/sdparm
%{_bindir}/sas_disk_blink
%{_bindir}/scsi_ch_swp
%{_mandir}/man8/sdparm*
%{_mandir}/man8/sas_disk_blink*
%{_mandir}/man8/scsi_ch_swp*

%changelog
* Fri Jul 25 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.12-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_43_Mass_Rebuild

* Sun Jan 19 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.12-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Wed Sep 04 2024 Miroslav Suchý <msuchy@redhat.com> - 1.12-10
- convert license to SPDX

* Wed Aug 21 2024 Carl George <carlwgeorge@fedoraproject.org> - 1.12-9
- Migrated to SPDX license

* Sat Jul 20 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.12-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Sat Jan 27 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.12-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sat Jul 22 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.12-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Sat Jan 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.12-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.12-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Sat Jan 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.12-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.12-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Apr 23 2021 Terje Rosten <terje.rosten@ntnu.no> - 1.12-1
- 1.12

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.11-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.11-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Mar 09 2020 Terje Rosten <terje.rosten@ntnu.no> - 1.11-1
- 1.11

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.10-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.10-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.10-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.10-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.10-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.10-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.10-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.10-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Feb 24 2016 Terje Rosten <terje.rosten@ntnu.no> - 1.10-2
- date fix

* Wed Feb 24 2016 Terje Rosten <terje.rosten@ntnu.no> - 1.10-1
- 1.10

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.09-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Jun 19 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.09-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Mon Dec 29 2014 Terje Rosten <terje.rosten@ntnu.no> - 1.09-1
- 1.09
- Use internel sg3_utils on FC20 (shipped sg3_utils is too old)
- Various spec cleanups

* Mon Aug 18 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.08-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.08-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.08-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Sun Jun 09 2013 Terje Rosten <terje.rosten@ntnu.no> - 1.08-1
- 1.08

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.07-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.07-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sun Jan 29 2012 Terje Rosten <terje.rosten@ntnu.no> - 1.07-1
- 1.07

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.06-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Mon Jul 18 2011 Dan Horák <dan@danny.cz> - 1.06-3
- rebuilt for sg3_utils 1.31

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.06-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Thu Nov 18 2010 Terje Rosten <terje.rosten@ntnu.no> - 1.06-1
- 1.06

* Thu Apr 15 2010 Terje Rosten <terje.rosten@ntnu.no> - 1.05-2
- build with shared libs (thanks to Dan Horák)

* Thu Apr 15 2010 Terje Rosten <terje.rosten@ntnu.no> - 1.05-1
- 1.05

* Wed Oct 14 2009 Dan Horák <dan[at]danny.cz> - 1.04-1
- 1.04

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.03-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.03-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Sun Feb  8 2009 Terje Rosten <terje.rosten@ntnu.no> - 1.03-2
- Website has moved

* Tue Aug 12 2008 Terje Rosten <terje.rosten@ntnu.no> - 1.03-1
- 1.03

* Sat Feb  9 2008 Terje Rosten <terje.rosten@ntnu.no> - 1.02-2
- Rebuild

* Mon Nov  5 2007 Terje Rosten <terje.rosten@ntnu.no> - 1.02-1
- 1.02

* Tue Aug 28 2007 Terje Rosten <terje.rosten@ntnu.no> - 1.01-3
- Rebuild

* Mon May 21 2007 Terje Rosten <terje.rosten@ntnu.no> - 1.01-2
- Tag problem

* Mon May 21 2007 Terje Rosten <terje.rosten@ntnu.no> - 1.01-1
- New upstream release: 1.01

* Mon Nov 20 2006 Terje Rosten <terje.rosten@ntnu.no> - 1.00-4
- Fix changelog
- Don't install INSTALL

* Mon Nov 20 2006 Terje Rosten <terje.rosten@ntnu.no> - 1.00-3
- Maybe we should build in %%build :-)
- Remove check in %%clean/%%install

* Mon Nov 20 2006 Terje Rosten <terje.rosten@ntnu.no> - 1.00-2
- fix license, buildroot and group
- remove hardcoded packager tag
- use %%configure macro
- dist tag
- make install on single line
- fix files section
- remove strange use of macros (name, version and release)
- untabify

* Mon Oct 16 2006 Douglas Gilbert <dgilbert at interlog dot com> - 1.00
- update Background control mode subpage, vendor specific mode pages
- sdparm-1.00

* Sat Jul 08 2006 Douglas Gilbert <dgilbert at interlog dot com> - 0.99
- add old power condition page for disks
- sdparm-0.99

* Thu May 18 2006 Douglas Gilbert <dgilbert at interlog dot com> - 0.98
- add medium configuration mode page
- sdparm-0.98

* Wed Jan 25 2006 Douglas Gilbert <dgilbert at interlog dot com> - 0.97 
- add SAT pATA control and medium partition mode (sub)pages
- sdparm-0.97

* Fri Nov 18 2005 Douglas Gilbert <dgilbert at interlog dot com> - 0.96
- add capacity, ready and sync commands
- sdparm-0.96

* Tue Sep 20 2005 Douglas Gilbert <dgilbert at interlog dot com> - 0.95
- add debian build directory, decode more VPD pages
- sdparm-0.95

* Thu Jul 28 2005 Douglas Gilbert <dgilbert at interlog dot com> - 0.94
- add '--command=<cmd>' option
- sdparm-0.94

* Thu Jun 02 2005 Douglas Gilbert <dgilbert at interlog dot com> - 0.93
- add '--transport=' and '--dbd' options
- sdparm-0.93

* Fri May 20 2005 Douglas Gilbert <dgilbert at interlog dot com> - 0.92
- add some tape, cd/dvd, disk, ses and rbc mode pages
- sdparm-0.92

* Fri May 06 2005 Douglas Gilbert <dgilbert at interlog dot com> - 0.91
- if lk 2.4 detected, map non-sg SCSI device node to sg equivalent
- sdparm-0.91

* Mon Apr 18 2005 Douglas Gilbert <dgilbert at interlog dot com> - 0.90
- initial version
- sdparm-0.90
