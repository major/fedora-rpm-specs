# Review: https://bugzilla.redhat.com/show_bug.cgi?id=499282

%global minorversion 0.9
%global xfceversion 4.20

Name:           xfce4-notifyd
Version:        0.9.7
Release:        %autorelease
Summary:        Simple notification daemon for Xfce

# Automatically converted from old format: GPLv2 - review is highly recommended.
License:        GPL-2.0-only
URL:            http://goodies.xfce.org/projects/applications/xfce4-notifyd
#VCS:           git:git://http://git.xfce.org/apps/xfce4-notifyd/
Source0:        http://archive.xfce.org/src/apps/%{name}/%{minorversion}/%{name}-%{version}.tar.bz2

BuildRequires:  make
BuildRequires:  gcc-c++
BuildRequires:  gtk3-devel >= 3.20.0
BuildRequires:  libxfce4ui-devel >= %{xfceversion}
BuildRequires:  libxfce4util-devel >= %{xfceversion}
BuildRequires:  xfconf-devel >= %{xfceversion}
BuildRequires:  xfce4-panel-devel >= %{xfceversion}
BuildRequires:  glib2-devel >= 2.42.0
BuildRequires:  libnotify-devel >= 0.7.0
BuildRequires:  sqlite-devel
BuildRequires:  desktop-file-utils
BuildRequires:  intltool
BuildRequires:  systemd

Requires:       dbus
Requires:       hicolor-icon-theme
# for compatibility this package provides
Provides:       desktop-notification-daemon
# and obsoletes all notification-daemon-xfce releases
Obsoletes:      notification-daemon-xfce <= 0.3.7


%description
Xfce4-notifyd is a simple, visually-appealing notification daemon for Xfce 
that implements the freedesktop.org desktop notifications specification.
Features:
* Themable using the GTK+ theming mechanism
* Visually appealing: rounded corners, shaped windows
* Supports transparency and fade effects


%prep
%setup -q


%build
%configure
%make_build

%install
%make_install

desktop-file-validate %{buildroot}%{_datadir}/applications/%{name}-config.desktop
%find_lang %{name}

# remove libtool archives
find %{buildroot} -name \*.la -exec rm {} \;


%files -f %{name}.lang
%license COPYING
%doc AUTHORS NEWS TODO
%{_bindir}/xfce4-notifyd-config
%{_libdir}/xfce4/notifyd/
%{_libdir}/xfce4/panel/plugins/libnotification-plugin.so
%{_datadir}/applications/xfce4-notifyd-config.desktop
%{_datadir}/themes/Default/xfce-notify-4.0/
%{_datadir}/themes/Smoke/
%{_datadir}/themes/ZOMG-PONIES!/
%{_datadir}/themes/Bright/
%{_datadir}/themes/Retro/
%{_datadir}/themes/XP-Balloon/
%{_datadir}/icons/hicolor/*/*/*
%{_datadir}/xfce4/panel/plugins/notification-plugin.desktop
%{_mandir}/man1/xfce4-notifyd-config.1.*
%{_sysconfdir}/xdg/autostart/%{name}.desktop
%{_userunitdir}/xfce4-notifyd.service
%{_datadir}/dbus-1/services/org.xfce.xfce4-notifyd.Notifications.service
%{_datadir}/dbus-1/services/org.xfce.xfce4-notifyd.Notifyd.service

%changelog
%autochangelog
