%global toolchain clang
%global reltag 6.0.2-RELEASE

Name:           libdispatch
Version:        6.0.2
Release:        2%{?dist}
Summary:        Apple's Grand Central Dispatch library
License:        Apache-2.0
URL:            https://github.com/apple/swift-corelibs-libdispatch

Source0:        https://github.com/apple/swift-corelibs-libdispatch/archive/swift-%{reltag}.tar.gz#/corelibs-libdispatch.tar.gz


BuildRequires:  clang
BuildRequires:  libbsd-devel
BuildRequires:  ninja-build
BuildRequires:  cmake
BuildRequires:  chrpath

ExclusiveArch:  x86_64 aarch64 ppc64le

Provides:       libblocksruntime = %{version}-%{release}
Obsoletes:      libblocksruntime < 7.0.0-5

Epoch:          1

%description
Grand Central Dispatch (GCD or libdispatch) provides 
comprehensive support for concurrent code execution on 
multicore hardware.

libdispatch is currently available on all Darwin platforms. 
This project aims to make a modern version of libdispatch 
available on all other Swift platforms. To do this, we will 
implement as much of the portable subset of the API as 
possible, using the existing open source C implementation.

libdispatch on Darwin is a combination of logic in the xnu 
kernel alongside the user-space Library. The kernel has the 
most information available to balance workload across the 
entire system. As a first step, however, we believe it is 
useful to bring up the basic functionality of the library 
using user-space pthread primitives on Linux. Eventually, a 
Linux kernel module could be developed to support more 
informed thread scheduling.


%package devel
Summary:    Development files for libdispatch
Requires:   %{name}%{?_isa} =  %{epoch}:%{version}-%{release}


%description devel
Development files for libdispatch


%prep
%setup -q -n swift-corelibs-libdispatch-swift-%{reltag}


%build
export CXX=clang++
export CC=clang
export CFLAGS="-Wno-error=cast-function-type `echo $CFLAGS`"
%cmake -G Ninja 
%cmake_build


%install
%cmake_install
chrpath --delete %{buildroot}%{_libdir}/libdispatch.so


%files
%license LICENSE
%{_libdir}/libBlocksRuntime.so
%{_libdir}/libdispatch.so
%{_mandir}/man3/*


%files devel
%{_includedir}/Block.h
%{_includedir}/dispatch/*
%{_includedir}/os/*


%changelog
* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1:6.0.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Tue Oct 29 2024 Ron Olson <tachoknight@gmail.com> 6.0.2-1
- Updated to 6.0.2-1-RELEASE

* Thu Sep 26 2024 Ron Olson <tachoknight@gmail.com> 6.0.1-1
- Updated to 6.0.1-1-RELEASE

* Tue Sep 17 2024 Ron Olson <tachoknight@gmail.com> 6.0-1
- Updated to 6.0-1-RELEASE

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1:5.10-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Mon Jun 24 2024 Ron Olson <tachoknight@gmail.com> 5.10.1-1
- Updated to 5.10.1-RELEASE

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1:5.9-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1:5.9-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Sep 28 2023 Ron Olson <tachoknight@gmail.com> 5.9-1
- Updated to 5.9-RELEASE

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1:5.7.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Fri Jan 27 2023 Ron Olson <tachoknight@gmail.com> 5.7.3-1
- Updated to 5.7.3-RELEASE
* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1:5.7.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Dec 16 2022 Ron Olson <tachoknight@gmail.com> 5.7.2-1
- Updated to 5.7.2-RELEASE
  SPDX migration
* Mon Dec 05 2022 Ron Olson <tachoknight@gmail.com> 5.7.1-1
- Updated to 5.7.1-RELEASE
* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1:5.6.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu May 12 2022 Ron Olson <tachoknight@gmail.com> 5.6.1-2
- Merged patch 0a56660 from Shawn Anastasio to include
  ppc64le as one of the architectures to build for
* Fri Apr 15 2022 Ron Olson <tachoknight@gmail.com> 5.6.1-1
- Updated to 5.6.1-RELEASE
* Wed Mar 23 2022 Ron Olson <tachoknight@gmail.com> 5.6.0-2
- Added patch to allow for building on EPEL-8
* Tue Mar 22 2022 Ron Olson <tachoknight@gmail.com> 5.6.0-1
- Updated to 5.6.0-RELEASE
* Tue Dec 14 2021 Ron Olson <tachoknight@gmail.com> 5.5.2-1
- Updated to 5.5.2-RELEASE
* Fri Oct 29 2021 Ron Olson <tachoknight@gmail.com> 5.5.1-1
- Updated to 5.5.1-RELEASE
* Tue Jun 01 2021 Ron Olson <tachoknight@gmail.com> 5.4.1-1
- Updated to 5.4.1-RELEASE
* Sat May 01 2021 Ron Olson <tachoknight@gmail.com> 5.4-1
- Updated to 5.4-RELEASE also added explicit CMake step
  for EPEL8
* Wed Feb 03 2021 Ron Olson <tachoknight@gmail.com> 5.3.3-1
- Initial version based on version 5.3.3-RELEASE
