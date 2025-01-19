
# trim changelog included in binary rpms
%global _changelog_trimtime %(date +%s -d "1 year ago")

Name:	 kile
Summary: (La)TeX source editor and TeX shell
Version: 2.9.94
%global respin -1
Release: 4%{?dist}

License: GPL-2.0-or-later
URL:     https://kile.sourceforge.io/
Source0: https://downloads.sourceforge.net/sourceforge/kile/kile-%{version}%{?pre}%{?respin}.tar.bz2

# patch to org.kde.kile.desktop by David Auer <dreua@posteo.de>
Patch0:  kile-2.9.94-fix-missing-icon.patch

BuildRequires: desktop-file-utils
BuildRequires: libappstream-glib

BuildRequires: gettext

BuildRequires: extra-cmake-modules >= 6.0.0
BuildRequires: cmake(KF6Codecs)
BuildRequires: cmake(KF6Config)
BuildRequires: cmake(KF6CoreAddons)
BuildRequires: cmake(KF6Crash)
BuildRequires: cmake(KF6DBusAddons)
BuildRequires: cmake(KF6DocTools)
BuildRequires: cmake(KF6GuiAddons)
BuildRequires: cmake(KF6I18n)
BuildRequires: cmake(KF6IconThemes)
BuildRequires: cmake(KF6KIO)
BuildRequires: cmake(KF6Parts)
BuildRequires: cmake(KF6TextEditor)
BuildRequires: cmake(KF6TextWidgets)
BuildRequires: cmake(KF6WindowSystem)
BuildRequires: cmake(KF6XmlGui)

BuildRequires: pkgconfig(Qt6DBus)
BuildRequires: pkgconfig(Qt6Widgets)
BuildRequires: pkgconfig(Qt6Qml)
BuildRequires: pkgconfig(Qt6Test)
BuildRequires: pkgconfig(Qt6Core5Compat)

BuildRequires: cmake(Okular6)
BuildRequires: pkgconfig(poppler-qt6)

Requires: konsole-part
Requires: tex(latex)

## Optional/recommended, but not absolutely required.
#Requires: dvipdfmx

%description
Kile is a user friendly (La)TeX editor.  The main features are:
  * Compile, convert and view your document with one click.
  * Auto-completion of (La)TeX commands
  * Templates and wizards makes starting a new document very little work.
  * Easy insertion of many standard tags and symbols and the option to define
    (an arbitrary number of) user defined tags.
  * Inverse and forward search: click in the DVI viewer and jump to the
    corresponding LaTeX line in the editor, or jump from the editor to the
    corresponding page in the viewer.
  * Finding chapter or sections is very easy, Kile constructs a list of all
    the chapter etc. in your document. You can use the list to jump to the
    corresponding section.
  * Collect documents that belong together into a project.
  * Easy insertion of citations and references when using projects.
  * Advanced editing commands.


%prep
%setup -q -n %{name}-%{version}%{?pre}
%patch -P 0 -p1 -b .fix-missing-icon


%build
%cmake_kf6
%cmake_build

%install
%cmake_install

%find_lang %{name} --with-html


%check
appstream-util validate-relax --nonet %{buildroot}%{_kf6_metainfodir}/org.kde.kile.appdata.xml
desktop-file-validate %{buildroot}%{_kf6_datadir}/applications/org.kde.kile.desktop


