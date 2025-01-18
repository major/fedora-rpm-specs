%global glib2_version 2.25
%global gnome_stack 3.1.91
%global gtk3_version 2.99.3

Name:           budgie-screensaver
Version:        5.1.0
Release:        7%{?dist}
Summary:        A fork of gnome-screensaver intended for use with Budgie Desktop

# Automatically converted from old format: GPLv2 - review is highly recommended.
License:        GPL-2.0-only
URL:            https://github.com/BuddiesOfBudgie/budgie-screensaver
Source0:  %{url}/releases/download/v%{version}/%{name}-v%{version}.tar.xz

BuildRequires:  pkgconfig(dbus-glib-1) >= 0.3.0
BuildRequires:  pkgconfig(gio-2.0) >= %{glib2_version}
BuildRequires:  pkgconfig(glib-2.0) >= %{glib2_version}
BuildRequires:  pkgconfig(gnome-desktop-3.0) >= %{gnome_stack}
BuildRequires:  pkgconfig(gsettings-desktop-schemas) >= %{gnome_stack}
BuildRequires:  pkgconfig(gthread-2.0) >= %{glib2_version}
BuildRequires:  pkgconfig(gtk+-3.0) >= %{gtk3_version}
BuildRequires:  pkgconfig(libgnomekbdui) >= 3.28.0
BuildRequires:  pkgconfig(libsystemd) >= 209
BuildRequires:  pkgconfig(pam)
BuildRequires:  pkgconfig(x11) >= 1.0
BuildRequires:  pkgconfig(xxf86vm) >= 1.0
BuildRequires:  desktop-file-utils
BuildRequires:  gcc
BuildRequires:  gettext
BuildRequires:  intltool
BuildRequires:  meson

%description
A fork of gnome-screensaver intended for use with Budgie Desktop.

%prep
%autosetup

%build
%meson
%meson_build

%install
%meson_install
%find_lang %{name}

%check
desktop-file-validate %{buildroot}%{_datadir}/applications/budgie-screensaver.desktop

%files -f %{name}.lang
%doc README.md
%license LICENSE
%{_bindir}/budgie-screensaver-command
%{_bindir}/budgie-screensaver
%{_datadir}/applications/budgie-screensaver.desktop
%{_libexecdir}/budgie-screensaver-dialog
%{_mandir}/man1/budgie-screensaver-command.1*
%{_mandir}/man1/budgie-screensaver.1*
%{_sysconfdir}/pam.d/budgie-screensaver

%changelog
* Thu Jan 16 2025 Fedora Release Engineering <releng@fedoraproject.org> - 5.1.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Mon Jul 29 2024 Miroslav Suchý <msuchy@redhat.com> - 5.1.0-6
- convert license to SPDX

* Wed Jul 17 2024 Fedora Release Engineering <releng@fedoraproject.org> - 5.1.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Tue Jan 23 2024 Fedora Release Engineering <releng@fedoraproject.org> - 5.1.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 5.1.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 5.1.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Sun Jan 29 2023 Joshua Strobl <me@joshuastrobl.com> - 5.1.0-1
- Update to 5.1.0 release

* Wed Jan 18 2023 Fedora Release Engineering <releng@fedoraproject.org> - 5.0.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Wed Jul 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 5.0.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed Jul 20 2022 Kalev Lember <klember@redhat.com> - 5.0.1-2
- Rebuilt for libgnome-desktop soname bump

* Sun May 15 2022 Joshua Strobl <me@joshuastrobl.com> - 5.0.1-1
- Initial packaging of budgie-screensaver
