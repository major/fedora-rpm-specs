%global po_package %{name}-3.0

%global use_evolution_data_server 1

Name:           gnome-panel
Version:        3.58.1
Release:        %autorelease
Summary:        GNOME Flashback panel

License:        GPL-2.0-or-later AND LGPL-2.1-or-later
URL:            https://wiki.gnome.org/Projects/GnomePanel
Source:         https://download.gnome.org/sources/%{name}/3.58/%{name}-%{version}.tar.xz

BuildRequires:  autoconf
BuildRequires:  automake >= 1.16.4
BuildRequires:  desktop-file-utils
BuildRequires:  gcc
BuildRequires:  gettext-devel
BuildRequires:  gnome-common
BuildRequires:  gtk-doc
BuildRequires:  intltool
BuildRequires:  itstool
BuildRequires:  libxslt
BuildRequires:  make
BuildRequires:  yelp-tools

BuildRequires:  pkgconfig(cairo-gobject)
BuildRequires:  pkgconfig(cairo-xlib)
BuildRequires:  pkgconfig(dconf) >= 0.13.4
BuildRequires:  pkgconfig(gdk-pixbuf-2.0) >= 2.26.0
BuildRequires:  pkgconfig(gdm)
BuildRequires:  pkgconfig(geocode-glib-2.0)
BuildRequires:  pkgconfig(glib-2.0) >= 2.67.1
BuildRequires:  pkgconfig(gnome-desktop-3.0) >= 3.35.3
BuildRequires:  pkgconfig(gsettings-desktop-schemas) >= 42.0
BuildRequires:  pkgconfig(gtk+-3.0) >= 3.22.0
BuildRequires:  pkgconfig(gweather4) >= 3.91
BuildRequires:  pkgconfig(libgnome-menu-3.0) >= 3.7.90
BuildRequires:  pkgconfig(libsystemd) >= 230
BuildRequires:  pkgconfig(libwnck-3.0) >= 43.2
BuildRequires:  pkgconfig(pango) >= 1.15.4
BuildRequires:  pkgconfig(polkit-gobject-1)
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(xi)
BuildRequires:  pkgconfig(xrandr) >= 1.3.0
%if %{use_evolution_data_server}
BuildRequires:  pkgconfig(libecal-2.0) >= 3.33.2
BuildRequires:  pkgconfig(libedataserver-1.2) >= 3.33.2
%endif

Requires:       gnome-desktop3
Requires:       gnome-menus >= 3.7.90
%if %{use_evolution_data_server}
Requires:       evolution-data-server >= 3.33.2
%endif
Requires:       %{name}-libs%{?_isa} = %{version}-%{release}
Requires:       hicolor-icon-theme

Suggests:       %{name}-doc

# https://fedoraproject.org/wiki/Changes/EncourageI686LeafRemoval
ExcludeArch:    %{ix86}

%description
Gnome Panel is a component that is part of GnomeFlashback and provides panels
and default applets for the desktop. A panel is a horizontal or vertical bar
that can be added to each side of the screen. By default there is one panel on
the top of the screen and one on the bottom, but this is configurable. The
panels are used to add applets such as a menu bar to open applications, a clock
and indicator applets which provide access to configure features of the system
such as the network, sound or the current keyboard layout. On the bottom panel
there is usually a list of open applications.


# libs package
%package        libs
Summary:        Libraries for %{name}
License:        LGPL-2.1-or-later

%description    libs
Libraries for %{name}.


# devel package
%package        devel
Summary:        Devel files for %{name}

Requires:       %{name}-libs%{?_isa} = %{version}-%{release}

%description    devel
Devel files for %{name}.


# doc package
%package        doc
Summary:        Docs for %{name}
BuildArch:      noarch

%description    doc
Docs for %{name}.


%prep
%autosetup -p1
rm -f libtool
autoreconf -fiv


%build
%configure              \
    --enable-gtk-doc    \
%if %{use_evolution_data_server}
    --enable-eds=yes
%else
    --enable-eds=no
%endif
%make_build


%install
%make_install
rm -rf %{buildroot}/var/scrollkeeper
find %{buildroot} -name '*.la' -delete;
%find_lang %{po_package} --all-name


%check
desktop-file-validate %{buildroot}%{_datadir}/applications/*.desktop


%files -f %{po_package}.lang
%license COPYING COPYING.LESSER
%doc AUTHORS NEWS README.md
%{_bindir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/glib-2.0/schemas/org.gnome.%{name}.*.xml
%{_datadir}/%{name}/
%{_datadir}/icons/hicolor/*/apps/*.png
%{_datadir}/icons/hicolor/scalable/apps/*.svg
%{_datadir}/man/man*/*
%{_libdir}/%{name}/
%{_userunitdir}/%{name}.service

%files libs
%{_libdir}/lib%{name}.so.*

%files devel

%{_includedir}/%{name}/
%{_libdir}/lib%{name}.so
%{_libdir}/pkgconfig/lib%{name}.pc

%files doc
%{_datadir}/help/


%changelog
%autochangelog
