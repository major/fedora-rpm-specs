Name:           sparrow
Version:        2.3.0
Release:        %autorelease
Summary:        C++20 idiomatic APIs for the Apache Arrow Columnar Format
License:        Apache-2.0
URL:            https://github.com/man-group/sparrow
%global github  https://github.com/man-group/sparrow
Source:         %{github}/archive/%{version}/%{name}-%{version}.tar.gz
Patch0:         %{github}/pull/655.diff

BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  doctest-devel

%global _description \
sparrow is an implementation of the Apache Arrow Columnar format in C++. It \
provides array structures with idiomatic APIs and convenient conversions from \
and to the C interface.

%description %_description

%package devel
Summary:        %{summary}
Requires:       %{name} = %{version}-%{release}
Provides:       %{name} = %{version}-%{release}
Provides:       %{name}-static = %{version}-%{release}

%description devel %_description

%prep
%autosetup -p1

%build
%cmake -DBUILD_TESTS=ON -DUSE_DATE_POLYFILL=OFF
%cmake_build

%install
%cmake_install

%check
%cmake_build --target test_sparrow_lib
%cmake_build --target run_tests

%files
%doc README.md
%license LICENSE
%{_libdir}/lib%{name}.so.*

%files devel
%{_includedir}/%{name}.hpp
%{_includedir}/%{name}/
%{_datadir}/cmake/%{name}
%{_libdir}/lib%{name}.so

%changelog
%autochangelog
