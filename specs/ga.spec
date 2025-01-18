# Warning:
# Anyone editing this spec file please make sure the same spec file
# works on other fedora and epel releases, which are supported by this software.
# No quick Rawhide-only fixes will be allowed.

%if 0%{?fedora} >= 38
# openmpi segmentation fault on i686 bug #2142304
ExcludeArch: %{ix86}
%endif

%define mpich_name mpich

%if 0%{?fedora} >= 33 || 0%{?rhel} >= 9
%global blaslib flexiblas
%else
%global blaslib openblas
%endif

Name:    ga
Version: 5.8.2
Release: 10%{?dist}
Summary: Global Arrays Toolkit
# Automatically converted from old format: BSD - review is highly recommended.
License: LicenseRef-Callaway-BSD
Source: https://github.com/GlobalArrays/ga/releases/download/v%{version}/ga-%{version}.tar.gz
URL: http://github.com/GlobalArrays/ga
ExclusiveArch: %{ix86} x86_64 %{arm} aarch64 ppc64le riscv64
BuildRequires: openmpi-devel, %{mpich_name}-devel, gcc-c++, gcc-gfortran
BuildRequires: %{blaslib}-devel, openssh-clients, dos2unix

%define ga_desc_base \
The Global Arrays (GA) toolkit provides an efficient and portable \
"shared-memory" programming interface for distributed-memory \
computers. Each process in a MIMD parallel program can asynchronously \
access logical blocks of physically distributed dense multi- \
dimensional arrays, without need for explicit cooperation by other \
processes. Unlike other shared-memory environments, the GA model \
exposes to the programmer the non-uniform memory access (NUMA) \
characteristics of the high performance computers and acknowledges \
that access to a remote portion of the shared data is slower than to \
the local portion. The locality information for the shared data is \
available, and a direct access to the local portions of shared data \
is provided.

%description
%{ga_desc_base}
- Global Arrays Toolkit Base Package.

%package common
Summary: Global Arrays Common Files
BuildArch: noarch
%description common
%{ga_desc_base}
- Global Arrays Common Files.

%package mpich
Summary: Global Arrays Toolkit for MPICH
BuildRequires: scalapack-%{mpich_name}-devel
BuildRequires: %{blaslib}-devel
Requires: %{name}-common = %{version}
Provides: %{name}-mpich2 = %{version}-%{release}
Obsoletes: %{name}-mpich2 < %{version}-%{release}
%description mpich
%{ga_desc_base}
- Libraries against MPICH.
%package mpich-devel
Summary: Global Arrays Toolkit for MPICH Development
Requires: scalapack-%{mpich_name}-devel, %{mpich_name}-devel
Requires: %{blaslib}-devel, %{name}-common = %{version}, %{name}-mpich = %{version}
Provides: %{name}-mpich2-devel = %{version}-%{release}
Obsoletes: %{name}-mpich2-devel < %{version}-%{release}
%description mpich-devel
%{ga_desc_base}
- Development Software against MPICH.
%package mpich-static
Summary: Global Arrays Toolkit for MPICH Static Libraries
Requires: scalapack-%{mpich_name}-devel, %{mpich_name}-devel
Requires: %{blaslib}-devel, %{name}-common = %{version}, %{name}-mpich = %{version}
Provides: %{name}-mpich2-static = %{version}-%{release}
Obsoletes: %{name}-mpich2-static < %{version}-%{release}
%description mpich-static
%{ga_desc_base}
- Static Libraries against MPICH.
%ldconfig_scriptlets mpich

%package openmpi
Summary: Global Arrays Toolkit for OpenMPI
BuildRequires: scalapack-openmpi-devel
BuildRequires: %{blaslib}-devel
BuildRequires: make
Requires: %{name}-common = %{version}
%description openmpi
%{ga_desc_base}
- Libraries against OpenMPI.
%package openmpi-devel
Summary: Global Arrays Toolkit for OpenMPI Development
Requires: scalapack-openmpi-devel, openmpi-devel
Requires: %{blaslib}-devel, %{name}-common = %{version}, %{name}-openmpi = %{version}
%description openmpi-devel
%{ga_desc_base}
- Development Software against OpenMPI.
%package openmpi-static
Summary: Global Arrays Toolkit for OpenMPI Static Libraries
Requires: scalapack-openmpi-devel, openmpi-devel
Requires: %{blaslib}-devel, %{name}-common = %{version}, %{name}-openmpi = %{version}
%description openmpi-static
%{ga_desc_base}
- Static Libraries against OpenMPI.
%ldconfig_scriptlets openmpi


%define ga_version %{version}

