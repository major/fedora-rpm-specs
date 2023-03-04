%global _description %{expand:
This library provides a header only cross-platform mDNS and DNS-DS library
in C.

The library does DNS-SD discovery and service as well as one-shot single
record mDNS query and response. There are no memory allocations done by
the library, all buffers used must be passed in by the caller.

Custom data for use in processing can be passed along using a user data
opaque pointer.}

Name: mdns
Version: 1.4.2
Release: 2%{?dist}

License: LicenseRef-Fedora-Public-Domain
Summary: Cross-platform mDNS/DNS-SD library in C
URL: https://github.com/mjansson/%{name}
Source0: %{url}/archive/%{version}/%{name}-%{version}.tar.gz
BuildArch: noarch

Patch100: %{name}-upstream-fixes.patch
Patch101: %{name}-cmake-installation-fix.patch

BuildRequires: cmake
BuildRequires: gcc-c++
BuildRequires: ninja-build

%description %{_description}

%package devel
Summary: Header-only mDNS/DNS-SD library in C
Provides: %{name}-static = %{?epoch:%{epoch}:}%{version}-%{release}

%description devel %{_description}

%prep
%autosetup -p1

%build
%cmake -G Ninja \
    -DCMAKE_BUILD_TYPE=Release \
    -DMDNS_BUILD_EXAMPLE:BOOL=OFF
%cmake_build

%install
%cmake_install

%files devel
%doc CHANGELOG README.md
%license LICENSE
%{_datadir}/cmake/%{name}/
%{_includedir}/%{name}.h

%changelog
* Thu Mar 02 2023 Vitaly Zaitsev <vitaly@easycoding.org> - 1.4.2-2
- Explicitly marked generated CMake configs as architecture independent.

* Thu Mar 02 2023 Vitaly Zaitsev <vitaly@easycoding.org> - 1.4.2-1
- Initial SPEC release.
