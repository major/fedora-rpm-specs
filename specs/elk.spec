# Warning:
# Anyone editing this spec file please make sure the same spec file
# works on other fedora and epel releases, which are supported by this software.
# No quick Rawhide-only fixes will be allowed.

%if 0%{?el6} || 0%{?el7}
elk-5.2.14 requires libxc 3 or newer
%quit
%endif

# missing on el6
%{?!_fmoddir: %global _fmoddir %{_libdir}/gfortran/modules}

%if 0%{?fedora} >= 32 || 0%{?rhel} >= 9
%global extra_gfortran_flags -fallow-argument-mismatch
%else
%global extra_gfortran_flags %{nil}
%endif

%if 0%{?el6}
# el6/ppc64 Error: No Package found for mpich-devel
ExclusiveArch:          x86_64 %{ix86}
%else
%if 0%{?fedora} >= 40
ExclusiveArch:          x86_64 aarch64 %{arm} %{power64}
%else
ExclusiveArch:          x86_64 %{ix86} aarch64 %{arm} %{power64}
%endif
%endif

%if 0%{?fedora} >= 33 || 0%{?rhel} >= 9
%global BLASLAPACK flexiblas
%else
%global BLASLAPACK openblas
%endif
%global FFTW -L%{_libdir} -lfftw3 -lfftw3f
%if 0%{?fedora} >= 25 || 0%{?rhel} >= 9
%global LIBXC -L%{_libdir} -lxc -lxcf03
%else
%global LIBXC -L%{_libdir} -lxc
%endif

Name:			elk
Version:		9.2.12
Release:		6%{?dist}
Summary:		An all-electron full-potential linearised augmented-plane wave code

# Automatically converted from old format: GPLv3+ - review is highly recommended.
License:		GPL-3.0-or-later
URL:			http://elk.sourceforge.net/
Source0:		https://downloads.sourceforge.net/project/%{name}/%{name}-%{version}.tgz

# Patch for libxc 7 compatibility: standard Fortran interface has been called libxcf03 since libxc 3
Patch0:                 elk-9.2.12-libxc7.patch

BuildRequires:		patch
BuildRequires:		time

BuildRequires:		gcc-gfortran
BuildRequires:		%{BLASLAPACK}-devel
# Use openblas-serial instead of openblas-openmp, but it's unavailable on centos stream
# due to https://bugzilla.redhat.com/show_bug.cgi?id=2182460, so use a workaround of export OMP_NUM_THREADS=1
# https://github.com/edoapra/fedpkg/issues/10#issuecomment-731855285
%if 0%{?fedora} >= 33 || 0%{?rhel} >= 9
BuildRequires:		flexiblas-openblas-openmp
Requires:		flexiblas-openblas-openmp
%endif

BuildRequires:		fftw3-devel
BuildRequires:		libxc-devel

Requires:		%{name}-species = %{version}-%{release}


%global desc_base \
An all-electron full-potential linearised augmented-plane wave (FP-LAPW) code\
with many advanced features. Written originally at\
Karl-Franzens-Universität Graz as a milestone of the EXCITING EU Research and\
Training Network, the code is designed to be as simple as possible so that new\
developments in the field of density functional theory (DFT) can be added\
quickly and reliably.


%description
%{desc_base}


%package openmpi
Summary:		%{name} - openmpi version
BuildRequires:		openmpi-devel
Requires:		%{name}-species = %{version}-%{release}

%description openmpi
%{desc_base}

This package contains the openmpi version.


%package mpich
Summary:		%{name} - mpich version
BuildRequires:		mpich-devel
BuildRequires: make
Requires:		%{name}-species = %{version}-%{release}

%description mpich
%{desc_base}

This package contains the mpich version.


%package species
Summary:		%{name} - species files
Requires:		%{name}-common = %{version}-%{release}
BuildArch:		noarch

%description species
%{desc_base}

This package contains the species files.


%package common
Summary:		%{name} - common files

%description common
%{desc_base}

This package contains the common binaries.


%prep
%setup -q -n %{name}-%{version}
%patch 0 -p 1 -b .libxc7

