%global gobject_introspection_version 1.35.9
%global gtk4_version 4.5.0
%global pygobject_version 3.36.1
%global tracker_sparql_version 2.99.3
%global grilo_version 0.3.13

%global tarball_version %%(echo %{version} | tr '~' '.')

Name:          gnome-music
Summary:       Music player and management application for GNOME
Version:       44~beta
Release:       1%{?dist}

# The sources are under the GPLv2+ license, except for:
# - the gnome-music icon which is CC-BY-SA
#
# Also: https://bugzilla.gnome.org/show_bug.cgi?id=706457
License:       (GPLv2+ with exceptions) and CC-BY-SA
URL:           https://wiki.gnome.org/Apps/Music
Source0:       https://download.gnome.org/sources/%{name}/44/%{name}-%{tarball_version}.tar.xz

BuildArch:     noarch
BuildRequires: /usr/bin/appstream-util
BuildRequires: desktop-file-utils
BuildRequires: gettext
BuildRequires: itstool
BuildRequires: meson
BuildRequires: pkgconfig(gio-2.0)
BuildRequires: pkgconfig(goa-1.0)
BuildRequires: pkgconfig(gobject-introspection-1.0) >= %{gobject_introspection_version}
BuildRequires: pkgconfig(grilo-0.3) >= %{grilo_version}
BuildRequires: pkgconfig(grilo-plugins-0.3)
BuildRequires: pkgconfig(gtk4) >= %{gtk4_version}
BuildRequires: pkgconfig(libadwaita-1)
BuildRequires: pkgconfig(libmediaart-2.0)
BuildRequires: pkgconfig(libsoup-3.0)
BuildRequires: pkgconfig(py3cairo)
BuildRequires: pkgconfig(pygobject-3.0) >= %{pygobject_version}
BuildRequires: pkgconfig(tracker-sparql-3.0) >= %{tracker_sparql_version}
BuildRequires: python3-devel

Requires:      gdk-pixbuf2
Requires:      gnome-online-accounts
Requires:      gobject-introspection >= %{gobject_introspection_version}
Requires:      grilo >= %{grilo_version}
Requires:      grilo-plugins
Requires:      gstreamer1
Requires:      gstreamer1-plugins-base
Requires:      gtk4 >= %{gtk4_version}
Requires:      libmediaart
Requires:      libnotify >= 0.7.6
Requires:      libsoup
Requires:      libtracker-sparql3 >= %{tracker_sparql_version}
Requires:      pango
Requires:      python3-cairo
Requires:      python3-gobject >= %{pygobject_version}

%description
Music player and management application for GNOME.


%prep
%autosetup -p1 -n %{name}-%{tarball_version}


%build
%meson
%meson_build


%install
%meson_install
%find_lang %{name} --with-gnome --all-name


%check
appstream-util validate-relax --nonet %{buildroot}%{_datadir}/metainfo/org.gnome.Music.appdata.xml
desktop-file-validate %{buildroot}%{_datadir}/applications/org.gnome.Music.desktop


%files -f %{name}.lang
%license LICENSE
%doc NEWS README.md
%{_bindir}/gnome-music
%{_datadir}/applications/org.gnome.Music.desktop
%{_datadir}/glib-2.0/schemas/org.gnome.Music.gschema.xml
%{_datadir}/org.gnome.Music/
%{_datadir}/icons/hicolor/scalable/apps/org.gnome.Music.svg
%{_datadir}/icons/hicolor/symbolic/apps/org.gnome.Music-symbolic.svg
%{_metainfodir}/org.gnome.Music.appdata.xml
%{python3_sitelib}/gnomemusic


%changelog
* Thu Feb 16 2023 David King <amigadave@amigadave.com> - 44~beta-1
- Update to 44.beta

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 42.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 42.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon Jun 13 2022 Python Maint <python-maint@redhat.com> - 42.1-2
- Rebuilt for Python 3.11

* Mon Apr 25 2022 David King <amigadave@amigadave.com> - 42.1-1
- Update to 42.1

