%global tarball_version %%(echo %{version} | tr '~' '.')
%global major_version %%(echo %%{tarball_version} | awk -F. '{print $1}')

Name:           gnome-font-viewer
Version:        47.0
Release:        2%{?dist}
Summary:        Utility for previewing fonts for GNOME

License:        GPL-2.0-or-later AND CC0-1.0
URL:            https://gitlab.gnome.org/GNOME/gnome-font-viewer
Source0:        https://download.gnome.org/sources/gnome-font-viewer/%{major_version}/%{name}-%{tarball_version}.tar.xz

BuildRequires:  gcc
BuildRequires:  gettext
BuildRequires:  meson
BuildRequires:  pkgconfig(fontconfig)
BuildRequires:  pkgconfig(freetype2)
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(gnome-desktop-4)
BuildRequires:  pkgconfig(gtk4)
BuildRequires:  pkgconfig(harfbuzz)
BuildRequires:  pkgconfig(libadwaita-1)
BuildRequires:  /usr/bin/appstream-util
BuildRequires:  /usr/bin/desktop-file-validate

%description
Use gnome-font-viewer, the Font Viewer, to preview fonts and display
information about a specified font. You can use the Font Viewer to display the
name, style, type, size, version and copyright of the font.

%prep
%autosetup -p1 -n %{name}-%{tarball_version}

%build
%meson
%meson_build

%install
%meson_install

%find_lang %{name} --with-gnome

%check
desktop-file-validate %{buildroot}%{_datadir}/applications/org.gnome.font-viewer.desktop
appstream-util validate-relax --nonet %{buildroot}%{_metainfodir}/org.gnome.font-viewer.appdata.xml

%files -f %{name}.lang
%license COPYING
%doc NEWS
%{_bindir}/%{name}
%{_bindir}/gnome-thumbnail-font
%{_datadir}/applications/org.gnome.font-viewer.desktop
%{_datadir}/dbus-1/services/org.gnome.font-viewer.service
%{_datadir}/icons/hicolor/scalable/apps/org.gnome.font-viewer.svg
%{_datadir}/icons/hicolor/symbolic/apps/org.gnome.font-viewer-symbolic.svg
%{_datadir}/thumbnailers/%{name}.thumbnailer
%{_metainfodir}/org.gnome.font-viewer.appdata.xml

%changelog
* Thu Jan 16 2025 Fedora Release Engineering <releng@fedoraproject.org> - 47.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Wed Sep 18 2024 nmontero <nmontero@redhat.com> - 47.0-1
- Update to 47.0

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 47~alpha-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Fri Jul 12 2024 David King <amigadave@amigadave.com> - 47~alpha-1
- Update to 47.alpha

* Fri Mar 22 2024 David King <amigadave@amigadave.com> - 46.0-1
- Update to 46.0

* Wed Jan 24 2024 Fedora Release Engineering <releng@fedoraproject.org> - 45.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Florian Weimer <fweimer@redhat.com> - 45.0-3
- Fix C89 compatibility issue

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 45.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Sep 20 2023 Kalev Lember <klember@redhat.com> - 45.0-1
- Update to 45.0

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 45~alpha-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Tue Jul 04 2023 Kalev Lember <klember@redhat.com> - 45~alpha-1
- Update to 45.alpha

* Tue Mar 21 2023 David King <amigadave@amigadave.com> - 44.0-1
- Update to 44.0

* Mon Mar 06 2023 David King <amigadave@amigadave.com> - 44~rc-1
- Update to 44.rc

* Thu Feb 16 2023 David King <amigadave@amigadave.com> - 44~beta-1
- Update to 44.beta

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 43.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Tue Sep 20 2022 Kalev Lember <klember@redhat.com> - 43.0-1
- Update to 43.0

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

* Mon Feb 14 2022 David King <amigadave@amigadave.com> - 42~beta-1
- Update to 42.beta

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 42~alpha-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Jan 12 2022 David King <amigadave@amigadave.com> - 42~alpha-1
- Update to 42.alpha

