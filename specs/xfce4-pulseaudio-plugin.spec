%global _hardened_build 1
%global xfceversion 4.18
%global versnum 0.5

Name:		xfce4-pulseaudio-plugin
Version:	0.5.1
Release:	%autorelease
Summary:	Pulseaudio plugin for Xfce4

# Automatically converted from old format: GPLv2+ - review is highly recommended.
License:	GPL-2.0-or-later
URL:		https://github.com/andrzej-r/xfce4-pulseaudio-plugin
Source0:	http://archive.xfce.org/src/panel-plugins/%{name}/%{versnum}/%{name}-%{version}.tar.xz

BuildRequires:	make
BuildRequires:	gcc-c++
BuildRequires:	meson
BuildRequires:	libxfce4ui-devel >= %{xfceversion}
BuildRequires:	libxfce4util-devel >= %{xfceversion}
BuildRequires:	xfce4-panel-devel >= %{xfceversion}
BuildRequires:	pulseaudio-libs-devel >= 0.9.19
BuildRequires:	glib2-devel >= 2.24.0
BuildRequires:	gtk3-devel >= 3.6.0
BuildRequires:	xfconf-devel >= 4.6.0
BuildRequires:	exo-devel
BuildRequires:	keybinder3-devel
BuildRequires:	libnotify-devel
BuildRequires:	libcanberra-devel
BuildRequires:	libxfce4windowing-devel

Obsoletes:	xfce4-mixer <= 4.11
# Obsoletes--->xfce4-volumed <= 0.1.13

Requires:	pulseaudio-daemon
Requires:	pavucontrol

%description
Pulseaudio panel plugin for Xfce Desktop Environment

%prep
%autosetup

# remove empty files
rm -f AUTHORS README

%build
%meson
%meson_build

%install
%meson_install

# remove libtool archives
find %{buildroot} -name '*.la' -exec rm -f {} ';'

%find_lang %{name}

# remove zero-length files
rm -f %{buildroot}/%{defaultdocdir}/AUTHORS
rm -f %{buildroot}/%{defaultdocdir}/README


%files -f %{name}.lang
%{license} COPYING
%{_datadir}/xfce4/panel/plugins/*.desktop
%{_libdir}/xfce4/panel/plugins/libpulseaudio-plugin.so
%{_datadir}/icons/hicolor/32x32/apps/%{name}*
%{_datadir}/icons/hicolor/48x48/apps/%{name}*
%{_datadir}/icons/hicolor/scalable/apps/%{name}*
%{_datadir}/icons/hicolor/scalable/status/*

%changelog
%autochangelog
