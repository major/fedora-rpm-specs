%global dconf_version 0.26.1
%global glib2_version 2.56.0
%global gtk3_version 3.22.27

%global tarball_version %%(echo %{version} | tr '~' '.')

Name:           dconf-editor
Version:        45.0.1
Release:        6%{?dist}
Summary:        Configuration editor for dconf

License:        GPL-3.0-or-later AND CC0-1.0
URL:            https://wiki.gnome.org/Projects/dconf
Source0:        https://download.gnome.org/sources/dconf-editor/45/dconf-editor-%{tarball_version}.tar.xz
Source1:        https://raw.githubusercontent.com/flathub/ca.desrt.dconf-editor/master/start-dconf-editor.sh

BuildRequires:  /usr/bin/appstream-util
BuildRequires:  desktop-file-utils
BuildRequires:  gettext
BuildRequires:  meson
BuildRequires:  pkgconfig(dconf) >= %{dconf_version}
BuildRequires:  pkgconfig(glib-2.0) >= %{glib2_version}
BuildRequires:  pkgconfig(gmodule-2.0)
BuildRequires:  pkgconfig(gtk+-3.0) >= %{gtk3_version}
BuildRequires:  pkgconfig(libhandy-1)
BuildRequires:  pkgconfig(libxml-2.0)
BuildRequires:  vala

Requires:       dconf%{?_isa} >= %{dconf_version}
Requires:       glib2%{?_isa} >= %{glib2_version}
Requires:       gtk3%{?_isa} >= %{gtk3_version}

%description
Graphical tool for editing the dconf configuration database.

%prep
%autosetup -p1 -n %{name}-%{tarball_version}

%build
%meson
%meson_build

%install
%meson_install

%if 0%{?flatpak}
install -m 755 %{SOURCE1} $RPM_BUILD_ROOT%{_bindir}/start-dconf-editor
%endif

%find_lang dconf-editor

%check
appstream-util validate-relax --nonet $RPM_BUILD_ROOT%{_datadir}/metainfo/ca.desrt.dconf-editor.appdata.xml
desktop-file-validate $RPM_BUILD_ROOT%{_datadir}/applications/ca.desrt.dconf-editor.desktop

%files -f dconf-editor.lang
%license COPYING
%{_bindir}/dconf-editor
%if 0%{?flatpak}
%{_bindir}/start-dconf-editor
%endif
%{_datadir}/applications/ca.desrt.dconf-editor.desktop
%{_datadir}/bash-completion/
%{_datadir}/dbus-1/services/ca.desrt.dconf-editor.service
%{_datadir}/glib-2.0/schemas/ca.desrt.dconf-editor.gschema.xml
%{_datadir}/icons/hicolor/scalable/actions/ca.desrt.dconf-editor.big-rows-symbolic.svg
%{_datadir}/icons/hicolor/scalable/actions/ca.desrt.dconf-editor.small-rows-symbolic.svg
%{_datadir}/icons/hicolor/scalable/apps/ca.desrt.dconf-editor.Devel.svg
%{_datadir}/icons/hicolor/scalable/apps/ca.desrt.dconf-editor.svg
%{_datadir}/icons/hicolor/symbolic/apps/ca.desrt.dconf-editor-symbolic.svg
%{_datadir}/metainfo/ca.desrt.dconf-editor.appdata.xml
%{_mandir}/man1/dconf-editor.1*

%changelog
* Thu Jan 16 2025 Fedora Release Engineering <releng@fedoraproject.org> - 45.0.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Wed Jul 17 2024 Fedora Release Engineering <releng@fedoraproject.org> - 45.0.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Tue Feb  6 2024 Marek Kasik <mkasik@redhat.com> - 45.0.1-4
- Migrated to SPDX license

* Wed Jan 24 2024 Fedora Release Engineering <releng@fedoraproject.org> - 45.0.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 45.0.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Sep 20 2023 Kalev Lember <klember@redhat.com> - 45.0.1-1
- Update to 45.0.1

