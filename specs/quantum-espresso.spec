# Warning:
# Anyone editing this spec file please make sure the same spec file
# works on other fedora and epel releases, which are supported by this software.
# No quick Rawhide-only fixes will be allowed.

%if 0%{?el6}
gfortran < 4.9 unsupported https://gitlab.com/QEF/q-e/issues/113
%quit
%endif

%if 0%{?el7}
# Error: Assumed-shape array 'zvec' at (1) cannot be an argument to the procedure 'c_loc' because it is not C interoperable
gfortran < 4.9 unsupported https://lists.quantum-espresso.org/pipermail/users/2020-November/046420.html
%quit
%endif

%if 0%{?fedora} >= 32 || 0%{?rhel} >= 9
# -fallow-argument-mismatch is a workaround to compile UtilXlib/mp.f90
# "Type mismatch between actual argument at (1) and actual argument at (2)"
# Use -fno-lto on f36 gfortran-12 https://gitlab.com/QEF/q-e/-/issues/460
%global extra_gfortran_flags -fallow-argument-mismatch -fno-lto
%else
%global extra_gfortran_flags %{nil}
%endif

%if 0%{?fedora} || 0%{?rhel} >= 8
%global python python3
%else
%global python python
%endif

%if 0%{?fedora} >= 33 || 0%{?rhel} >= 9
%global blaslib flexiblas
%else
%global blaslib openblas
%endif

# devxlib compilation fails on armv7hl
# configure: error: cannot guess build type; you must specify one
ExclusiveArch:		x86_64 aarch64 %{power64}

# disable compilation warnings
%global wnoflags -Wno-unused-variable -Wno-conversion -Wno-unused-dummy-argument -Wno-character-truncation -Wno-missing-include-dirs -Wno-unused-function -Wno-maybe-unitialized

Name:			quantum-espresso
Version:		7.0
Release:		13%{?dist}
Summary:		A suite for electronic-structure calculations and materials modeling

# See bundling discussion in https://gitlab.com/QEF/q-e/-/issues/366
Provides:               bundled(FoXlibf)
Provides:               bundled(deviceXlib)
Provides:               bundled(libmbd)

# Automatically converted from old format: GPLv2+ - review is highly recommended.
License:		GPL-2.0-or-later
# BSD: PP/src/bgw2pw.f90
# BSD: PP/src/pw2bgw.f90
# LGPLv2+: Modules/bspline.f90
# MIT: install/install-sh
# zlib/libpng: clib/md5.c
# zlib/libpng: clib/md5.h
URL:			http://www.quantum-espresso.org/
Source0:		https://github.com/QEF/q-e/archive/refs/tags/qe-%{version}.tar.gz

# pseudopotentials not included in the source and needed by PW/tests
# cd test-suite && make pseudo
Source1:		pseudo.tar.gz

# Bundle gitlab.com/max-centre/components/devicexlib
Source2:		devicexlib-a6b89ef77b1ceda48e967921f1f5488d2df9226d.tar.gz

# handle license on el{6,7}: global must be defined after the License field above
%{!?_licensedir: %global license %doc}

BuildRequires:		make
%if 0%{?fedora} || 0%{?rhel} >= 8
BuildRequires:		python3
BuildRequires:		python3-numpy
%else
BuildRequires:		python
BuildRequires:		numpy
%endif
BuildRequires:		gcc-gfortran
BuildRequires:		%{blaslib}-devel
# Use openblas-serial instead of openblas-openmp
%if 0%{?fedora} >= 33 || 0%{?rhel} >= 9
BuildRequires:		flexiblas-openblas-serial
Requires:		flexiblas-openblas-serial
%endif
BuildRequires:		fftw3-devel

BuildRequires:		openssh-clients
BuildRequires:		which

Requires:		openssh-clients

%global desc_base \
QUANTUM ESPRESSO is an integrated suite of Open-Source computer codes for\
electronic-structure calculations and materials modeling at the nanoscale.\
It is based on density-functional theory, plane waves, and pseudopotentials.


%description
%{desc_base}

Serial version.


