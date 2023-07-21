%ifnarch s390 s390x
%global with_papi 1
%endif

%bcond_without check

%global sover 17

Summary: High-performance library for parallel solution of eigenvalue problems
Name: elpa
Version: 2022.05.001
Release: 3%{?dist}
URL: https://elpa.mpcdf.mpg.de/software
Source0: https://elpa.mpcdf.mpg.de/software/tarball-archive/Releases/%{version}/elpa-%{version}.tar.gz
Source1: https://elpa.mpcdf.mpg.de/software/tarball-archive/Releases/%{version}/elpa-%{version}.tar.gz.asc
Source2: gpg-keyring-26BC8F899C6A2698BDD6EF6A69260748A5F870B5.gpg

# drop _onenode suffix from non-MPI builds
Patch1: elpa-onenode.patch

Patch2: elpa-configure-c99.patch

License: LGPLv3+
BuildRequires: flexiblas-devel
BuildRequires: gcc-c++
BuildRequires: gcc-gfortran
BuildRequires: gnupg2
BuildRequires: libtool
BuildRequires: /usr/bin/execstack
BuildRequires: /usr/bin/xxd
%if %{with papi}
BuildRequires: papi-devel
%endif
Requires: %{name}-common = %{version}-%{release}

%description
ELPA is a Fortran-based high-performance computational library for the
(massively) parallel solution of symmetric or Hermitian, standard or generalized
eigenvalue problems.

This is the kind of eigenvalue problem which is frequently encountered in
Electronic Structure Theory (solution of Schrödinger's Equation or variants
thereof), but also in many other fields. Typically, the solution effort scales
as O(size^3), where "size" is a measure of the system size, for example the
dimension of the associated matrices or the number of required
eigenvalue/eigenvector pairs (less than or equal to the matrix dimension). Thus,
an algebraically exact solution of the eigenproblem may quickly become the
bottleneck in a practical application.

%package common
Summary: Common files for ELPA
BuildArch: noarch

%description common
ELPA is a Fortran-based high-performance computational library for the
(massively) parallel solution of symmetric or Hermitian, standard or generalized
eigenvalue problems.

This package contains common files for ELPA.

%package common-devel
Summary: Common development files for ELPA (non-MPI version)
Requires: %{name}-common = %{version}-%{release}

%description common-devel
ELPA is a Fortran-based high-performance computational library for the
(massively) parallel solution of symmetric or Hermitian, standard or generalized
eigenvalue problems.

This package contains the common development files for ELPA (non-MPI version).

%package devel
Summary: Development files for ELPA (non-MPI version)
Requires: %{name}%{?_isa} = %{version}-%{release}
Requires: %{name}-common-devel = %{version}-%{release}

%description devel
ELPA is a Fortran-based high-performance computational library for the
(massively) parallel solution of symmetric or Hermitian, standard or generalized
eigenvalue problems.

This package contains the development files for ELPA (non-MPI version).

%package mpich
Summary: Fast library for parallel solution of eigenvalue problems (MPICH version)
BuildRequires: mpich-devel
BuildRequires: blacs-mpich-devel
BuildRequires: scalapack-mpich-devel
Requires: %{name}-common = %{version}-%{release}

%description mpich
ELPA is a Fortran-based high-performance computational library for the
(massively) parallel solution of symmetric or Hermitian, standard or generalized
eigenvalue problems.

This package contains ELPA built against MPICH.

%package mpich-devel
Summary: Development files for ELPA (MPICH version)
Requires: %{name}-mpich%{?_isa} = %{version}-%{release}
Requires: gcc-gfortran%{?_isa}
Requires: %{name}-common-devel = %{version}-%{release}
Provides: %{name}-mpi-devel = %{version}-%{release}

%description mpich-devel
ELPA is a Fortran-based high-performance computational library for the
(massively) parallel solution of symmetric or Hermitian, standard or generalized
eigenvalue problems.

This package contains the development files for ELPA (MPICH version).

%package openmpi
Summary: Fast library for parallel solution of eigenvalue problems (OpenMPI version)
# required for running the testsuite
%if %{with check}
BuildRequires: rsh
%endif
BuildRequires: openmpi-devel
BuildRequires: blacs-openmpi-devel
BuildRequires: scalapack-openmpi-devel
BuildRequires: make
Requires: %{name}-common = %{version}-%{release}

