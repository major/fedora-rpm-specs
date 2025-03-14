%global debug_package %{nil}

Name: cxxopts
Version: 3.2.1
Release: %autorelease

Summary: Lightweight C++ command line option parser
License: MIT
URL: https://github.com/jarro2783/%{name}
Source0: %{url}/archive/v%{version}/%{name}-%{version}.tar.gz

# https://github.com/jarro2783/cxxopts/commit/63d1b65a694cfceafc20863afa75df49dfbe6b2a
Patch100: %{name}-3.2.1-add-missing-include.patch
# https://github.com/jarro2783/cxxopts/pull/451
Patch101: %{name}-3.2.1-cmake4-compatibility.patch

BuildRequires: cmake
BuildRequires: gcc-c++
BuildRequires: ninja-build

%description
CXXOpts is a lightweight C++ option parser library, supporting the standard
GNU style syntax for options.

%package devel
Summary: Development files for %{name}
Provides: %{name}-static%{?_isa} = %{?epoch:%{epoch}:}%{version}-%{release}
Provides: %{name}-static = %{?epoch:%{epoch}:}%{version}-%{release}
Provides: %{name}%{?_isa} = %{?epoch:%{epoch}:}%{version}-%{release}
Provides: %{name} = %{?epoch:%{epoch}:}%{version}-%{release}
Requires: libstdc++-devel%{?_isa}

%description devel
%{summary}.

%prep
%autosetup -p1

%build
%cmake -G Ninja \
    -DCMAKE_BUILD_TYPE=Release \
    -DCXXOPTS_ENABLE_INSTALL:BOOL=ON \
    -DCXXOPTS_ENABLE_WARNINGS:BOOL=OFF \
    -DCXXOPTS_BUILD_EXAMPLES:BOOL=ON \
    -DCXXOPTS_BUILD_TESTS:BOOL=ON
%cmake_build

%check
%ctest

%install
%cmake_install

%files devel
%doc README.md
%license LICENSE
%{_includedir}/%{name}.hpp
%{_libdir}/cmake/%{name}/
%{_libdir}/pkgconfig/%{name}.pc

%changelog
%autochangelog
