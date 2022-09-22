%global gtk3_version 3.20.0
%global libdmapsharing_version 3.9.4
%global libsecret_version 0.18

%global __provides_exclude_from ^%{_libdir}/%{name}/plugins/.*/.*\\.so.*$

Name:    rhythmbox
Version: 3.4.6
Release: 2%{?dist}
Summary: Music Management Application

License: GPLv2+ with exceptions and GFDL
URL:     https://wiki.gnome.org/Apps/Rhythmbox
Source0: https://download.gnome.org/sources/rhythmbox/3.4/%{name}-%{version}.tar.xz

BuildRequires: pkgconfig(gobject-introspection-1.0) >= 0.10.0
BuildRequires: pkgconfig(grilo-0.3) >= 0.3.0
BuildRequires: pkgconfig(gstreamer-1.0)
BuildRequires: pkgconfig(gstreamer-pbutils-1.0)
BuildRequires: pkgconfig(gtk+-3.0) >= %{gtk3_version}
BuildRequires: pkgconfig(gudev-1.0)
BuildRequires: pkgconfig(json-glib-1.0)
BuildRequires: pkgconfig(libbrasero-media3)
BuildRequires: pkgconfig(libdmapsharing-4.0) >= %{libdmapsharing_version}
%if 0%{?fedora} || 0%{?rhel} >= 9
BuildRequires: pkgconfig(libgpod-1.0)
%endif
BuildRequires: pkgconfig(libmtp)
BuildRequires: pkgconfig(libnotify)
BuildRequires: pkgconfig(libpeas-gtk-1.0)
BuildRequires: pkgconfig(libsecret-1) >= %{libsecret_version}
BuildRequires: pkgconfig(libsoup-2.4) >= 2.42.0
BuildRequires: pkgconfig(libxml-2.0)
BuildRequires: pkgconfig(pygobject-3.0)
BuildRequires: pkgconfig(tdb)
BuildRequires: pkgconfig(totem-plparser) >= 3.2.0
BuildRequires: /usr/bin/desktop-file-validate
BuildRequires: gettext
BuildRequires: intltool
BuildRequires: itstool
BuildRequires: kernel-headers
BuildRequires: libappstream-glib
BuildRequires: meson
BuildRequires: python3-devel
BuildRequires: yelp-tools
BuildRequires: vala

ExcludeArch:    s390 s390x

Requires: gtk3%{?_isa} >= %{gtk3_version}
%if 0%{?fedora} || 0%{?rhel} >= 9
Requires: gvfs-afc
%endif
Requires: libdmapsharing4%{?_isa} >= %{libdmapsharing_version}
Requires: libpeas-loader-python3%{?_isa}
Requires: libsecret%{?_isa} >= %{libsecret_version}
Requires: media-player-info
Requires: python3-gobject
Requires: python3-mako
Requires: gstreamer1-plugins-good
Suggests: zeitgeist-libs%{?_isa}

Obsoletes: rhythmbox-upnp < %{version}-%{release}
Provides: rhythmbox-upnp = %{version}-%{release}
Obsoletes: rhythmbox-lirc < %{version}-%{release}
Provides: rhythmbox-lirc = %{version}-%{release}

%description
Rhythmbox is an integrated music management application based on the powerful
GStreamer media framework. It has a number of features, including an easy to
use music browser, searching and sorting, comprehensive audio format support
through GStreamer, Internet Radio support, playlists and more.

Rhythmbox is extensible through a plugin system.

%package devel
Summary: Development files for Rhythmbox plugins
Requires: %{name}%{?_isa} = %{version}-%{release}

%description devel
This package contains the development files necessary to create
a Rhythmbox plugin.

%prep
%autosetup -p1

%build
%meson \
    -Dlirc=disabled
%meson_build

%install
%meson_install

# Byte-compile Python plugins that are outside the standard Python paths
%py_byte_compile %{__python3} %{buildroot}%{_libdir}/rhythmbox

%find_lang %name --with-gnome

# Don't package api docs
rm -rf %{buildroot}/%{_datadir}/gtk-doc/

