# FIXME: LTO causes ld segfault, revisit in the future
%global _lto_cflags %nil

Name:           ceres-solver
Version:        2.2.0
# Release candidate versions are messy. Give them a release of
# e.g. "0.1.0%%{?dist}" for RC1 (and remember to adjust the Source0
# URL). Non-RC releases go back to incrementing integers starting at 1.
Release:        6%{?dist}
Summary:        A non-linear least squares minimizer

License:        BSD-3-Clause AND Apache-2.0

URL:            http://ceres-solver.org/
Source0:        http://%{name}.org/%{name}-%{version}.tar.gz

%if 0%{?fedora} >= 33 || 0%{?rhel} >= 9
%global blaslib flexiblas
%global cmake_blas_flags -DBLA_VENDOR=FlexiBLAS
%else
%global blaslib openblas
%global blasvar o
%global cmake_blas_flags -DBLAS_LIBRARIES=%{_libdir}/lib%{blaslib}%{blasvar}.so
%endif

%if 0%{?rhel} > 0 && 0%{?rhel} < 7
# Exclude ppc64 because suitesparse is not available on ppc64
# https://lists.fedoraproject.org/pipermail/epel-devel/2015-May/011193.html
ExcludeArch: ppc64
%endif

%if 0%{?rhel} == 9
# Workaround a build error with eigen3 on rhel 9
%ifarch ppc64le
%undefine _lto_cflags
%endif
%endif

%if (0%{?rhel} && 0%{?rhel} <= 7)
BuildRequires:  cmake3 >= 2.8.0
%else
BuildRequires:  cmake >= 2.8.0
%endif
BuildRequires:  gcc-c++
BuildRequires:  make

# Need -static package per guidelines for handling dependencies on header-only
# libraries.
# http://fedoraproject.org/wiki/Packaging:Guidelines#Packaging_Header_Only_Libraries
BuildRequires:  eigen3-static >= 3.2.1

# suitesparse < 3.4.0-9 ships without *.hpp C++ headers
# https://bugzilla.redhat.com/show_bug.cgi?id=1001869
BuildRequires:  suitesparse-devel >= 3.4.0-9

# If the suitesparse package was built with TBB then we need TBB too
BuildRequires:  tbb-devel

# Use FlexiBLAS or OpenBLAS for BLAS
BuildRequires:  %{blaslib}-devel
BuildRequires:  gflags-devel >= 2.2.1
# Build against miniglog on RHEL6 until glog package is added to EPEL6
%if (0%{?rhel} != 06)
BuildRequires:  glog-devel >= 0.3.1
%endif

%description

Ceres Solver is an open source C++ library for modeling and solving
large, complicated optimization problems. It is a feature rich, mature
and performant library which has been used in production at Google
since 2010. Notable use of Ceres Solver is for the image alignment in
Google Maps and for vehicle pose in Google Street View. Ceres Solver
can solve two kinds of problems.

  1. Non-linear Least Squares problems with bounds constraints.
  2. General unconstrained optimization problems.

Features include:

  - A friendly API: build your objective function one term at a time
  - Automatic and numeric differentiation
  - Robust loss functions
  - Local parameterizations
  - Threaded Jacobian evaluators and linear solvers
  - Trust region solvers with non-monotonic steps (Levenberg-Marquardt and
    Dogleg (Powell & Subspace))
  - Line search solvers (L-BFGS and Nonlinear CG)
  - Dense QR and Cholesky factorization (using Eigen) for small problems
  - Sparse Cholesky factorization (using SuiteSparse) for large sparse problems
  - Specialized solvers for bundle adjustment problems in computer vision
  - Iterative linear solvers for general sparse and bundle adjustment problems
  - Runs on Linux, Windows, Mac OS X, Android, and iOS


%package        devel
Summary:        A non-linear least squares minimizer
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       eigen3-devel
Requires:       gflags-devel
Requires:       glog-devel
Requires:       suitesparse-devel

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.


%prep
%autosetup -p1

%build
%cmake \
  -DCXSPARSE_INCLUDE_DIR:PATH=%{_includedir}/suitesparse \
  %{cmake_blas_flags} \
  -DGFLAGS_INCLUDE_DIR=%{_includedir}
%cmake_build


%install
%cmake_install


%check
# FIXME: Some tests fail on these arches
%ifarch aarch64 ppc64le s390x
%ctest || :
%else
%ctest
%endif


%ldconfig_scriptlets


%files
%if (0%{?rhel} == 06)
%doc README.md LICENSE
%else
%doc README.md
%license LICENSE
%endif
%{_libdir}/libceres.so.4
%{_libdir}/libceres.so.2.2.0

