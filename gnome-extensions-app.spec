%global _vpath_srcdir subprojects/extensions-app
%global source_name gnome-shell
%global tarball_version %%(echo %{version} | tr '~' '.')

Name:          gnome-extensions-app
Version:       44~rc
Release:       1%{?dist}
Summary:       Manage GNOME Shell extensions

License:       GPLv2+
URL:           https://gitlab.gnome.org/GNOME/%{source_name}
Source0:       https://download.gnome.org/sources/%{source_name}/44/%{source_name}-%{tarball_version}.tar.xz

BuildRequires: gcc
BuildRequires: gettext
BuildRequires: meson
BuildRequires: git

BuildRequires: pkgconfig(glib-2.0)
BuildRequires: pkgconfig(gtk4)
BuildRequires: pkgconfig(gobject-introspection-1.0)
BuildRequires: gjs
BuildRequires: desktop-file-utils
BuildRequires: libappstream-glib

Requires:      gjs%{_isa}
Requires:      libadwaita%{_isa}

%define exec_name gnome-extensions-app
%define bus_name org.gnome.Extensions

%description
GNOME Extensions is an application for configuring and removing
GNOME Shell extensions.


%prep
%setup -q -n %{source_name}-%{tarball_version}

%{_vpath_srcdir}/generate-translations.sh


%build
%meson
%meson_build

%check
%meson_test
desktop-file-validate %{buildroot}%{_datadir}/applications/%{bus_name}.desktop


%install
%meson_install

%find_lang %{name}

rm -rf %{buildroot}/%{_datadir}/%{name}/gir-1.0

%files -f %{name}.lang
%license COPYING
%{_bindir}/%{exec_name}
%{_datadir}/applications/%{bus_name}.desktop
%{_datadir}/dbus-1/services/%{bus_name}.service
%{_datadir}/metainfo/%{bus_name}.metainfo.xml
%{_datadir}/icons/hicolor/scalable/apps/%{bus_name}.svg
%{_datadir}/icons/hicolor/scalable/apps/%{bus_name}.Devel.svg
%{_datadir}/icons/hicolor/symbolic/apps/%{bus_name}-symbolic.svg
%{_datadir}/%{name}/
%{_libdir}/%{name}/


%changelog
* Wed Mar 08 2023 Florian Müllner <fmuellner@redhat.com> - 44~rc-1
- Update to 44.rc

* Tue Feb 14 2023 Florian Müllner <fmuellner@redhat.com> - 44~beta-1
- Update to 44.beta

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 43~beta-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Wed Aug 10 2022 Florian Müllner <fmuellner@redhat.com> - 43~beta-1
- Update to 43.beta

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 42.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Sun Mar 20 2022 Florian Müllner <fmuellner@redhat.com> - 42.0-1
- Update to 42.0

* Tue Feb 15 2022 Florian Müllner <fmuellner@redhat.com> - 42~beta-1
- Update to 42.beta

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 41~rc-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Mon Sep 06 2021 Florian Müllner <fmuellner@redhat.com> - 41~rc-1
- Update to 41.rc

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 40.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Sun Mar 28 2021 Kalev Lember <klember@redhat.com> - 40.0-1
- Update to 40.0

* Mon Mar 15 2021 Florian Müllner <fmuellner@redhat.com> - 40.0~rc-1
- Update to 40.rc

* Thu Mar 11 2021 Florian Müllner <fmuellner@redhat.com> - 40.0~beta-1
- Update to 40.beta

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 3.38.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Sep 15 2020 Florian Müllner <fmuellner@redhat.com> - 3.38.0-1
- Update to 3.38.0

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.37.3-3
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.37.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jul 07 2020 Florian Müllner <fmuellner@gnome.org> - 3.37.2-1
- Update to 3.37.3

* Wed Jun 03 2020 Florian Müllner <fmuellner@gnome.org> - 3.37.2-1
- Update to 3.37.2

* Thu Apr 30 2020 Florian Müllner <fmuellner@gnome.org> - 3.37.1-1
- Update to 3.37.1

* Wed Apr 01 2020 Florian Müllner <fmuellner@gnome.org> - 3.36.1-1
- Make flatpak build compatible with F31

* Tue Mar 31 2020 Florian Müllner <fmuellner@gnome.org> - 3.36.1-1
- Build initial version
