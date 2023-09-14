%global git 0
%global snapshot 20210528
%global commit f848ba0b7a55a5943658d43e9dc204f6f1beee25
%global shortcommit %(c=%{commit}; echo ${c:0:7})
%global dbcsr_commit 46cd0928465ee6bf21d82e5aac0a1970dcb54501
%global dbcsr_shortcommit %(c=%{dbcsr_commit}; echo ${c:0:7})
%global dbcsr_version 2.2.0

# TODO OpenCL support: -D__ACC -D__DBCSR_ACC -D__OPENCL

%global __provides_exclude_from ^%{_libdir}/(cp2k/lib|(mpich|openmpi)/lib/cp2k).*\\.so$
%global __requires_exclude ^lib(cp2k|clsmm|dbcsr|micsmm).*\\.so.*$

%bcond_with check

Name: cp2k
Version: 2023.1
Release: %autorelease
Summary: Ab Initio Molecular Dynamics
License: GPLv2+
URL: http://cp2k.org/
%if %{git}
Source0: https://github.com/cp2k/cp2k/archive/%{commit}/%{name}-%{shortcommit}.tar.gz
Source1: https://github.com/cp2k/dbcsr/archive/%{dbcsr_commit}/dbcsr-%{dbcsr_shortcommit}.tar.gz
%else
Source0: https://github.com/cp2k/cp2k/releases/download/v%{version}/cp2k-%{version}.tar.bz2
%endif
Source4: cp2k-snapshot.sh
# Fedora patches
# patch to:
# use rpm optflags
# link with flexiblas instead of vanilla blas/lapack
# build with libint and libxc
# build shared libraries
Patch10: %{name}-rpm.patch
BuildRequires: flexiblas-devel
# for regtests
BuildRequires: bc
BuildRequires: fftw-devel
BuildRequires: gcc-c++
BuildRequires: gcc-gfortran
BuildRequires: glibc-langpack-en
BuildRequires: libint2-devel
BuildRequires: libxc-devel >= 5.1.0
%ifarch x86_64
# See https://bugzilla.redhat.com/show_bug.cgi?id=1515404
BuildRequires: libxsmm-devel >= 1.8.1-3
%endif
BuildRequires: python3-fypp
BuildRequires: spglib-devel
BuildRequires: /usr/bin/hostname
BuildRequires: python3-devel
Provides: bundled(dbcsr) = %{dbcsr_version}

# Libint can break the API between releases
Requires: libint2(api)%{?_isa} = %{_libint2_apiversion}

Requires: %{name}-common = %{version}-%{release}

%global cp2k_desc_base \
CP2K is a freely available (GPL) program, written in Fortran 95, to\
perform atomistic and molecular simulations of solid state, liquid,\
molecular and biological systems. It provides a general framework for\
different methods such as e.g. density functional theory (DFT) using a\
mixed Gaussian and plane waves approach (GPW), and classical pair and\
many-body potentials.\
\
CP2K does not implement Car-Parinello Molecular Dynamics (CPMD).

%description
%{cp2k_desc_base}

This package contains the non-MPI single process and multi-threaded versions.

%package openmpi
Summary: Molecular simulations software - openmpi version
BuildRequires:  openmpi-devel
BuildRequires:  blacs-openmpi-devel
BuildRequires:  elpa-openmpi-devel >= 2018.05.001
BuildRequires:  scalapack-openmpi-devel
Provides: bundled(dbcsr) = %{dbcsr_version}
Requires: %{name}-common = %{version}-%{release}
# Libint may have API breakage
Requires: libint2(api)%{?_isa} = %{_libint2_apiversion}

%description openmpi
%{cp2k_desc_base}

This package contains the parallel single- and multi-threaded versions
using OpenMPI.

%package mpich
Summary: Molecular simulations software - mpich version
BuildRequires:  mpich-devel
BuildRequires:  blacs-mpich-devel
BuildRequires:  elpa-mpich-devel >= 2018.05.001
BuildRequires:  scalapack-mpich-devel
BuildRequires: make
Provides: bundled(dbcsr) = %{dbcsr_version}
Requires: %{name}-common = %{version}-%{release}
# Libint may have API breakage
Requires: libint2(api)%{?_isa} = %{_libint2_apiversion}

