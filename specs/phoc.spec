Name:		phoc
Version:	0.44.1
Release:	%{autorelease}
Summary:	Display compositor designed for phones

License:	GPL-3.0-or-later
URL:		https://gitlab.gnome.org/World/Phosh/phoc
Source:	https://gitlab.gnome.org/World/Phosh/phoc/-/archive/v%{version}/%{name}-v%{version}.tar.gz

BuildRequires:	gcc
BuildRequires:	meson
BuildRequires:	cmake

BuildRequires:	pkgconfig(gio-2.0) >= 2.70
BuildRequires:	pkgconfig(glib-2.0) >= 2.70
BuildRequires:	pkgconfig(gobject-2.0) >= 2.70a
BuildRequires:	pkgconfig(glesv2)
BuildRequires:	pkgconfig(gnome-desktop-3.0) >= 3.26
BuildRequires:	pkgconfig(libinput)
BuildRequires:	pkgconfig(libudev)
BuildRequires:	pkgconfig(libdrm)
BuildRequires:	pkgconfig(pixman-1)
BuildRequires:	pkgconfig(wayland-client)
BuildRequires:	pkgconfig(wayland-protocols) >= 1.15
BuildRequires:	pkgconfig(wayland-server)
BuildRequires:	pkgconfig(xkbcommon)
BuildRequires:	pkgconfig(gmobile) >= 0.1.0
BuildRequires:	(pkgconfig(wlroots) >= 0.17.0 with pkgconfig(wlroots) < 0.18)
BuildRequires:	pkgconfig(gsettings-desktop-schemas)
BuildRequires:	pkgconfig(json-glib-1.0)

ExcludeArch:	i686

%description
Phoc is a wlroots based Phone compositor as used on the Librem5. Phoc is
pronounced like the English word fog.

%prep
%setup -q -n %{name}-v%{version}

%build
%meson -Dembed-wlroots=disabled
%meson_build

%install
%meson_install

%files
%doc README.md
%license LICENSES
%{_bindir}/phoc
%{_datadir}/phoc
%{_datadir}/glib-2.0/schemas/sm.puri.phoc.gschema.xml
%{_datadir}/applications/mobi.phosh.Phoc.desktop
%{_datadir}/icons/hicolor/symbolic/apps/mobi.phosh.Phoc.svg

%changelog
%autochangelog
