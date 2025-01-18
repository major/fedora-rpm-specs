Summary:        A lightweight C++ utility library
Name:           elements-alexandria
Version:        2.31.2
Release:        6%{?dist}
# Automatically converted from old format: LGPLv3+ - review is highly recommended.
License:        LGPL-3.0-or-later
URL:            https://github.com/astrorama/Alexandria
Source0:        https://github.com/astrorama/Alexandria/archive/%{version}/%{name}-%{version}.tar.gz
# This file is used to link the documentation to cppreference.com
# It is downloaded from:
# https://upload.cppreference.com/w/File:cppreference-doxygen-web.tag.xml
Source1:        cppreference-doxygen-web.tag.xml
Patch0:         0000-Use-Elements-6.3.2.patch
Patch1:         0001-Clear-Python-error.patch

%global elements_version 6.3.2

BuildRequires: CCfits-devel
BuildRequires: boost-devel >= 1.53
BuildRequires: cfitsio-devel
BuildRequires: cppunit-devel
BuildRequires: elements-devel = %{elements_version}
BuildRequires: log4cpp-devel
# Required for the generation of the documentation
BuildRequires: elements-doc = %{elements_version}
BuildRequires: doxygen
BuildRequires: graphviz

BuildRequires: gcc-c++ > 4.7
BuildRequires: cmake >= 2.8.5
%if 0%{?fedora} >= 30
BuildRequires: python3
BuildRequires: python3-pytest
BuildRequires: python3-devel
%else
BuildRequires: python2
BuildRequires: python2-pytest
BuildRequires: python2-devel
%endif
BuildRequires: make

%if 0%{?rhel} && 0%{?rhel} <= 7
Requires: cmake%{?_isa}
%else
Requires: cmake-filesystem%{?_isa}
%endif

%global cmakedir %{_libdir}/cmake/ElementsProject

%global makedir %{_datadir}/Elements/make
%global confdir %{_datadir}/Elements
%global auxdir %{_datadir}/auxdir
%global docdir %{_docdir}/Alexandria

%if 0%{?fedora} >= 30
%global python_sitearch %{python3_sitearch}
%else
%global python_sitearch %{python2_sitearch}
%endif

%description
A lightweight C++ utility library.

%package devel
Summary: The development part of the %{name} package
Requires: %{name}%{?_isa} = %{version}-%{release}
Requires: elements-devel%{?_isa} = %{elements_version}

%description devel
The development part of the %{name} package.

%package doc
Summary: Documentation for package %{name}
# Automatically converted from old format: LGPLv3+ and CC-BY-SA - review is highly recommended.
License: LGPL-3.0-or-later AND LicenseRef-Callaway-CC-BY-SA
BuildArch: noarch
Requires: elements-doc = %{elements_version}

%description doc
Documentation for package %{name}

%prep
%autosetup -n Alexandria-%{version} -p1

%build
export VERBOSE=1
EXTRA_CMAKE_FLAGS="-DUSE_ENV_FLAGS=ON"
%if 0%{?fedora} >= 30
EXTRA_CMAKE_FLAGS="${EXTRA_CMAKE_FLAGS} -DPYTHON_EXPLICIT_VERSION=3"
%else
EXTRA_CMAKE_FLAGS="${EXTRA_CMAKE_FLAGS} -DPYTHON_EXPLICIT_VERSION=2"
%endif
# Build
%cmake -B "%{_vpath_builddir}" -DELEMENTS_BUILD_TESTS=ON -DELEMENTS_INSTALL_TESTS=OFF -DSQUEEZED_INSTALL:BOOL=ON -DINSTALL_DOC:BOOL=ON \
    -DUSE_SPHINX=OFF --no-warn-unused-cli \
    -DCMAKE_LIB_INSTALL_SUFFIX=%{_lib} -DUSE_VERSIONED_LIBRARIES=ON ${EXTRA_CMAKE_FLAGS}
# Copy cppreference-doxygen-web.tag.xml into the build directory
mkdir -p "%{_vpath_builddir}/doc/doxygen"
cp -v "%{SOURCE1}" "%{_vpath_builddir}/doc/doxygen"

%make_build -C "%{_vpath_builddir}"

%install
export VERBOSE=1
%make_install -C "%{_vpath_builddir}"
rm -fv "%{buildroot}/%{_libdir}/"*BoostTest.so*

%check
make test -C "%{_vpath_builddir}"

%files
%license LICENSE
%{cmakedir}/AlexandriaEnvironment.xml

%{_bindir}/AlexandriaVersion

