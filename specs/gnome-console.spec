%global gtk4_version 4.19
%global libadwaita_version 1.8
%global vte_version 0.77.0

%global tarball_version %%(echo %%{version} | tr '~' '.')
%global major_version %%(echo %%{tarball_version} | cut -d "." -f 1)

Name:           gnome-console
Version:        50.0
Release:        %autorelease
Summary:        Simple user-friendly terminal emulator for the GNOME desktop

License:        GPL-3.0-or-later
URL:            https://gitlab.gnome.org/GNOME/console
Source:         https://download.gnome.org/sources/%{name}/%{major_version}/%{name}-%{tarball_version}.tar.xz

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
# check for human errors
if [ `echo "%{version}" | grep -cE "\.alpha|\.beta|\.rc"` = "1" ]; then echo "Error: Use tilde in Version field in front of alpha/beta/rc; checked '%{version}'" 1>&2; exit 1; fi

%autosetup -p 1 -n %{name}-%{tarball_version}

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
