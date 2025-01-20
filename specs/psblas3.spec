ExcludeArch: %{ix86}

%global with_mpich 1
%global with_serial 0
%global with_check 1
%global with_openmpi 1

%if 0%{?with_serial}
%if 0%{?fedora}
%if %{?__isa_bits:%{__isa_bits}}%{!?__isa_bits:32} == 64
%global arch64 0
%else
%global arch64 0
%endif
%endif
%endif

%if 0%{?rhel}
%global arch64 0
%endif

%if 0%{?fedora} || 0%{?rhel} >= 9
%global blaslib flexiblas
%else
%global blaslib openblas
%endif

%global fc_optflags %{build_fflags}

%global major_version 3
%global major_minor %{major_version}.8
%global postrelease_version -2

Name: psblas3
Summary: Parallel Sparse Basic Linear Algebra Subroutines
Version: %{major_minor}.1
Release: 7.post2%{?dist}
License: BSD-3-Clause
URL: https://github.com/sfilippone/psblas3
Source0: https://github.com/sfilippone/psblas3/archive/v%{version}%{?postrelease_version}/psblas3-%{version}%{?postrelease_version}.tar.gz
Source1: psblas3-Makefile

# Call default Fedora ldflags when linker creates links 
Patch0: %{name}-fix_ldflags.patch

# Rename libraries for psblas3-serial64
Patch1: %{name}-rename_libs_for_arch64.patch

BuildRequires: gcc-gfortran
BuildRequires: gcc, gcc-c++
BuildRequires: suitesparse-devel
BuildRequires: %{blaslib}-devel
BuildRequires: metis-devel
BuildRequires: make

%description
The PSBLAS library, developed with the aim to facilitate the parallelization
of computationally intensive scientific applications,
is designed to address parallel implementation of iterative solvers for sparse
linear systems through the distributed memory paradigm.
It includes routines for multiplying sparse matrices by dense matrices,
solving block diagonal systems with triangular diagonal entries,
preprocessing sparse matrices, and contains additional routines for
dense matrix operations.
The current implementation of PSBLAS addresses a distributed memory execution
model operating with message passing.


%if 0%{?with_serial}
%package serial
Summary: %{name} serial mode
Requires: %{name}-common = %{version}-%{release}
Requires: gcc-gfortran%{?_isa}

%description serial
The PSBLAS library, developed with the aim to facilitate the parallelization
of computationally intensive scientific applications,
is designed to address parallel implementation of iterative solvers for sparse
linear systems through the distributed memory paradigm.
It includes routines for multiplying sparse matrices by dense matrices,
solving block diagonal systems with triangular diagonal entries,
preprocessing sparse matrices, and contains additional routines for
dense matrix operations.
The current implementation of PSBLAS addresses a distributed memory execution
model operating with message passing.
This is a PSBLAS version in pure serial mode.


%package serial-devel
Summary: Development files for %{name}
Requires: %{name}-serial%{?_isa} = %{version}-%{release}

%description serial-devel
Shared links, header files and static libraries for serial %{name}.
%endif


%package common
Summary: Documentation files for %{name}
BuildArch: noarch
#BuildRequires: texlive-tex4ht, texlive-latex, doxygen, ghostscript
#BuildRequires: texlive-fancybox, texlive-kpathsea, texlive-metafont
#BuildRequires: texlive-mfware, texlive-iftex

%description common
HTML, PDF and license files of %{name}.

########################################################
%if 0%{?arch64}
%package -n %{name}-serial64
Summary: %{name} for long-integer (8-byte) data
BuildRequires: suitesparse64-devel
BuildRequires: %{blaslib}-devel
BuildRequires: metis64-devel
Requires: %{name}-common = %{version}-%{release}

%description -n psblas3-serial64
The PSBLAS library, developed with the aim to facilitate the parallelization
of computationally intensive scientific applications,
is designed to address parallel implementation of iterative solvers for sparse
linear systems through the distributed memory paradigm.
It includes routines for multiplying sparse matrices by dense matrices,
solving block diagonal systems with triangular diagonal entries,
preprocessing sparse matrices, and contains additional routines for
dense matrix operations.
The current implementation of PSBLAS addresses a distributed memory execution
model operating with message passing.
This is a PSBLAS version for long-integer (8-byte) data.


%package -n %{name}-serial64-devel
Summary: The %{name}-serial64 headers and development-related files
Requires: %{name}-serial64%{?_isa} = %{version}-%{release}
Provides: %{name}-serial64-static = %{version}-%{release}

%description -n %{name}-serial64-devel
Shared links, header files and static libraries for %{name}-serial64.
%endif
##########################################################

########################################################
%if 0%{?with_openmpi}
%package openmpi
Summary: OpenMPI %{name}
BuildRequires: openmpi-devel
Requires: openmpi%{?_isa}
Requires: %{name}-common = %{version}-%{release}
Obsoletes: %{name}-serial < 0:3.8.1-1
Obsoletes: %{name}-serial64 < 0:3.8.1-1

%description openmpi
The PSBLAS library, developed with the aim to facilitate the parallelization
of computationally intensive scientific applications,
is designed to address parallel implementation of iterative solvers for sparse
linear systems through the distributed memory paradigm.
It includes routines for multiplying sparse matrices by dense matrices,
solving block diagonal systems with triangular diagonal entries,
preprocessing sparse matrices, and contains additional routines for
dense matrix operations.
The current implementation of PSBLAS addresses a distributed memory execution
model operating with message passing.
This is a OpenMPI PSBLAS version.

%package openmpi-static
Summary: OpenMPI static libraries of %{name}
Requires: openmpi%{?_isa}
Obsoletes: %{name}-openmpi-devel < 0:3.8.1-2

