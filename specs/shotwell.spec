# Not enabled by default for now - see rhbz#2190013
%bcond_with facedetect

Name:           shotwell
Version:        0.32.10
Release:        2%{?dist}
Summary:        A photo organizer for the GNOME desktop

# LGPLv2+ for the code
# CC-BY-SA for some of the icons
License:        LGPL-2.1-or-later AND CC-BY-SA-3.0
URL:            https://wiki.gnome.org/Apps/Shotwell
Source0:        https://download.gnome.org/sources/shotwell/0.32/shotwell-%{version}.tar.xz

BuildRequires:  vala
BuildRequires:  desktop-file-utils
BuildRequires:  libappstream-glib >= 0.7.3
BuildRequires:  gettext
BuildRequires:  itstool
BuildRequires:  meson
BuildRequires:  pkgconfig(atk)
BuildRequires:  pkgconfig(cairo)
BuildRequires:  pkgconfig(clutter-1.0)
BuildRequires:  pkgconfig(clutter-gtk-1.0)
BuildRequires:  pkgconfig(gcr-3)
BuildRequires:  pkgconfig(gcr-ui-3)
BuildRequires:  pkgconfig(gdk-3.0) >= 3.22
BuildRequires:  pkgconfig(gdk-pixbuf-2.0)
BuildRequires:  pkgconfig(gdk-x11-3.0)
BuildRequires:  pkgconfig(gee-0.8) >= 0.8.5
BuildRequires:  pkgconfig(gexiv2) >= 0.11.0
BuildRequires:  pkgconfig(gio-2.0) >= 2.40
BuildRequires:  pkgconfig(gio-unix-2.0) >= 2.40
BuildRequires:  pkgconfig(glib-2.0) >= 2.40.0
BuildRequires:  pkgconfig(gmodule-2.0) >= 2.40
BuildRequires:  pkgconfig(gstreamer-1.0) >= 1.0
BuildRequires:  pkgconfig(gstreamer-base-1.0) >= 1.0
BuildRequires:  pkgconfig(gstreamer-pbutils-1.0) >= 1.0
BuildRequires:  pkgconfig(gstreamer-plugins-base-1.0) >= 1.0
BuildRequires:  pkgconfig(gtk+-3.0) >= 3.22
BuildRequires:  pkgconfig(gudev-1.0) >= 145
BuildRequires:  pkgconfig(json-glib-1.0)
BuildRequires:  pkgconfig(libexif) >= 0.6.16
BuildRequires:  pkgconfig(libgdata)
BuildRequires:  pkgconfig(libgphoto2) >= 2.5.0
BuildRequires:  pkgconfig(libportal-gtk3) >= 0.5
BuildRequires:  pkgconfig(libraw) >= 0.13.2
BuildRequires:  pkgconfig(libsoup-3.0)
BuildRequires:  pkgconfig(libwebp)
BuildRequires:  pkgconfig(libwebpdemux)
BuildRequires:  pkgconfig(libxml-2.0) >= 2.6.32
BuildRequires:  pkgconfig(sqlite3) >= 3.5.9
BuildRequires:  pkgconfig(webkit2gtk-4.1) >= 2.26
BuildRequires:  pkgconfig(libsecret-1)
%if %{with facedetect}
BuildRequires:  pkgconfig(opencv4)
BuildRequires:  gcc-c++
%endif

# to fix symlinks
BuildRequires:  symlinks fakechroot

# provides the icon directories
Requires:       hicolor-icon-theme

%description
Shotwell is an easy-to-use, fast photo organizer designed for the GNOME
desktop.  It allows you to import photos from your camera or disk, organize
them by date and subject matter, even ratings.  It also offers basic photo
editing, like crop, red-eye correction, color adjustments, and straighten.
Shotwell's non-destructive photo editor does not alter your master photos,
making it easy to experiment and correct errors.


%prep
%autosetup -p1


%build
%meson \
  -Dinstall_apport_hook=false \
%if %{with facedetect}
  -Dface_detection=true \
  -Dface_detection_helper=true \
  -Dface_detection_helper_bus=session \
%endif
  %{nil}

%meson_build


%install
%meson_install

pushd %{buildroot}
fakechroot -- symlinks -C -cvr %{_datadir}/help
popd

