%global forgeurl https://github.com/rakshasa/libtorrent
Version:       0.16.27
%forgemeta

Name:          libtorrent
License:       GPL-2.0-or-later
Release:       %autorelease
Summary:       BitTorrent library with a focus on high performance & good code
URL:           %{forgeurl}
Source0:       https://github.com/rakshasa/rtorrent/releases/download/v%{version}/libtorrent-%{version}.tar.gz

BuildRequires: cppunit-devel
BuildRequires: curl-devel
BuildRequires: gcc
BuildRequires: gcc-c++
BuildRequires: make
BuildRequires: openssl-devel
BuildRequires: pkgconfig
BuildRequires: zlib-devel

%description
LibTorrent is a BitTorrent library written in C++ for *nix, with a focus 
on high performance and good code. The library differentiates itself 
from other implementations by transferring directly from file pages to
the network stack. On high-bandwidth connections it is able to seed at 
3 times the speed of the official client.

%package devel
Summary: Libtorrent development environment
Requires: %{name}%{?_isa} = %{version}-%{release}

%description devel
Header and library definition files for developing applications
with the libtorrent libraries.

%prep
%forgeautosetup -p1

%build
%configure
%make_build

%install
%make_install
rm -f %{buildroot}%{_libdir}/*.la

%check
%make_build check

%ldconfig_scriptlets

%files
%doc AUTHORS README.md
%license COPYING
%{_libdir}/libtorrent.so.*

%files devel
%{_libdir}/pkgconfig/libtorrent.pc
%{_includedir}/torrent
%{_libdir}/*.so

%changelog
%autochangelog
