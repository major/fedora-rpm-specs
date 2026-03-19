%global tarball_version %%(echo %%{version} | tr '~' '.')
%global major_version %%(echo %%{tarball_version} | cut -d "." -f 1)

Name:           gnome-power-manager
Version:        50.0
Release:        %autorelease
Summary:        GNOME power management service

License:        GPL-2.0-or-later
URL:            https://projects.gnome.org/gnome-power-manager/
Source0:        https://download.gnome.org/sources/%{name}/%{major_version}/%{name}-%{tarball_version}.tar.xz

BuildRequires:  gcc
BuildRequires:  gettext
BuildRequires:  meson
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(gobject-2.0)
BuildRequires:  pkgconfig(gio-2.0)
BuildRequires:  pkgconfig(gtk4)
BuildRequires:  pkgconfig(cairo)
BuildRequires:  pkgconfig(upower-glib)
BuildRequires:  docbook-utils
BuildRequires:  desktop-file-utils
BuildRequires:  libappstream-glib

%description
GNOME Power Manager uses the information and facilities provided by UPower
displaying icons and handling user callbacks in an interactive GNOME session.

%prep
# check for human errors
if [ `echo "%{version}" | grep -cE "\.alpha|\.beta|\.rc"` = "1" ]; then echo "Error: Use tilde in Version field in front of alpha/beta/rc; checked '%{version}'" 1>&2; exit 1; fi

%autosetup -p1 -n %{name}-%{tarball_version}

%build
%meson
%meson_build

%install
%meson_install
%find_lang %{name} --with-gnome

%check
desktop-file-validate %{buildroot}%{_datadir}/applications/org.gnome.PowerStats.desktop
appstream-util --nonet validate-relax %{buildroot}%{_datadir}/metainfo/org.gnome.PowerStats.appdata.xml

%files -f %{name}.lang
%license COPYING
%doc AUTHORS README.md
%{_bindir}/gnome-power-statistics
%{_datadir}/applications/org.gnome.PowerStats.desktop
%{_datadir}/glib-2.0/schemas/org.gnome.power-manager.gschema.xml
%{_datadir}/icons/hicolor/*/apps/org.gnome.PowerStats*.*
%{_datadir}/metainfo/org.gnome.PowerStats.appdata.xml
%{_mandir}/man1/gnome-power-statistics.1*

%changelog
%autochangelog
