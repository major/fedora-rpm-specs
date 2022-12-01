Name:           simdjson
Version:        3.0.1
Release:        %autorelease
Summary:        Parsing gigabytes of JSON per second

License:        Apache-2.0 AND MIT
URL:			https://simdjson.org/
Source0:		https://github.com/simdjson/simdjson/archive/v%{version}/%{name}-%{version}.tar.gz

BuildRequires:  cmake
BuildRequires:  cxxopts-devel
BuildRequires:  gcc-c++
BuildRequires:  make

%description
JSON is everywhere on the Internet. Servers spend a *lot* of time parsing it.
We need a fresh approach. The simdjson library uses commonly available 
SIMD instructions and microparallel algorithms to parse JSON 4x faster than
RapidJSON and 25x faster than JSON for Modern C++.

%package devel
Summary: Development files for %{name}

%description devel
The package contains libraries and header files for developing applications
that use %{name}.

%package doc
Summary: Documents for %{name}

%description doc 
%{summary}

%prep
%autosetup -n %{name}-%{version}

%build
%cmake
%cmake_build

%install
%cmake_install

%check
%ctest

%files
%license LICENSE
%doc CONTRIBUTING.md README.md RELEASES.md
%{_libdir}/lib%{name}*.so.*

%files devel
%license LICENSE
%{_includedir}/%{name}.h
%{_libdir}/cmake/%{name}
%{_libdir}/lib%{name}*.so
%{_libdir}/pkgconfig/*.pc

%files doc
%license LICENSE
%doc doc

%changelog
%autochangelog