* Wed Sep 20 2023 Kalev Lember <klember@redhat.com> - 45.0-1
- Update to 45.0

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 43.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 43.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Tue Sep 20 2022 Kalev Lember <klember@redhat.com> - 43.0-1
- Update to 43.0

* Tue Aug 09 2022 Kalev Lember <klember@redhat.com> - 43~beta-1
- Update to 43.beta

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 43~alpha-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Tue Jul 19 2022 Kalev Lember <klember@redhat.com> - 43~alpha-1
- Update to 43.alpha

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 3.38.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 3.38.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Mar 23 2021 Kalev Lember <klember@redhat.com> - 3.38.3-1
- Update to 3.38.3
- Remove old conflicts with dconf package

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 3.38.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Nov 25 2020 Kalev Lember <klember@redhat.com> - 3.38.2-1
- Update to 3.38.2

* Sat Sep 12 2020 Kalev Lember <klember@redhat.com> - 3.38.0-1
- Update to 3.38.0

* Sat Aug 29 2020 Kalev Lember <klember@redhat.com> - 3.37.91-1
- Update to 3.37.91

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.36.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Jul 20 2020 Kalev Lember <klember@redhat.com> - 3.36.4-1
- Update to 3.36.4

* Sat Apr 25 2020 Kalev Lember <klember@redhat.com> - 3.36.2-1
- Update to 3.36.2

* Tue Mar 10 2020 Kalev Lember <klember@redhat.com> - 3.36.0-1
- Update to 3.36.0

* Mon Feb 17 2020 Kalev Lember <klember@redhat.com> - 3.35.91-1
- Update to 3.35.91

* Sun Feb 02 2020 Kalev Lember <klember@redhat.com> - 3.35.90-1
- Update to 3.35.90

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.34.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Tue Jan 07 2020 Kalev Lember <klember@redhat.com> - 3.34.3-1
- Update to 3.34.3

* Mon Oct 07 2019 Kalev Lember <klember@redhat.com> - 3.34.2-1
- Update to 3.34.2

* Tue Sep 10 2019 Kalev Lember <klember@redhat.com> - 3.34.1-1
- Update to 3.34.1

* Mon Aug 19 2019 Kalev Lember <klember@redhat.com> - 3.33.91-1
- Update to 3.33.91

* Mon Aug 12 2019 Kalev Lember <klember@redhat.com> - 3.33.90-1
- Update to 3.33.90

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.33.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Tue Jul 16 2019 Kalev Lember <klember@redhat.com> - 3.33.4-1
- Update to 3.33.4

* Tue Mar 12 2019 Kalev Lember <klember@redhat.com> - 3.32.0-1
- Update to 3.32.0

* Wed Feb 20 2019 Kalev Lember <klember@redhat.com> - 3.31.91-1
- Update to 3.31.91

* Tue Feb 05 2019 Kalev Lember <klember@redhat.com> - 3.31.90-1
- Update to 3.31.90

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.31.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Mon Jan 07 2019 Kalev Lember <klember@redhat.com> - 3.31.4-1
- Update to 3.31.4

* Wed Sep 26 2018 Kalev Lember <klember@redhat.com> - 3.30.2-1
- Update to 3.30.2

* Thu Sep 06 2018 Kalev Lember <klember@redhat.com> - 3.30.0-1
- Update to 3.30.0

* Mon Aug 13 2018 Kalev Lember <klember@redhat.com> - 3.29.90-1
- Update to 3.29.90

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.28.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Mon May 21 2018 Kalev Lember <klember@redhat.com> - 3.28.0-2
- Add versioned library deps
- Update license tag

* Tue Mar 13 2018 Kalev Lember <klember@redhat.com> - 3.28.0-1
- Update to 3.28.0

* Sun Mar 11 2018 Kalev Lember <klember@redhat.com> - 3.27.92-1
- Update to 3.27.92

