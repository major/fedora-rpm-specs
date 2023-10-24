# Header-only library.
%global debug_package %{nil}

Name:           cppzmq
Version:        4.10.0
Release:        %autorelease
Summary:        Header-only C++ binding for libzmq

License:        MIT
URL:            https://zeromq.org
Source0:        https://github.com/zeromq/%{name}/archive/v%{version}/%{name}-%{version}.tar.gz

BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  pkgconfig(libzmq)
BuildRequires:  (cmake(Catch2) >= 2.13.9 with cmake(Catch2) < 3)

%global _description \
cppzmq is a C++ binding for libzmq. \
\
cppzmq maps the libzmq C API to C++ concepts. In particular, it is type-safe, \
provides exception-based error handling, and provides RAII-style classes that \
automate resource management. cppzmq is a light-weight, header-only binding.

%description %{_description}

%package devel
Summary:        %{summary}
Provides:       %{name}-static = %{version}-%{release}

Requires:       pkgconfig(libzmq)

%description devel %{_description}

%prep
%autosetup -p1

%build
%cmake
%cmake_build

%install
%cmake_install

%check
%ctest

%files devel
%doc README.md
%license LICENSE
%{_includedir}/zmq*.hpp
%{_datadir}/cmake/%{name}
%{_libdir}/pkgconfig/%{name}.pc

%changelog
%autochangelog

