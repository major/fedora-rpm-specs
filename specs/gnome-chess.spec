%global tarball_version %%(echo %{version} | tr '~' '.')

%global libadwaita_version 1.5

Name:           gnome-chess
Version:        47.0
Release:        2%{?dist}
Summary:        GNOME Chess game

License:        GPL-3.0-or-later AND CC-BY-SA-3.0 AND CC0-1.0
URL:            https://wiki.gnome.org/Apps/Chess
Source0:        https://download.gnome.org/sources/%{name}/47/%{name}-%{tarball_version}.tar.xz

BuildRequires:  desktop-file-utils
BuildRequires:  gettext
BuildRequires:  itstool
BuildRequires:  meson
BuildRequires:  vala
BuildRequires:  pkgconfig(gtk4)
BuildRequires:  pkgconfig(libadwaita-1) >= %{libadwaita_version}
BuildRequires:  pkgconfig(librsvg-2.0)

Requires: gnuchess
Requires: libadwaita%{?_isa} >= %{libadwaita_version}

%description
A chess game that supports several chess engines.

%prep
%autosetup -p1 -n %{name}-%{tarball_version}


%build
%meson
%meson_build


%install
%meson_install

%find_lang %{name} --with-gnome


%check
desktop-file-validate $RPM_BUILD_ROOT%{_datadir}/applications/*.desktop


%files -f %{name}.lang
%license COPYING
%doc NEWS README.md
%config(noreplace) %{_sysconfdir}/gnome-chess/engines.conf
%{_bindir}/gnome-chess
%{_datadir}/applications/*.desktop
%{_datadir}/dbus-1/services/org.gnome.Chess.service
%{_datadir}/glib-2.0/schemas/org.gnome.Chess.gschema.xml
%{_datadir}/icons/hicolor/*/apps/org.gnome.Chess.svg
%{_datadir}/icons/hicolor/symbolic/apps/org.gnome.Chess-symbolic.svg
%{_metainfodir}/org.gnome.Chess.appdata.xml
%{_mandir}/man6/gnome-chess.6*


%changelog
* Thu Jan 16 2025 Fedora Release Engineering <releng@fedoraproject.org> - 47.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Mon Sep 16 2024 nmontero <nmontero@redhat.com> - 47.0-1
- Update to 47.0

* Mon Aug 05 2024 David King <amigadave@amigadave.com> - 47~alpha-1
- Update to 47.beta

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 46.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Sat Mar 16 2024 David King <amigadave@amigadave.com> - 46.0-1
- Update to 46.0

* Sat Feb 17 2024 David King <amigadave@amigadave.com> - 46~beta-1
- Update to 46.beta

* Wed Jan 24 2024 Fedora Release Engineering <releng@fedoraproject.org> - 43.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 43.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 43.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Sat Mar 18 2023 David King <amigadave@amigadave.com> - 43.2-1
- Update to 43.2

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 43.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Sun Jan 08 2023 David King <amigadave@amigadave.com> - 43.1-1
- Update to 43.1

* Mon Sep 19 2022 Kalev Lember <klember@redhat.com> - 43.0-1
- Update to 43.0

* Tue Sep 06 2022 Kalev Lember <klember@redhat.com> - 43~rc-1
- Update to 43.rc

* Wed Aug 10 2022 Kalev Lember <klember@redhat.com> - 42.1-1
- Update to 42.1

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 42.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Fri Mar 25 2022 David King <amigadave@amigadave.com> - 42.0-1
- Update to 42.0

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 42~alpha-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Sun Jan 09 2022 David King <amigadave@amigadave.com> - 42~alpha-2
- Fix isa macro in Requires

* Sun Jan 09 2022 David King <amigadave@amigadave.com> - 42~alpha-1
- Update to 42.alpha

* Mon Nov 01 2021 Kalev Lember <klember@redhat.com> - 41.1-1
- Update to 41.1

* Thu Sep 16 2021 Kalev Lember <klember@redhat.com> - 41.0-1
- Update to 41.0

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 40.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed May 05 2021 Kalev Lember <klember@redhat.com> - 40.1-1
- Update to 40.1

* Mon Mar 22 2021 Kalev Lember <klember@redhat.com> - 40.0-1
- Update to 40.0

* Fri Feb 19 2021 Kalev Lember <klember@redhat.com> - 40~alpha-1
- Update to 40.alpha

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 3.38.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Fri Dec 11 2020 Kalev Lember <klember@redhat.com> - 3.38.1-1
- Update to 3.38.1

* Sat Sep 12 2020 Kalev Lember <klember@redhat.com> - 3.38.0-1
- Update to 3.38.0

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.37.3-3
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.37.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Jul 20 2020 Kalev Lember <klember@redhat.com> - 3.37.3-1
- Update to 3.37.3

* Fri May 29 2020 Kalev Lember <klember@redhat.com> - 3.37.2-1
- Update to 3.37.2
- Drop old obsoletes

* Thu Apr 30 2020 Kalev Lember <klember@redhat.com> - 3.37.1.1-1
- Update to 3.37.1.1

