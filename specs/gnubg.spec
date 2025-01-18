Name:          gnubg
License:       GPL-3.0-only
Summary:       A backgammon game and analyser
Epoch:         1
Version:       1.08.003
Release:       6%{?dist}
Source0:       https://ftp.gnu.org/gnu/gnubg/gnubg-release-%{version}-sources.tar.gz
Source1:       gnubg.desktop
Source2:       gnubg.png

URL:           https://www.gnu.org/software/gnubg/
BuildRequires: libcanberra-devel
BuildRequires: sqlite-devel
BuildRequires: gmp-devel
BuildRequires: gtk2-devel
BuildRequires: gettext-devel
BuildRequires: automake
BuildRequires: bison
BuildRequires: libtool
BuildRequires: texinfo
BuildRequires: netpbm-progs
BuildRequires: gnuplot
BuildRequires: ghostscript
BuildRequires: info
BuildRequires: desktop-file-utils
BuildRequires: cairo-devel
BuildRequires: atk-devel
BuildRequires: pango-devel
BuildRequires: libpng-devel
BuildRequires: readline-devel
BuildRequires: freetype-devel
BuildRequires: flex
BuildRequires: make
#BuildRequires: gtkglext-devel
#BuildRequires: mesa-libGLU-devel
Requires: dejavu-sans-fonts
Requires: dejavu-serif-fonts

%description
GNU Backgammon is software for playing and analysing backgammon
positions, games and matches. It's based on a neural network. Although it
already plays at a very high level, it's still work in progress. You may
play GNU Backgammon using the command line or a graphical interface

%prep
%setup -q

/usr/bin/iconv -f ISO-8859-1 -t UTF8 ChangeLog > ChangeLog.tmp 
/bin/mv ChangeLog.tmp ChangeLog

%build
%ifarch x86_64
SSE=sse2
%else
SSE=no
%endif

%configure --with-python=no --enable-simd=$SSE --with-gtk --with-board3d=no
%make_build