* Sun Mar 20 2022 David King <amigadave@amigadave.com> - 42.0-1
- Update to 42.0

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 41.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Mon Sep 20 2021 Kalev Lember <klember@redhat.com> - 41.0-1
- Update to 41.0

* Wed Sep 08 2021 Kalev Lember <klember@redhat.com> - 41~rc-1
- Update to 41.rc

* Mon Aug 16 2021 Kalev Lember <klember@redhat.com> - 41~beta-1
- Update to 41.beta

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 40.1.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Mon Jun 21 2021 Kalev Lember <klember@redhat.com> - 40.1.1-1
- Update to 40.1.1

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 40.0-2
- Rebuilt for Python 3.10

* Mon Mar 22 2021 Kalev Lember <klember@redhat.com> - 40.0-1
- Update to 40.0
- Improve private library filtering

* Tue Mar 16 2021 Kalev Lember <klember@redhat.com> - 40~rc-1
- Update to 40.rc
- Use https upstream URL

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 3.38.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Nov 25 2020 Kalev Lember <klember@redhat.com> - 3.38.2-1
- Update to 3.38.2

* Mon Oct  5 2020 Kalev Lember <klember@redhat.com> - 3.38.1-1
- Update to 3.38.1

* Mon Sep 14 2020 Kalev Lember <klember@redhat.com> - 3.38.0-1
- Update to 3.38.0

* Wed Sep 09 2020 Kalev Lember <klember@redhat.com> - 3.37.92-1
- Update to 3.37.92
- Switch to tracker3

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.37.3-3
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.37.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Jul 20 2020 Kalev Lember <klember@redhat.com> - 3.37.3-1
- Update to 3.37.3

* Thu Jun 04 2020 Kalev Lember <klember@redhat.com> - 3.37.2-1
- Update to 3.37.2

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 3.36.2-2
- Rebuilt for Python 3.9

* Sat Apr 25 2020 Kalev Lember <klember@redhat.com> - 3.36.2-1
- Update to 3.36.2

* Sun Mar 29 2020 Kalev Lember <klember@redhat.com> - 3.36.1-1
- Update to 3.36.1

* Sat Mar 07 2020 Kalev Lember <klember@redhat.com> - 3.36.0-1
- Update to 3.36.0

* Tue Mar 03 2020 Kalev Lember <klember@redhat.com> - 3.35.92-1
- Update to 3.35.92

* Tue Feb 18 2020 Kalev Lember <klember@redhat.com> - 3.35.91.1-1
- Update to 3.35.91.1

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.35.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Tue Jan 07 2020 Kalev Lember <klember@redhat.com> - 3.35.3-1
- Update to 3.35.3

* Mon Dec 02 2019 Kalev Lember <klember@redhat.com> - 3.35.2-1
- Update to 3.35.2

* Thu Nov 28 2019 Kalev Lember <klember@redhat.com> - 3.34.2-2
- Update versioned dependencies
- Hard-require libtracker-sparql instead of tracker daemon
- Drop requires on python3-dbus as gnome-music now uses gdbus instead

* Wed Nov 27 2019 Kalev Lember <klember@redhat.com> - 3.34.2-1
- Update to 3.34.2

* Sat Oct 26 2019 Kalev Lember <klember@redhat.com> - 3.34.1-1
- Update to 3.34.1

* Tue Sep 10 2019 Kalev Lember <klember@redhat.com> - 3.34.0-1
- Update to 3.34.0

* Wed Sep 04 2019 Kalev Lember <klember@redhat.com> - 3.33.92-1
- Update to 3.33.92

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 3.33.90-2
- Rebuilt for Python 3.8

* Mon Aug 12 2019 Kalev Lember <klember@redhat.com> - 3.33.90-1
- Update to 3.33.90

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.33.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Jul 19 2019 Kalev Lember <klember@redhat.com> - 3.33.4-1
- Update to 3.33.4

* Tue May 21 2019 Kalev Lember <klember@redhat.com> - 3.33.2-1
- Update to 3.33.2

