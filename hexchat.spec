%global app_id io.github.Hexchat

Summary:   A popular and easy to use graphical IRC (chat) client
Name:      hexchat
Version:   2.16.1
Release:   %autorelease
License:   GPLv2+
URL:       https://hexchat.github.io
Source:    https://dl.hexchat.net/hexchat/%{name}-%{version}.tar.xz

BuildRequires: gcc
BuildRequires: meson
BuildRequires: hicolor-icon-theme
BuildRequires: pkgconfig(glib-2.0)
BuildRequires: pkgconfig(gtk+-2.0)
BuildRequires: pkgconfig(dbus-glib-1)
BuildRequires: pkgconfig(libcanberra)
BuildRequires: pkgconfig(libproxy-1.0)
BuildRequires: pkgconfig(iso-codes)
BuildRequires: pkgconfig(openssl)
BuildRequires: pkgconfig(python3)
BuildRequires: pkgconfig(libpci)
BuildRequires: pkgconfig(lua)
BuildRequires: perl-devel, perl-ExtUtils-Embed
BuildRequires: python3-cffi
Requires:      python3-cffi
Requires:      (enchant or enchant2)
Recommends:    sound-theme-freedesktop

%description
HexChat is an easy to use graphical IRC chat client for the X Window System.
It allows you to join multiple IRC channels (chat rooms) at the same time, 
talk publicly, private one-on-one conversations etc. Even file transfers
are possible.

%package devel
Summary: Development files for %{name}
Requires: %{name}%{?_isa} = %{version}-%{release}
%description devel
This package contains the development files for %{name}.

%prep
%autosetup

%build
%meson -Dwith-lua=lua
%meson_build

%install
%meson_install
%find_lang %{name}

%files -f %{name}.lang
%{_bindir}/hexchat
%license COPYING
%doc readme.md
%dir %{_libdir}/hexchat
%dir %{_libdir}/hexchat/plugins
%{_libdir}/hexchat/plugins/checksum.so
%{_libdir}/hexchat/plugins/fishlim.so
%{_libdir}/hexchat/plugins/lua.so
%{_libdir}/hexchat/plugins/sysinfo.so
%{_libdir}/hexchat/plugins/perl.so
%{_libdir}/hexchat/plugins/python.so
%{_libdir}/hexchat/python
%{_datadir}/applications/%{app_id}.desktop
%{_datadir}/icons/hicolor/*/apps/%{app_id}.*
%{_datadir}/metainfo/%{app_id}.appdata.xml
%{_datadir}/dbus-1/services/org.hexchat.service.service
%{_mandir}/man1/*.gz

%files devel
%{_includedir}/hexchat-plugin.h
%{_libdir}/pkgconfig/hexchat-plugin.pc

%changelog
%autochangelog
