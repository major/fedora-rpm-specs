## Debug builds?
%bcond_with debug
#

# Enable pthread support
%bcond_with pthread
#

%define _legacy_common_support 1
%define _lto_cflags %{nil}

%global with_mpich 1
%global with_openmpi 1

%if 0%{?rhel} && 0%{?rhel} == 7
%global with_openmpi 1
%global with_mpich 1

# Use devtoolset 6
%global dts devtoolset-6-
%endif

## BLAS ##
%if 0%{?fedora} || 0%{?rhel} >= 9
%global blaslib flexiblas
%global blasvar %{nil}
%else
%global blaslib openblas
%global blasvar o
%endif
###########

## Hypre ##
## Due to rhbz#1744780
%if 0%{?rhel} && 0%{?rhel} > 7
%global with_hypre 1
%global with_openmpicheck 0
%global with_mpichcheck 0
%endif
%if 0%{?fedora} || 0%{?rhel} >= 7
%global with_hypre 1
%ifnarch s390x
%global with_openmpicheck 0
%global with_mpichcheck 1
%endif
%endif
###########
%global with_sercheck 1

## PETSc ##
%global with_petsc 1
###########

## SuperLUMT ##
%global with_superlumt 0
###########

## superlu_dist is not compiled with index_size64 enabled ##
%global with_superludist 0
###########

## Fortran ##
%if %{?__isa_bits:%{__isa_bits}}%{!?__isa_bits:32} == 64
%global with_fortran 1
%else
%global with_fortran 0
%endif
#############

Summary:    Suite of nonlinear solvers
Name:       sundials
Version:    5.8.0
Release:    7%{?dist}
# SUNDIALS is licensed under BSD with some additional (but unrestrictive) clauses.
# Check the file 'LICENSE' for details.
License:    BSD
URL:        https://computation.llnl.gov/projects/%{name}/
Source0:    https://github.com/LLNL/%{name}/archive/v%{version}/%{name}-%{version}.tar.gz

# This patch rename superLUMT library
Patch0:     %{name}-5.5.0-set_superlumt_name.patch

# This patch rename superLUMT64 library
Patch1:     %{name}-5.5.0-set_superlumt64_name.patch

Patch2:     %{name}-change_petsc_variable.patch

BuildRequires: make
%if 0%{?with_fortran}
BuildRequires: gcc-gfortran
%endif
BuildRequires: python%{python3_pkgversion}-devel
BuildRequires: %{?dts}gcc, %{?dts}gcc-c++
%if 0%{?epel}
BuildRequires: epel-rpm-macros
%endif
BuildRequires: cmake3 >= 3.10
BuildRequires: %{blaslib}-devel
%if 0%{?with_superlumt}
%ifarch s390x x86_64 %{power64} aarch64
BuildRequires: SuperLUMT64-devel
%endif
%ifarch %{arm} %{ix86}
BuildRequires: SuperLUMT-devel
%endif
%endif

# KLU support
%if 0%{?fedora} || 0%{?rhel} >= 9
%ifarch s390x x86_64 %{power64} aarch64
BuildRequires: suitesparse64-devel
%endif
%ifarch %{arm} %{ix86}
BuildRequires: suitesparse-devel
%endif
%endif

%if 0%{?rhel} == 8
BuildRequires: suitesparse-devel
%endif

%if 0%{?rhel}
BuildRequires: rsh
%endif
%if 0%{?with_fortran}
Requires: gcc-gfortran%{?_isa}
%endif

%description
SUNDIALS is a SUite of Non-linear DIfferential/ALgebraic equation Solvers
for use in writing mathematical software.

SUNDIALS was implemented with the goal of providing robust time integrators
and nonlinear solvers that can easily be incorporated into existing simulation
codes. The primary design goals were to require minimal information from the
user, allow users to easily supply their own data structures underneath the
solvers, and allow for easy incorporation of user-supplied linear solvers and
preconditioners. 

%package devel
Summary:    Suite of nonlinear solvers (developer files)
Requires:   %{name}%{?_isa} = %{version}-%{release}
Provides:   %{name}-fortran-static = %{version}-%{release}
%description devel
SUNDIALS is a SUite of Non-linear DIfferential/ALgebraic equation Solvers
for use in writing mathematical software.
This package contains the developer files (.so file, header files).
#############################################################################
#########
%if 0%{?with_openmpi}
%package openmpi
Summary:    Suite of nonlinear solvers
BuildRequires: openmpi-devel
BuildRequires: hypre-openmpi-devel
%if 0%{?with_petsc}
BuildRequires: petsc-openmpi-devel >= 3.10
BuildRequires: scalapack-openmpi-devel
BuildRequires: hdf5-openmpi-devel
%endif
%if 0%{?with_superludist}
BuildRequires: superlu_dist-openmpi-devel
%endif

Requires: openmpi%{?_isa}
%if 0%{?with_fortran}
Requires: gcc-gfortran%{?_isa}
%endif

%description openmpi
SUNDIALS is a SUite of Non-linear DIfferential/ALgebraic equation Solvers
for use in writing mathematical software.
This package contains the Sundials Fortran parallel OpenMPI libraries.

%package openmpi-devel
Summary:    Suite of nonlinear solvers
Requires:   %{name}-openmpi%{?_isa} = %{version}-%{release}
Provides:   %{name}-openmpi-fortran-static = %{version}-%{release}
%description openmpi-devel
SUNDIALS is a SUite of Non-linear DIfferential/ALgebraic equation Solvers
for use in writing mathematical software.
This package contains the Sundials parallel OpenMPI devel libraries and
header files.
%endif
######
###############################################################################
######
%if 0%{?with_mpich}
%package mpich
Summary:    Suite of nonlinear solvers
BuildRequires: mpich-devel
BuildRequires: hypre-mpich-devel
%if 0%{?with_petsc}
BuildRequires: petsc-mpich-devel >= 3.10
BuildRequires: scalapack-mpich-devel
BuildRequires: hdf5-mpich-devel
%endif
%if 0%{?with_superludist}
BuildRequires: superlu_dist-mpich-devel
%endif

Requires: mpich%{?_isa}
%if 0%{?with_fortran}
Requires: gcc-gfortran%{?_isa}
%endif

%description mpich
SUNDIALS is a SUite of Non-linear DIfferential/ALgebraic equation Solvers
for use in writing mathematical software.
This package contains the Sundials parallel MPICH libraries.

%package mpich-devel
Summary:    Suite of nonlinear solvers
Requires:   %{name}-mpich%{?_isa} = %{version}-%{release}
Provides:   %{name}-mpich-fortran-static = %{version}-%{release}
%description mpich-devel
SUNDIALS is a SUite of Non-linear DIfferential/ALgebraic equation Solvers
for use in writing mathematical software.
This package contains the Sundials parallel MPICH devel libraries and
header files.
%endif
######
#############################################################################

%package doc
Summary:    Suite of nonlinear solvers (documentation)
BuildArch: noarch
%description doc
SUNDIALS is a SUite of Non-linear DIfferential/ALgebraic equation Solvers
for use in writing mathematical software.
This package contains the documentation files.

%prep
%setup -qc

pushd %{name}-%{version}

%ifarch s390x x86_64 %{power64} aarch64
%patch1 -p0 -b .set_superlumt64_name
%endif
%ifarch %{arm} %{ix86}
%patch0 -p0 -b .set_superlumt_name
%endif

mv src/arkode/README.md src/README-arkode.md
mv src/cvode/README.md src/README-cvode.md
mv src/cvodes/README.md src/README-cvodes.md
mv src/ida/README.md src/README-ida.md
mv src/idas/README.md src/README.idas.md
mv src/kinsol/README.md src/README-kinsol.md
popd

%if 0%{?with_openmpi}
cp -a sundials-%{version} buildopenmpi_dir
%endif
%if 0%{?with_mpich}
cp -a sundials-%{version} buildmpich_dir
%endif

%build
mkdir -p sundials-%{version}/build

export LIBBLASLINK=-l%{blaslib}%{blasvar}
export INCBLAS=%{_includedir}/%{blaslib}

%if 0%{?with_superlumt}
%ifarch s390x x86_64 %{power64} aarch64
export LIBSUPERLUMTLINK=-lsuperlumt64_d
%endif
%ifarch %{arm} %{ix86}
export LIBSUPERLUMTLINK=-lsuperlumt_d
%endif
%endif