%description mpich
%{cp2k_desc_base}

This package contains the parallel single- and multi-threaded versions
using mpich.

%package common
Summary: Molecular simulations software - common files

%description common
%{cp2k_desc_base}

This package contains the documentation and the manual.

%prep
%if %{git}
%setup -q -n %{name}-%{commit}
tar xzf %{S:1} -C exts/dbcsr --strip-components=1
echo git:%{shortcommit} > REVISION
%else
%setup -q
%endif
%patch10 -p1 -b .r
sed -i 's|@libdir@|%{_libdir}|' Makefile
rm tools/build_utils/fypp
rm -rv exts/dbcsr/tools/build_utils/fypp

# Generate necessary symlinks
TARGET=Linux-%{_target_cpu}-gfortran
ln -s Linux-x86-64-gfortran.ssmp arch/${TARGET}.ssmp
for m in mpich openmpi ; do
    ln -s Linux-x86-64-gfortran.psmp arch/${TARGET}-${m}.psmp
done

# fix crashes in fftw on i686. Need to run on original file, otherwise symlinks will be replaced with copies.
%ifarch i686
sed -i 's/-D__FFTW3/-D__FFTW3 -D__FFTW3_UNALIGNED/g' arch/Linux-x86-64-gfortran*
%endif

for f in arch/Linux-x86-64-gfortran.{psmp,ssmp}; do
%ifarch x86_64
 sed -i 's|@LIBSMM_DEFS@|-D__LIBXSMM|;s|@LIBSMM_LIBS@|-lxsmmf -lxsmm|' $f
%else
 sed -i 's|@LIBSMM_DEFS@||;s|@LIBSMM_LIBS@||' $f
%endif
done

%{__python3} %{_rpmconfigdir}/redhat/pathfix.py -i "%{__python3} -Es" -p $(find . -type f -name *.py)

%build
TARGET=Linux-%{_target_cpu}-gfortran
OPTFLAGS_COMMON="%(echo %{optflags} | sed -e 's/ -Werror=format-security//g') -fPIC -I%{_fmoddir} -fallow-argument-mismatch"
make OPTFLAGS="${OPTFLAGS_COMMON}" DISTLDFLAGS="%{__global_ldflags} -Wl,-rpath,%{_libdir}/cp2k" %{?_smp_mflags} ARCH="${TARGET}" VERSION="ssmp"
%{_openmpi_load}
make OPTFLAGS="${OPTFLAGS_COMMON} -I%{_fmoddir}/openmpi" DISTLDFLAGS="%{__global_ldflags} -Wl,-rpath,${MPI_LIB}/cp2k" %{?_smp_mflags} ARCH="${TARGET}-openmpi" VERSION="psmp"
%{_openmpi_unload}
%{_mpich_load}
make OPTFLAGS="${OPTFLAGS_COMMON} -I%{_fmoddir}/mpich" DISTLDFLAGS="%{__global_ldflags} -Wl,-rpath,${MPI_LIB}/cp2k" %{?_smp_mflags} ARCH="${TARGET}-mpich" VERSION="psmp"
%{_mpich_unload}

