%undefine __cmake_in_source_build
%global minorversion	2.10

Name:		xfce4-whiskermenu-plugin
Version:	2.10.1
Release:	%autorelease
Summary:	An alternate application launcher for Xfce

# Automatically converted from old format: GPLv2+ - review is highly recommended.
License:	GPL-2.0-or-later
URL:		http://gottcode.org/xfce4-whiskermenu-plugin/
Source0:	http://archive.xfce.org/src/panel-plugins/%{name}/%{minorversion}/%{name}-%{version}.tar.xz

BuildRequires:	gcc-c++
BuildRequires:	cmake
BuildRequires:	exo-devel
BuildRequires:	garcon-devel
BuildRequires:	xfce4-panel-devel
BuildRequires:	libxfce4ui-devel
BuildRequires:	libxfce4util-devel
BuildRequires:	accountsservice-devel
BuildRequires:	gtk-layer-shell-devel
BuildRequires:	gettext

Requires:	xfce4-panel
Requires:	hicolor-icon-theme


%description
Alternate application launcher for Xfce. When you open it you are shown 
a list of applications you have marked as favorites. You can browse through
all of your installed applications by clicking on the category buttons on the
side. Top level categories make browsing fast, and simple to switch between. 
Additionally, Whisker Menu keeps a list of the last ten applications 
that you’ve launched from it

%prep
%setup -q

%build
%cmake
%cmake_build

%install
%cmake_install

%find_lang %{name}

%ldconfig_scriptlets

%files -f %{name}.lang
%license COPYING
%doc README NEWS
%{_bindir}/xfce4-popup-whiskermenu
%{_libdir}/xfce4/panel/plugins/libwhiskermenu.so
# Type=X-XFCE-PanelPlugin is a valid extension of freedesktop.org specs, but 
# desktop-file-utils refuse to install or verify these files
%{_datadir}/xfce4/panel/plugins/whiskermenu.desktop
%{_datadir}/icons/hicolor/*/apps/org.xfce.panel.whiskermenu.*g
%{_mandir}/man1/xfce4-popup-whiskermenu.1*

%changelog
%autochangelog