%description openmpi
ELPA is a Fortran-based high-performance computational library for the
(massively) parallel solution of symmetric or Hermitian, standard or generalized
eigenvalue problems.

This package contains ELPA built against OpenMPI.

%package openmpi-devel
Summary: Development files for ELPA (OpenMPI version)
Requires: %{name}-openmpi%{?_isa} = %{version}-%{release}
Requires: gcc-gfortran%{?_isa}
Requires: %{name}-common-devel = %{version}-%{release}
Provides: %{name}-mpi-devel = %{version}-%{release}

%description openmpi-devel
ELPA is a Fortran-based high-performance computational library for the
(massively) parallel solution of symmetric or Hermitian, standard or generalized
eigenvalue problems.

This package contains the development files for ELPA (OpenMPI version).

%prep
gpgv2 --keyring %{S:2} %{S:1} %{S:0}
%setup -q -c -T -a 0
mv elpa-%{version} mpich
pushd mpich
%patch1 -p1 -b .onenode
%patch2 -p1 -b .c99
autoreconf -vifs
popd
cp -pr mpich openmpi
cp -pr mpich serial
mkdir _openmp
cp -pr mpich openmpi serial _openmp/

%build
%global defopts --disable-silent-rules --disable-static --docdir=%{_pkgdocdir}
%global ldflags %{__global_ldflags}
%if %{with atlas}
%global ldflags %{ldflags} -L%{_libdir}/atlas
%endif
%global fcflags %(echo %{optflags} | sed -e 's/ -Werror=format-security//') -I%{_fmoddir} -ffree-line-length-none -fallow-argument-mismatch

. /etc/profile.d/modules.sh

for mpi in '' mpich openmpi ; do
  export CFLAGS="%{optflags}"
%ifarch x86_64
  export CFLAGS="${CFLAGS} -mssse3 -mavx"
%endif
  export LDFLAGS="%{ldflags}"
  export FCFLAGS="%{fcflags}"
  if [ -n "$mpi" ]; then
    module load mpi/${mpi}-%{_arch}
    export LDFLAGS="${LDFLAGS} -L$MPI_LIB"
    export CFLAGS="${CFLAGS} -I$MPI_INCLUDE"
    export FCFLAGS="${FCFLAGS} -I$MPI_FORTRAN_MOD_DIR"
  fi
  for s in '' _openmp ; do
    pushd ${s:-.}/${mpi:-serial}
    if [ -n "$mpi" ]; then
      fmoddir="$MPI_FORTRAN_MOD_DIR"
      mpiflag="--libdir=$MPI_LIB"
%ifarch i686
      if [ -n "$s" -a "$mpi" = "openmpi" ]; then
        mpiflag="$mpiflag --without-threading-support-check-during-build --enable-allow-thread-limiting"
      fi
%endif
    else
      fmoddir="%{_fmoddir}"
      mpiflag="--with-mpi=no"
    fi
    sed -i -e "s,\${includedir}/elpa@SUFFIX@-@PACKAGE_VERSION@/modules,${fmoddir}," elpa.pc.in
    %configure %{defopts} \
%ifarch aarch64
      --enable-neon-arch64 \
%endif
%ifarch ppc64le
      --disable-vsx \
%endif
%ifnarch x86_64
      --disable-sse-assembly \
      --disable-sse \
      --disable-avx \
%endif
      --disable-avx2 \
      --disable-avx512 \
      ${s:+--enable-openmp} \
%if %{with papi}
      --with-papi \
%endif
      $mpiflag || cat config.log

    make %{?_smp_mflags} V=1
    popd
  done
  if [ -n "$mpi" ]; then
    module unload mpi/${mpi}-%{_arch}
  fi
done

