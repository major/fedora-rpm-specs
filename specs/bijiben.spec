Name:           bijiben
Version:        40.1
Release:        12%{?dist}
Summary:        Simple Note Viewer

# Bijiben is GPLv3+ apart a few files "LGPLv2 or LGPLv3"
# And ligd is LGPLv2+
License:        GPL-3.0-or-later AND LGPL-3.0-only AND LGPL-2.0-or-later
Url:            http://www.gnome.org
Source0:        http://download.gnome.org/sources/%{name}/40/%{name}-%{version}.tar.xz

Patch01:        meson-0.61-build.patch
Patch02:        webkitdep.patch

BuildRequires:  desktop-file-utils
BuildRequires:  itstool
BuildRequires:  gettext
BuildRequires:  meson
BuildRequires:  pkgconfig(gio-unix-2.0)
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(goa-1.0)
BuildRequires:  pkgconfig(gtk+-3.0)
BuildRequires:  pkgconfig(json-glib-1.0)
BuildRequires:  pkgconfig(libcurl)
BuildRequires:  pkgconfig(libecal-2.0) >= 3.45.1
BuildRequires:  pkgconfig(libedataserver-1.2) >= 3.45.1
BuildRequires:  pkgconfig(libhandy-1)
BuildRequires:  pkgconfig(libxml-2.0)
BuildRequires:  pkgconfig(tracker-sparql-3.0)
BuildRequires:  pkgconfig(uuid)
BuildRequires:  pkgconfig(webkit2gtk-4.1) >= 2.36
BuildRequires:  vala
BuildRequires:  yelp-tools
BuildRequires:  libappstream-glib-devel

Recommends:     gvfs-goa

# libgd is not meant to be installed as a system-wide shared library.
# It is just a way for GNOME applications to share widgets and other common
# code on an ad-hoc basis.
Provides: bundled(libgd)

%description
Simple note editor which emphasis on visuals : quickly write
notes, quickly find it back.


%prep
%autosetup -p1 -S gendiff


%build
%meson \
%if 0%{?flatpak}
  -Dprivate_store=true
%else
  -Dprivate_store=false
%endif

%meson_build


%install
%meson_install

# Creates the file for all locales
%find_lang %{name} --with-gnome


%check
appstream-util validate-relax --nonet %{buildroot}%{_datadir}/metainfo/org.gnome.Notes.appdata.xml
desktop-file-validate %{buildroot}%{_datadir}/applications/org.gnome.Notes.desktop


