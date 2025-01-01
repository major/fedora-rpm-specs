%global __provides_exclude_from ^%{_kf5_qmldir}/org/kde/amarok/.*\.so$

Name:    amarok
Summary: Media player
Version: 3.2.0
Release: 1%{?dist}

# KDE e.V. may determine that future GPL versions are accepted
License: GPL-2.0-only OR GPL-3.0-only
Url:     https://amarok.kde.org/
%if 0%{?commitdate}
Source0: https://invent.kde.org/multimedia/amarok/-/archive/%{commit}/amarok-%{commit}.tar.bz2
%else
Source0: https://download.kde.org/%{stable_kf5}/amarok/%{version}/amarok-%{version}.tar.xz
%endif

# partially revert https://invent.kde.org/multimedia/amarok/-/commit/c095ebf8780b693605ab23efa4eae6f4dd18fc5e
# it causes amarok to crash on launch for some reason
Patch1:  revert.patch

# Needed because not every distro installs mygpo-qt5 under the same path.
# For instance, Fedora namespaces qt5
Patch10: fix-mygpo-qt5-compilation.patch

BuildRequires: desktop-file-utils
BuildRequires: extra-cmake-modules
BuildRequires: gcc-c++
BuildRequires: gettext
BuildRequires: kf5-rpm-macros
BuildRequires: libappstream-glib
BuildRequires: perl-generators

BuildRequires: cmake(Qt5Core)
BuildRequires: cmake(Qt5DBus)
BuildRequires: cmake(Qt5Gui)
BuildRequires: cmake(Qt5QuickWidgets)
BuildRequires: cmake(Qt5Qml)
BuildRequires: cmake(Qt5Sql)
BuildRequires: cmake(Qt5Svg)
BuildRequires: cmake(Qt5Test)
BuildRequires: cmake(Qt5Widgets)
BuildRequires: cmake(Qt5Xml)
BuildRequires: cmake(Qt5QuickControls2)
%ifarch %{qt5_qtwebengine_arches}
BuildRequires: cmake(Qt5WebEngine)
%endif
BuildRequires: cmake(Qt5UiTools)

BuildRequires: cmake(KF5Archive)
BuildRequires: cmake(KF5Attica)
BuildRequires: cmake(KF5Codecs)
BuildRequires: cmake(KF5Config)
BuildRequires: cmake(KF5ConfigWidgets)
BuildRequires: cmake(KF5CoreAddons)
BuildRequires: cmake(KF5Crash)
BuildRequires: cmake(KF5DBusAddons)
BuildRequires: cmake(KF5Declarative)
BuildRequires: cmake(KF5DNSSD)
BuildRequires: cmake(KF5DocTools)
BuildRequires: cmake(KF5GlobalAccel)
BuildRequires: cmake(KF5GuiAddons)
BuildRequires: cmake(KF5I18n)
BuildRequires: cmake(KF5IconThemes)
BuildRequires: cmake(KF5KCMUtils)
BuildRequires: cmake(KF5KIO)
BuildRequires: cmake(KF5NewStuff)
BuildRequires: cmake(KF5Notifications)
BuildRequires: cmake(KF5Package)
BuildRequires: cmake(KF5Solid)
BuildRequires: cmake(KF5TextEditor)
BuildRequires: cmake(KF5ThreadWeaver)
BuildRequires: cmake(KF5WidgetsAddons)
BuildRequires: cmake(KF5WindowSystem)
BuildRequires: cmake(KF5Kirigami2)
# gpodder, lastfm
BuildRequires: cmake(KF5Wallet)

BuildRequires: pkgconfig(taglib) >= 1.6
BuildRequires: pkgconfig(taglib-extras) >= 1.0.1
BuildRequires: cmake(Phonon4Qt5)
BuildRequires: pkgconfig(libmariadb)
BuildRequires: pkgconfig(mariadb)
BuildRequires: mariadb-embedded-devel
BuildRequires: ffmpeg-free-devel
BuildRequires: fftw-devel
%if 0%{?fedora}
# dependencies not available in RHEL or EPEL
BuildRequires: liblastfm-qt5-devel
BuildRequires: libofa-devel
BuildRequires: cmake(Mygpo-qt5)
BuildRequires: pkgconfig(libmtp) >= 0.3.0
BuildRequires: pkgconfig(libgpod-1.0) >= 0.7.0
# only used together with libgpod
BuildRequires: pkgconfig(gdk-pixbuf-2.0)
# MP3Tunes
BuildRequires: pkgconfig(libcurl)
BuildRequires: pkgconfig(libxml-2.0)
BuildRequires: libgcrypt-devel
BuildRequires: pkgconfig(loudmouth-1.0)
BuildRequires: pkgconfig(glib-2.0) pkgconfig(gobject-2.0)
%endif

