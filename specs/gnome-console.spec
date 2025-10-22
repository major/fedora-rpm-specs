%global gtk4_version 4.14.0
%global libadwaita_version 1.6
%global vte_version 0.77.0

Name:           gnome-console
Version:        49.1
Release:        %autorelease
Summary:        Simple user-friendly terminal emulator for the GNOME desktop

License:        GPL-3.0-or-later
URL:            https://gitlab.gnome.org/GNOME/console
Source:         https://download.gnome.org/sources/gnome-console/49/gnome-console-%{version_no_tilde .}.tar.xz

BuildRequires:  meson >= 0.59.0
BuildRequires:  gcc
BuildRequires:  pkgconfig(gio-2.0)
BuildRequires:  pkgconfig(gsettings-desktop-schemas)
BuildRequires:  pkgconfig(gtk4) >= %{gtk4_version}
BuildRequires:  pkgconfig(libadwaita-1) >= %{libadwaita_version}
BuildRequires:  pkgconfig(libgtop-2.0)
BuildRequires:  pkgconfig(vte-2.91-gtk4) >= %{vte_version}
BuildRequires:  /usr/bin/appstream-util
BuildRequires:  /usr/bin/desktop-file-validate

Requires:       gtk4%{?_isa} >= %{gtk4_version}
Requires:       libadwaita%{?_isa} >= %{libadwaita_version}
Requires:       vte291-gtk4%{?_isa} >= %{vte_version}

# Removed in F37
Obsoletes: gnome-console-nautilus < 43~beta

ExcludeArch: %{ix86}

%description
%{summary}.

%prep
%autosetup -p 1 -n %{name}-%{version_no_tilde .}

%build
%meson
%meson_build

%install
%meson_install
%find_lang kgx

%check
desktop-file-validate %{buildroot}%{_datadir}/applications/org.gnome.Console.desktop
appstream-util validate-relax --nonet %{buildroot}%{_metainfodir}/org.gnome.Console.metainfo.xml

%files -f kgx.lang
%license COPYING
%doc NEWS README.md
%{_bindir}/kgx
%{_datadir}/applications/org.gnome.Console.desktop
%{_metainfodir}/org.gnome.Console.metainfo.xml
%{_datadir}/glib-2.0/schemas/org.gnome.Console.gschema.xml
%{_datadir}/dbus-1/services/org.gnome.Console.service
%{_datadir}/icons/hicolor/scalable/apps/org.gnome.Console.svg
%{_datadir}/icons/hicolor/symbolic/apps/org.gnome.Console-symbolic.svg

%changelog
%autochangelog
