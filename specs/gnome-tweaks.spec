%global tarball_version %%(tr '~' '.' <<<%{version})
%global major_version %%(cut -d '.' -f 1 <<<%{tarball_version})

Name:           gnome-tweaks
Version:        46.1
Release:        4%{?dist}
Summary:        Customize advanced GNOME 3 options

# Software is GPL-3.0+, Appdata file is CC0-1.0
License:        GPL-3.0-or-later AND CC0-1.0
URL:            https://wiki.gnome.org/Apps/Tweaks
Source0:        https://download.gnome.org/sources/%{name}/%{major_version}/%{name}-%{tarball_version}.tar.xz

BuildRequires:  desktop-file-utils
BuildRequires:  gettext
BuildRequires:  libappstream-glib
BuildRequires:  meson
BuildRequires:  python3-devel
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(gobject-introspection-1.0)
BuildRequires:  pkgconfig(gsettings-desktop-schemas) >= 46.0
BuildRequires:  pkgconfig(gtk4)
BuildRequires:  pkgconfig(gudev-1.0)
BuildRequires:  pkgconfig(libadwaita-1)
BuildRequires:  pkgconfig(pygobject-3.0)
Requires:       gnome-desktop4
Requires:       gobject-introspection
Requires:       gsettings-desktop-schemas
Requires:       gtk4
Requires:       libadwaita
Requires:       libgudev
Requires:       libnotify
Requires:       pango
Requires:       %{py3_dist pygobject}
Recommends:     gnome-settings-daemon
Recommends:     gnome-shell
Recommends:     mutter
Recommends:     sound-theme-freedesktop
Suggests:       gnome-shell-extension-user-theme
Provides:       gnome-tweak-tool = %{version}-%{release}
BuildArch:      noarch

%description
GNOME Tweaks allows adjusting advanced configuration settings in GNOME 3. This
includes things like the fonts used in user interface elements, alternative user
interface themes, changes in window management behavior, GNOME Shell appearance
and extension, etc.


%prep
%autosetup -n %{name}-%{tarball_version} -p1


%build
%meson
%meson_build


%install
%meson_install

%find_lang %{name}