* Thu Mar 05 2020 Kalev Lember <klember@redhat.com> - 3.36.0-1
- Update to 3.36.0

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.35.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Tue Jan 07 2020 Kalev Lember <klember@redhat.com> - 3.35.3-1
- Update to 3.35.3

* Sun Sep 08 2019 Kalev Lember <klember@redhat.com> - 3.34.0-1
- Update to 3.34.0

* Wed Jul 31 2019 Michael Catanzaro <mcatanzaro@gnome.org> - 3.33.90-1
- Update to 3.33.90

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.32.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Mon Mar 11 2019 Kalev Lember <klember@redhat.com> - 3.32.0-1
- Update to 3.32.0

* Mon Mar 04 2019 Kalev Lember <klember@redhat.com> - 3.31.92-1
- Update to 3.31.92

* Tue Feb 05 2019 Kalev Lember <klember@redhat.com> - 3.31.90-1
- Update to 3.31.90

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.31.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Wed Jan 23 2019 Kalev Lember <klember@redhat.com> - 3.31.3-1
- Update to 3.31.3

* Thu Sep 06 2018 Kalev Lember <klember@redhat.com> - 3.30.0-1
- Update to 3.30.0

* Mon Aug 13 2018 Kalev Lember <klember@redhat.com> - 3.29.90-1
- Update to 3.29.90

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.28.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Apr 10 2018 Kalev Lember <klember@redhat.com> - 3.28.1-1
- Update to 3.28.1

* Sun Mar 11 2018 Kalev Lember <klember@redhat.com> - 3.28.0-1
- Update to 3.28.0
- Switch to the meson build system

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.26.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Fri Jan 05 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 3.26.0-2
- Remove obsolete scriptlets

* Sun Sep 10 2017 Kalev Lember <klember@redhat.com> - 3.26.0-1
- Update to 3.26.0

* Mon Jul 31 2017 Kalev Lember <klember@redhat.com> - 3.25.4-1
- Update to 3.25.4

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.24.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Wed Apr 12 2017 Kalev Lember <klember@redhat.com> - 3.24.1-1
- Update to 3.24.1

* Wed Mar 22 2017 Kalev Lember <klember@redhat.com> - 3.24.0-1
- Update to 3.24.0

* Thu Mar 16 2017 Kalev Lember <klember@redhat.com> - 3.23.92.5-1
- Update to 3.23.92.5

* Wed Mar 15 2017 Michael Catanzaro <mcatanzaro@gnome.org> - 3.23.92-2
- Reenable hardened build since bgo#758816 is fixed upstream

* Sat Mar 11 2017 Richard Hughes <rhughes@redhat.com> - 3.23.92-1
- Update to 3.23.92

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.22.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Nov 23 2016 Kalev Lember <klember@redhat.com> - 3.22.2-1
- Update to 3.22.2

* Thu Sep 22 2016 Kalev Lember <klember@redhat.com> - 3.22.0-1
- Update to 3.22.0

* Thu Aug 18 2016 Kalev Lember <klember@redhat.com> - 3.21.90-1
- Update to 3.21.90
- Move desktop file validation to the check section

* Wed Jun 22 2016 Richard Hughes <rhughes@redhat.com> - 3.21.3-1
- Update to 3.21.3

* Sun May 08 2016 Kalev Lember <klember@redhat.com> - 3.20.1-1
- Update to 3.20.1

* Sun Mar 20 2016 Kalev Lember <klember@redhat.com> - 3.20.0-1
- Update to 3.20.0

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 3.19.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Tue Jan 26 2016 Michael Catanzaro <mcatanzaro@gnome.org> - 3.19.4-2
- Disable hardening for bug #1280470

* Wed Jan 20 2016 Kalev Lember <klember@redhat.com> - 3.19.4-1
- Update to 3.19.4

* Wed Dec 16 2015 Kalev Lember <klember@redhat.com> - 3.19.3-1
- Update to 3.19.3

* Sat Nov 21 2015 Kalev Lember <klember@redhat.com> - 3.19.2-1
- Update to 3.19.2

* Wed Oct 28 2015 Kalev Lember <klember@redhat.com> - 3.19.1-1
- Update to 3.19.1

* Mon Sep 21 2015 Kalev Lember <klember@redhat.com> - 3.18.0-1
- Update to 3.18.0

* Sun Sep 13 2015 Kalev Lember <klember@redhat.com> - 3.17.92-1
- Update to 3.17.92

* Mon Aug 17 2015 Kalev Lember <klember@redhat.com> - 3.17.90-1
- Update to 3.17.90
- Use make_install macro

* Tue Jul 28 2015 Kalev Lember <klember@redhat.com> - 3.17.4-1
- Update to 3.17.4

* Tue Jun 30 2015 Kalev Lember <klember@redhat.com> - 3.17.3-1
- Update to 3.17.3

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.17.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sun May 31 2015 Kalev Lember <kalevlember@gmail.com> - 3.17.2-1
- Update to 3.17.2
- Include new symbolic icon

