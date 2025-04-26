%global branch 1.28

Name:          mate-session-manager
Summary:       MATE Desktop session manager
# Automatically converted from old format: GPLv2+ - review is highly recommended.
License:       GPL-2.0-or-later
Version:       %{branch}.0
Release:       %autorelease
Source0:       http://pub.mate-desktop.org/releases/%{branch}/%{name}-%{version}.tar.xz

# https://github.com/mate-desktop/mate-session-manager/commit/5424817
Patch1:        mate-session-manager_0001-Use-g_info-for-screensaver-left-the-bus-message.patch

BuildRequires: dbus-glib-devel
BuildRequires: desktop-file-utils
BuildRequires: gtk3-devel
BuildRequires: libSM-devel
BuildRequires: libXtst-devel
BuildRequires: make
BuildRequires: mate-common
BuildRequires: mesa-libGLES-devel
BuildRequires: systemd-devel
BuildRequires: xmlto
BuildRequires: xorg-x11-xtrans-devel

Requires: system-logos
# Needed for mate-settings-daemon
Requires: mate-control-center
# we need an authentication agent in the session
Requires: mate-polkit
# and we want good defaults
Requires: polkit-desktop-policy
# for gsettings shemas
Requires: mate-desktop-libs
# for /bin/dbus-launch
Requires: dbus-x11

%description
This package contains a session that can be started from a display
manager such as MDM. It will load all necessary applications for a
full-featured user session.

%prep
%autosetup -p1

#NOCONFIGURE=1 ./autogen.sh

%build
%configure                    \
    --disable-static          \
    --enable-ipv6             \
    --with-default-wm=marco   \
    --with-systemd            \
    --enable-docbook-docs     \
    --disable-schemas-compile

make %{?_smp_mflags} V=1

%install
%{make_install}

desktop-file-install                               \
        --delete-original                          \
        --dir=%{buildroot}%{_datadir}/applications \
%{buildroot}%{_datadir}/applications/mate-session-properties.desktop

%find_lang %{name} --with-gnome --all-name


%files -f %{name}.lang
%doc AUTHORS COPYING README
%{_mandir}/man1/*
%{_bindir}/mate-session
%{_bindir}/mate-session-inhibit
%{_bindir}/mate-session-properties
%{_bindir}/mate-session-save
%{_bindir}/mate-wm
%{_libexecdir}/mate-session-check-accelerated
%{_libexecdir}/mate-session-check-accelerated-gl-helper
%{_libexecdir}/mate-session-check-accelerated-gles-helper
%{_datadir}/applications/mate-session-properties.desktop
%{_datadir}/mate-session-manager
%{_datadir}/icons/hicolor/*/apps/*.png
%{_datadir}/icons/hicolor/scalable/apps/mate-session-properties.svg
%{_datadir}/glib-2.0/schemas/org.mate.session.gschema.xml
%{_datadir}/xsessions/mate.desktop
%{_docdir}/mate-session-manager/dbus/mate-session.html


%changelog
%autochangelog