%files -f %{name}.lang
%license COPYING
%doc AUTHORS NEWS README.md
%{_bindir}/bijiben
%{_datadir}/applications/org.gnome.Notes.desktop
%{_datadir}/bijiben/
%{_datadir}/dbus-1/services/org.gnome.Notes.SearchProvider.service
%{_datadir}/glib-2.0/schemas/org.gnome.Notes.gschema.xml
# co-own these directories
%dir %{_datadir}/gnome-shell
%dir %{_datadir}/gnome-shell/search-providers
%{_datadir}/gnome-shell/search-providers/org.gnome.Notes-search-provider.ini
%{_datadir}/icons/hicolor/*/apps/org.gnome.Notes.svg
%{_datadir}/icons/hicolor/symbolic/apps/org.gnome.Notes-symbolic.svg
%{_datadir}/metainfo/org.gnome.Notes.appdata.xml
%{_datadir}/mime/packages/org.gnome.Notes.xml
%{_libexecdir}/bijiben-shell-search-provider


%changelog
* Thu Jan 16 2025 Fedora Release Engineering <releng@fedoraproject.org> - 40.1-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Wed Jul 17 2024 Fedora Release Engineering <releng@fedoraproject.org> - 40.1-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Tue Jan 23 2024 Fedora Release Engineering <releng@fedoraproject.org> - 40.1-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 40.1-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Mon Jan 08 2024 Milan Crha <mcrha@redhat.com> - 40.1-8
- Rebuilt for evolution-data-server soname version bump

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 40.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Wed Jan 18 2023 Fedora Release Engineering <releng@fedoraproject.org> - 40.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Wed Jul 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 40.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed Jul 20 2022 Milan Crha <mcrha@redhat.com> - 40.1-4
- Rebuilt for evolution-data-server soname version bump
- Build with WebKitGTK 4.1 API (using libsoup3)

* Wed Jan 19 2022 Fedora Release Engineering <releng@fedoraproject.org> - 40.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 40.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed May 05 2021 Kalev Lember <klember@redhat.com> - 40.1-1
- Update to 40.1

* Thu Mar 18 2021 Kalev Lember <klember@redhat.com> - 40.0-1
- Update to 40.0

* Fri Feb 19 2021 Kalev Lember <klember@redhat.com> - 3.38.0-4
- Port to libhandy-1
- Switch to tracker3

* Fri Feb 12 2021 Milan Crha <mcrha@redhat.com> - 3.38.0-3
- Rebuilt for evolution-data-server soname version bump

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 3.38.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Sep 21 09:44:42 CEST 2020 Kalev Lember <klember@redhat.com> - 3.38.0-1
- Update to 3.38.0

* Wed Sep 09 2020 Kalev Lember <klember@redhat.com> - 3.37.92-1
- Update to 3.37.92

* Sat Aug 29 2020 Kalev Lember <klember@redhat.com> - 3.37.91-1
- Update to 3.37.91

* Mon Aug 17 2020 Kalev Lember <klember@redhat.com> - 3.37.90-1
- Update to 3.37.90

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.37.1-4
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.37.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Jul 03 2020 Milan Crha <mcrha@redhat.com> - 3.37.1-2
- Rebuilt for evolution-data-server soname version bump

* Tue May 05 2020 Kalev Lember <klember@redhat.com> - 3.37.1-1
- Update to 3.37.1

* Sun Apr 05 2020 Kalev Lember <klember@redhat.com> - 3.36.1-1
- Update to 3.36.1

* Sat Mar 07 2020 Kalev Lember <klember@redhat.com> - 3.36.0-1
- Update to 3.36.0

* Thu Mar 05 2020 Kalev Lember <klember@redhat.com> - 3.35.92-1
- Update to 3.35.92

* Thu Feb 20 2020 Kalev Lember <klember@redhat.com> - 3.35.91-1
- Update to 3.35.91

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.35.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Mon Jan 20 2020 Kalev Lember <klember@redhat.com> - 3.35.2-1
- Update to 3.35.2

* Mon Dec 02 2019 Kalev Lember <klember@redhat.com> - 3.35.1-1
- Update to 3.35.1

* Mon Oct 14 2019 Kalev Lember <klember@redhat.com> - 3.34.1-1
- Update to 3.34.1

* Tue Sep 10 2019 Kalev Lember <klember@redhat.com> - 3.34.0-1
- Update to 3.34.0

* Wed Sep 04 2019 Kalev Lember <klember@redhat.com> - 3.33.92-1
- Update to 3.33.92

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.32.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Jul 19 2019 Kalev Lember <klember@redhat.com> - 3.32.2-2
- Recommend gvfs-goa, instead of hard requiring

* Fri Jul 19 2019 Kalev Lember <klember@redhat.com> - 3.32.2-1
- Update to 3.32.2

* Tue May 21 2019 Milan Crha <mcrha@redhat.com> - 3.32.1-3
- Add patch to build against newer evolution-data-server (libecal-2.0)

* Tue Apr 16 2019 Adam Williamson <awilliam@redhat.com> - 3.32.1-2
- Rebuild with Meson fix for #1699099

* Wed Apr 10 2019 Kalev Lember <klember@redhat.com> - 3.32.1-1
- Update to 3.32.1

* Wed Mar 13 2019 Kalev Lember <klember@redhat.com> - 3.32.0-1
- Update to 3.32.0

* Tue Mar 05 2019 Kalev Lember <klember@redhat.com> - 3.31.92-1
- Update to 3.31.92

* Mon Feb 18 2019 Kalev Lember <klember@redhat.com> - 3.31.91-1
- Update to 3.31.91

* Tue Feb 05 2019 Kalev Lember <klember@redhat.com> - 3.31.90-1
- Update to 3.31.90

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.31.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Tue Jan 08 2019 Kalev Lember <klember@redhat.com> - 3.31.4-1
- Update to 3.31.4
- Validate the appdata file

* Sat Nov 17 2018 Kalev Lember <klember@redhat.com> - 3.30.3-1
- Update to 3.30.3
- Use upstream screenshots in appdata

* Mon Oct 22 2018 Kalev Lember <klember@redhat.com> - 3.30.2-1
- Update to 3.30.2

* Wed Sep 26 2018 Kalev Lember <klember@redhat.com> - 3.30.1-1
- Update to 3.30.1

* Thu Sep 06 2018 Kalev Lember <klember@redhat.com> - 3.30.0-1
- Update to 3.30.0

* Mon Aug 13 2018 Kalev Lember <klember@redhat.com> - 3.29.90-1
- Update to 3.29.90

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.28.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 26 2018 Kalev Lember <klember@redhat.com> - 3.28.3-1
- Update to 3.28.3

* Fri May 11 2018 Kalev Lember <klember@redhat.com> - 3.28.2-1
- Update to 3.28.2

* Mon Apr 09 2018 Kalev Lember <klember@redhat.com> - 3.28.1-1
- Update to 3.28.1

* Mon Mar 05 2018 Kalev Lember <klember@redhat.com> - 3.28.0-1
- Update to 3.28.0
- Switch to the meson build system

* Wed Feb 07 2018 Kalev Lember <klember@redhat.com> - 3.26.2-5
- Rebuilt for evolution-data-server soname bump

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.26.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Fri Jan 05 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 3.26.2-3
- Remove obsolete scriptlets

* Wed Nov 08 2017 Milan Crha <mcrha@redhat.com> - 3.26.2-2
- Rebuild for newer libical

* Wed Nov 01 2017 Kalev Lember <klember@redhat.com> - 3.26.2-1
- Update to 3.26.2

* Sun Oct 08 2017 Kalev Lember <klember@redhat.com> - 3.26.1-1
- Update to 3.26.1

* Wed Sep 13 2017 Kalev Lember <klember@redhat.com> - 3.26.0-1
- Update to 3.26.0

* Mon Sep 11 2017 Kalev Lember <klember@redhat.com> - 3.24.2-1
- Update to 3.24.2

* Fri Aug 11 2017 Kalev Lember <klember@redhat.com> - 3.24.1-1
- Update to 3.24.1

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.24.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.24.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Mon Jun 12 2017 Kalev Lember <klember@redhat.com> - 3.24.0-1
- Update to 3.24.0

* Fri May 05 2017 Milan Crha <mcrha@redhat.com> - 3.21.2-4
- Add upstream patches to build with webkitgtk4

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.21.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Jul 18 2016 Milan Crha <mcrha@redhat.com> - 3.21.2-2
- Rebuild for newer evolution-data-server

* Wed Jun 22 2016 Richard Hughes <rhughes@redhat.com> - 3.21.2-1
- Update to 3.21.2

* Tue Jun 21 2016 Milan Crha <mcrha@redhat.com> - 3.20.2-2
- Rebuild for newer evolution-data-server

* Tue May 10 2016 Kalev Lember <klember@redhat.com> - 3.20.2-1
- Update to 3.20.2

* Fri Apr 15 2016 David Tardon <dtardon@redhat.com> - 3.20.0-3
- rebuild for ICU 57.1

* Sun Apr 03 2016 Mathieu Bridon <bochecha@daitauha.fr> - 3.20.0-2
- Drop the Zeitgeist dependency.

* Tue Mar 22 2016 Kalev Lember <klember@redhat.com> - 3.20.0-1
- Update to 3.20.0

* Mon Mar 14 2016 Kalev Lember <klember@redhat.com> - 3.19.92-1
- Update to 3.19.92

* Tue Feb 16 2016 Richard Hughes <rhughes@redhat.com> - 3.19.90-1
- Update to 3.19.90

* Tue Feb 16 2016 Milan Crha <mcrha@redhat.com> - 3.19.4.1-3
- Rebuild for newer evolution-data-server

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 3.19.4.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Tue Jan 19 2016 David King <amigadave@amigadave.com> - 3.19.4-1
- Update to 3.19.4

* Mon Jan 18 2016 David Tardon <dtardon@redhat.com> - 3.19.3-2
- rebuild for libical 2.0.0

* Mon Dec 14 2015 Kalev Lember <klember@redhat.com> - 3.19.3-1
- Update to 3.19.3

* Wed Oct 28 2015 Kalev Lember <klember@redhat.com> - 3.19.1-1
- Update to 3.19.1

* Mon Oct 12 2015 Kalev Lember <klember@redhat.com> - 3.18.1-1
- Update to 3.18.1

* Sun Sep 20 2015 Kalev Lember <klember@redhat.com> - 3.18.0-1
- Update to 3.18.0

* Sun Sep 13 2015 Kalev Lember <klember@redhat.com> - 3.17.92-1
- Update to 3.17.92

* Mon Aug 31 2015 Kalev Lember <klember@redhat.com> - 3.17.91-1
- Update to 3.17.91

* Tue Aug 18 2015 Kalev Lember <klember@redhat.com> - 3.17.90-1
- Update to 3.17.90
- Use make_install macro

* Wed Jul 22 2015 Milan Crha <mcrha@redhat.com> - 3.17.4-2
- Rebuild for newer evolution-data-server

* Sun Jul 19 2015 David King <amigadave@amigadave.com> - 3.17.4-1
- Update to 3.17.4

* Tue Jun 23 2015 David King <amigadave@amigadave.com> - 3.17.3-1
- Update to 3.17.3

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.17.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Tue May 26 2015 David King <amigadave@amigadave.com> - 3.17.2-1
- Update to 3.17.2 (#1175138)
- Use pkgconfig for BuildRequires

* Fri May 01 2015 Kalev Lember <kalevlember@gmail.com> - 3.17.1-1
- Update to 3.17.1

* Tue Apr 28 2015 Milan Crha <mcrha@redhat.com> - 3.16.1-2
- Rebuild for newer evolution-data-server

* Tue Apr 14 2015 Kalev Lember <kalevlember@gmail.com> - 3.16.1-1
- Update to 3.16.1

* Mon Mar 30 2015 Richard Hughes <rhughes@redhat.com> - 3.16.0-2
- Use better AppData screenshots

* Fri Mar 20 2015 Kalev Lember <kalevlember@gmail.com> - 3.16.0-1
- Update to 3.16.0

* Tue Mar 17 2015 Kalev Lember <kalevlember@gmail.com> - 3.15.92-1
- Update to 3.15.92
- Use license macro for the COPYING file

* Mon Mar 02 2015 Kalev Lember <kalevlember@gmail.com> - 3.15.91-1
- Update to 3.15.91

* Sat Feb 21 2015 Kalev Lember <kalevlember@gmail.com> - 3.15.90-1
- Update to 3.15.90

* Tue Feb 17 2015 Adam Williamson <awilliam@redhat.com> - 3.15.3-2
- rebuild for new e-d-s (patch from mrcha, BGO #744660)

* Fri Dec 19 2014 Richard Hughes <rhughes@redhat.com> - 3.15.3-1
- Update to 3.15.3

* Tue Nov 25 2014 Kalev Lember <kalevlember@gmail.com> - 3.15.2-1
- Update to 3.15.2

* Mon Oct 27 2014 Pierre-Yves Luyten <py@luyten.fr> - 3.15.1-1
- Update to 3.15.1

* Mon Oct 13 2014 Kalev Lember <kalevlember@gmail.com> - 3.14.1-1
- Update to 3.14.1

* Mon Sep 22 2014 Kalev Lember <kalevlember@gmail.com> - 3.14.0-1
- Update to 3.14.0

* Sat Sep 20 2014 Kalev Lember <kalevlember@gmail.com> - 3.13.92-2
- Update mime scriptlets

* Tue Sep 16 2014 Kalev Lember <kalevlember@gmail.com> - 3.13.92-1
- Update to 3.13.92
- Drop large ChangeLog file

* Tue Sep 02 2014 Kalev Lember <kalevlember@gmail.com> - 3.13.91-1
- Update to 3.13.91

* Tue Aug 19 2014 Kalev Lember <kalevlember@gmail.com> - 3.13.90-1
- Update to 3.13.90

* Fri Aug 15 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.13.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Tue Aug 05 2014 Pierre-Yves Luyten <py@luyten.fr> - 3.13.4-2
- Rebuild for bump.

* Mon Jul 21 2014 Kalev Lember <kalevlember@gmail.com> - 3.13.4-1
- Update to 3.13.4

* Tue Jun 24 2014 Richard Hughes <rhughes@redhat.com> - 3.13.3-1
- Update to 3.13.3

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.13.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Wed May 28 2014 Kalev Lember <kalevlember@gmail.com> - 3.13.2-1
- Update to 3.13.2

* Wed May 14 2014 Pierre-Yves Luyten <py@luyten.fr> - 3.13.1-2
- Depend on gvfs-goa

* Tue Apr 29 2014 Richard Hughes <rhughes@redhat.com> - 3.13.1-1
- Update to 3.13.1

* Mon Mar 24 2014 Richard Hughes <rhughes@redhat.com> - 3.12.0-1
- Update to 3.12.0

* Tue Mar 18 2014 Richard Hughes <rhughes@redhat.com> - 3.11.92-1
- Update to 3.11.92

* Tue Mar 04 2014 Pierre-Yves Luyten <py@luyten.fr> - 3.11.91-1
- Update to 3.11.91

* Thu Feb 20 2014 Kalev Lember <kalevlember@gmail.com> - 3.11.90-2
- Rebuilt for cogl soname bump

* Wed Feb 19 2014 Kalev Lember <kalevlember@gmail.com> - 3.11.90-1
- Update to 3.11.90

* Mon Feb 10 2014 Peter Hutterer <peter.hutterer@redhat.com> - 3.11.5-2
- Rebuild for libevdev soname bump

* Wed Feb 05 2014 Adam Williamson <awilliam@redhat.com> - 3.11.5-1
- new upstream release

* Wed Feb 05 2014 Kalev Lember <kalevlember@gmail.com> - 3.11.4-2
- Rebuilt for cogl soname bump

* Tue Jan 14 2014 Pierre-Yves Luyten <py@luyten.fr> - 3.11.4-1
- new upstream release

* Fri Dec 27 2013 Adam Williamson <awilliam@redhat.com> - 3.11.3-1
- new upstream release, rebuild for new tracker

* Mon Oct 28 2013 Pierre-Yves Luyten <py@luyten.fr> - 3.11.1-1
- Upgrade to 3.11.1
    Improve list view
    Bug Fixes

* Mon Oct 14 2013 Pierre-Yves Luyten <py@luyten.fr> - 3.10.1-1
- Upgrade to 3.10.1
    Fix Tomboy / Gnote import

* Mon Sep 23 2013 Pierre-Yves Luyten <py@luyten.fr> - 3.10.0-1
- Upgrade to 3.10.0

* Mon Sep 02 2013 Pierre-Yves Luyten <py@luyten.fr> - 3.9.92-1
- Upgrade to 3.9.92

* Mon Sep 02 2013 Pierre-Yves Luyten <py@luyten.fr> - 3.9.91-1
- Upgrade to 3.9.91
    Ship appdata
    Update documentation
    Update about dialog
    Use native close button
    Do not abort when traker connection fails

* Tue Aug 20 2013 Pierre-Yves Luyten <py@luyten.fr> - 3.9.90-1
- Upgrade to 3.9.90
    Add a default provider setting
    Update the selection toolbar

* Fri Aug 09 2013 Kalev Lember <kalevlember@gmail.com> - 3.9.5-2
- Rebuilt for cogl 1.15.4 soname bump

* Fri Aug 02 2013 Pierre-Yves Luyten <py@luyten.fr> - 3.9.5-1
- Upgrade to 3.9.5
    Improve Zeitgeist integration
    Fix a crash when immediately closing a note

* Sun Jul 14 2013 Pierre-Yves Luyten <py@luyten.fr> - 3.9.4-1
- Upgrade to 3.9.4
    Rename Notes
    Ship a High Contrast Icon
    Use zeitgeist-2.0
    Use title as a window decoration

* Wed Jun 19 2013 Pierre-Yves Luyten <py@luyten.fr> - 3.9.3-1
- Upgrade to 3.9.3

* Thu May 30 2013 Pierre-Yves Luyten <py@luyten.fr> - 3.9.2-1
- Upgrade to 3.9.2

* Sat May 11 2013 Pierre-Yves Luyten <py@luyten.fr> - 3.9.1-1
- Upgrade to 3.9.1

* Thu May 09 2013 Pierre-Yves Luyten <py@luyten.fr> - 3.8.1-2
- Remove news duplicate, obsolete autoreconf and libgd.la exclude

* Thu Apr 18 2013 Pierre-Yves Luyten <py@luyten.fr> - 3.8.1-1
- New release

* Wed Mar 27 2013 Pierre-Yves Luyten <py@luyten.fr> - 3.8.0-1
- New release

* Mon Mar 18 2013 Pierre-Yves Luyten <py@luyten.fr> - 3.7.92-1
- New release

* Fri Mar 15 2013 Pierre-Yves Luyten <py@luyten.fr> - 3.7.91-3
- Fix icon update (timestamp) in post
- BuildRequire desktop-file-utils

* Wed Mar 13 2013 Pierre-Yves Luyten <py@luyten.fr> - 3.7.91-2
- Patch to get rid of GPLv2+
- Patch to use static link to libgd
- Use find_lang
- Remove define for url_ver
- desktop-file-validate
- update timestamp for icons
- BuildRequire gettext
- BuildRequire yelp-tools
- Provides bundled libgd
- Don't "clean"

* Sun Mar 10 2013 Pierre-Yves Luyten <py@luyten.fr> - 3.7.91-1
- Fix BuildRequires
- Update desktop database
- Add it

* Sun Feb 17 2013 Pierre-Yves Luyten <py@luyten.fr> - 3.7.90-1
- Bump release

* Sat Feb 02 2013 Pierre-Yves Luyten <py@luyten.fr> - 3.7.5-1
- Add cs.

* Mon Jan 14 2013 Pierre-Yves Luyten <py@luyten.fr> - 3.7.4-1
- Add ca pt zh. Remove upstreamed patch.

* Mon Dec 17 2012 Pierre-Yves Luyten <py@luyten.fr> - 3.7.3-1
- Initial package