%prep
%setup -q -c -n %{name}-%{version}

pushd %{name}-%{ga_version}

popd
for i in mpich openmpi; do
  cp -a %{name}-%{ga_version} %{name}-%{version}-$i
done


%build
%define doBuild \
export LIBS="-lscalapack -l%{blaslib}" && \
export CFLAGS="%{optflags} -O1" && \
export CXXFLAGS="%{optflags} -O1" && \
export FFLAGS="%{optflags} -O1" && \
cd %{name}-%{version}-$MPI_COMPILER_NAME && \
%configure \\\
  --bindir=$MPI_BIN \\\
  --libdir=$MPI_LIB \\\
  --includedir=$MPI_INCLUDE \\\
  --with-scalapack4=-lscalapack \\\
  --with-blas4=-l%{blaslib} \\\
  --enable-shared \\\
  --enable-static \\\
  --enable-cxx \\\
  --enable-f77 \\\
  $GA_CONFIGURE_OPTIONS && \
%make_build && \
cd ..

export MPI_COMPILER_NAME=mpich
export GA_CONFIGURE_OPTIONS=""
%{_mpich_load}
%doBuild
%{_mpich_unload}

export MPI_COMPILER_NAME=openmpi
%{_openmpi_load}
%doBuild
%{_openmpi_unload}


%install
%define doInstall \
cd %{name}-%{version}-$MPI_COMPILER_NAME && \
%make_install && \
cd ..

rm -rf $RPM_BUILD_ROOT
export MPI_COMPILER_NAME=mpich
%{_mpich_load}
%doInstall
%{_mpich_unload}

export MPI_COMPILER_NAME=openmpi
%{_openmpi_load}
%doInstall
%{_openmpi_unload}

find %{buildroot} -type f -name "*.la" -exec rm -f {} \;

mkdir -p $RPM_BUILD_ROOT/%{_sysconfdir}/sysctl.d
echo 'kernel.shmmax = 134217728' > $RPM_BUILD_ROOT/%{_sysconfdir}/sysctl.d/armci.conf
%define do_test 1
%check
%if %{?do_test}0
%if 0%{?rhel} != 6
%{_mpich_load}
cd %{name}-%{version}-mpich
make NPROCS=2 VERBOSE=1 check-ma check-travis
make NPROCS=2 TESTS="global/testing/test.x global/testing/testc.x global/testing/testmatmult.x global/testing/patch.x global/testing/simple_groups_comm.x global/testing/elempatch.x" check-TESTS VERBOSE=1
cd ..
%{_mpich_unload}
%endif
%{_openmpi_load}
cd %{name}-%{version}-openmpi
export OMPI_MCA_btl=^uct
export OMPI_MCA_btl_base_warn_component_unused=0
make NPROCS=2 VERBOSE=1 check-ma check-travis
make NPROCS=2 TESTS="global/testing/test.x global/testing/testc.x global/testing/testmatmult.x global/testing/patch.x global/testing/simple_groups_comm.x global/testing/elempatch.x" check-TESTS VERBOSE=1
cd ..
%{_openmpi_unload}
%endif

%files common
%doc %{name}-%{ga_version}/README.md %{name}-%{ga_version}/CHANGELOG.md
%doc %{name}-%{ga_version}/DISCLAIMER %{name}-%{ga_version}/LICENSE
%config(noreplace) %{_sysconfdir}/sysctl.d/armci.conf

