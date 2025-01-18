Name:      gnome-packagekit
Version:   43.0
Release:   7%{?dist}
Summary:   Session applications to manage packages
License:   GPL-2.0-or-later
URL:       https://www.freedesktop.org/software/PackageKit/
Source0:   http://download.gnome.org/sources/gnome-packagekit/43/%{name}-%{version}.tar.xz

BuildRequires: glib2-devel >= 2.25.8
BuildRequires: gtk3-devel
BuildRequires: libnotify-devel >= 0.7.0
BuildRequires: desktop-file-utils
BuildRequires: gettext
BuildRequires: libtool
BuildRequires: cairo-devel
BuildRequires: startup-notification-devel
BuildRequires: PackageKit-devel >= 0.5.0
BuildRequires: xorg-x11-proto-devel
BuildRequires: fontconfig-devel
BuildRequires: libcanberra-devel
BuildRequires: libgudev1-devel
BuildRequires: libxslt
BuildRequires: docbook-utils
BuildRequires: systemd-devel
BuildRequires: meson
BuildRequires: polkit-devel
BuildRequires: itstool
BuildRequires: appstream

# the top level package depends on all the apps to make upgrades work
Requires: %{name}-installer
Requires: %{name}-updater

%description
gnome-packagekit provides session applications for the PackageKit API.
There are several utilities designed for installing, updating and
removing packages on your system.

%package common
Summary: Common files required for %{name}
Requires:  adwaita-icon-theme
Requires:  PackageKit%{?_isa} >= 0.5.0
Requires:  PackageKit-libs >= 0.5.0
Requires:  shared-mime-info
Requires:  iso-codes
Requires:  libcanberra%{?_isa} >= 0.10

%description common
Files shared by all subpackages of %{name}

%package installer
Summary: PackageKit package installer
Requires: %{name}-common%{?_isa} = %{version}-%{release}

%description installer
A graphical package installer for PackageKit which is used to manage software
not shown in GNOME Software.

%package updater
Summary: PackageKit package updater
Requires: %{name}-common%{?_isa} = %{version}-%{release}

%description updater
A graphical package updater for PackageKit which is used to update packages
without rebooting.

%prep
%setup -q

%build
%meson
%meson_build

%install
%meson_install

%find_lang %name --with-gnome

%files
# nada

%files common -f %{name}.lang
%license COPYING
%doc AUTHORS
%{_bindir}/gpk-log
%{_bindir}/gpk-prefs
%dir %{_datadir}/gnome-packagekit
%dir %{_datadir}/gnome-packagekit/icons
%dir %{_datadir}/gnome-packagekit/icons/hicolor
%dir %{_datadir}/gnome-packagekit/icons/hicolor/*
%dir %{_datadir}/gnome-packagekit/icons/hicolor/*/*
%{_datadir}/gnome-packagekit/icons/hicolor/*/*/*.png
%{_datadir}/gnome-packagekit/icons/hicolor/scalable/*/*.svg*
%{_datadir}/icons/hicolor/scalable/*/*.svg*
%{_datadir}/applications/gpk-log.desktop
%{_datadir}/applications/gpk-prefs.desktop
%{_datadir}/glib-2.0/schemas/org.gnome.packagekit.gschema.xml
%{_datadir}/GConf/gsettings/org.gnome.packagekit.gschema.migrate
%{_mandir}/man1/gpk-log.1*
%{_mandir}/man1/gpk-prefs.1*

%files installer
%{_bindir}/gpk-application
%{_datadir}/applications/org.gnome.Packages.desktop
%{_datadir}/metainfo/org.gnome.Packages.metainfo.xml
%{_mandir}/man1/gpk-application.1*

%files updater
%{_bindir}/gpk-update-viewer
%{_datadir}/applications/org.gnome.PackageUpdater.desktop
%{_datadir}/metainfo/org.gnome.PackageUpdater.metainfo.xml
%{_mandir}/man1/gpk-update-viewer.1*

%changelog
* Thu Jan 16 2025 Fedora Release Engineering <releng@fedoraproject.org> - 43.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 43.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Wed Jan 24 2024 Fedora Release Engineering <releng@fedoraproject.org> - 43.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 43.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 43.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 43.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Nov 04 2022 Richard Hughes <rhughes@redhat.com> - 43.0-1
- Update to 43.0

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 3.32.0-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 3.32.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 3.32.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 3.32.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.32.0-6
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.32.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.32.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.32.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Wed Jun 12 2019 Kalev Lember <klember@redhat.com> - 3.32.0-2
- Remove obsolete PackageKit-session-service virtual provide

