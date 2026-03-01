Name: libmypaint
Version: 1.6.1
Release: %autorelease
Summary: Library for making brush strokes

# Compute some version related macros.
%global major %{lua:
    print((string.gsub(macros.version, '^(%d+)%..*$', '%1')))
}
%global minor %{lua:
    print((string.gsub(macros.version, '^%d+%.(%d+)%..*$', '%1')))
}
%global micro %{lua:
    print((string.gsub(macros.version, '^%d+%.%d+%.(%d+).*$', '%1')))
}

License: ISC
URL: https://github.com/mypaint/libmypaint
Source0: https://github.com/mypaint/libmypaint/releases/download/v%{version}/libmypaint-%{version}.tar.xz

BuildRequires: doxygen
BuildRequires: gcc
BuildRequires: intltool
BuildRequires: make
BuildRequires: pkgconfig(gobject-2.0)
BuildRequires: pkgconfig(gobject-introspection-1.0) >= 1.32.0
BuildRequires: pkgconfig(json-c)
BuildRequires: python3-breathe
BuildRequires: python3-sphinx

%description
This is a self-contained library containing the MyPaint brush engine.

%package devel
Summary: Development files for libmypaint
Requires: %{name}%{?isa} = %{?epoch:%{epoch}:}%{version}-%{release}
Requires: pkgconfig

%description devel
This package contains files needed for development with libmypaint.

%prep
%autosetup -p1

%build
%configure --enable-docs --enable-introspection=yes --disable-gegl
%make_build

%install
%make_install
find %{buildroot}%{_libdir} -name '*.la' -delete -print

%find_lang %{name}

%ldconfig_scriptlets

%check
make check

%files -f %{name}.lang
%license COPYING
%doc README.md
%{_libdir}/libmypaint.so.0*
%dir %{_libdir}/girepository-1.0
%{_libdir}/girepository-1.0/MyPaint-%{major}.%{minor}.typelib

%files devel
%doc doc/build/*
%{_libdir}/libmypaint.so
%{_includedir}/%{name}
%{_libdir}/pkgconfig/libmypaint.pc
%dir %{_datadir}/gir-1.0
%{_datadir}/gir-1.0/MyPaint-%{major}.%{minor}.gir

%changelog
%autochangelog
