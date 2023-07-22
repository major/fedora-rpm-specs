%global major   9.0
Name:           midori
Version:        9.0
Release:        13%{?dist}
Summary:        a lightweight, fast and free web browser

License:        LGPLv1.1
URL:            https://github.com/midori-browser/core
Source0:        https://github.com/midori-browser/core/releases/download/v%{major}/midori-v%{major}.tar.gz
Patch0:         https://github.com/midori-browser/core/commit/0115b02f43d23612366d0c5063e6b314d04e3853.patch

BuildRequires:  cmake
BuildRequires:  glib2-devel
BuildRequires:  gtk3-devel
BuildRequires:  gcr3-devel
BuildRequires:  webkit2gtk3-devel
BuildRequires:  vala
BuildRequires:  vala-devel
BuildRequires:  libsoup-devel
BuildRequires:  libpeas-devel
BuildRequires:  sqlite-devel
BuildRequires:  intltool
BuildRequires:  desktop-file-utils
BuildRequires:  json-glib-devel
BuildRequires:  libarchive-devel
# For tests
BuildRequires:  xorg-x11-server-Xvfb

%description
Midori is a lightweight yet powerful web browser which runs just as well
on little embedded computers named for delicious pastries as it does on
beefy machines with a core temperature exceeding that of planet earth.
And it looks good doing that, too. Oh, and of course it's free software.

%prep
%autosetup -n midori-v%{version} -p1

%build
%cmake -DCMAKE_INSTALL_SYSCONFDIR=/etc
%cmake_build

%install
%cmake_install

%find_lang %{name}

desktop-file-install                                    \
        --delete-original                               \
        --dir %{buildroot}%{_datadir}/applications      \
        %{buildroot}%{_datadir}/applications/org.midori_browser.Midori.desktop

# we want to package this as license
rm -f %{buildroot}/%{_datadir}/doc/midori/COPYING

%check
#xvfb-run make check

%files -f %{name}.lang
%license COPYING
%doc README.md
%{_bindir}/midori
%{_libdir}/%{name}/
%{_libdir}/libmidori-core.*
%{_libdir}/girepository-1.0/Midori-0.6.typelib
%{_datadir}/applications/org.midori_browser.Midori.desktop
%{_datadir}/icons/*/*/apps/org.midori_browser.Midori.svg
%{_datadir}/icons/*/*/apps/org.midori_browser.Midori.png
%{_datadir}/gir-1.0/Midori-0.6.gir
%{_datadir}/metainfo/org.midori_browser.Midori.appdata.xml

%changelog
* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 9.0-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 9.0-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Sat Jul 23 2022 Kevin Fenzi <kevin@scrye.com> - 9.0-11
- Fixed FTBFS

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 9.0-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 9.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 9.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Thu Feb 25 2021 Kevin Fenzi <kevin@scrye.com> - 9.0-7
- Add patch to fix / and urlbar issue. rhbz#1933198

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 9.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Aug 03 2020 Kevin Fenzi <kevin@scrye.com> - 9.0-5
- Fix FTBFS with cmake. Fixes rhbz#1864133

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 9.0-4
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 9.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 9.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sat Aug 24 2019 Kevin Fenzi <kevin@scrye.com> - 9.0-1
- Update to 9.0

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 8.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Tue Mar 19 2019 Kevin Fenzi <kevin@scrye.com> - 8.0-1
- Update to 8.0.

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 7.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Dec 06 2018 Kevin Fenzi <kevin@scrye.com> - 7.0-1
- Update to 7.0

* Tue Nov 06 2018 Kevin Fenzi <kevin@scrye.com> - 6.0-1
- Update to 6.0

* Thu Oct 18 2018 Kevin Fenzi <kevin@scrye.com> - 0.6.0-0.1.20181018git
- Update to 20181018

* Sun Sep 23 2018 Kevin Fenzi <kevin@scrye.com> - 0.6.0-0.1.20180923git
- Initial versionn of vala based browser

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.12-0.8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Sun Jun 10 2018 Kevin Fenzi <kevin@scrye.com> - 0.5.12-0.7
- Fix FTBFS. Fixes bug #1582923

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.12-0.6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jan 18 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.5.12-0.5
- Remove obsolete scriptlets

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.12-0.4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.12-0.3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.12-0.2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Tue Dec 27 2016 Kevin Fenzi <kevin@scrye.com> - 0.5.12-0.1
- Switch to webKitTwoOnly branch and webkit2. Fixes bugs #1375821 #1172120
- Add support for system wide crypto with gnutls. Fixes bug #1348218

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.11-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Sun Aug 30 2015 Kevin Fenzi <kevin@scrye.com> 0.5.11-1
- Update to 0.5.11 Fixes bug #1258227

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5.10-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sun Apr 19 2015 Kevin Fenzi <kevin@scrye.com> 0.5.10-1
- Update to 0.5.10

