Name:           gnome-console
Version:        43.0
Release:        %autorelease
Summary:        Simple user-friendly terminal emulator for the GNOME desktop
License:        GPLv3+
URL:            https://gitlab.gnome.org/GNOME/console
Source:         https://download.gnome.org/sources/gnome-console/43/gnome-console-%{version_no_tilde .}.tar.xz

BuildRequires:  meson >= 0.59.0
BuildRequires:  gcc
BuildRequires:  pkgconfig(gio-2.0) >= 2.66
BuildRequires:  pkgconfig(gtk4)
BuildRequires:  pkgconfig(libadwaita-1)
BuildRequires:  pkgconfig(vte-2.91-gtk4)
BuildRequires:  pkgconfig(libgtop-2.0)
BuildRequires:  pkgconfig(gsettings-desktop-schemas)
BuildRequires:  /usr/bin/desktop-file-validate
BuildRequires:  /usr/bin/appstreamcli

# Removed in F37
Obsoletes: gnome-console-nautilus < 43~beta

%description
%{summary}.

%prep
%autosetup -p 1 -n %{name}-%{version_no_tilde .}
# All these are handled by the RPM filetriggers
# … and -Werror is just terrible
sed -i -r -e '/(werror=|glib_compile_schemas|gtk_update_icon_cache|update_desktop_database)/s/true/false/' meson.build

%build
%meson
%meson_build

%install
%meson_install
%find_lang kgx

%check
desktop-file-validate %{buildroot}%{_datadir}/applications/org.gnome.Console.desktop
appstreamcli validate --no-net %{buildroot}%{_metainfodir}/org.gnome.Console.metainfo.xml

%files -f kgx.lang
%{_bindir}/kgx
%{_datadir}/applications/org.gnome.Console.desktop
%{_metainfodir}/org.gnome.Console.metainfo.xml
%{_datadir}/glib-2.0/schemas/org.gnome.Console.gschema.xml
%{_datadir}/dbus-1/services/org.gnome.Console.service
%{_datadir}/icons/hicolor/scalable/apps/org.gnome.Console.svg
%{_datadir}/icons/hicolor/symbolic/apps/org.gnome.Console-symbolic.svg

%changelog
%autochangelog
