# header-only library
%global debug_package %{nil}

%global forgeurl https://github.com/jlblancoc/nanoflann
Version:        1.7.0
%forgemeta

Name:           nanoflann
Release:        %autorelease
Summary:        A C++11 header-only library for Nearest Neighbor (NN) search with KD-trees
License:        BSD-3-Clause
URL:            %{forgeurl}
Source0:        %{forgesource}

BuildRequires:  gcc-c++
BuildRequires:  cmake
BuildRequires:  ninja-build
BuildRequires:  cmake(gtest)

%description
nanoflann is a C++11 header-only library for building KD-Trees of datasets with
different topologies: R2, R3 (point clouds), SO(2) and SO(3) (2D and 3D rotation
groups). No support for approximate NN is provided.

%package        devel
Summary:        Development files for %{name}
Provides:       %{name}-static%{?_isa} = %{version}-%{release}

%description    devel
nanoflann is a C++11 header-only library for building KD-Trees of datasets with
different topologies: R2, R3 (point clouds), SO(2) and SO(3) (2D and 3D rotation
groups). No support for approximate NN is provided.

The %{name}-devel package contains development files for %{name}.

%prep
%forgeautosetup -p1

rm -r tests/gtest-1.8.0

%build
%cmake \
    -GNinja \
    -DCMAKE_BUILD_TYPE=Release \
    -DNANOFLANN_USE_SYSTEM_GTEST=ON \

%cmake_build

%install
%cmake_install

%check
%ctest

%files devel
%license COPYING
%doc README.md
%{_includedir}/nanoflann.hpp
%{_libdir}/pkgconfig/nanoflann.pc
%{_datadir}/cmake/nanoflann/

%changelog
%autochangelog
