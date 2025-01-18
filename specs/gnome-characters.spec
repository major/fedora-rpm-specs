%global appname org.gnome.Characters

%global gjs_version 1.50
%global gtk4_version 4.6
%global libadwaita_version 1.5~alpha

%global tarball_version %%(echo %{version} | tr '~' '.')

Name:		gnome-characters
Version:	47.0
Release:	2%{?dist}
Summary:	Character map application for GNOME
# Files from gtk-js-app are licensed under 3-clause BSD.
# Other files are GPL 2.0 or later.
License:	BSD-3-Clause AND GPL-2.0-or-later
URL:		https://wiki.gnome.org/Design/Apps/CharacterMap
Source0:	https://download.gnome.org/sources/%{name}/47/%{name}-%{tarball_version}.tar.xz

BuildRequires:	desktop-file-utils
BuildRequires:	gettext
BuildRequires:	gobject-introspection-devel
BuildRequires:	libappstream-glib
BuildRequires:	libunistring-devel
BuildRequires:	meson
BuildRequires:	pkgconfig(gjs-1.0) >= %{gjs_version}
BuildRequires:	pkgconfig(gtk4) >= %{gtk4_version}
BuildRequires:	pkgconfig(libadwaita-1) >= %{libadwaita_version}

Requires:	gjs >= %{gjs_version}
Requires:	gnome-desktop4%{_isa}
Requires:	gtk4%{_isa} >= %{gtk4_version}
Requires:	libadwaita%{?_isa} >= %{libadwaita_version}

%description
Characters is a simple utility application to find and insert unusual
characters.


%prep
%autosetup -p1 -n %{name}-%{tarball_version}


%build
%meson
%meson_build


%install
%meson_install
%find_lang %{appname}


%check
desktop-file-validate $RPM_BUILD_ROOT/%{_datadir}/applications/%{appname}.desktop


%files -f %{appname}.lang
%doc NEWS README.md
%license COPYING COPYINGv2
%{_bindir}/%{name}
%{_datadir}/applications/%{appname}.desktop
%{_datadir}/dbus-1/services/%{appname}.service
%{_datadir}/glib-2.0/schemas/%{appname}.gschema.xml
%{_datadir}/%{appname}
%{_datadir}/gnome-shell/search-providers/%{appname}.search-provider.ini
%{_datadir}/icons/hicolor/scalable/apps/%{appname}.svg
%{_datadir}/icons/hicolor/symbolic/apps/%{appname}-symbolic.svg
%{_metainfodir}/%{appname}.appdata.xml
%{_libdir}/%{appname}


%changelog
* Thu Jan 16 2025 Fedora Release Engineering <releng@fedoraproject.org> - 47.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Wed Sep 18 2024 nmontero <nmontero@redhat.com> - 47.0-1
- Update to 47.0

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 47~alpha-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Mon Jul 15 2024 David King <amigadave@amigadave.com> - 47~alpha-1
- Update to 47.alpha

* Wed Mar 20 2024 David King <amigadave@amigadave.com> - 46.0-1
- Update to 46.0

* Wed Jan 24 2024 Fedora Release Engineering <releng@fedoraproject.org> - 45.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 45.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Tue Sep 19 2023 Kalev Lember <klember@redhat.com> - 45.0-1
- Update to 45.0

* Fri Jul 28 2023 Kevin Fenzi <kevin@scrye.com> - 45~alpha-3
- Add patch to fix gjs crash

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 45~alpha-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Tue Jul 04 2023 Kalev Lember <klember@redhat.com> - 45~alpha-1
- Update to 45.alpha

