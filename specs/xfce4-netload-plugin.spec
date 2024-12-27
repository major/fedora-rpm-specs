%global _hardened_build 1
%global minor_version 1.4
%global xfceversion 4.16

Name:           xfce4-netload-plugin
Version:        1.4.2
Release:        %autorelease
Summary:        Network-load monitor for the Xfce panel

# Automatically converted from old format: GPLv2+ - review is highly recommended.
License:        GPL-2.0-or-later
URL:            http://goodies.xfce.org/projects/panel-plugins/%{name}
Source0:        http://archive.xfce.org/src/panel-plugins/%{name}/%{minor_version}/%{name}-%{version}.tar.bz2

BuildRequires:  make
BuildRequires:  gcc-c++
BuildRequires:  pkgconfig(libxfce4panel-2.0) >= %{xfceversion}
BuildRequires:  pkgconfig(libxfce4ui-2) >= %{xfceversion}
BuildRequires:  libxml2-devel
BuildRequires:  gettext

Requires:       xfce4-panel >= %{xfceversion}

%description
A network-load monitor plugin for the Xfce panel.


%prep
%autosetup

%build
%configure
%make_build


%install
%make_install
%find_lang %{name}
chmod 755 %{buildroot}/%{_libdir}/xfce4/panel/plugins/libnetload.so
rm -f %{buildroot}/%{_libdir}/xfce4/panel/plugins/libnetload.la


%files -f %{name}.lang
%doc AUTHORS ChangeLog README
%license COPYING
%{_datadir}/icons/hicolor/*/*/*
%{_libdir}/xfce4/panel/plugins/libnetload.so
%{_datadir}/xfce4/panel/plugins/*.desktop

%changelog
%autochangelog
