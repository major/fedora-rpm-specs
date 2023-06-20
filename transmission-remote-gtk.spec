Name:           transmission-remote-gtk
Version:        1.6.0
Release:        %autorelease
Summary:        GTK remote control for the Transmission BitTorrent client

License:        GPLv2+
URL:            https://github.com/transmission-remote-gtk/transmission-remote-gtk
Source0:        %{url}/releases/download/%{version}/%{name}-%{version}.tar.xz

BuildRequires:  meson
BuildRequires:  gcc
BuildRequires:  json-glib-devel
BuildRequires:  gtk3-devel
BuildRequires:  glib2-devel
BuildRequires:  libsoup3-devel
BuildRequires:  libappindicator-gtk3-devel
BuildRequires:  GeoIP-devel
BuildRequires:  git

%description
transmission-remote-gtk is a GTK client for remote management of
the Transmission BitTorrent client, using its HTTP RPC protocol.

%prep
%autosetup -p1 -S git

%build
%meson
%meson_build

%install
%meson_install

%find_lang %{name}

%files -f %{name}.lang
%license COPYING
%doc README.md AUTHORS ChangeLog
%{_bindir}/%{name}
%{_datadir}/applications/io.github.TransmissionRemoteGtk.desktop
%{_datadir}/metainfo/io.github.TransmissionRemoteGtk.appdata.xml
%{_datadir}/icons/hicolor/*/apps/%{name}.*
%{_mandir}/man1/%{name}.1*

%changelog
%autochangelog
