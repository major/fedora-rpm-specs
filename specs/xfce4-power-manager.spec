%global xfceversion 4.20

Name:           xfce4-power-manager
Version:        4.20.1
Release:        %autorelease
Summary:        Power management for the Xfce desktop environment

# Automatically converted from old format: GPLv2+ - review is highly recommended.
License:        GPL-2.0-or-later
URL:            http://goodies.xfce.org/projects/applications/%{name}
#VCS: git:git://git.xfce.org/xfce/xfce4-power-manager
Source0:        http://archive.xfce.org/src/xfce/%{name}/%{xfceversion}/%{name}-%{version}.tar.bz2
Source1:        %{name}.xml

BuildRequires:  desktop-file-utils
BuildRequires:  gcc-c++
BuildRequires:  gettext
BuildRequires:  libappstream-glib
BuildRequires:  make
BuildRequires:  pkgconfig(gdk-wayland-3.0) >= 3.24.0
BuildRequires:  pkgconfig(gdk-x11-3.0) >= 3.24.0
BuildRequires:  pkgconfig(gio-2.0) >= 2.72.0
BuildRequires:  pkgconfig(gio-unix-2.0) >= 2.72.0
BuildRequires:  pkgconfig(glib-2.0) >= 2.72.0
BuildRequires:  pkgconfig(gmodule-2.0) >= 2.72.0
BuildRequires:  pkgconfig(gobject-2.0) >= 2.72.0
BuildRequires:  pkgconfig(gthread-2.0) >= 2.72.0
BuildRequires:  pkgconfig(gtk+-3.0) >= 3.24.0
BuildRequires:  pkgconfig(libnotify) >= 0.7.8
BuildRequires:  pkgconfig(libxfconf-0) >= %{xfceversion}
BuildRequires:  pkgconfig(libxfce4panel-2.0) >= %{xfceversion}
BuildRequires:  pkgconfig(libxfce4ui-2) >= %{xfceversion}
BuildRequires:  pkgconfig(libxfce4util-1.0) >= %{xfceversion}
BuildRequires:  pkgconfig(polkit-gobject-1) >= 0.102
BuildRequires:  pkgconfig(upower-glib) >= 0.99.10
BuildRequires:  pkgconfig(wayland-client) >= 1.20
BuildRequires:  pkgconfig(wayland-protocols) >= 1.25
BuildRequires:  pkgconfig(wayland-scanner) >= 1.20
BuildRequires:  pkgconfig(x11) >= 1.6.7
BuildRequires:  pkgconfig(xext) >= 1.0.0
BuildRequires:  pkgconfig(xrandr) >= 1.5.0

Requires:       xfce4-panel >= %{xfceversion}
Requires:       polkit
Requires:       upower >= 0.99

%description
Xfce Power Manager uses the information and facilities provided by HAL to 
display icons and handle user callbacks in an interactive Xfce session.
Xfce Power Preferences allows authorised users to set policy and change 
preferences.


%prep
%autosetup -p1


%build
%configure
%make_build


%install
%make_install

# Rename hye locale to hy as expected by Fedora
if [ -d %{buildroot}%{_datadir}/locale/hye ]; then
    mv %{buildroot}%{_datadir}/locale/hye %{buildroot}%{_datadir}/locale/hy
fi

# install xfpm default config
mkdir -p %{buildroot}%{_sysconfdir}/xdg/xfce4/xfconf/xfce-perchannel-xml
cp -p %{SOURCE1} %{buildroot}%{_sysconfdir}/xdg/xfce4/xfconf/xfce-perchannel-xml/

%find_lang %{name}

find %{buildroot} -name '*.la' -exec rm -f {} ';'


%check
desktop-file-validate %{buildroot}%{_datadir}/applications/%{name}-settings.desktop
appstream-util validate-relax --nonet %{buildroot}%{_metainfodir}/%{name}.appdata.xml


%files -f %{name}.lang
%license COPYING
%doc AUTHORS ChangeLog NEWS
%config(noreplace) %{_sysconfdir}/xdg/xfce4/xfconf/xfce-perchannel-xml/%{name}.xml
%{_bindir}/%{name}
%{_bindir}/%{name}-settings
%{_sbindir}/xfce4-pm-helper
%{_metainfodir}/%{name}.appdata.xml
%{_libdir}/xfce4/panel/plugins/libxfce4powermanager.so
%{_datadir}/xfce4/panel/plugins/power-manager-plugin.desktop
%{_sbindir}/xfpm-power-backlight-helper
%config(noreplace) %{_sysconfdir}/xdg/autostart/%{name}.desktop
%{_datadir}/applications/%{name}-settings.desktop
%{_datadir}/icons/hicolor/*/*/*.*
%{_datadir}/polkit-1/actions/org.xfce.power.policy
%{_mandir}/man1/%{name}-settings.1.*
%{_mandir}/man1/%{name}.1.*


%changelog
%autochangelog
