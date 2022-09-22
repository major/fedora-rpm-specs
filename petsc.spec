# Broken package_note links in rules and variables files
# Disabling this functionality
%undefine _package_note_file

# Testing libpetsc ?
%bcond_without check
#

# Python binding and its testing
%bcond_without python
%ifnarch %{power64} %{arm}
%bcond_with pycheck
%endif
%global pymodule_name petsc4py
%global pymodule_version %{version}
#

## Debug builds ?
%bcond_with debug
#

# Define _pkgdocdir macro on epel
%{?el7:%global _pkgdocdir %{_docdir}/%{name}}
#

%bcond_without mpich
%bcond_without openmpi

%if %{?__isa_bits:%{__isa_bits}}%{!?__isa_bits:32} == 64
%bcond_without arch64
%else
%bcond_with arch64
%endif

%bcond_without blas
%if %{with arch64}
%bcond_without blas64
%endif

%if 0%{?fedora} || 0%{?rhel} >= 9
%global blaslib flexiblas
%global blasvar %{nil}
%else
%global blaslib openblas
%global blasvar %{nil}
%endif

#
## PETSC looks incompatible with serial MUMPS
%bcond_without mumps_serial
#
## Sundials needs mpi ?
%bcond_with sundials_serial
#
%bcond_without superlu
#

## Suitesparse
## This version of PETSc needs the 5.6.0 at least
%bcond_with suitesparse
%bcond_with suitesparse64
#

## SuperLUDIST needs parmetis
%if 0%{?fedora} || 0%{?rhel} > 7
%bcond_without superludist >= 6.3.0
%bcond_without cgns
%bcond_without hdf5
%else
# Needed superludist >= 6.3.0
%bcond_with superludist
## hdf5 is required by cgns
## See rhbz#1904164
%bcond_with cgns
%bcond_with hdf5
%endif
%bcond_with superlumt
#

## Tetgen
%bcond_with tetgen
#

## Metis
%bcond_without metis
%if 0%{?fedora} || 0%{?rhel} < 8
%bcond_without metis64
%endif
#

# 'scalapack' is required by 'MUMPS'
%if %{with openmpi}
%bcond_without mpi
# PETSC-3.* is incompatible with Sundials 3+
%bcond_with sundials
%bcond_without scalapack
%bcond_without mumps
%bcond_without ptscotch
%bcond_without hypre
%endif

%if %{with mpich}
%bcond_without mpi
# PETSC-3.* is incompatible with Sundials 3+
%bcond_with sundials
%bcond_without scalapack
%bcond_without mumps
%bcond_without ptscotch
%bcond_without hypre
%endif

%global petsc_build_options \\\
 %if %{with debug} \
 CFLAGS="-O0 -g -Wl,-z,now -fPIC" CXXFLAGS="-O0 -g -Wl,-z,now -fPIC" FFLAGS="-O0 -g -Wl,-z,now -fPIC -I%{_libdir}/gfortran/modules" COPTFLAGS="-O0 -g -Wl,-z,now" \\\
  CXXOPTFLAGS="-O0 -g -Wl,-z,now" FOPTFLAGS="-O0 -g -Wl,-z,now -I%{_libdir}/gfortran/modules" LDFLAGS="$LDFLAGS -fPIC" \\\
  FCFLAGS="-O0 -g -Wl,-z,now -fPIC -I%{_libdir}/gfortran/modules" \\\
 %else \
 CFLAGS="$CFLAGS -O3 -fPIC" CXXFLAGS="$CXXFLAGS -O3 -fPIC" FFLAGS="$FFLAGS -O3 -fPIC" LDFLAGS="$LDFLAGS -fPIC" \\\
  COPTFLAGS="$CFLAGS -O3" CXXOPTFLAGS="$CXXFLAGS -O3" FOPTFLAGS="$FFLAGS -O3" \\\
  FCFLAGS="$FFLAGS -O3 -fPIC" \\\
 %endif \
 --CC_LINKER_FLAGS="$LDFLAGS" \\\
 --FC_LINKER_FLAGS="$LDFLAGS -lgfortran" \\\
 --with-default-arch=0 --with-make=1 \\\
 --with-cmake-exec=%{_bindir}/cmake3 --with-ctest-exec=%{_bindir}/ctest3 \\\
 --with-single-library=1 \\\
 --with-precision=double \\\
 --with-petsc-arch=%{_arch} \\\
 --with-clanguage=C \\\
 --with-shared-libraries=1 \\\
 --with-fortran-interfaces=1 \\\
 --with-windows-graphics=0 \\\
 --CC=gcc \\\
 --FC=gfortran \\\
 --CXX=g++ \\\
 --with-shared-ld=ld \\\
 --with-pic=1 \\\
 --with-clib-autodetect=0 \\\
 --with-fortranlib-autodetect=0 \\\
 --with-threadsafety=0 --with-log=1 \\\
 --with-mkl_sparse=0 \\\
 --with-mkl_sparse_optimize=0 \\\
 --with-mkl_cpardiso=0 \\\
 --with-mkl_pardiso=0 \\\
 --with-python=0 \\\
 --with-cxxlib-autodetect=1 \\\
 %if %{with debug} \
  --with-debugging=1 \\\
 %else \
  --with-debugging=0 \\\
 %endif \
 %if %{with mumps_serial} \
  --with-mumps-serial=1 \\\
 %endif \
  --with-mpi=0 \\\
 %if %{with hdf5} \
  --with-hdf5=1 \\\
  --with-hdf5-include= \\\
  --with-hdf5-lib="-lhdf5 -lhdf5_hl" \\\
 %endif \
 %if %{with cgns} \
  --with-cgns=1 \\\
  --with-cgns-include= \\\
  --with-cgns-lib=-lcgns \\\
 %endif \
  --with-x=1 \\\
  --with-openmp=0 \\\
  --with-hwloc=0 \\\
  --with-ssl=0 \\\
 %if %{with sundials_serial} \
  --with-sundials=1 \\\
  --with-sundials-include=%{_includedir} \\\
  --with-sundials-lib="-lsundials_nvecserial -lsundials_cvode" \\\
 %endif \
  --with-pthread=1 \\\
  --with-valgrind=1

%global petsc_mpibuild_options \\\
 %if %{with debug} \
 CFLAGS="-O0 -g -Wl,-z,now -fPIC" CXXFLAGS="-O0 -g -Wl,-z,now -fPIC" FFLAGS="-O0 -g -Wl,-z,now -fPIC -I${MPI_FORTRAN_MOD_DIR}" COPTFLAGS="-O0 -g -Wl,-z,now" \\\
  CXXOPTFLAGS="-O0 -g -Wl,-z,now" FOPTFLAGS="-O0 -g -Wl,-z,now -I${MPI_FORTRAN_MOD_DIR}" LDFLAGS="$LDFLAGS -fPIC" \\\
  FCFLAGS="-O0 -g -Wl,-z,now -fPIC -I${MPI_FORTRAN_MOD_DIR}" \\\
 %else \
 CFLAGS="$CFLAGS -O3 -fPIC" CXXFLAGS="$CXXFLAGS -O3 -fPIC" FFLAGS="$FFLAGS -O3 -fPIC" LDFLAGS="$LDFLAGS -fPIC" \\\
  COPTFLAGS="$CFLAGS -O3" CXXOPTFLAGS="$CXXFLAGS -O3" FOPTFLAGS="$FFLAGS -O3" \\\
  FCFLAGS="$FFLAGS -O3 -fPIC" \\\
 %endif \
  --CC_LINKER_FLAGS="$LDFLAGS" \\\
  --with-default-arch=0 --with-make=1 \\\
  --with-cmake-exec=%{_bindir}/cmake3 --with-ctest-exec=%{_bindir}/ctest3 \\\
  --with-single-library=1 \\\
  --with-precision=double \\\
  --with-petsc-arch=%{_arch} \\\
  --with-clanguage=C \\\
  --with-shared-libraries=1 \\\
  --with-fortran-interfaces=1 \\\
  --with-windows-graphics=0 \\\
  --with-cc=${MPI_BIN}/mpicc \\\
  --with-cxx=${MPI_BIN}/mpicxx \\\
  --with-fc=${MPI_BIN}/mpif90 \\\
  --with-shared-ld=ld \\\
  --with-pic=1 \\\
  --with-clib-autodetect=0 \\\
  --with-fortranlib-autodetect=0 \\\
  --with-mkl_sparse=0 \\\
  --with-mkl_sparse_optimize=0 \\\
  --with-mkl_cpardiso=0 \\\
  --with-mkl_pardiso=0 \\\
 %if %{with python} \
  --with-python=1 \\\
  --with-python-exec=%{__python3} \\\
  --with-petsc4py=1 \\\
  --with-petsc4py-test-np="`/usr/bin/getconf _NPROCESSORS_ONLN`" \\\
 %endif \
  --with-cxxlib-autodetect=1 \\\
  --with-threadsafety=0 --with-log=1 \\\
 %if %{with debug} \
  --with-debugging=1 \\\
    --with-mpiexec="${MPI_BIN}/mpiexec -n `/usr/bin/getconf _NPROCESSORS_ONLN` --mca btl_base_warn_component_unused 0 --mca orte_base_help_aggregate 0" \\\
 %else \
  --with-debugging=0 \\\
    --with-mpiexec="${MPI_BIN}/mpiexec -n `/usr/bin/getconf _NPROCESSORS_ONLN` --mca btl_base_warn_component_unused 0" \\\
 %endif \
 %if %{with scalapack} \
  --with-scalapack=1 \\\
  --with-scalapack-lib="-L$MPI_LIB -lscalapack" \\\
  --with-scalapck-include="" \\\
 %endif \
 %if %{with mpi} \
  --with-mpi=1 \\\
 %endif \
 %if %{with cgns} \
  --with-cgns=1 \\\
  --with-cgns-include= \\\
  --with-cgns-lib=-lcgns \\\
 %endif \
 %if %{with hdf5} \
  --with-hdf5=1 \\\
  --with-hdf5-include= \\\
  --with-hdf5-lib="-L$MPI_LIB -lhdf5 -lhdf5_hl" \\\
 %endif \
 %if %{with ptscotch} \
  --with-ptscotch=1 \\\
  --with-ptscotch-include= \\\
  --with-ptscotch-lib="-L$MPI_LIB -lptscotch -lscotch -lptscotcherr -lscotcherr" \\\
 %endif \
 %if %{with mumps} \
  --with-mumps=1 \\\
 %endif \
 %if %{with sundials} \
  --with-sundials=1 \\\
  --with-sundials-include=$MPI_INCLUDE \\\
  --with-sundials-lib=-lsundials_nvecparallel \\\
 %endif \
 %if %{with superludist} \
  --with-superlu_dist=1 \\\
  --with-superlu_dist-include=$MPI_INCLUDE/superlu_dist \\\
  --with-superlu_dist-lib=-lsuperlu_dist \\\
 %endif \
  --with-x=1 \\\
  --with-openmp=0 \\\
  --with-hwloc=0 \\\
  --with-ssl=0 \\\
 %if %{with hypre} \
  --with-hypre=1 \\\
  --with-hypre-include=$MPI_INCLUDE/hypre \\\
  --with-hypre-lib="-L$MPI_LIB -lHYPRE" \\\
 %endif \
 %if %{with fftw} \
  --with-fftw=1 \\\
  --with-fftw-include= \\\
  --with-fftw-lib="-L$MPI_LIB -lfftw3_mpi -lfftw3" \\\
 %endif \
  --with-pthread=1 \\\
  --with-valgrind=1
  
