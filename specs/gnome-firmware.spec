%global app_id org.gnome.Firmware

Name:           gnome-firmware
Version:        49.0
Release:        %autorelease
Summary:        Install firmware on devices

License:        GPL-2.0-or-later
URL:            https://gitlab.gnome.org/World/gnome-firmware
Source:         %{url}/-/archive/%{version}/gnome-firmware-%{version}.tar.gz

BuildRequires:  gcc
BuildRequires:  meson >= 0.59.0

# -Dsystemd=true
BuildRequires:  systemd-devel
# -Dman=true
BuildRequires:  help2man
# For fixing the man page
BuildRequires:  python3

BuildRequires:  pkgconfig(fwupd) >= 1.9.16
BuildRequires:  pkgconfig(gio-2.0) >= 2.74.0
BuildRequires:  pkgconfig(gtk4) >= 4.2.0
BuildRequires:  pkgconfig(xmlb) >= 0.3.8
BuildRequires:  pkgconfig(libadwaita-1) >= 1.8

BuildRequires:  desktop-file-utils
# Still required by guidelines for now
# (https://pagure.io/packaging-committee/issue/1053):
BuildRequires:  libappstream-glib
# Matches what gnome-software and others use:
BuildRequires:  appstream

Requires:       hicolor-icon-theme

%description
This application can:

- Upgrade, downgrade and reinstall firmware on devices supported by fwupd.
- Unlock locked fwupd devices
- Verify firmware on supported devices
- Display all releases for a fwupd device


%prep
%autosetup -p1 -n gnome-firmware-%{version}


%conf
%meson -Dconsolekit=true -Dsystemd=true -Dman=true


%build
%meson_build


%install
%meson_install
%find_lang gnome-firmware --with-gnome

# Unicode characters in --help output don’t play well with help2man
# https://gitlab.gnome.org/World/gnome-firmware/-/issues/74
%{python3} <<'EOF'
man = "%{buildroot}%{_mandir}/man1/gnome-firmware.1"
with open(man, "rb") as bad:
    text = bad.read()
text = text.replace(b"\xe2\x5c\x26\x2e\xa6", rb"\[u2026]")
with open(man, "wb") as good:
    good.write(text)
EOF


%check
desktop-file-validate '%{buildroot}%{_datadir}/applications/%{app_id}.desktop'
# Still required by guidelines for now
# (https://pagure.io/packaging-committee/issue/1053):
appstream-util validate-relax --nonet \
    '%{buildroot}%{_metainfodir}/%{app_id}.metainfo.xml'
# Matches what gnome-software and others use:
appstreamcli validate --no-net --explain \
    '%{buildroot}%{_metainfodir}/%{app_id}.metainfo.xml'


%files -f %{name}.lang
%license COPYING
%doc README.md
%doc MAINTAINERS

%{_bindir}/gnome-firmware
%{_mandir}/man1/gnome-firmware.1*

%{_datadir}/icons/hicolor/scalable/apps/%{app_id}.svg
%{_datadir}/icons/hicolor/symbolic/apps/%{app_id}-symbolic.svg

%{_datadir}/applications/%{app_id}.desktop
%{_metainfodir}/%{app_id}.metainfo.xml

%{_datadir}/glib-2.0/schemas/%{app_id}.gschema.xml
%{_datadir}/dbus-1/services/%{app_id}.service


%changelog
%autochangelog
