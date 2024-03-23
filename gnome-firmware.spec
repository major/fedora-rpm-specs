%global uuid    org.gnome.Firmware
%global tarball_version %%(echo %{version} | tr '~' '.')

Name:           gnome-firmware
Version:        46.0
Release:        %autorelease
Summary:        Install firmware on devices

License:        GPL-2.0-or-later
URL:            https://gitlab.gnome.org/World/gnome-firmware
Source0:        %{url}/-/archive/%{tarball_version}/%{name}-%{tarball_version}.tar.gz

BuildRequires:  desktop-file-utils
BuildRequires:  gcc
BuildRequires:  help2man
BuildRequires:  libappstream-glib
BuildRequires:  meson >= 0.46.0
BuildRequires:  systemd-devel
BuildRequires:  pkgconfig(appstream-glib)
BuildRequires:  pkgconfig(fwupd) >= 1.8.11
BuildRequires:  pkgconfig(gio-2.0) >= 2.74.0
BuildRequires:  pkgconfig(gtk4) >= 4.6.0
BuildRequires:  pkgconfig(xmlb) >= 0.1.7
BuildRequires:  pkgconfig(libadwaita-1) >= 1.3.99

Requires:       hicolor-icon-theme

%description
This application can:

- Upgrade, downgrade and reinstall firmware on devices supported by fwupd.
- Unlock locked fwupd devices
- Verify firmware on supported devices
- Display all releases for a fwupd device

%prep
%autosetup -p1 -n %{name}-%{tarball_version}

%build
%meson -Dman=true
%meson_build

%install
%meson_install
%find_lang %{name} --with-gnome

%check
appstream-util validate-relax --nonet %{buildroot}%{_metainfodir}/%{uuid}.metainfo.xml
desktop-file-validate %{buildroot}%{_datadir}/applications/%{uuid}.desktop

%files -f %{name}.lang
%license COPYING
%doc README.md MAINTAINERS
%{_bindir}/%{name}
%{_datadir}/applications/*.desktop
%{_datadir}/icons/hicolor/*/*/*.svg
%{_mandir}/man1/*.1.*
%{_metainfodir}/*.xml

%changelog
%autochangelog
