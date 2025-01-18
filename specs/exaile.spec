Name:           exaile
Version:        4.1.3
Release:        9%{?dist}
Summary:        Simple but powerful Amarok-style music player for GTK users
License:        GPL-2.0-or-later
URL:            http://www.exaile.org
Source0:        https://github.com/exaile/exaile/archive/%{version}/%{name}-%{version}.tar.gz
# 'pipes' is deprecated (#935)
Patch0:         f37bb5e3ef33f05c12fd30fcbf38207498d7a909.patch
# 'sunau' is deprecated (#936)
Patch1:         af42edf558fcf614ff861c18806986c2bf6fdfe7.patch
BuildArch:      noarch

BuildRequires:  python3-rpm-macros

# Dependencies:
# see also https://github.com/exaile/exaile/blob/master/DEPS
BuildRequires:  cairo-gobject
BuildRequires:  desktop-file-utils
BuildRequires:  gettext
BuildRequires:  gobject-introspection
BuildRequires:  gstreamer1-plugins-base >= 1.16
BuildRequires:  gstreamer1-plugins-good >= 1.16
BuildRequires:  gtk3 >= 3.24
BuildRequires:  help2man
BuildRequires:  libappstream-glib
BuildRequires:  python3-bsddb3
BuildRequires:  python3-cairo
BuildRequires:  python3-dbus
BuildRequires:  python3-devel
BuildRequires:  python3-gobject-devel >= 3.24
BuildRequires:  python3-gstreamer1 >= 1.16
BuildRequires:  python3-mutagen >= 1.44
BuildRequires:  python3-setproctitle
BuildRequires:  python3-pytest

Requires:       python3 >= 3.8
Requires:       python3-bsddb3
Requires:       gtk3 >= 3.24
Requires:       python3-gstreamer1 >= 1.16
Requires:       gstreamer1-plugins-good >= 1.16
Requires:       gstreamer1-plugins-base >= 1.16
Requires:       python3-mutagen >= 1.44
Requires:       python3-dbus
Requires:       python3-gobject >= 3.24
Requires:       python3-cairo
Requires:       cairo-gobject
Requires:       python3-setproctitle

# Device detection:
Recommends:     libudisks2
# DAAP plugins (daapserver and daapclient):
#Not packaged for Fedora
#Recommends:     spydaap
#Recommends:     python3-zeroconf
# Last.FM integration:
Recommends:     python3-pylast
# Lyrics from lyricsmania.com (lyricsmania):
Recommends:     python3-lxml
# Lyrics from lyrics.wikia.com (lyricwiki):
Recommends:     python3-beautifulsoup4
# Musicbrainz covers:
Recommends:     python3-musicbrainzngs
# Podcast plugin:
Recommends:     python3-feedparser
# Wikipedia info:
#Not packaged for fedora
#Recommends:     webkit2gtk3
# Xlib-based hotkeys:
Recommends:     keybinder3
# Scalable icons:
Recommends:     librsvg2
# Native Notifications:
Recommends:     libnotify
# Recording streams:
Recommends:     streamripper
# Moodbar plugin:
#FTBFS on Fedora 30+, may be dropped soon
#Recommends:     moodbar
# BPM Counter plugin:
Recommends:     gstreamer1-plugins-bad-free
# CD Info and Musicbrainz covers:
Recommends:     python3-discid
Recommends:     python3-musicbrainzngs


%description
Exaile is a music player with a simple interface and powerful music
management capabilities. Features include automatic fetching of album art,
lyrics fetching, streaming internet radio, tabbed playlists, smart
playlists with extensive filtering/search capabilities, and much more.

Exaile is written using Python and GTK+ and is easily extensible via
plugins. There are over 50 plugins distributed with Exaile that include
advanced track tagging, last.fm scrobbling, support for portable media
players, podcasts, internet radio such as icecast and Soma.FM,
ReplayGain, output via a secondary output device (great for DJs!), and
much more.

%prep
%autosetup -p1

%build
%set_build_flags

# Keep timestamps while installing
# Delegate pyc compilation to brp-python-bytecompile
sed -i "s|install -m|\$(INSTALL) -m|;s|all: compile |all: |" Makefile

# Disable plugins that aren't packaged or don't work on Fedora
sed -i "s|BAD = \[\]|BAD = ['daapclient', 'daapserver', 'moodbar', 'winmmkeys', 'wikipedia']|" plugins/list.py

%make_build

%install
%make_install PREFIX=%{_prefix} LIBINSTALLDIR=%{_datadir} PYTHON3_CMD=%{__python3}

desktop-file-install --delete-original \
    --dir=%{buildroot}%{_datadir}/applications \
    %{buildroot}%{_datadir}/applications/%{name}.desktop

%find_lang %{name}

%check
# this test should be ignored on Fedora/Debian systems and also doesn't work via Koji
rm tests/xl/trax/test_migration.py

