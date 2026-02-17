%global gvc_commit 1cdc1cb2d622d64e9ad2781093bcc63719c5ea5b

Name:		phosh-mobile-settings
Version:	0.53.0
Release:	%autorelease
Summary:	Mobile Settings App for phosh and related components
License:	GPL-3.0-or-later AND LGPL-3.0-or-later
URL:		https://gitlab.gnome.org/World/Phosh/phosh-mobile-settings
Source0:	https://gitlab.gnome.org/World/Phosh/phosh-mobile-settings/-/archive/v%{version_no_tilde _}/phosh-mobile-settings-v%{version_no_tilde _}.tar.gz
# This library doesn't compile into a DSO nor has any tagged releases.
# Other projects such as gnome-shell use it this way.
Source1:	https://gitlab.gnome.org/guidog/libgnome-volume-control/-/archive/%{gvc_commit}/libgnome-volume-control-%{gvc_commit}.tar.gz

ExcludeArch:	%{ix86}
# https://bugzilla.redhat.com/show_bug.cgi?id=2415478
ExcludeArch:	s390x
# https://bugzilla.redhat.com/show_bug.cgi?id=2415700
ExcludeArch:	ppc64le

BuildRequires:	gcc
BuildRequires:	gcc-c++
BuildRequires:	meson >= 1.7.0

BuildRequires:	pkgconfig(glib-2.0) >= 2.84
BuildRequires:	pkgconfig(gio-2.0) >= 2.84
BuildRequires:	pkgconfig(gio-unix-2.0) >= 2.84
BuildRequires:	pkgconfig(gmodule-2.0) >= 2.84
BuildRequires:	pkgconfig(gmobile) >= 0.4.0
BuildRequires:	pkgconfig(gsound)
BuildRequires:	pkgconfig(gtk4) >= 4.18.0
BuildRequires:	pkgconfig(gtk4-wayland) >= 4.12.5
BuildRequires:	pkgconfig(phosh-plugins) >= 0.23.0
BuildRequires:	pkgconfig(phosh-settings) >= 0.40.0
BuildRequires:	pkgconfig(json-glib-1.0) >= 1.6.2
BuildRequires:	pkgconfig(libadwaita-1) >= 1.7
BuildRequires:	pkgconfig(wayland-client) >= 1.14
BuildRequires:	pkgconfig(wayland-protocols) >= 1.12
BuildRequires:	pkgconfig(gnome-desktop-4) >= 44
BuildRequires:	pkgconfig(libportal-gtk4) >= 0.9.1
BuildRequires:	pkgconfig(libfeedback-0.0) >= 0.8.0
BuildRequires:	pkgconfig(libcellbroadcast-0.0) >= 0.0.2
BuildRequires:	pkgconfig(yaml-0.1)
BuildRequires:	appstream-devel
BuildRequires:	lm_sensors-devel
BuildRequires:	desktop-file-utils
BuildRequires:	dbus-daemon
# gvc
BuildRequires:	pkgconfig(libpulse) >= 12.99.3

Requires:	feedbackd >= 0.8.0
Requires:	phoc >= 0.34.0
Requires:	phosh >= 0.44.0

%description
Mobile Settings App for phosh and related components

%prep
%autosetup -a1 -p1 -n %{name}-v%{version_no_tilde _}
mv libgnome-volume-control-%{gvc_commit} subprojects/gvc
mkdir -p /tmp/runtime-dir
chmod 0700 /tmp/runtime-dir

%conf
%meson -Dtweaks-data-dir=%{_datadir}/phosh-tweaks

%build
%meson_build

%install
%meson_install
install -d %{buildroot}%{_datadir}/phosh-tweaks
%find_lang %{name}

%check
# FIXME: how to handle XDG_RUNTIME_DIR properly
export XDG_RUNTIME_DIR=/tmp/runtime-dir
dbus-run-session sh <<'SH'
%meson_test
SH

%files -f %{name}.lang
%{_bindir}/phosh-mobile-settings
%dir %{_libdir}/phosh-mobile-settings
%{_libdir}/phosh-mobile-settings/plugins/libms-plugin-librem5.so
%{_datadir}/applications/mobi.phosh.MobileSettings.desktop
%{_datadir}/dbus-1/services/mobi.phosh.MobileSettings.service
%{_datadir}/glib-2.0/schemas/mobi.phosh.MobileSettings.gschema.xml
%{_datadir}/icons/hicolor/scalable/apps/mobi.phosh.MobileSettings.svg
%{_datadir}/icons/hicolor/symbolic/apps/mobi.phosh.MobileSettings-symbolic.svg
%{_datadir}/metainfo/mobi.phosh.MobileSettings.metainfo.xml
%dir %{_datadir}/phosh-tweaks

%doc README.md
%license COPYING

%changelog
%autochangelog
