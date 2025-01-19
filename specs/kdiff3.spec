%undefine __cmake_in_source_build
# %%global gitcommit_full ad0d6a26ef59652247322971753bf142231a703a
# %%global gitcommit %%(c=%%{gitcommit_full}; echo ${c:0:7})

Name:           kdiff3
Version:        1.12.0
Release:        2%{?dist}
Summary:        Compare + merge 2 or 3 files or directories

License:        GPL-2.0-or-later
URL:            https://invent.kde.org/sdk/kdiff3
Source0:        https://invent.kde.org/sdk/kdiff3/-/archive/%{version}/%{name}-%{version}.tar.bz2

BuildRequires:  cmake3
BuildRequires:  gcc-c++
BuildRequires:  desktop-file-utils
BuildRequires:  gettext
BuildRequires:  libappstream-glib
BuildRequires:  extra-cmake-modules
BuildRequires:  cmake(Qt6)
BuildRequires:  cmake(KF6KIO)
BuildRequires:  cmake(KF6WidgetsAddons)
BuildRequires:  cmake(KF6Parts)
BuildRequires:  cmake(KF6IconThemes)
BuildRequires:  cmake(KF6DocTools)
BuildRequires:  cmake(KF6Crash)
BuildRequires:  cmake(KF6CoreAddons)
BuildRequires:  cmake(KF6I18n)
BuildRequires:  cmake(KF6Bookmarks)
BuildRequires:  qt6-qt5compat-devel
BuildRequires:  kf6-rpm-macros
BuildRequires:  extra-cmake-modules
BuildRequires:  boost-devel
BuildRequires:  ninja-build

Provides: mergetool

%description
KDiff3 is a program that
- compares and merges two or three input files or directories,
- shows the differences line by line and character by character (!),
- provides an automatic merge-facility and
- an integrated editor for comfortable solving of merge-conflicts
- has support for KDE-KIO (ftp, sftp, http, fish, smb)
- and has an intuitive graphical user interface.


%prep
%autosetup -p1
#-n KDE-%{name}-%{gitcommit}


%build
%cmake_kf6 -DBUILD_WITH_QT6:BOOL=ON
%cmake_build

%install
%cmake_install

%find_lang %{name} --with-html --with-man --all-name
chmod -x %{buildroot}%{_datadir}/applications/org.kde.%{name}.desktop


%check
appstream-util validate-relax --nonet %{buildroot}%{_datadir}/metainfo/org.kde.%{name}.appdata.xml
desktop-file-validate %{buildroot}%{_datadir}/applications/org.kde.%{name}.desktop

