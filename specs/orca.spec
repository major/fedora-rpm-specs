%global tarball_version %%(echo %{version} | tr '~' '.')

Name:           orca
Version:        47.2
Release:        2%{?dist}
Summary:        Assistive technology for people with visual impairments

License:        LGPL-2.1-or-later AND CC-BY-SA-3.0
URL:            https://wiki.gnome.org/Projects/Orca
Source0:        https://download.gnome.org/sources/%{name}/47/%{name}-%{tarball_version}.tar.xz

BuildArch:      noarch

BuildRequires:  pkgconfig(atk-bridge-2.0)
BuildRequires:  pkgconfig(atspi-2)
BuildRequires:  pkgconfig(liblouis)
BuildRequires:  pkgconfig(pygobject-3.0)
BuildRequires:  brlapi-devel
BuildRequires:  brltty
BuildRequires:  gettext
BuildRequires:  intltool
BuildRequires:  gtk3-devel
BuildRequires:  itstool
BuildRequires:  meson
BuildRequires:  python3-brlapi
BuildRequires:  python3-devel
BuildRequires:  python3-louis
BuildRequires:  python3-pyatspi
BuildRequires:  python3-speechd
BuildRequires:  /usr/bin/desktop-file-validate

Requires:       libwnck3
Requires:       python3-brlapi
Requires:       python3-louis
Requires:       python3-pyatspi
Requires:       python3-speechd
Requires:       speech-dispatcher

%description
Orca is a screen reader that provides access to the graphical desktop via
user-customizable combinations of speech and/or braille. Orca works with
applications and toolkits that support the assistive technology service
provider interface (AT-SPI), e.g. the GNOME desktop.

%prep
%autosetup -p1 -n %{name}-%{tarball_version}


%build
%meson
%meson_build


%install
%meson_install

%find_lang %{name} --with-gnome


%check
desktop-file-validate %{buildroot}%{_sysconfdir}/xdg/autostart/orca-autostart.desktop


