%undefine __cmake_in_source_build
%ifarch %{valgrind_arches}
%global with_valgrind 1
%endif
%global soversion 2

Name:           libccd
Version:        2.1
Release:        15%{?dist}
Summary:        Library for collision detection between convex shapes

# The src/testsuites/cu/ directory contains some GPL-3.0-or-later code, but it
# is not incorporated in the binary RPMs and does not contribute to their
# licenses.
License:        BSD-3-Clause
URL:            http://libccd.danfis.cz
Source0:        https://github.com/danfis/%{name}/archive/v%{version}/%{name}-%{version}.tar.gz
# This patch integrates additional programs that are present in
# the testsuites folder into CMake, via CTest.
# It also increments the version number to match the release.
# Not yet submitted  upstream
Patch0:         %{name}-2.1-ctest.patch
# This patch changes the ccd.pc file to point to the correct include
# directory.  Not yet submitted upstream
Patch1:         %{name}-2.1-pkgconfig.patch
# Convert check_regressions to python3
# Not submitted upstream
Patch2:         %{name}-2.1-py3.patch

BuildRequires: make
BuildRequires:  gcc-c++
BuildRequires:  cmake
# These are required for executing the test suite
BuildRequires:  python3
%if 0%{?with_valgrind}
BuildRequires:  valgrind
%endif

%description
libccd implements variation on Gilbert-Johnson-Keerthi (GJK) algorithm + 
Expand Polytope Algorithm (EPA). It also implements Minkowski Portal 
Refinement (MPR, a.k.a. XenoCollide) algorithm as published in Game 
Programming Gems 7.


%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%prep
%setup -q
%patch -P0 -p0 -b .ctest
%patch -P1 -p0 -b .pkgconfig
%patch -P2 -p0 -b .py3

%build
%cmake \
  -DBUILD_TESTS=ON \
  -DCMAKE_BUILD_TYPE=Release \
  ..
%cmake_build

%install
%cmake_install
find %{buildroot} -name '*.la' -exec rm -f {} ';'
rm -f %{buildroot}%{_libdir}/*.a
rm -rf %{buildroot}%{_docdir}/ccd


%check
%if 0%{?with_valgrind}
make -C build test ||exit 0
%endif


%files
%doc BSD-LICENSE README.md
%{_libdir}/*.so.%{version}
%{_libdir}/*.so.%{soversion}

%files devel
%{_includedir}/*
%{_libdir}/*.so
%{_libdir}/pkgconfig/*.pc
%{_libdir}/ccd

%changelog
* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 2.1-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.1-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Wed Mar 27 2024 Benjamin A. Beasley <code@musicinmybrain.net> - 2.1-13
- Convert License to SPDX

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.1-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.1-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.1-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Tue Jan 31 2023 Milkice Qiu <milkice@milkice.me> - 2.1-9
- Switch to %%{valgrind_arches}
- Patch from David Abdurachmanov <david.abdurachmanov@sifive.com>

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.1-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.1-3
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Sat Apr 18 2020 Rich Mattes <richmattes@gmail.com> - 2.1-1
- Update to release 2.1
- Update test suite to use python 3 (rhbz#1807509)

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.0-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.0-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.0-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.0-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Mar 15 2018 Iryna Shcherbina <ishcherb@redhat.com> - 2.0-12
- Update Python 2 dependency declarations to new packaging standards
  (See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3)

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.0-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.0-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri Aug 12 2016 Michal Toman <mtoman@fedoraproject.org> - 2.0-7
- No valgrind on MIPS

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 2.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Aug 27 2015 Marcin Juszkiewicz <mjuszkiewicz@redhat.com> - 2.0-5
- Valgrind is not available only on s/390 (rhbz#1257526)

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Jun 01 2014 Rich Mattes <rmattes@fedoraproject.org> - 2.0-1
- Update to release 2.0

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Wed Jan 09 2013 Dan Horák <dan[at]danny.cz> - 1.4-2
- build on platforms without valgrind

* Mon Oct 22 2012 Rich Mattes <richmattes@gmail.com> - 1.4-1
- Update to release 1.4

* Tue May 29 2012 Rich Mattes <richmattes@gmail.com> - 1.3-3
- Fixed pkgconfig file to point to correct include dir

* Sat May 26 2012 Rich Mattes <richmattes@gmail.com> - 1.3-2
- Convert test suite to CTest

* Fri May 25 2012 Rich Mattes <richmattes@gmail.com> - 1.3-1
- Update to release 1.3
- Remove upstreamed soname patch

* Sun May 06 2012 Rich Mattes <richmattes@gmail.com> - 1.2-3
- Removed -static subpackage.

* Mon Apr 30 2012 Rich Mattes <richmattes@gmail.com> - 1.2-2
- Update soname patch to match upstream implementation 

* Fri Apr 27 2012 Rich Mattes <richmattes@gmail.com> - 1.2-1
- Initial package