%if 0%{?fedora} >= 41
# Libxc 7 split off the functionals into a different module
sed -i 's|use xc_f03_lib_m|use xc_f03_lib_m\nuse xc_f03_funcs_m|g' src/libxcifc.f90
%endif

# create common make.inc.common
# default serial fortran
echo "SRC_MPI = mpi_stub.f90" > make.inc.common
echo "F90 = gfortran -fopenmp %{extra_gfortran_flags}" >> make.inc.common
echo "F77 = gfortran -fopenmp %{extra_gfortran_flags}" >> make.inc.common
echo "F90_OPTS = -I%{_fmoddir} %{optflags}" >> make.inc.common
echo "F77_OPTS = \$(F90_OPTS)" >> make.inc.common
echo "AR = ar" >> make.inc.common
# Use stub routines which Elk can call when libraries are not available
echo "SRC_MKL = mkl_stub.f90" >> make.inc.common
echo "SRC_BLIS = blis_stub.f90" >> make.inc.common
echo "SRC_W90S = w90_stub.f90" >> make.inc.common
# enable blas/fftw/libxc dynamic linking
echo "F90_LIB = -L%{_libdir} -l%{BLASLAPACK} %{FFTW}" >> make.inc.common
echo "SRC_FFT = zfftifc_fftw.f90 cfftifc_fftw.f90" >> make.inc.common
echo "LIB_LIBXC = %LIBXC" >> make.inc.common
echo "SRC_LIBXC = libxcifc.f90" >> make.inc.common

# remove bundling of BLAS/LAPACK/FFTW/LIBXC/ERF
sed -i "s/blas lapack fft elk/elk/" src/Makefile
sed -i "s/erf.f90//" src/Makefile
sed -i "s/,erf//" src/stheta_mp.f90
# remove bundled sources
rm -rf src/LAPACK src/BLAS src/fftlib
rm -f src/libxc_funcs.f90 src/libxc.f90 src/libxcf90.f90
rm -f src/erf.f90


%build
# Have to do off-root builds to be able to build many versions at once
mv src src.orig

# To avoid replicated code define a macro
%global dobuild() \
cp -p make.inc.common make.inc&& \
%{__sed} -i "s|F90 =.*|F90 = mpif90 -fopenmp %{extra_gfortran_flags}|" make.inc&& \
%{__sed} -i "s|F77 =.*|F77 = mpif77 -fopenmp %{extra_gfortran_flags}|" make.inc&& \
%{__sed} -i "s|F90_OPTS =|F90_OPTS = -I\${MPI_FORTRAN_MOD_DIR}|" make.inc&& \
echo "SRC_MPI =" >> make.inc&&\
cat make.inc&& \
cp -p make.inc make.inc$MPI_SUFFIX&& \
%{__make}&& \
mv src/%{name} %{name}$MPI_SUFFIX&& \
%{__make} clean

# build serial/openmp version
export MPI_SUFFIX=_openmp
cp -rp src.orig src
cp -p make.inc.common make.inc&& \
cat make.inc&& \
cp -p make.inc make.inc$MPI_SUFFIX&& \
%{__make}&& \
mv src/%{name} .&& \
mv src/eos/eos elk-eos&& \
mv src/spacegroup/spacegroup elk-spacegroup&& \
%{__make} clean&& \
rm -rf src

# build openmpi version
cp -rp src.orig src
%{_openmpi_load}
%dobuild
%{_openmpi_unload}
rm -rf src

cp -rp src.orig src
# build mpich version
%{_mpich_load}
%dobuild
%{_mpich_unload}
# leave last src build for debuginfo


%install
mkdir -p $RPM_BUILD_ROOT%{_sysconfdir}