%description openmpi-static
The PSBLAS library, developed with the aim to facilitate the parallelization
of computationally intensive scientific applications,
is designed to address parallel implementation of iterative solvers for sparse
linear systems through the distributed memory paradigm.
It includes routines for multiplying sparse matrices by dense matrices,
solving block diagonal systems with triangular diagonal entries,
preprocessing sparse matrices, and contains additional routines for
dense matrix operations.
The current implementation of PSBLAS addresses a distributed memory execution
model operating with message passing.


%package openmpi-devel
Summary: The OpenMPI %{name} headers and development-related files
Requires: %{name}-openmpi%{?_isa} = %{version}-%{release}

%description openmpi-devel
Shared links, header files and static libraries for OpenMPI %{name}.
%endif
##########################################################
########################################################
%if 0%{?with_mpich}
%package mpich
Summary: MPICH %{name}
BuildRequires:	mpich-devel
Requires: mpich%{?_isa}
Requires: %{name}-common = %{version}-%{release}
Obsoletes: %{name}-serial < 0:3.8.1-1
Obsoletes: %{name}-serial64 < 0:3.8.1-1

%description mpich
The PSBLAS library, developed with the aim to facilitate the parallelization
of computationally intensive scientific applications,
is designed to address parallel implementation of iterative solvers for sparse
linear systems through the distributed memory paradigm.
It includes routines for multiplying sparse matrices by dense matrices,
solving block diagonal systems with triangular diagonal entries,
preprocessing sparse matrices, and contains additional routines for
dense matrix operations.
The current implementation of PSBLAS addresses a distributed memory execution
model operating with message passing.
This is a MPICH PSBLAS version.

%package mpich-static
Summary: MPICH static libraries of %{name}
Requires: mpich%{?_isa}
Obsoletes: %{name}-mpich-devel < 0:3.8.1-2

%description mpich-static
The PSBLAS library, developed with the aim to facilitate the parallelization
of computationally intensive scientific applications,
is designed to address parallel implementation of iterative solvers for sparse
linear systems through the distributed memory paradigm.
It includes routines for multiplying sparse matrices by dense matrices,
solving block diagonal systems with triangular diagonal entries,
preprocessing sparse matrices, and contains additional routines for
dense matrix operations.
The current implementation of PSBLAS addresses a distributed memory execution
model operating with message passing.


%package mpich-devel
Summary: The MPICH %{name} headers and development-related files
Requires: %{name}-mpich%{?_isa} = %{version}-%{release}

%description mpich-devel
Shared links, header files and static libraries for MPICH %{name}.
%endif
##########################################################

%prep
%setup -qc -n psblas3-%{version}%{?postrelease_version}

pushd psblas3-%{version}%{?postrelease_version}
%patch -P 0 -p0
popd

#######################################################
## Copy source for MPI versions
%if 0%{?with_openmpi}
cp -a psblas3-%{version}%{?postrelease_version} openmpi-build
%endif
%if 0%{?with_mpich}
cp -a psblas3-%{version}%{?postrelease_version} mpich-build
%endif
######################################################

#######################################################
## Copy source for long-integer version
%if 0%{?arch64}
cp -a psblas3-%{version}%{?postrelease_version} build64
pushd build64
%patch -P 1 -p1
popd
%endif
#####################################################

%build
%if 0%{?with_serial}
cd psblas3-%{version}%{?postrelease_version}

# '-Werror=format-security' flag is not valid for gfortran
FC_OPT_FLAGS=$(echo "%{?fc_optflags}" | %{__sed} -e 's/-Werror=format-security//')
%configure \
 --enable-serial --with-fcopt="$FC_OPT_FLAGS -Wno-unused-variable -Wno-unused-dummy-argument -fPIC" \
 --with-ccopt="%{build_cflags} -fPIC" --with-include-path="%{_includedir}/%{blaslib} -I%{_fmoddir}" \
 --with-metis=-lmetis --with-amd=-lamd --with-blas=-l%{blaslib} --with-lapack= \
 --with-amdincdir=%{_includedir}/suitesparse --with-lpk=4 --includedir=%{_includedir}/%{name}-serial \
 --enable-bootstrap --enable-languages=c,c++,fortran,lto --with-bugurl=http://bugzilla.redhat.com/bugzilla \
 --enable-shared --enable-threads=posix --enable-checking=release --enable-multilib --with-system-zlib --enable-__cxa_atexit \
 --disable-libunwind-exceptions --enable-gnu-unique-object --enable-linker-build-id --with-gcc-major-version-only \
 --enable-libstdcxx-backtrace --with-linker-hash-style=gnu --enable-plugin --enable-initfini-array --enable-offload-targets=nvptx-none \
 --without-cuda-driver --enable-offload-defaulted --enable-gnu-indirect-function --enable-cet --with-tune=generic --build=x86_64-redhat-linux \
 --with-build-config=bootstrap-lto --enable-link-serialization=1

%make_build

# Make shared libraries
pushd lib
gfortran %{optflags} -fPIC -shared %{__global_ldflags} -fallow-argument-mismatch -frecursive -I../modules/ -Wl,--whole-archive libpsb_base.a -Wl,-no-whole-archive -Wl,-Bdynamic -L%{_libdir} -l%{blaslib} -lgfortran -lm -Wl,-soname,libpsb_base.so.%{major_minor} -o libpsb_base.so.%{major_minor}
ln -sf libpsb_base.so.%{major_minor} ./libpsb_base.so.%{major_version}
ln -sf libpsb_base.so.%{major_minor} ./libpsb_base.so

gfortran %{optflags} -fPIC -shared %{__global_ldflags} -I../modules/ -Wl,--whole-archive libpsb_krylov.a -Wl,-no-whole-archive -Wl,-Bdynamic -L./ -lpsb_base -L%{_libdir} -l%{blaslib} -lgfortran -lm -Wl,-soname,libpsb_krylov.so.%{major_minor} -o libpsb_krylov.so.%{major_minor}
ln -sf libpsb_krylov.so.%{major_minor} ./libpsb_krylov.so.%{major_version}
ln -sf libpsb_krylov.so.%{major_minor} ./libpsb_krylov.so

