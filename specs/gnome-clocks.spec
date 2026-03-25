%global geoclue2_version 2.6.0
%global gtk4_version 4.5
%global libadwaita_version 1.5

%global tarball_version %%(echo %%{version} | tr '~' '.')
%global major_version %%(echo %%{tarball_version} | cut -d "." -f 1)

Name:           gnome-clocks
Version:        50.0
Release:        %autorelease
Summary:        Clock application designed for GNOME 3

# Sources are under GPL-2.0-or-later, Appdata is under CC0-1.0 and help is
# under CC-BY-SA-3.0.
License:        GPL-2.0-or-later AND CC-BY-SA-3.0 AND CC0-1.0
URL:            https://wiki.gnome.org/Apps/Clocks
Source0:        https://download.gnome.org/sources/%{name}/%{major_version}/%{name}-%{tarball_version}.tar.xz

BuildRequires:  meson
BuildRequires:  desktop-file-utils
BuildRequires:  gettext
BuildRequires:  itstool
BuildRequires:  libappstream-glib
BuildRequires:  vala

BuildRequires:  pkgconfig(geocode-glib-2.0)
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(gnome-desktop-4)
BuildRequires:  pkgconfig(gobject-2.0)
BuildRequires:  pkgconfig(gsound)
BuildRequires:  pkgconfig(gtk4) >= %{gtk4_version}
BuildRequires:  pkgconfig(gweather4)
BuildRequires:  pkgconfig(libgeoclue-2.0) >= %{geoclue2_version}
BuildRequires:  pkgconfig(libadwaita-1) >= %{libadwaita_version}
BuildRequires:  vorbis-tools

Requires:       geoclue2-libs%{?_isa} >= %{geoclue2_version}
Requires:       gtk4%{?_isa} >= %{gtk4_version}
Requires:       libadwaita%{?_isa} >= %{libadwaita_version}

%description
Clock application designed for GNOME 3

%prep
# check for human errors
if [ `echo "%{version}" | grep -cE "\.alpha|\.beta|\.rc"` = "1" ]; then echo "Error: Use tilde in Version field in front of alpha/beta/rc; checked '%{version}'" 1>&2; exit 1; fi

%autosetup -p1 -n %{name}-%{tarball_version}

%build
%meson
%meson_build

%install
%meson_install
%find_lang gnome-clocks --with-gnome

%check
desktop-file-validate $RPM_BUILD_ROOT%{_datadir}/applications/org.gnome.clocks.desktop

%files -f gnome-clocks.lang
%doc AUTHORS.md NEWS README.md
%license LICENSE.md
%{_bindir}/gnome-clocks
%{_datadir}/icons/hicolor/scalable/apps/org.gnome.clocks.svg
%{_datadir}/icons/hicolor/symbolic/apps/org.gnome.clocks-symbolic.svg
%{_datadir}/applications/org.gnome.clocks.desktop
%{_datadir}/dbus-1/services/org.gnome.clocks.service
%{_datadir}/glib-2.0/schemas/org.gnome.clocks.gschema.xml
%dir %{_datadir}/gnome-shell/
%dir %{_datadir}/gnome-shell/search-providers/
%{_datadir}/gnome-shell/search-providers/org.gnome.clocks.search-provider.ini
%{_metainfodir}/org.gnome.clocks.metainfo.xml
%{_datadir}/sounds/gnome/default/alarms/*.oga

%changelog
%autochangelog
