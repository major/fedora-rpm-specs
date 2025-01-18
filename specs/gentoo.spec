Name:           gentoo
Version:        0.20.7
Release:        23%{?dist}
Summary:        Graphical file management program written in GTK+3
# Automatically converted from old format: GPLv2 - review is highly recommended.
License:        GPL-2.0-only
URL:            https://sourceforge.net/projects/gentoo/
Source0:        http://downloads.sourceforge.net/%{name}/%{name}-%{version}.tar.gz
Source1:        gentoo.desktop
# icons/gentoo.png is not within standard sizes
# Get here http://www.obsession.se/gentoo/gfx/logo.png (not in sources)
Source2:        gentoo.png
# Remove duplicated translations
Patch0:         %{name}-0.19.12-locales.patch
BuildRequires:  gcc
BuildRequires:  desktop-file-utils
BuildRequires:  gtk3-devel >= 3.12
BuildRequires:  gettext
BuildRequires: make

%description
gentoo is a file manager written from scratch in pure C. It uses the GTK3 
toolkit for all of its interface needs. gentoo provides 100%% GUI 
configurability; no need to edit config files by hand and re-start the 
program. gentoo supports identifying the type of various files (using 
extension, regular expressions, and/or the 'file' command), and can display 
files of different types with different colors and icons. gentoo borrows 
some of its look and feel from the classic Amiga file manager 
"Directory OPUS"(TM) (written by Jonathan Potter).

%prep
%setup -q
%patch -P0 -p1
# Remove duplicated translations, keep only UTF-8
pushd po
mv ja{_JP.UTF-8,}.po
mv ja{_JP.UTF-8,}.gmo
mv ru{_RU.UTF-8,}.po
mv ru{_RU.UTF-8,}.gmo
rm -frv ru_RU.*.{po,gmo}
popd

%build
%configure
%make_build

%install
%make_install

# Included man page, not installed by default
install -pDm0644 docs/gentoo.1x %{buildroot}%{_mandir}/man1/gentoo.1
# Don't install the man page again in %doc
rm -frv docs/gentoo.1x
# Our own desktop entry, with its icon
install -pDm0644 %{SOURCE2} \
    %{buildroot}%{_datadir}/icons/hicolor/64x64/apps/gentoo.png

desktop-file-install --dir %{buildroot}%{_datadir}/applications %{SOURCE1}

%find_lang %{name}

%files -f %{name}.lang
%doc AUTHORS BUGS ChangeLog CONFIG-CHANGES CREDITS docs/
%doc NEWS README* TODO
%license COPYING
%config %{_sysconfdir}/gentoo*
%{_bindir}/gentoo
%{_datadir}/applications/gentoo.desktop
%{_datadir}/gentoo/
%{_datadir}/icons/hicolor/64x64/apps/gentoo.png
%{_mandir}/man1/gentoo.1*

