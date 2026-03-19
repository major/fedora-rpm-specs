%global glib_version 2.72

Name:    xdg-native-messaging-proxy
Version: 0.1.0
Release: %autorelease
Summary: Native messaging host proxy for sandboxed applications

License: LGPL-2.1-or-later
URL:     https://github.com/flatpak/xdg-native-messaging-proxy
Source0: https://github.com/flatpak/xdg-native-messaging-proxy/releases/download/%{version}/%{name}-%{version}.tar.xz

BuildRequires: gcc
BuildRequires: meson
BuildRequires: systemd-rpm-macros
BuildRequires: pkgconfig(gio-unix-2.0) >= %{glib_version}
BuildRequires: pkgconfig(json-glib-1.0)
BuildRequires: pkgconfig(libdex-1)
%{?systemd_requires}

%description
This is a small service which can be used to find native messaging host
manifests, as well as start and stop those native messaging hosts.

Applications running inside a sandbox might have a limited view of the host
which might prevent them from finding and executing native messaging hosts which
exist outside of the sandbox. This proxy is supposed to run outside of any
sandbox, which will make the native messaging hosts outside the sandbox
available to anyone with access to the D-Bus service.

%prep
%autosetup -p1


%build
%meson
%meson_build


%install
%meson_install


%post
%systemd_user_post xdg-native-messaging-proxy.service

%preun
%systemd_user_preun xdg-native-messaging-proxy.service

%postun
%systemd_user_postun xdg-native-messaging-proxy.service


%files
%doc README.md
%license COPYING
%{_datadir}/dbus-1/interfaces/org.freedesktop.NativeMessagingProxy.xml
%{_datadir}/dbus-1/services/org.freedesktop.NativeMessagingProxy.service
%{_userunitdir}/xdg-native-messaging-proxy.service
%{_libexecdir}/xdg-native-messaging-proxy

%changelog
%autochangelog
