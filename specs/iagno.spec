%global tarball_version %%(echo %%{version} | tr '~' '.')
%global major_version %%(echo %%{tarball_version} | cut -d "." -f 1)

Name:           iagno
Version:        50.0
Release:        %autorelease
Summary:        GNOME Reversi game

# Automatically converted from old format: GPLv3+ and CC-BY-SA - review is highly recommended.
License:        GPL-3.0-or-later AND LicenseRef-Callaway-CC-BY-SA
URL:            https://wiki.gnome.org/Apps/Iagno
Source0:        https://download.gnome.org/sources/%{name}/%{major_version}/%{name}-%{tarball_version}.tar.xz

BuildRequires:  gcc
BuildRequires:  gettext
BuildRequires:  glib2-devel
BuildRequires:  gsound-devel
BuildRequires:  pkgconfig(glycin-gtk4-2)
BuildRequires:  pkgconfig(gtk4)
BuildRequires:  pkgconfig(libadwaita-1)
BuildRequires:  pkgconfig(librsvg-2.0)
BuildRequires:  libcanberra-devel
BuildRequires:  itstool
BuildRequires:  desktop-file-utils
BuildRequires:  libappstream-glib
BuildRequires:  meson
BuildRequires:  vala

%description
The GNOME version of Reversi. The goal is to control the most disks
on the board.


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
desktop-file-validate $RPM_BUILD_ROOT%{_datadir}/applications/org.gnome.Reversi.desktop


%files -f %{name}.lang
%license COPYING
%{_bindir}/iagno
%{_datadir}/applications/org.gnome.Reversi.desktop
%{_datadir}/dbus-1/services/org.gnome.Reversi.service
%{_datadir}/glib-2.0/schemas/org.gnome.Reversi.gschema.xml
%{_datadir}/iagno/
%{_datadir}/icons/hicolor/scalable/apps/org.gnome.Reversi.svg
%{_datadir}/icons/hicolor/symbolic/apps/org.gnome.Reversi-symbolic.svg
%{_datadir}/metainfo/org.gnome.Reversi.metainfo.xml
%{_mandir}/man6/iagno.6*


%changelog
%autochangelog
