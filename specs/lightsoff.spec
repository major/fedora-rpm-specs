%global tarball_version %%(echo %%{version} | tr '~' '.')
%global major_version %%(echo %%{tarball_version} | cut -d "." -f 1)

Name:           lightsoff
Version:        50.0
Release:        %autorelease
Summary:        GNOME Lightsoff game

# Code is under GPLv2+, help is under CC-BY-SA 3.0 Unported
License:        GPL-2.0-or-later AND CC-BY-SA-3.0
URL:            https://wiki.gnome.org/Apps/Lightsoff
Source0:        https://download.gnome.org/sources/%{name}/%{major_version}/%{name}-%{tarball_version}.tar.xz

BuildRequires:  desktop-file-utils
BuildRequires:  gettext
BuildRequires:  itstool
BuildRequires:  meson
BuildRequires:  vala
BuildRequires:  pkgconfig(gtk4)
BuildRequires:  pkgconfig(libadwaita-1)
BuildRequires:  pkgconfig(librsvg-2.0)

%description
A puzzle played on an 5X5 grid with the aim to turn off all the lights. Each
click on a tile toggles the state of the clicked tile and its non-diagonal
neighbors.

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
desktop-file-validate $RPM_BUILD_ROOT%{_datadir}/applications/org.gnome.LightsOff.desktop

%files -f %{name}.lang
%license COPYING
%doc NEWS
%{_bindir}/lightsoff
%{_datadir}/applications/org.gnome.LightsOff.desktop
%{_datadir}/dbus-1/services/org.gnome.LightsOff.service
%{_datadir}/glib-2.0/schemas/org.gnome.LightsOff.gschema.xml
%{_datadir}/icons/hicolor/scalable/apps/org.gnome.LightsOff.svg
%{_datadir}/icons/hicolor/scalable/apps/org.gnome.LightsOff.Devel.svg
%{_datadir}/icons/hicolor/symbolic/apps/org.gnome.LightsOff-symbolic.svg
%{_metainfodir}/org.gnome.LightsOff.metainfo.xml
%{_mandir}/man6/lightsoff.6*


%changelog
%autochangelog
