%global tarball_version %%(echo %{version} | tr '~' '.')

Name:           tali
Version:        40.9
Release:        7%{?dist}
Summary:        GNOME Tali game

# Automatically converted from old format: GPLv2+ and GFDL - review is highly recommended.
License:        GPL-2.0-or-later AND LicenseRef-Callaway-GFDL
URL:            https://wiki.gnome.org/Apps/Tali
Source0:        https://download.gnome.org/sources/tali/40/tali-%{tarball_version}.tar.xz

BuildRequires:  desktop-file-utils
BuildRequires:  gcc
BuildRequires:  gettext
BuildRequires:  itstool
BuildRequires:  meson
BuildRequires:  pkgconfig(gtk+-3.0)
BuildRequires:  pkgconfig(libgnome-games-support-1)

%description
Sort of poker with dice and less money. An ancient Roman game.

%prep
%autosetup -p1 -n tali-%{tarball_version}


%build
%meson
%meson_build


%install
%meson_install

%find_lang %{name} --all-name --with-gnome


%check
desktop-file-validate $RPM_BUILD_ROOT%{_datadir}/applications/*.desktop

%files -f %{name}.lang
%doc NEWS
%license COPYING
%{_bindir}/tali
%{_datadir}/applications/org.gnome.Tali.desktop
%{_datadir}/glib-2.0/schemas/org.gnome.Tali.gschema.xml
%{_datadir}/icons/hicolor/*/apps/org.gnome.Tali.*
%{_datadir}/icons/hicolor/symbolic/apps/org.gnome.Tali-symbolic.svg
%{_datadir}/metainfo/org.gnome.Tali.appdata.xml
%{_datadir}/tali/
%{_mandir}/man6/tali.6*


%changelog
* Sun Jan 19 2025 Fedora Release Engineering <releng@fedoraproject.org> - 40.9-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Wed Sep 04 2024 Miroslav Suchý <msuchy@redhat.com> - 40.9-6
- convert license to SPDX

* Sat Jul 20 2024 Fedora Release Engineering <releng@fedoraproject.org> - 40.9-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Sat Jan 27 2024 Fedora Release Engineering <releng@fedoraproject.org> - 40.9-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sat Jul 22 2023 Fedora Release Engineering <releng@fedoraproject.org> - 40.9-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Sat Jan 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 40.9-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Sun Jan 08 2023 David King <amigadave@amigadave.com> - 40.9-1
- Update to 40.9

* Mon Aug 08 2022 Kalev Lember <klember@redhat.com> - 40.8-1
- Update to 40.8

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 40.7-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon Apr 25 2022 David King <amigadave@amigadave.com> - 40.7-1
- Update to 40.7

* Sun Mar 20 2022 David King <amigadave@amigadave.com> - 40.6-1
- Update to 40.6

* Tue Feb 01 2022 David King <amigadave@amigadave.com> - 40.5-1
- Update to 40.5

* Sat Jan 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 40.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Mon Nov 01 2021 Kalev Lember <klember@redhat.com> - 40.4-1
- Update to 40.4

* Sat Sep 18 2021 Kalev Lember <klember@redhat.com> - 40.3-1
- Update to 40.3

* Sun Aug 15 2021 Kalev Lember <klember@redhat.com> - 40.2-1
- Update to 40.2

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 40.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed May 26 2021 Kalev Lember <klember@redhat.com> - 40.1-1
- Update to 40.1

* Mon Mar 22 2021 Kalev Lember <klember@redhat.com> - 40.0-1
- Update to 40.0

* Tue Mar 16 2021 Kalev Lember <klember@redhat.com> - 40~rc-1
- Update to 40.rc
- Remove old obsoletes

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 3.38.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Sat Jan 16 2021 Kalev Lember <klember@redhat.com> - 3.38.3-1
- Update to 3.38.3

* Wed Nov 25 2020 Kalev Lember <klember@redhat.com> - 3.38.2-1
- Update to 3.38.2

