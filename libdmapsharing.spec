Name: libdmapsharing
Version: 2.9.41
Release: %autorelease
License: LGPLv2+
Source: http://www.flyn.org/projects/libdmapsharing/%{name}-%{version}.tar.gz
URL: http://www.flyn.org/projects/libdmapsharing/
Summary: A DMAP client and server library
BuildRequires: pkgconfig, glib2-devel, libsoup-devel >= 2.32
BuildRequires: gdk-pixbuf2-devel, gstreamer1-plugins-base-devel
BuildRequires: pkgconfig(avahi-client) pkgconfig(avahi-glib)
BuildRequires: vala libgee-devel
BuildRequires: make

%description 
libdmapsharing implements the DMAP protocols. This includes support for
DAAP and DPAP.

%files 
%{_libdir}/libdmapsharing-3.0.so.*
%doc AUTHORS COPYING ChangeLog README

%package devel
Summary: Libraries/include files for libdmapsharing
Requires: %{name} = %{version}-%{release}
# -vala subpackage removed in F30
Obsoletes: libdmapsharing-vala < 2.9.37-8
Provides: libdmapsharing-vala = %{version}-%{release}

%description devel
libdmapsharing implements the DMAP protocols. This includes support for
DAAP and DPAP.  This package provides the libraries, include files, and
other resources needed for developing applications using libdmapsharing.

%files devel
%{_libdir}/pkgconfig/libdmapsharing-3.0.pc
%{_includedir}/libdmapsharing-3.0/
%{_libdir}/libdmapsharing-3.0.so
%{_libdir}/girepository-1.0/DMAP-3.0.typelib
%{_datadir}/gtk-doc/html/libdmapsharing-3.0
%{_datadir}/gir-1.0/DMAP-3.0.gir
%dir %{_datadir}/vala
%dir %{_datadir}/vala/vapi
%{_datadir}/vala/vapi/libdmapsharing-3.0.vapi

%prep
%setup -q

%build
%configure --disable-static --disable-tests --disable-check
make %{?_smp_mflags}

%install
make install DESTDIR=$RPM_BUILD_ROOT INSTALL="install -p"
rm -f ${RPM_BUILD_ROOT}%{_libdir}/libdmapsharing-3.0.la

%ldconfig_scriptlets

%changelog
%autochangelog
