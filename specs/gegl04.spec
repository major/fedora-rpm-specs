%global apiver 0.4

%if 0%{?rhel}
%bcond lensfun 0
%else
%bcond lensfun 1
%endif

# Whether or not docs should be built
%bcond docs 1

Name:           gegl04
Version:        0.4.52
Release:        %autorelease
Summary:        Graph based image processing framework

# The binary is under the GPL, while the libs are under LGPL.
License:        GPL-3.0-or-later AND LGPL-3.0-or-later
URL:            https://www.gegl.org/
Source0:        http://download.gimp.org/pub/gegl/%{apiver}/gegl-%{version}.tar.xz
# Include <stdio.h> for fprintf()
# https://gitlab.gnome.org/GNOME/gegl/-/merge_requests/207
Patch:          0001-Include-stdio.h-for-fprintf.patch

BuildRequires:  chrpath
BuildRequires:  enscript
BuildRequires:  gcc-c++
BuildRequires:  gettext-devel >= 0.19.8
BuildRequires:  gobject-introspection-devel >= 1.32.0
BuildRequires:  gtk-doc
BuildRequires:  libspiro-devel
BuildRequires:  meson
BuildRequires:  perl-interpreter
BuildRequires:  ruby
BuildRequires:  suitesparse-devel
BuildRequires:  vala
BuildRequires:  asciidoc

BuildRequires:  pkgconfig(babl-0.1) >= 0.1.100
BuildRequires:  pkgconfig(cairo) >= 1.12.2
BuildRequires:  pkgconfig(exiv2) >= 0.25
BuildRequires:  pkgconfig(gdk-pixbuf-2.0) >= 2.32.0
BuildRequires:  pkgconfig(gexiv2)
BuildRequires:  pkgconfig(glib-2.0) >= 2.44.0
BuildRequires:  pkgconfig(jasper) >= 1.900.1
BuildRequires:  pkgconfig(json-glib-1.0)
BuildRequires:  pkgconfig(lcms2) >= 2.8
%if %{with lensfun}
BuildRequires:  pkgconfig(lensfun) >= 0.2.5
%endif
BuildRequires:  pkgconfig(libraw) >= 0.15.4
BuildRequires:  pkgconfig(libpng) >= 1.6.0
BuildRequires:  pkgconfig(librsvg-2.0) >= 2.40.6
BuildRequires:  pkgconfig(libv4l2) >= 1.0.1
BuildRequires:  pkgconfig(libwebp) >= 0.5.0
BuildRequires:  pkgconfig(lua) >= 5.1.0

%if ! 0%{?rhel}
%ifarch aarch64 %{ix86} x86_64
BuildRequires:  pkgconfig(luajit) >= 2.0.4
%endif
BuildRequires:  pkgconfig(OpenEXR) >= 2.5.4
%endif

BuildRequires:  pkgconfig(pango) >= 1.38.0
BuildRequires:  pkgconfig(pangocairo) >= 1.38.0
BuildRequires:  pkgconfig(pygobject-3.0) >= 3.2
BuildRequires:  pkgconfig(sdl2) >= 2.0.5
BuildRequires:  pkgconfig(vapigen) >= 0.20.0
BuildRequires:  pkgconfig(libtiff-4) >= 4.0.0

# operations/common/magick-load.c has a fallback image loader which uses /usr/bin/convert
# However, this code path has no error handling, so no application should rely on it; and
# there is a general trend to migrate away from ImageMagick.
# Requires:       /usr/bin/convert

# gegl contains a stripped down version of poly2tri-c, a C+glib port of
# poly2tri, a 2D constrained Delaunay triangulation library.
# Version information:
#     CURRENT REVISION: b27c5b79df2ffa4e2cb37f9e5536831f16afb11b
#     CACHED ON: August 11th, 2012
Provides:       bundled(poly2tri-c)
Obsoletes:      gegl03 < 0.3.31

%description
GEGL (Generic Graphics Library) is a graph based image processing framework.
GEGLs original design was made to scratch GIMP's itches for a new
compositing and processing core. This core is being designed to have
minimal dependencies and a simple well defined API.


%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Obsoletes:      %{name}-devel < 0.4.2
Obsoletes:      gegl03-devel < 0.3.31
Conflicts:      %{name}-devel < 0.4.2

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use GEGL API version %{apiver}.


%if %{with docs}
%package        devel-docs
Summary:        Documentation files for developing with %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Obsoletes:      %{name}-devel < 0.4.2
Obsoletes:      gegl03-devel-docs < 0.3.31
Conflicts:      %{name}-devel < 0.4.2
Conflicts:      gegl-devel < 0.4

%description    devel-docs
The %{name}-devel-docs package contains documentation files for developing
applications that use GEGL API version %{apiver}.
%endif


%package        tools
Summary:        Command line tools for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Obsoletes:      gegl03-tools < 0.3.31
Conflicts:      gegl < 0.4

%description    tools
The %{name}-tools package contains tools for the command line that use the
GEGL library.


%prep
%autosetup -p1 -n gegl-%{version}


%build
%meson --auto-features=auto %{!?with_docs:-Ddocs=false -Dgtk-doc=false}%{?with_docs:-Ddocs=true -Dgtk-doc=true}
%meson_build


%install
%meson_install

# Remove rpaths
chrpath --delete %{buildroot}%{_bindir}/*
chrpath --delete %{buildroot}%{_libdir}/*.so*
chrpath --delete %{buildroot}%{_libdir}/gegl-%{apiver}/*.so

%find_lang gegl-%{apiver}


%ldconfig_scriptlets


%files -f gegl-%{apiver}.lang
%license COPYING.LESSER
%{_libdir}/gegl-%{apiver}/
%{_libdir}/libgegl-%{apiver}.so.*
%{_libdir}/libgegl-npd-%{apiver}.so
%{_libdir}/libgegl-sc-%{apiver}.so
%{_libdir}/girepository-1.0/Gegl-%{apiver}.typelib

%if ! 0%{?rhel}
%ifarch aarch64 %{ix86} x86_64
%dir %{_datadir}/gegl-%{apiver}/
%{_datadir}/gegl-%{apiver}/lua/
%endif
%endif

%files devel
%{_includedir}/gegl-%{apiver}/
%{_libdir}/libgegl-%{apiver}.so
%{_libdir}/pkgconfig/gegl-%{apiver}.pc
%{_libdir}/pkgconfig/gegl-sc-%{apiver}.pc
%dir %{_datadir}/gir-1.0
%{_datadir}/gir-1.0/Gegl-%{apiver}.gir
%dir %{_datadir}/vala
%dir %{_datadir}/vala/vapi
%{_datadir}/vala/vapi/gegl-%{apiver}.deps
%{_datadir}/vala/vapi/gegl-%{apiver}.vapi

%if %{with docs}
%files devel-docs
%doc %{_datadir}/gtk-doc/
%endif

%files tools
%license COPYING
%{_bindir}/*


%changelog
%autochangelog