# Don't include header files for plugins
rm -rf %{buildroot}%{_libdir}/rhythmbox/plugins/*/*.h

# Context plugin is disabled, so do not install the files.
rm -rf %{buildroot}%{_libdir}/rhythmbox/plugins/context

# Update the screenshot shown in the software center
#
# NOTE: It would be *awesome* if this file was pushed upstream.
#
# See http://people.freedesktop.org/~hughsient/appdata/#screenshots for more details.
#
appstream-util replace-screenshots %{buildroot}%{_metainfodir}/org.gnome.Rhythmbox3.appdata.xml \
  https://raw.githubusercontent.com/hughsie/fedora-appstream/master/screenshots-extra/rhythmbox/a.png \
  https://raw.githubusercontent.com/hughsie/fedora-appstream/master/screenshots-extra/rhythmbox/b.png 

%check
desktop-file-validate %{buildroot}/%{_datadir}/applications/org.gnome.Rhythmbox3*.desktop

%ldconfig_scriptlets

%files -f %{name}.lang
%license COPYING
%doc AUTHORS README NEWS
%{_bindir}/*
%{_datadir}/rhythmbox/
%{_datadir}/applications/org.gnome.Rhythmbox3.desktop
%{_datadir}/applications/org.gnome.Rhythmbox3.device.desktop
%{_datadir}/dbus-1/services/org.gnome.Rhythmbox3.service
%{_datadir}/glib-2.0/schemas/org.gnome.rhythmbox.gschema.xml
%{_datadir}/icons/hicolor/scalable/apps/org.gnome.Rhythmbox3.svg
%{_datadir}/icons/hicolor/scalable/apps/org.gnome.Rhythmbox3-symbolic.svg
%{_metainfodir}/org.gnome.Rhythmbox3.appdata.xml
%{_libdir}/librhythmbox-core.so*
%dir %{_libdir}/rhythmbox
%dir %{_libdir}/rhythmbox/plugins
%{_libdir}/girepository-1.0/*.typelib
%{_libdir}/rhythmbox/plugins/android/
%{_libdir}/rhythmbox/plugins/artsearch/
%{_libdir}/rhythmbox/plugins/audiocd/
%{_libdir}/rhythmbox/plugins/audioscrobbler/
%{_libdir}/rhythmbox/plugins/cd-recorder/
%{_libdir}/rhythmbox/plugins/daap/
%{_libdir}/rhythmbox/plugins/dbus-media-server/
%{_libdir}/rhythmbox/plugins/fmradio/
%{_libdir}/rhythmbox/plugins/generic-player/
%{_libdir}/rhythmbox/plugins/grilo/
%{_libdir}/rhythmbox/plugins/im-status/
%{_libdir}/rhythmbox/plugins/ipod/
%{_libdir}/rhythmbox/plugins/iradio/
%{_libdir}/rhythmbox/plugins/listenbrainz/
%{_libdir}/rhythmbox/plugins/lyrics/
%{_libdir}/rhythmbox/plugins/magnatune/
%{_libdir}/rhythmbox/plugins/mpris/
%{_libdir}/rhythmbox/plugins/mtpdevice/
%{_libdir}/rhythmbox/plugins/notification/
%{_libdir}/rhythmbox/plugins/power-manager/
%{_libdir}/rhythmbox/plugins/python-console/
%{_libdir}/rhythmbox/plugins/rb/
%{_libdir}/rhythmbox/plugins/rbzeitgeist/
%{_libdir}/rhythmbox/plugins/replaygain/
%{_libdir}/rhythmbox/plugins/webremote/
%{_libexecdir}/rhythmbox-metadata
%{_mandir}/man1/rhythmbox*.1*

%files devel
%{_includedir}/rhythmbox/
%{_libdir}/pkgconfig/rhythmbox.pc
%{_datadir}/gir-1.0/*.gir
%{_datadir}/vala/

%changelog
* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 3.4.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed Jun 22 2022 David King <amigadave@amigadave.com> - 3.4.6-1
- Update to 3.4.6 (#2099940)

* Mon May 09 2022 David King <amigadave@amigadave.com> - 3.4.5-3
- Fix translations

* Tue May 03 2022 David King <amigadave@amigadave.com> - 3.4.5-2
- Fix dbus service binary path

* Mon May 02 2022 David King <amigadave@amigadave.com> - 3.4.5-1
- Update to 3.4.5 (#2080798)

* Sun Jan 23 2022 David King <amigadave@amigadave.com> - 3.4.4-12
- Add tdb to pkgconfig dependencies (#2043849)

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 3.4.4-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Dec 22 2021 David King <amigadave@amigadave.com> - 3.4.4-10
- Fix crash with iphone connected (#2032678)

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 3.4.4-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 3.4.4-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Nov 16 2020 Nils Philippsen <nils@tiptoe.de> - 3.4.4-7
- Fix cross-fade playback with GStreamer 1.18+ (#1895139)

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.4.4-6
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.4.4-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Jun 25 2020 Merlin Mathesius <mmathesi@redhat.com> - 3.4.4-4
- Add explicit % py_byte_compile since % _python_bytecompile_extra has been discontinued
  See: https://fedoraproject.org/wiki/Changes/No_more_automagic_Python_bytecompilation_phase_3
- Minor conditional fixes for ELN

* Fri Feb 14 2020 Bastien Nocera <bnocera@redhat.com> - 3.4.4-3
+ rhythmbox-3.4.4-3
- Disable "iPod" support on RHEL, it doesn't work on any modern devices

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.4.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sun Jan 05 2020 David King <amigadave@amigadave.com> - 3.4.4-1
- Update to 3.4.4 (#1787904)

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.4.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 09 2019 Phil Wyett <philwyett@kathenas.org> - 3.4.3-3
- Update library version requirements
- Eliminate some rpm lint warnings

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.4.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sun Jan 06 2019 Kalev Lember <klember@redhat.com> - 3.4.3-1
- Update to 3.4.3

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.4.2-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 3.4.2-8
- Rebuilt for Python 3.7

* Wed Jun 13 2018 Bastien Nocera <bnocera@redhat.com> - 3.4.2-7
+ rhythmbox-3.4.2-7
- Fix warnings in art search when playing a radio (#1317500)
- Fix initial import never finishing
- Fix multimedia keys integration in GNOME (#1567981)

* Thu Jun 07 2018 Bastien Nocera <bnocera@redhat.com> - 3.4.2-6
+ rhythmbox-3.4.2-6
- Add gstreamer1-plugins-good requirement

* Wed Jun 06 2018 Bastien Nocera <bnocera@redhat.com> - 3.4.2-5
+ rhythmbox-3.4.2-5
- Remove LIRC plugin
- Fix 2 build warnings
- Remove BRs for removed visualiser plugin

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.4.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Fri Feb 02 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 3.4.2-3
- Switch to %%ldconfig_scriptlets

* Thu Jan 18 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 3.4.2-2
- Remove obsolete scriptlets

* Mon Oct 09 2017 Kalev Lember <klember@redhat.com> - 3.4.2-1
- Update to 3.4.2

* Thu Aug 10 2017 Kalev Lember <klember@redhat.com> - 3.4.1-6
- Rebuilt for libtotem-plparser soname bump

* Mon Jul 31 2017 Kalev Lember <klember@redhat.com> - 3.4.1-5
- Rebuilt for libtotem-plparser soname bump

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.4.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.4.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Sun Dec 04 2016 David King <amigadave@amigadave.com> - 3.4.1-2
- Bump for libtdb update

* Sun Sep 11 2016 Kalev Lember <klember@redhat.com> - 3.4.1-1
- Update to 3.4.1
- Don't set group tags

* Sun Aug 14 2016 Kalev Lember <klember@redhat.com> - 3.4-1
- Update to 3.4

* Sun Apr 03 2016 David King <amigadave@amigadave.com> - 3.3.1-1
- Update to 3.3.1

* Wed Feb 10 2016 David King <amigadave@amigadave.com> - 3.3-3
- Drop non-functional Zeitgeist plugin (#1062912)
- Update man page glob in files section
- Avoid running configure twice
- Use pkgconfig for BuildRequires
- Use global instead of define
- Update URL

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 3.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Sun Jan 24 2016 Kalev Lember <klember@redhat.com> - 3.3-1
- Update to 3.3

* Fri Jan 08 2016 Michael Catanzaro <mcatanzaro@gnome.org> - 3.2.1-6
- Port to WK2
- Fix LibreFM icon

* Fri Dec 18 2015 Kalev Lember <klember@redhat.com> - 3.2.1-5
- Build with grilo 0.3.0

* Tue Nov 10 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.2.1-4
- Rebuilt for https://fedoraproject.org/wiki/Changes/python3.5

* Sat Jul 04 2015 Kalev Lember <klember@redhat.com> - 3.2.1-3
- Require libpeas-loader-python3 for Python 3 plugin support (#1226879)

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.2.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sun Apr 19 2015 Kalev Lember <kalevlember@gmail.com> - 3.2.1-1
- Update to 3.2.1
- Use license macro for the COPYING file

* Mon Mar 30 2015 Richard Hughes <rhughes@redhat.com> - 3.2-2
- Use better AppData screenshots

* Sun Mar 29 2015 Kalev Lember <kalevlember@gmail.com> - 3.2-1
- Update to 3.2

* Sun Sep 28 2014 Kalev Lember <kalevlember@gmail.com> - 3.1-1
- Update to 3.1
- Tighten subpackage deps

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.0.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Tue Jul 22 2014 Kalev Lember <kalevlember@gmail.com> - 3.0.3-3
- Rebuilt for gobject-introspection 1.41.4

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.0.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun May 25 2014 Kalev Lember <kalevlember@gmail.com> - 3.0.3-1
- Update to 3.0.3

* Fri May 23 2014 Adam Williamson <awilliam@redhat.com> - 3.0.2-4
- backport crash-on-import fix, BGO #724931, RHBZ #1013858

* Wed May 07 2014 Kalev Lember <kalevlember@gmail.com> - 3.0.2-3
- Drop gnome-icon-theme dependency on F21+

* Wed May 07 2014 Kalev Lember <kalevlember@gmail.com> - 3.0.2-2
- Backport upstream fix for the previous issue

* Wed Apr 02 2014 Kalev Lember <kalevlember@gmail.com> - 3.0.2-1.1
- Revert a menu rebuilding optimization that triggers crashes with F20
  gtk3 (#1082543)

* Sun Mar 23 2014 Kalev Lember <kalevlember@gmail.com> - 3.0.2-1
- Update to 3.0.2

* Thu Feb 20 2014 Kalev Lember <kalevlember@gmail.com> - 3.0.1-8
- Rebuilt for cogl soname bump

* Mon Feb 10 2014 Peter Hutterer <peter.hutterer@redhat.com> 3.0.1-7
- FTBFS fix: run autoreconf to deal with new automake

* Mon Feb 10 2014 Peter Hutterer <peter.hutterer@redhat.com> - 3.0.1-6
- Rebuild for libevdev soname bump

* Wed Feb 05 2014 Adam Williamson <awilliam@redhat.com> - 3.0.1-5
- backport upstream fix for crash in libsoup stuff

* Wed Feb 05 2014 Kalev Lember <kalevlember@gmail.com> - 3.0.1-4
- Rebuilt for cogl soname bump

* Mon Dec 30 2013 Adam Williamson <awilliam@redhat.com> - 3.0.1-3
- backport fix for BGO #719514 / RH #1047018 (use_after_deref)

* Thu Dec 26 2013 Adam Williamson <awilliam@redhat.com> - 3.0.1-2
- backport fix for BGO #710493 / RH #1043259 (generate_images_hidden)

* Tue Dec 10 2013 Adam Williamson <awilliam@redhat.com> - 3.0.1-1
- new upstream release 3.0.1

* Thu Sep 19 2013 Kalev Lember <kalevlember@gmail.com> - 3.0-3
- Rebuilt for totem-pl-parser soname bump

* Fri Sep 13 2013 Kalev Lember <kalevlember@gmail.com> - 3.0-2
- Backport a patch to fix music importing when compiled with
  stack-protector-strong

* Tue Sep 10 2013 Kalev Lember <kalevlember@gmail.com> - 3.0-1
- Update to 3.0
- Switch to Python 3

* Fri Aug 09 2013 Kalev Lember <kalevlember@gmail.com> - 2.99.1-3
- Rebuilt for cogl 1.15.4 soname bump

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.99.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Sat Apr 13 2013 Kalev Lember <kalevlember@gmail.com> 2.99.1-1
- Update to 2.99.1

* Sun Apr 07 2013 Kalev Lember <kalevlember@gmail.com> 2.99-1
- Update to 2.99

* Sat Mar 30 2013 Peter Robinson <pbrobinson@fedoraproject.org> 2.98-7
- Add missing files to fix FTBFS

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.98-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Wed Jan 16 2013 Matthias Clasen <mclasen@redhat.com> 2.98-5
- Rebuild

* Wed Oct 17 2012 Kalev Lember <kalevlember@gmail.com> 2.98-4
- Backport a patch to fix a crash with the visualiser plugin enabled

* Thu Oct 11 2012 Kalev Lember <kalevlember@gmail.com> 2.98-3
- Disable the context pane plugin when webkit isn't available

* Wed Oct 10 2012 Kalev Lember <kalevlember@gmail.com> 2.98-2
- Temporarly disable webkit support to prevent mixed gst 0.10 / 1.0 linkage

* Sun Sep 30 2012 Kalev Lember <kalevlember@gmail.com> 2.98-1
- Update to 2.98
- Drop the dep on musicbrainz; rhythmbox now uses an internal library instead

* Thu Aug 30 2012 Tom Callaway <spot@fedoraproject.org> 2.97-5
- rebuild for grilo 0.2.0

* Thu Aug 30 2012 Bastien Nocera <bnocera@redhat.com> 2.97-4
- Port to libmusicbrainz5

* Tue Aug 28 2012 Matthias Clasen <mclasen@redhat.com> 2.97-3
- Rebuild against new cogl/clutter

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.97-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Wed Jun 06 2012 Bastien Nocera <bnocera@redhat.com> 2.97-1
- Update to 2.97

* Tue Apr 24 2012 Kalev Lember <kalevlember@gmail.com> - 2.96-3
- Silence rpm scriptlet output

* Wed Apr 11 2012 Peter Robinson <pbrobinson@fedoraproject.org> - 2.96-2
- Rebuild for new libimobiledevice and usbmuxd

* Tue Mar 13 2012 Cosimo Cecchi <cosimoc@redhat.com> - 2.96-1
- Update to 2.96

* Sat Mar 10 2012 Matthias Clasen <mclasen@redhat.com> - 2.95-5
- Rebuild for new cogl

* Thu Mar  1 2012 Bill Nottingham <notting@redhat.com> - 2.95-4
- Fix python dependencies

* Sun Feb 26 2012 Matthias Clasen <mclasen@redhat.com> - 2.95-3
- Rebuild for new cogl

* Thu Jan 19 2012 Matthias Clasen <mclasen@redhat.com> - 2.95-2
- Rebuild for new cogl

* Tue Jan 17 2012 Cosimo Cecchi <cosimoc@redhat.com> - 2.95-1
- Update to 2.95

* Mon Jan 09 2012 Bastien Nocera <bnocera@redhat.com> 2.90.2-1.git20111104
- Update to 2.90.2

* Thu Nov 24 2011 Matthias Clasen <mclasen@redhat.com> -  2.90.1-20.git20111104
- Rebuild against new clutter

* Fri Nov  4 2011 Adam Williamson <awilliam@redhat.com> - 2.90.1-19.git20111104
- another git snapshot
- magnatune plugin is 'temporarily' disabled upstream

* Fri Oct 14 2011 Adam Williamson <awilliam@redhat.com> - 2.90.1-18.git20111014
- another git snapshot

* Tue Sep 27 2011 Cosimo Cecchi <cosimoc@redhat.com> - 2.90.1-17.git20110927
- Update to a newer git snapshot
- Include the new Grilo-based plugin, obsoletes the UPNP and Jamendo plugins

* Tue Sep 20 2011 Matthias Clasen <mclasen@redhat.com> - 2.90.1-16.git20110829
- Rebuild against newer clutter

* Mon Aug 29 2011 Adam Williamson <awilliam@redhat.com> - 2.90.1-15.git20110829
- update to a newer git snapshot to fix another crasher
- rebuild against new libpeas to make plugins work again (rh #732855)

* Tue Aug 23 2011 Adam Williamson <awilliam@redhat.com> - 2.90.1-14.git20110823
- update to a newer git snapshot again to fix a crasher

* Mon Aug 22 2011 Adam Williamson <awilliam@redhat.com> - 2.90.1-13.git20110822
- update to a newer git snapshot
- adjust BRs
    + libgnome-media-profiles is no longer needed (not used
      upstream), but it implied gconf2-devel, so add that
    + add clutter-gst, clutter-gtk and libmx for the vis plugin
    + bump version of libdmapsharing required
- package the visualizer plugin

* Sat Jul 16 2011 Cosimo Cecchi <cosimoc@redhat.com> - 2.90.1-12.git20110716
- Update to a newer git snapshot

* Sat Jun 18 2011 Michael Schwendt <mschwendt@fedoraproject.org> - 2.90.1-11.git20110502
- Rebuild for libmtp SONAME change.

* Wed May 25 2011 Dan Williams <dcbw@redhat.com> - 2.90.1-10.git20110502
- Fix crash handling dates (rh #699290)

* Mon May 02 2011 Cosimo Cecchi <cosimoc@redhat.com> - 2.90.1-9.git20110502
- Update to a newer git snapshot

* Thu Apr 14 2011 Cosimo Cecchi <cosimoc@redhat.com> - 2.90.1-8.git20110414
- Update to a newer git snapshot

* Tue Mar 29 2011 Cosimo Cecchi <cosimoc@redhat.com> - 2.90.1-7.git20110329
- Update to a newer git snapshot, should hopefully fix cover art.

* Mon Mar 28 2011 Cosimo Cecchi <cosimoc@redhat.com> - 2.90.1-6.git20110328
- Update to a newer git snapshot

* Wed Mar 16 2011 Cosimo Cecchi <cosimoc@redhat.com> - 2.90.1-5.git20110316
- Update to a newer git snapshot

* Fri Feb 11 2011 Matthias Clasen <mclasen@redhat.com>
- Rebuild against newer gtk

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.90.1-3.git20110207
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Tue Feb  8 2011 Cosimo Cecchi <cosimoc@redhat.com> - 2.91.0-2.git20110207
- Re-enable DAAP sharing plugin now that we have a newer libdmapsharing
- Add WebKitGTK 3 to build requires

* Mon Feb  7 2011 Cosimo Cecchi <cosimoc@redhat.com> - 2.91.0-1.git20110207
- Update to a 2.91.0 git snapshot
- Disable DAAP sharing plugin, as it requires a newer libdmapsharing
- Depend on gtk3

* Wed Feb  2 2011 Matthias Clasen <mclasen@Redhat.com>  0.13.3-3
- Rebuild against newer gtk

* Tue Jan 25 2011 Matthias Clasen <mclasen@Redhat.com>  0.13.3-2
- Just require gnome-icon-theme-legacy for icons

* Sun Jan 16 2011 Matthias Clasen <mclasen@Redhat.com>  0.13.3-1
- Update to 0.13.3

* Tue Jan 11 2011 Adam Williamson <awilliam@redhat.com> 0.13.2-4
- replace Matthias' incomplete patch for libgnome-media-profiles
  with upstream commit dae77ce5437884bec29c90d5ae303816abc18434
  (from gobject-introspection branch), rediffed (configure.ac)

* Mon Jan 10 2011 Matthias Clasen <mclasen@redhat.com> 0.13.2-3
- Rebuild against newer gtk

* Tue Nov  2 2010 Matthias Clasen <mclasen@redhat.com> 0.13.2-2
- Build against libnotify 0.7.0

* Mon Nov 01 2010 Bastien Nocera <bnocera@redhat.com> 0.13.2-1
- Update to 0.13.2

* Tue Sep 07 2010 Bastien Nocera <bnocera@redhat.com> 0.13.1-1
- Update to 0.13.1

* Wed Aug 25 2010 Jochen Schmitt <Jochen herr-schmitt de> - 0.13.0-6
- Rebuild to fix broken deps

* Wed Aug 11 2010 Matthias Clasen <mclasen@redhat.com> - 0.13.0-5
- Rebuild against newer brasero

* Tue Jul 27 2010 David Malcolm <dmalcolm@redhat.com> - 0.13.0-4
- Rebuilt for https://fedoraproject.org/wiki/Features/Python_2.7/MassRebuild

* Mon Jul 19 2010 Bastien Nocera <bnocera@redhat.com> 0.13.0-3
- Recompile against gnome-media with GTK+ 3.x support, even
  if it will break run-time

* Thu Jul 15 2010 Matthias Clasen <mclasen@redhat.com> - 0.13.0-2
- Rebuild against new brasero, drop brasero-media dep temporarily

* Sat Jul  3 2010 Matthias Clasen <mclasen@redhat.com> - 0.13.0-1
- Update to 0.13.0

* Mon Jun 28 2010 Bastien Nocera <bnocera@redhat.com> 0.12.90-2
- Fix pkgconfig requires (not pkg-config!)

* Fri Jun 25 2010 Bastien Nocera <bnocera@redhat.com> 0.12.90-1
- Update to 0.12.90

* Fri Jun 11 2010 Matthias Clasen <mclasen@redhatcom> 0.12.8-5
- Rebuild against new brasero

* Tue Jun 01 2010 Bastien Nocera <bnocera@redhat.com> 0.12.8-4
- Another pass at removing HAL deps

* Wed Apr 07 2010 Bastien Nocera <bnocera@redhat.com> 0.12.8-3
- Require gnome-icon-theme-extras for device icon goodness

* Mon Mar 29 2010 Bastien Nocera <bnocera@redhat.com> 0.12.8-2
- Update to 0.12.8
- Rebuild with a changelog

* Mon Mar 22 2010 Bastien Nocera <bnocera@redhat.com> 0.12.7-5
- Fix iPhones and iPod Touches being handled by the MTP plugin

* Mon Mar 15 2010 Bastien Nocera <bnocera@redhat.com> 0.12.7-4
- Fix assertion in rhythmdb_property_model_delete_prop() (#540065)

* Thu Mar 11 2010 Bastien Nocera <bnocera@redhat.com> 0.12.7-3
- Really remove HAL dependency
- Require gvfs-afc for iPhone support

* Wed Mar  3 2010 Matthias Clasen <mclasen@redhat.com> 0.12.7-2
- Add a missing icon back

* Mon Mar 01 2010 Bastien Nocera <bnocera@redhat.com> 0.12.7-1
- Update to 0.12.7

* Sun Feb 21 2010 Bastien Nocera <bnocera@redhat.com> 0.12.6.91-1
- Update to 0.12.6.91

* Tue Feb 09 2010 Bastien Nocera <bnocera@redhat.com> 0.12.6-8
- Fix crasher on startup when the MTP device could not be
  opened (#563195)

* Tue Jan 26 2010 Bastien Nocera <bnocera@redhat.com> 0.12.6-7
- Rebuild for new totem-pl-parser

* Wed Jan 06 2010 Bastien Nocera <bnocera@redhat.com> 0.12.6-6
- Add patches from F-12

* Tue Dec 15 2009 Matthias Clasen <mclasen@redhat.com> 0.12.6-5
- Don't include header files for plugins

* Thu Dec 10 2009 Bastien Nocera <bnocera@redhat.com> 0.12.6-4
- Fix crasher when musicbrainz cannot read a disc (#546188)

* Thu Dec 10 2009 Bastien Nocera <bnocera@redhat.com> 0.12.6-3
- Fix crasher in WebKit when using the context pane (#540672)

* Mon Dec 07 2009 Bastien Nocera <bnocera@redhat.com> 0.12.6-2
- Remove libhal requirement

* Sun Nov 22 2009 Bastien Nocera <bnocera@redhat.com> 0.12.6-1
- Update to 0.12.6

* Wed Nov 18 2009 Bastien Nocera <bnocera@redhat.com> 0.12.5.91-1
- Update to 0.12.5.91

* Tue Nov 03 2009 Bastien Nocera <bnocera@redhat.com> 0.12.5-8
- Fix brasero project generation

* Mon Oct 19 2009 Bastien Nocera <bnocera@redhat.com> 0.12.5-7
- Use bicubic volumes in the UI

* Fri Oct 16 2009 Bastien Nocera <bnocera@redhat.com> 0.12.5-6
- Avoid using HEAD to get podcast mime-types

* Tue Oct 13 2009 Bastien Nocera <bnocera@redhat.com> 0.12.5-5
- Fix DAAP plugin not working

* Wed Sep 30 2009 Bastien Nocera <bnocera@redhat.com> 0.12.5-4
- Enable the FM radio plugin

* Mon Sep 28 2009 Bastien Nocera <bnocera@redhat.com> 0.12.5-3
- Fix the symbols for the browser plugin being mangled (#525826)

* Mon Sep 28 2009 Richard Hughes  <rhughes@redhat.com> - 0.12.5-2
- Apply a patch from upstream to inhibit gnome-session, rather than
  gnome-power-manager. This fixes a warning on rawhide.

* Fri Sep 18 2009 Bastien Nocera <bnocera@redhat.com> 0.12.5-1
- Update to 0.12.5

* Wed Sep 02 2009 Bastien Nocera <bnocera@redhat.com> 0.12.4-3
- Add upstream patch to use the correct path for mpi files

* Tue Sep 01 2009 Bastien Nocera <bnocera@redhat.com> 0.12.4-2
- Remove obsolete configure flags
- Add libgudev BR
- Add media-player-info requires (note, not built yet)

* Tue Sep 01 2009 Bastien Nocera <bnocera@redhat.com> 0.12.4-1
- Update to 0.12.4

* Sat Aug 22 2009 Matthias Clasen <mclasen@redhat.com> - 0.12.3-5
- Respect the button-images setting better

* Wed Aug 19 2009 Matthias Clasen <mclasen@redhat.com> - 0.12.3-4
- Use the right spinner icon

* Wed Aug 19 2009 Bastien Nocera <bnocera@redhat.com> 0.12.3-3
- Fix audio CD activation (#517685)

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.12.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Thu Jul 09 2009 Bastien Nocera <bnocera@redhat.com> 0.12.3-1
- Udpate to 0.12.3

* Wed Jul 01 2009 Bastien Nocera <bnocera@redhat.com> 0.12.2.93-1
- Update to 0.12.2.93

* Tue Jun 30 2009 Bastien Nocera <bnocera@redhat.com> 0.12.2.92-1
- Update to 0.12.2.92

* Mon Jun 29 2009 Bastien Nocera <bnocera@redhat.com> 0.12.2.91-1
- Update to 0.12.2.91

* Thu Jun 04 2009 Bastien Nocera <bnocera@redhat.com> 0.12.2-1
- Update to 0.12.2

* Thu May 07 2009 Bastien Nocera <bnocera@redhat.com> 0.12.1-3
- Add patch for sound-juicer changes

* Wed Apr 29 2009 - Matthias Clasen <mclasen@redhat.com> - 0.12.1-2
- Update WKNC urls (#498258)

* Tue Apr 28 2009 - Bastien Nocera <bnocera@redhat.com> - 0.12.1-1
- Update to 0.12.1

* Wed Apr 22 2009 - Bastien Nocera <bnocera@redhat.com> - 0.12.0.92-1
- Update to 0.12.0.92

* Tue Apr 14 2009 - Bastien Nocera <bnocera@redhat.com> - 0.12.0-5
- Fix possible crashers in the libmusicbrainz3 code

* Thu Apr 09 2009 - Bastien Nocera <bnocera@redhat.com> - 0.12.0-4
- Fix iPod detection with the DeviceKit-disks gvfs monitor (#493640)

* Wed Mar 25 2009 - Bastien Nocera <bnocera@redhat.com> - 0.12.0-3
- Fix crasher in the PSP and Nokia plugins

* Tue Mar 24 2009 - Bastien Nocera <bnocera@redhat.com> - 0.12.0-2
- Add patch to use decodebin2 instead of decodebin and fix
  playback problems with chained ogg streams (#446283)

* Thu Mar 19 2009 - Bastien Nocera <bnocera@redhat.com> - 0.12.0-1
- Update to 0.12.0

* Wed Mar 18 2009 - Bastien Nocera <bnocera@redhat.com> - 0.11.99.3-1
- Update to 0.11.99.3 pre-release

* Tue Mar 17 2009 - Bastien Nocera <bnocera@redhat.com> - 0.11.99.2-1
- Update to 0.11.99.2 pre-release

* Fri Mar 13 2009 - Bastien Nocera <bnocera@redhat.com> - 0.11.99.1-1
- Update to 0.11.99.1 pre-release

* Thu Mar 12 2009 - Bastien Nocera <bnocera@redhat.com> - 0.11.99-1
- Update to 0.11.99 pre-release

* Mon Mar 09 2009 - Bastien Nocera <bnocera@redhat.com> - 0.11.6-30.r6184
- Update to r6184
- Change default burner plugin to brasero

* Wed Mar 04 2009 - Bastien Nocera <bnocera@redhat.com> - 0.11.6-29.r6176
- Update to r6176
- Drop upstreamed patches

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.11.6-28.r6096
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Fri Feb 20 2009 Todd Zullinger <tmz@pobox.com> - 0.11.6-27.r6096
- Rebuild against libgpod-0.7.0

* Thu Feb 19 2009 - Bastien Nocera <bnocera@redhat.com> - 0.11.6-26.r6096
- libmusicbrainz is gone

* Tue Feb 17 2009 - Bastien Nocera <bnocera@redhat.com> - 0.11.6-25.r6096
- Add patch to set the PulseAudio properties

* Fri Feb 13 2009 - Bastien Nocera <bnocera@redhat.com> - 0.11.6-24.r6096
- Use the pulsesink's volume instead of our own one
- Fix crasher when musicbrainz3 doesn't get a match for an audio CD (#481441)

* Tue Jan 20 2009 - Bastien Nocera <bnocera@redhat.com> - 0.11.6-23.r6096
- Fix UPNP plugin for use with external Louie (#480036)

* Mon Jan 19 2009 Brian Pepple <bpepple@fedoraproject.org> - 0.11.6-22.r6096
- Backport patch to fix avahi assertion in DAAP plugin.

* Tue Jan 13 2009 - Bastien Nocera <bnocera@redhat.com> - 0.11.6-21.r6096
- Add more Python deps for the UPNP plugin (#474372)
- Require gstreamer-python-devel, as it's been split from gstreamer-python

* Mon Jan 05 2009 - Bastien Nocera <bnocera@redhat.com> - 0.11.6-20.r6096
- Don't ship our own iradio playlist, the changes are already upstream

* Tue Dec 09 2008 - Bastien Nocera <bnocera@redhat.com> - 0.11.6-19.r6096
- Update to rev 6096
- Fixes some crashers during playback

* Tue Dec 02 2008 - Bastien Nocera <bnocera@redhat.com> - 0.11.6-18-r6086
- Update to rev 6086
- Add libmusicbrainz3 support

* Sun Nov 30 2008 Ignacio Vazquez-Abrams <ivazqueznet+rpm@gmail.com> - 0.11.6-17.r6005
- Rebuild for Python 2.6

* Sat Nov 22 2008 Matthias Clasen <mclasen@redhat.com>
- Better URL
- Tweak description

* Thu Oct 30 2008 - Bastien Nocera <bnocera@redhat.com> - 0.11.6-15.r6005
- Update to rev 6005
- Fixes typo in the LIRC config
- Force GConf library location to be a URI on startup

* Mon Oct 27 2008 - Bastien Nocera <bnocera@redhat.com> - 0.11.6-15.r6002
- Update to rev 6002

* Mon Oct 20 2008 - Bastien Nocera <bnocera@redhat.com> - 0.11.6-14.r5988
- Update to rev 5988, add patch to avoid duplicate tracks on iPods

* Wed Oct  8 2008 Matthias Clasen  <mclasen@redhat.com> - 0.11.6-13.r5966
- Save some space

* Fri Oct 03 2008 - Bastien Nocera <bnocera@redhat.com> - 0.11.6-12.r5966
- Update to latest trunk
- Fix license info to match that of upstream

* Wed Oct 01 2008 - Bastien Nocera <bnocera@redhat.com> - 0.11.6-11.r5957
- Update source name

* Wed Oct 01 2008 - Bastien Nocera <bnocera@redhat.com> - 0.11.6-10.r5957
- Update to latest trunk
- Fixes lirc plugin never finishing loading

* Wed Oct 01 2008 - Bastien Nocera <bnocera@redhat.com> - 0.11.6-9.r5956
- Update release version

* Wed Oct 01 2008 - Bastien Nocera <bnocera@redhat.com> 0.11.6-r5956
- Update to latest trunk version, with GIO support and very many
  bug fixes
- Remove obsoleted patches, autotools and xulrunner-devel BRs

* Wed Sep  3 2008 Tom "spot" Callaway <tcallawa@redhat.com> 0.11.6-8
- fix license tag

* Mon Sep 01 2008 - Bastien Nocera <bnocera@redhat.com> 0.11.6-7
- Add wbur.org to the default playlist (#446791)

* Sat Aug 23 2008 - Linus Walleij <triad@df.lth.se> 0.11.6-6
- Rebuild package to pick up libmtp 0.3.0 deps

* Thu Aug 14 2008 - Bastien Nocera <bnocera@redhat.com> 0.11.6-5
- Add a default LIRC configuration, so it works out-of-the-box

* Tue Aug 12 2008 - Bastien Nocera <bnocera@redhat.com> 0.11.6-4
- Add patch for libmtp 0.3 support (#458388)

* Sat Jul 26 2008 Matthias Clasen  <mclasen@redhat.com> 0.11.6-3
- Use standard icon names in a few places

* Sun Jul 20 2008 Adam Jackson <ajax@redhat.com> 0.11.6-2
- rhythmbox-0.11.5-xfade-buffering.patch: Backport from svn to fix playback
  start when the crossfader is active.

* Mon Jul 14 2008 - Bastien Nocera <bnocera@redhat.com> - 0.11.6-1
- Update to 0.11.6
- Remove loads of upstreamed patches

* Mon Jun 16 2008 - Bastien Nocera <bnocera@redhat.com> - 0.11.5-15
- Avoid crash on new iPods (#451547)

* Wed May 14 2008 - Matthias Clasen <mclasen@redhat.com> - 0.11.5-14
- Rebuild again 

* Tue May 13 2008 - Bastien Nocera <bnocera@redhat.com> - 0.11.5-13
- Rebuild

* Wed May 07 2008 - Bastien Nocera <bnocera@redhat.com> - 0.11.5-12
- Prefer Ogg previews for Magnatune

* Thu Apr 17 2008 Matthias Clasen <mclasen@redhat.com> - 0.11.5-11
- Drop big ChangeLog file

* Fri Apr 11 2008 - Bastien Nocera <bnocera@redhat.com> - 0.11.5-10
- Add patch to use the new Amazon search, the old one was shutdown

* Tue Apr 08 2008 - Bastien Nocera <bnocera@redhat.com> - 0.11.5-9
- Update deadlock fix patch

* Mon Apr 07 2008 - Bastien Nocera <bnocera@redhat.com> - 0.11.5-8
- Add patch to avoid deadlocks when playing music through the cross-fade backend

* Fri Apr 04 2008 - Bastien Nocera <bnocera@redhat.com> - 0.11.5-7
- Add patch to work-around transfer of some filenames to VFAT iPods (#440668)

* Fri Apr 04 2008 - Bastien Nocera <bnocera@redhat.com> - 0.11.5-6
- Add patch to fix CDDA autostart from nautilus (#440489)

* Mon Mar 31 2008 - Bastien Nocera <bnocera@redhat.com> - 0.11.5-5
- Force podcast parsing, as we already know it's a Podcast

* Mon Mar 31 2008 - Bastien Nocera <bnocera@redhat.com> - 0.11.5-4
- Add a 24x24 icon so it doesn't look blurry in the panel

* Thu Mar 20 2008 - Bastien Nocera <bnocera@redhat.com> - 0.11.5-3
- Patch from upstream to fix URL encoding, as soup_encode_uri()
  doesn't encode in place anymore, should fix track submission
  with last.fm

* Mon Mar 17 2008 - Bastien Nocera <bnocera@redhat.com> - 0.11.5-2
- Fix possible crasher in playlist activation

* Mon Mar 17 2008 - Bastien Nocera <bnocera@redhat.com> - 0.11.5-1
- Update to 0.11.5
- Remove outdated patches

* Thu Mar 13 2008 - Bastien Nocera <bnocera@redhat.com> - 0.11.4-13
- Big update of the UPNP plugin, with MediaRenderer support
- Add patch to make the pane window bigger by default (#437066)

* Wed Mar 12 2008 - Bastien Nocera <bnocera@redhat.com> - 0.11.4-12
- Remove ExcludeArch for ppc/ppc64

* Tue Mar 04 2008 - Bastien Nocera <bnocera@redhat.com> - 0.11.4-11
- Add patch to save the album artwork onto the iPod (#435952)

* Mon Mar 03 2008 - Bastien Nocera <bnocera@redhat.com> - 0.11.4-10
- Add a patch to fix activating audio players with a directory instead
  of a device path (GNOME bug #519737)

* Mon Feb 18 2008 Matthias Clasen <mclasen@redhat.com> - 0.11.4-9
- Fix the media player patch to work

* Thu Feb 14 2008 Matthias Clasen <mclasen@redhat.com> - 0.11.4-8
- Rebuild against new libsoup

* Tue Feb 05 2008 - Bastien Nocera <bnocera@redhat.com> - 0.11.4-7
- Update libsoup 2.4 patch again from upstream

* Mon Feb 04 2008 - Bastien Nocera <bnocera@redhat.com> - 0.11.4-6
- Update libsoup 2.4 patch from upstream
- Add patch to fix the media player keys API usage

* Tue Jan 29 2008  Matthias Clasen <mclasen@redhat.com> - 0.11.4-5
- Port to libsoup 2.4

* Fri Jan 18 2008  Matthias Clasen <mclasen@redhat.com> - 0.11.4-4
- Add content-type support

* Thu Jan 17 2008 - Bastien Nocera <bnocera@redhat.com> - 0.11.4-3
- Own the plugins dir (#389111)

* Wed Jan 09 2008 - Bastien Nocera <bnocera@redhat.com> - 0.11.4-2
- Add patch to make the power manager plugin disablable (#428034)

* Fri Dec 21 2007 Matthias Clasen <mclasen@redhat.com> - 0.11.4-1
- Update to 0.11.4

* Fri Dec 07 2007 - Bastien Nocera <bnocera@redhat.com> - 0.11.3-9
- Add patch to fix possible crasher when playing any song (#410991)

* Fri Nov 30 2007 - Bastien Nocera <bnocera@redhat.com> - 0.11.3-8
- Update patch for the Podcast parsing to include the browser plugin
  for the iTunes detection

* Fri Nov 30 2007 - Bastien Nocera <bnocera@redhat.com> - 0.11.3-7
- Add patch to avoid crashing if no Python plugins are enabled by default
  (#393531)

* Thu Nov 29 2007 - Bastien Nocera <bnocera@redhat.com> - 0.11.3-6
- Remove stupid return that caused Podcasts never to be updated
  (see http://bugzilla.gnome.org/show_bug.cgi?id=500325)

* Wed Nov 21 2007 Todd Zullinger <tmz@pobox.com> - 0.11.3-5
- Rebuild against libgpod-0.6.0

* Sat Nov 17 2007 - Bastien Nocera <bnocera@redhat.com> - 0.11.3-4
- Better DAAP fix (#382351)

* Wed Nov 14 2007 - Bastien Nocera <bnocera@redhat.com> - 0.11.3-3
- Add missing gstreamer-python run-time dependency (#382921)

* Tue Nov 13 2007 - Bastien Nocera <bnocera@redhat.com> - 0.11.3-2
- Add upstream patch to implement missing plugins support

* Mon Nov 12 2007 - Bastien Nocera <bnocera@redhat.com> - 0.11.3-1
- Update to 0.11.3
- Remove a whole load of upstreamed patches

* Sat Nov 10 2007 Matthias Clasen <mclasen@redhat.com> - 0.11.2-14
- Rebuild against newer libmtp

* Wed Oct 31 2007 - Bastien Nocera <bnocera@redhat.com> - 0.11.2-13
- Rebuild for new totem

* Mon Oct 29 2007 - Bastien Nocera <bnocera@redhat.com> - 0.11.2-12
- Update patch for #242260, tooltips weren't working
- Add patch to fix problems importing files with spaces in them (#291571)
- Add patch to remove iPod tracks when removed, rather than put them
  in the trash (#330101)
- Add upstream patch to support new playlist parser in Totem, and add
  better Podcast support, as well as iTunes podcast support

* Mon Oct 22 2007  Matthias Clasen <mclasen@redhat.com> - 0.11.2-11
- Rebuild against new dbus-glib

* Thu Oct 11 2007 - Bastien Nocera <bnocera@redhat.com> - 0.11.2-10
- Add patch to avoid Rhythmbox escaping the primary text in notifications
  as per the spec (#242260)

* Wed Oct 10 2007 - Bastien Nocera <bnocera@redhat.com> - 0.11.2-9
- Add the plugin to handle MTP devices (#264541)

* Tue Oct 09 2007 - Bastien Nocera <bnocera@redhat.com> - 0.11.2-8
- Add patch to make the gnome-power-manager plugin work again
  (GNOME #483721)

* Tue Oct 02 2007 - Bastien Nocera <bnocera@redhat.com> - 0.11.2-7
- Add upstream patch to make the Upnp media store work (GNOME #482548)

* Thu Sep 20 2007 - Bastien Nocera <bnocera@redhat.com> - 0.11.2-6
- Init pygobject threads early (GNOME #469852)

* Fri Aug 24 2007 Todd Zullinger <tmz@pobox.com> - 0.11.2-5
- Rebuild against new libgpod

* Thu Aug 23 2007 - Bastien Nocera <bnocera@redhat.com> - 0.11.2-4
- Rebuild with PPC-enabled, now that liboil is "fixed"

* Mon Aug 20 2007 - Bastien Nocera <bnocera@redhat.com> - 0.11.2-3
- Own some directories of ours (#246156)

* Mon Aug 20 2007 - Bastien Nocera <bnocera@redhat.com> - 0.11.2-2
- Disable PPC for now
- Add the LIRC plugin (#237269)
- Add Coherence UPNP plugin

* Wed Aug 15 2007 Matthias Clasen <mclasen@redhat.com> - 0.11.2-1
- Update to 0.11.2

* Tue Aug  7 2007 Matthias Clasen <mclasen@redhat.com> - 0.11.1-2
- Update the license field
- Use %%find_lang for help files

* Wed Jun 27 2007 - Bastien Nocera <bnocera@redhat.com> - 0.11.1-1
- Update to 0.11.1
- Drop obsolete patches
- Work-around a possible buggy GStreamer plugin

* Mon Jun 04 2007 - Bastien Nocera <bnocera@redhat.com> - 0.11.0-5
- Add patch to not ignore tags with trailing white spaces

* Tue May 29 2007 - Bastien Nocera <bnocera@redhat.com> - 0.11.0-4
- Update totem playlist parser requirements

* Tue May 29 2007 - Bastien Nocera <bnocera@redhat.com> - 0.11.0-3
- Use the store resize patch for 0.11.x rather than the one for 0.10.x

* Tue May 29 2007 - Bastien Nocera <bnocera@redhat.com> - 0.11.0-2
- Re-add the store resize patch, as it's not upstream

* Mon May 28 2007 Matthias Clasen <mclasen@redhat.com> - 0.11.0-1
- Update to 0.11.0
- Drop upstreamed patches

* Sun May 20 2007 Matthias Clasen <mclasen@redhat.com> - 0.10.0-9
- Rebuild against new totem-plparser

* Tue May 08 2007 - Bastien Nocera <bnocera@redhat.com> - 0.10.0-8.fc7
- Add patch to avoid the window resizing when loading the stores
  (#236972)

* Mon Apr 30 2007 - Bastien Nocera <bnocera@redhat.com> - 0.10.0-7.fc7
- Add missing gnome-python2-gconf and gnome-python2-gnomevfs deps
  (#238363)

* Fri Apr 20 2007 - Bastien Nocera <bnocera@redhat.com> - 0.10.0-6.fc7
- Enable the Magnatune and Jamendo stores by default (#237131)

* Wed Apr 18 2007 - Bastien Nocera <bnocera@redhat.com> - 0.10.0-5.fc7
- Set the first time flag on startup, otherwise the iRadio's initial
  playlist is never loaded (Gnoem BZ #431167)

* Wed Apr 11 2007 - Bastien Nocera <bnocera@redhat.com> - 0.10.0-4.fc7
- Provide some quality Ogg radios in the default iRadio catalogue
  (#229677)

* Wed Apr 11 2007 - Bastien Nocera <bnocera@redhat.com> - 0.10.0-3.fc7
- Add requires for gnome-themes, spotted by Nigel Jones (#235818)

* Wed Apr 04 2007 - Bastien Nocera <bnocera@redhat.com> - 0.10.0-2.fc7
- Use multiple CPUs to build, the upstream bug is fixed now

* Wed Apr 04 2007 - Bastien Nocera <bnocera@redhat.com> - 0.10.0-1.fc7
- Update to the stable branch 0.10.0, fixes a large number of crashers
- Add patch for xdg-user-dirs support

* Wed Mar 28 2007 - Bastien Nocera <bnocera@redhat.com> - 0.9.8-4.fc7
- Add upstream patch for bug 234216

* Sun Mar 25 2007  Matthias Clasen <mclasen@redhat.com> - 0.9.8-3
- Fix a directory ownership issue (#233911)

* Thu Mar 15 2007 - Bastien Nocera <bnocera@redhat.com> - 0.9.8-2.fc7
- Add missing dependency on gnome-python2 for the Python gnome-vfs
 bindings (#232189)

* Wed Feb 21 2007 - Bastien Nocera <bnocera@redhat.com> - 0.9.8-1.fc7
- Update to 0.9.8, drop unneeded requirements and patches
- Change iradio default stations location
- Add new rhythmbox-core library

* Wed Jan 31 2007 - Bastien Nocera <bnocera@redhat.com> - 0.9.7-11.fc7
- Require automake in the BuildRequires as well, as we need to generate
  plugins/mmkeys/Makefile.in

* Wed Jan 31 2007 - Bastien Nocera <bnocera@redhat.com> - 0.9.7-10.fc7
- Require autoconf in the BuildRequires, as it's not in the minimum build
  environment

* Wed Jan 31 2007 - Bastien Nocera <bnocera@redhat.com> - 0.9.7-9.fc7
- Exclude s390* from the builds, as there's no gnome-media there

* Wed Jan 31 2007 - Bastien Nocera <bnocera@redhat.com> - 0.9.7-8.fc7
- Add patch to make the multimedia keys work with the new control-center
  way of doing things (#197540)

* Mon Jan 22 2007 Alexander Larsson <alexl@redhat.com> - 0.9.7-7.fc7
- Specfile cleanups from Todd Zullinger
- Buildrequire gnome-media-devel for gnome-media-profiles.pc
- Remove explicit libgpod dep
- install missing artwork image (Gnome BZ #387413)

* Tue Jan 16 2007 Alexander Larsson <alexl@redhat.com> - 0.9.7-6.fc7
- rebuild with new libgpod

* Tue Dec 19 2006 Matthias Clasen <mclasen@redhat.com> - 0.9.7-5
- Update to 0.9.7

* Thu Dec  7 2006 Jeremy Katz <katzj@redhat.com> - 0.9.6-4
- rebuild for python 2.5

* Tue Nov 21 2006 Ray Strode <rstrode@redhat.com> - 0.9.6-3
- drop keybinding patch

* Mon Nov 13 2006 Matthias Clasen <mclasen@redhat.com> - 0.9.6-2
- Rebuild

* Sun Oct 22 2006 Matthias Clasen <mclasen@redhat.com> - 0.9.6-1
- Update to 0.9.6

* Mon Oct 2 2006 Ray Strode <rstrode@redhat.com> - 0.9.5-6.fc6
- first unfinished, buggy crack at fixing keybindings

* Mon Sep 18 2006 John (J5) Palmieri <johnp@redhat.com> - 0.9.5-5
- Enable tag editing

* Wed Sep 13 2006 Matthias Clasen <mclasen@redhat.com> - 0.9.5-4
- Fix a crash when a radio station is missing  (#206170)

* Thu Sep  7 2006 Matthias Clasen <mclasen@redhat.com> - 0.9.5-3
- Support transparent panels (#205584)

* Wed Jul 19 2006 John (J5) Palmieri <johnp@redhat.com> - 0.9.5-2
- Add BR for dbus-glib-devel 
- Add patch to fix deprecated dbus function

* Wed Jul 12 2006 Jesse Keating <jkeating@redhat.com> - 0.9.5-1.1
- rebuild

* Fri Jul  7 2006 Bill Nottingham <notting@redhat.com>
- don't require eel2

* Mon Jun 19 2006 Matthias Clasen <mclasen@redhat.com> - 0.9.5-1
- Update to 0.9.5

* Wed Jun 14 2006 Bill Nottingham <notting@redhat.com> - 0.9.4.1-8
- apply patch from CVS to port to nautilus-cd-burner 2.15.3

* Wed Jun 14 2006 Matthias Clasen <mclasen@redhat.com> - 0.9.4.1-7
- Rebuild

* Fri May 26 2006 Jeremy Katz <katzj@redhat.com> - 0.9.4.1-6
- try to fix building on s390{,x}

* Wed May 24 2006 John (J5) Palmieri <johnp@redhat.com> - 0.9.4.1-5
- Patch to build with latest libnotify

* Mon May 22 2006 Matthias Clasen <mclasen@redhat.com> - 0.9.4.1-4
- Rebuild

* Sun May 21 2006 Matthias Clasen <mclasen@redhat.com> - 0.9.4.1-3
- Add missing BuildRequires (#129145)

* Tue Apr 25 2006 Matthias Clasen <mclasen@redhat.com> - 0.9.4.1-2
- Update to 0.9.4.1

* Mon Apr 17 2006 Matthias Clasen <mclasen@redhat.com> - 0.9.4-2
- Update to 0.9.4
- Drop upstreamed patches

* Wed Mar 08 2006 Ray Strode <rstrode@redhat.com> - 0.9.3.1-3
- fix icon on notification bubbles (bug 183720)
- patch from CVS to escape bubble markup, found by 
  Bill Nottingham

* Fri Mar 03 2006 Ray Strode <rstrode@redhat.com> - 0.9.3.1-2
- add patch from James "Doc" Livingston to stop a hang
  for new users (bug 183883)

* Fri Feb 10 2006 Jesse Keating <jkeating@redhat.com> - 0.9.3.1-1.2
- bump again for double-long bug on ppc(64)

* Tue Feb 07 2006 Jesse Keating <jkeating@redhat.com> - 0.9.3.1-1.1
- rebuilt for new gcc4.1 snapshot and glibc changes

* Sat Feb  4 2006 Christopher Aillon <caillon@redhat.com> 0.9.3.1-1
- Update to 0.9.3.1
- Use gstreamer (0.10)

* Wed Feb  1 2006 Christopher Aillon <caillon@redhat.com> 0.9.3-2
- Remove hack for 173869, as its no longer needed.

* Wed Feb  1 2006 Christopher Aillon <caillon@redhat.com> 0.9.3-1
- 0.9.3

* Wed Feb  1 2006 Christopher Aillon <caillon@redhat.com> 0.9.2.cvs20060201-1
- Newer CVS snapshot

* Sun Jan 22 2006 Christopher Aillon <caillon@redhat.com> 0.9.2.cvs20060123-1
- Update to latest CVS
- Add hack to workaround bug #173869

* Thu Jan 19 2006 Christopher Aillon <caillon@redhat.com> 0.9.2-8
- Rebuild, now that gstreamer08-plugins has been fixed

* Thu Jan 19 2006 Ray Strode <rstrode@redhat.com> 0.9.2-7
- bonobo multilib issue (bug 156982)

* Wed Jan 04 2006 John (J5) Palmieri <johnp@redhat.com> 0.9.2-5
- rebuild with ipod support

* Tue Jan 03 2006 Jesse Keating <jkeating@redhat.com> 0.9.2-4
- rebuilt again

* Fri Dec 09 2005 Jesse Keating <jkeating@redhat.com>
- rebuilt

* Mon Dec  5 2005 Matthias Clasen <mclasen@redhat.com>
- rebuild

* Thu Dec 01 2005 John (J5) Palmieri <johnp@redhat.com>
- rebuild for new dbus

* Wed Nov 30 2005 Matthias Clasen <mclasen@redhat.com>
- Update to 0.9.2

* Tue Oct 25 2005 Matthias Clasen <mclasen@redhat.com>
- Update to 0.9.1

* Fri Sep 02 2005 Colin Walters <walters@redhat.com> 
- Add configure flags --with-bonobo --with-dbus
- BR nautilus-cd-burner-devel
- New upstream CVS snapshot for testing
- Drop IDL file and ui .xml
- Add dbus service file
- Drop upstreamed rhythmbox-bluecurve.tar.gz
- Drop upstreamed rhythmbox-0.8.8-cell-renderer.patch

* Mon Jun 13 2005 Colin Walters <walters@redhat.com> - 0.8.8-3
- Add Bluecurve-ized icons from Jeff Schroeder (157716)
- Add rhythmbox-0.8.8-cell-renderer.patch to remove use of custom
  cell renderer for playback icon (no longer necessary) and
  changes the rating renderer to work with non-b&w icons

* Mon Mar 14 2005 Colin Walters <walters@redhat.com> - 0.8.8-2
- Rebuild for GCC4

* Tue Oct 05 2004 Colin Walters <walters@redhat.com> - 0.8.8-1
- New upstream version
- Remove librb-nautilus-context-menu.so, killed upstream

* Thu Sep 30 2004 Christopher Aillon <caillon@redhat.com> 0.8.7-2
- PreReq desktop-file-utils >= 0.9

* Wed Sep 29 2004 Colin Walters <walters@redhat.com> - 0.8.7-1
- New upstream version

* Sat Sep 18 2004 Colin Walters <walters@redhat.com> - 0.8.6-2
- Fix postun to use correct syntax, thanks Nils Philippsen

* Sat Sep 18 2004 Colin Walters <walters@redhat.com> - 0.8.6-1
- New upstream version
- Call update-desktop-database in post and postun

* Thu Jun 24 2004 Colin Walters <walters@redhat.com> - 0.8.5-1
- New upstream version

* Tue Jun 15 2004 Elliot Lee <sopwith@redhat.com>
- rebuilt

* Tue May 18 2004 Colin Walters <walters@redhat.com> - 0.8.4-1
- New upstream version
- Remove backported patches
- Gratuitiously bump various BuildRequires versions

* Mon May 10 2004 Colin Walters <walters@redhat.com> - 0.8.3-4
- Remove code to unregister GConf schema for now (Closes: #122532)

* Fri May 07 2004 Colin Walters <walters@redhat.com> - 0.8.3-3
- Apply tiny patch from 0.8 arch to fix GConf key used
  for initial sorting

* Fri May 07 2004 Colin Walters <walters@redhat.com> - 0.8.3-2
- Apply patch from 0.8 arch tree to fix a number of memleaks

* Sun May 02 2004 Colin Walters <walters@redhat.com> - 0.8.3-1
- Update to 0.8.3: fixes showstopper bug with internet radio

* Fri Apr 30 2004 Colin Walters <walters@redhat.com> - 0.8.2-1
- Update to 0.8.2
- Fix Source url
- Add smp_mflags
- Bump BuildRequires on gstreamer to 0.8.1

* Fri Apr 23 2004 Colin Walters <walters@redhat.com> - 0.8.1-2
- Uninstall GConf schemas on removal

* Tue Apr 20 2004 Colin Walters <walters@redhat.com> - 0.8.1-1
- Update to 0.8.1

* Fri Apr 16 2004 Colin Walters <walters@redhat.com> - 0.8.0-1
- Update to 0.8.0

* Fri Apr 02 2004 Colin Walters <walters@redhat.com> - 0.7.2-1
- Update to 0.7.2

* Mon Mar 29 2004 Colin Walters <walters@redhat.com> - 0.7.1-2
- Remove BuildRequires on autoconf and libvorbis-devel

* Mon Mar 29 2004 Colin Walters <walters@redhat.com> - 0.7.1-1
- New major version - I know we are past major version slush, but
  this should have been done two weeks ago along with the GNOME 2.6
  upload.  As upstream author as well, I believe this version is
  good enough for FC2.
- Remove --disable-mp3
- Remove id3, flac variables
- Remove GStreamer major version patch
- Fix typo in description

* Tue Mar 16 2004 Jeremy Katz <katzj@redhat.com> - 0.6.8-2
- rebuild for new gstreamer

* Thu Mar 11 2004 Alex Larsson <alexl@redhat.com> 0.6.8-1
- update to 0.6.8

* Tue Mar 02 2004 Elliot Lee <sopwith@redhat.com>
- rebuilt

* Mon Mar  1 2004 Alexander Larsson <alexl@redhat.com> 0.6.7-1
- update to 0.6.7

* Fri Feb 13 2004 Elliot Lee <sopwith@redhat.com>
- rebuilt

* Mon Jan 12 2004 Colin Walters <walters@verbum.org> 0.6.4-1
- New upstream version
- Don't re-run the autotools; upstream incorporates newer versions.
* Tue Oct 28 2003 Jonathan Blandford <jrb@redhat.com> 0.5.4-1
- new version
- remove smp_flags

* Fri Oct 24 2003 Jonathan Blandford <jrb@redhat.com> 0.5.3-5
- remove the initial iradio channels as they all are mp3 based.

* Wed Oct  8 2003 Matthias Saou <matthias@rpmforge.net> 0.5.3-3
- Fix category from Development/Libraries to Applications/Multimedia.
- Use bz2 instead of gz as ftp.gnome.org has both, 300k saved in the src.rpm.
- Fix SCHEMES vs. SCHEMAS in the post scriplet.
- Added gstreamer-plugins-devel, libvorbis-devel, scrollkeeper and gettext deps.
- Removed unnecessary date expansion define.
- Updated description, including mp3 reference removal.
- Added libid3tag and flac optional support for convenient rebuild.
- Removed obsolete omf.make and xmldocs.make (included ones are the same now).

* Mon Sep 22 2003 Jonathan Blandford <jrb@redhat.com> 0.5.3-1
- new version
- use _sysconfdir instead of /etc

* Wed Jan 22 2003 Tim Powers <timp@redhat.com>
- rebuilt

* Wed Dec 18 2002 Jonathan Blandford <jrb@redhat.com>
- gave up on other archs for the Beta
- new version
- remove werror and add missing files

* Thu Nov  7 2002 Jeremy Katz <katzj@redhat.com>
- update to newer cvs snap

* Mon Sep 23 2002 Jeremy Katz <katzj@redhat.com>
- update to cvs snap

* Sun Sep 22 2002 Jeremy Katz <katzj@redhat.com>
- use %%(lang)

* Sun Aug 11 2002 Jeremy Katz <katzj@redhat.com>
- fix post to actually install the schema

* Sat Jun 22 2002 Christian F.K. Schaller <Uraeus@linuxrising.org>
- Added gconf file
- Added i18n directory

* Sat Jun 15 2002 Christian F.K. Schaller <Uraeus@linuxrising.org>
- Updated for new rewrite of rhythmbox, thanks to Jeroen

* Mon Mar 18 2002 Jorn Baayen <jorn@nl.linux.org>
- removed bonobo dependency
* Sat Mar 02 2002 Christian Schaller <Uraeus@linuxrising.org>
- created new spec file
