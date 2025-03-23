%global commit0 98b0a46bce017382a6351a19577ec43a715b6835
%global shortcommit0 %(c=%{commit0}; echo ${c:0:7})
%global date0 20240619

%bcond_with check

Summary:        Conversion to/from half-precision floating point format
Name:           FP16
License:        MIT
Version:        1.0^git%{date0}.%{shortcommit0}
Release:        %autorelease

# Only a header
BuildArch:      noarch

URL:            https://github.com/Maratyszcza/%{name}
Source0:        %{url}/archive/%{commit0}/%{name}-%{shortcommit0}.tar.gz
# https://github.com/Maratyszcza/FP16/issues/36
Patch0:         0001-Revert-Remove-PeachPy-implementations.patch

BuildRequires: cmake
BuildRequires: gcc-c++
BuildRequires: python3-devel

%if %{with check}
BuildRequires: gtest-devel
%endif

%description
Header-only library for conversion to/from half-precision floating point formats

* Supports IEEE and ARM alternative half-precision floating-point format
  *  Property converts infinities and NaNs
  *  Properly converts denormal numbers, even on systems without denormal
     support
* Header-only library, no installation or build required
* Compatible with C99 and C++11
* Fully covered with unit tests and microbenchmarks


%package devel

Summary:        Conversion to/from half-precision floating point format
Provides:       %{name}-static = %{version}-%{release}
Requires: python3dist(peachpy)

%description devel
Header-only library for conversion to/from half-precision floating point formats

* Supports IEEE and ARM alternative half-precision floating-point format
  *  Property converts infinities and NaNs
  *  Properly converts denormal numbers, even on systems without denormal
     support
* Header-only library, no installation or build required
* Compatible with C99 and C++11
* Fully covered with unit tests and microbenchmarks

%prep
%autosetup -p1 -n %{name}-%{commit0}

%build

%cmake \
       -DFP16_USE_SYSTEM_LIBS=ON \
%if %{without check}
       -DFP16_BUILD_TESTS=OFF \
%endif
       -DFP16_BUILD_BENCHMARKS=OFF \
       
%cmake_build

%if %{with check}
%check
%ctest
%endif

%install
%cmake_install

mkdir -p %{buildroot}%{python3_sitelib}/fp16
cp -p include/fp16/*.py %{buildroot}%{python3_sitelib}/fp16

%files devel
%license LICENSE
%doc README.md
%{_includedir}/fp16.h
%{_includedir}/fp16/
%{python3_sitelib}/fp16/*

%changelog
%autochangelog