* Mon Sep 14 2020 Kalev Lember <klember@redhat.com> - 3.38.0-1
- Update to 3.38.0

* Sun Sep 06 2020 Kalev Lember <klember@redhat.com> - 3.37.92-1
- Update to 3.37.92

* Sun Aug 23 2020 Kalev Lember <klember@redhat.com> - 3.37.91-1
- Update to 3.37.91

* Mon Aug 17 2020 Kalev Lember <klember@redhat.com> - 3.37.90-1
- Update to 3.37.90

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.37.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Jul 20 2020 Kalev Lember <klember@redhat.com> - 3.37.3-1
- Update to 3.37.3

* Wed May 06 2020 Kalev Lember <klember@redhat.com> - 3.37.1-1
- Update to 3.37.1

* Sun Mar 29 2020 Kalev Lember <klember@redhat.com> - 3.36.1-1
- Update to 3.36.1

* Sat Mar 07 2020 Kalev Lember <klember@redhat.com> - 3.36.0-1
- Update to 3.36.0

* Mon Feb 17 2020 Kalev Lember <klember@redhat.com> - 3.35.91-1
- Update to 3.35.91

* Sun Feb 02 2020 Kalev Lember <klember@redhat.com> - 3.35.90-1
- Update to 3.35.90

* Fri Jan 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.35.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jan 10 2020 Kalev Lember <klember@redhat.com> - 3.35.3-1
- Update to 3.35.3

* Wed Aug 14 2019 Kalev Lember <klember@redhat.com> - 3.32.1-1
- Update to 3.32.1

* Sat Jul 27 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.32.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Mon Mar 11 2019 Kalev Lember <klember@redhat.com> - 3.32.0-1
- Update to 3.32.0

* Mon Feb 04 2019 Kalev Lember <klember@redhat.com> - 3.31.90-1
- Update to 3.31.90

* Thu Jan 31 2019 Kalev Lember <klember@redhat.com> - 3.31.3-1
- Update to 3.31.3
- Switch to the meson build system

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.22.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.22.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jan 18 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 3.22.0-5
- Remove obsolete scriptlets

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.22.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.22.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.22.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Sep 22 2016 Kalev Lember <klember@redhat.com> - 3.22.0-1
- Update to 3.22.0

* Thu Aug 18 2016 Kalev Lember <klember@redhat.com> - 3.21.90-1
- Update to 3.21.90
- Update source URLs
- Move desktop-file-validate to the check section

* Wed Jul 20 2016 Richard Hughes <rhughes@redhat.com> - 3.21.4-1
- Update to 3.21.4

* Tue Mar 22 2016 Kalev Lember <klember@redhat.com> - 3.20.0-1
- Update to 3.20.0

* Tue Mar 15 2016 Kalev Lember <klember@redhat.com> - 3.19.92-1
- Update to 3.19.92

* Tue Feb 16 2016 Richard Hughes <rhughes@redhat.com> - 3.19.90-1
- Update to 3.19.90

* Fri Feb 05 2016 Fedora Release Engineering <releng@fedoraproject.org> - 3.18.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Mon Sep 21 2015 Kalev Lember <klember@redhat.com> - 3.18.0-1
- Update to 3.18.0

* Mon Sep 14 2015 Kalev Lember <klember@redhat.com> - 3.17.92-1
- Update to 3.17.92

* Mon Aug 31 2015 Kalev Lember <klember@redhat.com> - 3.17.91-1
- Update to 3.17.91
- Use make_install macro

* Fri Jun 19 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.16.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Wed May 13 2015 Kalev Lember <kalevlember@gmail.com> - 3.16.1-1
- Update to 3.16.1
- Include new symbolic app icon

* Mon Mar 23 2015 Kalev Lember <kalevlember@gmail.com> - 3.16.0-1
- Update to 3.16.0

