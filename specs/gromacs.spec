#global _rcname rc1
#global _rc -%%_rcname

%if 0%{?fedora} >= 33
%global blaslib flexiblas
%else
%global blaslib openblas
%endif

# 32-bit arch
# https://gitlab.com/gromacs/gromacs/-/merge_requests/2453
# openmpi 5 & s390x
ExcludeArch:    i686 armv7hl s390x

%global with_opencl 1

%global simd None
%ifarch x86_64
%global simd SSE2
%endif
%ifarch ppc64p7
%global simd IBM_VMX
%endif
# IBM_VSX is broken with >=gcc-9
#ifarch ppc64le
#global simd IBM_VSX
#endif
%ifarch aarch64
%global simd ARM_NEON_ASIMD
%endif

Name:		gromacs
Version:	2024.5
Release:	1%{?dist}
Summary:	Fast, Free and Flexible Molecular Dynamics
# Automatically converted from old format: GPLv2+ - review is highly recommended.
License:	LGPL-2.1-or-later
URL:		http://www.gromacs.org

Source0:	https://ftp.gromacs.org/gromacs/gromacs-%{version}%{?_rc}.tar.gz
Source1:	https://ftp.gromacs.org/manual/manual-%{version}%{?_rc}.pdf
Source2:	https://ftp.gromacs.org/regressiontests/regressiontests-%{version}%{?_rc}.tar.gz
Source3:	gromacs-README.fedora
BuildRequires:	gcc-c++
BuildRequires:  cmake3 >= 3.18.4
BuildRequires:	%{blaslib}-devel
BuildRequires:	fftw-devel
BuildRequires:	gsl-devel
BuildRequires:	hwloc
BuildRequires:	hwloc-devel
BuildRequires:	lmfit-devel >= 6.0
BuildRequires:	muParser-devel
%if %{with_opencl}
BuildRequires:	ocl-icd-devel
BuildRequires:	opencl-headers
Recommends:	gromacs-opencl = %{version}-%{release}
%endif
BuildRequires:	tng-devel
# Dependencies used for regressiontest
BuildRequires:	perl(Carp)
BuildRequires:	perl(Cwd)
BuildRequires:	perl(Exporter)
BuildRequires:	perl(File::Basename)
BuildRequires:	perl(File::Copy)
BuildRequires:	perl(File::Spec)
BuildRequires:	perl(lib)
BuildRequires:	perl(List::Util)
BuildRequires:	perl(strict)
BuildRequires:	perl(vars)
%define compdir %{?bash_completions_dir}%{!?bash_completions_dir:/etc/bash_completion.d}
Requires:	gromacs-common = %{version}-%{release}
Requires:	gromacs-libs = %{version}-%{release}
Obsoletes:	gromacs-ngmx < 5.0.4-1
Obsoletes:	gromacs-csh < 2016.1-2
Obsoletes:	gromacs-zsh < 2016.1-2

%description
GROMACS is a versatile and extremely well optimized package to perform
molecular dynamics computer simulations and subsequent trajectory analysis.
It is developed for bio-molecules like proteins, but the extremely high
performance means it is used also in several other field like polymer chemistry
and solid state physics.

This package provides single and double precision binaries.
The documentation is in the package gromacs-common.

mdrun has been compiled with thread parallellization, so it runs in parallel
on shared memory systems. If you want to run on a cluster, you probably want
to install one of the MPI parallellized packages.

N.B. All binaries have names starting with g_, for example mdrun has been
renamed to g_mdrun.


%package common
Summary:	GROMACS shared data and documentation
BuildArch:	noarch
Provides:	gromacs-bash = %{version}-%{release}
Obsoletes:	gromacs-bash < 5.0.4-1

%description common
GROMACS is a versatile and extremely well optimized package to perform
molecular dynamics computer simulations and subsequent trajectory analysis.
It is developed for bio-molecules like proteins, but the extremely high
performance means it is used also in several other field like polymer chemistry
and solid state physics.

This package includes architecture independent data and HTML documentation.


%if %{with_opencl}
%package opencl
Summary:	GROMACS OpenCL kernels
# suggest installing a GPU-based OpenCL implementation
Suggests:	beignet
Suggests:	mesa-libOpenCL
# or at least a CPU-based one
Suggests:	pocl

%description opencl
GROMACS is a versatile and extremely well optimized package to perform
molecular dynamics computer simulations and subsequent trajectory analysis.
It is developed for bio-molecules like proteins, but the extremely high
performance means it is used also in several other field like polymer chemistry
and solid state physics.

This package includes the OpenCL kernels.
%endif


%package doc
Summary:	GROMACS manual
BuildArch:	noarch
Obsoletes: gromacs-common < 5.0.5-2

%description doc
GROMACS is a versatile and extremely well optimized package to perform
molecular dynamics computer simulations and subsequent trajectory analysis.
It is developed for bio-molecules like proteins, but the extremely high
performance means it is used also in several other field like polymer chemistry
and solid state physics.

This package the manual in PDF format.