* Mon May 06 2019 Kalev Lember <klember@redhat.com> - 3.32.2-1
- Update to 3.32.2

* Tue Apr 16 2019 Adam Williamson <awilliam@redhat.com> - 3.32.1-2
- Rebuild with Meson fix for #1699099

* Tue Apr 09 2019 Kalev Lember <klember@redhat.com> - 3.32.1-1
- Update to 3.32.1

* Tue Mar 12 2019 Kalev Lember <klember@redhat.com> - 3.32.0-1
- Update to 3.32.0

* Tue Mar 05 2019 Kalev Lember <klember@redhat.com> - 3.31.92-1
- Update to 3.31.92

* Tue Feb 19 2019 Kalev Lember <klember@redhat.com> - 3.31.91-1
- Update to 3.31.91

* Sat Feb 09 2019 Phil Wyett <philwyett@kathenas.org> - 3.31.90-1
- Update to 3.31.90-1

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.30.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Oct 26 2018 Kalev Lember <klember@redhat.com> - 3.30.2-1
- Update to 3.30.2

* Sat Sep 29 2018 Kalev Lember <klember@redhat.com> - 3.30.1-1
- Update to 3.30.1

* Fri Sep 07 2018 Kalev Lember <klember@redhat.com> - 3.30.0-1
- Update to 3.30.0

* Mon Aug 13 2018 Kalev Lember <klember@redhat.com> - 3.29.90-1
- Update to 3.29.90

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.28.2.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 3.28.2.1-2
- Rebuilt for Python 3.7

* Tue May 08 2018 Kalev Lember <klember@redhat.com> - 3.28.2.1-1
- Update to 3.28.2.1

* Mon Apr 09 2018 Kalev Lember <klember@redhat.com> - 3.28.1-1
- Update to 3.28.1

* Mon Mar 19 2018 Kalev Lember <klember@redhat.com> - 3.28.0.1-1
- Update to 3.28.0.1

* Mon Mar 12 2018 Kalev Lember <klember@redhat.com> - 3.28.0-1
- Update to 3.28.0

* Mon Mar 05 2018 Kalev Lember <klember@redhat.com> - 3.27.92.1-1
- Update to 3.27.92.1
- Switch to the meson build system

* Wed Feb 07 2018 Kalev Lember <klember@redhat.com> - 3.26.2-1
- Update to 3.26.2

* Fri Jan 05 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 3.26.1-2
- Remove obsolete scriptlets

* Sun Oct 08 2017 Kalev Lember <klember@redhat.com> - 3.26.1-1
- Update to 3.26.1

* Mon Sep 11 2017 Kalev Lember <klember@redhat.com> - 3.26.0-1
- Update to 3.26.0

* Thu Sep 07 2017 Kalev Lember <klember@redhat.com> - 3.25.92-1
- Update to 3.25.92

* Fri Aug 25 2017 Kalev Lember <klember@redhat.com> - 3.25.91-1
- Update to 3.25.91

* Tue Aug 15 2017 Kalev Lember <klember@redhat.com> - 3.25.90-1
- Update to 3.25.90

* Mon Jul 31 2017 Kalev Lember <klember@redhat.com> - 3.25.4-1
- Update to 3.25.4

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.24.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Wed May 10 2017 Kalev Lember <klember@redhat.com> - 3.24.2-1
- Update to 3.24.2

* Tue Apr 11 2017 Kalev Lember <klember@redhat.com> - 3.24.1.1-1
- Update to 3.24.1.1

* Tue Mar 21 2017 Kalev Lember <klember@redhat.com> - 3.24.0-1
- Update to 3.24.0

* Thu Mar 16 2017 Kalev Lember <klember@redhat.com> - 3.23.92-1
- Update to 3.23.92

* Tue Feb 28 2017 Richard Hughes <rhughes@redhat.com> - 3.23.91-1
- Update to 3.23.91

* Tue Feb 14 2017 Richard Hughes <rhughes@redhat.com> - 3.23.90-1
- Update to 3.23.90