%if 0%{?el7}
%{?dts:source /opt/rh/devtoolset-6/enable}
%endif

%if %{with debug}
%undefine _hardened_build
export CFLAGS=" "
export FFLAGS=" "
%global _cmake cmake3
%_cmake -B sundials-%{version}/build -S sundials-%{version} \
 -DCMAKE_VERBOSE_MAKEFILE:BOOL=ON \
 -DCMAKE_BUILD_TYPE:STRING=Debug \
 -DCMAKE_C_FLAGS_DEBUG:STRING="-O0 -g %{__global_ldflags} -I$INCBLAS" \
 -DCMAKE_Fortran_FLAGS_DEBUG:STRING="-O0 -g %{__global_ldflags} -I$INCBLAS" \
 -DCMAKE_SHARED_LINKER_FLAGS_DEBUG:STRING="%{__global_ldflags} $LIBBLASLINK $LIBSUPERLUMTLINK" \
%else
export CFLAGS="%{build_cflags}"
export CFLAGS="%{build_fflags}"
%cmake3 -B sundials-%{version}/build -S sundials-%{version} \
%endif
%if 0%{?fedora} || 0%{?rhel} >= 9
%if %{?__isa_bits:%{__isa_bits}}%{!?__isa_bits:32} == 64
 -DSUNDIALS_INDEX_SIZE:STRING=64 \
 -DKLU_ENABLE=ON -DKLU_LIBRARY_DIR:PATH=%{_libdir} -DKLU_LIBRARY=%{_libdir}/libklu64.so \
 -DAMD_LIBRARY=%{_libdir}/libamd64.so -DAMD_LIBRARY_DIR:PATH=%{_libdir} \
 -DBTF_LIBRARY=%{_libdir}/libbtf64.so -DBTF_LIBRARY_DIR:PATH=%{_libdir} \
 -DCOLAMD_LIBRARY=%{_libdir}/libcolamd64.so -DCOLAMD_LIBRARY_DIR:PATH=%{_libdir} \
%else
 -DSUNDIALS_INDEX_SIZE:STRING=32 \
 -DKLU_ENABLE=ON -DKLU_LIBRARY_DIR:PATH=%{_libdir} -DKLU_LIBRARY=%{_libdir}/libklu.so \
 -DAMD_LIBRARY=%{_libdir}/libamd.so -DAMD_LIBRARY_DIR:PATH=%{_libdir} \
 -DBTF_LIBRARY=%{_libdir}/libbtf.so -DBTF_LIBRARY_DIR:PATH=%{_libdir} \
 -DCOLAMD_LIBRARY=%{_libdir}/libcolamd.so -DCOLAMD_LIBRARY_DIR:PATH=%{_libdir} \
%endif
%endif
%if 0%{?rhel} == 8
 -DKLU_ENABLE=ON -DKLU_LIBRARY_DIR:PATH=%{_libdir} -DKLU_LIBRARY=%{_libdir}/libklu.so \
 -DAMD_LIBRARY=%{_libdir}/libamd.so -DAMD_LIBRARY_DIR:PATH=%{_libdir} \
 -DBTF_LIBRARY=%{_libdir}/libbtf.so -DBTF_LIBRARY_DIR:PATH=%{_libdir} \
 -DCOLAMD_LIBRARY=%{_libdir}/libcolamd.so -DCOLAMD_LIBRARY_DIR:PATH=%{_libdir} \
%endif
 -DKLU_INCLUDE_DIR:PATH=%{_includedir}/suitesparse \
 -DCMAKE_VERBOSE_MAKEFILE:BOOL=ON \
 -DCMAKE_BUILD_TYPE:STRING=Release \
 -DCMAKE_C_FLAGS_RELEASE:STRING="%{optflags} -I$INCBLAS" \
 -DCMAKE_Fortran_FLAGS_RELEASE:STRING="%{optflags} -I$INCBLAS" \
 -DCMAKE_SHARED_LINKER_FLAGS_RELEASE:STRING="%{__global_ldflags} $LIBBLASLINK $LIBSUPERLUMTLINK" \
 -DCMAKE_INSTALL_INCLUDEDIR:PATH=%{_includedir} \
 -DLAPACK_ENABLE:BOOL=OFF \
 -DCMAKE_MODULE_LINKER_FLAGS:STRING="%{__global_ldflags}" \
 -DCMAKE_INSTALL_PREFIX:PATH=%{_prefix} -DCMAKE_INSTALL_LIBDIR:PATH=%{_lib} \
 -DPYTHON_EXECUTABLE:FILEPATH=%{__python3} \
 -DEXAMPLES_ENABLE_CXX:BOOL=ON -DEXAMPLES_ENABLE_C:BOOL=ON \
 -DCMAKE_SKIP_RPATH:BOOL=YES -DCMAKE_SKIP_INSTALL_RPATH:BOOL=YES \
 -DBUILD_SHARED_LIBS:BOOL=ON -DBUILD_STATIC_LIBS:BOOL=ON \
 -DMPI_ENABLE:BOOL=OFF \
%if 0%{?with_fortran}
 -DF77_INTERFACE_ENABLE:BOOL=ON \
 -DEXAMPLES_ENABLE_F77:BOOL=ON \
 -DF2003_INTERFACE_ENABLE:BOOL=ON \
 -DEXAMPLES_ENABLE_F90:BOOL=ON \
 -DFortran_INSTALL_MODDIR:PATH=%{_fmoddir}/%{name} \
%endif
 -DUSE_GENERIC_MATH:BOOL=ON \
 -DOPENMP_ENABLE:BOOL=ON \
%if %{with pthread}
 -DPTHREAD_ENABLE:BOOL=ON \
%endif
 -DSUNDIALS_PRECISION:STRING=double \
%if 0%{?with_superlumt}
 -DSUPERLUMT_ENABLE:BOOL=ON \
 -DSUPERLUMT_INCLUDE_DIR:PATH=%{_includedir}/SuperLUMT \
 -DSUPERLUMT_LIBRARY_DIR:PATH=%{_libdir} \
 -DSUPERLUMT_THREAD_TYPE:STRING=OpenMP \
%endif
 -DSUPERLUDIST_ENABLE:BOOL=OFF \
 -DHYPRE_ENABLE:BOOL=OFF \
 -DEXAMPLES_INSTALL:BOOL=OFF \
 -DSUNDIALS_BUILD_WITH_MONITORING:BOOL=ON -Wno-dev

%make_build V=1 -C sundials-%{version}/build

#############################################################################
#######
%if 0%{?with_openmpi}

mkdir -p buildopenmpi_dir/build
%{_openmpi_load}

## Blas
export LIBBLASLINK=-l%{blaslib}%{blasvar}
export INCBLAS=%{_includedir}/%{blaslib}
##

## SuperLUMT
%if 0%{?with_superlumt}
%ifarch s390x x86_64 %{power64} aarch64
export LIBSUPERLUMTLINK=-lsuperlumt64_d
%endif
%ifarch %{arm} %{ix86}
export LIBSUPERLUMTLINK=-lsuperlumt_d
%endif
%endif

## Hypre
%if 0%{?with_hypre}
export LIBHYPRELINK="-L$MPI_LIB -lHYPRE"
%endif
##

# Force MPI compilers
export CC=$MPI_BIN/mpicc
export CXX=$MPI_BIN/mpic++
%if 0%{?fedora}
export FC=$MPI_BIN/mpifort
%else
export FC=$MPI_BIN/mpif77
%endif
##

%if 0%{?el7}
%{?dts:source /opt/rh/devtoolset-6/enable}
%endif

%if %{with debug}
%undefine _hardened_build
export CFLAGS=" "
export FFLAGS=" "
%global _cmake cmake3
%_cmake -B buildopenmpi_dir/build -S buildopenmpi_dir \
 -DCMAKE_VERBOSE_MAKEFILE:BOOL=ON \
 -DCMAKE_BUILD_TYPE:STRING=Debug \
 -DCMAKE_C_FLAGS_DEBUG:STRING="-O0 -g %{__global_ldflags} -I$INCBLAS" \
 -DCMAKE_Fortran_FLAGS_DEBUG:STRING="-O0 -g %{__global_ldflags} -I$INCBLAS" \
 -DCMAKE_SHARED_LINKER_FLAGS_DEBUG:STRING="%{__global_ldflags} $LIBBLASLINK $LIBSUPERLUMTLINK $LIBHYPRELINK" \