%package devel
Summary:	GROMACS header files and development libraries
Requires:	gromacs-libs = %{version}-%{release}
# cmake files refer to /usr/bin/gmx as well
Requires:	gromacs = %{version}-%{release}
Obsoletes:	gromacs-mpich-devel < 2016-0.1.20160318gitbec9c87
Obsoletes:	gromacs-openmpi-devel < 2016-0.1.20160318gitbec9c87

%description devel
GROMACS is a versatile and extremely well optimized package to perform
molecular dynamics computer simulations and subsequent trajectory analysis.
It is developed for bio-molecules like proteins, but the extremely high
performance means it is used also in several other field like polymer chemistry
and solid state physics.

This package contains header files and development libraries for the GROMACS
molecular dynamics software. You need it if you want to write your own analysis
programs.


%package libs
Summary:	GROMACS shared libraries

%description libs
GROMACS is a versatile and extremely well optimized package to perform
molecular dynamics computer simulations and subsequent trajectory analysis.
It is developed for bio-molecules like proteins, but the extremely high
performance means it is used also in several other field like polymer chemistry
and solid state physics.

This package contains libraries needed for operation of GROMACS.


%package openmpi
Summary:	GROMACS Open MPI binaries and libraries
Requires:	gromacs-common = %{version}-%{release}
%if %{with_opencl}
Recommends:	gromacs-opencl = %{version}-%{release}
%endif
Obsoletes:	gromacs-openmpi-libs < 2016-0.1.20160318gitbec9c87
BuildRequires:	openmpi-devel

%description openmpi
GROMACS is a versatile and extremely well optimized package to perform
molecular dynamics computer simulations and subsequent trajectory analysis.
It is developed for bio-molecules like proteins, but the extremely high
performance means it is used also in several other field like polymer chemistry
and solid state physics.

mdrun has been compiled with thread parallellization (for running on
a single node) and with Open MPI (for running on multiple nodes).
This package single and double precision binaries and libraries.


%package mpich
Summary:	GROMACS MPICH binaries and libraries
Requires:	gromacs-common = %{version}-%{release}
%if %{with_opencl}
Recommends:	gromacs-opencl = %{version}-%{release}
%endif
Obsoletes:	gromacs-mpich-libs < 2016-0.1.20160318gitbec9c87
BuildRequires:	mpich-devel

%description mpich
GROMACS is a versatile and extremely well optimized package to perform
molecular dynamics computer simulations and subsequent trajectory analysis.
It is developed for bio-molecules like proteins, but the extremely high
performance means it is used also in several other field like polymer chemistry
and solid state physics.

mdrun has been compiled with thread parallellization (for running on
a single node) and with MPICH (for running on multiple nodes).
This package single and double precision binaries and libraries.


%prep
%autosetup -p1 %{?SOURCE2:-a 2} -n gromacs-%{version}%{?_rc}
install -Dpm644 %{SOURCE1} ./serial/docs/manual/gromacs.pdf
# Delete bundled stuff so that it doesn't get used accidentally
# Don't remove tinyxml2 as gromacs needs an old version to build
# test, see: https://redmine.gromacs.org/issues/2389
# googletest has modifications not in the packaged version
# clfft is not packaged
# Changes needed to CMakeLists to use packaged Boost stl_interfaces
rm -r src/external/{build-fftw,fftpack,lmfit,muparser,tng_io}

# increase timeout of tests
sed -i 's/set(_timeout [0-9]*)/set(_timeout 9000)/' src/testutils/TestMacros.cmake

%build
# Default options, used for all compilations
# note: Fedora's tinyxml2 is too new, so use the bundled one to build the test (only)
%global defopts \\\
 -DBUILD_TESTING:BOOL=ON \\\
 -DCMAKE_SKIP_INSTALL_RPATH=ON \\\
 -DGMX_BLAS_USER=%{blaslib} \\\
 -DGMX_BUILD_UNITTESTS:BOOL=ON \\\
 -DGMX_USE_LMFIT=EXTERNAL \\\
 -DGMX_EXTERNAL_TNG:BOOL=ON \\\
 -DGMX_EXTERNAL_TINYXML2:BOOL=OFF \\\
 -DGMX_USE_MUPARSER=EXTERNAL \\\
 -DGMX_LAPACK_USER=%{blaslib} \\\
 -DGMX_USE_RDTSCP=OFF \\\
 -DGMX_INSTALL_LEGACY_API=ON \\\
 -DGMX_VERSION_STRING_OF_FORK='Fedora%{fedora}' \\\
 -DGMX_SIMD=%{simd}

#HEFFTE only works with CUDA for now
%if %{with_opencl}
# OpenCL is available for single precision only
%global single -DGMX_GPU=OpenCL
%endif
%global double -DGMX_DOUBLE:BOOL=ON
%global mpi -DGMX_MPI:BOOL=ON -DGMX_THREAD_MPI:BOOL=OFF -DGMX_DEFAULT_SUFFIX:BOOL=OFF -DBUILD_SHARED_LIBS:BOOL=OFF -DGMX_USE_HEFFTE=OFF
%global _vpath_srcdir ..

