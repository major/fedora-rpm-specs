Name:           gweled
Version:        0.9.1
Release:        30.20130730git819bed%{?dist}

Summary:        Swapping gem game

License:        GPL-2.0-or-later
URL:            http://launchpad.net/gweled
#Source0:        http://launchpad.net/gweled/trunk/0.9/+download/gweled-%%{version}.tar.gz
#Fork using sdl_mixer rather than libcanberra or mikmod
#https://github.com/Marisa-Chan/gweled-sdl_mixer.git
Source0:	gweled-sdl_mixer-819bed.tar.gz
Patch0:		gweled-fix-librsvg-segfault-v2.patch

BuildRequires:  libgnomeui-devel >= 2.0.0
BuildRequires:  librsvg2-devel >= 2.0.0
BuildRequires:  desktop-file-utils
BuildRequires:	intltool libtool
BuildRequires:	SDL_mixer-devel
BuildRequires: make
Requires:	hicolor-icon-theme

%description
Gweled is a Gnome version of a popular PalmOS/Windows/Java game called
"Bejeweled" or "Diamond Mine". The aim of the game is to make alignment of 3 or
more gems, both vertically or horizontally by swapping adjacent gems. The game
ends when there are no possible moves left.


%prep
%setup -qn gweled-sdl_mixer-819bed
%patch0 -p0

%build

export LDFLAGS="${LDFLAGS} -lm -Wl,--export-dynamic "
./autogen.sh
%configure --localstatedir=/var/lib
#echo "Encoding=UTF-8" >> data/gweled.desktop
#mv gweled.desktop gweled.desktop.old
#iconv --from-code=ISO-8859-1 --to-code=UTF-8 <gweled.desktop.old > gweled.desktop
make %{?_smp_mflags}



%install
make install DESTDIR=$RPM_BUILD_ROOT
desktop-file-install --delete-original \
  --dir ${RPM_BUILD_ROOT}%{_datadir}/applications      \
  --add-category LogicGame                    \
  --remove-category Application                        \
  ${RPM_BUILD_ROOT}%{_datadir}/applications/%{name}.desktop

# Register as an application to be visible in the software center
#
# NOTE: It would be *awesome* if this file was maintained by the upstream
# project, translated and installed into the right place during `make install`.
#
# See http://www.freedesktop.org/software/appstream/docs/ for more details.
#
mkdir -p $RPM_BUILD_ROOT%{_datadir}/appdata
cat > $RPM_BUILD_ROOT%{_datadir}/appdata/%{name}.appdata.xml <<EOF
<?xml version="1.0" encoding="UTF-8"?>
<!-- Copyright 2014 William Moreno <williamjmorenor@fedoraproject.org> -->
<!--
BugReportURL: https://bugs.launchpad.net/gweled/+bug/1322917
SentUpstream: 2014-06-12
-->
<application>
  <id type="desktop">gweled.desktop</id>
  <metadata_license>CC0-1.0</metadata_license>
  <summary>Align three identical gems to remove them from board</summary>
  <description>
    <p>
      Gweled is a version for GNU / Linux of the popular mobile game called
      Bejeweled or Diamond Mine.
      The game consist in to move adjacent gems to align three or more vertically
      or horizontally to remove them from the board.
    </p>
  </description>
  <url type="homepage">http://launchpad.net/gweled</url>
  <screenshots>
    <screenshot type="default">http://gweled.org/images/screen1.png</screenshot>
  </screenshots>
</application>
EOF

%find_lang %{name}



%files -f %{name}.lang
%license COPYING
%doc AUTHORS NEWS
%attr(2551,root,games) %{_bindir}/%{name}
%config(noreplace) %attr(0664,games,games) %{_localstatedir}/lib/games/*
%{_datadir}/appdata/%{name}.appdata.xml
%{_datadir}/applications/%{name}.desktop
%{_datadir}/pixmaps/*
%{_datadir}/icons/hicolor/*/apps/%{name}.*
%{_datadir}/%{name}/
%{_datadir}/sounds/%{name}/

%changelog
* Fri Mar 03 2023 Gwyn Ciesla <gwync@protonmail.com> - 0.9.1-30.20130730git819bed
- migrated to SPDX license

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.1-29.20130730git819bed
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.1-28.20130730git819bed
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.1-27.20130730git819bed
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.1-26.20130730git819bed
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.1-25.20130730git819bed
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.1-24.20130730git819bed
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.1-23.20130730git819bed
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.1-22.20130730git819bed
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.1-21.20130730git819bed
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.1-20.20130730git819bed
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Mon Mar 05 2018 Gwyn Ciesla <limburgher@gmail.com> - 0.9.1-19.20130730git819bed
- segfault patch.

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.1-18.20130730git819bed
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.1-17.20130730git819bed
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.1-16.20130730git819bed
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.1-15.20130730git819bed
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.1-14.20130730git819bed
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Oct 29 2015 Jon Ciesla <limburgher@gmail.com> - 0.9.1-13.20130730git819bed
- Require hicolor-icon-theme, BZ 1172521.

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.1-12.20130730git819bed
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Thu Mar 26 2015 Richard Hughes <rhughes@redhat.com> - 0.9.1-11.20130730git819bed
- Add an AppData file for the software center

* Sat Aug 16 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.1-10.20130730git819bed
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.1-9.20130730git819bed
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Tue Jul 30 2013 Jon Ciesla <limburgher@gmail.com> - 0.9.1-8.20130730git819bed
- Switch to fork using SDL_mixer rather than mikmod or libcanberra.
- https://admin.fedoraproject.org/updates/FEDORA-2013-13664/gweled-0.9.1-7.20130725bzr91.fc19