%global mpichversion %(rpm -qi mpich | awk -F': ' '/Version/ {print $2}')
%global openmpiversion %(rpm -qi openmpi | awk -F': ' '/Version/ {print $2}')
%global majorver 3
%global releasever 3.17

Name:    petsc
Summary: Portable Extensible Toolkit for Scientific Computation
Version: %{releasever}.4
Release: 3%{?dist}
License: BSD
URL:     https://petsc.org/
Source0: https://ftp.mcs.anl.gov/pub/petsc/release-snapshots/petsc-with-docs-%{version}.tar.gz
Source1: https://ftp.mcs.anl.gov/pub/petsc/release-snapshots/petsc4py-%{version}.tar.gz

## Remove rpath flags
Patch0:  %{name}-3.11-no-rpath.patch

## Rename library name for 64-bit integer package
Patch1:  %{name}-lib64.patch

# Reverting patch for Hypre-2.11.2
Patch2:  %{name}-3.14-hypre_2.11.2_reverting.patch

Patch3:  %{name}-3.17.0-fix_mumps_includes.patch
Patch4:  %{name}-3.13.0-fix_metis64.patch
Patch5:  %{name}-3.15.0-fix_sundials_version.patch
Patch6:  %{name}-3.14.1-fix_pkgconfig_file.patch
Patch7:  %{name}-3.17.0-avoid_fake_MKL_detection.patch
Patch8:  %{name}-porting_to_python311.patch

%if %{with superlu}
BuildRequires: SuperLU-devel >= 5.2.0
%endif
%if %{with superlumt}
BuildRequires: SuperLUMT-devel
%endif
%if %{with mumps_serial}
BuildRequires: MUMPS-devel >= 5.2.1
%endif
%if %{with metis}
BuildRequires: metis-devel >= 5.1.0
%endif
%if %{with suitesparse}
BuildRequires: suitesparse-devel >= 5.6.0
%endif
%if %{with blas}
BuildRequires: %{blaslib}-devel
%endif
BuildRequires: chrpath
BuildRequires: gcc, gcc-c++, cmake3
BuildRequires: gcc-gfortran
BuildRequires: make
BuildRequires: libX11-devel
BuildRequires: python3-devel
BuildRequires: python3-setuptools
BuildRequires: pcre2-devel
%if 0%{?el7}
BuildRequires: pkgconfig
%else
BuildRequires: pkgconf-pkg-config
%endif
%if %{with hdf5}
BuildRequires: hdf5-devel
%endif
%if %{with cgns}
BuildRequires: cgnslib-devel
BuildRequires: hdf5-devel
%endif
BuildRequires: tcsh
%if %{with tetgen}
BuildRequires: tetgen-devel
%endif
BuildRequires: xorg-x11-server-Xvfb
BuildRequires: valgrind-devel

%description
PETSc, pronounced PET-see (the S is silent), is a suite of data structures
and routines for the scalable (parallel) solution of scientific applications
modeled by partial differential equations.

%package devel
Summary:    Portable Extensible Toolkit for Scientific Computation (developer files)
Requires:   %{name}%{?_isa} = %{version}-%{release}
%if 0%{?el7}
Requires: pkgconfig%{?_isa}
%else
Requires: pkgconf-pkg-config%{?_isa}
%endif
Requires: gcc-gfortran%{?_isa}
%description devel
Portable Extensible Toolkit for Scientific Computation (developer files).

%package doc
Summary:    Portable Extensible Toolkit for Scientific Computation (documentation files)
BuildRequires: python3-sphinx
BuildArch:  noarch
%description doc
Portable Extensible Toolkit for Scientific Computation.
PDF and HTML documentation files.

%if %{with arch64}
%package -n petsc64
Summary: Portable Extensible Toolkit for Scientific Computation (64bit INTEGER)
%if %{with metis64}
BuildRequires: metis64-devel >= 5.1.0
%endif

%description -n petsc64
PETSc, pronounced PET-see (the S is silent), is a suite of data structures
and routines for the scalable (parallel) solution of scientific applications
modeled by partial differential equations (64bit INTEGER).

%package -n petsc64-devel
Requires:   %{name}64%{?_isa} = %{version}-%{release}
Requires:   gcc-gfortran%{?_isa}
%if 0%{?el7}
Requires: pkgconfig%{?_isa}
%else
Requires: pkgconf-pkg-config%{?_isa}
%endif
Summary: Portable Extensible Toolkit for Scientific Computation (64bit INTEGER)

%description -n petsc64-devel
Portable Extensible Toolkit for Scientific Computation (developer files)
(64bit INTEGER).
%endif

#############################################################################
#########
%if %{with openmpi}
%package openmpi
Summary:    Portable Extensible Toolkit for Scientific Computation (OpenMPI)
BuildRequires: openmpi-devel
%if %{with hdf5}
BuildRequires: hdf5-openmpi-devel
%endif
%if %{with cgns}
BuildRequires: cgnslib-devel
BuildRequires: hdf5-openmpi-devel
%endif
%if %{with ptscotch}
BuildRequires: ptscotch-openmpi-devel
%endif
%if %{with scalapack}
BuildRequires: scalapack-openmpi-devel
%if 0%{?rhel} || 0%{?fedora} < 32
BuildRequires: blacs-openmpi-devel
%endif
%endif
%if %{with mumps}
BuildRequires: MUMPS-openmpi-devel >= 5.2.1
%endif
%if %{with sundials}
BuildRequires: sundials-openmpi-devel
%endif
%if %{with superludist}
BuildRequires: superlu_dist-openmpi-devel >= 6.3.0
%endif
%if %{with fftw}
BuildRequires: fftw-devel
BuildRequires: fftw-openmpi-devel
%endif
%if %{with hypre}
BuildRequires: hypre-openmpi-devel
%endif

%description openmpi
PETSc, pronounced PET-see (the S is silent), is a suite of data structures
and routines for the scalable (parallel) solution of scientific applications
modeled by partial differential equations.

%package openmpi-devel
Summary:    Portable Extensible Toolkit for Scientific Computation (OpenMPI)
Requires:   %{name}-openmpi%{?_isa} = %{version}-%{release}
Requires:   openmpi-devel%{?_isa} = 0:%{openmpiversion}
%description openmpi-devel
Portable Extensible Toolkit for Scientific Computation (developer files).
%endif

%if %{with python}
%package -n     python%{python3_pkgversion}-%{name}-openmpi
Summary:        Python3 bindings for OpenMPI PETSc
%{?python_provide:%python_provide python%{python3_pkgversion}-%{name}-openmpi}

BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  python%{python3_pkgversion}-setuptools
BuildRequires:  hdf5-openmpi-devel
BuildRequires:  scalapack-openmpi-devel
BuildRequires:  ptscotch-openmpi-devel
BuildRequires:  python%{python3_pkgversion}-numpy, python%{python3_pkgversion}-Cython
Requires:       petsc-openmpi%{?_isa}
Requires:       hdf5-openmpi%{?_isa}
Requires:       scalapack-openmpi%{?_isa}
Requires:       ptscotch-openmpi%{?_isa}
Requires:       openmpi%{?_isa} = 0:%{openmpiversion}
Requires:       MUMPS-openmpi%{?_isa}

Obsoletes:      %{pymodule_name}-openmpi < 0:3.14.0-3
Obsoletes:      python%{python3_pkgversion}-%{pymodule_name}-openmpi < 0:3.14.0-3
Provides:       python%{python3_pkgversion}-%{pymodule_name}-openmpi = 0:%{pymodule_version}-%{release}
Provides:       python-%{pymodule_name}-openmpi = 0:%{pymodule_version}-%{release}
Provides:       %{pymodule_name}-openmpi = 0:%{pymodule_version}-%{release}

%description -n python%{python3_pkgversion}-%{name}-openmpi
This package provides Python3 bindings for OpenMPI PETSc,
the Portable, Extensible Toolkit for Scientific Computation.

%package -n     python%{python3_pkgversion}-%{name}-mpich
Summary:        Python3 bindings for MPICH PETSc
%{?python_provide:%python_provide python%{python3_pkgversion}-%{name}-mpich}

BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  python%{python3_pkgversion}-setuptools
BuildRequires:  hdf5-mpich-devel
BuildRequires:  scalapack-mpich-devel
BuildRequires:  ptscotch-mpich-devel
BuildRequires:  python%{python3_pkgversion}-numpy, python%{python3_pkgversion}-Cython
Requires:       petsc-mpich%{?_isa}
Requires:       hdf5-mpich%{?_isa}
Requires:       scalapack-openmpi%{?_isa}
Requires:       ptscotch-mpich%{?_isa}
Requires:       mpich%{?_isa} = 0:%{mpichversion}
Requires:       MUMPS-mpich%{?_isa}

Obsoletes:      %{pymodule_name}-mpich < 0:3.14.0-3
Obsoletes:      python%{python3_pkgversion}-%{pymodule_name}-mpich < 0:3.14.0-3
Provides:       python%{python3_pkgversion}-%{pymodule_name}-mpich = 0:%{pymodule_version}-%{release}
Provides:       python-%{pymodule_name}-mpich = 0:%{pymodule_version}-%{release}
Provides:       %{pymodule_name}-mpich = 0:%{pymodule_version}-%{release}

