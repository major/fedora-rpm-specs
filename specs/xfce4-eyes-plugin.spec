%global _hardened_build 1
%global minor_version 4.6
%global xfceversion 4.16

Name:           xfce4-eyes-plugin
Version:        4.6.2
Release:        %autorelease
Summary:        Eyes for the Xfce panel

# Automatically converted from old format: GPLv2+ - review is highly recommended.
License:        GPL-2.0-or-later
URL:            http://goodies.xfce.org/projects/panel-plugins/%{name}
Source0:        http://archive.xfce.org/src/panel-plugins/%{name}/%{minor_version}/%{name}-%{version}.tar.bz2

BuildRequires:  make
BuildRequires:  gcc-c++
BuildRequires:  xfce4-panel-devel >= %{xfceversion}
BuildRequires:  libxfce4ui-devel >= %{xfceversion}
BuildRequires:  libxml2-devel
BuildRequires:  intltool
BuildRequires:  gettext

Requires:       xfce4-panel >= %{xfceversion}

%description
A xfce4 panel plugin that adds eyes which watch your every step. Scary!

%prep
%autosetup

%build
%configure --disable-static
%make_build

%install
%make_install
%find_lang %{name}

find %{buildroot} -name \*.la -exec rm {} \;


%files -f %{name}.lang
%doc AUTHORS ChangeLog
%license COPYING
%{_datadir}/xfce4/panel/plugins/*.desktop
%{_libdir}/xfce4/panel/plugins/libeyes.so
%{_datadir}/icons/hicolor/*/apps/xfce4-eyes.png
%{_datadir}/xfce4/eyes

%changelog
%autochangelog
