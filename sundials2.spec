%global __cmake_in_source_build 1

## Debug builds?
%bcond_with debug
#
%global with_openmpi 1
%global with_mpich 1

%if 0%{?rhel}
%global dts devtoolset-8-
%global dtsbindir /opt/rh/devtoolset-8/root/usr/bin/
%endif

%if 0%{?fedora} >= 33 || 0%{?rhel} >= 9
%global blaslib flexiblas
%global blasvar %{nil}
%else
%global blaslib openblas
%global blasvar o
%endif

Summary:    Suite of nonlinear solvers
Name:       sundials2
Version:    2.7.0
Release:    13%{?dist}
# SUNDIALS is licensed under BSD with some additional (but unrestrictive) clauses.
# Check the file 'LICENSE' for details.
License:    BSD
URL:        https://www.llnl.gov/casc/sundials/
Source0:    https://www.llnl.gov/casc/sundials/download/code/sundials-%{version}.tar.gz

# This patch rename superLUMT library
Patch0:     %{name}-%{version}-set_superlumt_name.patch
Patch1: sundials2-cmake-c99.patch
Patch2: sundials2-hypre-c99.patch

BuildRequires: make
BuildRequires: %{?dts}gcc-gfortran
BuildRequires: %{?dts}gcc
BuildRequires: %{?dts}gcc-c++
BuildRequires: suitesparse-devel
BuildRequires: cmake3
BuildRequires: %{blaslib}-devel
BuildRequires: SuperLUMT-devel
BuildRequires: rsh

Obsoletes: sundials < 0:2.7.0-11
Obsoletes: sundials-openmp < 0:2.7.0-11
Obsoletes: sundials-fortran < 0:2.7.0-11
Obsoletes: sundials-threads < 0:2.7.0-11

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
Provides:   %{name}-static = %{version}-%{release}
Conflicts:  sundials-devel >= 0:2.7.0-11
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
%ifnarch s390x
BuildRequires: hypre-openmpi-devel
%endif
Requires: openmpi
Obsoletes: sundials-openmpi < 0:2.7.0-11
Obsoletes: sundials-fortran-openmpi < 0:2.7.0-11
%description openmpi
SUNDIALS is a SUite of Non-linear DIfferential/ALgebraic equation Solvers
for use in writing mathematical software.
This package contains the Sundials Fortran parallel OpenMPI libraries.

%package openmpi-devel
Summary:    Suite of nonlinear solvers
Requires:   %{name}-openmpi%{?_isa} = %{version}-%{release}
Conflicts:  sundials-openmpi-devel >= 0:2.7.0-11
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
%ifnarch s390x
BuildRequires: hypre-mpich-devel
%endif
Requires: mpich
Obsoletes: sundials-mpich < 0:2.7.0-11
Obsoletes: sundials-fortran-mpich < 0:2.7.0-11
%description mpich
SUNDIALS is a SUite of Non-linear DIfferential/ALgebraic equation Solvers
for use in writing mathematical software.
This package contains the Sundials parallel MPICH libraries.

%package mpich-devel
Summary:    Suite of nonlinear solvers
Requires:   %{name}-mpich%{?_isa} = %{version}-%{release}
Conflicts:  sundials-mpich-devel >= 0:2.7.0-11
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

pushd sundials-%{version}
%ifnarch %{power64} aarch64
%patch0 -p0
%patch1 -p1
%patch2 -p1
%endif

