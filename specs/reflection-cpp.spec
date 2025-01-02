# header-only library
%global debug_package %{nil}

Name:           reflection-cpp
Version:        0.1.0
Release:        %autorelease
Summary:        C++ static reflection support library
License:        Apache-2.0
URL:            https://github.com/contour-terminal/reflection-cpp
Source0:        %{url}/archive/v%{version}/%{name}-%{version}.tar.gz

BuildRequires:  gcc-c++
BuildRequires:  cmake

%description
C++ static reflection support library.

%package        devel
Summary:        Development files for %{name}
Provides:       %{name}-static = %{version}-%{release}

%description    devel
%{description}.

%prep
%autosetup -p1

%build
%cmake
%cmake_build

%install
%cmake_install

%files devel
%license LICENSE.txt
%doc README.md
%dir %{_includedir}/reflection-cpp
%{_includedir}/reflection-cpp/reflection.hpp
%{_libdir}/cmake/reflection-cpp

%changelog
%autochangelog
