Name:           sound-juicer
Version:        3.40.0
Release:        6%{?dist}
Summary:        Clean and lean CD ripper

# Automatically converted from old format: GPLv2+ - review is highly recommended.
License:        GPL-2.0-or-later
URL:            https://wiki.gnome.org/Apps/SoundJuicer
Source0:        https://download.gnome.org/sources/%{name}/3.40/%{name}-%{version}.tar.xz

BuildRequires:  gcc
BuildRequires:  meson
BuildRequires:  pkgconfig(gmodule-export-2.0)
BuildRequires:  pkgconfig(gsettings-desktop-schemas)
BuildRequires:  pkgconfig(gstreamer-1.0)
BuildRequires:  pkgconfig(gstreamer-plugins-base-1.0)
BuildRequires:  pkgconfig(gstreamer-pbutils-1.0)
BuildRequires:  pkgconfig(gtk+-3.0)
BuildRequires:  pkgconfig(iso-codes)
BuildRequires:  pkgconfig(libbrasero-media3)
BuildRequires:  pkgconfig(libcanberra-gtk3)
BuildRequires:  pkgconfig(libdiscid)
BuildRequires:  pkgconfig(libmusicbrainz5)
BuildRequires:  gstreamer1-plugins-good
BuildRequires:  gettext
BuildRequires:  desktop-file-utils
BuildRequires:  itstool
BuildRequires:  /usr/bin/appstream-util

ExcludeArch:    s390 s390x

Requires:       gstreamer1-plugins-good

%description
GStreamer-based CD ripping tool. Saves audio CDs to Ogg/vorbis.

%prep
%autosetup -p1

%build
%meson
%meson_build

%install
%meson_install

# These are installed to the correct location with the doc macro down below
rm $RPM_BUILD_ROOT%{_datadir}/doc/sound-juicer/AUTHORS
rm $RPM_BUILD_ROOT%{_datadir}/doc/sound-juicer/COPYING
rm $RPM_BUILD_ROOT%{_datadir}/doc/sound-juicer/NEWS
rm $RPM_BUILD_ROOT%{_datadir}/doc/sound-juicer/README.md

%find_lang sound-juicer --with-gnome

%check
appstream-util validate-relax --nonet $RPM_BUILD_ROOT%{_datadir}/metainfo/org.gnome.SoundJuicer.metainfo.xml
desktop-file-validate $RPM_BUILD_ROOT%{_datadir}/applications/org.gnome.SoundJuicer.desktop

