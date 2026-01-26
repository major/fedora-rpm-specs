%global gitdate 20251028
%global commit 39b8965fa2cad6de9f609a3796b16efaf64fb2e8
%global shortcommit %(c=%{commit}; echo ${c:0:7})

Name:           pagmo2
Version:        2.19.1^%{gitdate}git%{shortcommit}
Release:        %autorelease
Summary:        A C++ platform to perform parallel computations of optimisation tasks
License:        LGPL-3.0-or-later OR GPL-3.0-or-later
URL:            https://github.com/esa/pagmo2
Source0:        %{url}/archive/%{commit}/%{name}-%{shortcommit}.tar.gz

BuildRequires:  gcc-c++
BuildRequires:  cmake
BuildRequires:  eigen3-devel
BuildRequires:  tbb-devel
BuildRequires:  boost-devel
BuildRequires:  pkgconfig(nlopt)
%ifnarch %{ix86}
BuildRequires:  pkgconfig(ipopt)
%endif

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
%autosetup -p1 -C

%build
%cmake \
    -DCMAKE_BUILD_TYPE=RelWithDebInfo \
    -DPAGMO_BUILD_TESTS=ON \
    -DPAGMO_WITH_EIGEN3=ON \
    -DPAGMO_WITH_NLOPT=ON \
%ifnarch %{ix86}
    -DPAGMO_WITH_IPOPT=ON \
%endif
    -DPAGMO_ENABLE_IPO=ON
%cmake_build

%install
%cmake_install

%check
%ctest -E bfe

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
