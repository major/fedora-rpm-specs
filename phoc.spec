Name:		phoc
Version:	0.23.0
Release:	2%{?dist}
Summary:	Display compositor designed for phones

License:	GPLv3+
URL:		https://gitlab.gnome.org/World/Phosh/phoc
Source0:	https://gitlab.gnome.org/World/Phosh/phoc/-/archive/v%{version}/%{name}-v%{version}.tar.gz

BuildRequires:	gcc
BuildRequires:	meson

BuildRequires:	pkgconfig(gio-2.0) >= 2.50.0
BuildRequires:	pkgconfig(glib-2.0) >= 2.50.0
BuildRequires:	pkgconfig(gobject-2.0) >= 2.50.0
BuildRequires:  pkgconfig(gsettings-desktop-schemas)
BuildRequires:	pkgconfig(libinput)
BuildRequires:	pkgconfig(pixman-1)
BuildRequires:	pkgconfig(wayland-client)
BuildRequires:	pkgconfig(wayland-protocols) >= 1.15
BuildRequires:	pkgconfig(wayland-server)
BuildRequires:	pkgconfig(xkbcommon)
BuildRequires:	(pkgconfig(wlroots) >= 0.15 with pkgconfig(wlroots) < 0.16)

BuildRequires:	pkgconfig(gnome-desktop-3.0)

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
%{_bindir}/phoc
%{_datadir}/glib-2.0/schemas/sm.puri.phoc.gschema.xml
%doc README.md
%license COPYING

%changelog
* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.23.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

%autochangelog