%files -f %{name}.lang
%license COPYING
%doc README
%{_bindir}/%{name}
%{_kf6_plugindir}/kfileitemaction/kdiff3fileitemaction.so
# %{_kf6_plugindir}/parts/kdiff3part.so
%{_datadir}/metainfo/org.kde.%{name}.appdata.xml
%{_datadir}/applications/org.kde.%{name}.desktop
%{_datadir}/icons/hicolor/*/apps/*.png
%{_datadir}/icons/hicolor/scalable/apps/%{name}.svgz
# %{_datadir}/kservices6/kdiff3part.desktop
# %%{_datadir}/kservices5/kdiff3part.desktop
# %{_datadir}/kxmlgui6/%{name}
# %{_datadir}/kxmlgui6/kdiff3part
%{_mandir}/man1/%{name}.1*


%changelog
* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.12.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Mon Dec 09 2024 Vasiliy N. Glazov <vascom2@gmail.com> - 1.12.0-1
- Update to 1.12.0

* Wed Nov 06 2024 Vasiliy N. Glazov <vascom2@gmail.com> - 1.11.5-1
- Update to 1.11.5

* Wed Oct 09 2024 Vasiliy N. Glazov <vascom2@gmail.com> - 1.11.4-1
- Update to 1.11.4

* Tue Aug 27 2024 Yaakov Selkowitz <yselkowi@redhat.com> - 1.11.2-1
- Update to 1.11.2

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.11.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Tue Jun 18 2024 Vasiliy N. Glazov <vascom2@gmail.com> - 1.11.1-1
- Update to 1.11.1

* Wed Jan 24 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.10.7-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.10.7-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Mon Dec 11 2023 Vasiliy N. Glazov <vascom2@gmail.com> - 1.10.7-1
- Update to 1.10.7

* Mon Sep 25 2023 Vasiliy N. Glazov <vascom2@gmail.com> - 1.10.6-1
- Update to 1.10.6

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.10.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Wed Jul 12 2023 Vasiliy N. Glazov <vascom2@gmail.com> - 1.10.5-1
- Update to 1.10.5

* Tue May 23 2023 Vasiliy N. Glazov <vascom2@gmail.com> - 1.10.4-1
- Update to 1.10.4

* Wed May 17 2023 Vasiliy N. Glazov <vascom2@gmail.com> - 1.10.3-1
- Update to 1.10.3

* Sat Apr 01 2023 Vasiliy N. Glazov <vascom2@gmail.com> - 1.10.1-1
- Update to 1.10.1

* Thu Feb 02 2023 Justin Zobel <justin@1707.io> - 1.10.0-1
- Update to 1.10.0

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.9.6-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.9.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Tue Jun 28 2022 Vasiliy N. Glazov <vascom2@gmail.com> - 1.9.6-1
- Update to 1.9.6

* Thu Mar 03 2022 Vasiliy N. Glazov <vascom2@gmail.com> - 1.9.5-1
- Update to 1.9.5

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.9.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Dec 08 2021 Vasiliy N. Glazov <vascom2@gmail.com> - 1.9.4-1
- Update to 1.9.4

* Fri Sep 24 2021 Vasiliy N. Glazov <vascom2@gmail.com> - 1.9.3-1
- Update to 1.9.3

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.9.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed May 19 2021 Vasiliy N. Glazov <vascom2@gmail.com> - 1.9.2-1
- Update to 1.9.2

* Mon Feb 22 2021 Vasiliy N. Glazov <vascom2@gmail.com> - 1.8.5-1
- Update to 1.8.5

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Sat Sep 05 2020 Marie Loise Nolden <loise@kde.org> - 1.8.4-1
- Update to 1.8.4

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Jun 26 2020 Marie Loise Nolden <loise@kde.org> - 1.8.3-1
- Update to 1.8.3

* Thu Jun 18 2020 Vasiliy N. Glazov <vascom2@gmail.com> - 1.8.2-1
- Update to 1.8.2

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Tue Jan 14 2020 Vasiliy N. Glazov <vascom2@gmail.com> - 1.8.1-4
- Really ix crash

* Fri Jan 10 2020 Vasiliy N. Glazov <vascom2@gmail.com> - 1.8.1-3
- Fix crash end error

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat May 18 2019 Vasiliy N. Glazov <vascom2@gmail.com> - 1.8.1-1
- Update to 1.8.1

* Wed May 15 2019 Vasiliy N. Glazov <vascom2@gmail.com> - 1.8.0-1
- Update to 1.8.0

* Fri Mar 29 2019 Vasiliy N. Glazov <vascom2@gmail.com> 1.7.90-4
- Update to latest git

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.90-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Wed Jan 16 2019 Vasiliy N. Glazov <vascom2@gmail.com> 1.7.90-2
- Update to latest git
- Solve #1664996

* Mon Oct 15 2018 Vasiliy N. Glazov <vascom2@gmail.com> 1.7.90-1
- Switch to Qt5/KF5

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.98-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.98-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.98-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.98-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Mon Feb 20 2017 Rex Dieter <rdieter@fedoraproject.org> - 0.9.98-9
- fix FTBFS (#1423810), .spec cleanup

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.98-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Feb 03 2016 Rex Dieter <rdieter@fedoraproject.org> - 0.9.98-7
- use %%qmake_qt4 macro to ensure proper build flags

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.98-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat May 02 2015 Kalev Lember <kalevlember@gmail.com> - 0.9.98-5
- Rebuilt for GCC 5 C++11 ABI change

* Tue Sep 16 2014 Rex Dieter <rdieter@fedoraproject.org> 0.9.98-4
- -qt subpkg, Qt-only build (#746663)

* Tue Sep 16 2014 Rex Dieter <rdieter@fedoraproject.org> - 0.9.98-3
- Provides: mergetool (#990447)
- .spec cleanup
- install manpage

* Sat Aug 16 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.98-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Tue Jul  8 2014 nbecker <ndbecker2@gmail.com> - 0.9.98-1
- Update to 0.9.98

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.97-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.97-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.97-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Mon Jan 21 2013 Neal Becker <ndbecker2@gmail.com> - 0.9.97-5
- bump version to match f17 version

* Wed Nov 21 2012 Johan Cwiklinski <johan AT x-tnd DOT be> - 0.9.97-4.trashy
- Fix for saving files on KDE with relative path specified
  via command line option -o.

* Mon Aug 13 2012 Neal Becker <ndbecker2@gmail.com> - 0.9.97-3
- Remove libkdiff3*.so

* Mon Aug 13 2012 Neal Becker <ndbecker2@gmail.com> - 0.9.97-1
- Update to 0.9.97

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.96-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Feb 24 2012 Neal Becker <ndbecker2@gmail.com> - 0.9.96-6
- Add req: oxygen-icon-theme to close BR 771356

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.96-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Sat Sep  3 2011 Neal Becker <ndbecker2@gmail.com> - 0.9.96-5
- added kdiff3fileitemactionplugin

* Sat Sep  3 2011 Neal Becker <ndbecker2@gmail.com> - 0.9.96-4
- Remove patch2

* Sat Sep  3 2011 Neal Becker <ndbecker2@gmail.com> - 0.9.96-3
- Remove patch1

* Sat Sep  3 2011 Neal Becker <ndbecker2@gmail.com> - 0.9.96-2
- fix patch

* Sat Sep  3 2011 Neal Becker <ndbecker2@gmail.com> - 0.9.96-1
- Update to 0.9.96

* Mon Feb 07 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.95-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Tue Jul 13 2010 Rex Dieter <rdieter@fedoraproject.org> - 0.9.95-5
- ftbfs against kde-4.5 (pre)releases
- optimize scriplets
- drop HTML doc hackery, use %%find_lang --with-kde

* Sun Mar 28 2010 Neal Becker <ndbecker2@gmail.com> - 0.9.95-4
- Install kdiff3_part.rc into correct location

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.95-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Wed Mar  4 2009 Neal Becker <ndbecker2@gmail.com> - 0.9.95-2
- Fix Changelog order

* Wed Mar  4 2009 Neal Becker <ndbecker2@gmail.com> - 0.9.95-1
- Update to 0.9.95

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.94-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Sat Jan 17 2009 Neal Becker <ndbecker2@gmail.com> - 0.9.94-1
- Update to 0.9.94

* Fri Jan  9 2009 Neal Becker <ndbecker2@gmail.com> - 0.9.93-1.3%{?dist}
- Update to 0.9.93-3

* Tue Jan  6 2009 Neal Becker <ndbecker2@gmail.com> - 0.9.93-2-1
- Update to 0.9.93-2

* Tue Jan  6 2009 Rex Dieter <rdieter@fedoraproject.org> - 0.9.93-6
- use kde4 macros
- add scriptlets for locolor icons
- update d-f-i usage
- include khelpcenter handbook
- update Source0 URL

* Tue Jan  6 2009 Neal Becker <ndbecker2@gmail.com> - 0.9.93-5
- Fix HTML_DIR and use kde4_ versions of datadir, libdir, bindir

* Tue Jan  6 2009 Neal Becker <ndbecker2@gmail.com> - 0.9.93-4
- Remove /etc/profile.d/qt.sh, remove configure

* Tue Jan  6 2009 Neal Becker <ndbecker2@gmail.com> - 0.9.93-3
- Change BR, no longer kde3

* Tue Jan  6 2009 Neal Becker <ndbecker2@gmail.com> - 0.9.93-2
- Add br cmake

* Tue Jan  6 2009 Neal Becker <ndbecker2@gmail.com> - 0.9.93-1
- Update to 0.9.93

* Thu Jun 5 2008 Manuel Wolfshant <wolfy@fedoraproject.org> - 0.9.92-14
- add a conditional BR, allowing build in EPEL-5

* Tue Mar 25 2008 Rex Dieter <rdieter@fedoraproject.org> - 0.9.92-13
- drop BR: qt-devel (broken)
- omit 64bit configure hack (invalid and not needed)

* Tue Feb 19 2008 Fedora Release Engineering <rel-eng@fedoraproject.org> - 0.9.92-12
- Autorebuild for GCC 4.3

* Sun Dec  2 2007 Neal Becker <ndbecker2@gmail.com> - 0.9.92-11
- BR qt-devel
- source /etc/profile.d/qt.sh for mock

* Wed Nov  7 2007 Neal Becker <ndbecker2@gmail.com> - 0.9.92-10
- Update desktop-file-install as suggest by Rex

* Wed Nov  7 2007 Neal Becker <ndbecker2@gmail.com> - 0.9.92-8
- Use desktop-file-install for kdiff3plugin.desktop

* Tue Nov  6 2007 Neal Becker <ndbecker2@gmail.com> - 0.9.92-7
- Update to 0.9.92
- Add /usr/share/applnk/.hidden/kdiff3plugin.desktop

* Thu Oct 05 2006 Christian Iseli <Christian.Iseli@licr.org> 0.9.90-7
 - rebuilt for unwind info generation, broken in gcc-4.1.1-21

* Sun Aug 27 2006 Neal Becker <ndbecker2@gmail.com> - 0.9.90-6
- Untabify
- --add-category X-Fedora
- Add gtk-update-icon-cache

* Fri May 12 2006 Neal Becker <ndbecker2@gmail.com> - 0.9.88-5
- Remove ldconfig
* Fri May 12 2006 Laurent Rineau <laurent.rineau__fc_extra@normalesup.org> - 0.9.88-5
- Quote percent sign in %%changelog.
- Cleanup in %%files
- Removed Requires: tag.


* Fri May 12 2006 Neal Becker <ndbecker2@gmail.com> - 0.9.88-4
- Remove applnk stuff
- Add %%post + %%postun

* Fri May 12 2006 Neal Becker <ndbecker2@gmail.com> - 0.9.88-3
- Fix symlinks (from Rex Dieter)

* Fri May 12 2006 Neal Becker <ndbecker2@gmail.com> - 0.9.88-2
- Fix source0
- Fix E: kdiff3 standard-dir-owned-by-package /usr/share/icons
  E: kdiff3 standard-dir-owned-by-package /usr/share/man
  E: kdiff3 standard-dir-owned-by-package /usr/share/man/man1
- Fix Summary

* Thu May 11 2006 Neal Becker <ndbecker2@gmail.com> - 0.9.88-1
- Initial

