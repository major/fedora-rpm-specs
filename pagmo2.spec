%global forgeurl https://github.com/esa/pagmo2
Version:        2.19.0
%forgemeta

Name:           pagmo2
Release:        %autorelease
Summary:        A C++ platform to perform parallel computations of optimisation tasks
License:        LGPL-3.0-or-later OR GPL-3.0-or-later
URL:            %{forgeurl}
Source0:        %{forgesource}

BuildRequires:  gcc-c++
BuildRequires:  cmake
BuildRequires:  ninja-build
BuildRequires:  eigen3-devel
BuildRequires:  tbb-devel
BuildRequires:  boost-devel
BuildRequires:  pkgconfig(nlopt)
BuildRequires:  pkgconfig(ipopt)

%description
pagmo is a C++ scientific library for massively parallel optimization. It is
built around the idea of providing a unified interface to optimization
algorithms and to optimization problems and to make their deployment in
massively parallel environments easy.

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
    -DPAGMO_BUILD_TESTS=ON \
    -DPAGMO_WITH_EIGEN3=ON \
    -DPAGMO_WITH_NLOPT=ON \
    -DPAGMO_WITH_IPOPT=ON \
    -DPAGMO_ENABLE_IPO=ON \

%cmake_build

%install
%cmake_install

%check
%ctest

%files
%license COPYING.gpl3 COPYING.lgpl3
%doc README.md
%{_libdir}/libpagmo.so.9*

%files devel
%{_libdir}/libpagmo.so
%{_includedir}/pagmo/
%{_libdir}/cmake/pagmo/

%changelog
%autochangelog