%else
export CFLAGS="%{build_cflags}"
export CFLAGS="%{build_fflags}"
%cmake3 -B buildopenmpi_dir/build -S buildopenmpi_dir \
%endif
%if 0%{?fedora} || 0%{?rhel} >= 9
%if %{?__isa_bits:%{__isa_bits}}%{!?__isa_bits:32} == 64
 -DSUNDIALS_INDEX_SIZE:STRING=64 \
 -DKLU_ENABLE=ON -DKLU_LIBRARY_DIR:PATH=%{_libdir} -DKLU_LIBRARY=%{_libdir}/libklu64.so \
 -DAMD_LIBRARY=%{_libdir}/libamd64.so -DAMD_LIBRARY_DIR:PATH=%{_libdir} \
 -DBTF_LIBRARY=%{_libdir}/libbtf64.so -DBTF_LIBRARY_DIR:PATH=%{_libdir} \
 -DCOLAMD_LIBRARY=%{_libdir}/libcolamd64.so -DCOLAMD_LIBRARY_DIR:PATH=%{_libdir} \
%else
 -DSUNDIALS_INDEX_SIZE:STRING=32 \
 -DKLU_ENABLE=ON -DKLU_LIBRARY_DIR:PATH=%{_libdir} -DKLU_LIBRARY=%{_libdir}/libklu.so \
 -DAMD_LIBRARY=%{_libdir}/libamd.so -DAMD_LIBRARY_DIR:PATH=%{_libdir} \
 -DBTF_LIBRARY=%{_libdir}/libbtf.so -DBTF_LIBRARY_DIR:PATH=%{_libdir} \
 -DCOLAMD_LIBRARY=%{_libdir}/libcolamd.so -DCOLAMD_LIBRARY_DIR:PATH=%{_libdir} \
%endif
%endif
%if 0%{?rhel} == 8
 -DKLU_ENABLE=ON -DKLU_LIBRARY_DIR:PATH=%{_libdir} -DKLU_LIBRARY=%{_libdir}/libklu.so \
 -DAMD_LIBRARY=%{_libdir}/libamd.so -DAMD_LIBRARY_DIR:PATH=%{_libdir} \
 -DBTF_LIBRARY=%{_libdir}/libbtf.so -DBTF_LIBRARY_DIR:PATH=%{_libdir} \
 -DCOLAMD_LIBRARY=%{_libdir}/libcolamd.so -DCOLAMD_LIBRARY_DIR:PATH=%{_libdir} \
%endif
 -DKLU_INCLUDE_DIR:PATH=%{_includedir}/suitesparse \
 -DCMAKE_VERBOSE_MAKEFILE:BOOL=ON \
 -DCMAKE_BUILD_TYPE:STRING=Release \
 -DCMAKE_C_FLAGS_RELEASE:STRING="%{optflags} -I$INCBLAS" \
 -DCMAKE_Fortran_FLAGS_RELEASE:STRING="%{optflags} -I$INCBLAS" \
 -DCMAKE_SHARED_LINKER_FLAGS_RELEASE:STRING="%{__global_ldflags} $LIBBLASLINK $LIBSUPERLUMTLINK $LIBHYPRELINK" \
 -DMPI_INCLUDE_PATH:PATH=$MPI_INCLUDE \
 -DCMAKE_INSTALL_INCLUDEDIR:PATH=$MPI_INCLUDE \
 -DLAPACK_ENABLE:BOOL=OFF \
%if 0%{?with_petsc}
 -DPETSC_ENABLE:BOOL=ON \
 -DPETSC_INCLUDES:PATH=$MPI_INCLUDE/petsc \
 -DPETSC_LIBRARIES:PATH=$MPI_LIB/libpetsc.so \
 -DPETSC_EXECUTABLE_RUNS=YES \
%endif
 -DCMAKE_INSTALL_PREFIX:PATH=%{_prefix} -DCMAKE_INSTALL_LIBDIR:PATH=%{_lib}/openmpi/lib \
 -DPYTHON_EXECUTABLE:FILEPATH=%{__python3} \
 -DEXAMPLES_ENABLE_CXX:BOOL=ON -DEXAMPLES_ENABLE_C:BOOL=ON \
 -DBUILD_SHARED_LIBS:BOOL=ON -DBUILD_STATIC_LIBS:BOOL=ON \
 -DCMAKE_SKIP_RPATH:BOOL=YES -DCMAKE_SKIP_INSTALL_RPATH:BOOL=YES \
 -DMPI_ENABLE:BOOL=ON \
%if 0%{?with_fortran}
%if 0%{?fedora}
 -DMPI_Fortran_COMPILER:STRING=$MPI_BIN/mpifort \
%else
 -DMPI_Fortran_COMPILER:STRING=$MPI_BIN/mpif77 \
%endif
 -DF77_INTERFACE_ENABLE:BOOL=ON \
 -DEXAMPLES_ENABLE_F77:BOOL=ON \
 -DF2003_INTERFACE_ENABLE:BOOL=ON \
 -DEXAMPLES_ENABLE_F90:BOOL=ON \
 -DFortran_INSTALL_MODDIR:PATH=$MPI_FORTRAN_MOD_DIR/%{name} \
%endif
 -DUSE_GENERIC_MATH:BOOL=ON \
 -DOPENMP_ENABLE:BOOL=ON \
%if %{with pthread}
 -DPTHREAD_ENABLE:BOOL=ON \
%endif
%if 0%{?with_superlumt}
 -DSUPERLUMT_ENABLE:BOOL=ON \
 -DSUPERLUMT_INCLUDE_DIR:PATH=%{_includedir}/SuperLUMT \
 -DSUPERLUMT_LIBRARY_DIR:PATH=%{_libdir} \
 -DSUPERLUMT_THREAD_TYPE:STRING=OpenMP \
%endif
%if 0%{?with_superludist}
 -DSUPERLUDIST_ENABLE:BOOL=ON \
 -DSUPERLUDIST_INCLUDE_DIR:PATH=$MPI_INCLUDE/superlu_dist \
 -DSUPERLUDIST_LIBRARY_DIR:PATH=$MPI_LIB \
 -DSUPERLUDIST_LIBRARIES:STRING=libsuperlu_dist.so \
%endif
%if 0%{?with_hypre}
 -DHYPRE_ENABLE:BOOL=ON \
 -DHYPRE_INCLUDE_DIR:PATH=$MPI_INCLUDE/hypre \
 -DHYPRE_LIBRARY_DIR:PATH=$MPI_LIB \
%endif
 -DEXAMPLES_INSTALL:BOOL=OFF \
 -DSUNDIALS_BUILD_WITH_MONITORING:BOOL=ON -Wno-dev

%make_build V=1 -C buildopenmpi_dir/build
%{_openmpi_unload}
%endif
######
###########################################################################

%if 0%{?with_mpich}

mkdir -p buildmpich_dir/build
%{_mpich_load}

## Blas
export LIBBLASLINK=-l%{blaslib}%{blasvar}
export INCBLAS=%{_includedir}/%{blaslib}
##

## SuperLUMT
%if 0%{?with_superlumt}
%ifarch s390x x86_64 %{power64} aarch64
export LIBSUPERLUMTLINK=-lsuperlumt64_d
%endif
%ifarch %{arm} %{ix86}
export LIBSUPERLUMTLINK=-lsuperlumt_d
%endif
%endif

## Hypre
%if 0%{?with_hypre}
export LIBHYPRELINK="-L$MPI_LIB -lHYPRE"
%endif
##

# Force MPI compilers
export CC=$MPI_BIN/mpicc
export CXX=$MPI_BIN/mpic++
%if 0%{?fedora}
export FC=$MPI_BIN/mpifort
%else
export FC=$MPI_BIN/mpif77
%endif
##

%if 0%{?el7}
%{?dts:source /opt/rh/devtoolset-6/enable}
%endif

%if %{with debug}
%undefine _hardened_build
export CFLAGS=" "
export FFLAGS=" "
%global _cmake cmake3
%_cmake -B buildmpich_dir/build -S buildmpich_dir \
 -DCMAKE_VERBOSE_MAKEFILE:BOOL=ON \
 -DCMAKE_BUILD_TYPE:STRING=Debug \
 -DCMAKE_C_FLAGS_DEBUG:STRING="-O0 -g %{__global_ldflags} -I$INCBLAS" \
 -DCMAKE_Fortran_FLAGS_DEBUG:STRING="-O0 -g %{__global_ldflags} -I$INCBLAS" \
 -DCMAKE_SHARED_LINKER_FLAGS_DEBUG:STRING="%{__global_ldflags} $LIBBLASLINK $LIBSUPERLUMTLINK $LIBHYPRELINK" \
