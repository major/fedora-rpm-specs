%bcond_without autoreconf

Name:           readosm
Version:        1.1.0a
%global so_version 1
Release:        %autorelease
Summary:        Library to extract valid data from within an Open Street Map input file

License:        MPLv1.1 or GPLv2+ or LGPLv2+
Source0:        https://www.gaia-gis.it/gaia-sins/readosm-sources/readosm-%{version}.tar.gz
URL:            https://www.gaia-gis.it/fossil/readosm

%if %{with autoreconf}
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  libtool
%endif

BuildRequires:  make
BuildRequires:  gcc

BuildRequires:  expat-devel
BuildRequires:  zlib-devel

%description
ReadOSM is a simple library intended for extracting the contents from 
Open Street Map files: both input formats (.osm XML based and .osm.pbf based
on Google's Protocol Buffer serialization) are indifferently supported.

%package devel
Summary:        Development libraries and headers for ReadOSM

Requires:       readosm%{?_isa} = %{version}-%{release}

%description devel
The readosm-devel package contains libraries and header files for
developing applications that use ReadOSM.


%prep
%autosetup


%build
%if %{with autoreconf}
autoreconf --force --install --verbose
%endif
%configure --disable-static
%make_build


%install
%make_install
# Delete undesired libtool archives
find '%{buildroot}' -type f -name '*.la' -print -delete


%check
%make_build check


%files
%license COPYING
%doc AUTHORS

%{_libdir}/libreadosm.so.%{so_version}
%{_libdir}/libreadosm.so.%{so_version}.*


%files devel
%{_libdir}/pkgconfig/readosm.pc
%{_libdir}/libreadosm.so
%{_includedir}/readosm.h


%changelog
%autochangelog
