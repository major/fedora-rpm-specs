%global gjs_version 1.69.2
%global libadwaita_version 1.5
%global libshumate_version 1.2~alpha

%global tarball_version %%(echo %{version} | tr '~' '.')

%global __provides_exclude_from ^%{_libdir}/%{name}/.*\\.so.*$

Name:           gnome-maps
Version:        47.2
Release:        2%{?dist}
Summary:        Map application for GNOME

License:        GPL-2.0-or-later AND CC0-1.0
URL:            https://wiki.gnome.org/Apps/Maps
Source0:        https://download.gnome.org/sources/%{name}/47/%{name}-%{tarball_version}.tar.xz

BuildRequires:  gcc
BuildRequires:  gettext
BuildRequires:  gsettings-desktop-schemas
BuildRequires:  meson
BuildRequires:  pkgconfig(geoclue-2.0)
BuildRequires:  pkgconfig(geocode-glib-2.0)
BuildRequires:  pkgconfig(gio-2.0)
BuildRequires:  pkgconfig(gjs-1.0) >= %{gjs_version}
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(gobject-introspection-1.0)
BuildRequires:  pkgconfig(gtk4)
BuildRequires:  pkgconfig(gweather4)
BuildRequires:  pkgconfig(libadwaita-1) >= %{libadwaita_version}
BuildRequires:  pkgconfig(libportal)
BuildRequires:  pkgconfig(librsvg-2.0)
BuildRequires:  pkgconfig(libxml-2.0)
BuildRequires:  pkgconfig(rest-1.0)
BuildRequires:  pkgconfig(shumate-1.0) >= %{libshumate_version}
BuildRequires:  /usr/bin/appstream-util
BuildRequires:  /usr/bin/desktop-file-validate
# Required for tests.
BuildRequires:  libsecret

Requires:       dbus
Requires:       gdk-pixbuf2%{?_isa}
Requires:       geoclue2-libs%{?_isa}
Requires:       geocode-glib2%{?_isa}
Requires:       gjs%{?_isa} >= %{gjs_version}
Requires:       gobject-introspection%{?_isa}
Requires:       gsettings-desktop-schemas%{?_isa}
Requires:       gtk4%{?_isa}
Requires:       libadwaita%{?_isa} >= %{libadwaita_version}
Requires:       libgweather4%{?_isa}
Requires:       libportal%{?_isa}
Requires:       libshumate%{?_isa} >= %{libshumate_version}
Requires:       libsoup3%{?_isa}
Requires:       rest%{?_isa}

%description
GNOME Maps is a simple map application for the GNOME desktop.


%prep
%autosetup -p1 -n %{name}-%{tarball_version}


%build
%meson
%meson_build


%install
%meson_install

# Remove unneeded development files
rm %{buildroot}%{_libdir}/gnome-maps/libgnome-maps.so

%find_lang %{name}


%check
appstream-util validate-relax --nonet %{buildroot}%{_datadir}/metainfo/org.gnome.Maps.appdata.xml
desktop-file-validate %{buildroot}%{_datadir}/applications/org.gnome.Maps.desktop
%meson_test


%files -f %{name}.lang
%doc NEWS README
%license COPYING
%{_bindir}/%{name}
%{_datadir}/applications/org.gnome.Maps.desktop
%{_datadir}/dbus-1/services/org.gnome.Maps.service
%{_datadir}/glib-2.0/schemas/org.gnome.Maps.gschema.xml
%{_datadir}/%{name}
%{_datadir}/icons/hicolor/scalable/apps/org.gnome.Maps.svg
%{_datadir}/icons/hicolor/symbolic/apps/org.gnome.Maps-symbolic.svg
%{_metainfodir}/org.gnome.Maps.appdata.xml
%{_libdir}/%{name}/


%changelog
* Thu Jan 16 2025 Fedora Release Engineering <releng@fedoraproject.org> - 47.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Mon Nov 25 2024 nmontero <nmontero@redhat.com> - 47.2-1
- Update to 47.2

* Fri Oct 11 2024 David King <amigadave@amigadave.com> - 47.1-1
- Update to 47.1

* Mon Sep 16 2024 nmontero <nmontero@redhat.com> - 47.0-1
- Update to 47.0