* Tue Mar 06 2018 Kalev Lember <klember@redhat.com> - 3.27.91-1
- Update to 3.27.91
- Switch to the meson build system

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.26.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Fri Jan 05 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 3.26.2-2
- Remove obsolete scriptlets

* Wed Nov 01 2017 Kalev Lember <klember@redhat.com> - 3.26.2-1
- Update to 3.26.2

* Sun Oct 08 2017 Kalev Lember <klember@redhat.com> - 3.26.1-1
- Update to 3.26.1

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.23.4-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.23.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.23.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Sat Jan 14 2017 Kalev Lember <klember@redhat.com> - 3.23.4-1
- Update to 3.23.4

* Wed Oct 12 2016 Kalev Lember <klember@redhat.com> - 3.22.1-1
- Update to 3.22.1

* Fri Sep 16 2016 Kalev Lember <klember@redhat.com> - 3.21.92-1
- Update to 3.21.92

* Thu Aug 18 2016 Kalev Lember <klember@redhat.com> - 3.21.90-1
- Update to 3.21.90

* Wed Jul 20 2016 Richard Hughes <rhughes@redhat.com> - 3.21.4-1
- Update to 3.21.4

* Tue May 03 2016 Kalev Lember <klember@redhat.com> - 3.21.1-1
- Update to 3.21.1

* Thu Apr 14 2016 Kalev Lember <klember@redhat.com> - 3.20.1-1
- Update to 3.20.1

* Tue Mar 22 2016 Kalev Lember <klember@redhat.com> - 3.20.0-1
- Update to 3.20.0

* Tue Mar 15 2016 Richard Hughes <rhughes@redhat.com> - 3.19.92-1
- Update to 3.19.92

* Tue Mar 01 2016 Richard Hughes <rhughes@redhat.com> - 3.19.91-1
- Update to 3.19.91

* Tue Feb 16 2016 Richard Hughes <rhughes@redhat.com> - 3.19.90-1
- Update to 3.19.90

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 3.19.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Tue Dec 15 2015 Kalev Lember <klember@redhat.com> - 3.19.3-1
- Update to 3.19.3

* Tue Nov 24 2015 Kalev Lember <klember@redhat.com> - 3.19.2-1
- Update to 3.19.2

* Fri Nov 13 2015 Kalev Lember <klember@redhat.com> - 3.18.2-1
- Update to 3.18.2

* Mon Oct 12 2015 Kalev Lember <klember@redhat.com> - 3.18.1-1
- Update to 3.18.1

* Mon Sep 21 2015 Kalev Lember <klember@redhat.com> - 3.18.0-1
- Update to 3.18.0

* Tue Sep 15 2015 Kalev Lember <klember@redhat.com> - 3.17.92-1
- Update to 3.17.92

* Tue Sep 01 2015 Kalev Lember <klember@redhat.com> - 3.17.91-1
- Update to 3.17.91

* Wed Aug 19 2015 Kalev Lember <klember@redhat.com> - 3.17.90-1
- Update to 3.17.90

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.17.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Fri May 01 2015 Kalev Lember <kalevlember@gmail.com> - 3.17.1-1
- Update to 3.17.1

* Tue Apr 14 2015 Kalev Lember <kalevlember@gmail.com> - 3.16.1-1
- Update to 3.16.1

* Mon Mar 23 2015 Kalev Lember <kalevlember@gmail.com> - 3.16.0-1
- Update to 3.16.0

* Tue Mar 17 2015 Kalev Lember <kalevlember@gmail.com> - 3.15.92-1
- Update to 3.15.92
- Ship the man page

* Tue Mar 03 2015 Kalev Lember <kalevlember@gmail.com> - 3.15.91-3
- Fix unowned HighContrast icon theme directories (#1197898)

* Tue Mar 03 2015 Kalev Lember <kalevlember@gmail.com> - 3.15.91-2
- Fix appdata screenshot URL
- Validate appdata during %%check

* Mon Mar 02 2015 Kalev Lember <kalevlember@gmail.com> - 3.15.91-1
- Initial Fedora packaging
