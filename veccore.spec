# header-only library
%global debug_package %{nil}

%global forgeurl https://github.com/root-project/veccore
Version:        0.8.1
%forgemeta

Name:           veccore
Release:        %autorelease
Summary:        C++ Library for Portable SIMD Vectorization
License:        Apache-2.0
URL:            %{forgeurl}
Source0:        %{forgesource}

BuildRequires:  gcc-c++
BuildRequires:  cmake
BuildRequires:  ninja-build
BuildRequires:  gtest-devel

%description
VecCore is a simple abstraction layer on top of other vectorization libraries.
It provides an architecture-independent API for expressing vector operations on
data. Code written with this API can then be dispatched to one of several
backends implemented using libraries like Vc, UME::SIMD, or a scalar
implementation.

%package        devel
Summary:        Development files for %{name}
Provides:       %{name}-static = %{version}-%{release}

%description    devel
This package contains development files for %{name}.

%prep
%forgeautosetup -p1

%build
%cmake \
    -GNinja \
    -DBUILD_TESTING=ON \

%cmake_build

%install
%cmake_install

%check
%ctest

%files devel
%license LICENSE
%doc README.md
%{_includedir}/VecCore/
%dir %{_libdir}/cmake/VecCore
%{_libdir}/cmake/VecCore/*.cmake

%changelog
%autochangelog
