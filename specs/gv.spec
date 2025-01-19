Summary: A X front-end for the Ghostscript PostScript(TM) interpreter
Name: gv
Version: 3.7.4
Release: 36%{?dist}
# Automatically converted from old format: GPLv3+ - review is highly recommended.
License: GPL-3.0-or-later
%if 0%{?fedora} || 0%{?rhel} >= 8
Requires: ghostscript-x11
%else
Requires: ghostscript
%endif
URL: http://www.gnu.org/software/gv/
Source0: ftp://ftp.gnu.org/gnu/gv/gv-%{version}.tar.gz
#Source0: ftp://alpha.gnu.org/gnu/gv/gv-%{version}.tar.gz
Source1: gv.png
# Check for null pointers in resource requests
# https://savannah.gnu.org/bugs/?38727
Patch0:  gv-resource.patch
# Change tab to space in gv_user_res.dat
# http://savannah.gnu.org/patch/?7998
Patch1:  gv-dat.patch
# Support aarch64
Patch2:  gv-aarch64.patch
# Fix bounding box recognition
Patch3:  gv-bounding-box.patch
# Fix NULL access segfault
# https://bugzilla.redhat.com/show_bug.cgi?id=1071238
Patch4:  gv-bug1071238.patch
# Fix PDF printing
# https://bugzilla.redhat.com/show_bug.cgi?id=1536211
Patch5:  gv-bz1536211.patch
# Fix buffer overflows in resource.c
# https://savannah.gnu.org/patch/?10096
Patch6:  gv-overflow.patch
BuildRequires:  gcc
BuildRequires: /usr/bin/makeinfo
BuildRequires: Xaw3d-devel
BuildRequires: libXinerama-devel
BuildRequires: zlib-devel, bzip2-devel
BuildRequires: desktop-file-utils
BuildRequires: make

%description
GNU gv is a user interface for the Ghostscript PostScript(TM) interpreter.
Gv can display PostScript and PDF documents on an X Window System.


%prep
%setup -q
%patch -P0 -p1 -b .resource
%patch -P1 -p1 -b .resdat
%patch -P2 -p1 -b .aarch64
%patch -P3 -p2 -b .bounding-box
%patch -P4 -p1 -b .bug1071238
%patch -P5 -p1 -b .bz1536211
%patch -P6 -p2 -b .overflow


%build
%configure
%make_build


%install
%make_install

#Still provide link
ln $RPM_BUILD_ROOT%{_bindir}/gv $RPM_BUILD_ROOT%{_bindir}/ghostview

mkdir -p $RPM_BUILD_ROOT%{_datadir}/applications

cat > gv.desktop <<EOF
[Desktop Entry]
Name=GNU GV PostScript/PDF Viewer
GenericName=PostScript/PDF Viewer
Comment="View PostScript and PDF files"
Type=Application
Icon=gv
MimeType=application/postscript;application/pdf;
StartupWMClass=GV
Exec=gv %f
EOF

desktop-file-install \
       --add-category=Applications\
       --add-category=Graphics \
       --dir %{buildroot}%{_datadir}/applications/ \
       gv.desktop

#Icon
mkdir -p $RPM_BUILD_ROOT%{_datadir}/pixmaps
cp -p %SOURCE1 $RPM_BUILD_ROOT%{_datadir}/pixmaps

# Remove info dir file
rm -f ${RPM_BUILD_ROOT}%{_infodir}/dir

%files
%license COPYING
%doc AUTHORS ChangeLog NEWS README
%{_bindir}/ghostview
%{_bindir}/gv
%{_bindir}/gv-update-userconfig
%{_datadir}/gv/
%{_datadir}/applications/gv.desktop
%{_datadir}/info/gv.info.gz
%{_datadir}/pixmaps/gv.png
%{_mandir}/man1/gv.*
%{_mandir}/man1/gv-update-userconfig.*


