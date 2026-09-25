%global upstream_version 3.3.6-unstable

Name:           xapps
Version:        3.3.6^unstable
Release:        %autorelease
Summary:        Common files for XApp desktop apps

License:        LGPL-3.0-only
URL:            https://github.com/linuxmint/%{name}
Source0:        %{url}/archive/%{upstream_version}/%{name}-%{upstream_version}.tar.gz
Source1:        http://packages.linuxmint.com/pool/main/f/flags/flags_1.0.4.tar.xz
Patch0:         watcher_fix_libexec.patch

ExcludeArch:    %{ix86}

BuildSystem:   meson
BuildOption(conf): --buildtype=debugoptimized
BuildOption(conf): -D deprecated_warnings=false
BuildRequires:  desktop-file-utils
BuildRequires:  glib2-devel
BuildRequires:  gobject-introspection-devel
BuildRequires:  gtk3-devel
BuildRequires:  gtk-layer-shell-devel
BuildRequires:  libdbusmenu-gtk3-devel
BuildRequires:  libX11-devel
BuildRequires:  libgnomekbd-devel
BuildRequires:  python3-gobject-devel
BuildRequires:  python3-devel
BuildRequires:  vala

Requires:       fpaste
%if 0%{?fedora}
Recommends:     inxi
%endif
Requires:       python3-xapps-overrides%{?_isa} = %{version}-%{release}
Requires:       xdg-utils
Requires:       xorg-x11-xinit
Recommends:     switcheroo-control
Obsoletes:      python2-xapps-overrides < %{version}-%{release}

%description
This package includes files that are shared between several XApp
apps (i18n files and configuration schemas).

%package        mate
Summary:        Mate status applet with HIDPI support
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    mate
Mate status applet with HIDPI support

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
Development libraries and header files for
developing XApp apps.

%package     -n python3-xapps-overrides
Summary:        Python%{python3_version} files for %{name}

Requires:       python3-gobject-base%{?_isa}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Provides:       python3-xapps-overrides = %{version}-%{release}
Provides:       python3-xapps-overrides%{?_isa} = %{version}-%{release}

%description -n python3-xapps-overrides
Python%{python3_version} files for XApp apps.

%prep
%autosetup -p1 -n xapp-%{upstream_version}

%install -a
tar -xf %{SOURCE1} -C %{buildroot}%{_datadir} --strip 3
rm %{buildroot}%{_datadir}/format

%{_bindir}/desktop-file-validate %{buildroot}%{_sysconfdir}/xdg/autostart/xapp-sn-watcher.desktop

%find_lang xapp

%files -f xapp.lang
%license COPYING
%doc README.md
%{_sysconfdir}/xdg/autostart/xapp-sn-watcher.desktop
%{_sysconfdir}/X11/xinit/xinitrc.d/80xapp-gtk3-module.sh
%{_bindir}/pastebin
%{_bindir}/upload-system-info
%{_bindir}/xapp-gpu-offload
%{_bindir}/xfce4-set-wallpaper
%{_libdir}/libxapp.so.*
%{_libdir}/girepository-1.0/XApp-1.0.typelib
%{_libdir}/gtk-3.0/modules/libxapp-gtk3-module.so
%dir %{_libexecdir}/xapps/
%{_libexecdir}/xapps/xapp-sn-watcher
%{_datadir}/dbus-1/services/org.x.StatusNotifierWatcher.service
%{_datadir}/iso-flag-png/
%{_datadir}/glib-2.0/schemas/org.x.apps.*.xml
%{_datadir}/icons/hicolor/scalable/*/*.svg

%files mate
%{_libexecdir}/xapps/*.py
%{_datadir}/dbus-1/services/org.mate.panel.applet.MateXAppStatusAppletFactory.service
%{_datadir}/mate-panel/applets/org.x.MateXAppStatusApplet.mate-panel-applet

%files devel
%{_includedir}/*
%{_libdir}/libxapp.so
%{_libdir}/pkgconfig/xapp.pc
%{_datadir}/gir-1.0/XApp-1.0.gir
%{_datadir}/glade/catalogs/xapp-glade-catalog.xml
%{_datadir}/vala/vapi/xapp.vapi
%{_datadir}/vala/vapi/xapp.deps

%files -n python3-xapps-overrides
%{python3_sitearch}/gi/overrides/XApp.py
%{python3_sitearch}/gi/overrides/__pycache__/XApp.cpython-%{python3_version_nodots}*.py*

%changelog
%autochangelog