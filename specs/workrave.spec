%bcond	gnome		1
%bcond	gnome40		1
%bcond	gnome45		%[0%{?fedora} || 0%{?rhel} >= 10]
%bcond	gnome_flashback	%{undefined flatpak}
%bcond	mate		%{undefined flatpak}
%bcond	xfce		%{undefined flatpak}

%global app_id org.workrave.Workrave

Name:          workrave
Version:       1.11.0~beta.13
Release:       %autorelease
Summary:       Program that assists in the recovery and prevention of RSI
# Based on older packages by Dag Wieers <dag@wieers.com> and Steve Ratcliffe
License:       GPL-3.0-or-later AND LGPL-2.0-or-later
URL:           https://workrave.org/
%global tag %(echo %{version} | sed -e 's/[\\.~]/_/g')
Source:        https://github.com/rcaelers/workrave/archive/v%{tag}/%{name}-v%{tag}.tar.gz

BuildRequires: cmake
BuildRequires: desktop-file-utils
BuildRequires: gettext
BuildRequires: gcc-c++
BuildRequires: libappstream-glib
# Base dependencies
BuildRequires: boost-devel
BuildRequires: python3-devel
BuildRequires: python3-jinja2
# Gtk+3 interface
BuildRequires: pkgconfig(glib-2.0) >= 2.56.0
BuildRequires: pkgconfig(gio-2.0) >= 2.56.0
BuildRequires: pkgconfig(gtk+-3.0) >= 3.22.0
BuildRequires: pkgconfig(glibmm-2.4) >= 2.28.0
BuildRequires: pkgconfig(gtkmm-3.0) >= 3.22.0
# Sound support
BuildRequires: pkgconfig(gstreamer-1.0)
BuildRequires: pkgconfig(libpulse) >= 0.9.15
BuildRequires: pkgconfig(libpulse-mainloop-glib) >= 0.9.15
# Wayland support
BuildRequires: pkgconfig(wayland-client)
BuildRequires: pkgconfig(wayland-scanner)
# X11 support
BuildRequires: libX11-devel
BuildRequires: libXScrnSaver-devel
BuildRequires: libXtst-devel
# Desktop applets
BuildRequires: pkgconfig(ayatana-appindicator3-0.1)
BuildRequires: pkgconfig(dbusmenu-glib-0.4)
BuildRequires: pkgconfig(dbusmenu-gtk3-0.4)
BuildRequires: pkgconfig(gobject-introspection-1.0)
%if %{with gnome_flashback}
BuildRequires: pkgconfig(libgnome-panel)
%endif
%if %{with gnome40}
BuildRequires: pkgconfig(gtk4)
%endif
%if %{with xfce}
BuildRequires: pkgconfig(libxfce4panel-2.0) >= 4.12
%endif
%if %{with mate}
BuildRequires: pkgconfig(libmatepanelapplet-4.0) >= 1.20.0
%endif
# Logging
BuildRequires: cmake(fmt)
BuildRequires: cmake(spdlog)

Requires:      dbus-common
Requires:      hicolor-icon-theme
Recommends:    (%{name}-cinnamon if cinnamon)
Recommends:    (%{name}-gnome if gnome-shell)
Recommends:    (%{name}-gnome-flashback if gnome-panel)
Recommends:    (%{name}-mate if mate-panel)
Recommends:    (%{name}-xfce if xfce4-panel)
Recommends:    gstreamer1-plugins-base
Recommends:    gstreamer1-plugins-good
Obsoletes:     %{name}-devel < %{version}-%{release}

# https://fedoraproject.org/wiki/Changes/EncourageI686LeafRemoval
ExcludeArch:   %{ix86}

%global _description Workrave is a program that assists in the recovery and prevention of\
Repetitive Strain Injury (RSI). The program frequently alerts you to\
take micro-pauses, rest breaks and restricts you to your daily limit.

%description
%{_description}

%package cinnamon
Requires:      %{name}%{?_isa} = %{version}-%{release}
Summary:       Workrave applet for Cinnamon desktop

%description cinnamon
%{_description}

This package provides an applet for the Cinnamon desktop.

%package gnome
Requires:      %{name}%{?_isa} = %{version}-%{release}
Summary:       Workrave applet for GNOME desktop

%description gnome
%{_description}

This package provides an applet for the GNOME desktop.

%package gnome-flashback
Requires:      %{name}%{?_isa} = %{version}-%{release}
Summary:       Workrave applet for GNOME Flashback

