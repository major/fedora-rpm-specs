%global gst_plugins_base_version 1.6.0
%global gtk3_version 3.19.4

%global tarball_version %%(echo %{version} | tr '~' '.')

Name: totem
Epoch: 1
Version: 43.1
Release: 3%{?dist}
Summary: Movie player for GNOME

# Automatically converted from old format: GPLv2+ with exceptions - review is highly recommended.
License: LicenseRef-Callaway-GPLv2+-with-exceptions
URL: https://wiki.gnome.org/Apps/Videos
Source0: https://download.gnome.org/sources/%{name}/43/%{name}-%{tarball_version}.tar.xz

# https://gitlab.gnome.org/GNOME/totem/-/merge_requests/369
# https://gitlab.gnome.org/GNOME/totem/-/issues/593
# https://bugzilla.redhat.com/show_bug.cgi?id=2176726
# Fixes crash when trying to delete last video
Patch: 0001-grilo-Fix-crash-when-deleting-video.patch
# https://gitlab.gnome.org/GNOME/totem/-/merge_requests/410
Patch: 0001-remove-broken-plugins.patch

BuildRequires: pkgconfig(cairo)
BuildRequires: pkgconfig(gnome-desktop-3.0)
BuildRequires: pkgconfig(gsettings-desktop-schemas)
BuildRequires: pkgconfig(gstreamer-1.0)
BuildRequires: pkgconfig(gstreamer-base-1.0)
BuildRequires: pkgconfig(gstreamer-plugins-base-1.0) >= %{gst_plugins_base_version}
BuildRequires: pkgconfig(gstreamer-audio-1.0)
BuildRequires: pkgconfig(gstreamer-tag-1.0)
BuildRequires: pkgconfig(gstreamer-video-1.0)
BuildRequires: pkgconfig(gtk+-3.0) >= %{gtk3_version}
BuildRequires: pkgconfig(libportal-gtk3)
BuildRequires: pkgconfig(libhandy-1)
BuildRequires: pkgconfig(libpeas-gtk-1.0)
BuildRequires: pkgconfig(totem-plparser)
BuildRequires: pkgconfig(x11)

# Needed for the videoscale element.
BuildRequires: gstreamer1-plugins-good
# For the gtkglsink element.
BuildRequires: gstreamer1-plugins-good-gtk

BuildRequires: gcc-c++
BuildRequires: gettext
BuildRequires: gtk-doc
BuildRequires: itstool
BuildRequires: meson
BuildRequires: python3-devel
BuildRequires: pkgconfig(pygobject-3.0)
BuildRequires: vala
BuildRequires: /usr/bin/appstream-util
BuildRequires: /usr/bin/desktop-file-validate

# Work-around for fontconfig bug https://bugzilla.redhat.com/show_bug.cgi?id=480928
BuildRequires: liberation-sans-fonts

# For plugins
BuildRequires: pkgconfig(grilo-0.3)
BuildRequires: pkgconfig(grilo-pls-0.3)

Requires: %{name}-video-thumbnailer%{?_isa} = %{epoch}:%{version}-%{release}

# For all the Python plugins
Requires: libpeas-loader-python3%{?_isa}
Requires: python3-gobject

Requires: iso-codes
Requires: gstreamer1%{?_isa}
Requires: gstreamer1-plugins-base%{?_isa} >= %{gst_plugins_base_version}
Requires: gstreamer1-plugins-good%{?_isa}
Requires: gstreamer1-plugins-good-gtk%{?_isa}
Requires: gstreamer1-plugins-ugly-free%{?_isa}
%if ! 0%{?flatpak}
Requires: gvfs-fuse%{?_isa}
%endif
# Disabled until ported to GStreamer 1.0
# Requires: gnome-dvb-daemon
Requires: grilo-plugins%{?_isa}
Requires: gsettings-desktop-schemas%{?_isa}
Requires: gtk3%{?_isa} >= %{gtk3_version}

Recommends: gstreamer1-plugin-openh264%{?_isa}
Recommends: gstreamer1-plugins-bad-free%{?_isa}

# Removed in F30
Obsoletes: totem-nautilus < 1:3.31.91
# Removed in F31
Obsoletes: totem-lirc < 1:3.33.0

%description
Totem is simple movie player for the GNOME desktop. It features a
simple playlist, a full-screen mode, seek and volume controls, as well as
a pretty complete keyboard navigation.

Totem is extensible through a plugin system.

%package video-thumbnailer
Summary: Totem video thumbnailer
# split out from totem package in F34
Conflicts: totem < 1:3.38.0-4

%description video-thumbnailer
This package contains the Totem video thumbnailer.

%package devel
Summary: Plugin writer's documentation for totem
Requires: %{name}%{?_isa} = %{epoch}:%{version}-%{release}

%description devel
The %{name}-devel package contains API documentation for
developing developing plugins for %{name}.

%prep
%autosetup -p1 -n %{name}-%{tarball_version}

%build
%meson -Denable-gtk-doc=true
# -j1 to work-around https://github.com/mesonbuild/meson/issues/1994
%meson_build -j1

%install
%meson_install
%find_lang %{name} --with-gnome

%py_byte_compile %{python3} %{buildroot}%{_libdir}/totem/plugins/

%check
appstream-util validate-relax --nonet $RPM_BUILD_ROOT%{_datadir}/metainfo/org.gnome.Totem.appdata.xml
desktop-file-validate $RPM_BUILD_ROOT%{_datadir}/applications/org.gnome.Totem.desktop

%ldconfig_scriptlets

