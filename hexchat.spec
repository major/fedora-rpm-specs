%global app_id io.github.Hexchat

Summary:   A popular and easy to use graphical IRC (chat) client
Name:      hexchat
Version:   2.16.2
Release:   %autorelease
License:   GPLv2+
URL:       https://hexchat.github.io
Source:    https://github.com/hexchat/hexchat/releases/download/v%{version}/hexchat-%{version}.tar.xz
# Fix release date
Patch0:    https://github.com/hexchat/hexchat/commit/70069cd50eb07e8a40ac9b0efbb83fcb91a78b99.patch
# replace hexchat.net links
Patch1:    https://github.com/hexchat/hexchat/commit/cc60ad275a56126904df0b5e37cfd20db22cb359.patch

BuildRequires: gcc
BuildRequires: meson
BuildRequires: hicolor-icon-theme
BuildRequires: pkgconfig(glib-2.0)
BuildRequires: pkgconfig(gtk+-2.0)
BuildRequires: pkgconfig(dbus-glib-1)
BuildRequires: pkgconfig(libcanberra)
BuildRequires: pkgconfig(iso-codes)
BuildRequires: pkgconfig(openssl)
BuildRequires: pkgconfig(python3)
BuildRequires: pkgconfig(libpci)
BuildRequires: pkgconfig(lua)
BuildRequires: perl-devel, perl-ExtUtils-Embed
BuildRequires: python3-cffi
BuildRequires: desktop-file-utils
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
%autosetup -p1

%build
%meson -Dwith-lua=lua %{?flatpak:-Ddbus-service-use-appid=true}
%meson_build

%install
%meson_install
%find_lang %{name}

desktop-file-validate %{buildroot}/%{_datadir}/applications/%{app_id}.desktop

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
%if 0%{?flatpak}
%{_datadir}/dbus-1/services/%{app_id}.service
%else
%{_datadir}/dbus-1/services/org.hexchat.service.service
%endif
%{_mandir}/man1/hexchat.1*

%files devel
%{_includedir}/hexchat-plugin.h
%{_libdir}/pkgconfig/hexchat-plugin.pc

%changelog
%autochangelog
