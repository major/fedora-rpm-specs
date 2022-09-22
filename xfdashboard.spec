%global majorversion 1.0
%global libversion 0.10000.0

Name:		xfdashboard
Version:	1.0.0
Release:	%autorelease
Summary:	GNOME shell like dashboard for Xfce

License:	GPLv2+
URL:		http://goodies.xfce.org/projects/applications/%{name}/start
Source0:	http://archive.xfce.org/src/apps/xfdashboard/%{majorversion}/%{name}-%{version}.tar.bz2

BuildRequires: make
BuildRequires:	libwnck3-devel
BuildRequires:	clutter-devel
BuildRequires:	xfconf-devel
BuildRequires:	garcon-devel
BuildRequires:	libxfce4util-devel
BuildRequires:	libtool
BuildRequires:	xfce4-dev-tools
BuildRequires:	libICE-devel
BuildRequires:	desktop-file-utils
BuildRequires:	libXcomposite-devel
BuildRequires:	libXdamage-devel
BuildRequires:	libXinerama-devel
BuildRequires:	libappstream-glib

%description
Xfdashboard provides a GNOME shell dashboard like interface for use with Xfce
desktop. It can be configured to run to any keyboard shortcut and when executed
provides an overview of applications currently open enabling the user to switch
between different applications. The search feature works like Xfce's app finder
which makes it convenient to search for and start applications.

%package themes
Summary:	Themes for xfdashboard
Requires:	%{name}

%description themes
Additional themes for use with xfdashboard

%package devel
Summary:	Devel files for xfdashboard
Requires:	%{name} = %{version}-%{release}

%description devel
Development related files for xfdashboard

%prep
%setup -q

%build
export CFLAGS="%{optflags}"

%configure
%make_build

%install
%make_install

%find_lang %{name}

# remove .la files
find %{buildroot} -name '*.la' -exec rm -f {} ';'

%check
appstream-util validate-relax --nonet %{buildroot}%{_metainfodir}/*%{name}*metainfo.xml
desktop-file-validate %{buildroot}%{_datadir}/applications/org.xfce*%{name}.desktop
desktop-file-validate %{buildroot}%{_datadir}/applications/org.xfce*%{name}-settings.desktop
desktop-file-validate %{buildroot}%{_sysconfdir}/xdg/autostart/org.xfce*%{name}-autostart.desktop

%ldconfig_scriptlets

%files -f %{name}.lang
%license COPYING
%doc AUTHORS
%{_bindir}/%{name}
%{_bindir}/%{name}-settings
%{_datadir}/%{name}/bindings.xml
%{_datadir}/%{name}/preferences.ui
%{_metainfodir}/*%{name}*metainfo.xml
%{_datadir}/applications/org.xfce*%{name}.desktop
%{_datadir}/applications/org.xfce*%{name}-settings.desktop
%{_sysconfdir}/xdg/autostart/org.xfce*%{name}-autostart.desktop
%{_datadir}/icons/hicolor/*/*/org.xfce.%{name}.*
%{_datadir}/themes/%{name}/*
%{_libdir}/lib%{name}.so.0
%{_libdir}/lib%{name}.so.%{libversion}
%{_libdir}/%{name}/plugins/clock-view.so
%{_libdir}/%{name}/plugins/gnome-shell-search-provider.so
%{_libdir}/%{name}/plugins/autopin-windows.so
%{_libdir}/%{name}/plugins/recently-used-search-provider.so
%{_libdir}/%{name}/plugins/hot-corner.so
%{_libdir}/%{name}/plugins/middle-click-window-close.so

%files themes
%{_datadir}/themes/%{name}-*

%files devel
%{_includedir}/%{name}/*
%{_libdir}/pkgconfig/lib%{name}.pc
%{_libdir}/lib%{name}.so

%changelog
%autochangelog
