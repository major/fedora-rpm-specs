# Review: https://bugzilla.redhat.com/bugzilla/show_bug.cgi?id=173674

%global minor_version 0.8

%global xfceversion 4.16

Name:           xfce4-xkb-plugin
Version:        0.8.5
Release:        %autorelease
Summary:        XKB layout switcher for the Xfce panel

# Automatically converted from old format: BSD - review is highly recommended.
License:        LicenseRef-Callaway-BSD
URL:            http://goodies.xfce.org/projects/panel-plugins/%{name}
Source0:        http://archive.xfce.org/src/panel-plugins/%{name}/%{minor_version}/%{name}-%{version}.tar.bz2

BuildRequires: make
BuildRequires:  gcc-c++
BuildRequires:  libxfce4ui-devel >= %{xfceversion}
BuildRequires:  xfce4-panel-devel >= %{xfceversion}
BuildRequires:  libxklavier-devel >= 5.0
BuildRequires:  librsvg2-devel >= 2.18
BuildRequires:  garcon-devel
BuildRequires:  gettext
BuildRequires:  intltool
BuildRequires:  libwnck3-devel
Requires:       xfce4-panel >= %{xfceversion}
Requires:       xfce4-settings


%description
Xfce XKB layout switch plugin for the Xfce panel. It displays the current 
keyboard layout, and refreshes when layout changes. The layout can be 
switched by simply clicking on the plugin. For now the keyboard layouts 
cannot be configured from the plugin itself, they should be set in the 
XF86Config file or some other way (e.g. setxkbmap).

%prep
%setup -q


%build
%configure --disable-static
%make_build


%install
%make_install

# remove la file
find %{buildroot} -name '*.la' -exec rm -f {} ';'

# make sure debuginfo is generated properly
chmod -c +x %{buildroot}%{_libdir}/xfce4/panel/plugins/*.so

%find_lang %{name}


%files -f %{name}.lang
%license COPYING
%doc AUTHORS ChangeLog
%{_libdir}/xfce4/panel/plugins/*.so
%{_datadir}/xfce4/panel/plugins/*.desktop
%{_datadir}/icons/hicolor/*/apps/org.xfce.panel.xkb.*
%dir %{_datadir}/xfce4/xkb/
%dir %{_datadir}/xfce4/xkb/flags
%{_datadir}/xfce4/xkb/flags/*.svg

%changelog
%autochangelog