%package openmpi
Summary:		%{name} - openmpi version
BuildRequires:		openmpi-devel
BuildRequires:		scalapack-openmpi-devel
Requires:		openmpi
%if 0%{?el7}
Requires:		scalapack-openmpi
Requires:		blacs-openmpi
%endif

%description openmpi
%{desc_base}

This package contains the openmpi version.


%package mpich
Summary:		%{name} - mpich version
BuildRequires:		mpich-devel
BuildRequires:		scalapack-mpich-devel
Requires:		mpich
%if 0%{?el7}
Requires:		scalapack-mpich
Requires:		blacs-mpich
%endif

%description mpich
%{desc_base}

This package contains the mpich version.


%prep
%setup -q -n q-e-qe-%{version}

# bundle gitlab.com/max-centre/components/devicexlib
cp -p %{SOURCE2} external/devxlib/devxlib.tar.gz
sed -i 's|wget $(DEVXLIB_URL) -O devxlib.tar.gz|ls devxlib.tar.gz|' install/extlibs_makefile

# remove bundled libraries
rm -rf archive/lapack*gz
rm -rf archive/blas*gz
rm -rf archive/ELPA*gz

# -D__FFTW must be specified https://bugs.debian.org/cgi-bin/bugreport.cgi?bug=980677
# Error: Symbol 'cft_2xy' at (1) has no IMPLICIT type
sed -i 's|MANUAL_DFLAGS  =|MANUAL_DFLAGS  = -D__FFTW %{extra_gfortran_flags}|' install/make.inc.in

# Allow for passing FOXFLAGS to external utils like fox or devicexlib
# relocation R_X86_64_32 against `.rodata' can not be used when making a PIE object; recompile with -fPIE
# Cannot compile fox without optimization due to
# #warning _FORTIFY_SOURCE requires compiling with optimization (-O)
# /usr/bin/ld: /tmp/ccy03rFL.ltrans0.ltrans.o:/builddir/build/BUILD/q-e-qe-7.0/PW/src/../../UtilXlib/fletcher32_mod.f90:216:
# more undefined references to `fletcher32' follow collect2: error: ld returned 1 exit status
sed -i 's|FOX_FLAGS = @foxflags@|FOX_FLAGS = $(FOXFLAGS)|' install/make.inc.in

# Horror! Tests use $HOME/tmp or /tmp by default!
sed -i 's#TMP_DIR=.*#TMP_DIR=./tmp#' environment_variables
sed -i 's#ESPRESSO_TMPDIR=.*#ESPRESSO_TMPDIR=./tmp#' test-suite/ENVIRONMENT
# NO network access during build!
sed -i 's#NETWORK_PSEUDO=.*#NETWORK_PSEUDO=/dev/null#' environment_variables
sed -i 's#NETWORK_PSEUDO=.*#NETWORK_PSEUDO=/dev/null#' test-suite/ENVIRONMENT
# must set ESPRESSO_ROOT explicitly
sed -i "s#ESPRESSO_ROOT=.*#ESPRESSO_ROOT=${PWD}#" test-suite/ENVIRONMENT
# set TESTCODE_NPROCS
sed -i "s#TESTCODE_NPROCS=.*#TESTCODE_NPROCS=2#" test-suite/ENVIRONMENT
# increase test verbosity
sed -i "s#--verbose#-vvv#" test-suite/Makefile
# bash uses source and not include
sed -i "s#include #source #" test-suite/run-cp.sh
sed -i "s#include #source #" test-suite/run-pw.sh
# don't use python2
sed -i "s#python2#%{python}#" test-suite/testcode/bin/testcode.py
# Fix ModuleNotFoundError: No module named 'testcode2' https://bugzilla.redhat.com/show_bug.cgi?id=2301229
sed -i "s#pipes#shlex#" test-suite/testcode/lib/testcode2/__init__.py

# remove -D__XLF on ppc64
# http://qe-forge.org/pipermail/pw_forum/2009-January/085834.html
sed -i '/D__XLF/d' install/configure
# remove -D__LINUX_ESSL on ppc64
sed -i 's/try_dflags -D__LINUX_ESSL/try_dflags/' install/configure
sed -i 's/have_essl=1/have_essl=0/' install/configure


%build
# Have to do off-root builds to be able to build many versions at once
mv install install.orig