* Tue Sep 21 2021 Kalev Lember <klember@redhat.com> - 41.0-1
- Update to 41.0

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 40.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Mon Mar 22 2021 Kalev Lember <klember@redhat.com> - 40.0-1
- Update to 40.0

* Thu Feb 18 2021 Kalev Lember <klember@redhat.com> - 40~beta-1
- Update to 40.beta
- Update upstream URLs

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 3.34.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.34.0-5
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.34.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.34.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jan 16 2020 Kalev Lember <klember@redhat.com> - 3.34.0-2
- Rebuilt for libgnome-desktop soname bump

* Sun Sep 15 2019 Kalev Lember <klember@redhat.com> - 3.34.0-1
- Update to 3.34.0

* Tue Aug 20 2019 Kalev Lember <klember@redhat.com> - 3.33.90-1
- Update to 3.33.90

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.33.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Jul 21 2019 Kalev Lember <klember@redhat.com> - 3.33.4-2
- Rebuilt for libgnome-desktop soname bump

* Fri Jul 19 2019 Kalev Lember <klember@redhat.com> - 3.33.4-1
- Update to 3.33.4

* Fri Mar 15 2019 Kalev Lember <klember@redhat.com> - 3.32.0-1
- Update to 3.32.0

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.30.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Sep 06 2018 Kalev Lember <klember@redhat.com> - 3.30.0-1
- Update to 3.30.0

* Tue Jul 31 2018 Florian Weimer <fweimer@redhat.com> - 3.28.0-3
- Rebuild with fixed binutils

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.28.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Mar 13 2018 Kalev Lember <klember@redhat.com> - 3.28.0-1
- Update to 3.28.0

* Mon Mar 05 2018 Kalev Lember <klember@redhat.com> - 3.27.90-1
- Update to 3.27.90

* Tue Feb 13 2018 Björn Esser <besser82@fedoraproject.org> - 3.26.0-3
- Rebuild against newer gnome-desktop3 package

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.26.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Mon Sep 18 2017 Kalev Lember <klember@redhat.com> - 3.26.0-1
- Update to 3.26.0

* Tue Aug 15 2017 Kalev Lember <klember@redhat.com> - 3.25.90-1
- Update to 3.25.90
- Switch to the meson build system

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.24.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.24.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sun May 21 2017 Michael Catanzaro <mcatanzaro@gnome.org> - 3.24.0-2
- Fix crash on startup
- Remove custom appstream screenshots

* Tue May 09 2017 Kalev Lember <klember@redhat.com> - 3.24.0-1
- Update to 3.24.0

* Mon Mar 06 2017 Kalev Lember <klember@redhat.com> - 3.23.91-1
- Update to 3.23.91

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.22.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Sep 22 2016 Kalev Lember <klember@redhat.com> - 3.22.0-1
- Update to 3.22.0
- Don't set group tags
- Use make_install macro

* Thu May 12 2016 Kalev Lember <klember@redhat.com> - 3.20.2-1
- Update to 3.20.2

* Wed Mar 30 2016 Kalev Lember <klember@redhat.com> - 3.20.0-1
- Update to 3.20.0

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 3.16.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jul 22 2015 David King <amigadave@amigadave.com> - 3.16.2-3
- Bump for new gnome-desktop3

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.16.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Wed May 13 2015 Kalev Lember <kalevlember@gmail.com> - 3.16.2-1
- Update to 3.16.2
- Use license macro for the COPYING file

* Mon Mar 30 2015 Richard Hughes <rhughes@redhat.com> - 3.16.0-2
- Use better AppData screenshots

* Tue Mar 24 2015 Kalev Lember <kalevlember@gmail.com> - 3.16.0-1
- Update to 3.16.0

* Thu Feb 19 2015 Richard Hughes <rhughes@redhat.com> - 3.15.90-1
- Update to 3.15.90