* Sat Feb 21 2015 Till Maas <opensource@till.name> - 0.5.9-3
- Rebuilt for Fedora 23 Change
  https://fedoraproject.org/wiki/Changes/Harden_all_packages_with_position-independent_code

* Fri Jan 16 2015 Kevin Fenzi <kevin@scrye.com> 0.5.9-2
- Add patch to disable sslv3. Fixes bug #1182623

* Tue Nov 11 2014 Kevin Fenzi <kevin@scrye.com> 0.5.9-1
- Update to 0.5.9

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5.8-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5.8-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Thu Apr 03 2014 Kevin Fenzi <kevin@scrye.com> 0.5.8-1
- Update to 0.5.8

* Fri Jan 17 2014 Kevin Fenzi <kevin@scrye.com> 0.5.7-1
- Update to 0.5.7

* Tue Nov 19 2013 Kevin Fenzi <kevin@scrye.com> 0.5.6-1
- Update to 0.5.6

* Wed Nov 06 2013 Kevin Fenzi <kevin@scrye.com> 0.5.5-2
- Add update-desktop-database scriptlet. Fixes bug #1003658

* Fri Aug 16 2013 Kevin Fenzi <kevin@scrye.com> 0.5.5-1
- Update to 0.5.5

* Sat Jul 27 2013 Kevin Fenzi <kevin@scrye.com> 0.5.4-2
- Fix for unversioned doc dirs

* Mon Jul 15 2013 Kevin Fenzi <kevin@scrye.com> 0.5.4-1
- Update to 0.5.4

* Fri May 17 2013 Kevin Fenzi <kevin@scrye.com> 0.5.2-1
- Update to 0.5.2

* Thu May 16 2013 Kevin Fenzi <kevin@scrye.com> 0.5.1-1
- Update to 0.5.1

* Thu Apr 04 2013 Kevin Fenzi <kevin@scrye.com> 0.5.0-1
- Update to 0.5.0

* Thu Mar 07 2013 Kevin Fenzi <kevin@scrye.com> 0.4.9-1
- Update to 0.4.9

* Thu Feb 14 2013 Toshio Kuratomi <toshio@fedoraproject.org> - 0.4.8-3
- Use a conditional on the --vendor removal so the speccan be used on Fedora < 19

* Thu Feb 14 2013 Toshio Kuratomi <toshio@fedoraproject.org> - 0.4.8-2
- Remove the --vendor flag to desktop-file-install

* Tue Feb 05 2013 Kevin Fenzi <kevin@scrye.com> 0.4.8-1
- Update to 0.4.8

* Wed Jan 09 2013 Kevin Fenzi <kevin@scrye.com> 0.4.7-2
- Add patch to fix private browsing crash. Fixes bug #872393

* Wed Sep 19 2012 Kevin Fenzi <kevin@scrye.com> 0.4.7-1
- Update to 0.4.7

* Thu Aug 09 2012 Kevin Fenzi <kevin@scrye.com> - 0.4.6-3
- Fix FTBFS issue with libsoup version detection.

* Fri Jul 27 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Mon May 14 2012 Kevin Fenzi <kevin@scrye.com> - 0.4.6-1
- Update to 0.4.6. Drop upstreamed patch. 

* Tue May 08 2012 Kevin Fenzi <kevin@scrye.com> - 0.4.5-2
- Backport patch to fix https validataion. 
- https://bugs.launchpad.net/midori/+bug/983137

* Sat Apr 14 2012 Kevin Fenzi <kevin@scrye.com> - 0.4.5-1
- Update to 0.4.5
- Drop no longer needed waf doc fix.

* Thu Mar 08 2012 Kevin Fenzi <kevin@scrye.com> - 0.4.4-1
- Update to 0.4.4

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Sun Dec 18 2011 Christoph Wickert <wickert@kolabsys.com> - 0.4.3-1
- Update to 0.4.3

* Thu Nov 10 2011 Kevin Fenzi <kevin@scrye.com> - 0.4.2-1
- Update to 0.4.2-1

* Wed Oct 26 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4.1-3
- Rebuilt for glibc bug#747377

* Mon Oct 24 2011 Kevin Fenzi <kevin@scrye.com> - 0.4.1-2
- Add patch to fix bookmarks. 
- https://bugs.launchpad.net/midori/+bug/874592

* Sun Oct 09 2011 Kevin Fenzi <kevin@scrye.com> - 0.4.1-1
- Update to 0.4.1

* Mon Aug 01 2011 Kevin Fenzi <kevin@scrye.com> - 0.4.0-1
- Update to 0.4.0