# To avoid replicated code define a macro
%global doinstall() \
mkdir -p $RPM_BUILD_ROOT/$MPI_BIN&& \
install -p -m 755 %{name}$MPI_SUFFIX $RPM_BUILD_ROOT/$MPI_BIN/%{name}_binary$MPI_SUFFIX&& \
echo '#!/bin/bash' >  $RPM_BUILD_ROOT/$MPI_BIN/%{name}$MPI_SUFFIX&& \
echo 'export FLEXIBLAS=openblas-openmp' >>  $RPM_BUILD_ROOT/$MPI_BIN/%{name}$MPI_SUFFIX&& \
echo 'export OMP_NUM_THREADS=1' >>  $RPM_BUILD_ROOT/$MPI_BIN/%{name}$MPI_SUFFIX&& \
echo -n "%{name}_binary$MPI_SUFFIX " >>  $RPM_BUILD_ROOT/$MPI_BIN/%{name}$MPI_SUFFIX&& \
echo '"$@"' >>  $RPM_BUILD_ROOT/$MPI_BIN/%{name}$MPI_SUFFIX&& \
chmod 755  $RPM_BUILD_ROOT/$MPI_BIN/%{name}$MPI_SUFFIX&& \
cat $RPM_BUILD_ROOT/$MPI_BIN/%{name}$MPI_SUFFIX


# install serial version
mkdir -p $RPM_BUILD_ROOT%{_bindir}
install -p -m 755 %{name} elk-eos elk-spacegroup $RPM_BUILD_ROOT%{_bindir}

# install openmpi version
%{_openmpi_load}
%doinstall
%{_openmpi_unload}

# install mpich version
%{_mpich_load}
%doinstall
%{_mpich_unload}

mkdir -p $RPM_BUILD_ROOT%{_datadir}/%{name}

# don't copy utilities - they trigger dependency on perl, python ...
cp -rp species $RPM_BUILD_ROOT%{_datadir}/%{name}
cp -rp make.inc* $RPM_BUILD_ROOT%{_datadir}/%{name}
cp -rp tests tests-libxc examples $RPM_BUILD_ROOT%{_datadir}/%{name}


%check

export NPROC=2 # test on X cores
export OMP_NUM_THREADS=1

# save tests
mv tests-libxc tests-libxc.orig
mv tests tests.orig

export TIMEOUT_OPTS='--preserve-status --kill-after 10 7200'

# To avoid replicated code define a macro
%global docheck() \
cp -rp tests-libxc.orig tests-libxc&& \
cp -rp tests.orig tests&& \
sed -i "s#mpirun -n 4 ../../src/elk#$ELK_EXECUTABLE#g" tests/test-mpi.sh&& \
sed -i "/Failed/ a \ \ \ \ cat test.log" tests/test-mpi.sh&& \
timeout ${TIMEOUT_OPTS} time %{__make} test-libxc-mpi 2>&1 | tee test-libxc-mpi.${NPROC}$MPI_SUFFIX.log&& \
rm -rf tests tests-libxc&& \
cp -rp tests.orig tests&& \
sed -i "s#mpirun -n 4 ../../src/elk#$ELK_EXECUTABLE#g" tests/test-mpi.sh&& \
sed -i "/Failed/ a \ \ \ \ cat test.log" tests/test-mpi.sh&& \
timeout ${TIMEOUT_OPTS} time %{__make} test-mpi 2>&1 | tee test-mpi.${NPROC}$MPI_SUFFIX.log&& \
rm -rf tests

# check serial version
ELK_EXECUTABLE="../../%{name}" MPI_SUFFIX=_openmp %docheck

# check openmpi version
%{_openmpi_load}
ELK_EXECUTABLE="mpiexec -np ${NPROC} ../../%{name}$MPI_SUFFIX" %docheck
%{_openmpi_unload}

# this will fail for mpich2 on el6 - mpd would need to be started ...
# check mpich version
%{_mpich_load}
ELK_EXECUTABLE="mpiexec -np ${NPROC} ../../%{name}$MPI_SUFFIX" %docheck
%{_mpich_unload}

# restore tests
mv tests-libxc.orig tests-libxc
mv tests.orig tests


%files
%{_bindir}/%{name}


%files common
%doc COPYING README
%{_bindir}/elk-eos
%{_bindir}/elk-spacegroup
%{_datadir}/%{name}
%exclude %{_datadir}/%{name}/species


%files species
%{_datadir}/%{name}/species