* Sun Sep 01 2024 David King <amigadave@amigadave.com> - 47~rc-1
- Update to 47.rc

* Sun Aug 04 2024 David King <amigadave@amigadave.com> - 47~beta-1
- Update to 47.beta

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 47~alpha2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Mon Jul 08 2024 David King <amigadave@amigadave.com> - 47~alpha2-1
- Update to 47.alpha2

* Sun Jul 07 2024 David King <amigadave@amigadave.com> - 47~alpha-1
- Update to 47.alpha

* Mon May 13 2024 David King <amigadave@amigadave.com> - 46.11-1
- Update to 46.11

* Sat Apr 20 2024 David King <amigadave@amigadave.com> - 46.10-1
- Update to 46.10

* Sat Mar 16 2024 David King <amigadave@amigadave.com> - 46.0-1
- Update to 46.0

* Fri Mar 15 2024 David King <amigadave@amigadave.com> - 46~rc-1
- Update to 46.rc

* Wed Jan 24 2024 Fedora Release Engineering <releng@fedoraproject.org> - 45.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 45.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jan 11 2024 Kalev Lember <klember@redhat.com> - 45.3-1
- Update to 45.3

* Wed Dec 06 2023 Kalev Lember <klember@redhat.com> - 45.2-1
- Update to 45.2

* Sat Oct 21 2023 Kalev Lember <klember@redhat.com> - 45.1-1
- Update to 45.1