%{_libdir}/libAlexandriaKernel.so.%{version}
%{_libdir}/libConfiguration.so.%{version}
%{_libdir}/libFilePool.so.%{version}
%{_libdir}/libGridContainer.so.%{version}
%{_libdir}/libHistogram.so.%{version}
%{_libdir}/libKdTree.so.%{version}
%{_libdir}/libMathUtils.so.%{version}
%{_libdir}/libNdArray.so.%{version}
%{_libdir}/libPhysicsUtils.so.%{version}
%{_libdir}/libPyston.so.%{version}
%{_libdir}/libSOM.so.%{version}
%{_libdir}/libSourceCatalog.so.%{version}
%{_libdir}/libTable.so.%{version}
%{_libdir}/libXYDataset.so.%{version}

%{python_sitearch}/ALEXANDRIA_VERSION.py*
%{python_sitearch}/ALEXANDRIA_INSTALL.py*
%if 0%{?fedora} >= 30
%{python_sitearch}/__pycache__/ALEXANDRIA*.pyc
%endif

%files devel
%{_libdir}/libAlexandriaKernel.so
%{_libdir}/libConfiguration.so
%{_libdir}/libFilePool.so
%{_libdir}/libGridContainer.so
%{_libdir}/libHistogram.so
%{_libdir}/libKdTree.so
%{_libdir}/libMathUtils.so
%{_libdir}/libNdArray.so
%{_libdir}/libPhysicsUtils.so
%{_libdir}/libPyston.so
%{_libdir}/libSOM.so
%{_libdir}/libSourceCatalog.so
%{_libdir}/libTable.so
%{_libdir}/libXYDataset.so

%{_includedir}/ALEXANDRIA_VERSION.h
%{_includedir}/ALEXANDRIA_INSTALL.h
%{_includedir}/AlexandriaKernel/
%{_includedir}/Configuration/
%{_includedir}/GridContainer/
%{_includedir}/FilePool/
%{_includedir}/Histogram/
%{_includedir}/KdTree/
%{_includedir}/MathUtils/
%{_includedir}/NdArray/
%{_includedir}/PhysicsUtils/
%{_includedir}/Pyston/
%{_includedir}/SOM/
%{_includedir}/SourceCatalog/
%{_includedir}/Table/
%{_includedir}/XYDataset/

%{cmakedir}/AlexandriaBuildEnvironment.xml
%{cmakedir}/AlexandriaConfig.cmake
%{cmakedir}/AlexandriaConfigVersion.cmake
%{cmakedir}/AlexandriaExports-relwithdebinfo.cmake
%{cmakedir}/AlexandriaExports.cmake
%{cmakedir}/AlexandriaKernelExport.cmake
%{cmakedir}/AlexandriaPlatformConfig.cmake
%{cmakedir}/ConfigurationExport.cmake
%{cmakedir}/FilePoolExport.cmake
%{cmakedir}/GridContainerExport.cmake
%{cmakedir}/HistogramExport.cmake
%{cmakedir}/KdTreeExport.cmake
%{cmakedir}/MathUtilsExport.cmake
%{cmakedir}/NdArrayExport.cmake
%{cmakedir}/PhysicsUtilsExport.cmake
%{cmakedir}/PystonExport.cmake
%{cmakedir}/SOMExport.cmake
%{cmakedir}/SourceCatalogExport.cmake
%{cmakedir}/TableExport.cmake
%{cmakedir}/XYDatasetExport.cmake

%files doc
%license LICENSE
%{docdir}

%changelog
* Thu Jan 16 2025 Fedora Release Engineering <releng@fedoraproject.org> - 2.31.2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Fri Nov 01 2024 Alejandro Alvarez Ayllon <a.alvarezayllon@gmail.com> - 2.31.2-5
- Rebuild for elements 6.3.2

* Wed Aug 28 2024 Miroslav Suchý <msuchy@redhat.com> - 2.31.2-4
- convert license to SPDX

* Wed Jul 17 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.31.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Sat Jun 08 2024 Python Maint <python-maint@redhat.com> - 2.31.2-2
- Rebuilt for Python 3.13

* Wed May 29 2024 Alejandro Alvarez Ayllon <a.alvarezayllon@gmail.com> - 2.31.2-1
- Release 2.31.2

* Wed Mar 20 2024 Alejandro Alvarez Ayllon <a.alvarezayllon@gmail.com> - 2.31.0-6
- Rebuild for Fedora 41

* Thu Jan 25 2024 Alejandro Alvarez Ayllon <a.alvarezayllon@gmail.com> - 2.31.0-5
- Fix tests for python 3.13

* Wed Jan 24 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.31.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.31.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jan 18 2024 Jonathan Wakely <jwakely@redhat.com> - 2.31.0-2
- Rebuilt for Boost 1.83

* Thu Nov 09 2023 Alejandro Alvarez Ayllon <a.alvarezayllon@gmail.com> - 2.31.0-1
- Release 2.31.0

* Thu Aug 17 2023 Alejandro Alvarez Ayllon <a.alvarezayllon@gmail.com> - 2.30.1-3
- Rebuilt for Fedora 40

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.30.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Mon Jul 10 2023 Alejandro Alvarez Ayllon <a.alvarezayllon@gmail.com> - 2.30.1-1
- Release 2.30.1

