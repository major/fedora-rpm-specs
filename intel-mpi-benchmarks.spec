%if 0%{?fedora} >= 40
%ifarch %{ix86}
%bcond_with openmpi
%else
%bcond_without openmpi
%endif
%else
%bcond_without openmpi
%endif

Summary: Intel MPI benchmarks
Name:    intel-mpi-benchmarks
Version: 2021.3
Release: 7%{?dist}
License: CPL
URL:     https://software.intel.com/en-us/articles/intel-mpi-benchmarks
Source0: https://github.com/intel/mpi-benchmarks/archive/IMB-v%{version}.tar.gz
BuildRequires: make
BuildRequires: gcc
BuildRequires: gcc-c++

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
%description openmpi
%{desc}

This package was built against the Open MPI implementation of MPI.
%endif

%package mpich
Summary: Intel MPI benchmarks compiled against mpich
BuildRequires: mpich-devel
# Require explicitly for dir ownership and to guarantee the pickup of the right runtime
Requires: mpich
Requires: %{name}-license = %{version}-%{release}
%description mpich
%{desc}

This package was built against the MPICH implementation of MPI.

%prep
%setup -q -n mpi-benchmarks-IMB-v%{version}

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

%{_mpich_load}
do_build
%{_mpich_unload}

%install
do_install() {
  mkdir -p %{buildroot}$MPI_BIN
  cd build-$MPI_COMPILER
  for f in IMB-*; do
    cp "$f" "%{buildroot}$MPI_BIN/${f}$MPI_SUFFIX"
  done
  cd ..
}

# do N installs, one for each mpi stack
%if %{with openmpi}
%{_openmpi_load}
do_install
%{_openmpi_unload}
%endif

%{_mpich_load}
do_install
%{_mpich_unload}

%files license
%license license/{,use-of-trademark-}license.txt

%if %{with openmpi}
%files openmpi
%{_libdir}/openmpi/bin/IMB-{MPI1,EXT,IO,NBC,RMA,MT,P2P}_openmpi
%endif

%files mpich
%{_libdir}/mpich/bin/IMB-{MPI1,EXT,IO,NBC,RMA,MT,P2P}_mpich

%changelog
* Wed Jan 24 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2021.3-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sat Jan 20 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2021.3-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Oct 29 2023 Orion Poplawski <orion@nwra.com> - 2021.3-5
- Rebuild for openmpi 5.0.0, drops support for i686

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2021.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2021.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2021.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Tue May 17 2022 Izabela Bakollari <izabela.bakollari@gmail.com> - 2021.3-1
- Update to upstream release v2021.3.

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2018.0-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2018.0-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2018.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2018.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2018.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2018.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Feb 14 2019 Orion Poplawski <orion@nwra.com> - 2018.0-5
- Rebuild for openmpi 3.1.3

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2018.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2018.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2018.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Fri Nov 03 2017 Michal Schmidt <mschmidt@redhat.com> - 2018.0-1
- Update to upstream release v2018.0.
- The doc/ directory has been removed by upstream. The -doc subpackage is gone.

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2017-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2017-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Tue Mar 07 2017 Michal Schmidt <mschmidt@redhat.com> - 2017-2
- Remove HTML docs from the tarball due to non-free JavaScript files.

* Wed Feb 22 2017 Michal Schmidt <mschmidt@redhat.com> - 2017-1
- Initial package for Fedora.
- Parts copied from the mpitests package from RHEL.
