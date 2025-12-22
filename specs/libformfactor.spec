Name:           libformfactor
Version:        0.3.2
Release:        %autorelease
Summary:        Efficient computation of scattering form factors of arbitrary polyhedra
# the library is under GPL-3.0-or-later
# test/3rdparty/catch.hpp - BSL-1.0
License:        GPL-3.0-or-later
URL:            https://jugit.fz-juelich.de/mlz/libformfactor
Source0:        %{url}/-/archive/v%{version}/%{name}-v%{version}.tar.bz2

BuildRequires:  gcc-c++
BuildRequires:  cmake
BuildRequires:  ninja-build
BuildRequires:  cmake(LibHeinz)

%description
A C++ library for the efficient computation of scattering form factors
(Fourier shape transforms) of arbitrary polyhedra according to Joachim Wuttke,
[J Appl Cryst 54, 580-587 (2021)](https://doi.org/10.1107/S1600576721001710).

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
The %{name}-devel package contains development files for %{name}.

%prep
%autosetup -p1 -n %{name}-v%{version}

sed -i 's|DESTINATION lib|DESTINATION %{_libdir}|g' ff/CMakeLists.txt
sed -i 's|DESTINATION cmake|DESTINATION %{_libdir}/cmake/formfactor|g' CMakeLists.txt

%build
%cmake
%cmake_build

%install
%cmake_install

%check
%ctest

%files
%license LICENSE
%doc README.md
%{_libdir}/libformfactor.so.%{version}

%files devel
%{_libdir}/libformfactor.so
%{_includedir}/ff/
%{_libdir}/cmake/formfactor/

%changelog
%autochangelog