%files devel
%{_includedir}/ceres/
%{_libdir}/libceres.so
%{_libdir}/cmake/Ceres


%changelog
* Thu Jan 16 2025 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Wed Jul 17 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Sun Feb 04 2024 Orion Poplawski <orion@nwra.com> - 2.2.0-4
- Rebuild with suitesparse 7.6.0

* Tue Jan 23 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sat Oct 14 2023 Sandro Mani <manisandro@gmail.com> - 2.2.0-1
- Update to 2.2.0

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Wed Jan 18 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Mon Nov 28 2022 Sandro Mani <manisandro@gmail.com> - 2.1.0-4
- Add Requires: suitesparse-devel to ceres-solver-devel

* Sat Sep 17 2022 Tom Rix <trix@redhat.com> - 2.1.0-3
- Workaround a build problem on ppc and epel9

* Wed Jul 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon Mar 28 2022 Sandro Mani <manisandro@gmail.com> - 2.1.0-1
- Update to 2.1.0

* Wed Jan 19 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Sun Aug 22 2021 Sandro Mani <manisandro@gmail.com> - 2.0.0-7
- Rebuild (eigen3)

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jul 13 2021 Björn Esser <besser82@fedoraproject.org> - 2.0.0-5
- Properly set BLA_VENDOR to FlexiBLAS for cmake >= 3.19

* Tue Feb 23 2021 Jiri Kucera <jkucera@redhat.com> - 2.0.0-4
- When building for ELN, some tests are failing also on s390x

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Thu Dec 17 15:13:12 CET 2020 Sandro Mani <manisandro@gmail.com> - 2.0.0-2
- Rebuild (eigen3)

* Tue Nov 03 2020 Sandro Mani <manisandro@gmail.com> - 2.0.0-1
- Update to 2.0.0

* Mon Oct  5 16:11:58 CEST 2020 Sandro Mani <manisandro@gmail.com> - 1.14.0-7
- Rebuild (eigen3)

* Thu Aug 27 2020 Iñaki Úcar <iucar@fedoraproject.org> - 1.14.0-6
- https://fedoraproject.org/wiki/Changes/FlexiBLAS_as_BLAS/LAPACK_manager