* Mon Feb 13 2017 Richard Hughes <rhughes@redhat.com> - 3.23.4-1
- Update to 3.23.4

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.23.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Dec 19 2016 Miro Hrončok <mhroncok@redhat.com> - 3.23.2-2
- Rebuild for Python 3.6

* Thu Dec 01 2016 Kalev Lember <klember@redhat.com> - 3.23.2-1
- Update to 3.23.2

* Fri Nov 04 2016 Kalev Lember <klember@redhat.com> - 3.23.1-1
- Update to 3.23.1

* Wed Oct 12 2016 Kalev Lember <klember@redhat.com> - 3.22.1-1
- Update to 3.22.1

* Mon Sep 19 2016 Kalev Lember <klember@redhat.com> - 3.22.0-1
- Update to 3.22.0

* Wed Sep 14 2016 Kalev Lember <klember@redhat.com> - 3.21.92-1
- Update to 3.21.92

* Tue Aug 23 2016 Kalev Lember <klember@redhat.com> - 3.21.90-1
- Update to 3.21.90

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.20.2-3
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Mon May 16 2016 Kalev Lember <klember@redhat.com> - 3.20.2-2
- Add missing gnome-online-accounts and python3-requests deps (#1336317)

* Tue May 10 2016 Kalev Lember <klember@redhat.com> - 3.20.2-1
- Update to 3.20.2

* Tue Mar 22 2016 Kalev Lember <klember@redhat.com> - 3.20.0-1
- Update to 3.20.0

* Wed Mar 16 2016 Kalev Lember <klember@redhat.com> - 3.19.92-1
- Update to 3.19.92

* Fri Mar 04 2016 Richard Hughes <rhughes@redhat.com> - 3.19.91-1
- Update to 3.19.91

* Tue Feb 16 2016 Richard Hughes <rhughes@redhat.com> - 3.19.90-1
- Update to 3.19.90

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 3.19.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jan 20 2016 Kalev Lember <klember@redhat.com> - 3.19.4-1
- Update to 3.19.4

* Sun Dec 27 2015 Michael Catanzaro <mcatanzaro@gnome.org> - 3.18.2-4
- Add more grilo 0.3 patches

* Sat Dec 26 2015 Michael Catanzaro <mcatanzaro@gnome.org> - 3.18.2-3
- Add symbolic icon

* Fri Dec 18 2015 Kalev Lember <klember@redhat.com> - 3.18.2-2
- Build with grilo 0.3

* Mon Nov 16 2015 Kalev Lember <klember@redhat.com> - 3.18.2-1
- Update to 3.18.2

* Tue Nov 10 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.18.0-2
- Rebuilt for https://fedoraproject.org/wiki/Changes/python3.5

* Tue Sep 22 2015 Kalev Lember <klember@redhat.com> - 3.18.0-1
- Update to 3.18.0

* Mon Sep 14 2015 Kalev Lember <klember@redhat.com> - 3.17.92-1
- Update to 3.17.92

* Tue Sep 01 2015 Kalev Lember <klember@redhat.com> - 3.17.91-1
- Update to 3.17.91

* Tue Aug 18 2015 Kalev Lember <klember@redhat.com> - 3.17.90-1
- Update to 3.17.90
- Use make_install macro

* Mon Jul 20 2015 David King <amigadave@amigadave.com> - 3.17.4-1
- Update to 3.17.4

* Wed Jun 24 2015 David King <amigadave@amigadave.com> - 3.17.3-1
- Update to 3.17.3

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.16.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Tue Apr 14 2015 Kalev Lember <kalevlember@gmail.com> - 3.16.1-1
- Update to 3.16.1

* Mon Mar 23 2015 Kalev Lember <kalevlember@gmail.com> - 3.16.0-1
- Update to 3.16.0

* Mon Mar 16 2015 Kalev Lember <kalevlember@gmail.com> - 3.15.92-1
- Update to 3.15.92

* Tue Mar 03 2015 Kalev Lember <kalevlember@gmail.com> - 3.15.91-1
- Update to 3.15.91

* Mon Feb 16 2015 David King <amigadave@amigadave.com> - 3.15.90-1
- Update to 3.15.90
- Use license macro for COPYING

* Tue Jan 27 2015 David King <amigadave@amigadave.com> - 3.15.4-1
- Update to 3.15.4
- Update man page glob in files section
- Validate AppData during check

* Tue Nov 25 2014 Kalev Lember <kalevlember@gmail.com> - 3.15.2-1
- Update to 3.15.2

* Wed Nov 12 2014 Kalev Lember <kalevlember@gmail.com> - 3.14.2-1
- Update to 3.14.2

* Mon Oct 13 2014 Kalev Lember <kalevlember@gmail.com> - 3.14.1-1
- Update to 3.14.1

* Mon Sep 22 2014 Kalev Lember <kalevlember@gmail.com> - 3.14.0-1
- Update to 3.14.0

* Mon Sep 15 2014 Kalev Lember <kalevlember@gmail.com> - 3.13.92-1
- Update to 3.13.92

* Tue Aug 19 2014 Kalev Lember <kalevlember@gmail.com> - 3.13.90-1
- Update to 3.13.90
- Include HighContrast icons

* Sat Aug 16 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.13.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Tue Jul 22 2014 Kalev Lember <kalevlember@gmail.com> - 3.13.4-1
- Update to 3.13.4

* Tue Jul 22 2014 Kalev Lember <kalevlember@gmail.com> - 3.13.3-2
- Rebuilt for gobject-introspection 1.41.4

* Tue Jun 24 2014 Richard Hughes <rhughes@redhat.com> - 3.13.3-1
- Update to 3.13.3

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.13.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Tue May 27 2014 Kalev Lember <kalevlember@gmail.com> - 3.13.2-2
- Rebuilt for https://fedoraproject.org/wiki/Changes/Python_3.4

* Tue May 27 2014 Kalev Lember <kalevlember@gmail.com> - 3.13.2-1
- Update to 3.13.2

* Mon Apr 28 2014 Richard Hughes <rhughes@redhat.com> - 3.13.1-1
- Update to 3.13.1

* Tue Apr 15 2014 Kalev Lember <kalevlember@gmail.com> - 3.12.1-1
- Update to 3.12.1

* Mon Mar 24 2014 Richard Hughes <rhughes@redhat.com> - 3.12.0-1
- Update to 3.12.0

* Tue Mar 18 2014 Richard Hughes <rhughes@redhat.com> - 3.11.92-1
- Update to 3.11.92

* Wed Mar 05 2014 Mathieu Bridon <bochecha@fedoraproject.org> - 3.11.91-2
- Fix handling of the help files.

* Tue Mar 04 2014 Richard Hughes <rhughes@redhat.com> - 3.11.91-1
- Update to 3.11.91

* Mon Feb 17 2014 Richard Hughes <rhughes@redhat.com> - 3.11.90-1
- Update to 3.11.90

* Mon Nov 25 2013 Richard Hughes <rhughes@redhat.com> - 3.11.2-1
- Update to 3.11.2

* Tue Oct 29 2013 Richard Hughes <rhughes@redhat.com> - 3.10.1-1
- Update to 3.10.1

* Wed Sep 25 2013 Kalev Lember <kalevlember@gmail.com> - 3.10.0-1
- Update to 3.10.0

* Wed Sep 18 2013 Kalev Lember <kalevlember@gmail.com> - 3.9.92-1
- Update to 3.9.92
- Include the appdata file

* Tue Sep 03 2013 Kalev Lember <kalevlember@gmail.com> - 3.9.91-1
- Update to 3.9.91

* Wed Aug 21 2013 Mathieu Bridon <bochecha@fedoraproject.org> - 3.9.90-2
- A couple of fixes, based on Ankur's feedback:
  - Fix the upstream URL
  - Fix the license tag
  - Validate the desktop file
  - Make the build verbose

* Wed Aug 21 2013 Mathieu Bridon <bochecha@fedoraproject.org> - 3.9.90-1
- Initial package for Fedora.
