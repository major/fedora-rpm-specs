%if 0%{?fedora} >= 33 || 0%{?rhel} >= 9
%global blaslib flexiblas
%global cmake_blas_flags -DBLAS_TYPE=FLEXIBLAS -DLAPACK_TYPE=FLEXIBLAS
%else
%global blaslib openblas
%global blasvar o
%global cmake_blas_flags -DBLAS_LIBRARIES=%{_libdir}/lib%{blaslib}%{blasvar}.so -DLAPACK_LIBRARIES=%{_libdir}/lib%{blaslib}%{blasvar}.so
%endif

# Disable x86 architectures since libint2 is not available there
ExcludeArch: %{ix86}
# The builds experience random crashes across platforms which suggests out-of-memory issues, reduce to four threads
%define _smp_mflags -j4

Name:           psi4
Epoch:          1
Version:        1.9.1
Release:        5%{?dist}
Summary:        An ab initio quantum chemistry package
# Automatically converted from old format: LGPLv3 and MIT - review is highly recommended.
License:        LGPL-3.0-only AND LicenseRef-Callaway-MIT
URL:            http://www.psicode.org/
Source0:        https://github.com/psi4/psi4/archive/v%{version}/psi4-%{version}.tar.gz

# Fix memory error, patch extracted from https://github.com/psi4/psi4/pull/3194
Patch0:         psi4-1.9.1-libint2.patch
# Tests should call python3 not python
Patch1:         psi4-1.3.2-python3.patch
# Fix memory overflow issue
Patch2:         psi4-1.9.1-overflow.patch
# Disable test that uses qcengine, since psi4 backend of python-qcengine is broken (BZ#2309462)
Patch3:         psi4-1.9.1-noqcetest.patch
# Disable test that uses qcengine, since psi4 backend of python-qcengine is broken (BZ#2309462)
Patch4:         psi4-1.9.1-noecpgrad.patch
# Don't strip the library
Patch5:         psi4-1.9.1-nostrip.patch
# Patch build system so that libxc 7.0.0 is accepted
Patch6:         psi4-1.9.1-libxc7.patch

BuildRequires:  cmake
BuildRequires:  bison-devel
BuildRequires:  byacc
BuildRequires:  flex
BuildRequires:  gcc-c++
BuildRequires:  gcc-gfortran
BuildRequires:  perl-devel
BuildRequires:  gsl-devel
BuildRequires:  hdf5-devel
BuildRequires:  zlib-devel

BuildRequires:  %{blaslib}-devel
BuildRequires:  CheMPS2-devel
BuildRequires:  libint2-devel >= 2.9.0-1
BuildRequires:  libxc-devel
BuildRequires:  pybind11-static
BuildRequires:  gau2grid-devel
BuildRequires:  libefp-devel
BuildRequires:  libecpint-devel

# Libint2 cmake requires this too
BuildRequires:  boost-devel
BuildRequires:  eigen3-devel
BuildRequires:  gmp-devel
BuildRequires:  mpfr-devel

BuildRequires:  python3-devel >= 2.7
BuildRequires:  python3-numpy
BuildRequires:  python3-scipy
BuildRequires:  python3-deepdiff
BuildRequires:  python3-sphinx >= 1.1
BuildRequires:  python3-pydantic
BuildRequires:  python3-qcengine
BuildRequires:  python3-qcelemental
BuildRequires:  python3-optking
BuildRequires:  python3-pint
BuildRequires:  python3-setuptools
BuildRequires:  python3-pytest
# For the documentation
BuildRequires:  tex(latex)
BuildRequires:  tex-preview
BuildRequires:  dvipng
BuildRequires:  graphviz

# These are required also at runtime
Requires:       python3-numpy
Requires:       python3-scipy
Requires:       python3-pydantic
Requires:       python3-qcengine
Requires:       python3-qcelemental
Requires:       python3-deepdiff
Requires:       python3-optking
# For directory ownership
Requires:       cmake

%if %{with tests}
# Needed for running tests
BuildRequires:  perl(Env)
%endif

Requires:  %{name}-data = %{epoch}:%{version}-%{release}
# Libint can break the api between releases
Requires:  libint2(api)%{?_isa} = %{_libint2_apiversion}

# Don't have documentation in the cmake version yet.. 
Obsoletes: psi4-doc < 1:0.3-1

# As there are no static libraries anymore, the build system doesn't
# allow building a devel package, but the CMake configuration is still
# architecture dependent.
Provides:       psi4-devel = %{version}-%{release}
Obsoletes:      psi4-devel < %{version}-%{release}