* Fri May 01 2015 Kalev Lember <kalevlember@gmail.com> - 3.17.1-1
- Update to 3.17.1

* Tue Apr 14 2015 Kalev Lember <kalevlember@gmail.com> - 3.16.1-1
- Update to 3.16.1

* Fri Mar 20 2015 Kalev Lember <kalevlember@gmail.com> - 3.16.0-1
- Update to 3.16.0

* Sat Mar 14 2015 Kalev Lember <kalevlember@gmail.com> - 3.15.92-1
- Update to 3.15.92
- Use %%license macro for the COPYING file

* Mon Mar 02 2015 Kalev Lember <kalevlember@gmail.com> - 3.15.91-1
- Update to 3.15.91

* Tue Feb 17 2015 Richard Hughes <rhughes@redhat.com> - 3.15.90-1
- Update to 3.15.90

* Tue Jan 20 2015 Richard Hughes <rhughes@redhat.com> - 3.15.4-1
- Update to 3.15.4

* Wed Dec 17 2014 Michael Catanzaro <mcatanzaro@gnome.org> - 3.15.3-1
- Update to 3.15.3
- Update package description, URL, Source, and license

* Mon Nov 10 2014 Kalev Lember <kalevlember@gmail.com> - 3.14.1-1
- Update to 3.14.1

* Mon Sep 22 2014 Kalev Lember <kalevlember@gmail.com> - 3.14.0-1
- Update to 3.14.0

* Tue Sep 16 2014 Kalev Lember <kalevlember@gmail.com> - 3.13.92-1
- Update to 3.13.92

* Tue Aug 19 2014 Kalev Lember <kalevlember@gmail.com> - 3.13.90-1
- Update to 3.13.90

* Sat Aug 16 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.13.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Mon Jul 21 2014 Kalev Lember <kalevlember@gmail.com> - 3.13.4-2
- Drop an unneeded sqlite build dep

* Mon Jul 21 2014 Kalev Lember <kalevlember@gmail.com> - 3.13.4-1
- Update to 3.13.4

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.13.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Mon Apr 28 2014 Richard Hughes <rhughes@redhat.com> - 3.13.1-1
- Update to 3.13.1

* Tue Apr 15 2014 Kalev Lember <kalevlember@gmail.com> - 3.12.1-1
- Update to 3.12.1

* Mon Mar 24 2014 Richard Hughes <rhughes@redhat.com> - 3.12.0-1
- Update to 3.12.0

* Mon Mar 17 2014 Richard Hughes <rhughes@redhat.com> - 3.11.92-1
- Update to 3.11.92

* Mon Feb 17 2014 Richard Hughes <rhughes@redhat.com> - 3.11.90-1
- Update to 3.11.90

* Mon Jan 13 2014 Richard Hughes <rhughes@redhat.com> - 3.11.4-1
- Update to 3.11.4

* Tue Dec 17 2013 Richard Hughes <rhughes@redhat.com> - 3.11.3-1
- Update to 3.11.3

* Mon Nov 18 2013 Richard Hughes <rhughes@redhat.com> - 3.11.2-1
- Update to 3.11.2

* Mon Oct 28 2013 Richard Hughes <rhughes@redhat.com> - 3.11.1-1
- Update to 3.11.1

* Wed Sep 25 2013 Kalev Lember <kalevlember@gmail.com> - 3.10.0-1
- Update to 3.10.0

* Wed Sep 18 2013 Kalev Lember <kalevlember@gmail.com> - 3.9.92-1
- Update to 3.9.92
- Include the appdata file

* Mon Aug 19 2013 Tanner Doshier <doshitan@gmail.com> - 3.9.90-1
- Update to 3.9.90

* Tue Jul 30 2013 Tanner Doshier <doshitan@gmail.com> - 3.9.5-1
- Update to 3.9.5

* Tue Jul 09 2013 Tanner Doshier <doshitan@gmail.com> - 3.9.4-1
- Update to 3.9.4

* Sat Jun 22 2013 Kalev Lember <kalevlember@gmail.com> - 3.9.2-2
- Obsolete gnome-games-extra (for upgrades from f17)

* Sun Jun 02 2013 Kalev Lember <kalevlember@gmail.com> - 3.9.2-1
- Update to 3.9.2

* Tue May 28 2013 Matthias Clasen <mclasen@redhat.com> - 3.8.2.1-1
- Update to 3.8.2.1

* Tue Apr 30 2013 Tanner Doshier <doshitan@gmail.com> - 3.8.1-1
- Update to 3.8.1
- Add Requires for gnuchess

* Fri Mar 29 2013 Tanner Doshier <doshitan@gmail.com> - 3.8.0-1
- Update to 3.8.0

* Fri Mar 22 2013 Tanner Doshier <doshitan@gmail.com> - 3.7.92-1
- Update to 3.7.92
- Use old desktop file name

* Tue Mar 12 2013 Tanner Doshier <doshitan@gmail.com> - 3.7.90-1
- Initial packaging of standalone gnome-chess