%files -f %{name}.lang
%doc AUTHORS ChangeLog README*
%doc kile-remote-control.txt
%license COPYING
%{_kf6_bindir}/kile
%{_kf6_datadir}/config.kcfg/kile.kcfg
%{_kf6_datadir}/kconf_update/*
%{_kf6_datadir}/kile/
%{_kf6_datadir}/applications/org.kde.kile.desktop
%{_kf6_metainfodir}/org.kde.kile.appdata.xml
%{_kf6_datadir}/dbus-1/interfaces/org.kde.kile.main.xml
%{_kf6_datadir}/icons/hicolor/*/*/*
%{_kf6_datadir}/mime/packages/kile.xml
%{_kf6_datadir}/qlogging-categories6/kile.categories


%changelog
* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 2.9.94-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.9.94-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Fri Apr 19 2024 Kevin Kofler <Kevin@tigcc.ticalc.org> - 2.9.94-2
- fix Requires: konsole-part (no versioned konsole6-part Provides available)

* Thu Apr 18 2024 Kevin Kofler <Kevin@tigcc.ticalc.org> - 2.9.94-1
- update to 2.9.94-1 (3.0 beta 4, respun tarball) (#2269165, #2261281, #2268194)
- rebase fix-missing-icon patch
- do not use autosetup
- now uses Qt6/KF6 instead of Qt5/KF5, update BRs and macros, remove k(de)init
- update file list
- convert License tag to SPDX

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.9.93-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.9.93-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.9.93-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.9.93-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.9.93-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.9.93-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.9.93-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Sat Jun 12 2021 David Auer <dreua@posteo.de> - 2.9.93-6
- Fix missing icon

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.9.93-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Aug 25 2020 Christian Dersch <lupinix@mailbox.org> - 2.9.93-4
- Adapt for
  https://fedoraproject.org/wiki/Changes/CMake_to_do_out-of-source_builds

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.9.93-3
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.9.93-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jun 17 2020 Kevin Kofler <Kevin@tigcc.ticalc.org> - 2.9.93-1
- update to 2.9.93 (3.0 beta 3)

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.9.92-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jan 17 2020 Marek Kasik <mkasik@redhat.com> - 2.9.92-4
- Rebuild for poppler-0.84.0

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.9.92-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.9.92-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Jul 26 2018 Rex Dieter <rdieter@fedoraproject.org> - 2.9.92-1
- kile-2.9.92

* Thu Jul 26 2018 Rex Dieter <rdieter@fedoraproject.org> - 2.1.3-16
- .spec cleanup, use %%make_build %%license
- use scriptlets only on older releases that need them

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.3-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.3-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.3-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.3-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.3-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.3-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.1.3-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat May 02 2015 Kalev Lember <kalevlember@gmail.com> - 2.1.3-8
- Rebuilt for GCC 5 C++11 ABI change

* Sat Jan 31 2015 Rex Dieter <rdieter@fedoraproject.org> 2.1.3-7
- kde-apps cleanup, .spec cleanup

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.1.3-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Thu Jul 03 2014 Rex Dieter <rdieter@fedoraproject.org> 2.1.3-5
- opimize mimeinfo scriptlet, minor .spec cleanup

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.1.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.1.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.1.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Wed Sep 26 2012 Kevin Kofler <Kevin@tigcc.ticalc.org> - 2.1.3-1
- update to 2.1.3 (bugfix release, #860363)
- drop upstreamed kde#299569 patch

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.1.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Tue May 08 2012 Kevin Kofler <Kevin@tigcc.ticalc.org> - 2.1.2-2
- fix kile process remaining in memory after closing (kde#299569)

* Sun Apr 29 2012 Kevin Kofler <Kevin@tigcc.ticalc.org> - 2.1.2-1
- update to 2.1.2 (bugfix release, #816521)

* Sun Jan 29 2012 Kevin Kofler <Kevin@tigcc.ticalc.org> - 2.1.1-1
- update to 2.1.1 (bugfix release, #785528)
- don't Require kate-part on EL (no such package or Provides)
- don't Require konsole-part on F15 nor EL (no such package or Provides)

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Nov 15 2011 Rex Dieter <rdieter@fedoraproject.org> 2.1-2
- Requires: kate-part konsole-part (#744443)

* Mon Jun 13 2011 Kevin Kofler <Kevin@tigcc.ticalc.org> - 2.1-1
- update to 2.1 final, finally includes translations (drop extra tarball)

* Mon Feb 07 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.1-0.11.b5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Fri Jan 21 2011 Kevin Kofler <Kevin@tigcc.ticalc.org> - 2.1-0.10.b5
- update to 2.1b5 and matching translations (revision 1211084 from 2011-01-03)
- drop docbook version hack and completion-kde46 patch, fixed upstream

* Tue Dec 07 2010 Kevin Kofler <Kevin@tigcc.ticalc.org> - 2.1-0.9.b4
- backport upstream patch to make completion work with kdelibs 4.6
- update docbook version to make doc-translations build with kdelibs 4.6

* Sat Apr 17 2010 Kevin Kofler <Kevin@tigcc.ticalc.org> - 2.1-0.8.b4
- update translations

* Mon Apr 12 2010 Rex Dieter <rdieter@fedoraproject.org> - 2.1-0.7.b4
- kile-2.1b4

* Tue Feb 02 2010 Kevin Kofler <Kevin@tigcc.ticalc.org> - 2.1-0.6.b3
- force termination when the main window is closed (#557436, kde#220343)

* Sun Dec 20 2009 Kevin Kofler <Kevin@tigcc.ticalc.org> - 2.1-0.5.b3
- add translations from l10n-kde4 SVN (revision 1055480 from Nov 28)

* Mon Nov 30 2009 Rex Dieter <rdieter@fedoraproject.org> - 2.1-0.4.b3
- kile-2.1b3

* Sun Aug 23 2009 Rex Dieter <rdieter@fedoraproject.org> - 2.1-0.3.b2
- kile-2.1b2

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.1-0.2.b1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Wed Jun 17 2009 Rex Dieter <rdieter@fedoraproject.org> - 2.1-0.1.b1
- kile-2.1b1, kde4 version, woo!

* Mon Mar 23 2009 Rex Dieter <rdieter@fedoraproject.org> - 2.0.3-3
- optimize scriptlets

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Mon Dec 15 2008 Kevin Kofler <Kevin@tigcc.ticalc.org> 2.0.3-1
- update to 2.0.3 (#476108)

* Sun Sep 28 2008 Kevin Kofler <Kevin@tigcc.ticalc.org> 2.0.2-1
- update to 2.0.2 (#464320)

* Sun Jun 22 2008 Kevin Kofler <Kevin@tigcc.ticalc.org> 2.0.1-2
- also change QuickPreview to use xdg-open (#445934 reloaded)

* Sun May 11 2008 Rex Dieter <rdieter@fedoraproject.org> 2.0.1-1
- kile-2.0.1 (#445975)
- kile should require: kdebase3 (#445933)
- kpdf preview is broken (#445934)
- drop deprecated kile-i18n references

* Fri Feb 15 2008 Rex Dieter <rdieter@fedoraproject.org> 2.0-4
- respin (new tarball)
- f9+: Requires: tex(latex)

* Sat Feb 09 2008 Kevin Kofler <Kevin@tigcc.ticalc.org> 2.0-3
- rebuild for GCC 4.3

* Thu Jan 03 2008 Kevin Kofler <Kevin@tigcc.ticalc.org> 2.0-2
- BR kdelibs3-devel (F7+, EL6+)

* Mon Nov 19 2007 Rex Dieter <rdieter[AT]fedoraproject.org> 2.0-1
- kile-2.0

* Sat Aug 25 2007 Rex Dieter <rdieter[AT]fedoraproject.org> 1.9.3-6
- patch kile.desktop to satisfy desktop-file-validate

* Sat Aug 25 2007 Rex Dieter <rdieter[AT]fedoraproject.org> 1.9.3-5
- respin (BuildID)
- BR: desktop-file-utils (again)

* Sat Aug 11 2007 Rex Dieter <rdieter[AT]fedoraproject.org> 1.9.3-3
- License: GPLv2+

* Tue Nov 28 2006 Rex Dieter <rexdieter[AT]users.sf.net> 1.9.3-2
- drop desktop-file-utils usage

* Sat Nov 25 2006 Rex Dieter <rexdieter[AT]users.sf.net> 1.9.3-1
- kile-1.9.3, CVE-2006-6085 (#217238)

* Tue Aug 29 2006 Rex Dieter <rexdieter[AT]users.sf.net> 1.9.2-4
- revert to saner/simpler symlink handling

* Mon Aug 28 2006 Rex Dieter <rexdieter[AT]users.sf.net> 1.9.2-3
- fc6 respin

* Sun Aug 27 2006 Rex Dieter <rexdieter[AT]users.sf.net> 1.9.2-1
- kile-1.9.2

* Sat Jun 24 2006 Rex Dieter <rexdieter[AT]users.sf.net> 1.9.1-1
- kile-1.9.1

* Mon May 08 2006 Rex Dieter <rexdieter[AT]users.sf.net> 1.9-2
- safer abs->rel symlink conversion 

* Fri Mar 17 2006 Rex Dieter <rexdieter[AT]users.sf.net> 1.9-1
- 1.9(final)

* Mon Mar 13 2006 Rex Dieter <rexdieter[AT]users.sf.net> 1.9-0.1.rc
- 1.9rc1

* Wed Mar 1 2006 Rex Dieter <rexdieter[AT]users.sf.net>
- fc5: gcc/glibc respin

* Thu Nov 10 2005 Rex Dieter <rexdieter[AT]users.sf.net> 1.8.3-7
- fix symlinks
- simplify configure

* Fri Oct 22 2005 Rex Dieter <rexdieter[AT]users.sf.net> 1.8.3-5
- %%description: < 80 columns
- %%post/%%postun: update-desktop-database
- touchup %%post/%%postun icon handling to match icon spec
- absolute->relative symlinks
- remove Req: qt/kdelibs crud

* Tue Oct 11 2005 Rex Dieter <rexdieter[AT]users.sf.net> 1.8.3-4
- use gtk-update-icon-cache (#170291)

* Thu Aug 18 2005 Rex Dieter <rexdieter[AT]users.sf.net> 1.8.1-3
- fix broken Obsoletes (#166300)

* Thu Jun 02 2005 Rex Dieter 1.8.1-1
- 1.8.1
- x86_64 fix (bug #161343)

* Tue May 31 2005 Rex Dieter 1.8-2
- Obsoletes: kile-i18n

* Mon May 23 2005 Rex Dieter 1.8-1
- 1.8 

* Sun May 22 2005 Jeremy Katz <katzj@redhat.com> - 1.7.1
- rebuild on all arches

* Fri Apr  7 2005 Michael Schwendt <mschwendt[AT]users.sf.net>
- rebuilt

* Wed Jan 12 2005 Rex Dieter <rexdieter[AT]users.sf.net> 0:1.7.1-3
- fix (katepart) conflicts with kde >= 3.2
- update %%description

* Mon Oct 18 2004 Rex Dieter <rexdieter at sf.net> 0:1.7.1-0.fdr.2
- -katepart: fix conflicts with kde >= 3.3 (optional)

* Mon Oct 18 2004 Rex Dieter <rexdieter at sf.net> 0:1.7.1-0.fdr.1
- 1.7.1

* Tue Sep 28 2004 Rex Dieter <rexdieter at sf.net> 0:1.6.3-0.fdr.2
- respin (against kde-3.3)

* Fri May 14 2004 Rex Dieter <rexdieter at sf.net> 0:1.6.3-0.fdr.1
- 1.6.3

* Sun Mar 28 2004 Rex Dieter <rexdieter at sf.net> 0:1.6.2-0.fdr.2
- BuildRequires: gettext

* Mon Mar 22 2004 Rex Dieter <rexdieter at sf.net> 0:1.6.2-0.fdr.1
- 1.6.2

* Wed Mar 17 2004 Rex Dieter <rexdietet at sf.net> 0:1.6.1-0.fdr.7
- fix detection/usage of desktop-file-install

* Thu Mar 16 2004 Rex Dieter <rexdieter at sf.net> 0:1.6.1-0.fdr.6
- properly fix desktop file.
- BuildRequires: fam-devel for lame/broken (err, fc2) kde builds.

* Thu Mar 11 2004 Rex Dieter <rexdieter at sf.net> 0:1.6.1-0.fdr.5
- dynamically determine versions for qt and kdelibs dependancies.

* Wed Mar 10 2004 Rex Dieter <rexdieter at sf.net> 0:1.6.1-0.fdr.4
- loosen Requires a bit

* Tue Mar 09 2004 Rex Dieter <rexdieter at sf.net> 0:1.6.1-0.fdr.3
- --disable-rpath

* Tue Mar 09 2004 Rex Dieter <rexdieter at sf.net> 0:1.6.1-0.fdr.2
- respin for kde-3.2.1

* Wed Feb 11 2004 Rex Dieter <rexdieter at sf.net> 0:1.6.1-0.fdr.1
- Allow for building on/for both kde-3.1/kde-3.2

* Sun Feb 01 2004 Rex Dieter <rexdieter at sf.net> 0:1.6.1-0.fdr.0
- 1.6.1

* Mon Dec 01 2003 Rex Dieter <rexdieter at sf.net> 0:1.6-0.fdr.5
- add BuildRequires to satisfy fedora's build system.

* Wed Nov 26 2003 Rex Dieter <rexdieter at sf.net> 0:1.6-0.fdr.4
- removed Utility;TextEditor desktop Categories.

* Wed Nov 26 2003 Rex Dieter <rexdieter at sf.net> 0:1.6-0.fdr.3
- Requires: tetex-latex
- configure --disable-rpath
- remove Obsoletes: ktexmaker2

* Mon Nov 24 2003 Rex Dieter <rexdieter at sf.net> 0:1.6-0.fdr.2
- fixup file lists
- update macros for Fedora Core support

* Sat Nov 01 2003 Rex Dieter <rexdieter at sf.net> 0:1.6-0.fdr.1
- 1.6

* Wed Sep 17 2003 Rex Dieter <rexdieter at sf.net> 0:1.5.2-0.fdr.4
- fix missing latexhelp.html

* Thu Sep 11 2003 Rex Dieter <rexdieter at sf.net> 0:1.5.2-0.fdr.3
- patch1 

* Wed Aug 20 2003 Rex Dieter <rexdieter at sf.net> 0:1.5.2-0.fdr.2
- 1.5.2

* Fri May 30 2003 Rex Dieter <rexdieter at sf.net> 0:1.5-0.fdr.2
- re-add %%find_lang and %%doc files not present in 1.5.2a

* Thu May 29 2003 Rex Dieter <rexdieter at sf.net> 0:1.5-0.fdr.1
- resync with unstable branch.

* Fri May 16 2003 Rex Dieter <rexdieter at sf.net> 0:1.5-0.fdr.0
- bite bullet now, revert back to 1.5.
- fedora versioning.

* Fri Apr 25 2003 Rex Dieter <rexdieter at sf.net> 1.50-0.0
- 1.5 release, artificially use 1.50 so rpm thinks it is > 1.32.

* Fri Apr 25 2003 Rex Dieter <rexdieter at sf.net> 1.40-1.3
- remove %%doc NEWS

* Mon Mar 03 2003 Rex Dieter <rexdieter at sf.net> 1.40-1.2 
- version: 1.4 -> 1.40 so silly rpm knows that 1.40 is newer than 1.32
- use epochs in Obsoletes/Provides/Requires.

* Fri Feb 21 2003 Rex Dieter <rexdieter at sf.net> 1.4-1.1
- yank kmenu

* Tue Feb 18 2003 Rex Dieter <rexdieter at sf.net> 1.4-1.0
- 1.40
- use desktop-create-kmenu

* Fri Feb 07 2003 Rex Dieter <rexdieter at sf.net> 1.32-0.0
- 1.32
- kde-redhat versioning

* Tue Jan 14 2003 Rex Dieter <rdieter@unl.edu> 1.31-0
- 1.31
- update Url, Vendor
- specfile cleanup

* Fri Oct 25 2002 Rex Dieter <rdieter@unl.edu> 1.3-1
- 1.3 (final).

* Wed Oct 23 2002 Rex Dieter <rdieter@unl.edu> 1.3-0.beta.1
- 1.3beta.

* Mon Sep 09 2002 Rex Dieter <rdieter@unl.edu> 1.2-0
- 1.2

* Wed Aug 21 2002 Rex Dieter <rdieter@unl.edu> 1.1-1.1
- workaround automake bug.

* Wed Aug 14 2002 Rex Dieter <rdieter@unl.edu> 1.1-1.0
- rebuild on/for kde 3.0.3

* Fri Aug 09 2002 Rex Dieter <rdieter@unl.edu> 1.1-0.0
- first shot at 1.1

* Mon Jul 08 2002 Rex Dieter <rdieter@unl.edu. 1.0-2
- rebuild for kde 3.0.2

* Sun Jun 16 2002 Rex Dieter <rdieter@unl.edu> 1.0-1
- 1.0