* Sun May 15 2011 Kevin Fenzi <kevin@tummy.com> - 0.3.6-1
- Update to 0.3.6

* Sun May 01 2011 Kevin Fenzi <kevin@scrye.com> - 0.3.5-1
- Update to 0.3.5

* Sun Mar 13 2011 Christoph Wickert <cwickert@fedoraproject.org> - 0.3.3-1
- Update to 0.3.3

* Sun Feb 20 2011 Christoph Wickert <cwickert@fedoraproject.org> - 0.3.2-1
- Update to 0.3.2
- No longer require gtksourceview2-devel, libidn-devel and libsexy-devel
- New build requirement: libXScrnSaver-devel

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Sun Jan 30 2011 Kevin Fenzi <kevin@tummy.com> - 0.3.0-1
- Update to 0.3.0

* Sun Jan 09 2011 Kevin Fenzi <kevin@tummy.com> - 0.2.9-4
- Add patch to fix crasher on links. 

* Sat Jan 08 2011 Christoph Wickert <cwickert@fedoraproject.org> - 0.2.9-3
- Add docdir patch again, problem was not fixed properly upstream

* Fri Nov 05 2010 Kevin Fenzi <kevin@tummy.com> - 0.2.9-2
- Add patch for new libnotify

* Sun Oct 31 2010 Kevin Fenzi <kevin@tummy.com> - 0.2.9-1
- Update to 0.2.9

* Wed Sep 29 2010 jkeating - 0.2.8-2
- Rebuilt for gcc bug 634757

* Mon Sep 20 2010 Christoph Wickert <cwickert@fedoraproject.org> - 0.2.8-1
- Update to 0.2.8

* Tue Aug 24 2010 Christoph Wickert <cwickert@fedoraproject.org> - 0.2.7-1
- Update to 0.2.7
- Build separate devel package
- BuildRequire vala
- Include gtk-doc

* Tue Jul 06 2010 Peter Gordon <peter@thecodergeek.com> - 0.2.6-2
- Rebuild for WebKitGTK+ ABI bump.

* Mon May 24 2010 Adam Miller <maxamillion@fedoraproject.org> - 0.2.6-1
- Update to 0.2.6

* Tue May 18 2010 Christoph Wickert <cwickert@fedoraproject.org> - 0.2.5
- Update to 0.2.5

