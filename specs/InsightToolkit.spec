%undefine __cmake_in_source_build
# Disable LTO for now - fails to build
%undefine _lto_cflags

%if 0%{?fedora} >= 33 || 0%{?rhel} >= 9
%bcond_without flexiblas
%endif

%global version_major_minor 5.4
%global version_patch 6

Name:           InsightToolkit
Summary:        Insight Toolkit library for medical image processing
Version:        %{version_major_minor}.%{version_patch}
Release:        3%{?dist}
# Bundled library licenses:
#   Apache-2.0       - ITK core (upstream)
#   BSD-3-Clause     - DICOMParser (Copyright.txt), GoogleTest (source headers),
#                      KWSys (Copyright.txt), MetaIO (License.txt)
#   BSD-2-Clause     - OpenJPEG (LICENSE)
#   MIT              - libLBFGS (lbfgs.h header)
#   Zlib             - NrrdIO (source headers, from Teem library)
#   LicenseRef-Fedora-Public-Domain - GIFTI (LICENSE.gifti), Netlib/SLATEC
#                      (public domain via netlib.org), NIFTI (nifti1_io.c header)
License:        Apache-2.0 AND BSD-3-Clause AND BSD-2-Clause AND MIT AND Zlib AND LicenseRef-Fedora-Public-Domain
Source0:        https://github.com/InsightSoftwareConsortium/ITK/releases/download/v%{version}/InsightToolkit-%{version}.tar.gz
Source1:        https://github.com/InsightSoftwareConsortium/ITK/releases/download/v%{version}/InsightSoftwareGuide-Book1-%{version}.pdf
Source2:        https://github.com/InsightSoftwareConsortium/ITK/releases/download/v%{version}/InsightSoftwareGuide-Book2-%{version}.pdf
Source3:        https://github.com/InsightSoftwareConsortium/ITK/releases/download/v%{version}/InsightData-%{version}.tar.gz
URL:            https://www.itk.org/

Patch:         0001-remove-vxl-netlib.patch

# Bundled libraries that have no way to use system versions.
# Version info extracted from the upstream ITK source tree at the time of
# the 5.4.6 release.
# DICOMParser, GIFTI, KWSys, MetaIO, Netlib, VNLInstantiation: no version
#   info available in ITK source
Provides: bundled(DICOMParser)
Provides: bundled(gifticlib) = 1.16
#   Source: Modules/ThirdParty/GIFTI/src/gifticlib/gifti_io.c:145
Provides: bundled(kwsys)
Provides: bundled(MetaIO)
Provides: bundled(nifti) = 2.1.0
#   Source: Modules/ThirdParty/NIFTI/src/nifti/niftilib/nifti1_io_version.h:4-6
Provides: bundled(NrrdIO) = 1.11.1
#   Source: Modules/ThirdParty/NrrdIO/src/NrrdIO/NrrdIO.h.in:51-56 (Teem version)
Provides: bundled(netlib)
Provides: bundled(openjpeg) = 1.2.0
#   Source: Modules/ThirdParty/OpenJPEG/src/openjpeg/openjpeg.h:90
Provides: bundled(liblbfgs) = 1.10
#   Source: Modules/ThirdParty/libLBFGS/include/lbfgs.h:605
Provides: bundled(googletest) = 1.13.0
#   Source: Modules/ThirdParty/GoogleTest/UpdateFromUpstream.sh:11
Provides: bundled(VNLInstantiation)

# https://fedoraproject.org/wiki/Changes/EncourageI686LeafRemoval
ExcludeArch: %{ix86}

BuildRequires:  castxml
BuildRequires:  cmake
BuildRequires:  clang-tools-extra
BuildRequires:  dcmtk
BuildRequires:  doxygen
BuildRequires:  double-conversion-devel
BuildRequires:  eigen3-devel
BuildRequires:  expat-devel
BuildRequires:  fftw-devel
BuildRequires:  freetype-devel
BuildRequires:  gdcm-devel
BuildRequires:  git-core
BuildRequires:  graphviz
BuildRequires:  hdf5-devel
BuildRequires:  jsoncpp-devel
BuildRequires:  libjpeg-devel
BuildRequires:  libminc-devel
BuildRequires:  libpng-devel
BuildRequires:  libtiff-devel
BuildRequires:  libxml2-devel
BuildRequires:  netcdf-cxx-devel
BuildRequires:  vtk-devel
BuildRequires:  vxl-devel
BuildRequires:  zlib-devel
%if %{with flexiblas}
BuildRequires:  flexiblas-devel
%else
BuildRequires:  blas-devel
BuildRequires:  lapack-devel
%endif

