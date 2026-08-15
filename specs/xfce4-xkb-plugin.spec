# Review: https://bugzilla.redhat.com/bugzilla/show_bug.cgi?id=173674
# VCS   https://gitlab.xfce.org/panel-plugins/xfce4-xkb-plugin

%global minor_version 0.9
%global xfceversion 4.20

Name:           xfce4-xkb-plugin
Version:        0.9.0
Release:        %autorelease
Summary:        XKB layout switcher for the Xfce panel

License:        GPL-2.0-or-later
URL:            https://docs.xfce.org/panel-plugins/xfce4-xkb-plugin
Source0:        https://archive.xfce.org/src/panel-plugins/%{name}/%{minor_version}/%{name}-%{version}.tar.xz

BuildRequires:  garcon-devel
BuildRequires:  gcc
BuildRequires:  gettext
BuildRequires:  libX11-devel
BuildRequires:  libnotify-devel
BuildRequires:  libwnck3-devel
BuildRequires:  libxfce4ui-devel >= %{xfceversion}
BuildRequires:  libxfce4util-devel
BuildRequires:  libxklavier-devel >= 5.3
BuildRequires:  librsvg2-devel >= 2.40
BuildRequires:  meson
BuildRequires:  xfce4-panel-devel >= %{xfceversion}
BuildRequires:  xfconf-devel

Requires:       xfce4-panel >= %{xfceversion}
Requires:       xfce4-settings

%description
Xfce XKB layout switch plugin for the Xfce panel. It displays the current 
keyboard layout, and refreshes when layout changes. The layout can be 
switched by simply clicking on the plugin. For now the keyboard layouts 
cannot be configured from the plugin itself, they should be set in the 
XF86Config file or some other way (e.g. setxkbmap).

%prep
%autosetup

%build
%meson
%meson_build

%install
%meson_install

# make sure debuginfo is generated properly
chmod -c +x %{buildroot}%{_libdir}/xfce4/panel/plugins/*.so

# Rename non-standard hye locale to hy
if [ -d %{buildroot}%{_datadir}/locale/hye ]; then
    mv %{buildroot}%{_datadir}/locale/hye %{buildroot}%{_datadir}/locale/hy
fi

%find_lang %{name}

%check
%meson_test

%files -f %{name}.lang
%license COPYING
%doc AUTHORS NEWS README.md
%{_libdir}/xfce4/panel/plugins/*.so
%{_datadir}/xfce4/panel/plugins/*.desktop
%{_datadir}/icons/hicolor/*/apps/org.xfce.panel.xkb.*
%dir %{_datadir}/xfce4/xkb/
%dir %{_datadir}/xfce4/xkb/flags
%{_datadir}/xfce4/xkb/flags/*.svg

%changelog
%autochangelog