* Sun Mar 21 2010 Christoph Wickert <cwickert@fedoraproject.org> - 0.2.4-1
- Update to 0.2.4
- Fix docs location (#523778)
- Update gtk icon cache scriptlets

* Sat Feb 20 2010 Adam Miller <maxamillion@fedoraproject.org> - 0.2.3-1
- Update to 0.2.3 - spec patch by Kevin Fenzi <kevin@tummy.com>

* Fri Jan 29 2010 Peter Gordon <peter@thecodergeek.com> - 0.2.2-2
- Apply patch to set the Fedora-specific default homepage
  (start.fedoraproject.org), for consistency with other browser packages such
  as Firefox and Epiphany.
  + fedora-homepage.patch
- Resolves: #559740 (Home page is not start.fedoraproject.org)

* Wed Dec 16 2009 Adam Miller <maxamillion@fedoraproject.org> - 0.2.2-1
- Update to new upstream release (0.2.2)

* Wed Dec 02 2009 Adam Miller <maxamillion@fedoraproject.org> - 0.2.1-1
- Update to new upstream release (0.2.1)

* Tue Oct 20 2009 Peter Gordon <peter@thecodergeek.com> - 0.2.0-1
- Update to new upstream release (0.2.0): Drag-scroll on touchscreen devices,
  Speed Dial fixes, faster AdBlock (for all WebKitGTK+ versions), updated DNS
  and IDN handling, new form history extension, various bookmark and history
  fixes.

* Tue Sep 15 2009 Peter Gordon <peter@thecodergeek.com> - 0.1.10-1
- Update to new upstream release (0.1.10): Updated AdBlock for WebKitGTK+
  1.1.14, improved address completion, fixes for tab and feed handling, better
  desktop integration, and Undo/Redo support - among other bugfixes and
  enhancements.

* Wed Aug 05 2009 Peter Gordon <peter@thecodergeek.com> - 0.1.9-1
- Update to new upstream release (0.1.9): lots of fixes and updates for tab
  functionality and the tab panel, as well as menu fixes, and enhancements
  for deleting private data with just a few simple clicks!
- Revert to using the system waf, now that it no longer causes Python errors
  when compiling.

* Sat Jul 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1.7-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Wed Jun 03 2009 Peter Gordon <peter@thecodergeek.com> - 0.1.7-1
- Update to new upstream release (0.1.7): Implements saving activation state
  of extensions, ignore mouse buttons used for horizontal scrolling, panel
  handling improvements, adds "Feed Panel" extension, friendlier error pages,
  and spell checking support; libnotify support for finished transfers,
  introduces basic @-moz-document user style support, and additional tabs/font
  preferences.
  
* Mon Apr 20 2009 Peter Gordon <peter@thecodergeek.com> - 0.1.6-2
- Re-enable libunique support, thanks to it being updated accordingly.

* Sun Apr 19 2009 Peter Gordon <peter@thecodergeek.com> - 0.1.6-1
- Update to new upstream release (0.1.6): Implements "Clear private data,"
  "Default" search engine, support "mailto:" links and news feeds with external
  aggregators, "data:" URIs, and external download manager, and a new Cookie
  Manager extension. Also fixes several memory leaks and performance bugs.

* Sat Apr 11 2009 Peter Gordon <peter@thecodergeek.com> - 0.1.5-2
- Update to new upstream release (0.1.5): download support (with WebKitGTK
  1.1.3+), a new "Colorful Tabs" extension, and saving of extension settings.
- Temporarily switch to building using the in-tarball waf (FTBFS otherwise).
- Temporarily disable libunique (single-instance) support, as it's broken
  with libunique 1.0.4 (which is the current in rawhide).

* Tue Mar 10 2009 Peter Gordon <peter@thecodergeek.com> - 0.1.4-2
- Build against the recently-updated libidn for proper IDN support.

* Mon Mar 09 2009 Peter Gordon <peter@thecodergeek.com>
- Add TODO note about libidn support. (Thanks to Kevin Fenzi via IRC.)

* Sat Mar 07 2009 Peter Gordon <peter@thecodergeek.com> - 0.1.4-1
- Update to new upstream release (0.1.4): mostly small usability fixes and
  related improvements.
- Drop upstreamed no-git patch.
  - no-git.patch

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Sun Feb 22 2009 Peter Gordon <peter@thecodergeek.com> - 0.1.3-1
- Update to new upstream release (0.1.3): support for bookmark folders,
  full image zoom, and "Find as you type" (among other enhancements).
- Add patch to remove git build-time dependency:
  + no-git.patch

* Sat Jan 31 2009 Peter Gordon <peter@thecodergeek.com> - 0.1.2-1
- Update to new upstream release (0.1.2): support for bookmarklets
  ("javascript:foo" URLs and bookmarks), better persistent cookie support,
  preference changes saved dynamically. Lots of startup fixes for speed
  issues, too. :)

* Sat Dec 20 2008 Peter Gordon <peter@thecodergeek.com> - 0.1.1-1
- Update to new upstream release (0.1.1): contains many enhancements and
  bugfixes - including error pages, basic documentation, panel history
  support, icon caching, libsoup integration, support for WebKit's Inspector
  functionality, and the beginnings of support for runtime extensions (in C).

* Tue Sep 09 2008 Peter Gordon <peter@thecodergeek.com> - 0.0.21-1
- Update to new upstream release (0.0.21): contains updated translations,
  fixes for GVFS-->GIO regressions, and various aesthetic enhancements.
  (See the included ChangeLog for full details.)
- Update Source0 URL.

* Sun Sep 07 2008 Peter Gordon <peter@thecodergeek.com> - 0.0.20-2
- Add scriplets for GTK+ icon cache.

* Sun Sep 07 2008 Peter Gordon <peter@thecodergeek.com> - 0.0.20-1
- Update to new upstream release (0.0.20): adds support for single instances,
  some userscripts and Greasemonkey scripting, zooming and printing, as well as
  enhanced news feed detection and session-saving (among other improvements).
- Switch to WAF build system.

* Fri Aug  8 2008 Tom "spot" Callaway <tcallawa@redhat.com> - 0.0.18-2
- fix license tag

* Sat May 24 2008 Peter Gordon <peter@thecodergeek.com> - 0.0.18-1
- Update to new upstream release (0.0.18), adds some translations and
  a lot of bug-fixes.
- Alphabetize dependency list (aesthetic-only change).

* Sat Apr 12 2008 Peter Gordon <peter@thecodergeek.com> - 0.0.17-3
- Rebuild for updated WebKit library so-name and include directory.

* Mon Mar 03 2008 Peter Gordon <peter@thecodergeek.com> - 0.0.17-2
- Cleanups from review (bug 435661):
  (1) Fix consistency of tabs/spaces usage.
  (2) Fix source permissions.
  (3) Add desktop-file-utils build dependency.

* Sun Mar 02 2008 Peter Gordon <peter@thecodergeek.com> - 0.0.17-1
- Initial packaging for Fedora.
