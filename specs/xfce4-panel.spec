%global xfceversion 4.20
%global forgeurl https://gitlab.xfce.org/xfce/xfce4-panel

%global namespc Libxfce4panel

%global __provides_exclude_from ^%{_libdir}/xfce4/panel/plugins/.*\\.so$
# vapigen failed with vala 0.47:
# https://bugzilla.xfce.org/show_bug.cgi?id=16426
# It is safe to disable vapigen by now, since no package in Fedora requires the
# vapi
%global _with_vala 0

Name:           xfce4-panel
Version:        4.20.8
%forgemeta
Release:        %autorelease
Summary:        Next generation panel for Xfce

License:        GPL-2.0-or-later AND LGPL-2.0-or-later
URL:            http://www.xfce.org/
#VCS git:git://git.xfce.org/xfce/xfce4-panel
Source0:        %{forgesource}

# clock icon taken from system-config-date, license is GPLv2+
Source1:        xfce4-clock.png
Source2:        xfce4-clock.svg

BuildRequires:  desktop-file-utils
BuildRequires:  exo-devel >= 0.3.93
BuildRequires:  garcon-devel >= 0.6.0
BuildRequires:  gcc
BuildRequires:  gettext
BuildRequires:  gobject-introspection-devel
BuildRequires:  gtk-doc
BuildRequires:  gtk-layer-shell-devel >= 0.7.0
BuildRequires:  gtk3-devel
BuildRequires:  libwnck3-devel >= 3.14
BuildRequires:  libxfce4ui-devel >= %{xfceversion}
BuildRequires:  libxfce4windowing-devel >= 4.20.6
BuildRequires:  libxml2-devel >= 2.4.0
BuildRequires:  meson
BuildRequires:  startup-notification-devel
BuildRequires:  xfce4-dev-tools
BuildRequires:  xfconf-devel >= %{xfceversion}

%if 0%{?fedora}
BuildRequires:  libdbusmenu-gtk3-devel
%endif

%if %{_with_vala}
BuildRequires:  vala
%endif


# obsolete old plugins
Obsoletes:      orage < 4.12.1-17.fc34
Obsoletes:      xfce4-embed-plugin < 1.6.0-13.fc34
Obsoletes:      xfce4-cellmodem-plugin < 0.0.5-29.fc34
Obsoletes:      xfce4-kbdleds-plugins < 0.0.6-20.fc34
Obsoletes:      xfce4-hardware-monitor-plugin < 1.6.0-11

%description
This package includes the panel for the Xfce desktop environment.

%package devel
Summary:        Development headers for xfce4-panel
Requires:       %{name} = %{version}-%{release}
Requires:       libxfce4ui-devel >= %{xfceversion}
Requires:       libxfce4util-devel >= %{xfceversion}
Requires:       pkgconfig

%description devel
This package includes the header files you will need to build
plugins for xfce4-panel.


%prep
%forgeautosetup -p1

# Fix icon in 'Add new panel item' dialog
sed -i 's|Icon=office-calendar|Icon=xfce4-clock|g' plugins/clock/clock.desktop.in.in


%build
%meson \
  -Dgtk-doc=true \
%if %{_with_vala}
  -Dvala=enabled
%else
  -Dvala=disabled
%endif

%meson_build


%install
%meson_install

# Rename invalid hye locale to hy
if [ -d %{buildroot}%{_datadir}/locale/hye ]; then
  mv %{buildroot}%{_datadir}/locale/hye %{buildroot}%{_datadir}/locale/hy
fi

%find_lang %{name}

desktop-file-validate %{buildroot}/%{_datadir}/applications/panel-desktop-handler.desktop
desktop-file-validate %{buildroot}/%{_datadir}/applications/panel-preferences.desktop

# install additional icons
install -pm 0644 %{SOURCE1} %{buildroot}%{_datadir}/icons/hicolor/48x48/apps/
install -pm 0644 %{SOURCE2} %{buildroot}%{_datadir}/icons/hicolor/scalable/apps/


%check
%meson_test


%files -f %{name}.lang
%license COPYING
%doc AUTHORS ChangeLog NEWS
%config(noreplace) %{_sysconfdir}/xdg/xfce4/panel/default.xml
%{_bindir}/xfce4-panel
%{_bindir}/xfce4-popup-applicationsmenu
%{_bindir}/xfce4-popup-directorymenu
%{_bindir}/xfce4-popup-windowmenu
%{_libdir}/libxfce4panel-*.so.*
%{_libdir}/xfce4/panel/
%{_libdir}/girepository-1.0/%{namespc}-2.0.typelib
%{_datadir}/icons/hicolor/*/*/*
%{_datadir}/xfce4/panel/
%{_datadir}/applications/*.desktop
%if %{_with_vala}
%{_datadir}/vala/vapi/libxfce4panel-2.0.deps
%{_datadir}/vala/vapi/libxfce4panel-2.0.vapi
%endif

%files devel
%{_libdir}/pkgconfig/*
%{_libdir}/libxfce4panel-*.so
%{_datadir}/gir-1.0/%{namespc}-2.0.gir
%doc %{_datadir}/gtk-doc/html/libxfce4panel-*/
%{_includedir}/xfce4/libxfce4panel-*/

%changelog
%autochangelog
