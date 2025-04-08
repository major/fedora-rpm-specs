%global xfceversion 4.20

%global namespc Libxfce4util

Name:           libxfce4util
Version:        4.20.1
Release:        %autorelease
Summary:        Utility library for the Xfce4 desktop environment

# Automatically converted from old format: LGPLv2+ - review is highly recommended.
License:        LicenseRef-Callaway-LGPLv2+
URL:            http://www.xfce.org/
Source0:        http://archive.xfce.org/src/xfce/%{name}/%{xfceversion}/%{name}-%{version}.tar.bz2
#VCS: git:git://git.xfce.org/xfce/libxfce4util

BuildRequires:  gcc-c++
BuildRequires:  pkgconfig(glib-2.0) >= 2.24.0
BuildRequires:  gettext
BuildRequires:  intltool
BuildRequires:  gtk-doc
BuildRequires:  gobject-introspection-devel
BuildRequires:  vala
BuildRequires:  make

%description
This package includes basic utility non-GUI functions for Xfce4.

%package devel
Summary: Developpment tools for libxfce4util library
Requires: %{name} = %{version}-%{release}
Requires: glib2-devel
Requires: gtk3-devel
Requires: pkgconfig

%description devel
This package includes static libraries and header files for the
libxfce4util library.

%prep
%setup -q

%build
%configure --disable-static
# Remove rpaths
sed -i 's|^hardcode_libdir_flag_spec=.*|hardcode_libdir_flag_spec=""|g' libtool
sed -i 's|^runpath_var=LD_RUN_PATH|runpath_var=DIE_RPATH_DIE|g' libtool
export LD_LIBRARY_PATH="`pwd`/libxfce4util/.libs"

%make_build

%install
%make_install

# kevin identified the issue - fixes wrong library permissions
chmod 755 %{buildroot}/%{_libdir}/*.so

rm -f %{buildroot}%{_libdir}/*.la

%find_lang %{name}

%ldconfig_scriptlets

%files -f %{name}.lang
%license COPYING
%doc AUTHORS ChangeLog NEWS
%{_libdir}/lib*.so.*
%{_sbindir}/xfce4-kiosk-query
%{_libdir}/girepository-1.0/%{namespc}-1.0.typelib
%{_datadir}/gir-1.0/%{namespc}-1.0.gir
%{_datadir}/vala/vapi/%{name}-1.0.vapi

%files devel
%{_libdir}/lib*.so
%{_libdir}/pkgconfig/*.pc
%{_includedir}/xfce4
%doc %{_datadir}/gtk-doc/

%changelog
%autochangelog