%description gnome-flashback
%{_description}

This package provides an applet for the GNOME Flashback panel.

%package mate
Requires:      %{name}%{?_isa} = %{version}-%{release}
Summary:       Workrave applet for MATE

%description mate
%{_description}

This package provides an applet for the MATE panel.

%package xfce
Requires:      %{name}%{?_isa} = %{version}-%{release}
Summary:       Workrave applet for Xfce

%description xfce
%{_description}

This package provides an applet for the Xfce panel.


%prep
%autosetup -n workrave-%{tag} -p1

# use versioned python command
%py3_shebang_fix libs/dbus/bin/dbusgen.py


%build
%cmake \
  -DWITH_GNOME_CLASSIC_PANEL:BOOL=%{?with_gnome_flashback:ON}%{!?with_gnome_flashback:OFF} \
  -DWITH_GNOME45:BOOL=%{?with_gnome45:ON}%{!?with_gnome45:OFF} \
  -DWITH_MATE:BOOL=%{?with_mate:ON}%{!?with_mate:OFF} \
  -DWITH_XFCE4:BOOL=%{?with_xfce:ON}%{!?with_xfce:OFF} \
  -DWITH_DBUS:BOOL=ON \
  -DWITH_GSTREAMER:BOOL=ON \
  -DWITH_PULSE:BOOL=ON \
  -DWITH_DBUSMENU:BOOL=ON \
  -DWITH_INDICATOR:BOOL=ON \
  -DWITH_APPINDICATOR:BOOL=ON \
  -DWITH_WAYLAND:BOOL=ON \
  %{nil}

%cmake_build


%install
%cmake_install

# workrave does not provide a public API
rm -f %{buildroot}%{_datadir}/gir-1.0/*.gir
rm -f %{buildroot}%{_libdir}/*.so
# indicators need to be enabled to build GIR but are not needed otherwise
rm -f %{buildroot}%{_libdir}/*indicators3/7/libworkrave.so*

# fix appstream ID
appstream-util modify %{buildroot}%{_metainfodir}/%{app_id}.metainfo.xml id %{app_id}

%find_lang %{name}


%check
desktop-file-validate %{buildroot}%{_datadir}/applications/%{app_id}.desktop
appstream-util validate-relax --nonet %{buildroot}%{_metainfodir}/%{app_id}.metainfo.xml


%files -f %{name}.lang
%doc AUTHORS COPYING NEWS README.md
%{_bindir}/%{name}
%{_datadir}/applications/%{app_id}.desktop
%{_datadir}/dbus-1/services/%{app_id}.service
%{_datadir}/glib-2.0/schemas/org.workrave.*.xml
%{_datadir}/icons/hicolor/*/apps/%{name}.*
%{_datadir}/sounds/%{name}/
%{_datadir}/%{name}/
%{_metainfodir}/%{app_id}.metainfo.xml
# support library for gtk3 applets
%{_libdir}/girepository-1.0/Workrave-1.0.typelib
%{_libdir}/libworkrave-private-1.0.so.*

%files cinnamon
%dir %{_datadir}/cinnamon/
%dir %{_datadir}/cinnamon/applets/
%{_datadir}/cinnamon/applets/workrave@workrave.org/

%if %{with gnome}
%files gnome
%if %{with gnome40}
%{_libdir}/girepository-1.0/Workrave-2.0.typelib
%{_libdir}/libworkrave-gtk4-private-1.0.so.*
%endif
%dir %{_datadir}/gnome-shell/
%dir %{_datadir}/gnome-shell/extensions/
%{_datadir}/gnome-shell/extensions/workrave@workrave.org/
%endif

%if %{with gnome_flashback}
%files gnome-flashback
%{_libdir}/gnome-panel/modules/libworkrave-applet.so
%endif

%if %{with xfce}
%files xfce
%{_libdir}/xfce4/panel/plugins/libworkrave-plugin.so
%{_datadir}/xfce4/panel/plugins/workrave-xfce-applet.desktop
%endif

%if %{with mate}
%files mate
%{_libdir}/mate-applets/workrave-applet
%{_datadir}/dbus-1/services/org.mate.panel.applet.WorkraveAppletFactory.service
%{_datadir}/mate-panel/applets/org.workrave.WorkraveApplet.mate-panel-applet
%{_datadir}/mate-panel/ui/workrave-menu.xml
%endif

%changelog
%autochangelog
