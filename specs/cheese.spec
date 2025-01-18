%global tarball_version %%(echo %{version} | tr '~' '.')

Name:           cheese
Epoch:          2
Version:        44.1
Release:        8%{?dist}
Summary:        Application for taking pictures and movies from a webcam

License:        GPL-2.0-or-later
URL:            https://wiki.gnome.org/Apps/Cheese
Source0:        https://download.gnome.org/sources/%{name}/44/%{name}-%{tarball_version}.tar.xz
Patch0: cheese-c99.patch
# https://gitlab.gnome.org/GNOME/cheese/-/merge_requests/73
# https://gitlab.gnome.org/GNOME/cheese/-/issues/183
# https://bugzilla.redhat.com/show_bug.cgi?id=2315884
# Fix crash on startup due to invalid JSON
Patch1: 73.patch

BuildRequires:  gcc
BuildRequires:  meson
BuildRequires:  gtk-doc
BuildRequires:  desktop-file-utils
BuildRequires:  docbook-dtds
BuildRequires:  docbook-style-xsl
BuildRequires:  gettext
BuildRequires:  itstool
BuildRequires:  libXtst-devel
BuildRequires:  vala
BuildRequires:  pkgconfig(clutter-1.0)
BuildRequires:  pkgconfig(clutter-gst-3.0)
BuildRequires:  pkgconfig(clutter-gtk-1.0)
BuildRequires:  pkgconfig(gdk-pixbuf-2.0)
BuildRequires:  pkgconfig(gio-2.0)
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(gnome-desktop-3.0) >= 3.27.90
BuildRequires:  pkgconfig(gobject-introspection-1.0)
BuildRequires:  pkgconfig(gtk+-3.0)
BuildRequires:  pkgconfig(gstreamer-pbutils-1.0)
BuildRequires:  pkgconfig(gstreamer-plugins-bad-1.0)
BuildRequires:  pkgconfig(libcanberra-gtk3)
BuildRequires:  pkgconfig(x11)
BuildRequires:  /usr/bin/appstream-util
BuildRequires:  /usr/bin/xsltproc

Requires: %{name}-libs%{?_isa} = %{epoch}:%{version}-%{release}
Requires: gstreamer1-plugins-good%{?_isa}
Requires: gstreamer1-plugins-bad-free%{?_isa}
Requires: gnome-video-effects

%description
Cheese is a Photobooth-inspired GNOME application for taking pictures and
videos from a webcam. It can also apply fancy graphical effects.

%package libs
Summary:        Webcam display and capture widgets
License:        GPL-2.0-or-later
# Camera service was removed upstream in 3.25.90
Obsoletes: cheese-camera-service < 2:3.25.90

%description libs
This package contains libraries needed for applications that
want to display a webcam in their interface.

%package libs-devel
Summary:        Development files for %{name}-libs
License:        GPL-2.0-or-later
Requires:       %{name}-libs%{?_isa} = %{epoch}:%{version}-%{release}

%description libs-devel
This package contains the libraries and header files that are needed
for writing applications that require a webcam display widget.


%prep
%autosetup -p1 -n %{name}-%{tarball_version}
# Trigger recompilation of all Vala sources.
find -name '*.vala' -exec touch {} \;

%build
%meson -Dtests=false
%meson_build


%install
%meson_install

%find_lang %{name} --with-gnome


%check
desktop-file-validate %{buildroot}%{_datadir}/applications/org.gnome.Cheese.desktop
%meson_test


%files
%doc AUTHORS README
%{_bindir}/cheese
%{_datadir}/applications/org.gnome.Cheese.desktop
%{_datadir}/metainfo/org.gnome.Cheese.appdata.xml
%{_datadir}/dbus-1/services/org.gnome.Cheese.service
%{_datadir}/icons/hicolor/scalable/apps/org.gnome.Cheese.svg
%{_datadir}/icons/hicolor/symbolic/apps/org.gnome.Cheese-symbolic.svg
%{_mandir}/man1/cheese.1*

%files -f %{name}.lang libs
%license COPYING
%{_libdir}/libcheese.so.8*
%{_libdir}/libcheese-gtk.so.25*
%{_datadir}/glib-2.0/schemas/org.gnome.Cheese.gschema.xml
%{_libdir}/girepository-1.0/Cheese-3.0.typelib

%files libs-devel
%{_libdir}/libcheese.so
%{_libdir}/libcheese-gtk.so
%{_includedir}/cheese/
%{_datadir}/gtk-doc/
%{_libdir}/pkgconfig/cheese.pc
%{_libdir}/pkgconfig/cheese-gtk.pc
%{_datadir}/gir-1.0/Cheese-3.0.gir