%install
. /etc/profile.d/modules.sh
for s in '' _openmp ; do
# install serial last to avoid overwriting non-MPI binaries in _bindir
  for mpi in mpich openmpi '' ; do
    pushd ${s:-.}/${mpi:-serial}
    make DESTDIR=%{buildroot} install
    if [ -n "$mpi" ]; then
      module load mpi/${mpi}-%{_arch}
      libdir=%{_libdir}/${mpi}/lib
      fmoddir=$MPI_FORTRAN_MOD_DIR
      mkdir -p %{buildroot}$MPI_BIN
      mv %{buildroot}%{_bindir}/elpa2_print_kernels${s} %{buildroot}$MPI_BIN
      module unload mpi/${mpi}-%{_arch}
    else
      libdir=%{_libdir}
      fmoddir=%{_fmoddir}
    fi
    execstack -c .libs/libelpa${s}.so.%{sover}.* %{buildroot}${libdir}/libelpa${s}.so.%{sover}.*
    mkdir -p %{buildroot}${fmoddir}
    for f in $(ls -1 %{buildroot}%{_includedir}/elpa${s}-%{version}/modules/*.mod) ; do
      m=$(basename ${f} .mod)
      mv %{buildroot}%{_includedir}/elpa${s}-%{version}/modules/${m}.mod %{buildroot}${fmoddir}/${m}${s}.mod
    done
    rmdir %{buildroot}%{_includedir}/elpa${s}-%{version}/modules
    rm %{buildroot}${libdir}/libelpa${s}.la
    popd
  done
done
echo ".so elpa2_print_kernels.1" > %{buildroot}%{_mandir}/man1/elpa2_print_kernels_openmp.1

%if %{with check}
%check
. /etc/profile.d/modules.sh
for s in '' _openmp ; do
%ifarch i686
  for mpi in '' mpich ; do
%else
  for mpi in '' mpich openmpi ; do
%endif
    pushd ${s:-.}/${mpi:-serial}
    if [ -n "$mpi" ]; then
      module load mpi/${mpi}-%{_arch}
      MTASKS=$(expr \( %{_smp_build_ncpus} + 1 \) / 2)
    else
      MTASKS=%{_smp_build_ncpus}
    fi
    if [ -n "$s" ]; then
      export OMP_NUM_THREADS=2
      export ELPA_DEFAULT_omp_threads=2
      MFLAGS="-j$(expr \( $MTASKS + 1 \) / 2)"
    else
      unset OMP_NUM_THREADS
      unset ELPA_DEFAULT_omp_threads
      MFLAGS="-j$MTASKS"
    fi
    make check V=1 TEST_FLAGS="150 50 16" $MFLAGS || cat ./test-suite.log
    if [ -n "$mpi" ]; then
      module unload mpi/${mpi}-%{_arch}
    fi
    popd
  done
done
%endif

%ldconfig_scriptlets

%ldconfig_scriptlets mpich

%ldconfig_scriptlets openmpi

%files
%{_bindir}/elpa2_print_kernels
%{_bindir}/elpa2_print_kernels_openmp
%{_libdir}/libelpa.so.%{sover}*
%{_libdir}/libelpa_openmp.so.%{sover}*

%files common
%license %{_pkgdocdir}/COPYING
%license %{_pkgdocdir}/LICENSE
%license %{_pkgdocdir}/gpl.txt
%license %{_pkgdocdir}/lgpl.txt
%{_pkgdocdir}/README.md
%{_mandir}/man1/elpa2_print_kernels.1*
%{_mandir}/man1/elpa2_print_kernels_openmp.1*

%files common-devel
%{_includedir}/elpa-%{version}
%{_includedir}/elpa_openmp-%{version}
%{_pkgdocdir}/Changelog
%{_pkgdocdir}/CONTRIBUTING.md
%exclude %{_pkgdocdir}/INSTALL.md
%{_pkgdocdir}/PERFORMANCE_TUNING.md
%{_pkgdocdir}/mpi_elpa1.png
%{_pkgdocdir}/mpi_elpa2.png
%{_pkgdocdir}/USERS_GUIDE.md
%{_mandir}/man3/elpa_*.3*

%files devel
%{_libdir}/libelpa.so
%{_libdir}/libelpa_openmp.so
%{_libdir}/pkgconfig/elpa.pc
%{_libdir}/pkgconfig/elpa_openmp.pc
%{_fmoddir}/*.mod

%files mpich
%{_libdir}/mpich/bin/elpa2_print_kernels
%{_libdir}/mpich/bin/elpa2_print_kernels_openmp
%{_libdir}/mpich/lib/libelpa.so.%{sover}*
%{_libdir}/mpich/lib/libelpa_openmp.so.%{sover}*

%files mpich-devel
%{_libdir}/mpich/lib/libelpa.so
%{_libdir}/mpich/lib/libelpa_openmp.so
%{_libdir}/mpich/lib/pkgconfig/elpa.pc
%{_libdir}/mpich/lib/pkgconfig/elpa_openmp.pc
%{_fmoddir}/mpich*/*.mod

%files openmpi
%{_libdir}/openmpi/bin/elpa2_print_kernels
%{_libdir}/openmpi/bin/elpa2_print_kernels_openmp
%{_libdir}/openmpi/lib/libelpa.so.%{sover}*
%{_libdir}/openmpi/lib/libelpa_openmp.so.%{sover}*

%files openmpi-devel
%{_libdir}/openmpi/lib/libelpa.so
%{_libdir}/openmpi/lib/libelpa_openmp.so
%{_libdir}/openmpi/lib/pkgconfig/elpa.pc
%{_libdir}/openmpi/lib/pkgconfig/elpa_openmp.pc
%{_fmoddir}/openmpi*/*.mod

%changelog
* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2022.05.001-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2022.05.001-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Tue Dec 20 2022 Dominik Mierzejewski <dominik@greysector.net> 2022.05.002-1
- update to 2022.05.002 (ABI break) (#2027276)
- re-enable all mpich tests
- drop unsupported flag from FCFLAGS
- skip OpenMPI tests on i686 (#2155197)

* Sat Dec 10 2022 Florian Weimer <fweimer@redhat.com> - 2021.05.002-6
- Port configure script to C99

* Fri Nov 18 2022 Mamoru TASAKA <mtasaka@fedoraproject.org> - 2021.05.002-5
- Rebuild for new papi

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2021.05.002-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2021.05.002-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2021.05.002-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Jul 07 2021 Dominik Mierzejewski <rpm@greysector.net> 2021.05.002-1
- update to 2021.05.002 (#1956381)
- re-enable mpich tests
- add missing BR on gcc-c++
- include more docs in -devel
- disable two hanging mpich tests (#1950149)

* Thu Apr 15 2021 Dominik Mierzejewski <rpm@greysector.net> 2020.11.001-1
- update to 2020.11.001
- drop obsolete patches
- disable mpich tests for now, they seem to hang on all arches
- enable openmpi tests on all arches instead

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2020.05.001-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Sep 15 2020 Dominik Mierzejewski <rpm@greysector.net> 2020.05.001-1
- update to 2020.05.001 (ABI and API break)
- rebase patches and drop obsolete ones
- legacy API removed
- build only SSE3 and AVX SIMD kernels for x86 which should still work on 10yo machines
- disable VSX SIMD as the kernels are broken in this release

* Wed Aug 12 2020 Iñaki Úcar <iucar@fedoraproject.org> - 2019.05.002-6
- https://fedoraproject.org/wiki/Changes/FlexiBLAS_as_BLAS/LAPACK_manager

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2019.05.002-5
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2019.05.002-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Sun Apr 05 2020 Dominik Mierzejewski <rpm@greysector.net> 2019.05.002-3
- fix test failures on x86_64
- work around compilation errors with gfortran 10

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2019.05.002-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Dec 06 2019 Dominik Mierzejewski <rpm@greysector.net> 2019.05.002-1
- update to 2019.05.002 (ABI and API break)
- add new GPG key
- drop upstreamed papi detection patch
- build VSX kernels on ppc64le (Power8)
- build NEON kernels on aarch64
- re-enable OpenMPI tests on i686
- disable FMA usage on aarc64 to fix failing tests
- parallelize test suite according to upstream guidance
- decrease matrix size to make test suite run faster

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2017.05.003-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Feb 14 2019 Orion Poplawski <orion@nwra.com> - 2017.05.003-5
- Rebuild for openmpi 3.1.3

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2017.05.003-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2017.05.003-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2017.05.003-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Fri Nov 10 2017 Dominik Mierzejewski <rpm@greysector.net> 2017.05.003-1
- update to 2017.05.003 (ABI and API break)
- drop obsolete openblas patch
- re-enable OpenMPI OpenMP builds
- enable papi on supported arches
- build and ship non-MPI version (without _onenode suffix)
- provide a man-link for openmp version of elpa2_print_kernels
- execstack is now available everywhere
- include and verify GPG signature
- conditionalize running tests and reduce testsuite runtime per upstream
  recommendation
- split out API documentation and headers into -common-devel subpackage
- disable all non-generic kernels on non-x86_64 for now
- disable testing under OpenMPI for now (rhbz#1512229)

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2015.11.001-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2015.11.001-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Mon Jun 12 2017 Dominik Mierzejewski <rpm@greysector.net> 2015.11.001-6
- fix AVX2 instructions usage enablement (#1383412)

* Sun Jun 11 2017 Dominik Mierzejewski <rpm@greysector.net> 2015.11.001-5
- update URL and Source URL, switch to https
- factorize build process
- fix Fortran mods path (#1409235)
- build against openblas on supported arches to match scalapack
- don't run the testsuite on ARM 32bit (takes 6.5 hours)
- execstack is not available on some arches for EPEL (#1460531)

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2015.11.001-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Sun Nov 13 2016 Peter Robinson <pbrobinson@fedoraproject.org> 2015.11.001-3
- Rebuild (Power64)

* Fri Oct 21 2016 Orion Poplawski <orion@cora.nwra.com> - 2015.11.001-2
- Rebuild for openmpi 2.0

* Sun Apr 03 2016 Dominik Mierzejewski <rpm@greysector.net> 2015.11.001-1
- update to 2015.11.001 release
- update URL and Source URL
- fix AVX(2) support detection and usage
- drop condition around execstack usage, it's available everywhere now
- drop _opt_cc_suffix usage and factor out more stuff into common macros

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 2015.05.001-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Tue Sep 15 2015 Orion Poplawski <orion@cora.nwra.com> - 2015.05.001-3
- Rebuild for openmpi 1.10.0

* Mon Aug 10 2015 Sandro Mani <manisandro@gmail.com> - 2015.05.001-2
- Rebuild for RPM MPI Requires Provides Change

* Thu Aug 06 2015 Dominik Mierzejewski <rpm@greysector.net> 2015.05.001-1
- update to 2015.05.001 release
- don't use all available cores for the testsuite (interferes with OpenMP)
  (work around #1220161)
- drop obsolete comments and rename patch0 appropriately
- fix AVX support detection

* Tue Aug 04 2015 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 2015.02.002-6
- Use new execstack (#1247795)

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2015.02.002-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Mon May 04 2015 Dominik Mierzejewski <rpm@greysector.net> 2015.02.002-4
- fix build on EPEL7 (missing _pkgdocdir macro and BR: rsh for openmpi)
- move examples to -devel subpackage
- print whole testsuite log in case of test failure
- re-enable openmpi tests on i686 and armv7hl

* Sat May 02 2015 Kalev Lember <kalevlember@gmail.com> - 2015.02.002-3
- Rebuilt for GCC 5 C++11 ABI change

* Mon Mar 23 2015 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 2015.02.002-2
- Rebuild for fortran update (#1204420)

* Thu Mar 19 2015 Dominik Mierzejewski <rpm@greysector.net> 2015.02.002-1
- update to 2015.02.002 release (ABI change)
- drop libtool bug workaround
- make builds more verbose
- take advantage of upstream build system improvements
- ship C headers in -devel subpackage

* Mon Mar 16 2015 Thomas Spura <tomspur@fedoraproject.org> - 2013.11-6.008
- Rebuild for changed mpich libraries

* Tue Sep 16 2014 Dominik Mierzejewski <rpm@greysector.net> 2013.11-5.008
- fix release string broken by previous bump by releng script
- disable openmpi tests on armv7hl (bug #1144408)

* Sat Aug 16 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2013.11-4.9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Thu Jul  3 2014 Peter Robinson <pbrobinson@fedoraproject.org> 2013.11-4.008
- aarch64/ppc64le don't have prelink

* Sun Jun 29 2014 Dominik Mierzejewski <rpm@greysector.net> 2013.11-3.008
- fix typo in execstack -c call
- link against atlas

* Thu Jun 26 2014 Dominik Mierzejewski <rpm@greysector.net> 2013.11-2.008
- remove executable stack from installed libraries
- fix undefined non-weak mpi symbols
- reorder build section and drop some redundant parts
- add missing gfortran Requires for -devel subpackages
- use correct URL and provide link to source tarball

* Tue Jun 24 2014 Dominik Mierzejewski <rpm@greysector.net> 2013.11-1.008
- initial build
