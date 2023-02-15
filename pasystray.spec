Name:           pasystray
Version:        0.8.2
Release:        %autorelease
Summary:        PulseAudio system tray
License:        LGPL-2.1-or-later
URL:            https://github.com/christophgysin/pasystray

Source0:        https://github.com/christophgysin/pasystray/archive/%{version}/%{name}-%{version}.tar.gz
# https://bugzilla.redhat.com/show_bug.cgi?id=1471192
# https://bugzilla.redhat.com/show_bug.cgi?id=2035305
Patch1:         pasystray-0.8.0-wayland.patch

BuildRequires:  gcc
BuildRequires:  make
BuildRequires:  automake
BuildRequires:  pkgconfig(libpulse)
BuildRequires:  pkgconfig(avahi-client)
BuildRequires:  pkgconfig(avahi-glib)
BuildRequires:  pkgconfig(libnotify)
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(gtk+-3.0)
BuildRequires:  pkgconfig(appindicator3-0.1)
BuildRequires:  desktop-file-utils
BuildRequires:  libappstream-glib

%if 0%{?fedora}
Recommends:     paman
Recommends:     pavucontrol
Recommends:     pavumeter
#Recommends:     paprefs
#Recommends:     pulseaudio-qpaeq
%endif

%description
A replacement for the deprecated padevchooser.
pasystray allows setting the default PulseAudio source/sink and moving streams
on the fly between sources/sinks without restarting the client applications.

%prep
%autosetup -p1

%build
autoreconf -i
%configure
%make_build

%install
%make_install

desktop-file-validate %{buildroot}/%{_datadir}/applications/%{name}.desktop

mkdir -p %{buildroot}%{_metainfodir}
cat > %{buildroot}%{_metainfodir}/%{name}.metainfo.xml <<EOF
<?xml version="1.0" encoding="UTF-8"?>
<component type="desktop">
  <id>io.github.christophgysin.pasystray</id>
  <metadata_license>CC0-1.0</metadata_license>
  <project_license>LGPL-2.1-or-later</project_license>
  <name>PulseAudio System Tray</name>
  <developer_name>Christoph Gysin</developer_name>
  <summary>Tray icon for controlling PulseAudio</summary>
  <url type="homepage">https://github.com/christophgysin/pasystray/</url>
  <content_rating type="oars-1.1" />
  <description>
    <p>PulseAudio System Tray (pasystray) allows setting the default PulseAudio
       source/sink and moving streams on the fly between sources/sinks without
       restarting the client applications.</p>
  </description>
  <launchable type="desktop-id">pasystray.desktop</launchable>
  <provides>
    <binary>pasystray</binary>
  </provides>
  <releases>
    <release version="%{version}" date="%(date +%F -r %{SOURCE0})"/>
  </releases>
</component>
EOF

appstream-util validate-relax --nonet %{buildroot}%{_metainfodir}/%{name}.metainfo.xml

%files
%{_bindir}/%{name}
%{_datadir}/%{name}
%{_datadir}/pixmaps/%{name}.png
%{_datadir}/applications/%{name}.desktop
%{_datadir}/icons/hicolor/scalable/apps/%{name}.svg
%{_metainfodir}/%{name}.metainfo.xml
%config(noreplace) %{_sysconfdir}/xdg/autostart/%{name}.desktop
%{_mandir}/man1/%{name}.1*
%license LICENSE
%doc README.md

%changelog
%autochangelog