* Thu Jul 25 2013 Jon Ciesla <limburgher@gmail.com> - 0.9.1-7.20130725bzr91
- Fix dates.
- Update to bzr checkout to correct sound issue.

* Mon Feb 11 2013 Jon Ciesla <limburgher@gmail.com> - 0.9.1-6
- Drop desktop vendor tag.

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Thu Nov 10 2011 Jon Ciesla <limb@jcomserv.net> - 0.9.1-3
- Rebuild for libpng 1.5.

* Thu Jun 09 2011 Jon Ciesla <limb@jcomserv.net> - 0.9.1-2
- Specified localstate dir for score files, BZ 711553.

* Thu Jun 09 2011 Jon Ciesla <limb@jcomserv.net> - 0.9.1-1
- New upstream release.

* Fri Mar 11 2011 Jon Ciesla <limb@jcomserv.net> - 0.9-3
- Marked score files config noreplace, BZ 618603.

* Wed Mar 09 2011 Jon Ciesla <limb@jcomserv.net> - 0.9-2
- Added disttag.

* Wed Mar 09 2011 Jon Ciesla <limb@jcomserv.net> - 0.9-1
- New upstream release from new project maintainer.

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.7-18.1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Sat Feb 13 2010 Thorsten Leemhuis <fedora[AT]leemhuis[DOT]info> - 0.7-17
- add another patch as suggested in #544575#3
- add -lm to linker flags for DSOLinkChange stuff from F13

* Tue Feb 09 2010 Thorsten Leemhuis <fedora[AT]leemhuis[DOT]info> - 0.7-16
- add patch from to disable music as requested in #544575

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.7-15.1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Tue Feb 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.7-14.1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Fri Feb 13 2009 Thorsten Leemhuis <fedora[AT]leemhuis[DOT]info> - 0.7-13
- remove Application, add LogicGame to desktop file

* Tue Sep 02 2008 Thorsten Leemhuis <fedora[AT]leemhuis[DOT]info> - 0.7-12
- define _default_patch_fuzz 2

* Sat Feb 09 2008 Thorsten Leemhuis <fedora[AT]leemhuis[DOT]info> - 0.7-11
- rebuilt (again, this time for new mikmod)

* Sat Feb 09 2008 Thorsten Leemhuis <fedora[AT]leemhuis[DOT]info> - 0.7-10
- rebuilt

* Fri Aug 03 2007 Thorsten Leemhuis <fedora [AT] leemhuis [DOT] info>
- Update License field due to the "Licensing guidelines changes"

* Thu Apr 19 2007 Thorsten Leemhuis <fedora[AT]leemhuis.info> - 0.7-9
- remove dist in devel
- rebuild for new mikmod

* Sat Mar 17 2007 Thorsten Leemhuis <fedora[AT]leemhuis.info> - 0.7-8
- create gweled.timed.scores manually, fixes 232184

* Sat Feb 24 2007 Thorsten Leemhuis <fedora[AT]leemhuis.info> - 0.7-7
- Add gweled-ppc.diff and gweled-mikmod-disable-disk-writers.diff from
  debian package; the later fixes #227984

* Tue Aug 29 2006 Thorsten Leemhuis <fedora[AT]leemhuis.info> - 0.7-6
- Rebuild for devel

* Sun Mar 26 2006 Thorsten Leemhuis <fedora[AT]leemhuis.info> - 0.7-5
- Add LDFLAGS="-Wl,--export-dynamic" (thx to Kevin Kofler for the hint)

* Mon Feb 13 2006 Thorsten Leemhuis <fedora[AT]leemhuis.info> - 0.7-4
- Rebuild for Fedora Extras 5

* Sun Jan 29 2006 Thorsten Leemhuis <fedora[AT]leemhuis.info> - 0.7-3
- Fix build in devel (mv behaviour changed)

* Wed Oct 05 2005 Thorsten Leemhuis <fedora[AT]leemhuis.info> - 0.7-2
- Use dist

* Tue Oct 04 2005 Thorsten Leemhuis <fedora[AT]leemhuis.info> - 0.7-1
- Update to 0.7
- drop gcc4 patch (upstream now)
- Update Makefile-patch
- add Sample_Free.patch to avoid double free on exit (with help from adrianr)
- score file must not be conffile 

* Wed Apr 13 2005 Adrian Reber <adrian@lisas.de> - 0.6-3
- fixed gcc4 errors
- removed empty README file
- fixed segfault caused by:
  call to __builtin___memset_chk will always overflow destination buffer

* Thu Apr  7 2005 Michael Schwendt <mschwendt[AT]users.sf.net>
- rebuilt

* Tue Aug 31 2004 Thorsten Leemhuis <fedora[AT]leemhuis.info> - 0:0.6-1
- Update to 0.6
- Remove highscore workaround
- Add Makefile patch
- Don't overwrite highscores during update

* Tue Aug 31 2004 Thorsten Leemhuis <fedora[AT]leemhuis.info> - 0:0.5-0.fdr.1
- Update to 0.5
- Add highscorce workaround

* Thu Jan 15 2004 Thorsten Leemhuis <fedora[AT]leemhuis.info> - 0:0.4-0.fdr.2
- Own dirs correctly
- BuildRequires desktop-file-utils

* Fri Jan 09 2004 Thorsten Leemhuis <fedora[AT]leemhuis.info> - 0:0.4-0.fdr.1
- Update to 0.4
- Correct permissions so highscores work
- Add UTF-8 to desktop file

* Thu Nov 27 2003 Phillip Compton <pcompton[AT]proteinmedia.com> - 0:0.3-0.fdr.1
- Initial RPM release.
