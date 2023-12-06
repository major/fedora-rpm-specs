# header-only library
%global debug_package %{nil}

Name:           libheinz
Version:        2.0.0
Release:        %autorelease
Summary:        C++ base library of Heinz Maier-Leibnitz Zentrum

License:        0BSD
URL:            https://jugit.fz-juelich.de/mlz/libheinz
Source0:        %{url}/-/archive/v%{version}/%{name}-v%{version}.tar.bz2

# use GNUInstallDirs to facilitate the installation of the library
# use ARCH_INDEPENDENT for header-only library when CMake >= 3.14
# create the INTERFACE library since the library is header-only and ALIAS targets
# install and export the targets
# https://jugit.fz-juelich.de/mlz/libheinz/-/issues/2
Patch0:         libheinz-fix-cmake.patch

BuildRequires:  gcc-c++
BuildRequires:  cmake

%description
It is a header-only C++ base library of Heinz Maier-Leibnitz Zentrum, which
provides several generic utilities for use in several products of the Scientific
Computing Group.

Contents:
- [Complex.h](inc/heinz/Complex.h). Defines `complex_t`, and a few elementary
functions.
- [Vectors3D.h](inc/heinz/Vectors3D.h). Templated 3D vectors, and abbreviations
`I3`, `R3`, `C3`.
- [Rotations3D.h](inc/heinz/Rotations3D.h). SO3 rotations, internally
parameterized by quaternions.

%package        devel
Summary:        Development files for %{name}
Provides:       %{name}-static%{?_isa} = %{version}-%{release}

%description    devel
The %{name}-devel package contains development files for %{name}.

%prep
%autosetup -p1 -n %{name}-v%{version}

%build
%cmake
%cmake_build

%install
%cmake_install

%check
%ctest

%files devel
%license LICENSE
%doc README.md
%{_includedir}/heinz/
%{_datadir}/cmake/LibHeinz/

%changelog
%autochangelog
