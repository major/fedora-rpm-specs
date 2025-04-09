%global branch 1.28

Name:          mate-power-manager
Version:       %{branch}.1
Release:       %autorelease
Summary:       MATE power management service
# Automatically converted from old format: GPLv2+ - review is highly recommended.
License:       GPL-2.0-or-later
URL:           http://pub.mate-desktop.org
Source0:       http://pub.mate-desktop.org/releases/%{branch}/%{name}-%{version}.tar.xz

# https://github.com/mate-desktop/mate-power-manager/commit/a0aeec5
Patch1:        mate-power-manager_0001-Keyboard-backlight-handling-improvements-404.patch

BuildRequires: cairo-devel
BuildRequires: dbus-glib-devel
BuildRequires: desktop-file-utils
BuildRequires: libcanberra-devel
BuildRequires: glib2-devel
BuildRequires: gtk3-devel
BuildRequires: libnotify-devel
BuildRequires: libsecret-devel
BuildRequires: make
BuildRequires: mate-common
BuildRequires: mate-desktop-devel
BuildRequires: mate-panel-devel
BuildRequires: mesa-libGL-devel
BuildRequires: popt-devel
BuildRequires: upower-devel
BuildRequires: polkit-devel

%description
MATE Power Manager uses the information and facilities provided by UPower
displaying icons and handling user callbacks in an interactive MATE session.


%prep
%autosetup -p1

#NOCONFIGURE=1 ./autogen.sh

%build
%configure \
     --disable-schemas-compile

make %{?_smp_mflags} V=1

%install
%{make_install}

desktop-file-install                               \
     --delete-original                             \
     --dir=%{buildroot}%{_datadir}/applications    \
%{buildroot}%{_datadir}/applications/*.desktop

%check
desktop-file-validate %{buildroot}%{_sysconfdir}/xdg/autostart/mate-power-manager.desktop

%find_lang %{name} --with-gnome --all-name


%files  -f %{name}.lang
%doc AUTHORS COPYING README
%{_mandir}/man1/mate-power-*.*
%{_bindir}/mate-power-manager
%{_bindir}/mate-power-preferences
%{_bindir}/mate-power-statistics
%{_sbindir}/mate-power-backlight-helper
%{_datadir}/applications/mate-*.desktop
%{_datadir}/dbus-1/services/*.service
%{_datadir}/mate-power-manager/
%{_datadir}/icons/hicolor/*/apps/mate-*.*
%{_datadir}/polkit-1/actions/org.mate.power.policy
%{_datadir}/mate-panel/applets/org.mate.BrightnessApplet.mate-panel-applet
%{_datadir}/mate-panel/applets/org.mate.InhibitApplet.mate-panel-applet
%{_datadir}/glib-2.0/schemas/org.mate.power-manager.gschema.xml
%{_sysconfdir}/xdg/autostart/mate-power-manager.desktop
%{_libexecdir}/mate-brightness-applet
%{_libexecdir}/mate-inhibit-applet


%changelog
%autochangelog
