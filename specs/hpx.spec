Name:           hpx
Version:        1.10.0
Release:        5%{?dist}
Summary:        General Purpose C++ Runtime System
License:        BSL-1.0
URL:            https://hpx.stellar-group.org/
Source0:        https://github.com/STEllAR-GROUP/hpx/archive/%{version}/%{name}-%{version}.tar.gz

BuildRequires:  gcc-c++ >= 4.9
BuildRequires:  gperftools-devel
BuildRequires:  boost-devel
BuildRequires:  hwloc-devel
BuildRequires:  cmake
BuildRequires:  fdupes
BuildRequires:  git
BuildRequires:  libatomic
BuildRequires:  asio-devel

%global hpx_desc \
HPX is a general purpose C++ runtime system for parallel and distributed \
applications of any scale. \
\
The goal of HPX is to create a high quality, freely available, \
open source implementation of the ParalleX model for conventional systems, \
such as classic Linux based Beowulf clusters or multi-socket highly parallel \
SMP nodes. At the same time, we want to have a very modular and well designed \
runtime system architecture which would allow us to port our implementation \
onto new computer system architectures. We want to use real world applications\
to drive the development of the runtime system, coining out required \
functionality and converging onto a stable API which will provide a smooth \
migration path for developers. The API exposed by HPX is modeled after the \
interfaces defined by the C++11 ISO standard and adheres to the \
programming guidelines used by the Boost collection of C++ libraries.

%description
%{hpx_desc}

This package contains the libraries

%package examples
Summary: HPX examples
Requires:       hpx = %{version}-%{release}

%description examples
%{hpx_desc}

This package contains the examples

%package devel
Summary:    Development headers and libraries for hpx
Requires:   hpx = %{version}-%{release}
Requires:   asio-devel
Requires:   boost-devel
Requires:   hwloc-devel
Requires:   gperftools-devel
Requires:   gcc-c++


ExcludeArch: i686

%description devel
%{hpx_desc}

This package contains development headers and libraries

%package mpich
Summary:        HPX MPICH libraries
Requires:       mpich-devel
BuildRequires:  mpich-devel

%description mpich
%{hpx_desc}

This package contains the libraries

%package mpich-examples
Summary: HPX MPICH examples
Requires:       mpich
Requires:       hpx-mpich = %{version}-%{release}
BuildRequires:  mpich-devel

%description mpich-examples
%{hpx_desc}

This package contains the examples

%package mpich-devel
Summary:    Development headers and libraries for hpx
Requires:   hpx-mpich = %{version}-%{release}
Requires:   boost-devel
Requires:   hwloc-devel
Requires:   mpich-devel
Requires:   gperftools-devel
Requires:   asio-devel

%description mpich-devel
%{hpx_desc}.

This package contains development headers and libraries

%package openmpi
Summary:        HPX Open MPI libraries
Requires:       openmpi-devel
BuildRequires:  openmpi-devel


%description openmpi
%{hpx_desc}

This package contains the libraries

%package openmpi-examples
Summary: HPX Open MPI examples
Requires:       openmpi
Requires:       hpx-openmpi = %{version}-%{release}
BuildRequires:  openmpi-devel
BuildRequires: make

%description openmpi-examples
%{hpx_desc}.

This package contains the examples


%package openmpi-devel
Summary:    Development headers and libraries for hpx
Requires:   hpx-openmpi = %{version}-%{release}
Requires:   boost-devel
Requires:   hwloc-devel
Requires:   openmpi-devel
Requires:   gperftools-devel
Requires:   asio-devel

%description openmpi-devel
%{hpx_desc}

This package contains development headers and libraries

%prep
%autosetup -p1

%build
# This package uses -Wl,-wrap to wrap calls at link time.  This is incompatible
# with LTO.
# Disable LTO
%define _lto_cflags %{nil}

# use generic context for these archs
%ifarch aarch64 
%define cmake_opts -DHPX_WITH_GENERIC_CONTEXT_COROUTINES=ON
%endif

# ppc64 do not have enough memory
%ifarch ppc64le aarch64 armv7hl
%global _smp_mflags -j1
%endif

# use a different optimization level for arm dueo to memory limitations
%ifarch armv7hl
%define cmake_opts -DCMAKE_CXX_FLAGS="$RPM_OPT_FLAGS -O1" -DHPX_WITH_GENERIC_CONTEXT_COROUTINES=ON
%endif

# add lib atomic for s390x
%ifarch s390x
%define cmake_opts -DCMAKE_SHARED_LINKER_FLAGS="$RPM_OPT_FLAGS -latomic" -DCMAKE_EXE_LINKER_FLAGS="$RPM_OPT_FLAGS -latomic"
%endif