%changelog
* Thu Jan 16 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.20.7-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Mon Jul 29 2024 Miroslav Suchý <msuchy@redhat.com> - 0.20.7-22
- convert license to SPDX

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.20.7-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Wed Jan 24 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.20.7-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.20.7-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.20.7-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.20.7-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.20.7-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.20.7-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.20.7-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.20.7-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.20.7-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.20.7-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.20.7-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.20.7-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.20.7-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.20.7-7
- Escape macros in %%changelog

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.20.7-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jan 11 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.20.7-5
- Remove obsolete scriptlets

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.20.7-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.20.7-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.20.7-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Jun 15 2016 David King <amigadave@amigadave.com> - 0.20.7-1
- Update to 0.20.7 (#1346831)

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.20.6-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.20.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Fri Feb 13 2015 Christopher Meng <rpm@cicku.me> - 0.20.6-1
- Update to 0.20.6
- Switching to GTK+3

* Sat Aug 16 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.19.13-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.19.13-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.19.13-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.19.13-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.19.13-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Mon Mar 26 2012 Matthias Saou <matthias@saou.eu> 0.19.13-1
- Update to 0.19.13.

* Mon Feb  6 2012 Matthias Saou <matthias@saou.eu> 0.19.12-1
- Update to 0.19.12.

* Sun Feb  5 2012 Matthias Saou <matthias@saou.eu> 0.19.6-4
- Fix desktop icon by removing trailing white space (#726376).

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.19.6-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Dec 06 2011 Adam Jackson <ajax@redhat.com> - 0.19.6-3
- Rebuild for new libpng

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.19.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Thu Dec  9 2010 Robin Lee <cheeselee@fedoraproject.org> - 0.19.6-1
- Updated to 0.19.6 (#646950)
- Undef GTK_DISABLE_DEPRECATED (#660799).

* Sun Oct 17 2010 Robin Lee <cheeselee@fedoraproject.org> - 0.19.3-1
- Update to 0.19.3
- gentoo-0.15.6-gtk-2.20.patch removed
- Include the translations
- gentoo-0.19.2-locales.patch added to exclude duplicated translations
- BR: gamin-devel removed, gettext added
- Include more documents

* Mon Apr 26 2010 Robin Lee <robinlee.sysu@gmail.com> - 0.15.6-1
- Update to 0.15.6
- Update Source0 URL
- Provide a patch to make it compiled against GTK+ 2.20
- Translations are suppressed from building. They do not actually function.
- Desktop file revised

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.15.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Thu May  7 2009 Ville Skyttä <ville.skytta at iki.fi> - 0.15.2-2
- Build with $RPM_OPT_FLAGS (#499710).
- Disable autotools dependency tracking during build for cleaner build logs
  and possible slight build speedup.

* Mon Mar 16 2009 Matthias Saou <http://freshrpms.net/> 0.15.2-1
- Update to 0.15.2, the first gtk2 version at last!
- Update desktop file Categories to System;FileManager;.
- Include new 64x64 icon (taken from the website, the sources one is 55x55).
- Install icon in hicolor directory and include all current relevant scriplets.

* Tue Feb 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org>
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Tue Feb 19 2008 Fedora Release Engineering <rel-eng@fedoraproject.org>
- Autorebuild for GCC 4.3

* Wed Aug 22 2007 Matthias Saou <http://freshrpms.net/> 0.11.56-5
- Rebuild for new BuildID feature.

* Sun Aug  5 2007 Matthias Saou <http://freshrpms.net/> 0.11.56-4
- Update License field.

* Fri Jun 22 2007 Matthias Saou <http://freshrpms.net/> 0.11.56-3
- Use DESTDIR install method.
- Remove "fedora" prefix and useless category from desktop file.
- Preserve timestamps on
- Externalize desktop file.
- Remove dist, as it might be a long while before a new rebuild takes place.

* Wed Oct 11 2006 Matthias Saou <http://freshrpms.net/> 0.11.56-2
- Fix translations (#210205).

* Mon Aug 28 2006 Matthias Saou <http://freshrpms.net/> 0.11.56-1
- Update to 0.11.56.
- FC6 rebuild.
- Drop pomkinstalldirs patch, this release fixes the problem.

* Mon Mar  6 2006 Matthias Saou <http://freshrpms.net/> 0.11.55-3
- FC5 rebuild.

* Wed Feb  8 2006 Matthias Saou <http://freshrpms.net/> 0.11.55-2
- Rebuild for new gcc/glibc.

* Mon Jun  6 2005 Matthias Saou <http://freshrpms.net/> 0.11.55-1
- Update to 0.11.55.
- Replace gnome-db-icon.png used until now with included gentoo.png.

* Thu Apr  7 2005 Michael Schwendt <mschwendt[AT]users.sf.net>
- rebuilt

* Wed Nov 10 2004 Matthias Saou <http://freshrpms.net/> 0.11.53.2
- Bump release to provide Extras upgrade path.

* Mon Nov  8 2004 Matthias Saou <http://freshrpms.net/> 0.11.53-1
- Update to 0.11.53.

* Tue Nov  2 2004 Matthias Saou <http://freshrpms.net/> 0.11.52-1
- Update to 0.11.52.
- Add gentoo-0.11.52-pomkinstalldirs.patch to fix building.

* Mon May 10 2004 Matthias Saou <http://freshrpms.net/> 0.11.51-1
- Update to 0.11.51.

* Tue May  4 2004 Matthias Saou <http://freshrpms.net/> 0.11.50-1
- Update to 0.11.50.

* Mon May  3 2004 Matthias Saou <http://freshrpms.net/> 0.11.49-1
- Update to 0.11.49.

* Fri Apr 16 2004 Matthias Saou <http://freshrpms.net/> 0.11.48-1
- Update to 0.11.48.

* Thu Apr 15 2004 Matthias Saou <http://freshrpms.net/> 0.11.47-1
- Update to 0.11.47.

* Mon Mar  1 2004 Matthias Saou <http://freshrpms.net/> 0.11.46-1
- Update to 0.11.46.

* Wed Dec  3 2003 Matthias Saou <http://freshrpms.net/> 0.11.45-1
- Update to 0.11.45.

* Mon Dec  1 2003 Matthias Saou <http://freshrpms.net/> 0.11.44-1
- Update to 0.11.44.

* Wed Nov 19 2003 Matthias Saou <http://freshrpms.net/> 0.11.43-1
- Update to 0.11.43.

* Wed Nov 19 2003 Matthias Saou <http://freshrpms.net/> 0.11.42-1
- Update to 0.11.42.
- Added icon suggested by Matthias Haase.

* Mon Nov 17 2003 Matthias Saou <http://freshrpms.net/> 0.11.41-1
- Update to 0.11.41.

* Tue Nov 11 2003 Matthias Saou <http://freshrpms.net/> 0.11.40-1
- Update to 0.11.40.

* Fri Nov  7 2003 Matthias Saou <http://freshrpms.net/> 0.11.39-2
- Rebuild for Fedora Core 1.

* Thu Oct 30 2003 Matthias Saou <http://freshrpms.net/> 0.11.39-1
- Update to 0.11.39.

* Mon Oct 27 2003 Matthias Saou <http://freshrpms.net/> 0.11.38-1
- Update to 0.11.38.

* Tue Oct 21 2003 Matthias Saou <http://freshrpms.net/>
- Update to 0.11.37.

* Fri Oct  3 2003 Matthias Saou <http://freshrpms.net/>
- Update to 0.11.35.

* Mon Mar 31 2003 Matthias Saou <http://freshrpms.net/>
- Rebuilt for Red Hat Linux 9.

* Sun Sep 29 2002 Matthias Saou <http://freshrpms.net/>
- Rebuilt for Red Hat Linux 8.0.
- New menu entry.

* Mon Sep  9 2002 Matthias Saou <http://freshrpms.net/>
- Update to 0.11.34.

* Mon Aug 26 2002 Matthias Saou <http://freshrpms.net/>
- Update to 0.11.32.

* Mon Aug 12 2002 Matthias Saou <http://freshrpms.net/>
- Update to 0.11.31.

* Mon Jul 22 2002 Matthias Saou <http://freshrpms.net/>
- Update to 0.11.30.

* Fri Jul 19 2002 Matthias Saou <http://freshrpms.net/>
- Update to 0.11.29.

* Thu Jul 18 2002 Matthias Saou <http://freshrpms.net/>
- Update to 0.11.28.
- Added the lang stuff.

* Tue Jun 25 2002 Matthias Saou <http://freshrpms.net/>
- Update to 0.11.27.

* Mon Jun 10 2002 Matthias Saou <http://freshrpms.net/>
- Update to 0.11.26.

* Wed Jun  5 2002 Matthias Saou <http://freshrpms.net/>
- Update to 0.11.25.

* Tue Apr  2 2002 Matthias Saou <http://freshrpms.net/>
- Update to 0.11.23.

* Thu Mar 14 2002 Matthias Saou <http://freshrpms.net/>
- Update to 0.11.22.

* Sun Feb 24 2002 Matthias Saou <http://freshrpms.net/>
- Update to 0.11.21.

* Fri Feb 22 2002 Matthias Saou <http://freshrpms.net/>
- Update to 0.11.20.

* Mon Feb 11 2002 Matthias Saou <http://freshrpms.net/>
- Update to 0.11.19.

* Mon Oct 15 2001 Matthias Saou <http://freshrpms.net/>
- Update to 0.11.18.

* Mon Aug 27 2001 Matthias Saou <http://freshrpms.net/>
- Update to 0.11.17.
- The sources are now much cleaner, so hacks were removed from the spec.

* Thu Jul  5 2001 Matthias Saou <http://freshrpms.net/>
- Update to 0.11.16.
- Spec file cleanup for Red Hat 7.1.

* Fri Sep 15 2000 Ryan Weaver <ryanw@infohwy.com>
  [gentoo-0.11.15-1]
- Definition of demonstration SelectRE-work-a-like button command
  changed, since it was broken. Also added glob check button.
- Lack of internal quoting caused Dir{To,From}Other to fail on
  paths containing spaces, as did the shortcuts. Fixed.
- Changed appearance of check buttons {Ix} input dialog codes.
- Having lurked among the giants of comp.lang.c for at least five
  years, I finally realized that identifiers whose names begin
  with an underscore immediately followed by an upper case letter
  are reserved for the implementation. Since I, for some historical
  reason, tend to use structure tags formed like that, gentoo was
  very much in violation of the holy scripture of ISO C. This has
  now been fixed, of course (except in widgets/). Feels good. :)
- Being urged on by a Brazilian gentoo user, Alceu Rodrigues de
  Freitas Junior, I caved in and went through the code, marking
  all strings suitable for translation using gettext. A translation
  to my own mother tongue, Swedish, is included in the locale/sv/
  directory. gentoo's I18N support is very early, and by default
  it will not build with it included. I need help with autoconfig
  before doing that.
- Capped the percentage number in the textviewer at 100%%. :)
- Left-adjusted the filename in the progress window. :)
- Improved behavior when an operation (such as Copy or Move) is
  cancelled. Previously, it was not possible to correctly cancel
  if the files being copied were smaller than the copy buffer
  size, and the 'keep full-sized copy on error?' flag was on.
- A long operation can now be cancelled by simply closing the
  progress-reporting window.
- Made parsing of {Fup} (among other things, hopefully) work
  better when 'treat focus as selection?' flag is on. Sneaky.
- Test-compiled against glib and GTK+ version 1.2.8. Went fine.
- Fixed buglet that prevented modes (aka permissions) from being
  formatted correctly. Reported by Erik Johansson.
- Banged a bit on the page up/down response for the focus bar.
  Way less ugly implementation, and (I think) better behavior
  now. Still wish GTK+ permitted use of it's built-in focusing
  bar, though. :(
- Updated to the latest version (0.5) of Johan Hanson's
  odemilbutton widget.

* Wed Apr 19 2000 Ryan Weaver <ryanw@infohwy.com>
  [gentoo-0.11.14-3]
- Doh!. Was not setting default icon path in default gentoorc. Fixed.
  Thanks Udo K. Schuermann <walrus@ringlord.com>.

* Mon Apr 17 2000 Ryan Weaver <ryanw@infohwy.com>
  [gentoo-0.11.14-1]
- Added support for extracting tar.gz, tar.bz2, and zip files to
  the example config. Select archive, right click, then choose
  the "extract" item in the "File Action" submenu.
- Due to an internal quoting problem, MkDir would fail to enter
  the created directory if the name contained spaces. Fixed.
- The Makefile no longer attempts to create a backup of the config,
  and only installs the supplied example if no old config exists.
- The ChOwn command now uses combo boxes rather than menus to
  display the system data, and also allows you to type in a
  user and/or group number or name directly. Way nicer.
- Brought back the 'grab' button in the window pos/size config,
  but only for the main window. Should make a few users happy. :)
- Altered the huge parent buttons' relief style; they now look
  more like wide borders, which JH and I find less distracting.
- Added an option (hidden away in the Command Options page,
  DpFocus tab) that makes gentoo move the focus row to the last
  row selected using the mouse. Only works if focusing is on.
- The MenuPopup command can now be bound to a keyboard key, just
  like any other command. Previously, it could only be bound to
  a mouse button. Bound to Ctrl+Space in example config.
- Added Ctrl+A and Shift+Ctrl+A as keyboard shortcuts for the
  [Select] All and None commands, respectively. :)
- Improved ANSI compliance by removing use of "str" as a prefix
  in function names. :)
- A pane's contents can now be sorted on any content type, not
  just those that are displayed. There is currently no way of
  changing to a non-displayed type without opening the config
  window, though.
- Touched up the sorting code somewhat, and while doing that
  noted that user and group names could not actually be sorted
  on as text. They sure can now.
- Fixed horrible bug in the {}-code parsing and handling, that
  made gentoo segfault when certain sequences of commands were
  run. Reported by T. Tilton.

* Mon Mar 20 2000 Ryan Weaver <ryanw@infohwy.com>
  [gentoo-0.11.13-1]
- Fixed incredibly stupid bug (reported by plenty of people, it's
  nice to know people care :) which prevented the text viewer
  window from closing when it should. It's a two-line fix.
- If you enable the "System Default" Control key mode in the
  dirpane config, it will now work.
- There was some broken logic related to quitting and the dialog
  that asks about saving changed configs. Fixed that, and also
  cleaned up the code significantly, removing duplicate stuff.

* Mon Mar  6 2000 Ryan Weaver <ryanw@infohwy.com>
  [gentoo-0.11.12-1]
- I'm reasonably sure I fixed a bug which caused a crash if you
  hit enter after entering an *empty* directory using the key-
  board-controlled focusing mechanism.
- Added support for tall, thin, parent buttons along the outer
  edges in the panes. Enable through the "Huge Parent Button?"
  checkbox in the config. The position and action of these is
  currently not configurable; it's always outer edge & DirParent.
- Incorporated alternative implementation of the GtkLabel widget
  provided by Johan Hanson. This label implementation is only used
  for the status line in the top of the window, which reportedly
  had refresh-problems with some pixmap-based GTK+ themes.
- Redid the code for the textviewer, which was very old and some-
  what confused. This might make it support mouse wheel scrolling
  better. Since I don't have a wheelie mouse, I can't test it...
- Fixed tiny bug which caused GTK+ warnings if you hit TAB in the
  command selection dialog without having typed anything first.
- Implemented a Join command, to counter the (still incomplete)
  Split command. Pretty neat, with DnD reordering.
- gentoo can now optionally ignore the state of the NumLock key
  when parsing keyboard and mouse input. Enable the check button
  in the bottom of the Controls config page. Note that only the
  input event is filtered, not the definition (do not use NumLock
  in actual mappings with this flag on).
- New version of the odscrolledbox widget, provided by Johan
  Hanson as always. Should fix some smudgy redrawing problems.
- Brought the (c) in the About box into the 21th century, added
  acknowledgement (and mail address) of Johan Hanson's work.
- Added recognition and viewing of LHa compressed files to the
  example config. Requires the 'lha' external command.
- gentoo can now remember the position and size of the config and
  textviewer windows, in addition to the main window. See config
  page labeled "Windows" (was "Pos & Size" previously). Eh, also
  see the BUGS file, since this feature has a few problems still. :(
- Tweaked code that dealt with 64-bit stuff; gentoo should now
  compile better on Linux/Alpha platforms.
- Selected content in the right-hand list in the Dirpane config
  page can now be reordered directly, by dragging. You can still
  use the up/down buttons below the list, like always.
- Er, not a fix per se, but this version of gentoo has been
  compiled and executed using GTK+ 1.2.7. No extensive tests,
  though.

* Mon Nov 22 1999 Ryan Weaver <ryanw@infohwy.com>
  [gentoo-0.11.11-1]
- Tweaked the FileAction command slightly: now it will stop running
  the action if the selection is empty. This helps when you run a
  command containing e.g. a {Fu} code on more than one file, since
  it will then just run the command once, then stop since the {Fu}
  "consumed" the entire selection. Hopefully this is not a bad thing.
- The GetSize command no longer loses track of the pane's vertical
  position.
- The pane centering on startup was changed back to the pre-0.11.10
  behavior, since the "fix" didn't help the user who reported the
  problem. Weird.
- Rewrote core file copying routine, used by Copy, CopyAs, Move,
  and other commands. It now handles "magic" files whose length
  looks like zero (like most files in the /proc filesystem). It's
  also shorter, simpler, and possibly a tiny bit faster.
- Fixed semi-obscure bug in the Split command; it wouldn't close
  output files on failed writes. Oops.
- In an attack of POSIX panic, I removed all my symbols whose names
  ended in _MAX, leaving only standard ones. Touched ~130 places.
- The SelectRE command now lets you chose what column content you
  wish to match against. This is sometimes useful, for example you
  could use the following command to select all rows whose files
  have an odd size: 'SelectRE glob=0 full=0 content=size [13579]$'.
     See "docs/scratch/command_args.txt" for a brief table of
  content names.
- Removed all uses of stdlib's malloc() & free(), replacing them
  with glib's g_XXX work-alikes, making the code more consistent.
- Added tooltips to the pane control widgets (the parent button,
  the path entry field, and the cryptic 'H' hide button).
- RTFM:ed a bit, and fixed example config's "view_man" command to
  stop emitting control codes for bold and underline. This makes
  it work better with gentoo's viewer. Unsure about portability.
- Added type, style, and view support for AVI and MPEG video clips
  to the example config. Both use 'xanim' for view. Untested. Also
  added support for IFF-ILBM bitmap images, through 'xv' as always.
- Added a new command, DpFocusPath, which moves GTK+'s input focus
  to the current pane's path entry box. Bound to shift+Return in
  the example config. Call with select=1 to select contents, too.
- Fixed buglet which made it annoying to bind commands to Return,
  since the config window's default button ("OK") would trigger.

* Tue Nov  9 1999 Ryan Weaver <ryanw@infohwy.com>
  [gentoo-0.11.10-1]
- Got mail from Jesse Perry <jap@unx.dec.com>, reporting problems
  building gentoo on an Alpha, running Tru64. Luckily, the report
  (and followups) included lots of detail and helpful hints, so I
  went over the offending code. Hopefully it works now.
- I still got the expand/collapse tracking in the Styles config
  page wrong. <HOMER>Duh!</HOMER> Fixed again. This time, for sure!
- Wrote a new command, RenameRE. It provides two ways of doing search
  and replace over selected file names, and then renaming the files.
  Learn about in "docs/scratch/renamere.txt". Recommended reading!
- Fixed bug which prevented an error from the Rename command (and
  others, no doubt) from showing up.
- Did a long-overdue, minimal, change in the way the active pane gets
  hilighted, now uses Johan Hanson's code in "colorutil.c". Should
  work better if you're running a themed GTK+.
- Pressing return after entering a path name now causes that path
  to be entered, instead of (uselessly) popping up the combo menu
  showing directory history. Oops.
- When running a command bound to a key, the key press signal is
  no longer propagated to GTK+; gentoo consumes it. This makes things
  work better when you bind stuff to e.g. cursor keys, which are
  used by GTK+ to control focus. A neat one-line fix.
- The 'view_tar_bzip2' command in the example config has been made
  more portable (uses --use-compress-prog=bzip2 rather than -y).
- If you attempt to DirRescan a directory which no longer exists,
  you will get an informative message. Better than silence.
- Included a new icons package from Johan Hanson (<johan@tiq.com>).
  There are around 20 new icons, including a very cute Commodore
  logo for SID music files! Check them out in the icons/ subdir!
- Fixed a portability problem in dirpane.c; a reference to strncmp().
- Upgraded my home development machine to GTK+/glib 1.2.6, which
  went fairly smooth. It exposed a bug in the config GUI, though.
- The centering of the panes is now done later during startup,
  since one user reported problems with it. This is too bad, since
  it now looks kind of worse during startup. :(

