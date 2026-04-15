## Debug builds?
%bcond_with debug
#

# This flag is not recognized in GFortran land, make silent all related warnings
%global optflags %(echo '%optflags' | sed s/-Wp,-D_GLIBCXX_ASSERTIONS//)

ExcludeArch: %{ix86}

%global with_mpich 1
%global with_openmpi 1
%global with_serial 1

# Disable tests, see https://github.com/sfilippone/amg4psblas/issues/7
%global with_check 0

##
%bcond_without superludist
#

%global major_version 1
%global major_minor %{major_version}.2
%global postrelease_version 1

%global blaslib flexiblas

%global libname libamg_prec

Name: amg4psblas
Summary: Algebraic Multigrid Package based on PSBLAS
Version: %{major_minor}.0
Release: %autorelease -e post%{?postrelease_version}
License: MIT-CMU AND BSD-3-Clause
URL: https://psctoolkit.github.io/products/amg4psblas/
Source0: https://github.com/sfilippone/amg4psblas/archive/V%{version}%{?postrelease_version}/amg4psblas-%{version}-%{?postrelease_version}.tar.gz
BuildRequires: gcc-gfortran
BuildRequires: gcc
BuildRequires: gcc-c++
BuildRequires: suitesparse-devel
BuildRequires: %{blaslib}-devel
BuildRequires: make
BuildRequires: metis-devel
%description
AMG4PSBLAS (Algebraic MultiGrid Preconditioners Package
based on PSBLAS) is a package of parallel algebraic
multilevel preconditioners included in the PSCToolkit
(Parallel Sparse Computation Toolkit) software framework.

%if 0%{?with_serial}
%package serial
Summary: %{name} serial mode
BuildRequires: psblas3-serial-devel >= 3.9.0
BuildRequires: MUMPS-devel
BuildRequires: MUMPS-srpm-macros
BuildRequires: SuperLU-devel
Requires: %{name}-doc = %{version}-%{release}
Obsoletes: mld2p4-serial < 0:2.2.2-9
%description serial
AMG4PSBLAS (Algebraic MultiGrid Preconditioners Package
based on PSBLAS) is a package of parallel algebraic
multilevel preconditioners included in the PSCToolkit
(Parallel Sparse Computation Toolkit) software framework.

%package serial-devel
Summary: Development files for %{name}
Requires: %{name}-serial%{?_isa} = %{version}-%{release}
Requires: psblas3-serial-devel%{?_isa}
Obsoletes: mld2p4-serial-devel < 0:2.2.2-9
Requires: gcc-gfortran%{?_isa}
%description serial-devel
Shared links and header files of serial %{name}.

%package serial-static
Summary: Static libraries of %{name}
Requires: %{name}-doc = %{version}-%{release}
%description serial-static
AMG4PSBLAS (Algebraic MultiGrid Preconditioners Package
based on PSBLAS) is a package of parallel algebraic
multilevel preconditioners included in the PSCToolkit
(Parallel Sparse Computation Toolkit) software framework.
%endif

########################################################
%if 0%{?with_openmpi}
%package openmpi
Summary: OpenMPI %{name}
BuildRequires: MUMPS-openmpi-devel
BuildRequires: openmpi-devel
BuildRequires: psblas3-openmpi-devel >= 0:3.9.0
BuildRequires: superlu_dist-openmpi-devel
BuildRequires: MUMPS-srpm-macros
Obsoletes: %{name}-serial < 0:1.1.2-1

Requires: openmpi%{?_isa}
Requires: %{name}-doc = %{version}-%{release}
Obsoletes: mld2p4-openmpi < 0:2.2.2-9
%description openmpi
AMG4PSBLAS (Algebraic MultiGrid Preconditioners Package
based on PSBLAS) is a package of parallel algebraic
multilevel preconditioners included in the PSCToolkit
(Parallel Sparse Computation Toolkit) software framework.

%package openmpi-static
Summary: Static OpenMPI libraries of %{name}
%description openmpi-static
AMG4PSBLAS (Algebraic MultiGrid Preconditioners Package
based on PSBLAS) is a package of parallel algebraic
multilevel preconditioners included in the PSCToolkit
(Parallel Sparse Computation Toolkit) software framework.

%package openmpi-devel
Summary: The %{name} headers and development-related files
Requires: %{name}-openmpi%{?_isa} = %{version}-%{release}
Requires: psblas3-openmpi-devel%{?_isa}  >= 0:3.9.0
Obsoletes: mld2p4-openmpi-devel < 0:2.2.2-9
%description openmpi-devel
Shared links, header files for OpenMPI %{name}.
%endif
##########################################################
########################################################
%if 0%{?with_mpich}
%package mpich
Summary: MPICH %{name}
BuildRequires: MUMPS-mpich-devel
BuildRequires: mpich-devel
BuildRequires: psblas3-mpich-devel >= 0:3.9.0
BuildRequires: superlu_dist-mpich-devel
BuildRequires: MUMPS-srpm-macros
Obsoletes: %{name}-serial < 0:1.1.2-1

Requires: mpich%{?_isa}
Requires: %{name}-doc = %{version}-%{release}
Obsoletes: mld2p4-mpich < 0:2.2.2-9
%description mpich
AMG4PSBLAS (Algebraic MultiGrid Preconditioners Package
based on PSBLAS) is a package of parallel algebraic
multilevel preconditioners included in the PSCToolkit
(Parallel Sparse Computation Toolkit) software framework.

%package mpich-static
Summary: Static MPICH libraries of %{name}
Requires: mpich%{?_isa}
%description mpich-static
AMG4PSBLAS (Algebraic MultiGrid Preconditioners Package
based on PSBLAS) is a package of parallel algebraic
multilevel preconditioners included in the PSCToolkit
(Parallel Sparse Computation Toolkit) software framework.

%package mpich-devel
Summary: The %{name} headers and development-related files
Requires: %{name}-mpich%{?_isa} = %{version}-%{release}
Requires: psblas3-mpich-devel%{?_isa} >= 0:3.9.0
Obsoletes: mld2p4-mpich-devel < 0:2.2.2-9
%description mpich-devel
Shared links, header files for MPICH %{name}.
%endif
##########################################################

%package doc
Summary: Documentation files for %{name}
BuildArch: noarch
BuildRequires: texlive-tex4ht, texlive-latex, doxygen, ghostscript
BuildRequires: texlive-fancybox, texlive-kpathsea, texlive-metafont
BuildRequires: texlive-mfware
%description doc
HTML, PDF and license files of %{name}.

%prep
%setup -qc -n %{name}-%{version}-%{?postrelease_version}

mv %{name}-%{version}-%{?postrelease_version} serial-build

#######################################################
## Copy source for MPI versions
%if 0%{?with_openmpi}
cp -a serial-build openmpi-build
%endif
%if 0%{?with_mpich}
cp -a serial-build mpich-build
%endif
######################################################

%build
%if 0%{?with_serial}
cd serial-build

export LIBBLAS=-l%{blaslib}
export INCBLAS=-I%{_includedir}/%{blaslib}
export FCFLAGS="%{optflags} %{__global_ldflags} -fPIC"
export CFLAGS="%{optflags} -fPIC"

%if %{with debug}
./configure --enable-serial --with-fcopt="-O0 -g -fPIC -I%{_fmoddir}" --with-ccopt="-O0 -g -fPIC" \
  --with-cxxopt="-O0 -g -fPIC" LDFLAGS="%{__global_ldflags} -fPIC" CPPFLAGS="$INCBLAS" \
  FCFLAGS="-O0 -g -fPIC" CFLAGS="-O0 -g -fPIC" \
%else
%configure --enable-serial --with-fcopt="$FCFLAGS" --with-ccopt="%{optflags} %{__global_ldflags} -fPIC" \
  --with-cxxopt="%{optflags} %{__global_ldflags} -fPIC" LDFLAGS="%{__global_ldflags} %{__global_ldflags}" CPPFLAGS="$INCBLAS" \
  FCFLAGS="$FCFLAGS" CFLAGS="%{optflags} %{__global_ldflags} -fPIC" \
%endif
  FC=gfortran CC=gcc CXX=g++ \
  --with-psblas-libdir=%{_libdir} --with-psblas-moddir=%{_fmoddir}/psblas3-serial --with-psblas-incdir=%{_includedir}/psblas3-serial \
  --with-blas=$LIBBLAS --with-lapack=$LIBLAPACK \
  --with-mumps="-ldmumps -lcmumps -lsmumps -lzmumps" --with-mumpsincdir="%{_includedir}/MUMPS" \
  --with-mumpsmoddir=%{_fmoddir}/MUMPS-%{_MUMPS_version} \
  --with-superlu=-lsuperlu --with-superluincdir=%{_includedir}/SuperLU \
  --with-umfpack=-lumfpack --with-umfpackincdir=%{_includedir}/suitesparse
#cat config.log
#exit 1

%make_build

# Make shared libraries
pushd lib
gfortran -shared %{__global_ldflags} -fPIC -Wl,--whole-archive %{libname}.a -Wl,-no-whole-archive -Wl,-Bdynamic -L%{_libdir} $LIBBLAS $LIBLAPACK -lpsb_base -lpsb_prec -lpsb_linsolve -lpsb_ext -lpsb_util -lpsb_cbind -ldmumps -lcmumps -lsmumps -lzmumps -lumfpack -lsuperlu -lmetis -lgfortran -lm -Wl,-soname,%{libname}.so.%{major_minor} -o %{libname}.so.%{major_minor}
ln -sf %{libname}.so.%{major_minor} ./%{libname}.so.%{major_version}
ln -sf %{libname}.so.%{major_minor} ./%{libname}.so
popd

cd ../
%endif

#######################################################
## Build MPI versions
%if 0%{?with_openmpi}
pushd openmpi-build

%{_openmpi_load}
export CC=mpicc
export CXX=mpic++
export FC=mpifort
export LIBBLAS=-l%{blaslib}
export INCBLAS=-I%{_includedir}/%{blaslib}
export FCFLAGS="%{optflags} %{__global_ldflags} -fPIC"
export CFLAGS="%{optflags} -fPIC"

%if %{with debug}
./configure --with-fcopt="-O0 -g -fPIC -I${MPI_FORTRAN_MOD_DIR} $INCBLAS" --with-ccopt="-O0 -g -fPIC $INCBLAS" \
  --with-cxxopt="-O0 -g -fPIC" LDFLAGS="%{__global_ldflags} -fPIC" CPPFLAGS="-I$MPI_INCLUDE/psblas3 $INCBLAS" \
  FCFLAGS="-O0 -g -fPIC" CFLAGS="-O0 -g -fPIC" \
%else
%configure --with-fcopt="$FCFLAGS $INCBLAS" --with-ccopt="%{optflags} %{__global_ldflags} -fPIC $INCBLAS" \
  --with-cxxopt="%{optflags} %{__global_ldflags} -fPIC" LDFLAGS="%{__global_ldflags}" CPPFLAGS="-I$MPI_INCLUDE/psblas3 $INCBLAS" \
  FCFLAGS="$FCFLAGS" CFLAGS="%{optflags} %{__global_ldflags} -fPIC $INCBLAS" \
%endif
  MPIFC=mpif90 MPICC=mpicc MPICXX=mpic++ \
  --with-psblas-libdir=$MPI_LIB --with-psblas-moddir=$MPI_FORTRAN_MOD_DIR/psblas3 --with-psblas-incdir=$MPI_INCLUDE/psblas3 \
  --with-blas=$LIBBLAS --with-lapack=$LIBLAPACK \
  --with-mumps="-ldmumps -lcmumps -lsmumps -lzmumps" --with-mumpsincdir="$MPI_INCLUDE/MUMPS" \
  --with-mumpsmoddir=$MPI_FORTRAN_MOD_DIR/MUMPS-%{_MUMPS_version} \
%if %{with superludist}
  --with-superludist=-lsuperlu_dist --with-superludistincdir=$MPI_INCLUDE/superlu_dist \
%else
  --without-superludist \
%endif
  --with-umfpack=-lumfpack --with-umfpackincdir=%{_includedir}/suitesparse
#cat config.log && exit 1

%make_build

# Make shared libraries
cd lib
mpifort %{optflags} -fPIC -shared %{__global_ldflags} -Wl,-Bdynamic -L%{_libdir} $LIBBLAS $LIBLAPACK -lmetis -lumfpack -lgfortran -lm -Wl,-rpath -Wl,$MPI_LIB -Wl,--enable-new-dtags %(pkgconf --libs ompi-f90) -lpsb_base -lpsb_prec -lpsb_linsolve -lpsb_ext -lpsb_util -lpsb_cbind -ldmumps -lcmumps -lsmumps -lzmumps %{?with_superludist:-lsuperlu_dist} -Wl,-soname,%{libname}.so.%{major_minor} -o %{libname}.so.%{major_minor} -Wl,--whole-archive %{libname}.a -Wl,-no-whole-archive
ln -sf %{libname}.so.%{major_minor} ./%{libname}.so.%{major_version}
ln -sf %{libname}.so.%{major_minor} ./%{libname}.so
cd ../
%{_openmpi_unload}
popd
%endif

%if 0%{?with_mpich}
pushd mpich-build

%{_mpich_load}
export CC=mpicc
export CXX=mpic++
export FC=mpif90
export LIBBLAS=-l%{blaslib}
export INCBLAS=-I%{_includedir}/%{blaslib}
export FCFLAGS="%{optflags} %{__global_ldflags} -fPIC"
export CFLAGS="%{optflags} -fPIC"

%if %{with debug}
./configure --with-fcopt="-O0 -g -fPIC -I${MPI_FORTRAN_MOD_DIR} $INCBLAS" --with-ccopt="-O0 -g -fPIC $INCBLAS" \
  --with-cxxopt="-O0 -g -fPIC" LDFLAGS="%{__global_ldflags} -fPIC" CPPFLAGS="-I$MPI_INCLUDE/psblas3 $INCBLAS" \
  FCFLAGS="-O0 -g -fPIC" CFLAGS="-O0 -g -fPIC" \
%else
%configure --with-fcopt="$FCFLAGS $INCBLAS" --with-ccopt="%{optflags} %{__global_ldflags} -fPIC $INCBLAS" \
  --with-cxxopt="%{optflags} %{__global_ldflags} -fPIC" LDFLAGS="%{__global_ldflags} %{__global_ldflags}" CPPFLAGS="-I$MPI_INCLUDE/psblas3 $INCBLAS" \
  FCFLAGS="$FCFLAGS" CFLAGS="%{optflags} %{__global_ldflags} -fPIC $INCBLAS" \
%endif
 MPIFC=mpif90 MPICC=mpicc MPICXX=mpic++ \
  --with-psblas-libdir=$MPI_LIB --with-psblas-moddir=$MPI_FORTRAN_MOD_DIR/psblas3 --with-psblas-incdir=$MPI_INCLUDE/psblas3 \
  --with-blas=$LIBBLAS --with-lapack=$LIBLAPACK \
  --with-mumps="-ldmumps -lcmumps -lsmumps -lzmumps" --with-mumpsincdir="$MPI_FORTRAN_MOD_DIR/MUMPS-%{_MUMPS_version} -I$MPI_INCLUDE/MUMPS" \
  --with-mumpsmoddir=$MPI_FORTRAN_MOD_DIR/MUMPS-%{_MUMPS_version} \
%if %{with superludist}
  --with-superludist=-lsuperlu_dist --with-superludistincdir=$MPI_INCLUDE/superlu_dist \
%else
  --without-superludist \
%endif
  --with-umfpack=-lumfpack --with-umfpackincdir=%{_includedir}/suitesparse
  
%make_build

# Make shared libraries
cd lib

mpifort %{optflags} -fPIC -shared %{__global_ldflags} -Wl,-Bdynamic -L%{_libdir} $LIBBLAS $LIBLAPACK -lumfpack -lmetis -lgfortran -lm -Wl,-rpath -Wl,$MPI_LIB -Wl,-z,noexecstack $MPIFLIB %(pkgconf --libs mpich) -lpsb_base -lpsb_prec -lpsb_linsolve -lpsb_ext -lpsb_util -lpsb_cbind -ldmumps -lcmumps -lsmumps -lzmumps %{?with_superludist:-lsuperlu_dist} -Wl,-soname,%{libname}.so.%{major_minor} -o %{libname}.so.%{major_minor} -Wl,--whole-archive %{libname}.a -Wl,-no-whole-archive
ln -sf %{libname}.so.%{major_minor} ./%{libname}.so.%{major_version}
ln -sf %{libname}.so.%{major_minor} ./%{libname}.so
cd ../
%{_mpich_unload}
popd
%endif

%install
%if 0%{?with_serial}
pushd serial-build
mkdir -p $RPM_BUILD_ROOT%{_libdir}
mkdir -p $RPM_BUILD_ROOT%{_includedir}/%{name}-serial
mkdir -p $RPM_BUILD_ROOT%{_fmoddir}/%{name}-serial

pushd lib
cp --preserve=all -P *.so* $RPM_BUILD_ROOT%{_libdir}/
install -pm 644 *.a $RPM_BUILD_ROOT%{_libdir}/
popd

install -pm 644 modules/*.mod $RPM_BUILD_ROOT%{_fmoddir}/%{name}-serial/
install -pm 644 include/*.h $RPM_BUILD_ROOT%{_includedir}/%{name}-serial/
install -pm 644 include/Make.inc.amg4psblas $RPM_BUILD_ROOT%{_includedir}/%{name}-serial/
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
cp --preserve=all -P *.a $RPM_BUILD_ROOT$MPI_LIB/
cd ../

install -pm 644 modules/*.mod $RPM_BUILD_ROOT$MPI_FORTRAN_MOD_DIR/%{name}/
install -pm 644 include/*.h $RPM_BUILD_ROOT$MPI_INCLUDE/%{name}/
install -pm 644 include/Make.inc.amg4psblas $RPM_BUILD_ROOT$MPI_INCLUDE/%{name}/
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
cp --preserve=all -P *.a $RPM_BUILD_ROOT$MPI_LIB/
cd ../

install -pm 644 modules/*.mod $RPM_BUILD_ROOT$MPI_FORTRAN_MOD_DIR/%{name}/
install -pm 644 include/*.h $RPM_BUILD_ROOT$MPI_INCLUDE/%{name}/
install -pm 644 include/Make.inc.amg4psblas $RPM_BUILD_ROOT$MPI_INCLUDE/%{name}/
%{_mpich_unload}
popd
%endif
#######################################################

%if 0%{?with_check}
%check
%if 0%{?with_serial}
pushd serial-build
export LD_LIBRARY_PATH=$RPM_BUILD_ROOT%{_libdir}
make check LINKOPT="%{__global_ldflags}"

# Running tests
cd samples/advanced/pdegen/runs
export LD_LIBRARY_PATH=$RPM_BUILD_ROOT%{_libdir}
./amg_d_pde2d amg_pde2d.inp
./amg_d_pde3d amg_pde3d.inp
./amg_s_pde2d amg_pde2d.inp
./amg_s_pde3d amg_pde3d.inp
cd ../
popd
%endif

%if 0%{?with_openmpi}
pushd openmpi-build
%{_openmpi_load}
export LD_LIBRARY_PATH=$RPM_BUILD_ROOT$MPI_LIB
export CC=mpicc
export CXX=mpic++
export FC=mpif90
make check LINKOPT="%{__global_ldflags} %(pkgconf --libs ompi-f90)" && exit 1

# Running tests
cd samples/advanced/pdegen/runs
export LD_LIBRARY_PATH=$RPM_BUILD_ROOT$MPI_LIB
./amg_d_pde2d amg_pde2d.inp
./amg_d_pde3d amg_pde3d.inp
./amg_s_pde2d amg_pde2d.inp
./amg_s_pde3d amg_pde3d.inp
cd ../
%{_openmpi_unload}
popd
%endif

%if 0%{?with_mpich}
pushd mpich-build
%{_mpich_load}
export LD_LIBRARY_PATH=$RPM_BUILD_ROOT$MPI_LIB
export CC=mpicc
export CXX=mpic++
export FC=mpif90
make check LINKOPT="%{__global_ldflags} %(pkgconf --libs mpich)"

# Running tests
cd samples/advanced/pdegen/runs
export LD_LIBRARY_PATH=$RPM_BUILD_ROOT$MPI_LIB
./amg_d_pde2d amg_pde2d.inp
./amg_d_pde3d amg_pde3d.inp
./amg_s_pde2d amg_pde2d.inp
./amg_s_pde3d amg_pde3d.inp
cd ../
%{_mpich_unload}
popd
%endif
%endif

#######################################################

%if 0%{?with_serial}
%files serial
%{_libdir}/*.so.%{major_minor}
%{_libdir}/*.so.%{major_version}

%files serial-devel
%{_libdir}/*.so
%{_includedir}/%{name}-serial/
%{_fmoddir}/%{name}-serial/

%files serial-static
%{_libdir}/*.a
%endif

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
%{_fmoddir}/openmpi/%{name}/
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
%{_fmoddir}/mpich/%{name}/
%endif
######################################################

%files doc
%doc serial-build/README*
%doc serial-build/docs/html serial-build/docs/*.pdf
%doc serial-build/ReleaseNews
%license serial-build/LICENSE

%changelog
%autochangelog