* Tue Mar 17 2015 Kalev Lember <kalevlember@gmail.com> - 3.15.92-1
- Update to 3.15.92
- Use license macro for the COPYING file

* Tue Feb 17 2015 Richard Hughes <rhughes@redhat.com> - 3.15.90-1
- Update to 3.15.90

* Tue Nov 25 2014 Kalev Lember <kalevlember@gmail.com> - 3.15.2-1
- Update to 3.15.2

* Mon Sep 22 2014 Kalev Lember <kalevlember@gmail.com> - 3.14.0-1
- Update to 3.14.0

* Tue Sep 16 2014 Kalev Lember <kalevlember@gmail.com> - 3.13.92-1
- Update to 3.13.92

* Mon Sep 01 2014 Kalev Lember <kalevlember@gmail.com> - 3.13.91-1
- Update to 3.13.91

* Tue Aug 19 2014 Kalev Lember <kalevlember@gmail.com> - 3.13.90-1
- Update to 3.13.90

* Mon Aug 18 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.13.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Mon Jul 21 2014 Kalev Lember <kalevlember@gmail.com> - 3.13.4-1
- Update to 3.13.4

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.13.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Tue Apr 29 2014 Richard Hughes <rhughes@redhat.com> - 3.13.1-1
- Update to 3.13.1

* Wed Apr 16 2014 Kalev Lember <kalevlember@gmail.com> - 3.12.1-1
- Update to 3.12.1

* Sun Mar 23 2014 Kalev Lember <kalevlember@gmail.com> - 3.12.0-1
- Update to 3.12.0

* Wed Mar 19 2014 Kalev Lember <kalevlember@gmail.com> - 3.11.92-2
- Don't install as setgid games

* Tue Mar 18 2014 Richard Hughes <rhughes@redhat.com> - 3.11.92-1
- Update to 3.11.92

* Tue Mar 04 2014 Richard Hughes <rhughes@redhat.com> - 3.11.91-1
- Update to 3.11.91

* Mon Feb 17 2014 Richard Hughes <rhughes@redhat.com> - 3.11.90-1
- Update to 3.11.90

* Mon Feb 03 2014 Richard Hughes <rhughes@redhat.com> - 3.11.5-1
- Update to 3.11.5

* Mon Jan 13 2014 Richard Hughes <rhughes@redhat.com> - 3.11.4-1
- Update to 3.11.4

* Tue Dec 17 2013 Richard Hughes <rhughes@redhat.com> - 3.11.3-1
- Update to 3.11.3

* Mon Nov 18 2013 Richard Hughes <rhughes@redhat.com> - 3.11.2-1
- Update to 3.11.2

* Tue Oct 29 2013 Richard Hughes <rhughes@redhat.com> - 3.11.1-1
- Update to 3.11.1

* Wed Sep 25 2013 Kalev Lember <kalevlember@gmail.com> - 3.10.0-1
- Update to 3.10.0

* Wed Sep 18 2013 Kalev Lember <kalevlember@gmail.com> - 3.9.92-1
- Update to 3.9.92
- Include the appdata file
- Package up the HighContrast icons and add cache scriptlets

* Thu Aug 22 2013 Kalev Lember <kalevlember@gmail.com> - 3.9.90-1
- Update to 3.9.90

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.8.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Sat Jun 22 2013 Kalev Lember <kalevlember@gmail.com> - 3.8.0-2
- Obsolete gnome-games-extra (for upgrades from f17)

* Fri Mar 29 2013 Tanner Doshier <doshitan@gmail.com> - 3.8.0-1
- Update to 3.8.0
- Use setgid games

* Fri Mar 22 2013 Tanner Doshier <doshitan@gmail.com> - 3.7.92-1
- Update to 3.7.92
- Use old desktop file name

* Tue Mar 12 2013 Tanner Doshier <doshitan@gmail.com> - 3.7.4-1
- Initial packaging of standalone tali
