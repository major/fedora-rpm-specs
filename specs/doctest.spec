%global debug_package %{nil}

Name: doctest
Version: 2.5.1
Release: %autorelease
Summary: Feature-rich header-only C++ testing framework
# logo is CC-BY-4.0
# doctest/doctest.h and doctest/parts/doctest_fwd.h include BSL-1.0
# scripts/*.cmake are BSD-3-Clause
# doc/html_generated is GPL-3.0-only but it is not included in binary rpm
License: MIT AND CC-BY-4.0 AND BSL-1.0 AND BSD-3-Clause
URL: https://github.com/doctest/%{name}
Source0: %{url}/archive/refs/tags/v%{version}.tar.gz

BuildRequires: gcc-c++
BuildRequires: cmake
BuildRequires: git

%description
A fast (both in compile times and runtime) C++ testing framework, with the
ability to write tests directly along production source (or in their own
source, if you prefer).

%package devel
Summary: Development files for %{name}
Provides: %{name}-static = %{?epoch:%{epoch}:}%{version}-%{release}
Provides: %{name}%{?_isa} = %{?epoch:%{epoch}:}%{version}-%{release}
Requires: libstdc++-devel%{?_isa}

%description devel
%{summary}.

%prep
%autosetup -p1

%build
%cmake \
  -DCMAKE_BUILD_TYPE=Release \
  -DDOCTEST_WITH_TESTS:BOOL=ON \
  %{nil}
%cmake_build

%check
%ctest

%install
%cmake_install

%files devel
%doc README.md CHANGELOG.md CONTRIBUTING.md
%license LICENSE.txt
%{_includedir}/%{name}/
%{_libdir}/cmake/%{name}/
%{_libdir}/pkgconfig/%{name}.pc

%changelog
%autochangelog