* Tue Sep 23 2014 Kalev Lember <kalevlember@gmail.com> - 3.14.0-1
- Update to 3.14.0

* Thu Aug 21 2014 Kalev Lember <kalevlember@gmail.com> - 3.13.90-1
- Update to 3.13.90

* Sat Aug 16 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.12.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.12.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Wed Mar 26 2014 Richard Hughes <rhughes@redhat.com> - 3.12.0-1
- Update to 3.12.0

* Wed Feb 19 2014 Richard Hughes <rhughes@redhat.com> - 3.10.0-2
- Rebuild for gnome-desktop soname bump

* Wed Sep 25 2013 Richard Hughes <rhughes@redhat.com> - 3.10.0-1
- Update to 3.10.0

* Tue Sep 03 2013 Kalev Lember <kalevlember@gmail.com> - 3.9.90-2
- Rebuilt for libgnome-desktop soname bump

* Thu Aug 22 2013 Kalev Lember <kalevlember@gmail.com> - 3.9.90-1
- Update to 3.9.90

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.8.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Tue Mar 26 2013 Kalev Lember <kalevlember@gmail.com> - 3.8.0-1
- Update to 3.8.0

* Thu Mar  7 2013 Matthias Clasen <mclasen@redhat.com> - 3.7.91-1
- Update to 3.7.91

* Wed Feb 20 2013 Kalev Lember <kalevlember@gmail.com> - 3.7.5-2
- Rebuilt for libgnome-desktop soname bump

* Thu Feb 07 2013 Kalev Lember <kalevlember@gmail.com> - 3.7.5-1
- Update to 3.7.5

* Wed Jan 16 2013 Matthias Clasen <mclasen@redhat.com> - 3.7.4-1
- Update to 3.7.4

* Fri Dec 21 2012 Kalev Lember <kalevlember@gmail.com> - 3.7.3-1
- Update to 3.7.3

* Thu Dec  6 2012 Rui Matos <rmatos@redhat.com> - 3.6.2-1
- Update to 3.6.2

* Tue Nov 13 2012 Kalev Lember <kalevlember@gmail.com> - 3.6.1-1
- Update to 3.6.1

* Tue Sep 25 2012 Matthias Clasen <mclasen@redhat.com> - 3.6.0-1
- Update to 3.6.0

* Wed Sep 19 2012 Kalev Lember <kalevlember@gmail.com> - 3.5.92-1
- Update to 3.5.92

* Wed Jul 18 2012 Kalev Lember <kalevlember@gmail.com> - 3.5.4-1
- Update to 3.5.4

* Thu Jun 28 2012 Kalev Lember <kalevlember@gmail.com> - 3.5.3-1
- Update to 3.5.3

* Fri Jun  8 2012 Matthias Clasen <mclasen@redhat.com> - 3.5.2-1
- Update to 3.5.2

* Sat May 05 2012 Kalev Lember <kalevlember@gmail.com> - 3.5.1-1
- Update to 3.5.1

* Wed Mar 28 2012 Rui Matos <rmatos@redhat.com> - 3.4.0-3
- Use %%global instead of %%define
- Don't define Version as the result of macro expansions so that we
  don't break automated tools

* Wed Mar 28 2012 Rui Matos <rmatos@redhat.com> - 3.4.0-2
- Use rpm macros to define the version number
- Do verbose builds

* Tue Mar 27 2012 Rui Matos <rmatos@redhat.com> - 3.4.0-1
- Update to 3.4.0

* Mon Mar  5 2012 Rui Matos <rmatos@redhat.com> - 3.3.2.1-3
- spec file cleanup
- removed unneeded GConf2-devel BR
- call update-desktop-database to rebuild the MIME types cache

* Tue Dec 06 2011 Anuj More <anujmorex@gmail.com> - 3.3.2.1-2
- made some formating changes in the spec file

* Fri Nov 18 2011 Anuj More <anujmorex@gmail.com> - 3.3.2.1-1
- rebuilt

