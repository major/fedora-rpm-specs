Name:		phoc
Version:	0.46~rc2
Release:	%{autorelease}
Summary:	Display compositor designed for phones

License:	GPL-3.0-or-later
URL:		https://gitlab.gnome.org/World/Phosh/phoc
Source:	https://gitlab.gnome.org/World/Phosh/phoc/-/archive/v%{version_no_tilde _}/%{name}-v%{version_no_tilde _}.tar.gz

BuildRequires:	gcc
BuildRequires:	meson
BuildRequires:	cmake
BuildRequires:	/usr/bin/rst2man

BuildRequires:	pkgconfig(gio-2.0) >= 2.80
BuildRequires:	pkgconfig(glib-2.0) >= 2.80
BuildRequires:	pkgconfig(gobject-2.0) >= 2.80
BuildRequires:	pkgconfig(glesv2)
BuildRequires:	pkgconfig(gnome-desktop-3.0) >= 3.26
BuildRequires:	pkgconfig(libinput)
BuildRequires:	pkgconfig(libudev)
BuildRequires:	pkgconfig(libdrm)
BuildRequires:	pkgconfig(pixman-1) >= 0.43.4
BuildRequires:	pkgconfig(wayland-client)
BuildRequires:	pkgconfig(wayland-protocols) >= 1.15
BuildRequires:	pkgconfig(wayland-server)
BuildRequires:	pkgconfig(xkbcommon)
BuildRequires:	pkgconfig(gmobile) >= 0.1.0
BuildRequires:	pkgconfig(wlroots-0.18)
BuildRequires:	pkgconfig(gsettings-desktop-schemas)
BuildRequires:	pkgconfig(json-glib-1.0)
# tests needs xvfb-run
BuildRequires:	xorg-x11-server-Xvfb
# tests need dbus-daemon, mutter gschemas and Xwayland
BuildRequires:	dbus-daemon
BuildRequires:	mutter-common
BuildRequires:	xorg-x11-server-Xwayland

ExcludeArch:	i686

%description
Phoc is a wlroots based Phone compositor as used on the Librem5. Phoc is
pronounced like the English word fog.

%prep
%setup -q -n %{name}-v%{version_no_tilde _}

%build
%meson -Dembed-wlroots=disabled -Dman=true
%meson_build

%install
%meson_install

# xdg-decoration test fails on s390x
# timed-animations fails on ppc64le
%ifnarch s390x ppc64le
%check
xvfb-run -s -noreset sh <<HERE
%meson_test
HERE
%endif

%files
%doc README.md
%license LICENSES
%{_bindir}/phoc
%{_datadir}/phoc
%{_datadir}/glib-2.0/schemas/sm.puri.phoc.gschema.xml
%{_datadir}/applications/mobi.phosh.Phoc.desktop
%{_datadir}/icons/hicolor/symbolic/apps/mobi.phosh.Phoc.svg
%{_mandir}/man1/phoc.1.gz
%{_mandir}/man5/phoc.gsettings.5.gz
%{_mandir}/man5/phoc.ini.5.gz

%changelog
%autochangelog