* Mon Mar 11 2019 Kalev Lember <klember@redhat.com> - 3.32.0-1
- Update to 3.32.0

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.30.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Sep 06 2018 Kalev Lember <klember@redhat.com> - 3.30.0-1
- Update to 3.30.0

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.28.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Mon Mar 12 2018 Kalev Lember <klember@redhat.com> - 3.28.0-1
- Update to 3.28.0

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.26.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jan 11 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 3.26.0-2
- Remove obsolete scriptlets

* Mon Sep 11 2017 Kalev Lember <klember@redhat.com> - 3.26.0-1
- Update to 3.26.0

* Tue Aug 15 2017 Kalev Lember <klember@redhat.com> - 3.25.90-1
- Update to 3.25.90
- Switch to the meson build system

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.24.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.24.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Tue Mar 21 2017 Kalev Lember <klember@redhat.com> - 3.24.0-1
- Update to 3.24.0

* Sat Mar 11 2017 Richard Hughes <rhughes@redhat.com> - 3.23.92-1
- Update to 3.23.92

* Fri Mar 10 2017 Kalev Lember <klember@redhat.com> - 3.23.90-2
- Fix gnome-packagekit-install dependencies

* Mon Feb 13 2017 Richard Hughes <rhughes@redhat.com> - 3.23.90-1
- Update to 3.23.90

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.22.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Oct 12 2016 Kalev Lember <klember@redhat.com> - 3.22.1-1
- Update to 3.22.1

* Mon Sep 19 2016 Kalev Lember <klember@redhat.com> - 3.22.0-1
- Update to 3.22.0

* Wed Sep 14 2016 Kalev Lember <klember@redhat.com> - 3.21.92-1
- Update to 3.21.92

* Mon Aug 29 2016 Kalev Lember <klember@redhat.com> - 3.21.91-1
- Update to 3.21.91
- Don't set group tags

* Wed Aug 17 2016 Kalev Lember <klember@redhat.com> - 3.21.90-1
- Update to 3.21.90

* Mon Jul 18 2016 Richard Hughes <rhughes@redhat.com> - 3.21.4-1
- Update to 3.21.4

* Tue Mar 22 2016 Kalev Lember <klember@redhat.com> - 3.20.0-1
- Update to 3.20.0

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 3.18.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Mon Sep 21 2015 Kalev Lember <klember@redhat.com> - 3.18.0-1
- Update to 3.18.0

* Wed Aug 19 2015 Kalev Lember <klember@redhat.com> - 3.17.90-1
- Update to 3.17.90
- Use make_install macro

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.16.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Mon Mar 23 2015 Kalev Lember <kalevlember@gmail.com> - 3.16.0-1
- Update to 3.16.0

* Mon Mar 16 2015 Kalev Lember <kalevlember@gmail.com> - 3.15.92-1
- Update to 3.15.92

* Mon Mar 02 2015 Kalev Lember <kalevlember@gmail.com> - 3.15.91-1
- Update to 3.15.91

* Tue Feb 17 2015 Richard Hughes <rhughes@redhat.com> - 3.15.90-1
- Update to 3.15.90

* Mon Jan 19 2015 Richard Hughes <rhughes@redhat.com> - 3.15.4-1
- Update to 3.15.4

* Thu Dec 18 2014 Richard Hughes <rhughes@redhat.com> - 3.15.3-1
- Update to 3.15.3

* Mon Nov 10 2014 Kalev Lember <kalevlember@gmail.com> - 3.14.2-1
- Update to 3.14.2

* Mon Sep 22 2014 Kalev Lember <kalevlember@gmail.com> - 3.14.0-1
- Update to 3.14.0

* Fri Sep 12 2014 Kalev Lember <kalevlember@gmail.com> - 3.13.92-1
- Update to 3.13.92

* Mon Sep 01 2014 Kalev Lember <kalevlember@gmail.com> - 3.13.91-1
- Update to 3.13.91

* Mon Aug 18 2014 Kalev Lember <kalevlember@gmail.com> - 3.13.90-1
- Update to 3.13.90

* Sat Aug 16 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.12.2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild
