# We have to call the package libASL instead of ASL, because a package asl
# exists. https://fedoraproject.org/wiki/Packaging:Conflicts#Conflicting_Package_Names
%global upstream ASL
%global _cmake_build_subdir build-%{?__isa}%{?dist}

Name:           lib%{upstream}
Version:        0.1.7
Release:        42%{?dist}
Summary:        Advanced Simulation Library hardware accelerated multiphysics simulation platform

License:        AGPLv3 and BSD and MIT
# ===== License-breakdown =====
#
# AGPL (v3)
# ---------
# * except the files explicitly named below
#
# BSD (3 clause)
# --------------
# cmake/Modules/FindMATIO.cmake
# cmake/Modules/FindOpenCL.cmake
# cmake/Modules/FindPackageMessage.cmake
#
# MIT/X11 (BSD like)
# ------------------
# src/acl/cl.hpp
#

URL:            http://asl.org.il/
Source0:        https://github.com/AvtechScientific/%{upstream}/archive/v%{version}/%{upstream}-%{version}.tar.gz
# Add support for VTK8
# https://github.com/AvtechScientific/ASL/pull/44
Patch0:         libASL-vtk8.patch

BuildRequires:  boost-devel
BuildRequires:  cmake3
BuildRequires:  doxygen
BuildRequires:  graphviz
BuildRequires:  matio-devel
BuildRequires:  netcdf-cxx-devel
BuildRequires:  ocl-icd-devel
BuildRequires:  opencl-headers
BuildRequires:  vtk-devel
# For tests, pocl not available on EPEL
%if 0%{?fedora}
%ifnarch aarch64 ppc64 ppc64le s390 s390x
BuildRequires:  pocl-devel
%endif
%endif

%description
Advanced Simulation Library (ASL) is a free and open source hardware
accelerated multiphysics simulation platform (and an extensible general
purpose tool for solving Partial Differential Equations). Its
computational engine is written in OpenCL and utilizes matrix-free
solution techniques which enable extraordinarily high performance,
memory efficiency and deployability on a variety of massively parallel
architectures, ranging from inexpensive FPGAs, DSPs and GPUs up to
heterogeneous clusters and supercomputers. The engine is hidden entirely
behind simple C++ classes, so that no OpenCL knowledge is required from
application programmers. Mesh-free, immersed boundary approach allows to
move from CAD directly to simulation drastically reducing pre-processing
efforts and amount of potential errors. ASL can be used to model various
coupled physical and chemical phenomena and employed in a multitude of
fields: computational fluid dynamics, virtual sensing, industrial
process data validation and reconciliation, image-guided surgery,
computer-aided engineering, design space exploration, crystallography,
etc..


%package        bin 
Summary:        Binaries for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    bin
Binaries for %{name}

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       boost-devel%{?_isa}
Requires:       matio-devel%{?_isa}
Requires:       netcdf-cxx-devel%{?_isa}
Requires:       ocl-icd-devel%{?_isa}
Requires:       opencl-headers
Requires:       vtk-devel%{?_isa}


%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%package        doc
# Not noarch here because otherwise koji fails 
# http://koji.fedoraproject.org/koji/taskinfo?taskID=11237671
#BuildArch:      noarch
Summary:        Documentation for %{name}

%description    doc
The %{name}-doc package contains documentation for %{name}

%package        examples
Summary:        Examples for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    examples
The %{name}-examples package contains examples for %{name}

%prep
%setup -q -n %{upstream}-%{version}
%patch0 -p1 -b .vtk8
# These conflict with current cmake
# https://github.com/AvtechScientific/ASL/pull/49
rm cmake/Modules/{CMakeParseArguments,FindOpenCL,FindPackageHandleStandardArgs}.cmake

%build
%cmake  -DWITH_API_DOC:BOOL=ON \
        -DWITH_MATIO:BOOL=ON  \
        -DWITH_EXAMPLES=ON \
        -DWITH_TESTS=ON 
%cmake_build
%cmake_build --target docs

%install
%cmake_install
find %{buildroot} -name '*.la' -delete

# Move docs and examples to right places
%{__mkdir_p} %{buildroot}%{_docdir}/%{name}-doc
mv %{buildroot}%{_docdir}/%{upstream}/html %{buildroot}%{_docdir}/%{name}-doc
mv %{buildroot}%{_docdir}/%{upstream}/examples %{buildroot}%{_docdir}/%{name}-examples
# Move input data for examples
# https://github.com/AvtechScientific/ASL/commit/0246d6adb1ebded5b2ef1d0e82433f86d90ea4ba
mv %{buildroot}%{_datadir}/%{upstream}/input %{buildroot}%{_docdir}/%{name}-examples


%if 0%{?fedora}
%ifnarch %{arm} aarch64 ppc64 ppc64le s390 s390x
# Do nothing for now... pocl is broken, therefore we cannot test
%check
#pushd %{_cmake_build_subdir}
# Test failures
# https://github.com/AvtechScientific/ASL/issues/16
#ctest3 -V -E 'testPrivateVar|testReductionFunction'
#ctest3 -V -R 'testPrivateVar|testReductionFunction' || :
%endif
%endif


%ldconfig_scriptlets


%files
%license COPYRIGHT.org LICENSE
%doc NEWS.org README.org
%{_libdir}/*.so.*

%files bin
%license COPYRIGHT.org LICENSE
%{_bindir}/asl-hardware

%files devel
%license COPYRIGHT.org LICENSE
%dir %{_libdir}/cmake/%{upstream}
%{_includedir}/*
%{_libdir}/*.so
%{_libdir}/cmake/%{upstream}/*.cmake
%{_libdir}/pkgconfig/%{upstream}.pc

%files doc
%license COPYRIGHT.org LICENSE
%dir %{_docdir}/%{name}-doc
%{_docdir}/%{name}-doc/html

%files examples
%license COPYRIGHT.org LICENSE
%dir %{_docdir}/%{name}-examples
%{_docdir}/%{name}-examples/*
%{_bindir}/asl-acousticWaves
%{_bindir}/asl-bus_wind
%{_bindir}/asl-compressor
%{_bindir}/asl-cubeGravity
%{_bindir}/asl-cubeIncompressibleGravity
%{_bindir}/asl-cubePoroelasticGravity
%{_bindir}/asl-flow
%{_bindir}/asl-flow2
%{_bindir}/asl-flow3
%{_bindir}/asl-flowKDPGrowth
%{_bindir}/asl-flowRotatingCylinders
%{_bindir}/asl-jumpingBox
%{_bindir}/asl-levelSetBasic
%{_bindir}/asl-levelSetFacetedGrowth
%{_bindir}/asl-levelSetNormalGrowth
%{_bindir}/asl-locomotive
%{_bindir}/asl-locomotive_laminar
%{_bindir}/asl-locomotive_stability
%{_bindir}/asl-multicomponent_flow
%{_bindir}/asl-multiphase_flow
%{_bindir}/asl-pitot_tube_ice
%{_bindir}/asl-poroelastic
%{_bindir}/asl-surfaceFlux
%{_bindir}/asl-testSMDiff
%{_bindir}/asl-testSMDiff3C
%{_bindir}/asl-testSMPhi
%{_bindir}/asl-testSMPhiBV


%changelog
* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.7-42
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.7-41
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Jan 17 2024 Jonathan Wakely <jwakely@redhat.com> - 0.1.7-40
- Rebuilt for Boost 1.83

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.7-39
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Mon Feb 20 2023 Jonathan Wakely <jwakely@redhat.com> - 0.1.7-38
- Rebuilt for Boost 1.81

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.7-37
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Sun Jan 15 2023 Orion Poplawski <orion@nwra.com> - 0.1.7-36
- Rebuild for vtk 9.2.5

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.7-35
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed May 04 2022 Thomas Rodgers <trodgers@redhat.com> - 0.1.7-34
- Rebuilt for Boost 1.78

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.7-33
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Nov 25 2021 Orion Poplawski <orion@nwra.com> - 0.1.7-32
- Rebuild for vtk 9.1.0

* Fri Aug 06 2021 Jonathan Wakely <jwakely@redhat.com> - 0.1.7-31
- Rebuilt for Boost 1.76

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.7-30
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Mon Apr 05 2021 Gwyn Ciesla <gwync@protonmail.com> - 0.1.7-29
- matio rebuild

* Sun Jan 31 2021 Orion Poplawski <orion@nwra.com> - 0.1.7-28
- Rebuild for VTK 9

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.7-27
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Fri Jan 22 2021 Jonathan Wakely <jwakely@redhat.com> - 0.1.7-26
- Rebuilt for Boost 1.75

* Mon Sep 21 2020 Gwyn Ciesla <gwync@protonmail.com> - 0.1.7-25
- Matio rebuild.

* Tue Aug 25 2020 Christian Dersch <lupinix@mailbox.org> - 0.1.7-24
- Use cmake macros

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.7-23
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.7-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu May 28 2020 Jonathan Wakely <jwakely@redhat.com> - 0.1.7-21
- Rebuilt for Boost 1.73

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.7-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.7-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Mon Mar 18 2019 Orion Poplawski <orion@nwra.com> - 0.1.7-18
- Rebuild for vtk 8.2

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.7-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jan 25 2019 Jonathan Wakely <jwakely@redhat.com> - 0.1.7-16
- Rebuilt for Boost 1.69

* Sat Oct 27 2018 Orion Poplawski <orion@cora.nwra.com> - 0.1.7-15
- Rebuild for VTK 8.1

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.7-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 14 2018 Christian Dersch <lupinix@mailbox.org> - 0.1.7-13
- Disabled all tests as pocl is currently broken...

* Tue Feb 13 2018 Christian Dersch <lupinix@mailbox.org> - 0.1.7-12
- rebuilt

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.7-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Tue Jan 23 2018 Jonathan Wakely <jwakely@redhat.com> - 0.1.7-10
- Rebuilt for Boost 1.66

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.7-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.7-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Wed Jul 19 2017 Jonathan Wakely <jwakely@redhat.com> - 0.1.7-7
- Rebuilt for s390x binutils bug

* Tue Jul 18 2017 Jonathan Wakely <jwakely@redhat.com> - 0.1.7-6
- Rebuilt for Boost 1.64

* Sat Mar 04 2017 Christian Dersch <lupinix@mailbox.org> - 0.1.7-5
- Deactivated tests on armv7hl for now

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.7-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Dec 7 2016 Orion Poplawski <orion@cora.nwra.com> - 0.1.7-3
- Rebuild for vtk 7.1

* Wed Nov 09 2016 Orion Poplawski <orion@cora.nwra.com> - 0.1.7-2
- Updated summary
- Use cmake3 for EPEL7 compatibility
- Run tests on supported pocl arches

* Wed Nov 09 2016 Christian Dersch <lupinix@mailbox.org> - 0.1.7-1
- new version

* Sun Jul 03 2016 Christian Dersch <lupinix@mailbox.org> - 0.1.6-6
- Rebuilt for matio 1.5.8

* Fri May 13 2016 Christian Dersch <lupinix@mailbox.org> - 0.1.6-5
- Rebuilt for gcc 6.1.1

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.6-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Sat Jan 23 2016 Christian Dersch <lupinix@mailbox.org> - 0.1.6-3
- Rebuild for boost 1.60

* Fri Jan 22 2016 Orion Poplawski <orion@cora.nwra.com> - 0.1.6-2
- Rebuild for netcdf 4.4.0

* Mon Nov 09 2015 Christian Dersch <lupinix@fedoraproject.org> - 0.1.6-1
- initial SCM import (RHBZ #1244797)

* Mon Nov 09 2015 Christian Dersch <lupinix@fedoraproject.org> - 0.1.6-0.5
- more spec fixes for review
- added license breakdown
- adjusted requirements

* Sun Nov 08 2015 Christian Dersch <lupinix@fedoraproject.org> - 0.1.6-0.4
- spec adjustments for review

* Sat Sep 26 2015 Christian Dersch <lupinix@fedoraproject.org> - 0.1.6-0.3
- doc subpackage no longer noarch due to build failure

* Sat Sep 26 2015 Christian Dersch <lupinix@fedoraproject.org> - 0.1.6-0.2
- Small spec fixes

* Tue Sep 22 2015 Christian Dersch <lupinix@fedoraproject.org> - 0.1.6-0.1
- initial spec
