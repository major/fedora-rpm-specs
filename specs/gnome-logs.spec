%global tarball_version %%(echo %%{version} | tr '~' '.')
%global major_version %%(echo %%{tarball_version} | cut -d "." -f 1)

Name:           gnome-logs
Version:        50.0
Release:        %autorelease
Summary:        Log viewer for the systemd journal

# data/org.gnome.Logs.metainfo.xml.in is CC0-1.0
# data/icons/scalable/org.gnome.Logs.svg is CC-BY-3.0
License:        GPL-3.0-or-later AND CC0-1.0 AND CC-BY-3.0
URL:            https://wiki.gnome.org/Apps/Logs
Source0:        https://download.gnome.org/sources/%{name}/%{major_version}/%{name}-%{tarball_version}.tar.xz

BuildRequires:  desktop-file-utils
BuildRequires:  docbook-dtds
BuildRequires:  docbook-style-xsl
BuildRequires:  gcc
BuildRequires:  itstool
BuildRequires:  libxslt
BuildRequires:  meson
BuildRequires:  pkgconfig(gtk4)
BuildRequires:  pkgconfig(libadwaita-1)
BuildRequires:  pkgconfig(libsystemd)
BuildRequires:  /usr/bin/appstream-util
Requires:       gsettings-desktop-schemas

%description
A log viewer for the systemd journal.

%prep
# check for human errors
if [ `echo "%{version}" | grep -cE "\.alpha|\.beta|\.rc"` = "1" ]; then echo "Error: Use tilde in Version field in front of alpha/beta/rc; checked '%{version}'" 1>&2; exit 1; fi

%autosetup -p1 -n %{name}-%{tarball_version}


%build
%meson -Dman=true
%meson_build


%install
%meson_install
%find_lang %{name} --with-gnome


%check
%meson_test


%files -f %{name}.lang
%doc AUTHORS README NEWS
%license COPYING
%{_bindir}/%{name}
%{_datadir}/applications/org.gnome.Logs.desktop
%{_datadir}/dbus-1/services/org.gnome.Logs.service
%{_datadir}/glib-2.0/schemas/org.gnome.Logs.*.xml
%{_datadir}/icons/hicolor/scalable/apps/org.gnome.Logs.svg
%{_datadir}/icons/hicolor/symbolic/apps/org.gnome.Logs-symbolic.svg
%{_datadir}/metainfo/org.gnome.Logs.metainfo.xml
%{_mandir}/man1/gnome-logs.1*


%changelog
%autochangelog