* Sun Mar 19 2023 David King <amigadave@amigadave.com> - 44.0-1
- Update to 44.0 (#2179673)

* Mon Mar 06 2023 David King <amigadave@amigadave.com> - 44~rc-1
- Update to 44.rc (#2150952)

* Thu Feb 16 2023 David King <amigadave@amigadave.com> - 44~beta-1
- Update to 44.beta

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 43.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Tue Dec 06 2022 David King <amigadave@amigadave.com> - 43.1-1
- Update to 43.1

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

* Sat Mar 19 2022 David King <amigadave@amigadave.com> - 42.0-1
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

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 3.34.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.34.0-4
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.34.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Mar 09 2020 Kalev Lember <klember@redhat.com> - 3.34.0-2
- Rebuild

* Thu Feb 27 2020 Kalev Lember <klember@redhat.com> - 3.34.0-1
- Update to 3.34.0

* Wed Feb 26 2020 Bastien Nocera <bnocera@redhat.com> - 3.32.1-5
+ gnome-characters-3.32.1-5
- Fix use of removed functions

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.32.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.32.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Tue Apr 16 2019 Adam Williamson <awilliam@redhat.com> - 3.32.1-2
- Rebuild with Meson fix for #1699099

* Mon Apr 08 2019 Kalev Lember <klember@redhat.com> - 3.32.1-1
- Update to 3.32.1

* Wed Mar 20 2019 Matthias Clasen <mclasen@redhat.com> - 3.32.0-2
- Add a missing runtime dep. This was causing the
  flatpak build to miss gnome-desktop3, which is
  used by introspection

* Fri Mar 15 2019 Kalev Lember <klember@redhat.com> - 3.32.0-1
- Update to 3.32.0

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.30.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Tue Oct 09 2018 Kalev Lember <klember@redhat.com> - 3.30.0-1
- Update to 3.30.0

* Thu Sep 06 2018 Kalev Lember <klember@redhat.com> - 3.29.91-1
- Update to 3.29.91

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.28.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue May 08 2018 Kalev Lember <klember@redhat.com> - 3.28.2-1
- Update to 3.28.2

* Mon Mar 12 2018 Kalev Lember <klember@redhat.com> - 3.28.0-1
- Update to 3.28.0

* Mon Mar 05 2018 Kalev Lember <klember@redhat.com> - 3.27.92-1
- Update to 3.27.92
- Switch to the meson build system
- Build with system libunistring

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.26.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Sat Jan 06 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 3.26.2-2
- Remove obsolete scriptlets

* Wed Nov 01 2017 Kalev Lember <klember@redhat.com> - 3.26.2-1
- Update to 3.26.2

* Sun Oct 08 2017 Kalev Lember <klember@redhat.com> - 3.26.1-1
- Update to 3.26.1

* Thu Sep 07 2017 Kalev Lember <klember@redhat.com> - 3.25.92-1
- Update to 3.25.92

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.24.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.24.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Tue Jul 18 2017 Kalev Lember <klember@redhat.com> - 3.24.0-1
- Update to 3.24.0

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.22.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Sep 21 2016 Daiki Ueno <dueno@redhat.com> - 3.22.0-1
- Update to 3.22.0

* Sat Aug 27 2016 Kalev Lember <klember@redhat.com> - 3.21.91.1-1
- Update to 3.21.91.1

* Wed Apr 13 2016 Kalev Lember <klember@redhat.com> - 3.20.1-1
- Update to 3.20.1

* Tue Mar 22 2016 Kalev Lember <klember@redhat.com> - 3.20.0-1
- Update to 3.20.0

* Mon Mar 14 2016 Kalev Lember <klember@redhat.com> - 3.19.92-1
- Update to 3.19.92

* Tue Feb 16 2016 Richard Hughes <rhughes@redhat.com> - 3.19.90-1
- Update to 3.19.90

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 3.19.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Mon Dec 14 2015 Kalev Lember <klember@redhat.com> - 3.19.3-1
- Update to 3.19.3

* Sun Oct 11 2015 Kalev Lember <klember@redhat.com> - 3.18.1-1
- Update to 3.18.1

* Fri Oct 09 2015 Michael Catanzaro <mcatanzaro@gnome.org> - 3.18.0-3
- Disable the search provider by default.

* Tue Sep 29 2015 Michael Catanzaro <mcatanzaro@gnome.org> - 3.18.0-2
- Add symbolic icon and X-GNOME-Utilities desktop category.

* Mon Sep 21 2015 Kalev Lember <klember@redhat.com> - 3.18.0-1
- Update to 3.18.0

* Mon Aug 31 2015 Kalev Lember <klember@redhat.com> - 3.17.91-1
- Update to 3.17.91

* Fri Aug 21 2015 Matthias Clasen <mclasen@redhat.com> - 3.17.90-2
- Force-update the icon cache for the gnome theme. This is necessary
  because icons were moved from gnome to hicolor, and if we don't update
  the gnome icon cache, it hides the icons in lower hicolor theme.
  This is a one-shot fix, and should be removed in the next package
  update.

* Tue Aug 18 2015 Kalev Lember <klember@redhat.com> - 3.17.90-1
- Update to 3.17.90

* Wed Jul 29 2015 Daiki Ueno <dueno@redhat.com> - 3.17.4.1-1
- Update to 3.17.4.1

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.16.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Tue May 12 2015 Kalev Lember <kalevlember@gmail.com> - 3.16.2-1
- Update to 3.16.2

* Tue Apr 14 2015 Kalev Lember <kalevlember@gmail.com> - 3.16.1-1
- Update to 3.16.1

* Mon Mar 23 2015 Kalev Lember <kalevlember@gmail.com> - 3.16.0-1
- Update to 3.16.0

* Tue Mar 17 2015 Daiki Ueno <dueno@redhat.com> - 3.15.92-1
- Initial packaging for Fedora
