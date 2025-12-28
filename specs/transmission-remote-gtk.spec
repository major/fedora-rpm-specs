%global app_id  io.github.TransmissionRemoteGtk

Name:           transmission-remote-gtk
Version:        1.7.0
Release:        %autorelease
Summary:        GTK remote control for the Transmission BitTorrent client

# the project is generally GPLv2+, except:
# src/bencode.*: public domain
# src/hig.*, src/torrent-cell-renderer.*: GPLv2
License:        GPL-2.0-or-later AND GPL-2.0-only AND LicenseRef-Fedora-Public-Domain
URL:            https://github.com/transmission-remote-gtk/transmission-remote-gtk
Source0:        %{url}/releases/download/%{version}/%{name}-%{version}.tar.xz

# https://fedoraproject.org/wiki/Changes/EncourageI686LeafRemoval
ExcludeArch:    %{ix86}

BuildRequires:  desktop-file-utils
BuildRequires:  gcc
BuildRequires:  gettext
BuildRequires:  git-core
BuildRequires:  libappstream-glib
BuildRequires:  meson
BuildRequires:  python3-docutils
# required dependencies
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(gtk+-3.0)
BuildRequires:  pkgconfig(json-glib-1.0)
BuildRequires:  pkgconfig(libsoup-3.0)
# optional dependencies
BuildRequires:  pkgconfig(ayatana-appindicator3-0.1)

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

%check
desktop-file-validate %{buildroot}%{_datadir}/applications/%{app_id}.desktop
appstream-util validate-relax --nonet %{buildroot}%{_metainfodir}/%{app_id}.appdata.xml

%files -f %{name}.lang
%license COPYING
%doc README.md AUTHORS ChangeLog
%{_bindir}/%{name}
%{_datadir}/applications/%{app_id}.desktop
%{_datadir}/icons/hicolor/*/apps/%{name}.*
%{_mandir}/man1/%{name}.1*
%{_metainfodir}/%{app_id}.appdata.xml

%changelog
%autochangelog