Requires:      %{name}-libs%{?_isa} = %{version}-%{release}
Requires:      %{name}-utils = %{version}-%{release}
Requires:      kf5-filesystem
# QML module dependencies
Requires:      kf5-kirigami2%{?_isa}
Requires:      qt5-qtquickcontrols2%{?_isa}

Recommends:    kf5-audiocd-kio
%if 0%{?fedora} >= 40 || 0%{?rhel} >= 10
Recommends:    kio-extras-kf5
%else
Recommends:    kio-extras
%endif
%ifarch %{qt5_qtwebengine_arches}
# Wikipedia QML plugin
Recommends:    qt5-qtwebengine%{?_isa}
%endif
%if 0%{?fedora}
Recommends:    ifuse
Recommends:    media-player-info
%endif

%description
Amarok is a multimedia player with:
 - fresh playlist concept, very fast to use, with drag and drop
 - plays all formats supported by the various engines
 - audio effects, like reverb and compressor
 - compatible with the .m3u and .pls formats for playlists
 - nice GUI, integrates into the KDE look, but with a unique touch

%package libs
Summary: Runtime libraries for %{name}
%description libs
%{summary}.

%package utils
Summary: Amarok standalone utilities
Requires: %{name}-libs = %{version}-%{release}
%description utils
%{summary}, including amarokcollectionscanner.

%package doc
Summary: Application handbook, documentation, translations
Requires:  %{name} = %{version}-%{release}
BuildArch: noarch
%description doc
%{summary}.


%prep
%autosetup %{?commitdate:-n %{name}-%{commit}} -p1

sed -i -e 's|/usr/bin/mysqld|%{_libexecdir}/mysqld|' src/importers/amarok/AmarokConfigWidget.cpp


%build
%if 0%{?flatpak}
# find /app-built libmygpo-qt headers
CXXFLAGS="$CXXFLAGS -I%{_includedir}/qt5"
%endif
# force non-use of MYSQLCONFIG, to avoid (potential bogus) stuff from: mysql_config --libmysqld-libs
%{cmake_kf5} \
%if ! 0%{?fedora}
  -DWITH_GPODDER=OFF -DWITH_IPOD=OFF -DWITH_LASTFM=OFF \
%endif
  -DMYSQLCONFIG_EXECUTABLE:BOOL=OFF
%{cmake_build}


%install
%cmake_install

%find_lang amarokcollectionscanner_qt --with-qt --without-mo --all-name
%find_lang amarok --all-name
%find_lang amarok-doc --with-html --without-mo --all-name


%check
appstream-util validate-relax --nonet %{buildroot}%{_kf5_metainfodir}/org.kde.%{name}.appdata.xml
desktop-file-validate %{buildroot}%{_kf5_datadir}/applications/org.kde.%{name}*.desktop