gfortran %{optflags} -fPIC -shared %{__global_ldflags} -I../modules/ -Wl,--whole-archive libpsb_prec.a -Wl,-no-whole-archive -Wl,-Bdynamic -L./ -lpsb_base -L%{_libdir} -l%{blaslib} -lgfortran -lm -Wl,-soname,libpsb_prec.so.%{major_minor} -o libpsb_prec.so.%{major_minor}
ln -sf libpsb_prec.so.%{major_minor} ./libpsb_prec.so.%{major_version}
ln -sf libpsb_prec.so.%{major_minor} ./libpsb_prec.so

gfortran %{optflags} -fPIC -shared %{__global_ldflags} -I../modules/ -Wl,--whole-archive libpsb_util.a -Wl,-no-whole-archive -Wl,-Bdynamic -L./ -lpsb_base -L%{_libdir} -l%{blaslib} -lmetis -lamd -lgfortran -lm -Wl,-soname,libpsb_util.so.%{major_minor} -o libpsb_util.so.%{major_minor}
ln -sf libpsb_util.so.%{major_minor} ./libpsb_util.so.%{major_version}
ln -sf libpsb_util.so.%{major_minor} ./libpsb_util.so

gcc %{optflags} -fPIC -shared %{__global_ldflags} -Wl,--whole-archive libpsb_cbind.a -Wl,-no-whole-archive -Wl,-Bdynamic -L./ -lpsb_base -lpsb_prec -lpsb_krylov -lpsb_util -L%{_libdir} -lmetis -lamd -lm -Wl,-soname,libpsb_cbind.so.%{major_minor} -o libpsb_cbind.so.%{major_minor}
ln -sf libpsb_cbind.so.%{major_minor} ./libpsb_cbind.so.%{major_version}
ln -sf libpsb_cbind.so.%{major_minor} ./libpsb_cbind.so
popd

cd ../

%if 0%{?arch64}
cd build64

FC_OPT_FLAGS=$(echo "%{?fc_optflags}" | %{__sed} -e 's/-Werror=format-security//')
%configure \
 --enable-serial --with-fcopt="$FC_OPT_FLAGS -Wno-unused-variable -Wno-unused-dummy-argument -fPIC" \
 --with-ccopt="%{build_cflags} -fPIC" --with-include-path="%{_includedir}/%{blaslib} -I%{_fmoddir}" \
 --with-metis=-lmetis64 --with-metisincfile=metis64.h --with-metisincdir=%{_includedir} --with-amd=-lamd64 --with-blas=-l%{blaslib}64 --with-lapack= \
 --with-amdincdir=%{_includedir}/suitesparse --with-lpk=8 --includedir=%{_includedir}/%{name}-serial64 \
 --enable-bootstrap --enable-languages=c,c++,fortran,lto --with-bugurl=http://bugzilla.redhat.com/bugzilla \
 --enable-shared --enable-threads=posix --enable-checking=release --enable-multilib --with-system-zlib --enable-__cxa_atexit \
 --disable-libunwind-exceptions --enable-gnu-unique-object --enable-linker-build-id --with-gcc-major-version-only \
 --enable-libstdcxx-backtrace --with-linker-hash-style=gnu --enable-plugin --enable-initfini-array --enable-offload-targets=nvptx-none \
 --without-cuda-driver --enable-offload-defaulted --enable-gnu-indirect-function --enable-cet --with-tune=generic --build=x86_64-redhat-linux \
 --with-build-config=bootstrap-lto --enable-link-serialization=1

%make_build

# Make shared libraries
pushd lib
gfortran -shared %{__global_ldflags} -I../modules/ -Wl,--whole-archive libpsb64_base.a -Wl,-no-whole-archive -Wl,-Bdynamic -L%{_libdir} -l%{blaslib}64 -lgfortran -lm -Wl,-soname,libpsb64_base.so.%{major_minor} -o libpsb64_base.so.%{major_minor}
ln -sf libpsb64_base.so.%{major_minor} ./libpsb64_base.so.%{major_version}
ln -sf libpsb64_base.so.%{major_minor} ./libpsb64_base.so

gfortran -shared %{__global_ldflags} -I../modules/ -Wl,--whole-archive libpsb64_krylov.a -Wl,-no-whole-archive -Wl,-Bdynamic -L./ -lpsb64_base -L%{_libdir} -l%{blaslib}64 -lgfortran -lm -Wl,-soname,libpsb64_krylov.so.%{major_minor} -o libpsb64_krylov.so.%{major_minor}
ln -sf libpsb64_krylov.so.%{major_minor} ./libpsb64_krylov.so.%{major_version}
ln -sf libpsb64_krylov.so.%{major_minor} ./libpsb64_krylov.so

gfortran -shared %{__global_ldflags} -I../modules/ -Wl,--whole-archive libpsb64_prec.a -Wl,-no-whole-archive -Wl,-Bdynamic -L./ -lpsb64_base -L%{_libdir} -l%{blaslib}64 -lgfortran -lm -Wl,-soname,libpsb64_prec.so.%{major_minor} -o libpsb64_prec.so.%{major_minor}
ln -sf libpsb64_prec.so.%{major_minor} ./libpsb64_prec.so.%{major_version}
ln -sf libpsb64_prec.so.%{major_minor} ./libpsb64_prec.so

gfortran -shared %{__global_ldflags} -I../modules/ -Wl,--whole-archive libpsb64_util.a -Wl,-no-whole-archive -Wl,-Bdynamic -L./ -lpsb64_base -L%{_libdir} -l%{blaslib}64 -lmetis64 -lamd64 -lgfortran -lm -Wl,-soname,libpsb64_util.so.%{major_minor} -o libpsb64_util.so.%{major_minor}
ln -sf libpsb64_util.so.%{major_minor} ./libpsb64_util.so.%{major_version}
ln -sf libpsb64_util.so.%{major_minor} ./libpsb64_util.so

