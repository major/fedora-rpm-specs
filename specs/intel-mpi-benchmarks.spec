%bcond_without openmpi
%bcond_without mpich

Summary: Intel MPI benchmarks
Name:    intel-mpi-benchmarks
Version: 2021.8
Release: %autorelease
License: BSD-3-Clause
URL:     https://software.intel.com/en-us/articles/intel-mpi-benchmarks
Source0: https://github.com/intel/mpi-benchmarks/archive/IMB-v%{version}.tar.gz
BuildRequires: make
BuildRequires: gcc
BuildRequires: gcc-c++
# https://bugzilla.redhat.com/show_bug.cgi?id=2303465
# Not worth fixing. Open MPI is no longer built on ix86.
ExcludeArch: %{ix86}

%global desc The Intel MPI Benchmarks perform a set of MPI performance measurements for\
point-to-point and global communication operations for a range of message\
sizes. The generated benchmark data fully characterizes:\
 - Performance of a cluster system, including node performance, network\
   latency, and throughput\
 - Efficiency of the MPI implementation used

%description
%{desc}

%package license
Summary: License of Intel MPI benchmarks
BuildArch: noarch
%description license
This package contains the license of Intel MPI benchmarks.

%if %{with openmpi}
%package openmpi
Summary: Intel MPI benchmarks compiled against openmpi
BuildRequires: openmpi-devel
# Require explicitly for dir ownership and to guarantee the pickup of the right runtime
Requires: openmpi
Requires: %{name}-license = %{version}-%{release}
Obsoletes: mpitests-openmpi < 7.4
%description openmpi
%{desc}

This package was built against the Open MPI implementation of MPI.
%endif

%if %{with mpich}
%package mpich
Summary: Intel MPI benchmarks compiled against mpich
BuildRequires: mpich-devel
# Require explicitly for dir ownership and to guarantee the pickup of the right runtime
Requires: mpich
Requires: %{name}-license = %{version}-%{release}
Obsoletes: mpitests-mpich < 7.4
%description mpich
%{desc}

This package was built against the MPICH implementation of MPI.
%endif

%patchlist
0001-fix-compiler-warnings-for-gcc.patch
0002-remove-Werror-flag.patch
0003-do-not-override-optimization-flags.patch

%prep
%autosetup -p1 -n mpi-benchmarks-IMB-v%{version}

%build
do_build() {
  mkdir .$MPI_COMPILER
  cp -al * .$MPI_COMPILER
  mv .$MPI_COMPILER build-$MPI_COMPILER
  cd build-$MPI_COMPILER
  export CC=mpicc
  export CXX=mpicxx
  make -f Makefile OPTFLAGS="%{optflags}" MPI_HOME="$MPI_HOME" all
  cd ..
}

# do N builds, one for each mpi stack
%if %{with openmpi}
%{_openmpi_load}
do_build
%{_openmpi_unload}
%endif

%if %{with mpich}
%{_mpich_load}
do_build
%{_mpich_unload}
%endif

%install
do_install() {
  mkdir -p %{buildroot}$MPI_BIN
  cd build-$MPI_COMPILER
  for f in IMB-*; do
    cp "$f" "%{buildroot}$MPI_BIN/"
  done
  cd ..
}

# do N installs, one for each mpi stack
%if %{with openmpi}
%{_openmpi_load}
do_install
%{_openmpi_unload}
%endif

%if %{with mpich}
%{_mpich_load}
do_install
%{_mpich_unload}
%endif

%files license
%license license/{,use-of-trademark-}license.txt

%if %{with openmpi}
%files openmpi
%{_libdir}/openmpi/bin/IMB-{MPI1,EXT,IO,NBC,RMA,MT,P2P}
%endif

%if %{with mpich}
%files mpich
%{_libdir}/mpich/bin/IMB-{MPI1,EXT,IO,NBC,RMA,MT,P2P}
%endif

%changelog
%autochangelog