%files openmpi
%{_libdir}/openmpi%{?_opt_cc_suffix}/bin/%{name}_binary_openmpi
%{_libdir}/openmpi%{?_opt_cc_suffix}/bin/%{name}_openmpi


%files mpich
%{_libdir}/mpich%{?_opt_cc_suffix}/bin/%{name}_binary_mpich
%{_libdir}/mpich%{?_opt_cc_suffix}/bin/%{name}_mpich


%changelog
* Thu Jan 16 2025 Fedora Release Engineering <releng@fedoraproject.org> - 9.2.12-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Sat Oct 12 2024 Susi Lehtola <jussilehtola@fedoraproject.org> - 9.2.12-5
- Missed an explicit libxc version check.

* Sat Oct 12 2024 Susi Lehtola <jussilehtola@fedoraproject.org> - 9.2.12-4
- Remove bunded Libxc sources and patch for libxc 7 compatibility.

* Thu Jul 25 2024 Miroslav Suchý <msuchy@redhat.com> - 9.2.12-3
- convert license to SPDX

* Wed Jul 17 2024 Fedora Release Engineering <releng@fedoraproject.org> - 9.2.12-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Tue Jan 30 2024 Marcin Dulak <marcindulak@fedoraproject.org> - 9.2.12-1
- Remove support for i686 due to openmpi removal

* Wed Jan 24 2024 Fedora Release Engineering <releng@fedoraproject.org> - 8.8.26-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 8.8.26-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 8.8.26-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Fri Jun 09 2023 Marcin Dulak <marcindulak@fedoraproject.org> - 8.8.26-1
- New upstream release
- Switch to flexiblas-openblas-openmp due to bug #2182460

* Tue Mar 28 2023 Marcin Dulak <marcindulak@fedoraproject.org> - 8.7.10-1
- New upstream release
- Use 4 cores for test-libxc-mpi

* Thu Jan 19 2023 Marcin Dulak <marcindulak@fedoraproject.org> - 8.7.2-1
- New upstream release

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 8.5.10-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Nov 17 2022 Marcin Dulak <marcindulak@fedoraproject.org> - 8.5.10-1
- New upstream release
- Patch for libxc6 compatibility bug #2137308

* Thu Oct 27 2022 Mamoru TASAKA <mtasaka@fedoraproject.org> - 8.3.22-3
- Rebuild for new libxc

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 8.3.22-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Sun Jan 30 2022 Marcin Dulak <marcindulak@fedoraproject.org> - 8.3.22-1
- New upstream release

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 7.2.42-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Tue Aug 03 2021 Marcin Dulak <marcindulak@fedoraproject.org> - 7.2.42-2
- export FLEXIBLAS=openblas-serial using a wrapper https://bugzilla.redhat.com/show_bug.cgi?id=1920009

* Tue Aug 03 2021 Marcin Dulak <marcindulak@fedoraproject.org> - 7.2.42-1
- New upstream release

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 7.1.14-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri May 07 2021 Marcin Dulak <marcindulak@fedoraproject.org> - 7.1.14-1
- New upstream release
- Change changelog email

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 6.8.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Sun Sep 06 2020 Marcin Dulak <marcindulak@fedoraproject.org> - 6.8.4-1
- New upstream release
- Run test-libxc and test-mpi
- Patch for 32-bit systems

* Wed Aug 12 2020 Iñaki Úcar <iucar@fedoraproject.org> - 6.3.2-5
- https://fedoraproject.org/wiki/Changes/FlexiBLAS_as_BLAS/LAPACK_manager

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 6.3.2-4
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 6.3.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Mar 02 2020 Marcin Dulak <marcindulak@fedoraproject.org> - 6.3.2-2
- handle -fallow-argument-mismatch outside of f32

* Fri Jan 31 2020 Marcin Dulak <marcindulak@fedoraproject.org> - 6.3.2-1
- new upstream release

* Fri Jan 31 2020 Marcin Dulak <marcindulak@fedoraproject.org> - 5.2.14-4
- fix gfortran 10 -fallow-argument-mismatch

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 5.2.14-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 5.2.14-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri May 17 2019 Marcin Dulak <marcindulak@fedoraproject.org> - 5.2.14-1
- new upstream release
- stop maintenance on epel6/epel7 since libxc 3 or newer is required by elk-5.2.14

