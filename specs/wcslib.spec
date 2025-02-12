Name: wcslib
Version: 8.4
Release: %autorelease
Summary: An implementation of the FITS World Coordinate System standard

# Library is under LGPLv3+ utils under GPLv3+
License: LGPL-3.0-or-later
URL: https://www.atnf.csiro.au/computing/software/wcs/index.html
Source0: https://www.atnf.csiro.au/computing/software/wcs/WCS/wcslib-%{version}.tar.bz2

# General stuff
BuildRequires: make
BuildRequires: flex
BuildRequires: gcc
# Development libraries
BuildRequires: cfitsio-devel
BuildRequires: zlib-devel

%description
WCSLIB is a library that implements the "World Coordinate System" (WCS) 
convention in FITS (Flexible Image Transport System)

%package devel
Summary: Libraries, includes, etc. used to develop an application with %{name}
License: LGPL-3.0-or-later
Requires: wcslib = %{version}-%{release}
%description devel
These are the files needed to develop an application using %{name}.

%package utils
Summary: Utility programs provided by %{name}
License: GPL-3.0-or-later
Requires: wcslib = %{version}-%{release}
%description utils
Utils provided with %{name}

%prep
%setup -q 

%build
%configure --disable-fortran --disable-static
# Does not like multithread builds...
make

%install
make install DESTDIR=%{buildroot}
# fix permissions
rm -rf %{buildroot}%{_datadir}/doc/wcslib*
chmod 755 %{buildroot}%{_includedir}/wcslib-%{version}

%check
make check

%ldconfig_scriptlets

%files
%license COPYING.LESSER
%doc README
%{_libdir}/*.so.*

%files devel
%license COPYING.LESSER
%doc html wcslib.pdf
%{_libdir}/*.so
%exclude %{_libdir}/*.a
%{_libdir}/pkgconfig/wcslib.pc
%{_includedir}/wcslib
%{_includedir}/wcslib-%{version}

%files utils
%license COPYING 
%{_bindir}/*
%{_mandir}/man1/*

%changelog
%autochangelog
