%global branch 1.28

Name:          mate-notification-daemon
Version:       %{branch}.5
Release:       %autorelease
Summary:       Notification daemon for MATE Desktop
# Automatically converted from old format: GPLv2+ - review is highly recommended.
License:       GPL-2.0-or-later
URL:           http://mate-desktop.org
Source0:       http://pub.mate-desktop.org/releases/%{branch}/%{name}-%{version}.tar.xz

BuildRequires: desktop-file-utils
BuildRequires: gtk-layer-shell-devel
BuildRequires: libcanberra-devel
BuildRequires: libnotify-devel
BuildRequires: libwnck3-devel
BuildRequires: libxml2-devel
BuildRequires: make
BuildRequires: mate-common
BuildRequires: mate-desktop-devel
BuildRequires: mate-panel-devel

Provides:      desktop-notification-daemon

%description
Notification daemon for MATE Desktop

%prep
%autosetup -p1

#NOCONFIGURE=1 ./autogen.sh

%build
%configure --disable-schemas-compile \
           --enable-x11 \
           --enable-wayland \
           --enable-in-process

make %{?_smp_mflags} V=1

%install
%{make_install}

desktop-file-install                               \
        --delete-original                          \
        --dir=%{buildroot}%{_datadir}/applications \
%{buildroot}/%{_datadir}/applications/mate-notification-properties.desktop

find %{buildroot} -name '*.la' -exec rm -f {} ';'
find %{buildroot} -name '*.a' -exec rm -f {} ';'

# remove desktop file, no need of it
rm -f  %{buildroot}%{_datadir}/applications/mate-notification-daemon.desktop

desktop-file-validate %{buildroot}%{_sysconfdir}/xdg/autostart/mate-notification-daemon.desktop

%find_lang %{name} --with-gnome --all-name


%files -f %{name}.lang
%doc AUTHORS COPYING README
%{_bindir}/mate-notification-properties
%{_datadir}/applications/mate-notification-properties.desktop
%{_datadir}/dbus-1/services/org.freedesktop.mate.Notifications.service
#%%{_libexecdir}/mate-notification-applet
%{_libexecdir}/mate-notification-daemon
#%%{_datadir}/dbus-1/services/org.mate.panel.applet.MateNotificationAppletFactory.service
%{_datadir}/glib-2.0/schemas/org.mate.NotificationDaemon.gschema.xml
%{_datadir}/mate-panel/applets/org.mate.applets.MateNotificationApplet.mate-panel-applet
%{_datadir}/icons/hicolor/*/apps/mate-notification-properties.*
%{_mandir}/man1/mate-notification-properties.1.gz
%{_libdir}/mate-notification-daemon
%{_sysconfdir}/xdg/autostart/mate-notification-daemon.desktop


%changelog
%autochangelog