%files -f sound-juicer.lang
%doc AUTHORS NEWS README.md
%license COPYING
%{_bindir}/sound-juicer
%{_datadir}/sound-juicer
%{_datadir}/applications/org.gnome.SoundJuicer.desktop
%{_datadir}/dbus-1/services/org.gnome.SoundJuicer.service
%{_datadir}/GConf/gsettings/sound-juicer.convert
%{_datadir}/glib-2.0/schemas/org.gnome.sound-juicer.gschema.xml
%{_datadir}/icons/hicolor/*/apps/org.gnome.SoundJuicer.png
%{_datadir}/metainfo/org.gnome.SoundJuicer.metainfo.xml
%{_mandir}/man1/*

%changelog
* Sun Jan 19 2025 Fedora Release Engineering <releng@fedoraproject.org> - 3.40.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Fri Jul 26 2024 Miroslav Suchý <msuchy@redhat.com> - 3.40.0-5
- convert license to SPDX

* Sat Jul 20 2024 Fedora Release Engineering <releng@fedoraproject.org> - 3.40.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Sat Jan 27 2024 Fedora Release Engineering <releng@fedoraproject.org> - 3.40.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sat Jul 22 2023 Fedora Release Engineering <releng@fedoraproject.org> - 3.40.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Mon Jun 19 2023 Kalev Lember <klember@redhat.com> - 3.40.0-1
- Update to 3.40.0

* Sat Jan 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 3.38.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Sun Aug 14 2022 Hans de Goede <hdegoede@redhat.com> - 3.38.0-6
- Fix FTBFS (rhbz#2113732)

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 3.38.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Sat Jan 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 3.38.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 3.38.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 3.38.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Sat Sep 12 2020 Kalev Lember <klember@redhat.com> - 3.38.0-1
- Update to 3.38.0
- Switch to the meson build system
- Use upstream appdata screenshots

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.24.0-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.24.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.24.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.24.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.24.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.24.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jan 18 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 3.24.0-4
- Remove obsolete scriptlets

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.24.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.24.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Tue Mar 21 2017 Kalev Lember <klember@redhat.com> - 3.24.0-1
- Update to 3.24.0

* Thu Mar 16 2017 Kalev Lember <klember@redhat.com> - 3.23.92-1
- Update to 3.23.92

* Tue Feb 14 2017 Richard Hughes <rhughes@redhat.com> - 3.23.90-1
- Update to 3.23.90

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.22.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Oct 10 2016 Bastien Nocera <bnocera@redhat.com> - 3.22.1-1
+ sound-juicer-3.22.1-1
- Update to 3.22.1

* Mon Sep 19 2016 Kalev Lember <klember@redhat.com> - 3.22.0-1
- Update to 3.22.0

* Wed Sep 14 2016 Kalev Lember <klember@redhat.com> - 3.21.92-1
- Update to 3.21.92

* Thu Aug 18 2016 Kalev Lember <klember@redhat.com> - 3.21.90-1
- Update to 3.21.90
- Modernize the spec file
- Use desktop-file-validate instead of desktop-file-install

* Tue Mar 22 2016 Kalev Lember <klember@redhat.com> - 3.20.0-1
- Update to 3.20.0

* Mon Mar 14 2016 Kalev Lember <klember@redhat.com> - 3.19.92-1
- Update to 3.19.92

* Mon Feb 29 2016 Richard Hughes <rhughes@redhat.com> - 3.19.91-1
- Update to 3.19.91

* Mon Feb 15 2016 David King <amigadave@amigadave.com> - 3.19.90-1
- Update to 3.19.90
- Update URL

* Fri Feb 05 2016 Fedora Release Engineering <releng@fedoraproject.org> - 3.18.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Mon Nov 16 2015 Kalev Lember <klember@redhat.com> - 3.18.1-1
- Update to 3.18.1

* Mon Sep 21 2015 Kalev Lember <klember@redhat.com> - 3.18.0-1
- Update to 3.18.0

* Tue Sep 01 2015 Kalev Lember <klember@redhat.com> - 3.17.91-1
- Update to 3.17.91

* Mon Aug 17 2015 Kalev Lember <klember@redhat.com> - 3.17.90-1
- Update to 3.17.90
- Use make_install macro

* Fri Jun 19 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.16.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Mon Apr 13 2015 David King <amigadave@amigadave.com> - 3.16.1-1
- Update to 3.16.1

* Mon Mar 30 2015 Richard Hughes <rhughes@redhat.com> - 3.16.0-2
- Use better AppData screenshots

* Mon Mar 23 2015 Kalev Lember <kalevlember@gmail.com> - 3.16.0-1
- Update to 3.16.0

* Mon Mar 16 2015 Kalev Lember <kalevlember@gmail.com> - 3.15.92-1
- Update to 3.15.92

* Mon Mar 02 2015 David King <amigadave@amigadave.com> - 3.15.91-1
- Update to 3.15.91
- Use license macro for COPYING
- Validate AppData in check

* Sun Dec 14 2014 David King <amigadave@amigadave.com> - 3.14.0-3
- Stop requiring gtk2 (#1147157)
- Use pkgconfig for BuildRequires

* Thu Nov 27 2014 Haïkel Guémar <hguemar@fedoraproject.org> - 3.14.0-2
- Rebuilt against newer libmusicbrainz5

* Mon Sep 22 2014 Kalev Lember <kalevlember@gmail.com> - 3.14.0-1
- Update to 3.14.0

* Mon Sep 15 2014 Kalev Lember <kalevlember@gmail.com> - 3.13.92-1
- Update to 3.13.92

* Mon Sep 01 2014 Kalev Lember <kalevlember@gmail.com> - 3.13.91-1
- Update to 3.13.91

* Tue Aug 19 2014 Kalev Lember <kalevlember@gmail.com> - 3.13.90-1
- Update to 3.13.90

* Mon Aug 18 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.12.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.12.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Mon May 26 2014 Christophe Fergeau <cfergeau@redhat.com> 3.12.0-1
- Update to sound-juicer 3.12.0

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.5.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Fri Feb 15 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.5.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Fri Oct 26 2012 Bastien Nocera <bnocera@redhat.com> 3.5.0-3
- Another build fix for GStreamer macros

* Wed Aug 29 2012 Bastien Nocera <bnocera@redhat.com> 3.5.0-2
- Add missing run-time Requires
- Remove unneeded cdparanoia dependency

* Wed Aug 22 2012 Richard Hughes <hughsient@gmail.com> - 3.5.0-1
- Update to 3.5.0

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.4.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Wed Mar 28 2012 Richard Hughes <hughsient@gmail.com> - 3.4.0-1
- Update to 3.4.0

* Thu Mar 15 2012 Christophe Fergeau <cfergeau@redhat.com> 3.3.90-1
- Update to 3.3.90

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.32.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Fri Feb 11 2011 Matthias Clasen <mclasen@redhat.com> 2.32.0-7
- Rebuild against newer gtk

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.32.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Wed Feb  2 2011 Matthias Clasen <mclasen@redhat.com> 2.32.0-5
- Rebuild against newer gtk3

* Sun Jan  9 2011 Matthias Clasen <mclasen@redhat.com> 2.32.0-4
- Rebuild against newer gtk3

* Fri Dec  3 2010 Matthias Clasen <mclasen@redhat.com> 2.32.0-3
- Reuild against new gtk

* Fri Nov 12 2010 Adam Williamson <awilliam@redhat.com> 2.32.0-2
- add drawable.patch to fix a build/crasher issue (upstream #631887)
- add profiles.patch to handle rename of gnome-media-profiles (upstream
  #634729)

* Tue Sep 28 2010 Matthias Clasen <mclasen@redhat.com> 2.32.0-1
- Update to 2.32.0

* Mon Sep 20 2010 Matthias Clasen <mclasen@redhat.com> 2.31.6-1
- Update to 2.31.6

* Fri Aug 20 2010 Matthias Clasen <mclasen@redhat.com> 2.31.5-2
- Rebuild against newer brasero

* Tue Jul 13 2010 Matthias Clasen <mclasen@redhat.com> 2.31.5-1
- Update to 2.31.5

* Tue Jul 13 2010 Matthias Clasen <mclasen@redhat.com> 2.28.2-6
- Rebuild against newer brasero

* Fri Jun 25 2010 Bastien Nocera <bnocera@redhat.com> 2.28.2-5
- Add missing desktop-file-utils scriptlet requires

* Sat Jun 12 2010 Matthias Clasen <mclasen@redhat.com> 2.28.2-4
- Fix build

* Fri Jun 11 2010 Matthias Clasen <mclasen@redhat.com> 2.28.2-3
- Rebuild against newer brasero

* Fri May 14 2010 Bastien Nocera <bnocera@redhat.com> 2.28.2-2
- Fix package review bugs

* Tue Mar 30 2010 Matthias Clasen <mclasen@redhat.com> 2.28.2-1
- Update to 2.28.2

* Wed Jan 06 2010 Bastien Nocera <bnocera@redhat.com> 2.28.1-2
- Fix potential musicbrainz crasher

* Wed Nov 25 2009 Bastien Nocera <bnocera@redhat.com> 2.28.1-1
- Update to 2.28.1

* Tue Oct 27 2009 Bastien Nocera <bnocera@redhat.com> 2.28.0-4
- Fix crasher when extracting a CD that's not in musicbrainz (#528297)

* Mon Sep 28 2009 Richard Hughes  <rhughes@redhat.com> - 2.28.0-3
- Apply a patch from upstream to inhibit gnome-session, rather than
  gnome-power-manager. This fixes a warning on rawhide when using sound-juicer.

* Fri Sep 25 2009 Bastien Nocera <bnocera@redhat.com> 2.28.0-2
- Remove old libmusicbrainz BR

* Wed Sep 23 2009 Matthias Clasen <mclasen@redhat.com> - 2.28.0-1
- Update to 2.28.0

* Wed Sep 23 2009 Orcan Ogetbil <oget[DOT]fedora[AT]gmail[DOT]com> - 2.26.1-6
- Update desktop file according to F-12 FedoraStudio feature

* Wed Jul 29 2009 Matthias Clasen <mclasen@redhat.com> - 2.26.1-5
- Drop unneeded direct deps

* Sun Jul 26 2009 Matthias Clasen <mclasen@redhat.com> - 2.26.1-4
- Rebuild to shrink GConf schemas

* Thu May 07 2009 Bastien Nocera <bnocera@redhat.com> 2.26.1-3
- Update patch for #498764

* Thu May 07 2009 Bastien Nocera <bnocera@redhat.com> 2.26.1-2
- Fix gvfs metadata getter crasher (#498764)

* Sun Apr 12 2009 Matthias Clasen <mclasen@redhat.com> - 2.26.1-1
- Update to 2.26.1
- See http://download.gnome.org/sources/sound-juicer/2.26/sound-juicer-2.26.1.news

* Tue Mar 17 2009 Matthias Clasen <mclasen@redhat.com> - 2.26.0-1
- Update to 2.26.0

* Mon Mar 09 2009 - Bastien Nocera <bnocera@redhat.com> - 2.25.92-1
- Update to 2.25.92

* Mon Mar 02 2009 - Bastien Nocera <bnocera@redhat.com> - 2.25.3-3
- Remove nautilus-cd-burner dependency

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.25.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Tue Feb 17 2009 Matthias Clasen <mclasen@redhat.com> - 2.25.3-1
- Update to 2.25.3

* Tue Feb 03 2009 - Bastien Nocera <bnocera@redhat.com> - 2.25.2-1
- Update to 2.25.2
- Use libmusicbrainz3 in addition to the old one, replace ncb dep with brasero
- Remove a lot of GNOME BRs

* Sun Nov 23 2008 Matthias Clasen <mclasen@redhat.com> - 2.25.1-1
- Update to 2.25.1

* Sun Sep 21 2008 Matthias Clasen <mclasen@redhat.com> - 2.24.0-1
- Update to 2.24.0

* Mon Sep 08 2008 - Bastien Nocera <bnocera@redhat.com> - 2.23.3-1
- Update to 2.23.3

* Fri Aug 22 2008 Matthias Clasen <mclasen@redhat.com> - 2.23.2-1
- Update to 2.23.2

* Tue Aug  5 2008 Matthias Clasen <mclasen@redhat.com> - 2.23.1-1
- Update to 2.23.1

* Thu Jul 10 2008 Matthias Clasen <mclasen@redhat.com> - 2.23.0-2
- There is need to BR hal anymore

* Mon Jun 09 2008 - Bastien Nocera <bnocera@redhat.com> - 2.23.0-1
- Update to 2.23.0

* Tue Apr 29 2008 - Bastien Nocera <bnocera@redhat.com> - 2.22.0-3
- Handle URIs from gvfs

* Wed Mar 12 2008 - Bastien Nocera <bnocera@redhat.com> - 2.22.0-2
- Remove the ExcludeArch

* Mon Mar 10 2008 Matthias Clasen <mclasen@redhat.com> - 2.22.0-1
- Update to 2.22.0

* Tue Mar 04 2008 - Bastien Nocera <bnocera@redhat.com> - 2.21.92-2
- ExcludeArch ppc and ppc64 added (#435771)

* Tue Feb 26 2008  Matthias Clasen <mclasen@redhat.com> - 2.21.92-1
- Update to 2.21.92

* Thu Feb 14 2008  Matthias Clasen <mclasen@redhat.com> - 2.21.91-1
- Update to 2.21.91

* Thu Jan 31 2008  Matthias Clasen <mclasen@redhat.com> - 2.21.3-1
- Update to 2.21.3

* Fri Jan 18 2008  Matthias Clasen <mclasen@redhat.com> - 2.21.2-2
- Add content-type support

* Mon Jan 14 2008  Matthias Clasen <mclasen@redhat.com> - 2.21.2-1
- Update to 2.21.2

* Tue Jan 08 2008 - Bastien Nocera <bnocera@redhat.com> - 2.21.1-1
- Update to 2.21.1

* Fri Dec 21 2007 Matthias Clasen <mclasen@redhat.com> - 2.21.0-1
- Update to 2.21.0

* Mon Oct 15 2007 Matthias Clasen <mclasen@redhat.com> - 2.20.1-1
- Update to 2.20.1 (crash fixes)

* Thu Sep 20 2007 - Bastien Nocera <bnocera@redhat.com> - 2.20.0-2
- Fix crasher when editing profiles and the profile gets unref'ed
  (#278861)

* Mon Sep 17 2007 Matthias Clasen <mclasen@redhat.com> - 2.20.0-1
- Update to 2.20.0

* Sat Aug 25 2007 - Bastien Nocera <bnocera@redhat.com> - 2.19.3-3
- Remove work-around for gst-inspect crashing

* Fri Aug 24 2007 Adam Jackson <ajax@redhat.com> - 2.19.3-2
- Rebuild for build ID

* Mon Aug 13 2007 Matthias Clasen <mclasen@redhat.com> - 2.19.3-1
- Update to 2.19.3

* Tue Aug  7 2007 Matthias Clasen <mclasen@redhat.com> - 2.19.2-2
- Update license field
- Use %%find_lang for help files

* Mon Jun 18 2007 Matthias Clasen <mclasen@redhat.com> - 2.19.2-1
- Update to 2.19.2

* Sat May 19 2007 Matthias Clasen <mclasen@redhat.com> - 2.19.1-1
- Update to 2.19.1

* Tue Apr 17 2007 - Bastien Nocera <bnocera@redhat.com> - 2.16.4-1
- Update to 2.16.4 to get xdg-users-dir support, fix #236658, and
  follow the device selection in the control-center

* Tue Feb 20 2007 - Bastien Nocera <bnocera@redhat.com> - 2.16.3-1
- Update to 2.16.3

* Sat Feb  3 2007 Matthias Clasen <mclasen@redhat.com> - 2.16.2-3
- Minor fixes from package review:
 * Remove unnecessary Requires
 * Add URL
 * Correct Source, BuildRoot
 * Fix directory ownership

* Thu Jan 25 2007 Alexander Larsson <alexl@redhat.com> - 2.16.2-2
- Remove hicolor icon theme cache (#223483)

* Tue Dec  5 2006 Matthias Clasen <mclasen@redhat.com> - 2.16.2-1
- Update to 2.16.2

* Sun Oct 22 2006 Matthias Clasen <mclasen@redhat.com> - 2.16.1-1
- Update to 2.16.1

* Wed Oct 18 2006 Matthias Clasen <mclasen@redhat.com> - 2.16.0-2
- Fix scripts according to the packaging guidelines

* Mon Sep  4 2006 Matthias Clasen <mclasen@redhat.com> - 2.16.0-1.fc6
- Update to 2.16.0

* Sun Aug 20 2006 Matthias Clasen <mclasen@redhat.com> - 2.15.5.1-1.fc6
- Update to 2.15.5.1

* Thu Aug  3 2006 Matthias Clasen <mclasen@redhat.com> - 2.15.4-1.fc6
- Update to 2.15.4

* Wed Jul 19 2006 Matthias Clasen <mclasen@redhat.com> - 2.15.3-3
- Rebuild against dbus

* Wed Jul 12 2006 Jesse Keating <jkeating@redhat.com> - 2.15.3-2.1
- rebuild

* Wed Jun 14 2006 Matthias Clasen <mclasen@redhat.com> - 2.15.3-2
- Work around a gstreamer problem

* Wed Jun 14 2006 Matthias Clasen <mclasen@redhat.com> - 2.15.3-1
- Update to 2.15.3

* Sat Jun 10 2006 Matthias Clasen <mclasen@redhat.com> - 2.15.2.1-3
- More missing BuildRequires

* Sat May 20 2006 Matthias Clasen <mclasen@redhat.com> - 2.15.2.1-2
- Add missing BuildRequires (#182174)

* Wed May 17 2006 Matthias Clasen <mclasen@redhat.com> - 2.15.2.1-1
- Update to 2.15.2.1

* Mon Apr 17 2006 Matthias Clasen <mclasen@redhat.com> - 2.14.3-2
- Update to 2.14.3

* Mon Apr 10 2006 Matthias Clasen <mclasen@redhat.com> - 2.14.2-2
- Update to 2.14.2

* Wed Apr  5 2006 Matthias Clasen <mclasen@redhat.com> - 2.14.1-2
- Update to 2.14.1

* Sun Mar 12 2006 Matthias Clasen <mclasen@redhat.com> - 2.14.0-1
- Update to 2.14.0

* Tue Feb 28 2006 Matthias Clasen <mclasen@redhat.com> - 2.13.6-1
- Update to 2.13.6

* Sun Feb 12 2006 Matthias Clasen <mclasen@redhat.com> - 2.13.5-1
- Update to 2.13.5

* Fri Feb 10 2006 Jesse Keating <jkeating@redhat.com> - 2.13.4-3.2
- bump again for double-long bug on ppc(64)

* Tue Feb 07 2006 Jesse Keating <jkeating@redhat.com> - 2.13.4-3.1
- rebuilt for new gcc4.1 snapshot and glibc changes

* Sun Feb  5 2006 Christopher Aillon <caillon@redhat.com> 2.13.4-3
- Fix broken Requires

* Sat Feb  4 2006 Christopher Aillon <caillon@redhat.com> 2.13.4-2
- Update to use gstreamer (0.10)

* Mon Jan 30 2006 Matthias Clasen <mclasen@redhat.com> 2.13.4-1
- Update to 2.13.4

* Mon Jan 09 2006 John (J5) Palmieri <johnp@redhat.com> 2.13.2-1
- Upgrade to 2.13.2

* Mon Jan 09 2006 John (J5) Palmieri <johnp@redhat.com> 2.13.1-4
- Add a patch that adds -Wl,--export-dynamic to the build

* Thu Jan 05 2006 John (J5) Palmieri <johnp@redhat.com> 2.13.1-3
- GStreamer has been split into gstreamer08 and gstreamer (0.10) packages
  we need gstreamer08 for now

* Fri Dec 09 2005 Jesse Keating <jkeating@redhat.com>
- rebuilt

* Fri Dec 02 2005 John (J5) Palmieri <johnp@redhat.com> 2.13.1-2
- Rebuild with new libnautilus-cd-burner

* Wed Aug 17 2005 Matthias Clasen <mclasen@redhat.com> 2.13.1-1
- Update to 2.13.1

* Wed Aug 17 2005 Matthias Clasen <mclasen@redhat.com> 2.11.91-1
- Newer upstream version

* Tue Jul 12 2005 Matthias Clasen <mclasen@redhat.com> 2.11.3-1
- Newer upstream version

* Mon Apr 04 2005 John (J5) Palmieri <johnp@redhat.com> 2.10.1-1
- update to upstream 2.10.1 which should fix crashes when clicking
  extract

* Wed Mar 23 2005 John (J5) Palmieri <johnp@redhat.com> 2.10.0-2
- Rebuild for libmusicbrainz-2.1.1

* Fri Mar 11 2005 John (J5) Palmieri <johnp@redhat.com> 2.10.0-1
- Update to upstream version 2.10.0 

* Tue Mar 08 2005 John (J5) Palmieri <johnp@redhat.com> 2.9.91-3
- Build in rawhide
- Disable build on s390 and s390x

* Fri Feb 25 2005 John (J5) Palmieri <johnp@redhat.com> 2.9.91-2
- Reenabled BuildRequires for hal-devel >= 0.5.0
- Added (Build)Requires for nautilus-cd-burner(-devel) >= 2.9.6

* Wed Feb 23 2005 John (J5) Palmieri <johnp@redhat.com> 2.9.91-1
- New upstream version (version jump resulted from sound-juicer using gnome
  versioning scheme)
  
* Fri Feb 04 2005 Colin Walters <walters@redhat.com> 0.6.0-1
- New upstream version
- Remove obsoleted sound-juicer-idle-safety.patch
- BR latest gnome-media

* Fri Nov 12 2004 Warren Togami <wtogami@redhat.com> 0.5.14-5
- minor spec cleanups
- req cdparanoia and gstreamer-plugins

* Tue Nov 09 2004 Colin Walters <walters@redhat.com> 0.5.14-4
- Add sound-juicer-idle-safety.patch (bug 137847)

* Wed Oct 27 2004 Colin Walters <walters@redhat.com> 0.5.14-2
- Actually enable HAL
- BR hal-devel

* Wed Oct 13 2004 Colin Walters <walters@redhat.com> 0.5.14-1
- New upstream
- This release fixes corruption on re-read, upstream 153085
- Remove upstreamed sound-juicer-0.5.13-prefs-crash.patch

* Mon Oct 04 2004 Colin Walters <walters@redhat.com> 0.5.13-2
- Apply patch to avoid prefs crash

* Tue Sep 28 2004 Colin Walters <walters@redhat.com> 0.5.13-1
- New upstream 0.5.13

* Mon Sep 27 2004 Colin Walters <walters@redhat.com> 0.5.12.cvs20040927-1
- New upstream CVS snapshot, 20040927

* Mon Sep 20 2004 Colin Walters <walters@redhat.com> 0.5.12-1
- New upstream version 0.5.12
- Delete upstreamed patch sound-juicer-0.5.9-pref-help.patch
- Delete upstreamed patch sound-juicer-0.5.10-gstreamer.patch
- Delete call to autoconf

* Tue Jun 15 2004 Elliot Lee <sopwith@redhat.com>
- rebuilt

* Tue Mar 16 2004 Jeremy Katz <katzj@redhat.com> 0.5.10.1-8
- rebuild for new gstreamer

* Thu Mar 11 2004 Brent Fox <bfox@redhat.com> 0.5.10.1-5
- rebuild

* Fri Feb 27 2004 Brent Fox <bfox@redhat.com> 0.5.10.1-3
- rebuild

* Fri Feb 13 2004 Elliot Lee <sopwith@redhat.com>
- rebuilt

* Thu Feb  5 2004 Brent Fox <bfox@redhat.com> 0.5.10.1-1
- new version

* Wed Jan 28 2004 Alexander Larsson <alexl@redhat.com> 0.5.9-4
- rebuild to use new gstreamer

* Fri Jan 16 2004 Brent Fox <bfox@redhat.com> 0.5.9-3
- add preun to clean up GConf entries on uninstall

* Wed Jan 14 2004 Brent Fox <bfox@redhat.com> 0.5.9-2
- create init patch to make help work

* Tue Jan 13 2004 Brent Fox <bfox@redhat.com> 0.5.9-1
- update to 0.5.9

* Mon Dec 15 2003 Christopher Blizzard <blizzard@redhat.com> 0.5.8-1
- Add upstream patch that fixes permissions of created directories.

* Wed Dec 03 2003 Christopher Blizzard <blizzard@redhat.com> 0.5.8-0
- Update to 0.5.8

* Tue Oct 21 2003 Brent Fox <bfox@redhat.com> 0.5.5-1
- update to 0.5.5-1

* Mon Sep  1 2003 Jonathan Blandford <jrb@redhat.com>
- warning dialog fix
- add a quality option

* Fri Aug 29 2003 Elliot Lee <sopwith@redhat.com> 0.5.2-5
- scrollkeeper stuff should be removed

* Wed Aug 27 2003 Brent Fox <bfox@redhat.com> 0.5.2-4
- remove ExcludeArches since libmusicbrainz is building on all arches now

* Wed Aug 27 2003 Brent Fox <bfox@redhat.com> 0.5.2-3
- bump relnum

* Wed Aug 27 2003 Brent Fox <bfox@redhat.com> 0.5.2-2
- spec file cleanups
- add exclude arch for ia64, x86_64, ppc64, and s390x
- add file macros
- remove Requires for gstreamer-cdparanoia and gstreamer-vorbis

* Tue Apr 22 2003 Frederic Crozat <fcrozat@mandrakesoft.com>
- Use more macros

* Sun Apr 20 2003 Ronald Bultje <rbultje@ronald.bitfreak.net>
- Make spec file for sound-juicer (based on netRB spec file)
