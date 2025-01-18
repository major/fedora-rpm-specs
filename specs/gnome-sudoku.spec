%global tarball_version %%(echo %{version} | tr '~' '.')

Name:           gnome-sudoku
Epoch:          1
Version:        47.1.1
Release:        2%{?dist}
Summary:        GNOME Sudoku game

License:        GPL-3.0-or-later AND CC-BY-SA-3.0 AND CC0-1.0
URL:            https://wiki.gnome.org/Apps/Sudoku
Source0:        https://download.gnome.org/sources/%{name}/47/%{name}-%{tarball_version}.tar.xz

BuildRequires:  pkgconfig(gee-0.8)
BuildRequires:  pkgconfig(gio-2.0)
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(gtk4)
BuildRequires:  pkgconfig(json-glib-1.0)
BuildRequires:  pkgconfig(libadwaita-1)
BuildRequires:  pkgconfig(qqwing)

BuildRequires:  gcc gcc-c++
BuildRequires:  desktop-file-utils
BuildRequires:  gettext-devel
BuildRequires:  itstool
BuildRequires:  meson
BuildRequires:  vala

%description
GNOME version of the popular Sudoku Japanese logic game.


%prep
%autosetup -p1 -n %{name}-%{tarball_version}

%build
%meson
%meson_build


%install
%meson_install

%find_lang %{name} --with-gnome


%check
desktop-file-validate $RPM_BUILD_ROOT%{_datadir}/applications/org.gnome.Sudoku.desktop