%files mpich
%doc %{name}-%{ga_version}/DISCLAIMER %{name}-%{ga_version}/LICENSE
%{_libdir}/%{mpich_name}/lib/lib*.so.*
%{_libdir}/%{mpich_name}/bin/*.x
%files mpich-devel
%doc %{name}-%{ga_version}/DISCLAIMER %{name}-%{ga_version}/LICENSE
%{_libdir}/%{mpich_name}/lib/lib*.so
%{_includedir}/%{mpich_name}-%{_arch}/*
%{_libdir}/%{mpich_name}/bin/ga-config
%{_libdir}/%{mpich_name}/bin/armci-config
%{_libdir}/%{mpich_name}/bin/comex-config
%files mpich-static
%doc %{name}-%{ga_version}/DISCLAIMER %{name}-%{ga_version}/LICENSE
%{_libdir}/%{mpich_name}/lib/lib*.a

%files openmpi
%doc %{name}-%{ga_version}/DISCLAIMER %{name}-%{ga_version}/LICENSE
%{_libdir}/openmpi/lib/lib*.so.*
%{_libdir}/openmpi/bin/*.x
%files openmpi-devel
%doc %{name}-%{ga_version}/DISCLAIMER %{name}-%{ga_version}/LICENSE
%{_libdir}/openmpi/lib/lib*.so
%{_includedir}/openmpi-%{_arch}/*
%{_libdir}/openmpi/bin/ga-config
%{_libdir}/openmpi/bin/armci-config
%{_libdir}/openmpi/bin/comex-config
%files openmpi-static
%doc %{name}-%{ga_version}/DISCLAIMER %{name}-%{ga_version}/LICENSE
%{_libdir}/openmpi/lib/lib*.a

%changelog
* Thu Jan 16 2025 Fedora Release Engineering <releng@fedoraproject.org> - 5.8.2-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Wed Aug 28 2024 Miroslav Suchý <msuchy@redhat.com> - 5.8.2-9
- convert license to SPDX

* Wed Jul 17 2024 Fedora Release Engineering <releng@fedoraproject.org> - 5.8.2-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Sun Apr 14 2024 Marcin Dulak <marcindulak@fedoraproject.org> - 5.8.2-7
- Correct shell continuation to be && instead of ;
- Use make macros
- https://fedoraproject.org/wiki/Changes/UseMakeBuildInstallMacro
- The above two thanks to https://src.fedoraproject.org/rpms/ga/pull-request/1

* Thu Apr 11 2024 Jiasheng Zhao <JasenChao@gmail.com> - 5.8.2-6
- Add riscv64 support

* Wed Jan 24 2024 Fedora Release Engineering <releng@fedoraproject.org> - 5.8.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 5.8.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Oct 29 2023 Orion Poplawski <orion@nwra.com> - 5.8.2-3
- Rebuild for openmpi 5.0.0, drops C++ API

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 5.8.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 19 2023 Marcin Dulak <marcindulak@fedoraproject.org> - 5.8.2-1
- New upstream release

* Thu Jan 19 2023 Marcin Dulak <marcindulak@fedoraproject.org> - 5.7.2-13
- Exlude %%{ix86} due to bug #2142304

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 5.7.2-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Mon Dec 12 2022 Florian Weimer <fweimer@redhat.com> - 5.7.2-11
- Apply upstream patches to port to C99

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 5.7.2-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Sun Jan 23 2022 Marcin Dulak <marcindulak@fedoraproject.org> - 5.7.2-9
- Run configure in the build section, bug #2044028
- Reduce the optimization to -O1, bug #2045402

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 5.7.2-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 5.7.2-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 5.7.2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Fri Aug 28 2020 Iñaki Úcar <iucar@fedoraproject.org> - 5.7.2-5
- https://fedoraproject.org/wiki/Changes/FlexiBLAS_as_BLAS/LAPACK_manager

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 5.7.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Mar 05 2020 Edoardo Apra <edoardo.apra@gmail.com> - 5.7.2-3
- fixed 5.7.2 version
- fixed dereferencing type-punned pointer warning

* Tue Mar 03 2020 Edoardo Apra <edoardo.apra@gmail.com> - 5.7.2-2
- work-around for openmpi 4.0.1 segfault
- perform small number of tests with NPROC=2

* Fri Feb 28 2020 Edoardo Apra <edoardo.apra@gmail.com> - 5.7.2-1
- Release 5.7.2 from https://github.com/GlobalArrays/ga/

* Mon Feb 17 2020 Edoardo Apra <edoardo.apra@gmail.com> - 5.7.1-1
- Release 5.7.1
- enabled tests
- removed ga-openmpi-pr RPMs

* Fri Feb 14 2020 Marcin Dulak <marcindulak@fedoraproject.org> - 5.6.5-8
- -fallow-argument-mismatch fix for gfortran 10

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 5.6.5-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Oct 02 2019 Edoardo Apra <edoardo.apra@gmail.com> - 5.7-1.1
- added ga-openmpi-pr RPMs built with NETWORK=MPI-PR

* Tue Oct 01 2019 Edoardo Apra <edoardo.apra@gmail.com> - 5.7-1
- Release 5.7
- removed openib target
- fix for MKL error "PDSTEDC parameter number 10 had an illegal value"
- fix for MPI-2 deprecated MPI_Type_struct and MPI_Errhandler_set
- added NOUSE_MMAP config.h option for 32bit linux
- fix for pgcc configure error

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 5.6.5-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Feb 14 2019 Orion Poplawski <orion@nwra.com> - 5.6.5-5
- Rebuild for openmpi 3.1.3

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 5.6.5-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Tue Aug 07 2018 Edoardo Apra <edoardo.apra@gmail.com> - 5.6.5-3
- fortran integer casting in ga_diag. Fixes #1613089

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 5.6.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Jun 13 2018 Edoardo Apra <edoardo.apra@gmail.com> - 5.6.5-1
- New release 5.6.5
- Replaced Atlas with OpenBLAS
- Made compatible with ScaLapack RPM updates
- Added options -with-blas4 to work with NWChem

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 5.6.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Fri Aug 25 2017 Adam Williamson <awilliam@redhat.com> - 5.6.1-1
- New release 5.6.1
- Minor spec fixups

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 5.3b-24
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 5.3b-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 5.3b-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri Oct 21 2016 Orion Poplawski <orion@cora.nwra.com> - 5.3b-21
- Rebuild for openmpi 2.0

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 5.3b-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Tue Sep 15 2015 Orion Poplawski <orion@cora.nwra.com> - 5.3b-19
- Rebuild for openmpi 1.10.0

* Sun Jul 26 2015 Sandro Mani <manisandro@gmail.com> - 5.3b-18
- Rebuild for RPM MPI Requires Provides Change

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 5.3b-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat May 02 2015 Kalev Lember <kalevlember@gmail.com> - 5.3b-16
- Rebuilt for GCC 5 C++11 ABI change

* Fri Mar 20 2015 David Brown <david.brown@pnnl.gov> - 5.3b-15
- Rebuild to support new version of mpich

* Wed Nov 19 2014 David Brown <david.brown@pnnl.gov> - 5.3b-14
- Fix bug #1150473 to support epel7

* Wed Oct 29 2014 David Brown <david.brown@pnnl.gov> - 5.3b-13
- Rebuild to fix bug #1155077

* Sun Oct 5 2014 David Brown <david.brown@pnnl.gov> - 5.3b-12
- Fix up some conditions for f22
- Add more dependancies on lapack-devel in right places

* Tue Sep 30 2014 David Brown <david.brown@pnnl.gov> - 5.3b-11
- Rebuilt for updated upstream package

* Sat Aug 16 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 5.3b-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Mon Jul 07 2014 David Brown <david.brown@pnnl.gov> - 5.3b-8
- add explicit requires for mpich and openmpi packages (#1116627)

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 5.3b-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Mon May 12 2014 Tom Callaway <spot@fedoraproject.org> - 5.3b-7
- rebuild against new blacs

* Thu Mar 27 2014 David Brown <david.brown@pnnl.gov> - 5.3b-6
- version bump to get all fedora/epel versions in sync

* Thu Mar 27 2014 David Brown <david.brown@pnnl.gov> - 5.3b-5
- Parameterize mpich name and environment loading to cover EPEL

* Thu Mar 27 2014 David Brown <david.brown@pnnl.gov> - 5.3b-4
- Update to include configure option fixes (1081403)

* Sun Feb 23 2014 David Brown <david.brown@pnnl.gov> - 5.3b-3
- Updated revision for new mpich

* Wed Feb 5 2014 David Brown <david.brown@pnnl.gov> - 5.3b-2
- Fix BuildRoot
- add more generic/specific atlas config

* Mon Jan 27 2014 David Brown <david.brown@pnnl.gov> - 5.3b-1
- Update to upstream version
- Fix exclusive arch to match documentation
- add patch for format security fixes (1037075)

* Mon Sep 23 2013 David Brown <david.brown@pnnl.gov> - 5.1.1-8
- Rebuild for updated atlas.
- Fix atlas libs since they changed things

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 5.1.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Mon Jul 22 2013 David Brown <david.brown@pnnl.gov> - 5.1.1-6
- forgot obsoletes and provides for sub packages as well.

* Mon Jul 22 2013 David Brown <david.brown@pnnl.gov> - 5.1.1-5
- forgot about obsoletes and provides for new mpich packages.

* Mon Jul 15 2013 David Brown <david.brown@pnnl.gov> - 5.1.1-4
- Rebuild for updated openmpi
- resolved issues with doBuild function to proper define
- also renamed mpich2 to mpich

* Tue May 21 2013 David Brown <david.brown@pnnl.gov> - 5.1.1-3
- modify exclusive arch some more (964424, 964946)

* Tue May 14 2013 David Brown <david.brown@pnnl.gov> - 5.1.1-2
- Add exclusive arch for EPEL.
- And lib*.la files are bad too.

* Wed May 1 2013 David Brown <david.brown@pnnl.gov> - 5.1.1-1
- Update to upstream version
- fixed file locations and clean up rpmlint

* Thu Jul 5 2012 David Brown <david.brown@pnnl.gov> - 5.1-2
- added common package with license and sysctl additions

* Mon Apr 9 2012 David Brown <david.brown@pnnl.gov> - 5.1-1
- initial packaging

