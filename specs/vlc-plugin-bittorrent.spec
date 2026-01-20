%global srcname vlc-bittorrent

Name:           vlc-plugin-bittorrent
Version:        2.16
Release:        %autorelease
Summary:        Bittorrent plugin for VLC
License:        GPL-3.0-or-later
URL:            https://github.com/johang/vlc-bittorrent
Source:         %{url}/archive/v%{version}/%{srcname}-%{version}.tar.gz

BuildRequires:  autoconf-archive
BuildRequires:  gcc-c++
BuildRequires:  libtool
BuildRequires:  desktop-file-utils
BuildRequires:  pkgconfig(vlc-plugin) >= 3.0.0
BuildRequires:  pkgconfig(libtorrent-rasterbar) >= 1.0.0

Requires:       vlc-plugins-base%{?_isa}

Obsoletes:      vlc-bittorrent < 2.14-4
Provides:       vlc-bittorrent = %{version}-%{release}


%description
With vlc-bittorrent, you can open a .torrent file or magnet link with
VLC and stream any media that it contains.


%prep
%autosetup -n %{srcname}-%{version} -p1
autoreconf -vif
# do not hardcode vlc path, for flatpak builds
sed -i -e 's|/usr/bin/||' data/%{name}.desktop


%build
%if 0%{?fedora} >= 41 || 0%{?rhel} >= 10
# https://fedoraproject.org/wiki/Changes/OpensslDeprecateEngine
CXXFLAGS="$CXXFLAGS -DOPENSSL_NO_ENGINE"
%endif
%configure --disable-static --libdir=%{vlc_plugindir}/access
%make_build


%install
%make_install
# still needed for RHEL 9 and older
find %{buildroot}%{_libdir} -name "*.la" -delete


%check
desktop-file-validate %{buildroot}%{_datadir}/applications/%{name}.desktop


%files
%license LICENSE
%doc README.md
%{vlc_plugindir}/access/libaccess_bittorrent_plugin.so
%{_datadir}/applications/%{name}.desktop


%changelog
%autochangelog