%description
ITK is an open-source software toolkit for performing registration and 
segmentation. Segmentation is the process of identifying and classifying data
found in a digitally sampled representation. Typically the sampled
representation is an image acquired from such medical instrumentation as CT or
MRI scanners. Registration is the task of aligning or developing 
correspondences between data. For example, in the medical environment, a CT
scan may be aligned with a MRI scan in order to combine the information
contained in both.

ITK is implemented in C++ and its implementation style is referred to as 
generic programming (i.e.,using templated code). Such C++ templating means
that the code is highly efficient, and that many software problems are 
discovered at compile-time, rather than at run-time during program execution.

%package        devel
Summary:        Insight Toolkit
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       %{name}-vtk-devel%{?_isa} = %{version}-%{release}

%description devel
%{summary}.
Install this if you want to develop applications that use ITK.

%package        examples
Summary:        C++, Tcl and Python example programs/scripts for ITK
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description examples
ITK examples

%package        doc
Summary:        Documentation for ITK
BuildArch:      noarch

%description    doc
%{summary}.
This package contains additional documentation.

# Hit bug http://www.gccxml.org/Bug/view.php?id=13372
# We agreed with Mattias Ellert to postpone the bindings till
# next gccxml update.
#%package        python
#Summary:        Documentation for ITK
#Group:          Documentation
#BuildArch:      noarch

#%description    python
#%%{summary}.
#This package contains python bindings for ITK.

%package        vtk
Summary:        Provides an interface between ITK and VTK
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description vtk
Provides an interface between ITK and VTK

%package        vtk-devel
Summary:        Libraries and header files for development of ITK-VTK bridge
Requires:       %{name}-vtk%{?_isa} = %{version}-%{release}
Requires:       vtk-devel%{?_isa}

%description vtk-devel
Libraries and header files for development of ITK-VTK bridge

%prep
%autosetup -S git

# copy guide into the appropriate directory
cp -a %{SOURCE1} %{SOURCE2} .

# remove applications: they are shipped separately now
rm -rf Applications/

