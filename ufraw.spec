%if (0%{?fedora} >= 7 && 0%{?fedora} <= 19) || 0%{?rhel} == 6
%bcond_without cinepaint
%else
%bcond_with cinepaint
%endif

%global gimptool %{_bindir}/gimptool-2.0
%global gimpplugindir %(%___build_pre; %gimptool --gimpplugindir)/plug-ins

%if %{with cinepaint}
%global cinepaintplugindir %(pkg-config --variable=programplugindir cinepaint-gtk)/plug-ins
%endif

Summary: Raw image data retrieval tool for digital cameras
Name: ufraw
Version: 0.23
Release: 0.18.20210425%{?dist}
License: GPLv2+
URL: http://ufraw.sourceforge.net
Source0: http://downloads.sourceforge.net/ufraw/ufraw-0.22.tar.gz
# beautify_style.sh file is not in the ufraw-0.22.tar.gz, so we need add it, to apply diff from git without errors
Source1: https://raw.githubusercontent.com/sergiomb2/ufraw/02bc2df0c6c2d9d1892bd16a58e319d81e79559d/beautify_style.sh
Source2: ufraw.thumbnailer
Patch1:  https://github.com/sergiomb2/ufraw/compare/ufraw-0-22..f34669b.diff

BuildRequires: make
BuildRequires: automake
BuildRequires: libtool
BuildRequires: gettext-devel
BuildRequires: gcc-c++
BuildRequires: gimp-devel >= 2.2
BuildRequires: gimp >= 2.2
%if %{with cinepaint}
BuildRequires: cinepaint-devel >= 0.22
BuildRequires: cinepaint >= 0.22
%endif
BuildRequires: glib2-devel >= 2.12
BuildRequires: gtk2-devel >= 2.12
BuildRequires: gtkimageview-devel >= 1.6.1
BuildRequires: lcms2-devel
BuildRequires: libexif-devel >= 0.6.13
BuildRequires: exiv2-devel >= 0.18.1
BuildRequires: lensfun-devel >= 0.2.5
BuildRequires: libtiff-devel
BuildRequires: libjpeg-devel
BuildRequires: jasper-devel
BuildRequires: pkgconfig >= 0.9.0
BuildRequires: perl-interpreter
BuildRequires: gettext
BuildRequires: cfitsio-devel
Requires: ufraw-common = %{?epoch:%{epoch}:}%{version}-%{release}

Provides: bundled(dcraw) = 9.28


%description
UFRaw is a tool for opening raw format images of digital cameras.

%package common
Summary: Common files needed by UFRaw

%description common
The ufraw-common files includes common files for UFRaw, e.g. language support.

%package gimp
Summary: GIMP plugin to retrieve raw image data from digital cameras
Requires: ufraw-common = %{?epoch:%{epoch}:}%{version}-%{release}
Requires: gimp%{?_isa}

%description gimp
The ufraw-gimp package contains a GIMP plugin for opening raw format images of
digital cameras.

%if %{with cinepaint}
%package cinepaint
Summary: CinePaint plugin to retrieve raw image data from digital cameras
Requires: ufraw-common = %{?epoch:%{epoch}:}%{version}-%{release}
Requires: cinepaint%{?_isa}

%description cinepaint
The ufraw-cinepaint package contains a CinePaint plugin for opening raw format
images of digital cameras.
%else
Obsoletes: %{name}-cinepaint < 0.19.2-4
%endif

%prep
cat << EOF

Building UFRaw with these settings:
cinepaint:      %{with cinepaint}

EOF
%setup -qn ufraw-0.22
cp %{SOURCE1} .
%patch1 -p1

%build
autoreconf -i
%configure --enable-mime --enable-extras --enable-contrast --disable-silent-rules --enable-jasper

%make_build schemas_DATA=''

%install
%make_install schemas_DATA=''
# don't ship dcraw binary
rm -f %{buildroot}%{_bindir}/dcraw
install -d -m 0755 %buildroot%{_datadir}/mime/packages
install -m 0644 ufraw-mime.xml %buildroot%{_datadir}/mime/packages
pushd %{buildroot}%{_mandir}/man1
ln -s ufraw.1 ufraw-batch.1
popd
# install modern thumbnailer entry
install -D -m0644 %{SOURCE2} %{buildroot}%{_datadir}/thumbnailers/%{name}.thumbnailer

%find_lang %{name}

%files common -f %{name}.lang
%doc COPYING README
%{_datadir}/mime/packages/ufraw-mime.xml