# Set destination of the include libraries
mv src/sundials src/sundials2
mv include/sundials include/sundials2
sed -i 's|sundials/|sundials2/|g' include/*/*
find src \( -name \*.c -o -name \*.h \) -print0 | xargs -0 sed -i 's|sundials/|sundials2/|g'
sed -i 's|src/sundials/|src/sundials2/|g' src/*/CMakeLists.txt
sed -i 's|src/sundials/|src/sundials2/|g' examples/nvector/*/CMakeLists.txt
sed -i 's|src/sundials/|src/sundials2/|g' CMakeLists.txt
sed -i 's|include/sundials/|include/sundials2/|g' CMakeLists.txt
sed -i 's|include/sundials/|include/sundials2/|g' src/sundials2/CMakeLists.txt
sed -i 's!ADD_SUBDIRECTORY(src/sundials)!ADD_SUBDIRECTORY(src/sundials2)!g' CMakeLists.txt

# Set destination library's paths
sed -i 's/DESTINATION lib/DESTINATION %{_lib}/g' src/arkode/CMakeLists.txt
sed -i 's|DESTINATION lib|DESTINATION %{_lib}|g' src/arkode/fcmix/CMakeLists.txt
sed -i 's/DESTINATION lib/DESTINATION %{_lib}/g' src/cvode/CMakeLists.txt
sed -i 's|DESTINATION lib|DESTINATION %{_lib}|g' src/cvode/fcmix/CMakeLists.txt
sed -i 's/DESTINATION lib/DESTINATION %{_lib}/g' src/cvodes/CMakeLists.txt
sed -i 's/DESTINATION lib/DESTINATION %{_lib}/g' src/ida/CMakeLists.txt
sed -i 's|DESTINATION lib|DESTINATION %{_lib}|g' src/ida/fcmix/CMakeLists.txt
sed -i 's/DESTINATION lib/DESTINATION %{_lib}/g' src/idas/CMakeLists.txt
sed -i 's/DESTINATION lib/DESTINATION %{_lib}/g' src/kinsol/CMakeLists.txt
sed -i 's|DESTINATION lib|DESTINATION %{_lib}|g' src/kinsol/fcmix/CMakeLists.txt
sed -i 's|DESTINATION lib|DESTINATION %{_lib}|g' src/nvec_openmp/CMakeLists.txt

# Set pthread library's paths
sed -i 's|INSTALL(TARGETS sundials_nvecpthreads_shared DESTINATION lib)|INSTALL(TARGETS sundials_nvecpthreads_shared DESTINATION %{_libdir})|g' src/nvec_pthreads/CMakeLists.txt
sed -i 's|INSTALL(TARGETS sundials_fnvecpthreads_shared DESTINATION lib)|INSTALL(TARGETS sundials_fnvecpthreads_shared DESTINATION %{_libdir})|g' src/nvec_pthreads/CMakeLists.txt

# Set serial library's paths
sed -i 's|TARGETS sundials_nvecserial_shared DESTINATION lib|TARGETS sundials_nvecserial_shared DESTINATION %{_libdir}|g' src/nvec_ser/CMakeLists.txt
sed -i 's|DESTINATION include/nvector|DESTINATION %{_includedir}/%{name}/nvector|g' src/nvec_ser/CMakeLists.txt
sed -i 's|DESTINATION include/nvector|DESTINATION %{_includedir}/%{name}/nvector|g' src/nvec_openmp/CMakeLists.txt
sed -i 's|DESTINATION include/nvector|DESTINATION %{_includedir}/%{name}/nvector|g' src/nvec_pthreads/CMakeLists.txt
sed -i 's|DESTINATION include/arkode|DESTINATION %{_includedir}/%{name}/arkode|g' src/arkode/CMakeLists.txt
sed -i 's|DESTINATION include/cvode|DESTINATION %{_includedir}/%{name}/cvode|g' src/cvode/CMakeLists.txt
sed -i 's|DESTINATION include/cvodes|DESTINATION %{_includedir}/%{name}/cvodes|g' src/cvodes/CMakeLists.txt
sed -i 's|DESTINATION include/ida|DESTINATION %{_includedir}/%{name}/ida|g' src/ida/CMakeLists.txt
sed -i 's|DESTINATION include/idas|DESTINATION %{_includedir}/%{name}/idas|g' src/idas/CMakeLists.txt
sed -i 's|DESTINATION include/kinsol|DESTINATION %{_includedir}/%{name}/kinsol|g' src/kinsol/CMakeLists.txt
sed -i 's|DESTINATION include/sundials|DESTINATION %{_includedir}/%{name}|g' src/sundials2/CMakeLists.txt
sed -i 's|DESTINATION include/sundials|DESTINATION %{_includedir}/%{name}|g' CMakeLists.txt
sed -i 's|TARGETS sundials_fnvecserial_shared DESTINATION lib|TARGETS sundials_fnvecserial_shared DESTINATION %{_libdir}|g' src/nvec_ser/CMakeLists.txt

## mpif77 test fails
## Hardened flags break cmake's MPI Fortran compiler test
sed -i 's|set(MPIF_PERFORM_TEST TRUE)|set(MPIF_PERFORM_TEST FALSE)|g' config/SundialsMPIF.cmake
sed -i 's|set(MPIF_FOUND FALSE)|set(MPIF_FOUND TRUE)|g' config/SundialsMPIF.cmake

mv src/arkode/README src/README-arkode
mv src/cvode/README src/README-cvode
mv src/cvodes/README src/README-cvodes
mv src/ida/README src/README-ida
mv src/idas/README src/README.idas
mv src/kinsol/README src/README-kinsol
mv src/nvec_ser/README src/README-nvec_ser
mv src/nvec_par/README src/README-nvec_par
mv src/nvec_pthreads/README src/README-nvec_pthreads
popd

%if 0%{?with_openmpi}
cp -a sundials-%{version} buildopenmpi_dir
%endif
%if 0%{?with_mpich}
cp -a sundials-%{version} buildmpich_dir
%endif

%build
pushd sundials-%{version}
mkdir -p build && cd build

## Blas
export LIBBLASLINK=-l%{blaslib}%{blasvar}
export INCBLAS=%{_includedir}/%{blaslib}
##

%if %{with debug}
export CFLAGS=""
cmake \
 -DCMAKE_VERBOSE_MAKEFILE:BOOL=ON \
 -DCMAKE_BUILD_TYPE:STRING=Debug \
 -DCMAKE_C_FLAGS_DEBUG:STRING="-O0 -g %{__global_ldflags} -I$INCBLAS" \
 -DCMAKE_Fortran_FLAGS_DEBUG:STRING="-O0 -g %{__global_ldflags} -I%{_fmoddir} -pthread -fopenmp -I$INCBLAS" \
 -DCMAKE_SHARED_LINKER_FLAGS_DEBUG:STRING="%{__global_ldflags} -lklu $LIBBLASLINK -lgomp -lsuperlumt_d -lpthread -lm" \
%else
%cmake3 \
 -DCMAKE_VERBOSE_MAKEFILE:BOOL=ON \
 -DCMAKE_BUILD_TYPE:STRING=Release \
 -DCMAKE_C_FLAGS_RELEASE:STRING="%{optflags} %{__global_ldflags} -pthread -fopenmp -I$INCBLAS" \
 -DCMAKE_Fortran_FLAGS_RELEASE:STRING="%{optflags} %{__global_ldflags} -pthread -fopenmp -I$INCBLAS" \
 -DCMAKE_SHARED_LINKER_FLAGS_RELEASE:STRING="%{__global_ldflags} -lklu $LIBBLASLINK -lgomp -lsuperlumt_d -lpthread -lm" \
%endif
 -DCMAKE_C_COMPILER:FILE=%{?dtsbindir}gcc \
 -DCMAKE_Fortran_COMPILER:FILE=%{?dtsbindir}gcc-gfortran \
 -DCMAKE_MODULE_LINKER_FLAGS:STRING="%{__global_ldflags}" \
 -DCMAKE_INSTALL_PREFIX=%{_prefix} \
 -DEXAMPLES_ENABLE=OFF -DEXAMPLES_INSTALL=OFF \
 -DCMAKE_SKIP_RPATH:BOOL=YES -DCMAKE_SKIP_INSTALL_RPATH:BOOL=YES \
 -DBUILD_SHARED_LIBS:BOOL=ON -DBUILD_STATIC_LIBS:BOOL=OFF \
 -DMPI_ENABLE:BOOL=OFF \
 -DCMAKE_Fortran_COMPILER:STRING=gfortran \
 -DFCMIX_ENABLE:BOOL=ON \
 -DF90_ENABLE:BOOL=ON \
 -DUSE_GENERIC_MATH:BOOL=ON \
 -DOPENMP_ENABLE:BOOL=ON \
 -DCXX_ENABLE:BOOL=ON \
 -DPTHREAD_ENABLE:BOOL=ON \
 -DLAPACK_ENABLE:BOOL=OFF \
 -DSUNDIALS_PRECISION:STRING=double \
 -DSUPERLUMT_ENABLE:BOOL=ON \
 -DSUPERLUMT_INCLUDE_DIR:PATH=%{_includedir}/SuperLUMT \
 -DSUPERLUMT_LIBRARY_DIR:PATH=%{_libdir} \
 -DSUPERLUMT_THREAD_TYPE:STRING=OpenMP \
 -DHYPRE_ENABLE:BOOL=OFF \
 -DKLU_ENABLE=ON -DKLU_LIBRARY_DIR:PATH=%{_libdir} -DKLU_INCLUDE_DIR:PATH=%{_includedir}/suitesparse -Wno-dev ..

%make_build
cd ..
popd

#############################################################################
#######
%if 0%{?with_openmpi}
pushd buildopenmpi_dir
##Set openmpi library's paths
sed -i 's|TARGETS sundials_nvecparallel_shared DESTINATION lib|TARGETS sundials_nvecparallel_shared DESTINATION %{_libdir}/openmpi/lib|g' src/nvec_par/CMakeLists.txt
sed -i 's|DESTINATION include/nvector|DESTINATION %{_includedir}/openmpi-%{_arch}/%{name}/nvector|g' src/nvec_par/CMakeLists.txt
sed -i 's|DESTINATION include/nvector|DESTINATION %{_includedir}/openmpi-%{_arch}/%{name}/nvector|g' src/nvec_parhyp/CMakeLists.txt
sed -i 's|TARGETS sundials_fnvecparallel_shared DESTINATION lib|TARGETS sundials_fnvecparallel_shared DESTINATION %{_libdir}/openmpi/lib|g' src/nvec_par/CMakeLists.txt
sed -i 's|TARGETS sundials_nvecparhyp_shared DESTINATION lib|TARGETS sundials_nvecparhyp_shared DESTINATION %{_libdir}/openmpi/lib|g' src/nvec_parhyp/CMakeLists.txt

mkdir -p build && cd build

## Blas
export LIBBLASLINK=-l%{blaslib}%{blasvar}
export INCBLAS=%{_includedir}/%{blaslib}
##

%{_openmpi_load}
export CC=mpicc
export CXX=mpicxx
export FC=mpif77
%if %{with debug}
export CFLAGS=""
cmake \
 -DCMAKE_VERBOSE_MAKEFILE:BOOL=ON \
 -DCMAKE_BUILD_TYPE:STRING=Debug \
 -DCMAKE_C_FLAGS_DEBUG:STRING="-O0 -g %{__global_ldflags} -I$INCBLAS" \
 -DCMAKE_Fortran_FLAGS_DEBUG:STRING="-O0 -g %{__global_ldflags} -I${MPI_FORTRAN_MOD_DIR} -pthread -fopenmp -I$INCBLAS" \
 -DCMAKE_SHARED_LINKER_FLAGS_DEBUG:STRING="%{__global_ldflags} -lm -lpthread $LIBBLASLINK -lgomp -lklu \
%ifnarch s390x
-L${MPI_LIB} -lHYPRE" \
%endif
%else
%cmake3 \
 -DCMAKE_VERBOSE_MAKEFILE:BOOL=ON \
 -DCMAKE_BUILD_TYPE:STRING=Release \
 -DCMAKE_C_FLAGS_RELEASE:STRING="%{optflags} %{__global_ldflags} -I$INCBLAS" \
 -DCMAKE_Fortran_FLAGS_RELEASE:STRING="%{optflags} %{__global_ldflags} -pthread -fopenmp -I$INCBLAS" \
%ifnarch s390x
 -DCMAKE_SHARED_LINKER_FLAGS_RELEASE:STRING="%{__global_ldflags} -lm -lpthread $LIBBLASLINK -lgomp -lklu -L${MPI_LIB} -lHYPRE" \
%else
 -DCMAKE_SHARED_LINKER_FLAGS_RELEASE:STRING="%{__global_ldflags} -lm -lpthread $LIBBLASLINK -lgomp -lklu" \
%endif
%endif
 -DCMAKE_INSTALL_PREFIX=%{_prefix} \
 -DEXAMPLES_ENABLE=OFF -DEXAMPLES_INSTALL=OFF \
 -DBUILD_SHARED_LIBS:BOOL=ON -DBUILD_STATIC_LIBS:BOOL=OFF \
 -DCMAKE_SKIP_RPATH:BOOL=YES -DCMAKE_SKIP_INSTALL_RPATH:BOOL=YES \
 -DMPI_ENABLE:BOOL=ON \
 -DMPI_MPICC:STRING=${MPI_BIN}/mpicc \
 -DMPI_RUN_COMMAND=${MPI_BIN}/mpirun \
 -DMPI_MPIF77:STRING=${MPI_BIN}/mpif77 \
 -DFCMIX_ENABLE:BOOL=ON \
 -DF90_ENABLE:BOOL=OFF \
 -DUSE_GENERIC_MATH:BOOL=ON \
 -DOPENMP_ENABLE:BOOL=ON \
 -DCXX_ENABLE:BOOL=ON \
 -DCMAKE_Fortran_COMPILER:STRING=${MPI_BIN}/mpif77 \
 -DPTHREAD_ENABLE:BOOL=ON \
 -DLAPACK_ENABLE:BOOL=OFF \
 -DSUPERLUMT_ENABLE:BOOL=OFF \
%ifnarch s390x
 -DHYPRE_ENABLE:BOOL=ON \
 -DHYPRE_INCLUDE_DIR:PATH=${MPI_INCLUDE}/hypre \
 -DHYPRE_LIBRARY_DIR:PATH=${MPI_LIB} \
%endif
 -DKLU_ENABLE=ON -DKLU_LIBRARY_DIR:PATH=%{_libdir} -DKLU_INCLUDE_DIR:PATH=%{_includedir}/suitesparse -Wno-dev ..

%make_build
%{_openmpi_unload}
cd ..
popd
%endif
######
#############################################################################
######
%if 0%{?with_mpich}
pushd buildmpich_dir
##Set mpich library's paths
sed -i 's|TARGETS sundials_nvecparallel_shared DESTINATION lib|TARGETS sundials_nvecparallel_shared DESTINATION %{_libdir}/mpich/lib|g' src/nvec_par/CMakeLists.txt
sed -i 's|DESTINATION include/nvector|DESTINATION %{_includedir}/mpich-%{_arch}/%{name}/nvector|g' src/nvec_par/CMakeLists.txt
sed -i 's|DESTINATION include/nvector|DESTINATION %{_includedir}/mpich-%{_arch}/%{name}/nvector|g' src/nvec_parhyp/CMakeLists.txt
sed -i 's|TARGETS sundials_fnvecparallel_shared DESTINATION lib|TARGETS sundials_fnvecparallel_shared DESTINATION %{_libdir}/mpich/lib|g' src/nvec_par/CMakeLists.txt
sed -i 's|TARGETS sundials_nvecparhyp_shared DESTINATION lib|TARGETS sundials_nvecparhyp_shared DESTINATION %{_libdir}/mpich/lib|g' src/nvec_parhyp/CMakeLists.txt

mkdir -p build && cd build

## Blas
export LIBBLASLINK=-l%{blaslib}%{blasvar}
export INCBLAS=%{_includedir}/%{blaslib}
##

%{_mpich_load}
export CC=mpicc
export CXX=mpicxx
export F77=mpif77
export FC=mpif90
%if %{with debug}
export CFLAGS=""
cmake \
 -DCMAKE_VERBOSE_MAKEFILE:BOOL=ON \
 -DCMAKE_BUILD_TYPE:STRING=Debug \
 -DCMAKE_C_FLAGS_DEBUG:STRING="-O0 -g %{__global_ldflags} -I$INCBLAS" \
 -DCMAKE_Fortran_FLAGS_DEBUG:STRING="-O0 -g %{__global_ldflags} -I${MPI_FORTRAN_MOD_DIR} -lm -lpthread -I$INCBLAS" \
 -DCMAKE_SHARED_LINKER_FLAGS_DEBUG:STRING="%{__global_ldflags} -lm -lpthread $LIBBLASLINK -lgomp -lklu \
%ifnarch s390x
-L${MPI_LIB} -lHYPRE" \
%endif
%else
%cmake3 \
 -DCMAKE_VERBOSE_MAKEFILE:BOOL=ON \
 -DCMAKE_BUILD_TYPE:STRING=Release \
 -DCMAKE_C_FLAGS_RELEASE:STRING="%{optflags} %{__global_ldflags}" \
 -DCMAKE_Fortran_FLAGS_RELEASE:STRING="%{optflags} -%{__global_ldflags} -lm -lpthread $LIBBLASLINK -lgomp" \
%ifnarch s390x
 -DCMAKE_SHARED_LINKER_FLAGS_RELEASE:STRING="%{__global_ldflags} -lm -lpthread $LIBBLASLINK -lgomp -lklu -L${MPI_LIB} -lHYPRE" \
%else
 -DCMAKE_SHARED_LINKER_FLAGS_RELEASE:STRING="%{__global_ldflags} -lm -lpthread $LIBBLASLINK -lgomp -lklu" \
%endif
%endif
 -DCMAKE_INSTALL_PREFIX=%{_prefix} \
 -DEXAMPLES_ENABLE=OFF -DEXAMPLES_INSTALL=OFF \
 -DBUILD_SHARED_LIBS:BOOL=ON -DBUILD_STATIC_LIBS:BOOL=OFF \
 -DCMAKE_SKIP_RPATH:BOOL=YES -DCMAKE_SKIP_INSTALL_RPATH:BOOL=YES \
 -DMPI_ENABLE:BOOL=ON \
 -DMPI_MPICC:STRING=${MPI_BIN}/mpicc \
 -DMPI_RUN_COMMAND=${MPI_BIN}mpirun \
 -DMPI_MPIF77:STRING=${MPI_BIN}/mpif77 \
 -DMPI_MPIF90:STRING=${MPI_BIN}/mpif90 \
 -DFCMIX_ENABLE:BOOL=ON \
 -DF90_ENABLE:BOOL=ON \
 -DUSE_GENERIC_MATH:BOOL=ON \
 -DOPENMP_ENABLE:BOOL=ON \
 -DCXX_ENABLE:BOOL=ON \
 -DCMAKE_Fortran_COMPILER:STRING=${MPI_BIN}/mpif77 \
 -DPTHREAD_ENABLE:BOOL=ON \
 -DLAPACK_ENABLE:BOOL=OFF \
 -DSUPERLUMT_ENABLE:BOOL=OFF \
%ifnarch s390x
 -DHYPRE_ENABLE:BOOL=ON \
 -DHYPRE_INCLUDE_DIR:PATH=${MPI_INCLUDE}/hypre \
 -DHYPRE_LIBRARY_DIR:PATH=${MPI_LIB} \
%endif
 -DKLU_ENABLE=ON -DKLU_LIBRARY_DIR:PATH=%{_libdir} -DKLU_INCLUDE_DIR:PATH=%{_includedir}/suitesparse -Wno-dev ..

%make_build
%{_mpich_unload}
cd ..
popd
%endif
######
#############################################################################

%install
%if 0%{?with_openmpi}
%{_openmpi_load}
%make_install -C buildopenmpi_dir/build

find %{buildroot}${MPI_LIB} -name "libsundials-*" -exec rename 's/libsundials/libsundials2/' {} \;
%{_openmpi_unload}
%endif

%if 0%{?with_mpich}
%{_mpich_load}
%make_install -C buildmpich_dir/build

find %{buildroot}${MPI_LIB} -name "libsundials-*" -exec rename 's/libsundials/libsundials2/' {} \;
%{_mpich_unload}
%endif

%make_install -C sundials-%{version}/build

%ldconfig_scriptlets

%files
%license sundials-%{version}/LICENSE
%doc sundials-%{version}/README sundials-%{version}/src/README-*
%{_libdir}/libsundials_nvecserial.so.*
%{_libdir}/libsundials_cvode.so.*
%{_libdir}/libsundials_cvodes.so.*
%{_libdir}/libsundials_arkode.so.* 
%{_libdir}/libsundials_ida.so.* 
%{_libdir}/libsundials_idas.so.* 
%{_libdir}/libsundials_kinsol.so.*
%{_libdir}/libsundials_nvecopenmp.so.*
%{_libdir}/libsundials_fnvecopenmp.so.*
%{_libdir}/libsundials_fnvecserial.so.*
%{_libdir}/libsundials_nvecpthreads.so.*
%{_libdir}/libsundials_fnvecpthreads.so.*

%files doc
%license sundials-%{version}/LICENSE
%doc sundials-%{version}/README
%doc sundials-%{version}/doc/cvode/cv_examples.pdf
%doc sundials-%{version}/doc/cvode/cv_guide.pdf
%doc sundials-%{version}/doc/kinsol/kin_examples.pdf
%doc sundials-%{version}/doc/kinsol/kin_guide.pdf
%doc sundials-%{version}/doc/cvodes/cvs_examples.pdf
%doc sundials-%{version}/doc/cvodes/cvs_guide.pdf
%doc sundials-%{version}/doc/ida/ida_examples.pdf
%doc sundials-%{version}/doc/ida/ida_guide.pdf
%doc sundials-%{version}/doc/arkode/*

%files devel
%{_libdir}/libsundials_nvecserial.so
%{_libdir}/libsundials_cvode.so
%{_libdir}/libsundials_cvodes.so
%{_libdir}/libsundials_arkode.so 
%{_libdir}/libsundials_ida.so 
%{_libdir}/libsundials_idas.so 
%{_libdir}/libsundials_kinsol.so
%{_libdir}/libsundials_nvecopenmp.so
%{_libdir}/libsundials_fnvecopenmp.so
%{_libdir}/libsundials_fnvecserial.so
%{_libdir}/libsundials_nvecpthreads.so
%{_libdir}/libsundials_fnvecpthreads.so
%{_libdir}/libsundials_*.a
%{_includedir}/%{name}/

%if 0%{?with_openmpi}
%files openmpi
%license sundials-%{version}/LICENSE
%doc sundials-%{version}/README sundials-%{version}/src/README-nvec_par
%{_libdir}/openmpi/lib/libsundials_nvecparallel.so.*
%{_libdir}/openmpi/lib/libsundials_fnvecparallel.so.*
%ifnarch s390x
%{_libdir}/openmpi/lib/libsundials_nvecparhyp.so.*
%endif

%files openmpi-devel
%{_includedir}/openmpi-%{_arch}/%{name}/
%{_libdir}/openmpi/lib/libsundials_nvecparallel.so
%{_libdir}/openmpi/lib/libsundials_fnvecparallel.so
%ifnarch s390x
%{_libdir}/openmpi/lib/libsundials_nvecparhyp.so
%endif
%endif

%if 0%{?with_mpich}
%files mpich
%license sundials-%{version}/LICENSE
%doc sundials-%{version}/README sundials-%{version}/src/README-nvec_par
%{_libdir}/mpich/lib/libsundials_nvecparallel.so.*
%{_libdir}/mpich/lib/libsundials_fnvecparallel.so.*
%ifnarch s390x
%{_libdir}/mpich/lib/libsundials_nvecparhyp.so.*
%endif

%files mpich-devel
%{_includedir}/mpich-%{_arch}/%{name}/
%{_libdir}/mpich/lib/libsundials_nvecparallel.so
%{_libdir}/mpich/lib/libsundials_fnvecparallel.so
%ifnarch s390x
%{_libdir}/mpich/lib/libsundials_nvecparhyp.so
%endif
%endif

%changelog
* Sat Jul 22 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.7.0-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 19 2023 Florian Weimer <fweimer@redhat.com> - 2.7.0-12
- C99 compatibility fixes

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.7.0-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Sat Jan 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.7.0-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.7.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.7.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Fri Aug 21 2020 Iñaki Úcar <iucar@fedoraproject.org> - 2.7.0-7
- https://fedoraproject.org/wiki/Changes/FlexiBLAS_as_BLAS/LAPACK_manager

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.7.0-6
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.7.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Sun Apr 05 2020 Antonio Trande <sagitterATfedoraproject.org> - 2.7.0-4
- Fix rhbz#1820991

* Fri Jan 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.7.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Aug 29 2019 Antonio Trande <sagitterATfedoraproject.org> - 2.7.0-2
- Use default library name
- Add Conflicts tags

* Sat Jul 27 2019 Antonio Trande <sagitterATfedoraproject.org> - 2.7.0-1
- Sundials2 libraries on EPEL
- Use devtooolset-8
