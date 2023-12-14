%global xfceversion 4.18

Name:		xfce4-power-manager
Version:	4.18.3
Release:	%autorelease
Summary:	Power management for the Xfce desktop environment

License:	GPLv2+
URL:		http://goodies.xfce.org/projects/applications/%{name}
#VCS: git:git://git.xfce.org/xfce/xfce4-power-manager
Source0:	http://archive.xfce.org/src/xfce/%{name}/%{xfceversion}/%{name}-%{version}.tar.bz2
Source1:	%{name}.xml

BuildRequires: make
BuildRequires:  gcc-c++
BuildRequires:  pkgconfig(libxfconf-0) >= %{xfceversion}
BuildRequires:  pkgconfig(libxfce4ui-2) >= %{xfceversion}
BuildRequires:  pkgconfig(libxfce4panel-2.0) >= %{xfceversion}
BuildRequires:  pkgconfig(dbus-1) >= 0.60
BuildRequires:  pkgconfig(dbus-glib-1) >= 0.70
BuildRequires:  pkgconfig(libnotify) >= 0.4.1
BuildRequires:  pkgconfig(xrandr) >= 1.2.0
BuildRequires:  xorg-x11-proto-devel >= 1.0.0
BuildRequires:  gettext
BuildRequires:  intltool
BuildRequires:  desktop-file-utils
BuildRequires:  upower-devel
BuildRequires:  libappstream-glib

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

# install xfpm default config
mkdir -p %{buildroot}%{_sysconfdir}/xdg/xfce4/xfconf/xfce-perchannel-xml
cp -p %{SOURCE1} %{buildroot}%{_sysconfdir}/xdg/xfce4/xfconf/xfce-perchannel-xml/

%find_lang %{name}
desktop-file-validate %{buildroot}%{_datadir}/applications/%{name}-settings.desktop

appstream-util validate-relax --nonet %{buildroot}%{_metainfodir}/%{name}.appdata.xml

find %{buildroot} -name '*.la' -exec rm -f {} ';'

%files -f %{name}.lang
%license COPYING
%doc AUTHORS ChangeLog NEWS TODO
%{_sysconfdir}/xdg/xfce4/xfconf/xfce-perchannel-xml/%{name}.xml
%{_bindir}/%{name}
%{_bindir}/%{name}-settings
%{_sbindir}/xfce4-pm-helper
%{_metainfodir}/%{name}.appdata.xml
%{_libdir}/xfce4/panel/plugins/libxfce4powermanager.so
%{_datadir}/xfce4/panel/plugins/power-manager-plugin.desktop
%{_sbindir}/xfpm-power-backlight-helper
%config %{_sysconfdir}/xdg/autostart/%{name}.desktop
%{_datadir}/applications/%{name}-settings.desktop
%{_datadir}/icons/hicolor/*/*/*.*
%{_datadir}/polkit-1/actions/org.xfce.power.policy
%doc
%{_mandir}/man1/%{name}-settings.1.*
%{_mandir}/man1/%{name}.1.*

%changelog
%autochangelog