. /etc/profile.d/modules.sh
for p in '' _d ; do
  for mpi in '' mpich openmpi ; do
    test -n "${mpi}" && module load mpi/${mpi}-%{_arch}
    mkdir -p ${mpi:-serial}${p}
    pushd ${mpi:-serial}${p}
    test -z "${mpi}" && cp -al ../regressiontests* tests/ # use with -DREGRESSIONTEST_PATH=${PWD}/tests below
    %{cmake3} %{defopts} \
      $(test -n "${mpi}" && echo %{mpi} -DGMX_BINARY_SUFFIX=${MPI_SUFFIX}${p} -DGMX_LIBS_SUFFIX=${MPI_SUFFIX}${p} -DCMAKE_INSTALL_BINDIR=${MPI_BIN} -DCMAKE_INSTALL_LIBDIR=${MPI_LIB}) \
      $(test -z "${mpi}" && echo "-DREGRESSIONTEST_PATH=${PWD}/tests") \
      $(test -n "$p" && echo %{double} || echo %{?single})
    %cmake_build
    popd
    test -n "${mpi}" && module unload mpi/${mpi}-%{_arch}
  done
done

%install
. /etc/profile.d/modules.sh
for p in '' _d ; do
  for mpi in '' mpich openmpi ; do
    test -n "${mpi}" && module load mpi/${mpi}-%{_arch}
    pushd ${mpi:-serial}${p}
    %cmake_install
    popd
    test -n "${mpi}" && module unload mpi/${mpi}-%{_arch}
  done
done

mkdir -p %{buildroot}%{_docdir}/gromacs
install -pm 644 AUTHORS COPYING README %{buildroot}%{_docdir}/gromacs
# Install manual & packager's note
install -cpm 644 serial/docs/manual/gromacs.pdf %{buildroot}%{_docdir}/gromacs/manual.pdf
install -cpm 644 %{SOURCE3} %{buildroot}%{_docdir}/gromacs/README.fedora

pushd %{buildroot}
# rm GMXRC, not needed when installed in /usr
rm ./%{_bindir}/GMXRC*

# serial stuff in mpi-versoin
rm ./%{_libdir}/*mpi*/bin/GMXRC* ./%{_libdir}/*mpi*/bin/*.pl

for bin in demux.pl xplor2gmx.pl; do
  mv ./%{_bindir}/$bin ./%{_bindir}/g_${bin}
done

# Move completion files around
mkdir -p ./%{compdir}
for bin in gmx{,_d}; do
  cat ./%{_bindir}/gmx-completion{,-$bin}.bash > ./%{compdir}/${bin}
  rm ./%{_bindir}/gmx-completion-${bin}.bash
done
rm ./%{_bindir}/gmx-completion.bash ./%{_libdir}/*mpi*/bin/gmx-completion*.bash

%ldconfig_scriptlets libs

%check
. /etc/profile.d/modules.sh
for p in '' _d ; do
  for mpi in '' mpich openmpi ; do
    test -n "${mpi}" && module load mpi/${mpi}-%{_arch}
    pushd ${mpi:-serial}${p}
    [[ ${mpi} = openmpi ]] && export OMPI_MCA_rmaps_base_oversubscribe=1 PRTE_MCA_rmaps_default_mapping_policy=:oversubscribe
    %cmake_build --target check -v
    [[ ${mpi} = openmpi ]] && unset OMPI_MCA_rmaps_base_oversubscribe PRTE_MCA_rmaps_default_mapping_policy
    popd
    test -n "${mpi}" && module unload mpi/${mpi}-%{_arch}
  done
done

%files
%{_bindir}/gmx*
%{_bindir}/g_*

%files common
%{_docdir}/gromacs
%exclude %{_docdir}/gromacs/manual.pdf
%{compdir}/gmx*
%{_mandir}/man1/gmx*.1*
%{_datadir}/%{name}
%exclude %{_datadir}/%{name}/template
%if %{with_opencl}
%exclude %{_datadir}/%{name}/opencl

%files opencl
%{_datadir}/%{name}/opencl
%endif

%files doc
%{_docdir}/gromacs/manual.pdf

%files libs
%{_libdir}/libgromacs*.so.*
%{_libdir}/libgmxapi*.so.*
%{_libdir}/libnblib*.so.*

%files devel
%{_includedir}/%{name}
%{_includedir}/gmxapi
%{_includedir}/nblib
%{_libdir}/libgromacs*.so
%{_libdir}/libgmxapi*.so
%{_libdir}/libnblib*.so
%{_libdir}/pkgconfig/libgromacs*.pc
%{_datadir}/%{name}/template
%{_datadir}/cmake/gromacs*
%{_datadir}/cmake/gmxapi*

%files openmpi
%{_libdir}/openmpi/bin/gmx_openmpi*

%files mpich
%{_libdir}/mpich/bin/gmx_mpich*

