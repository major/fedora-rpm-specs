%define __cmake_in_source_build 1
%global rocm_release 5.6
%global rocm_patch 0
%global rocm_version %{rocm_release}.%{rocm_patch}
Name:           hsakmt
Version:        1.0.6
Release:        31.rocm%{rocm_version}%{?dist}
Summary:        AMD HSA thunk library

License:        MIT
URL:            https://github.com/RadeonOpenCompute/ROCT-Thunk-Interface
Source0:        https://github.com/RadeonOpenCompute/ROCT-Thunk-Interface/archive/rocm-%{rocm_version}.tar.gz#/%{name}-rocm-%{rocm_version}.tar.gz

Patch0:         0001-Don-t-install-asan-license-if-disabled.patch

# Fedora builds AMD HSA kernel support for these 64bit targets:
ExclusiveArch: x86_64 aarch64 ppc64le
BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires: cmake
BuildRequires: pciutils-devel
BuildRequires: libdrm-devel
BuildRequires: numactl-devel

%if 0%{?epel} == 7
# We still the original cmake package on epel, because it provides the
# %%cmake macro.
BuildRequires: cmake3
%global __cmake %{_bindir}/cmake3
%endif

%description
This package includes the libhsakmt (HSA thunk) libraries for AMD KFD


%package devel
Summary: AMD HSA thunk library development package
Requires: %{name}%{?_isa} = %{version}-%{release}
Provides: hsakmt(rocm) = %{rocm_release}

%description devel
Development library for the libhsakmt (HSA thunk) libraries for AMD KFD

%prep
%autosetup -n  ROCT-Thunk-Interface-rocm-%{rocm_version} -p1

%build
mkdir build
cd build

%cmake .. -DCMAKE_BUILD_TYPE=RelWithDebInfo
%cmake_build

%install
cd build
%cmake_install

# We install this via license macro instead:
rm %{buildroot}%{_docdir}/hsakmt/LICENSE.md

%ldconfig_scriptlets

%files
%doc README.md
%license LICENSE.md
%{_libdir}/libhsakmt.so.%{version}
%{_libdir}/libhsakmt.so.1

%files devel
%{_libdir}/libhsakmt.so
%{_includedir}/hsakmt
%{_libdir}/cmake/hsakmt/
%{_datadir}/pkgconfig/libhsakmt.pc
#These headers are deprecated and will be removed soon:
%{_includedir}/hsakmt.h
%{_includedir}/hsakmttypes.h

%changelog
* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.6-31.rocm5.6.0
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jun 29 2023 Jeremy Newton <alexjnewt at hotmail dot com> - 1.0.6-30.rocm5.6.0
- Update to 5.6

* Mon May 01 2023 Jeremy Newton <alexjnewt at hotmail dot com> - 1.0.6-29.rocm5.5.0
- Update to 5.5

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.6-28.rocm5.4.1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Sun Dec 18 2022 Jeremy Newton <alexjnewt at hotmail dot com> - 1.0.6-27.rocm5.4.1
- Update to 5.4.1

* Mon Oct 03 2022 Jeremy Newton <alexjnewt at hotmail dot com> - 1.0.6-26.rocm5.3.0
- Update to 5.3.0

* Sun Jul 24 2022 Jeremy Newton <alexjnewt at hotmail dot com> - 1.0.6-25.rocm5.2.1
- Update to 5.2.1

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.6-24.rocm5.2.0
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Sun Jul 03 2022 Jeremy Newton <alexjnewt at hotmail dot com> - 1.0.6-23.rocm5.2.0
- Update to 5.2.0

* Sat Apr 09 2022 Jeremy Newton <alexjnewt at hotmail dot com> - 1.0.6-22.rocm5.1.1
- Update to ROCm version 5.1.1

* Tue Apr 05 2022 Jeremy Newton <alexjnewt at hotmail dot com> - 1.0.6-21.rocm5.1.0
- Enable ppc64le

* Thu Mar 31 2022 Jeremy Newton <alexjnewt at hotmail dot com> - 1.0.6-20.rocm5.1.0
- Update to ROCm version 5.1.0

* Fri Feb 11 2022 Jeremy Newton <alexjnewt at hotmail dot com> - 1.0.6-19.rocm5.0.0
- Update to ROCm version 5.0.0
- General improvements to spec file

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.6-18.rocm3.9.0
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.6-17.rocm3.9.0
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.6-16.rocm3.9.0
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Nov 23 2020 Philipp Knechtges <philipp-dev@knechtges.com> - 1.0.6-15.rocm3.9.0
- Update to ROCm version 3.9.0

* Wed Sep 23 2020 Jeff Law <law@redhat.com> - 1.0.6-14.rocm3.5.0
- Use cmake_in_source_build to fix FTBFS due to recent cmake macro changes

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.6-13.rocm3.5.0
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.6-12.rocm3.5.0
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Jul 16 2020 Tom Stellard <tstellar@redhat.com> - 1.0.6-11.rocm3.5.0
- ROCm 3.5.0 Release

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.6-10.rocm2.0.0
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.6-9.rocm2.0.0
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.6-8.rocm2.0.0
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Tue Jan 15 2019 Tom Stellard <tstellar@redhat.com> - 1.0.6-7.rocm2.0.0
- ROCm 2.0.0 Release

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.6-6.20171026git172d101
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 23 2018 Tom Stellard <tstellar@redhat.com> - 1.0.6-5.20171026git172d101
- Fix build for epel7

* Mon Feb 12 2018 Tom Stellard <tstellar@redhat.com> - 1.0.6-4.20171026git172d101
- Fix build flag injection
- rhbz#1543787

* Fri Feb 09 2018 Tom Stellard <tstellar@redhat.com> - 1.0.6-3.20171026git172d101
- Build for aarch64

* Mon Feb 05 2018 Tom Stellard <tstellar@redhat.com> - 1.0.6-2.20171026git172d101
- Fix build with gcc 8

* Thu Oct 26 2017 Tom Stellard <tstellar@redhat.com> - 1.0.6-1.20171026git172d101
- Update with latest code from https://github.com/RadeonOpenCompute/ROCT-Thunk-Interface

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Nov 13 2015 Oded Gabbay <oded.gabbay@gmail.com> 1.0.0-5
- Don't build for arm and i686

* Fri Nov 13 2015 Oded Gabbay <oded.gabbay@gmail.com> 1.0.0-4
- Rename package back to hsakmt

* Sun Nov 1 2015 Oded Gabbay <oded.gabbay@gmail.com> 1.0.0-3
- Rename package to libhsakmt

* Thu Oct 29 2015 Oded Gabbay <oded.gabbay@gmail.com> 1.0.0-2
- Changed doc to license
- Added GPLv2 to license
- Changed RPM_BUILD_ROOT to {buildroot}

* Sat Oct 24 2015 Oded Gabbay <oded.gabbay@gmail.com> 1.0.0-1
- Initial release of hsakmt, ver. 1.0.0

