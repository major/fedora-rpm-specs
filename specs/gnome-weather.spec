%global gobject_introspection_version 1.35.9
%global gtk4_version 4.5
%global gjs_version 1.71.0

%global tarball_version %%(echo %{version} | tr '~' '.')

Name:		gnome-weather
Version:	47.0
Release:	2%{?dist}
Summary:	A weather application for GNOME

License:	GPL-2.0-or-later AND BSD-3-Clause and CC-BY-3.0 and CC-BY-SA-3.0
URL:		https://wiki.gnome.org/Apps/Weather
Source0:	https://download.gnome.org/sources/%{name}/47/%{name}-%{tarball_version}.tar.xz

BuildArch:	noarch

BuildRequires:	desktop-file-utils
BuildRequires:	gettext
BuildRequires:	meson
BuildRequires:	python3-devel
BuildRequires:	pkgconfig(geoclue-2.0)
BuildRequires:	pkgconfig(gjs-1.0) >= %{gjs_version}
BuildRequires:	pkgconfig(glib-2.0)
BuildRequires:	pkgconfig(gobject-introspection-1.0) >= %{gobject_introspection_version}
BuildRequires:	pkgconfig(gtk4) >= %{gtk4_version}
BuildRequires:	pkgconfig(gweather4)
BuildRequires:	pkgconfig(libadwaita-1)

Requires:	gdk-pixbuf2
Requires:	geoclue2-libs
Requires:	gjs >= %{gjs_version}
Requires:	glib2
Requires:	gobject-introspection >= %{gobject_introspection_version}
Requires:	gsettings-desktop-schemas
Requires:	gtk4 >= %{gtk4_version}
Requires:	libadwaita
Requires:	libgweather4

%description
gnome-weather is a weather application for GNOME

%prep
%autosetup -p1 -n %{name}-%{tarball_version}
%{__python3} %{_rpmconfigdir}/redhat/pathfix.py -i %{__python3} .

%build
%meson
%meson_build

%install
%meson_install

%find_lang org.gnome.Weather

%check
desktop-file-validate %{buildroot}%{_datadir}/applications/org.gnome.Weather.desktop

