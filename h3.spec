%global forgeurl https://github.com/uber/h3
Version:        4.1.0
%forgemeta

Name:           h3
Release:        %autorelease
Summary:        Hexagonal hierarchical geospatial indexing system
License:        Apache-2.0
URL:            %{forgeurl}
Source0:        %{forgesource}

# Use CMAKE_INSTALL_LIBDIR
Patch0:         https://github.com/uber/h3/pull/819.patch

BuildRequires:  gcc-c++
BuildRequires:  cmake
BuildRequires:  ninja-build

%description
H3 is a geospatial indexing system using a hexagonal grid that can be
(approximately) subdivided into finer and finer hexagonal grids, combining the
benefits of a hexagonal grid with S2's hierarchical subdivisions.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
The %{name}-devel package contains development files for %{name}.

%prep
%forgeautosetup -p1

%build
%cmake \
    -GNinja \
    -DCMAKE_BUILD_TYPE=RelWithDebInfo \
    -DENABLE_DOCS=OFF \

%cmake_build

%install
%cmake_install

%check
%ctest

%files
%license LICENSE
%doc README.md
%{_libdir}/libh3.so.1

%files devel
%{_includedir}/h3/h3api.h
%{_libdir}/libh3.so
%{_libdir}/cmake/h3/
%{_bindir}/cellToBoundary
%{_bindir}/cellToBoundaryHier
%{_bindir}/cellToLatLng
%{_bindir}/cellToLatLngHier
%{_bindir}/cellToLocalIj
%{_bindir}/gridDisk
%{_bindir}/gridDiskUnsafe
%{_bindir}/h3
%{_bindir}/h3ToComponents
%{_bindir}/h3ToHier
%{_bindir}/latLngToCell
%{_bindir}/localIjToCell

%changelog
%autochangelog