%description
PSI4 is an open-source suite of ab initio quantum chemistry programs
designed for efficient, high-accuracy simulations of a variety of
molecular properties. We can routinely perform computations with more
than 2500 basis functions running serially or in parallel.

%package data
Summary:   Data files necessary for operation of PSI4
BuildArch: noarch

%description data
This package contains necessary data files for PSI4, e.g., basis sets
and the quadrature grids.

%prep
%setup -q
%patch 0 -p1 -b .libint2
%patch 1 -p1 -b .python3
%patch 2 -p1 -b .overflow
%patch 3 -p1 -b .noqcetest
%patch 4 -p1 -b .noecpgrad
%patch 5 -p1 -b .nostrip
%patch 6 -p1 -b .libxc7

%build
export F77=gfortran
export FC=gfortran

# Massage the Python site directory for the installer
export pymoddir=$(echo %{python3_sitearch} | sed "s|%{_libdir}||g")

%cmake \
       -DENABLE_OPENMP=ON -DENABLE_XHOST=OFF \
       -DPYMOD_INSTALL_LIBDIR=${pymoddir} \
       %{cmake_blas_flags} -DENABLE_AUTO_LAPACK=ON \
       -DCMAKE_Fortran_COMPILER=gfortran -DCMAKE_C_COMPILER=gcc -DCMAKE_CXX_COMPILER=g++ \
       -DCUSTOM_C_FLAGS='%{optflags} -std=c11 -DNDEBUG' -DCUSTOM_CXX_FLAGS='%{optflags} -DNDEBUG' \
       -DCUSTOM_Fortran_FLAGS='-I%{_libdir}/gfortran/modules %{optflags} -DNDEBUG' \
       -DCMAKE_BUILD_TYPE=Release -DCMAKE_INSTALL_LIBDIR="%{_lib}" \
       -DENABLE_CheMPS2=ON -DENABLE_libefp=OFF -DENABLE_ecpint=ON
#libefp turned off since it needs a separate Python wrapper

# Build program
%cmake_build

%install
%cmake_install

# Get rid of spurious files
rm -rf %{buildroot}%{_builddir}
rm -rf %{buildroot}%{_datadir}/TargetHDF5/
rm -rf %{buildroot}%{_datadir}/TargetLAPACK/
rm -rf %{buildroot}%{_datadir}/TargetHDF5/
rm -rf %{buildroot}%{_datadir}/cmake/TargetHDF5/
rm -rf %{buildroot}%{_datadir}/cmake/TargetLAPACK/

%check
# Run quick tests to see the program works.
# quicktests are too long, whole test suite way too long.
cd %{_vpath_builddir}/tests
ctest -L smoketests --output-on-failure

%files
%license COPYING COPYING.LESSER
%doc README.md
%{python3_sitearch}/psi4/
%{_datadir}/cmake/psi4/
%{_includedir}/psi4/
%{_bindir}/psi4

%files data
%license COPYING COPYING.LESSER
%{_datadir}/psi4/

%changelog
* Sat Jan 18 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1:1.9.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Fri Oct 25 2024 Orion Poplawski <orion@nwra.com> - 1:1.9.1-4
- Rebuild for hdf5 1.14.5

* Sat Oct 12 2024 Susi Lehtola <jussilehtola@fedoraproject.org> - 1:1.9.1-3
- Patch for libxc 7.0.0 compatibility in rawhide.

* Wed Sep 04 2024 Miroslav Suchý <msuchy@redhat.com> - 1:1.9.1-2
- convert license to SPDX

* Tue Sep 03 2024 Susi Lehtola <jussilehtola@fedoraproject.org> - 1:1.9.1-1
- Update to 1.9.1.

* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1:1.3.2-24
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Sat Jun 29 2024 Python Maint <python-maint@redhat.com> - 1:1.3.2-23
- Rebuilt for Python 3.13

