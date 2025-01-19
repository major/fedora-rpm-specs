Name:           monitor-edid
Summary:        Tool for probing and parsing monitor EDID

# Automatically converted from old format: GPLv3+ - review is highly recommended.
License:        GPL-3.0-or-later
Url:            http://gitweb.mageia.org/software/monitor-edid/

Version:        3.4
Release:        10%{?dist}

Source0:        https://gitweb.mageia.org/software/monitor-edid/snapshot/refs/tags/v%{version}.tar.gz#/%{name}-%{version}.tar.gz

# Fix Makefile to permit RPM CFLAGS
Patch000:	monitor-edid-Makefile.patch

# fix double include
Patch001:	Avoid-double-include.patch

Requires:	perl(File::Find)

BuildRequires:  coreutils
BuildRequires:  make
BuildRequires:  sed

BuildRequires:  perl-generators

# for tests
BuildRequires:	perl(Data::Dumper)
BuildRequires:	perl(Getopt::Long)
BuildRequires:	perl(Parse::EDID)

%ifarch %{ix86} x86_64
BuildRequires: libx86-devel
BuildRequires: gcc
%else
# not binary on non x86 arches
%global debug_package %{nil}
%endif

%description
Monitor-edid is a tool for probing and parsing Extended display
identification data (EDID) from monitors.

For more information about EDID, see http://en.wikipedia.org/wiki/EDID


%prep
%autosetup -n refs/tags/v%{version}


%build
# Use default build flags
%set_build_flags

# Remove -Wl,--as-needed  from LDFLAGS as that is not compatible with libx86
LDFLAGS=$(echo ${LDFLAGS} | sed -e 's/-Wl,--as-needed//')
export LDFLAGS

%make_build


%install
%make_install


%check
cd test
# see https://bugs.mageia.org/show_bug.cgi?id=25334
make new_MonitorsDB
make all


%files
%doc README NEWS ChangeLog
%license COPYING
%{_bindir}/monitor-parse-edid
%{_sbindir}/monitor-edid
%{_sbindir}/monitor-get*

# Mandriva specific scripts (requires lspcidrake)
%exclude %{_sbindir}/monitor-probe*