%files -f amarok.lang
%doc AUTHORS ChangeLog README
%license COPYING
%{_qt5_settingsdir}/amarok_homerc
%{_kf5_bindir}/amarok
%{_kf5_bindir}/amarok_afttagger
%{_kf5_datadir}/amarok/
%{_kf5_datadir}/applications/org.kde.amarok.desktop
%{_kf5_datadir}/applications/org.kde.amarok_containers.desktop
%{_kf5_datadir}/config.kcfg/amarokconfig.kcfg
%{_kf5_datadir}/dbus-1/interfaces/*.xml
%{_kf5_datadir}/dbus-1/services/org.kde.amarok.service
%{_kf5_datadir}/icons/hicolor/*/*/*
%{_kf5_datadir}/knotifications5/amarok.notifyrc
%{_kf5_datadir}/kpackage/amarok/org.kde.amarok.*
%{_kf5_datadir}/kpackage/genericqml/org.kde.amarok.context
%{_kf5_datadir}/kservices5/ServiceMenus/amarok_append.desktop
%{_kf5_datadir}/kservices5/amarok*
%{_kf5_datadir}/solid/actions/amarok-play-audiocd.desktop
%{_kf5_metainfodir}/org.kde.amarok.*.xml
%{_kf5_qmldir}/org/kde/amarok
%{_kf5_qtplugindir}/amarok_collection-audiocdcollection.so
%{_kf5_qtplugindir}/amarok_collection-daapcollection.so
%if 0%{?fedora}
%{_kf5_qtplugindir}/amarok_collection-ipodcollection.so
%{_kf5_qtplugindir}/amarok_collection-mtpcollection.so
%endif
%{_kf5_qtplugindir}/amarok_collection-mysqlcollection.so
%{_kf5_qtplugindir}/amarok_collection-playdarcollection.so
%{_kf5_qtplugindir}/amarok_collection-umscollection.so
%{_kf5_qtplugindir}/amarok_importer-amarok.so
%{_kf5_qtplugindir}/amarok_importer-banshee.so
%{_kf5_qtplugindir}/amarok_importer-clementine.so
%{_kf5_qtplugindir}/amarok_importer-fastforward.so
%{_kf5_qtplugindir}/amarok_importer-itunes.so
%{_kf5_qtplugindir}/amarok_importer-rhythmbox.so
%{_kf5_qtplugindir}/amarok_service_*.so
%{_kf5_qtplugindir}/amarok_storage-mysqlestorage.so
%{_kf5_qtplugindir}/amarok_storage-mysqlserverstorage.so
%{_kf5_qtplugindir}/kcm_amarok_service*.so

%files libs
%{_kf5_libdir}/libamarokcore.so.1*
%{_kf5_libdir}/libamaroklib.so.1*
%{_kf5_libdir}/libamarokshared.so.1*
%{_kf5_libdir}/libamarok-sqlcollection.so.1*
%{_kf5_libdir}/libamarok-transcoding.so.1*
%{_kf5_libdir}/libampache_account_login.so
%{_kf5_libdir}/libamarok-sqlcollection.so
%{_kf5_libdir}/libamarok-transcoding.so
%{_kf5_libdir}/libamarokcore.so
%{_kf5_libdir}/libamaroklib.so
%{_kf5_libdir}/libamarokpud.so
%{_kf5_libdir}/libamarokshared.so
%if 0%{?fedora}
%{_kf5_libdir}/libamarok_service_lastfm_config.so
%{_kf5_libdir}/libgpodder_service_config.so
%endif

%files utils -f amarokcollectionscanner_qt.lang
%{_kf5_bindir}/amarokcollectionscanner

%files doc -f amarok-doc.lang


%changelog
* Mon Dec 30 2024 Steve Cossette <farchord@gmail.com> - 3.2.0-1
- 3.2.0

* Sun Sep 29 2024 Marc Deop i Argemí <marcdeop@fedoraproject.org> - 3.1.1-1
- 3.1.1

* Wed Sep 25 2024 Dominik Mierzejewski <dominik@greysector.net> - 3.0.81-2
- Rebuilt for FFmpeg 7

* Wed Jul 24 2024 Marc Deop i Argemí <marcdeop@fedoraproject.org> - 3.0.81-1
- 3.1 Beta

* Wed Jul 17 2024 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Sun Jul 07 2024 Marc Deop i Argemí <marcdeop@fedoraproject.org> - 3.0.1-1
- 3.0.1

* Wed May 01 2024 Marc Deop i Argemí <marcdeop@fedoraproject.org> - 3.0.0-1
- Update to 3.0.0

* Sun Mar 31 2024 Marc Deop i Argemí <marcdeop@fedoraproject.org> - 2.9.71^git20240330.7ec45dd-1
- Update to snapshot 7ec45dddb109fd391b900dad8705dacd4088a3c3

* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.9.71^git20231231.387c30d-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.9.71^git20231231.387c30d-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Tue Jan 02 2024 Yaakov Selkowitz <yselkowitz@fedoraproject.org> - 2.9.71^20231231git387c30d-1
- Update to KF5-based git snapshot

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.9.0-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Wed Jan 18 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.9.0-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Wed Jul 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.9.0-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed Jan 19 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.9.0-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.9.0-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.9.0-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Jan 25 2021 Honza Horak <hhorak@redhat.com> - 2.9.0-10
- Use correct name for the mariadb package

* Fri Jul 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.9.0-9
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.9.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jun 23 2020 Rex Dieter <rdieter@fedoraproject.org> - 2.9.0-7
- drop loudmouth support f33+

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.9.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.9.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Mon Apr 22 2019 Rex Dieter <rdieter@fedoraproject.org> - 2.9.0-4
- rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.9.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.9.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Mar 07 2018 Rex Dieter <rdieter@fedoraproject.org> - 2.9.0-1
- amarok-2.9.0

* Wed Feb 28 2018 Rex Dieter <rdieter@fedoraproject.org> - 2.8.90-19
- use %%ldconfig_scriptlets, %%_kf5_metainfodir, BR: gcc-c++

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.8.90-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Sun Jan 07 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 2.8.90-17
- Remove obsolete scriptlets

* Tue Oct 17 2017 Rex Dieter <rdieter@fedoraproject.org> - 2.8.90-16
- amzdownloader.desktop: NoDisplay=true

* Thu Oct 05 2017 Rex Dieter <rdieter@fedoraproject.org> - 2.8.90-15
- use mariadb-connector-c-devel on f28+ (#1494091)

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.8.90-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.8.90-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Mon Apr 03 2017 Rex Dieter <rdieter@fedoraproject.org> - 2.8.90-11
- pul in more upstream fixes

* Thu Feb 23 2017 Rex Dieter <rdieter@fedoraproject.org> - 2.8.90-10
- Recommends: audiocd-kio kio_mtp kio-upnp-ms

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.8.90-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Sun Aug 07 2016 Rex Dieter <rdieter@fedoraproject.org> - 2.8.90-8
- pull in upstream fixes

* Sat Jul 23 2016 Rex Dieter <rdieter@fedoraproject.org> - 2.8.90-7
- fix mpris support (kde#365275)

* Wed Jun 01 2016 Rex Dieter <rdieter@fedoraproject.org> - 2.8.90-6
- pull in upstream fixes, fix build with gcc6 (kde#363054)

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 2.8.90-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Tue Dec 29 2015 Rex Dieter <rdieter@fedoraproject.org> 2.8.90-4
- add support for kf5 solid/actions,ServiceMenus

* Thu Dec 10 2015 Rex Dieter <rdieter@fedoraproject.org> 2.8.90-3
- workaround 'mysql_config --libmysqld-libs' madness (#1290517)

* Thu Dec 10 2015 Rex Dieter <rdieter@fedoraproject.org> 2.8.90-2
- make kde-runtime dep unversioned, use %%license

* Fri Sep 11 2015 Rex Dieter <rdieter@fedoraproject.org> 2.8.90-1
- 2.8.90

* Fri Aug 28 2015 Rex Dieter <rdieter@fedoraproject.org> 2.8.0-19
- backport upstream FindTaglib.cmake fix

* Mon Jun 29 2015 Rex Dieter <rdieter@fedoraproject.org> 2.8.0-18
- Amarok has an unmet dependency on rhel7: audiocd-kio (#1232818)

* Sun Jun 28 2015 Rex Dieter <rdieter@fedoraproject.org> 2.8.0-17
- pull in upstream fixes for wikipedia plugin (kde#349313)

* Tue Jun 16 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.8.0-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat May 02 2015 Kalev Lember <kalevlember@gmail.com> - 2.8.0-15
- Rebuilt for GCC 5 C++11 ABI change

* Fri Feb 20 2015 Rex Dieter <rdieter@fedoraproject.org> - 2.8.0-14
- backport gl crasher workaround (kde#323635)
- deprecate -nepomukcollection (f22+)

* Sat Nov 08 2014 Rex Dieter <rdieter@fedoraproject.org> 2.8.0-13
- use fresher upstream appdata (translations mostly)

* Fri Nov 07 2014 Rex Dieter <rdieter@fedoraproject.org> 2.8.0-12
- pull in upstream (master/ branch) appdata

* Sat Oct 18 2014 Rex Dieter <rdieter@fedoraproject.org> 2.8.0-11
- drop Requires: moodbar (which still pulls in gstreamer-0.10)

* Wed Oct 01 2014 Rex Dieter <rdieter@fedoraproject.org> 2.8.0-10
- rebuild (libmygpo-qt test)

* Fri Aug 15 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.8.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Tue Jul 08 2014 Rex Dieter <rdieter@fedoraproject.org> 2.8.0-8
- scriptet polish

* Thu Jul 03 2014 Rex Dieter <rdieter@fedoraproject.org> 2.8.0-7
- optimize mimeinfo scriplet

* Thu Jun 19 2014 Rex Dieter <rdieter@fedoraproject.org> 2.8.0-6
- work on epel7 support, BR: kdelibs4-webkit-devel

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.8.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Mon Apr 14 2014 Rex Dieter <rdieter@fedoraproject.org> 2.8.0-4
- -nepomukcollection subpkg

* Tue Aug 27 2013 Rex Dieter <rdieter@fedoraproject.org> 2.8.0-3.1
- BR: libmygpo-qt-devel >= 1.0.7

* Sat Aug 17 2013 Rex Dieter <rdieter@fedoraproject.org> 2.8.0-3
- Requires: moodbar

* Fri Aug 16 2013 Rex Dieter <rdieter@fedoraproject.org> 2.8.0-2
- (Build)Requires: clamz

* Thu Aug 15 2013 Rex Dieter <rdieter@fedoraproject.org> 2.8.0-1
- 2.8.0

* Sat Aug 03 2013 Petr Pisar <ppisar@redhat.com> - 2.7.90-2
- Perl 5.18 rebuild

* Thu Aug 01 2013 Rex Dieter <rdieter@fedoraproject.org> 2.7.90-1
- 2.7.90

* Wed Jul 17 2013 Petr Pisar <ppisar@redhat.com> - 2.7.1-3
- Perl 5.18 rebuild

* Fri May 17 2013 Rex Dieter <rdieter@fedoraproject.org> 2.7.1-2
- drop already-included qtwebkit/wikipedia fixer

* Thu May 16 2013 Rex Dieter <rdieter@fedoraproject.org> 2.7.1-1
- 2.7.1

* Mon May 13 2013 Rex Dieter <rdieter@fedoraproject.org> - 2.7.0-4
- backport a few upstream fixes, in particular...
- workaround for qtwebkit/wikipedia related crashes (kde #319371)

* Sat Feb 02 2013 Rex Dieter <rdieter@fedoraproject.org> 2.7.0-3
- rebuild (mariadb)

* Mon Jan 28 2013 Rex Dieter <rdieter@fedoraproject.org> 2.7.0-2
- Requires: kio_mtp, kio-upnp-ms

* Thu Jan 17 2013 Rex Dieter <rdieter@fedoraproject.org> 2.7.0-1
- 2.7.0

* Sat Dec 15 2012 Rex Dieter <rdieter@fedoraproject.org> - 2.6.90-2
- up build deps (nepomuk-core, liblastfm)
- changelog: prune, fix bad dates

* Fri Dec 14 2012 Rex Dieter <rdieter@fedoraproject.org> 2.6.90-1
- 2.6.90

* Tue Nov 27 2012 Jan Grulich <jgrulich@redhat.com> 2.6.0-7
- rebuild (qjson)

* Sat Nov 24 2012 Rex Dieter <rdieter@fedoraproject.org> 2.6.0-6
- rebuild (qjson)

* Tue Sep 11 2012 Rex Dieter <rdieter@fedoraproject.org> 2.6.0-5
- -doc: update summary to mention translations

* Fri Sep 7 2012 Dominique Bribanick <chepioq@gmail.com> 2.6.0-4
- add patch for french translation (#855655)

* Sat Aug 25 2012 Rex Dieter <rdieter@fedoraproject.org> 2.6.0-3
- Requires: kdemultimedia-kio_audiocd/audiocd-kio

* Wed Aug 22 2012 Rex Dieter <rdieter@fedoraproject.org> 2.6.0-2.1
- use liblastfm1 on f16/f17 too

* Sun Aug 12 2012 Rex Dieter <rdieter@fedoraproject.org> 2.6.0-2
- Requires: media-player-info

* Sat Aug 11 2012 Rex Dieter <rdieter@fedoraproject.org> 2.6.0-1
- 2.6.0

* Thu Aug 02 2012 Rex Dieter <rdieter@fedoraproject.org> 2.5.96-1
- 2.5.96 (2.6rc1)

* Wed Jul 18 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.5.90-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Mon Jul 16 2012 Rex Dieter <rdieter@fedoraproject.org> 2.5.90-5
- backport upstream commit to disable polling (kde#289462)

* Sat Jul 14 2012 Rex Dieter <rdieter@fedoraproject.org> 2.5.90-4
- update kdelibs/phonon dep versions

* Tue Jul 03 2012 Rex Dieter <rdieter@fedoraproject.org> 2.5.90-3
- add reviewboard patch to support liblastfm1

* Tue Jul 03 2012 Rex Dieter <rdieter@fedoraproject.org> 2.5.90-2
- rebuild (liblastfm)

* Wed May 30 2012 Rex Dieter <rdieter@fedoraproject.org> 2.5.90-1
- 2.5.90

* Wed Mar 21 2012 Rex Dieter <rdieter@fedoraproject.org> 2.5.0-9
- new iteration of proxy_loading patch (kde#295199)

* Tue Mar 13 2012 Rex Dieter <rdieter@fedoraproject.org> 2.5.0-8
- Load all XSPF tracks (kde#295199)

* Tue Feb 28 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.5.0-7
- Rebuilt for c++ ABI breakage

* Sun Jan 29 2012 Kevin Kofler <Kevin@tigcc.ticalc.org> 2.5.0-6
- help: invoke a browser on the online UserBase doc if amarok-doc not installed

* Fri Jan 27 2012 Rex Dieter <rdieter@fedoraproject.org> 2.5.0-5
- make -doc only handbook, put translations back in main pkg

* Fri Jan 27 2012 Rex Dieter <rdieter@fedoraproject.org> 2.5.0-4
- -doc subpkg for large'ish application handbook and translations

* Fri Jan 27 2012 Rex Dieter <rdieter@fedoraproject.org> 2.5.0-3
- fix context view when on kde48 (kde#290123)

* Thu Jan 12 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.5.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Fri Dec 16 2011 Rex Dieter <rdieter@fedoraproject.org> 2.5.0-1
- 2.5.0

* Mon Nov 14 2011 Rex Dieter <rdieter@fedoraproject.org> 2.4.90-1
- 2.4.90

* Wed Nov 09 2011 Rex Dieter <rdieter@fedoraproject.org> 2.4.3-4
- pkgconfig-style deps
- drop extraneous/old BR's

* Mon Sep 19 2011 Rex Dieter <rdieter@fedoraproject.org> 2.4.3-3
- Wikipedia applet crashes (kde#279813)

* Fri Sep 16 2011 Rex Dieter <rdieter@fedoraproject.org> 2.4.3-2
- re-enable libgpod support inadvertantly lost in 2.4.1.90-1

* Sat Jul 30 2011 Rex Dieter <rdieter@fedoraproject.org> 2.4.3-1
- 2.4.3

* Sun Jul 24 2011 Rex Dieter <rdieter@fedoraproject.org> 2.4.2-2
- don't query kwallet for lastfm credentials on every track change (kde#278177)

* Fri Jul 22 2011 Rex Dieter <rdieter@fedoraproject.org> 2.4.2-1
- 2.4.2

* Fri Jul 08 2011 Rex Dieter <rdieter@fedoraproject.org> 2.4.1.90-1
- 2.4.1.90
- drop no-longer-needed %%ifarch s390 conditionals

* Fri Jun 10 2011 Rex Dieter <rdieter@fedoraproject.org> 2.4.1-4
- drop ancient Obsoletes

* Fri Jun 10 2011 Rex Dieter <rdieter@fedoraproject.org> 2.4.1-3
- rebuild (libmtp)

* Tue May 24 2011 Rex Dieter <rdieter@fedoraproject.org> 2.4.1-2
- BR: libmygpo-qt-devel

* Fri May 06 2011 Rex Dieter <rdieter@fedoraproject.org> 2.4.1-1
- 2.4.1 (final)

* Wed Mar 23 2011 Rex Dieter <rdieter@fedoraproject.org> 2.4.0.90-2
- rebuild (mysql)

* Mon Mar 21 2011 Rex Dieter <rdieter@fedoraproject.org> 2.4.0.90-1
- 2.4.1 beta1

* Wed Feb 09 2011 Rex Dieter <rdieter@fedoraproject.org> 2.4.0-3
- License: GPLv2 or GPLv3 

* Mon Feb 07 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.4.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Tue Jan 11 2011 Rex Dieter <rdieter@fedoraproject.org> 2.4.0-1
- 2.4.0
- libmtp-hal dependency missing for amarok (#666173)

* Tue Dec 28 2010 Rex Dieter <rdieter@fedoraproject.org> 2.3.90-3
- rebuild (mysql)

* Tue Dec 07 2010 Thomas Janssen <thomasj@fedoraproject.org> 2.3.90-2
- fixed missing libampache

* Mon Dec 06 2010 Thomas Janssen <thomasj@fedoraproject.org> 2.3.90-1
- 2.3.90 (2.4beta1)

* Tue Nov 30 2010 Rex Dieter <rdieter@fedoraproject.org> 2.3.2-7
- recognize audio/flac mimetype too (kde#257488)

* Fri Nov 05 2010 Thomas Janssen <thomasj@fedoraproject.org> 2.3.2-6
- rebuild for new libxml2

* Thu Nov 04 2010 Rex Dieter <rdieter@fedoraproject.org> 2.3.2-5
- appletsize patch
- fix/improve ipod3 support patch
- another collectionscanner patch

* Wed Sep 29 2010 jkeating - 2.3.2-4
- Rebuilt for gcc bug 634757

* Fri Sep 24 2010 Thomas Janssen <thomasj@fedoraproject.org> 2.3.2-3
- added patch to fix scanning qt bug/regression

* Mon Sep 20 2010 Thomas Janssen <thomasj@fedoraproject.org> 2.3.2-2
- added patch to fix BPM tags in flac

* Thu Sep 16 2010 Rex Dieter <rdieter@fedoraproject.org> - 2.3.2-1
- amarok-2.3.2

* Thu Sep 16 2010 Dan Horák <dan[at]danny.cz> - 2.3.1.90-3
- no libgpod on s390(x)

* Mon Aug 16 2010 Rex Dieter <rdieter@fedoraproject.org> - 2.3.1.90-2
- fix/patch installation of amarok handbooks

* Mon Aug 16 2010 Rex Dieter <rdieter@fedoraproject.org> - 2.3.1.90-1
- amarok-2.3.1.90 (2.3.2 beta1)

* Fri Jul 09 2010 Rex Dieter <rdieter@fedoraproject.org> - 2.3.1-2
- No Notification Area icon for non-KDE desktops (kde#232578,rh#603336)

* Fri May 28 2010 Rex Dieter <rdieter@fedoraproject.org> - 2.3.1-1
- amarok-2.3.1

* Sat Apr 17 2010 Rex Dieter <rdieter@fedoraproject.org> - 2.3.0.90-1
- amarok-2.3.0.90

* Thu Mar 25 2010 Rex Dieter <rdieter@fedoraproject.org> - 2.3.0-5
- fix mp3 support logic

* Mon Mar 22 2010 Rex Dieter <rdieter@fedoraproject.org> - 2.3.0-4
- rebuild (libgpod) 

* Mon Mar 22 2010 Rex Dieter <rdieter@fedoraproject.org>  - 2.3.0-3
- workaround info applet crasher (kde#227639,kde#229756)

* Thu Mar 11 2010 Rex Dieter <rdieter@fedoraproject.org> - 2.3.0-2
- fix Source0 URL
- -libs: drop unused/extraneous kdelibs4 dep

* Thu Mar 11 2010 Thomas Janssen <thomasj@fedoraproject.org> 2.3.0-1
- amarok 2.3.0

* Sat Feb 13 2010 Rex Dieter <rdieter@fedoraproject.org> - 2.2.2.90-1
- amarok-2.2.2.90 (2.3beta1)

* Thu Jan 28 2010 Rex Dieter <rdieter@fedoraproject.org> - 2.2.2-4
- use %%{_kde4_version} provided elsewhere (kde-filesystem)

* Sun Jan 10 2010 Rex Dieter <rdieter@fedoraproject.org> - 2.2.2-3
- collection scan crash patch, take 2 (kde#220532)

* Fri Jan 08 2010 Rex Dieter <rdieter@fedoraproject.org> - 2.2.2-2
- collection scan crash patch (kde#220532)

* Tue Jan 05 2010 Rex Dieter <rdieter@fedoraproject.org> - 2.2.2-1
- amarok-2.2.2

* Thu Dec 10 2009 Rex Dieter <rdieter@fedoraproject.org> - 2.2.1.90-1
- amarok-2.2.1.90 (2.2.2 beta1)

* Mon Nov 23 2009 Rex Dieter <rdieter@fedoraproject.org> - 2.2.1-3 
- rebuild (for qt-4.6.0-rc1, f13+)

* Mon Nov 16 2009 Rex Dieter <rdieter@fedoraproject.org> 2.2.1-2
- playlist_default_layout_fix.diff (kde#211717)

* Wed Nov 11 2009 Rex Dieter <rdieter@fedoraproject.org> 2.2.1-1
- amarok-2.2.1

* Thu Oct 08 2009 Rex Dieter <rdieter@fedoraproject.org> 2.2.0-3
- upstream lyric.patch

* Fri Oct 02 2009 Rex Dieter <rdieter@fedoraproject.org> 2.2.0-2
- Requires: kdebase-runtime (need kio_trash, kcm_phonon, etc)

* Tue Sep 29 2009 Rex Dieter <rdieter@fedoraproject.org> 2.2.0-1
- amarok-2.2.0

* Wed Sep 23 2009 Rex Dieter <rdieter@fedoraproject.org> 2.1.90-2.20090923git
- 20090923git snapshot

* Mon Sep 21 2009 Rex Dieter <rdieter@fedoraproject.org> 2.1.90-1
- amarok-2.1.90 (2.2rc1)

* Thu Sep 17 2009 Rex Dieter <rdieter@fedoraproject.org> 2.1.85-2
- BR: taglib-devel >= 1.6, taglib-extras-devel >= 1.0

* Mon Sep 14 2009 Rex Dieter <rdieter@fedoraproject.org> 2.1.85-1
- amarok-2.1.85 (2.2beta2)

* Wed Sep 02 2009 Rex Dieter <rdieter@fedoraproject.org> 2.1.80-2
- another lyricwiki fix

* Wed Sep 02 2009 Rex Dieter <rdieter@fedoraproject.org> 2.1.80-1
- amarok-2.1.80 (2.2beta1)
- -libs subpkg

* Fri Aug 21 2009 Tomas Mraz <tmraz@redhat.com> - 2.1.1-5
- rebuilt with new openssl

* Sat Aug 08 2009 Rex Dieter <rdieter@fedoraproject.org> 2.1.1-4
- lyricwiki patch (kdebug#202366)

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.1.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Tue Jul 07 2009 Rex Dieter <rdieter@fedoraproject.org> 2.1.1-2
- Requires: qtscriptbindings%%{?_isa}  (#510133)

* Fri Jun 12 2009 Rex Dieter <rdieter@fedoraproject.org> 2.1.1-1
- amarok-2.1.1

* Sat May 30 2009 Rex Dieter <rdieter@fedoraproject.org> 2.1-1
- amarok-2.1

* Mon May 18 2009 Rex Dieter <rdieter@fedoraproject.org> 2.0.96-2.20090518
- 20090518svn snapshot

* Mon May 11 2009 Rex Dieter <rdieter@fedoraproject.org> 2.0.96-1
- amarok-2.9.96 (2.1 beta2)
- -utilities -> -utils

* Fri Apr 10 2009 Rex Dieter <rdieter@fedoraproject.org> 2.0.90-2
- -collectionscanner -> -utilities

* Fri Apr 10 2009 Rex Dieter <rdieter@fedoraproject.org> 2.0.90-1
- amarok-2.0.90 (amarok-2.1 beta1)

* Wed Apr 08 2009 Rex Dieter <rdieter@fedoraproject.org> 2.0.2-6
- fix lastfm (kdebug#188678, rhbz#494871)
- fix qtscriptgenerator/qtscriptbindings deps

* Tue Apr 07 2009 Rex Dieter <rdieter@fedoraproject.org> 2.0.2-5
- enable external qtscriptgenerator/qtscriptbindings
- optimize scriptlets

* Tue Mar 10 2009 Rex Dieter <rdieter@fedoraproject.org> 2.0.2-4
- Req: qtscriptgenerator (f11+) (not enabled, pending review)
- use desktop-file-validate

* Fri Mar 06 2009 Rex Dieter <rdieter@fedoraproject.org> 2.0.2-3
- add minimal qt4,kdelibs4 deps

* Wed Mar 04 2009 Rex Dieter <rdieter@fedoraproject.org> 2.0.2-1
- amarok-2.0.2

* Tue Feb 24 2009 Than Ngo <than@redhat.com> 2.0.1.1-6
- fix build issue against gcc-4.4

* Mon Feb 23 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0.1.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Mon Feb 23 2009 Rex Dieter <rdieter@fedoraproject.org> - 2.0.1.1-4
- qt45 patch

* Fri Feb 20 2009 Todd Zullinger <tmz@pobox.com> - 2.0.1.1-3
- Rebuild against libgpod-0.7.0
- Drop gtk2-devel BR, libgpod properly requires that now

* Thu Jan 22 2009 Rex Dieter <rdieter@fedoraproject.org> - 2.0.1.1-2 
- respin (mysql)

* Fri Jan 09 2009 Rex Dieter <rdieter@fedoraproject.org> - 2.0.1.1-1
- amarok-2.0.1.1

* Tue Jan 06 2009 Rex Dieter <rdieter@fedoraproject.org> - 2.0.1-1
- amarok-2.0.1

* Tue Dec 09 2008 Rex Dieter <rdieter@fedoraproject.org> - 2.0-2
- respin tarball

* Fri Dec 05 2008 Rex Dieter <rdieter@fedoraproject.org> - 2.0-1
- amarok-2.0 (final, first cut)