. /etc/profile.d/modules.sh
for mpi in '' openmpi mpich ; do
  test -n "${mpi}" && module load mpi/${mpi}-%{_arch}
  mkdir -p ${mpi:-serial}
  #pushd ${mpi:-serial}
  %define _vpath_builddir %{_target_platform}-${mpi:-serial}
  test -n "${mpi}" && export CC=mpicc && export CXX=mpicxx
  %{cmake} ${mpi:+-DHPX_WITH_PARCELPORT_MPI=ON} %{?cmake_opts:%{cmake_opts}} -DHPX_WITH_BUILD_BINARY_PACKAGE=ON -DLIB_INSTALL_DIR=%_libdir/${mpi}/${mpi:+lib/} -DLIBDIR=%_libdir/${mpi}/${mpi:+lib/} -DCMAKE_INSTALL_LIBDIR=%_libdir/${mpi}/${mpi:+lib/}
  #cd %{__cmake_builddir}
  #%make_build
  %cmake_build
  #cd ..
  test -n "${mpi}" && unset CC CXX
  #popd
  test -n "${mpi}" && module unload mpi/${mpi}-%{_arch}
done

%install
# do serial install last due to move of executables to _bindir
. /etc/profile.d/modules.sh
for mpi in openmpi mpich '' ; do
  test -n "${mpi}" && module load mpi/${mpi}-%{_arch} && mkdir -p %{buildroot}/${MPI_BIN}
  #pushd ${mpi:-serial}
  #cd %{__cmake_builddir}
  %define _vpath_builddir %{_target_platform}-${mpi:-serial}
  %cmake_install
  #%make_install
  #cd ..
  #sed -i '1s@env python@python3@' %{buildroot}/%{_bindir}/{hpx*.py,hpxcxx} 
  #popd
  pushd %{buildroot}/%{_bindir}
  # rename executable with too generic names
  for exe in  *; do
    test -n '${exe##hpx*}' && mv "${exe}" "hpx_${exe}"
  done
  popd
  test -n "${mpi}" && mv %{buildroot}/%{_bindir}/* %{buildroot}/${MPI_BIN}/            
  test -n "${mpi}" && module unload mpi/${mpi}-%{_arch}
done


rm %{buildroot}/%{_datadir}/%{name}/LICENSE_1_0.txt
%fdupes %{buildroot}%{_prefix}

%check
. /etc/profile.d/modules.sh
for mpi in '' openmpi mpich ; do
  test -n "${mpi}" && module load mpi/${mpi}-%{_arch}
  make -C %{__cmake_builddir}/ tests.examples
  test -n "${mpi}" && module unload mpi/${mpi}-%{_arch}
done

%ldconfig_scriptlets

%files
%doc README.rst
%license LICENSE_1_0.txt
%{_libdir}/%{name}/
%{_libdir}/lib*.so.*

%files examples
%doc README.rst
%license LICENSE_1_0.txt
%{_bindir}/*

%files openmpi
%doc README.rst
%license LICENSE_1_0.txt
%{_libdir}/openmpi*/lib/lib*.so.*
%{_libdir}/openmpi*/lib/%{name}

%files openmpi-examples
%doc README.rst
%license LICENSE_1_0.txt
%{_libdir}/openmpi*/bin/*

%files openmpi-devel
%{_includedir}/%{name}
%{_libdir}/openmpi*/lib/pkgconfig/*.pc
%{_libdir}/openmpi*/lib/cmake/HPX
%{_libdir}/openmpi*/lib/lib*.a
%{_libdir}/openmpi*/lib/lib*.so*

%files mpich
%doc README.rst
%license LICENSE_1_0.txt
%{_libdir}/mpich*/lib/lib*.so.*
%{_libdir}/mpich*/lib/%{name}

%files mpich-examples
%doc README.rst
%license LICENSE_1_0.txt
%{_libdir}/mpich*/bin/*

%files mpich-devel
%{_includedir}/%{name}
%{_libdir}/mpich*/lib/pkgconfig/*.pc
%{_libdir}/mpich*/lib/cmake/HPX
%{_libdir}/mpich*/lib/lib*.a
%{_libdir}/mpich*/lib/lib*.so*