%files
%{_bindir}/*
%{_datadir}/pixmaps/*
%{_datadir}/applications/*.desktop
%{_datadir}/appdata/*.appdata.xml
%{_datadir}/thumbnailers/%{name}.thumbnailer
%{_mandir}/man1/*

%files gimp
%{gimpplugindir}/ufraw-gimp

%if %{with cinepaint}
%files cinepaint
%{cinepaintplugindir}/ufraw-cinepaint
%endif

%changelog
* Wed Nov 01 2023 Yaakov Selkowitz <yselkowi@redhat.com> - 0.23-0.18.20210425
- Drop GConf2 schemas
- Register freedesktop thumbnailer

* Sat Jul 22 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.23-0.17.20210425
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Sat Jan 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.23-0.16.20210425
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Dec 29 2022 Maxwell G <gotmax@e.email> - 0.23-0.15.20210425
- Rebuild for cfitsio 4.2

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.23-0.14.20210425
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Sat Jan 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.23-0.13.20210425
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.23-0.12.20210425
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Sun Apr 25 2021 Sérgio Basto <sergio@serjux.com> - 0.23-0.11.20210425
- f34669b Fix build with autoconf-2.70
- 3bdd177 Add .gitignore
- 2618933 try fix warning: The macro `GLIB_GNU_GETTEXT' is obsolete.
- a581163 ufraw-boundary.patch
- 3d6eaf4 ufraw-glibc210.patch
- 33e3580 GCC 10/11 warnings eliminated
- 122257e more room for ljpeg row
- 188c8b5 Fix Index-out-of-bounds · LibRaw::nikon_load_raw
- 00f4cb4 autoupdate
- a8f76d3 C++11 requirements fix
- c56f8be Fix build against glib-2.68 fixes #10
- enable jasper

* Wed Feb 03 2021 Gwyn Ciesla <gwync@protonmail.com> - 0.23.0.10-20201114
- cfitsio rebuild.

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.23-0.9.20201114
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Sun Nov 15 2020 Sérgio Basto <sergio@serjux.com> - 0.23-0.8.20201114
- Update spec, remove support to el4 !

* Sat Nov 14 2020 Sérgio Basto <sergio@serjux.com> - 0.23-0.7.20201114
- Update to git 20201114 with ufraw-gimp: properly send EXIF data to Gimp 2.9
  and later and dcraw updated to 9.28

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.23-0.6.20190612
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Jan 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.23-0.5.20190612
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sat Jul 27 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.23-0.4.20190612
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Wed Jun 12 2019 Sérgio Basto <sergio@serjux.com> - 0.23-0.3.20190612
- Update to latest commit, some build fixes and minor change

* Fri Mar  8 2019 Tim Landscheidt <tim@tim-landscheidt.de> - 0.23-0.2
- Remove obsolete requirements for %%post/%%postun scriptlets

* Thu Feb 14 2019 Sérgio Basto <sergio@serjux.com> - 0.23-0.1
- The latest commits of ufraw made after 0.22 and some fixes found over the
  internet.
- Re-enable openmp.

* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.22-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Wed Jan 30 2019 Rex Dieter <rdieter@fedoraproject.org> - 0.22-15
- Pull in FTBFS fix for exiv2-0.27 (#1671153)
- use %%make_build %%make_install macros
- FTBFS related to openmp support on f30+, workaround with --disable-openmp (for now)

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.22-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Sat May 26 2018 Christian Dersch <lupinix@mailbox.org> - 0.22-13
- rebuilt for cfitsio 3.450

* Fri Feb 23 2018 Christian Dersch <lupinix@mailbox.org> - 0.22-12
- rebuilt for cfitsio 3.420 (so version bump)

* Tue Feb 20 2018 Nils Philippsen <nils@tiptoe.de> - 0.22-11
- require gcc, gcc-c++ for building

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.22-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.22-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.22-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Tue May 02 2017 Rex Dieter <rdieter@fedoraproject.org> - 0.22-7
- rebuild (exiv2)

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.22-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri Dec 30 2016 Sérgio Basto <sergio@serjux.com> - 0.22-5
- Fix rpmlint warning, ufraw.src:81: W: unversioned-explicit-provides
  bundled(dcraw)
- Add BR jasper-devel to fix the build in rawhide.

* Sun Dec 18 2016 Sérgio Basto <sergio@serjux.com> - 0.22-4
- Fix crash on destroy of lensfun object on PEF images (#1350210)

* Wed Oct 26 2016 Sérgio Basto <sergio@serjux.com> - 0.22-3
- Add 2 patches from upsteam and re-enable lensfun, rhbz#1350210

* Mon Jul 11 2016 Sérgio Basto <sergio@serjux.com> - 0.22-2
- Build without lensfun, rhbz #1350210, until we find a fix.

* Wed Feb 24 2016 Sérgio Basto <sergio@serjux.com> - 0.22-1
- Update to 0.22
- Drop Patch0 is upstreamed.
- Add 05_fix_build_due_to_unsigned_char.patch

* Fri Feb 05 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.21-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Tue Jan 19 2016 Nils Philippsen <nils@redhat.com>
- use %%global instead of %%define

* Sun Jan 03 2016 Rex Dieter <rdieter@fedoraproject.org> 0.21-4
- rebuild (lensfun)

* Wed Jun 24 2015 Rex Dieter <rdieter@fedoraproject.org> - 0.21-3
- rebuild (exiv2)

* Fri Jun 19 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.21-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Thu May 21 2015 Nils Philippsen <nils@redhat.com> - 0.21-1
- avoid writing past array boundaries when reading certain raw formats
  (CVE-2015-3885)

* Wed May 20 2015 Nils Philippsen <nils@redhat.com> - 0.21-1
- version 0.21
- don't manually specify, clean buildroot
- add Provides: bundled(dcraw)

* Thu May 14 2015 Nils Philippsen <nils@redhat.com> - 0.20-4
- rebuild for lensfun-0.3.1

* Wed May 13 2015 Nils Philippsen <nils@redhat.com> - 0.20-3
- rebuild for lensfun-0.3.0

* Sat May 02 2015 Kalev Lember <kalevlember@gmail.com> - 0.20-2
- Rebuilt for GCC 5 C++11 ABI change

* Tue Oct 07 2014 Nils Philippsen <nils@redhat.com> - 0.20-1
- version 0.20

* Mon Aug 18 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.19.2-16.20140414cvs
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Aug 09 2014 Rex Dieter <rdieter@fedoraproject.org> 0.19.2-15.20140414cvs
- optimize mime scriptlet, %%configure --disable-silent-rules

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.19.2-14.20140414cvs
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Tue Apr 29 2014 Nils Philippsen <nils@redhat.com> - 0.19.2-13
- fix tweaking color temperature, green value based off camera WB

* Sat Apr 26 2014 Nils Philippsen <nils@redhat.com> - 0.19.2-12
- snapshot cvs20140414: fixes using camera white balance with Sony SLT-A99V

* Fri Jan 10 2014 Orion Poplawski <orion@cora.nwra.com> - 0.19.2-11
- Rebuild for cfitsio 3.360

* Fri Dec 06 2013 Nils Philippsen <nils@redhat.com> - 0.19.2-10
- harden against corrupt input files (CVE-2013-1438)

* Tue Dec 03 2013 Rex Dieter <rdieter@fedoraproject.org> 0.19.2-9
- rebuild (exiv2)

* Sat Oct 05 2013 Nils Philippsen <nils@redhat.com> - 0.19.2-8
- actually require lcms2-devel for building
- update lcms2 patch so that it builds with lcms2 < 2.5

* Wed Oct 02 2013 Nils Philippsen <nils@redhat.com> - 0.19.2-7
- build against lcms2
- drop obsolete configure options (exiv2, lensfun, libexif)

* Thu Sep 19 2013 Nils Philippsen <nils@redhat.com> - 0.19.2-6
- fix disabling cinepaint subpackage from F-20 on (#986689)

* Fri Sep 13 2013 Nils Philippsen <nils@redhat.com> - 0.19.2-6
- drop ancient obsoletes (#1002124)

* Fri Sep 13 2013 Nils Philippsen <nils@redhat.com> - 0.19.2-5
- gimp plug-in:
  - decode EXIF into XMP
  - register TIFF and XML file loader magic values to fix loading raw files in
    and sending images to upcoming GIMP versions

* Wed Jul 31 2013 Nils Philippsen <nils@redhat.com> - 0.19.2-4
- don't own plug-in directories (#989890)
- install symlinked ufraw-batch man page

* Mon Jul 29 2013 Nils Philippsen <nils@redhat.com> - 0.19.2-3
- disable cinepaint subpackage from F-20 on (#986689)
- rebuild for newer cfitsio

* Sat May 11 2013 Rex Dieter <rdieter@fedoraproject.org> 0.19.2-2.1
- rebuild for newer lensfun (#947988)

* Wed Mar 27 2013 Nils Philippsen <nils@redhat.com> - 0.19.2-2
- upstream rolled new tarball supporting aarch64

* Mon Mar 25 2013 Nils Philippsen <nils@redhat.com> - 0.19.2-1
- version 0.19.2
- enable building on aarch64

* Sun Mar 24 2013 Peter Robinson <pbrobinson@fedoraproject.org> 0.19-2
- rebuild (libcfitsio)

* Fri Mar 01 2013 Nils Philippsen <nils@redhat.com> - 0.19-1
- version 0.19
- drop obsolete patches

* Fri Feb 15 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.18-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Mon Jan 21 2013 Adam Tkac <atkac redhat com> - 0.18-16
- rebuild due to "jpeg8-ABI" feature drop

* Fri Dec 21 2012 Adam Tkac <atkac redhat com> - 0.18-15
- rebuild against new libjpeg

* Sat Sep 08 2012 Nils Philippsen <nils@redhat.com> - 0.18-14
- fix trimming excessive EXIF data

* Sun Jul 22 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.18-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Wed May 02 2012 Rex Dieter <rdieter@fedoraproject.org> - 0.18-12
- rebuild (exiv2)

* Mon Apr 16 2012 Nils Philippsen <nils@redhat.com> - 0.18-11
- rebuild for new cinepaint

* Tue Apr 03 2012 Nils Philippsen <nils@redhat.com> - 0.18-10
- rebuild against gimp 2.8.0 release candidate

* Fri Mar 16 2012 Nils Philippsen <nils@redhat.com> - 0.18-9
- use new GIMP 2.8 API if available

* Tue Feb 28 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.18-8
- Rebuilt for c++ ABI breakage

* Tue Jan 10 2012 Nils Philippsen <nils@redhat.com> - 0.18-7
- rebuild for gcc 4.7

* Fri Dec 16 2011 Nils Philippsen <nils@redhat.com> - 0.18-6
- rebuild for GIMP 2.7

* Mon Nov 07 2011 Nils Philippsen <nils@redhat.com> - 0.18-5
- rebuild (libpng)

* Fri Oct 14 2011 Rex Dieter <rdieter@fedoraproject.org> - 0.18-4
- rebuild (exiv2)

* Fri Aug 12 2011 Nils Philippsen <nils@redhat.com> - 0.18-3
- fix crop area ratios if working on multiple images (#634235, patch by Udi
  Fuchs)

* Tue Mar 15 2011 Nils Philippsen <nils@redhat.com> - 0.18-2
- fix crash when loading dark frame (#683199)

* Fri Mar 04 2011 Nils Philippsen <nils@redhat.com> - 0.18-1
- version 0.18
- add/update versioned build requirements

* Mon Feb 07 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.17-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Sun Jan 02 2011 Rex Dieter <rdieter@fedoraproject.org> - 0.17-3
- rebuild (exiv2)

* Fri Dec 03 2010 Nils Philippsen <nils@redhat.com> - 0.17-2
- rebuild (exiv2)

* Wed Jun 02 2010 Nils Philippsen <nils@redhat.com> - 0.17-1
- version 0.17
- add BR: cfitsio-devel

* Mon May 31 2010 Rex Dieter <rdieter@fedoraproject.org> - 0.16-3 
- rebuild (exiv2)

* Mon Jan 04 2010 Rex Dieter <rdieter@fedoraproject.org> - 0.16-2 
- rebuild (exiv2)

* Sat Dec 05 2009 Dennis Gilmore <dennis@ausil.us> - 0.16-1
- update to 0.16

* Mon Aug 17 2009 Nils Philippsen <nils@redhat.com> - 0.15-4
- fix building with lensfun (#517558), only build with lensfun from F-12 on
- explain gcc-4.4 patch

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.15-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Mon Mar 02 2009 Nils Philippsen <nils@redhat.com> - 0.15-2
- fix building with gcc-4.4

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org>
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Mon Jan 26 2009 Nils Philippsen <nils@redhat.com> - 0.15-1
- version 0.15:
  - Multiprocessing support using OpenMP. Patch by Bruce Guenter.
  - Add progress report during the loading of raw files.
  - Add JPEG optimization to reduce the file size without effecting image
    quality.
  - Compatibility with the just released Exiv2-0.18.
  - Support sRAW1 and sRAW2 formats of the Canon 50D and 5D Mark II.
  - Some annoying bugs got squashed.
- use downloads.sourceforge.net source URL

* Thu Dec 18 2008 Rex Dieter <rdieter@fedoraproject.org> - 0.14.1-4 
- respin (exiv2)

* Tue Dec 02 2008 Nils Philippsen <nils@redhat.com> - 0.14.1-3
- require gimp and cinepaint in the respective subpackages (#474021)

* Mon Dec 01 2008 Nils Philippsen <nils@redhat.com> - 0.14.1-2
- change license to GPLv2+

* Fri Nov 28 2008 Nils Philippsen <nils@redhat.com> - 0.14.1-1
- version 0.14.1
- use %%bcond_with/without macros
- enable building with lensfun from F11 on

* Fri Jul 04 2008 Nils Philippsen <nphilipp@redhat.com> - 0.13-6
- rebuild with gtkimageview-1.6.1

* Wed Jun 25 2008 Rex Dieter <rdieter@fedoraproject.org> - 0.13-5 
- respin for exiv2

* Tue Feb 19 2008 Fedora Release Engineering <rel-eng@fedoraproject.org> - 0.13-4
- Autorebuild for GCC 4.3

* Wed Jan 02 2008 Nils Philippsen <nphilipp@redhat.com> - 0.13-3
- build against gtkimageview, drop scrollable-preview patch (#427028)

* Fri Nov 30 2007 Nils Philippsen <nphilipp@redhat.com> - 0.13-2
- make preview scrollable, window resizable

* Fri Nov 30 2007 Nils Philippsen <nphilipp@redhat.com> - 0.13-1
- version 0.13
- build cinepaint plugin from Fedora 7 on (#282641)

* Wed Nov 14 2007 Nils Philippsen <nphilipp@redhat.com> - 0.12-3
- rephrase summary
- use full path to gimptool

* Wed Sep 05 2007 Nils Philippsen <nphilipp@redhat.com> - 0.12-2
- change license to GPLv2

* Mon Aug 06 2007 Nils Philippsen <nphilipp@redhat.com> - 0.12-1
- version 0.12
- drop obsolete exiv2, cmserrorhandler patches
- package ufraw-mime.xml for up to Fedora 7, RHEL 5

* Thu May 24 2007 Nils Philippsen <nphilipp@redhat.com> - 0.11-8
- use correct patch

* Thu May 24 2007 Nils Philippsen <nphilipp@redhat.com> - 0.11-7
- prevent crash in CMS error handler (#239147)

* Wed Apr 25 2007 Rex Dieter <rdieter[AT]fedoraproject> - 0.11-6
- exiv2 patch (#237846)

* Wed Apr 25 2007 Rex Dieter <rdieter[AT]fedoraproject> - 0.11-5
- respin for exiv2-0.14

* Tue Apr 24 2007 Nils Philippsen <nphilipp@redhat.com> - 0.11-4
- eventually put GConf2, shared-mime-info requirements into -common subpackage
  (#235583)

* Mon Mar 12 2007 Nils Philippsen <nphilipp@redhat.com> - 0.11-3
- split pkg from fc6/rhel5 on to avoid upgrading mess

* Mon Mar 12 2007 Nils Philippsen <nphilipp@redhat.com> - 0.11-2
- use %%rhel, not %%redhat

* Mon Mar 12 2007 Nils Philippsen <nphilipp@redhat.com> - 0.11-1
- version 0.11

* Mon Feb 19 2007 Nils Philippsen <nphilipp@redhat.com> - 0.10-2
- don't ship dcraw binary (#229044)

* Wed Feb 07 2007 Nils Philippsen <nphilipp@redhat.com> - 0.10-1
- version 0.10
- add BR: perl, exiv2-devel, gettext
- split standalone tools and GIMP plugin in Rawhide

* Mon Aug 28 2006 Nils Philippsen <nphilipp@redhat.com> - 0.9.1-1
- version 0.9.1
- require gimp >= 2.0 for building

* Fri Feb 17 2006 Nils Philippsen <nphilipp@redhat.com> - 0.6-2
- rebuild

* Mon Nov 21 2005 Nils Philippsen <nphilipp@redhat.com> - 0.6-1
- version 0.6

* Thu Oct 06 2005 Nils Philippsen <nphilipp@redhat.com> - 0.5-1
- version 0.5

* Sun May 22 2005 Jeremy Katz <katzj@redhat.com> - 0.4-2
- rebuild to sync arches

* Tue Mar 29 2005 Seth Vidal <skvidal at phy.duke.edu> - 0.4-1
- buildrequire libtiff-devel and libjpeg-devel

* Thu Mar 24 2005 Nils Philippsen <nphilipp@redhat.com> - 0.4-1
- buildrequire lcms-devel
- trim summary
- change buildroot

* Wed Mar 02 2005 Nils Philippsen <nphilipp@redhat.com>
- version 0.4
- update URLs

* Wed Dec 01 2004 Nils Philippsen <nphilipp@redhat.com>
- version 0.2
- initial build
