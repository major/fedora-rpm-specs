%global debug_package %{nil}

Name: cxxopts
Version: 3.3.1
Release: %autorelease

Summary: Lightweight C++ command line option parser
License: MIT
URL: https://github.com/jarro2783/%{name}
Source0: %{url}/archive/v%{version}/%{name}-%{version}.tar.gz


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
%{_datadir}/cmake/%{name}/
%{_datadir}/pkgconfig/%{name}.pc

%changelog
%autochangelog
