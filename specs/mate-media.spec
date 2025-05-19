Name:           mate-media
Version:        1.28.1
Release:        %autorelease
Summary:        MATE media programs
# Automatically converted from old format: GPLv2+ and LGPLv2+ - review is highly recommended.
License:        GPL-2.0-or-later AND LicenseRef-Callaway-LGPLv2+
URL:            http://mate-desktop.org
Source0:        http://pub.mate-desktop.org/releases/1.28/%{name}-%{version}.tar.xz

BuildRequires: desktop-file-utils
BuildRequires: gtk3-devel
BuildRequires: gtk-layer-shell-devel
BuildRequires: libmatemixer-devel
BuildRequires: libxml2-devel
BuildRequires: libcanberra-devel
BuildRequires: make
BuildRequires: mate-desktop-devel
BuildRequires: mate-common
BuildRequires: mate-panel-devel

%description
This package contains a few media utilities for the MATE desktop,
including a volume control.


%prep
%autosetup -p1

%build
%configure \
        --disable-static \
        --disable-schemas-compile \
        --enable-panelapplet=yes \
        --enable-statusicon=yes \
        --enable-wayland \
        --enable-in-process

make %{?_smp_mflags} V=1

%install
%{make_install}

find %{buildroot} -name '*.la' -exec rm -rf {} ';'

desktop-file-install                                                    \
        --delete-original                                               \
        --dir=%{buildroot}%{_datadir}/applications                      \
%{buildroot}%{_datadir}/applications/mate-volume-control.desktop

# disable autostart of na-tray-applet
rm -rf %{buildroot}%{_sysconfdir}/xdg/autostart/mate-volume-control-status-icon.desktop

%find_lang %{name} --with-gnome --all-name


%files -f %{name}.lang
%doc AUTHORS COPYING NEWS README
%{_mandir}/man1/*
%{_bindir}/mate-volume-control
%{_bindir}/mate-volume-control-status-icon
%{_datadir}/mate-media/
%{_datadir}/sounds/mate/
%{_datadir}/applications/mate-volume-control.desktop
%{_libdir}/libmate-volume-control-applet.so*
#%%{_libexecdir}/mate-volume-control-applet
#%%{_datadir}/dbus-1/services/org.mate.panel.applet.GvcAppletFactory.service
%{_datadir}/mate-panel/applets/org.mate.applets.GvcApplet.mate-panel-applet


%changelog
%autochangelog