appstream-util validate-relax --nonet %{buildroot}%{_metainfodir}/exaile.appdata.xml

make test

%files -f %{name}.lang
%doc README.md
%license COPYING
%{_bindir}/exaile
%{_metainfodir}/exaile.appdata.xml
%{_datadir}/applications/exaile.desktop
%{_datadir}/bash-completion/completions/exaile
%{_datadir}/fish/vendor_completions.d/exaile.fish
%{_datadir}/icons/hicolor/*/apps/exaile.*
%{_datadir}/exaile/
%{_datadir}/dbus-1/services/org.exaile.Exaile.service
%dir %{_sysconfdir}/xdg/exaile/
%config(noreplace) %{_sysconfdir}/xdg/exaile/settings.ini
%{_mandir}/man1/exaile*.1*

%changelog
* Thu Jan 16 2025 Fedora Release Engineering <releng@fedoraproject.org> - 4.1.3-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Thu Aug 01 2024 Graham White <graham_alton@hotmail.com> - 4.1.3-8
- re-add Sun AU format with new AU metadata parser

* Tue Jul 30 2024 Graham White <graham_alton@hotmail.com> - 4.1.3-7
- re-add fish completions with patch (#935)
- remove Sun AU format support as it's deprecated in Python 3.13 (#936)

* Tue Jul 30 2024 Graham White <graham_alton@hotmail.com> - 4.1.3-6
- remove fish completions due to the use of python pipes which is deprecated

* Thu Jul 25 2024 Miroslav Suchý <msuchy@redhat.com> - 4.1.3-5
- convert license to SPDX

* Wed Jul 17 2024 Fedora Release Engineering <releng@fedoraproject.org> - 4.1.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Wed Jan 24 2024 Fedora Release Engineering <releng@fedoraproject.org> - 4.1.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 4.1.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Tue Nov 14 2023 Graham White <graham_alton@hotmail.com> - 4.1.3-1
- Update to 4.1.3
- Re-enable CD Info plugin
- Disable Wikipedia plugin

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 4.1.2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Fri May 19 2023 Yaakov Selkowitz <yselkowi@redhat.com> - 4.1.2-5
- Use webkit2gtk-4.1 in wikipedia plugin

* Fri Feb 24 2023 Graham White <graham_alton@hotmail.com> - 4.1.2-4
- Enable the BPM Counter plugin

* Thu Jan 19 2023 Yaakov Selkowitz <yselkowi@redhat.com> - 4.1.2-3
- Install icons according to FreeDesktop specification
- Add soft dependency needed for BPM Counter plugin

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 4.1.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Wed Aug 10 2022 Graham White <graham_alton@hotmail.com> - 4.1.2-1
- Update to 4.1.2
- Re-enable testing framework
- Update path to appdata

* Tue Aug 02 2022 Graham White <graham_alton@hotmail.com> - 4.1.1-9
- Disable testing framework that uses deprecated packages (#2113217)

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 4.1.1-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 4.1.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Sep 08 2021 Graham White <graham_alton@hotmail.com> - 4.1.1-6
- Fix traceback when scanning files that have been removed (BZ #1990693)

* Tue Aug 03 2021 Graham White <graham_alton@hotmail.com> - 4.1.1-5
- Disable plugins that aren't packaged or don't work on Fedora

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 4.1.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jul 09 2021 Graham White <graham_alton@hotmail.com> - 4.1.1-2
- Responding to package review (BZ #1980282)

* Fri Apr 16 2021 Graham White <graham_alton@hotmail.com> - 4.1.1-1
- Update to 4.1.1
- Python 3 compatibility

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 4.0.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Jun 22 2019 Christian Stadelmann <genodeftest@fedoraproject.org> - 4.0.0-2
- Update dependencies, add plugin dependencies as optional

* Thu Jun 20 2019 Leigh Scott <leigh123linux@googlemail.com> - 4.0.0-1
- Update to 4.0.0

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.4.5-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.4.5-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 3.4.5-8
- Escape macros in %%changelog

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.4.5-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Tue Feb 06 2018 Iryna Shcherbina <ishcherb@redhat.com> - 3.4.5-6
- Update Python 2 dependency declarations to new packaging standards
  (See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3)

* Sat Aug 26 2017 William Moreno <williamjmorenor@gmail.com> - 3.4.5-5
- Update requires to python2 binary rename

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.4.5-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.4.5-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 3.4.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Jul 10 2015 Christopher Meng <rpm@cicku.me> - 3.4.5-1
- Update to 3.4.5

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.4.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Fri Jan 09 2015 Christopher Meng <rpm@cicku.me> - 3.4.3-1
- Update to 3.4.3

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.3.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Fri Feb 21 2014 Deji Akingunola <dakingun@gmail.com> - 3.3.2-1
- Update to 3.3.2

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.3.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Fri Mar 08 2013 Jon Ciesla <limburgher@gmail.com> - 3.3.1-3
- Drop desktop vendor tag.

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.3.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sat Nov 17 2012 Deji Akingunola <dakingun@gmail.com> - 3.3.1-1
- Update to 3.3.1

* Mon Sep 24 2012 Deji Akingunola <dakingun@gmail.com> - 3.3.0-1
- Update to 3.3.0

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3.2.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3.2.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Mon Sep 12 2011 Deji Akingunola <dakingun@gmail.com> - 0.3.2.2-2
- Place exaile's private modules in %%datadir
- Trim (un-necessary?) requires

* Wed Aug 31 2011 Deji Akingunola <dakingun@gmail.com> - 0.3.2.2-1
- Update to 0.3.2.2
- Drop hal. Apply patch to support udisk from upstream bzr's udisk branch

* Thu Mar 03 2011 Deji Akingunola <dakingun@gmail.com> - 0.3.2.1-1
- Update to 0.3.2.1

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3.2.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Wed Jul 21 2010 David Malcolm <dmalcolm@redhat.com> - 0.3.2.0-2
- Rebuilt for https://fedoraproject.org/wiki/Features/Python_2.7/MassRebuild

* Mon Jun 28 2010 Deji Akingunola <dakingun@gmail.com> - 0.3.2.0-1
- Update to 0.3.2.0

* Wed Jun 09 2010 Deji Akingunola <dakingun@gmail.com> - 0.3.1.2-1
- Update to 0.3.1.2

* Fri Apr 09 2010 Deji Akingunola <dakingun@gmail.com> - 0.3.1.1-1
- Update to 0.3.1.1

* Sat Mar 20 2010 Deji Akingunola <dakingun@gmail.com> - 0.3.1.0-1
- Update to 0.3.1.0

* Wed Nov 25 2009 Deji Akingunola <dakingun@gmail.com> - 0.3.0.2-1
- Update to 0.3.0.2

* Wed Sep 30 2009 Deji Akingunola <dakingun@gmail.com> - 0.3.0.1-1
- Update to 0.3.0.1

* Fri Aug 28 2009 Deji Akingunola <dakingun@gmail.com> - 0.3.0-1
- Update to 0.3.0

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2.14-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Tue Feb 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2.14-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Sun Nov 30 2008 Ignacio Vazquez-Abrams <ivazqueznet+rpm@gmail.com> - 0.2.14-2
- Rebuild for Python 2.6

* Thu Oct 09 2008 Deji Akingunola <dakingun@gmail.com> - 0.2.14-1
- Update to 0.2.14

* Fri Jul 11 2008 Tom "spot" Callaway <tcallawa@redhat.com> - 0.2.13-3
- fix license tag

* Mon Jul 07 2008 Tom "spot" Callaway <tcallawa@redhat.com> - 0.2.13-2
- fix conditional comparison
- add sparc64 to 64bit arch check

* Wed Apr 02 2008 Deji Akingunola <dakingun@gmail.com> - 0.2.13-1
- Update to 0.2.13

* Sun Feb 10 2008 Deji Akingunola <dakingun@gmail.com> - 0.2.11.1-2
- Rebuild for gcc43

* Thu Nov 29 2007 Deji Akingunola <dakingun@gmail.com> - 0.2.11.1-1
- Update to 0.2.11.1 that removes bogus cruft from 0.2.11 source tarball
- Rebuild for firefox-2.0.0.10

* Tue Nov 06 2007 Deji Akingunola <dakingun@gmail.com> - 0.2.11-2
- Rebuild for firefox-2.0.0.9

* Mon Oct 22 2007 Deji Akingunola <dakingun@gmail.com> - 0.2.11-1
- New release

* Tue Sep 11 2007 Deji Akingunola <dakingun@gmail.com> - 0.2.10-3
- Require pygtk2-libglade (BZ #278471)

* Wed Aug 22 2007 Deji Akingunola <dakingun@gmail.com> - 0.2.10-2
- Rebuild

* Fri Aug 03 2007 Deji Akingunola <dakingun@gmail.com> - 0.2.10-2
- License tag update

* Sat Jun 30 2007 Deji Akingunola <dakingun@gmail.com> - 0.2.10-1
- New release

* Fri Mar 30 2007 Deji Akingunola <dakingun@gmail.com> - 0.2.9-1
- New release

* Tue Jan 09 2007 Deji Akingunola <dakingun@gmail.com> - 0.2.8-1
- New release

* Sat Dec 30 2006 Deji Akingunola <dakingun@gmail.com> - 0.2.7-1
- New release

* Wed Dec 27 2006 Deji Akingunola <dakingun@gmail.com> - 0.2.6-3
- Rework the python include patch

* Wed Dec 27 2006 Deji Akingunola <dakingun@gmail.com> - 0.2.6-2
- Rewrite the build patch to be more generic

* Tue Dec 26 2006 Deji Akingunola <dakingun@gmail.com> - 0.2.6-1
- First version for Fedora Extras
