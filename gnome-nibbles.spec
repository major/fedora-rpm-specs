%global app_id  org.gnome.Nibbles

Name:           gnome-nibbles
Version:        3.38.2
Release:        7%{?dist}
Summary:        GNOME Nibbles game
License:        GPL-3.0-or-later AND BSD-2-Clause AND GFDL-1.1-no-invariants-or-later
URL:            https://wiki.gnome.org/Apps/Nibbles
Source0:        https://download.gnome.org/sources/gnome-nibbles/3.38/gnome-nibbles-%{version}.tar.xz
# https://bugzilla.redhat.com/show_bug.cgi?id=1987505
Patch0:         1b48446068608aff9b5edf1fdbd4b8c0d9f0be94.patch
Patch1:         62964e9256fcac616109af874dbb2bd8342a9853.patch

BuildRequires:  desktop-file-utils
BuildRequires:  gcc
BuildRequires:  gettext
BuildRequires:  itstool
BuildRequires:  libappstream-glib
BuildRequires:  meson
BuildRequires:  vala
BuildRequires:  pkgconfig(clutter-1.0) >= 1.22.0
BuildRequires:  pkgconfig(clutter-gtk-1.0) >= 1.4.0
BuildRequires:  pkgconfig(gee-0.8)
BuildRequires:  pkgconfig(gio-2.0) >= 2.42.0
BuildRequires:  pkgconfig(gsound) >= 1.0.2
BuildRequires:  pkgconfig(gtk+-3.0) >= 3.24.0
BuildRequires:  pkgconfig(libgnome-games-support-1) >= 1.7.1

Obsoletes: gnome-games-extra < 1:3.7.4
Obsoletes: gnome-games-gnibbles < 1:3.7.4

%description
Pilot a worm around a maze trying to collect diamonds and at the same time
avoiding the walls and yourself. With each diamond your worm grows longer and
navigation becomes more and more difficult. Playable by up to four people.

%prep
%autosetup -p1


%build
%meson
%meson_build


%install
%meson_install

%find_lang %{name} --with-gnome


%check
desktop-file-validate %{buildroot}%{_datadir}/applications/%{app_id}.desktop
appstream-util validate-relax --nonet %{buildroot}%{_metainfodir}/%{app_id}.appdata.xml


%files -f %{name}.lang
%license COPYING
%{_bindir}/gnome-nibbles
%{_datadir}/applications/%{app_id}.desktop
%{_datadir}/dbus-1/services/%{app_id}.service
%{_datadir}/glib-2.0/schemas/%{app_id}.gschema.xml
%{_datadir}/%{name}/
%{_datadir}/icons/hicolor/*/*/%{app_id}*
%{_metainfodir}/%{app_id}.appdata.xml
%{_mandir}/man6/gnome-nibbles.6*