%files devel
%{_includedir}/%{name}
%{_libdir}/pkgconfig/*.pc
%{_libdir}/cmake/HPX
%{_libdir}/lib*.a
%{_libdir}/lib*.so*

%changelog
* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.10.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Thu Aug 22 2024 Christoph Junghans <junghans@votca.org> - 1.10.0-4
- Re-enable openmpi build

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.10.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Wed May 29 2024 Patrick Diehl <me@diehlpk.de> - 1.10.0-2
- Bump to HPX 1.10.0

* Thu May 16 2024 Patrick Diehl <me@diehlpk.de> - 1.10.0-1
- Bump to HPX 1.10.0-rc2
- Remove support for i686 due to issues with 32bit

* Wed Jan 24 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.9.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sat Jan 20 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.9.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Oct 29 2023 Orion Poplawski <orion@nwra.com> - 1.9.1-2
- Rebuild for openmpi 5.0.0, drops support for i686

* Tue Oct 10 2023 Patrick Diehl <me@diehlpk.de> - 1.9.1-1
- Bump to HPX 1.9.1

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Feb 23 2023 Christoph Junghans <junghans@votca.org> - 1.8.1-4
- Fix deps for devel packages

* Mon Feb 20 2023 Orion Poplawski <orion@nwra.com> - 1.8.1-3
- Update URL and Source (bz#2119214)
- Move Requires on libatomic to -devel subpackages (bz#2119214)
- Add upstream patch for gcc13 support (FTBFS bz#2171569)
- Use SPDX License tag

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Wed Aug 03 2022 Patrick Diehl <patrickdiehl1@gmail.com> - 1.8.1-1
- Bump to HPX 1.8.1

* Wed Jul 20 2022 Patrick Diehl <patrickdiehl1@gmail.com> - 1.8.0-1
- Bump to HPX 1.8.0

* Wed May 04 2022 Thomas Rodgers <trodgers@redhat.com> - 1.7.1-3
- Rebuilt for Boost 1.78

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Mon Aug 16 2021 patrick Diehl <patrickdiehl@lsu.edu> - 1.7.1-1
- Hpx 1.7.1

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jun 8 2021 Patrick Diehl <patrickdiehl@lsu.edu> - 1.7.0-1
- Update to HPX 1.7.0

* Tue Apr 20 2021 Patrick Diehl <patrickdiehl@lsu.edu> - 1.6.0-3
- Patch to fix examples

* Wed Mar 31 2021 Jonathan Wakely <jwakely@redhat.com> - 1.6.0-2
- Rebuilt for removed libstdc++ symbols (#1937698)

* Wed Feb 17 2021 Patrick Diehl <patrickdiehl@lsu.edu> - 1.6.0-1
- HPX 1.6.0

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Fri Jan 22 2021 Jonathan Wakely <jwakely@redhat.com> - 1.5.1-2
- Rebuilt for Boost 1.75

* Fri Oct 2 2020 Patrick Diehl <patrickdiehl@lsu.edu> - 1.5.1-1
- HPX 1.5.1

* Wed Sep 2 2020 Patrick Diehl <patrickdiehl@lsu.edu> - 1.5.0-1
- HPX 1.5.0

* Mon Jul 27 2020 Patrick Diehl <patrickdiehl@lsu.edu> - 1.4.1-4
- Update to the new cmake changes

* Fri Jul  17 2020 Patrick Diehl <patrickdiehl@lsu.edu> - 1.4.1-3
- Patch to compile with the latest boost version
- Patch to compile with a newer MPICH version

* Wed Jul  1 2020 Jeff Law <lwa@redhat.com> - 1.4.1-2
- Disable LTO

* Fri Feb 21 2020 Patrick Diehl <patrickdiehl@lsu.edu> - 1.4.1-1
- HPX 1.4.1 release - Patches to the HPX 1.4.0 release 

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Jan 15 2020 Patrick Diehl <patrickdiehl@lsu.edu> - 1.4.0-1
- HPX 1.4.0 release

* Sun Aug 25 2019 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 1.3.0-4
- Rebuilt for hwloc-2.0

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Wed Jun 26 2019 Patrick Diehl <patrickdiehl@lsu.edu>  - 1.3.0-2
- Disbale the strict compiler check

* Fri May 03 2019 Patrick Diehl <patrickdiehl@lsu.edu>  - 1.3.0-1
- HPX 1.3.0 release

* Wed Feb 20 2019 Patrick Diehl <patrickdiehl@lsu.edu>  - 1.2.1-1
- HPX 1.2.1 release

* Thu Feb 14 2019 Orion Poplawski <orion@nwra.com> - 1.2.0-7
- Rebuild for openmpi 3.1.3

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sun Dec 16 2018 Christoph Junghans <junghans@votca.org> - 1.2.0-5
- added 3591.patch to fix build on armv7hlv

* Thu Nov 22 2018 Christoph Junghans <junghans@votca.org> - 1.2.0-4
- use python3 for scripts

* Fri Nov 16 2018 Christoph Junghans <junghans@votca.org> - 1.2.0-3
- Disable parallel build for aarch64

* Thu Nov 15 2018 Christoph Junghans <junghans@votca.org> - 1.2.0-2
- Added upstream patch 3551.patch to fix build on i686

* Wed Nov 14 2018 Christoph Junghans <junghans@votca.org> - 1.2.0-1
- Version bump to hpx-1.2.0

* Fri Nov 09 2018 Patrick Diehl <patrickdiehl@lsu.edu> - 1.2-0.1.rc1
- Initial Release of HPX 1.2_rc1
