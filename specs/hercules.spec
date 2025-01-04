Summary: Hercules S/370, ESA/390, and z/Architecture emulator
Name: hercules
Version: 3.13
Release: 19%{?dist}
# Automatically converted from old format: QPL - review is highly recommended.
License: QPL-1.0
URL: http://www.hercules-390.eu/
Source0: http://downloads.hercules-390.eu/%{name}-%{version}.tar.gz
Source1: hercules.cnf
Source2: hercules-run
Source3: README-rpm
Source4: generic.prm
Patch0: %{name}-3.10-fedora.patch
Patch1: hercules-configure-c99.patch
BuildRequires: zlib-devel
BuildRequires: bzip2-devel
BuildRequires: libcap-devel
BuildRequires: libtool
BuildRequires: libtool-ltdl-devel
BuildRequires: make
Conflicts: sdl-hercules
Conflicts: sdl-hercules-data

%description
Hercules is an emulator for the IBM System/370, ESA/390, and z/Architecture
series of mainframe computers. It is capable of running any IBM operating
system and applications that a real system will run, as long as the hardware
needed is emulated. Hercules can emulate FBA and CKD DASD, tape, printer,
card reader, card punch, channel-to-channel adapter, LCS Ethernet, and
printer-keyboard, 3270 terminal, and 3287 printer devices.


%prep
%setup -q

%patch -P0 -p1 -b .fedora
%patch -P1 -p1

rm autoconf/libtool.m4
autoreconf -f -i

# remove unbundled stuff
rm ltdl.[ch]