gcc -shared %{__global_ldflags} -fPIC -Wl,--whole-archive libpsb64_cbind.a -Wl,-no-whole-archive -Wl,-Bdynamic -L./ -lpsb64_base -lpsb64_prec -lpsb64_krylov -lpsb64_util -L%{_libdir} -lmetis64 -lamd64 -lm -Wl,-soname,libpsb64_cbind.so.%{major_minor} -o libpsb64_cbind.so.%{major_minor}
ln -sf libpsb64_cbind.so.%{major_minor} ./libpsb64_cbind.so.%{major_version}
ln -sf libpsb64_cbind.so.%{major_minor} ./libpsb64_cbind.so
popd

cd ../

%endif
%endif

#######################################################
## Build MPI versions
%if 0%{?with_openmpi}
pushd openmpi-build

%{_openmpi_load}
export CC=mpicc
export CXX=mpic++
FC_OPT_FLAGS=$(echo "%{?fc_optflags}" | %{__sed} -e 's/-Werror=format-security//')
%configure \
 --with-fcopt="$FC_OPT_FLAGS -Wno-unused-variable -Wno-unused-dummy-argument -fPIC -I${MPI_FORTRAN_MOD_DIR}" \
 --with-ccopt="%{build_cflags} -fPIC" --with-include-path="%{_includedir}/%{blaslib} -I${MPI_FORTRAN_MOD_DIR}" \
 MPIFC=mpifort MPICC=mpicc MPICXX=mpic++ \
 --with-metis=-lmetis --with-amd=-lamd --with-blas=-l%{blaslib} --with-lapack= \
 --with-amdincdir=%{_includedir}/suitesparse --with-lpk=4 --includedir=$MPI_INCLUDE/%{name} \
 --enable-bootstrap --enable-languages=c,c++,fortran,lto --with-bugurl=http://bugzilla.redhat.com/bugzilla \
 --enable-shared --enable-threads=posix --enable-checking=release --enable-multilib --with-system-zlib --enable-__cxa_atexit \
 --disable-libunwind-exceptions --enable-gnu-unique-object --enable-linker-build-id --with-gcc-major-version-only \
 --enable-libstdcxx-backtrace --with-linker-hash-style=gnu --enable-plugin --enable-initfini-array --enable-offload-targets=nvptx-none \
 --without-cuda-driver --enable-offload-defaulted --enable-gnu-indirect-function --enable-cet --with-tune=generic --build=x86_64-redhat-linux \
 --with-build-config=bootstrap-lto --enable-link-serialization=1

%make_build

# Make shared libraries
cd lib
mpifort %{optflags} -fPIC -shared %{__global_ldflags} -I../modules/ -Wl,--whole-archive libpsb_base.a -Wl,-no-whole-archive -Wl,-Bdynamic -L$MPI_LIB -Wl,-rpath -Wl,$MPI_LIB -Wl,--enable-new-dtags -lmpi_mpifh -lmpi -L%{_libdir} -l%{blaslib} -lgfortran -lm -Wl,-soname,libpsb_base.so.%{major_minor} -o libpsb_base.so.%{major_minor}
ln -sf libpsb_base.so.%{major_minor} ./libpsb_base.so.%{major_version}
ln -sf libpsb_base.so.%{major_minor} ./libpsb_base.so

mpifort %{optflags} -fPIC -shared %{__global_ldflags} -I../modules/ -Wl,--whole-archive libpsb_krylov.a -Wl,-no-whole-archive -Wl,-Bdynamic -L./ -lpsb_base -L$MPI_LIB -Wl,-rpath -Wl,$MPI_LIB -Wl,--enable-new-dtags -lmpi_mpifh -lmpi -L%{_libdir} -l%{blaslib} -lmetis -lamd -lgfortran -lm -lrt -Wl,-soname,libpsb_krylov.so.%{major_minor} -o libpsb_krylov.so.%{major_minor}
ln -sf libpsb_krylov.so.%{major_minor} ./libpsb_krylov.so.%{major_version}
ln -sf libpsb_krylov.so.%{major_minor} ./libpsb_krylov.so

mpifort %{optflags} -fPIC -shared %{__global_ldflags} -I../modules/ -Wl,--whole-archive libpsb_prec.a -Wl,-no-whole-archive -Wl,-Bdynamic -L./ -lpsb_base -L$MPI_LIB -Wl,-rpath -Wl,$MPI_LIB -Wl,--enable-new-dtags -lmpi_mpifh -lmpi -L%{_libdir} -l%{blaslib} -lmetis -lamd -lgfortran -lm -lrt -Wl,-soname,libpsb_prec.so.%{major_minor} -o libpsb_prec.so.%{major_minor}
ln -sf libpsb_prec.so.%{major_minor} ./libpsb_prec.so.%{major_version}
ln -sf libpsb_prec.so.%{major_minor} ./libpsb_prec.so

mpifort %{optflags} -fPIC -shared %{__global_ldflags} -I../modules/ -Wl,--whole-archive libpsb_util.a -Wl,-no-whole-archive -Wl,-Bdynamic -L./ -lpsb_base -L$MPI_LIB -Wl,-rpath -Wl,$MPI_LIB -Wl,--enable-new-dtags -lmpi_mpifh -lmpi -L%{_libdir} -l%{blaslib} -lmetis -lamd -lgfortran -lm -lrt -Wl,-soname,libpsb_util.so.%{major_minor} -o libpsb_util.so.%{major_minor}
ln -sf libpsb_util.so.%{major_minor} ./libpsb_util.so.%{major_version}
ln -sf libpsb_util.so.%{major_minor} ./libpsb_util.so