# To avoid replicated code define a macro
%global dobuild() \
mkdir -p bin$MPI_SUFFIX&& \
if [ "$MPI_SUFFIX" == "_serial" ]; then FORTRAN='gfortran'; CONFIGURE='--disable-parallel'; fi&& \
if [ "$MPI_SUFFIX" != "_serial" ]; then FORTRAN='mpif90'; CONFIGURE='--enable-parallel --with-scalapack=yes'; fi&& \
if [ "$MPI_SUFFIX" == "_openmpi" ] && [ -r "$MPI_LIB/libmpi_f90.so" ]; then export LIBMPI='-lmpi -lmpi_f90 -lmpi_f77'; fi&& \
if [ "$MPI_SUFFIX" == "_openmpi" ] && [ -r "$MPI_LIB/libmpi_usempi.so" ]; then export LIBMPI='-lmpi -lmpi_usempi -lmpi_mpifh'; fi&& \
if [ "$MPI_SUFFIX" == "_openmpi" ] && [ -r "$MPI_LIB/libmpi_usempif08.so" ]; then export LIBMPI='-lmpi -lmpi_usempif08 -lmpi_mpifh'; fi&& \
if [ "$MPI_SUFFIX" == "_mpich2" ]; then export LIBMPI='-lmpich'; fi&& \
if [ "$MPI_SUFFIX" == "_mpich" ]; then export LIBMPI='-lmpich'; fi&& \
    export CC=gcc &&\
    export CXX=c++ &&\
    export F90="${FORTRAN}" &&\
    export MPIF90="${FORTRAN}" &&\
    export FCFLAGS='%{optflags} %{extra_gfortran_flags}' &&\
    export CFLAGS='%{optflags} %{wnoflags} %{extra_gfortran_flags}' &&\
    export FFLAGS='%{optflags} %{extra_gfortran_flags}' &&\
    export FOXFLAGS='%{optflags} %{extra_gfortran_flags} -fPIE -x f95-cpp-input' &&\
    export BLAS_LIBS='-l%{blaslib}' &&\
    export LAPACK_LIBS='-l%{blaslib}' &&\
    export FFT_LIBS='-lfftw3' &&\
    export MPI_LIBS="-L${MPI_LIB} $LIBMPI" &&\
    export SCALAPACK_LIBS="-L${MPI_LIB} -lscalapack" &&\
    %{_configure} $CONFIGURE && \