* Fri Jan 26 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1:1.3.2-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1:1.3.2-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1:1.3.2-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Tue May 02 2023 Susi Lehtola <jussilehtola@fedoraproject.org> - 1:1.3.2-19
- Address deprecated np.int (BZ #2192326).

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1:1.3.2-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Wed Nov 02 2022 Susi Lehtola <jussilehtola@fedoraproject.org> - 1:1.3.2-17
- Fix build issue on rawhide.

* Thu Oct 27 2022 Mamoru TASAKA <mtasaka@fedoraproject.org> - 1:1.3.2-16
- Rebuild for new libxc

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1:1.3.2-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1:1.3.2-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1:1.3.2-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jul 13 2021 Björn Esser <besser82@fedoraproject.org> - 1:1.3.2-12
- Add a patch for native support of FlexiBLAS
- Explicitly turn ENABLE_AUTO_LAPACK on

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 1:1.3.2-11
- Rebuilt for Python 3.10

* Wed Mar 31 2021 Susi Lehtola <jussilehtola@fedoraproject.org> - 1:1.3.2-10
- Make the psi4 Python module importable.
- Remove rpath.

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1:1.3.2-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Aug 26 2020 Jeff Law <law@redhat.com> - 1:1.3.2-8
- Do not force C++11 mode

* Sun Aug 16 2020 Iñaki Úcar <iucar@fedoraproject.org> - 1:1.3.2-7
- https://fedoraproject.org/wiki/Changes/FlexiBLAS_as_BLAS/LAPACK_manager

* Wed Aug 05 2020 Susi Lehtola <jussilehtola@fedoraproject.org> - 1:1.3.2-6
- Adapt to new CMake scripts.

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1:1.3.2-5
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1:1.3.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue May 05 2020 Susi Lehtola <jussilehtola@fedoraproject.org> - 1:1.3.2-3
- Rebuild against libxc 5 in rawhide.
- Add missing deepdiff requires.

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1:1.3.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Mon Jan 13 2020 Susi Lehtola <jussilehtola@fedoraproject.org> - 1:1.3.2-1
- Update to 1.3.2.

* Mon Mar 04 2019 Susi Lehtola <jussilehtola@fedoraproject.org> - 1:1.3.0-1
- Update to 1.3.0.

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1:1.2.1-5.b167f47
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Wed Jan 02 2019 Susi Lehtola <jussilehtola@fedoraproject.org> - 1:1.2.1-4.b167f473git
- Add deepdiff requires.

* Sun Dec 09 2018 Miro Hrončok <mhroncok@redhat.com> - 1:1.2.1-3.b167f47
- Require python3-numpy instead of python2-numpy

* Wed Sep 26 2018 Susi Lehtola <jussilehtola@fedoraproject.org> - 1:1.2.1-2.b167f473git
- Update to git snapshot to make code run with -D_GLIBCXX_ASSERTIONS.

* Sat Sep 22 2018 Susi Lehtola <jussilehtola@fedoraproject.org> - 1:1.2.1-1
- Update to 1.2.1.

* Fri Aug 10 2018 Marcel Plch <mplch@redhat.com> - 1:1.1-8.add49b9git
- Patch for pybind 2.2.3

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1:1.1-7.add49b9git
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 1:1.1-6.add49b9git
- Rebuilt for Python 3.7

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1:1.1-5.add49b9git
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1:1.1-4.add49b9git
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1:1.1-3.add49b9git
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri May 19 2017 Susi Lehtola <jussilehtola@fedoraproject.org> - 1:1.1-2.add49b95git
- Epoch was missing from a requires.

* Wed May 17 2017 Susi Lehtola <jussilehtola@fedoraproject.org> - 1:1.1-1.add49b95git
- Update to version 1.1. License changes from GPLv2+ to LGPLv3.
- Make sure binary is linked to right atlas library.

* Mon May 15 2017 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1:1.0-3.2118f2fgit
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_27_Mass_Rebuild

* Thu Mar 02 2017 Susi Lehtola <jussilehtola@fedoraproject.org> - 1:1.0-2.2118f2f5git
- Update to get patch that fixes build on rawhide.

* Mon Feb 27 2017 Susi Lehtola <jussilehtola@fedoraproject.org> - 1:1.0-1.926879e2git
- Update to newest git snapshot.

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1:1.0-0.3.rc.15fc63cgit
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri Jan 27 2017 Jonathan Wakely <jwakely@redhat.com> - 1:1.0-0.2.rc.15fc63cgit
- Rebuilt for Boost 1.63

* Thu Jun 02 2016 Susi Lehtola <jussilehtola@fedoraproject.org> - 1:1.0-0.1.rc.15fc64cgit
- Update to 1.0 release candidate.

* Tue May 17 2016 Jonathan Wakely <jwakely@redhat.com> - 1:0.3-7.1881450git
- Rebuilt for linker errors in boost (#1331983)

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1:0.3-6.1881450git
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Jan 15 2016 Jonathan Wakely <jwakely@redhat.com> - 1:0.3-5.1881450git
- Rebuilt for Boost 1.60

* Wed Sep 09 2015 Susi Lehtola <jussilehtola@fedoraproject.org> - 1:0.3-4.1881450fgit
- Use narrowing patch from upstream instead of -Wno-narrowing.

* Tue Sep 08 2015 Susi Lehtola <jussilehtola@fedoraproject.org> - 1:0.3-3.1881450fgit
- Add epoch to explicit requires.

* Tue Sep 08 2015 Susi Lehtola <jussilehtola@fedoraproject.org> - 1:0.3-2.1881450fgit
- Patch to fix broken linkage.

* Sun Sep 06 2015 Susi Lehtola <jussilehtola@fedoraproject.org> - 1:0.3-1.1881450fgit
- Update to newest release, switched to using github release tags.

* Wed Jul 29 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.0-0.21.c7deee9git.1
- Rebuilt for https://fedoraproject.org/wiki/Changes/F23Boost159

* Wed Jul 22 2015 David Tardon <dtardon@redhat.com> - 4.0-0.20.c7deee9git.1
- rebuild for Boost 1.58

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.0-0.19.c7deee9git.1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat May 02 2015 Kalev Lember <kalevlember@gmail.com> - 4.0-0.18.c7deee9git.1
- Rebuilt for GCC 5 C++11 ABI change

* Tue Jan 27 2015 Petr Machata <pmachata@redhat.com> - 4.0-0.17.c7deee9git.1
- Rebuild for boost 1.57.0

* Thu Sep 11 2014 Susi Lehtola <jussilehtola@fedoraproject.org> - 4.0-0.16.c7deee99.1
- Forgot to tag buildroot override in previous build.

* Wed Sep 10 2014 Susi Lehtola <jussilehtola@fedoraproject.org> - 4.0-0.16.c7deee99
- Update to newest snapshot.
- Requires libint(api).

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.0-0.15.0c7ea92git.1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Wed Jul 02 2014 Susi Lehtola <jussilehtola@fedoraproject.org> - 4.0-0.14.0c7ea92git.1
- Rebuild due to rebuilt libint.

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.0-0.14.0c7ea92git
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Fri May 23 2014 Petr Machata <pmachata@redhat.com> - 4.0-0.13.0c7ea92git
- Rebuild for boost 1.55.0

* Tue May 13 2014 Susi Lehtola <jussilehtola@fedoraproject.org> - 4.0-0.12.0c7ea928git
- Add BR: perl(Env) for tests.

* Tue May 13 2014 Susi Lehtola <jussilehtola@fedoraproject.org> - 4.0-0.11.0c7ea928git
- Update to newest git snapshot.
- Remove BR: ruby-devel.

* Mon Mar 10 2014 Susi Lehtola <jussilehtola@fedoraproject.org> - 4.0-0.10.b5
- Rebuild against updated libint.

* Sat Jan 04 2014 Susi Lehtola <jussilehtola@fedoraproject.org> - 4.0-0.9.b5
- Drop %%?_isa from virtual provide of -static package (BZ #951582).

* Fri Dec 27 2013 Susi Lehtola <jussilehtola@fedoraproject.org> - 4.0-0.8.b5
- Versioned libint build dependency.

* Tue Dec 24 2013 Susi Lehtola <jussilehtola@fedoraproject.org> - 4.0-0.7.b5
- Added LICENSE and COPYING to -data as well.
- Versioned libint dependency.

* Sat Dec 21 2013 Susi Lehtola <jussilehtola@fedoraproject.org> - 4.0-0.6.b5
- Get rid of bundled madness.

* Thu Dec 19 2013 Susi Lehtola <jussilehtola@fedoraproject.org> - 4.0-0.5.b5
- Added BR and R on numpy.
- Use ATLAS after all.

* Fri Aug 16 2013 Susi Lehtola <jussilehtola@fedoraproject.org> - 4.0-0.4.b5
- Use openblas on supported architectures.
- Update to beta5.

* Thu May 02 2013 Susi Lehtola <jussilehtola@fedoraproject.org> - 4.0-0.3.b4
- Added BR on graphviz and enabled dot in configure for documentation.

* Tue Apr 30 2013 Susi Lehtola <jussilehtola@fedoraproject.org> - 4.0-0.2.b4
- Review fixes.

* Thu Apr 11 2013 Susi Lehtola <jussilehtola@fedoraproject.org> - 4.0-0.1.b4
- First release.