%changelog
* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 3.7.4-36
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Thu Jul 25 2024 Miroslav Suchý <msuchy@redhat.com> - 3.7.4-35
- convert license to SPDX

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 3.7.4-34
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Wed Jan 24 2024 Fedora Release Engineering <releng@fedoraproject.org> - 3.7.4-33
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sat Jan 20 2024 Fedora Release Engineering <releng@fedoraproject.org> - 3.7.4-32
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 3.7.4-31
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 3.7.4-30
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 3.7.4-29
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 3.7.4-28
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Sep 16 2021 Orion Poplawski <orion@nwra.com> - 3.7.4-27
- Add patch to fix buffer overflows

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 3.7.4-26
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Sat Jan 30 2021 Orion Poplawski <orion@nwra.com> - 3.7.4-25
- Require ghostscript-x11 on EL8 (bz#1918041)

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 3.7.4-24
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.7.4-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.7.4-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Mon Nov 18 2019 Orion Poplawski <orion@nwra.com> - 3.7.4-21
- Add patch properly to fix PDF printing (bz#1536211)

* Thu Nov 14 2019 Orion Poplawski <orion@nwra.com> - 3.7.4-20
- Add patch to fix PDF printing (bz#1536211)
- Modernize spec

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.7.4-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.7.4-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.7.4-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Jun 14 2018 Jason L Tibbitts III <tibbs@math.uh.edu> - 3.7.4-16
- Change dependency from ghostscript to ghostscript-x11 to match the
  reorganized ghostscript package.

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.7.4-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.7.4-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.7.4-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.7.4-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 3.7.4-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.7.4-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Aug 16 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.7.4-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.7.4-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Mon Mar 3 2014 Orion Poplawski <orion@cora.nwra.com> - 3.7.4-7
- Update to upstream's fix for zoom segfault (bug #1071238)

* Fri Feb 28 2014 Orion Poplawski <orion@cora.nwra.com> - 3.7.4-6
- Fix NULL access segfault (bug #1071238)

* Thu Jan 23 2014 Orion Poplawski <orion@cora.nwra.com> - 3.7.4-5
- Fix bounding box recognition with CR line terminators

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.7.4-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Tue Apr 16 2013 Orion Poplawski <orion@cora.nwra.com> - 3.7.4-3
- Add patch to change tab to space in gv_user_res.dat
- Add patch to support aarch64 (bug #925536)

* Mon Apr 15 2013 Orion Poplawski <orion@cora.nwra.com> - 3.7.4-2
- Add patch to fix segfault in cases of missing resources

* Mon Mar 18 2013 Orion Poplawski <orion@cora.nwra.com> - 3.7.4-1
- Update to 3.7.4

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.7.3.90-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Tue Feb 12 2013 Orion Poplawski <orion@cora.nwra.com> - 3.7.3.90-4
- Drop vendor from desktop file

* Wed Jan 9 2013 Orion Poplawski <orion@cora.nwra.com> - 3.7.3.90-3
- Add filename argument to desktop file exec option (bug #890851)

* Fri Jul 27 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.7.3.90-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Thu Apr 5 2012 Orion Poplawski <orion@cora.nwra.com> - 3.7.3.90-1
- Update to 3.7.3.90
- Drop Xaw3d patch applied upstream

* Sun Feb 26 2012 Orion Poplawski <orion@cora.nwra.com> - 3.7.3-3
- Rebuild with Xaw3d 1.6.1
- Add patch from Gentoo for Xawd3d 1.6

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.7.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Fri Dec 2 2011 Orion Poplawski <orion@cora.nwra.com> 3.7.3-1
- Update to 3.7.3

* Wed Oct 26 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.7.2-2
- Rebuilt for glibc bug#747377

* Mon May 2 2011 Orion Poplawski <orion@cora.nwra.com> 3.7.2-1
- Update to 3.7.2

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.7.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Mon Nov 8 2010 Orion Poplawski <orion@cora.nwra.com> 3.7.1-2
- Re-enable international support

* Mon Jun 28 2010 Orion Poplawski <orion@cora.nwra.com> 3.7.1-1
- Update to 3.7.1
- Disable international support to avoid segfault on exit until
  bug 587349 is fixed

* Thu Jun 3 2010 Orion Poplawski <orion@cora.nwra.com> 3.6.91-1
- Update to 3.6.91 to fix CVE-2010-2055 and CVE-2010-2056

* Mon Apr 26 2010 Orion Poplawski <orion@cora.nwra.com> 3.6.9-1
- Update to 3.6.9

* Tue Mar 2 2010 Orion Poplawski <orion@cora.nwra.com> 3.6.8-2
- Ship icon, update desktop file

* Mon Dec 28 2009 Orion Poplawski <orion@cora.nwra.com> 3.6.8-1
- Update to 3.6.8

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.6.7-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Tue Mar 24 2009 Orion Poplawski <orion@cora.nwra.com> 3.6.7-1
- Update to 3.6.7

* Tue Feb 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.6.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Tue Oct 21 2008 Orion Poplawski <orion@cora.nwra.com> 3.6.6-1
- Update to 3.6.6
- Add extra neede BuildRequires
- Remove upstreamed patches
- Fix license - GPLv3+

* Wed Aug 6 2008 Orion Poplawski <orion@cora.nwra.com> 3.6.5-3
- Apply upstream patch to display more error messages

* Fri Jul 18 2008 Orion Poplawski <orion@cora.nwra.com> 3.6.5-2
- Change install dir patch to be more palatable for upstream

* Thu Jul 17 2008 Orion Poplawski <orion@cora.nwra.com> 3.6.5-1
- Update to 3.6.5

* Mon Jun 2 2008 Orion Poplawski <orion@cora.nwra.com> 3.6.4-1
- Update to 3.6.4
- Cleanup desktop file a little

* Sat Feb  9 2008 Orion Poplawski <orion@cora.nwra.com> 3.6.3-3
- Rebuild for gcc 3.4

* Tue Aug 21 2007 Orion Poplawski <orion@cora.nwra.com> 3.6.3-2
- Update license tag to GPLv2+
- Rebuild for ppc32

* Fri Jun 29 2007 Orion Poplawski <orion@cora.nwra.com> 3.6.3-1
- Update to 3.6.3

* Tue Dec  5 2006 Orion Poplawski <orion@cora.nwra.com> 3.6.2-2
- Apply patch from Mandriva to fix CVE-2006-5864/bug 215136

* Wed Oct 11 2006 Orion Poplawski <orion@cora.nwra.com> 3.6.2-1
- Update to 3.6.2

* Tue Aug 29 2006 Orion Poplawski <orion@cora.nwra.com> 3.6.1-8
- Rebuild for FC6

* Mon Feb 13 2006 Orion Poplawski <orion@cora.nwra.com> 3.6.1-7
- Rebuild for gcc/glibc changes

* Wed Feb  1 2006 Orion Poplawski <orion@cora.nwra.com> 3.6.1-6
- Remove info dir file

* Wed Dec 21 2005 Orion Poplawski <orion@cora.nwra.com> 3.6.1-5
- Rebuild

* Thu Oct 27 2005 Orion Poplawski <orion@cora.nwra.com> 3.6.1-4
- Add patch find app defaults file (#171848)
- Add BR: /usr/bin/makeinfo to properly build .info file (#171849)

* Thu Oct 20 2005 Orion Poplawski <orion@cora.nwra.com> 3.6.1-3
- Fixup .desktop file, add Comment and StartupWMClass

* Thu Oct 20 2005 Orion Poplawski <orion@cora.nwra.com> 3.6.1-2
- Trim install paragraph from Description
- Add MimeType to desktop and update mime and desktop databases
- Fix info file handling

* Mon Oct 17 2005 Orion Poplawski <orion@cora.nwra.com> 3.6.1-1
- Updated to 3.6.1
- Fedora Extras version

* Sun Sep 19 2004 Dan Williams <dcbw@redhat.com> 3.5.8-29
- Fix .desktop file (#125849)

* Tue Jun 15 2004 Elliot Lee <sopwith@redhat.com>
- rebuilt

* Fri May 14 2004 Dan Williams <dcbw@redhat.com> 3.5.8-27
- display empty page when input file has size 0 (#100538)

* Fri May 14 2004 Dan Williams <dcbw@redhat.com> 3.5.8-26
- fix argv array size (#80672)

* Tue May  4 2004 Bill Nottingham <notting@redhat.com> 3.5.8-25
- fix desktop file (#120190)

* Fri Feb 13 2004 Elliot Lee <sopwith@redhat.com>
- rebuilt

* Wed Jun 04 2003 Elliot Lee <sopwith@redhat.com>
- rebuilt

* Wed Jan 22 2003 Tim Powers <timp@redhat.com>
- rebuilt

* Thu Dec 12 2002 Tim Powers <timp@redhat.com> 3.5.8-21
- rebuild on all arches

* Tue Nov 19 2002 Bill Nottingham <notting@redhat.com> 3.5.8-20
- rebuild

* Tue Sep 24 2002 Bill Nottingham <notting@redhat.com>
- fix handling of certain postscript/pdf headers
- use mkstemp

* Fri Jun 21 2002 Tim Powers <timp@redhat.com>
- automated rebuild

* Wed Jun 12 2002 Bill Nottingham <notting@redhat.com>
- remove anti-aliasing change; it causes problems

* Thu May 23 2002 Tim Powers <timp@redhat.com>
- automated rebuild

* Thu Feb 21 2002 Bill Nottingham <notting@redhat.com>
- rebuild

* Fri Jan 25 2002 Bill Nottingham <notting@redhat.com>
- fix anti-aliasing (#58686)

* Fri Jul 13 2001 Bill Nottingham <notting@redhat.com>
- fix some build issues (#48983, #48984)

* Thu Jul 13 2000 Prospector <bugzilla@redhat.com>
- automatic rebuild

* Fri Jun  9 2000 Bill Nottingham <notting@redhat.com>
- add filename quoting patch from debian
- rebuild in new build environment

* Mon May  8 2000 Bernhard Rosenkraenzer <bero@redhat.com>
- rebuild with new libXaw3d

* Mon Feb 07 2000 Preston Brown <pbrown@redhat.com>
- wmconfig -> desktop

* Thu Feb  3 2000 Bill Nottingham <notting@redhat.com>
- handle compressed man pages

* Sun Mar 21 1999 Cristian Gafton <gafton@redhat.com> 
- auto rebuild in the new build environment (release 7)

* Mon Jan 25 1999 Michael Maher <mike@redhat.com>
- fixed bug #272, changed group

* Thu Dec 17 1998 Michael Maher <mike@redhat.com>
- built pacakge for 6.0

* Sat Aug 15 1998 Jeff Johnson <jbj@redhat.com>
- build root

* Fri May 08 1998 Prospector System <bugs@redhat.com>
- translations modified for de, fr, tr

* Fri Apr 10 1998 Cristian Gafton <gafton@redhat.com>
- Manhattan build

* Thu Nov 06 1997 Cristian Gafton <gafton@redhat.com>
- we are installin a symlink to ghostview

* Wed Oct 22 1997 Cristian Gafton <gafton@redhat.com>
- updated to 3.5.8

* Thu Jul 17 1997 Erik Troan <ewt@redhat.com>
- built against glibc

* Tue Apr 15 1997 Erik Troan <ewt@redhat.com>
- added ghostscript requirement, added errlist patch for glibc.