%changelog
* Thu Jan 16 2025 Fedora Release Engineering <releng@fedoraproject.org> - 2:44.1-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Tue Oct 01 2024 Adam Williamson <awilliam@redhat.com> - 2:44.1-7
- Backport MR #73 to fix a crash on startup with recent json-glib

* Wed Jul 17 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2:44.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Sat May 25 2024 Fabio Valentini <decathorpe@gmail.com> - 2:44.1-5
- Rebuild for gstreamer-plugins-bad 1.24.

* Tue Jan 23 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2:44.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Florian Weimer <fweimer@redhat.com> - 2:44.1-3
- GCC 14 compatiblity fixes & Vala rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2:44.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Mon Jul 24 2023 Kalev Lember <klember@redhat.com> - 2:44.1-1
- Update to 44.1

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2:44.0.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Wed May 31 2023 Kalev Lember <klember@redhat.com> - 2:44.0.1-1
- Update to 44.0.1

* Mon Apr 10 2023 David King <amigadave@amigadave.com> - 44.0-1
- Update to 44.0

* Wed Jan 18 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2:43~alpha-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Wed Jul 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2:43~alpha-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Tue Jul 19 2022 Kalev Lember <klember@redhat.com> - 2:43~alpha-1
- Update to 43.alpha
- Remove ldconfig_scriptlets use
- Remove some leftover from autotools build
- Tighten soname globs

* Wed Jan 19 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2:41.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Mon Nov 15 2021 David King <amigadave@amigadave.com> - 2:41.1-1
- Update to 41.1

* Mon Sep 20 2021 David King <amigadave@amigadave.com> - 2:41.0-1
- Update to 41.0