%changelog
* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 3.38.2-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 3.38.2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 3.38.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Tue Nov 09 2021 Yaakov Selkowitz <yselkowi@redhat.com> - 3.38.2-4
- Cherry-pick upstream build fixes for Vala 0.52 (#1987505)

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 3.38.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 3.38.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Nov  4 2020 Kalev Lember <klember@redhat.com> - 3.38.2-1
- Update to 3.38.2

* Mon Oct  5 2020 Kalev Lember <klember@redhat.com> - 3.38.1-1
- Update to 3.38.1

* Sat Sep 12 2020 Kalev Lember <klember@redhat.com> - 3.38.0-1
- Update to 3.38.0

* Mon Aug 17 2020 Kalev Lember <klember@redhat.com> - 3.37.90-1
- Update to 3.37.90

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.36.1-3
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.36.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Jul 20 2020 Kalev Lember <klember@redhat.com> - 3.36.1-1
- Update to 3.36.1

* Sun Mar 08 2020 Kalev Lember <klember@redhat.com> - 3.36.0-1
- Update to 3.36.0

* Mon Feb 17 2020 Kalev Lember <klember@redhat.com> - 3.35.90-1
- Update to 3.35.90

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.34.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Tue Jan 07 2020 Kalev Lember <klember@redhat.com> - 3.34.2-1
- Update to 3.34.2

* Mon Oct 07 2019 Kalev Lember <klember@redhat.com> - 3.34.1-1
- Update to 3.34.1

* Thu Sep 12 2019 Kalev Lember <klember@redhat.com> - 3.34.0-1
- Update to 3.34.0

* Tue Aug 20 2019 Kalev Lember <klember@redhat.com> - 3.33.90-1
- Update to 3.33.90
- Switch to the meson build system

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.31.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.31.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Wed Jan 23 2019 Kalev Lember <klember@redhat.com> - 3.31.3-1
- Update to 3.31.3

* Tue Sep 04 2018 Kalev Lember <klember@redhat.com> - 3.24.1-1
- Update to 3.24.1

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.24.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Mon Feb 19 2018 Michael Catanzaro <mcatanzaro@gnome.org> - 3.24.0-6
- Rebuilt for libgnome-games-support soname bump

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.24.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jan 11 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 3.24.0-4
- Remove obsolete scriptlets

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.24.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.24.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Tue Mar 21 2017 Kalev Lember <klember@redhat.com> - 3.24.0-1
- Update to 3.24.0

* Thu Mar 16 2017 Kalev Lember <klember@redhat.com> - 3.23.92-1
- Update to 3.23.92

* Mon Mar 06 2017 Kalev Lember <klember@redhat.com> - 3.23.91-1
- Update to 3.23.91

* Mon Feb 13 2017 Richard Hughes <rhughes@redhat.com> - 3.23.2-1
- Update to 3.23.2

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.23.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Sun Oct 30 2016 Kalev Lember <klember@redhat.com> - 3.23.1-1
- Update to 3.23.1

* Wed Oct 12 2016 Kalev Lember <klember@redhat.com> - 3.22.1-1
- Update to 3.22.1

* Tue Sep 20 2016 Kalev Lember <klember@redhat.com> - 3.22.0-1
- Update to 3.22.0

* Tue Sep 13 2016 Kalev Lember <klember@redhat.com> - 3.21.92-1
- Update to 3.21.92

* Fri Sep 02 2016 Kalev Lember <klember@redhat.com> - 3.21.91-1
- Update to 3.21.91

* Thu Aug 18 2016 Kalev Lember <klember@redhat.com> - 3.21.90-1
- Update to 3.21.90
- Move desktop file validation to the check section

* Sun Jul 17 2016 Kalev Lember <klember@redhat.com> - 3.21.4-1
- Update to 3.21.4

* Wed Jun 22 2016 Richard Hughes <rhughes@redhat.com> - 3.21.3-1
- Update to 3.21.3

* Mon May 09 2016 Kalev Lember <klember@redhat.com> - 3.20.2.1-1
- Update to 3.20.2.1

* Wed Apr 13 2016 Kalev Lember <klember@redhat.com> - 3.20.1-1
- Update to 3.20.1

* Wed Mar 23 2016 Kalev Lember <klember@redhat.com> - 3.20.0-1
- Update to 3.20.0

* Tue Mar 15 2016 Richard Hughes <rhughes@redhat.com> - 3.19.92-1
- Update to 3.19.92

* Mon Feb 29 2016 Richard Hughes <rhughes@redhat.com> - 3.19.91-1
- Update to 3.19.91

* Tue Feb 16 2016 Richard Hughes <rhughes@redhat.com> - 3.19.90-1
- Update to 3.19.90

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 3.19.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jan 20 2016 Kalev Lember <klember@redhat.com> - 3.19.4-1
- Update to 3.19.4

* Mon Dec 14 2015 Kalev Lember <klember@redhat.com> - 3.19.3-1
- Update to 3.19.3
- Update download URLs

* Tue Nov 10 2015 Kalev Lember <klember@redhat.com> - 3.18.2-1
- Update to 3.18.2

* Sun Oct 11 2015 Kalev Lember <klember@redhat.com> - 3.18.1-1
- Update to 3.18.1

* Mon Sep 21 2015 Kalev Lember <klember@redhat.com> - 3.18.0-1
- Update to 3.18.0

* Thu Aug 13 2015 Kalev Lember <klember@redhat.com> - 3.17.90-1
- Update to 3.17.90
- Use make_install macro

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.16.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Tue Apr 14 2015 Kalev Lember <kalevlember@gmail.com> - 3.16.1-1
- Update to 3.16.1

* Mon Mar 23 2015 Kalev Lember <kalevlember@gmail.com> - 3.16.0-1
- Update to 3.16.0

* Tue Mar 17 2015 Kalev Lember <kalevlember@gmail.com> - 3.15.92-1
- Update to 3.15.92

* Tue Mar 03 2015 Kalev Lember <kalevlember@gmail.com> - 3.15.91.1-1
- Update to 3.15.91.1
- Use the %%license macro for the COPYING file

* Tue Feb 17 2015 Richard Hughes <rhughes@redhat.com> - 3.15.90-1
- Update to 3.15.90

* Mon Oct 13 2014 Kalev Lember <kalevlember@gmail.com> - 3.14.1-1
- Update to 3.14.1

* Mon Sep 22 2014 Kalev Lember <kalevlember@gmail.com> - 3.14.0-1
- Update to 3.14.0

* Tue Sep 16 2014 Kalev Lember <kalevlember@gmail.com> - 3.13.92-1
- Update to 3.13.92

* Mon Sep 01 2014 Kalev Lember <kalevlember@gmail.com> - 3.13.91-1
- Update to 3.13.91

* Tue Aug 19 2014 Kalev Lember <kalevlember@gmail.com> - 3.13.90-1
- Update to 3.13.90

* Sat Aug 16 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.12.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.12.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Thu May 15 2014 Kalev Lember <kalevlember@gmail.com> - 3.12.2-1
- Update to 3.12.2

* Tue Apr 15 2014 Kalev Lember <kalevlember@gmail.com> - 3.12.1-1
- Update to 3.12.1

* Mon Mar 24 2014 Richard Hughes <rhughes@redhat.com> - 3.12.0-1
- Update to 3.12.0

* Wed Mar 19 2014 Kalev Lember <kalevlember@gmail.com> - 3.11.92-2
- Don't install as setgid games

* Mon Mar 17 2014 Richard Hughes <rhughes@redhat.com> - 3.11.92-1
- Update to 3.11.92

* Thu Feb 20 2014 Kalev Lember <kalevlember@gmail.com> - 3.11.90.1-2
- Rebuilt for cogl soname bump

* Mon Feb 17 2014 Richard Hughes <rhughes@redhat.com> - 3.11.90.1-1
- Update to 3.11.90.1

* Mon Feb 10 2014 Peter Hutterer <peter.hutterer@redhat.com> - 3.11.5-3
- Rebuild for libevdev soname bump

* Wed Feb 05 2014 Kalev Lember <kalevlember@gmail.com> - 3.11.5-2
- Rebuilt for cogl soname bump

* Tue Feb 04 2014 Richard Hughes <rhughes@redhat.com> - 3.11.5-1
- Update to 3.11.5

* Tue Oct 29 2013 Richard Hughes <rhughes@redhat.com> - 3.11.1-1
- Update to 3.11.1

* Wed Sep 25 2013 Kalev Lember <kalevlember@gmail.com> - 3.10.0-1
- Update to 3.10.0

* Wed Sep 18 2013 Kalev Lember <kalevlember@gmail.com> - 3.9.92-1
- Update to 3.9.92
- Include the appdata file

* Fri Aug 09 2013 Kalev Lember <kalevlember@gmail.com> - 3.8.0-4
- Rebuilt for cogl 1.15.4 soname bump

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.8.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Sat Jun 22 2013 Kalev Lember <kalevlember@gmail.com> - 3.8.0-2
- Obsolete gnome-games-extra (for upgrades from f17)

* Fri Mar 29 2013 Tanner Doshier <doshitan@gmail.com> - 3.8.0-1
- Update to 3.8.0
- Add high contrast icons
- Use old desktop file name
- Use setgid games

* Wed Mar 6 2013 Tanner Doshier <doshitan@gmail.com> - 3.7.4-1
- Initial packaging of standalone gnome-nibbles