%check
desktop-file-validate $RPM_BUILD_ROOT%{_datadir}/applications/*.desktop
appstream-util validate-relax --nonet $RPM_BUILD_ROOT%{_metainfodir}/*.appdata.xml


%files -f %{name}.lang
%doc AUTHORS NEWS README.md
%license LICENSES/*
%{_bindir}/%{name}
%{python3_sitelib}/gtweak/
%{_datadir}/%{name}/
%{_datadir}/applications/*.desktop
%{_datadir}/glib-2.0/schemas/*.xml
%{_datadir}/icons/hicolor/*/apps/org.gnome.tweaks.svg
%{_datadir}/icons/hicolor/symbolic/apps/org.gnome.tweaks-symbolic.svg
%{_metainfodir}/*.appdata.xml


%changelog
* Thu Jan 16 2025 Fedora Release Engineering <releng@fedoraproject.org> - 46.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 46.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Fri Jun 07 2024 Python Maint <python-maint@redhat.com> - 46.1-2
- Rebuilt for Python 3.13

* Fri Apr 26 2024 David King <amigadave@amigadave.com> - 46.1-1
- Update to 46.1

* Mon Mar 18 2024 David King <amigadave@amigadave.com> - 46.0-1
- Update to 46.0

* Tue Mar 05 2024 Adam Williamson <awilliam@redhat.com> - 46~beta-2
- Backport MR #133 to fix compatibility with our current pygobject (#2266153)

* Fri Feb 16 2024 David King <amigadave@amigadave.com> - 46~beta-1
- Update to 46.beta

* Wed Jan 24 2024 Fedora Release Engineering <releng@fedoraproject.org> - 45.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 45.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Sep 24 2023 Mohamed El Morabity <melmorabity@fedoraproject.org> - 45.0-1
- Update to 45.0

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 42~beta-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jun 15 2023 Python Maint <python-maint@redhat.com> - 42~beta-7
- Rebuilt for Python 3.12

* Mon May 01 2023 Mohamed El Morabity <melmorabity@fedoraproject.org> - 42~beta-6
- Switch to SPDX license identifiers
- Separate app and host requirements (https://src.fedoraproject.org/rpms/gnome-tweaks/pull-request/2)

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 42~beta-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 42~beta-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon Jun 27 2022 Mohamed El Morabity <melmorabity@fedoraproject.org> - 42~beta-3
- Drop useless dependency on libsoup (RHBZ #2090983)

* Mon Jun 13 2022 Python Maint <python-maint@redhat.com> - 42~beta-2
- Rebuilt for Python 3.11

* Mon Mar 07 2022 Mohamed El Morabity <melmorabity@fedoraproject.org> - 42~beta-1
- Update to 42.beta

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 40.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 40.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 40.0-3
- Rebuilt for Python 3.10

* Sat Mar 27 2021 Kalev Lember <klember@redhat.com> - 40.0-2
- Use upstream appdata screenshots

* Sat Mar 27 2021 Kalev Lember <klember@redhat.com> - 40.0-1
- Update to 40.0

* Tue Feb 23 2021 Kalev Lember <klember@redhat.com> - 40~beta-4
- Require gnome-themes-extra for gtk3 css files

* Thu Feb 18 2021 Kalev Lember <klember@redhat.com> - 40~beta-3
- Use same pre-release system as in other GNOME packages

* Wed Feb 17 2021 Kalev Lember <klember@redhat.com> - 40~beta-2
- Require libhandy1 instead of libhandy

* Mon Feb 15 2021 Mohamed El Morabity <melmorabity@fedoraproject.org> - 40~beta-1
- Update to 40.beta

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 3.34.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Fri Dec 11 2020 Kalev Lember <klember@redhat.com> - 3.34.1-1
- Update to 3.34.1

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.34.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 3.34.0-5
- Rebuilt for Python 3.9

* Sat Apr 04 2020 Mohamed El Morabity <melmorabity@fedoraproject.org> - 3.34.0-4
- Fix extension preferences opening (RHBZ #1820396)

* Sat Mar 28 2020 Mohamed El Morabity <melmorabity@fedoraproject.org> - 3.34.0-3
- Add dependency on gnome-extensions-app (RHBZ #1812779)

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.34.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Sep 27 2019 Kalev Lember <klember@redhat.com> - 3.34.0-1
- Update to 3.34.0

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 3.33.90-2
- Rebuilt for Python 3.8

* Fri Aug 09 2019 Mohamed El Morabity <melmorabity@fedoraproject.org> - 3.33.90-1
- Update to 3.33.90

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.32.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Wed Jun 19 2019 Mohamed El Morabity <melmorabity@fedoraproject.org> - 3.32.0-2
- Fix typo in Provides version (RHBZ #1721864)

* Mon Mar 11 2019 Kalev Lember <klember@redhat.com> - 3.32.0-1
- Update to 3.32.0

* Wed Feb 06 2019 Kalev Lember <klember@redhat.com> - 3.31.90-1
- Update to 3.31.90

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.31.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Wed Jan 23 2019 Kalev Lember <klember@redhat.com> - 3.31.3-1
- Update to 3.31.3

* Wed Dec 19 2018 Kalev Lember <klember@redhat.com> - 3.30.2-1
- Update to 3.30.2
- Fix opening system installed extensions in gnome-software

* Fri Sep 28 2018 Kalev Lember <klember@redhat.com> - 3.30.1-1
- Update to 3.30.1

* Thu Sep 06 2018 Mohamed El Morabity <melmorabity@fedoraproject.org> - 3.30.0-1
- Update to 3.30.0

* Wed Aug 29 2018 Mohamed El Morabity <melmorabity@fedoraproject.org> - 3.29.92-1
- Update to 3.29.92

* Mon Aug 13 2018 Kalev Lember <klember@redhat.com> - 3.29.91.1-1
- Update to 3.29.91.1

* Fri Aug 03 2018 Mohamed El Morabity <melmorabity@fedoraproject.org> - 3.29.90.1-1
- Update to 3.29.90.1

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.29.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 3.29.2-2
- Rebuilt for Python 3.7

* Mon May 21 2018 Mohamed El Morabity <melmorabity@fedoraproject.org> - 3.29.2-1
- Update to 3.29.2

* Sun Apr 08 2018 Kalev Lember <klember@redhat.com> - 3.28.1-1
- Update to 3.28.1

* Mon Mar 12 2018 Mohamed El Morabity <melmorabity@fedoraproject.org> - 3.28.0-1
- Update to 3.28.0

* Fri Mar 09 2018 Mohamed El Morabity <melmorabity@fedoraproject.org> - 3.27.92-1
- Initial RPM release, based on gnome-tweak-tool.spec
