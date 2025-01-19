Name:           gpodder
Version:        3.11.5
Release:        2%{?dist}
Summary:        Podcast receiver/catcher written in Python
# Mostly GPL-3.0-or-later, but some files use something different
License:        GPL-2.0-or-later AND GPL-3.0-or-later AND LGPL-2.1-or-later AND LGPL-3.0-or-later AND ISC
URL:            http://gpodder.org
Source0:        https://github.com/gpodder/gpodder/archive/%{version}/gpodder-%{version}.tar.gz
# Rename the appdata file to comply with Fedora Packaging Guidelines
Patch:          rename-appdata.patch
Patch:          disable-auto-update-check.patch
Patch:          disable-coverage-report.patch
BuildArch:      noarch
BuildRequires:  python3-devel, python3-feedparser, python3-build, python3-installer
BuildRequires:  desktop-file-utils
BuildRequires:  gettext
BuildRequires:  intltool
BuildRequires:  help2man
BuildRequires:  make
BuildRequires:  libappstream-glib
# Test tools
BuildRequires:  pytest
BuildRequires:  python3-minimock
BuildRequires:  python3-pytest-httpserver
# Runtime dependencies needed in tests
BuildRequires:  python3-podcastparser
BuildRequires:  python3-mygpoclient
BuildRequires:  python3-requests
#Requires:       python-gpod, python-eyed3 #re-enable once Python 3 support exists.
Requires:       python3-gobject
Requires:       python3-dbus
Requires:       python3-podcastparser
Requires:       python3-imaging
Requires:       python3-mygpoclient
Requires:       python3-requests
# Can be removed once Python 3.12 support is available in a release:
# https://github.com/gpodder/gpodder/pull/1571
Requires:       python3-zombie-imp
Requires:       hicolor-icon-theme
Requires:       yt-dlp
Requires:       /usr/bin/xdg-open
Recommends:     python3-html5lib
%description
gPodder is a Podcast receiver/catcher written in Python, using GTK. 
It manages podcast feeds for you and automatically downloads all 
podcasts from as many feeds as you like.
It also optionally supports syncing with ipods.

%prep
%autosetup -p1 -n %{name}-%{version}

# Drop unused tools that complicate licensing
rm -rf tools/max-osx
rm -rf tools/win_installer

#drop examples for now
rm -rf share/gpodder/examples

%generate_buildrequires
%pyproject_buildrequires

%build
make messages

