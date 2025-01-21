Name: sane-frontends
Version: 1.0.14
Release: 52%{?dist}
Summary: Graphical frontend to SANE
URL: http://www.sane-project.org

# Repacked the upstream source to remove bundled glibc functions
# reported here https://gitlab.com/sane-project/frontends/-/merge_requests/11
#Source0: ftp://ftp.sane-project.org/pub/sane/%%{name}-%%{version}/%%{name}-%%{version}.tar.gz
Source0: %{name}-%{version}-repacked.tar.gz

# Fix array subscript out of bounds errors (#133121).
# Upstream commit 5113e3de39846a8226909088ad5c1aa4969f3030 and commit
# 7336b064653026171a715dfaf803693b638c67a5 (partial)
Patch0: sane-frontends-1.0.14-array-out-of-bounds.patch
# Fix building with sane-backends >= 1.0.20.
# Upstream commit 5e96223e497538d06e18d8e84b774c4a35f654b4 (partial) and commit
# c554cfce37e37a33f94a9051afe2062c4759072b
Patch1: sane-frontends-1.0.14-sane-backends-1.0.20.patch
# Describe correct option names in xcam man page.
# Upstream commit 7e079e377174826453a1041719fb347d69d3ba5f
Patch2: sane-frontends-1.0.14-xcam-man.patch
# 1837961 - [abrt] sane-frontends: operator delete(): scanadf killed by SIGSEGV
# original PR https://gitlab.com/sane-project/frontends/-/merge_requests/1 (bz1837961)
# updated PR https://gitlab.com/sane-project/frontends/-/merge_requests/7 (bz2133813)
Patch3: frontends-scanadf-segv.patch
Patch4: sane-frontends-configure-c99.patch
Patch5: sane-frontends-c99.patch
# 2225209 - scanadf crashes when showing help for specific device
# https://gitlab.com/sane-project/frontends/-/merge_requests/12
Patch6: 0001-src-scanadf.c-Fix-segfault-when-scanadf-h-d-device.patch

License: GPL-2.0-or-later AND GPL-2.0-or-later WITH SANE-exception
# gcc is no longer in buildroot by default
BuildRequires: gcc
# use for autosetup
BuildRequires: git-core
# uses make
BuildRequires: make

BuildRequires: gtk2-devel
BuildRequires: sane-backends-devel >= 1.0.19-15

%description
This packages includes the scanadf and xcam programs.

%prep
%autosetup -S git

%build
%configure --with-gnu-ld --prefix=%{_prefix} --sysconfdir=%{_sysconfdir} --mandir=%{_mandir}
%make_build

%install
%make_install

# Not xscanimage; use xsane instead.
rm -f %{buildroot}%{_bindir}/xscanimage
rm -f %{buildroot}%{_mandir}/man1/xscanimage*
rm -f %{buildroot}%{_datadir}/sane/sane-style.rc

%files
%doc AUTHORS README
%license COPYING
%{_bindir}/scanadf
%{_bindir}/xcam
%{_mandir}/man1/scanadf.1.gz
%{_mandir}/man1/xcam.1.gz
# there is no desktop file for xcam because while it is a GUI program it is
# intended to be used from the command line

%changelog
* Sun Jan 19 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.14-52
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Sat Jul 20 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.14-51
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Sat Jan 27 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.14-50
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Aug 30 2023 Zdenek Dohnal <zdohnal@redhat.com> - 1.0.14-49
- applied accepted license exception

* Wed Jul 26 2023 Zdenek Dohnal <zdohnal@redhat.com> - 1.0.14-48
- 2225209 - scanadf crashes when showing help for specific device

* Sat Jul 22 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.14-47
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Feb 09 2023 Zdenek Dohnal <zdohnal@redhat.com> - 1.0.14-46
- update License tag to SPDX name and unbundle glibc funcs

* Sat Jan 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.14-45
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Tue Jan 17 2023 Florian Weimer <fweimer@redhat.com> - 1.0.14-44
- Fix C99 compatibility issues

* Wed Oct 12 2022 Zdenek Dohnal <zdohnal@redhat.com> - 1.0.14-43
- 2133813 - scanadf crashes on device enumeration

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.14-42
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Sat Jan 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.14-41
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.14-40
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.14-39
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Thu Nov 05 2020 Zdenek Dohnal <zdohnal@redhat.com> - 1.0.14-38
- make is no longer in buildroot by default

