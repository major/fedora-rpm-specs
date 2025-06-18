%global catch_version 1.9.6
%global variant_version 1.1.5

%global debug_package %{nil}

Name:           geometry-hpp
Version:        2.0.3
Release:        %autorelease
Summary:        Generic C++ interfaces for geometry types, collections, and features

License:        ISC
URL:            https://github.com/mapbox/geometry.hpp
Source0:        https://github.com/mapbox/geometry.hpp/archive/v%{version}/%{name}-%{version}.tar.gz
# Make benchmarks optional (add a BENCHMARKS CMake option)
# https://github.com/mapbox/geometry.hpp/pull/74
Patch:          %{url}/pull/74.patch#/geometry-hpp-optional-benchmarks.patch
# Rip out mason stuff - we use our own packages
Patch:          geometry-hpp-mason.patch

BuildRequires:  cmake gcc-c++
BuildRequires:  catch1-devel >= %{catch_version}
BuildRequires:  mapbox-variant-devel >= %{variant_version}
BuildRequires:  mapbox-variant-static >= %{variant_version}

%description
Provides header-only, generic C++ interfaces for geometry
types, geometry collections, and features.

These types are designed to be easy to parse and serialize
to GeoJSON and to be a robust and high performance container
for data processing and conversion.


%package        devel
Summary:        Development files for %{name}
Provides:       %{name}-static = %{version}-%{release}

Requires:       mapbox-variant-devel >= %{variant_version}

%description    devel
Provides header-only, generic C++ interfaces for geometry
types, geometry collections, and features.

These types are designed to be easy to parse and serialize
to GeoJSON and to be a robust and high performance container
for data processing and conversion.


%prep
%autosetup -p 1 -n geometry.hpp-%{version}


%conf
%cmake -DWERROR:BOOL=OFF -DBENCHMARKS:BOOL=OFF


%build
%cmake_build


%install
# CMakeLists.txt does not handle installation.
mkdir -p %{buildroot}%{_includedir}
cp -pr include/mapbox %{buildroot}%{_includedir}


%check
%{_vpath_builddir}/unit-tests


%files devel
%doc README.md
%license LICENSE
%{_includedir}/mapbox


%changelog
%autochangelog
