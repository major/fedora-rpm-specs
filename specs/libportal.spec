%bcond qt5 %[%{undefined rhel} || 0%{?rhel} < 10]

Name:           libportal
Version:        0.11.0
Release:        %autorelease
Summary:        Flatpak portal library
# doc/urlmap.js is LGPL-2.1-or-later
# everything else is LGPL-3.0-only
License:        LGPL-3.0-only AND LGPL-2.1-or-later
Url:            https://github.com/flatpak/libportal
Source:         https://github.com/flatpak/libportal/releases/download/%{version}/%{name}-%{version}.tar.xz

BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  gi-docgen
BuildRequires:  meson
BuildRequires:  vala
BuildRequires:  pkgconfig(gio-2.0)
BuildRequires:  pkgconfig(gio-unix-2.0)
BuildRequires:  pkgconfig(gobject-introspection-1.0)
BuildRequires:  pkgconfig(gtk+-3.0)
BuildRequires:  pkgconfig(gtk4)
BuildRequires:  pkgconfig(Qt6Core)
BuildRequires:  pkgconfig(Qt6Gui)
BuildRequires:  pkgconfig(Qt6Widgets)
BuildRequires:  qt6-qtbase-private-devel
%if %{with qt5}
BuildRequires:  pkgconfig(Qt5Core)
BuildRequires:  pkgconfig(Qt5Gui)
BuildRequires:  pkgconfig(Qt5Widgets)
BuildRequires:  pkgconfig(Qt5X11Extras)
%endif

%description
libportal provides GIO-style asynchronous APIs for most Flatpak portals.

%package gtk3
Summary: GTK+ 3 libraries for %name
Requires: %{name}%{?_isa} = %{version}-%{release}

%description gtk3
%name provides GIO-style asynchronous APIs for most Flatpak portals.

This package provides files for GTK+ 3 and %name.

%package gtk4
Summary: GTK 4 libraries for %name
Requires: %{name}%{?_isa} = %{version}-%{release}

%description gtk4
%name provides GIO-style asynchronous APIs for most Flatpak portals.

This package provides files for GTK 4 and %name.

%package qt6
Summary: Qt6 libraries for %name
Requires: %{name}%{?_isa} = %{version}-%{release}

%description qt6
%name provides GIO-style asynchronous APIs for most Flatpak portals.

This package provides files for Qt 6 and %name.

%if %{with qt5}
%package qt5
Summary: Qt5 libraries for %name
Requires: %{name}%{?_isa} = %{version}-%{release}

%description qt5
%name provides GIO-style asynchronous APIs for most Flatpak portals.

This package provides files for Qt 5 and %name.
%endif

%package devel
Summary: Development files and libraries for %name
Requires: %{name}%{?_isa} = %{version}-%{release}

%description devel
%name provides GIO-style asynchronous APIs for most Flatpak portals.

This package provides files for development with %name.

%package gtk3-devel
Summary: GTK+ 3 development files and libraries for %name
Requires: %{name}-devel%{?_isa} = %{version}-%{release}
Requires: %{name}-gtk3%{?_isa} = %{version}-%{release}

%description gtk3-devel
%name provides GIO-style asynchronous APIs for most Flatpak portals.

This package provides files for development with GTK+ 3 and %name.

%package gtk4-devel
Summary: GTK 4 development files and libraries for %name
Requires: %{name}-devel%{?_isa} = %{version}-%{release}
Requires: %{name}-gtk4%{?_isa} = %{version}-%{release}

%description gtk4-devel
%name provides GIO-style asynchronous APIs for most Flatpak portals.

This package provides files for development with GTK 4 and %name.

%package qt6-devel
Summary: Qt 6 development files and libraries for %name
Requires: %{name}-devel%{?_isa} = %{version}-%{release}
Requires: %{name}-qt6%{?_isa} = %{version}-%{release}

%description qt6-devel
%name provides GIO-style asynchronous APIs for most Flatpak portals.

This package provides files for development with Qt 6 and %name.

%if %{with qt5}
%package qt5-devel
Summary: Qt 5 development files and libraries for %name
Requires: %{name}-devel%{?_isa} = %{version}-%{release}
Requires: %{name}-qt5%{?_isa} = %{version}-%{release}

%description qt5-devel
%name provides GIO-style asynchronous APIs for most Flatpak portals.

This package provides files for development with Qt 5 and %name.
%endif

%package devel-doc
Summary: Development documentation for libportal
# Because web fonts from upstream are not bundled in the gi-docgen package,
# packages containing documentation generated with gi-docgen should depend on
# this metapackage to ensure the proper system fonts are present.
Recommends: gi-docgen-fonts
BuildArch: noarch

%description devel-doc
libportal provides GIO-style asynchronous APIs for most Flatpak portals.

This package provides development documentations for libportal.

%prep
%autosetup -p1

%build
%meson \
  -Dbackend-gtk3=enabled \
  -Dbackend-gtk4=enabled \
  -Dbackend-qt6=enabled \
%if %{with qt5}
  -Dbackend-qt5=enabled \
%else
  -Dbackend-qt5=disabled \
%endif
  %{nil}
%meson_build

%install
%meson_install

%files
%license COPYING
%doc README.md NEWS
%{_libdir}/girepository-1.0/Xdp-1.0.typelib
%{_libdir}/libportal.so.1*

%files gtk3
%{_libdir}/girepository-1.0/XdpGtk3-1.0.typelib
%{_libdir}/libportal-gtk3.so.1*

%files gtk4
%{_libdir}/girepository-1.0/XdpGtk4-1.0.typelib
%{_libdir}/libportal-gtk4.so.1*

%if %{with qt5}
%files qt5
%{_libdir}/libportal-qt5.so.1*
%endif

%files qt6
%{_libdir}/libportal-qt6.so.1*

%files devel
%{_datadir}/gir-1.0/Xdp-1.0.gir
%{_datadir}/vala/vapi/libportal.deps
%{_datadir}/vala/vapi/libportal.vapi
%{_includedir}/libportal
%{_libdir}/libportal.so
%{_libdir}/pkgconfig/libportal.pc

%files gtk3-devel
%{_datadir}/gir-1.0/XdpGtk3-1.0.gir
%{_datadir}/vala/vapi/libportal-gtk3.deps
%{_datadir}/vala/vapi/libportal-gtk3.vapi
%{_includedir}/libportal-gtk3
%{_libdir}/libportal-gtk3.so
%{_libdir}/pkgconfig/libportal-gtk3.pc

%files gtk4-devel
%{_datadir}/gir-1.0/XdpGtk4-1.0.gir
%{_datadir}/vala/vapi/libportal-gtk4.deps
%{_datadir}/vala/vapi/libportal-gtk4.vapi
%{_includedir}/libportal-gtk4
%{_libdir}/libportal-gtk4.so
%{_libdir}/pkgconfig/libportal-gtk4.pc

%if %{with qt5}
%files qt5-devel
%{_includedir}/libportal-qt5
%{_libdir}/libportal-qt5.so
%{_libdir}/pkgconfig/libportal-qt5.pc
%endif

%files qt6-devel
%{_includedir}/libportal-qt6
%{_libdir}/libportal-qt6.so
%{_libdir}/pkgconfig/libportal-qt6.pc

%files devel-doc
%{_datadir}/doc/libportal-1

%changelog
%autochangelog