%description -n python%{python3_pkgversion}-%{name}-mpich
This package provides Python3 bindings for MPICH PETSc,
the Portable, Extensible Toolkit for Scientific Computation.
%endif
######
###############################################################################
######
%if %{with mpich}
%package mpich
Summary:    Portable Extensible Toolkit for Scientific Computation (MPICH)
BuildRequires: mpich-devel
%if %{with hdf5}
BuildRequires: hdf5-mpich-devel
%endif
%if %{with cgns}
BuildRequires: cgnslib-devel
BuildRequires: hdf5-mpich-devel
%endif
%if %{with ptscotch}
BuildRequires: ptscotch-mpich-devel
%endif
%if %{with scalapack}
BuildRequires: scalapack-mpich-devel
%if 0%{?rhel} || 0%{?fedora} < 32
BuildRequires: blacs-mpich-devel
%endif
%endif
%if %{with mumps}
BuildRequires: MUMPS-mpich-devel >= 5.2.1
%endif
%if %{with sundials}
BuildRequires: sundials-mpich-devel
%endif
%if %{with superludist}
BuildRequires: superlu_dist-mpich-devel >= 6.3.0
%endif
%if %{with hypre}
BuildRequires: hypre-mpich-devel
%endif
%if %{with fftw}
BuildRequires: fftw-devel
BuildRequires: fftw-mpich-devel
%endif
Requires:   mpich%{?_isa} = 0:%{mpichversion}

%description mpich
PETSc, pronounced PET-see (the S is silent), is a suite of data structures
and routines for the scalable (parallel) solution of scientific applications
modeled by partial differential equations.

%package mpich-devel
Summary:    Portable Extensible Toolkit for Scientific Computation (MPICH)
Requires:   %{name}-mpich%{?_isa} = %{version}-%{release}
%if 0%{?el7}
# https://bugzilla.redhat.com/show_bug.cgi?id=1397192
Requires:       mpich-devel
%else
Requires:       mpich-devel%{?_isa} = 0:%{mpichversion}
%endif
%description mpich-devel
Portable Extensible Toolkit for Scientific Computation (developer files).
%endif
######
#############################################################################

%prep
%setup -qc

