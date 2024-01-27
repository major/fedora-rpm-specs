%global libgmobile_commit f4d4e5740c3e4b2de40864ab8a9e7b7f957d6aec

Name:		phosh-mobile-settings
Version:	0.32.0
Release:	3%{?dist}
Summary:	Mobile Settings App for phosh and related components
License:	GPLv3+
URL:		https://gitlab.gnome.org/guidog/phosh-mobile-settings
Source0:	https://gitlab.gnome.org/guidog/phosh-mobile-settings/-/archive/v%{version}/phosh-mobile-settings-v%{version}.tar.gz
Source1:    https://gitlab.gnome.org/guidog/gmobile/-/archive/%{libgmobile_commit}/gmobile-%{libgmobile_commit}.tar.gz


ExcludeArch:	i686

BuildRequires:	gcc
BuildRequires:	gcc-c++
BuildRequires:	meson


BuildRequires:	pkgconfig(glib-2.0) >= 2.62
BuildRequires:	pkgconfig(gio-2.0) >= 2.62
BuildRequires:	pkgconfig(gio-unix-2.0) >= 2.62
BuildRequires:  pkgconfig(json-glib-1.0)
BuildRequires:	pkgconfig(gmodule-2.0) >= 2.62
BuildRequires:	pkgconfig(gsound)
BuildRequires:	pkgconfig(gtk4) >= 4.4
BuildRequires:	pkgconfig(gtk4-wayland) >= 4.4
BuildRequires:	pkgconfig(libadwaita-1) >= 1.1
BuildRequires:	pkgconfig(wayland-client) >= 1.14
BuildRequires:	pkgconfig(wayland-protocols) >= 1.12
BuildRequires:	appstream-devel
BuildRequires:	lm_sensors-devel
BuildRequires:	desktop-file-utils
BuildRequires:	phosh

Requires:		feedbackd
Requires:		phoc >= 0.30.0
Requires:		phosh >= 0.29.0

%description
Mobile Settings App for phosh and related components

%prep
%setup -a1 -q -n %{name}-v%{version}

mv gmobile-%{libgmobile_commit} subprojects/gmobile

%build
%meson
%meson_build

%install
%meson_install
%find_lang %{name}

%check
%meson_test

%files -f %{name}.lang
%{_bindir}/phosh-mobile-settings
%dir %{_libdir}/phosh-mobile-settings
%{_libdir}/phosh-mobile-settings/plugins/libms-plugin-librem5.so
%{_datadir}/applications/org.sigxcpu.MobileSettings.desktop
%{_datadir}/glib-2.0/schemas/org.sigxcpu.MobileSettings.gschema.xml
%{_datadir}/icons/hicolor/scalable/apps/org.sigxcpu.MobileSettings.svg
%{_datadir}/icons/hicolor/symbolic/apps/org.sigxcpu.MobileSettings-symbolic.svg
%{_datadir}/metainfo/org.sigxcpu.MobileSettings.metainfo.xml

%doc README.md
%license COPYING

%changelog
* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.32.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.32.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

%autochangelog

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.29.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Tue Jun 13 2023 Torrey Sorensen <torbuntu@fedoraproject.org> - 0.26.0-2
- Initial packaging