* Thu Feb 14 2019 Orion Poplawski <orion@nwra.com> - 4.3.6-31
- Rebuild for openmpi 3.1.3

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 4.3.6-30
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 4.3.6-29
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Sat Apr 07 2018 Marcin Dulak <marcindulak@fedoraproject.org> - 4.3.6-28
- keep both libxc 3 and 4 patches, since the repo is synced to older fedora and epel

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 4.3.6-27
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Mon Oct 23 2017 Susi Lehtola <susi.lehtola@iki.fi> - 4.3.6-26
- Rebuild against libxc 4.

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 4.3.6-25
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 4.3.6-24
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Wed Mar 29 2017 Marcin Dulak <marcindulak@fedoraproject.org> - 4.3.6-23
- upstream update

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 4.0.15-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri Oct 21 2016 Orion Poplawski <orion@cora.nwra.com> - 4.0.15-22
- Rebuild for openmpi 2.0

* Tue Aug 09 2016 Marcin Dulak <marcindulak@fedoraproject.org> - 4.0.15-21
- upstream update
- remove defattr
- run all tests
- speedup test by running on single core
- libxc 3 on fedora >= 25

* Thu Jul 14 2016 Peter Robinson <pbrobinson@fedoraproject.org> 3.3.17-20
- openblas supported on Power64

* Wed Jul 13 2016 Peter Robinson <pbrobinson@fedoraproject.org> 3.3.17-19
- openblas supported on aarch64

* Thu Apr 21 2016 Susi Lehtola <jussilehtola@fedoraproject.org> - 3.3.17-18
- Rebuild against libxc 3.0.0.

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 3.3.17-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Jan 22 2016 Marcin Dulak <marcindulak@fedoraproject.org> - 3.3.17-16
- upstream update
- ExclusiveArch due to openblas
- old el6 mpich macros removed

* Tue Sep 15 2015 Orion Poplawski <orion@cora.nwra.com> - 3.1.12-15
- Rebuild for openmpi 1.10.0

* Sat Aug 15 2015 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 3.1.12-14
- Rebuild for MPI provides

* Sun Jul 26 2015 Sandro Mani <manisandro@gmail.com> - 3.1.12-13
- Rebuild for RPM MPI Requires Provides Change

* Thu Jul  2 2015 Marcin Dulak <marcindulak@fedoraproject.org> - 3.1.12-12
- upstream update
- defattr set

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.0.18-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Fri Apr 24 2015 Marcin Dulak <marcindulak@fedoraproject.org> - 3.0.18-10
- upstream update

* Fri Feb 13 2015 Marcin Dulak <marcindulak@fedoraproject.org> - 3.0.4-10
- upstream update

* Thu Oct 23 2014 Marcin Dulak <marcindulak@fedoraproject.org> - 2.3.22-10
- mpich version 3 on EL6

* Tue Oct 07 2014 Marcin Dulak <marcindulak@fedoraproject.org> - 2.3.22-9
- build against new openmpi

* Sat Aug 16 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.3.22-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Marcin Dulak <marcindulak@fedoraproject.org> - 2.3.22-7
- upstream update
- fix mpi build
- tests/test-018 hangs - disabled

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.3.16-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Tue Apr 22 2014 Marcin Dulak <marcindulak@fedoraproject.org> - 2.3.16-5
- upstream update

* Tue Mar 18 2014 Björn Esser <bjoern.esser@gmail.com> - 2.2.10-4
- rebuilt for mpich-3.1

* Tue Feb 18 2014 Marcin Dulak <marcindulak@fedoraproject.org> 2.2.10-3
- removed bundling of BLAS, LAPACK, FFTW, LIBXC, ERF
- test on 2 cores to reduce randomness in koji multicore builds

* Fri Feb 7 2014 Marcin Dulak <marcindulak@fedoraproject.org> 2.2.10-2
- update for Fedora/EPEL

* Fri Jun 12 2009 Marcin Dulak <marcindulak@fedoraproject.org> 0.9.262-1
- initial build
