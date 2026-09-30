%bcond cdrdao %[!(0%{?rhel} >= 9)]
%bcond cdrkit %[!(0%{?rhel} >= 9)]
%bcond dvdrwtools %[!(0%{?rhel} >= 9)]
# The Meson build does not yet support the Nautilus extension.
%bcond nautilus 0
%bcond plparser %[!(0%{?rhel} >= 10)]

Name:      brasero
Version:   3.12.4
Release:   %autorelease
Summary:   Gnome CD/DVD burning application


# see https://bugzilla.gnome.org/show_bug.cgi?id=683503
# SVG files are GPL-2.0-only
# data/icons/hicolor_actions_scalable_transform-crop-and-resize.svg is CC-BY-SA-2.0
# libbrasero-media is GPL-2.0-or-later WITH GStreamer-exception-2008
License:   GPL-3.0-or-later AND LGPL-2.0-or-later AND GPL-2.0-only AND CC-BY-SA-2.0 AND GPL-2.0-or-later WITH GStreamer-exception-2008
URL:       https://wiki.gnome.org/Apps/Brasero
Source0:   https://download.gnome.org/sources/%{name}/%{gnome_major_minor_version}/%{name}-%{version}.tar.xz

BuildRequires:  pkgconfig(gstreamer-plugins-base-1.0) >= 0.11.92
BuildRequires:  pkgconfig(gtk+-3.0) >= 2.99.0
BuildRequires:  pkgconfig(libburn-1) >= 0.4.0
BuildRequires:  pkgconfig(libcanberra-gtk3)
BuildRequires:  pkgconfig(libisofs-1) >= 0.6.4
BuildRequires:  pkgconfig(libnotify) >= 0.7.0
%if %{with nautilus}
BuildRequires:  pkgconfig(libnautilus-extension) >= 2.22.2
%endif
BuildRequires:  pkgconfig(libxml-2.0) >= 2.6.0
%if %{with plparser}
BuildRequires:  pkgconfig(totem-plparser) >= 2.29.1
BuildRequires:  pkgconfig(tracker-sparql-3.0)
%endif
BuildRequires:  appstream
BuildRequires:  desktop-file-utils
BuildRequires:  gcc
BuildRequires:  gettext
BuildRequires:  gtk-doc
BuildRequires:  itstool
BuildRequires:  meson >= 1.4.0
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
%meson \
        -Dnautilus=%{?with_nautilus:enabled}%{!?with_nautilus:disabled} \
        -Dlibburn=enabled \
        -Dlibisofs=enabled \
        -Dsearch=%{?with_plparser:enabled}%{!?with_plparser:disabled} \
        -Dplaylist=%{?with_plparser:enabled}%{!?with_plparser:disabled} \
        -Dpreview=enabled \
        -Dcdrdao=%{?with_cdrdao:true}%{!?with_cdrdao:false} \
        -Dcdrkit=%{?with_cdrkit:true}%{!?with_cdrkit:false} \
        -Dgrowisofs=%{?with_dvdrwtools:true}%{!?with_dvdrwtools:false} \
        -Dgtk-doc=true
%meson_build


%install
%meson_install
%find_lang %{name}


%check
%meson_test


%ldconfig_scriptlets libs


%files -f %{name}.lang
%license COPYING
%doc AUTHORS NEWS README
%{_mandir}/man1/%{name}.*
%{_bindir}/*
%{_libdir}/brasero3
%{_datadir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/metainfo/org.gnome.Brasero.metainfo.xml
%{_datadir}/help/*
%{_datadir}/icons/hicolor/*/apps/*
%{_datadir}/mime/packages/*
%{_datadir}/glib-2.0/schemas/org.gnome.brasero.gschema.xml

%files libs
%{_libdir}/*.so.*

%if %{with nautilus}
%files nautilus
%{_libdir}/nautilus/extensions-3.0/*.so
%{_datadir}/applications/brasero-nautilus.desktop
%endif

%files devel
%doc %{_datadir}/gtk-doc/html/libbrasero-media
%doc %{_datadir}/gtk-doc/html/libbrasero-burn
%doc ChangeLog.old
%{_libdir}/*.so
%{_libdir}/pkgconfig/*.pc
%{_includedir}/brasero3


%changelog
%autochangelog