%changelog
* Sat Jan 25 2025 Christoph Junghans <junghans@votca.org> - 2024.5-1
- Version bump to v2024.5 (bug #2341964)

* Fri Jan 24 2025 Christoph Junghans <junghans@votca.org> - 2024.4-4
- Fix build with gcc-15 (bug #2340576)
- Drop heffte support again, only work with cuda for now

* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 2024.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Thu Dec 12 2024 Andrey Alekseenko <al42and@gmail.com> - 2024.4-2
- Correct SPDX license ID
- Update build-time CMake dependency and remove X11 dependency
- Remove unused CMake argument
- Remove unused bundled code
- Add overscribe environment variable for openmpi 5+

* Fri Nov 01 2024 Christoph Junghans <junghans@votca.org> - 2024.4-1
- Version bump to v2024.4 (bug #2322950)
- Enable HeFFTE support

* Tue Sep 03 2024 Christoph Junghans <junghans@votca.org> - 2024.3-1
- Version bump to v2024.3 (bug #2309068)

* Fri Jul 26 2024 Miroslav Suchý <msuchy@redhat.com> - 2024.1-3
- convert license to SPDX

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2024.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Fri May 03 2024 Christoph Junghans <junghans@votca.org> - 2024.1-1
- Version bump to v2024.1 (bug #2261951)

* Tue Jan 30 2024 Christoph Junghans <junghans@votca.org> - 2024-1
- Version bump to v2024 (bug #2261951)

* Wed Jan 24 2024 Christoph Junghans <junghans@votca.org> - 2023.4-1
- Version bump to v2023.4 (bug#2260114)

* Wed Jan 24 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2023.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sat Jan 20 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2023.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Nov 10 2023 Christoph Junghans <junghans@votca.org> - 2023.3-1
- Version bump v2023.3 (bug #2143353)

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2022.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2022.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Wed Sep 28 2022 Christoph Junghans <junghans@votca.org> - 2022.3-2
- Rebuild for muparser

* Fri Sep 02 2022 Fedora Release Monitoring <release-monitoring@fedoraproject.org> - 2022.3-1
- Update to 2022.3 (#2123647)

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2022.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Fri Jun 17 2022 Christoph Junghans <junghans@votca.org> - 2022.2-1
- Version bump to v2022.2 (bug #2097747)

* Fri Apr 22 2022 Christoph Junghans <junghans@votca.org> - 2022.1-1
- Version bump to v2022.1 (bug #2057081)

* Sat Jan 29 2022 Christoph Junghans <junghans@votca.org> - 2021.5-1
- Version bump to v2021.5 (bug #1787785)

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2019.6-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2019.6-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2019.6-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Oct 14 2020 Jeff Law <law@redhat.com> - 2019.6-8
- Add missing #includes for gcc-11

* Wed Aug 12 2020 Iñaki Úcar <iucar@fedoraproject.org> - 2019.6-7
- https://fedoraproject.org/wiki/Changes/FlexiBLAS_as_BLAS/LAPACK_manager

* Mon Aug 03 2020 Christoph Junghans <junghans@votca.org> - 2019.6-6
- Fix out-of-source build on F33 (bug #1863834)

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2019.6-5
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2019.6-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Jul 24 2020 Jeff Law <law@redhat.com> - 2019.6-3
- Use __cmake_in_source_build

* Wed Apr 01 2020 Jitka Plesnikova <jplesnik@redhat.com> - 2019.6-2
- Specify perl dependencies needed for tests

* Fri Feb 28 2020 Christoph Junghans <junghans@votca.org> - 2019.6-1
- Version bump to 2019.6

* Sat Feb 15 2020 Christoph Junghans <junghans@votca.org> - 2019.5-3
- fix build with gcc10

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2019.5-2.1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jan 09 2020 Christoph Junghans <junghans@votca.org> - 2019.5-1.1
- Rebuild for koji

* Mon Dec 23 2019 Christoph Junghans <junghans@votca.org> - 2019.5-1
- Version bump to 2019.5 (bug #1786201)

* Wed Oct 02 2019 Christoph Junghans <junghans@votca.org> - 2019.4-1
- Version bump to 2019.4 (bug #1757694)
- drop cmake-3.11.4.patch to merged upstream

* Sun Aug 25 2019 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 2019.3-1.2
- Rebuilt for hwloc-2.0

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2019.3-1.1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Jun 14 2019 Christoph Junghans <junghans@votca.org> - 2019.3-1
- Version bump to 2019.3 (bug #1720697)

* Tue Apr 16 2019 Christoph Junghans <junghans@votca.org> - 2019.2-1
- Version bump to 2019.2 (bug #1677678)

* Sat Feb 16 2019 Christoph Junghans <junghans@votca.org> - 2019.1-1
- Version bump to 2019.1 (bug #1677678)

* Thu Feb 14 2019 Orion Poplawski <orion@nwra.com> - 2018.5-2
- Rebuild for openmpi 3.1.3

* Fri Feb 01 2019 Christoph Junghans <junghans@votca.org> - 2018.5-1
- Version bump to 2018.5

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2018.4-1.1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Mon Nov 12 2018 Christoph Junghans <junghans@votca.org> - 2018.4-1
- Version bump to 2018.4
- Re-added gromacs-issue-2366.patch for f28 and lower

* Thu Nov 8 2018 Christoph Junghans <junghans@votca.org> - 2018.3-2
- Enable OpenCL for some archs on epel7
- Drop gromacs-issue-2366.patch (bug #1558206) - seems to be fixed

* Fri Nov 2 2018 Christoph Junghans <junghans@votca.org> - 2018.3-1
- Version bump to 2018.3
- Major spec files clean up

* Wed Jul 18 2018 Christoph Junghans <junghans@votca.org> - 2018.2-1
- Version bump to 2018.2 (bug #1591052)
- Add support for lmfit-7 (patch will be part of v2019)
- Switch to OpenBlas (bug #1602822)
- Disable brittle regressiontests

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2018.1-1.1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Mar 27 2018 Christoph Junghans <junghans@votca.org> - 2018.1-1
- Bump to version 2018.1 (bug #1559202)

* Sat Feb 24 2018 Christoph Junghans <junghans@votca.org> - 2018-1.2
- add gcc-c++ as BuildRequires
- use bundled tinyml2 to build tests, system one is too new

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2018-1.1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Fri Jan 19 2018 Christoph Junghans <junghans@votca.org> - 2018-1
- Update to 2018
- Drop 43a0002.diff, merged upstream

* Sat Dec 30 2017 Christoph Junghans <junghans@votca.org> - 2018-0.2rc1
- Update to 2018-rc1 for testing
- Update b7713bf.diff to 43a0002.diff

* Mon Dec 25 2017 Christoph Junghans <junghans@votca.org> - 2018-0.1beta3
- Update to 2018-beta3 for testing
- Disable HardwareTopologyTest.NumaCacheSelfconsistency test on aarch64
- Run regressiontests for serial build (don't work for mpi build)
- Clean up
  - Drop execstack as everything is intristic now
  - No la .files anymore, so drop find -delete
  - OpenMPI was ported to s390, so enable it everywhere

* Fri Sep 15 2017 Christoph Junghans <junghans@votca.org> - 2016.4-1
- Update to 2016.4

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2016.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2016.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Tue Mar 14 2017 Christoph Junghans <junghans@votca.org> - 2016.3-1
- Update to 2016.3

* Tue Feb 07 2017 Christoph Junghans <junghans@votca.org> - 2016.2-1
- Update to 2016.2
- Drop boost dependency, not uses anymore
- Drop gromacs-tng.patch, made it upstream

* Fri Jan 27 2017 Jonathan Wakely <jwakely@redhat.com> - 2016.1-3
- Rebuilt for Boost 1.63

* Fri Dec 23 2016 Christoph Junghans <junghans@votca.org> - 2016.1-2
- fixed wording description
- drop dangerous GMXRC* - not needed when installed in /usr
  would prepent /usr/lib in LD_LIBRARY_PATH
 -drop otherwise empty zsh/csh package as actual completion is done in 2016
  nothing left in package after removing GMXRC.*
- fix location of bash-completion
- added GMX_USE_RDTSCP=OFF for docker, which has not support of rdtscp yet

* Thu Nov 03 2016 Christoph Junghans <junghans@votca.org> - 2016.1-1
- Update to 2016.1
- Drop gromacs-use-system-lmfit.patch, made it upstream
- Update gromacs-tng.patch, https://gerrit.gromacs.org/#/c/6319/

* Fri Oct 21 2016 Orion Poplawski <orion@cora.nwra.com>
- Rebuild for openmpi 2.0

* Tue Aug 23 2016 Dominik 'Rathann' Mierzejewski <rpm@greysector.net> - 2016-1
- update to 2016 release
- drop upstreamed patches
- fix build with system lmfit
- fix build with bundled tng removed
- drop pocl from BuildRequires, it's not required to build
- enable OpenCL on all arches (except ppc64le, where it's still failing)

* Sat May 21 2016 Dominik 'Rathann' Mierzejewski <rpm@greysector.net> - 2016-0.5.20160510gitd44d7d6
- unbundle tinyxml2

* Sun Apr 10 2016 Dominik 'Rathann' Mierzejewski <rpm@greysector.net> - 2016-0.4.20160510gitd44d7d6
- update from git master
- enable OpenCL on armv7hl and BR: pocl >= 0.13-4 (#1324438)
- drop libxml2 BR (upstream switched to bundled tinyxml2-3.0.0)
- add missing arches in arch-dependent sections

* Wed Apr 06 2016 Dominik 'Rathann' Mierzejewski <rpm@greysector.net> - 2016-0.3.20160403gitd6e35c9
- re-enable OpenCL (pocl was fixed recently)

* Mon Apr 04 2016 Dominik 'Rathann' Mierzejewski <rpm@greysector.net> - 2016-0.2.20160403gitd6e35c9
- update to git master branch
- drop obsolete patches
- enable NEON instructions on armv7hnl arch
- drop condition around execstack usage, it's available everywhere now

* Fri Mar 18 2016 Dominik 'Rathann' Mierzejewski <rpm@greysector.net> - 2016-0.1.20160318gitbec9c87
- update to git master branch
- disable OpenCL for now (due to pocl FTBFS #1307869)
- use BOOL with all boolean cmake options
- enable hwloc support
- don't install OpenCL kernels by default (but recommend them)
- unbundle lmfit (F24+), tng
- don't build shared libs for MPI builds
- drop -libs and -devel MPI subpackages
- disable failing tests on arm and i686

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 5.1.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Tue Nov 17 2015 Dominik 'Rathann' Mierzejewski <rpm@greysector.net> - 5.1.1-1
- update to 5.1.1

* Wed Sep 23 2015 Dominik 'Rathann' Mierzejewski <rpm@greysector.net> - 5.1-6
- don't remove -DNDEBUG from CFLAGS (makes HandlesPermuteModifier test fail
  randomly)
- convert shell variables to rpm macros
- enable OpenCL support (x86 and single precision only)

* Tue Sep 22 2015 Dominik 'Rathann' Mierzejewski <rpm@greysector.net> - 5.1-5
- disable HandlesPermuteModifier test which fails randomly on i686

* Tue Sep 15 2015 Orion Poplawski <orion@cora.nwra.com> - 5.1-4
- Rebuild for openmpi 1.10.0

* Thu Aug 27 2015 Jonathan Wakely <jwakely@redhat.com> - 5.1-3
- Rebuilt for Boost 1.59

* Wed Aug 19 2015 Dominik 'Rathann' Mierzejewski <rpm@greysector.net> - 5.1-2
- enable NEON SIMD on aarch64
- fix compilation of VSX code with double precision on ppc64le
- enable VSX on ppc64le only
- don't manually output testuite logs upon failure, ctest does that already

* Sat Aug 15 2015 Dominik 'Rathann' Mierzejewski <rpm@greysector.net> - 5.1-1
- update to 5.1
- drop ancient Obsoletes:/Provides:
- drop Group: tags
- build mdrun-only MPI binaries again
- simplify SIMD enablement handling
- enable SIMD on ppc64(le)
- no execstack on ppc64 or s390(x), either
- output testsuite logs upon failure

* Sat Aug 15 2015 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 5.0.6-6
- Rebuild for MPI provides

* Mon Aug 10 2015 Sandro Mani <manisandro@gmail.com> - 5.0.6-5
- Rebuild for RPM MPI Requires Provides Change

* Thu Aug 06 2015 Dominik 'Rathann' Mierzejewski <rpm@greysector.net> - 5.0.6-4
- fix up dependencies between subpackages

* Thu Aug 06 2015 Jonathan Wakely <jwakely@redhat.com> 5.0.6-3
- Rebuilt for Boost 1.58

* Wed Jul 29 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 5.0.6-2
- Rebuilt for https://fedoraproject.org/wiki/Changes/F23Boost159

* Sun Jul 26 2015 Dominik 'Rathann' Mierzejewski <rpm@greysector.net> - 5.0.6-1
- update to 5.0.6

* Wed Jul 22 2015 David Tardon <dtardon@redhat.com> - 5.0.5-4
- rebuild for Boost 1.58

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 5.0.5-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Mon Jun 15 2015 Dominik 'Rathann' Mierzejewski <rpm@greysector.net> - 5.0.5-2
- obsolete old -common subpackage in -doc so that users don't lose the manual

* Sat Jun 13 2015 Dominik 'Rathann' Mierzejewski <rpm@greysector.net> - 5.0.5-1
- update to 5.0.5
- fix path to packaged dssp
- drop upstreamed patch
- move the large manual into a separate -doc subpackage

* Tue Apr 14 2015 Dominik 'Rathann' Mierzejewski <rpm@greysector.net> - 5.0.4-1
- update to 5.0.4
- switch Motif library to original Motif (as it's in Fedora since long)
- link against new-style atlas library (atlas 3.10.1+)
- BR: boost-devel
- csh/zsh completion removed upstream
- move bash completion into main package
- separate ngmx and mdrun dropped upstream
- enable testsuite
- factorize a lot of build logic
- drop redundant comments
- skip double precision tests on i686 (http://redmine.gromacs.org/issues/1716)

* Mon Apr 13 2015 Dominik Mierzejewski <rpm@greysector.net> - 4.6.5-6
- rebuilt for changed mpich libraries

* Sat Aug 16 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.6.5-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Fri Jun 13 2014 Peter Robinson <pbrobinson@fedoraproject.org> 4.6.5-4
- Fix builds on aarch64/ppc64le
- Modernise spec
- Remove ancient obsoletes

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.6.5-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Feb 22 2014 Deji Akingunola <dakingun@gmail.com> - 4.6.5-2
- Rebuild for mpich-3.1

* Tue Dec 03 2013 Susi Lehtola <jussilehtola@fedoraproject.org> - 4.6.5-1
- Update to 4.6.5.

* Thu Nov 14 2013 Susi Lehtola <jussilehtola@fedoraproject.org> - 4.6.4-1
- Update to 4.6.4.

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.6.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Sat Jul 20 2013 Deji Akingunola <dakingun@gmail.com> - 4.6.3-2
- Rename mpich2 sub-packages to mpich and rebuild for mpich-3.0

* Sat Jul 06 2013 Susi Lehtola <jussilehtola@fedoraproject.org> - 4.6.3-1
- Update to 4.6.3.

* Tue Jun 04 2013 Susi Lehtola <jussilehtola@fedoraproject.org> - 4.6.2-1
- Update to 4.6.2.

* Wed Mar 06 2013 Susi Lehtola <jussilehtola@fedoraproject.org> - 4.6.1-1
- Update to 4.6.1.

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Mon Jan 21 2013 Susi Lehtola <jussilehtola@fedoraproject.org> - 4.6-1
- Update to stable 4.6 release.

* Mon Dec 31 2012 Dan Horák <dan[at]danny.cz> - 4.6-0.2.beta3
- fix build on non-x86 arches

* Mon Dec 24 2012 Susi Lehtola <jussilehtola@fedoraproject.org> - 4.6-0.1.beta3
- Update to 4.6 beta 3.

* Fri Nov 02 2012 Jussi Lehtola <jussilehtola@fedoraproject.org> - 4.5.5-3.1
- Bump due to MPICH2 update.

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.5.5-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.5.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Sep 20 2011 Jussi Lehtola <jussilehtola@fedoraproject.org> - 4.5.5-1
- Update to 4.5.5.

* Wed Mar 30 2011 Deji Akingunola <dakingun@gmail.com> - 4.5.4-2
- Rebuild for mpich2 soname bump

* Wed Mar 23 2011 Jussi Lehtola <jussilehtola@fedoraproject.org> - 4.5.4-1
- Update to 4.5.4.

* Sun Feb 13 2011 Jussi Lehtola <jussilehtola@fedoraproject.org> - 4.5.3-4
- Get rid of executable stacks.

* Mon Feb 07 2011 Dan Horák <dan[at]danny.cz> - 4.5.3-3
- conditionalize OpenMPI support
- fix build on 64-bit platforms

* Mon Dec 20 2010 Jussi Lehtola <jussilehtola@fedoraproject.org> - 4.5.3-2
- Fix rest of BZ #649338.

* Thu Nov 18 2010 Jussi Lehtola <jussilehtola@fedoraproject.org> - 4.5.3-1
- Update to 4.5.3.

* Fri Nov 05 2010 Jussi Lehtola <jussilehtola@fedoraproject.org> - 4.5.2-3
- Rebuild due to libxml2 soname bump.

* Wed Nov 03 2010 Jussi Lehtola <jussilehtola@fedoraproject.org> - 4.5.2-2
- Make gromacs package obsolete older versions of gromacs package due to the
  branching of libraries.

* Mon Nov 01 2010 Jussi Lehtola <jussilehtola@fedoraproject.org> - 4.5.2-1
- Update to 4.5.2.

* Wed Oct 27 2010 Jussi Lehtola <jussilehtola@fedoraproject.org> - 4.5.1-2
- Patch around #644950.
- Split libraries in own packages to avoid multilib problems.

* Sat Oct 09 2010 Jussi Lehtola <jussilehtola@fedoraproject.org> - 4.5.1-1
- Update to 4.5.1.

* Sun Dec 06 2009 Jussi Lehtola <jussilehtola@fedoraproject.org> - 4.0.7-1
- Update to 4.0.7.

* Sun Dec 06 2009 Jussi Lehtola <jussilehtola@fedoraproject.org> - 4.0.6-1
- Update to 4.0.6.

* Fri Dec 04 2009 Jussi Lehtola <jussilehtola@fedoraproject.org> - 4.0.5-6
- Fix file conflict.

* Tue Dec 01 2009 Jussi Lehtola <jussilehtola@fedoraproject.org> - 4.0.5-5
- Put correct MPI devel package requires in place.

* Tue Dec 01 2009 Jussi Lehtola <jussilehtola@fedoraproject.org> - 4.0.5-4
- Fix obsoletes.

* Mon Nov 30 2009 Jussi Lehtola <jussilehtola@fedoraproject.org> - 4.0.5-3
- Combine libs with binaries and drop debug packages to avoid explosion of
  number of packages.
- Adopt use of MPI guidelines.

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.0.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Fri May 22 2009 Jussi Lehtola <jussi.lehtola@iki.fi> - 4.0.5-1
- Update to 4.0.5.
- Change spec %%defines to %%globals.
- Add debug subpackages to make debugging of GROMACS possible.

* Tue Feb 17 2009 Jussi Lehtola <jussi.lehtola@iki.fi> - 4.0.4-1
- Update to 4.0.4.

* Mon Jan 19 2009 Jussi Lehtola <jussi.lehtola@iki.fi> - 4.0.3-4
- Retry fixing gmxdemo.

* Mon Jan 19 2009 Jussi Lehtola <jussi.lehtola@iki.fi> - 4.0.3-3
- Fixed gmxdemo.

* Mon Jan 19 2009 Jussi Lehtola <jussi.lehtola@iki.fi> - 4.0.3-2
- Fix EPEL 4 build.

* Mon Jan 19 2009 Jussi Lehtola <jussi.lehtola@iki.fi> - 4.0.3-1
- Update to 4.0.3.

* Wed Jan 14 2009 Jussi Lehtola <jussi.lehtola@iki.fi> - 4.0.2-7
- Update manual to latest version.
- Removed Requires: blas and lapack.

* Mon Nov 10 2008 Jussi Lehtola <jussi.lehtola@iki.fi> - 4.0.2-6
- Update to 4.0.2.

* Sun Nov 09 2008 Jussi Lehtola <jussi.lehtola@iki.fi> - 4.0.1-5
- Add Requires: blas too.

* Sun Nov 09 2008 Jussi Lehtola <jussi.lehtola@iki.fi> - 4.0.1-4
- Update to 4.0.1.
- Add Requires: lapack and openmpi to prevent yum from pulling atlas and lam
instead.

* Wed Oct 15 2008 Jussi Lehtola <jussi.lehtola@iki.fi> - 4.0-3
- Rename also man pages.

* Mon Oct 13 2008 Jussi Lehtola <jussi.lehtola@iki.fi> - 4.0-2
- Added noreplace to bash completion file.
- Changed double precision mpi binary suffix to _mpi_d.

* Sun Oct 12 2008 Jussi Lehtola <jussi.lehtola@iki.fi> - 4.0-1
- Update to Gromacs 4.0.
- Remove module system and patch file names to begin with g_.

* Wed Oct 08 2008 Jussi Lehtola <jussi.lehtola@iki.fi> - 4.0-0.15.rc3
- Changed location of binaries.
- Removed conflict of module file, as the program is binary compatible with older versions.

* Wed Oct 08 2008 Jussi Lehtola <jussi.lehtola@iki.fi> - 4.0-0.14.rc3
- The gromacs module is loaded automatically and it conflicts with gromacs3.

* Tue Oct 07 2008 Jussi Lehtola <jussi.lehtola@iki.fi> - 4.0-0.13.rc3
- Renamed module files from %%{name}-%%{version} to %%{name}.

* Mon Oct 06 2008 Jussi Lehtola <jussi.lehtola@iki.fi> - 4.0-0.12.rc3
- Fix BR to get GROMACS to build in mock for epel-4.

* Sat Oct 04 2008 Jussi Lehtola <jussi.lehtola@iki.fi> - 4.0-0.11.rc3
- Fix to get GROMACS to build in mock for epel-5.

* Sat Oct 04 2008 Jussi Lehtola <jussi.lehtola@iki.fi> - 4.0-0.10.rc3
- Implement module system & remove binary renaming.
- No need for autoreconf anymore.
- Update to rc3.

* Sat Oct 04 2008 Jussi Lehtola <jussi.lehtola@iki.fi> - 4.0-0.9.rc2
- Fall back to autoreconf due to binary renaming.

* Fri Oct 03 2008 Jussi Lehtola <jussi.lehtola@iki.fi> - 4.0-0.8.rc2
- Modified install commands to preserve timestamps.

* Fri Oct 03 2008 Jussi Lehtola <jussi.lehtola@iki.fi> - 4.0-0.7.rc2
- Even more review fixes.
- Binaries renamed:
	highway	->	g_highway
	luck	->	g_luck
	sigeps	->	g_sigeps
	wheel	->	g_wheel

* Thu Oct 02 2008 Jussi Lehtola <jussi.lehtola@iki.fi> - 4.0-0.6.rc2
- Final review fixes.

* Wed Oct 01 2008 Jussi Lehtola <jussi.lehtola@iki.fi> - 4.0-0.5.rc2
- Strip down requires by branching tutor to its own package.

* Tue Sep 30 2008 Jussi Lehtola <jussi.lehtola@iki.fi> - 4.0-0.4.rc2
- Extensive package review fixes.
- Unclear licenses on some files, filed upstream bug 217.
  http://bugzilla.gromacs.org/show_bug.cgi?id=217

* Mon Sep 29 2008 Jussi Lehtola <jussi.lehtola@iki.fi> - 4.0-0.3.rc2
- Move .so files to -devel package.
- Remove .la files.

* Mon Sep 29 2008 Jussi Lehtola <jussi.lehtola@iki.fi> - 4.0-0.2.rc2
- Implement out-of-tree-builds.
- Add --noexecstack to CFLAGS.
- Remove execstack procedure and prelink from buildreqs.
- Filed upstream bug 215 to add .note.GNU-stack .
- Fix incorrect file permission on src/tools/gmx_xpm2ps.c .

* Mon Sep 29 2008 Jussi Lehtola <jussi.lehtola@iki.fi> - 4.0-0.1.rc2
- Alphabetized buildrequires.
- Changed gromacs-share to gromacs-common.

* Fri Sep 26 2008 Jussi Lehtola <jussi.lehtola@iki.fi> - 4.0-0.0.rc2
- Initial build.