mpicc %{optflags} -fPIC -shared %{__global_ldflags} -Wl,--whole-archive libpsb_cbind.a -Wl,-no-whole-archive -Wl,-Bdynamic -L./ -lpsb_base -lpsb_prec -lpsb_krylov -lpsb_util -L$MPI_LIB -Wl,-rpath -Wl,$MPI_LIB -Wl,--enable-new-dtags -lgfortran -lmpi_mpifh -lmpi -L%{_libdir} -l%{blaslib} -lmetis -lamd -lm -lrt -Wl,-soname,libpsb_cbind.so.%{major_minor} -o libpsb_cbind.so.%{major_minor}
ln -sf libpsb_cbind.so.%{major_minor} ./libpsb_cbind.so.%{major_version}
ln -sf libpsb_cbind.so.%{major_minor} ./libpsb_cbind.so
cd ../

%{_openmpi_unload}
popd
%endif

%if 0%{?with_mpich}
pushd mpich-build

%{_mpich_load}
export CC=mpicc
FC_OPT_FLAGS=$(echo "%{?fc_optflags}" | %{__sed} -e 's/-Werror=format-security//')
%configure \
 --with-fcopt="$FC_OPT_FLAGS -Wno-unused-variable -Wno-unused-dummy-argument -fPIC -I${MPI_FORTRAN_MOD_DIR}" \
 --with-ccopt="%{build_cflags} -fPIC" --with-include-path="%{_includedir}/%{blaslib} -I${MPI_FORTRAN_MOD_DIR}" \
 MPIFC=mpif90 MPICC=mpicc \
 --with-metis=-lmetis --with-amd=-lamd --with-blas=-l%{blaslib} --with-lapack= \
 --with-amdincdir=%{_includedir}/suitesparse --with-lpk=4 --includedir=$MPI_INCLUDE/%{name} \
 --enable-bootstrap --enable-languages=c,c++,fortran,lto --with-bugurl=http://bugzilla.redhat.com/bugzilla \
 --enable-shared --enable-threads=posix --enable-checking=release --enable-multilib --with-system-zlib --enable-__cxa_atexit \
 --disable-libunwind-exceptions --enable-gnu-unique-object --enable-linker-build-id --with-gcc-major-version-only \
 --enable-libstdcxx-backtrace --with-linker-hash-style=gnu --enable-plugin --enable-initfini-array --enable-offload-targets=nvptx-none \
 --without-cuda-driver --enable-offload-defaulted --enable-gnu-indirect-function --enable-cet --with-tune=generic --build=x86_64-redhat-linux \
 --with-build-config=bootstrap-lto --enable-link-serialization=1

%make_build

# Make shared libraries
cd lib

%if 0%{?fedora}
export MPIFLIB=" -lmpifort -lmpi"
%else
export MPIFLIB=" -lmpich -lfmpich " 
%endif

mpif90 %{optflags} -fPIC -shared %{__global_ldflags} -I../modules/ -Wl,--whole-archive libpsb_base.a -Wl,-no-whole-archive -Wl,-Bdynamic -L$MPI_LIB -Wl,-rpath -Wl,$MPI_LIB -Wl,-z,noexecstack $MPIFLIB -L%{_libdir} -l%{blaslib} -lgfortran -lm -Wl,-soname,libpsb_base.so.%{major_minor} -o libpsb_base.so.%{major_minor}
ln -sf libpsb_base.so.%{major_minor} ./libpsb_base.so.%{major_version}
ln -sf libpsb_base.so.%{major_minor} ./libpsb_base.so

mpif90 %{optflags} -fPIC -shared %{__global_ldflags} -I../modules/ -Wl,--whole-archive libpsb_krylov.a -Wl,-no-whole-archive -Wl,-Bdynamic -L./ -lpsb_base -L$MPI_LIB -Wl,-rpath -Wl,$MPI_LIB -Wl,-z,noexecstack $MPIFLIB -L%{_libdir} -l%{blaslib} -lmetis -lamd -lgfortran -lm -lrt -Wl,-soname,libpsb_krylov.so.%{major_minor} -o libpsb_krylov.so.%{major_minor}
ln -sf libpsb_krylov.so.%{major_minor} ./libpsb_krylov.so.%{major_version}
ln -sf libpsb_krylov.so.%{major_minor} ./libpsb_krylov.so

mpif90 %{optflags} -fPIC -shared %{__global_ldflags} -I../modules/ -Wl,--whole-archive libpsb_prec.a -Wl,-no-whole-archive -Wl,-Bdynamic -L./ -lpsb_base -L$MPI_LIB -Wl,-rpath -Wl,$MPI_LIB -Wl,-z,noexecstack $MPIFLIB -L%{_libdir} -l%{blaslib} -lmetis -lamd -lgfortran -lm -lrt -Wl,-soname,libpsb_prec.so.%{major_minor} -o libpsb_prec.so.%{major_minor}
ln -sf libpsb_prec.so.%{major_minor} ./libpsb_prec.so.%{major_version}
ln -sf libpsb_prec.so.%{major_minor} ./libpsb_prec.so

mpif90 %{optflags} -fPIC -shared %{__global_ldflags} -I../modules/ -Wl,--whole-archive libpsb_util.a -Wl,-no-whole-archive -Wl,-Bdynamic -L./ -lpsb_base -L$MPI_LIB -Wl,-rpath -Wl,$MPI_LIB $MPIFLIB -Wl,-z,noexecstack -L%{_libdir} -l%{blaslib} -lmetis -lamd -lgfortran -lm -lrt -Wl,-soname,libpsb_util.so.%{major_minor} -o libpsb_util.so.%{major_minor}
ln -sf libpsb_util.so.%{major_minor} ./libpsb_util.so.%{major_version}
ln -sf libpsb_util.so.%{major_minor} ./libpsb_util.so

mpicc %{optflags} -fPIC -shared %{__global_ldflags} -Wl,--whole-archive libpsb_cbind.a -Wl,-no-whole-archive -Wl,-Bdynamic -L./ -lpsb_base -lpsb_prec -lpsb_krylov -lpsb_util -L$MPI_LIB -Wl,-rpath -Wl,$MPI_LIB $MPIFLIB -Wl,-z,noexecstack -L%{_libdir} -l%{blaslib} -lmetis -lgfortran -lamd -lm -lrt -Wl,-soname,libpsb_cbind.so.%{major_minor} -o libpsb_cbind.so.%{major_minor}
ln -sf libpsb_cbind.so.%{major_minor} ./libpsb_cbind.so.%{major_version}
ln -sf libpsb_cbind.so.%{major_minor} ./libpsb_cbind.so
cd ../

