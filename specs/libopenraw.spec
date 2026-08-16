Summary:	Decode camera RAW files
Name:		libopenraw
Version:	0.3.7
Release:	%autorelease
License:	LGPL-3.0-or-later
URL:		https://libopenraw.freedesktop.org/libopenraw/
Source0:	http://libopenraw.freedesktop.org/download/%{name}-%{version}.tar.bz2

%global soname_version %{lua:
    print((string.gsub(macros.version, '^(%d+%.%d+)%..*$', '%1')))
}

BuildRequires:  boost-devel >= 1.33.1
BuildRequires:  cargo
BuildRequires:  gcc-c++
BuildRequires:  libjpeg-devel
BuildRequires:  make
BuildRequires:  pkgconfig(gdk-pixbuf-2.0)
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(libcurl)
BuildRequires:  pkgconfig(libxml-2.0) >= 2.5.0
BuildRequires:  rust >= 1.70
BuildRequires:  rust-packaging

%description
libopenraw is an ongoing project to provide a free software
implementation for camera RAW files decoding. One of the main reason is
that dcraw is not suited for easy integration into applications, and
there is a need for an easy to use API to build free software digital
image processing application.

%package gnome
Summary:	GUI components of %{name}
Requires:	%{name}%{?_isa} = %{version}-%{release}

%description gnome 
The %{name}-gnome package contains gui components of %{name}.

%package devel
Summary:	Development files for %{name}
Requires:	%{name}%{?_isa} = %{version}-%{release}

%description devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%package gnome-devel
Summary:	Development files for %{name}-gnome
Requires:	%{name}-gnome%{?_isa} = %{version}-%{release}
Requires:	%{name}-devel%{?_isa} = %{version}-%{release}

%description    gnome-devel
The %{name}-gnome-devel package contains libraries and header files for
developing applications that use %{name}-gnome.

%package pixbuf-loader
Summary:	RAW image loader for GTK+ applications
Requires:	%{name}%{?_isa} = %{version}-%{release}

%description pixbuf-loader
%{name}-pixbuf-loader contains a plugin to load RAW images, as created by
digital cameras, in GTK+ applications.

%prep
%autosetup
# this may be installed into a different prefix than gdk-pixbuf2 (e.g. flatpaks)
sed -i -e '/gdk_pixbuf_moduledir/s/PKG_CONFIG/& --define-variable=prefix=${prefix}/' configure

%build
%configure --disable-static --enable-gnome --disable-silent-rules

# Omit unused direct shared library dependencies.
sed --in-place --expression 's! -shared ! -Wl,--as-needed\0!g' libtool

%{make_build}

pushd lib/mp4
%cargo_license_summary
%{cargo_license} > ../../LICENSE.dependencies
popd

%check
make check

%install
%make_install
find $RPM_BUILD_ROOT -type f -name "*.la" -delete

%ldconfig_scriptlets

%ldconfig_scriptlets gnome


%files
# COPYING only covers a file in test/ which isn’t shipped
%license COPYING.LESSER MPL-2.0 LICENSE.dependencies
%doc AUTHORS NEWS README TODO
%{_libdir}/%{name}.so.*

%files gnome
%{_libdir}/%{name}gnome.so.*

%files devel
%{_libdir}/%{name}.so
%{_libdir}/pkgconfig/%{name}-%{soname_version}.pc

%dir %{_includedir}/%{name}-%{soname_version}
%{_includedir}/%{name}-%{soname_version}/%{name}/*.h

%files gnome-devel
%{_libdir}/%{name}gnome.so
%{_libdir}/pkgconfig/%{name}-gnome-%{soname_version}.pc

%dir %{_includedir}/%{name}-%{soname_version}/%{name}-gnome
%{_includedir}/%{name}-%{soname_version}/%{name}-gnome/gdkpixbuf.h

%files pixbuf-loader
%{_libdir}/gdk-pixbuf-2.0/*/loaders/*.so

%changelog
%autochangelog
