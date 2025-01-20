# There are no ELF objects in this package, so turn off debuginfo generation.
%global debug_package %{nil}

Name:           permlib
Version:        0.2.9
Release:        23%{?dist}
Summary:        Library for permutation computations

License:        BSD-3-Clause
URL:            https://github.com/tremlin/PermLib
VCS:            git:%{url}.git
Source0:        %{url}/archive/v%{version}/%{name}-%{version}.tar.gz
# Doxygen config file written by Jerry James <loganjerry@gmail.com>
Source1:        %{name}-Doxyfile
# Fix gcc 6 build failure
Patch:          %{name}-0.2.8-gcc6.patch
# Adapt to changes in recent versions of boost
Patch:          %{name}-0.2.9-boost.patch

# See https://fedoraproject.org/wiki/Changes/EncourageI686LeafRemoval
ExcludeArch:    %{ix86}

BuildRequires:  boost-devel
BuildRequires:  cmake
BuildRequires:  dvipng
BuildRequires:  doxygen-latex
BuildRequires:  gcc-c++
BuildRequires:  ghostscript
BuildRequires:  gmp-devel
BuildRequires:  make
BuildRequires:  tex(newunicodechar.sty)

%description
PermLib is a callable C++ library for permutation computations.
Currently it supports set stabilizer and in-orbit computations, based on
bases and strong generating sets (BSGS).  Additionally, it computes
automorphisms of symmetric matrices and finds the lexicographically
smallest set in an orbit of sets.

%package devel
# The code is BSD-3-Clause.  Other licenses are due to files added by doxygen.
# GPL-1.0-or-later: html/*.{css,png,svg}
# MIT: html/*.js
License:        BSD-3-Clause AND GPL-1.0-or-later AND MIT
Summary:        Header files for developing programs that use PermLib
BuildArch:      noarch
Requires:       boost-devel
Provides:       %{name}-static = %{version}-%{release}
Provides:       bundled(js-jquery)

%description devel
PermLib is a callable C++ library for permutation computations.
Currently it supports set stabilizer and in-orbit computations, based on
bases and strong generating sets (BSGS).  Additionally, it computes
automorphisms of symmetric matrices and finds the lexicographically
smallest set in an orbit of sets.

This package contains header files for developing programs that use
PermLib.

%prep
%autosetup -p0 -n PermLib-%{version}
sed "s/@VERSION@/%{version}/" %{SOURCE1} > Doxyfile

%build
%cmake
%cmake_build

# Build the documentation
mkdir doc
doxygen
rm -f doc/html/installdox

%install
# No install target is generated in the makefile, and
# DESTDIR=$RPM_BUILD_ROOT cmake -P cmake_install.cmake
# does nothing, so we do it by hand.

# Install the header files
mkdir -p $RPM_BUILD_ROOT%{_includedir}
cp -a include/%{name} $RPM_BUILD_ROOT%{_includedir}

%check
%ctest

%files devel
%doc AUTHORS CHANGELOG doc/html
%license LICENSE
%{_includedir}/permlib

%changelog
* Sat Jan 18 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.9-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.9-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.9-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.9-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Tue Jan 16 2024 Jerry James <loganjerry@gmail.com> - 0.2.9-19
- Stop building for 32-bit x86

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.9-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Fri Jul 14 2023 Jerry James <loganjerry@gmail.com> - 0.2.9-18
- Comply with header-only packaging guidelines

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.9-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Mon Dec 12 2022 Jerry James <loganjerry@gmail.com> - 0.2.9-17
- Convert License tag to SPDX
- Provide permlib-static

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.9-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.9-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.9-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.9-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.9-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.9-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.9-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Wed Feb  6 2019 Jerry James <loganjerry@gmail.com> - 0.2.9-10
- Add -boost patch

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.9-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.9-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.2.9-8
- Escape macros in %%changelog

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.9-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.9-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Wed Jul 19 2017 Jonathan Wakely <jwakely@redhat.com> - 0.2.9-5
- Rebuilt for s390x binutils bug

* Tue Jul 04 2017 Jonathan Wakely <jwakely@redhat.com> - 0.2.9-4
- Rebuilt for Boost 1.64

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.9-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri Jan 27 2017 Jonathan Wakely <jwakely@redhat.com> - 0.2.9-2
- Rebuilt for Boost 1.63
- Make build reproducible by removing %%{?_isa} on Requires.

* Wed Jul 20 2016 Jerry James <loganjerry@gmail.com> - 0.2.9-1
- New upstream release
- Update Doxyfile
- Drop upstreamed boost patch

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.8-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Aug 27 2015 Jonathan Wakely <jwakely@redhat.com> - 0.2.8-14
- Rebuilt for Boost 1.59

* Wed Jul 29 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2.8-13
- Rebuilt for https://fedoraproject.org/wiki/Changes/F23Boost159

* Wed Jul 22 2015 David Tardon <dtardon@redhat.com> - 0.2.8-12
- rebuild for Boost 1.58

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2.8-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Feb 21 2015 Jerry James <loganjerry@gmail.com> - 0.2.8-10
- Update URLs
- Note bundled jquery
- Use license macro

* Tue Jan 27 2015 Petr Machata <pmachata@redhat.com> - 0.2.8-9
- Rebuild for boost 1.57.0

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2.8-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Fri May 23 2014 Petr Machata <pmachata@redhat.com> - 0.2.8-7
- Rebuild for boost 1.55.0

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2.8-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Tue Jul 30 2013 Petr Machata <pmachata@redhat.com> - 0.2.8-5
- Rebuild for boost 1.54.0
- Remove -mt suffix from boost_unit_testing_framework DSO
  (permlib-0.2.8-boost_mt.patch)

* Sun Feb 10 2013 Denis Arnaud <denis.arnaud_fedora@m4x.org> - 0.2.8-4
- Rebuild for Boost-1.53.0

* Sat Feb 09 2013 Denis Arnaud <denis.arnaud_fedora@m4x.org> - 0.2.8-3
- Rebuild for Boost-1.53.0

* Fri Feb  8 2013 Jerry James <loganjerry@gmail.com> - 0.2.8-2
- Adjust BRs for TeXLive 2012

* Thu Sep 27 2012 Jerry James <loganjerry@gmail.com> - 0.2.8-1
- New upstream release
- Drop upstreamed patch

* Wed Sep 26 2012 Jerry James <loganjerry@gmail.com> - 0.2.7-1
- New upstream release
- Update Doxyfile
- Add -test patch to fix two test failures

* Mon Aug  6 2012 Jerry James <loganjerry@gmail.com> - 0.2.6-4
- Rebuild for boost 1.50
- Update Doxyfile

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2.6-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri May  4 2012 Jerry James <loganjerry@gmail.com> - 0.2.6-2
- BR gmp-devel
- Add comment on origin of Doxyfile

* Fri Mar 16 2012 Jerry James <loganjerry@gmail.com> - 0.2.6-1
- Initial RPM