%files -f %{name}.lang
%license COPYING
%doc AUTHORS NEWS README.md
%{_bindir}/orca
%{python3_sitelib}/orca/
%{_datadir}/icons/hicolor/*/apps/orca.png
%{_datadir}/icons/hicolor/scalable/apps/orca.svg
%{_datadir}/icons/hicolor/symbolic/apps/orca-symbolic.svg
%{_datadir}/orca
%{_sysconfdir}/xdg/autostart/orca-autostart.desktop
%{_mandir}/man1/orca.1*


%changelog
* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 47.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Mon Nov 25 2024 nmontero <nmontero@redhat.com> - 47.2-1
- Update to 47.2

* Sun Oct 27 2024 David King <amigadave@amigadave.com> - 47.1-1
- Update to 47.1

* Tue Oct 15 2024 Gwyn Ciesla <gwync@protonmail.com> - 47.0-2
- brltty rebuild

* Wed Sep 18 2024 nmontero <nmontero@redhat.com> - 47.0-1
- Update to 47.0

* Mon Sep 02 2024 David King <amigadave@amigadave.com> - 47~rc-1
- Update to 47.rc

* Mon Aug 19 2024 nmontero <nmontero@redhat.com> - 47~beta-1
- Update to 47.beta

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 47~alpha-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Wed Jun 26 2024 Nieves Montero <nmontero@redhat.com> - 46.2-1
- Update to 46.2

* Fri Jun 07 2024 Python Maint <python-maint@redhat.com> - 46.1-4
- Rebuilt for Python 3.13

* Fri Jun 07 2024 Python Maint <python-maint@redhat.com> - 46.1-3
- Rebuilt for Python 3.13

* Thu May 02 2024 Lukas Tyrychtr <ltyrycht@redhat.com> - 46.1-2
- Require speech-dispatcher, restoring the behavior of bringing it as well, as after the split we got only its libraries, and we need it for speech synthesis

* Tue Apr 02 2024 David King <amigadave@amigadave.com> - 46.1-1
- Update to 46.1

* Fri Mar 15 2024 David King <amigadave@amigadave.com> - 46.0-1
- Update to 46.0

* Sat Mar 02 2024 David King <amigadave@amigadave.com> - 46~beta-1
- Update to 46.beta

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 46~alpha-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Mon Jan 22 2024 David King <amigadave@amigadave.com> - 46~alpha-1
- Update to 46.alpha

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 45.2-2

- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jan 11 2024 Kalev Lember <klember@redhat.com> - 45.2-1
- Update to 45.2

* Sat Oct 21 2023 Kalev Lember <klember@redhat.com> - 45.1-1
- Update to 45.1

* Tue Sep 19 2023 Kalev Lember <klember@redhat.com> - 45.0-1
- Update to 45.0

* Wed Sep 06 2023 Kalev Lember <klember@redhat.com> - 45~rc-1
- Update to 45.rc

* Thu Aug 17 2023 Kalev Lember <klember@redhat.com> - 45~beta2-1
- Update to 45.beta2

* Mon Aug 14 2023 Kalev Lember <klember@redhat.com> - 45~beta-1
- Update to 45.beta
- Drop requires on python3-zombie-imp now that orca is ported away from it

* Sun Aug 13 2023 Kalev Lember <klember@redhat.com> - 45~alpha-2
- Add requires on python3-zombie-imp

* Sat Aug 05 2023 Kalev Lember <klember@redhat.com> - 45~alpha-1
- Update to 45.alpha

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 44.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jun 15 2023 Python Maint <python-maint@redhat.com> - 44.1-2
- Rebuilt for Python 3.12

* Wed May 31 2023 Kalev Lember <klember@redhat.com> - 44.1-1
- Update to 44.1

* Mon Mar 27 2023 David King <amigadave@amigadave.com> - 44.0-1
- Update to 44.0

* Thu Mar 09 2023 David King <amigadave@amigadave.com> - 44~rc-1
- Update to 44.rc

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 43.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Jan 05 2023 David King <amigadave@amigadave.com> - 43.1-1
- Update to 43.1

* Fri Sep 23 2022 Kalev Lember <klember@redhat.com> - 43.0-1
- Update to 43.0

* Tue Sep 06 2022 Kalev Lember <klember@redhat.com> - 43~beta-1
- Update to 43.beta

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 43~alpha-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed Jul 06 2022 David King <amigadave@amigadave.com> - 43~alpha-1
- Update to 43.alpha

* Mon Jun 13 2022 Python Maint <python-maint@redhat.com> - 42.1-2
- Rebuilt for Python 3.11

* Tue May 17 2022 David King <amigadave@amigadave.com> - 42.1-1
- Update to 42.1

* Tue Mar 22 2022 David King <amigadave@amigadave.com> - 42.0-1
- Update to 42.0

* Fri Mar 11 2022 David King <amigadave@amigadave.com> - 42~rc-1
- Update to 42.rc

* Tue Feb 15 2022 David King <amigadave@amigadave.com> - 42~beta-1
- Update to 42.beta

* Tue Feb 01 2022 David King <amigadave@amigadave.com> - 41.2-1
- Update to 41.2

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 41.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Tue Dec 07 2021 Kalev Lember <klember@redhat.com> - 41.1-1
- Update to 41.1

* Tue Nov 16 2021 Kalev Lember <klember@redhat.com> - 41.0-2
- Backport another fix for compatibility with Python 3.10 (#2023682)

* Thu Sep 16 2021 Kalev Lember <klember@redhat.com> - 41.0-1
- Update to 41.0

* Fri Sep 10 2021 Kalev Lember <klember@redhat.com> - 41~rc-2
- Fix compatibility with Python 3.10 (#1973397)

* Wed Sep 08 2021 Kalev Lember <klember@redhat.com> - 41~rc-1
- Update to 41.rc

* Tue Aug 24 2021 Kalev Lember <klember@redhat.com> - 41~beta-1
- Update to 41.beta

* Thu Aug 19 2021 Kalev Lember <klember@redhat.com> - 41~alpha-1
- Update to 41.alpha

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 40.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 40.0-2
- Rebuilt for Python 3.10

* Mon Mar 22 2021 Kalev Lember <klember@redhat.com> - 40.0-1
- Update to 40.0

* Thu Mar 11 2021 Kalev Lember <klember@redhat.com> - 40~rc-1
- Update to 40.rc

* Mon Feb 22 2021 Kalev Lember <klember@redhat.com> - 40~beta-1
- Update to 40.beta

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 3.38.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jan  5 2021 Kalev Lember <klember@redhat.com> - 3.38.2-1
- Update to 3.38.2

* Fri Dec 11 2020 Kalev Lember <klember@redhat.com> - 3.38.1-1
- Update to 3.38.1

* Fri Sep 11 2020 Kalev Lember <klember@redhat.com> - 3.38.0-1
- Update to 3.38.0

* Mon Aug 17 2020 Kalev Lember <klember@redhat.com> - 3.37.90-1
- Update to 3.37.90

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.37.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Jun 04 2020 Kalev Lember <klember@redhat.com> - 3.37.2-1
- Update to 3.37.2

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 3.37.1-2
- Rebuilt for Python 3.9

* Tue May 05 2020 Kalev Lember <klember@redhat.com> - 3.37.1-1
- Update to 3.37.1

* Fri Apr 24 2020 Kalev Lember <klember@redhat.com> - 3.36.2-1
- Update to 3.36.2

* Wed Mar 11 2020 Kalev Lember <klember@redhat.com> - 3.36.1-1
- Update to 3.36.1

* Wed Mar 11 2020 Kalev Lember <klember@redhat.com> - 3.36.0-1
- Update to 3.36.0

* Wed Mar 04 2020 Kalev Lember <klember@redhat.com> - 3.35.92-1
- Update to 3.35.92

* Sun Feb 23 2020 Kalev Lember <klember@redhat.com> - 3.35.91-1
- Update to 3.35.91

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.35.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Tue Jan 07 2020 Kalev Lember <klember@redhat.com> - 3.35.3-1
- Update to 3.35.3

* Sat Nov 16 2019 Kalev Lember <klember@redhat.com> - 3.34.1-1
- Update to 3.34.1

* Mon Sep 09 2019 Kalev Lember <klember@redhat.com> - 3.34.0-1
- Update to 3.34.0

* Tue Aug 27 2019 Kalev Lember <klember@redhat.com> - 3.33.91-1
- Update to 3.33.91

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 3.33.90-2
- Rebuilt for Python 3.8

* Mon Aug 12 2019 Kalev Lember <klember@redhat.com> - 3.33.90-1
- Update to 3.33.90

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.33.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Wed Jun 19 2019 Kalev Lember <klember@redhat.com> - 3.33.3-1
- Update to 3.33.3

* Thu May 09 2019 Kalev Lember <klember@redhat.com> - 3.33.1-1
- Update to 3.33.1

* Wed Mar 13 2019 Kalev Lember <klember@redhat.com> - 3.32.0-1
- Update to 3.32.0

* Fri Mar 08 2019 Kalev Lember <klember@redhat.com> - 3.31.92-1
- Update to 3.31.92

* Thu Feb 21 2019 Kalev Lember <klember@redhat.com> - 3.31.91-1
- Update to 3.31.91

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.31.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Mon Jan 14 2019 Kalev Lember <klember@redhat.com> - 3.31.4-1
- Update to 3.31.4

* Fri Oct 19 2018 Kalev Lember <klember@redhat.com> - 3.30.1-1
- Update to 3.30.1

* Tue Sep 18 2018 Kalev Lember <klember@redhat.com> - 3.30.0-1
- Update to 3.30.0

* Thu Sep 06 2018 Kalev Lember <klember@redhat.com> - 3.29.92-1
- Update to 3.29.92

* Mon Aug 13 2018 Kalev Lember <klember@redhat.com> - 3.29.4-1
- Update to 3.29.4

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.28.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Jun 29 2018 Kalev Lember <klember@redhat.com> - 3.28.2-1
- Update to 3.28.2

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 3.28.1-2
- Rebuilt for Python 3.7

* Sun Apr 22 2018 Kalev Lember <klember@redhat.com> - 3.28.1-1
- Update to 3.28.1

* Mon Mar 26 2018 Kalev Lember <klember@redhat.com> - 3.28.0-1
- Update to 3.28.0

* Sun Mar 11 2018 Kalev Lember <klember@redhat.com> - 3.27.91-1
- Update to 3.27.91

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.26.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Fri Jan 05 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 3.26.0-2
- Remove obsolete scriptlets

* Fri Sep 15 2017 Kalev Lember <klember@redhat.com> - 3.26.0-1
- Update to 3.26.0

* Mon Jul 31 2017 Kalev Lember <klember@redhat.com> - 3.25.4-1
- Update to 3.25.4

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.24.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Tue Mar 21 2017 Kalev Lember <klember@redhat.com> - 3.24.0-1
- Update to 3.24.0

* Tue Feb 28 2017 Richard Hughes <rhughes@redhat.com> - 3.23.91-1
- Update to 3.23.91

* Mon Feb 13 2017 Richard Hughes <rhughes@redhat.com> - 3.23.4-1
- Update to 3.23.4

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.22.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Dec 19 2016 Miro Hrončok <mhroncok@redhat.com> - 3.22.2-2
- Rebuild for Python 3.6

* Thu Nov 24 2016 Kalev Lember <klember@redhat.com> - 3.22.2-1
- Update to 3.22.2

* Wed Oct 12 2016 Kalev Lember <klember@redhat.com> - 3.22.1-1
- Update to 3.22.1

* Fri Sep 16 2016 Kalev Lember <klember@redhat.com> - 3.21.92-1
- Update to 3.21.92

* Sat Sep 03 2016 Kalev Lember <klember@redhat.com> - 3.21.91-1
- Update to 3.21.91
- Don't set group tags
- Validate autostart desktop file

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.21.3-2
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Wed Jun 22 2016 Richard Hughes <rhughes@redhat.com> - 3.21.3-1
- Update to 3.21.3

* Tue May 03 2016 Kalev Lember <klember@redhat.com> - 3.21.1-1
- Update to 3.21.1

* Tue Mar 22 2016 Kalev Lember <klember@redhat.com> - 3.20.0-1
- Update to 3.20.0

* Sun Mar 20 2016 Kalev Lember <klember@redhat.com> - 3.19.92-1
- Update to 3.19.92

* Fri Mar 04 2016 Kalev Lember <klember@redhat.com> - 3.19.91-1
- Update to 3.19.91

* Thu Feb 18 2016 Richard Hughes <rhughes@redhat.com> - 3.19.90-1
- Update to 3.19.90

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 3.19.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Dec 16 2015 Kalev Lember <klember@redhat.com> - 3.19.3-1
- Update to 3.19.3

* Thu Nov 26 2015 Kalev Lember <klember@redhat.com> - 3.19.2-1
- Update to 3.19.2

* Tue Nov 10 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.18.2-2
- Rebuilt for https://fedoraproject.org/wiki/Changes/python3.5

* Tue Nov 10 2015 Kalev Lember <klember@redhat.com> - 3.18.2-1
- Update to 3.18.2

* Wed Oct 14 2015 Kalev Lember <klember@redhat.com> - 3.18.1-1
- Update to 3.18.1

* Mon Oct 05 2015 Bastien Nocera <bnocera@redhat.com> 3.18.0-2
- Hide the Orca launcher in GNOME

* Mon Sep 21 2015 Kalev Lember <klember@redhat.com> - 3.18.0-1
- Update to 3.18.0

* Wed Sep 16 2015 Kalev Lember <klember@redhat.com> - 3.17.92-1
- Update to 3.17.92

* Wed Sep 02 2015 Kalev Lember <klember@redhat.com> - 3.17.91-1
- Update to 3.17.91

* Sun Aug 23 2015 Kalev Lember <klember@redhat.com> - 3.17.90-2
- Adapt for liblouis-python3 -> python3-louis rename

* Wed Aug 19 2015 Kalev Lember <klember@redhat.com> - 3.17.90-1
- Update to 3.17.90
- Use make_install macro

* Tue Jul 28 2015 David King <amigadave@amigadave.com> - 3.17.4-1
- Update to 3.17.4
- Update URL
- Update man page glob in files section
- Use pkgconfig for BuildRequires
- Validate desktop files in check phase
- Preserve timestamps during install

* Tue Jun 30 2015 Kalev Lember <klember@redhat.com> - 3.17.3-1
- Update to 3.17.3

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.17.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sun May 31 2015 Kalev Lember <kalevlember@gmail.com> - 3.17.2-1
- Update to 3.17.2

* Tue May 12 2015 Kalev Lember <kalevlember@gmail.com> - 3.16.2-1
- Update to 3.16.2

* Thu Apr 16 2015 Kalev Lember <kalevlember@gmail.com> - 3.16.1-1
- Update to 3.16.1

* Mon Mar 23 2015 Kalev Lember <kalevlember@gmail.com> - 3.16.0-1
- Update to 3.16.0

* Tue Mar 17 2015 Kalev Lember <kalevlember@gmail.com> - 3.15.92-1
- Update to 3.15.92

* Tue Mar 03 2015 Kalev Lember <kalevlember@gmail.com> - 3.15.91-1
- Update to 3.15.91
- Use the %%license macro for the COPYING file

* Tue Jan 20 2015 Richard Hughes <rhughes@redhat.com> - 3.15.4-1
- Update to 3.15.4

* Thu Dec 04 2014 Kalev Lember <kalevlember@gmail.com> - 3.14.3-1
- Update to 3.14.3

* Mon Nov 10 2014 Kalev Lember <kalevlember@gmail.com> - 3.14.2-1
- Update to 3.14.2

* Tue Sep 23 2014 Kalev Lember <kalevlember@gmail.com> - 3.14.0-1
- Update to 3.14.0

* Wed Sep 17 2014 Kalev Lember <kalevlember@gmail.com> - 3.13.92-1
- Update to 3.13.92

* Wed Sep 03 2014 Kalev Lember <kalevlember@gmail.com> - 3.13.91-1
- Update to 3.13.91

* Tue Aug 19 2014 Kalev Lember <kalevlember@gmail.com> - 3.13.90-1
- Update to 3.13.90

* Tue Jun 24 2014 Richard Hughes <rhughes@redhat.com> - 3.13.3-1
- Update to 3.13.3

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.13.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Tue May 27 2014 Kalev Lember <kalevlember@gmail.com> - 3.13.1-2
- Rebuilt for https://fedoraproject.org/wiki/Changes/Python_3.4

* Thu May 01 2014 Kalev Lember <kalevlember@gmail.com> - 3.13.1-1
- Update to 3.13.1
- Drop pre-historic gnopernicus obsoletes

* Wed Apr 16 2014 Kalev Lember <kalevlember@gmail.com> - 3.12.1-1
- Update to 3.12.1

* Mon Mar 24 2014 Richard Hughes <rhughes@redhat.com> - 3.12.0-1
- Update to 3.12.0

* Sun Mar 23 2014 Kalev Lember <kalevlember@gmail.com> - 3.11.92-2
- Drop the dependency on control-center (#1074350)

* Wed Mar 19 2014 Richard Hughes <rhughes@redhat.com> - 3.11.92-1
- Update to 3.11.92

* Tue Mar 04 2014 Richard Hughes <rhughes@redhat.com> - 3.11.91-1
- Update to 3.11.91

* Wed Feb 19 2014 Richard Hughes <rhughes@redhat.com> - 3.11.90-1
- Update to 3.11.90

* Wed Feb 05 2014 Richard Hughes <rhughes@redhat.com> - 3.11.5.1-1
- Update to 3.11.5.1

* Wed Jan 15 2014 Richard Hughes <rhughes@redhat.com> - 3.11.4-1
- Update to 3.11.4

* Tue Dec 17 2013 Richard Hughes <rhughes@redhat.com> - 3.11.3-1
- Update to 3.11.3

* Mon Nov 25 2013 Richard Hughes <rhughes@redhat.com> - 3.11.2-1
- Update to 3.11.2

* Thu Nov 14 2013 Richard Hughes <rhughes@redhat.com> - 3.10.2-1
- Update to 3.10.2

* Tue Oct 29 2013 Richard Hughes <rhughes@redhat.com> - 3.10.1-1
- Update to 3.10.1

* Wed Sep 25 2013 Kalev Lember <kalevlember@gmail.com> - 3.10.0-1
- Update to 3.10.0

* Wed Sep 18 2013 Kalev Lember <kalevlember@gmail.com> - 3.9.92-1
- Update to 3.9.92
- Build as noarch
- Drop the python3-cairo dependency (#1007598)

* Tue Sep 03 2013 Kalev Lember <kalevlember@gmail.com> - 3.9.91-1
- Update to 3.9.91

* Thu Aug 22 2013 Kalev Lember <kalevlember@gmail.com> - 3.9.90-1
- Update to 3.9.90

* Sat Aug 10 2013 Kalev Lember <kalevlember@gmail.com> - 3.9.5-1
- Update to 3.9.5

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.9.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Tue Jul 16 2013 Richard Hughes <rhughes@redhat.com> - 3.9.4-1
- Update to 3.9.4

* Fri Jun 21 2013 Kalev Lember <kalevlember@gmail.com> - 3.9.3-1
- Update to 3.9.3

* Sun Jun 02 2013 Kalev Lember <kalevlember@gmail.com> - 3.9.2-1
- Update to 3.9.2

* Wed Apr 17 2013 Kalev Lember <kalevlember@gmail.com> - 3.8.1-1
- Update to 3.8.1

* Fri Apr 05 2013 Kalev Lember <kalevlember@gmail.com> - 3.8.0-2
- Enable the brlapi support

* Tue Mar 26 2013 Kalev Lember <kalevlember@gmail.com> - 3.8.0-1
- Update to 3.8.0

* Wed Mar 20 2013 Richard Hughes <rhughes@redhat.com> - 3.7.92-1
- Update to 3.7.92

* Tue Mar 19 2013 Richard Hughes <rhughes@redhat.com> - 3.7.91-1
- Update to 3.7.91

* Wed Feb 20 2013 Richard Hughes <rhughes@redhat.com> - 3.7.90-1
- Update to 3.7.90

* Wed Feb 06 2013 Richard Hughes <rhughes@redhat.com> - 3.7.5-1
- Update to 3.7.5

* Wed Jan 16 2013 Richard Hughes <hughsient@gmail.com> - 3.7.4-1
- Update to 3.7.4

* Wed Jan 09 2013 Richard Hughes <hughsient@gmail.com> - 3.7.3-1
- Update to 3.7.3

* Wed Nov 21 2012 Richard Hughes <hughsient@gmail.com> - 3.7.2-1
- Update to 3.7.2

* Fri Nov 09 2012 Kalev Lember <kalevlember@gmail.com> - 3.7.1-1
- Update to 3.7.1

* Tue Oct 16 2012 Kalev Lember <kalevlember@gmail.com> - 3.6.1-1
- Update to 3.6.1

* Tue Sep 25 2012 Kalev Lember <kalevlember@gmail.com> - 3.6.0-1
- Update to 3.6.0

* Tue Sep 18 2012 Kalev Lember <kalevlember@gmail.com> - 3.5.92-1
- Update to 3.5.92

* Tue Sep 04 2012 Richard Hughes <hughsient@gmail.com> - 3.5.91-1
- Update to 3.5.91

* Tue Aug 21 2012 Richard Hughes <hughsient@gmail.com> - 3.5.90-1
- Update to 3.5.90

* Wed Jul 18 2012 Kalev Lember <kalevlember@gmail.com> - 3.5.4-1
- Back down to 3.5.4, we want to stick with python 2.7 for now

* Tue Jul 17 2012 Richard Hughes <hughsient@gmail.com> - 3.7.0.4-1
- Update to 3.7.0.4

* Wed Jun 27 2012 Matthias Clasen <mclasen@redhat.com> - 1:3.5.3-2
- Back down to 3.5.3, we want to stick with python 2.7 for now

* Tue Jun 26 2012 Richard Hughes <hughsient@gmail.com> - 3.7.0.3-1
- Update to 3.7.0.3

* Mon Jun 25 2012 Richard Hughes <hughsient@gmail.com> - 3.5.3-1
- Update to 3.5.3

* Thu Jun 07 2012 Richard Hughes <hughsient@gmail.com> - 3.5.2-1
- Update to 3.5.2

* Sat May 05 2012 Kalev Lember <kalevlember@gmail.com> - 3.5.1-1
- Update to 3.5.1

* Tue Apr 17 2012 Kalev Lember <kalevlember@gmail.com> - 3.4.1-2
- Don't depend on gnome 2 python libs (#716719)
- Require pyxdg (#761306)

* Tue Apr 17 2012 Kalev Lember <kalevlember@gmail.com> - 3.4.1-1
- Update to 3.4.1

* Tue Mar 27 2012 Kalev Lember <kalevlember@gmail.com> - 3.4.0-1
- Update to 3.4.0

* Wed Mar 21 2012 Kalev Lember <kalevlember@gmail.com> - 3.3.92-1
- Update to 3.3.92

* Tue Mar  6 2012 Matthias Clasen <mclasen@redhat.com> - 3.3.91-1
- Update to 3.3.91

* Sat Feb 25 2012 Matthias Clasen <mclasen@redhat.com> - 3.3.90-1
- Update to 3.3.90

* Tue Feb  7 2012 Matthias Clasen <mclasen@redhat.com> - 3.3.5-1
- Update to 3.3.5

* Tue Jan 17 2012 Matthias Clasen <mclasen@redhat.com> - 3.3.4-1
- Update to 3.3.4

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.3.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Dec 20 2011 Matthias Clasen <mclasen@redhat.com> - 3.3.3-1
- Update to 3.3.3

* Wed Nov 23 2011 Matthias Clasen <mclasen@redhat.com> - 3.3.2-1
- Update to 3.3.2

* Wed Nov  2 2011 Matthias Clasen <mclasen@redhat.com> - 3.3.1-1
- Update to 3.3.1

* Wed Oct 26 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.2.1-2
- Rebuilt for glibc bug#747377

* Tue Oct 18 2011 Matthias Clasen <mclasen@redhat.com> - 3.2.1-1
- Update to 3.2.1

* Tue Sep 27 2011 Ray <rstrode@redhat.com> - 3.2.0-1
- Update to 3.2.0

* Tue Sep 20 2011 Matthias Clasen <mclasen@redhat.com> 3.1.92-1
- Update to 3.1.92

* Fri Sep  9 2011 Matthias Clasen <mclasen@redhat.com> 3.1.91-1
- Update to 3.1.91

* Thu Aug 18 2011 Matthias Clasen <mclasen@redhat.com> 3.1.5-1
- Update to 3.1.5

* Mon Jul 25 2011 Matthias Clasen <mclasen@redhat.com> 3.1.4-1
- Update to 3.1.4

* Tue Jul 05 2011 Bastien Nocera <bnocera@redhat.com> 3.1.3-1
- Update to 3.1.3

* Thu Jun 16 2011 Tomas Bzatek <tbzatek@redhat.com> - 3.1.2-1
- Update to 3.1.2

* Wed May 11 2011 Tomas Bzatek <tbzatek@redhat.com> 3.1.1-1
- Update to 3.1.1

* Tue Apr 26 2011 Matthias Clasen <mclasen@redhat.com> 3.0.1-1
- Update to 3.0.1

* Thu Apr  7 2011 Matthias Clasen <mclasen@redhat.com> 3.0.0-2
- Only autostart in GNOME

* Mon Apr  4 2011 Matthias Clasen <mclasen@redhat.com> 3.0.0-1
- Update to 3.0.0
- Bring the gnome-speech dependency back

* Sun Apr  3 2011 Matthias Clasen <mclasen@redhat.com> 2.91.93-2
- Drop PyYAML depencency (no longer used)
- Don't require gnome-speech (speech-dispatcher is preferred)

* Fri Mar 25 2011 Matthias Clasen <mclasen@redhat.com> 2.91.93-1
- Update to 2.91.93

* Fri Mar 25 2011 Bastien Nocera <bnocera@redhat.com> 2.91.92-2
- Use GSettings to check whether toolkit accessibility is enabled,
  patch from Frederic Crozat

* Tue Mar 22 2011 Matthias Clasen <mclasen@redhat.com> 2.91.92-1
- Update to 2.91.92

* Thu Mar  3 2011 Matthias Clasen <mclasen@redhat.com> 2.91.91-1
- Update to 2.91.91
- Drop a space-saving hack

* Tue Feb 22 2011 Matthias Clasen <mclasen@redhat.com> 2.91.90-1
- Update to 2.91.90

* Sun Feb 20 2011 Matthias Clasen <mclasen@redhat.com> 2.91.6-4
- Fix dependencies

* Thu Feb 17 2011 Bastien Nocera <bnocera@redhat.com> 2.91.6-3
- Don't remove the desktop files, as they are "no display" anyway
  (this would also have removed the autostart desktop file in
  newer versions of Orca)

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.91.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Wed Feb  2 2011 Christopher Aillon <caillon@redhat.com> - 2.91.6-1
- Update to 2.91.6

* Tue Jan 11 2011 Matthias Clasen <mclasen@redhat.com> - 2.91.5-1
- Update to 2.91.5

* Thu Dec  2 2010 Matthias Clasen <mclasen@redhat.com> - 2.91.3-1
- Update to 2.91.3

* Thu Nov 11 2010 Matthias Clasen <mclasen@redhat.com> - 2.91.2-1
- Update to 2.91.2

* Wed Oct  6 2010 Matthias Clasen <mclasen@redhat.com> - 2.91.0-1
- Update to 2.91.0

* Mon Oct 04 2010 Ray Strode <rstrode@redhat.com> 2.32.0-2
- Require orbit at-spi python bindings
http://lists.fedoraproject.org/pipermail/desktop/2010-October/006568.html

* Wed Sep 29 2010 Matthias Clasen <mclasen@redhat.com> - 2.32.0-1
- Update to 2.32.0

* Tue Aug 31 2010 Matthias Clasen <mclasen@redhat.com> - 2.31.91-1
- Update to 2.31.91

* Thu Aug 19 2010 Matthias Clasen <mclasen@redhat.com> - 2.31.90-1
- Update to 2.31.90

* Mon Aug 16 2010 Matthias Clasen <mclasen@redhat.com> - 2.31.6-2
- Curb excessive BRs

* Tue Aug  3 2010 Matthias Clasen <mclasen@redhat.com> - 2.31.6-1
- Update to 2.31.6

* Wed Jul 21 2010 David Malcolm <dmalcolm@redhat.com> - 2.31.5-2
- Rebuilt for https://fedoraproject.org/wiki/Features/Python_2.7/MassRebuild

* Mon Jul 12 2010 Matthias Clasen <mclasen@redhat.com> - 2.31.5-1
- Update to 2.31.5

* Tue Jun 29 2010 Matthias Clasen <mclasen@redhat.com> - 2.31.4-1
- Update to 2.31.4

* Wed Jun 16 2010 Matthias Clasen <mclasen@redhat.com> - 2.31.3-2
- Require pyatspi, not at-spi-python

* Tue Jun  8 2010 Matthias Clasen <mclasen@redhat.com> - 2.31.3-1
- Update to 2.31.3

* Fri May 28 2010 Matthias Clasen <mclasen@redhat.com> - 2.31.2-1
- Update to 2.31.2

* Sat May 15 2010 Matthias Clasen <mclasen@redhat.com> - 2.31.1-1
- Update to 2.31.1

* Tue Apr 27 2010 Matthias Clasen <mclasen@redhat.com> - 2.30.1-1
- Update to 2.30.1

* Mon Mar 29 2010 Matthias Clasen <mclasen@redhat.com> - 2.30.0-1
- Update to 2.30.0

* Wed Mar 10 2010 Matthias Clasen <mclasen@redhat.com> - 2.29.92-1
- Update to 2.29.92

* Sat Feb 20 2010 Matthias Clasen <mclasen@redhat.com> - 2.29.91-1
- Update to 2.29.91

* Wed Feb 10 2010 Bastien Nocera <bnocera@redhat.com> 2.29.90-1
- Update to 2.29.90

* Tue Jan 26 2010 Matthias Clasen <mclasen@redhat.com> - 2.29.6-1
- Update to 2.29.6

* Sun Jan 17 2010 Matthias Clasen <mclasen@redhat.com> - 2.29.5-1
- Update to 2.29.5

* Tue Dec 22 2009 Matthias Clasen <mclasen@redhat.com> - 2.29.4-1
- Update to 2.29.4

* Sat Dec  5 2009 Matthias Clasen <mclasen@redhat.com> - 2.29.2-1
- Update to 2.29.2

* Tue Sep 22 2009 Matthias Clasen <mclasen@redhat.com> - 2.28.0-1
- Update to 2.28.0

* Mon Sep  7 2009 Matthias Clasen <mclasen@redhat.com> - 2.27.92-1
- Update to 2.27.92

* Mon Aug 24 2009 Matthias Clasen <mclasen@redhat.com> - 2.27.91-1
- Update to 2.27.91

* Mon Aug 10 2009 Matthias Clasen <mclasen@redhat.com> - 2.27.90-1
- Update to 2.27.90

* Tue Jul 28 2009 Matthias Clasen <mclasen@redhat.com> - 2.27.5-1
- Update to 2.27.5

* Sat Jul 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.27.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Tue Jul 14 2009 Matthias Clasen <mclasen@redhat.com> - 2.27.4-1
- Update to 2.27.4

* Thu Jun 18 2009 Matthias Clasen <mclasen@redhat.com> - 2.27.3-2
- We don't have debuginfo

* Tue Jun 16 2009 Matthias Clasen <mclasen@redhat.com> - 2.27.3-1
- Update to 2.27.3

* Thu Jun 11 2009 Matthias Clasen <mclasen@redhat.com> - 2.27.2-2
- Add a dependency on gnome-speech (#503193)

* Sun May 31 2009 Matthias Clasen <mclasen@redhat.com> - 2.27.2-1
- Update to 2.27.2

* Mon Apr 13 2009 Matthias Clasen <mclasen@redhat.com> - 2.26.1-1
- Update to 2.26.1
- See http://download.gnome.org/sources/orca/2.26/orca-2.26.1.news

* Mon Mar 16 2009 Matthias Clasen <mclasen@redhat.com> - 2.26.0-1
- Update to 2.26.0

* Mon Mar  2 2009 Matthias Clasen <mclasen@redhat.com> - 2.25.92-1
- Update to 2.25.92

* Thu Feb 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.25.91-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Wed Feb 18 2009 Matthias Clasen <mclasen@redhat.com> - 2.25.91-1
- Update to 2.25.91

* Tue Feb  3 2009 Matthias Clasen <mclasen@redhat.com> - 2.25.90-1
- Update to 2.25.90

* Tue Jan 20 2009 Matthias Clasen <mclasen@redhat.com> - 2.25.5-1
- Update to 2.25.5

* Tue Jan  6 2009 Matthias Clasen <mclasen@redhat.com> - 2.25.4-1
- Update to 2.25.4

* Wed Dec 17 2008 Matthias Clasen <mclasen@redhat.com> - 2.25.3-2
- Update to 2.25.3

* Thu Dec  4 2008 Matthias Clasen <mclasen@redhat.com> - 2.25.2-2
- Rebuild for Python 2.6

* Wed Dec  3 2008 Matthias Clasen <mclasen@redhat.com> - 2.25.2-1
- Update to 2.25.2

* Sat Nov 29 2008 Ignacio Vazquez-Abrams <ivazqueznet+rpm@gmail.com> - 2.25.1-3
- Rebuild for Python 2.6

* Fri Nov 21 2008 Matthias Clasen <mclasen@redhat.com> - 2.25.1-2
- Tweak description

* Wed Nov 12 2008 Matthias Clasen <mclasen@redhat.com> - 2.25.1-1
- Update to 2.25.1

* Fri Oct 17 2008 Matthias Clasen <mclasen@redhat.com> - 2.24.1-1
- Update to 2.24.1

* Mon Sep 22 2008 Matthias Clasen <mclasen@redhat.com> - 2.24.0-1
- Update to 2.24.0

* Mon Sep  8 2008 Matthias Clasen <mclasen@redhat.com> - 2.23.92-1
- Update to 2.23.92

* Tue Sep  2 2008 Matthias Clasen <mclasen@redhat.com> - 2.23.91-1
- Update to 2.23.91

* Tue Aug 26 2008 Matthias Clasen <mclasen@redhat.com> - 2.23.90-2
- Require gnome-python2-gnome

* Sat Aug 23 2008 Matthias Clasen <mclasen@redhat.com> - 2.23.90-1
- Update to 2.23.90

* Tue Aug  5 2008 Matthias Clasen <mclasen@redhat.com> - 2.23.6-1
- Update to 2.23.6

* Tue Jul 22 2008 Matthias Clasen <mclasen@redhat.com> - 2.23.5-1
- Update to 2.23.5

* Wed Jun 18 2008 Matthias Clasen <mclasen@redhat.com> - 2.23.4-1
- Update to 2.23.4

* Tue Jun  3 2008 Matthias Clasen <mclasen@redhat.com> - 2.23.3-1
- Update to  2.23.3

* Wed May 28 2008 Jon McCann <jmccann@redhat.com> - 2.23.2-3
- Add BuildRequires gnome-python2-bonobo back

* Wed May 28 2008 Jon McCann <jmccann@redhat.com> - 2.23.2-2
- Require gnome-python2-bonobo and gnome-python2-libwnck

* Tue May 13 2008 Matthias Clasen <mclasen@redhat.com> - 2.23.2-1
- Update to 2.23.2

* Sun May  4 2008 Matthias Clasen <mclasen@redhat.com> - 2.23.1-2
- Fix source url

* Fri Apr 25 2008 Matthias Clasen <mclasen@redhat.com> - 2.23.1-1
- Update to 2.23.1

* Mon Apr  7 2008 Jon McCann <jmccann@redhat.com> - 2.22.1-2
- Fix signal handling (GNOME bug #525831)

* Mon Apr  7 2008 Matthias Clasen <mclasen@redhat.com> - 2.22.1-1
- Update to 2.22.1

* Mon Mar 10 2008 Matthias Clasen <mclasen@redhat.com> - 2.22.0-1
- Update to 2.22.0

* Mon Feb 25 2008 Matthias Clasen <mclasen@redhat.com> - 2.21.92-1
- Update to 2.21.92

* Tue Feb 12 2008 Matthias Clasen <mclasen@redhat.com> - 2.21.91-1
- Update to 2.21.91

* Tue Jan 29 2008 Matthias Clasen <mclasen@redhat.com> - 2.21.90-1
- Update to 2.21.90

* Mon Jan 14 2008 Matthias Clasen <mclasen@redhat.com> - 2.21.5-1
- Update to 2.21.5

* Fri Jan  4 2008 Matthias Clasen <mclasen@redhat.com> - 2.21.4-2
- Require at-spi-python (#427432)

* Tue Dec 18 2007 Matthias Clasen <mclasen@redhat.com> - 2.21.4-1
- Update to 2.21.4

* Wed Dec  5 2007 Matthias Clasen <mclasen@redhat.com> - 2.21.3-1
- Update to 2.21.3

* Tue Nov 13 2007 Matthias Clasen <mclasen@redhat.com> - 2.21.2-1
- Update to 2.21.2

* Mon Oct 15 2007 Matthias Clasen <mclasen@redhat.com> - 2.20.0.1-1
- Update to 2.20.0.1 (bug fixes and translation updates)

* Sun Sep 16 2007 Matthias Clasen <mclasen@redhat.com> - 2.20.0-1
- Update to 2.20.0

* Tue Sep  4 2007 Matthias Clasen <mclasen@redhat.com> - 2.19.92-1
- Update to 2.19.92

* Mon Aug 13 2007 Matthias Clasen <mclasen@redhat.com> - 2.19.90-1
- Update to 2.19.90

* Tue Aug  7 2007 Matthias Clasen <mclasen@redhat.com> - 2.19.6-2
- Update license field

* Sun Jul 29 2007 Matthias Clasen <mclasen@redhat.com> - 2.19.6-1
- Update to 2.19.6

* Mon Jul  9 2007 Matthias Clasen <mclasen@redhat.com> - 2.19.5-1
- Update to 2.19.5

* Sun Jun 17 2007 Matthias Clasen <mclasen@redhat.com> - 2.19.4-1
- Update to 2.19.4

* Tue Jun  5 2007 Matthias Clasen <mclasen@redhat.com> - 2.19.3-1
- Update to 2.19.3

* Sun May 20 2007 Matthias Clasen <mclasen@redhat.com> - 2.19.2-1
- Update to 2.19.2

* Tue Mar 13 2007 Matthias Clasen <mclasen@redhat.com> - 2.18.0-1
- Update to 2.18.0

* Wed Feb 28 2007 Matthias Clasen <mclasen@redhat.com> - 2.17.92-1
- Update to 2.17.92

* Sun Feb 11 2007 Matthias Clasen <mclasen@redhat.com> - 2.17.91-1
- Update to 2.17.91

* Mon Jan 22 2007 Matthias Clasen <mclasen@redhat.com> - 2.17.90-1
- Update to 2.17.90

* Thu Jan 11 2007 Matthias Clasen <mclasen@redhat.com> - 2.17.5-1
- Update to orca 2.17.5

* Tue Dec 19 2006 Matthias Clasen <mclasen@redhat.com> - 2.17.4-1
- Update to orca 2.17.4

* Thu Dec  7 2006 Jeremy Katz <katzj@redhat.com> - 2.17.3-2
- rebuild for python 2.5

* Tue Dec  5 2006 Matthias Clasen <mclasen@redhat.com> - 2.17.3-1
- Update to orca 2.17.3

* Tue Nov  7 2006 Matthias Clasen <mclasen@redhat.com> - 2.17.2-1
- Update to orca 2.17.2

* Tue Nov  7 2006 Matthias Clasen <mclasen@redhat.com> - 2.17.1-2
- Fix typos in the spec

* Sat Oct 21 2006 Matthias Clasen <mclasen@redhat.com> - 2.17.1-1
- Update to 2.17.1

*  Sun Oct 01 2006 Jesse Keating <jkeating@redhat.com> - 1.0.0-4
- rebuilt for unwind info generation, broken in gcc-4.1.1-21

* Tue Sep 19 2006 John (J5) Palmieri <johnp@redhat.com> - 1.0.0-3
- Add patch to shutdown orca

* Tue Sep 19 2006 John (J5) Palmieri <johnp@redhat.com> - 1.0.0-2
- Add requirements on gnome-mag and newer version of control-center
- remove .desktop file and make control-center start and configure orca

* Sun Sep  3 2006 Matthias Clasen <mclasen@redhat.com> - 1.0.0-1
- Update to 1.0.0

* Thu Aug 31 2006 Matthias Clasen <mclasen@redhat.com> - 0.9.0-4
- Obsolete gnome-mag-devel, too

* Tue Aug 29 2006 John (J5) Palmieri <johnp@redhat.com> - 0.9.0-3
- Spec file cleanups

* Mon Aug 21 2006 John (J5) Palmieri <johnp@redhat.com> - 0.9.0-1
- Initial package