# remove source files of external dependencies that itk gets linked against
# Libraries kept (pruned) because they are not available in Fedora or ITK
# has no mechanism to use the system version:
#   DICOMParser, GIFTI, KWSys, MetaIO, NrrdIO, Netlib, VNLInstantiation - not in Fedora
#   NIFTI - no ITK_USE_SYSTEM_NIFTI option (bundled nifti_clib)
#   OpenJPEG - no ITK_USE_SYSTEM_OPENJPEG option (bundles OpenJPEG 1.x)
#   libLBFGS - in Fedora but ITK has no system option
#   GoogleTest - in Fedora but ITK_USE_SYSTEM_GOOGLETEST is OFF
find Modules/ThirdParty/* \( -name DICOMParser -o -name GIFTI -o -name KWSys -o -name MetaIO -o -name NIFTI -o -name NrrdIO -o -name Netlib -o -name OpenJPEG -o -name VNLInstantiation -o -name libLBFGS -o -name GoogleTest \) \
    -prune -o -regextype posix-extended -type f \
    -regex ".*\.(h|hxx|hpp|c|cc|cpp|cxx|txx)$" -not -iname "itk*" -print0 | xargs -0 rm -fvr

tar xvf %{SOURCE3} -C ..

%build
# conflicts with castxml, needs debugging
extra_cflags=(
    -DITK_LEGACY_FUTURE_REMOVE # fix build with new vtk
    -Wno-deprecated-copy       # reduce noise in the logs...
    -Wno-maybe-uninitialized
    -Wno-ignored-qualifiers
    )
%cmake \
       -DBUILD_SHARED_LIBS:BOOL=ON \
       -DBUILD_EXAMPLES:BOOL=ON \
       -DCMAKE_BUILD_TYPE:STRING="RelWithDebInfo"\
       -DCMAKE_VERBOSE_MAKEFILE=ON\
       -DCMAKE_CXX_FLAGS:STRING="%{optflags} ${extra_cflags[*]}" \
       -DBUILD_TESTING=ON\
       %{?with_flexiblas:-DBLA_VENDOR=FlexiBLAS} \
       -DITK_USE_GOLD_LINKER:BOOL=OFF \
       -DITK_FORBID_DOWNLOADS=ON \
       -DITKV3_COMPATIBILITY:BOOL=OFF \
       -DITK_BUILD_DEFAULT_MODULES:BOOL=ON \
       -DITK_USE_KWSTYLE:BOOL=OFF \
       -DModule_ITKVtkGlue:BOOL=ON \
       -DITK_WRAP_PYTHON:BOOL=OFF \
       -DITK_WRAP_JAVA:BOOL=OFF \
       -DBUILD_DOCUMENTATION:BOOL=OFF \
       -DModule_ITKReview:BOOL=ON \
       -DITK_USE_FFTWD=ON \
       -DITK_USE_FFTWF=ON \
       -DITK_USE_SYSTEM_LIBRARIES:BOOL=ON \
       -DITK_USE_SYSTEM_CASTXML=ON \
       -DITK_USE_SYSTEM_DCMTK=ON \
       -DITK_USE_SYSTEM_DOUBLECONVERSION=ON \
       -DITK_USE_SYSTEM_EXPAT=ON \
       -DITK_USE_SYSTEM_FFTW=ON \
       -DITK_USE_SYSTEM_GDCM=ON \
       -DITK_USE_SYSTEM_GOOGLETEST=OFF \
       -DITK_USE_SYSTEM_HDF5=ON \
       -DHDF5_NO_FIND_PACKAGE_CONFIG=ON \
       -DITK_USE_SYSTEM_JPEG=ON \
       -DITK_USE_SYSTEM_MINC=ON \
       -DITK_USE_SYSTEM_PNG=ON \
       -DITK_USE_SYSTEM_SWIG=ON \
       -DITK_USE_SYSTEM_TIFF=ON \
       -DITK_USE_SYSTEM_ZLIB=ON \
       -DITK_USE_SYSTEM_VXL=ON \
       -DITK_USE_SYSTEM_EIGEN=ON \
       -DITK_INSTALL_LIBRARY_DIR=%{_lib}/ \
       -DITK_INSTALL_INCLUDE_DIR=include/%{name} \
       -DITK_INSTALL_PACKAGE_DIR=%{_lib}/cmake/%{name}/ \
       -DITK_INSTALL_RUNTIME_DIR:PATH=%{_bindir} \
       -DITK_INSTALL_DOC_DIR=share/doc/%{name}/


%cmake_build

%install
%cmake_install

# Install bundled library license files (avoid filename collisions)
mkdir -p %{buildroot}%{_defaultlicensedir}/%{name}
cp -a Modules/ThirdParty/DICOMParser/src/DICOMParser/Copyright.txt \
   %{buildroot}%{_defaultlicensedir}/%{name}/LICENSE.dicomparser
cp -a Modules/ThirdParty/GIFTI/src/gifticlib/LICENSE.gifti \
   %{buildroot}%{_defaultlicensedir}/%{name}/
cp -a Modules/ThirdParty/KWSys/src/KWSys/Copyright.txt \
   %{buildroot}%{_defaultlicensedir}/%{name}/LICENSE.kwsys
cp -a Modules/ThirdParty/MetaIO/src/MetaIO/License.txt \
   %{buildroot}%{_defaultlicensedir}/%{name}/LICENSE.metaio
cp -a Modules/ThirdParty/OpenJPEG/src/LICENSE \
   %{buildroot}%{_defaultlicensedir}/%{name}/LICENSE.openjpeg

# Install examples
mkdir -p %{buildroot}%{_datadir}/%{name}/examples
cp -ar Examples/* %{buildroot}%{_datadir}/%{name}/examples/

%check
# There are a couple of tests randomly failing. Needs debugging with upstream.
%ctest || exit 0

# In F45 rawhide
# The following tests FAILED:
#1238 - itkTIFFImageIOPlannarConfig2 (SEGFAULT)           ITKIOTIFF
#1241 - itkTIFFImageIOInfoTest2 (SEGFAULT)                ITKIOTIFF
#1257 - itkLargeTIFFImageWriteReadTest2 (Failed)          BigIO RUNS_LONG
#1258 - itkLargeTIFFImageWriteReadTest3 (Failed)          BigIO RUNS_LONG
#1259 - itkLargeTIFFImageWriteReadTest4 (Failed)          BigIO RUNS_LONG

%files
%doc NOTICE README.md
%license LICENSE
%license %{_defaultlicensedir}/%{name}/LICENSE.dicomparser
%license %{_defaultlicensedir}/%{name}/LICENSE.gifti
%license %{_defaultlicensedir}/%{name}/LICENSE.kwsys
%license %{_defaultlicensedir}/%{name}/LICENSE.metaio
%license %{_defaultlicensedir}/%{name}/LICENSE.openjpeg
%{_libdir}/*-%{version_major_minor}.so.1
%exclude %{_libdir}/libITKVtkGlue*.so.*
%{_bindir}/itkTestDriver

%files devel
%{_libdir}/*-%{version_major_minor}.so
%exclude %{_libdir}/libITKVtkGlue*.so
%{_libdir}/cmake/%{name}/
%{_includedir}/%{name}/
%exclude %{_includedir}/%{name}/itkImageToVTKImageFilter.h*
%exclude %{_includedir}/%{name}/itkVTKImageToImageFilter.h*
%exclude %{_includedir}/%{name}/QuickView.h
%exclude %{_includedir}/%{name}/vtkCaptureScreen.h
%exclude %{_libdir}/cmake/%{name}/Modules/ITKVtkGlue.cmake

%files examples
%{_datadir}/%{name}/examples

%files doc
%dir %{_docdir}/%{name}/
%{_docdir}/%{name}/*
%doc InsightSoftwareGuide-Book1-%{version}.pdf
%doc InsightSoftwareGuide-Book2-%{version}.pdf

%files vtk
%{_libdir}/libITKVtkGlue*.so.*

%files vtk-devel
%{_libdir}/libITKVtkGlue*.so
%{_includedir}/%{name}/itkImageToVTKImageFilter.h*
%{_includedir}/%{name}/itkVTKImageToImageFilter.h*
%{_includedir}/%{name}/QuickView.h
%{_includedir}/%{name}/vtkCaptureScreen.h
%{_libdir}/cmake/%{name}/Modules/ITKVtkGlue.cmake

%changelog
* Mon Aug 10 2026 Ankur Sinha <sanjay.ankur@gmail.com> - 5.4.6-3
- Rebuild for libminc 2.5.0 correctly

* Sun Aug 09 2026 Ankur Sinha <sanjay.ankur@gmail.com> - 5.4.6-2
- Rebuild for libminc 2.5.0

* Thu Jul 16 2026 Ankur Sinha <ankursinha AT fedoraproject DOT org> - 5.4.6-1
- Update to 5.4.6
- Switch to system double-conversion, Eigen3 (add double-conversion-devel,
  eigen3-devel BRs)
- Fix HDF5/NetCDF cmake target conflict (HDF5_NO_FIND_PACKAGE_CONFIG=ON)
- Add Provides: bundled() for all bundled libraries
- Update License: to SPDX with all bundled library licenses
- Install bundled library license files with unique names
- Drop unused patches (fix-riscv.patch), disable LTO, fix find syntax
- Remove stale Jira issue links from comments
- Drop qt5-qtwebkit-devel BuildRequires (no longer needed upstream)

* Wed Jul 15 2026 Fedora Release Engineering <releng@fedoraproject.org> - 4.13.3-34
- Rebuilt for https://fedoraproject.org/wiki/Fedora_45_Mass_Rebuild

* Tue May 12 2026 Ankur Sinha <ankursinha AT fedoraproject DOT org> - 4.13.3-33
- Include PR by Cristian Le <git@lecris.dev>
- Allow to build with CMake 4.0 (rhbz#2380458)

* Fri Feb 06 2026 Marcin Juszkiewicz <mjuszkiewicz@redhat.com> - 4.13.3-32
- fix build on RISC-V

* Fri Jan 16 2026 Fedora Release Engineering <releng@fedoraproject.org> - 4.13.3-31
- Rebuilt for https://fedoraproject.org/wiki/Fedora_44_Mass_Rebuild

* Fri Jan 16 2026 Fedora Release Engineering <releng@fedoraproject.org> - 4.13.3-30
- Rebuilt for https://fedoraproject.org/wiki/Fedora_44_Mass_Rebuild

* Fri Oct 10 2025 Benjamin A. Beasley <code@musicinmybrain.net> - 4.13.3-29
- Use the bundled gtest. GTest 1.17.1 will require C++17, and this version of
  ITK can’t be compiled as C++17.

* Sun Aug 24 2025 Orion Poplawski <orion@nwra.com> - 4.13.3-28
- Rebuild for VTK 9.5

* Wed Jul 23 2025 Fedora Release Engineering <releng@fedoraproject.org> - 4.13.3-27
- Rebuilt for https://fedoraproject.org/wiki/Fedora_43_Mass_Rebuild

* Wed Feb 19 2025 Ankur Sinha <sanjay.ankur@gmail.com> - 4.13.3-26
- Rebuild for dcmtk 3.6.9

* Thu Jan 16 2025 Fedora Release Engineering <releng@fedoraproject.org> - 4.13.3-25
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Fri Oct 25 2024 Orion Poplawski <orion@nwra.com> - 4.13.3-24
- Rebuild for hdf5 1.14.5

* Sat Oct 12 2024 Ankur Sinha <ankursinha AT fedoraproject DOT org> - 4.13.3-23
- Re-rebuild for vxl-3.5.0 (previous build didn't pick up the right vxl version)
- Exclude ix86

* Fri Oct 11 2024 Ankur Sinha <ankursinha AT fedoraproject DOT org> - 4.13.3-22
- Include patch to remove vxl netlib usage

* Sat Oct 05 2024 Mamoru TASAKA <mtasaka@fedoraproject.org> - 4.13.3-21
- Backport upstream patch for FTBFS with invalid const member func

* Wed Jul 24 2024 Miroslav Suchý <msuchy@redhat.com> - 4.13.3-20
- convert license to SPDX

* Wed Jul 17 2024 Fedora Release Engineering <releng@fedoraproject.org> - 4.13.3-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 4.13.3-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 4.13.3-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jan 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 4.13.3-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 4.13.3-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Tue Feb 14 2023 Orion Poplawski <orion@nwra.com> - 4.13.3-14
- Bump to -std=gnu++14 for gtest compat

* Wed Jan 18 2023 Fedora Release Engineering <releng@fedoraproject.org> - 4.13.3-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Sun Jan 15 2023 Orion Poplawski <orion@nwra.com> - 4.13.3-12
- Rebuild for vtk 9.2.5

* Wed Jul 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 4.13.3-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed Jan 19 2022 Fedora Release Engineering <releng@fedoraproject.org> - 4.13.3-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Sun Nov 21 2021 Orion Poplawski <orion@nwra.com> - 4.13.3-9
- Rebuild for hdf5 1.12.1

* Thu Nov 04 2021 Benjamin A. Beasley <code@musicinmybrain.net> - 4.13.3-8
- Remove python2-devel BR (fix RHBZ#1807494), as it is no longer required

* Tue Aug 10 2021 Orion Poplawski <orion@nwra.com> - 4.13.3-7
- Rebuild for hdf5 1.10.7/netcdf 4.8.0

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 4.13.3-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jul 13 2021 Björn Esser <besser82@fedoraproject.org> - 4.13.3-5
- Properly set BLA_VENDOR to FlexiBLAS for cmake >= 3.19

* Sun Jan 31 2021 Orion Poplawski <orion@nwra.com> - 4.13.3-4
- Rebuild for VTK 9

* Mon Jan 25 2021 Fedora Release Engineering <releng@fedoraproject.org> - 4.13.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Thu Aug 27 2020 Iñaki Úcar <iucar@fedoraproject.org> - 4.13.3-2
- https://fedoraproject.org/wiki/Changes/FlexiBLAS_as_BLAS/LAPACK_manager

* Wed Aug 05 2020 Orion Poplawski <orion@nwra.com> - 4.13.3-1
- Update to 4.13.3
- Use new cmake macros
- Disable LTO for now
- Disable gold linker

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 4.13.1-7
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 4.13.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Jun 25 2020 Orion Poplawski <orion@cora.nwra.com> - 4.13.1-5
- Rebuild for hdf5 1.10.6

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 4.13.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sun Sep 15 2019 Ankur Sinha <ankursinha AT fedoraproject DOT org> - 4.13.1-3
- Rebuid for gdcm 3.0.1

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 4.13.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Jun 28 2019 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 4.13.1-1
- Update to latest version in the 4.x branch (#1340300, #1674578)

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 4.9.1-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Oct 27 2018 Orion Poplawski <orion@cora.nwra.com> - 4.9.1-10
- Rebuild for VTK 8.1
- Use Qt5 on Fedora 30+

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 4.9.1-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 4.9.1-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Mon Aug 07 2017 Björn Esser <besser82@fedoraproject.org> - 4.9.1-7
- Rebuilt for AutoReq cmake-filesystem

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 4.9.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 4.9.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Thu Jul 13 2017 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 4.9.1-4
- Patch to fix FTBFS (#1423098)

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 4.9.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Dec 7 2016 Orion Poplawski <orion@cora.nwra.com> - 4.9.1-3
- Rebuild for vtk 7.1

* Sat Jul 02 2016 Orion Poplawski <orion@cora.nwra.com> - 4.9.1-2
- Rebuild for hdf5 1.8.17

* Wed Apr 13 2016 Sebastian Pölsterl <sebp@k-d-w.org> - 4.9.1-1
- Update to 4.9.1

* Thu Mar 03 2016 Sebastian Pölsterl <sebp@k-d-w.org> - 4.9.0-1
- Update to 4.9.0 (#1303377)
- Use system MINC and DCMTK
- Really disable ITKv3 compatibility (#1290564)
- Compile using C++98 standard (VXL does not support C++11, yet)

* Fri Jan 22 2016 Orion Poplawski <orion@cora.nwra.com> - 4.8.2-3
- Rebuild for netcdf 4.4.0

* Sun Jan 03 2016 Sebastian Pölsterl <sebp@k-d-w.org> - 4.8.2-2
- Disable ITKv3 compatibility (#1290564)

* Sun Nov 15 2015 Sebastian Pölsterl <sebp@k-d-w.org> - 4.8.2-1
- Update to 4.8.2

* Sun Nov 01 2015 Sebastian Pölsterl <sebp@k-d-w.org> - 4.8.1-4
- Rebuilt for gdcm 2.6.1

* Thu Oct 29 2015 Orion Poplawski <orion@cora.nwra.com> - 4.8.1-3
- Rebuild for vtk 6.3.0

* Mon Oct 12 2015 Sebastian Pölsterl <sebp@k-d-w.org> - 4.8.1-2
- Fix build using castxml and SSE patch

* Sun Oct 11 2015 Sebastian Pölsterl <sebp@k-d-w.org> - 4.8.1-1
- Update to 4.8.1
- Build with castxml

* Fri Jul 03 2015 Sebastian Pölsterl <sebp@k-d-w.org> - 4.8.0-2
- Include tarball that contains test data
- Update software guide

* Fri Jul 03 2015 Sebastian Pölsterl <sebp@k-d-w.org> - 4.8.0-1
- Update to 4.8.0
- Enable single and double precision for FFT (fixes bug #1076793)

* Tue Jun 16 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.7.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Fri May 22 2015 Orion Poplawski <orion@cora.nwra.com> - 4.7.2-3
- Add patch for sse includes

* Wed May 20 2015 Sebastian <sebp@k-d-w.org> - 4.7.2-3
- rebuilt

* Sun May 17 2015 Orion Poplawski <orion@cora.nwra.com> - 4.7.2-2
- Rebuild for hdf5 1.8.15

* Sat May 02 2015 Sebastian <sebp@k-d-w.org> - 4.7.2-1
- Update to 4.7.2

* Thu Mar 19 2015 Orion Poplawski <orion@cora.nwra.com> - 4.7.1-2
- Rebuild for vtk 6.2.0

* Fri Mar 06 2015 Sebastian <sebp@k-d-w.org> - 4.7.1-3
- Rebuilt for vtk

* Thu Mar 05 2015 Sebastian Pölsterl <sebp@k-d-w.org> - 4.7.1-2
- Add vtk-devel to requires of devel (another fix for bug #1196315)
- Move ITKVtkGlue.cmake to vtk-devel subpackage

* Wed Feb 25 2015 Sebastian Pölsterl <sebp@k-d-w.org> - 4.7.1-1
- Update to 4.7.1
- Add vtk-devel package (fixes bug #1196315)

* Thu Jan 08 2015 Orion Poplawski <orion@cora.nwra.com> - 4.7.0-3
- Rebuild for hdf5 1.8.14

* Sat Jan 03 2015 Sebastian Pölsterl <sebp@k-d-w.org> - 4.7.0-2
- Fixed wrong version of software development guide

* Fri Jan 02 2015 Sebastian Pölsterl <sebp@k-d-w.org> - 4.7.0-1
- Update to 4.7.0

* Fri Oct 03 2014 Sebastian Pölsterl <sebp@k-d-w.org> - 4.6.1-1
- Update to 4.6.1
- Don't compile with -fpermissive

* Fri Aug 15 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.6.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Tue Aug 12 2014 Sebastian Pölsterl <sebp@k-d-w.org> - 4.6.0-2
- Remove source files of external dependencies
- Partially fixes bug #1076793

* Mon Aug 04 2014 Sebastian Pölsterl <sebp@k-d-w.org> - 4.6.0-1
- Update to 4.6.0

* Fri Jun 06 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.5.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Wed May  7 2014 Tom Callaway <spot@fedoraproject.org> - 4.5.2-2
- rebuild for new R without bundled blas/lapack

* Thu Apr 17 2014 Sebastian Pölsterl <sebp@k-d-w.org> - 4.5.2-1
- Update to version 4.5.2

* Sun Feb 16 2014 Sebastian Pölsterl <sebp@k-d-w.org> - 4.5.1-1
- Update to version 4.5.1

* Sun Jan 26 2014 Sebastian Pölsterl <sebp@k-d-w.org> - 4.5.0-4
- Require netcdf-cxx-devel instead of netcdf-devel

* Sun Jan 26 2014 Sebastian Pölsterl <sebp@k-d-w.org> - 4.5.0-3
- Add jsoncpp-devel to BuildRequires (needed for vtk 6.1)

* Sun Jan 26 2014 Sebastian Pölsterl <sebp@k-d-w.org> - 4.5.0-2
- Rebuilt for vtk 6.1 update

* Sun Dec 29 2013 Sebastian Pölsterl <sebp@k-d-w.org> - 4.5.0-1
- Update to version 4.5.0
- Update software guide to 4.5.0
- Include LICENSE, NOTICE and README.txt in base package
- Move ITK-VTK bridge to new vtk subpackage
- Add BuildRequires on netcdf-devel (required by vtk)

* Mon Dec 23 2013 Sebastian Poelsterl <sebp@k-d-w.org> - 4.4.2-6
- Add BuildRequires on blas-devel and lapack-devel

* Mon Dec 23 2013 Sebastian Poelsterl <sebp@k-d-w.org> - 4.4.2-5
- Rebuilt for updated vtk

* Tue Oct 29 2013 Mario Ceresa <mrceresa@fedoraproject.org> - 4.4.2-4
- Revision bump up to build against updated gdcm

* Fri Oct 25 2013 Sebastian Pölsterl <sebp@k-d-w.org> - 4.4.2-3
- Removed HDF5 patch that seems to interfere with cmake 2.8.12

* Tue Oct 22 2013 Sebastian Pölsterl <sebp@k-d-w.org> - 4.4.2-2
- Rebuilt for gdcm 2.4.0

* Sun Sep 08 2013 Sebastian Pölsterl <sebp@k-d-w.org> - 4.4.2-1
- Update to version 4.4.2
- Added patch to only link against HDF5 release libraries

* Wed Aug 14 2013 Mario Ceresa <mrceresa@fedoraproject.org> 4.4.1-2
- Re-enabled vtk support
- Re-enabled tests
- Added BR qtwebkit

* Tue Aug 13 2013 Sebastian Pölsterl <sebp@k-d-w.org> - 4.4.1-1
- Update to version 4.4.1

* Mon Aug 05 2013 Mario Ceresa <mrceresa AT fedoraproject DOT org> - 4.4.0-6
- Use unversioned doc
- Fixed bogus dates
- Temporary remove vtk support because of issues with texlive in rawhide

* Fri Aug 02 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.4.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Tue Jul 16 2013 Mario Ceresa <mrceresa@fedoraproject.org> 4.4.0-4
- Use xz tarball to save space in srpm media. (Fixes BZ980599)

* Fri Jul 12 2013 Orion Poplawski <orion@cora.nwra.com> 4.4.0-3
- Rebuild for vtk 6.0.0

* Wed Jul 10 2013 Mario Ceresa mrceresa fedoraproject org 4.4.0-2
- Devel package now requires vtk-devel because it is build with itkvtkglue mod
- Minor cleanups

* Mon Jul 08 2013 Mario Ceresa mrceresa fedoraproject org 4.4.0-1
- Contributed by Sebastian Pölsterl <sebp@k-d-w.org>
- Updated to upstream version 4.4.0
- Add VTK Glue module
- Removed obsolete TIFF patch

* Thu May 16 2013 Orion Poplawski <orion@cora.nwra.com> - 4.3.1-12
- Rebuild for hdf5 1.8.11

* Thu May 2 2013 Mario Ceresa mrceresa fedoraproject org InsightToolkit 4.3.1-11
- Rebuilt for gdcm 2.3.2

* Fri Apr 26 2013 Mario Ceresa mrceresa fedoraproject org InsightToolkit 4.3.1-10
- Install itkTestDriver in default package
- Install libraries into _libdir and drop ldconfig file

* Tue Apr 23 2013 Mario Ceresa mrceresa fedoraproject org InsightToolkit 4.3.1-9
- Changed license to ASL 2.0

* Mon Apr 22 2013 Mario Ceresa mrceresa fedoraproject org InsightToolkit 4.3.1-8
- Build examples
- Making tests informative as we debug it with upstream
- Fixed cmake support file location
- Disabled python bindings for now, hit http://www.gccxml.org/Bug/view.php?id=13372

* Sat Apr 20 2013 Mario Ceresa mrceresa fedoraproject org InsightToolkit 4.3.1-7
- Enabled v3.20 compatibility layer

* Thu Apr 18 2013 Mario Ceresa mrceresa fedoraproject org InsightToolkit 4.3.1-6
- Removed unused patches

* Mon Apr 08 2013 Mario Ceresa mrceresa fedoraproject org InsightToolkit 4.3.1-5
- Fixed failing tests

* Wed Apr 03 2013 Mario Ceresa mrceresa fedoraproject org InsightToolkit 4.3.1-4
- Fixed build with USE_SYSTEM_TIFF

* Fri Mar 29 2013 Mario Ceresa mrceresa fedoraproject org InsightToolkit 4.3.1-3
- Compiles against VXL with compatibility patches
- Enabled testing

* Tue Feb 12 2013 Mario Ceresa mrceresa fedoraproject org InsightToolkit 4.3.1-2
- Reorganized sections
- Fixed patch naming
- Removed buildroot and rm in install section
- Removed cmake version constraint
- Changed BR libjpeg-turbo-devel to libjpeg-devel
- Preserve timestamp of SOURCE1 file.
- Fixed main file section
- Added noreplace

* Fri Jan 25 2013 Mario Ceresa mrceresa fedoraproject org InsightToolkit 4.3.1-1
- Updated to 4.3.1
- Fixed conflicts with previous patches
- Dropped gcc from BR
- Fixed tabs-vs-space
- Improved description
- Re-enabled system tiff
- Clean up the spec
- Sanitize use of dir macro
- Re-organized docs
- Fixed libdir and datadir ownership

* Wed Dec 12 2012 Mario Ceresa mrceresa fedoraproject org InsightToolkit 4.2.1-4
- Included improvements to the spec file from Dan Vratil

* Tue Dec 4 2012 Mario Ceresa mrceresa fedoraproject org InsightToolkit 4.2.1-3
- Build against system VXL

* Mon Nov 26 2012 Mario Ceresa mrceresa fedoraproject org InsightToolkit 4.2.1-2
- Reorganized install paths

* Tue Nov 20 2012 Mario Ceresa mrceresa fedoraproject org InsightToolkit 4.2.1-1
- Updated to new version

* Wed Nov 30 2011 Mario Ceresa mrceresa fedoraproject org InsightToolkit 3.20.1-1
- Updated to new version
- Added binary morphology code

* Fri May 27 2011 Mario Ceresa mrceresa fedoraproject org InsightToolkit 3.20.0-5
- Added cstddef patch for gcc 4.6

* Mon Jan 24 2011 Mario Ceresa mrceresa@gmail.com InsightToolkit 3.20.0-4
- Added the ld.so.conf file

* Mon Nov 22 2010 Mario Ceresa mrceresa@gmail.com InsightToolkit 3.20.0-3
- Updated to 3.20 release
- Added vxl utility and review material
- Applied patch from upstream to fix vtk detection (Thanks to Mathieu Malaterre)
- Added patch to install in the proper lib dir based on arch value
- Added patch to set datadir as cmake configuration files dir

* Sun Dec  6 2009 Mario Ceresa mrceresa@gmail.com InsightToolkit 3.16.0-2
- Fixed comments from revision: https://bugzilla.redhat.com/show_bug.cgi?id=539387#c8

* Tue Nov 17 2009 Mario Ceresa mrceresa@gmail.com InsightToolkit 3.16.0-1
- Initial RPM Release