* Fri Jul 07 2023 Python Maint <python-maint@redhat.com> - 2.28.2-2
- Rebuilt for Python 3.12

* Tue Mar 14 2023 Alejandro Alvarez Ayllon <a.alvarezayllon@gmail.com> - 2.28.2-1
- Alexandria 2.28.2

* Mon Feb 20 2023 Jonathan Wakely <jwakely@redhat.com> - 2.27.0-5
- Rebuilt for Boost 1.81

* Tue Jan 31 2023 Alejandro Alvarez Ayllon <a.alvarezayllon@gmail.com> - 2.27.0-4
- Rebuild for gcc 13

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.27.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Dec 29 2022 Maxwell G <gotmax@e.email> - 2.27.0-2
- Rebuild for cfitsio 4.2

* Tue Oct 18 2022 Alejandro Alvarez Ayllon <aalvarez@fedoraproject.org> - 2.27.0-1
- Alexandria 2.27.0

* Tue Aug 23 2022 Mamoru TASAKA <mtasaka@fedoraproject.org> - 2.25.0-5
- Rebuild for gcc / f38 (needed to build sourcextractor++)

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.25.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon Jun 13 2022 Python Maint <python-maint@redhat.com> - 2.25.0-3
- Rebuilt for Python 3.11

* Wed May 04 2022 Thomas Rodgers <trodgers@redhat.com> - 2.25.0-2
- Rebuilt for Boost 1.78

* Wed Apr 20 2022 Alejandro Alvarez Ayllon <aalvarez@fedoraproject.org> - 2.25.0-1
- Alexandria 2.25.0

* Wed Jan 26 2022 Alejandro Alvarez Ayllon <aalvarez@fedoraproject.org> - 2.22.0-3
- Fix build on f36

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.22.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Dec 16 2021 Alejandro Alvarez Ayllon <aalvarez@fedoraproject.org> - 2.22.0-1
- Alexandria 2.22.0

* Wed Aug 11 2021 Alejandro Alvarez Ayllon <aalvarez@fedoraproject.org> - 2.19-6
- Rebuild after f35 branching

* Mon Aug 09 2021 Alejandro Alvarez Ayllon <aalvarez@fedoraproject.org> - 2.19-5
- Rebuild for gcc 11.2

* Sat Aug 07 2021 Jonathan Wakely <jwakely@redhat.com> - 2.19-4
- Rebuilt for Boost 1.76

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.19-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 2.19-2
- Rebuilt for Python 3.10

* Mon May 31 2021 Alejandro Alvarez Ayllon <aalvarez@fedoraproject.org> - 2.19-1
- Release 2.19

* Mon May 10 2021 Alejandro Alvarez Ayllon <aalvarez@fedoraproject.org> - 2.18-3
- Rebuild for gcc11.1

* Wed Apr 21 2021 Alejandro Alvarez Ayllon <aalvarez@fedoraproject.org> - 2.18-2
- Rebuild for Fedora 35

* Fri Feb 05 2021 Alejandro Alvarez Ayllon <aalvarez@fedoraproject.org> - 2.18-1
- Release 2.18

* Thu Feb 04 2021 Alejandro Alvarez Ayllon <a.alvarezayllon@gmail.com> - 2.16-8
- Rebuilt for cfitsio 3.490

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.16-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Jan 25 2021 Jonathan Wakely <jwakely@redhat.com> - 2.16-6
- Add patch for Boost 1.75.0

* Fri Jan 22 2021 Jonathan Wakely <jwakely@redhat.com> - 2.16-5
- Rebuilt for Boost 1.75

* Mon Dec 07 2020 Alejandro Alvarez Ayllon <alejandro.alvarezayllon@unige.ch> 2.16-4
- Rebuilt for Fedora 34

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.16-3
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.16-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Jul 17 2020 Alejandro Alvarez Ayllon <alejandro.alvarezayllon@unige.ch> 2.16-1
- New upstream release 2.16

* Thu May 28 2020 Jonathan Wakely <jwakely@redhat.com> - 2.14.1-7
- Rebuilt for Boost 1.73

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 2.14.1-6
- Rebuilt for Python 3.9

* Wed Feb 26 2020 Alejandro Alvarez Ayllon <a.alvarezayllon@gmail.com> - 2.14.1-5
- Rebuild for Fedora 33

* Mon Feb 03 2020 Alejandro Alvarez Ayllon <a.alvarezayllon@gmail.com> - 2.14.1-4
- Rebuild for elements 5.8-6

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.14.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Mon Jan 13 2020 Alejandro Alvarez Ayllon <alejandro.alvarezayllon@unige.ch> 2.14.1-2
- Fix conditional dependency on cmake-filesystem
- Add LICENSE file to the main package

* Fri Jan 10 2020 Alejandro Alvarez Ayllon <alejandro.alvarezayllon@unige.ch> 2.14.1-1
- Initial RPM
