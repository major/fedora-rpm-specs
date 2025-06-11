%global tarball_version %%(echo %{version} | tr '~' '_')

Name:           sfwbar
Version:        1.0~beta16.1
Release:        %autorelease
Summary:        S* Floating Window Bar

# Icons are from yr.no and are licensed under MIT license
License:        GPL-3.0-only AND MIT
URL:            https://github.com/LBCrion/sfwbar
Source0:        %{url}/archive/v%{tarball_version}/%{name}-%{tarball_version}.tar.gz

BuildRequires:  gcc
BuildRequires:  make
BuildRequires:  meson
BuildRequires:  python3-docutils
BuildRequires:  pkgconfig(alsa)
BuildRequires:  pkgconfig(gio-2.0)
BuildRequires:  pkgconfig(gio-unix-2.0)
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(gmodule-2.0)
BuildRequires:  pkgconfig(gtk-layer-shell-0)
BuildRequires:  pkgconfig(gtk+-3.0)
BuildRequires:  pkgconfig(json-c)
BuildRequires:  pkgconfig(libmpdclient)
BuildRequires:  pkgconfig(libpulse-mainloop-glib)
BuildRequires:  pkgconfig(libpulse)
BuildRequires:  pkgconfig(wayland-client)
BuildRequires:  pkgconfig(wayland-protocols) >= 1.17
BuildRequires:  pkgconfig(xkbregistry)

Requires:       hicolor-icon-theme

%description
SFWBar (S* Floating Window Bar) is a flexible taskbar application for wayland
compositors, designed with a stacking layout in mind. Originally developed for
Sway, SFWBar will work with any wayland compositor supporting layer shell
protocol, the taskbar and window switcher functionality shall work with any
compositor supporting foreign toplevel protocol, but the pager, and window
placement functionality require sway (or at least i3 IPC support).

%prep
%autosetup -p1 -n %{name}-%{tarball_version}

%build
%meson
%meson_build

%install
%meson_install

%files
%doc README.md doc/ChangeLog
%license LICENSE
# Icons license file:
# %%{_datadir}/%%{name}/icons/weather/LICENSE
%{_bindir}/%{name}
%{_datadir}/%{name}/
%{_datadir}/icons/hicolor/scalable/*/*.svg
%{_libdir}/%{name}/
%{_mandir}/man1/*.1*

%changelog
%autochangelog
