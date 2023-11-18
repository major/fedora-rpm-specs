%global forgeurl https://github.com/tevador/RandomX

Name:    randomx
Version: 1.2.1
Release: %autorelease
Summary: A proof-of-work algorithm that is optimized for general-purpose CPUs
License: BSD-3-Clause
URL:     %forgeurl

%forgemeta
Source0: %forgesource

# From Debian https://salsa.debian.org/cryptocoin-team/librandomx/-/blob/debian/latest/debian/patches/2001_shared-lib.patch
Patch0: randomx-sharedlib.patch

BuildRequires: gcc
BuildRequires: gcc-c++
BuildRequires: cmake >= 3.5

%description
RandomX is a proof-of-work (PoW) algorithm that is optimized for
general-purpose CPUs. RandomX uses random code execution (hence the name)
together with several memory-hard techniques to minimize the efficiency
advantage of specialized hardware.

%package devel
Requires: %{name}%{?_isa} = %{version}-%{release}
Summary: RandomX development files

%description devel
%{summary}.

%prep
%forgeautosetup -p1

%build
%cmake
%cmake_build

%install
%cmake_install

%files
%license LICENSE
%doc README.md
%{_libdir}/librandomx.so.0
%{_libdir}/librandomx.so.0.0.0

%files devel
%license LICENSE
%doc README.md
%doc doc
%{_includedir}/randomx.h
%{_libdir}/librandomx.so

%changelog
* Wed Nov 15 2023 Jonny Heggheim <hegjon@gmail.com> - 1.2.1-1
- Updated to version 1.2.1

* Mon Apr 25 2022 Jonny Heggheim <hegjon@gmail.com> - 1.1.10-1
- Initial package
