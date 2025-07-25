%define gettext_package redhat-menus

Summary: Configuration and data files for the desktop menus
Name: redhat-menus
Version: 12.0.2
Release: 30%{?dist}
URL: http://www.redhat.com
#FIXME-> There is no hosting website for this project.
Source0: %{name}-%{version}.tar.gz
License: GPL-1.0-or-later
BuildArch: noarch
BuildRequires: make
BuildRequires:  gcc
BuildRequires: desktop-file-utils
BuildRequires: intltool

%description
This package contains the XML files that describe the menu layout for
GNOME and KDE, and the .desktop files that define the names and icons
of "subdirectories" in the menus.

%prep
%setup -q

%build
%configure
make %{?_smp_mflags}

%install
make install DESTDIR=$RPM_BUILD_ROOT INSTALL="install -p"

%find_lang %{gettext_package}

# create the settings-merged to prevent gamin from looking for it
# in a loop
mkdir -p $RPM_BUILD_ROOT%{_sysconfdir}/xdg/menus/settings-merged ||:

%files  -f %{gettext_package}.lang
%doc COPYING
%dir %{_sysconfdir}/xdg/menus
%dir %{_sysconfdir}/xdg/menus/applications-merged
%dir %{_sysconfdir}/xdg/menus/preferences-merged
%dir %{_sysconfdir}/xdg/menus/preferences-post-merged
%dir %{_sysconfdir}/xdg/menus/settings-merged
%config %{_sysconfdir}/xdg/menus/*.menu
%exclude %{_datadir}/desktop-menu-patches/*.desktop
%{_datadir}/desktop-directories/*.directory

%changelog
* Fri Jul 25 2025 Fedora Release Engineering <releng@fedoraproject.org> - 12.0.2-30
- Rebuilt for https://fedoraproject.org/wiki/Fedora_43_Mass_Rebuild

* Sat Jan 18 2025 Fedora Release Engineering <releng@fedoraproject.org> - 12.0.2-29
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 12.0.2-28
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Mon Jun 17 2024 Miroslav Suchý <msuchy@redhat.com> - 12.0.2-27
- convert license to SPDX

* Fri Jan 26 2024 Fedora Release Engineering <releng@fedoraproject.org> - 12.0.2-26
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 12.0.2-25
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 12.0.2-24
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 12.0.2-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 12.0.2-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 12.0.2-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 12.0.2-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 12.0.2-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 12.0.2-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 12.0.2-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 12.0.2-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 12.0.2-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 12.0.2-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 12.0.2-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 12.0.2-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 12.0.2-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 12.0.2-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 12.0.2-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 12.0.2-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 12.0.2-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 12.0.2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 12.0.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 12.0.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 12.0.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Thu Sep 16 2010 Parag Nemade <paragn AT fedoraproject.org> 12.0.2-2
- Merge-review cleanup (#226364)

* Wed Apr  7 2010 Matthias Clasen <mclasen@redhat.com> - 12.0.2-1
- Don't let release notes show up in Applications>Other

* Mon Nov 30 2009 Matthias Clasen <mclasen@redhat.com> - 12.0.1-2
- Drop desktop-menu-patches

* Thu Sep 24 2009 Matthias Clasen <mclasen@redhat.com> - 12.0.1-1
* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 10.0.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Wed Feb 25 2009 Matthias Clasen <mclasen@redhat.com> - 10.0.1-3
- Make adding submenus to Preferences work

* Fri Feb  6 2009 Matthias Clasen <mclasen@redhat.com> - 10.0.1-2
- Remove the submenus from Preferences

* Mon Nov 10 2008 Ray Strode <rstrode@redhat.com> - 10.0.1-1
- Update translations (bug 470652)

* Fri Oct 24 2008 Matthias Clasen <mclasen@redhat.com> - 10.0.0-2
- One more directory rename. Thank you, gnome-menus

* Tue Oct 14 2008 Ray Strode <rstrode@redhat.com> - 10.0.0-1
- Update to 10.0.0 to pull in latest translations

* Mon Oct  6 2008 Matthias Clasen <mclasen@redhat.com> - 8.9.11-7
- Remove obsolete no translation (#465673)

* Sun Aug 24 2008 Matthias Clasen <mclasen@redhat.com> - 8.9.11-6
- Use standard icon names where available 

* Wed Aug 13 2008 Matthias Clasen <mclasen@redhat.com> - 8.9.11-5
- Own /etc/xdg/menus

* Tue Jul  8 2008 Matthias Clasen <mclasen@redhat.com> - 8.9.11-4
- Fix icons for menus

* Fri Mar 14 2008 Matthias Clasen <mclasen@redhat.com> - 8.9.11-3
- Remove special handling for pirut

* Sat Jan  5 2008 Matthew Barnes <mbarnes@redhat.com> - 8.9.11-2
- Send all Evolution bugs to the new BugBuddyBugs Bugzilla component.
  (GNOME bug #507311)

* Mon Oct  1 2007 Matthias Clasen <mclasen@redhat.com> - 8.9.11-1
- Move patches upstream
- Fix license field
- Spec file fixes

* Fri Sep  7 2007 Matthias Clasen <mclasen@redhat.com> - 8.9.10-10
- More category finetuning; remove remaining overrides

* Thu Sep  6 2007 Ray Strode <rstrode@redhat.com> - 8.9.10-9
- create /etx/xdg/menus/settings-merged by default

* Wed Jul  2 2007 Matthias Clasen <mclasen@redhat.com> - 8.9.10-8
- More category finetuning

* Wed Jun 27 2007 Matthias Clasen <mclasen@redhat.com> - 8.9.10-7
- More category finetuning

* Wed Jun 27 2007 Matthias Clasen <mclasen@redhat.com> - 8.9.10-6
- Reduce hardcoded applications where categories have been fixed

* Wed Jun 27 2007 Matthias Clasen <mclasen@redhat.com> - 8.9.10-5
- Clean up use of categories in menu files

* Tue Jun 26 2007 Ray Strode <rstrode@redhat.com> - 8.9.10-4
- hide screensavers from menus (bug 241058)

* Thu Jun 07 2007 Matthew Barnes <mbarnes@redhat.com> - 8.9.10-3
- Add X-GNOME-Bugzilla-Version to Evolution desktop files (#243101).
- Bump evolution-data-server version in desktop files to 1.12.

* Sun May  6 2007 Matthias Clasen <mclasen@redhat.com> - 8.9.10-2
- Don't own directories that are already owned by 
  the filesystem package

* Thu Mar 29 2007 Ray Strode <rstrode@redhat.com> - 8.9.10-1
- add encoding to all the desktop files that don't have it 
  (bug 105796)

* Tue Mar 27 2007 Matthias Clasen <mclasen@redhat.com> - 7.8.12-1
- Use System-Tools for Application > System

* Wed Mar 21 2007 Matthew Barnes <mbarnes@redhat.com> - 7.8.11-2
- Update evolution files, add X-GNOME-Bugzilla-Component (#224199)

* Mon Mar 19 2007 Matthias Clasen <mclasen@redhat.com> - 7.8.11-1
- Don't use Application category

* Tue Feb 13 2007 Matthias Clasen <mclasen@redhat.com> - 7.8.10-1
- Use Education

* Fri Feb  9 2007 Matthias Clasen <mclasen@redhat.com> - 7.8.9-6
- Really don't show gdmflexiserver
 
* Thu Feb  8 2007 Matthias Clasen <mclasen@redhat.com> - 7.8.9-5
- Reduce the amount of System menus

* Tue Jan 23 2007 Matthias Clasen <mclasen@redhat.com> - 7.8.9-4
- Once more with better categories

* Tue Jan 23 2007 Matthias Clasen <mclasen@redhat.com> - 7.8.9-3
- Update preferences.menu for the control center shell

* Thu Jan 11 2007 Matthias Clasen <mclasen@redhat.com> - 7.8.9-2
- Resolve a conflict with gnome-menus

* Sun Dec 10 2006 Ray Strode <rstrode@redhat.com> - 7.8.9-1
- Update to 7.8.9

* Mon Nov 20 2006 Ray Strode <rstrode@redhat.com> - 6.7.8-2
- Move <DefaultMergeDirs/> to end of applications.menu

* Mon Nov  6 2006 Matthias Clasen <mclasen@redhat.com> - 6.7.8-1
- Pick up missing translations  (#214241)

* Wed Nov  1 2006 Matthias Clasen <mclasen@redhat.com> - 6.7.7-1
- Add a documentation menu (#213191)

* Tue Oct 31 2006 Than Ngo <than@redhat.com> - 6.7.6-2.el5
- add missing kdelegacydirs #213202

* Sun Aug 20 2006 Matthias Clasen <mclasen@redhat.com> - 6.7.6-1.fc6
- Make menu editors happy

* Thu Jun 08 2006 Jesse Keating <jkeating@redhat.com> - 6.7.5-3
- Add missing BR of perl-XML-Parser, gettext

* Thu Mar 2 2006 Bill Nottingham <notting@redhat.com> - 6.7.5-1
- add locales (#176139)

* Thu Feb 9 2006 Matthias Clasen <mclasen@redhat.com> - 6.6.5-1
- Really move pirut to toplevel

* Tue Feb 7 2006 Ray Strode <rstrode@redhat.com> - 6.6.4-1
- use gnome icon names for "-Other" menu files

* Sun Feb 5 2006 Matthias Clasen <mclasen@redhat.com> - 6.5.4-3
- Add missing requires

* Wed Feb 1 2006 Ray Strode <rstrode@redhat.com> - 6.5.4-2
- fix applications menu

* Wed Feb 1 2006 Ray Strode <rstrode@redhat.com> - 6.5.4-1
- merge /usr/local/share/applications
- ship separate directory file for System menu

* Mon Jan 30 2006 Ray Strode <rstrode@redhat.com> - 5.5.5-2
- a few more tweaks needed to get pirut in toplevel applications
  menu

* Mon Jan 30 2006 Ray Strode <rstrode@redhat.com> - 5.5.5-1
- Update to 5.5.5
- put pirut in toplevel applications menu

* Tue Jan  3 2006 Matthias Clasen <mclasen@redhat.com> - 5.0.8-1
- Make "Other" disappear again

* Fri Dec 09 2005 Jesse Keating <jkeating@redhat.com>
- rebuilt

* Wed Dec  7 2005 Matthias Clasen <mclasen@redhat.com> - 5.0.7-3
- hide the separator as well

* Fri Dec  2 2005 Jeremy Katz <katzj@redhat.com> - 5.0.7-2
- hide system-config-packages from the applications menu until it works again

* Tue Nov 22 2005 Matthias Clasen <mclasen@redhat.com> 5.0.7-1
- Clean up menus

* Wed Nov 16 2005 Matthias Clasen <mclasen@redhat.com> 5.0.6-1
- Hide userinfo, userpassword and gdmphotosetup by default

* Fri Oct 28 2005 Matthias Clasen <mclasen@redhat.com> 5.0.5-1
- Hide usermount by default

* Tue Oct 25 2005 David Malcolm <dmalcolm@redhat.com> - 5.0.4-1
- Split the evolution desktop file into four separate ones: one per component.
  Force people to update evolution, to avoid it using a stale symlink. 
  (#170799).

* Fri Oct 21 2005 Matthias Clasen <mclasen@redhat.com> 5.0.2-1
- Hide gfloppy by default

* Tue Sep 27 2005 Ray Strode <rstrode@redhat.com> 5.0.1-1
- don't use dir name preferences-merged.  It has special
  significance (bug 169108)

* Mon Sep 26 2005 Ray Strode <rstrode@redhat.com> 5.0.0-2
- one commented out patch was actually important and 
  shouldn't have been removed.

* Mon Sep 26 2005 Ray Strode <rstrode@redhat.com> 5.0.0-1
- add a preferences-merged dir for per package
  preference menus overriding
- remove old patches

* Thu Apr 14 2005 Ray Strode <rstrode@redhat.com> 3.8.0-1
- don't include kde legacy stuff anymore, since
  kde uses it's own applications menu file now and it 
  breaks gnome (bug 153125)

* Thu Mar 31 2005 Matthias Clasen <mclasen@redhat.com> 3.7.1-9
- don't pick up a pointless Desktop/System directory

* Thu Mar 31 2005 Than Ngo <than@redhat.com> 3.7.1-8
- don't mess gnome menu up

* Mon Mar 21 2005 Than Ngo <than@redhat.com> 3.7.1-7
- add mssing kwrite/kate/kedit, kcontrol center, System setting
  in menu #147121, #12218, #1221811, #143937
- get rid of capplets from preferences.menu, #149233
- fix icon entry in desktop file #143336

* Fri Feb  8 2005  <mclasen@redhat.com> - 3.7.1-6
- Don't pick up duplicates in the Others menu

* Thu Feb  3 2005  <mclasen@redhat.com> - 3.7.1-5
- Add settings.menu

* Mon Nov 22 2004  <jrb@redhat.com> - 3.7.1-3
- Sync to upstream
- #rh138282# Get redhat-evolution.desktop.in

* Mon Nov 22 2004 Dan Williams <dcbw@redhat.com> 3.7-5
- #rh137520# Add "application/x-ole-storage" to Calc, Impress, and Writer
 desktop files, so Evolution can associate these with OOo

* Tue Nov 16 2004 Dan Williams <dcbw@redhat.com> 3.7-4
- #rh137520# Add more supported mime-types to OpenOffice.org .desktop files

* Mon Nov  1 2004 <dcbw@redhat.com> - 3.7-2
- Gratuitous version bump from upstream
- #rh74651# no mimetype entries for microsoft offic
- #rh136731# wordperfect files (.wpd) should be associated with openoffice

* Fri Oct 22 2004  <jrb@redhat.com> - 1.13-1
- New release.  This just has new translations and an evolution desktop file

* Mon Oct 18 2004  <jrb@redhat.com> - 1.12-1
- new version to deal with default mail client

* Mon Oct 18 2004  <jrb@redhat.com> - 1.11-1
- New release to get new translations and change the default web browser

* Wed Oct 13 2004 Colin Walters <walters@redhat.com> 1.10-1
- Add application/ogg to redhat-audio-player.desktop,
  for bug 134547 (hi Sopwith)
  
* Wed Oct 13 2004 Bill Nottingham <notting@redhat.com> 1.9-2
- own /etc/xdg (#130596)

* Wed Sep 29 2004 Ray Strode <rstrode@redhat.com> 1.9-1
- release 1.9, add gthumb desktop file  

* Fri Sep 24 2004 Ray Strode <rstrode@redhat.com> 1.8-1
- release 1.8, remove AC_PROG_LIBTOOL from configure.in
- release 1.7, remove gnome-control-center.desktop

* Wed Sep 22 2004 Warren Togami <wtogami@redhat.com> 1.6.1-2
- remove ugly hacks so package is easier to maintain

* Tue Sep 21 2004 Seth Nickell <snickell@redhat.com> 1.6.1-1
- release 1.6.1, don't call AC_PROG_LIBTOOL

* Tue Sep 21 2004 Seth Nickell <snickell@redhat.com> 1.6-1
- release 1.6, add a bunch of translations to the build

* Fri May 07 2004 Than Ngo <than@redhat.com> 1.4.1-1
- release 1.4.1, add More submenu, fix Preferences/Others menu

* Wed May 05 2004 Warren Togami <wtogami@redhat.com> 1.4-2
- Temporary hacks for Preferred Browser launching in FC2

* Tue Mar 16 2004 Than Ngo <than@redhat.com> 1.3-1
- Release 1.3, add applications-kmenuedit.menu that makes kmenuedit working

* Tue Mar 16 2004 Than Ngo <than@redhat.com> 1.2-1
- Release 1.2, fixed KDE menu issue

* Fri Mar 12 2004 Than Ngo <than@redhat.com> 1.1-1
- Release 1.1, cleanup KDE menus, get rid of KDE stuffs which are now included in kde package

* Thu Mar 11 2004 Seth Nickell <snickell@redhat.com>
- Release 1.0 which conforms to xdg menu spec 0.8

* Fri Feb 13 2004 Elliot Lee <sopwith@redhat.com>
- rebuilt

* Fri Oct  3 2003 Havoc Pennington <hp@redhat.com> 0.40-1
- 0.40

* Mon Jul 28 2003 Than Ngo <than@redhat.com> 0.39-2
- rebuilt

* Mon Jul 28 2003 Than Ngo <than@redhat.com> 0.39-1
- 0.39, clean up

* Thu Feb  6 2003 Havoc Pennington <hp@redhat.com> 0.37-1
- 0.37

* Wed Jan 29 2003 Havoc Pennington <hp@redhat.com>
- 0.36 fixes missing Preferences in start-here hopefully

* Mon Jan 27 2003 Havoc Pennington <hp@redhat.com>
- 0.35

* Wed Jan 22 2003 Tim Powers <timp@redhat.com>
- rebuilt

* Wed Jan 22 2003 Than Ngo <than@redhat.com>
- 0.34, enable start-here.menu

* Sat Jan 11 2003 Havoc Pennington <hp@redhat.com>
- 0.33

* Thu Jan  9 2003 Havoc Pennington <hp@redhat.com>
- 0.32

* Tue Jan  7 2003 Havoc Pennington <hp@redhat.com>
- 0.31

* Thu Dec 12 2002 Havoc Pennington <hp@redhat.com>
- 0.29, rebuild

* Wed Dec  4 2002 Than Ngo <than@redhat.com>
- 0.27, added some new catagories for KDE 3.1

* Tue Sep 03 2002 Phil Knirsch <pknirsch@redhat.com>
- 0.26 fixed start-here.menu missing </Folder> tag for Preferences

* Fri Aug 30 2002 Havoc Pennington <hp@redhat.com>
- 0.25 with htmlview, fixed start-here.menu

* Tue Aug 27 2002 Havoc Pennington <hp@redhat.com>
- 0.23 with new translations, KDE MIME fixes, openoffice Exec= fixes
- don't munge en_US text, broke docs. Back to just "Web Browser"

* Fri Aug 23 2002 Havoc Pennington <hp@redhat.com>
- 0.22 new translations
- munge en_US text to "Mozilla Web Browser" etc.

* Wed Aug 21 2002 Havoc Pennington <hp@redhat.com>
- 0.21 with new translations

* Fri Aug 16 2002 Havoc Pennington <hp@redhat.com>
- 0.20 with new icons, etc.

* Fri Aug 16 2002 Havoc Pennington <hp@redhat.com>
- new icons, translations
- drop control-center patch, use from cvs

* Thu Aug 15 2002 Jonathan Blandford <jrb@redhat.com>
- move the control-center

* Wed Aug 14 2002 Havoc Pennington <hp@redhat.com>
- 0.18 with changed icons etc.

* Fri Aug  9 2002 Havoc Pennington <hp@redhat.com>
- 0.17 with System Settings submenu and translations

* Wed Aug  7 2002 Havoc Pennington <hp@redhat.com>
- 0.16 with start here

* Wed Aug  7 2002 Havoc Pennington <hp@redhat.com>
- 0.15 with placeholder icons for panel desktop files

* Tue Aug  6 2002 Havoc Pennington <hp@redhat.com>
- 0.14 with KDE preferences submenus

* Fri Aug  2 2002 Havoc Pennington <hp@redhat.com>
- 0.12 with server-settings and system-settings

* Wed Jul 31 2002 Havoc Pennington <hp@redhat.com>
- make it noarch

* Wed Jul 31 2002 Havoc Pennington <hp@redhat.com>
- 0.11 with audio player desktop file

* Wed Jul 31 2002 Havoc Pennington <hp@redhat.com>
- 0.10 trying Extras instead of All Apps, and add Advanced to preferences

* Tue Jul 30 2002 Havoc Pennington <hp@redhat.com>
- 0.9, has gdmsetup replacement desktop file

* Mon Jul 29 2002 Havoc Pennington <hp@redhat.com>
- 0.8

* Wed Jul 24 2002 Havoc Pennington <hp@redhat.com>
- 0.7, adds documentation submenu, strips Base-Only out of All Apps

* Wed Jul 24 2002 Havoc Pennington <hp@redhat.com>
- 0.6

* Tue Jul 23 2002 Havoc Pennington <hp@redhat.com>
- 0.5

* Sat Jul 20 2002 Than Ngo <than@redhat.com>
- add BaseGroup settings into Settings.directory

* Thu Jul 11 2002 Havoc Pennington <hp@redhat.com>
- fix group

* Mon Jun 24 2002 Havoc Pennington <hp@redhat.com>
- 0.3
- 0.4

* Fri Jun 21 2002 Tim Powers <timp@redhat.com>
- automated rebuild

* Tue Jun 11 2002 Havoc Pennington <hp@redhat.com>
- move menus to sysconfdir/X11
- hack on applications.menu a small amount. Needs
  major help.

* Tue May 28 2002 Havoc Pennington <hp@redhat.com>
- rebuild in different environment

* Tue May 28 2002 Havoc Pennington <hp@redhat.com>
- description would be good

* Tue May 28 2002 Havoc Pennington <hp@redhat.com>
- Initial build.