%files -f org.gnome.Weather.lang
%license COPYING.md
%doc NEWS data/CREDITS
%{_bindir}/gnome-weather
%{_datadir}/applications/org.gnome.Weather.desktop
%{_datadir}/dbus-1/services/org.gnome.Weather.service
%{_datadir}/dbus-1/services/org.gnome.Weather.BackgroundService.service
%{_datadir}/glib-2.0/schemas/org.gnome.Weather.gschema.xml
%dir %{_datadir}/gnome-shell/
%dir %{_datadir}/gnome-shell/search-providers/
%{_datadir}/gnome-shell/search-providers/org.gnome.Weather.search-provider.ini
%{_datadir}/icons/hicolor/*/apps/org.gnome.Weather*
%{_datadir}/icons/hicolor/scalable/status/*.svg
%{_datadir}/metainfo/org.gnome.Weather.appdata.xml
%{_datadir}/org.gnome.Weather/

%changelog
* Thu Jan 16 2025 Fedora Release Engineering <releng@fedoraproject.org> - 47.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Wed Sep 18 2024 nmontero <nmontero@redhat.com> - 47.0-1
- Update to 47.0

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 47~alpha-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Sun Jul 14 2024 David King <amigadave@amigadave.com> - 47~alpha-1
- Update to 47.alpha

* Fri Mar 22 2024 David King <amigadave@amigadave.com> - 46.0-1
- Update to 46.0

* Wed Jan 24 2024 Fedora Release Engineering <releng@fedoraproject.org> - 45.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 45.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Sep 20 2023 Kalev Lember <klember@redhat.com> - 45.0-1
- Update to 45.0

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 45~alpha-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Tue Jul 04 2023 Kalev Lember <klember@redhat.com> - 45~alpha-1
- Update to 45.alpha

* Mon Mar 06 2023 David King <amigadave@amigadave.com> - 44~rc-1
- Update to 44.rc

* Wed Feb 15 2023 David King <amigadave@amigadave.com> - 44~beta-1
- Update to 44.beta

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 43.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Tue Sep 20 2022 Kalev Lember <klember@redhat.com> - 43.0-1
- Update to 43.0
- Build the package as noarch

* Tue Sep 06 2022 Kalev Lember <klember@redhat.com> - 43~rc-1
- Update to 43.rc

* Mon Aug 08 2022 Kalev Lember <klember@redhat.com> - 43~beta-1
- Update to 43.beta

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 43~alpha-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon Jul 18 2022 Kalev Lember <klember@redhat.com> - 43~alpha-1
- Update to 43.alpha

* Mon Mar 21 2022 David King <amigadave@amigadave.com> - 42.0-1
- Update to 42.0

* Tue Mar 08 2022 David King <amigadave@amigadave.com> - 42~rc-1
- Update to 42.rc

* Wed Feb 16 2022 David King <amigadave@amigadave.com> - 42~beta-1
- Update to 42.beta

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 42~alpha-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Jan 12 2022 David King <amigadave@amigadave.com> - 42~alpha-1
- Update to 42.alpha

* Tue Oct 05 2021 Kalev Lember <klember@redhat.com> - 41.0-2
- Make the package archful again

* Tue Sep 21 2021 Kalev Lember <klember@redhat.com> - 41.0-1
- Update to 41.0

* Wed Aug 18 2021 Kalev Lember <klember@redhat.com> - 40.1-1
- Update to 40.1

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 40.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Mon Mar 22 2021 Kalev Lember <klember@redhat.com> - 40.0-1
- Update to 40.0

* Wed Feb 17 2021 Kalev Lember <klember@redhat.com> - 40~beta-1
- Update to 40.beta
- Drop old obsoletes

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 3.36.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.36.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Apr 10 2020 Kalev Lember <klember@redhat.com> - 3.36.1-1
- Update to 3.36.1

* Mon Apr 06 2020 Kalev Lember <klember@redhat.com> - 3.36.0-1
- Update to 3.36.0

* Fri Apr 03 2020 Kalev Lember <klember@redhat.com> - 3.34.1-1
- Update to 3.34.1

* Wed Mar 25 2020 Michael Catanzaro <mcatanzaro@redhat.com> - 3.34.0-3
- Fix weather selecting the wrong cites. Also: deduplicate recent cities.

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.34.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Sep 25 2019 Kalev Lember <klember@redhat.com> - 3.34.0-1
- Update to 3.34.0

* Mon Aug 12 2019 Kalev Lember <klember@redhat.com> - 3.33.90-1
- Update to 3.33.90

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.32.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Tue Jun 11 2019 Kalev Lember <klember@redhat.com> - 3.32.2-2
- Add a few missing requires

* Mon May 06 2019 Kalev Lember <klember@redhat.com> - 3.32.2-1
- Update to 3.32.2

* Tue Apr 16 2019 Adam Williamson <awilliam@redhat.com> - 3.32.1-2
- Rebuild with Meson fix for #1699099

* Sat Apr 06 2019 Kalev Lember <klember@redhat.com> - 3.32.1-1
- Update to 3.32.1

* Mon Mar 11 2019 Kalev Lember <klember@redhat.com> - 3.32.0-1
- Update to 3.32.0

* Tue Mar 05 2019 Kalev Lember <klember@redhat.com> - 3.31.92-1
- Update to 3.31.92

* Mon Feb 04 2019 Kalev Lember <klember@redhat.com> - 3.31.90-1
- Update to 3.31.90
- Switch to the meson build system
- Drop -tests subpackage as the installed tests are gone upstream

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.31.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sun Dec 16 2018 Phil Wyett <philwyett@kathenas.org> - 3.31.3-1
- Update to 3.31.3

* Tue Aug 07 2018 Merlin Mathesius <mmathesi@redhat.com> - 3.26.0-6
- Fix unversioned python shebang lines

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.26.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.26.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Fri Jan 05 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 3.26.0-3
- Remove obsolete scriptlets

* Thu Sep 21 2017 Kalev Lember <klember@redhat.com> - 3.26.0-2
- Update gjs minimum required version (#1490432)

* Mon Sep 11 2017 Kalev Lember <klember@redhat.com> - 3.26.0-1
- Update to 3.26.0

* Thu Sep 07 2017 Kalev Lember <klember@redhat.com> - 3.25.92-1
- Update to 3.25.92

* Mon Aug 28 2017 Kalev Lember <klember@redhat.com> - 3.25.91-1
- Update to 3.25.91

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.24.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Tue Mar 21 2017 Kalev Lember <klember@redhat.com> - 3.24.0-1
- Update to 3.24.0

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.20.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Aug 17 2016 Kalev Lember <klember@redhat.com> - 3.20.2-1
- Update to 3.20.2

* Mon May 09 2016 Kalev Lember <klember@redhat.com> - 3.20.1-1
- Update to 3.20.1

* Tue Mar 22 2016 Kalev Lember <klember@redhat.com> - 3.20.0-1
- Update to 3.20.0

* Tue Mar 15 2016 Richard Hughes <rhughes@redhat.com> - 3.19.92-1
- Update to 3.19.92

* Tue Feb 16 2016 Richard Hughes <rhughes@redhat.com> - 3.19.90-1
- Update to 3.19.90

* Sat Feb 13 2016 Ralf Corsépius <corsepiu@fedoraproject.org> - 3.19.1-3
- Add BR: pkgconfig(libgeoclue-2.0) (Fix F24FTBFS).

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 3.19.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Tue Jan 26 2016 Richard Hughes <rhughes@redhat.com> - 3.19.1-1
- Update to 3.19.1

* Mon Oct 12 2015 Kalev Lember <klember@redhat.com> - 3.18.1-1
- Update to 3.18.1

* Mon Sep 21 2015 Kalev Lember <klember@redhat.com> - 3.18.0-1
- Update to 3.18.0

* Fri Sep 11 2015 Kalev Lember <klember@redhat.com> - 3.17.92-1
- Update to 3.17.92
- Use make_install macro

* Tue Jul 28 2015 Kalev Lember <klember@redhat.com> - 3.17.1-1
- Update to 3.17.1

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.16.2.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Tue Apr 28 2015 Kalev Lember <kalevlember@gmail.com> - 3.16.2.1-1
- Update to 3.16.2.1
- Include new symbolic icon

* Mon Apr 27 2015 Kalev Lember <kalevlember@gmail.com> - 3.16.2-1
- Update to 3.16.2

* Tue Apr 14 2015 Kalev Lember <kalevlember@gmail.com> - 3.16.1-1
- Update to 3.16.1

* Mon Mar 23 2015 Kalev Lember <kalevlember@gmail.com> - 3.16.0-1
- Update to 3.16.0

* Tue Mar 17 2015 Kalev Lember <kalevlember@gmail.com> - 3.15.92-1
- Update to 3.15.92
- Ship the COPYING file

* Tue Mar 03 2015 Kalev Lember <kalevlember@gmail.com> - 3.15.91-1
- Update to 3.15.91

* Mon Feb 16 2015 Richard Hughes <rhughes@redhat.com> - 3.15.90-1
- Update to 3.15.90

* Tue Jan 20 2015 Richard Hughes <rhughes@redhat.com> - 3.15.1-1
- Update to 3.15.1

* Mon Oct 13 2014 Kalev Lember <kalevlember@gmail.com> - 3.14.1-1
- Update to 3.14.1

* Mon Sep 22 2014 Kalev Lember <kalevlember@gmail.com> - 3.14.0-1
- Update to 3.14.0
- Build as noarch (#1139049)

* Tue Sep 16 2014 Kalev Lember <kalevlember@gmail.com> - 3.13.92-1
- Update to 3.13.92

* Fri Sep  5 2014 Vadim Rutkovsky <vrutkovs@redhat.com> - 3.13.91-2
- Build installed tests

* Mon Sep 01 2014 Kalev Lember <kalevlember@gmail.com> - 3.13.91-1
- Update to 3.13.91
- Include HighContrast icons
- Add missing requires now that it's a pure gjs app

* Tue Aug 19 2014 Kalev Lember <kalevlember@gmail.com> - 3.13.90-1
- Update to 3.13.90

* Sat Aug 16 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.13.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Tue Jul 22 2014 Kalev Lember <kalevlember@gmail.com> - 3.13.4-1
- Update to 3.13.4

* Tue Jun 24 2014 Richard Hughes <rhughes@redhat.com> - 3.13.3-1
- Update to 3.13.3

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.13.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Wed May 28 2014 Kalev Lember <kalevlember@gmail.com> - 3.13.2-1
- Update to 3.13.2

* Thu May 01 2014 Kalev Lember <kalevlember@gmail.com> - 3.13.1-1
- Update to 3.13.1
- Adjust rpm provides filtering for renamed private libs directory

* Tue Mar 25 2014 Richard Hughes <rhughes@redhat.com> - 3.12.0-1
- Update to 3.12.0

* Tue Mar 18 2014 Richard Hughes <rhughes@redhat.com> - 3.11.92-1
- Update to 3.11.92

* Tue Mar 04 2014 Richard Hughes <rhughes@redhat.com> - 3.11.91-1
- Update to 3.11.91

* Tue Feb 18 2014 Richard Hughes <rhughes@redhat.com> - 3.11.90-1
- Update to 3.11.90

* Mon Feb 03 2014 Richard Hughes <rhughes@redhat.com> - 3.11.5-1
- Update to 3.11.5

* Tue Jan 14 2014 Richard Hughes <rhughes@redhat.com> - 3.11.4-1
- Update to 3.11.4

* Wed Jan 08 2014 Richard Hughes <rhughes@redhat.com> - 3.11.3-1
- Update to 3.11.3

* Tue Oct 29 2013 Richard Hughes <rhughes@redhat.com> - 3.10.1-1
- Update to 3.10.1

* Wed Sep 25 2013 Kalev Lember <kalevlember@gmail.com> - 3.10.0-1
- Update to 3.10.0

* Wed Sep 18 2013 Kalev Lember <kalevlember@gmail.com> - 3.9.92-1
- Update to 3.9.92

* Tue Sep 03 2013 Kalev Lember <kalevlember@gmail.com> - 3.9.91-1
- Update to 3.9.91

* Thu Aug 22 2013 Kalev Lember <kalevlember@gmail.com> - 3.9.90-1
- Update to 3.9.90

* Sat Aug 10 2013 Kalev Lember <kalevlember@gmail.com> - 3.9.5-1
- Update to 3.9.5

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.9.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Fri Jun 21 2013 Kalev Lember <kalevlember@gmail.com> - 3.9.3-1
- Update to 3.9.3
- Include new icons and add icon cache scriptlets

* Sun Jun 02 2013 Kalev Lember <kalevlember@gmail.com> - 3.9.2-1
- Update to 3.9.2

* Tue May 14 2013 Richard Hughes <rhughes@redhat.com> - 3.8.2-1
- Update to 3.8.2

* Wed Apr 17 2013 Kalev Lember <kalevlember@gmail.com> - 3.8.1-1
- Update to 3.8.1

* Thu Mar 28 2013 Cosimo Cecchi <cosimoc@gnome.org> - 3.8.0-1
- Update to 3.8.0

* Tue Mar 19 2013 Cosimo Cecchi <cosimoc@gnome.org> - 3.7.92-1
- Initial packaging

