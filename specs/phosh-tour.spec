Name:     phosh-tour
Version:  0.50.0
Release:  %autorelease
Summary:  Simple introduction to Phosh
License:  GPL-3.0-or-later
URL:      https://gitlab.gnome.org/World/Phosh/phosh-tour
Source:   https://gitlab.gnome.org/World/Phosh/phosh-tour/-/archive/v%{version_no_tilde _}/%{name}-v%{version_no_tilde _}.tar.gz
# Ensure appstream file is tested
Patch:    Require-appstreamcli-to-validate-appstream-file.patch

ExcludeArch:  %{ix86}

BuildRequires:  gcc
BuildRequires:  meson
BuildRequires:  pkgconfig(glib-2.0) >= 2.74
BuildRequires:  pkgconfig(gio-2.0) >= 2.74
BuildRequires:  pkgconfig(gtk4) >= 4.12
BuildRequires:  pkgconfig(libadwaita-1) >= 1.4
BuildRequires:  pkgconfig(gmobile) >= 0.1.0
BuildRequires:  libappstream-glib
BuildRequires:  desktop-file-utils
BuildRequires:  systemd-rpm-macros

Requires:  hicolor-icon-theme

%description
Simple introduction to Phosh shell.

%prep
%autosetup -p1 -n %{name}-v%{version_no_tilde _}

%build
%meson -Dvendor="Fedora Remix Mobility"
%meson_build

%install
%meson_install
%find_lang %{name}

%check
desktop-file-validate %{buildroot}%{_datadir}/applications/mobi.phosh.PhoshTour.desktop
%meson_test

%post
%systemd_user_post mobi.phosh.PhoshTour-first-login.service

%preun
%systemd_user_preun mobi.phosh.PhoshTour-first-login.service

%postun
%systemd_user_postun_with_restart mobi.phosh.PhoshTour-first-login.service
%systemd_user_postun_with_reload mobi.phosh.PhoshTour-first-login.service
%systemd_user_postun mobi.phosh.PhoshTour-first-login.service

%files -f %{name}.lang
%doc README.md
%license COPYING
%{_bindir}/phosh-tour
%{_datadir}/applications/mobi.phosh.PhoshTour.desktop
%{_datadir}/glib-2.0/schemas/mobi.phosh.PhoshTour.gschema.xml
%{_datadir}/icons/hicolor/scalable/apps/mobi.phosh.PhoshTour.svg
%{_datadir}/icons/hicolor/symbolic/apps/mobi.phosh.PhoshTour-symbolic.svg
%{_metainfodir}/mobi.phosh.PhoshTour.metainfo.xml
%{_sysconfdir}/xdg/autostart/mobi.phosh.PhoshTour-first-login.desktop
%{_userunitdir}/mobi.phosh.PhoshTour-first-login.service

%changelog
%autochangelog