%files -f %{name}.lang
%doc NEWS README.md
%license COPYING
%{_bindir}/gnome-sudoku
%{_datadir}/applications/org.gnome.Sudoku.desktop
%{_datadir}/dbus-1/services/org.gnome.Sudoku.service
%{_datadir}/glib-2.0/schemas/org.gnome.Sudoku.gschema.xml
%{_datadir}/icons/hicolor/*/apps/org.gnome.Sudoku*
%{_metainfodir}/org.gnome.Sudoku.metainfo.xml
%{_mandir}/man6/gnome-sudoku.6*


%changelog
* Thu Jan 16 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1:47.1.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Sat Oct 19 2024 David King <amigadave@amigadave.com> - 1:47.1.1-1
- Update to 47.1.1

* Mon Sep 16 2024 nmontero <nmontero@redhat.com> - 1:47.0-1
- Update to 47.0

* Sun Sep 01 2024 David King <amigadave@amigadave.com> - 1:47~rc-1
- Update to 47.rc

* Mon Aug 05 2024 nmontero <nmontero@redhat.com> - 1:47~beta-1
- Update to 47.beta

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1:47~alpha-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Fri Jul 05 2024 David King <amigadave@amigadave.com> - 1:47~alpha-1
- Update to 47.alpha

* Mon Jun 10 2024 Nieves Montero <nmontero@redhat.com> - 1:46.2-1
- Update to 46.2

* Mon May 06 2024 David King <amigadave@amigadave.com> - 1:46.1-1
- Update to 46.1

* Fri Mar 15 2024 David King <amigadave@amigadave.com> - 1:46.0-1
- Update to 46.0

* Mon Mar 04 2024 David King <amigadave@amigadave.com> - 1:46~rc-1
- Update to 46.rc

* Wed Feb 14 2024 David King <amigadave@amigadave.com> - 1:46~beta-1
- Update to 46.beta

* Wed Jan 24 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1:46~alpha-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Mon Jan 22 2024 David King <amigadave@amigadave.com> - 1:46~alpha-1
- Update to 46.alpha

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1:45.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jan 11 2024 Kalev Lember <klember@redhat.com> - 1:45.4-1
- Update to 45.4

* Wed Dec 06 2023 Kalev Lember <klember@redhat.com> - 1:45.3-1
- Update to 45.3

* Sat Oct 21 2023 Kalev Lember <klember@redhat.com> - 1:45.2-1
- Update to 45.2

* Tue Sep 19 2023 Kalev Lember <klember@redhat.com> - 1:45.0-1
- Update to 45.0

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1:45~alpha-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Fri Jun 30 2023 Kalev Lember <klember@redhat.com> - 1:45~alpha-1
- Update to 45.alpha

* Sat Mar 18 2023 David King <amigadave@amigadave.com> - 1:44.0-1
- Update to 44.0

* Fri Feb 17 2023 David King <amigadave@amigadave.com> - 44~beta-1
- Update to 44.beta

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1:43.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Mon Sep 19 2022 Kalev Lember <klember@redhat.com> - 1:43.0-1
- Update to 43.0

* Mon Aug 08 2022 Kalev Lember <klember@redhat.com> - 1:43~beta-1
- Update to 43.beta

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1:43~alpha-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Fri Jul 15 2022 Kalev Lember <klember@redhat.com> - 1:43~alpha-1
- Update to 43.alpha

* Fri Mar 25 2022 David King <amigadave@amigadave.com> - 1:42.0-1
- Update to 42.0

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1:40.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Tue Aug 03 2021 Kalev Lember <klember@redhat.com> - 1:40.2-1
- Update to 40.2

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1:40.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed May 05 2021 Kalev Lember <klember@redhat.com> - 1:40.1-1
- Update to 40.1

* Tue Mar 30 2021 Jonathan Wakely <jwakely@redhat.com> - 1:40.0-2
- Rebuilt for removed libstdc++ symbol (#1937698)

* Mon Mar 22 2021 Kalev Lember <klember@redhat.com> - 1:40.0-1
- Update to 40.0

* Fri Feb 19 2021 Kalev Lember <klember@redhat.com> - 1:40~alpha-1
- Update to 40.alpha

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1:3.38.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Sat Sep 12 2020 Kalev Lember <klember@redhat.com> - 1:3.38.0-1
- Update to 3.38.0

* Fri Sep 04 2020 Kalev Lember <klember@redhat.com> - 1:3.37.92-1
- Update to 3.37.92

* Mon Aug 17 2020 Kalev Lember <klember@redhat.com> - 1:3.37.90-1
- Update to 3.37.90

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1:3.37.3-3
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1:3.37.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Jul 20 2020 Kalev Lember <klember@redhat.com> - 1:3.37.3-1
- Update to 3.37.3

* Fri May 29 2020 Kalev Lember <klember@redhat.com> - 1:3.37.2-1
- Update to 3.37.2

* Tue May 05 2020 Kalev Lember <klember@redhat.com> - 1:3.37.1-1
- Update to 3.37.1

* Thu Mar 05 2020 Kalev Lember <klember@redhat.com> - 1:3.36.0-1
- Update to 3.36.0

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1:3.34.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Mon Oct 14 2019 Yanko Kaneti <yaneti@declera.com> - 1:3.34.1-1
- Update to 3.34.1

* Sun Sep 08 2019 Kalev Lember <klember@redhat.com> - 1:3.34.0-1
- Update to 3.34.0

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1:3.33.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Mon Jul 15 2019 Yanko Kaneti <yaneti@declera.com> - 1:3.33.4-1
- Update to 3.33.4

* Mon Mar 11 2019 Kalev Lember <klember@redhat.com> - 1:3.32.0-1
- Update to 3.32.0

* Mon Mar  4 2019 Yanko Kaneti <yaneti@declera.com> - 1:3.31.92-1
- Update to 3.31.92

* Tue Feb  5 2019 Yanko Kaneti <yaneti@declera.com> - 1:3.31.90-1
- Update to 3.31.90
- Application ID change to or.gnome.Sudoku

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1:3.31.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Wed Jan 23 2019 Kalev Lember <klember@redhat.com> - 1:3.31.1-1
- Update to 3.31.1

* Sun Sep  9 2018 Yanko Kaneti <yaneti@declera.com> - 1:3.30.0-2
- Rebuild

* Mon Sep  3 2018 Yanko Kaneti <yaneti@declera.com> - 1:3.30.0-1
- Update to 3.30.0

* Sat Jul 14 2018 Yanko Kaneti <yaneti@declera.com> - 1:3.29.2-3
- BR: gcc gcc-c++ - https://fedoraproject.org/wiki/Changes/Remove_GCC_from_BuildRoot

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1:3.29.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue May 22 2018 Yanko Kaneti <yaneti@declera.com> - 1:3.29.2-1
- Update to 3.29.2. Upstream move to meson

* Sat Mar 10 2018 Yanko Kaneti <yaneti@declera.com> - 1:3.28.0-1
- Update to 3.28.0

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1:3.27.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Sat Jan 06 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 1:3.27.3-2
- Remove obsolete scriptlets

* Tue Dec 12 2017 Yanko Kaneti <yaneti@declera.com> - 1:3.27.3-1
- Update to 3.27.3

* Sat Sep  9 2017 Yanko Kaneti <yaneti@declera.com> - 1:3.26.0-1
- Update to 3.26.0

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1:3.25.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1:3.25.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Wed Jul 19 2017 Yanko Kaneti <yaneti@declera.com> - 1:3.25.4-1
- Update to 3.25.5

* Tue Mar 21 2017 Yanko Kaneti <yaneti@declera.com> - 1:3.24.0-1
- Update to 3.24.0

* Mon Mar 13 2017 Yanko Kaneti <yaneti@declera.com> - 1:3.23.92.1-1
- Update to 3.23.92.1

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1:3.22.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Nov  7 2016 Yanko Kaneti <yaneti@declera.com> - 1:3.22.2-1
- Update to 3.22.2.
- Replace intltool requirement with gettext-devel

* Wed Sep 21 2016 Kalev Lember <klember@redhat.com> - 1:3.22.0-1
- Update to 3.22.0

* Thu Aug 18 2016 Kalev Lember <klember@redhat.com> - 1:3.21.90-1
- Update to 3.21.90
- Move desktop file validation to the check section
- Use make_install macro

* Sun Jul 17 2016 Kalev Lember <klember@redhat.com> - 1:3.21.4-1
- Update to 3.21.4

* Tue Jun 21 2016 Yanko Kaneti <yaneti@declera.com> - 1:3.21.3-1
- Update to 3.21.3. Drop ancient obsoletes

* Tue May 24 2016 Kalev Lember <klember@redhat.com> - 1:3.20.2-1
- Update to 3.20.2

* Sat May  7 2016 Yanko Kaneti <yaneti@declera.com> - 1:3.20.1-1
- Update to 3.20.1

* Sun Mar 20 2016 Yanko Kaneti <yaneti@declera.com> - 1:3.20.0-1
- Update to 3.20.0. License change to GPLv3+

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1:3.19.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Sun Jan 17 2016 Yanko Kaneti <yaneti@declera.com> - 1:3.19.4-1
- Update to 3.19.4

* Fri Nov 20 2015 Yanko Kaneti <yaneti@declera.com> - 1:3.19.2-1
- First development release from the 3.20 cycle

* Sun Nov  8 2015 Yanko Kaneti <yaneti@declera.com> - 1:3.18.2-1
- Update to 3.18.2

* Sun Oct 11 2015 Kalev Lember <klember@redhat.com> - 1:3.18.1-1
- Update to 3.18.1

* Mon Sep 21 2015 Kalev Lember <klember@redhat.com> - 1:3.18.0-1
- Update to 3.18.0

* Sun Sep 13 2015 Yanko Kaneti <yaneti@declera.com> - 3.17.92-1
- Update to 3.17.92

* Fri Aug 14 2015 Yanko Kaneti <yaneti@declera.com> - 3.17.90-1
- Update to 3.17.90

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1:3.17.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Mon May 25 2015 Yanko Kaneti <yaneti@declera.com> - 3.17.2-1
- Update to 3.17.2
- No more HighContrast icons

* Sat Apr 18 2015 Yanko Kaneti <yaneti@declera.com> - 3.16.0-2
- Rebuild for silent qqwing ABI breakage - bug 1213051

* Mon Mar 23 2015 Yanko Kaneti <yaneti@declera.com> - 3.16.0-1
- Update to 3.16.0
- Use license macro

* Mon Mar 16 2015 Yanko Kaneti <yaneti@declera.com> - 3.15.92-1
- Update to 3.15.92

* Mon Mar  2 2015 Yanko Kaneti <yaneti@declera.com> - 3.15.91-1
- Update to 3.15.91

* Mon Feb 16 2015 Yanko Kaneti <yaneti@declera.com> - 3.15.90.1-1
- Update to 3.15.90.1

* Tue Nov 25 2014 Yanko Kaneti <yaneti@declera.com> - 3.15.2-1
- Update to 3.15.2

* Fri Oct 31 2014 Yanko Kaneti <yaneti@declera.com> - 3.15.1-1
- First devlopment release from the 3.16 cycle

* Wed Oct 15 2014 Yanko Kaneti <yaneti@declera.com> - 1:3.14.1-1
- Update to 3.14.1

* Mon Sep 22 2014 Yanko Kaneti <yaneti@declera.com> - 1:3.14.0-1
- Update to 3.14.0

* Tue Sep 16 2014 Yanko Kaneti <yaneti@declera.com> - 1:3.13.92-1
- Update to 3.13.92

* Sun Aug 24 2014 Michael Catanzaro <mcatanzaro@gnome.org> - 1:3.13.90-3
- Really rebuilt for qqwing 1.2.0

* Sat Aug 23 2014 Michael Catanzaro <mcatanzaro@gnome.org> - 1:3.13.90-2
- Rebuilt for qqwing 1.2.0

* Tue Aug 19 2014 Kalev Lember <kalevlember@gmail.com> - 1:3.13.90-1
- Update to 3.13.90

* Sat Aug 16 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1:3.13.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Mon Jul 21 2014 Yanko Kaneti <yaneti@declera.com> - 3.13.4-1
- Update to 3.13.4

* Tue Jun 24 2014 Yanko Kaneti <yaneti@declera.com> - 3.13.3-1
- First development release from the 3.14 cycle.
- Redesigned and rewritten in vala. Spec rework.

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1:3.12.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Tue May 27 2014 Kalev Lember <kalevlember@gmail.com> - 1:3.12.2-2
- Rebuilt for https://fedoraproject.org/wiki/Changes/Python_3.4

* Mon May 12 2014 Yanko Kaneti <yaneti@declera.com> - 3.12.2-1
- Update to 3.12.2

* Mon Apr 14 2014 Yanko Kaneti <yaneti@declera.com> - 3.12.1-1
- Update to 3.12.1

* Mon Mar 24 2014 Yanko Kaneti <yaneti@declera.com> - 3.12.0-1
- Update to 3.12.0

* Sun Mar 16 2014 Yanko Kaneti <yaneti@declera.com> - 3.11.92-1
- Update to 3.11.92

* Mon Feb 17 2014 Yanko Kaneti <yaneti@declera.com> - 3.11.90-1
- Update to 3.11.90

* Mon Dec 16 2013 Yanko Kaneti <yaneti@declera.com> - 3.11.3-1
- Update to 3.11.3. Update url. Drop upstreamed patch

* Sat Nov 16 2013 Yanko Kaneti <yaneti@declera.com> - 3.11.2-1
- Update to 3.11.2. Move to python 3

* Mon Oct 28 2013 Yanko Kaneti <yaneti@declera.com> - 3.11.1-1
- First release from the new upstream devel cycle

* Sat Oct 12 2013 Yanko Kaneti <yaneti@declera.com> - 3.10.1-1
- Update to 3.10.1

* Mon Sep 23 2013 Yanko Kaneti <yaneti@declera.com> - 1:3.10.0-1
- Update to 3.10.0

* Tue Sep 17 2013 Yanko Kaneti <yaneti@declera.com> - 1:3.9.92-1
- Update to 3.9.92
- Drop upstreamed patch
- Add appdata

* Wed Aug 21 2013 Yanko Kaneti <yaneti@declera.com> - 1:3.9.90-1
- Update to 3.9.90
- Drop upstreamed patch - add a new one

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1:3.8.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Sat Jun 22 2013 Kalev Lember <kalevlember@gmail.com> - 1:3.8.1-3
- Obsolete gnome-games-help as well

* Thu Jun 20 2013 Matthias Clasen <mclasen@redhat.com> - 1:3.8.1-2
- Obsolete gnome-games (for upgrades from f17)

* Mon Apr 15 2013 Kalev Lember <kalevlember@gmail.com> - 1:3.8.1-1
- Update to 3.8.1

* Wed Mar 27 2013 Yanko Kaneti <yaneti@declera.com> - 1:3.8.0-2
- HighContrast icon theme scriptlet fixes

* Wed Mar 27 2013 Yanko Kaneti <yaneti@declera.com> - 1:3.8.0-1
- Update to 3.8.0

* Thu Feb 14 2013 Yanko Kaneti <yaneti@declera.com> - 1:3.7.4-2
- Add epoch to avoid being obsoleted by gnome-games-sudoku

* Wed Feb 13 2013 Yanko Kaneti <yaneti@declera.com> - 1:3.7.4-1
- Initial packaging of standalone gnome-sudoku
