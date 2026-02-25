%bcond_without openmpi
%bcond_without mpich

Name:           osu-micro-benchmarks
Version:        7.5.2
Release:        %autorelease
Summary:        OSU Micro-Benchmarks for MPI
License:        BSD-3-Clause
URL:            https://mvapich.cse.ohio-state.edu/benchmarks/
Source0:        https://mvapich.cse.ohio-state.edu/download/mvapich/%{name}-%{version}.tar.gz
BuildRequires:  make gcc gcc-c++
# openmpi already excludes ix86. And c/util/osu_util_validation.c uses __int128_t.
# https://bugzilla.redhat.com/show_bug.cgi?id=2307721
ExcludeArch:    %{ix86}

%global desc OSU Micro-Benchmarks for MPI.\
Point-to-Point MPI Benchmarks: Latency, multi-threaded latency, multi-pair\
latency, multiple bandwidth / message rate test, bandwidth, bidirectional\
bandwidth\
Blocking Collective MPI Benchmarks: Collective latency tests for various MPI\
collective operations such as MPI_Allgather, MPI_Alltoall, MPI_Allreduce,\
MPI_Barrier, MPI_Bcast, MPI_Gather, MPI_Reduce, MPI_Reduce_Scatter, MPI_Scatter\
and vector collectives.\
Non-Blocking Collective (NBC) MPI Benchmarks: Collective latency and Overlap\
tests for various MPI collective operations such as MPI_Iallgather,\
MPI_Iallreduce, MPI_Ialltoall, MPI_Ibarrier, MPI_Ibcast, MPI_Igather,\
MPI_Ireduce, MPI_Iscatter and vector collectives.\
One-sided MPI Benchmarks: one-sided put latency, one-sided put bandwidth,\
one-sided put bidirectional bandwidth, one-sided get latency, one-sided get\
bandwidth, one-sided accumulate latency, compare and swap latency, fetch and\
operate and get_accumulate latency for MVAPICH2 (MPI-2 and MPI-3).\
Startup Benchmarks: osu_init, osu_hello

%description
%{desc}

%package common
Summary:        Common files for OSU Micro-Benchmarks
BuildArch:      noarch
%description common
This package contains common files for OSU Micro-Benchmarks.

%if %{with openmpi}
%package openmpi
Summary:        OSU Micro-Benchmarks for Open MPI
BuildRequires:  openmpi-devel
Requires:       openmpi
Requires:       %{name}-common = %{version}-%{release}
Obsoletes:      mpitests-openmpi < 7.4
%description openmpi
%{desc}

This package is built for Open MPI.
%endif

%if %{with mpich}
%package mpich
Summary:        OSU Micro-Benchmarks for MPICH
BuildRequires:  mpich-devel
Requires:       mpich
Requires:       %{name}-common = %{version}-%{release}
Obsoletes:      mpitests-mpich < 7.4
%description mpich
%{desc}

This package is built for MPICH.
%endif

%prep
%autosetup

%build
%global _configure ../configure
do_build() {
	mkdir build-$MPI_COMPILER
	pushd build-$MPI_COMPILER
	%configure
	%make_build
	popd
}

export CC=mpicc
export CXX=mpicxx

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
	pushd build-$MPI_COMPILER
	%make_install DESTDIR=%{buildroot}/staging-$MPI_COMPILER
	popd
	mkdir -p %{buildroot}$MPI_BIN
	find %{buildroot}/staging-$MPI_COMPILER -name 'osu_*' -type f -perm -111 \
		-exec mv -t %{buildroot}$MPI_BIN/ {} +
}

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

%files common
%license COPYRIGHT
%doc README CHANGES

%if %{with openmpi}
%files openmpi
%{_libdir}/openmpi/bin/osu_*
%endif

%if %{with mpich}
%files mpich
%{_libdir}/mpich/bin/osu_*
%endif

%changelog
%autochangelog