%check
make unittest
appstream-util validate-relax --nonet %{buildroot}%{_metainfodir}/*.appdata.xml

%install
make install DESTDIR=$RPM_BUILD_ROOT PREFIX=%{_prefix}

desktop-file-install --delete-original          \
  --dir $RPM_BUILD_ROOT%{_datadir}/applications                 \
  --remove-key Miniicon --add-category Application              \
  --remove-category FileTransfer --remove-category News         \
  --remove-category Network                                     \
  $RPM_BUILD_ROOT%{_datadir}/applications/%{name}.desktop

%find_lang %{name}

%files -f %{name}.lang
%doc COPYING README.md
%{_bindir}/%{name}
%{_bindir}/gpo
%{_bindir}/%{name}-migrate2tres
%{_datadir}/%{name}/
%{_datadir}/icons/hicolor/*/apps/*
%{_mandir}/man1/*
%{_metainfodir}/*.appdata.xml
%{_datadir}/applications/*.desktop
%{_datadir}/dbus-1/services/org.gpodder.service
%{python3_sitelib}/%{name}/
%{python3_sitelib}/%{name}*.dist-info

%changelog
* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 3.11.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Wed Dec 18 2024 Gwyn Ciesla <gwync@protonmail.com> - 3.11.5-1
- 3.11.5

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 3.11.4-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Wed Jun 12 2024 Gwyn Ciesla <gwync@protonmail.com> - 3.11.4-5
- Python 3.13 rebuild

* Wed Jan 24 2024 Fedora Release Engineering <releng@fedoraproject.org> - 3.11.4-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sat Jan 20 2024 Fedora Release Engineering <releng@fedoraproject.org> - 3.11.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Nov 22 2023 Otto Liljalaakso <otto.liljalaakso@iki.fi> - 3.11.4-2
- Add missing dependencies (rhbz#2248679)

* Fri Oct 13 2023 Gwyn Ciesla <gwync@protonmail.com> - 3.11.4-1
- 3.11.4

* Mon Oct 02 2023 Gwyn Ciesla <gwync@protonmail.com> - 3.11.3-1
- 3.11.3

* Tue Aug 15 2023 Gwyn Ciesla <gwync@protonmail.com> - 3.11.2-1
- 3.11.2

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 3.11.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Wed Jun 14 2023 Python Maint <python-maint@redhat.com> - 3.11.1-2
- Rebuilt for Python 3.12

* Mon Feb 20 2023 Otto Liljalaakso <otto.liljalaakso@iki.fi> - 3.11.1-1
- Update to 3.11.1 (rhbz#2171198)
- Review licensing, use SPDX license identifiers

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 3.11.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Wed Dec 21 2022 Gwyn Ciesla <gwync@protonmail.com> - 3.11.0-2
- BR setuptools.

* Mon Aug 01 2022 Gwyn Ciesla <gwync@protonmail.com> - 3.11.0-1
- 3.11.0

* Thu Jul 28 2022 Gwyn Ciesla <gwync@protonmail.com> - 3.10.21-8
- Move from youtube-dl to yt-dlp.

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 3.10.21-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon Jun 13 2022 Python Maint <python-maint@redhat.com> - 3.10.21-6
- Rebuilt for Python 3.11

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 3.10.21-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Tue Aug 17 2021 Gwyn Ciesla <gwync@protonmail.com> - 3.10.21-4
- Additional patch.

* Mon Aug 16 2021 Gwyn Ciesla <gwync@protonmail.com> - 3.10.21-3
- Disable startup update checks, BZ 1984726.

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 3.10.21-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Jul 21 2021 Gwyn Ciesla <gwync@protonmail.com> - 3.10.21-1
- 3.10.21

* Tue Jun 08 2021 Gwyn Ciesla <gwync@protonmail.com> - 3.10.20-1
- 3.10.20

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 3.10.19-2
- Rebuilt for Python 3.10

* Thu Apr 15 2021 Gwyn Ciesla <gwync@protonmail.com> - 3.10.19-1
- 3.10.19

* Mon Apr 12 2021 Gwyn Ciesla <gwync@protonmail.com> - 3.10.18-1
- 3.10.18

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 3.10.17-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Jan 18 2021 Otto Urpelainen <oturpe@iki.fi> - 3.10.17-2
- Make appdata.xml comply with Fedora Packaging Guidelines

* Mon Nov 23 2020 Gwyn Ciesla <gwync@protonmail.com> - 3.10.17-1
- 3.10.17

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.10.16-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Jun 22 2020 Gwyn Ciesla <gwync@protonmail.com> - 3.10.16-1
- 3.10.16

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 3.10.15-2
- Rebuilt for Python 3.9

* Wed Apr 15 2020 Gwyn Ciesla <gwync@protonmail.com> - 3.10.15-1
- 3.10.15

* Tue Apr 14 2020 Gwyn Ciesla <gwync@protonmail.com> - 3.10.14-1
- 3.10.14

* Wed Jan 29 2020 Gwyn Ciesla <gwync@protonmail.com> - 3.10.13-1
- 3.10.13

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.10.12-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Mon Jan 27 2020 Gwyn Ciesla <gwync@protonmail.com> - 3.10.12-1
- 3.10.12

* Mon Sep 30 2019 Gwyn Ciesla <gwync@protonmail.com> - 3.10.11-1
- 3.10.11

* Fri Sep 27 2019 Gwyn Ciesla <gwync@protonmail.com> - 3.10.10-1
- 3.10.10

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 3.10.9-3
- Rebuilt for Python 3.8

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.10.9-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Tue Jun 11 2019 Gwyn Ciesla <gwync@protonmail.com> - 3.10.9-1
- 3.10.9

* Wed Jun 05 2019 Gwyn Ciesla <gwync@protonmail.com> - 3.10.8-1
- 3.10.8

* Sat Feb 02 2019 Gwyn Ciesla <limburgher@gmail.com> - 3.10.7-1
- 3.10.7

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.10.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Wed Jan 02 2019 Gwyn Ciesla <limburgher@gmail.com> - 3.10.6-1
- 3.10.6.

* Mon Sep 17 2018 Gwyn Ciesla <limburgher@gmail.com> - 3.10.5-1
- 3.10.5.

* Tue Sep 11 2018 Gwyn Ciesla <limburgher@gmail.com> - 3.10.4-1
- 3.10.4

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.10.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Mon Jun 25 2018 Todd Zullinger <tmz@pobox.com> - 3.10.2-3
- Avoid python 3.7 "async" keyword

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 3.10.2-2
- Rebuilt for Python 3.7

* Mon Jun 11 2018 Gwyn Ciesla <limburgher@gmail.com> - 3.10.2-1
- 3.10.2

* Mon May 07 2018 Gwyn Ciesla <limburgher@gmail.com> - 3.10.1-2
- Bump EVR for f28 release issue.

* Tue Feb 20 2018 Gwyn Ciesla <limburgher@gmail.com> - 3.10.1-1
- 3.10.1

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.10.0-3.1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Fri Jan 12 2018 Gwyn Ciesla <limburgher@gmail.com> - 3.10.0-2.1
- Patch for opml error.

* Thu Jan 11 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 3.10.0-2
- Remove obsolete scriptlets

* Tue Jan 02 2018 Gwyn Ciesla <limburgher@gmail.com> - 3.10.0-1
- 3.10.0, move to Python 3.

* Mon Dec 18 2017 Gwyn Ciesla <limburgher@gmail.com> - 3.9.5-1
- 3.9.5 prerelease.

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.9.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.9.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri Dec 23 2016 Jon Ciesla <limburgher@gmail.com> - 3.9.3-1
- 3.9.3

* Wed Nov 30 2016 Jon Ciesla <limburgher@gmail.com> - 3.9.2-1
- 3.9.2
- Requires python2-podcastparser

* Thu Sep 01 2016 Jon Ciesla <limburgher@gmail.com> - 3.9.1-1
- 3.9.1

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.9.0-4
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Thu Jul 07 2016 Jon Ciesla <limburgher@gmail.com> - 3.9.0-3
- Fix directory ownership.

* Tue Jun 14 2016 Jon Ciesla <limburgher@gmail.com> - 3.9.0-2
- Drop pywebkitgtk.

* Thu Feb 04 2016 Jon Ciesla <limburgher@gmail.com> - 3.9.0-1
- 3.9.0, BZ 1304554.

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 3.8.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Dec 02 2015 Jon Ciesla <limburgher@gmail.com> - 3.8.5-1
- 3.8.5.

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.8.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Mon May 25 2015 Jon Ciesla <limburgher@gmail.com> - 3.8.4-1
- 3.8.4.

* Thu Mar 26 2015 Richard Hughes <rhughes@redhat.com> - 3.8.3-2
- Add an AppData file for the software center

* Fri Nov 21 2014 Jon Ciesla <limburgher@gmail.com> - 3.8.3-1
- 3.8.3.

* Wed Oct 29 2014 Jon Ciesla <limburgher@gmail.com> - 3.8.2-1
- 3.8.2.

* Wed Jul 30 2014 Jon Ciesla <limburgher@gmail.com> - 3.8.0-1
- 3.8.0.

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.7.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Mon Jun 02 2014 Jon Ciesla <limburgher@gmail.com> - 3.7.0-1
- 3.7.0.

* Mon Mar 17 2014 Jon Ciesla <limburgher@gmail.com> - 3.6.1-1
- 3.6.1.

* Mon Mar 03 2014 Jon Ciesla <limburgher@gmail.com> - 3.6.0-1
- 3.6.0.

* Wed Jan 29 2014 Jon Ciesla <limburgher@gmail.com> - 3.5.2-1
- 3.5.2.
- Date fixups.
- License tag fixup.

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.20.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Tue Feb 12 2013 Jon Ciesla <limburgher@gmail.com> - 2.20.3-1
- 2.20.3.
- Drop desktop vendor tag.
- Youtube patch upstreamed.

* Mon Feb  4 2013 Toshio Kuratomi <toshio@fedoraproject.org> - 2.20.2-2
- Patch for compatibility with pyhton-pillow as well as python-imaging

* Tue Oct 09 2012 Ville-Pekka Vainio <vpvainio AT iki.fi> - 2.20.2-1
- New upstream release
- Add patch from git master to fix Youtube feeds

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.20.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sun Feb 26 2012 Ville-Pekka Vainio <vpvainio AT iki.fi> - 2.20.1-1
- New upstream release
- Update project and source URLs

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.20-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Thu Nov 10 2011 Ville-Pekka Vainio <vpvainio AT iki.fi> - 2.20-1
- New upstream release
- Remove the INSTALL file from the docs

* Fri Sep 16 2011 Ville-Pekka Vainio <vpvainio AT iki.fi> - 2.19-1
- New upstream release

* Sun Aug 14 2011 Ville-Pekka Vainio <vpvainio AT iki.fi> - 2.18-1
- New upstream release

* Sat Aug 06 2011 Ville-Pekka Vainio <vpvainio AT iki.fi> - 2.17-1
- New upstream release

* Sat Jul 23 2011 Matěj Cepl <mcepl@redhat.com> - 2.16-1
- New upstream release

* Wed May 18 2011 Ville-Pekka Vainio <vpivaini AT cs.helsinki.fi> - 2.15-1
- New upstream release
- Remove dependency on gstreamer-python. Upstream removed gstreamer track
  length detection because it was too crashy.

* Sat Apr 23 2011 Ville-Pekka Vainio <vpivaini AT cs.helsinki.fi> - 2.14-1
- New upstream release, remove upstreamed patches

* Wed Mar 02 2011 Ville-Pekka Vainio <vpivaini AT cs.helsinki.fi> - 2.13-2
- Add patch to fix problems if there is no active podcast (rhbz #681383,
  gPodder #1291)
- Add patch to fix invalid UTF-8 text in podcast descriptions (gPodder #1277)

* Wed Feb 23 2011 Ville-Pekka Vainio <vpivaini AT cs.helsinki.fi> - 2.13-1
- New upstream release, remove upstreamed patches

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.12-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Thu Feb 03 2011 Ville-Pekka Vainio <vpivaini AT cs.helsinki.fi> - 2.12-2
- Add patch to fix encoding issues in minidb (rhbz #674758, gPodder #1088)

* Sat Jan 15 2011 Ville-Pekka Vainio <vpivaini AT cs.helsinki.fi> - 2.12-1
- New upstream release
- Add patch to fix exception handling in the 'gpo' command line utility
  (rhbz #668284, gPodder #1264)
- Add patch to fix youtube search (Maemo #11756)
- Require python-pymtp for MTP support

* Mon Dec 20 2010 Ville-Pekka Vainio <vpivaini AT cs.helsinki.fi> - 2.11-1
- New upstream release

* Sat Dec 18 2010 Ville-Pekka Vainio <vpivaini AT cs.helsinki.fi> - 2.10-1
- New upstream release

* Tue Oct 12 2010 Ville-Pekka Vainio <vpivaini AT cs.helsinki.fi> - 2.9-1
- New upstream release
- Remove unneeded patch
- Add patch to use systemwide pymtp and remove bundled pymtp

* Sun Oct 03 2010 Ville-Pekka Vainio <vpivaini AT cs.helsinki.fi> - 2.8-2
- Add a patch to fix the 'gpo update' command, rhbz #638107, Maemo #11217

* Sun Aug 29 2010 Ville-Pekka Vainio <vpivaini AT cs.helsinki.fi> - 2.8-1
- New upstream release
- Remove both patches, upstreamed
- Add dependency on gstreamer-python for ipod sync

* Mon Aug 23 2010 Ville-Pekka Vainio <vpivaini AT cs.helsinki.fi> - 2.7-3
- Add patches to fix two Fedora bugs, #620584 (problems with the episode list)
  and #619295 (database ProgrammingError)

* Wed Jul 21 2010 David Malcolm <dmalcolm@redhat.com> - 2.7-2
- Rebuilt for https://fedoraproject.org/wiki/Features/Python_2.7/MassRebuild

* Wed Jul 07 2010 Ville-Pekka Vainio <vpivaini AT cs.helsinki.fi> - 2.7-1
- New upstream release
- Drop all patches, upstreamed
- Upstream added the Network category to the .desktop file, remove it so that
  gPodder doesn't show up in both the Network and the Audio menu

* Fri Jun 04 2010 Ville-Pekka Vainio <vpivaini AT cs.helsinki.fi> - 2.6-7
- Add a patch to fix another TypeError, upstream bug #1041, rhbz #599232

* Sun May 30 2010 Ville-Pekka Vainio <vpivaini AT cs.helsinki.fi> - 2.6-6
- Require python-mygpoclient >= 1.4, rhbz #597740

* Fri May 28 2010 Jef Spaleta <jspaleta AT fedoraproject DOT org> - 2.6-5
- Replace All Episodes patch with better patch from upstream.  

* Fri May 28 2010 Ville-Pekka Vainio <vpivaini AT cs.helsinki.fi> - 2.6-4
- Upstream patch for TypeError in gui.py, upstream bug #934, rhbz #595980

* Sun May 23 2010 Jef Spaleta <jspaleta AT fedoraproject DOT org> - 2.6-3
- better patch 

* Sun May 23 2010 Jef Spaleta <jspaleta AT fedoraproject DOT org> - 2.6-2
- small patch to prevent crashes when selecting All episodes for subscription edit 

* Sun May 23 2010 Ville-Pekka Vainio <vpivaini AT cs.helsinki.fi> - 2.6-1
- New upstream release, mostly bug fixes

* Sun May 02 2010 Ville-Pekka Vainio <vpivaini AT cs.helsinki.fi> - 2.5-1
- Update to the latest upstream release
- Require pywebkitgtk instead of gnome-python2-gtkhtml2
- Remove both patches, they are upstreamed
- Remove desktop file categories News and FileTransfer,
  desktop-file-install would require the Network category to be used with
  them, but that would put gPodder into both the Network and the Audio menus

* Mon Mar 15 2010 Ville-Pekka Vainio <vpivaini AT cs.helsinki.fi> - 2.3-3
- Add a patch from upstream git to not raise an exception if PyMTP is
  missing, helps avoid ABRT reports which are not bugs, such as
  rhbz#570811. Upstream bug #924.

* Mon Mar 01 2010 Ville-Pekka Vainio <vpivaini AT cs.helsinki.fi> - 2.3-2
- Add a patch from upstream git to fix rhbz#569111, upstream bug #911
  (GError in desktopfile.py)

* Sat Feb 27 2010 Ville-Pekka Vainio <vpivaini AT cs.helsinki.fi> - 2.3-1
- New upstream release
- Remove both patches, they're in the release

* Thu Feb 25 2010 Ville-Pekka Vainio <vpivaini AT cs.helsinki.fi> - 2.2-3
- Add patch from upstream git to mention gnome-bluetooth instead of bluez in
  gPodder's own dependency manager
- Drop RPM dependency on gnome-bluetooth so that gPodder can be installed
  without having PulseAudio in the system, upstream bug #884

* Wed Feb 24 2010 Ville-Pekka Vainio <vpivaini AT cs.helsinki.fi> - 2.2-2
- Add patch from upstream git to fix rhbz#566566, upstream bug #874
  (crash in episode lock counting)

* Wed Feb 10 2010 Ville-Pekka Vainio <vpivaini AT cs.helsinki.fi> - 2.2-1
- New upstream release
- Add Requires python-mygpoclient and dbus-python
- Add Requires gnome-python2-gtkhtml2 for nicer shownotes
- Remove BuildRequires ImageMagick
- Remove Requires wget and pybluez, not needed anymore

* Mon Dec 14 2009 Jef Spaleta <jspaleta AT fedoraproject DOT org> - 2.1-1
- New upstream release

* Mon Aug 17 2009 Jef Spaleta <jspaleta AT fedoraproject DOT org> - 2.0-1
- New upstream release

* Mon Aug 17 2009 Jef Spaleta <jspaleta AT fedoraproject DOT org> - 0.17.0-3
- Fix for desktop file encoding packaging problem

* Mon Jul 27 2009 Jef Spaleta <jspaleta AT fedoraproject DOT org> - 0.17.0-2
- New upstream release, fixes multiple bugs since 0.16.1.

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.16.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Thu Jul 2 2009 - 0.16.1-2 jpaleta <jspaleta AT fedoraproject DOT org>
- feedparser buildrequires fix

* Sun Jun 14 2009 - 0.16.1-1 jpaleta <jspaleta AT fedoraproject DOT org>
- new upstream point release new features and bug fixes. See upstream website for details.

* Mon Apr 13 2009 - 0.15.2-1 jpaleta <jspaleta AT fedoraproject DOT org>
- new upstream point release with multiple bug fixes and updates translations.

* Fri Mar 20 2009 - 0.15.1-1 jpaleta <jspaleta AT fedoraproject DOT org>
- new upstream release and packaging fixes

* Thu Feb 05 2009 Jef Spaleta <jspaleta AT fedoraproject DOT org> - 0.14.1-1
- new upstream release

* Sat Jan 03 2009 Jef Spaleta <jspaleta AT fedoraproject DOT org> - 0.14.0-2
- pybluez dep fix

* Thu Dec 11 2008 Jef Spaleta <jspaleta AT fedoraproject DOT org> - 0.14.0-1
- New upstream release

* Mon Dec 01 2008 Jef Spaleta <jspaleta AT fedoraproject DOT org> - 0.13.1-2.1
- Source Fix

* Sat Nov 29 2008 Ignacio Vazquez-Abrams <ivazqueznet+rpm@gmail.com> - 0.13.1-2
- Rebuild for Python 2.6

* Wed Nov 12 2008 Jef Spaleta <jspaleta AT fedoraproject DOT org> 0.13.1-1
- Update to 0.13.1 

* Thu Oct 9 2008 Jef Spaleta <jspaleta AT fedoraproject DOT org> 0.13.0-1
- 0.13 Series

* Sun Aug 10 2008 Jef Spaleta <jspaleta AT fedoraproject DOT org> 0.12.2-1
- Bugfix release of the 0.12.x series

* Tue Jul 15 2008 Jef Spaleta <jspaleta AT fedoraproject DOT org> 0.12.0-1
- First of the 0.12.x series

* Tue Jul 1 2008 Jef Spaleta <jspaleta AT fedoraproject DOT org> 0.11.3-1
- latest stable release

* Wed Apr 2 2008 Jef Spaleta <jspaleta@fedoraproject.org> 0.11.1-2
- New Upstream version. 

* Wed Feb 27 2008 Jef Spaleta <jspaleta@fedoraproject.org> 0.11.1-1
- New Upstream version. 

* Wed Jan 23 2008 Jef Spaleta <jspaleta@fedoraproject.org> 0.10.4-1
- New Upstream version. Minor desktop file patch needed.

* Mon Dec 17 2007 Jef Spaleta <jspaleta@gmail.com> 0.10.3-1
- New Upstream version

* Thu Nov 29 2007 Jef Spaleta <jspaleta@gmail.com> 0.10.2-1
- New Upstream version
- A mixed bag of bugfixes and enhancements
- See upstream release notes for full details

* Tue Oct 30 2007 Jef Spaleta <jspaleta@gmail.com> 0.10.1-1
- New Upstream version
- Channel list selection/update bugfixes
- Really load channel metadata
- See upstream website for full release notes

* Sun Oct 07 2007 Jef Spaleta <jspaleta@gmail.com> 0.10.0-1
- New Upstream version

* Sun Aug 26 2007 Jef Spaleta <jspaleta@gmail.com> 0.9.5-1
- New Upstream version

* Fri Aug 03 2007 Jef Spaleta <jspaleta@gmail.com> 0.9.4-2
- Update license tag to GPLv2+ for new licensing guidance

* Sat Jul 28 2007 Jef Spaleta <jspaleta@gmail.com> 0.9.4-1
- Update to 0.9.4 release and adjust specfile accordingly

* Mon Mar 26 2007 Jef Spaleta <jspaleta@gmail.com> 0.9.0-1
- Update to 0.9.0 release and adjust specfile accordingly

* Sun Feb 11 2007 Jef Spaleta <jspaleta@gmail.com> 0.8.9-1
- Update to 0.8.9 release and adjust specfile accordingly

* Wed Dec 27 2006 Jef Spaleta <jspaleta@gmail.com> 0.8.0-3
- Rmove X-Fedora-Extras Category and python dependancy as per review comments 

* Sun Dec 24 2006 Jef Spaleta <jspaleta@gmail.com> 0.8.0-2
- added iconv call to force utf-8 encoding.

* Sun Dec 24 2006 Jef Spaleta <jspaleta@gmail.com> 0.8.0-1
- Initial build for FE inclusion review
