Name:           clutter-gst3
Version:        3.0.27
Release:        %autorelease
Summary:        GStreamer integration library for Clutter

License:        LGPLv2+
URL:            https://developer.gnome.org/clutter-gst/stable/
Source0:        https://download.gnome.org/sources/clutter-gst/3.0/clutter-gst-%{version}.tar.xz

Patch0:         remove-rgbx-bgrx-support.patch

BuildRequires:  /usr/bin/chrpath
BuildRequires:  pkgconfig(clutter-1.0)
BuildRequires:  pkgconfig(cogl-2.0-experimental)
BuildRequires:  pkgconfig(gio-2.0)
BuildRequires:  pkgconfig(gobject-introspection-1.0)
BuildRequires:  pkgconfig(gstreamer-1.0)
BuildRequires:  pkgconfig(gstreamer-audio-1.0)
BuildRequires:  pkgconfig(gstreamer-base-1.0)
BuildRequires:  pkgconfig(gstreamer-pbutils-1.0)
BuildRequires:  pkgconfig(gstreamer-plugins-base-1.0)
BuildRequires:  pkgconfig(gstreamer-tag-1.0)
BuildRequires:  pkgconfig(gstreamer-video-1.0)
BuildRequires:  pkgconfig(gudev-1.0)
BuildRequires:  make


%description
Clutter is an open source software library for creating fast, visually
rich and animated graphical user interfaces.

Clutter GStreamer enables the use of GStreamer with Clutter.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description devel
Clutter is an open source software library for creating fast, visually
rich and animated graphical user interfaces.

Clutter GStreamer enables the use of GStreamer with Clutter.

The %{name}-devel package contains libraries and header files for
developing applications that use clutter-gst API version 3.0.


%prep
%autosetup -p1 -n clutter-gst-%{version}


%build
%configure
make %{?_smp_mflags} V=1


%install
%make_install

find %{buildroot} -name '*.la' -delete

rm -rf %{buildroot}%{_libdir}/gstreamer-1.0/


%files
%doc AUTHORS NEWS README
%license COPYING
%{_libdir}/girepository-1.0/ClutterGst-3.0.typelib
%{_libdir}/libclutter-gst-3.0.so.*

%files devel
%{_includedir}/clutter-gst-3.0/
%{_libdir}/libclutter-gst-3.0.so
%{_libdir}/pkgconfig/clutter-gst-3.0.pc
%{_datadir}/gir-1.0/ClutterGst-3.0.gir
%doc %{_datadir}/gtk-doc/


%changelog
%autochangelog
