# Installed library version
%global lib_version 2206.0.0

Name:           abseil-cpp
Version:        20220623.1
Release:        3%{?dist}
Summary:        C++ Common Libraries

# The entire source is Apache-2.0, except:
#   - The following files are LicenseRef-Fedora-Public-Domain:
#       absl/time/internal/cctz/src/tzfile.h
#         ** This file is in the public domain, so clarified as of
#         ** 1996-06-05 by Arthur David Olson.
#       absl/time/internal/cctz/testdata/zoneinfo/iso3166.tab
#         # This file is in the public domain, so clarified as of
#         # 2009-05-17 by Arthur David Olson.
#       absl/time/internal/cctz/testdata/zoneinfo/zone1970.tab
#         # This file is in the public domain.
License:        Apache-2.0 AND LicenseRef-Fedora-Public-Domain
URL:            https://abseil.io
Source0:        https://github.com/abseil/abseil-cpp/archive/%{version}/%{name}-%{version}.tar.gz

# Backport upstream commit 09e96049995584c3489e4bd1467313e3e85af99c, which
# corresponds to:
#
# Do not leak -maes -msse4.1 into pkgconfig
# https://github.com/abseil/abseil-cpp/pull/1216
#
# Fixes RHBZ#2108658.
Patch:          https://github.com/abseil/abseil-cpp/commit/09e96049995584c3489e4bd1467313e3e85af99c.patch
# Comment out two static assertions in the tests that fail with GCC 13.
#   Reported upstream:
# Static assertion failures compiling AllocatorTraits.Rebind test (GCC 13)
# https://github.com/abseil/abseil-cpp/issues/1366
Patch:          abseil-cpp-20220623.1-gcc13.patch

BuildRequires:  cmake
# The default make backend would work just as well; ninja is observably faster
BuildRequires:  ninja-build
BuildRequires:  gcc-c++

BuildRequires:  gmock-devel
BuildRequires:  gtest-devel

%ifarch s390x
# Symbolize.SymbolizeWithMultipleMaps fails in absl_symbolize_test on s390x
# with LTO
# https://github.com/abseil/abseil-cpp/issues/1133
%global _lto_cflags %{nil}
%endif

%description
Abseil is an open-source collection of C++ library code designed to augment
the C++ standard library. The Abseil library code is collected from
Google's own C++ code base, has been extensively tested and used in
production, and is the same code we depend on in our daily coding lives.

In some cases, Abseil provides pieces missing from the C++ standard; in
others, Abseil provides alternatives to the standard for special needs we've
found through usage in the Google code base. We denote those cases clearly
within the library code we provide you.

Abseil is not meant to be a competitor to the standard library; we've just
found that many of these utilities serve a purpose within our code base,
and we now want to provide those resources to the C++ community as a whole.

%package devel
Summary: Development files for %{name}
Requires: %{name}%{?_isa} = %{version}-%{release}

%description devel
Development headers for %{name}

%prep
%autosetup -p1 -S gendiff

%build
%cmake \
  -GNinja \
  -DABSL_USE_EXTERNAL_GOOGLETEST:BOOL=ON \
  -DABSL_FIND_GOOGLETEST:BOOL=ON \
  -DABSL_ENABLE_INSTALL:BOOL=ON \
  -DABSL_BUILD_TESTING:BOOL=ON \
  -DCMAKE_BUILD_TYPE:STRING=None \
  -DCMAKE_CXX_STANDARD:STRING=17
%cmake_build


%install
%cmake_install

%check
%ctest

%files
%license LICENSE
%doc FAQ.md README.md UPGRADES.md
%{_libdir}/libabsl_*.so.%{lib_version}

%files devel
%{_includedir}/absl
%{_libdir}/libabsl_*.so
%{_libdir}/cmake/absl
%{_libdir}/pkgconfig/*.pc

%changelog
* Wed Jan 18 2023 Fedora Release Engineering <releng@fedoraproject.org> - 20220623.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Sep 02 2022 Benjamin A. Beasley <code@musicinmybrain.net> - 20220623.1-2
- Update to 20220623.1 (close RHBZ#2123181)

* Sat Aug 13 2022 Benjamin A. Beasley <code@musicinmybrain.net> - 20220623.0-1
- Update to 20220623.0 (close RHBZ#2101021)
- Update License to SPDX

* Fri Jul 29 2022 Benjamin A. Beasley <code@musicinmybrain.net> - 20211102.0-4
- Do not leak -maes -msse4.1 into pkgconfig (fix RHBZ#2108658)

* Wed Jul 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 20211102.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Tue Mar 15 2022 Benjamin A. Beasley <code@musicinmybrain.net> - 20211102.0-2
- Disable LTO on s390x to work around test failure
- Skip SysinfoTest.NominalCPUFrequency on all architectures; it fails
  occasionally on aarch64, and upstream says we should not care

* Fri Feb 18 2022 Benjamin A. Beasley <code@musicinmybrain.net> - 20211102.0-1
- Update to 20211102.0 (close RHBZ#2019691)
- Drop --output-on-failure, already in %%ctest expansion
- On s390x, instead of ignoring all tests, skip only the single failing test
- Use ninja backend for CMake: speeds up build with no downsides
- Drop patch for armv7hl

* Mon Jan 31 2022 Benjamin A. Beasley <code@musicinmybrain.net> - 20210324.2-4
- Fix test failure (fix RHBZ#2045186)

* Wed Jan 19 2022 Fedora Release Engineering <releng@fedoraproject.org> - 20210324.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 20210324.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri May 21 2021 Rich Mattes <richmattes@gmail.com> - 20210324.1-2
- Update to release 20210324.2
- Enable and run test suite

* Mon Mar 08 2021 Rich Mattes <richmattes@gmail.com> - 20200923.3-1
- Update to release 20200923.3

* Mon Jan 25 2021 Fedora Release Engineering <releng@fedoraproject.org> - 20200923.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Sat Dec 19 2020 Rich Mattes <richmattes@gmail.com> - 20200923.2-1
- Update to release 20200923.2
- Rebuild to fix tagging in koji (rhbz#1885561)

* Fri Jul 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 20200225.2-4
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 20200225.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed May 27 2020 Rich Mattes <richmattes@gmail.com> - 20200225.2-2
- Don't remove buildroot in install

* Sun May 24 2020 Rich Mattes <richmattes@gmail.com> - 20200225.2-1
- Initial package.