# Scripts to be looked at, not executed from the docs
chmod -x util/*
# remove Makefile
rm util/Makefile*


%build
%configure \
    --enable-external-gui \
    --enable-optimization="%{optflags}"

make %{?_smp_mflags} V=1


%install
make install DESTDIR=%{buildroot}

mkdir -p %{buildroot}%{_sysconfdir}/hercules
# Install config files
install -p -m 0644 %{SOURCE1} %{buildroot}%{_sysconfdir}/hercules/
install -p -m 0644 %{SOURCE4} %{buildroot}%{_sysconfdir}/hercules/

# Install our wrapper script (takes care of tunnel networking)
install -D -p -m 0755 %{SOURCE2} %{buildroot}%{_sbindir}/hercules-run

# Copy our README to be included as doc
install -p -m 0644 %{SOURCE3} README-rpm

# Create empty directory where to store system images
mkdir -p %{buildroot}%{_sharedstatedir}/hercules

# Remove Makefile from html docs
rm html/Makefile*

# Remove libtool archives
rm %{buildroot}%{_libdir}/hercules/*.la
rm %{buildroot}%{_libdir}/*.la


%files
%doc COPYRIGHT README-rpm
%doc README.{COMMADPT,ECPSVM,HDL,HERCLOGO,NETWORKING,TAPE}
%doc RELEASE.NOTES hercules.cnf html/ util/
%dir %{_sysconfdir}/hercules/
%attr(0644, root, root) %config(noreplace) %{_sysconfdir}/hercules/hercules.cnf
%attr(0644, root, root) %config(noreplace) %{_sysconfdir}/hercules/generic.prm
%{_bindir}/*
%{_sbindir}/*
%{_datadir}/hercules/
%dir %{_libdir}/hercules/
%{_libdir}/hercules/*.so
%{_libdir}/*.so
%{_mandir}/man?/*
%dir %{_sharedstatedir}/hercules/


%changelog
* Wed Jan 01 2025 Davide Cavalca <dcavalca@fedoraproject.org> - 3.13-19
- Conflict with the sdl-hercules packages
- Drop old comments that trigger a FTBFS due to macro expansion
  Fixes: RHBZ#2300839

* Wed Aug 07 2024 Miroslav Suchý <msuchy@redhat.com> - 3.13-18
- convert license to SPDX

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 3.13-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Wed Jan 24 2024 Fedora Release Engineering <releng@fedoraproject.org> - 3.13-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sat Jan 20 2024 Fedora Release Engineering <releng@fedoraproject.org> - 3.13-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 3.13-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Fri Mar 17 2023 Florian Weimer <fweimer@redhat.com> - 3.13-13
- Port configure script to C99

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 3.13-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 3.13-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 3.13-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 3.13-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 3.13-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.13-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.13-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.13-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.13-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.13-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.13-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Fri Sep 29 2017 Dan Horák <dan[at]danny.cz> - 3.13-1
- updated to 3.13

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.12-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.12-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.12-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 3.12-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Sun Nov 29 2015 Dan Horák <dan[at]danny.cz> - 3.12-1
- updated to 3.12

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.11-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Mon Sep 29 2014 Dan Horák <dan[at]danny.cz> - 3.11-1
- updated to 3.11 (#1142927)

* Sat Aug 16 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.10-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.10-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Feb 01 2014 Dan Horák <dan[at]danny.cz> - 3.10-1
- updated to 3.10 (#1060467)

* Tue Dec 03 2013 Dan Horák <dan[at]danny.cz> - 3.09-2
- fix build with -Werror=format-security (#1037121)

* Tue Jul 30 2013 Dan Horák <dan[at]danny.cz> - 3.09-1
- updated to 3.09 (#989939)

* Sat Jun 01 2013 Dan Horák <dan[at]danny.cz> - 3.08.2-2
- fix build on EL-6

* Fri May 31 2013 Dan Horák <dan[at]danny.cz> - 3.08.2-1
- updated to 3.08.2
- updated build system for aarch64 (#925546)
- add manual page for hercules (#962722)

* Fri Mar 15 2013 Dan Horák <dan[at]danny.cz> - 3.08.1-1
- updated to 3.08.1

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.08-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sat Dec 08 2012 Dan Horák <dan[at]danny.cz> - 3.08-1
- updated to 3.08
- remove firewall rules after hercules finish in the hercules-run wrapper script (#884311)

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.07-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.07-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.07-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Tue Mar 16 2010 Dan Horák <dan[at]danny.cz> 3.07-1
- updated to 3.07

* Tue Jan  5 2010 Dan Horák <dan[at]danny.cz> 3.06-9.20100105svn5591
- updated to svn revision 5591

* Sun Dec 27 2009 Dan Horák <dan[at]danny.cz> 3.06-8.20091227svn5570
- updated to svn revision 5570
- dropped the force-hfp-unnormalized patch, because the feature is now implemented

* Mon Dec 14 2009 Dan Horák <dan[at]danny.cz> 3.06-7.20091214svn5544
- updated to svn revision 5544
- added workaround for booting Fedora kernels requiring z9 or better
- spec cleanup
- updated default config

* Sat Sep 26 2009 Dan Horák <dan[at]danny.cz> 3.06-6
- rebuilt to use POSIX capabilities

* Thu Sep 17 2009 Dan Horák <dan[at]danny.cz> 3.06-5
- fixed module loading with libtool >= 2.0

* Mon Sep  7 2009 Dan Horák <dan[at]danny.cz> 3.06-4
- enable support for external gui

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.06-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Tue Feb 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.06-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Wed Feb 18 2009 Dan Horak <dan[at]danny.cz> 3.06-1
- update to upstream version 3.06
- use system ltdl library

* Thu Oct 09 2008 Dan Horak <dan[at]danny.cz> 3.05-7.20081009cvs
- update to CVS snapshot 20081009 (#461044)
- install utils only as docs
- little cleanup

* Thu Apr 10 2008 Jarod Wilson <jwilson@redhat.com> 3.05-5
- Point to new project URL
- Add a template generic.prm matching provided hercules.cnf

* Sun Feb  3 2008 Hans de Goede <j.w.r.degoede@hhs.nl> 3.05-4
- Fix loading of plugins (bz 430805)

* Wed Aug 22 2007 Matthias Saou <http://freshrpms.net/> 3.05-3
- Rebuild for new BuildID feature.

* Sun Aug 12 2007 Matthias Saou <http://freshrpms.net/> 3.05-2
- Include open patch.

* Sun Aug  5 2007 Matthias Saou <http://freshrpms.net/> 3.05-1
- Update to 3.05.

* Tue Jun 19 2007 Matthias Saou <http://freshrpms.net/> 3.04.1-5
- Update included README-rpm (was README.fedora) to remove Fedora instructions
  since after the Core+Extras merge, Fedora isn't built for x390 (#234803).
- Remove rpath at last (using sed on the libtool script method).

* Mon Aug 28 2006 Matthias Saou <http://freshrpms.net/> 3.04.1-4
- FC6 rebuild.

* Tue Aug  1 2006 Matthias Saou <http://freshrpms.net/> 3.04.1-3
- Don't assume we have a sane default umask... (#200838).
- Update the README.fedora to include more details + RHL and RHEL steps.
- Update hercules.cnf to fix dasdinit tip and missing CTCI line.

* Mon Jul  3 2006 Matthias Saou <http://freshrpms.net/> 3.04.1-2
- Move out all the inlined configuration files, keep only the .cnf file.
- Update .cnf file so that it works (load modules required for the default).
- Include README.fedora to give quick instructions on how to get started.
- Include empty %%{_var}/lib/hercules/ directory.
- Rename hercules.init to hercules-run in PATH and clean it up somewhat.

* Mon Jul  3 2006 Matthias Saou <http://freshrpms.net/> 3.04.1-1
- Update to 3.04.1 (useless, I know).
- Remove no longer needed libgcrypt dependency.
- Add explicit LDFLAGS to fix x86_64 compilation at last! (#185906)
- Pass --disable-rpath to configure.
- Update lib vs. lib64 hack since it's only needed in configure now.

* Tue Mar 14 2006 Matthias Saou <http://freshrpms.net/> 3.04-1
- Update to 3.04.

* Thu Feb  9 2006 Matthias Saou <http://freshrpms.net/> 3.03.1-1
- Update to 3.03.1.

* Sun May 22 2005 Jeremy Katz <katzj@redhat.com> - 3.02-3
- rebuild on all arches

* Fri Apr  7 2005 Michael Schwendt <mschwendt[AT]users.sf.net> 3.02-2
- rebuilt

* Tue Jan 25 2005 Matthias Saou <http://freshrpms.net/> 3.02-1
- Update to 3.02 final.

* Fri Dec 24 2004 Thomas Vander Stichele <thomas at apestaart dot org>
- scrubbed release tag

* Thu Dec  2 2004 Michael Schwendt <mschwendt[AT]users.sf.net>
- BR s/libgcrypt/libgcrypt-devel/

* Mon Oct 25 2004 Matthias Saou <http://freshrpms.net/> 3.02-0.20041025.1
- Update to today's CVS snapshot.

* Thu Jul 29 2004 Matthias Saou <http://freshrpms.net/> 3.01-2.20040729
- Update to CVS version.
- Merge the docs back into the main package.

* Sat Jul 17 2004 Matthias Saou <http://freshrpms.net/> 3.01-2
- Updated config's ctc entry to the new syntax.

* Sat Apr 10 2004 Dag Wieers <dag@wieers.com> - 3.01-1
- Updated to release 3.01.
- Added default configuration from Florian La Roche.

* Fri Oct 3 2003 Jay Maynard <jmaynard@conmicro.cx>
Updates for version 3.00: lots of libraries and executable changes.

* Thu Feb 6 2003 Jay Maynard <jmaynard@conmicro.cx>
Fixed permissions again. Thanks to John Summerfield for finding
my screwup and pointing it out.

* Sun Feb 2 2003 Jay Maynard <jmaynard@conmicro.cx>
Updates for 2.17: new files, RPM 4 updates to build specifications (thanks
to Florian La Roche), fixed default attributes (thanks again to John
Summerfield, and this time it'll stick!), and RPM 4 updates to file header
(thanks to Frank Meurer).

* Wed Jul 3 2002 Jay Maynard <jmaynard@conmicro.cx>
Added Alpha build kludge to bypass setresuid test in configure.

* Sat May 4 2002 Jay Maynard <jmaynard@conmicro.cx>
Removed enable-setuid-hercifc option (thanks again to John Summerfield).

* Fri Apr 19 2002 Jay Maynard <jmaynard@conmicro.cx>
Added new HTTP server files for 2.16.

* Thu Dec 20 2001 Jay Maynard <jmaynard@conmicro.cx>
Changed build process to include configure step.

* Sun May 7 2001 Jay Maynard <jmaynard@conmicro.cx>
Changed executables for Hercules 2.12; set default attributes (thanks to
John Summerfield).

* Sun Feb 3 2001 Jay Maynard <jmaynard@conmicro.cx>
Changed executables for Hercules 2.10.

* Sun Oct 8 2000 Jay Maynard <jmaynard@conmicro.cx>
Added multi-architecture build processing.

* Sun Jul 4 2000 Jay Maynard <jmaynard@conmicro.cx>
Added BuildRoot (thanks to David Barth).

* Sun Jun 18 2000 Jay Maynard <jmaynard@conmicro.cx>
Created RPM.