%changelog
* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 3.4-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Thu Jul 25 2024 Miroslav Suchý <msuchy@redhat.com> - 3.4-9
- convert license to SPDX

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 3.4-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 3.4-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 3.4-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 3.4-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 3.4-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 3.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 3.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Mon Dec 13 2021 Pat Riehecky <riehecky@fnal.gov> - 3.4-1
- Update to latest upstream

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 3.2-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Mon May 17 2021 Pat Riehecky <riehecky@fnal.gov - 3.2-6
- Fix missing required BZ1960811

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 3.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Feb 19 2020 Pat Riehecky <riehecky@fnal.gov - 3.2-3
- Fix double include

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Mon Aug 19 2019 Pat Riehecky <riehecky@fnal.gov - 3.2-1
- Change URL from http://wiki.mandriva.com/en/Tools/monitor-edid
- Update to v3.2

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.0-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 3.0-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.0-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.0-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Jul 18 2013 Petr Pisar <ppisar@redhat.com> - 3.0-7
- Perl 5.18 rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Thu Jan 06 2011 Remi Collet <Fedora@famillecollet.com> 3.0-2
- remove mandriva specific scripts (#667568)

* Sat Feb 13 2010 Remi Collet <Fedora@famillecollet.com> 3.0-1
- update to new upstream version
- switch from lrmi to libx86

* Sun Oct 25 2009 Remi Collet <Fedora@famillecollet.com> 2.5-1
- new version
- bundle lrmi (not available on EL)

* Sat Oct 17 2009 Remi Collet <Fedora@famillecollet.com> 2.4-1
- new version

* Sat Jul 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Tue Apr 08 2008 Remi Collet <Fedora@famillecollet.com> 2.0-1
- new version

* Mon Apr 07 2008 Remi Collet <Fedora@famillecollet.com> 1.16-5
- lrmi not available on EL

* Sun Apr 06 2008 Remi Collet <Fedora@famillecollet.com> 1.16-4
- use system lrmi on ix86 (From Ville Skyttä)

* Mon Mar 17 2008 Remi Collet <Fedora@famillecollet.com> 1.16-3
- fix license again

* Sun Mar 16 2008 Remi Collet <Fedora@famillecollet.com> 1.16-2
- From review : clean + fix license

* Sun Mar 16 2008 Remi Collet <Fedora@famillecollet.com> 1.16-1
- initial spec for Fedora review

* Mon Mar 10 2008 Pixel <pixel@mandriva.com> 1.16-1mdv2008.1
+ Revision: 183268
- update URL
- 1.16:
- do not install monitor-get-edid-using-vbe on archs where VBE is not
  available (Remi Collet)

* Sun Mar  9 2008 Remi Collet <rpms@famillecollet.com> 1.15-1.fc#.remi
- build for Fedora

* Wed Jan 23 2008 Pixel <pixel@mandriva.com> 1.15-1mdv2008.1
+ Revision: 157016
- 1.15:
- monitor-probe:
  o probe "using DMI" before "using X"
- monitor-probe-using-X:
  o in last resort, get Intel BIOS mode when "BIOS panel mode is bigger than
    probed programmed mode"

* Thu Jan 10 2008 Pixel <pixel@mandriva.com> 1.14-1mdv2008.1
+ Revision: 147502
- 1.14:
- monitor-edid, monitor-get-edid:
  o call monitor-get-edid-using-vbe with a range of ports, it stops on first
    success (by default it tries port 0 then port 1)

* Tue Jan 08 2008 Pixel <pixel@mandriva.com> 1.13-1mdv2008.1
+ Revision: 146846
- 1.13:
- monitor-get-edid:
  o skip /proc/acpi/video/**/EDID files which can't be valid (#34417)
  o minimal support for getting EDID from different DDC port
    (experimental, need testing before using it in monitor-edid)

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

  + Thierry Vignaud <tvignaud@mandriva.com>
    - kill re-definition of %%buildroot on Pixel's request

* Sat Dec 15 2007 Remi Collet <rpms@famillecollet.com> 1.11-1.fc8.remi
- build for Fedora 8

* Wed Sep 26 2007 Pixel <pixel@mandriva.com> 1.12-1mdv2008.0
+ Revision: 93044
- use make install
- 1.12:
- monitor-probe-using-X:
  o when an EDID is found in Xorg.log, pass it to monitor-parse-edid
  o handle --perl option (passed to monitor-parse-edid)

* Fri Mar 30 2007 Remi Collet <rpms@famillecollet.com> 1.11-1
- build for Fedora 3-6 and RedHat EL 2-5

* Thu Aug 31 2006 Gwenole Beauchesne <gbeauchesne@mandriva.com> 1.11-1mdv2007.0
- fix ballback to old get_edid() function
- ignore VBIOS checksum failures, use CPU emulator in that case

* Tue Jul 11 2006 Pixel <pixel@mandriva.com> 1.10-1mdv2007.0
- use a fixed FontPath (do not default to unix:-1 in case xfs is not running)

* Wed Jun 07 2006 Per Øyvind Karlsen <pkarlsen@mandriva.com> 1.9-5mdv2007.0
- do not build on sparc
- build with $RPM_OPT_FLAGS
- do parallell build
- cosmetics

* Wed May 10 2006 Pixel <pixel@mandriva.com> 1.9-4mdk
- fix a segfault occuring on some boxes in monitor-get-edid-using-vbe, 
  when using try-in-console

* Fri Mar 10 2006 Pixel <pixel@mandriva.com> 1.9-3mdk
- set url to wiki page instead of the cvs

* Fri Jan  6 2006 Pixel <pixel@mandriva.com> 1.9-2mdk
- add missing monitor-get-edid

* Thu Jan  5 2006 Pixel <pixel@mandriva.com> 1.9-1mdk
- monitor-get-edid is now a perl script able to probe /proc/acpi/video
  (or /proc/device-tree on PPC)
- binary monitor-get-edid is now monitor-get-edid-using-vbe
- monitor-edid is able to get more than one head

* Mon Aug  8 2005 Pixel <pixel@mandriva.com> 1.5-1mdk
- add option --try-in-console when probing edid
  since probing edid sometimes only work in console
- use this option by default in monitor-probe

* Wed Apr  6 2005 Pixel <pixel@mandrakesoft.com> 1.4-1mdk
- default on old lrmi code to get ddc via int10
- fix build on vesa-cvt

* Fri Mar 25 2005 Pixel <pixel@mandrakesoft.com> 1.3-1mdk
- added vesa-cvt (allowing to compute reduced-blanking timings)

* Thu Mar 17 2005 Pixel <pixel@mandrakesoft.com> 1.2-1mdk
- new release (added monitor-probe and monitor-probe-using-X)

* Tue Mar  8 2005 Pixel <pixel@mandrakesoft.com> 1.1-1mdk
- new release

* Wed Feb 23 2005 Pixel <pixel@mandrakesoft.com> 1.0-1mdk
- first package