%if %{with python}
%setup -q -T -D -a 1
cp -a petsc4py-%{version}/* %{name}-%{version}/
rm -rf %{name}-%{version}/*.egg-info
rm -rf petsc4py-%{version}
%endif

pushd %{name}-%{version}

%patch7 -p1 -b .backup

find . -name 'setup.py' | xargs pathfix.py -pn -i "%{__python3}"
find . -name 'configure' | xargs pathfix.py -pn -i "%{__python3}"
find config -name '*.py' | xargs pathfix.py -pn -i "%{__python3}"
find src/benchmarks/streams -name '*.py' | xargs pathfix.py -pn -i "%{__python3}"

%if 0%{?el7}
%patch2 -p1 -b .backup
%endif
popd

# Remove pregenerated Cython C sources
pushd %{name}-%{version}
rm $(grep -rl '/\* Generated by Cython')
popd

%if %{with arch64}
cp -a %{name}-%{version} build64
pushd build64
%patch1 -p0
%if %{with metis64}
%patch4 -p1 -b .metis64
%endif
popd
%endif

pushd %{name}-%{version}
%patch0 -p0 -b .backup
%patch5 -p1 -b .backup
%patch6 -p1 -b .backup
%if 0%{?python3_version_nodots} >= 311
#%%patch8 -p1 -b .backup
%endif
popd

%if %{with openmpi}
cp -a %{name}-%{version} buildopenmpi_dir
%endif
%if %{with mpich}
cp -a %{name}-%{version} buildmpich_dir
%endif

# Do NOT move up this patch
pushd %{name}-%{version}
%patch3 -p1
popd

%build
%ifarch %{arm}
# Likely running out of memory during build
%global _lto_cflags %{nil}
%endif
pushd %{name}-%{version}
%configure --with-cc=gcc --with-cxx=g++ --with-fc=gfortran \
 %{petsc_build_options} \
 --with-64-bit-indices=0 \
%if %{with blas}
%if 0%{?fedora} || 0%{?rhel} >= 9
 --with-blaslapack=1 --with-blaslapack-lib=-l%{blaslib}%{blasvar} --with-blaslapack-include=%{_includedir}/%{blaslib} \
%else
 --with-openblas=1 --with-openblas-lib=-l%{blaslib}%{blasvar} --with-openblas-include=%{_includedir}/%{blaslib} \
%endif
%endif
%if %{with metis}
 --with-metis=1 \
%endif
%if %{with tetgen}
 --with-tetgen=1 \
 --with-tetgen-lib=-ltetgen \
%endif
%if %{with superlu}
 --with-superlu=1 \
 --with-superlu-include=%{_includedir}/SuperLU \
 --with-superlu-lib=-lsuperlu \
%endif
%if %{with suitesparse}
 --with-suitesparse=1 \
 --with-suitesparse-include=%{_includedir}/suitesparse \
 --with-suitesparse-lib="-lumfpack -lklu -lcholmod -lamd"
%endif
#cat config.log && exit 1
##

RPM_BUILD_NCPUS="`%{_bindir}/getconf _NPROCESSORS_ONLN`"
make \
 V=1 MAKE_NP=$RPM_BUILD_NCPUS PETSC_DIR=%{_builddir}/%{name}-%{version}/%{name}-%{version} PETSC_ARCH=%{_arch} all
popd

%if %{with arch64}
pushd build64
%configure --with-cc=gcc --with-cxx=g++ --with-fc=gfortran \
 %{petsc_build_options} \
 --with-64-bit-indices=1 \
%if %{with metis64}
 --with-metis=1 \
%endif
%if %{with blas64}
%if 0%{?fedora} || 0%{?rhel} >= 9
 --with-blaslapack=1 --with-blaslapack-lib=-l%{blaslib}%{blasvar}64 --with-blaslapack-include=%{_includedir}/%{blaslib} \
%else
 --with-openblas=1 --with-openblas-lib=-l%{blaslib}%{blasvar}64 --with-openblas-include=%{_includedir}/%{blaslib} \
%endif
%endif
%if %{with suitesparse64}
 --with-suitesparse=1 \
 --with-suitesparse-include=%{_includedir}/suitesparse \
 --with-suitesparse-lib="-lumfpack64 -lklu64 -lcholmod64 -lamd64"
%endif
##

RPM_BUILD_NCPUS="`%{_bindir}/getconf _NPROCESSORS_ONLN`"
make \
 V=1 MAKE_NP=$RPM_BUILD_NCPUS PETSC_DIR=%{_builddir}/%{name}-%{version}/build64 PETSC_ARCH=%{_arch} all
popd
%endif

%if %{with openmpi}
pushd buildopenmpi_dir

%{_openmpi_load}
export CC=mpicc
export CXX=mpic++
export FC=mpifort
%configure --with-cc=mpicc --with-cxx=mpic++ --with-fc=mpifort \
 --FC_LINKER_FLAGS="$LDFLAGS -lgfortran -lmpi_mpifh" \
 --LIBS=" -lmpi -lmpi_mpifh" \
 %{petsc_mpibuild_options} \
%if %{with metis}
 --with-metis=1 \
%endif
 --with-64-bit-indices=0 \
%if %{with blas}
%if 0%{?fedora} || 0%{?rhel} >= 9
 --with-blaslapack=1 --with-blaslapack-lib=-l%{blaslib}%{blasvar} --with-blaslapack-include=%{_includedir}/%{blaslib} \
%else
 --with-openblas=1 --with-openblas-lib=-l%{blaslib}%{blasvar} --with-openblas-include=%{_includedir}/%{blaslib} \
%endif
%endif
#cat config.log
#exit 1

RPM_BUILD_NCPUS="`%{_bindir}/getconf _NPROCESSORS_ONLN`"
make \
 V=1 MAKE_NP=$RPM_BUILD_NCPUS PETSC_DIR=%{_builddir}/%{name}-%{version}/buildopenmpi_dir PETSC_ARCH=%{_arch} all
 
%if %{with python}
export PETSC_ARCH=%{_arch}
export PETSC_DIR=./
%py3_build
unset PETSC_ARCH
unset PETSC_DIR
%endif

%{_openmpi_unload}
popd
%endif

%if %{with mpich}
pushd buildmpich_dir

%{_mpich_load}
export CC=mpicc
export CXX=mpic++
export FC=mpifort
%configure --with-cc=mpicc --with-cxx=mpic++ --with-fc=mpifort \
 --FC_LINKER_FLAGS="$LDFLAGS -lgfortran -lfmpich -lmpichf90" \
 --LIBS=" -lmpich -lfmpich -lmpichf90" \
 %{petsc_mpibuild_options} \
%if %{with metis}
 --with-metis=1 \
%endif
 --with-64-bit-indices=0 \
%if %{with blas}
%if 0%{?fedora} || 0%{?rhel} >= 9
 --with-blaslapack=1 --with-blaslapack-lib=-l%{blaslib}%{blasvar} --with-blaslapack-include=%{_includedir}/%{blaslib} \
%else
 --with-openblas=1 --with-openblas-lib=-l%{blaslib}%{blasvar} --with-openblas-include=%{_includedir}/%{blaslib} \
%endif
%endif
#cat config.log
#exit 1

RPM_BUILD_NCPUS="`%{_bindir}/getconf _NPROCESSORS_ONLN`"
make \
 V=1 MAKE_NP=$RPM_BUILD_NCPUS PETSC_DIR=%{_builddir}/%{name}-%{version}/buildmpich_dir PETSC_ARCH=%{_arch} all

%if %{with python}
export PETSC_ARCH=%{_arch}
export PETSC_DIR=./
%py3_build
unset PETSC_ARCH
unset PETSC_DIR
%endif

%{_mpich_unload}
popd
%endif

%install
pushd %{name}-%{version}
mkdir -p %{buildroot}%{_libdir} %{buildroot}%{_includedir}/%{name}
mkdir -p %{buildroot}%{_fmoddir}/%{name}
mkdir -p %{buildroot}%{_libdir}/%{name}/conf

install -pm 755 %{_arch}/lib/libpetsc.* %{buildroot}%{_libdir}
ln -sf libpetsc.so.%{version} %{buildroot}%{_libdir}/libpetsc.so
ln -sf libpetsc.so.%{version} %{buildroot}%{_libdir}/libpetsc.so.%{releasever}
ln -sf libpetsc.so.%{version} %{buildroot}%{_libdir}/libpetsc.so.%{majorver}

install -pm 644 %{_arch}/include/*.h %{buildroot}%{_includedir}/%{name}/
install -pm 644 %{_arch}/include/*.mod %{buildroot}%{_fmoddir}/%{name}/
cp -a include/* %{buildroot}%{_includedir}/%{name}/

cp -a %{_arch}/lib/pkgconfig %{buildroot}%{_libdir}/

install -pm 644 %{_arch}/lib/petsc/conf/petscrules %{buildroot}%{_libdir}/%{name}/conf/
install -pm 644 %{_arch}/lib/petsc/conf/petscvariables %{buildroot}%{_libdir}/%{name}/conf/
install -pm 644 lib/petsc/conf/rules %{buildroot}%{_libdir}/%{name}/conf/
install -pm 644 lib/petsc/conf/variables %{buildroot}%{_libdir}/%{name}/conf/
sed -e 's|%{_builddir}/%{name}-%{version}/%{name}-%{version}|%{_prefix}|g' -i %{buildroot}%{_libdir}/%{name}/conf/petscvariables
sed -e 's|%{_builddir}/%{name}-%{version}/%{name}-%{version}/%{_arch}/|%{_prefix}|g' -i %{buildroot}%{_libdir}/%{name}/conf/petscvariables
sed -e 's|-L%{_prefix}/%{_arch}/lib|-L%{_libdir}|g' -i %{buildroot}%{_libdir}/%{name}/conf/petscvariables
sed -e 's|-I%{_prefix}/%{_arch}/include|-I%{_includedir}/%{name} -I%{_fmoddir}/%{name}|g' -i %{buildroot}%{_libdir}/%{name}/conf/petscvariables
sed -e 's|${PETSC_DIR}/${PETSC_ARCH}/lib|${PETSC_DIR}/%{_lib}|g' -i %{buildroot}%{_libdir}/%{name}/conf/variables
sed -e 's|${PETSC_DIR}/${PETSC_ARCH}/lib|${PETSC_DIR}/%{_lib}|g' -i %{buildroot}%{_libdir}/%{name}/conf/rules
popd

%if %{with arch64}
pushd build64
mkdir -p %{buildroot}%{_libdir} %{buildroot}%{_includedir}/%{name}64
mkdir -p %{buildroot}%{_fmoddir}/%{name}64
mkdir -p %{buildroot}%{_libdir}/%{name}64/conf
mkdir -p %{buildroot}%{_libdir}/pkgconfig

install -pm 755 %{_arch}/lib/libpetsc64.* %{buildroot}%{_libdir}
ln -sf libpetsc64.so.%{version} %{buildroot}%{_libdir}/libpetsc64.so
ln -sf libpetsc64.so.%{version} %{buildroot}%{_libdir}/libpetsc64.so.%{releasever}
ln -sf libpetsc64.so.%{version} %{buildroot}%{_libdir}/libpetsc64.so.%{majorver}

install -pm 644 %{_arch}/include/*.h %{buildroot}%{_includedir}/%{name}64/
install -pm 644 %{_arch}/include/*.mod %{buildroot}%{_fmoddir}/%{name}64/
cp -a include/* %{buildroot}%{_includedir}/%{name}64/

cp -p %{_arch}/lib/pkgconfig/PETSc.pc %{buildroot}%{_libdir}/pkgconfig/PETSc64.pc
cp -p %{_arch}/lib/pkgconfig/PETSc.pc %{buildroot}%{_libdir}/pkgconfig/petsc64.pc

install -pm 644 %{_arch}/lib/petsc/conf/petscrules %{buildroot}%{_libdir}/%{name}64/conf/
install -pm 644 %{_arch}/lib/petsc/conf/petscvariables %{buildroot}%{_libdir}/%{name}64/conf/
install -pm 644 lib/petsc/conf/rules %{buildroot}%{_libdir}/%{name}64/conf/
install -pm 644 lib/petsc/conf/variables %{buildroot}%{_libdir}/%{name}64/conf/
sed -e 's|%{_builddir}/%{name}-%{version}/build64|%{_prefix}|g' -i %{buildroot}%{_libdir}/%{name}64/conf/petscvariables
sed -e 's|%{_builddir}/%{name}-%{version}/build64/%{_arch}/|%{_prefix}|g' -i %{buildroot}%{_libdir}/%{name}64/conf/petscvariables
sed -e 's|-L%{_prefix}/%{_arch}/lib|-L%{_libdir}|g' -i %{buildroot}%{_libdir}/%{name}64/conf/petscvariables
sed -e 's|-I%{_prefix}/%{_arch}/include/|-I%{_includedir}/%{name}64 -I%{_fmoddir}/%{name}64|g' -i %{buildroot}%{_libdir}/%{name}64/conf/petscvariables
sed -e 's|${PETSC_DIR}/${PETSC_ARCH}/lib|${PETSC_DIR}/%{_lib}|g' -i %{buildroot}%{_libdir}/%{name}64/conf/variables
sed -e 's|${PETSC_DIR}/${PETSC_ARCH}/lib|${PETSC_DIR}/%{_lib}|g' -i %{buildroot}%{_libdir}/%{name}64/conf/rules
popd
%endif

%if %{with openmpi}
pushd buildopenmpi_dir
%{_openmpi_load}
mkdir -p %{buildroot}$MPI_LIB %{buildroot}$MPI_INCLUDE/%{name}
mkdir -p %{buildroot}$MPI_FORTRAN_MOD_DIR/%{name}
mkdir -p %{buildroot}$MPI_LIB/%{name}/conf

install -pm 755 %{_arch}/lib/libpetsc.* %{buildroot}$MPI_LIB
ln -sf libpetsc.so.%{version} %{buildroot}$MPI_LIB/libpetsc.so
ln -sf libpetsc.so.%{version} %{buildroot}$MPI_LIB/libpetsc.so.%{releasever}
ln -sf libpetsc.so.%{version} %{buildroot}$MPI_LIB/libpetsc.so.%{majorver}

install -pm 644 %{_arch}/include/*.h %{buildroot}$MPI_INCLUDE/%{name}/
install -pm 644 %{_arch}/include/*.mod %{buildroot}$MPI_FORTRAN_MOD_DIR/%{name}/
cp -a include/* %{buildroot}$MPI_INCLUDE/%{name}/

cp -a %{_arch}/lib/pkgconfig %{buildroot}$MPI_LIB/
sed -e 's|-I${includedir}/petsc|-I%{_includedir}/openmpi-%{_arch}/petsc|g' -i %{buildroot}$MPI_LIB/pkgconfig/PETSc.pc
sed -e 's|-L${libdir}|-L%{_libdir}/openmpi/lib|g' -i %{buildroot}$MPI_LIB/pkgconfig/PETSc.pc
sed -e 's|ldflag_rpath=-L|ldflag_rpath=-L%{_libdir}/openmpi/lib|g' -i %{buildroot}$MPI_LIB/pkgconfig/PETSc.pc
sed -e 's|-lpetsc|-lpetsc -lhdf5|' -i %{buildroot}$MPI_LIB/pkgconfig/PETSc.pc

install -pm 644 %{_arch}/lib/petsc/conf/petscrules %{buildroot}$MPI_LIB/%{name}/conf/
install -pm 644 %{_arch}/lib/petsc/conf/petscvariables %{buildroot}$MPI_LIB/%{name}/conf/
install -pm 644 lib/petsc/conf/rules %{buildroot}$MPI_LIB/%{name}/conf/
install -pm 644 lib/petsc/conf/variables %{buildroot}$MPI_LIB/%{name}/conf/
sed -e 's|%{_builddir}/%{name}-%{version}/buildopenmpi_dir|%{_prefix}|g' -i %{buildroot}$MPI_LIB/%{name}/conf/petscvariables
sed -e 's|%{_builddir}/%{name}-%{version}/buildopenmpi_dir/%{_arch}/|%{_prefix}|g' -i %{buildroot}$MPI_LIB/%{name}/conf/petscvariables
sed -e 's|-L%{_prefix}/%{_arch}/lib|-L%{_libdir}/openmpi/lib|g' -i %{buildroot}$MPI_LIB/%{name}/conf/petscvariables
sed -e 's|-I%{_prefix}/%{_arch}/include|-I%{_includedir}/openmpi-%{_arch}/%{name} -I%{_fmoddir}/openmpi/%{name}|g' -i %{buildroot}$MPI_LIB/%{name}/conf/petscvariables
sed -e 's|${PETSC_DIR}/${PETSC_ARCH}/lib|${PETSC_DIR}/%{_lib}/openmpi/lib|g' -i %{buildroot}$MPI_LIB/%{name}/conf/variables
sed -e 's|${PETSC_DIR}/${PETSC_ARCH}/lib|${PETSC_DIR}/%{_lib}/openmpi/lib|g' -i %{buildroot}$MPI_LIB/%{name}/conf/rules

%if %{with python}
export PETSC_ARCH=%{_arch}
export PETSC_DIR=./
%py3_install

# Install petsc4py files into MPI directories
%if 0%{?rhel}
MPI_PYTHON3_SITEARCH=%{python3_sitearch}/openmpi
%endif

mkdir -p %{buildroot}$MPI_PYTHON3_SITEARCH
cp -a %{buildroot}%{python3_sitearch}/%{pymodule_name} %{buildroot}$MPI_PYTHON3_SITEARCH/
rm -rf %{buildroot}%{python3_sitearch}/%{pymodule_name}
cp -a %{buildroot}%{python3_sitearch}/%{pymodule_name}-%{pymodule_version}-py%{python3_version}.egg-info %{buildroot}$MPI_PYTHON3_SITEARCH/
rm -rf %{buildroot}%{python3_sitearch}/%{pymodule_name}-%{pymodule_version}-py%{python3_version}.egg-info

chrpath -r %{_libdir}/openmpi/lib %{buildroot}$MPI_PYTHON3_SITEARCH/%{pymodule_name}/lib/%{_arch}/*.so
%endif
%{_openmpi_unload}
popd
%endif

%if %{with mpich}
pushd buildmpich_dir
%{_mpich_load}
mkdir -p %{buildroot}$MPI_LIB %{buildroot}$MPI_INCLUDE/%{name}
mkdir -p %{buildroot}$MPI_FORTRAN_MOD_DIR/%{name}
mkdir -p %{buildroot}$MPI_LIB/%{name}/conf

install -pm 755 %{_arch}/lib/libpetsc.* %{buildroot}$MPI_LIB
ln -sf libpetsc.so.%{version} %{buildroot}$MPI_LIB/libpetsc.so
ln -sf libpetsc.so.%{version} %{buildroot}$MPI_LIB/libpetsc.so.%{releasever}
ln -sf libpetsc.so.%{version} %{buildroot}$MPI_LIB/libpetsc.so.%{majorver}

install -pm 644 %{_arch}/include/*.h %{buildroot}$MPI_INCLUDE/%{name}/
install -pm 644 %{_arch}/include/*.mod %{buildroot}$MPI_FORTRAN_MOD_DIR/%{name}/
cp -a include/* %{buildroot}$MPI_INCLUDE/%{name}/

cp -a %{_arch}/lib/pkgconfig %{buildroot}$MPI_LIB/
sed -e 's|-I${includedir}/petsc|-I%{_includedir}/mpich-%{_arch}/petsc|g' -i %{buildroot}$MPI_LIB/pkgconfig/PETSc.pc
sed -e 's|-L${libdir}|-L%{_libdir}/mpich/lib|g' -i %{buildroot}$MPI_LIB/pkgconfig/PETSc.pc
sed -e 's|ldflag_rpath=-L|ldflag_rpath=-L%{_libdir}/mpich/lib|g' -i %{buildroot}$MPI_LIB/pkgconfig/PETSc.pc
sed -e 's|-lpetsc|-lpetsc -lhdf5|' -i %{buildroot}$MPI_LIB/pkgconfig/PETSc.pc
pushd %{buildroot}$MPI_LIB/pkgconfig
#ln -fs PETSc.pc petsc.pc
popd

install -pm 644 %{_arch}/lib/petsc/conf/petscrules %{buildroot}$MPI_LIB/%{name}/conf/
install -pm 644 %{_arch}/lib/petsc/conf/petscvariables %{buildroot}$MPI_LIB/%{name}/conf/
install -pm 644 lib/petsc/conf/rules %{buildroot}$MPI_LIB/%{name}/conf/
install -pm 644 lib/petsc/conf/variables %{buildroot}$MPI_LIB/%{name}/conf/
sed -e 's|%{_builddir}/%{name}-%{version}/buildmpich_dir|%{_prefix}|g' -i %{buildroot}$MPI_LIB/%{name}/conf/petscvariables
sed -e 's|%{_builddir}/%{name}-%{version}/buildmpich_dir/%{_arch}/|%{_prefix}|g' -i %{buildroot}$MPI_LIB/%{name}/conf/petscvariables
sed -e 's|-L%{_prefix}/%{_arch}/lib|-L%{_libdir}/mpich/lib|g' -i %{buildroot}$MPI_LIB/%{name}/conf/petscvariables
sed -e 's|-I%{_prefix}/%{_arch}/include|-I%{_includedir}/mpich-%{_arch}/%{name} -I%{_fmoddir}/mpich/%{name}|g' -i %{buildroot}$MPI_LIB/%{name}/conf/petscvariables
sed -e 's|${PETSC_DIR}/${PETSC_ARCH}/lib|${PETSC_DIR}/%{_lib}/mpich/lib|g' -i %{buildroot}$MPI_LIB/%{name}/conf/variables
sed -e 's|${PETSC_DIR}/${PETSC_ARCH}/lib|${PETSC_DIR}/%{_lib}/mpich/lib|g' -i %{buildroot}$MPI_LIB/%{name}/conf/rules

%if %{with python}
export PETSC_ARCH=%{_arch}
export PETSC_DIR=./
%py3_install

# Install petsc4py files into MPI directories
%if 0%{?rhel}
MPI_PYTHON3_SITEARCH=%{python3_sitearch}/mpich
%endif

mkdir -p %{buildroot}$MPI_PYTHON3_SITEARCH
cp -a %{buildroot}%{python3_sitearch}/%{pymodule_name} %{buildroot}$MPI_PYTHON3_SITEARCH/
rm -rf %{buildroot}%{python3_sitearch}/%{pymodule_name}
cp -a %{buildroot}%{python3_sitearch}/%{pymodule_name}-%{pymodule_version}-py%{python3_version}.egg-info %{buildroot}$MPI_PYTHON3_SITEARCH/
rm -rf %{buildroot}%{python3_sitearch}/%{pymodule_name}-%{pymodule_version}-py%{python3_version}.egg-info

chrpath -r %{_libdir}/mpich/lib %{buildroot}$MPI_PYTHON3_SITEARCH/%{pymodule_name}/lib/%{_arch}/*.so
%endif
%{_mpich_unload}
popd
%endif

# Move html documentation in _pkgdocdir
pushd %{buildroot}%{_includedir}
mkdir -p %{buildroot}%{_pkgdocdir}/headers
for i in `find . -name "*.h.html" -type f -print`; do
    mv $i %{buildroot}%{_pkgdocdir}/headers
done
for i in `find . -name "*.html" -type f -print`; do
    mv $i %{buildroot}%{_pkgdocdir}/headers
done
find . -name "Makefile" -type f -print | xargs /bin/rm -f
popd
cp -a %{name}-%{version}/docs/* %{buildroot}%{_pkgdocdir}
#

%check

%if %{with openmpi}
%{_openmpi_load}
%if %{with check}
export LD_LIBRARY_PATH=%{buildroot}$MPI_LIB
export PETSC_DIR=%{_builddir}/%{name}-%{version}/buildopenmpi_dir
export PETSC_ARCH=%{_arch}
export MPI_INTERFACE_HOSTNAME=localhost
export OMPI_MCA_btl_base_warn_component_unused=0
export wPETSC_DIR=./
export DATAFILESPATH=%{_builddir}/%{name}-%{version}/buildopenmpi_dir/share/petsc/datafiles
RPM_BUILD_NCPUS="`%{_bindir}/getconf _NPROCESSORS_ONLN`"
%if %{with debug}
export PETSCVALGRIND_OPTIONS=" --tool=memcheck --leak-check=yes --track-origins=yes"
export CFLAGS="-O0 -g -Wl,-z,now -fPIC"
export CXXFLAGS="-O0 -g -Wl,-z,now -fPIC"
export FFLAGS="-O0 -g -Wl,-z,now -fPIC -I${MPI_FORTRAN_MOD_DIR}"
xvfb-run -a make MAKE_NP=$RPM_BUILD_NCPUS all test -C buildopenmpi_dir V=1 MPIEXEC='%{_builddir}/%{name}-%{version}/buildopenmpi_dir/lib/petsc/bin/petscmpiexec -valgrind'
%else
xvfb-run -a make MAKE_NP=$RPM_BUILD_NCPUS all test -C buildopenmpi_dir V=1
%endif
%endif

%if %{with python}
%if %{with pycheck}
pushd buildopenmpi_dir
export PETSC_ARCH=%{_arch}
export PETSC_DIR=./
%if 0%{?rhel}
MPI_PYTHON3_SITEARCH=%{python3_sitearch}/openmpi
%endif
export PYTHONPATH=%{buildroot}$MPI_PYTHON3_SITEARCH
export LD_LIBRARY_PATH=%{buildroot}$MPI_LIB
%{__python3} setup.py test
unset PETSC_ARCH
unset PETSC_DIR
popd
%endif
%endif
%{_openmpi_unload}
%endif

%if %{with mpich}
%{_mpich_load}
%if %{with check}
export LD_LIBRARY_PATH=%{_builddir}/%{name}-%{version}/buildmpich_dir/%{_arch}/lib
export PETSC_DIR=%{_builddir}/%{name}-%{version}/buildmpich_dir
export PETSC_ARCH=%{_arch}
export MPI_INTERFACE_HOSTNAME=localhost
export OMPI_MCA_btl_base_warn_component_unused=0
export wPETSC_DIR=./
export DATAFILESPATH=%{_builddir}/%{name}-%{version}/buildmpich_dir/share/petsc/datafiles
RPM_BUILD_NCPUS="`%{_bindir}/getconf _NPROCESSORS_ONLN`"
%if %{with debug}
export PETSCVALGRIND_OPTIONS=" --tool=memcheck --leak-check=yes --track-origins=yes"
export CFLAGS="-O0 -g -Wl,-z,now -fPIC"
export CXXFLAGS="-O0 -g -Wl,-z,now -fPIC"
export FFLAGS="-O0 -g -Wl,-z,now -fPIC -I${MPI_FORTRAN_MOD_DIR}"
xvfb-run -a make MAKE_NP=$RPM_BUILD_NCPUS all test -C buildmpich_dir V=1 MPIEXEC='%{_builddir}/%{name}-%{version}/buildmpich_dir/lib/petsc/bin/petscmpiexec -valgrind'
%else
xvfb-run -a make MAKE_NP=$RPM_BUILD_NCPUS all test -C buildmpich_dir V=1
%endif
%endif

%if %{with python}
%if %{with pycheck}
pushd buildmpich_dir
export PETSC_ARCH=%{_arch}
export PETSC_DIR=./
%if 0%{?rhel}
MPI_PYTHON3_SITEARCH=%{python3_sitearch}/mpich
%endif
export PYTHONPATH=%{buildroot}$MPI_PYTHON3_SITEARCH
export LD_LIBRARY_PATH=%{buildroot}$MPI_LIB
%{__python3} setup.py test
unset PETSC_ARCH
unset PETSC_DIR
popd
%endif
%endif
%{_mpich_unload}
%endif

%if %{with check}
export LD_LIBRARY_PATH=%{_libdir}:%{_builddir}/%{name}-%{version}/%{name}-%{version}/%{_arch}/lib
export PETSC_DIR=%{_builddir}/%{name}-%{version}/%{name}-%{version}
export PETSC_ARCH=%{_arch}
export wPETSC_DIR=./
export DATAFILESPATH=%{_builddir}/%{name}-%{version}/%{name}-%{version}/share/petsc/datafiles
RPM_BUILD_NCPUS="`%{_bindir}/getconf _NPROCESSORS_ONLN`"
%if %{with debug}
export PETSCVALGRIND_OPTIONS=" --tool=memcheck --leak-check=yes --track-origins=yes"
export CFLAGS="-O0 -g -Wl,-z,now -fPIC"
export CXXFLAGS="-O0 -g -Wl,-z,now -fPIC"
export FFLAGS="-O0 -g -Wl,-z,now -fPIC -I%{_libdir}/gfortran/modules"
xvfb-run -a make MAKE_NP=$RPM_BUILD_NCPUS all test -C %{name}-%{version} V=1 MPIEXEC='%{_builddir}/%{name}-%{version}/%{name}-%{version}/lib/petsc/bin/petscmpiexec -n $RPM_BUILD_NCPUS -valgrind'
%else
xvfb-run -a make MAKE_NP=$RPM_BUILD_NCPUS all test -C %{name}-%{version} V=1 MPIEXEC='%{_builddir}/%{name}-%{version}/%{name}-%{version}/lib/petsc/bin/petscmpiexec -n $RPM_BUILD_NCPUS'
%endif

%if %{with arch64}
export LD_LIBRARY_PATH=%{_libdir}:%{_builddir}/%{name}-%{version}/build64/%{_arch}/lib
export PETSC_DIR=%{_builddir}/%{name}-%{version}/build64
export PETSC_ARCH=%{_arch}
export wPETSC_DIR=./
export DATAFILESPATH=%{_builddir}/%{name}-%{version}/build64/share/petsc/datafiles
RPM_BUILD_NCPUS="`%{_bindir}/getconf _NPROCESSORS_ONLN`"
## 'make test' needs to link against -lpetsc
## Crude fix:
ln -s %{_builddir}/%{name}-%{version}/build64/%{_arch}/lib/libpetsc64.so %{_builddir}/%{name}-%{version}/build64/%{_arch}/lib/libpetsc.so

%if %{with debug}
export PETSCVALGRIND_OPTIONS=" --tool=memcheck --leak-check=yes --track-origins=yes"
export CFLAGS="-O0 -g -Wl,-z,now -fPIC"
export CXXFLAGS="-O0 -g -Wl,-z,now -fPIC"
export FFLAGS="-O0 -g -Wl,-z,now -fPIC -I%{_libdir}/gfortran/modules"
xvfb-run -a make MAKE_NP=$RPM_BUILD_NCPUS all test -C build64 V=1 MPIEXEC='%{_builddir}/%{name}-%{version}/build64/lib/petsc/bin/petscmpiexec -n $RPM_BUILD_NCPUS -valgrind'
%else
xvfb-run -a make MAKE_NP=$RPM_BUILD_NCPUS all test -C build64 V=1 MPIEXEC='%{_builddir}/%{name}-%{version}/build64/lib/petsc/bin/petscmpiexec -n $RPM_BUILD_NCPUS'
%endif
%endif
%endif

%files
%license %{name}-%{version}/LICENSE
%{_libdir}/libpetsc.so.3
%{_libdir}/libpetsc.so.%{releasever}
%{_libdir}/libpetsc.so.%{version}

%files devel
%{_libdir}/pkgconfig/PETSc.pc
%{_libdir}/pkgconfig/petsc.pc
%{_libdir}/%{name}/
%{_libdir}/libpetsc.so
%{_includedir}/%{name}/
%{_fmoddir}/%{name}/

%files doc
%license %{name}-%{version}/LICENSE
%{_pkgdocdir}/

%if %{with arch64}
%files -n petsc64
%license build64/LICENSE
%{_libdir}/libpetsc64.so.3
%{_libdir}/libpetsc64.so.%{releasever}
%{_libdir}/libpetsc64.so.%{version}

%files -n petsc64-devel
%{_libdir}/pkgconfig/PETSc64.pc
%{_libdir}/pkgconfig/petsc64.pc
%{_libdir}/%{name}64/
%{_libdir}/libpetsc64.so
%{_includedir}/%{name}64/
%{_fmoddir}/%{name}64/
%endif

%if %{with openmpi}
%files openmpi
%license buildopenmpi_dir/LICENSE
%{_libdir}/openmpi/lib/libpetsc.so.3
%{_libdir}/openmpi/lib/libpetsc.so.%{releasever}
%{_libdir}/openmpi/lib/libpetsc.so.%{version}

%files openmpi-devel
%{_libdir}/openmpi/lib/libpetsc.so
%{_libdir}/openmpi/lib/%{name}/
%{_libdir}/openmpi/lib/pkgconfig/PETSc.pc
%{_libdir}/openmpi/lib/pkgconfig/petsc.pc
%{_includedir}/openmpi-%{_arch}/%{name}/
%if 0%{?el7}
%{_fmoddir}/openmpi-%{_arch}/%{name}/
%else
%{_fmoddir}/openmpi/%{name}/
%endif

%if %{with python}
%files -n python%{python3_pkgversion}-%{name}-openmpi
%{python3_sitearch}/openmpi/%{pymodule_name}/
%{python3_sitearch}/openmpi/%{pymodule_name}-%{pymodule_version}-py%{python3_version}.egg-info
%endif
%endif

%if %{with mpich}
%files mpich
%license buildmpich_dir/LICENSE
%{_libdir}/mpich/lib/libpetsc.so.3
%{_libdir}/mpich/lib/libpetsc.so.%{releasever}
%{_libdir}/mpich/lib/libpetsc.so.%{version}

%files mpich-devel
%{_libdir}/mpich/lib/libpetsc.so
%{_libdir}/mpich/lib/%{name}/
%{_libdir}/mpich/lib/pkgconfig/PETSc.pc
%{_libdir}/mpich/lib/pkgconfig/petsc.pc
%{_includedir}/mpich-%{_arch}/%{name}/
%if 0%{?el7}
%{_fmoddir}/mpich-%{_arch}/%{name}/
%else
%{_fmoddir}/mpich/%{name}/
%endif

%if %{with python}
%files -n python%{python3_pkgversion}-%{name}-mpich
%{python3_sitearch}/mpich/%{pymodule_name}/
%{python3_sitearch}/mpich/%{pymodule_name}-%{pymodule_version}-py%{python3_version}.egg-info
%endif
%endif

%changelog
* Tue Sep 20 2022 Antonio Trande <sagitter@fedoraproject.org> - 3.17.4-3
- Use pcre2 (rhbz#2128348)

* Tue Aug 23 2022 Antonio Trande <sagitter@fedoraproject.org> - 3.17.4-2
- Disabling package-notes

* Sat Aug 06 2022 Antonio Trande <sagitter@fedoraproject.org> - 3.17.4-1
- Release 3.17.4

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 3.17.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Sun Jul 17 2022 Antonio Trande <sagitter@fedoraproject.org> - 3.17.3-2
- Rebuild for MUMPS-5.5.0

* Thu Jul 07 2022 Antonio Trande <sagitter@fedoraproject.org> - 3.17.3-1
- Release 3.17.3

* Fri Jun 24 2022 Antonio Trande <sagitter@fedoraproject.org> - 3.17.2-4
- Rebuild for superlu_dist-8.0.0

* Mon Jun 20 2022 Antonio Trande <sagitter@fedoraproject.org> - 3.17.2-3
- Fix rhbz#2039365

* Mon Jun 13 2022 Python Maint <python-maint@redhat.com> - 3.17.2-2
- Rebuilt for Python 3.11

* Sat Jun 04 2022 Antonio Trande <sagitter@fedoraproject.org> - 3.17.2-1
- Release 3.17.2

* Thu Jun 02 2022 Antonio Trande <sagitter@fedoraproject.org> - 3.17.1-2
- Rebuild for openmpi-4.1.4

* Mon May 02 2022 Antonio Trande <sagitter@fedoraproject.org> - 3.17.1-1
- Release 3.17.1

* Sun Apr 24 2022 Antonio Trande <sagitter@fedoraproject.org> - 3.17.0-2
- Enable tests

* Sat Apr 23 2022 Antonio Trande <sagitter@fedoraproject.org> - 3.17.0-1
- Release 3.17.0

* Tue Apr 19 2022 Antonio Trande <sagitter@fedoraproject.org> - 3.16.5-4
- Rebuild for openmpi-4.1.3

* Mon Apr 11 2022 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 3.16.5-3
- Rebuild for mpich-4.0.3

* Tue Mar 22 2022 Sandro Mani <manisandro@gmail.com> - 3.16.5-2
- Rebuild for cgnslib-4.3.0

* Sat Mar 05 2022 Antonio Trande <sagitter@fedoraproject.org> - 3.16.5-1
- Release 3.16.5

* Sat Feb 05 2022 Antonio Trande <sagitter@fedoraproject.org> - 3.16.4-1
- Release 3.16.4

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 3.16.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Jan 12 2022 Antonio Trande <sagitter@fedoraproject.org> - 3.16.3-1
- Release 3.16.3
- Fix rhbz#2039365

* Sun Nov 21 2021 Orion Poplawski <orion@nwra.com> - 3.16.0-5
- Rebuild for hdf5 1.12.1

* Sat Nov 20 2021 Antonio Trande <sagitter@fedoraproject.org> - 3.16.0-4
- Rebuild for MPI upgrades on epel8

* Sat Nov 06 2021 Antonio Trande <sagitter@fedoraproject.org> - 3.16.0-3
- Use openblas on epel8

* Sat Oct 30 2021 Antonio Trande <sagitter@fedoraproject.org> - 3.16.0-2
- Rebuild for SuperLU-5.3.0

* Sat Oct 16 2021 Antonio Trande <sagitter@fedoraproject.org> - 3.16.0-1
- Release 3.16.0

* Tue Oct 12 2021 Antonio Trande <sagitter@fedoraproject.org> - 3.15.4-4
- Rebuild for openmpi-4.1.2

* Mon Sep 20 2021 Antonio Trande <sagitter@fedoraproject.org> - 3.15.4-3
- Re-enable all builds (rhbz#2005791)

* Sun Sep 12 2021 Antonio Trande <sagitter@fedoraproject.org> - 3.15.4-2
- Set MAKE_NP option for testing
- Remove DATAFILESPATH options

* Sat Sep 11 2021 Antonio Trande <sagitter@fedoraproject.org> - 3.15.4-1
- Release 3.15.4

* Tue Aug 10 2021 Orion Poplawski <orion@nwra.com> - 3.15.3-2
- Rebuild for hdf5 1.10.7

* Sat Aug 07 2021 Antonio Trande <sagitter@fedoraproject.org> - 3.15.3-1
- Release 3.15.3

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 3.15.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jul 16 2021 Antonio Trande <sagitter@fedoraproject.org> - 3.15.2-1
- Release 3.15.2

* Sat Jun 19 2021 Antonio Trande <sagitter@fedoraproject.org> - 3.15.1-1
- Release 3.15.1

* Mon Jun 14 2021 Antonio Trande <sagitter@fedoraproject.org> - 3.15.0-5
- Fix ELN builds

* Thu Jun 10 2021 Python Maint <python-maint@redhat.com> - 3.15.0-4
- Patched and rebuilt for Python 3.10 (rhbz#1959088)

* Mon May 10 2021 Antonio Trande <sagitter@fedoraproject.org> - 3.15.0-3
- Workarounds for Python-3.10 

* Thu Apr 29 2021 Sandro Mani <manisandro@gmail.com> - 3.15.0-2
- Rebuild (cgnslib)

* Fri Apr 02 2021 Antonio Trande <sagitter@fedoraproject.org> - 3.15.0-1
- Release 3.15.0
- PETSc4py 3.15.0

* Fri Apr 02 2021 Antonio Trande <sagitter@fedoraproject.org> - 3.14.6-1
- Release 3.14.6

* Thu Mar 04 2021 Antonio Trande <sagitter@fedoraproject.org> - 3.14.5-1
- Release 3.14.5

* Sun Feb 07 2021 Antonio Trande <sagitter@fedoraproject.org> - 3.14.4-1
- Release 3.14.4
- Release PETSc4py-3.14.1

* Tue Feb 02 2021 Antonio Trande <sagitter@fedoraproject.org> - 3.14.2-5
- Rebuild for OpenMPI-4.1.0 and MPICH-3.4.1
- Explicit MPI dependencies (rhbz#1924231)

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 3.14.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Sun Dec 13 2020 Antonio Trande <sagitter@fedoraproject.org> - 3.14.2-3
- Obsolete the stand-alone PETSc4py packages
- This package now provides PETSc4py/python-petsc rpms

* Wed Dec 09 2020 Antonio Trande <sagitter@fedoraproject.org> - 3.14.2-2
- Compile PETSc4py code inside

* Sat Dec 05 2020 Antonio Trande <sagitter@fedoraproject.org> - 3.14.2-1
- Release 3.14.2

* Sat Dec 05 2020 Antonio Trande <sagitter@fedoraproject.org> - 3.14.1-3
- Update/Rebuild for MUMPS-5.3.5 on EPEL7
- Exclude superludist support on EPEL7
- Add Make BR

* Fri Nov 20 2020 Antonio Trande <sagitter@fedoraproject.org> - 3.14.1-2
- Fix pkg-config files

* Wed Nov 04 2020 Antonio Trande <sagitter@fedoraproject.org> - 3.14.1-1
- Release 3.14.1

* Fri Sep 04 2020 Antonio Trande <sagitter@fedoraproject.org> - 3.13.5-1
- Release 3.13.5

* Thu Aug 13 2020 Iñaki Úcar <iucar@fedoraproject.org> - 3.13.4-2
- https://fedoraproject.org/wiki/Changes/FlexiBLAS_as_BLAS/LAPACK_manager

* Sun Aug 02 2020 Antonio Trande <sagitter@fedoraproject.org> - 3.13.4-1
- Release 3.13.4

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.13.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Jul 02 2020 Antonio Trande <sagitter@fedoraproject.org> - 3.13.3-1
- Release 3.13.3

* Thu Jun 25 2020 Orion Poplawski <orion@cora.nwra.com> - 3.13.2-3
- Rebuild for hdf5 1.10.6

* Wed Jun 24 2020 Antonio Trande <sagitter@fedoraproject.org> - 3.13.2-2
- BuildRequires python3-setuptools explicitly

* Fri Jun 05 2020 Antonio Trande <sagitter@fedoraproject.org> - 3.13.2-1
- Release 3.13.2
- Compiled against openblas-threads

* Fri May 08 2020 Björn Esser <besser82@fedoraproject.org> - 3.13.1-2
- Rebuild (cgnslib)

* Sun May 03 2020 Antonio Trande <sagitter@fedoraproject.org> - 3.13.1-1
- Release 3.13.1

* Sun Apr 12 2020 Nicolas Chauvet <kwizart@gmail.com> - 3.13.0-2
- Rebuilt for MUMPS 5.3

* Fri Apr 10 2020 Antonio Trande <sagitter@fedoraproject.org> - 3.13.0-1
- Release 3.13.0
- Fix hdf5/cgns support
- Fix pkgconfig cflags
- Enable superludist

* Fri Feb 21 2020 Sandro Mani <manisandro@gmail.com> - 3.12.4-3
- Rebuild (cgnslib)

* Mon Feb 17 2020 Sandro Mani <manisandro@gmail.com> - 3.12.4-2
- Rebuild (cgnslib)

* Thu Feb 13 2020 Antonio Trande <sagitter@fedoraproject.org> - 3.12.4-1
- Release 3.12.4

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.12.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jan 10 2020 Antonio Trande <sagitter@fedoraproject.org> - 3.12.3-1
- Release 3.12.3

* Sun Jan 05 2020 Antonio Trande <sagitter@fedoraproject.org> - 3.12.2-2
- Fix Changelog
- Use mpiblacs on EPEL 7 and Fedora < 32

* Sat Nov 23 2019 Antonio Trande <sagitter@fedoraproject.org> - 3.12.2-1
- Release 3.12.2

* Wed Oct 23 2019 Antonio Trande <sagitter@fedoraproject.org> - 3.12.1-1
- Release 3.12.1

* Sun Oct 20 2019 Antonio Trande <sagitter@fedoraproject.org> - 3.12.0-2
- Patched for hypre-2.18.0

* Fri Oct 18 2019 Antonio Trande <sagitter@fedoraproject.org> - 3.12.0-1
- Release 3.12.0
- Rebuild for hypre 2.18.0

* Tue Oct 01 2019 Antonio Trande <sagitter@fedoraproject.org> - 3.11.3-10
- New rebuild

* Tue Oct 01 2019 Antonio Trande <sagitter@fedoraproject.org> - 3.11.3-9
- Explicit required MPICH version (rhbz#1757279)

* Thu Sep 19 2019 Orion Poplawski <orion@nwra.com> - 3.11.3-8
- Rebuild for hypre 2.17.0

* Wed Sep 11 2019 Orion Poplawski <orion@nwra.com> - 3.11.3-7
- Build for python3 only, without dts for EPEL8

* Mon Aug 26 2019 Antonio Trande <sagitter@fedoraproject.org> - 3.11.3-6
- Rebuilt for MPICH 3.2.1

* Wed Aug 21 2019 Antonio Trande <sagitter@fedoraproject.org> - 3.11.3-5
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.11.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Tue Jul 23 2019 Antonio Trande <sagitter@fedoraproject.org> - 3.11.3-3
- Complete rebuild

* Fri Jul 19 2019 Antonio Trande <sagitter@fedoraproject.org> - 3.11.3-2
- Rebuild for MUMPS-5.2.1
- Use Python 2 on EPEL

* Thu Jun 27 2019 Antonio Trande <sagitter@fedoraproject.org> - 3.11.3-1
- Release 3.11.3

* Sat May 25 2019 Antonio Trande <sagitter@fedoraproject.org> - 3.11.2-1
- Release 3.11.2

* Fri May 03 2019 Antonio Trande <sagitter@fedoraproject.org> - 3.11.1-2
- Rebuild for OpenMPI-4

* Mon Apr 15 2019 Antonio Trande <sagitter@fedoraproject.org> - 3.11.1-1
- Release 3.11.1
- Switch to Python3
- Use openblas always

* Sat Mar 16 2019 Orion Poplawski <orion@nwra.com> - 3.10.4-2
- Rebuild for hdf5 1.10.5

* Tue Mar 12 2019 Antonio Trande <sagitter@fedoraproject.org> - 3.10.4-1
- Release 3.10.4

* Tue Mar 12 2019 Sandro Mani <manisandro@gmail.com> - 3.10.3-4
- Rebuild (cgnslib)

* Thu Feb 14 2019 Orion Poplawski <orion@nwra.com> - 3.10.3-3
- Rebuild for openmpi 3.1.3

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.10.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Dec 20 2018 Antonio Trande <sagitter@fedoraproject.org> - 3.10.3-1
- Release 3.10.3

* Thu Nov 29 2018 Orion Poplawski <orion@nwra.com> - 3.10.2-2
- Re-enable OpenMPI tests - fixed with openmpi 2.1.6rc1

* Tue Oct 23 2018 Antonio Trande <sagitter@fedoraproject.org> - 3.10.2-1
- Update to 3.10.2
- Disable check of OpenMPI libraries on x86 temporarely (rhbz#1639646)

* Tue Oct 23 2018 Antonio Trande <sagitter@fedoraproject.org> - 3.9.3-5
- Fix paths inside of the 'rules' config files

* Fri Aug 03 2018 Antonio Trande <sagitter@fedoraproject.org> - 3.9.3-4
- Fix conditional macros for MPI builds

* Thu Aug 02 2018 Antonio Trande <sagitter@fedoraproject.org> - 3.9.3-3
- Exclude OpenMPI build on Fedora 28 s390x
- Patched for using Hypre-2.11.2 on epel7

* Tue Jul 31 2018 Florian Weimer <fweimer@redhat.com> - 3.9.3-2
- Rebuild with fixed binutils

* Fri Jul 27 2018 Antonio Trande <sagitter@fedoraproject.org> - 3.9.3-1
- Update to 3.9.3

* Thu Jul 19 2018 Sandro Mani <manisandro@gmail.com> - 3.9.0-5
- Rebuild (scotch)

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.9.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri May 04 2018 Antonio Trande <sagitter@fedoraproject.org> - 3.9.0-3
- Use unversioned directory for installing configuration files

* Thu Apr 26 2018 Antonio Trande <sagitter@fedoraproject.org> - 3.9.0-2
- Set again the MPI builds on Fedora

* Wed Apr 11 2018 Antonio Trande <sagitter@fedoraproject.org> - 3.9.0-1
- Update to 3.9.0

* Fri Mar 30 2018 Antonio Trande <sagitter@fedoraproject.org> - 3.8.4-1
- Update to 3.8.4
- Exclude MPI builds on s390 archirectures if fedora < 28 only
- Patched for using Hypre-2.14.0

* Tue Feb 06 2018 Antonio Trande <sagitter@fedoraproject.org> - 3.8.3-5
- Use unversioned directory for installing configuration files

* Tue Feb 06 2018 Antonio Trande <sagitter@fedoraproject.org> - 3.8.3-4
- Fix pkgconfig request on rhel

* Sun Feb 04 2018 Antonio Trande <sagitter@fedoraproject.org> - 3.8.3-3
- cgns/hdf5 support enabled (bz#1541616)

* Sat Feb 03 2018 Antonio Trande <sagitter@fedoraproject.org> - 3.8.3-2
- Fix PETSC_LIB_DIR variables
- cgns/hdf5 support temporarily disabled (bz#1541616)

* Sun Jan 28 2018 Antonio Trande <sagitter@fedoraproject.org> - 3.8.3-1
- Update to 3.8.3
- Rebuild for sundials-3.1.0

* Thu Dec 14 2017 Antonio Trande <sagitter@fedoraproject.org> - 3.8.1-4
- Not build 64-bit integer libraries on epel6

* Sun Dec 03 2017 Antonio Trande <sagitter@fedoraproject.org> - 3.8.1-3
- Build 64-bit integer libraries on epel7

* Sun Dec 03 2017 Antonio Trande <sagitter@fedoraproject.org> - 3.8.1-2
- Fix Fortran MPI library path on epel

* Wed Nov 22 2017 Antonio Trande <sagitter@fedoraproject.org> - 3.8.1-1
- Update to 3.8.1
- Disable Sundials
- Enable MUMPS on serial build

* Mon Nov 13 2017 Antonio Trande <sagitter@fedoraproject.org> - 3.8.0-5
- Install .mod files (bz#1212557)

* Thu Nov 09 2017 Antonio Trande <sagitter@fedoraproject.org> - 3.8.0-4
- Fix soname version

* Wed Nov 08 2017 Antonio Trande <sagitter@fedoraproject.org> - 3.8.0-3
- Rebuild for hypre-2.13.0
- Disable sundials on MPI builds

* Sun Oct 29 2017 Antonio Trande <sagitter@fedoraproject.org> - 3.8.0-2
- Define openblas arches

* Tue Oct 03 2017 Antonio Trande <sagitter@fedoraproject.org> - 3.8.0-1
- Update to 3.8.0
- with-mpiuni-fortran-binding option deprecated
- Remove obsolete patch2

* Mon Oct 02 2017 Antonio Trande <sagitter@fedoraproject.org> - 3.7.7-5
- Disable debugging
- Unset default compiler flags when tests are built

* Sun Oct 01 2017 Antonio Trande <sagitter@fedoraproject.org> - 3.7.7-4
- Rebuild for debugging

* Sun Oct 01 2017 Antonio Trande <sagitter@fedoraproject.org> - 3.7.7-3
- Exclude MPI builds on s390x

* Sat Sep 30 2017 Antonio Trande <sagitter@fedoraproject.org> - 3.7.7-2
- Enable mpiuni-fortran-binding on MPI builds

* Tue Sep 26 2017 Antonio Trande <sagitter@fedoraproject.org> - 3.7.7-1
- Update to 3.7.7
- Move petscvariables/petscrules under a private directory of libdir

* Wed Aug 16 2017 Antonio Trande <sagitterATfedoraproject.org> - 3.7.6-9
- Rebuild for lapack 3.7.1 (moved to 64_ suffix)

* Sun Aug 13 2017 Antonio Trande <sagitter@fedoraproject.org> - 3.7.6-8
- Option for Fedora < 25 definitively removed

* Sun Aug 13 2017 Antonio Trande <sagitter@fedoraproject.org> - 3.7.6-7
- Superlu_dist needs parmetis
- Use MPI variables

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.7.6-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.7.6-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Wed May 17 2017 Antonio Trande <sagitter@fedoraproject.org> - 3.7.6-4
- Fix Requires packages

* Mon May 15 2017 Antonio Trande <sagitter@fedoraproject.org> - 3.7.6-3
- Move petscvariables/petscrules under private directory of /usr/share

* Fri May 12 2017 Antonio Trande <sagitter@fedoraproject.org> - 3.7.6-2
- Move petscvariables/petscrules under private directory of /usr/lib

* Fri May 05 2017 Antonio Trande <sagitter@fedoraproject.org> - 3.7.6-1
- Update to 3.7.6
- Install petscvariables/petscrules
- Install pkgconfig files

* Sun Apr 09 2017 Antonio Trande <sagitter@fedoraproject.org> - 3.7.5-4
- Exclude aarch64 on fedora < 25

* Sat Mar 25 2017 Antonio Trande <sagitter@fedoraproject.org> - 3.7.5-3
- Rebuild for MUMPS-5.1.1

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.7.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Jan 04 2017 Antonio Trande <sagitter@fedoraproject.org> - 3.7.5-1
- Update to 3.7.5

* Fri Dec 02 2016 Antonio Trande <sagitter@fedoraproject.org> - 3.7.4-14
- Conditionalize mpich-devel%%{?_isa} (bz#1397192)

* Tue Nov 01 2016 Antonio Trande <sagitter@fedoraproject.org> - 3.7.4-13
- New architectures

* Wed Oct 26 2016 Antonio Trande <sagitter@fedoraproject.org> - 3.7.4-12
- Fix OpenMPI builds

* Tue Oct 25 2016 Antonio Trande <sagitter@fedoraproject.org> - 3.7.4-11
- Fix s390x builds again

* Tue Oct 25 2016 Antonio Trande <sagitter@fedoraproject.org> - 3.7.4-10
- Fix s390x builds

* Mon Oct 24 2016 Antonio Trande <sagitter@fedoraproject.org> - 3.7.4-9
- Build 64bit-int libs (bz#1382916)

* Sat Oct 22 2016 Antonio Trande <sagitter@fedoraproject.org> - 3.7.4-8
- Build 64bit-int libs (bz#1382916)

* Fri Oct 21 2016 Antonio Trande <sagitter@fedoraproject.org> - 3.7.4-7
- Install missing header files

* Wed Oct 19 2016 Antonio Trande <sagitter@fedoraproject.org> - 3.7.4-6
- Add the -O3 to restore vectorization over the RPM defaults
- Remove gmp support

* Thu Oct 13 2016 Antonio Trande <sagitter@fedoraproject.org> - 3.7.4-5
- 64bit-int libs not built (bz#1382916)
- Enable gmp and suitesparse support

* Thu Oct 13 2016 Antonio Trande <sagitter@fedoraproject.org> - 3.7.4-4
- superlu and fftw enabled
- Fixed settings of compiler flags
- Disable flags for "hardened" builds

* Mon Oct 10 2016 Antonio Trande <sagitter@fedoraproject.org> - 3.7.4-3
- Enabled fftw-mpi support (Fedora > 24)
- Omitted PAPI (obsolete)
- Omitted tetgen support (used with C++) 

* Sun Oct 09 2016 Antonio Trande <sagitter@fedoraproject.org> - 3.7.4-2
- Default optimization level (-O2)

* Sun Oct 09 2016 Antonio Trande <sagitter@fedoraproject.org> - 3.7.4-1
- Update to 3.7.4
- PAPI support disabled (upstream advice)

* Sat Oct 08 2016 Antonio Trande <sagitter@fedoraproject.org> - 3.7.3-8
- Add tcsh as BR package
- Patched for disabling petscnagupgrade.py check

* Fri Oct 07 2016 Antonio Trande <sagitter@fedoraproject.org> - 3.7.3-7
- Use Make for testing

* Thu Oct 06 2016 Antonio Trande <sagitter@fedoraproject.org> - 3.7.3-6
- Remove linkage to mpiblacs
- Tests enabled

* Thu Oct 06 2016 Antonio Trande <sagitter@fedoraproject.org> - 3.7.3-5
- hwloc/metis (needs parmetis) disabled (upstream advice)
- X support enabled
- Libraries detection disabled

* Wed Oct 05 2016 Antonio Trande <sagitter@fedoraproject.org> - 3.7.3-4
- Fix library paths

* Wed Oct 05 2016 Antonio Trande <sagitter@fedoraproject.org> - 3.7.3-3
- Fix PTScotch

* Wed Oct 05 2016 Antonio Trande <sagitter@fedoraproject.org> - 3.7.3-2
- Disabled fftw support

* Wed Sep 28 2016 Antonio Trande <sagitter@fedoraproject.org> - 3.7.3-1
- Update to 3.7.3
- Remove module files

* Tue Sep 13 2016 Antonio Trande <sagitter@fedoraproject.org> - 3.7.2-12
- Fix MAKE_NP option
- Remove --known-endian option
- Use architecture condition for openblas
- Fix unused-direct-shlib-dependency warnings

* Fri Aug 26 2016 Antonio Trande <sagitter@fedoraproject.org> - 3.7.2-11
- Use SuperLU on >=f25 only

* Thu Aug 25 2016 Antonio Trande <sagitter@fedoraproject.org> - 3.7.2-10
- Some fixes for epel6 builds
- Add -O3 flag
- Headers installed under a private directory
- Use %%{_modulesdir} macro
- Use 'openblas' instead of 'blas'

* Wed Aug 10 2016 Antonio Trande <sagitter@fedoraproject.org> - 3.7.2-9
- Fortran modules moved into devel sub-packages
- Some fixes of SPEC file's lines
- Set compiler/linker flags against PAPI-5.1.1 on epel6

* Thu Jul 28 2016 Dave Love <loveshack@fedoraproject.org> - 3.7.2-8
- Support el6
- Add cgnslib support

* Sat Jul 23 2016 Antonio Trande <sagitter@fedoraproject.org> - 3.7.2-7
- Rebuild with Hypre support

* Sun Jul 10 2016 Antonio Trande <sagitter@fedoraproject.org> - 3.7.2-6
- Packed additional header files
- Tests performed on EPEL7

* Mon Jun 27 2016 Antonio Trande <sagitter@fedoraproject.org> - 3.7.2-5
- Perform tests one-by-one
- Packaged all documentation files

* Mon Jun 27 2016 Antonio Trande <sagitter@fedoraproject.org> - 3.7.2-4
- Build OpenMPI/MPICH libraries
- Fix known-endian option

* Mon Jun 27 2016 Antonio Trande <sagitter@fedoraproject.org> - 3.7.2-3
- Disable additional libraries
- Build a minimal PETSC

* Fri Jun 24 2016 Antonio Trande <sagitter@fedoraproject.org> - 3.7.2-2
- Perform test

* Sun Jun 19 2016 Antonio Trande <sagitter@fedoraproject.org> - 3.7.2-1
- New package