%install
mkdir -p $RPM_BUILD_ROOT%{_prefix}
mkdir -p $RPM_BUILD_ROOT%{_datadir}/gnubg
make install DESTDIR=$RPM_BUILD_ROOT
rm -rf $RPM_BUILD_ROOT%{_datadir}/gnubg/fonts/*.ttf
ln -s ../../fonts/dejavu-sans-fonts/DejaVuSans.ttf $RPM_BUILD_ROOT%{_datadir}/gnubg/fonts/Vera.ttf
ln -s ../../fonts/dejavu-sans-fonts/DejaVuSans-Bold.ttf $RPM_BUILD_ROOT%{_datadir}/gnubg/fonts/VeraBd.ttf 
ln -s ../../fonts/dejavu-serif-fonts/DejaVuSerif-Bold.ttf $RPM_BUILD_ROOT%{_datadir}/gnubg/fonts/VeraSeBd.ttf 
install -Dpm 644 gnubg.weights $RPM_BUILD_ROOT%{_datadir}/gnubg/gnubg.weights

cp -rp textures* $RPM_BUILD_ROOT%{_datadir}/gnubg/
rm -rf $RPM_BUILD_ROOT%{_datadir}/gnubg/textures/CVS
rm -rf $RPM_BUILD_ROOT%{_datadir}/gnubg/textures/.cvsignore
rm -rf $RPM_BUILD_ROOT%{_datadir}/doc/gnubg/

%find_lang gnubg

# remove /usr/share/info/dir
/bin/rm -f $RPM_BUILD_ROOT/usr/share/info/dir

# below is the desktop file and icon stuff.
mkdir -p $RPM_BUILD_ROOT%{_datadir}/applications
desktop-file-install \
  --dir $RPM_BUILD_ROOT%{_datadir}/applications \
  %{SOURCE1}
mkdir -p $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/32x32/apps
install -p -m 644 %{SOURCE2} \
  $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/32x32/apps

%files -f gnubg.lang
%license COPYING
%doc AUTHORS README ChangeLog doc/images doc/*.html doc/*.pdf
%{_bindir}/bearoffdump
%{_bindir}/gnubg
%{_bindir}/makebearoff
%{_bindir}/makehyper
%{_bindir}/makeweights
%dir %{_datadir}/gnubg
%{_datadir}/gnubg/met
%{_datadir}/gnubg/boards.xml
%{_datadir}/gnubg/gnubg_os0.bd
%{_datadir}/gnubg/gnubg.weights
%{_datadir}/gnubg/sounds
%{_datadir}/gnubg/textures.txt
%{_datadir}/gnubg/textures
%{_mandir}/man6/*
%{_datadir}/applications/%{name}.desktop
%{_datadir}/icons/hicolor/32x32/apps/%{name}.png
%{_datadir}/gnubg/pixmaps/gnubg-big.png
%{_datadir}/icons/hicolor/16x16/apps/gnubg.png
%{_datadir}/icons/hicolor/22x22/apps/gnubg.png
%{_datadir}/icons/hicolor/24x24/apps/gnubg.png
%{_datadir}/icons/hicolor/48x48/apps/gnubg.png
%dir %{_datadir}/gnubg/fonts
%{_datadir}/gnubg/fonts/*
%{_datadir}/gnubg/gnubg.gtkrc
%{_datadir}/gnubg/gnubg.wd
%{_datadir}/gnubg/scripts/
%{_datadir}/gnubg/flags/
%{_datadir}/gnubg/gnubg.sql
%{_datadir}/gnubg/gnubg_ts0.bd
%{_datadir}/gnubg/gnubg.css
%{_datadir}/gnubg/Shaders/

%changelog
* Thu Jan 16 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1:1.08.003-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1:1.08.003-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Mon May 13 2024 Gwyn Ciesla <gwync@protonmail.com> - 1:1.08.003-4
- Compiler flag adjustments

* Fri May 10 2024 Gwyn Ciesla <gwync@protonmail.com> - 1:1.08.003-3
- Move back to gtk2, disable GL rendering.

* Thu May 09 2024 Gwyn Ciesla <gwync@protonmail.com> - 1:1.08.003-2
- Enable GL rendering.

* Mon Apr 29 2024 Gwyn Ciesla <gwync@protonmail.com> - 1:1.08.003-1
- 1.08.003

* Mon Feb 26 2024 Gwyn Ciesla <gwync@protonmail.com> - 1:1.08.002-1
- 1.08.002

* Mon Feb 05 2024 Gwyn Ciesla <gwync@protonmail.com> - 1:1.08.001-1
- 1.08.001

* Wed Jan 24 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1:1.07.001-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1:1.07.001-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1:1.07.001-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Mon May 22 2023 Gwyn Ciesla <gwync@protonmail.com> - 1:1.07.001-4
- Fix font symlinks

* Wed Mar 01 2023 Gwyn Ciesla <gwync@protonmail.com> - 1:1.07.001-3
- migrated to SPDX license

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1:1.07.001-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Tue Nov 15 2022 Gwyn Ciesla <gwync@protonmail.com> - 1:1.07.001-1
- 1.07.001

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1:1.06.001-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Sun Mar 13 2022 Sérgio Basto <sergio@serjux.com> - 1:1.06.001-15
- Fix build, ngettext is not detect because have some problem with build flags
- Drop BR glib-devel because gnubg don't use it.

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org>
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1:1.06.001-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1:1.06.001-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1:1.06.001-12
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1:1.06.001-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon May 11 2020 Gwyn Ciesla <gwync@protonmail.com> - 1:1.06.00-10
- Drop gtkglext.

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1:1.06.001-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Tue Aug 06 2019 Gwyn Ciesla <gwync@protonmail.com> - 1:1.06.001-8
- Drop Python 2.

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1:1.06.001-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Mar  7 2019 Tim Landscheidt <tim@tim-landscheidt.de> - 1:1.06.001-6
- Remove obsolete requirements for %%post/%%postun scriptlets

* Sun Feb 17 2019 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 1:1.06.001-5
- Rebuild for readline 8.0

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1:1.06.001-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1:1.06.001-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Feb 15 2018 Gwyn Ciesla <limburgher@gmail.com> - 1:1.06.001-2
- Disable simd.

* Thu Feb 08 2018 Gwyn Ciesla <limburgher@gmail.com> - 1:1.06.001-1
- Update to 1.06.001

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1:1.05.000-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jan 11 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 1:1.05.000-8
- Remove obsolete scriptlets

* Fri Jan 05 2018 Iryna Shcherbina <ishcherb@redhat.com> - 1:1.05.000-7
- Update Python 2 dependency declarations to new packaging standards
  (See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3)

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1:1.05.000-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1:1.05.000-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1:1.05.000-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Jan 12 2017 Igor Gnatenko <ignatenko@redhat.com> - 1:1.05.000-3
- Rebuild for readline 7.x

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1:1.05.000-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Tue Sep 01 2015 Jon Ciesla <limburgher@gmail.com> - 1:1.05.000-1
- Update to 1.05
- Fix FTBFS.

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1:1.04.000-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sun Dec 14 2014 Joseph Hansen <jeh@cardamom.net> - 1:1.04.000-1
- Update to 1.04
- fixes crash on startup, see https://bugs.launchpad.net/ubuntu/+source/gnubg/+bug/1346567
- BZ 1160717

* Sat Aug 16 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1:1.02.000-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1:1.02.000-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Wed Aug 14 2013 Jon Ciesla <limburgher@gmail.com> - 1:1.02.000-3
- Drop libpng seds.

* Sun Aug 11 2013 Michael Petch <mpetch@gnubg.org> - 1:1.02.000-2
- esound was deprecated in the code, use libcanberra
- Remove unused sound dependencies
- Remove unused dependency libxml2
- Add MySql-python runtime dependency
- Add sqlite database dependency
- Add gmp dependency to support long seeds
- gnubg.weights now included in upstream source tarball
- Remove deprecated configure "with" options
- Clean up the docdir directory.
- Add html and pdf files to docdir
- Change license to GPLv3

* Wed Aug 07 2013 Jon Ciesla <limburgher@gmail.com> - 1:1.02.000-1
- Latest upstream, BZ 994196.

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1:0.9.0.1-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Mon Jul 22 2013 Jon Ciesla <limburgher@gmail.com> - 1:0.9.0.1-20
- Update for libpng16.

* Wed Jul 10 2013 Jon Ciesla <limburgher@gmail.com> - 1:0.9.0.1-19
- Fix info.

* Mon Feb 18 2013 Jon Ciesla <limburgher@gmail.com> - 1:0.9.0.1-18
- Re-enable esound.

* Tue Feb 12 2013 Jon Ciesla <limburgher@gmail.com> - 1:0.9.0.1-17
- Drop esound.

* Mon Feb 11 2013 Jon Ciesla <limburgher@gmail.com> - 1:0.9.0.1-16
- Drop desktop vendor tag.

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1:0.9.0.1-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1:0.9.0.1-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Dec 13 2011 Jon Ciesla <limburgher@gmail.com> - 1:0.9.0.1-13
- Patched for libpng.

* Tue Dec 06 2011 Adam Jackson <ajax@redhat.com> - 1:0.9.0.1-12
- Rebuild for new libpng

* Thu Nov 10 2011 Jon Ciesla <limb@jcomserv.net> - 1:0.9.0.1-11
- Rebuild for libpng 1.5.

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1:0.9.0.1-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Tue Jul 27 2010 David Malcolm <dmalcolm@redhat.com> - 1:0.9.0.1-9
- Rebuilt for https://fedoraproject.org/wiki/Features/Python_2.7/MassRebuild

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1:0.9.0.1-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Tue Feb 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1:0.9.0.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Tue Jan 20 2009 Jon Ciesla <limb@jcomserv.net> - 1:0.9.0.1-6
- Fix for dejavu renaming, BZ 480456.
* Fri Jan 09 2009 Jon Ciesla <limb@jcomserv.net> - 1:0.9.0.1-5
- Switch to dejavu fonts.
* Fri Jan 02 2009 Jon Ciesla <limb@jcomserv.net> - 1:0.9.0.1-4.1
- Requires fix.
* Tue Dec 30 2008 Jon Ciesla <limb@jcomserv.net> - 1:0.9.0.1-4
- Drop and symlink to system fonts, BZ 477391.
* Thu Dec 11 2008 Jon Ciesla <limb@jcomserv.net> - 1:0.9.0.1-3
- Added coreutils requires, BZ 475933.
* Sun Nov 30 2008 Ignacio Vazquez-Abrams <ivazqueznet+rpm@gmail.com> - 1:0.9.0.1-2
- Rebuild for Python 2.6
* Fri Sep 05 2008 Jon Ciesla <limb@jcomserv.net> - 1:0.9.0.1-1
- Update to latest version, BZ 461281.
* Fri Feb 08 2008 Jon Ciesla <limb@jcomserv.net> - 20061119-14
- GCC 4.3 rebuild.
* Thu Aug 16 2007 Jon Ciesla <limb@jcomserv.net> - 20061119-13
- License tag correction.
* Mon Aug 13 2007 Jon Ciesla <limb@jcomserv.net> - 20061119-12
- Fixed .desktop file version.
* Wed Apr 04 2007 Jon Ciesla <limb@jcomserv.net> - 20061119-11
- rel bump for desktop mis-update fix.
* Wed Apr 04 2007 Jon Ciesla <limb@jcomserv.net> - 20061119-10
- Unified spec to fix EVR issues.
* Tue Mar 20 2007 Jon Ciesla <limb@jcomserv.net> - 20061119-9
- Explicity installing textures.
- Updated menu categories in desktop.
* Wed Feb 14 2007 Jon Ciesla <limb@jcomserv.net> - 20061119-8
- Corrected some duplicate files
* Wed Feb 14 2007 Jon Ciesla <limb@jcomserv.net> - 20061119-7
- BuildRequires fix.
* Wed Feb 14 2007 Jon Ciesla <limb@jcomserv.net> - 20061119-6
- BuildRequires fix.
* Wed Feb 14 2007 Jon Ciesla <limb@jcomserv.net> - 20061119-5
- BuildRequires fix.
* Wed Feb 14 2007 Jon Ciesla <limb@jcomserv.net> - 20061119-4
- BuildRequires fix.
* Wed Feb 14 2007 Jon Ciesla <limb@jcomserv.net> - 20061119-3
- BuildRequires fix.
* Tue Feb 13 2007 Jon Ciesla <limb@jcomserv.net> - 20061119-2
- Removed czech.png, added scripts, flags dirs.
* Tue Feb 13 2007 Jon Ciesla <limb@jcomserv.net> - 20061119-1
- Bumped to upstream verion 20061119; Updated URL
* Wed Aug 30 2006 Joost Soeterbroek <fedora@soeterbroek.com> - 20060629-1
- Rebuild for Fedora Extras 6; bumped to upstream version 20060629
* Mon Jun 26 2006 - Joost Soeterbroek <fedora@soeterbroek.com> - 20060626-1
- update to new upstream version
* Tue Jun  6 2006 - Joost Soeterbroek <fedora@soeterbroek.com> - 20060530-5
- minor change in man file conversion, move from install to prep
* Mon Jun  5 2006 - Joost Soeterbroek <fedora@soeterbroek.com> - 20060530-4
- added BuildReqs desktop-file-utils
* Sun Jun  4 2006 - Joost Soeterbroek <fedora@soeterbroek.com> - 20060530-3
- fixed utf8 error in /usr/share/man/man6/gnubg.6.gz
- removed BuildReqs gtk+-devel, freetype-devel, audiofile-devel
- added BuildReqs gtkglext-devel
- remove /usr/share/info/dir
- removed subpackages database- and sound-
- removed configure option without-board3d 
- sanitised %%files section
- ghost the .pyo files /usr/share/gnubg/scripts/
- added desktop file and icon
* Thu Jun  1 2006 - Joost Soeterbroek <fedora@soeterbroek.com> - 20060530-2
- moved autogen.sh from %%build to %%setup
- changed ./configure to %%configure macro
- removed install-strip
- added directories to files sections
- removed BuildReqs glib2 and autoconf
- added BuildReqs (mock): gettext-devel, gtk2-devel, texinfo, python-devel,
  netpbm-progs, gnuplot, ghostscript, info
* Wed May 31 2006 - Joost Soeterbroek <fedora@soeterbroek.com> - 20060530-1
- added find_lang macro
- added full URL to Source
- added BuildReqs.
- added correct Reqs. to sub-packages
- added defattr to sub-packages' files section
- added correct TexInfo scriptlet for post and preun
* Sun Apr 23 2006 - Joost Soeterbroek <fedora@soeterbroek.com>
- rebuild for FE
* Tue Dec 28 2004 - <ace@gnubg.org>
- new weights including pruning
* Mon Oct 11 2004 - <ace@gnubg.org>
- fixed some minor bugs
* Wed Sep 01 2004 - <ace@gnubg.org>
- new rpms with 3d enabled
* Wed Nov 05 2003 - <ace@gnubg.org>
- made the spec suit to redhat and suse <ace@gnubg.org>
- disabled 3d (still problems with nvidia)
- added gpg signature
* Thu Oct 23 2003 - <ace@gnubg.org>
- disabled gdbm and guile
- changed info- and manpath
* Mon Oct 20 2003 - <ace@gnubg.org>
- divided into three packages (gnubg, databases, sounds)
* Sat Oct 18 2003 - <ace@gnubg.org>
- initial package (Version 0.14)
