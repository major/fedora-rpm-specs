%global majorversion 0.4
%global xfceversion 4.18

Name:		xfce4-docklike-plugin
Version:	0.4.3
Release:	%autorelease
Summary:	A modern, minimalist taskbar for Xfce

License:	GPL-2.0-or-later AND GPL-3.0-or-later AND FSFUL
URL:		https://gitlab.xfce.org/panel-plugins/xfce4-docklike-plugin
Source0:	http://archive.xfce.org/src/panel-plugins/%{name}/%{majorversion}/%{name}-%{version}.tar.bz2

BuildRequires:	desktop-file-utils
BuildRequires:	gcc-c++
BuildRequires:	gettext
BuildRequires:	gtk3-devel
BuildRequires:	libxfce4windowing-devel
BuildRequires:	libwnck3-devel
BuildRequires:	libxfce4ui-devel >= %{xfceversion}
BuildRequires:	libX11-devel
BuildRequires:	make
BuildRequires:	xfce4-panel-devel >= %{xfceversion}

%description
Docklike Taskbar behaves similarly to many other desktop environments and
operating systems. Wherein all application windows are grouped together as
an icon and can be pinned to act as a launcher when the application is not
running. Commonly referred to as a dock.

%prep
%autosetup

# remove empty files
rm -f ChangeLog README

%build
%configure
%make_build

%install
%make_install

%find_lang %{name}

%files -f %{name}.lang
%license COPYING
%doc NEWS AUTHORS
%{_datadir}/xfce4/panel/plugins/docklike.desktop
%{_libdir}/xfce4/panel/plugins/libdocklike.so

%changelog
%autochangelog