%install
TARGET=Linux-%{_target_cpu}-gfortran
mkdir -p %{buildroot}{%{_bindir},%{_libdir}/cp2k,%{_datadir}/cp2k}
install -pm755 exe/${TARGET}/cp2k.ssmp %{buildroot}%{_bindir}
ln -s cp2k.ssmp %{buildroot}%{_bindir}/cp2k.sopt
ln -s cp2k.ssmp %{buildroot}%{_bindir}/cp2k_shell.ssmp
install -pm755 lib/${TARGET}/ssmp/lib*.so %{buildroot}%{_libdir}/cp2k/
install -pm755 lib/${TARGET}/ssmp/exts/dbcsr/libdbcsr.so %{buildroot}%{_libdir}/cp2k/
%{_openmpi_load}
mkdir -p %{buildroot}{${MPI_BIN},${MPI_LIB}/cp2k}
install -pm755 exe/${TARGET}-openmpi/cp2k.psmp %{buildroot}${MPI_BIN}/cp2k.psmp_openmpi
ln -s cp2k.psmp_openmpi %{buildroot}${MPI_BIN}/cp2k.popt_openmpi
ln -s cp2k.psmp_openmpi %{buildroot}${MPI_BIN}/cp2k_shell.psmp_openmpi
install -pm755 lib/${TARGET}-openmpi/psmp/lib*.so %{buildroot}${MPI_LIB}/cp2k/
install -pm755 lib/${TARGET}-openmpi/psmp/exts/dbcsr/libdbcsr.so %{buildroot}${MPI_LIB}/cp2k/
%{_openmpi_unload}
%{_mpich_load}
mkdir -p %{buildroot}{${MPI_BIN},${MPI_LIB}/cp2k}
install -pm755 exe/${TARGET}-mpich/cp2k.psmp %{buildroot}${MPI_BIN}/cp2k.psmp_mpich
ln -s cp2k.psmp_mpich %{buildroot}${MPI_BIN}/cp2k.popt_mpich
ln -s cp2k.psmp_mpich %{buildroot}${MPI_BIN}/cp2k_shell.psmp_mpich
install -pm755 lib/${TARGET}-mpich/psmp/lib*.so %{buildroot}${MPI_LIB}/cp2k/
install -pm755 lib/${TARGET}-mpich/psmp/exts/dbcsr/libdbcsr.so %{buildroot}${MPI_LIB}/cp2k/
%{_mpich_unload}
cp -pr data/* %{buildroot}%{_datadir}/cp2k/

%if %{with check}
# regtests take ~12 hours on aarch64 and ~48h on s390x
%check
cat > fedora.config << __EOF__
export LC_ALL=C
dir_base=%{_builddir}
__EOF__
. /etc/profile.d/modules.sh
export CP2K_DATA_DIR=%{buildroot}%{_datadir}/cp2k/
for mpi in '' mpich openmpi ; do
  if [ -n "$mpi" ]; then
    module load mpi/${mpi}-%{_arch}
    libdir=${MPI_LIB}/cp2k
    mpiopts="-maxtasks 4 -mpiranks 2"
    par=p
    suf="-${mpi}"
  else
    libdir=%{_libdir}/cp2k
    mpiopts=""
    par=s
    suf=""
  fi
  export LD_LIBRARY_PATH=%{buildroot}${libdir}${LD_LIBRARY_PATH:+:$LD_LIBRARY_PATH}
  tools/regtesting/do_regtest \
    -arch Linux-%{_target_cpu}-gfortran${suf} \
    -config fedora.config \
%if %{git}
    -cp2kdir cp2k-%{commit} \
%else
    -cp2kdir cp2k-%{version} \
%endif
    ${mpiopts} \
    -nobuild \
    -version ${par}smp \

  if [ -n "$mpi" ]; then
    module unload mpi/${mpi}-%{_arch}
  fi
done
%endif

%files common
%license LICENSE
%doc README.md
%{_datadir}/cp2k

%files
%{_bindir}/cp2k.sopt
%{_bindir}/cp2k.ssmp
%{_bindir}/cp2k_shell.ssmp
%dir %{_libdir}/cp2k
%{_libdir}/cp2k/lib*.so

%files openmpi
%{_libdir}/openmpi/bin/cp2k.popt_openmpi
%{_libdir}/openmpi/bin/cp2k.psmp_openmpi
%{_libdir}/openmpi/bin/cp2k_shell.psmp_openmpi
%dir %{_libdir}/openmpi/lib/cp2k
%{_libdir}/openmpi/lib/cp2k/lib*.so

%files mpich
%{_libdir}/mpich/bin/cp2k.popt_mpich
%{_libdir}/mpich/bin/cp2k.psmp_mpich
%{_libdir}/mpich/bin/cp2k_shell.psmp_mpich
%dir %{_libdir}/mpich/lib/cp2k
%{_libdir}/mpich/lib/cp2k/lib*.so

%changelog
%autochangelog