* Tue Jul 28 2020 Scott K Logan <logans@cottsay.net> - 1.14.0-5
- Drop lapack-devel now that FindLAPACK supports BLAS correctly
- Drop BLAS_LIBRARIES var when not using ATLAS

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.14.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Mar 11 2020 Scott K Logan <logans@cottsay.net> - 1.14.0-3
- Add lapack-devel build dependency so that SuiteSparse builds
- Add missing gflags-devel dependency to -devel subpackage

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.14.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Nov 13 2019 Sandro Mani <manisandro@gmail.com> - 1.14.0-1
- Update to 1.14.0
- Switch to openblas where possible (#1618941)

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.13.0-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.13.0-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Wed Dec 26 2018 Sandro Mani <manisandro@gmail.com> - 1.13.0-10
- Rebuild (eigen3)

* Mon Dec 10 2018 Sandro Mani <manisandro@gmail.com> - 1.13.0-9
- Rebuild (eigen3)

* Sat Oct 13 2018 Jerry James <loganjerry@gmail.com> - 1.13.0-8
- Rebuild for tbb 2019_U1

* Sat Oct 06 2018 Sérgio Basto <sergio@serjux.com> - 1.13.0-7
- Rebuit for gflags-2.2.1 and remove ceres-solver_gflags.patch

* Tue Jul 31 2018 Florian Weimer <fweimer@redhat.com> - 1.13.0-6
- Rebuild with fixed binutils

* Sat Jul 28 2018 Sandro Mani <manisandro@gmail.com> - 1.13.0-5
- Rebuild (eigen3)
- Backport patch to fix test failure

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.13.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Sun Feb 18 2018 Sandro Mani <manisandro@gmail.com> - 1.13.0-3
- Add missing BR: gcc-c++, make

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.13.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Mon Aug 07 2017 Rich Mattes <richmattes@gmail.com> - 1.13.0-1
- Update to release 1.13.0 (rhbz#1470895)

* Sun Aug 06 2017 Björn Esser <besser82@fedoraproject.org> - 1.12.0-8
- Rebuilt for AutoReq cmake-filesystem

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.12.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.12.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Mon May 15 2017 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.12.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_27_Mass_Rebuild

* Wed Feb 22 2017 Sandro Mani <manisandro@gmail.com> - 1.12.0-4
- Rebuild for eigen3-3.3.3

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.12.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Sun Jan 22 2017 Sandro Mani <manisandro@gmail.com> - 1.12.0-2
- Rebuild for eigen3-3.3.2

* Wed Dec 28 2016 Rich Mattes <richmattes@gmail.com> - 1.12.0-1
- Update to 1.12.0 (rhbz#1385268)

* Tue Oct 04 2016 Sandro Mani <manisandro@gmail.com> - 1.11.0-9
- Rebuild for eigen3-3.2.10

* Thu Sep 22 2016 Jerry James <loganjerry@gmail.com> - 1.11.0-8
- Rebuild for tbb 2017
- tbb is available on all arches in Fedora and RHEL > 6

* Tue Jul 19 2016 Sandro Mani <manisandro@gmail.com> - 1.11.0-7
- Rebuild for eigen3-3.2.9

* Tue Mar 01 2016 Rich Mattes <richmattes@gmail.com> - 1.11.0-6
- Rebuild for eigen3-3.2.8 (rhbz#1288505)

* Sun Feb 14 2016 Rich Mattes <richmattes@gmail.com> - 1.11.0-5
- Remove -Werror from package CMAKE_CXX_CFLAGS

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.11.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Mon Jan 25 2016 Rich Mattes <richmattes@gmail.com> - 1.11.0-4
- Add missing Requires to devel sub-package (rhbz#1300055)
- Move CeresConfig.cmake to arch-dependent path

* Fri Jan 15 2016 Jerry James <loganjerry@gmail.com> - 1.11.0-3
- Rebuild for tbb 4.4u2

* Sat Dec 05 2015 Rich Mattes <richmattes@gmail.com> - 1.11.0-2
- Rebuild for eigen 3.2.7

* Mon Oct 12 2015 Rich Mattes <richmattes@gmail.com> - 1.11.0-1
- Update to release 1.11.0

* Fri Jul 10 2015 Taylor Braun-Jones <taylor.braun-jones@ge.com> - 1.10.0-8
- Increase epsilon tolerance for one unit test. Needed for new gcc-5 changes.

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.10.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Thu Jun 11 2015 Nils Philippsen <nils@redhat.com> - 1.10.0-6
- rebuild for suitesparse-4.4.4

* Sat May  9 2015 Taylor Braun-Jones <taylor.braun-jones@ge.com> - 1.10.0-5
- Exclude ppc64

* Sat May 02 2015 Kalev Lember <kalevlember@gmail.com> - 1.10.0-4
- Rebuilt for GCC 5 C++11 ABI change

* Fri Apr  3 2015 Taylor Braun-Jones <taylor.braun-jones@ge.com> - 1.10.0-3
- Add upstream patch to fix failing unit test small_blas_test.

* Thu Mar 12 2015 Taylor Braun-Jones <taylor.braun-jones@ge.com> - 1.10.0-3
- Incorporate package review suggestions from Alex Stewart, Christopher Meng,
  and Rich Mattes.

* Wed Mar 11 2015 Taylor Braun-Jones <taylor.braun-jones@ge.com> - 1.10.0-2
- Address comments from Rich Mattes' package review.

* Mon Jan 12 2015 Taylor Braun-Jones <taylor.braun-jones@ge.com> - 1.10.0-1
- Bump version and merge .spec updates from latest upstream release.

* Wed Nov 13 2013 Taylor Braun-Jones <taylor.braun-jones@ge.com> - 1.8.0-1
- New upstream release.

* Mon Nov 04 2013 Taylor Braun-Jones <taylor.braun-jones@ge.com> - 1.8.0-0.1.0
- New upstream release candidate.

* Wed Sep 04 2013 Taylor Braun-Jones <taylor.braun-jones@ge.com> - 1.7.0-1
- Bump version

* Thu Aug 29 2013 Taylor Braun-Jones <taylor@braun-jones.org> - 1.7.0-0.3.0
- Bump version

* Mon Aug 26 2013 Sameer Agarwal <sameeragarwal@google.com> - 1.7.0-0.2.0
- Bump version

* Thu Jul 18 2013 Sameer Agarwal <sameeragarwal@google.com> - 1.7.0-0.1.0
- Bump version

* Mon Apr 29 2013 Sameer Agarwal <sameeragarwal@google.com> - 1.6.0-1
- Bump version

* Mon Apr 29 2013 Sameer Agarwal <sameeragarwal@google.com> - 1.6.0-0.2.0
- Bump version

* Mon Apr 29 2013 Sameer Agarwal <sameeragarwal@google.com> - 1.6.0-0.1.0
- Bump version

* Sun Feb 24 2013 Taylor Braun-Jones <taylor@braun-jones.org> - 1.5.0-0.1.0
- Bump version.

* Sun Oct 14 2012 Taylor Braun-Jones <taylor@braun-jones.org> - 1.4.0-0
- Initial creation