* Thu Aug 20 2020 Zdenek Dohnal <zdohnal@redhat.com> - 1.0.14-37
- 1837961 - [abrt] sane-frontends: operator delete(): scanadf killed by SIGSEGV

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.14-36
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jul 14 2020 Tom Stellard <tstellar@redhat.com> - 1.0.14-35
- Use make macros
- https://fedoraproject.org/wiki/Changes/UseMakeBuildInstallMacro

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.14-34
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.14-33
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.14-32
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Tue Jul 24 2018 Zdenek Dohnal <zdohnal@redhat.com> - 1.0.14-31
- correcting license

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.14-30
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Mon Feb 19 2018 Zdenek Dohnal <zdohnal@redhat.com> - 1.0.14-29
- gcc is no longer in buildroot by default

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.14-28
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Feb 08 2018 Zdenek Dohnal <zdohnal@redhat.com> - 1.0.14-27
- remove old stuff

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.14-26
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.14-25
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.14-24
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.14-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Jun 19 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.14-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Mon Aug 18 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.14-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.14-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Thu May 29 2014 Tom Callaway <spot@fedoraproject.org> - 1.0.14-19
- update lib/snprintf.c to resolve licensing issue (#1102522)

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.14-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Mon Jul 08 2013 Nils Philippsen <nils@redhat.com> - 1.0.14-17
- add comments to patches
- describe correct option names in xcam man page

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.14-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.14-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Tue Apr 03 2012 Nils Philippsen <nils@redhat.com> - 1.0.14-14
- clean up:
  - don't BR: gimp-devel, R: sane-backends
  - get rid of buildroot, %%makeinstall and %%clean section
  - dont obsolete/provide "sane" (ancient)

* Tue Jan 10 2012 Nils Philippsen <nils@redhat.com> - 1.0.14-13
- rebuild for gcc 4.7

* Mon Nov 07 2011 Nils Philippsen <nils@redhat.com> - 1.0.14-12
- rebuild (libpng)

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.14-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Fri Feb 26 2010 Nils Philippsen <nils@redhat.com> - 1.0.14-10
- add missing documentation files AUTHORS, COPYING, README
- don't distribute sane-style.rc
- use %%buildroot consistently
- explain missing xcam.desktop file

* Mon Aug 03 2009 Nils Philippsen <nils@redhat.com> 1.0.14-9
- remove ExcludeArch: s390 s390x

* Fri Jul 31 2009 Nils Philippsen <nils@redhat.com> 1.0.14-8
- replace badcode with array-out-of-bounds patch
- fix compilation with sane-backends-1.0.20

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.14-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Mon Mar 02 2009 Nils Philippsen <nils@redhat.com> 1.0.14-6
- don't require libieee2384-devel, libjpeg-devel but require fixed
  sane-backends-devel for building

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org>
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Thu Sep  4 2008 Tom "spot" Callaway <tcallawa@redhat.com> - 1.0.14-5
- fix license tag

* Tue Feb 19 2008 Fedora Release Engineering <rel-eng@fedoraproject.org> - 1.0.14-4
- Autorebuild for GCC 4.3

* Tue Apr 24 2007 Nils Philippsen <nphilipp@redhat.com> 1.0.14-3
- merge review (#226389):
  - add version info to obsoletes/provides
  - no config files in /usr
  - use %%configure macro
- add dist tag

* Thu Mar 15 2007 Karsten Hopp <karsten@redhat.com> 1.0.14-2
- rebuild with current gtk2 to add png support (#232013)

* Wed Jul 12 2006 Jesse Keating <jkeating@redhat.com> - 1.0.14-1.2.2
- rebuild

* Fri Feb 10 2006 Jesse Keating <jkeating@redhat.com> - 1.0.14-1.2.1
- bump again for double-long bug on ppc(64)

* Tue Feb 07 2006 Jesse Keating <jkeating@redhat.com> - 1.0.14-1.2
- rebuilt for new gcc4.1 snapshot and glibc changes

* Fri Dec 09 2005 Jesse Keating <jkeating@redhat.com>
- rebuilt

* Mon Nov 21 2005 Nils Philippsen <nphilipp@redhat.com> 1.0.14-1
- version 1.0.14
- fix build requires
- update badcode patch

* Wed Mar  2 2005 Tim Waugh <twaugh@redhat.com> 1.0.13-2
- Rebuild for new GCC.

* Mon Nov  8 2004 Tim Waugh <twaugh@redhat.com> 1.0.13-1
- 1.0.13.

* Mon Sep 27 2004 Tim Waugh <twaugh@redhat.com> 1.0.12-4
- Fixed mistaken array op (bug #133121).

* Sat Jun 19 2004 Jeremy Katz <katzj@redhat.com> - 1.0.12-3
- remove no longer valid requires on old gtk+ and gimp

* Tue Jun 15 2004 Elliot Lee <sopwith@redhat.com>
- rebuilt

* Wed Jun  2 2004 Tim Waugh <twaugh@redhat.com> 1.0.12-1
- 1.0.12.

* Wed May 12 2004 Tim Waugh <twaugh@redhat.com>
- s/ftp.mostang.com/ftp.sane-project.org/.

* Fri Feb 13 2004 Elliot Lee <sopwith@redhat.com>
- rebuilt

* Tue Oct 21 2003 Florian La Roche <Florian.LaRoche@redhat.de>
- BuildReq: libieee1284-devel, it seems to get picked up if available

* Mon Sep 29 2003 Tim Waugh <twaugh@redhat.com>
- Updated URL.

* Wed Jun 04 2003 Elliot Lee <sopwith@redhat.com>
- rebuilt

* Tue Apr 29 2003 Tim Waugh <twaugh@redhat.com> 1.0.11-1
- 1.0.11.

* Mon Mar 24 2003 Tim Waugh <twaugh@redhat.com> 1.0.10-2
- Don't require a specific version of sane-backends.

* Thu Mar 20 2003 Tim Waugh <twaugh@redhat.com> 1.0.10-1
- 1.0.10.

* Wed Jan 22 2003 Tim Powers <timp@redhat.com>
- rebuilt

* Fri Oct 25 2002 Tim Waugh <twaugh@redhat.com> 1.0.9-1
- 1.0.9.

* Fri Jun 21 2002 Tim Powers <timp@redhat.com>
- automated rebuild

* Thu Jun 20 2002 Tim Waugh <twaugh@redhat.com> 1.0.8-3
- Don't explicitly strip binaries (bug #62565).

* Wed Jun 12 2002 Tim Waugh <twaugh@redhat.com> 1.0.8-2
- Rebuild to fix bug #66129.

* Tue May 28 2002 Tim Waugh <twaugh@redhat.com> 1.0.8-1
- 1.0.8.

* Sun May 26 2002 Tim Powers <timp@redhat.com>
- automated rebuild

* Wed May 22 2002 Tim Waugh <twaugh@redhat.com> 1.0.8-0.20020522.1
- Update to CVS.  Release expected before the end of the month.
- Don't ship xscanimage any longer.

* Thu Feb 21 2002 Tim Waugh <twaugh@redhat.com> 1.0.7-2
- Rebuild in new environment.

* Mon Feb  4 2002 Tim Waugh <twaugh@redhat.com> 1.0.7-1
- 1.0.7.

* Sun Jan 27 2002 Tim Waugh <twaugh@redhat.com> 1.0.7-0.beta2.1
- 1.0.7-beta2.

* Wed Jan 23 2002 Tim Waugh <twaugh@redhat.com> 1.0.7-0.beta1.1
- 1.0.7-beta1.
- No longer need the fpe patch.

* Fri Nov 30 2001 Tim Waugh <twaugh@redhat.com> 1.0.6-2
- Fix a floating point exception (bug #56536).

* Mon Nov  5 2001 Tim Waugh <twaugh@redhat.com> 1.0.6-1
- 1.0.6.

* Sun Jul  1 2001 Tim Waugh <twaugh@redhat.com> 1.0.5-1
- 1.0.5.
- Change Copyright: to License:.

* Thu Jun  7 2001 Tim Waugh <twaugh@redhat.com> 1.0.5-0.20010605
- CVS snapshot 2001-06-05.
- Don't install xscanimage plug-in symlinks.  The old sane package never
  used to do this, and it looks confusing in gimp if you also have
  xsane-gimp (which is better) installed.  xscanimage works stand-alone
  anyhow.

* Sun Jun  3 2001 Tim Waugh <twaugh@redhat.com> 1.0.5-0.20010603.1000
- CVS snapshot 2001-06-03 10:00.

* Sat Jun  2 2001 Tim Waugh <twaugh@redhat.com> 1.0.5-0.20010530
- Built for Red Hat Linux.
- CVS snapshot 2001-05-30.

* Mon Jan 08 2001 Francis Galiegue <fg@mandrakesoft.com> 1.0.4-2mdk

- Summary now capitalised
- BuildRequires: sane (for sane-config)