%else
export CFLAGS="%{build_cflags}"
export CFLAGS="%{build_fflags}"
%cmake3 -B buildmpich_dir/build -S buildmpich_dir \
%endif
%if 0%{?fedora} || 0%{?rhel} >= 9
%if %{?__isa_bits:%{__isa_bits}}%{!?__isa_bits:32} == 64
 -DSUNDIALS_INDEX_SIZE:STRING=64 \
 -DKLU_ENABLE=ON -DKLU_LIBRARY_DIR:PATH=%{_libdir} -DKLU_LIBRARY=%{_libdir}/libklu64.so \
 -DAMD_LIBRARY=%{_libdir}/libamd64.so -DAMD_LIBRARY_DIR:PATH=%{_libdir} \
 -DBTF_LIBRARY=%{_libdir}/libbtf64.so -DBTF_LIBRARY_DIR:PATH=%{_libdir} \
 -DCOLAMD_LIBRARY=%{_libdir}/libcolamd64.so -DCOLAMD_LIBRARY_DIR:PATH=%{_libdir} \
%else
 -DSUNDIALS_INDEX_SIZE:STRING=32 \
 -DKLU_ENABLE=ON -DKLU_LIBRARY_DIR:PATH=%{_libdir} -DKLU_LIBRARY=%{_libdir}/libklu.so \
 -DAMD_LIBRARY=%{_libdir}/libamd.so -DAMD_LIBRARY_DIR:PATH=%{_libdir} \
 -DBTF_LIBRARY=%{_libdir}/libbtf.so -DBTF_LIBRARY_DIR:PATH=%{_libdir} \
 -DCOLAMD_LIBRARY=%{_libdir}/libcolamd.so -DCOLAMD_LIBRARY_DIR:PATH=%{_libdir} \
%endif
%endif
%if 0%{?rhel} == 8
 -DKLU_ENABLE=ON -DKLU_LIBRARY_DIR:PATH=%{_libdir} -DKLU_LIBRARY=%{_libdir}/libklu.so \
 -DAMD_LIBRARY=%{_libdir}/libamd.so -DAMD_LIBRARY_DIR:PATH=%{_libdir} \
 -DBTF_LIBRARY=%{_libdir}/libbtf.so -DBTF_LIBRARY_DIR:PATH=%{_libdir} \
 -DCOLAMD_LIBRARY=%{_libdir}/libcolamd.so -DCOLAMD_LIBRARY_DIR:PATH=%{_libdir} \
%endif
 -DKLU_INCLUDE_DIR:PATH=%{_includedir}/suitesparse \
 -DCMAKE_VERBOSE_MAKEFILE:BOOL=ON \
 -DCMAKE_BUILD_TYPE:STRING=Release \
 -DCMAKE_C_FLAGS_RELEASE:STRING="%{optflags} -I$INCBLAS" \
 -DCMAKE_Fortran_FLAGS_RELEASE:STRING="%{optflags} -I$INCBLAS" \
 -DCMAKE_SHARED_LINKER_FLAGS_RELEASE:STRING="%{__global_ldflags} $LIBBLASLINK $LIBSUPERLUMTLINK $LIBHYPRELINK" \
 -DLAPACK_ENABLE:BOOL=OFF \
 -DMPI_INCLUDE_PATH:PATH=$MPI_INCLUDE \
 -DCMAKE_INSTALL_INCLUDEDIR:PATH=$MPI_INCLUDE \
%if 0%{?with_petsc}
 -DPETSC_ENABLE:BOOL=ON \
 -DPETSC_INCLUDES:PATH=$MPI_INCLUDE/petsc \
 -DPETSC_LIBRARIES:PATH=$MPI_LIB/libpetsc.so \
 -DPETSC_EXECUTABLE_RUNS=YES \
%endif
 -DCMAKE_INSTALL_PREFIX:PATH=%{_prefix} -DCMAKE_INSTALL_LIBDIR:PATH=%{_lib}/mpich/lib \
 -DPYTHON_EXECUTABLE:FILEPATH=%{__python3} \
 -DEXAMPLES_ENABLE_CXX:BOOL=ON -DEXAMPLES_ENABLE_C:BOOL=ON \
 -DBUILD_SHARED_LIBS:BOOL=ON -DBUILD_STATIC_LIBS:BOOL=ON \
 -DCMAKE_SKIP_RPATH:BOOL=YES -DCMAKE_SKIP_INSTALL_RPATH:BOOL=YES \
 -DMPI_ENABLE:BOOL=ON \
%if 0%{?with_fortran}
%if 0%{?fedora}
 -DMPI_Fortran_COMPILER:STRING=$MPI_BIN/mpifort \
%else
 -DMPI_Fortran_COMPILER:STRING=$MPI_BIN/mpif77 \
%endif
 -DF77_INTERFACE_ENABLE:BOOL=ON \
 -DEXAMPLES_ENABLE_F77:BOOL=ON \
 -DF2003_INTERFACE_ENABLE:BOOL=ON \
 -DEXAMPLES_ENABLE_F90:BOOL=ON \
 -DFortran_INSTALL_MODDIR:PATH=$MPI_FORTRAN_MOD_DIR/%{name} \
%endif
 -DUSE_GENERIC_MATH:BOOL=ON \
 -DOPENMP_ENABLE:BOOL=ON \
%if %{with pthread}
 -DPTHREAD_ENABLE:BOOL=ON \
%endif
%if 0%{?with_superlumt}
 -DSUPERLUMT_ENABLE:BOOL=ON \
 -DSUPERLUMT_INCLUDE_DIR:PATH=%{_includedir}/SuperLUMT \
 -DSUPERLUMT_LIBRARY_DIR:PATH=%{_libdir} \
 -DSUPERLUMT_THREAD_TYPE:STRING=OpenMP \
%endif
%if 0%{?with_superludist}
 -DSUPERLUDIST_ENABLE:BOOL=ON \
 -DSUPERLUDIST_INCLUDE_DIR:PATH=$MPI_INCLUDE/superlu_dist \
 -DSUPERLUDIST_LIBRARY_DIR:PATH=$MPI_LIB \
 -DSUPERLUDIST_LIBRARIES:STRING=libsuperlu_dist.so \
%endif
%if 0%{?with_hypre}
 -DHYPRE_ENABLE:BOOL=ON \
 -DHYPRE_INCLUDE_DIR:PATH=$MPI_INCLUDE/hypre \
 -DHYPRE_LIBRARY_DIR:PATH=$MPI_LIB \
%endif
 -DEXAMPLES_INSTALL:BOOL=OFF \
 -DSUNDIALS_BUILD_WITH_MONITORING:BOOL=ON -Wno-dev

%make_build V=1 -C buildmpich_dir/build
%{_mpich_unload}
%endif
######
#############################################################################

%install
%if 0%{?with_openmpi}
%{_openmpi_load}
%make_install -C buildopenmpi_dir/build
rm -f %{buildroot}$MPI_INCLUDE/sundials/LICENSE
rm -f %{buildroot}$MPI_INCLUDE/sundials/NOTICE
%{_openmpi_unload}
%endif

%if 0%{?with_mpich}
%{_mpich_load}
%make_install -C buildmpich_dir/build
rm -f %{buildroot}$MPI_INCLUDE/sundials/LICENSE
rm -f %{buildroot}$MPI_INCLUDE/sundials/NOTICE
%{_mpich_unload}
%endif

%make_install -C sundials-%{version}/build

# Remove files in bad position
rm -f %{buildroot}%{_prefix}/LICENSE
rm -f %{buildroot}%{_includedir}/sundials/LICENSE
rm -f %{buildroot}%{_includedir}/sundials/NOTICE

%check
%if 0%{?with_openmpi}
%if 0%{?with_openmpicheck}
%define _vpath_builddir buildopenmpi_dir/build
%{_openmpi_load}
%if %{with debug}
export LD_LIBRARY_PATH=%{buildroot}$MPI_LIB:$MPI_LIB
export OMPI_MCA_rmaps_base_oversubscribe=yes
ctest3 --force-new-ctest-process -VV -j1 --output-on-failure --debug
%else
export LD_LIBRARY_PATH=%{buildroot}$MPI_LIB:$MPI_LIB
export OMPI_MCA_rmaps_base_oversubscribe=yes
%ifarch aarch64 %{power64}
%ctest -- -E 'test_fsunlinsol_dense_mod|test_sunnonlinsol_petscsnes'
%else
%ctest -- -E 'test_sunnonlinsol_petscsnes|test_sunlinsol_klu'
%endif
%endif
%{_openmpi_unload}
%endif
## if with_openmpicheck
%endif
## if with_openmpi

