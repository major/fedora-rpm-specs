Name:           cow
Version:        0.1
Release:        1%{?dist}
Summary:        Compositor on Wayland - A stacking window manager

License:        ISC
URL:            https://codeberg.org/thomasadam/cow
Source0:        %{url}/archive/%{version_no_tilde}.tar.gz#/%{name}-%{version_no_tilde}.tar.gz

BuildRequires: bison
BuildRequires: flex
BuildRequires: gcc
BuildRequires: pkgconfig(libbsd)
BuildRequires: pkgconfig(libevent)
BuildRequires: pkgconfig(xkbcommon)
BuildRequires: meson
BuildRequires: pkgconfig(cairo)
BuildRequires: pkgconfig(pangocairo)
BuildRequires: pkgconfig(scdoc)
BuildRequires: pkgconfig(wayland-client)
BuildRequires: pkgconfig(wayland-protocols)

Requires: libevdev-utils
Requires: libxkbcommon-utils
Requires: pasystray
Requires: river
Requires: waybar

%description
CoW (Compositor on Wayland) is a stacking window manager for Wayland.
CoW aims to provide the look-and-feel of FVWM and MWM with a sensible
configuration mechanism using dedicated commands that can be used both
as a configuration file and via IPC at runtime.

%prep
%autosetup -C -p1 

%conf
export CFLAGS="%{build_cflags} -Wno-error=format-security"
%meson -Detcprefix=/

%build
%meson_build

%install
%meson_install

%files
%{_bindir}/cow
%{_bindir}/cow-start
%{_bindir}/cowbar
%{_bindir}/cowpager
%{_bindir}/moocow
%{_bindir}/cowident
%{_bindir}/cowrearrange
%{_bindir}/cowbuttons
%{_bindir}/cowiconman
%dir %{_sysconfdir}/cow
%config(noreplace) %{_sysconfdir}/cow/cow.conf
%{_datadir}/wayland-sessions/cow.desktop
%{_datadir}/cow/icons/default.png
%{_mandir}/man1/cow.1*
%{_mandir}/man1/cowbar.1*
%{_mandir}/man1/cowident.1*
%{_mandir}/man1/cowpager.1*
%{_mandir}/man1/moocow.1*
%{_mandir}/man1/cowrearrange.1*
%{_mandir}/man1/cowbuttons.1*
%{_mandir}/man1/cowiconman.1*

%changelog
* Tue Aug 11 2026 Martin Cermak <mcermak@redhat.com> - 0.1-1
- The inaugural release of CoW!

* Fri Aug 7 2026 Martin Cermak <mcermak@redhat.com> - 0.1~rc-1
- Bug 2489821 - Review Request: cow - Compositor on Wayland
