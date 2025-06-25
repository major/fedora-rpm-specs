Summary:        A C++/Python build framework
Name:           elements
Version:        6.3.4
Release:        %autorelease
License:        LGPL-3.0-or-later
Source0:        https://github.com/astrorama/Elements/archive/%{version}/%{name}-%{version}.tar.gz
# Elements use this file to link the documentation to cppreference.com
# It is downloaded from:
# https://upload.cppreference.com/w/File:cppreference-doxygen-web.tag.xml
Source1:        cppreference-doxygen-web.tag.xml
URL:            https://github.com/degauden/Elements.git
# Remove Example programs and scripts, otherwise they will be installed
Patch0:         0000-Remove-examples.patch
# Disable the compilation of PDF documentation
Patch2:         0001-Disable-PDF-documentation.patch
# distutils have been removed
Patch3:         0002-Do-not-rely-on-distutils.patch

BuildRequires: CCfits-devel
BuildRequires: boost-devel >= 1.53
BuildRequires: cfitsio-devel
BuildRequires: cppunit-devel
BuildRequires: fftw-devel
BuildRequires: gmock-devel
BuildRequires: gtest-devel
BuildRequires: log4cpp-devel >= 1.1
BuildRequires: swig
BuildRequires: wcslib-devel
# Required for the generation of the documentation
BuildRequires: doxygen
BuildRequires: graphviz

BuildRequires: gcc-c++ > 4.7
BuildRequires: python3
BuildRequires: python3-pytest
BuildRequires: python3-devel
BuildRequires: python3-sphinx
BuildRequires: cmake >= 2.8.5

Requires: cmake-filesystem%{?_isa}

%global cmakedir %{_libdir}/cmake/ElementsProject

%global makedir %{_datadir}/Elements/make
%global confdir %{_datadir}/conf
%global auxdir %{_datadir}/auxdir
%global docdir %{_docdir}/Elements

%description
Elements is a C++/Python build framework. It helps to organize
the software into modules which are gathered into projects.

%package devel
Summary: The development part of the %{name} package
Requires: %{name}%{?_isa} = %{version}-%{release}

%description devel
The development part of the %{name} package.


%package doc
Summary: Documentation for package %{name}
License: LGPLv3+ and CC-BY-SA
BuildArch: noarch

%description doc
Documentation for package %{name}

%prep
%autosetup -n Elements-%{version} -p1

%build
export VERBOSE=1
# Build
%cmake -DELEMENTS_BUILD_TESTS=ON -DINSTALL_TESTS=OFF -DSQUEEZED_INSTALL:BOOL=ON -DINSTALL_DOC:BOOL=ON \
    -DUSE_SPHINX=OFF --no-warn-unused-cli \
    -DPYTHON_EXPLICIT_VERSION=3 -DCMAKE_POLICY_DEFAULT_CMP0148=OLD \
    -DCMAKE_LIB_INSTALL_SUFFIX=%{_lib} -DUSE_VERSIONED_LIBRARIES=ON \
    -DUSE_ENV_FLAGS=ON
# Copy cppreference-doxygen-web.tag.xml into the build directory
mkdir -p "%{_vpath_builddir}/doc/doxygen"
cp -v "%{SOURCE1}" "%{_vpath_builddir}/doc/doxygen"

%cmake_build

%install
export VERBOSE=1
%cmake_install
rm -rfv "%{buildroot}/%{confdir}/ElementsServices/testdata"
rm -fv "%{buildroot}/%{_bindir}/"*_test
rm -fv "%{buildroot}/%{_includedir}/"*BoostTest_export.h
rm -fv "%{buildroot}/%{_libdir}/"*BoostTest.so*

%check
export ELEMENTS_CONF_PATH="%{_builddir}/ElementsKernel/auxdir/"
%ctest

%files
%{confdir}/
%dir %{cmakedir}
%{cmakedir}/ElementsEnvironment.xml

%{_libdir}/libElementsKernel.so.%{version}
%{_libdir}/libElementsServices.so.%{version}

%{_bindir}/CreateElementsProject
%{_bindir}/AddElementsModule
%{_bindir}/AddCppClass
%{_bindir}/AddCppProgram
%{_bindir}/AddPythonProgram
%{_bindir}/AddScript
%{_bindir}/AddPythonModule
%{_bindir}/RemoveCppClass
%{_bindir}/RemoveCppProgram
%{_bindir}/RemovePythonProgram
%{_bindir}/RemovePythonModule
%{_bindir}/ElementsNameCheck
%{_bindir}/GetElementsFiles

%{python3_sitearch}/ELEMENTS_VERSION.py
%{python3_sitearch}/ELEMENTS_INSTALL.py
%{python3_sitearch}/__pycache__/ELEMENTS_*.pyc

%{python3_sitearch}/ElementsKernel/
%{python3_sitearch}/ElementsServices/

%dir %{auxdir}
%{auxdir}/ElementsKernel/

%files devel
%{_libdir}/libElementsKernel.so
%{_libdir}/libElementsServices.so
%{_includedir}/ELEMENTS_VERSION.h
%{_includedir}/ELEMENTS_INSTALL.h
%{_includedir}/ElementsKernel_export.h
%{_includedir}/ElementsServices_export.h
%{_includedir}/ElementsKernel/
%{_includedir}/ElementsServices/

%{cmakedir}/ElementsBuildEnvironment.xml
%{cmakedir}/ElementsBuildFlags.cmake
%{cmakedir}/ElementsCheck.cmake
%{cmakedir}/ElementsConfig.cmake
%{cmakedir}/ElementsConfigVersion.cmake
%{cmakedir}/ElementsCoverage.cmake
%{cmakedir}/ElementsDefaults.cmake
%{cmakedir}/ElementsDocumentation.cmake
%{cmakedir}/ElementsExports-relwithdebinfo.cmake
%{cmakedir}/ElementsExports.cmake
%{cmakedir}/ElementsGenerateBindings.cmake
%{cmakedir}/ElementsInfo.cmake
%{cmakedir}/ElementsKernelExport.cmake
%{cmakedir}/ElementsLocations.cmake
%{cmakedir}/ElementsPlatformConfig.cmake
%{cmakedir}/ElementsProjectConfig.cmake
%{cmakedir}/ElementsServicesExport.cmake
%{cmakedir}/ElementsToolChain.cmake
%{cmakedir}/ElementsToolChainMacros.cmake
%{cmakedir}/ElementsUninstall.cmake
%{cmakedir}/ElementsUtils.cmake
%{cmakedir}/GetGitRevisionDescription.cmake
%{cmakedir}/HelloWorld.cmake
%{cmakedir}/SGSPlatform.cmake
%{cmakedir}/auxdir
%{cmakedir}/check
%{cmakedir}/doc
%{cmakedir}/modules
%{cmakedir}/scripts
%{cmakedir}/tests

%{makedir}

%files doc
%license LICENSE.md
%{docdir}

%changelog
%autochangelog