%if 0%{?with_mpich}
%if 0%{?with_mpichcheck}
%define _vpath_builddir buildmpich_dir/build
%{_mpich_load}
%if %{with debug}
export LD_LIBRARY_PATH=%{buildroot}$MPI_LIB:$MPI_LIB
ctest3 --force-new-ctest-process -VV -j1 --output-on-failure --debug
%else
export LD_LIBRARY_PATH=%{buildroot}$MPI_LIB:$MPI_LIB
%ifarch aarch64 %{power64}
%ctest -- -E 'test_fsunlinsol_dense_mod|test_sunnonlinsol_petscsnes'
%else
%ctest -- -E 'test_sunnonlinsol_petscsnes|test_sunlinsol_klu'
%endif
%endif
%{_mpich_unload}
%endif
## if with_mpichcheck
%endif
## if with_mpich

%if 0%{?with_sercheck}
%define _vpath_builddir sundials-%{version}/build
%if %{with debug}
export LD_LIBRARY_PATH=%{buildroot}%{_libdir}:%{_libdir}
ctest3 --force-new-ctest-process -VV -j1 --output-on-failure --debug
%else
export LD_LIBRARY_PATH=%{buildroot}%{_libdir}:%{_libdir}
%ifarch aarch64 %{power64}
%ctest -- -E 'test_fsunlinsol_dense_mod'
%else
%ctest -- -E 'test_sunlinsol_klu'
%endif
%endif
%endif
## if with_sercheck

%files
%license sundials-%{version}/LICENSE
%doc sundials-%{version}/README.md
%doc sundials-%{version}/src/README-arkode.md
%doc sundials-%{version}/src/README-cvode.md
%doc sundials-%{version}/src/README-cvodes.md
%doc sundials-%{version}/src/README-ida.md
%doc sundials-%{version}/src/README.idas.md
%doc sundials-%{version}/src/README-kinsol.md
%doc sundials-%{version}/NOTICE
%{_libdir}/libsundials_generic.so.*
%{_libdir}/libsundials_ida*.so.*
%{_libdir}/libsundials_cvode*.so.*
%{_libdir}/libsundials_arkode*.so.*
%{_libdir}/libsundials_kinsol.so.*
%{_libdir}/libsundials_nvecserial.so.*
%{_libdir}/libsundials_nvecopenmp.so.*
%{_libdir}/libsundials_nvecmanyvector.so.*
%if %{with pthread}
%{_libdir}/libsundials_nvecpthreads.so.*
%endif
%{_libdir}/libsundials_sunmatrix*.so.*
%{_libdir}/libsundials_sunlinsol*.so.*
%{_libdir}/libsundials_sunnonlinsol*.so.*
%if 0%{?with_fortran}
%{_libdir}/libsundials_f*[_mod].so.*
%{_libdir}/libsundials_f*[!_mod].so.*
%endif

