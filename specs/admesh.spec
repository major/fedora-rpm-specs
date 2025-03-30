Name:           admesh
Version:        0.98.5
Release:        %autorelease
Summary:        Diagnose and/or repair problems with STereo Lithography files
# Automatically converted from old format: GPLv2+ - review is highly recommended.
License:        GPL-2.0-or-later
URL:            http://github.com/admesh/admesh/
Source:         http://github.com/admesh/admesh/releases/download/v%{version}/admesh-%{version}.tar.gz
BuildRequires:  gcc
BuildRequires:  make
Requires:       %{name}-libs%{?_isa} = %{version}-%{release}

# https://fedoraproject.org/wiki/Changes/EncourageI686LeafRemoval
%if 0%{?fedora} >= 42 || 0%{?rhel} >= 11
ExcludeArch:    %{ix86}
%endif

%description
ADMesh is a program for diagnosing and/or repairing commonly encountered
problems with STL (STereo Lithography) data files. It can remove degenerate
and unconnected facets, connect nearby facets, fill holes by adding facets,
and repair facet normals. Simple transformations such as scaling,
translation and rotation are also supported. ADMesh can read both
ASCII and binary format STL files, while the output can be in
AutoCAD DXF, Geomview OFF, STL, or VRML format.

%package devel
Summary:        Development files for the %{name} library
Requires:       %{name}-libs%{?_isa} = %{version}-%{release}

%description devel
ADMesh is a program for diagnosing and/or repairing commonly encountered
problems with STL (STereo Lithography) data files.

This package contains the development files needed for building new
applications that utilize the %{name} library.

%package libs
Summary:        Runtime library for the %{name} application

%description libs
This package contains the %{name} runtime library.

%prep
%autosetup -p1

%build
%configure
# Pass the -v option to libtool so we can better see what's going on
%make_build CFLAGS="%{optflags}" LIBTOOLFLAGS="-v"

%install
%make_install
# Remove the documentation installed by "make install" (rpm will handle that)
rm -rf %{buildroot}%{_defaultdocdir}/%{name}
# Remove the libtool archive installed by "make install"
rm -f %{buildroot}%{_libdir}/lib%{name}.la

%files
%doc ChangeLog ChangeLog.old README.md
%doc %{name}-doc.txt block.stl
%{_bindir}/%{name}
%{_mandir}/man1/*

%files devel
%dir %{_includedir}/admesh/
%{_includedir}/admesh/stl.h
%{_libdir}/lib%{name}.so
%{_libdir}/pkgconfig/*

%files libs
%doc AUTHORS
%license COPYING
%{_libdir}/lib%{name}.so.1*

%changelog
%autochangelog
