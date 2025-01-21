%global tarball_version %%(echo %{version} | tr '~' '.')

Name:           swell-foop
Version:        46.0
Release:        3%{?dist}
Summary:        GNOME colored tiles puzzle game

License:        GPL-2.0-or-later AND CC-BY-SA-4.0
URL:            https://wiki.gnome.org/Apps/Swell%20Foop
Source0:        https://download.gnome.org/sources/%{name}/46/%{name}-%{tarball_version}.tar.xz

BuildRequires:  pkgconfig(gee-0.8)
BuildRequires:  pkgconfig(gtk4)
BuildRequires:  pkgconfig(libgnome-games-support-2)
BuildRequires:  pkgconfig(librsvg-2.0)

BuildRequires:  desktop-file-utils
BuildRequires:  gettext-devel
BuildRequires:  itstool
BuildRequires:  meson
BuildRequires:  vala
BuildRequires:  yelp-tools


%description
Clear the screen by removing groups of colored and shaped tiles

%prep
%autosetup -p1 -n %{name}-%{tarball_version}

%build
%meson
%meson_build


%install
%meson_install

%find_lang %{name} --with-gnome


%check
desktop-file-validate $RPM_BUILD_ROOT%{_datadir}/applications/org.gnome.SwellFoop.desktop


%files -f %{name}.lang
%license COPYING
%doc NEWS
%{_bindir}/swell-foop
%{_datadir}/applications/org.gnome.SwellFoop.desktop
%{_datadir}/dbus-1/services/org.gnome.SwellFoop.service
%{_datadir}/glib-2.0/schemas/org.gnome.SwellFoop.gschema.xml
%{_datadir}/icons/hicolor/*/apps/org.gnome.SwellFoop*
%{_datadir}/metainfo/org.gnome.SwellFoop.appdata.xml


%changelog
* Sun Jan 19 2025 Fedora Release Engineering <releng@fedoraproject.org> - 46.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Sat Jul 20 2024 Fedora Release Engineering <releng@fedoraproject.org> - 46.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Sat Mar 16 2024 David King <amigadave@amigadave.com> - 46.0-1
- Update to 46.0

* Mon Mar 11 2024 David King <amigadave@amigadave.com> - 46~rc-1
- Update to 46.rc

* Sat Jan 27 2024 Fedora Release Engineering <releng@fedoraproject.org> - 46~alpha-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Mon Jan 22 2024 David King <amigadave@amigadave.com> - 46~alpha-1
- Update to 46.alpha

* Sat Jul 22 2023 Fedora Release Engineering <releng@fedoraproject.org> - 41.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Sat Jan 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 41.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 41.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Tue Apr 12 2022 David King <amigadave@amigadave.com> - 41.1-1
- Update to 41.1

* Sat Jan 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 41.0.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Mon Sep 20 2021 Kalev Lember <klember@redhat.com> - 41.0.1-1
- Update to 41.0.1

* Sat Sep 18 2021 Kalev Lember <klember@redhat.com> - 41.0-1
- Update to 41.0

* Thu Aug 19 2021 Kalev Lember <klember@redhat.com> - 41~alpha-1
- Update to 41.alpha

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 40.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed May 05 2021 Kalev Lember <klember@redhat.com> - 40.1-1
- Update to 40.1

* Mon Mar 22 2021 Kalev Lember <klember@redhat.com> - 40.0-1
- Update to 40.0

* Mon Mar 15 2021 Kalev Lember <klember@redhat.com> - 40~rc-1
- Update to 40.rc

* Thu Feb 18 2021 Kalev Lember <klember@redhat.com> - 40~beta-1
- Update to 40.beta

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 3.34.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.34.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Jan 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.34.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Tue Oct 15 2019 Yanko Kaneti <yaneti@declera.com> - 3.34.1-1
- Update to 3.34.1

* Mon Sep 09 2019 Kalev Lember <klember@redhat.com> - 3.34.0-1
- Update to 3.34.0

* Tue Sep 03 2019 Kalev Lember <klember@redhat.com> - 3.33.92-1
- Update to 3.33.92

* Sat Jul 27 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.32.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Mon Mar 11 2019 Kalev Lember <klember@redhat.com> - 3.32.0-1
- Update to 3.32.0

* Tue Mar 05 2019 Kalev Lember <klember@redhat.com> - 3.31.92-1
- Update to 3.31.92

* Mon Feb 18 2019 Kalev Lember <klember@redhat.com> - 3.31.91-1
- Update to 3.31.91

* Wed Feb  6 2019 Yanko Kaneti <yaneti@declera.com> - 3.31.90-1
- Update to 3.31.90
- New application id org.gnome.SwellFoop

* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.30.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Mon Sep  3 2018 Yanko Kaneti <yaneti@declera.com> - 3.30.0-1
- Update to 3.30.0

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.29.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Yanko Kaneti <yaneti@declera.com> - 3.29.3-1
- Update to 3.29.3

* Mon Mar 12 2018 Kalev Lember <klember@redhat.com> - 3.28.0-1
- Update to 3.28.0

* Mon Feb 26 2018 Yanko Kaneti <yaneti@declera.com> - 3.27.92-1
- Update to 3.27.92

* Wed Feb 21 2018 Yanko Kaneti <yaneti@declera.com> - 3.27.91-1
- Update to 3.27.91. Drop old workaround

* Wed Feb  7 2018 Yanko Kaneti <yaneti@declera.com> - 3.27.90.1-1
- Update to 3.27.90.1
- Drop patch - fixed upstream
- Add a temporary workaround to install help with meson

* Mon Feb  5 2018 Yanko Kaneti <yaneti@declera.com> - 3.27.90-1
- Update to 3.27.90. Switch to meson

* Sat Jan 06 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 3.27.2-2
- Remove obsolete scriptlets

* Tue Nov 14 2017 Yanko Kaneti <yaneti@declera.com> - 3.27.2-1
- Update to 3.27.2

* Mon Sep 11 2017 Yanko Kaneti <yaneti@declera.com> - 3.26.0-1
- Update to 3.26.0

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.25.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.25.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Tue May 23 2017 Yanko Kaneti <yaneti@declera.com> - 3.25.2-1
- Update to 3.25.2

* Tue Mar 21 2017 Yanko Kaneti <yaneti@declera.com> - 3.24.0-1
- Update to 3.24.0

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.23.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Tue Nov 22 2016 Yanko Kaneti <yaneti@declera.com> - 3.23.2-1
- Update to 3.23.2

* Tue Nov  8 2016 Yanko Kaneti <yaneti@declera.com> - 3.22.2-1
- Update to 3.22.2

* Mon Sep 19 2016 Kalev Lember <klember@redhat.com> - 3.22.0-1
- Update to 3.22.0

* Tue Sep 13 2016 Yanko Kaneti <yaneti@declera.com> - 3.21.92-1
- Update to 3.21.92

* Tue Aug 30 2016 Yanko Kaneti <yaneti@declera.com> - 3.21.91-1
- Update to 3.21.91

* Thu Aug 18 2016 Kalev Lember <klember@redhat.com> - 3.21.90-1
- Update to 3.21.90
- Move desktop file validation to the check section

* Tue Mar 22 2016 Yanko Kaneti <yaneti@declera.com> - 3.20.0-1
- Update to 3.20.0

* Mon Mar 14 2016 Yanko Kaneti <yaneti@declera.com> - 3.19.91-1
- Update to 3.19.91

* Tue Feb 16 2016 Yanko Kaneti <yaneti@declera.com> - 3.19.90-1
- Update to 3.19.90

* Fri Feb 05 2016 Fedora Release Engineering <releng@fedoraproject.org> - 3.19.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Tue Jan 19 2016 Yanko Kaneti <yaneti@declera.com> - 3.19.4-1
- Update to 3.19.4

* Mon Dec 14 2015 Yanko Kaneti <yaneti@declera.com> - 3.19.3-1
- Update to 3.19.3

* Tue Nov 10 2015 Kalev Lember <klember@redhat.com> - 3.18.1-1
- Update to 3.18.1

* Mon Sep 21 2015 Kalev Lember <klember@redhat.com> - 3.18.0-1
- Update to 3.18.0

* Mon Sep 14 2015 Kalev Lember <klember@redhat.com> - 3.17.92-1
- Update to 3.17.92

* Mon Aug 31 2015 Kalev Lember <klember@redhat.com> - 3.17.91-1
- Update to 3.17.91
- Use make_install macro

* Mon Aug 17 2015 Yanko Kaneti <yaneti@declera.com> - 3.17.90-1
- Update to 3.17.90

* Wed Aug 12 2015 Yanko Kaneti <yaneti@declera.com> - 3.16.2-1
- Update to 3.16.2. Bug #1252480

* Fri Jun 19 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.16.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Tue Apr 14 2015 Yanko Kaneti <yaneti@declera.com> - 3.16.1-1
- Update to 3.16.1
- No more separate HighContrast icons

* Mon Mar 23 2015 Yanko Kaneti <yaneti@declera.com> - 3.16.0-1
- Update to 3.16.0
- Use license macro

* Mon Mar 16 2015 Yanko Kaneti <yaneti@declera.com> - 3.15.92-1
- Update to 3.15.92

* Mon Mar  2 2015 Yanko Kaneti <yaneti@declera.com> - 3.15.91-1
- Update to 3.15.91

* Mon Feb 16 2015 Yanko Kaneti <yaneti@declera.com> - 3.15.90-1
- Update to 3.15.90

* Mon Jan 19 2015 Yanko Kaneti <yaneti@declera.com> - 3.15.4-1
- Update to 3.15.4

* Mon Dec 15 2014 Yanko Kaneti <yaneti@declera.com> - 3.15.3-1
- Update to 3.15.3

* Mon Oct 27 2014 Yanko Kaneti <yaneti@declera.com> - 3.15.1-1
- First devlopment release from the 3.16 cycle

* Mon Sep 22 2014 Yanko Kaneti <yaneti@declera.com> - 3.14.0-1
- Update to 3.14.0

* Tue Sep 16 2014 Yanko Kaneti <yaneti@declera.com> - 3.13.92-1
- Update to 3.13.92

* Tue Aug 19 2014 Yanko Kaneti <yaneti@declera.com> - 3.13.90-1
- Update to 3.13.90
- Theme snippets rework

* Mon Aug 18 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.13.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.13.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Mon Apr 28 2014 Yanko Kaneti <yaneti@declera.com> - 3.13.1-1
- First release from the new development cycle.

* Tue Apr 15 2014 Yanko Kaneti <yaneti@declera.com> - 3.12.1-1
- Update to 3.12.1. Drop upstreamed patch.

* Thu Mar 27 2014 Adam Williamson <awilliam@redhat.com> - 3.12.0-2
- backport upstream patch for touch input

* Mon Mar 24 2014 Richard Hughes <rhughes@redhat.com> - 3.12.0-1
- Update to 3.12.0

* Tue Mar 18 2014 Yanko Kaneti <yaneti@declera.com> - 3.11.92-1
- Update to 3.11.92

* Thu Feb 20 2014 Kalev Lember <kalevlember@gmail.com> - 3.11.90-2
- Rebuilt for cogl soname bump

* Tue Feb 18 2014 Yanko Kaneti <yaneti@declera.com> - 3.11.90-1
- Update to 3.11.90

* Mon Feb 10 2014 Peter Hutterer <peter.hutterer@redhat.com> - 3.11.3-3
- Rebuild for libevdev soname bump

* Wed Feb 05 2014 Kalev Lember <kalevlember@gmail.com> - 3.11.3-2
- Rebuilt for cogl soname bump

* Tue Dec 17 2013 Yanko Kaneti <yaneti@declera.com> - 3.11.3-1
- Update to 3.11.3. New url.

* Tue Oct 29 2013 Yanko Kaneti <yaneti@declera.com> - 3.11.1-1
- First 3.11 development release

* Sat Oct 12 2013 Yanko Kaneti <yaneti@declera.com> - 3.10.1-1
- Update to 3.10.1

* Mon Sep 23 2013 Yanko Kaneti <yaneti@declera.com> - 3.10.0-1
- Update to 3.10.0

* Tue Sep 17 2013 Yanko Kaneti <yaneti@declera.com> - 3.9.92-1
- Update to 3.9.92
- Add appdata
- Add HighContrast icons

* Tue Aug 20 2013 Yanko Kaneti <yaneti@declera.com> - 3.8.2-1
- Update to 3.8.2
- Drop patch merged upstream and do not autoreconf for it

* Fri Aug 09 2013 Kalev Lember <kalevlember@gmail.com> - 3.8.1-6
- Rebuilt for cogl 1.15.4 soname bump

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.8.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Sat Jun 22 2013 Kalev Lember <kalevlember@gmail.com> - 3.8.1-4
- Obsolete gnome-games-help as well

* Thu Jun 20 2013 Matthias Clasen <mclasen@redhat.com> - 3.8.1-3
- Obsolete gnome-games (for upgrades from f17)

* Fri Jun 14 2013 Matthias Clasen <mclasen@redhat.com> - 3.8.1-2
- Fix preferences

* Mon Apr 15 2013 Kalev Lember <kalevlember@gmail.com> - 3.8.1-1
- Update to 3.8.1

* Wed Mar 27 2013 Yanko Kaneti <yaneti@declera.com> - 3.8.0-1
- Update to 3.8.0

* Tue Mar 19 2013 Yanko Kaneti <yaneti@declera.com> - 3.7.92-1
- Update to 3.7.92

* Tue Feb 19 2013 Yanko Kaneti <yaneti@declera.com> - 3.7.90-1
- New upstream release 3.7.90
- Fix desktop file

* Fri Feb 15 2013 Yanko Kaneti <yaneti@declera.com> - 3.7.4-1
- Initial packaging of standalone swell-foop