%find_lang %{name} --with-gnome


%check
desktop-file-validate %{buildroot}%{_datadir}/applications/org.gnome.Shotwell.desktop
desktop-file-validate %{buildroot}%{_datadir}/applications/org.gnome.Shotwell-Viewer.desktop


%files -f %{name}.lang
%license COPYING
%doc README.md NEWS THANKS AUTHORS
%{_bindir}/shotwell
%{_libdir}/shotwell/
%{_libdir}/libshotwell-authenticator.so.*
%exclude %{_libdir}/libshotwell-authenticator.so
%{_libdir}/libshotwell-plugin-common.so.*
%exclude %{_libdir}/libshotwell-plugin-common.so
%{_libdir}/libshotwell-plugin-dev-1.0.so.*
%exclude %{_libdir}/libshotwell-plugin-dev-1.0.so
%{_libexecdir}/shotwell/
%{_datadir}/applications/org.gnome.Shotwell.desktop
%{_datadir}/applications/org.gnome.Shotwell.Auth.desktop
%{_datadir}/applications/org.gnome.Shotwell-Viewer.desktop
%{_datadir}/glib-2.0/schemas/*.xml
%{_datadir}/icons/hicolor/*/apps/org.gnome.Shotwell.png
%{_datadir}/icons/hicolor/scalable/apps/org.gnome.Shotwell.svg
%{_datadir}/icons/hicolor/symbolic/apps/org.gnome.Shotwell-symbolic.svg
%{_metainfodir}/org.gnome.Shotwell.appdata.xml
%{_mandir}/man1/shotwell.1*
%if %{with facedetect}
%{_datadir}/dbus-1/services/org.gnome.Shotwell.Faces1.service
%{_datadir}/shotwell/facedetect
%endif


%changelog
* Sun Jan 19 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.32.10-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Tue Oct 29 2024 nmontero <nmontero@redhat.com> - 0.32.10-1
- Update to 0.32.10

* Mon Sep 16 2024 David King <amigadave@amigadave.com> - 0.32.9-1
- Update to 0.32.9

* Mon Aug 12 2024 David King <amigadave@amigadave.com> - 0.32.8-1
- Update to 0.32.8

* Sat Jul 20 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.32.7-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Mon Jul 01 2024 Nieves Montero <nmontero@redhat.com> - 0.32.7-1
- Update to 0.32.7

* Wed Feb 14 2024 David King <amigadave@amigadave.com> - 0.32.6-1
- Update to 0.32.6

* Sat Jan 27 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.32.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Dec 06 2023 Kalev Lember <klember@redhat.com> - 0.32.4-1
- Update to 0.32.4

* Thu Nov 16 2023 Kalev Lember <klember@redhat.com> - 0.32.3-1
- Update to 0.32.3

* Sun Jul 23 2023 David King <amigadave@amigadave.com> - 0.32.2-1
- Update to 0.32.2

* Sat Jul 22 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.32.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Mon Jun 12 2023 Nicolas Chauvet <kwizart@gmail.com> - 0.32.1-2
- Enable RPM conditional --with facedetect, using opencv
  Disabled by default for now - see rhbz#2190013

* Wed May 10 2023 David King <amigadave@amigadave.com> - 0.32.1-1
- Update to 0.32.1

* Mon Apr 24 2023 David King <amigadave@amigadave.com> - 0.32.0-1
- Update to 0.32.0

* Mon Apr 10 2023 David King <amigadave@amigadave.com> - 0.31.90-1
- Update to 0.31.90

* Mon Mar 13 2023 David King <amigadave@amigadave.com> - 0.31.7-4
- Fix build with latest Vala

* Sat Jan 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.31.7-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Tue Dec 20 2022 Gwyn Ciesla <gwync@protonmail.com> - 0.31.7-2
- LibRaw rebuild

* Tue Dec 06 2022 David King <amigadave@amigadave.com> - 0.31.7-1
- Update to 0.31.7

* Sat Sep 17 2022 Kalev Lember <klember@redhat.com> - 0.31.5-3
- Drop unneeded libchamplain buildrequires

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.31.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Tue Jul 19 2022 Kalev Lember <klember@redhat.com> - 0.31.5-1
- Update to 0.31.5
- Switch to libsoup3

