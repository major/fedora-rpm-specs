Name:    qbittorrent
Summary: A Bittorrent Client
Epoch:   1
Version: 5.2.3
Release: %autorelease
# Automatically converted from old format: GPLv2+ - review is highly recommended.
License: GPL-2.0-or-later
URL:     https://www.qbittorrent.org

Source0: https://downloads.sourceforge.net/%{name}/%{name}-%{version}.tar.xz
Source1: https://downloads.sourceforge.net/%{name}/%{name}-%{version}.tar.xz.asc
Source2: https://github.com/qbittorrent/qBittorrent/raw/master/5B7CC9A2.asc
Source3: qbittorrent-nox.README

ExcludeArch:   %{ix86}

BuildRequires: appstream
BuildRequires: boost-devel >= 1.76
BuildRequires: cmake
BuildRequires: cmake(Qt6Core)
BuildRequires: cmake(Qt6DBus)
BuildRequires: cmake(Qt6Gui)
BuildRequires: cmake(Qt6LinguistTools)
BuildRequires: cmake(Qt6Network)
BuildRequires: cmake(Qt6Sql)
BuildRequires: cmake(Qt6Svg)
BuildRequires: cmake(Qt6Widgets)
BuildRequires: cmake(Qt6Xml)
BuildRequires: desktop-file-utils
BuildRequires: gcc-c++
BuildRequires: gnupg2
BuildRequires: ninja-build
BuildRequires: openssl-devel
BuildRequires: qt6-qtbase-private-devel
BuildRequires: rb_libtorrent-devel >= 1.2.19
BuildRequires: systemd
BuildRequires: systemd-rpm-macros
BuildRequires: zlib-ng-compat-static

Requires: python3
Requires: qt6-qtsvg%{?_isa}

%description
A Bittorrent client using rb_libtorrent and a Qt6 Graphical User Interface.
It aims to be as fast as possible and to provide multi-OS, unicode support.

%package nox
Summary: A Headless Bittorrent Client

%description nox
A Headless Bittorrent client using rb_libtorrent.
It aims to be as fast as possible and to provide multi-OS, unicode support.

%prep
%{gpgverify} --keyring='%{SOURCE2}' --signature='%{SOURCE1}' --data='%{SOURCE0}'
%autosetup -p1
cp %{SOURCE3} .

%build
%define _vpath_builddir build-nox
%cmake \
 -DSYSTEMD=ON \
 -DGUI=OFF

%cmake_build

# Build gui version
%define _vpath_builddir build-gui
%cmake

%cmake_build

%install
# install headless version
%define _vpath_builddir build-nox
%cmake_install

# install gui version
%define _vpath_builddir build-gui
%cmake_install

%check
desktop-file-validate %{buildroot}%{_datadir}/applications/org.qbittorrent.qBittorrent.desktop
appstreamcli validate --no-net %{buildroot}%{_metainfodir}/org.qbittorrent.qBittorrent.metainfo.xml
appstreamcli validate --no-net %{buildroot}%{_metainfodir}/org.qbittorrent.qBittorrent-nox.metainfo.xml

%post nox
%systemd_post qbittorrent-nox@.service

%preun nox
%systemd_preun qbittorrent-nox@.service

%postun nox
%systemd_postun_with_restart qbittorrent-nox@.service

%files
%license COPYING
%doc README.md AUTHORS Changelog
%{_bindir}/qbittorrent
%{_metainfodir}/org.qbittorrent.qBittorrent.metainfo.xml
%{_datadir}/applications/org.qbittorrent.qBittorrent.desktop
%{_datadir}/icons/hicolor/*/apps/qbittorrent.*
%{_datadir}/icons/hicolor/*/status/qbittorrent-tray*
%{_mandir}/man1/qbittorrent.1*
%{_mandir}/ru/man1/qbittorrent.1*

%files nox
%license COPYING
%doc qbittorrent-nox.README AUTHORS Changelog
%{_bindir}/qbittorrent-nox
%{_metainfodir}/org.qbittorrent.qBittorrent-nox.metainfo.xml
%{_unitdir}/qbittorrent-nox@.service
%{_mandir}/man1/qbittorrent-nox.1*
%{_mandir}/ru/man1/qbittorrent-nox.1*

%changelog
%autochangelog