%{__make} all&& \
for f in bin/*; do BASENAME=$(basename ${f}); cp -pL $f bin$MPI_SUFFIX/${BASENAME}; done&& \
if test -d upftools; then for f in upftools/*.x; do BASENAME=$(basename ${f}); cp -pL $f bin$MPI_SUFFIX/${BASENAME}; done; fi&& \
%{__make} clean


# build openmpi version
cp -rp install.orig install
%{_openmpi_load}
%dobuild
%{_openmpi_unload}
rm -rf install

# build mpich version
cp -rp install.orig install
%{_mpich_load}
%dobuild
%{_mpich_unload}
rm -rf install

# build serial version
cp -rp install.orig install
MPI_SUFFIX=_serial %dobuild


%install

# To avoid replicated code define a macro
%global doinstall() \
mkdir -p $RPM_BUILD_ROOT/$MPI_BIN&& \
mkdir -p $RPM_BUILD_ROOT/$MPI_LIB&& \
mkdir -p $RPM_BUILD_ROOT/$MPI_FORTRAN_MOD_DIR&& \
for f in bin$MPI_SUFFIX/*; do \
BASENAME=$(basename ${f})&& \
install -p -m 755 ${f} $RPM_BUILD_ROOT/$MPI_BIN/${BASENAME}_binary${EXE_SUFFIX}&& \
echo '#!/bin/bash' > $RPM_BUILD_ROOT/$MPI_BIN/${BASENAME}${EXE_SUFFIX}&& \
echo 'export FLEXIBLAS=openblas-serial' >> $RPM_BUILD_ROOT/$MPI_BIN/${BASENAME}${EXE_SUFFIX}&& \
echo -n "${BASENAME}_binary${EXE_SUFFIX} " >> $RPM_BUILD_ROOT/$MPI_BIN/${BASENAME}${EXE_SUFFIX}&& \
echo '"$@"' >> $RPM_BUILD_ROOT/$MPI_BIN/${BASENAME}${EXE_SUFFIX}&& \
chmod 755 $RPM_BUILD_ROOT/$MPI_BIN/${BASENAME}${EXE_SUFFIX}; done&& \
ls -al $RPM_BUILD_ROOT/$MPI_BIN

# install openmpi version
%{_openmpi_load}
EXE_SUFFIX=$MPI_SUFFIX %doinstall
%{_openmpi_unload}

# install mpich version
%{_mpich_load}
EXE_SUFFIX=$MPI_SUFFIX %doinstall
%{_mpich_unload}

# install serial version
EXE_SUFFIX="" MPI_SUFFIX="_serial" MPI_BIN=%{_bindir} MPI_LIB=%{_libdir} MPI_FORTRAN_MOD_DIR=%{_fmoddir} %doinstall


%check

# clean removes all extra pseudo - must copy them now
tar zxf %{SOURCE1}

%if 0%{?el6}
export TIMEOUT_OPTS='3600'
%else
export TIMEOUT_OPTS='--preserve-status --kill-after 10 3600'
%endif

# To avoid replicated code define a macro
%global docheck() \
export FLEXIBLAS=openblas-serial&& \
ldd bin$MPI_SUFFIX/pw.x && \
cp -rp test-suite.orig test-suite&& \
pushd test-suite&& \
for script in run-*.sh; do \
sed -i "s<}/bin/<}/bin$MPI_SUFFIX/<" ${script}&& \
sed -i "s<}/PW/src/<}/bin$MPI_SUFFIX/<" ${script}; \
done&& \
if [ $MPI_SUFFIX == _serial ]; then \
timeout ${TIMEOUT_OPTS} %{__make} run-tests-serial 2>&1 | tee ../tests$MPI_SUFFIX.log \
else \
timeout ${TIMEOUT_OPTS} %{__make} run-tests-parallel 2>&1 | tee ../tests$MPI_SUFFIX.log \
fi&& \
popd&& \
cat test-suite/pw_atom/test* && \
rm -rf test-suite

mv test-suite test-suite.orig

# check serial version
MPI_SUFFIX=_serial %docheck

# check openmpi version
%{_openmpi_load}
which mpirun
%docheck
%{_openmpi_unload}

# check mpich version
%{_mpich_load}
which mpirun
%docheck
%{_mpich_unload}

# restore tests
mv test-suite.orig test-suite


%files
%license License
%{_bindir}/*.x_binary
%{_bindir}/*.x


%files openmpi
%license License
%{_libdir}/openmpi%{?_opt_cc_suffix}/bin/*.x_binary_openmpi
%{_libdir}/openmpi%{?_opt_cc_suffix}/bin/*.x_openmpi


%files mpich
%license License
%{_libdir}/mpich%{?_opt_cc_suffix}/bin/*.x_binary_mpich
%{_libdir}/mpich%{?_opt_cc_suffix}/bin/*.x_mpich


%changelog
* Sat Jan 18 2025 Fedora Release Engineering <releng@fedoraproject.org> - 7.0-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Fri Aug 02 2024 Marcin Dulak <marcindulak@fedoraproject.org> - 7.0-12
- Fix python ModuleNotFoundError testcode2 import bug #2301229

* Fri Jul 26 2024 Miroslav Suchý <msuchy@redhat.com> - 7.0-11
- convert license to SPDX

* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 7.0-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Tue Jan 30 2024 Marcin Dulak <marcindulak@fedoraproject.org> - 7.0-9
- Remove support for i686 due to openmpi removal

* Fri Jan 26 2024 Fedora Release Engineering <releng@fedoraproject.org> - 7.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 7.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 7.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 7.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 7.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Sun Jan 30 2022 Marcin Dulak <marcindulak@fedoraproject.org> - 7.0-3
- Fix "relocation R_X86_64_32 against .rodata" by passing -fPIE to FOXFLAGS
- Workaround for segmentation fault with gfortran-12 -fno-lto, bug #2046933

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 7.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Dec 24 2021 Marcin Dulak <marcindulak@fedoraproject.org> - 7.0-1
- New upstream release

* Fri Aug 06 2021 Marcin Dulak <marcindulak@fedoraproject.org> - 6.8-1
- New upstream release
- Change changelog email
- Bundle gitlab.com/max-centre/components/devicexlib
- Remove no longer needed DEXX
- Remove no longer needed iotk
- Remove missing --with-elpa=no
- Export environment variables before configure
- Disable epel7 due to unsupported gfortran < 4.9
- export FLEXIBLAS=openblas-serial using a wrapper
- Remove empty devel and static packages

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 6.5-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Fri Aug 28 2020 Iñaki Úcar <iucar@fedoraproject.org> - 6.5-4
- https://fedoraproject.org/wiki/Changes/FlexiBLAS_as_BLAS/LAPACK_manager

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 6.5-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Mar 02 2020 Marcin Dulak <marcindulak@fedoraproject.org> - 6.5-2
- python and numpy br for epel8

* Fri Feb 14 2020 Marcin Dulak <marcindulak@fedoraproject.org> - 6.5-1
- new upstream release
- -fallow-argument-mismatch fix for gfortran 10
- fix serial and parallel test-suite build (use 1 and 2 processors respectively)

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 6.4.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 6.4.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri May 17 2019 Marcin Dulak <marcindulak@fedoraproject.org> - 6.4.1-1
- new upstream release
- kill hanging tests after timeout
- disable failed architectures: configure fails to find openblas, fftw on other %%{openblas_arches} than x86_64 %%{ix86}

* Thu Feb 14 2019 Orion Poplawski <orion@nwra.com> - 5.4.0-20
- Rebuild for openmpi 3.1.3

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 5.4.0-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 5.4.0-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed May 02 2018 Iryna Shcherbina <shcherbina.iryna@gmail.com> - 5.4.0-17
- Update Python 2 dependency declarations to new packaging standards
  (See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3)

* Wed Mar 07 2018 Adam Williamson <awilliam@redhat.com> - 5.4.0-16
- Rebuild to fix GCC 8 mis-compilation
  See https://da.gd/YJVwk ("GCC 8 ABI change on x86_64")

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 5.4.0-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 5.4.0-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 5.4.0-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 5.4.0-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri Oct 21 2016 Orion Poplawski <orion@cora.nwra.com> - 5.4.0-11
- Rebuild for openmpi 2.0

* Fri Sep 16 2016 Marcin Dulak <marcindulak@fedoraproject.org> - 5.4.0-10
- upsteam update
- speedup the tests by running on single core so koji %%{arm} builds finish within the timeout (bug #1356620)
- get rid of D__XLF and D__LINUX_ESSL on ppc64

* Tue Sep  6 2016 Peter Robinson <pbrobinson@fedoraproject.org> 5.3.0-9
- Sync openblas ExclusiveArch

* Thu Feb 18 2016 Marcin Dulak <marcindulak@fedoraproject.org> - 5.3.0-8
- use only 2 cores for tests (bug #1308481)
- defattr removed

* Sat Feb 13 2016 Marcin Dulak <marcindulak@fedoraproject.org> - 5.3.0-7
- explicit Requires are needed for scalapack, blacs on el6 (bug #1301922)
    
* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 5.3.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Tue Jan 12 2016 Marcin Dulak <marcindulak@fedoraproject.org> 5.3.0-5
- upsteam update
- switch to test-suite
- no more upftools?

* Mon Jan  4 2016 Marcin Dulak <marcindulak@fedoraproject.org> 5.2.1-4
- disable compilation warnings
- use lua for copying pseudos
- removed common package

* Sat Dec 19 2015 Marcin Dulak <marcindulak@fedoraproject.org> 5.2.1-3
- fix ExclusiveArch
- license is GPLv2+
- OMP_NUM_THREADS removed
- use %%{optflags}

* Fri Dec 18 2015 Dave Love <loveshack@fedoraproject.org> - 5.2.1-2
- Require %%{name}-common, not %%{name}-common%%{?_isa}

* Wed Dec 16 2015 Marcin Dulak <marcindulak@fedoraproject.org> 5.1.2-1
- initial build

