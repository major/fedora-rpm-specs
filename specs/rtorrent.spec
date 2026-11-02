%global forgeurl https://github.com/rakshasa/rtorrent
Version:          0.16.27
%forgemeta

Name:             rtorrent
# OpenSSL exception, see README
# Automatically converted from old format: GPLv2+ with exceptions - review is highly recommended.
License:          GPL-2.0-or-later WITH OpenSSL-exception
Release:          %autorelease
Summary:          BitTorrent client based on libtorrent
URL:              %{forgeurl}
Source0:          %{forgeurl}/releases/download/v%{version}/rtorrent-%{version}.tar.gz
Source1:          rtorrent.1

BuildRequires:    cppunit-devel
BuildRequires:    gcc-c++
BuildRequires:    libtorrent-devel >= 0.16.27
BuildRequires:    ncurses-devel
BuildRequires:    pkgconfig
BuildRequires:    xmlrpc-c-devel
BuildRequires:    zlib-devel

%description
A BitTorrent client using libtorrent, which on high-bandwidth connections is
able to seed at 3 times the speed of the official client. Using
ncurses its ideal for use with screen or dtach. It supports
saving of sessions and allows the user to add and remove torrents and scanning
of directories for torrent files to seed and/or download.

%prep
%autosetup -p1
for file in AUTHORS README.md doc/rtorrent.rc COPYING
do
    chmod -x "$file"
done

# Avoid an attempt to re-run autoconf.
touch -r aclocal.m4 scripts/common.m4

%build
%configure --with-xmlrpc-c --enable-ipv6
%make_build

%check
%make_build check

%install
%make_install
install -Dpm 0644 %SOURCE1 %{buildroot}/%{_mandir}/man1/rtorrent.1

%files
%doc AUTHORS README.md doc/rtorrent.rc
%license COPYING
%{_bindir}/%{name}
%{_mandir}/man1/rtorrent.1*
%dir %{_datadir}/%{name}
%dir %{_datadir}/%{name}/lua
%{_datadir}/%{name}/lua/%{name}.lua

%changelog
%autochangelog
