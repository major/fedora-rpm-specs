%define basever %(echo %{version} | sed "s/\.[0-9]*$//")

%bcond cdrdao %[!(0%{?rhel} >= 9)]
%bcond cdrkit %[!(0%{?rhel} >= 9)]
%bcond dvdrwtools %[!(0%{?rhel} >= 9)]
%bcond nautilus %[!(0%{?fedora} >= 37 || 0%{?rhel} >= 10)]
%bcond plparser %[!(0%{?rhel} >= 10)]

Name:      brasero
Version:   3.12.3
Release:   %autorelease
Summary:   Gnome CD/DVD burning application


# see https://bugzilla.gnome.org/show_bug.cgi?id=683503
# SVG files are GPL-2.0-only
# data/icons/hicolor_actions_scalable_transform-crop-and-resize.svg is CC-BY-SA-2.0
# libbrasero-media is GPL-2.0-or-later WITH GStreamer-exception-2008                                                                                                                         
License:   GPL-3.0-or-later AND LGPL-2.0-or-later AND GPL-2.0-only AND CC-BY-SA-2.0 AND GPL-2.0-or-later WITH GStreamer-exception-2008
URL:       https://wiki.gnome.org/Apps/Brasero
Source0:   https://download.gnome.org/sources/%{name}/%{basever}/%{name}-%{version}.tar.xz
# https://gitlab.gnome.org/GNOME/brasero/-/merge_requests/30
Patch0:    0001-Fix-gcc-14.x-build-failure.patch

BuildRequires:  pkgconfig(gstreamer-plugins-base-1.0) >= 0.11.92
BuildRequires:  pkgconfig(gtk+-3.0) >= 2.99.0
BuildRequires:  pkgconfig(ice)
BuildRequires:  pkgconfig(libburn-1) >= 0.4.0
BuildRequires:  pkgconfig(libcanberra-gtk3)
BuildRequires:  pkgconfig(libisofs-1) >= 0.6.4
BuildRequires:  pkgconfig(libnotify) >= 0.7.0
%if %{with nautilus}
BuildRequires:  pkgconfig(libnautilus-extension) >= 2.22.2
%endif
BuildRequires:  pkgconfig(libxml-2.0) >= 2.6.0
BuildRequires:  pkgconfig(sm)
%if %{with plparser}
BuildRequires:  pkgconfig(totem-plparser) >= 2.29.1
%endif
BuildRequires:  pkgconfig(tracker-sparql-3.0)
BuildRequires:  desktop-file-utils
BuildRequires:  gcc
BuildRequires:  gettext
BuildRequires:  gobject-introspection-devel
BuildRequires:  gtk-doc
BuildRequires:  intltool
BuildRequires:  itstool
BuildRequires:  libappstream-glib
BuildRequires:  make
BuildRequires:  yelp-tools

%{?with_dvdrwtools:Requires:  dvd+rw-tools}
%{?with_cdrkit:Requires:  wodim}
%{?with_cdrkit:Requires:  genisoimage}
Requires:  %{name}-libs%{?_isa} = %{version}-%{release}
%ifnarch s390x
%{?with_cdrdao:Requires:  cdrdao}
%endif
%{?with_cdrkit:Recommends: icedax}

%if %{without nautilus}
Obsoletes: %{name}-nautilus < %{version}-%{release}
%endif

%description
Simple and easy to use CD/DVD burning application for the Gnome
desktop.


%package   libs
Summary:   Libraries for %{name}

%description libs
The %{name}-libs package contains the runtime shared libraries for
%{name}.


%if %{with nautilus}
%package   nautilus
Summary:   Nautilus extension for %{name}
Requires:  %{name}%{?_isa} = %{version}-%{release}

%description nautilus
The %{name}-nautilus package contains the brasero nautilus extension.
%endif


%package   devel
Summary:   Headers for developing programs that will use %{name}
Requires:  %{name}-libs%{?_isa} = %{version}-%{release}


%description devel
This package contains the static libraries and header files needed for
developing brasero applications.


%prep
%autosetup -p1


%build
%configure \
        %{!?with_nautilus:--disable-nautilus} \
        --enable-libburnia \
        --enable-search \
        %{!?with_plparser:--disable-playlist} \
        --enable-preview \
        --enable-inotify \
        %{!?with_cdrdao:--disable-cdrdao} \
        %{!?with_cdrkit:--disable-cdrkit} \
        %{!?with_dvdrwtools:--disable-growisofs} \
        --disable-caches \
        --disable-static
sed -i -e 's! -shared ! -Wl,--as-needed\0!g' libtool
%make_build


%install
%make_install
find %{buildroot} -type f -name "*.la" -delete
%find_lang %{name}

# Update the screenshot shown in the software center
#
# NOTE: It would be *awesome* if this file was pushed upstream.
#
# See http://people.freedesktop.org/~hughsient/appdata/#screenshots for more details.
#
appstream-util replace-screenshots $RPM_BUILD_ROOT%{_datadir}/metainfo/brasero.appdata.xml \
  https://raw.githubusercontent.com/hughsie/fedora-appstream/master/screenshots-extra/brasero/a.png \
  https://raw.githubusercontent.com/hughsie/fedora-appstream/master/screenshots-extra/brasero/b.png \
  https://raw.githubusercontent.com/hughsie/fedora-appstream/master/screenshots-extra/brasero/c.png 


%check
appstream-util validate-relax --nonet %{buildroot}%{_datadir}/metainfo/%{name}.appdata.xml
desktop-file-validate %{buildroot}%{_datadir}/applications/*.desktop


%ldconfig_scriptlets libs


%files -f %{name}.lang
%license COPYING
%doc AUTHORS NEWS README
%{_mandir}/man1/%{name}.*
%{_bindir}/*
%{_libdir}/brasero3
%{_datadir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/metainfo/%{name}.appdata.xml
%{_datadir}/help/*
%{_datadir}/icons/hicolor/*/apps/*
%{_datadir}/mime/packages/*
%{_datadir}/GConf/gsettings/brasero.convert
%{_datadir}/glib-2.0/schemas/org.gnome.brasero.gschema.xml

%files libs
%{_libdir}/*.so.*
%{_libdir}/girepository-1.0/*.typelib

%if %{with nautilus}
%files nautilus
%{_libdir}/nautilus/extensions-3.0/*.so
%{_datadir}/applications/brasero-nautilus.desktop
%endif

%files devel
%doc %{_datadir}/gtk-doc/html/libbrasero-media
%doc %{_datadir}/gtk-doc/html/libbrasero-burn
%doc ChangeLog
%{_libdir}/*.so
%{_libdir}/pkgconfig/*.pc
%{_includedir}/brasero3
%{_datadir}/gir-1.0/*.gir


%changelog
%autochangelog
