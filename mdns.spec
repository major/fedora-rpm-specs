%global _description %{expand:
This library provides a header only cross-platform mDNS and DNS-DS library
in C.

The library does DNS-SD discovery and service as well as one-shot single
record mDNS query and response. There are no memory allocations done by
the library, all buffers used must be passed in by the caller.

Custom data for use in processing can be passed along using a user data
opaque pointer.}

%global debug_package %{nil}

Name: mdns
Version: 1.4.3
Release: %autorelease

License: LicenseRef-Fedora-Public-Domain
Summary: Cross-platform mDNS/DNS-SD library in C
URL: https://github.com/mjansson/mdns
Source0: %{url}/archive/%{version}/%{name}-%{version}.tar.gz

# Patch1:

BuildRequires: cmake
BuildRequires: gcc-c++
BuildRequires: ninja-build

%description %{_description}

%package devel
Summary: Header-only mDNS/DNS-SD library in C
Provides: %{name}-static = %{?epoch:%{epoch}:}%{version}-%{release}
BuildArch: noarch

%description devel %{_description}

%prep
%autosetup -p1

%build
%cmake -G Ninja
%cmake_build

%install
%cmake_install

%check
%{__cmake_builddir}/bin/mdns_example

%files devel
%doc CHANGELOG README.md
%license LICENSE
%{_datadir}/cmake/%{name}/
%{_includedir}/%{name}.h

%changelog
%autochangelog