%files devel
%{_libdir}/*.a
%{_libdir}/libsundials_generic.so
%{_libdir}/libsundials_ida*.so
%{_libdir}/libsundials_cvode*.so
%{_libdir}/libsundials_arkode*.so
%{_libdir}/libsundials_kinsol.so
%{_libdir}/libsundials_nvecserial.so
%{_libdir}/libsundials_nvecopenmp.so
%{_libdir}/libsundials_nvecmanyvector.so
%{_libdir}/cmake/sundials/
%if %{with pthread}
%{_libdir}/libsundials_nvecpthreads.so
%endif
%{_libdir}/libsundials_sunmatrix*.so
%{_libdir}/libsundials_sunlinsol*.so
%{_libdir}/libsundials_sunnonlinsol*.so
%if 0%{?with_fortran}
%{_libdir}/libsundials_f*[_mod].so
%{_libdir}/libsundials_f*[!_mod].so
%{_fmoddir}/%{name}/
%if %{with pthread}
%{_libdir}/libsundials_fnvecpthreads.so
%endif
%if 0%{?with_superlumt}
%{_libdir}/libsundials_fsunlinsolsuperlumt.so
%endif
%endif
%{_includedir}/nvector/
%{_includedir}/sunmatrix/
%{_includedir}/sunlinsol/
%{_includedir}/sunnonlinsol/
%{_includedir}/arkode/
%{_includedir}/cvode/
%{_includedir}/cvodes/
%{_includedir}/ida/
%{_includedir}/idas/
%{_includedir}/kinsol/
%dir %{_includedir}/sundials
%{_includedir}/sundials/sundials_export.h
%{_includedir}/sundials/sundials_band.h
%{_includedir}/sundials/sundials_dense.h
%{_includedir}/sundials/sundials_direct.h
%{_includedir}/sundials/sundials_futils.h
%{_includedir}/sundials/sundials_iterative.h
%{_includedir}/sundials/sundials_linearsolver.h
%{_includedir}/sundials/sundials_math.h
%{_includedir}/sundials/sundials_matrix.h
%{_includedir}/sundials/sundials_memory.h
%{_includedir}/sundials/sundials_nonlinearsolver.h
%{_includedir}/sundials/sundials_mpi_types.h
%{_includedir}/sundials/sundials_nvector.h
%{_includedir}/sundials/sundials_types.h
%{_includedir}/sundials/sundials_version.h
%{_includedir}/sundials/sundials_config.h
%{_includedir}/sundials/sundials_fconfig.h
%{_includedir}/sundials/sundials_fnvector.h

%if 0%{?with_openmpi}
%files openmpi
%license sundials-%{version}/LICENSE
%doc sundials-%{version}/README.md
%doc sundials-%{version}/src/README-arkode.md
%doc sundials-%{version}/src/README-cvode.md
%doc sundials-%{version}/src/README-cvodes.md
%doc sundials-%{version}/src/README-ida.md
%doc sundials-%{version}/src/README.idas.md
%doc sundials-%{version}/src/README-kinsol.md
%doc sundials-%{version}/NOTICE
%{_libdir}/openmpi/lib/libsundials_generic.so.*
%{_libdir}/openmpi/lib/libsundials_nvecparallel.so.*
%{_libdir}/openmpi/lib/libsundials_nvecparhyp.so.*
%if 0%{?with_petsc}
%{_libdir}/openmpi/lib/libsundials_nvecpetsc.so.*
%{_libdir}/openmpi/lib/libsundials_sunnonlinsolpetscsnes.so.*
%endif
%{_libdir}/openmpi/lib/libsundials_nvecmpimanyvector.so.*
%if %{with pthread}
%{_libdir}/openmpi/lib/libsundials_nvecmpipthreads.so.*
%endif
%{_libdir}/openmpi/lib/libsundials_nvecmpiplusx.so.*
%{_libdir}/openmpi/lib/libsundials_kinsol.so.*
%{_libdir}/openmpi/lib/libsundials_ida*.so.*
%{_libdir}/openmpi/lib/libsundials_cvode*.so.*
%{_libdir}/openmpi/lib/libsundials_arkode*.so.*
%{_libdir}/openmpi/lib/libsundials_nvecserial.so.*
%{_libdir}/openmpi/lib/libsundials_nvecopenmp.so.*
%{_libdir}/openmpi/lib/libsundials_sunmatrix*.so.*
%{_libdir}/openmpi/lib/libsundials_sunlinsol*.so.*
%{_libdir}/openmpi/lib/libsundials_sunnonlinsol*.so.*
%{_libdir}/openmpi/lib/libsundials_nvecmanyvector.so.*
%if %{with pthread}
%{_libdir}/openmpi/lib/libsundials_nvecpthreads.so.*
%endif
%if 0%{?with_fortran}
%{_libdir}/openmpi/lib/libsundials_f*[_mod].so.*
%{_libdir}/openmpi/lib/libsundials_f*[!_mod].so.*
%endif

%files openmpi-devel
%{_libdir}/openmpi/lib/*.a
%{_includedir}/openmpi-%{_arch}/nvector/
%{_includedir}/openmpi-%{_arch}/sundials/
%{_includedir}/openmpi-%{_arch}/arkode/
%{_includedir}/openmpi-%{_arch}/cvode/
%{_includedir}/openmpi-%{_arch}/cvodes/
%{_includedir}/openmpi-%{_arch}/ida/
%{_includedir}/openmpi-%{_arch}/idas/
%{_includedir}/openmpi-%{_arch}/kinsol/
%{_includedir}/openmpi-%{_arch}/sunlinsol/
%{_includedir}/openmpi-%{_arch}/sunmatrix/
%{_includedir}/openmpi-%{_arch}/sunnonlinsol/
%if 0%{?with_fortran}
%{_fmoddir}/openmpi%{?el7:-%_arch}/%{name}/
%{_libdir}/openmpi/lib/libsundials_f*[_mod].so
%{_libdir}/openmpi/lib/libsundials_f*[!_mod].so
%endif
%{_libdir}/openmpi/lib/libsundials_generic.so
%{_libdir}/openmpi/lib/libsundials_nvecparallel.so
%{_libdir}/openmpi/lib/libsundials_nvecparhyp.so
%if 0%{?with_petsc}
%{_libdir}/openmpi/lib/libsundials_nvecpetsc.so
%{_libdir}/openmpi/lib/libsundials_sunnonlinsolpetscsnes.so
%endif
%{_libdir}/openmpi/lib/libsundials_nvecmpimanyvector.so
%if %{with pthread}
%{_libdir}/openmpi/lib/libsundials_nvecmpipthreads.so
%{_libdir}/openmpi/lib/libsundials_nvecpthreads.so
%endif
%{_libdir}/openmpi/lib/libsundials_nvecmpiplusx.so
%{_libdir}/openmpi/lib/libsundials_kinsol.so
%{_libdir}/openmpi/lib/libsundials_ida*.so
%{_libdir}/openmpi/lib/libsundials_cvode*.so
%{_libdir}/openmpi/lib/libsundials_arkode*.so
%{_libdir}/openmpi/lib/libsundials_nvecserial.so
%{_libdir}/openmpi/lib/libsundials_nvecopenmp.so
%{_libdir}/openmpi/lib/libsundials_sunmatrix*.so
%{_libdir}/openmpi/lib/libsundials_sunlinsol*.so
%{_libdir}/openmpi/lib/libsundials_sunnonlinsol*.so
%{_libdir}/openmpi/lib/libsundials_nvecmanyvector.so
%{_libdir}/openmpi/lib/cmake/sundials/
%endif

%if 0%{?with_mpich}
%files mpich
%license sundials-%{version}/LICENSE
%doc sundials-%{version}/README.md
%doc sundials-%{version}/src/README-arkode.md
%doc sundials-%{version}/src/README-cvode.md
%doc sundials-%{version}/src/README-cvodes.md
%doc sundials-%{version}/src/README-ida.md
%doc sundials-%{version}/src/README.idas.md
%doc sundials-%{version}/src/README-kinsol.md
%doc sundials-%{version}/NOTICE
%{_libdir}/mpich/lib/libsundials_generic.so.*
%{_libdir}/mpich/lib/libsundials_nvecparallel.so.*
%{_libdir}/mpich/lib/libsundials_nvecparhyp.so.*
%if 0%{?with_petsc}
%{_libdir}/mpich/lib/libsundials_nvecpetsc.so.*
%{_libdir}/mpich/lib/libsundials_sunnonlinsolpetscsnes.so.*
%endif
%{_libdir}/mpich/lib/libsundials_nvecmpimanyvector.so.*
%if %{with pthread}
%{_libdir}/mpich/lib/libsundials_nvecmpipthreads.so.*
%endif
%{_libdir}/mpich/lib/libsundials_nvecmpiplusx.so.*
%{_libdir}/mpich/lib/libsundials_kinsol.so.*
%{_libdir}/mpich/lib/libsundials_ida*.so.*
%{_libdir}/mpich/lib/libsundials_cvode*.so.*
%{_libdir}/mpich/lib/libsundials_arkode*.so.*
%{_libdir}/mpich/lib/libsundials_nvecserial.so.*
%{_libdir}/mpich/lib/libsundials_nvecopenmp.so.*
%{_libdir}/mpich/lib/libsundials_sunmatrix*.so.*
%{_libdir}/mpich/lib/libsundials_sunlinsol*.so.*
%{_libdir}/mpich/lib/libsundials_sunnonlinsol*.so.*
%{_libdir}/mpich/lib/libsundials_nvecmanyvector.so.*
%if %{with pthread}
%{_libdir}/mpich/lib/libsundials_nvecpthreads.so.*
%endif
%if 0%{?with_fortran}
%{_libdir}/mpich/lib/libsundials_f*[_mod].so.*
%{_libdir}/mpich/lib/libsundials_f*[!_mod].so.*
%endif


%files mpich-devel
%{_includedir}/mpich-%{_arch}/nvector/
%{_includedir}/mpich-%{_arch}/sundials/
%{_includedir}/mpich-%{_arch}/arkode/
%{_includedir}/mpich-%{_arch}/cvode/
%{_includedir}/mpich-%{_arch}/cvodes/
%{_includedir}/mpich-%{_arch}/ida/
%{_includedir}/mpich-%{_arch}/idas/
%{_includedir}/mpich-%{_arch}/kinsol/
%{_includedir}/mpich-%{_arch}/sunlinsol/
%{_includedir}/mpich-%{_arch}/sunmatrix/
%{_includedir}/mpich-%{_arch}/sunnonlinsol/
%if 0%{?with_fortran}
%{_fmoddir}/mpich%{?el7:-%_arch}/%{name}/
%{_libdir}/mpich/lib/libsundials_f*[_mod].so
%{_libdir}/mpich/lib/libsundials_f*[!_mod].so
%endif
%{_libdir}/mpich/lib/*.a
%{_libdir}/mpich/lib/libsundials_generic.so
%{_libdir}/mpich/lib/libsundials_nvecparallel.so
%{_libdir}/mpich/lib/libsundials_nvecparhyp.so
%if 0%{?with_petsc}
%{_libdir}/mpich/lib/libsundials_nvecpetsc.so
%{_libdir}/mpich/lib/libsundials_sunnonlinsolpetscsnes.so
%endif
%{_libdir}/mpich/lib/libsundials_nvecmpimanyvector.so
%if %{with pthread}
%{_libdir}/mpich/lib/libsundials_nvecmpipthreads.so
%{_libdir}/mpich/lib/libsundials_nvecpthreads.so
%endif
%{_libdir}/mpich/lib/libsundials_nvecmpiplusx.so
%{_libdir}/mpich/lib/libsundials_kinsol.so
%{_libdir}/mpich/lib/libsundials_ida*.so
%{_libdir}/mpich/lib/libsundials_cvode*.so
%{_libdir}/mpich/lib/libsundials_arkode*.so
%{_libdir}/mpich/lib/libsundials_nvecserial.so
%{_libdir}/mpich/lib/libsundials_nvecopenmp.so
%{_libdir}/mpich/lib/libsundials_sunmatrix*.so
%{_libdir}/mpich/lib/libsundials_sunlinsol*.so
%{_libdir}/mpich/lib/libsundials_sunnonlinsol*.so
%{_libdir}/mpich/lib/libsundials_nvecmanyvector.so
%{_libdir}/mpich/lib/cmake/sundials/
%endif

%files doc
%license sundials-%{version}/LICENSE
%doc sundials-%{version}/README.md
%doc sundials-%{version}/NOTICE
%doc sundials-%{version}/doc/cvode/cv_guide.pdf
%doc sundials-%{version}/doc/kinsol/kin_guide.pdf
%doc sundials-%{version}/doc/cvodes/cvs_guide.pdf
%doc sundials-%{version}/doc/ida/ida_guide.pdf
%doc sundials-%{version}/doc/arkode/*

%changelog
* Sat Oct 29 2022 Antonio Trande <sagitter@fedoraproject.org> - 5.8.0-7
- Use multiple jobs for testing
- Disable OpenMPI tests

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 5.8.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Sat Apr 23 2022 Antonio Trande <sagitter@fedoraproject.org> - 5.8.0-5
- Rebuild for PETSc-3.17.0

* Sat Jan 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 5.8.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Sat Nov 20 2021 Antonio Trande <sagitter@fedoraproject.org> - 5.8.0-3
- Enable SuiteSparse support on epel8

* Sat Nov 06 2021 Antonio Trande <sagitter@fedoraproject.org> - 5.8.0-2
- Build on epel8

* Wed Oct 20 2021 Antonio Trande <sagitter@fedoraproject.org> - 5.8.0-1
- Release 5.8.0

* Mon Jul 26 2021 Antonio Trande <sagitter@fedoraproject.org> - 5.7.0-3
- Disable debug mode

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 5.7.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Sun Feb 21 2021 Antonio Trande <sagitter@fedoraproject.org> - 5.7.0-1
- Release 5.7.0

* Sun Feb 21 2021 Antonio Trande <sagitter@fedoraproject.org> - 5.6.1-3
- Fix the lists of installed files

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 5.6.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Dec 30 2020 Antonio Trande <sagitter@fedoraproject.org> - 5.6.1-1
- Release 5.6.1

* Thu Dec 10 2020 Antonio Trande <sagitter@fedoraproject.org> - 5.5.0-2
- Modify CMake options

* Sun Nov 08 2020 Antonio Trande <sagitter@fedoraproject.org> - 5.5.0-1
- Release 5.5.0

* Fri Sep 25 2020 Antonio Trande <sagitter@fedoraproject.org> - 5.4.0-1
- Release 5.4.0

* Mon Aug 24 2020 Antonio Trande <sagitter@fedoraproject.org> - 5.3.0-5
- Increase build release number

* Thu Aug 20 2020 Iñaki Úcar <iucar@fedoraproject.org> - 5.3.0-4
- https://fedoraproject.org/wiki/Changes/FlexiBLAS_as_BLAS/LAPACK_manager

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 5.3.0-3
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 5.3.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Sat May 23 2020 Antonio Trande <sagitter@fedoraproject.org> - 5.3.0-1
- Release 5.3.0
- CMake option SUNDIALS_BUILD_WITH_MONITORING activated

* Sat May 23 2020 Antonio Trande <sagitter@fedoraproject.org> - 5.2.0-5
- Add OMPI_MCA_rmaps_base_oversubscribe=yes option to prevent ctest
  failures due to insufficient number of slots
  
* Fri May 22 2020 Antonio Trande <sagitter@fedoraproject.org> - 5.2.0-4
- Fix installation of config.h files (rhbz#1839131)

* Fri Apr 24 2020 Antonio Trande <sagitter@fedoraproject.org> - 5.2.0-3
- Fix packaging of all libraries

* Fri Apr 24 2020 Antonio Trande <sagitter@fedoraproject.org> - 5.2.0-2
- Fix rhbz#1827675

* Fri Apr 10 2020 Antonio Trande <sagitter@fedoraproject.org> - 5.2.0-1
- Release 5.2.0
- Use -fcommon flag workaround for GCC-10
- Disable pthread support (do not mix-up openmp and pthread)

* Fri Jan 31 2020 Antonio Trande <sagitter@fedoraproject.org> - 4.1.0-12
- Use job 1 with ctest
- Disable MPI tests on EPEL8

* Fri Jan 31 2020 Antonio Trande <sagitter@fedoraproject.org> - 4.1.0-11
- Fix rhbz#1828004

* Fri Jan 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 4.1.0-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sat Jan 25 2020 Antonio Trande <sagitter@fedoraproject.org> - 4.1.0-9
- Workaround for GCC-10 (-fcommon)

* Sun Jan 05 2020 Antonio Trande <sagitter@fedoraproject.org> - 4.1.0-8
- New rebuild

* Sat Dec 21 2019 Antonio Trande <sagitter@fedoraproject.org> - 4.1.0-7
- Rebuild for petsc-3.11.3 on EPEL7

* Fri Oct 18 2019 Antonio Trande <sagitter@fedoraproject.org> - 4.1.0-6
- Rebuild for petsc-3.12.0

* Sat Jul 27 2019 Fedora Release Engineering <releng@fedoraproject.org> - 4.1.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Jun 30 2019 Antonio Trande <sagitter@fedoraproject.org> - 4.1.0-4
- Do not use devtoolset as runtime dependence

* Wed Jun 26 2019 Antonio Trande <sagitter@fedoraproject.org> - 4.1.0-3
- Do not use curly brackets under %%files

* Thu Apr 25 2019 Antonio Trande <sagitter@fedoraproject.org> - 4.1.0-2
- Reorganization of the files

* Sun Apr 21 2019 Antonio Trande <sagitter@fedoraproject.org> - 4.1.0-1
- Release 4.1.0
- Re-enable OpenMPI tests (rhbz#1639646)
- Use Python3
- Compile Fortran libraries

* Thu Feb 14 2019 Orion Poplawski <orion@nwra.com> - 3.2.1-4
- Rebuild for openmpi 3.1.3
- Disable tests of MPI libraries for "not enough slots available" errors

* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.2.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sun Dec 02 2018 Antonio Trande <sagitter@fedoraproject.org> - 3.2.1-2
- PETSc support is now re-enabled (rhbz#1639646)

* Sat Oct 20 2018 Antonio Trande <sagitter@fedoraproject.org> - 3.2.1-1
- Update to 3.2.1
- Disable PETSc support (rhbz#1639646)
- Disable OpenMPI tests (rhbz#1639646)

* Sat Oct 13 2018 Antonio Trande <sagitter@fedoraproject.org> - 3.2.0-1
- Update to 3.2.0

* Wed Sep 05 2018 Antonio Trande <sagitter@fedoraproject.org> - 3.1.2-2
- Forced to use python2 (tests work under python2 only)

* Wed Aug 01 2018 Antonio Trande <sagitter@fedoraproject.org> - 3.1.2-1
- Update to 3.1.2
- Enable PETSC support

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Jun 06 2018 Antonio Trande <sagitter@fedoraproject.org> - 3.1.1-2
- Do not pack examples
- Use SuperLUMT64 on 64bit systems

* Sun May 13 2018 Antonio Trande <sagitter@fedoraproject.org> - 3.1.1-1
- Update to 3.1.1

* Fri May 04 2018 Antonio Trande <sagitter@fedoraproject.org> - 3.1.0-5
- Rebuild for hypre-2.14.0

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Fri Feb 02 2018 Antonio Trande <sagitter@fedoraproject.org> - 3.1.0-3
- Use %%ldconfig_scriptlets

* Wed Jan 31 2018 Antonio Trande <sagitter@fedoraproject.org> - 3.1.0-2
- Rebuild for GCC-8

* Fri Dec 22 2017 Antonio Trande <sagitter@fedoraproject.org> - 3.1.0-1
- Update to 3.1.0

* Wed Nov 15 2017 Antonio Trande <sagitter@fedoraproject.org> - 3.0.0-3
- Use -Wl,--as-needed flag
- Fix shared-linker flags

* Thu Nov 09 2017 Antonio Trande <sagitter@fedoraproject.org> - 3.0.0-2
- Remove sub-packages
- Uninstall static libraries

* Mon Oct 30 2017 Antonio Trande <sagitter@fedoraproject.org> - 3.0.0-1
- Update to 3.0.0
- Use cmake3 on epel
- Install examples

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.7.0-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Mar 03 2017 Antonio Trande <sagitter@fedoraproject.org> - 2.7.0-10
- Build OpenMPI libraries on EPEL

* Fri Mar 03 2017 Antonio Trande <sagitter@fedoraproject.org> - 2.7.0-9
- Add KLU support

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.7.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Tue Nov 01 2016 Antonio Trande <sagitter@fedoraproject.org> - 2.7.0-7
- New architectures

* Mon Oct 24 2016 Antonio Trande <sagitter@fedoraproject.org> - 2.7.0-6
- Fix builds of MPICH libraries

* Fri Oct 21 2016 Orion Poplawski <orion@cora.nwra.com> - 2.7.0-5
- Rebuild for openmpi 2.0

* Mon Oct 17 2016 Antonio Trande <sagitter@fedoraproject.org> - 2.7.0-4
- Set debug builds

* Thu Oct 06 2016 Antonio Trande <sagitter@fedoraproject.org> - 2.7.0-3
- SuperLUMT support condizionalized
- Removed pkgconfig files

* Tue Oct 04 2016 Antonio Trande <sagitter@fedoraproject.org> - 2.7.0-2
- Enabled SuperLUMT and HYPRE support

* Thu Sep 29 2016 Antonio Trande <sagitter@fedoraproject.org> - 2.7.0-1
- Update to 2.7.0

* Sun Mar 27 2016 Antonio Trande <sagitter@fedoraproject.org> - 2.6.2-19
- Typos fixed

* Sat Mar 26 2016 Antonio Trande <sagitter@fedoraproject.org> - 2.6.2-18
- Enabled OpenMP support

* Sun Mar 20 2016 Mukundan Ragavan <nonamedotc@fedoraproject.org> - 2.6.2-17
- Add lapack-devel requires to -devel package

* Fri Feb 05 2016 Fedora Release Engineering <releng@fedoraproject.org> - 2.6.2-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Mon Jan 25 2016 Antonio Trande <sagitter@fedoraproject.org> - 2.6.2-15
- Fixed pthread flags

* Sun Jan 17 2016 Antonio Trande <sagitter@fedoraproject.org> - 2.6.2-14
- Fix OpenMPI compilers
- MPICH libraries enabled
- Cmake's MPI Fortran compiler test disabled
- Included pkgconfig files for MPICH libraries

* Thu Dec 31 2015 Antonio Trande <sagitter@fedoraproject.org> - 2.6.2-13
- Exclude pkgconfig for OpenMPI libs on s390

* Sat Dec 26 2015 Antonio Trande <sagitter@fedoraproject.org> - 2.6.2-12
- Fixed pkgconfig files
- Added pkgconfig files for OpenMPI libraries
- All Fortran libraries moved to default library paths

* Thu Nov 12 2015 Antonio Trande <sagitter@fedoraproject.org> - 2.6.2-11
- Fixes for EPEL7
- Set mpif77 only for OpenMPI < 1.17 (EPEL7)
- Set mpifort for OpenMPI > 1.17 (Fedora)
- Set LDFLAGS for EPEL7

* Wed Nov 11 2015 Antonio Trande <sagitter@fedoraproject.org> - 2.6.2-10
- OpenMPI Fortran lib tests not compiled on F<23

* Wed Nov 11 2015 Antonio Trande <sagitter@fedoraproject.org> - 2.6.2-9
- Hardened builds on <F23
- openmpi tests still crash/hang on i686 (Fedora 21)
- Rebuilt on Fedora 21

* Thu Oct 15 2015 Antonio Trande <sagitter@fedoraproject.org> - 2.6.2-8
- Rebuilt for cmake 3.4.0

* Sun Sep 20 2015 Antonio Trande <sagitter@fedoraproject.org> - 2.6.2-7
- Performed even tests of the parallel-libraries on ix86 arches

* Tue Sep 15 2015 Orion Poplawski <orion@cora.nwra.com> - 2.6.2-6
- Rebuild for openmpi 1.10.0

* Fri Aug 28 2015 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 2.6.2-5
- Rebuild for rpm-mpi-hooks-3-2

* Sat Aug 15 2015 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 2.6.2-4
- Rebuild for MPI provides

* Mon Aug 10 2015 Sandro Mani <manisandro@gmail.com> - 2.6.2-3
- Rebuild for RPM MPI Requires Provides Change

* Tue Aug 04 2015 Antonio Trande <sagitter@fedoraproject.org> - 2.6.2-2
- Added rsh as BR for EPEL7

* Tue Aug 04 2015 Antonio Trande <sagitter@fedoraproject.org> - 2.6.2-1
- Update to 2.6.2

* Fri Jun 19 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.6.1-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Wed Jun 03 2015 Antonio Trande <sagitter@fedoraproject.org> - 2.6.1-8
- Excluded some tests for s390 s390x
- openmpi tests disabled on ix86 %%{arm} (BZ#1201901)

* Sat May 09 2015 Antonio Trande <sagitter@fedoraproject.org> - 2.6.1-7
- Excluded kinKrylovDemo_ls test for aarch64

* Fri Apr 17 2015 Antonio Trande <sagitter@fedoraproject.org> - 2.6.1-6
- Performed parallel/serial tests

* Thu Apr 16 2015 Antonio Trande <sagitter@fedoraproject.org> - 2.6.1-5
- Fixed ldconfig scriptlets

* Sat Apr 04 2015 Antonio Trande <sagitter@fedoraproject.org> - 2.6.1-4
- Packaged static Fortran libraries

* Fri Apr 03 2015 Antonio Trande <sagitter@fedoraproject.org> - 2.6.1-3
- Packaged pkg-config files of Serial libraries

* Wed Apr 01 2015 Antonio Trande <sagitter@fedoraproject.org> - 2.6.1-2
- Built OpenMPI, libraries with threading support, Fortran libraries

* Mon Mar 30 2015 Mukundan Ragavan <nonamedotc@fedoraproject.org> - 2.6.1-1
- Update to version 2.6.1 
- Minor bugfixes

* Sun Mar 29 2015 Mukundan Ragavan <nonamedotc@fedoraproject.org> - 2.6.0-2
- Ensure the shared libraries are linked correctly

* Sun Mar 22 2015 Mukundan Ragavan <nonamedotc@fedoraproject.org> - 2.6.0-1
- Update to 2.6.0
- Drop patches that are not needed anymore

* Wed Dec 03 2014 Mukundan Ragavan <nonamedotc@fedoraproject.org> - 2.5.0-7
- Initial build for EPEL-7

* Mon Aug 18 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.5.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Mukundan Ragavan <nonamedotc@fedoraproject.org> - 2.5.0-5
- Fixed patches used in the previous build
- Fixes bug #1105767

* Wed May 21 2014 Mukundan Ragavan <nonamedotc@fedoraproject.org> - 2.5.0-4
- added patches to fix bugs #926583 and #1037342

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.5.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Mon Feb 18 2013 Dan Horák <dan[at]danny.cz> - 2.5.0-2
- openmpi not available s390(x)

* Sat Jan 26 2013 Rahul Sundaram <sundaram@fedoraproject.org> - 2.5.0-1
- upstream release 2.5.0
- enable parallel build
- drop obsolete patch

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.3.0-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.3.0-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.3.0-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.3.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.3.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Sun Sep 21 2008 Ville Skyttä <ville.skytta at iki.fi> - 2.3.0-7
- Fix Patch0:/%%patch mismatch (#463065).

* Tue Feb 19 2008 Fedora Release Engineering <rel-eng@fedoraproject.org> - 2.3.0-6
- Autorebuild for GCC 4.3

* Sat Aug 04 2007 John Pye <john@curioussymbols.com> 2.3.0-5
- Final corrections from Debarshi Ray:
- Changed all file-location macros to the curly-bracket format.
- License field changed to BSD and comments added regarding special conditions.

* Wed Aug 01 2007 John Pye <john@curioussymbols.com> 2.3.0-4
- Corrections from Mamoru Tasaka:
- Removed /sbin/ldconfig call for -devel package (not required).
- Moved *.a libraries to a -static package.
- Corrected sub/main package dependencies (added release num).
- Corrected and added extra 'defattr' statements in files sections.

* Tue Jul 31 2007 John Pye <john@curioussymbols.com> 2.3.0-3
- Removed INSTALL_NOTES.
- Added /sbin/ldconfig call for -devel package.
- Remove automake dependency.
- Changed --with-mpi-root location (currently commented out).
- Added /sbin/ldconfig call for -devel package.

* Mon Jul 30 2007 John Pye <john@curioussymbols.com> 2.3.0-2
- Removed OpenMPI dependencies (providing serial-only package at the moment).
- Fixing for Debarshi Ray's feedback:
- changed post/postun to use -p style,
- added comments for why 'makeinstall' is required,
- using macro instead of direct call to ./configure,
- replaced spaces with tabs,
- re-tagged -doc package as group Documentation,
- removed CC=... and CXX=... from %%configure command, and
- changed download location.

* Sun Jul 29 2007 John Pye <john@curioussymbols.com> 2.3.0-1
- Converting to Fedora RPM by removing distro-specific stuff.

* Wed Jun 27 2007 John Pye <john@curioussymbols.com> 2.3.0
- Creating separate devel, doc and library packages.

* Sun Jun 24 2007 John Pye <john@curioussymbols.com> 2.3.0
- Fixed problem with creation of shared libraries (correction thanks to Andrey Romanenko in Debian).

* Sat Jun 23 2007 John Pye <john@curioussymbols.com> 2.3.0
- Ported to OpenSUSE Build Service, working on support for openSUSE alongside FC6, FC7.

* Thu Jul 27 2006 John Pye <john.pye@student.unsw.edu.au> 2.3.0-0
- First RPM spec created.