%{_mpich_unload}
popd
%endif
#######################################################

%install
%if 0%{?with_serial}
pushd psblas3-%{version}%{?postrelease_version}
mkdir -p $RPM_BUILD_ROOT%{_includedir}/%{name}-serial
mkdir -p $RPM_BUILD_ROOT%{_fmoddir}/%{name}-serial

cd lib
cp --preserve=all -P *.so* $RPM_BUILD_ROOT%{_libdir}/
install -pm 644 *.a $RPM_BUILD_ROOT%{_libdir}/
rm -f *.a
cd ../

install -pm 644 modules/*.mod $RPM_BUILD_ROOT%{_fmoddir}/%{name}-serial
install -pm 644 include/*.h $RPM_BUILD_ROOT%{_includedir}/%{name}-serial/
popd
%endif

%if 0%{?arch64}
pushd build64
mkdir -p $RPM_BUILD_ROOT%{_includedir}/%{name}-serial64
mkdir -p $RPM_BUILD_ROOT%{_fmoddir}/%{name}-serial64

cd lib
cp --preserve=all -P *.so* $RPM_BUILD_ROOT%{_libdir}/
install -pm 644 *.a $RPM_BUILD_ROOT%{_libdir}/
rm -f *.a
cd ../

install -pm 644 modules/*.mod $RPM_BUILD_ROOT%{_fmoddir}/%{name}-serial64
install -pm 644 include/*.h $RPM_BUILD_ROOT%{_includedir}/%{name}-serial64/
popd
%endif

#######################################################
## Install MPI versions
%if 0%{?with_openmpi}
pushd openmpi-build
%{_openmpi_load}
mkdir -p $RPM_BUILD_ROOT$MPI_LIB
mkdir -p $RPM_BUILD_ROOT$MPI_INCLUDE/%{name}
mkdir -p $RPM_BUILD_ROOT$MPI_FORTRAN_MOD_DIR/%{name}

cd lib
cp --preserve=all -P *.so* $RPM_BUILD_ROOT$MPI_LIB/
install -pm 644 *.a $RPM_BUILD_ROOT$MPI_LIB/
rm -f *.a
cd ../

install -pm 644 modules/*.mod $RPM_BUILD_ROOT$MPI_FORTRAN_MOD_DIR/%{name}
install -pm 644 include/*.h $RPM_BUILD_ROOT$MPI_INCLUDE/%{name}/
%{_openmpi_unload}
popd
%endif

%if 0%{?with_mpich}
pushd mpich-build
%{_mpich_load}
mkdir -p $RPM_BUILD_ROOT$MPI_LIB
mkdir -p $RPM_BUILD_ROOT$MPI_INCLUDE/%{name}
mkdir -p $RPM_BUILD_ROOT$MPI_FORTRAN_MOD_DIR/%{name}

cd lib
cp --preserve=all -P *.so* $RPM_BUILD_ROOT$MPI_LIB/
install -pm 644 *.a $RPM_BUILD_ROOT$MPI_LIB/
rm -f *.a
cd ../

install -pm 644 modules/*.mod $RPM_BUILD_ROOT$MPI_FORTRAN_MOD_DIR/%{name}
install -pm 644 include/*.h $RPM_BUILD_ROOT$MPI_INCLUDE/%{name}/
%{_mpich_unload}
popd
%endif
#######################################################

%if 0%{?with_check}
%check
%if 0%{?with_serial}
pushd psblas3-%{version}%{?postrelease_version}
export LINKOPT="%{__global_ldflags} -lgfortran -l%{blaslib} -fallow-argument-mismatch -frecursive -I../../modules/"
export LD_LIBRARY_PATH=$RPM_BUILD_ROOT%{_libdir}
make check
popd
%endif

%if 0%{?arch64}
pushd build64
export LINKOPT="%{__global_ldflags} -lgfortran -l%{blaslib} -fallow-argument-mismatch -frecursive -I../../modules/"
export LD_LIBRARY_PATH=$RPM_BUILD_ROOT%{_libdir}:%{_libdir}
make check
popd
%endif

%if 0%{?with_openmpi}
pushd openmpi-build
%{_openmpi_load}
export LINKOPT="%{__global_ldflags} -lgfortran -l%{blaslib} -L$MPI_LIB -fallow-argument-mismatch -frecursive -I../../modules/"
export LD_LIBRARY_PATH=$RPM_BUILD_ROOT$MPI_LIB:$MPI_LIB
make check
%{_openmpi_unload}
popd
%endif

%if 0%{?with_mpich}
pushd mpich-build
%{_mpich_load}
%if 0%{?fedora}
export MPIFLIB="-lmpifort -lmpi"
%else
export MPIFLIB="-lmpich -lfmpich " 
%endif
export LINKOPT="%{__global_ldflags} -lgfortran -l%{blaslib} -L$MPI_LIB $MPIFLIB -fallow-argument-mismatch -frecursive -I../../modules/"
export LD_LIBRARY_PATH=$RPM_BUILD_ROOT$MPI_LIB:$MPI_LIB
make check
%{_mpich_unload}
popd
%endif
%endif

%if 0%{?with_serial}
%files serial
%{_libdir}/*.so.%{major_minor}
%{_libdir}/*.so.%{major_version}

%files serial-devel
%{_libdir}/*.so
%{_libdir}/*.a
%{_fmoddir}/%{name}-serial/
%{_includedir}/%{name}-serial/

%if 0%{?arch64}
%files -n %{name}-serial64
%{_libdir}/libpsb64*.so.%{major_minor}
%{_libdir}/libpsb64*.so.%{major_version}

%files -n %{name}-serial64-devel
%{_libdir}/libpsb64*.so
%{_libdir}/libpsb64*.a
%{_fmoddir}/%{name}-serial64/
%{_includedir}/%{name}-serial64/
%endif
%endif

%files common
%doc psblas3-%{version}%{?postrelease_version}/README.md psblas3-%{version}%{?postrelease_version}/Changelog
%doc psblas3-%{version}%{?postrelease_version}/ReleaseNews
%doc psblas3-%{version}%{?postrelease_version}/docs/html psblas3-%{version}%{?postrelease_version}/docs/*.pdf
%license psblas3-%{version}%{?postrelease_version}/LICENSE

#######################################################
## MPI versions
%if 0%{?with_openmpi}
%files openmpi
%{_libdir}/openmpi/lib/*.so.%{major_minor}
%{_libdir}/openmpi/lib/*.so.%{major_version}

%files openmpi-static
%{_libdir}/openmpi/lib/*.a

%files openmpi-devel
%{_libdir}/openmpi/lib/*.so
%{_includedir}/openmpi-%{_arch}/%{name}/
%if 0%{?fedora} || 0%{?rhel} > 7
%{_fmoddir}/openmpi/%{name}/
%else
%{_fmoddir}/openmpi-%{_arch}/%{name}/
%endif
%endif

%if 0%{?with_mpich}
%files mpich
%{_libdir}/mpich/lib/*.so.%{major_minor}
%{_libdir}/mpich/lib/*.so.%{major_version}

%files mpich-static
%{_libdir}/mpich/lib/*.a

%files mpich-devel
%{_libdir}/mpich/lib/*.so
%{_includedir}/mpich-%{_arch}/%{name}/
%if 0%{?fedora} || 0%{?rhel} > 7
%{_fmoddir}/mpich/%{name}/
%else
%{_fmoddir}/mpich-%{_arch}/%{name}/
%endif
%endif
######################################################

%changelog
* Sat Jan 18 2025 Fedora Release Engineering <releng@fedoraproject.org> - 3.8.1-7.post2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 3.8.1-6.post2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Sun Feb 04 2024 Orion Poplawski <orion@nwra.com> - 3.8.1-5.post2
- Rebuild with suitesparse 7.6.0

* Fri Jan 26 2024 Fedora Release Engineering <releng@fedoraproject.org> - 3.8.1-4.post2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 3.8.1-3.post2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Dec 17 2023 Antonio Trande <sagitter@fedoraproject.org> - 3.8.1-2.post2
- Static packages obsolete older devel packages

* Sat Dec 16 2023 Antonio Trande <sagitter@fedoraproject.org> - 3.8.1-1.post2
- Release 3.8.1 post-release 2
- Exclude serial* libraries (not fully supported)

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 3.8.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Sun Jul 16 2023 Antonio Trande <sagitter@fedoraproject.org> - 3.8.0-6
- Renew SPEC file

* Tue Feb 07 2023 Antonio Trande <sagitter@fedoraproject.org> - 3.8.0-5
- Drop OpenMPI support on i686

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 3.8.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Sat Aug 06 2022 Antonio Trande <sagitter@fedoraproject.org> - 3.8.0-3
- Release 3.8.0-2
- Restore Make's parallel jobs

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 3.8.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Sun Jun 05 2022 Antonio Trande <sagitter@fedoraproject.org> - 3.8.0-1
- Release 3.8.0-1

* Sat Apr 23 2022 Antonio Trande <sagitter@fedoraproject.org> - 3.7.1-2
- Rebuild for superlu_dist-7.2.0

* Mon Apr 18 2022 Antonio Trande <sagitter@fedoraproject.org> - 3.7.1-1
- Release 3.7.1

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 3.7.0.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Sun Sep 26 2021 Antonio Trande <sagitter@fedoraproject.org> - 3.7.0.2-1
- Release 3.7.0.2

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 3.7.0.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Sun May 23 2021 Antonio Trande <sagitter@fedoraproject.org> - 3.7.0.1-2
- Fix mpirun commands

* Thu May 20 2021 Antonio Trande <sagitter@fedoraproject.org> - 3.7.0.1-1
- Release 3.7.0.1

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 3.6.1-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Sat Dec 05 2020 Antonio Trande <sagitter@fedoraproject.org> - 3.6.1-13
- Use devtoolset-6 on EPEL7

* Sat Dec 05 2020 Antonio Trande <sagitter@fedoraproject.org> - 3.6.1-12
- Rebuild on EPEL7

* Thu Aug 13 2020 IÃ±aki Ãšcar <iucar@fedoraproject.org> - 3.6.1-11
- https://fedoraproject.org/wiki/Changes/FlexiBLAS_as_BLAS/LAPACK_manager

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.6.1-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Sat Jul 18 2020 Antonio Trande <sagitter@fedoraproject.org> - 3.6.1-9
- Release 3.6.1-4

* Sun Jun 28 2020 Antonio Trande <sagitter@fedoraproject.org> - 3.6.1-8
- Release 3.6.1-3

* Sat Apr 11 2020 Antonio Trande <sagitter@fedoraproject.org> - 3.6.1-7
- Fix Fortran optimization compiler flags

* Sat Apr 11 2020 Antonio Trande <sagitter@fedoraproject.org> - 3.6.1-6
- Release 3.6.1-2
- Drop MUMPS as dependency

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.6.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sun Jan 26 2020 Antonio Trande <sagitter@fedoraproject.org> - 3.6.1-4
- Workaround for GCC-10 (-fallow-argument-mismatch)

* Sat Dec 21 2019 Antonio Trande <sagitter@fedoraproject.org> - 3.6.1-3
- Rebuild for MUMPS-5.2.1 on EPEL7

* Fri Dec 20 2019 Antonio Trande <sagitter@fedoraproject.org> - 3.6.1-2
- Use devtoolset-8 on EPEL7

* Fri Dec 20 2019 Antonio Trande <sagitter@fedoraproject.org> - 3.6.1-1
- Release 3.6.1
- Remove format-security flags

* Sun Dec 15 2019 Antonio Trande <sagitter@fedoraproject.org> - 3.6.1-0.2.rc1
- Disable -Wl,--as-needed flags

* Fri Dec 13 2019 Antonio Trande <sagitter@fedoraproject.org> - 3.6.1-0.1.rc1
- Pre-release 3.6.1-rc1

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.6.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Jul 20 2019 Antonio Trande <sagitter@fedoraproject.org> - 3.6.0-4
- Rebuild for mumps-5.2.1

* Thu Feb 14 2019 Orion Poplawski <orion@nwra.com> - 3.6.0-3
- Rebuild for openmpi 3.1.3

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.6.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Tue Dec 04 2018 Antonio Trande <sagitter@fedoraproject.org> - 3.6.0-1
- Release 3.6.0

* Fri Nov 09 2018 Antonio Trande <sagitter@fedoraproject.org> - 3.6.0-0.1
- Pre-release 3.6.0-rc1

* Fri Nov 02 2018 Antonio Trande <sagitter@fedoraproject.org> - 3.5.2-5
- Enable MPI builds

* Fri Nov 02 2018 Antonio Trande <sagitter@fedoraproject.org> - 3.5.2-4
- Update to release 3.5.2-2

* Fri Sep 14 2018 Antonio Trande <sagitter@fedoraproject.org> - 3.5.2-3
- Fix upstream bug #9 (rhbz #1628858)

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.5.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Jun 28 2018 Antonio Trande <sagitter@fedoraproject.org> - 3.5.2-1
- Update to release 3.5.2

* Wed Apr 11 2018 Antonio Trande <sagitter@fedoraproject.org> - 3.5.1-1
- Update to release 3.5.1

* Sat Feb 17 2018 Antonio Trande <sagitter@fedoraproject.org> - 3.5.0-19
- Use %%ldconfig_scriptlets

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.5.0-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Jan 31 2018 Antonio Trande <sagitter@fedoraproject.org> - 3.5.0-17
- Minor fix post-release 3.5.0-3
- Rebuild for GCC-8

* Thu Dec 07 2017 Antonio Trande <sagitter@fedoraproject.org> - 3.5.0-16
- Hotfix post-release 3.5.0-2

* Sun Nov 12 2017 Antonio Trande <sagitter@fedoraproject.org> - 3.5.0-15
- Update to post-release 3.5.0-1

* Mon Nov 06 2017 Antonio Trande <sagitter@fedoraproject.org> - 3.5.0-14
- Use -Wl,-Bdynamic for linking psb_base library

* Mon Nov 06 2017 Antonio Trande <sagitter@fedoraproject.org> - 3.5.0-13
- Install static libraries
- Use -Wl,-Bdynamic for linking

* Sun Nov 05 2017 Antonio Trande <sagitter@fedoraproject.org> - 3.5.0-12
- libpsb_util serial library linked to Metis/AMD

* Sat Nov 04 2017 Antonio Trande <sagitter@fedoraproject.org> - 3.5.0-11
- Metis/AMD unused by psblas3-serial

* Sat Nov 04 2017 Antonio Trande <sagitter@fedoraproject.org> - 3.5.0-10
- Fix unused-direct-shlib-dependency

* Thu Nov 02 2017 Antonio Trande <sagitter@fedoraproject.org> - 3.5.0-9
- MPI builds activated

* Thu Nov 02 2017 Antonio Trande <sagitter@fedoraproject.org> - 3.5.0-8
- Remove -Wl,--as-needed flag

* Tue Oct 31 2017 Antonio Trande <sagitter@fedoraproject.org> - 3.5.0-7
- Install header files in a private MPI directory

* Sun Oct 29 2017 Antonio Trande <sagitter@fedoraproject.org> - 3.5.0-6
- Fix MPICH fortran links

* Sat Oct 28 2017 Antonio Trande <sagitter@fedoraproject.org> - 3.5.0-5
- Rebuild against openblas

* Fri Oct 27 2017 Antonio Trande <sagitter@fedoraproject.org> - 3.5.0-4
- Fix unused-direct-shlib-dependency warnings

* Thu Oct 26 2017 Antonio Trande <sagitter@fedoraproject.org> - 3.5.0-3
- Fix ldconfig scriptlet

* Thu Oct 26 2017 Antonio Trande <sagitter@fedoraproject.org> - 3.5.0-2
- PSBLAS not compiled on epel6

* Thu Oct 26 2017 Antonio Trande <sagitter@fedoraproject.org> - 3.5.0-1
- Update to 3.5.0 (stable release)
- Rebuilt against blas

* Wed May 31 2017 Antonio Trande <sagitter@fedoraproject.org> - 3.5.0-0.1.rc2
- Update to 3.5.0-rc2

* Fri Feb 10 2017 Antonio Trande <sagitter@fedoraproject.org> - 3.4.1-4
- Packed example files

* Thu Feb 09 2017 Antonio Trande <sagitter@fedoraproject.org> - 3.4.1-3
- Rebuilt against atlas

* Thu Feb 09 2017 Antonio Trande <sagitter@fedoraproject.org> - 3.4.1-2
- Fortran module's directory renamed

* Tue Feb 07 2017 Antonio Trande <sagitter@fedoraproject.org> - 3.4.1-1
- Update to 3.4.1
- Drop obsolete patch

* Fri Feb 03 2017 Antonio Trande <sagitter@fedoraproject.org> - 3.4.0-3
- Rebuild without disable-serial option

* Fri Feb 03 2017 Antonio Trande <sagitter@fedoraproject.org> - 3.4.0-2
- Set MPICH Fortran compiler on RHEL7

* Thu Feb 02 2017 Antonio Trande <sagitter@fedoraproject.org> - 3.4.0-1
- First package