%files -f %{name}.lang
%doc AUTHORS NEWS README
%license COPYING
%{_bindir}/totem
%{_libdir}/libtotem.so.*
%{_libdir}/girepository-1.0/Totem-1.0.typelib
%{_datadir}/applications/org.gnome.Totem.desktop
%{_datadir}/dbus-1/services/org.gnome.Totem.service
%{_datadir}/metainfo/org.gnome.Totem.appdata.xml
%dir %{_libdir}/totem
%dir %{_libdir}/totem/plugins
# Python plugins
%if 0%{?fedora} || 0%{?rhel} > 7
%{_libdir}/totem/plugins/opensubtitles
%{_libdir}/totem/plugins/pythonconsole
%endif
%{_libdir}/totem/plugins/autoload-subtitles
%{_libdir}/totem/plugins/im-status
%{_libdir}/totem/plugins/open-directory
%{_libdir}/totem/plugins/recent
%{_libdir}/totem/plugins/rotation
%{_libdir}/totem/plugins/screensaver
%{_libdir}/totem/plugins/skipto
%{_libdir}/totem/plugins/properties
%{_libdir}/totem/plugins/mpris
%{_libdir}/totem/plugins/screenshot
%{_libdir}/totem/plugins/save-file
%{_libdir}/totem/plugins/variable-rate
%{_libexecdir}/totem-gallery-thumbnailer
%{_datadir}/icons/hicolor/scalable/apps/org.gnome.Totem.svg
%{_datadir}/icons/hicolor/symbolic/apps/org.gnome.Totem-symbolic.svg
%{_datadir}/icons/hicolor/symbolic/apps/totem-tv-symbolic.svg
%{_mandir}/man1/totem.1*
%{_datadir}/GConf/gsettings/*.convert
%{_datadir}/glib-2.0/schemas/*.xml

%files video-thumbnailer
%license COPYING
%{_bindir}/totem-video-thumbnailer
%{_mandir}/man1/totem-video-thumbnailer.1*
%{_datadir}/thumbnailers/totem.thumbnailer

%files devel
%{_datadir}/gtk-doc/html/totem
%{_includedir}/totem
%{_libdir}/libtotem.so
%{_libdir}/pkgconfig/totem.pc
%{_datadir}/gir-1.0/Totem-1.0.gir

%changelog
* Fri Jan 24 2025 Daniel Rusek <mail@asciiwolf.com> - 1:43.1-3
- Removed now unused, broken apple-trailers and vimeo plugins

* Sun Jan 19 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1:43.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Wed Oct 23 2024 David King <amigadave@amigadave.com> - 1:43.1-1
- Update to 43.1

* Wed Sep 04 2024 Miroslav Suchý <msuchy@redhat.com> - 1:43.0-7
- convert license to SPDX

* Sat Jul 20 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1:43.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Tue May 07 2024 Adam Williamson <awilliam@redhat.com> - 43.0-5
- Backport MR #369 to fix crash when deleting last video

* Sat Jan 27 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1:43.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sat Jul 22 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1:43.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Sat Jan 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1:43.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Sep 16 2022 Bastien Nocera <bnocera@redhat.com> - 43.0-1
+ totem-43.0-1
- Update to 43.0

* Tue Sep 06 2022 Bastien Nocera <bnocera@redhat.com> - 43.rc-1
+ totem-43.rc-1
- Update to 43.rc

* Thu Aug 18 2022 Bastien Nocera <bnocera@redhat.com> - 43.beta-1
+ totem-43.beta-1
- Update to 43.beta

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1:43.alpha-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed Jul 20 2022 Kalev Lember <klember@redhat.com> - 1:43.alpha-2
- Rebuilt for libgnome-desktop soname bump

* Sat Jul 16 2022 Bastien Nocera <bnocera@redhat.com> - 43.alpha-1
+ totem-43.alpha-1
- Update to 43.alpha

* Fri Mar 18 2022 Bastien Nocera <bnocera@redhat.com> - 42.0-1
+ totem-42.0-1
- Update to 42.0

* Fri Feb 25 2022 David King <amigadave@amigadave.com> - 42~beta-1
- Update to 42.beta

* Sat Jan 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1:3.38.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Tue Oct 12 2021 Bastien Nocera <bnocera@redhat.com> - 3.38.2-1
+ totem-3.38.2-1
- Update to 3.38.2

* Thu Oct 07 2021 Kalev Lember <klember@redhat.com> - 1:3.38.1-4
- Rebuild to pull in gstreamer1-plugin-openh264 as 0-day F35 update

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1:3.38.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jun 29 2021 Bastien Nocera <bnocera@redhat.com> - 3.38.1-2
+ totem-3.38.1-2
- Remove wrongly licensed translation

* Wed Jun 16 2021 Bastien Nocera <bnocera@redhat.com> - 3.38.1-1
+ totem-3.38.1-1
- Update to 3.38.1

* Tue May 25 2021 Kalev Lember <klember@redhat.com> - 1:3.38.0-6
- Conflict with old totem version instead of using self-obsoletes (#1949422)

* Wed Mar 03 2021 Kalev Lember <klember@redhat.com> - 1:3.38.0-5
- Add self-obsoletes to help with the totem-video-thumbnailer split

* Tue Feb 23 2021 Kalev Lember <klember@redhat.com> - 1:3.38.0-4
- Split totem-video-thumbnailer out to a separate subpackage

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1:3.38.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Nov 17 2020 Kalev Lember <klember@redhat.com> - 1:3.38.0-2
- Rebuild

* Thu Sep 10 2020 Kalev Lember <klember@redhat.com> - 1:3.38.0-1
- Update to 3.38.0

* Tue Sep 01 2020 Kalev Lember <klember@redhat.com> - 1:3.37.90-1
- Update to 3.37.90

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1:3.34.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jun 16 2020 Bastien Nocera <bnocera@redhat.com> - 3.34.1-5
+ totem-3.34.1-5
- Remove automagic Python bytecompilation

* Fri Mar 20 2020 Kalev Lember <klember@redhat.com> - 1:3.34.1-4
- Recommend gstreamer1-plugin-openh264

* Fri Jan 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1:3.34.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jan 16 2020 Kalev Lember <klember@redhat.com> - 1:3.34.1-2
- Rebuilt for libgnome-desktop soname bump

* Mon Oct 07 2019 Kalev Lember <klember@redhat.com> - 1:3.34.1-1
- Update to 3.34.1

* Fri Sep 06 2019 Kalev Lember <klember@redhat.com> - 1:3.34.0-1
- Update to 3.34.0

* Mon Aug 12 2019 Kalev Lember <klember@redhat.com> - 1:3.33.90-1
- Update to 3.33.90

* Sat Jul 27 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1:3.33.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Jul 21 2019 Kalev Lember <klember@redhat.com> - 1:3.33.0-2
- Rebuilt for libgnome-desktop soname bump

* Fri Jul 19 2019 Kalev Lember <klember@redhat.com> - 1:3.33.0-1
- Update to 3.33.0
- Remove and obsolete totem-lirc subpackage

* Mon Jul 15 2019 Kalev Lember <klember@redhat.com> - 1:3.32.1-1
- Update to 3.32.1

* Mon Mar 11 2019 Kalev Lember <klember@redhat.com> - 1:3.32.0-1
- Update to 3.32.0

* Tue Mar 05 2019 Kalev Lember <klember@redhat.com> - 1:3.31.92-1
- Update to 3.31.92

* Tue Feb 19 2019 Kalev Lember <klember@redhat.com> - 1:3.31.91-2
- Rebuilt against fixed atk (#1626575)

* Tue Feb 19 2019 Kalev Lember <klember@redhat.com> - 1:3.31.91-1
- Update to 3.31.91
- Remove and obsolete totem-nautilus subpackage

* Fri Feb 08 2019 Kalev Lember <klember@redhat.com> - 1:3.31.90-1
- Update to 3.31.90

* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1:3.30.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Tue Dec 11 2018 Bastien Nocera <bnocera@redhat.com> - 1:3.30.0-1
- Update to 3.30.0

* Tue Jul 24 2018 Bastien Nocera <bnocera@redhat.com> - 3.26.2-1
+ totem-3.26.2-1
- Update to 3.26.2

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1:3.26.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 1:3.26.1-2
- Rebuilt for Python 3.7

* Fri Jun 15 2018 Bastien Nocera <bnocera@redhat.com> - 3.26.1-1
+ totem-3.26.1-1
- Update to 3.26.1

* Tue Feb 13 2018 Björn Esser <besser82@fedoraproject.org> - 1:3.26.0-7
- Rebuild against newer gnome-desktop3 package

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1:3.26.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Jan 10 2018 Bastien Nocera <bnocera@redhat.com> - 1:3.26.0-5
- Enable Python 3 plugins in RHEL newer than RHEL7 (#1523761)

* Tue Jan 09 2018 Bastien Nocera <bnocera@redhat.com> - 1:3.26.0-4
- Don't package Python plugins if Python support is disabled
  (for non-Fedora builds)

* Mon Jan 08 2018 Bastien Nocera <bnocera@redhat.com> - 1:3.26.0-3
- Work-around meson/Vala parallel build bugs (#1530729)
- Fix build with gtk-doc 1.26

* Fri Jan 05 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 1:3.26.0-2
- Remove obsolete scriptlets

* Mon Sep 11 2017 Kalev Lember <klember@redhat.com> - 1:3.26.0-1
- Update to 3.26.0

* Wed Aug 16 2017 Kalev Lember <klember@redhat.com> - 1:3.25.90.1-1
- Update to 3.25.90.1
- Switch to the meson build system

* Thu Aug 10 2017 Kalev Lember <klember@redhat.com> - 1:3.24.0-5
- Rebuilt for libtotem-plparser soname bump

* Mon Jul 31 2017 Kalev Lember <klember@redhat.com> - 1:3.24.0-4
- Rebuilt for libtotem-plparser soname bump

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1:3.24.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Thu Jul 06 2017 Bastien Nocera <bnocera@redhat.com> - 3.24.0-2
+ totem-3.24.0-2
- Take the guess work out of MP3 support and require gstreamer1-plugins-ugly-free

* Tue Mar 21 2017 Kalev Lember <klember@redhat.com> - 1:3.24.0-1
- Update to 3.24.0

* Fri Mar 03 2017 Bastien Nocera <bnocera@redhat.com> - 3.23.90-2
+ totem-3.23.90-2
- Remove empty youtube subpackage

* Tue Feb 14 2017 Richard Hughes <rhughes@redhat.com> - 1:3.23.90-1
- Update to 3.23.90

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1:3.22.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Jan 30 2017 Bastien Nocera <bnocera@redhat.com> - 3.22.0-2
+ totem-3.22.0-2
- Move gst-plugins-bad to Recommends, it's not required anymore
  since scaletempo moved to -good (#1417467)

* Mon Sep 19 2016 Kalev Lember <klember@redhat.com> - 1:3.22.0-1
- Update to 3.22.0

* Fri Sep 02 2016 Kalev Lember <klember@redhat.com> - 1:3.21.91-1
- Update to 3.21.91
- Don't set group tags

* Wed Apr 13 2016 Kalev Lember <klember@redhat.com> - 1:3.20.1-1
- Update to 3.20.1

* Sun Apr 03 2016 Mathieu Bridon <bochecha@daitauha.fr> - 1:3.20.0-2
- Drop the Zeitgeist dependency.

* Tue Mar 22 2016 Kalev Lember <klember@redhat.com> - 1:3.20.0-1
- Update to 3.20.0

* Thu Mar 17 2016 Kalev Lember <klember@redhat.com> - 1:3.19.92-1
- Update to 3.19.92

* Mon Mar 07 2016 Kalev Lember <klember@redhat.com> - 1:3.19.91-1
- Update to 3.19.91

* Fri Feb 05 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1:3.19.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Dec 18 2015 Kalev Lember <klember@redhat.com> - 1:3.19.3-1
- Update to 3.19.3

* Tue Nov 10 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1:3.18.1-2
- Rebuilt for https://fedoraproject.org/wiki/Changes/python3.5

* Mon Oct 12 2015 Kalev Lember <klember@redhat.com> - 1:3.18.1-1
- Update to 3.18.1

* Mon Sep 21 2015 Kalev Lember <klember@redhat.com> - 1:3.18.0-1
- Update to 3.18.0

* Tue Sep 15 2015 Kalev Lember <klember@redhat.com> - 1:3.17.92-1
- Update to 3.17.92

* Mon Aug 31 2015 Kalev Lember <klember@redhat.com> - 1:3.16.3-1
- Update to 3.16.3

* Wed Aug 19 2015 Kalev Lember <klember@redhat.com> - 1:3.16.2-4
- Use plugin installation API from gstreamer1-plugins-base 1.5.0
- Tighten deps with the _isa macro
- Use make_install macro

* Wed Jul 22 2015 David King <amigadave@amigadave.com> - 1:3.16.2-3
- Bump for new gnome-desktop3

* Sat Jul 04 2015 Kalev Lember <klember@redhat.com> - 1:3.16.2-2
- Switch to Python 3
- Require libpeas-loader-python3 for Python 3 plugin support (#1226879)

* Mon Jun 29 2015 David King <amigadave@amigadave.com> - 1:3.16.1-2
- Update to 3.16.2

* Fri Jun 19 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1:3.16.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Thu May 07 2015 Kalev Lember <kalevlember@gmail.com> - 1:3.16.1-1
- Update to 3.16.1

* Mon Mar 23 2015 Kalev Lember <kalevlember@gmail.com> - 1:3.16.0-1
- Update to 3.16.0

* Tue Mar 17 2015 Kalev Lember <kalevlember@gmail.com> - 1:3.15.92-1
- Update to 3.15.92

* Wed Mar 04 2015 Kalev Lember <kalevlember@gmail.com> - 1:3.15.91-1
- Update to 3.15.91

* Tue Feb 24 2015 David King <amigadave@amigadave.com> - 1:3.15.90-1
- Use clutter-gst3

* Sat Feb 21 2015 Kalev Lember <kalevlember@gmail.com> - 1:3.15.90-1
- Update to 3.15.90
- Use new missing plugins API from gstreamer1-plugins-base-1.4.5-2.fc22

* Fri Feb 13 2015 Richard Hughes <rhughes@redhat.com> - 1:3.15.4-1
- Update to 3.15.4

* Tue Feb 10 2015 David King <amigadave@amigadave.com> - 1:3.14.2-2
- Update URL
- Use pkgconfig for BuildRequires
- Validate desktop file and AppData in check
- Use license macro for COPYING
- Update man page glob in files section

* Thu Jan 29 2015 David King <amigadave@amigadave.com> - 1:3.14.2-1
- Update to 3.14.2

* Sun Nov 23 2014 Kalev Lember <kalevlember@gmail.com> - 1:3.14.1-1
- Update to 3.14.1

* Thu Nov 13 2014 Richard Hughes <richard@hughsie.com> - 1:3.14.0-3
- Remove pyxdg, it's no longer required

* Tue Nov 04 2014 Richard Hughes <richard@hughsie.com> - 1:3.14.0-2
- Fix non-Fedora build

* Mon Sep 22 2014 Kalev Lember <kalevlember@gmail.com> - 1:3.14.0-1
- Update to 3.14.0

* Wed Sep 03 2014 Kalev Lember <kalevlember@gmail.com> - 1:3.13.92-1
- Update to 3.13.92

* Wed Sep 03 2014 Kalev Lember <kalevlember@gmail.com> - 1:3.13.91-1
- Update to 3.13.91
- Tighten subpackage requires

* Mon Aug 18 2014 Kalev Lember <kalevlember@gmail.com> - 1:3.13.90-1
- Update to 3.13.90
- Drop gnome-icon-theme dependency
- Remove and obsolete -mozplugin and -mozplugin-vegas subpackages

* Mon Aug 18 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1:3.12.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Tue Jul 22 2014 Kalev Lember <kalevlember@gmail.com> - 1:3.12.1-4
- Rebuilt for gobject-introspection 1.41.4

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1:3.12.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Thu May 29 2014 Kalev Lember <kalevlember@gmail.com> - 1:3.12.1-2
- Fix parent class in template definition

* Tue May 20 2014 Kalev Lember <kalevlember@gmail.com> - 1:3.12.1-1
- Update to 3.12.1

* Mon Mar 24 2014 Richard Hughes <rhughes@redhat.com> - 1:3.12.0-1
- Update to 3.12.0

* Tue Mar 18 2014 Richard Hughes <rhughes@redhat.com> - 1:3.11.91-1
- Update to 3.11.91

* Thu Feb 20 2014 Kalev Lember <kalevlember@gmail.com> - 1:3.11.90-2
- Rebuilt for cogl soname bump

* Tue Feb 18 2014 Richard Hughes <rhughes@redhat.com> - 1:3.11.90-1
- Update to 3.11.90

* Mon Feb 10 2014 Peter Hutterer <peter.hutterer@redhat.com> - 1:3.11.5-4
- Rebuild for libevdev soname bump

* Thu Feb 06 2014 Kalev Lember <kalevlember@gmail.com> - 1:3.11.5-3
- Revert accidental epoch bump

* Thu Feb 06 2014 Adam Williamson <awilliam@redhat.com> - 2:3.11.5-2
- don't need patch to disable appdata validation, just autogen.sh

* Wed Feb 05 2014 Richard Hughes <rhughes@redhat.com> - 1:3.11.5-1
- Update to 3.11.5

* Thu Oct 03 2013 Bastien Nocera <bnocera@redhat.com> 3.10.1-1
- Update to 3.10.1

* Wed Sep 25 2013 Kalev Lember <kalevlember@gmail.com> - 1:3.10.0-1
- Update to 3.10.0

* Thu Sep 19 2013 Kalev Lember <kalevlember@gmail.com> - 1:3.9.92-1
- Update to 3.9.92

* Sat Aug 10 2013 Kalev Lember <kalevlember@gmail.com> - 1:3.9.5-1
- Update to 3.9.5
- Include the new vimeo plugin

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1:3.8.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Fri Jun 28 2013 Kalev Lember <kalevlember@gmail.com> - 1:3.8.2-2
- Adapt for gnome-icon-theme packaging changes

* Tue May 14 2013 Richard Hughes <rhughes@redhat.com> - 1:3.8.2-1
- Update to 3.8.2

* Tue Mar 26 2013 Kalev Lember <kalevlember@gmail.com> - 1:3.8.0-1
- Update to 3.8.0

* Wed Mar 20 2013 Richard Hughes <rhughes@redhat.com> - 1:3.7.93-1
- Update to 3.7.93

* Thu Feb 21 2013 Kalev Lember <kalevlember@gmail.com> 3.6.3-4
- Rebuilt for cogl soname bump

* Fri Jan 25 2013 Peter Robinson <pbrobinson@fedoraproject.org> 3.6.3-3
- Rebuild for new cogl

* Fri Jan 04 2013 Bastien Nocera <bnocera@redhat.com> 3.6.3-2
- Remove hard dependency on gnome-dvb-daemon until it's ported
  to GStreamer 1.0

* Thu Nov 08 2012 Bastien Nocera <bnocera@redhat.com> 3.6.3-1
- Update to 3.6.3

* Fri Oct 26 2012 Kalev Lember <kalevlember@gmail.com> - 1:3.6.2-1
- Update to 3.6.2

* Mon Oct  8 2012 Brian Pepple <bpepple@fedoraproject.org> - 1:3.6.0-2
- Rebuild against new gstreamer1.

* Tue Sep 25 2012 Kalev Lember <kalevlember@gmail.com> - 1:3.6.0-1
- Update to 3.6.0

* Wed Sep 19 2012 Tomas Bzatek <tbzatek@redhat.com> - 1:3.5.92-1
- Update to 3.5.92

* Tue Aug 28 2012 Matthias Clasen <mclasen@redhat.com> - 1:3.5.90-2
- Rebuild against newer cogl/clutter

* Wed Aug 22 2012 Richard Hughes <hughsient@gmail.com> - 1:3.5.90-1
- Update to 3.5.90

* Fri Jul 27 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1:3.4.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sun Jul 22 2012 Ville Skyttä <ville.skytta@iki.fi> - 1:3.4.3-2
- Call ldconfig at post(un)install time.
- Own the %%{_datadir}/totem dir.
- Fix tarball URL.

* Tue Jul 17 2012 Richard Hughes <hughsient@gmail.com> - 1:3.4.3-1
- Update to 3.4.3

* Wed Jun 27 2012 Bastien Nocera <bnocera@redhat.com> 3.4.2-2
- Enable the vala plugins

* Fri May 18 2012 Richard Hughes <hughsient@gmail.com> - 1:3.4.2-1
- Update to 3.4.2

* Sun May 06 2012 Adel Gadllah <adel.gadllah@gmail.com> 3.4.1-3
- Split off vegas plugin (RH #804435)

* Wed Apr 25 2012 Bastien Nocera <bnocera@redhat.com> 3.4.1-2
- Remove dependencies for removed plugin (#816245)

* Mon Apr 16 2012 Richard Hughes <hughsient@gmail.com> - 1:3.4.1-1
- Update to 3.4.1

* Tue Mar 27 2012 Richard Hughes <hughsient@gmail.com> - 1:3.4.0-1
- Update to 3.4.0

* Tue Mar 20 2012 Kalev Lember <kalevlember@gmail.com> - 1:3.3.92-1
- Update to 3.3.92

* Sat Mar 10 2012 Matthias Clasen <mclasen@redhat.com> - 1:3.3.90-2
- Rebuild against new cogl

* Sat Feb 25 2012 Matthias Clasen <mclasen@redhat.com> - 1:3.3.90-1
- Update to 3.3.90

* Thu Jan 19 2012 Matthias Clasen <mclasen@redhat.com> - 1:3.3.4-3
- Rebuild against new cogl

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1:3.3.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Wed Dec 21 2011 Matthias Clasen <mclasen@redhat.com> - 1:3.3.4-1
- Update to 3.3.4

* Tue Dec 20 2011 Matthias Clasen <mclasen@redhat.com> - 1:3.3.3-1
- Update to 3.3.3
- Drop a space-saving hack

* Thu Nov 24 2011 Matthias Clasen <mclasen@redhat.com> - 1:3.2.1-3
- Rebuild against new clutter

* Wed Nov  9 2011 Adam Williamson <awilliam@redhat.com> - 1:3.2.1-2
- bump to 3.2.1, with revision 2 to stay 'ahead' of f16

* Wed Oct 26 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1:3.2.0-2
- Rebuilt for glibc bug#747377

* Tue Sep 27 2011 Ray <rstrode@redhat.com> - 1:3.2.0-1
- Update to 3.2.0

* Tue Sep 20 2011 Matthias Clasen <mclasen@redhat.com> 3.1.92-1
- Update to 3.1.92

* Wed Aug 03 2011 Bastien Nocera <bnocera@redhat.com> 3.1.4-1
- Update to 3.1.4
- Remove obsoleted plugins

* Mon Jun 27 2011 Elad Alfassa <elad@fedoraproject.org> - 1:3.1.0-2
- Moved mozilla-viewer.ui to -mozplugin to fix bug #545131

* Wed May 11 2011 Bastien Nocera <bnocera@redhat.com> 3.1.0-1
- Update to 3.1.0

* Sat May 07 2011 Christopher Aillon <caillon@redhat.com> - 1:3.0.1-2
- Update gsettings schema scriptlet

* Tue Apr 26 2011 Bastien Nocera <bnocera@redhat.com> 3.0.1-1
- Update to 3.0.1

* Mon Apr 04 2011 Bastien Nocera <bnocera@redhat.com> 3.0.0-1
- Update to 3.0.0

* Mon Mar 28 2011 Bastien Nocera <bnocera@redhat.com> 2.91.93-1
- Update to 2.91.93
- Re-add iso-codes Requires, it's needed for translations of
  subtitles and audio track names

* Mon Mar 21 2011 Bastien Nocera <bnocera@redhat.com> 2.91.92-1
- Update to 2.91.92

* Thu Mar 10 2011 Bastien Nocera <bnocera@redhat.com> 2.91.91-1
- Update to 2.91.91

* Mon Feb 21 2011 Bastien Nocera <bnocera@redhat.com> 2.91.7-1
- Update to 2.91.7

* Fri Feb 11 2011 Matthias Clasen <mclasen@redhat.com> 2.91.6-3
- Rebuild against newer gtk

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1:2.91.6-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Wed Feb  2 2011 Matthias Clasen <mclasen@redhat.com> 2.91.6-2
- Rebuild against newer gtk

* Wed Feb 02 2011 Bastien Nocera <bnocera@redhat.com> 2.91.6-1
- Update to 2.91.6

* Fri Jan 28 2011 Bastien Nocera <bnocera@redhat.com> 2.91.5-1
- Update to 2.91.5

* Mon Jan 10 2011 Matthias Clasen <mclasen@redhat.com> 2.91.4-1
- Update to 2.91.4

* Fri Dec  3 2010 Matthias Clasen <mclasen@redhat.com> 2.91.0-4
- Rebuild against newer gtk3

* Fri Nov 19 2010 Bastien Nocera <bnocera@redhat.com> 2.91.0-3
- Fix missing calls to glib-compile-schemas

* Thu Nov 11 2010 Bastien Nocera <bnocera@redhat.com> 2.91.0-2
- Remove GConf schemas scripts
- Remove mythtv sub-package, was removed upstream

* Tue Nov 02 2010 Bastien Nocera <bnocera@redhat.com> 2.91.0-1
- Update to 2.91.0

* Fri Sep 24 2010 Parag Nemade <paragn AT fedoraproject.org> 2.90.5-8
- Merge-review cleanup (#226500)

* Wed Sep 22 2010 Matthias Clasen <mclasen@redhat.com> 2.90.5-7
- Rebuild against newer gobject-introspection

* Fri Aug 06 2010 Bastien Nocera <bnocera@redhat.com> 2.90.5-6
- Update epoch to match Fedora 14

* Wed Jul 28 2010 Adam Williamson <awilliam@redhat.com> - 2.90.5-5
- package various new bits (a shared library, and girepository stuff)

* Tue Jul 27 2010 David Malcolm <dmalcolm@redhat.com> - 2.90.5-4
- coherence_upnp doesn't built in rawhide: disable the subpackage for now

* Tue Jul 27 2010 David Malcolm <dmalcolm@redhat.com> - 2.90.5-3
- cherrypick fix for building against libpeas-0.5.3

* Tue Jul 27 2010 David Malcolm <dmalcolm@redhat.com> - 2.90.5-2
- Rebuilt for https://fedoraproject.org/wiki/Features/Python_2.7/MassRebuild

* Mon Jul 19 2010 Bastien Nocera <bnocera@redhat.com> 2.90.5-1
- Update to 2.90.5

* Fri May 14 2010 Bastien Nocera <bnocera@redhat.com> 2.30.2-2
- Fix spec bugs from review

* Wed May 12 2010 Bastien Nocera <bnocera@redhat.com> 2.30.2-1
- Update to 2.30.2

* Tue Apr 27 2010 Bastien Nocera <bnocera@redhat.com> 2.30.1-1
- Update to 2.30.1

* Thu Apr 08 2010 Bastien Nocera <bnocera@redhat.com> 2.30.0-2
- Rebuild for new libgdata

* Mon Mar 29 2010 Bastien Nocera <bnocera@redhat.com> 2.30.0-1
- Update to 2.30.0

* Mon Mar 15 2010 Bastien Nocera <bnocera@redhat.com> 2.29.92-1
- Update to 2.29.92

* Wed Mar 03 2010 Bastien Nocera <bnocera@redhat.com> 2.29.91-2
- Require gnome-dvb-daemon for DVB support

* Wed Feb 24 2010 Bastien Nocera <bnocera@redhat.com> 2.29.91-1
- Update to 2.29.91

* Sun Feb 14 2010 Matthias Clasen <mclasen@redhat.com> 2.29.4-3
- Add missing libs

* Mon Feb 01 2010 Bastien Nocera <bnocera@redhat.com> 2.29.4-2
- Update for new gstreamer-plugins-bad-free package

* Tue Jan 26 2010 Bastien Nocera <bnocera@redhat.com> 2.29.4-1
- Update to 2.29.4

* Tue Jan 26 2010 Bastien Nocera <bnocera@redhat.com> 2.29.3-1
- Update to 2.29.3

* Tue Jan 12 2010 Bastien Nocera <bnocera@redhat.com> 2.29.2-2
- Remove python-gdata requires

* Mon Nov 30 2009 Bastien Nocera <bnocera@redhat.com> 2.29.2-1
- Update to 2.29.2

* Mon Oct 26 2009 Bastien Nocera <bnocera@redhat.com> 2.28.2-1
- Update to 2.28.2

* Tue Oct 20 2009 Bastien Nocera <bnocera@redhat.com> 2.28.1-2
- Add missing dependency (#529845)

* Tue Sep 29 2009 Bastien Nocera <bnocera@redhat.com> 2.28.1-1
- Update to 2.28.1

* Fri Sep 25 2009 Matthias Clasen <mclasen@redhat.com> - 2.28.0-4
- More requires

* Fri Sep 25 2009 Matthias Clasen <mclasen@redhat.com> - 2.28.0-3
- Add requires for iplayer plugin (#522068)

* Thu Sep 24 2009 Bastien Nocera <bnocera@redhat.com> 2.28.0-2
- Rebuild for new libgdata

* Mon Sep 21 2009 Bastien Nocera <bnocera@redhat.com> 2.28.0-1
- Update to 2.28.0

* Tue Sep 15 2009 Bill Nottingham <notting@redhat.com> 2.27.92-3
- youtube plugin is now in C, remove python requires

* Tue Sep 15 2009 Bastien Nocera <bnocera@redhat.com> 2.27.92-2
- Use PA to set the stream volume

* Tue Sep 08 2009 Bastien Nocera <bnocera@redhat.com> 2.27.92-1
- Update to 2.27.92

* Sat Aug 29 2009 Caolán McNamara <caolanm@redhat.com> - 2.27.2-8
- rebuilt with new openssl

* Thu Aug 27 2009 Tomas Mraz <tmraz@redhat.com> - 2.27.2-7
- rebuilt with new openssl

* Sat Aug 22 2009 Matthias Clasen <mclasen@redhat.com> - 2.27.2-6
- Respect the button-images setting better

* Tue Aug 11 2009 Bastien Nocera <bnocera@redhat.com> 2.27.2-4
- Fix source URL

* Tue Aug 04 2009 Bastien Nocera <bnocera@redhat.com> 2.27.2-3
- Remove gnome-themes dependency, use gnome-icon-theme instead

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.27.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Thu Jul 23 2009 Bastien Nocera <bnocera@redhat.com> 2.27.2-1
- Update to 2.27.2

* Tue Jul 21 2009 Bastien Nocera <bnocera@redhat.com> 2.27.1-3
- Rebuild for new libgdata

* Mon Jun 08 2009 Bastien Nocera <bnocera@redhat.com> 2.27.1-2
- Rebuild against newer libgdata

* Wed May 06 2009 Bastien Nocera <bnocera@redhat.com> 2.27.1-1
- Update to 2.27.1
- Remove xine-lib backend

* Tue Apr 28 2009 Bastien Nocera <bnocera@redhat.com> 2.26.1-3
- Add missing pyxdg requires for the OpenSubtitles plugin (#497787)

* Thu Apr 23 2009 Bastien Nocera <bnocera@redhat.com> 2.26.1-4
- Add missing gnome-python2-gconf req (#483265)

* Thu Apr 02 2009 - Bastien Nocera <bnocera@redhat.com> - 2.26.1-2
- Update patch to set the PA stream volume, avoids setting the 
  volume when pulsesink isn't in a state where it has a stream
  (#488532)

* Wed Apr 01 2009 - Bastien Nocera <bnocera@redhat.com> - 2.26.1-1
- Update to 2.26.1

* Mon Mar 16 2009 - Bastien Nocera <bnocera@redhat.com> - 2.26.0-1
- Update to 2.26.0

* Tue Mar 03 2009 - Bastien Nocera <bnocera@redhat.com> -2.25.92-1
- Update to 2.25.92

* Thu Feb 26 2009 - Bastien Nocera <bnocera@redhat.com> - 2.25.91-4
- Kill galago plugin

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.25.91-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Tue Feb 17 2009 - Bastien Nocera <bnocera@redhat.com> - 2.25.91-2
- Add patch to set the PulseAudio application role

* Tue Feb 17 2009 - Bastien Nocera <bnocera@redhat.com> - 2.25.91-1
- Update to 2.25.91

* Thu Feb 12 2009 - Bastien Nocera <bnocera@redhat.com> - 2.25.90-3
- Add patch to set the PA stream volume from Totem, instead
  of having a separate one

* Wed Feb 04 2009 - Peter Robinson <pbrobinson@gmail.com> - 2.25.90-2
- Fix logic in spec file for xine disable

* Tue Feb 03 2009 - Bastien Nocera <bnocera@redhat.com> - 2.25.90-1
- Update to 2.25.90
- Add separate UPNP plugin package

* Wed Jan 28 2009 - Bastien Nocera <bnocera@redhat.com> - 2.25.3-9
- Remove gnome-desktop requires, it's not needed

* Fri Jan 23 2009 - Bastien Nocera <bnocera@redhat.com> - 2.25.3-8
- Rebuild for new MySQL libraries

* Fri Jan 16 2009  Matthias Clasen <mclasen@redhat.com> - 2.25.3-7
- Own /usr/lib/totem

* Mon Jan 05 2009 - Bastien Nocera <bnocera@redhat.com> - 2.25.3-6
- Remove compiled bits for the bug report scripts (#478889)

* Wed Dec 17 2008 - Bastien Nocera <bnocera@redhat.com> - 2.25.3-5
- Whatever

* Wed Dec 17 2008 - Bastien Nocera <bnocera@redhat.com> - 2.25.3-4
- Add totem-tv icons, and jamendo plugin

* Wed Dec 17 2008 - Bastien Nocera <bnocera@redhat.com> - 2.25.3-3
- Add missing, but temporary, startup-notification BR

* Wed Dec 17 2008 - Bastien Nocera <bnocera@redhat.com> - 2.25.3-2
- Disable tracker plugin until tracker is fixed

* Mon Dec 15 2008 - Bastien Nocera <bnocera@redhat.com> - 2.25.3-1
- Update to 2.25.3

* Wed Dec 10 2008 - Bastien Nocera <bnocera@redhat.com> - 2.24.3-4
- Remove hal, glade, gnome-desktop and control-center BRs, not needed anymore

* Sun Nov 30 2008 Ignacio Vazquez-Abrams <ivazqueznet+rpm@gmail.com> - 2.24.3-3
- Rebuild for Python 2.6

* Sat Nov 22 2008 Matthias Clasen <mclasen@redhat.com> - 2.24.3-2
- Tweak %%descriptions

* Sun Oct 26 2008 - Bastien Nocera <bnocera@redhat.com> - 2.24.3-1
- Update to 2.24.3
- Fixes for recent YouTube website changes (#468578)

* Fri Oct 24 2008 Brian Pepple <bpepple@fedoraproject.org> - 2.24.2-3
- rebuild for new libepc.

* Thu Oct  9 2008 Matthias Clasen <mclasen@redhat.com> - 2.24.2-2
- Save some space

* Tue Oct 07 2008 - Bastien Nocera <bnocera@redhat.com> - 2.24.2-1
- Update to 2.24.2

* Wed Oct 01 2008 - Bastien Nocera <bnocera@redhat.com> - 2.24.1-1
- Update to 2.24.1

* Sun Sep 21 2008 - Bastien Nocera <bnocera@redhat.com> - 2.24.0-1
- Update to 2.24.0

* Mon Sep  8 2008 Tom "spot" Callaway <tcallawa@redhat.com> - 2.23.91-3
- fix license tag

* Mon Sep 01 2008 - Bastien Nocera <bnocera@redhat.com> - 2.23.91-2
- Remove unneeded scrollkeeper BR (#460344)

* Fri Aug 29 2008 - Bastien Nocera <bnocera@redhat.com> - 2.23.91-1
- Update to 2.23.91

* Wed Jun 11 2008 - Bastien Nocera <bnocera@redhat.com> - 2.23.4-1
- Update to 2.23.4
- Remove gnome-vfs BRs
- Remove xulrunner patches and requires, we don't need them anymore

* Sat May 17 2008 - Bastien Nocera <bnocera@redhat.com> - 2.23.3-2
- Rebuild

* Wed May 14 2008 - Bastien Nocera <bnocera@redhat.com> - 2.23.3-1
- Update to 2.23.3

* Tue May 13 2008 - Bastien Nocera <bnocera@redhat.com> - 2.23.2-4
- Rebuild

* Wed May 07 2008 - Bastien Nocera <bnocera@redhat.com> - 2.23.2-3
- Require gstreamer-plugins-flumpegdemux as used by the DVB and DVD
  playback bits

* Mon Apr 21 2008 - Bastien Nocera <bnocera@redhat.com> - 2.23.2-1
- Update to 2.23.2
- Fix scriptlets removing the alternatives on upgrade (#442895)

* Tue Apr 08 2008 Stewart Adam <s.adam@diffingo.com> - 2.23.1-2
- Fix error when only a single backend has been installed (#439634)

* Tue Apr 08 2008 - Bastien Nocera <bnocera@redhat.com> - 2.23.1-1
- Update to 2.23.1

* Wed Mar 19 2008 Stewart Adam <s.adam@diffingo.com> - 2.23.0-6
- Use alternatives to switch the backend
- Update totem-backend script accordingly
- Remove ldconfig from %%postun, do that in individual the backends instead
- Do not restore a default backend, ldconfig in backends does this
- Fix Source0 URL

* Mon Mar 17 2008 Jesse Keating <jkeating@redhat.com> - 2.23.0-5
- Fix some Provides to prevent cross arch obsoletions.

* Mon Mar 10 2008 - Bastien Nocera <bnocera@redhat.com> - 2.23.0-4
- Try to build with a liboil with Altivec disabled

* Sun Mar 09 2008 - Bastien Nocera <bnocera@redhat.com> - 2.23.0-3
- Remove PPC/PPC64 ExcludeArch

* Fri Mar 07 2008 - Bastien Nocera <bnocera@redhat.com> - 2.23.0-2
- Re-add missing nautilus files section
- Fix obsoletes and provides to upgrade from the broken 2.21.96
  packages

* Tue Mar 04 2008 - Bastien Nocera <bnocera@redhat.com> - 2.23.0-1
- Update to 2.23.0, rework the -gstreamer/-xine backend split to
  switch libraries instead of having replacements for all the
  binaries

* Mon Mar 03 2008 - Bastien Nocera <bnocera@redhat.com> - 2.21.96-1
- Update to 2.21.96
- Add ppc and ppc64 to ExcludeArch as liboil is crashing on us (#435771)
- Add big patch from Stewart Adam <s.adam@diffingo.com> to allow
  switching between the GStreamer and the xine-lib backends at
  run-time, see #327211 for details

* Tue Feb 26 2008 - Bastien Nocera <bnocera@redhat.com> - 2.21.95-1
- Update to 2.21.95

* Sun Feb 24 2008 - Bastien Nocera <bnocera@redhat.com> - 2.21.94-1
- Update to 2.21.94

* Sun Feb 17 2008 - Bastien Nocera <bnocera@redhat.com> - 2.21.93-2
- Rebuild for dependencies

* Tue Feb 12 2008 - Bastien Nocera <bnocera@redhat.com> - 2.21.93-1
- Update to 2.21.93

* Tue Feb 05 2008 - Bastien Nocera <bnocera@redhat.com> - 2.21.92-2
- Remove unnecessary patch to the GMP plugin

* Mon Feb 04 2008 - Bastien Nocera <bnocera@redhat.com> - 2.21.92-1
- Update to 2.21.92

* Fri Jan 25 2008 - Bastien Nocera <bnocera@redhat.com> - 2.21.91-1
- Update to 2.21.91
- Split out the nautilus extension (#427832)
- Remove .a and .la files (#430328)

* Fri Jan 18 2008  Matthias Clasen <mclasen@redhat.com> - 2.21.90-2
- Add content-type support

* Mon Jan 07 2008 - Bastien Nocera <bnocera@redhat.com> - 2.21.90-1
- Update to 2.21.90
- Add patch to allow building against xulrunner

* Mon Dec 10 2007 - Bastien Nocera <bnocera@redhat.com> - 2.21.5-4
- Add the (non-working yet, missing files in the tarball) publish plugin

* Mon Dec 10 2007 - Bastien Nocera <bnocera@redhat.com> - 2.21.5-3
- Add the mythtv schemas to the mythtv subpackage (#410451)

* Sun Dec  9 2007  Matthias Clasen  <mclasen@redhat.com> - 2.21.5-2
- Make it build

* Sun Dec 09 2007 - Bastien Nocera <bnocera@redhat.com> - 2.21.5-1
- Update to 2.21.5
- Remove -devel and -plparser subpackages, they're in totem-pl-parser now

* Thu Dec 06 2007 - Bastien Nocera <bnocera@redhat.com> - 2.21.3-3
- The mozilla plugin only need gecko-libs, not devel
  Thanks to Jeremy Katz for noticing

* Thu Dec 06 2007 Release Engineering <rel-eng at fedoraproject dot org> - 2.21.3-2
- Rebuild for deps

* Mon Dec 03 2007 - Bastien Nocera <bnocera@redhat.com> - 2.21.3-1
- Update to 2.21.3
- Add tracker video search sub-package

* Wed Nov 21 2007 - Bastien Nocera <bnocera@redhat.com> - 2.21.2-2
- Try to build against xulrunner

* Mon Nov 12 2007 - Bastien Nocera <bnocera@redhat.com> - 2.21.2-1
- Update to 2.21.2

* Wed Oct 31 2007 - Bastien Nocera <bnocera@redhat.com> - 2.21.1-1
- Update to 2.21.1

* Wed Oct 24 2007 - Bastien Nocera <bnocera@redhat.com> - 2.21.0-3
- Add python BRs so we have Python support for the YouTube plugin

* Mon Oct 22 2007  Matthias Clasen <mclasen@redhat.com> - 2.21.0-2
- Rebuild against new dbus-glib

* Sun Oct 21 2007 - Bastien Nocera <bnocera@redhat.com> - 2.21.0-1
- Update to 2.21.0

* Wed Oct 17 2007 - Bastien Nocera <bnocera@redhat.com> - 2.20.1-1
- Update to 2.20.1
- Require GTK+ 2.12.1

* Sun Sep 16 2007 - Bastien Nocera <bnocera@redhat.com> - 2.20.0-1
- Update for 2.20.0

* Fri Aug 17 2007 - Bastien Nocera <bnocera@redhat.com> - 2.19.90-1
- Update for 2.19.90

* Wed Aug 15 2007 - Bastien Nocera <bnocera@redhat.com> - 2.19.6-5
- Up the gstreamer-plugins-base requirements so we get a newer liboil
  and PPC(64) builds work again (#252179)

* Tue Aug 14 2007 - Bastien Nocera <bnocera@redhat.com> - 2.19.6-4
- Disable ppc and ppc64 to work around a liboil bug (#252179)

* Tue Aug  7 2007 Matthias Clasen <mclasen@redhat.com> - 2.19.6-3
- Update license fields
- Use %%find_lang for help files

* Sat Aug 04 2007 - Bastien Nocera <bnocera@redhat.com> - 2.19.6-2
- Don't package the bemused plugin, it's not ready yet

* Mon Jul 30 2007 - Bastien Nocera <bnocera@redhat.com> - 2.19.6-1
- Update to 2.19.6
- Fix location of the browser plugins
- Avoid gst-inspect failing stopping the build

* Mon Jun 04 2007 - Bastien Nocera <bnocera@redhat.com> - 2.19.4-2.1
- Another rebuild with the liboil fixes

* Mon Jun 04 2007 - Bastien Nocera <bnocera@redhat.com> - 2.19.4-2
- Update to 2.19.4

* Mon May 21 2007 - Bastien Nocera <bnocera@redhat.com> - 2.19.3-2
- Don't forget the media-player-keys plugin

* Mon May 21 2007 - Bastien Nocera <bnocera@redhat.com> - 2.19.3-1
- Update to 2.19.3, fix build

* Mon May 21 2007 - Bastien Nocera <bnocera@redhat.com> - 2.19.2-3
- Fix unclosed curly brace

* Mon May 21 2007 - Bastien Nocera <bnocera@redhat.com> - 2.19.2-2
- Add lirc, and galago sub-packages

* Sun May 20 2007 Matthias Clasen <mclasen@redhat.com> - 2.19.2-1
- Update to 2.19.2

* Mon Apr 23 2007 - Bastien Nocera <bnocera@redhat.com> - 2.18.2-3
- Add missing control-center-devel BuildRequires, to use the new
  playback key infrastructure in gnome-settings-daemon (#237484)

* Wed Apr 11 2007 - Bastien Nocera <bnocera@redhat.com> - 2.18.1-2
- Add requires for gnome-themes, spotted by Nigel Jones (#235819)

* Wed Apr 04 2007 - Bastien Nocera <bnocera@redhat.com> - 2.18.1-1
- New upstream version with plenty of bug fixes

* Fri Mar 09 2007 - Bastien Nocera <bnocera@redhat.com> - 2.18.0-1
- Update to 2.18.0
- Update GStreamer base plugins requirements to get some "codec-buddy"
  support

* Wed Feb 21 2007 - Bastien Nocera <bnocera@redhat.com> - 2.17.92-2
- Add gstreamer-plugins-good as a builddep so that gconfaudiosink
  can be found during configure

* Wed Feb 21 2007 - Bastien Nocera <bnocera@redhat.com> - 2.17.92-1
- Update to 2.17.92

* Thu Feb 08 2007 - Bastien Nocera <bnocera@redhat.com> - 2.17.91-1
- Update to 2.17.91
- Resolves: #227661

* Mon Jan 29 2007 - Bastien Nocera <bnocera@redhat.com> - 2.17.90-1
- Make the -devel package own $includedir/totem and below
- Resolves: #212093
- Update homepage, and download URLs
- Update to 2.17.90, remove obsolete patch

* Tue Jan 16 2007 Matthias Clasen <mclasen@redhat.com> - 2.17.5-1
- Update to 2.17.5

* Mon Nov 20 2006 Alexander Larsson <alexl@redhat.com> - 2.17.3-2
- Remove libtotem-plparser.so from totem package
- Split out totem-plparser into subpackage
- Resolves: #203640

* Wed Nov 15 2006 Matthias Clasen <mclasen@redhat.com> - 2.17.3-1
- Update to 2.17.3
 
* Sat Nov  4 2006 Matthias Clasen <mclasen@redhat.com> - 2.17.2-1 
- Update to 2.17.2

* Sun Oct 22 2006 Matthias Clasen <mclasen@redhat.com> - 2.17.1-1 
- Update to 2.17.1

* Sat Oct 21 2006 Matthias Clasen <mclasen@redhat.com> - 2.17.0-1
- Update to 2.17.0

* Wed Oct 18 2006 Matthias Clasen <mclasen@redhat.com> - 2.16.1-2
- Fix scripts to follow packaging guidelines

* Thu Sep  7 2006 Matthias Clasen <mclasen@redhat.com> - 2.16.1-1.fc6
- Update to 2.16.1, including several improvements to 
  the mozilla plugin

* Sun Sep  3 2006 Matthias Clasen <mclasen@redhat.com> - 2.16.0-1.fc6
- Update to 2.16.0

* Tue Aug 22 2006 Matthias Clasen <mclasen@redhat.com> - 1.5.92-1.fc6
- Update to 1.5.92
- Require pkgconfig in the -devel package

* Mon Aug 14 2006 Matthias Clasen <mclasen@redhat.com> - 1.5.91-2.fc6
- Make translations work again

* Sun Aug 13 2006 Matthias Clasen <mclasen@redhat.com> - 1.5.91-1.fc6
- Update to 1.5.91

* Thu Aug  3 2006 Matthias Clasen <mclasen@redhat.com> - 1.5.90-1.fc6
- Update to 1.5.90

* Mon Jul 31 2006 Matthias Clasen <mclasen@redhat.com> - 1.5.4-4
- Rebuild against firefox-devel

* Wed Jul 19 2006 Matthias Clasen <mclasen@redhat.com> - 1.5.4-3
- Don't use deprecated dbus api

* Wed Jul 19 2006 Matthias Clasen <mclasen@redhat.com> - 1.5.4-2
- Rebuild against dbus

* Wed Jul 12 2006 Matthias Clasen <mclasen@redhat.com> - 1.5.4-1
- Update to 1.5.4

* Wed Jun 14 2006 Matthias Clasen <mclasen@redhat.com> - 1.5.2-2
- Work around a gstreamer problem

* Tue Jun 13 2006 Matthias Clasen <mclasen@redhat.com> - 1.5.2-1
- Update to 1.5.2
- BuildRequire hal
- Update icon themes

* Wed May 17 2006 Matthias Clasen <mclasen@redhat.com> - 1.5.1-1
- Update to 1.5.1

* Wed Apr 19 2006 Matthias Clasen <mclasen@redhat.com> - 1.4.0-3
- Add missing BuildRequires (#181304)

* Tue Mar 14 2006 Ray Strode <rstrode@redhat.com> - 1.4.0-2
- Update to 1.4.0

* Mon Mar 13 2006 Matthias Clasen <mclasen@redhat.com> - 1.4.0-1
- Update to 1.4.0

* Tue Feb 28 2006 Matthias Clasen <mclasen@redhat.com> - 1.3.92-1
- Update to 1.3.92

* Mon Feb 13 2006 Matthias Clasen <mclasen@redhat.com> - 1.3.91-1
- Update to 1.3.91

* Fri Feb 10 2006 Jesse Keating <jkeating@redhat.com> - 1.3.90-2.1
- bump again for double-long bug on ppc(64)

* Thu Feb  9 2006 Matthias Clasen <mclasen@redhat.com> - 1.3.90-2
- Rebuild

* Tue Feb 07 2006 Jesse Keating <jkeating@redhat.com> - 1.3.90-1.1
- rebuilt for new gcc4.1 snapshot and glibc changes

* Mon Jan 30 2006 Matthias Clasen <mclasen@redhat.com> - 1.3.90-1
- Update to 1.3.90

* Fri Jan 20 2006 Matthias Clasen <mclasen@redhat.com> - 1.3.1-1
- Update to 1.3.1

* Fri Jan 06 2006 John (J5) Palmieri <johnp@redhat.com> 1.3.0-3
- Build with gstreamer 0.10
- Enable the mozilla plugin

* Thu Jan 05 2006 John (J5) Palmieri <johnp@redhat.com> 1.3.0-2
- GStreamer has been split into gstreamer08 and gstreamer (0.10) packages
  we need gstreamer08 for now

* Tue Dec 20 2005 Matthias Clasen <mclasen@redhat.com> 1.3.0-1
- Update to 1.3.0

* Thu Dec 15 2005 Matthias Clasen <mclasen@redhat.com> 1.2.1-1
- Update to 1.2.1

* Fri Dec 09 2005 Jesse Keating <jkeating@redhat.com>
- rebuilt

* Wed Oct 26 2005 John (J5) Palmieri <johnp@redhat.com> - 1.2.0-1
- Update to 1.2.0

* Tue Oct 25 2005 Matthias Clasen <mclasen@redhat.com> - 1.1.5-1
- Update to 1.1.5

* Thu Aug 18 2005 John (J5) Palmieri <johnp@redhat.com> - 1.1.4-1
- Update to upstream version 1.1.4 and rebuild
- Don't build with nautilus-cd-burner on s390 platforms

* Fri Jul 22 2005 Colin Walters <walters@redhat.com> - 1.1.3-1
- Update to upstream version 1.1.2

* Wed Jun 29 2005 John (J5) Palmieri <johnp@redhat.com> - 1.1.2-1
- Update to upstream version 1.1.2

* Tue May 17 2005 John (J5) Palmieri <johnp@redhat.com> - 1.0.2-1
- Update to upstream version 1.0.2 to fix minor bugs
- Register the thumbnail and handlers schemas

* Tue Mar 29 2005 John (J5) Palmieri <johnp@redhat.com> - 1.0.1-1
- Update to upstream version 1.0.1
- Break out devel package

* Mon Feb 21 2005 Bill Nottingham <notting@redhat.com> - 0.101-4
- fix %%post

* Wed Feb  2 2005 Matthias Clasen <mclasen@redhat.com> - 0.101-3
- Obsolete nautilus-media
- Install property page and thumbnailer

* Wed Feb  2 2005 Matthias Clasen <mclasen@redhat.com> - 0.101-2
- Update to 0.101
 
* Mon Jan 03 2005 Colin Walters <walters@redhat.com> - 0.100-2
- Grab patch totem-0.100-desktopfile.patch from CVS to fix
  missing menu entry (144088)
- Remove workaround for desktop file being misinstalled, fixed
  by above patch

* Mon Jan 03 2005 Colin Walters <walters@redhat.com> - 0.100-1
- New upstream version 0.100

* Sun Dec  5 2004 Bill Nottingham <notting@redhat.com> - 0.99.22-1
- update to 0.99.22

* Thu Oct 28 2004 Colin Walters <walters@redhat.com> - 0.99.19-2
- Add patch to remove removed items from package from help

* Thu Oct 14 2004 Colin Walters <walters@redhat.com> - 0.99.19-1
- New upstream 0.99.19
  - Fixes crasher with CD playback (see NEWS)

* Tue Oct 12 2004 Alexander Larsson <alexl@redhat.com> - 0.99.18-2
- Call update-desktop-database in post

* Tue Oct 12 2004 Alexander Larsson <alexl@redhat.com> - 0.99.18-1
- update to 0.99.18

* Wed Oct  6 2004 Alexander Larsson <alexl@redhat.com> - 
- Initial version, based on specfile by Matthias Saou <http://freshrpms.net/>