* Fri Jul 15 2022 Kalev Lember <klember@redhat.com> - 0.31.4-1
- Update to 0.31.4

* Sun Jan 30 2022 Thomas Moschny <thomas.moschny@gmx.de> - 0.31.3-8
- Cherry-pick upstream patches to fix broken image import (bz#2010178).
- Cherry-pick upstream patches to fix FTBFS with vala 0.55.

* Sat Jan 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.31.3-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Sat Sep 11 2021 Thomas Moschny <thomas.moschny@gmx.de> - 0.31.3-7
- Cherry-pick upstream patches to fix FTBFS with vala 0.53.

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.31.3-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Mar 26 2021 Kalev Lember <klember@redhat.com> - 0.31.3-5
- Don't explicitly require dconf
- Remove ldconfig_scriptlets

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.31.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Sat Dec 26 2020 Thomas Moschny <thomas.moschny@gmx.de> - 0.31.3-3
- Fix build option.

* Sat Dec 26 2020 Thomas Moschny <thomas.moschny@gmx.de> - 0.31.3-2
- Update BRs from meson.build.

* Thu Dec 24 2020 Thomas Moschny <thomas.moschny@gmx.de> - 0.31.3-1
- Update to 0.31.3.

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.31.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri May 22 2020 Kalev Lember <klember@redhat.com> - 0.31.2-1
- Update to 0.31.2

* Mon May 11 2020 Gwyn Ciesla <gwync@protonmail.com> - 0.31.1-2
- Rebuild for new LibRaw

* Wed Mar 04 2020 Kalev Lember <klember@redhat.com> - 0.31.1-1
- Update to 0.31.1

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.31.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Nov 29 2019 Kalev Lember <klember@redhat.com> - 0.31.0-4
- Drop unused gnome-doc-utils build dep

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.31.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Tue Apr 16 2019 Adam Williamson <awilliam@redhat.com> - 0.31.0-2
- Rebuild with Meson fix for #1699099

* Fri Mar 29 2019 Kalev Lember <klember@redhat.com> - 0.31.0-1
- Update to 0.31.0
- Disable apport hook during build rather than rm -rf-ing it afterwards

* Thu Feb 07 2019 Kalev Lember <klember@redhat.com> - 0.30.2-1
- Update to 0.30.2
- Use upstream screenshots for appdata

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.30.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Sep 29 2018 Kalev Lember <klember@redhat.com> - 0.30.1-1
- Update to 0.30.1

* Mon Sep 17 2018 Kalev Lember <klember@redhat.com> - 0.30.0-1
- Update to 0.30.0

* Fri Sep 07 2018 Kalev Lember <klember@redhat.com> - 0.29.92-1
- Update to 0.29.92
- Switch to the meson build system

* Thu Jul 19 2018 Kevin Fenzi <kevin@scrye.com> - 0.28.4-2
- Rebuild for new LibRaw.

* Sun Jul 15 2018 Thomas Moschny <thomas.moschny@gmx.de> - 0.28.4-1
- Update to 0.28.4.

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.28.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri May 25 2018 Kalev Lember <klember@redhat.com> - 0.28.3-2
- Don't package libshotwell-authenticator.so symlink

* Tue May 08 2018 Kalev Lember <klember@redhat.com> - 0.28.3-1
- Update to 0.28.3

* Mon Apr 09 2018 Kalev Lember <klember@redhat.com> - 0.28.2-1
- Update to 0.28.2

* Mon Mar 26 2018 Kalev Lember <klember@redhat.com> - 0.28.1-1
- Update to 0.28.1

* Mon Mar 12 2018 Kalev Lember <klember@redhat.com> - 0.28.0-1
- Update to 0.28.0

* Sun Mar 11 2018 Kalev Lember <klember@redhat.com> - 0.27.92-1
- Update to 0.27.92

* Tue Feb  6 2018 Thomas Moschny <thomas.moschny@gmx.de> - 0.27.4-1
- Update to 0.27.4.

* Fri Feb 02 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.27.3-3
- Switch to %%ldconfig_scriptlets

* Thu Jan 18 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.27.3-2
- Remove obsolete scriptlets

* Sat Jan 13 2018 Thomas Moschny <thomas.moschny@gmx.de> - 0.27.3-1
- Update to 0.27.3.
- Appstream metadata location has changed (requires
  libappstream-glib >= 0.7.3).

* Fri Dec 15 2017 Thomas Moschny <thomas.moschny@gmx.de> - 0.27.2-1
- Update to 0.27.2.

* Sat Oct 21 2017 Thomas Moschny <thomas.moschny@gmx.de> - 0.27.1-1
- Update to 0.27.1.

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.27.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.27.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sun Jun 25 2017 Kalev Lember <klember@redhat.com> - 0.27.0-1
- Update to 0.27.0

* Mon Jun  5 2017 Thomas Moschny <thomas.moschny@gmx.de> - 0.26.2-1
- Update to 0.26.2.

* Tue Apr 11 2017 Kalev Lember <klember@redhat.com> - 0.26.1-1
- Update to 0.26.1

* Tue Mar 21 2017 Kalev Lember <klember@redhat.com> - 0.26.0-1
- Update to 0.26.0

* Wed Mar 15 2017 Thomas Moschny <thomas.moschny@gmx.de> - 0.25.92-1
- Update to 0.25.92.

* Tue Feb 28 2017 Richard Hughes <rhughes@redhat.com> - 0.25.90-1
- Update to 0.25.90

* Tue Feb 14 2017 Richard Hughes <rhughes@redhat.com> - 0.25.5-1
- Update to 0.25.5

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.25.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Tue Jan 31 2017 Kalev Lember <klember@redhat.com> - 0.25.4-1
- Update to 0.25.4

* Tue Jan 17 2017 Thomas Moschny <thomas.moschny@gmx.de> - 0.25.3-2
- Update to 0.25.3.

* Tue Dec 27 2016 Jon Ciesla <limburgher@gmail.com> - 0.25.2-2
- Rebuild for new LibRaw.

* Mon Dec 12 2016 Thomas Moschny <thomas.moschny@gmx.de> - 0.25.2-1
- Update to 0.25.2.

* Mon Nov 21 2016 Thomas Moschny <thomas.moschny@gmx.de> - 0.25.1-1
- Update to 0.25.1.
- Update BR.

* Tue Nov  8 2016 Thomas Moschny <thomas.moschny@gmx.de> - 0.25.0.1-1
- Update to 0.25.0.1.
- Update BR.

* Mon Oct 24 2016 Kalev Lember <klember@redhat.com> - 0.25.0-1
- Update to 0.25.0

* Sun Oct 16 2016 Kalev Lember <klember@redhat.com> - 0.24.1-1
- Update to 0.24.1

* Thu Sep 22 2016 Kalev Lember <klember@redhat.com> - 0.24.0-1
- Update to 0.24.0

* Wed Sep 14 2016 Kalev Lember <klember@redhat.com> - 0.23.7-1
- Update to 0.23.7
- Don't set group tags
- Use upstream shipped man page
- Update project URL
- Don't install libtool .la files
- Move desktop file validation to the check section

* Tue Aug 30 2016 Thomas Moschny <thomas.moschny@gmx.de> - 0.23.6-1
- Update to 0.23.6.

* Wed Aug 17 2016 Kalev Lember <klember@redhat.com> - 0.23.5-1
- Update to 0.23.5

* Thu Jul 21 2016 Thomas Moschny <thomas.moschny@gmx.de> - 0.23.4-1
- Update to 0.24.4.
- Restore filelist.
- Updates adopting to new build system:
  - Use standard rpm macros.
  - Reenable parallel builds.
  - Disable silent rules.
  - Small fixes.

* Wed Jul 20 2016 Richard Hughes <rhughes@redhat.com> - 0.23.3-1
- Update to 0.23.3

* Mon Jul 18 2016 Thomas Moschny <thomas.moschny@gmx.de> - 0.23.2-1
- Current Shotwell version doesn't support parallel make.

* Wed Jun 22 2016 Richard Hughes <rhughes@redhat.com> - 0.23.2-1
- Update to 0.23.2

* Tue May 24 2016 Thomas Moschny <thomas.moschny@gmx.de> - 0.23.1-1
- Update to 0.23.1.
- Hi-res icons have been added upstream.

* Wed Apr 27 2016 Thomas Moschny <thomas.moschny@gmx.de> - 0.23.0-1
- Update to 0.23.0.

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.23.0-0.2.20160105gitf2fb1f7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Tue Jan 05 2016 Michael Catanzaro <mcatanzaro@gnome.org> - 0.23.0-0.1.20160105gitf2fb1f7
- Update to git snapshot. Port to WebKit2 and verify TLS certificates.

* Thu Aug 20 2015 Jon Ciesla <limburgher@gmail.com> - 0.22.0-6
- Rebuild for new LibRaw.

* Fri Jun 19 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.22.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Mon Apr 27 2015 Michael Catanzaro <mcatanzaro@gnome.org> - 0.22.0-4
- Add symbolic icon

* Fri Apr 24 2015 Thomas Moschny <thomas.moschny@gmx.de> - 0.22.0-3
- Update dependencies.
- New appstream-util features available only in Fedora >= 22.

* Mon Mar 30 2015 Richard Hughes <rhughes@redhat.com> - 0.22.0-2
- Use better AppData screenshots

* Tue Mar 24 2015 Kalev Lember <kalevlember@gmail.com> - 0.22.0-1
- Update to 0.22.0
- Use license macro for the COPYING file

* Tue Feb 03 2015 Richard Hughes <rhughes@redhat.com> - 0.21.0-1
- Update to 0.21.0

* Wed Jan 21 2015 Peter Robinson <pbrobinson@fedoraproject.org> 0.20.2-2
- Rebuild (libgpohoto2)

* Tue Nov 04 2014 Kalev Lember <kalevlember@gmail.com> - 0.20.2-1
- Update to 0.20.2

* Fri Oct  3 2014 Thomas Moschny <thomas.moschny@gmx.de> - 0.20.1-1
- Update to 0.20.1.

* Fri Sep 19 2014 Kalev Lember <kalevlember@gmail.com> - 0.20.0-1
- Update to 0.20.0

* Sat Sep 06 2014 Thomas Moschny <thomas.moschny@gmx.de> - 0.19.0-2
- Rebuilt against newer vala trying to fix rhbz#1134128.

* Thu Aug 21 2014 Kalev Lember <kalevlember@gmail.com> - 0.19.0-1
- Update to 0.19.0

* Mon Aug 18 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.18.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Fri Jul 04 2014 Richard Hughes <rhughes@redhat.com> - 0.18.1-1
- Update to 0.18.1

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.18.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Thu Mar 20 2014 Kalev Lember <kalevlember@gmail.com> - 0.18.0-1
- Update to 0.18.0

* Tue Jan 21 2014 Jon Ciesla <limburgher@gmail.com> - 0.15.1-2
- Rebuild for new LibRaw.

* Tue Dec 17 2013 Thomas Moschny <thomas.moschny@gmx.de> - 0.15.1-1
- Update to 0.15.1.
- Update bug URLs.
- Add patch for rhbz#1037324 (-Werror=format-security).

* Fri Oct  4 2013 Thomas Moschny <thomas.moschny@gmx.de> - 0.15.0-1
- Update to 0.15.0.
- Include appdata file.

* Mon Sep 30 2013 Thomas Moschny <thomas.moschny@gmx.de> - 0.15.0-0.3.pr3
- Use upstream's man page.

* Mon Sep 30 2013 Debarshi Ray <rishi@fedoraproject.org> - 0.15.0-0.2.pr3
- Add a man page

* Sun Sep 29 2013 Kalev Lember <kalevlember@gmail.com> - 0.15.0-0.1.pr3
- Update to 0.15.0pr3
- Drop patches that have found their way upstream

* Fri Sep 20 2013 Thomas Moschny <thomas.moschny@gmx.de> - 0.14.1-5
- Add patch fixing the video-thumbnailer (rhbz#986574),
  thanks to David Woodhouse.
- Fix bogus dates in the %%changelog.

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.14.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Fri May 31 2013 Jon Ciesla <limburgher@gmail.com> - 0.14.1-3
- Rebuild for new LibRaw.

* Mon May 20 2013 Peter Robinson <pbrobinson@fedoraproject.org> 0.14.1-2
- Rebuild (libgexiv2)

* Thu Apr  4 2013 Thomas Moschny <thomas.moschny@gmx.de> - 0.14.1-1
- Update to 0.14.1.

* Tue Mar 19 2013 Thomas Moschny <thomas.moschny@gmx.de> - 0.14.0-2
- Rework BR section.

* Tue Mar 19 2013 Thomas Moschny <thomas.moschny@gmx.de> - 0.14.0-1
- Update to 0.14.0.
- Drop GStreamer 1.0 patch, applied upstream.

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.13.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Fri Oct  5 2012 Thomas Moschny <thomas.moschny@gmx.de> - 0.13.1-1
- Update to 0.13.1.
- shotwell-settings-migrator has been moved to %%{_libexecdir}.

* Thu Sep 27 2012 Bastien Nocera <bnocera@redhat.com> 0.13.0-2
- Port to GStreamer 1.0 (Shotwell already links against webkitgtk3
  which uses GStreamer 1.0)

* Thu Sep 20 2012 Thomas Moschny <thomas.moschny@gmx.de> - 0.13.0-1
- Update to 0.13.0.
- Remove patches applied upstream.
- Add BR on json-glib.
- Add runtime dependency on dconf.

* Tue Aug 21 2012 Jindrich Novy <jnovy@redhat.com> - 0.12.3-5
- add patch to fix build against libgphoto2-2.5.0, thanks to Clinton Rogers
  (http://redmine.yorba.org/issues/5553)

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.12.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sat Jul 14 2012 Thomas Moschny <thomas.moschny@gmx.de> - 0.12.3-3
- Add patches for compatibility with Vala 0.17.2.

* Sat Jul 14 2012 Michel Salim <salimma@fedoraproject.org> - 0.12.3-2
- Rebuild for libgphoto2 2.5.0

* Tue May 22 2012 Thomas Moschny <thomas.moschny@gmx.de> - 0.12.3-1
- Update to 0.12.3.

* Thu May 03 2012 Rex Dieter <rdieter@fedoraproject.org> 0.12.2-3
- rebuild (exiv2)

* Wed May 02 2012 Kalev Lember <kalevlember@gmail.com> - 0.12.2-2
- Fix startup when invoked as /bin/shotwell (#812652)

* Fri Apr 13 2012 Kalev Lember <kalevlember@gmail.com> - 0.12.2-1
- Update to 0.12.2
- Use find_lang --with-gnome for including help files

* Tue Apr 03 2012 Kalev Lember <kalevlember@gmail.com> - 0.12.1-1
- Update to 0.12.1
- Don't buildrequire gnome-vfs (#690563)

* Wed Feb 22 2012 Michel Salim <salimma@fedoraproject.org> - 0.12.0-0.3.20111117gitcf087489ea
- Remove dependency on totem, unneeded since 0.10 (# 794487)

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.12.0-0.2.20111117gitcf087489ea
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Thu Nov 17 2011 Siddhesh Poyarekar <siddhesh.poyarekar@gmail.com> 0.12.0-1.20111117gitcf087489ea
- Bump to current git to fix build against LibRaw
- LibRaw now has a dynamic library and shotwell is using it

* Thu Nov 10 2011 Adam Williamson <awilliam@redhat.com> 0.12.0-1.20111110git163bf4a114
- bump to current git to get vala 0.14 support for rawhide, GTK+ 3 port
- adjust dependencies for vala, gtk, gsettings
- adjust for gsettings port

* Mon Nov  7 2011 Matthias Clasen <mclasen@redhat.com> 0.11.1-3
- Rebuild against new libpng

* Sat Oct 15 2011 Rex Dieter <rdieter@fedoraproject.org> 0.11.1-2
- rebuild (exiv2)

* Thu Sep  8 2011 Matthias Clasen <mclasen@redhat.com> - 0.11.1-1
- Update to 0.11.1

* Wed Aug 24 2011 Matthias Clasen <mclasen@redhat.com> - 0.11.0-1
- Update to 0.11.0

* Wed Jul  6 2011 Matthias Clasen <mclasen@redhat.com> - 0.10.1-1
- Update to 0.10.1

* Thu May 26 2011 Michel Salim <salimma@fedoraproject.org> - 0.9.3-1
- Update to 0.9.3

* Wed Apr 13 2011 Michel Salim <salimma@fedoraproject.org> - 0.9.2-1
- Update to 0.9.2

* Tue Apr  5 2011 Michel Salim <salimma@fedoraproject.org> - 0.9.1-1
- Update to 0.9.1

* Fri Apr  1 2011 Michel Salim <salimma@fedoraproject.org> - 0.9.0-3
- Use more complete multilib fix from upstream

* Mon Mar 28 2011 Michel Salim <salimma@fedoraproject.org> - 0.9.0-2
- Look for plugins in correct directory on 64-bit systems (# 690927)

* Fri Mar 25 2011 Matthias Clasen <mclasen@redhat.com> - 0.9.0-1
- Update to 0.9.0
- Add hi-res icons (#690596)

* Fri Mar 18 2011 Michel Salim <salimma@fedoraproject.org> - 0.8.90-2.r2758
- Get gettext to actually generate translated strings (# 642092)

* Thu Mar 17 2011 Michel Salim <salimma@fedoraproject.org> - 0.8.90-1.r2758
- Update to 0.9.0 pre-release
- Switch declaration of build requirements to pkgconfig

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.8.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Sun Jan 16 2011 Christopher Aillon <caillon@redhat.com> - 0.8.1-1
- Update to 0.8.1

* Sat Jan  8 2011 Christopher Aillon <caillon@redhat.com> - 0.8.0-1
- Update to 0.8.0

* Sun Jan  2 2011 Siddhesh Poyarekar <siddhesh@redhat.com> - 0.7.2-4
- Add user_photos to permissions required. Fixes bz #666512.

* Sun Jan 02 2011 Rex Dieter <rdieter@fedoraproject.org> - 0.7.2-3
- rebuild (exiv2)

* Wed Sep 29 2010 jkeating - 0.7.2-2
- Rebuilt for gcc bug 634757

* Mon Sep 13 2010 Matthias Clasen <mclasen@redhat.com> - 0.7.2-1
- Update to 0.7.2

* Wed Sep  1 2010 Matthias Clasen <mclasen@redhat.com> - 0.7.1-1
- Update to 0.7.1

* Tue Jul 13 2010 Mike McGrath <mmcgrath@redhat.com> - 0.6.1-1.1
- Rebuilt to fix broken libwebkit-1.0.so.2 dep

* Fri Jul  9 2010 Matthias Clasen <mclasen@redhat.com> - 0.6.1-1
- Update to 0.6.1

* Wed May 12 2010 Matthias Clasen <mclasen@redhat.com> - 0.5.2-1
- Update to 0.5.2
- Translation updates for Czech, Finnish, Greek, Ukrainian and Russian

* Fri Mar 12 2010 Matthias Clasen <mclasen@redhat.com> - 0.5.0-1
- Update to 0.5.0
- Many new features, see http://www.yorba.org/shotwell/

* Mon Jan 18 2010 Matthias Clasen <mclasen@redhat.com> - 0.4.3-1
- Update to 0.4.3

* Tue Jan  5 2010 Matthias Clasen <mclasen@redhat.com> - 0.4.2-1
- Update to 0.4.2

* Wed Dec 23 2009 Matthias Clasen <mclasen@redhat.com> - 0.4.0-1
- Update to 0.4.0

* Fri Dec 18 2009 Matthias Clasen <mclasen@redhat.com> - 0.4.0-0.1.20091218svn
- 0.4 snapshot

* Thu Nov 12 2009 Matthias Clasen <mclasen@redhat.com> - 0.3.2-1
- Update to 0.3.2

* Tue Nov  3 2009 Matthias Clasen <mclasen@redhat.com> - 0.3.0-1
- Version 0.3.0

* Thu Aug 20 2009 Michel Salim <salimma@fedoraproject.org> - 0.2.0-3
- Rebuild against new libgee

* Wed Aug 12 2009  Matthias Clasen <mclasen@redhat.com> - 0.2.0-2.fc12
- Bring icon cache handling in sync with current guidelines

* Sun Aug  9 2009  Matthias Clasen <mclasen@redhat.com> - 0.2.0-1.fc12
- Initial packaging