* Thu Oct 05 2023 Kalev Lember <klember@redhat.com> - 45.0-2
- Add missing libportal runtime requires (rhbz#2242300)

* Tue Sep 19 2023 Kalev Lember <klember@redhat.com> - 45.0-1
- Update to 45.0
- Add minimum required libadwaita version

* Tue Sep 05 2023 Kalev Lember <klember@redhat.com> - 45~rc-1
- Update to 45.rc

* Wed Aug 23 2023 Adam Williamson <awilliam@redhat.com> - 45~beta-2
- Backport MR #329 to fix focus on opening route planning

* Fri Aug 04 2023 Kalev Lember <klember@redhat.com> - 45~beta-1
- Update to 45.beta

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 45~alpha-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Mon Jul 03 2023 Kalev Lember <klember@redhat.com> - 45~alpha-1
- Update to 45.alpha

* Sat Jul 01 2023 Kalev Lember <klember@redhat.com> - 44.3-1
- Update to 44.3

* Wed May 31 2023 Kalev Lember <klember@redhat.com> - 44.2-1
- Update to 44.2

* Mon Apr 24 2023 David King <amigadave@amigadave.com> - 44.1-1
- Update to 44.1

* Sun Apr 02 2023 Kalev Lember <klember@redhat.com> - 44.0-4
- Add missing dep on gsettings-desktop-schemas

* Tue Mar 28 2023 Kalev Lember <klember@redhat.com> - 44.0-3
- Add missing runtime dep on rest

* Wed Mar 22 2023 Adam Williamson <awilliam@redhat.com> - 44.0-2
- Backport MR #295, another animation tile server ban fix (#2177995)

* Sat Mar 18 2023 David King <amigadave@amigadave.com> - 44.0-1
- Update to 44.0

* Wed Mar 15 2023 Adam Williamson <awilliam@redhat.com> - 44~rc-2
- Backport workaround for animation making tile server ban us (#2177995)

* Sat Mar 04 2023 David King <amigadave@amigadave.com> - 44~rc-1
- Update to 44.rc

* Mon Feb 06 2023 David King <amigadave@amigadave.com> - 44~beta-1
- Update to 44.beta

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 43.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Tue Dec 06 2022 David King <amigadave@amigadave.com> - 43.2-1
- Update to 43.2

* Thu Oct 27 2022 David King <amigadave@amigadave.com> - 43.1-1
- Update to 43.1

* Tue Sep 20 2022 Kalev Lember <klember@redhat.com> - 43.0-1
- Update to 43.0

* Tue Sep 06 2022 Kalev Lember <klember@redhat.com> - 43~rc-1
- Update to 43.rc

* Tue Aug 23 2022 Kalev Lember <klember@redhat.com> - 43~beta-2
- Add missing dep on libsoup3

* Tue Aug 23 2022 Kalev Lember <klember@redhat.com> - 43~beta-1
- Update to 43.beta

* Thu Aug 11 2022 Kalev Lember <klember@redhat.com> - 43~alpha-3
- Add missing runtime dep on geocode-glib (#2117588)

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 43~alpha-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jul 07 2022 David King <amigadave@amigadave.com> - 43~alpha-1
- Update to 43.alpha

* Wed Jul 06 2022 David King <amigadave@amigadave.com> - 42.3-1
- Update to 42.3

* Sun May 29 2022 David King <amigadave@amigadave.com> - 42.2-1
- Update to 42.2

* Sun Apr 24 2022 David King <amigadave@amigadave.com> - 42.1-1
- Update to 42.1

* Sat Mar 19 2022 David King <amigadave@amigadave.com> - 42.0-1
- Update to 42.0

* Mon Mar 07 2022 David King <amigadave@amigadave.com> - 42~rc-1
- Update to 42.rc

* Mon Feb 14 2022 David King <amigadave@amigadave.com> - 42~beta-1
- Update to 42.beta

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 42~alpha-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Sun Jan 09 2022 David King <amigadave@amigadave.com> - 42~alpha-1
- Update to 42.alpha

* Tue Dec 07 2021 Kalev Lember <klember@redhat.com> - 41.2-1
- Update to 41.2

* Mon Nov 01 2021 Kalev Lember <klember@redhat.com> - 41.1-1
- Update to 41.1

* Sat Sep 18 2021 Kalev Lember <klember@redhat.com> - 41.0-1
- Update to 41.0

* Wed Sep 08 2021 Kalev Lember <klember@redhat.com> - 41~rc-1
- Update to 41.rc

* Mon Aug 16 2021 Kalev Lember <klember@redhat.com> - 41~beta-1
- Update to 41.beta

* Tue Aug 03 2021 Kalev Lember <klember@redhat.com> - 41~alpha-1
- Update to 41.alpha

* Sun Aug 01 2021 Phil Wyett <philip.wyett@kathenas.org> - 40.3-1
- Update to 40.3

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 40.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Mon Jun 21 2021 Kalev Lember <klember@redhat.com> - 40.2-1
- Update to 40.2

* Wed May 05 2021 Kalev Lember <klember@redhat.com> - 40.1-1
- Update to 40.1

* Mon Mar 22 2021 Kalev Lember <klember@redhat.com> - 40.0-1
- Update to 40.0
- Add missing libhandy runtime dep

* Mon Mar 15 2021 Kalev Lember <klember@redhat.com> - 40~rc-1
- Update to 40.rc

* Thu Feb 18 2021 Kalev Lember <klember@redhat.com> - 40~beta-1
- Update to 40.beta

* Tue Feb 16 2021 Kalev Lember <klember@redhat.com> - 3.38.3-3
- Rebuilt for folks soname bump

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 3.38.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Sat Jan 16 2021 Kalev Lember <klember@redhat.com> - 3.38.3-1
- Update to 3.38.3

* Wed Nov 25 2020 Kalev Lember <klember@redhat.com> - 3.38.2-1
- Update to 3.38.2

* Fri Oct  9 2020 Kalev Lember <klember@redhat.com> - 3.38.1.1-1
- Update to 3.38.1.1

* Mon Oct  5 2020 Kalev Lember <klember@redhat.com> - 3.38.1-1
- Update to 3.38.1

* Sat Sep 12 2020 Kalev Lember <klember@redhat.com> - 3.38.0-1
- Update to 3.38.0

* Sun Sep 06 2020 Kalev Lember <klember@redhat.com> - 3.37.92-1
- Update to 3.37.92

* Sat Aug 22 2020 Kalev Lember <klember@redhat.com> - 3.37.91-1
- Update to 3.37.91

* Mon Aug 17 2020 Kalev Lember <klember@redhat.com> - 3.37.90-1
- Update to 3.37.90

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.37.3-3
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.37.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Jul 20 2020 Kalev Lember <klember@redhat.com> - 3.37.3-1
- Update to 3.37.3

* Thu Jun 04 2020 Kalev Lember <klember@redhat.com> - 3.37.2-1
- Update to 3.37.2

* Thu Apr 30 2020 Kalev Lember <klember@redhat.com> - 3.37.1-1
- Update to 3.37.1

* Sat Apr 25 2020 Kalev Lember <klember@redhat.com> - 3.36.2-1
- Update to 3.36.2

* Sat Mar 28 2020 Kalev Lember <klember@redhat.com> - 3.36.1-1
- Update to 3.36.1

* Sat Mar 07 2020 Kalev Lember <klember@redhat.com> - 3.36.0-1
- Update to 3.36.0

* Mon Mar 02 2020 Kalev Lember <klember@redhat.com> - 3.35.92-1
- Update to 3.35.92

* Mon Feb 17 2020 Kalev Lember <klember@redhat.com> - 3.35.91-1
- Update to 3.35.91

* Sun Feb 02 2020 Kalev Lember <klember@redhat.com> - 3.35.90-1
- Update to 3.35.90

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.35.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jan 16 2020 Kalev Lember <klember@redhat.com> - 3.35.3-1
- Update to 3.35.3

* Tue Jan 07 2020 Kalev Lember <klember@redhat.com> - 3.34.3-1
- Update to 3.34.3

* Wed Nov 27 2019 Kalev Lember <klember@redhat.com> - 3.34.2-1
- Update to 3.34.2

* Mon Oct 07 2019 Kalev Lember <klember@redhat.com> - 3.34.1-1
- Update to 3.34.1

* Mon Sep 09 2019 Kalev Lember <klember@redhat.com> - 3.34.0-1
- Update to 3.34.0

* Tue Sep 03 2019 Kalev Lember <klember@redhat.com> - 3.33.92-1
- Update to 3.33.92

* Mon Aug 19 2019 Kalev Lember <klember@redhat.com> - 3.33.91-1
- Update to 3.33.91

* Mon Aug 05 2019 Phil Wyett <philwyett@kathenas.org> - 3.33.90-1
- Update to 3.33.90.

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.33.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Mon Jul 15 2019 Kalev Lember <klember@redhat.com> - 3.33.4-1
- Update to 3.33.4

* Mon Jun 17 2019 Kalev Lember <klember@redhat.com> - 3.33.3-1
- Update to 3.33.3

* Thu Jun 06 2019 Phil Wyett <philwyett@kathenas.org> - 3.33.2-2
- Add upstream patch to fix crash running geocode contact requests

* Tue May 21 2019 Phil Wyett <philwyett@kathenas.org> - 3.33.2-1
- Update to 3.33.2

* Thu Apr 25 2019 Phil Wyett <philwyett@kathenas.org> - 3.33.1-1
- Update to 3.33.1

* Tue Apr 16 2019 Adam Williamson <awilliam@redhat.com> - 3.32.1-2
- Rebuild with Meson fix for #1699099

* Sun Mar 31 2019 Kalev Lember <klember@redhat.com> - 3.32.1-1
- Update to 3.32.1

* Mon Mar 11 2019 Kalev Lember <klember@redhat.com> - 3.32.0-1
- Update to 3.32.0

* Mon Mar 04 2019 Kalev Lember <klember@redhat.com> - 3.31.92-1
- Update to 3.31.92

* Tue Feb 19 2019 Kalev Lember <klember@redhat.com> - 3.31.91-2
- Rebuilt against fixed atk (#1626575)

* Tue Feb 19 2019 Kalev Lember <klember@redhat.com> - 3.31.91-1
- Update to 3.31.91

* Mon Feb 04 2019 Phil Wyett <philwyett@kathenas.org> - 3.31.90-1
- Update to 3.31.90

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.31.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Mon Jan 07 2019 Kalev Lember <klember@redhat.com> - 3.31.4-1
- Update to 3.31.4

* Wed Dec 12 2018 Phil Wyett <philwyett@kathenas.org> - 3.31.3-1
- Update to 3.31.3

* Mon Oct 22 2018 Debarshi Ray <rishi@fedoraproject.org> - 3.31.1-1
- Update to 3.31.1

* Mon Oct 22 2018 Debarshi Ray <rishi@fedoraproject.org> - 3.30.1-2
- Prevent crashes when clicking on "What's here?"

* Wed Sep 26 2018 Kalev Lember <klember@redhat.com> - 3.30.1-1
- Update to 3.30.1

* Fri Sep 07 2018 Kalev Lember <klember@redhat.com> - 3.30.0-1
- Update to 3.30.0
- Switch to the meson build system

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.28.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue May 08 2018 Kalev Lember <klember@redhat.com> - 3.28.2-1
- Update to 3.28.2

* Mon Apr 09 2018 Kalev Lember <klember@redhat.com> - 3.28.1-1
- Update to 3.28.1

* Mon Mar 12 2018 Kalev Lember <klember@redhat.com> - 3.28.0-1
- Update to 3.28.0

* Mon Mar 05 2018 Kalev Lember <klember@redhat.com> - 3.27.92-1
- Update to 3.27.92

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.27.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Fri Jan 05 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 3.27.1-2
- Remove obsolete scriptlets

* Thu Nov 02 2017 Kalev Lember <klember@redhat.com> - 3.27.1-1
- Update to 3.27.1

* Wed Nov 01 2017 Kalev Lember <klember@redhat.com> - 3.26.2-1
- Update to 3.26.2

* Sun Oct 08 2017 Kalev Lember <klember@redhat.com> - 3.26.1-1
- Update to 3.26.1

* Wed Sep 13 2017 Kalev Lember <klember@redhat.com> - 3.26.0-1
- Update to 3.26.0

* Thu Sep 07 2017 Kalev Lember <klember@redhat.com> - 3.25.92-1
- Update to 3.25.92

* Mon Aug 28 2017 Kalev Lember <klember@redhat.com> - 3.25.91-1
- Update to 3.25.91

* Tue Aug 15 2017 Kalev Lember <klember@redhat.com> - 3.25.90-1
- Update to 3.25.90

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.25.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.25.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Thu Jul 20 2017 Kalev Lember <klember@redhat.com> - 3.25.4-1
- Update to 3.25.4

* Sun Jun 25 2017 Kalev Lember <klember@redhat.com> - 3.25.3-1
- Update to 3.25.3

* Mon Jun 12 2017 Kalev Lember <klember@redhat.com> - 3.25.2-1
- Update to 3.25.2

* Wed May 10 2017 Kalev Lember <klember@redhat.com> - 3.24.2-1
- Update to 3.24.2

* Tue Apr 11 2017 Kalev Lember <klember@redhat.com> - 3.24.1-1
- Update to 3.24.1

* Tue Mar 21 2017 Kalev Lember <klember@redhat.com> - 3.24.0-1
- Update to 3.24.0

* Thu Mar 16 2017 Kalev Lember <klember@redhat.com> - 3.23.92-1
- Update to 3.23.92

* Tue Feb 28 2017 Richard Hughes <rhughes@redhat.com> - 3.23.91-1
- Update to 3.23.91

* Tue Feb 14 2017 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 3.23.90-1
- Update to 3.23.90

* Mon Feb 13 2017 Richard Hughes <rhughes@redhat.com> - 3.23.4-1
- Update to 3.23.4

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.23.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Dec 01 2016 Kalev Lember <klember@redhat.com> - 3.23.2-1
- Update to 3.23.2

* Sun Oct 30 2016 Kalev Lember <klember@redhat.com> - 3.23.1-1
- Update to 3.23.1

* Wed Oct 12 2016 Kalev Lember <klember@redhat.com> - 3.22.1-1
- Update to 3.22.1

* Mon Sep 19 2016 Kalev Lember <klember@redhat.com> - 3.22.0-1
- Update to 3.22.0

* Wed Sep 14 2016 Kalev Lember <klember@redhat.com> - 3.21.92-2
- Set minimum champlain and gjs versions
- Tighten dependencies with the _isa macro

* Wed Sep 14 2016 Kalev Lember <klember@redhat.com> - 3.21.92-1
- Update to 3.21.92

* Fri Sep 02 2016 Kalev Lember <klember@redhat.com> - 3.21.91-1
- Update to 3.21.91
- Drop old emerillon obsoletes

* Tue Aug 23 2016 Kalev Lember <klember@redhat.com> - 3.21.90-1
- Update to 3.21.90

* Sat Jul 30 2016 Michael Catanzaro <mcatanzaro@gnome.org> - 3.21.4-1
- Update to 3.21.4

* Mon Jun 27 2016 Kalev Lember <klember@redhat.com> - 3.20.1-2
- Fix missing geoclue2-libs dependency (#1350009)

* Wed Apr 13 2016 Kalev Lember <klember@redhat.com> - 3.20.1-1
- Update to 3.20.1

* Tue Mar 22 2016 Kalev Lember <klember@redhat.com> - 3.20.0-1
- Update to 3.20.0

* Tue Mar 15 2016 Richard Hughes <rhughes@redhat.com> - 3.19.92-1
- Update to 3.19.92

* Thu Mar 03 2016 Kalev Lember <klember@redhat.com> - 3.19.91-2
- Backport a fix for a crash under the Wayland session

* Wed Mar 02 2016 Richard Hughes <rhughes@redhat.com> - 3.19.91-1
- Update to 3.19.91

* Tue Feb 16 2016 David King <amigadave@amigadave.com> - 3.19.90-1
- Update to 3.19.90

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 3.19.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Tue Jan 19 2016 David King <amigadave@amigadave.com> - 3.19.4-1
- Update to 3.19.4

* Mon Dec 14 2015 Kalev Lember <klember@redhat.com> - 3.19.3-1
- Update to 3.19.3

* Sun Nov 22 2015 Kalev Lember <klember@redhat.com> - 3.19.2-1
- Update to 3.19.2

* Tue Nov 10 2015 Kalev Lember <klember@redhat.com> - 3.18.2-1
- Update to 3.18.2

* Sun Oct 18 2015 Kalev Lember <klember@redhat.com> - 3.18.1-2
- Remove unneeded development files (#1272739)

* Sun Oct 11 2015 Kalev Lember <klember@redhat.com> - 3.18.1-1
- Update to 3.18.1

* Fri Sep 25 2015 Kalev Lember <klember@redhat.com> - 3.18.0.1-1
- Update to 3.18.0.1

* Sun Sep 20 2015 Kalev Lember <klember@redhat.com> - 3.18.0-1
- Update to 3.18.0
- Update URL

* Mon Sep 14 2015 Kalev Lember <klember@redhat.com> - 3.17.92-1
- Update to 3.17.92

* Sat Aug 29 2015 Kalev Lember <klember@redhat.com> - 3.17.91-1
- Update to 3.17.91

* Sat Aug 22 2015 Kalev Lember <klember@redhat.com> - 3.17.90.1-1
- Update to 3.17.90.1

* Sun Aug 16 2015 Kalev Lember <klember@redhat.com> - 3.17.90-1
- Update to 3.17.90

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.17.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Thu May 07 2015 Debarshi Ray <rishi@fedoraproject.org> - 3.17.1-2
- Add a run-time dependency on gfbgraph

* Fri May 01 2015 Kalev Lember <kalevlember@gmail.com> - 3.17.1-1
- Update to 3.17.1

* Tue Apr 14 2015 Kalev Lember <kalevlember@gmail.com> - 3.16.1-1
- Update to 3.16.1

* Mon Mar 23 2015 Kalev Lember <kalevlember@gmail.com> - 3.16.0-1
- Update to 3.16.0

* Tue Mar 17 2015 Kalev Lember <kalevlember@gmail.com> - 3.15.92-1
- Update to 3.15.92

* Sun Mar 01 2015 David King <amigadave@amigadave.com> - 3.15.91-1
- Update to 3.15.91

* Wed Feb 18 2015 David King <amigadave@amigadave.com> - 3.15.90.2-1
- Update to 3.15.90.2

* Sun Feb 15 2015 David King <amigadave@amigadave.com> - 3.15.90-1
- Update to 3.15.90.1
- Use license macro for COPYING
- Validate AppData in check
- Use pkgconfig for BuildRequires
- Add NEWS and README to doc

* Mon Jan 19 2015 Richard Hughes <rhughes@redhat.com> - 3.15.4-1
- Update to 3.15.4

* Fri Dec 19 2014 Richard Hughes <rhughes@redhat.com> - 3.15.3.2-1
- Update to 3.15.3.2

* Tue Nov 25 2014 Kalev Lember <kalevlember@gmail.com> - 3.15.2-1
- Update to 3.15.2

* Mon Nov 10 2014 Kalev Lember <kalevlember@gmail.com> - 3.14.2-1
- Update to 3.14.2

* Mon Oct 13 2014 Kalev Lember <kalevlember@gmail.com> - 3.14.1.2-1
- Update to 3.14.1.2

* Sat Oct 11 2014 Kalev Lember <kalevlember@gmail.com> - 3.14.1-1
- Update to 3.14.1

* Mon Sep 22 2014 Kalev Lember <kalevlember@gmail.com> - 3.14.0-1
- Update to 3.14.0

* Tue Sep 16 2014 Kalev Lember <kalevlember@gmail.com> - 3.13.92-1
- Update to 3.13.92

* Wed Sep 03 2014 Kalev Lember <kalevlember@gmail.com> - 3.13.91-1
- Update to 3.13.91
- Include HighContrast icons

* Sat Aug 16 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.13.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jul 19 2014 Kalev Lember <kalevlember@gmail.com> - 3.13.4-1
- Update to 3.13.4

* Wed Jun 25 2014 Richard Hughes <rhughes@redhat.com> - 3.13.3-1
- Update to 3.13.3

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.13.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Tue May 27 2014 Kalev Lember <kalevlember@gmail.com> - 3.13.2-1
- Update to 3.13.2

* Thu May 15 2014 Kalev Lember <kalevlember@gmail.com> - 3.12.2-1
- Update to 3.12.2

* Tue Apr 15 2014 Kalev Lember <kalevlember@gmail.com> - 3.12.1-1
- Update to 3.12.1

* Mon Mar 24 2014 Richard Hughes <rhughes@redhat.com> - 3.12.0-1
- Update to 3.12.0

* Tue Mar 18 2014 Richard Hughes <rhughes@redhat.com> - 3.11.92-1
- Update to 3.11.92

* Tue Mar 04 2014 Richard Hughes <rhughes@redhat.com> - 3.11.91-1
- Update to 3.11.91

* Tue Feb 18 2014 Richard Hughes <rhughes@redhat.com> - 3.11.90-1
- Update to 3.11.90

* Wed Feb 05 2014 Richard Hughes <rhughes@redhat.com> - 3.11.5.1-1
- Update to 3.11.5.1

* Wed Feb 05 2014 Richard Hughes <rhughes@redhat.com> - 3.11.5-1
- Update to 3.11.5

* Wed Jan 15 2014 Richard Hughes <rhughes@redhat.com> - 3.11.4.1-1
- Update to 3.11.4.1

* Mon Nov 25 2013 Richard Hughes <rhughes@redhat.com> - 3.11.2-1
- Update to 3.11.2

* Thu Nov 14 2013 Richard Hughes <rhughes@redhat.com> - 3.10.2-1
- Update to 3.10.2

* Wed Sep 25 2013 Kalev Lember <kalevlember@gmail.com> - 3.10.0-1
- Update to 3.10.0

* Wed Sep 18 2013 Kalev Lember <kalevlember@gmail.com> - 3.9.92-2
- Build the package as noarch

* Wed Sep 18 2013 Kalev Lember <kalevlember@gmail.com> - 3.9.92-1
- Update to 3.9.92

* Sun Sep 08 2013 Elad Alfassa <elad@fedoraproject.org> - 3.9.91-2
- Remove useless debuginfo package

* Tue Sep 03 2013 Kalev Lember <kalevlember@gmail.com> - 3.9.91-1
- Update to 3.9.91

* Tue Aug 27 2013 Elad Alfassa <elad@fedoraproject.org> - 3.9.90.2-3
- Add requires on gjs
- Make sure we have the right architecture of libraries installed

* Tue Aug 27 2013 Elad Alfassa <elad@fedoraproject.org> - 3.9.90.2-2
- Fix issues from review

* Sat Aug 24 2013 Elad Alfassa <elad@fedoraproject.org> - 3.9.90.2-1
- Now uses the geoclue dbus service instead of the library
- gnome-maps is JS only, so it should be a noarch package

* Sat Aug 24 2013 Elad Alfassa <elad@fedoraproject.org> - 3.9.90.1-2
- Add missing icon-cache update and glib schema compilation scripts

* Fri Aug 23 2013 Elad Alfassa <elad@fedoraproject.org> - 3.9.90.1-1
- Initial packaging for review