* Wed Jul 28 2021 David King <amigadave@amigadave.com> - 2:3.38.0-5
- Add isa to gstreamer plugin Requires (#1986432)

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2:3.38.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2:3.38.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Fri Sep 18 2020 Bastien Nocera <bnocera@redhat.com> - 3.38.0-2
+ cheese-3.38.0-2
- Fix infinite loop on exit

* Tue Sep 15 2020 Kalev Lember <klember@redhat.com> - 2:3.38.0-1
- Update to 3.38.0

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2:3.34.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2:3.34.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jan 16 2020 Kalev Lember <klember@redhat.com> - 2:3.34.0-2
- Rebuilt for libgnome-desktop soname bump

* Tue Sep 10 2019 David King <amigadave@amigadave.com> - 2:3.34.0-1
- Update to 3.34.0

* Tue Aug 06 2019 Phil Wyett <philwyett@kathenas.org> - 2:3.33.90.1-1
- Convert to using meson build system.
- Update to 3.33.90.1.

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2:3.32.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Jul 21 2019 Kalev Lember <klember@redhat.com> - 2:3.32.1-2
- Rebuilt for libgnome-desktop soname bump

* Mon Apr 08 2019 Kalev Lember <klember@redhat.com> - 2:3.32.1-1
- Update to 3.32.1

* Tue Mar 12 2019 David King <amigadave@amigadave.com> - 2:3.32.0-1
- Update to 3.32.0

* Mon Feb 04 2019 David King <amigadave@amigadave.com> - 2:3.31.90-1
- Update to 3.31.90

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2:3.30.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Sep 07 2018 Kalev Lember <klember@redhat.com> - 2:3.30.0-2
- Rebuilt against fixed atk (#1626575)

* Tue Sep 04 2018 David King <amigadave@amigadave.com> - 2:3.30.0-1
- Update to 3.30.0

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2:3.28.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Mon Mar 12 2018 Kalev Lember <klember@redhat.com> - 2:3.28.0-1
- Update to 3.28.0

* Tue Feb 13 2018 Björn Esser <besser82@fedoraproject.org> - 2:3.26.0-6
- Rebuild against newer gnome-desktop3 package, again

* Sat Feb 10 2018 Bastien Nocera <bnocera@redhat.com> - 2:3.26.0-5
- Rebuild against newer gnome-desktop3 package

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2:3.26.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Sat Feb 03 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 2:3.26.0-3
- Switch to %%ldconfig_scriptlets

* Fri Jan 05 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 2:3.26.0-2
- Remove obsolete scriptlets

* Mon Sep 11 2017 David King <amigadave@amigadave.com> - 2:3.26.0-1
- Update to 3.26.0

* Tue Aug 08 2017 David King <amigadave@amigadave.com> - 2:3.25.90-1
- Update to 3.25.90

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2:3.24.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2:3.24.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Tue Mar 21 2017 David King <amigadave@amigadave.com> - 2:3.24.0-1
- Update to 3.24.0

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2:3.22.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Oct 12 2016 Kalev Lember <klember@redhat.com> - 2:3.22.1-2
- Minor spec file cleanups

* Mon Oct 10 2016 David King <amigadave@amigadave.com> - 2:3.22.1-1
- Update to 3.22.1

* Tue Sep 20 2016 David King <amigadave@amigadave.com> - 2:3.22.0-1
- Update to 3.22.0

* Tue Sep 13 2016 David King <amigadave@amigadave.com> - 2:3.21.92-1
- Update to 3.21.92

* Tue Jun 21 2016 David King <amigadave@amigadave.com> - 2:3.21.3-1
- Update to 3.21.3

* Mon May 09 2016 David King <amigadave@amigadave.com> - 2:3.20.2-1
- Update to 3.20.2

* Mon Apr 11 2016 David King <amigadave@amigadave.com> - 2:3.20.1-1
- Update to 3.20.1

* Tue Mar 22 2016 David King <amigadave@amigadave.com> - 2:3.20.0-1
- Update to 3.20.0

* Tue Feb 16 2016 David King <amigadave@amigadave.com> - 2:3.19.90-1
- Update to 3.19.90

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 2:3.18.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Tue Oct 13 2015 David King <amigadave@amigadave.com> - 2:3.18.1-1
- Update to 3.18.1

* Tue Sep 22 2015 David King <amigadave@amigadave.com> - 2:3.18.0-1
- Update to 3.18.0

* Mon Sep 14 2015 David King <amigadave@amigadave.com> - 2:3.17.92-1
- Update to 3.17.92

* Tue Sep 01 2015 David King <amigadave@amigadave.com> - 2:3.17.91-1
- Update to 3.17.91

* Mon Aug 17 2015 Kalev Lember <klember@redhat.com> - 2:3.17.90-1
- Update to 3.17.90
- Use make_install macro

* Wed Jul 22 2015 David King <amigadave@amigadave.com> - 2:3.17.1-3
- Bump for new gnome-desktop3

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2:3.17.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Fri May 15 2015 Matthias Clasen <mclasen@redhat.com>
- Tighten up inter-subpackage deps to pacify rpmdiff

* Tue Apr 28 2015 David King <amigadave@amigadave.com> - 2:3.17.1-1
- Update to 3.17.1

* Mon Apr 13 2015 David King <amigadave@amigadave.com> - 2:3.16.1-1
- Update to 3.16.1

* Wed Apr 01 2015 David King <amigadave@amigadave.com> - 2:3.16.0-3
- Drop old AppData screenshots

* Mon Mar 30 2015 Richard Hughes <rhughes@redhat.com> - 2:3.16.0-2
- Use better AppData screenshots

* Tue Mar 24 2015 David King <amigadave@amigadave.com> - 2:3.16.0-1
- Update to 3.16.0

* Mon Mar 16 2015 David King <amigadave@amigadave.com> - 2:3.15.92-1
- Update to 3.15.92

* Mon Feb 16 2015 David King <amigadave@amigadave.com> - 2:3.15.90-1
- Update to 3.15.90
- Use license macro for COPYING

* Tue Jan 20 2015 Richard Hughes <rhughes@redhat.com> - 2:3.15.4-1
- Update to 3.15.4

* Thu Jan 08 2015 David King <amigadave@amigadave.com> - 2:3.15.3-2
- Update man page glob in files section

* Mon Dec 15 2014 David King <amigadave@amigadave.com> - 2:3.15.3-1
- Update to 3.15.3

* Mon Nov 24 2014 David King <amigadave@amigadave.com> - 2:3.15.2-1
- Update to 3.15.2
- Depend on appstream-util at build time for AppData check

* Mon Oct 27 2014 David King <amigadave@amigadave.com> - 2:3.15.1-1
- Update to 3.15.1

* Mon Oct 13 2014 David King <amigadave@amigadave.com> - 2:3.14.1-1
- Update to 3.14.1

* Tue Sep 23 2014 David King <amigadave@amigadave.com> - 2:3.14.0-1
- Update to 3.14.0

* Mon Sep 15 2014 David King <amigadave@amigadave.com> - 2:3.13.92-1
- Update to 3.13.92
- Split camera service out to a subpackage
- Use pkgconfig for BuildRequires
- Tidy spec file

* Tue Sep 09 2014 David King <amigadave@amigadave.com> - 2:3.13.90.1-2
- Fix crash when showing photo countdown (#1133394)

* Tue Aug 19 2014 Kalev Lember <kalevlember@gmail.com> - 2:3.13.90.1-1
- Update to 3.13.90.1

* Sat Aug 16 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2:3.13.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Tue Jul 22 2014 Kalev Lember <kalevlember@gmail.com> - 2:3.13.4-2
- Rebuilt for gobject-introspection 1.41.4

* Mon Jul 21 2014 Kalev Lember <kalevlember@gmail.com> - 2:3.13.4-1
- Update to 3.13.4

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2:3.13.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Tue Apr 29 2014 Richard Hughes <rhughes@redhat.com> - 2:3.13.1-1
- Update to 3.13.1

* Tue Apr 15 2014 Kalev Lember <kalevlember@gmail.com> - 2:3.12.1-1
- Update to 3.12.1
- Use desktop-file-validate instead of desktop-file-install

* Tue Mar 25 2014 Kalev Lember <kalevlember@gmail.com> - 2:3.12.0-1
- Update to 3.12.0

* Tue Mar 18 2014 Richard Hughes <rhughes@redhat.com> - 2:3.11.92-1
- Update to 3.11.92

* Wed Mar 05 2014 Richard Hughes <rhughes@redhat.com> - 2:3.11.91-1
- Update to 3.11.91

* Thu Feb 20 2014 Kalev Lember <kalevlember@gmail.com> - 2:3.11.90-3
- Rebuilt for cogl soname bump

* Wed Feb 19 2014 Richard Hughes <rhughes@redhat.com> - 2:3.11.90-2
- Rebuilt for gnome-desktop soname bump

* Tue Feb 18 2014 Richard Hughes <rhughes@redhat.com> - 2:3.11.90-1
- Update to 3.11.90

* Mon Feb 10 2014 Peter Hutterer <peter.hutterer@redhat.com> - 2:3.11.5-3
- Rebuild for libevdev soname bump

* Wed Feb 05 2014 Richard Hughes <rhughes@redhat.com> - 2:3.11.5-2
- Rebuilt for cogl soname bump

* Tue Feb 04 2014 Richard Hughes <rhughes@redhat.com> - 2:3.11.5-1
- Update to 3.11.5

* Tue Jan 14 2014 Richard Hughes <rhughes@redhat.com> - 2:3.11.3-1
- Update to 3.11.3

* Wed Oct 30 2013 Richard Hughes <rhughes@redhat.com> - 2:3.11.1-1
- Update to 3.11.1

* Mon Oct 28 2013 Richard Hughes <rhughes@redhat.com> - 2:3.10.1-1
- Update to 3.10.1

* Wed Sep 25 2013 Kalev Lember <kalevlember@gmail.com> - 2:3.10.0-1
- Update to 3.10.0

* Wed Sep 18 2013 Hans de Goede <hdegoede@redhat.com> - 2:3.9.92-1
- Update to 3.9.92

* Thu Sep 12 2013 Hans de Goede <hdegoede@redhat.com> - 2:3.9.91-3
- In F-19 we had a long list of bugfix patches, most of these have been merged
  into gnome-3.10 but not all have been merged yet, re-add the non merged ones
- Fix video recording not working
- Allow changing effects while recording
- Disallow changing camera settings while recording
- Fix cheese misbehavior when going from 0 -> 1 or 1 -> 0 camera devices

* Tue Sep 03 2013 Kalev Lember <kalevlember@gmail.com> - 2:3.9.91-2
- Rebuilt for libgnome-desktop soname bump

* Tue Sep 03 2013 Kalev Lember <kalevlember@gmail.com> - 2:3.9.91-1
- Update to 3.9.91

* Thu Aug 22 2013 Kalev Lember <kalevlember@gmail.com> - 2:3.9.90-1
- Update to 3.9.90

* Fri Aug 09 2013 Kalev Lember <kalevlember@gmail.com> - 2:3.9.5-1
- Update to 3.9.5

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2:3.9.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Tue Jul 16 2013 Richard Hughes <rhughes@redhat.com> - 2:3.9.4-1
- Update to 3.9.4

* Fri Jun 21 2013 Kalev Lember <kalevlember@gmail.com> - 2:3.9.3-1
- Update to 3.9.3
- Drop unused mx and libgee build deps

* Mon Jun 17 2013 Hans de Goede <hdegoede@redhat.com> - 2:3.9.2-2
- Fix cheese-introduction.png being in both cheese and cheese-libs (#893756)
- Put the COPYING file in the docs for cheese-libs (#893800)

* Sun Jun 02 2013 Kalev Lember <kalevlember@gmail.com> - 2:3.9.2-1
- Update to 3.9.2

* Sat May 04 2013 Kalev Lember <kalevlember@gmail.com> - 2:3.9.1-1
- Update to 3.9.1

* Mon Apr 15 2013 Kalev Lember <kalevlember@gmail.com> - 2:3.8.1-1
- Update to 3.8.1

* Tue Mar 26 2013 Kalev Lember <kalevlember@gmail.com> - 2:3.8.0-1
- Update to 3.8.0

* Wed Mar 20 2013 Kalev Lember <kalevlember@gmail.com> - 2:3.7.92-2
- Rebuilt for clutter-gtk soname bump

* Wed Mar 20 2013 Richard Hughes <rhughes@redhat.com> - 2:3.7.92-1
- Update to 3.7.92

* Wed Mar  6 2013 Matthias Clasen <mclasen@redhat.com> - 2:3.7.91-1
- Update to 3.7.91

* Thu Feb 21 2013 Kalev Lember <kalevlember@gmail.com> - 2:3.7.90-3
- Rebuilt for cogl soname bump

* Wed Feb 20 2013 Kalev Lember <kalevlember@gmail.com> - 2:3.7.90-2
- Rebuilt for libgnome-desktop soname bump

* Tue Feb 19 2013 Richard Hughes <rhughes@redhat.com> - 2:3.7.90-1
- Update to 3.7.90

* Fri Jan 25 2013 Peter Robinson <pbrobinson@fedoraproject.org> 2:3.7.4-2
- Rebuild for new cogl

* Wed Jan 16 2013 Richard Hughes <hughsient@gmail.com> - 2:3.7.4-1
- Update to 3.7.4

* Thu Dec 20 2012 Kalev Lember <kalevlember@gmail.com> - 2:3.7.3-1
- Update to 3.7.3

* Tue Nov 13 2012 Kalev Lember <kalevlember@gmail.com> - 2:3.6.2-1
- Update to 3.6.2

* Wed Oct 17 2012 Kalev Lember <kalevlember@gmail.com> - 2:3.6.1-1
- Update to 3.6.1

* Tue Sep 25 2012 Richard Hughes <hughsient@gmail.com> - 2:3.6.0-1
- Update to 3.6.0

* Wed Sep 19 2012 Richard Hughes <hughsient@gmail.com> - 2:3.5.92-1
- Update to 3.5.92

* Thu Sep  6 2012 Matthias Clasen <mclasen@redhat.com> - 2:3.5.91-1
- Update to 3.5.91
- Drop upstreamed patches

* Tue Aug 28 2012 Matthias Clasen <mclasen@redhat.com> - 2:3.5.5-2
- Rebuild against new cogl/clutter

* Wed Aug 22 2012 Hans de Goede <hdegoede@redhat.com> - 2:3.5.5-1
- New upstream release 3.5.5
- Fix cheese crashing on tvcards which report they can capture 0x0 as
  minimum resolution (rhbz#850505)

* Tue Aug 21 2012 Brian Pepple <bpepple@fedoraproject.org> - 2:3.5.2-6
- Rebuild for new libcogl.

* Fri Jul 27 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2:3.5.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Tue Jun 19 2012 Hans de Goede <hdegoede@redhat.com> - 2:3.4.2-3
- Reduce camerabin pipeline creation time (rhbz#797188, gnome#677731)
- Don't add 0 byte sized files to the thumb-view (rhbz#830166, gnome#677735)
- Fix sizing of horizontal thumbnail list (rhbz#829957)
- Optimize encoding parameters (rhbz#572169)

* Wed Jun 13 2012 Owen Taylor <otaylor@redhat.com> - 2:3.5.2-3
- Require matching version of cheese-libs for cheese

* Thu Jun 07 2012 Matthias Clasen <mclasen@redhat.com> - 2:3.5.2-2
- Rebuild against new gnome-desktop

* Thu Jun 07 2012 Richard Hughes <hughsient@gmail.com> - 2:3.5.2-1
- Update to 3.5.2

* Tue Jun  5 2012 Hans de Goede <hdegoede@redhat.com> - 2:3.5.1-2
- Fix missing images on buttons, also fixes the "Gtk-WARNING **: Attempting to
  add a widget with type GtkImage to a GtkButton ..." warnings (gnome#677543)
- Fix cheese crashing when started on machines with v4l2 radio or vbi devices
  (rhbz#810429, gnome#677544)

* Sun May 06 2012 Kalev Lember <kalevlember@gmail.com> - 2:3.5.1-1
- Update to 3.5.1

* Tue Apr 17 2012 Kalev Lember <kalevlember@gmail.com> - 2:3.4.1-1
- Update to 3.4.1

* Tue Mar 27 2012 Richard Hughes <hughsient@gmail.com> - 2:3.4.0-1
- Update to 3.4.0

* Wed Mar 14 2012 Brian Pepple <bpepple@fedoraproject.org> - 2:3.3.5-2
- Rebuild for new cogl

* Tue Feb  7 2012 Matthias Clasen <mclasen@redhat.com> - 2:3.3.5-1
- Update to 3.3.5

* Tue Jan 17 2012 Matthias Clasen <mclasen@redhat.com> - 2:3.3.4-1
- Update to 3.3.4

* Mon Jan 16 2012 Matthias Clasen <mclasen@redhat.com> - 2:3.3.3-3
- Add a BuildRequires for itstool

* Thu Jan 12 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2:3.3.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Wed Dec 21 2011 Matthias Clasen <mclasen@redhat.com> - 2:3.3.3-1
- Update to 3.3.3

* Thu Nov 24 2011 Matthias Clasen <mclasen@redhat.com> - 1:3.3.2-2
- Rebuild against new clutter

* Tue Nov 22 2011 Tomas Bzatek <tbzatek@redhat.com> - 1:3.3.2-1
- Update to 3.3.2

* Wed Nov  2 2011 Matthias Clasen <mclasen@redhat.com> - 1:3.3.1-1
- Update to 3.3.1-1

* Wed Oct 26 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1:3.2.1-2
- Rebuilt for glibc bug#747377

* Tue Oct 18 2011 Matthias Clasen <mclasen@redhat.com> - 1:3.2.1-1
- Update to 3.2.1

* Thu Sep 29 2011 Hans de Goede <hdegoede@redhat.com> - 1:3.2.0-2
- Add Requires: gstreamer-plugins-bad-free for the camerabin element (#717872)

* Tue Sep 27 2011 Ray <rstrode@redhat.com> - 1:3.2.0-1
- Update to 3.2.0

* Wed Sep 21 2011 Brian Pepple <bpepple@fedoraproject.org> - 1:3.1.92-2
- Rebuld for new libcogl.
- Use old libgee api.

* Tue Sep 20 2011 Matthias Clasen <mclasen@redhat.com> - 1:3.1.92-1
- Update to 3.1.92

* Tue Sep  6 2011 Matthias Clasen <mclasen@redhat.com> - 1:3.1.91.1-1
- Update to 3.1.91.1

* Tue Jul 26 2011 Matthias Clasen <mclasen@redhat.com> - 1:3.0.2-2
- Rebuild

* Mon Jul 25 2011 Matthias Clasen <mclasen@redhat.com> - 1:3.0.2-1
- Update to 3.0.2

* Wed Jun 29 2011 Julian Sikorski <belegdol@fedoraproject.org> - 1:3.0.1-3
- Removed RPATHS (RH #703636)

* Wed Jun 15 2011 Bastien Nocera <bnocera@redhat.com> 3.0.1-2
- Rebuild against newest gnome-desktop3

* Tue Apr 26 2011 Matthias Clasen <mclasen@redhat.com> 1:3.0.1-1
- Update to 3.0.1

* Tue Apr  5 2011 Matthias Clasen <mclasen@redhat.com> 1:3.0.0-2
- Add newer icons from upstream

* Mon Apr  4 2011 Christopher Aillon <caillon@redhat.com> 1:3.0.0-1
- Update to 3.0

* Wed Mar 30 2011 Alexander Larsson <alexl@redhat.com> - 1:2.91.93-3
- Move gsettings schema to cheese-libs, fixes control-center crash (#691667)
- Move typelib to cheese-libs

* Mon Mar 28 2011 Bastien Nocera <bnocera@redhat.com> 2.91.93-2
- Add missing gnome-video-effects dependency

* Fri Mar 25 2011 Bastien Nocera <bnocera@redhat.com> 2.91.93-1
- Update to 2.91.93

* Tue Mar 22 2011 Matthias Clasen <mclasen@redhat.com> 1:2.91.92-1
- Update to 2.91.92

* Sat Mar 12 2011 Bastien Nocera <bnocera@redhat.com> 2.91.91.1-1
- Update to 2.91.91.1

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1:2.91.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Wed Feb  2 2011 Christopher Aillon <caillon@redhat.com> 1:2.91.4-1
- Update to 2.91.4

* Mon Jan 10 2011 Matthias Clasen <mclasen@redhat.com> 1:2.91.3-1
- Update to 2.91.3

* Thu Sep 30 2010 Matthias Clasen <mclasen@redhat.com> 1:2.32.0-1
- Update to 2.32.0

* Tue Aug 31 2010 Matthias Clasen <mclasen@redhat.com> 1:2.31.91-1
- Update to 2.31.91

* Mon Aug 23 2010 Matthias Clasen <mclasen@redhat.com> 1:2.31.90-2
- Co-own /usr/share/gtk-doc

* Thu Aug 19 2010 Matthias Clasen <mclasen@redhat.com> 1:2.31.90-1
- Update to 2.31.90

* Wed Aug 11 2010 Matthias Clasen <mclasen@redhat.com> 1:2.31.1-2
- Add an epoch to stay ahead of F14

* Fri Aug  6 2010 Matthias Clasen <mclasen@redhat.com> 2.31.1-1
- Update to 2.31.1

* Tue Apr 27 2010 Matthias Clasen <mclasen@redhat.com> 2.30.1-1
- Update to 2.30.1
- Spec file cleanups

* Mon Mar 29 2010 Matthias Clasen <mclasen@redhat.com> 2.30.0-1
- Update to 2.30.0

* Wed Mar 24 2010 Bastien Nocera <bnocera@redhat.com> 2.29.92-4
- Fix possible crasher when countdown reaches zero

* Fri Mar 19 2010 Matthias Clasen <mclasen@redhat.com> 2.29.92-3
- Fix text rendering issues on the effects tab

* Tue Mar 16 2010 Matthias Clasen <mclasen@redhat.com> 2.29.92-2
- Use an existing icon

* Tue Mar 09 2010 Bastien Nocera <bnocera@redhat.com> 2.29.92-1
- Update to 2.29.92

* Tue Feb 09 2010 Bastien Nocera <bnocera@redhat.com> 2.29.90-2
- Fix include path, and missing requires for the pkg-config file

* Tue Feb 09 2010 Bastien Nocera <bnocera@redhat.com> 2.29.90-1
- Update to 2.29.90

* Sun Jan 17 2010 Matthias Clasen  <mclasen@redhat.com> 2.29.5-2
- Rebuild

* Tue Jan 12 2010 Matthias Clasen  <mclasen@redhat.com> 2.29.5-1
- Update to 2.29.5

* Sun Sep 27 2009 Orcan Ogetbil <oget[DOT]fedora[AT]gmail[DOT]com> 2.28.0-2
- Update desktop file according to F-12 FedoraStudio feature

* Mon Sep 21 2009 Matthias Clasen  <mclasen@redhat.com> 2.28.0-1
- Update to 2.28.0

* Mon Sep  7 2009 Matthias Clasen  <mclasen@redhat.com> 2.27.92-1
- Update to 2.27.92

* Mon Aug 24 2009 Matthias Clasen  <mclasen@redhat.com> 2.27.91-1
- Update to 2.27.91

* Sat Aug 22 2009 Matthias Clasen  <mclasen@redhat.com> 2.27.90-3
- Update sensitivity of menu items

* Fri Aug 14 2009 Matthias Clasen  <mclasen@redhat.com> 2.27.90-2
- Fix schemas file syntax

* Tue Aug 11 2009 Matthias Clasen  <mclasen@redhat.com> 2.27.90-1
- Update to 2.27.90

* Tue Jul 28 2009 Matthias Clasen  <mclasen@redhat.com> 2.27.5-1
- Update to 2.27.5

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.27.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Mon Jul 13 2009 Matthias Clasen  <mclasen@redhat.com> 2.27.4-1
- Update to 2.27.4

* Tue Jun 16 2009 Matthias Clasen  <mclasen@redhat.com> 2.27.3-1
- Update to 2.27.3

* Sun May 31 2009 Matthias Clasen  <mclasen@redhat.com> 2.27.2-1
- Update to 2.27.2

* Fri May 15 2009 Matthias Clasen  <mclasen@redhat.com> 2.27.1-1
- Update to 2.27.1

* Mon Mar 16 2009 Matthias Clasen  <mclasen@redhat.com> 2.26.0-1
- Update to 2.26.0

* Mon Mar  2 2009 Matthias Clasen  <mclasen@redhat.com> 2.25.92-1
- Update to 2.25.92

* Mon Feb 23 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.25.91-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Wed Feb 18 2009 Matthias Clasen  <mclasen@redhat.com> 2.25.91-1
- Update to 2.25.91

* Tue Feb  3 2009 Matthias Clasen  <mclasen@redhat.com> 2.25.90-1
- Update to 2.25.90

* Tue Jan  6 2009 Matthias Clasen  <mclasen@redhat.com> 2.25.4-1
- Update to 2.25.4

* Wed Dec 17 2008 Matthias Clasen  <mclasen@redhat.com> 2.25.3-1
- Update to 2.25.3

* Wed Dec  3 2008 Matthias Clasen  <mclasen@redhat.com> 2.25.2-1
- Update to 2.25.2

* Fri Nov 21 2008 Matthias Clasen  <mclasen@redhat.com> 2.25.1-4
- Better URL

* Thu Nov 13 2008 Matthias Clasen  <mclasen@redhat.com> 2.25.1-3
- Update to 2.25.1

* Sun Nov  9 2008 Hans de Goede <hdegoede@redhat.com> 2.24.1-2
- Fix cams which only support 1 resolution not working (rh470698, gnome560032)

* Mon Oct 20 2008 Matthias Clasen  <mclasen@redhat.com> 2.24.1-1
- Update to 2.24.1

* Wed Oct  8 2008 Matthias Clasen  <mclasen@redhat.com> 2.24.0-2
- Save space

* Mon Sep 22 2008 Matthias Clasen  <mclasen@redhat.com> 2.24.0-1
- Update to 2.24.0

* Tue Sep  9 2008 Matthias Clasen  <mclasen@redhat.com> 2.23.92-3
- Update to 2.23.92
- Drop upstreamed patches

* Wed Sep  3 2008 Hans de Goede <hdegoede@redhat.com> 2.23.91-2
- Fix use with multiple v4l devices (rh 460956, gnome 546868, gnome 547144)

* Tue Sep  2 2008 Matthias Clasen  <mclasen@redhat.com> 2.23.91-1
- Update to 2.23.91

* Fri Aug 22 2008 Matthias Clasen  <mclasen@redhat.com> 2.23.90-1
- Update to 2.23.90

* Tue Aug  5 2008 Matthias Clasen  <mclasen@redhat.com> 2.23.6-1
- Update to 2.23.6

* Tue Jul 22 2008 Matthias Clasen  <mclasen@redhat.com> 2.23.5-1
- Update to 2.23.5

* Wed Jun 18 2008 Matthias Clasen  <mclasen@redhat.com> 2.23.4-1
- Update to 2.23.4

* Tue Jun  3 2008 Matthias Clasen  <mclasen@redhat.com> 2.23.3-1
- Update to 2.23.3

* Tue May 13 2008 Matthias Clasen  <mclasen@redhat.com> 2.23.2-1
- Update to 2.23.2

* Fri Apr 25 2008 Matthias Clasen  <mclasen@redhat.com> 2.23.1-1
- Update to 2.23.1

* Tue Apr 22 2008 Matthias Clasen  <mclasen@redhat.com> 2.22.1-2
- Fix an invalid free

* Mon Apr  7 2008 Matthias Clasen  <mclasen@redhat.com> 2.22.1-1
- Update to 2.22.1

* Mon Mar 10 2008 Matthias Clasen  <mclasen@redhat.com> 2.22.0-1
- Update to 2.22.0

* Tue Feb 26 2008  Matthias Clasen  <mclasen@redhat.com> 2.21.92-1
- Update to 2.21.92

* Fri Feb 15 2008  Matthias Clasen  <mclasen@redhat.com> 2.21.91-3
- Fix a locking problem that causes the UI to freeze

* Fri Feb  8 2008  Matthias Clasen  <mclasen@redhat.com> 2.21.91-2
- Rebuild for gcc 4.3

* Tue Jan 29 2008  Matthias Clasen  <mclasen@redhat.com> 2.21.91-1
- Update to 2.21.91

* Mon Jan 14 2008  Matthias Clasen  <mclasen@redhat.com> 2.21.5-1
- Update to 2.21.5

* Mon Dec 24 2007  Matthias Clasen  <mclasen@redhat.com> 0.3.0-1
- Update to 0.3.0

* Fri Sep  7 2007  Matthias Clasen  <mclasen@redhat.com> 0.2.4-2
- package review feedback

* Thu Sep  6 2007  Matthias Clasen  <mclasen@redhat.com> 0.2.4-1
- Initial packages
