Name:     stevia
Version:  0.53~rc1
Release:  %autorelease
Summary:  On screen keyboard (OSK) Phosh
License:  GPL-3.0-or-later
URL:      https://gitlab.gnome.org/World/Phosh/stevia
Source:   %{url}/-/archive/v%{version_no_tilde _}/%{name}-v%{version_no_tilde _}.tar.gz

ExcludeArch:  %{ix86}
# https://bugzilla.redhat.com/show_bug.cgi?id=2420908
ExcludeArch:  s390x

BuildRequires:  gcc
BuildRequires:  meson
BuildRequires:  pkgconfig(glib-2.0) >= 2.80
BuildRequires:  pkgconfig(gio-2.0) >= 2.80
BuildRequires:  pkgconfig(gobject-2.0) >= 2.80
BuildRequires:  pkgconfig(gmobile) >= 0.2.0
BuildRequires:  pkgconfig(gnome-desktop-3.0) >= 3.26
BuildRequires:  pkgconfig(gsettings-desktop-schemas) >= 47
BuildRequires:  pkgconfig(gtk+-3.0) >= 3.22
BuildRequires:  pkgconfig(gtk+-wayland-3.0) >= 3.22
BuildRequires:  pkgconfig(gdk-3.0) >= 3.22
BuildRequires:  pkgconfig(gdk-wayland-3.0) >= 3.22
BuildRequires:  pkgconfig(json-glib-1.0)
BuildRequires:  pkgconfig(libfeedback-0.0)
BuildRequires:  pkgconfig(libhandy-1) >= 1.8.0
BuildRequires:  pkgconfig(libsystemd) >= 241
BuildRequires:  pkgconfig(wayland-client) >= 1.14
BuildRequires:  pkgconfig(wayland-protocols) >= 1.12
BuildRequires:  pkgconfig(xkbcommon)
BuildRequires:  pkgconfig(hunspell)
BuildRequires:  /usr/bin/fzf
BuildRequires:  /usr/bin/rst2man
BuildRequires:  /usr/bin/xwfb-run
BuildRequires:  mutter
BuildRequires:  gettext
BuildRequires:  systemd-rpm-macros
BuildRequires:  libappstream-glib
BuildRequires:  desktop-file-utils
BuildRequires:  words
BuildRequires:  systemd-rpm-macros

%description
Stevia is an on screen keyboard (OSK) for Phosh.

The purpose of Stevia is:
* to make typing pleasant and fast on touch screens
* be helpful when debugging input-method related issues
* be quick and easy to (cross)compile
* to be easy to extend (hence the API documentation)

%package phosh-osk-provider
Summary:   Use Stevia as Phosh's default OSK
BuildArch: noarch
Requires:  %{name}
Provides:  phosh-osk = 1.0
Conflicts: phosh-osk
Conflicts: squeekboard-phosh-osk-provider

%description phosh-osk-provider
%{summary}.

%prep
%autosetup -p1 -n %{name}-v%{version_no_tilde _}

%conf
%meson -Dman=true

%build
%meson_build

%install
%meson_install
%find_lang phosh-osk-%{name} --with-man

%check
desktop-file-validate %{buildroot}%{_datadir}/applications/sm.puri.OSK0.desktop
# Using mutter because https://gitlab.freedesktop.org/ofourdan/xwayland-run/-/issues/12
LC_ALL=C.UTF-8 xwfb-run -c mutter -- sh <<'SH'
%meson_test
SH

%files -f phosh-osk-%{name}.lang
%doc README.md
%license COPYING
%{_bindir}/phosh-osk-stevia
%{_datadir}/glib-2.0/schemas/mobi.phosh.osk.enums.xml
%{_datadir}/glib-2.0/schemas/mobi.phosh.osk.gschema.xml
%{_datadir}/metainfo/mobi.phosh.Stevia.metainfo.xml
%{_datadir}/phosh-osk-stevia/
%{_mandir}/man1/phosh-osk-stevia.1*

%files phosh-osk-provider
%{_datadir}/applications/sm.puri.OSK0.desktop
%{_userunitdir}/mobi.phosh.OSK.service

%changelog
%autochangelog
