# Review at https://bugzilla.redhat.com/show_bug.cgi?id=398111

%global minor_version 1.1
%global xfceversion 4.16

Name:           xfce4-time-out-plugin
Version:        1.1.4
Release:        %autorelease
Summary:        Xfce panel plugin for taking breaks from the computer

# Automatically converted from old format: GPLv2+ - review is highly recommended.
License:        GPL-2.0-or-later
URL:            http://goodies.xfce.org/projects/panel-plugins/%{name}
#VSC: git: git://git.xfce.org/panel-plugins/xfce4-time-out-plugin
Source0:        http://archive.xfce.org/src/panel-plugins/%{name}/%{minor_version}/%{name}-%{version}.tar.bz2

BuildRequires: make
BuildRequires:  gcc-c++
BuildRequires:  libxfce4ui-devel >= %{xfceversion}
BuildRequires:  xfce4-panel-devel >= %{xfceversion}
BuildRequires:  libxml2-devel
BuildRequires:  libICE-devel
BuildRequires:  gettext, intltool
Requires:       xfce4-panel >= %{xfceversion}

%description
This plugin makes it possible to take periodical breaks from the computer every
X minutes. During breaks it locks your screen. It optionally allows you to 
postpone breaks for a certain time.


%prep
%setup -q


%build
%configure 
%make_build


%install
%make_install

chmod -c +x %{buildroot}%{_libdir}/xfce4/panel/plugins/libtime-out.so

find %{buildroot} -name '*.la' -exec rm -f {} ';'

%find_lang %{name}

%files -f %{name}.lang
%license COPYING
%doc AUTHORS ChangeLog NEWS
%{_libdir}/xfce4/panel/plugins/
%{_datadir}/xfce4/panel/plugins/*.desktop
%{_datadir}/icons/hicolor/*/*/*


%changelog
%autochangelog
