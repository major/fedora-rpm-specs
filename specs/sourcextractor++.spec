Summary:        A program that extracts a catalog of sources from astronomical images, and the successor of SExtractor
Name:           sourcextractor++
Version:        1.0.1
Release:        %autorelease
# Automatically converted from old format: LGPLv3+ - review is highly recommended.
License:        LGPL-3.0-or-later
URL:            https://github.com/astrorama/sourcextractorplusplus
Source0:        https://github.com/astrorama/sourcextractorplusplus/archive/%{version}/%{name}-%{version}.tar.gz
# This file is used to link the documentation to cppreference.com
# It is downloaded from:
# https://upload.cppreference.com/w/File:cppreference-doxygen-web.tag.xml
Source1:        cppreference-doxygen-web.tag.xml
Patch1:         0000-Use-Fedora-compilation-flags.patch
Patch2:         0001-Remove-benchmarks.patch
Patch3:         0002-Remove-TestImage.patch
Patch4:         0003-Reduce-precision-requirement-for-test.patch
Patch5:         0004-Sync-version-with-tag.patch

%global elements_version 6.3.3
%global alexandria_version 2.31.4

# https://fedoraproject.org/wiki/Changes/EncourageI686LeafRemoval 
ExcludeArch:    %{ix86}

BuildRequires: make
BuildRequires: CCfits-devel
BuildRequires: boost-devel >= 1.53
BuildRequires: cfitsio-devel
BuildRequires: cppunit-devel
BuildRequires: fftw-devel >= 3
BuildRequires: levmar-devel >= 2.5
BuildRequires: log4cpp-devel
BuildRequires: ncurses-devel
BuildRequires: wcslib-devel
%if 0%{?fedora} >= 30
BuildRequires: gsl-devel >= 2.2.1
%endif
BuildRequires: elements-devel = %{elements_version}
BuildRequires: elements-alexandria-devel = %{alexandria_version} 
# Required for the generation of the documentation
BuildRequires: elements-doc = %{elements_version}
BuildRequires: elements-alexandria-doc = %{alexandria_version}
BuildRequires: doxygen
BuildRequires: graphviz
%ifnarch s390x %{arm}
BuildRequires: onnxruntime-devel
%endif
BuildRequires: texlive-latex
%if 0%{?fedora} >= 30
BuildRequires: texlive-newunicodechar
%endif
BuildRequires: texlive-dvips

BuildRequires: gcc-c++ > 4.7
BuildRequires: cmake >= 2.8.5
%if 0%{?fedora} >= 30
BuildRequires: python3
BuildRequires: python3-devel
BuildRequires: python3-pytest
BuildRequires: boost-python3-devel >= 1.53
%else
BuildRequires: python2
BuildRequires: python2-devel
BuildRequires: python2-pytest
BuildRequires: boost-python-devel >= 1.53
%endif

%if 0%{?rhel} && 0%{?rhel} <= 7
Requires: cmake%{?_isa}
%else
Requires: cmake-filesystem%{?_isa}
%endif
Requires:      python3-astropy%{?_isa}

%global cmakedir %{_libdir}/cmake/ElementsProject

%if 0%{?fedora} >= 30
%global python_sitearch %{python3_sitearch}
%global python_sitelib %{python3_sitelib}
%else
%global python_sitearch %{python2_sitearch}
%global python_sitelib %{python2_sitelib}
%endif

%description
%{name} is a program that extracts a catalog of sources from
astronomical images. It is the successor to the original SExtractor
package.

%package devel
Summary: The development part of the %{name} package
Requires: %{name}%{?_isa} = %{version}-%{release}
Requires: elements-devel%{?_isa} = %{elements_version}
Requires: elements-alexandria%{?_isa} = %{alexandria_version}

%description devel
The development part of the %{name} package.

%package doc
Summary: Documentation for package %{name}
# Automatically converted from old format: LGPLv3+ and CC-BY-SA - review is highly recommended.
License: LGPL-3.0-or-later AND LicenseRef-Callaway-CC-BY-SA
BuildArch: noarch
Requires: elements-doc = %{elements_version}
Requires: elements-alexandria-doc = %{alexandria_version}

%description doc
Documentation for package %{name}

%prep
%autosetup -n SourceXtractorPlusPlus-%{version} -p1

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
    -DCMAKE_LIB_INSTALL_SUFFIX=%{_lib} -DUSE_VERSIONED_LIBRARIES=ON -DPYTHON_DYNLIB_INSTALL_SUFFIX="%{python_sitearch}"\
    ${EXTRA_CMAKE_FLAGS}
# Copy cppreference-doxygen-web.tag.xml into the build directory
mkdir -p "%{_vpath_builddir}/doc/doxygen"
cp "%{SOURCE1}" "%{_vpath_builddir}/doc/doxygen"
# Disable FULL_PATH_NAMES on Doxygen, to avoid problems when building in different architectures
sed -i "s?^\\(EXCLUDE = .*\\)?\\1 $(pwd)/%{_vpath_builddir}?g" "%{_vpath_builddir}/doc/doxygen/Doxyfile"
# Disable interactive svg, so _org.svg files are not generated
# For some reason, some of these files go missing on s390x
sed -i "s?INTERACTIVE_SVG = YES?INTERACTIVE_SVG = NO?g" "%{_vpath_builddir}/doc/doxygen/Doxyfile"

%make_build -C "%{_vpath_builddir}"

%install
export VERBOSE=1
%make_install -C "%{_vpath_builddir}"
rm -fv "%{buildroot}/%{_libdir}/"*BoostTest.so*

# Because of limitations of Elements, ++ can not be used as part of the
# project name. For consistency, we rename some of the destination directories
# to sourcextractor++
mv %{buildroot}/%{_docdir}/SourceXtractorPlusPlus %{buildroot}/%{_docdir}/sourcextractor++

# Similarly, move the configuration file to /etc
mkdir -p %{buildroot}/%{_sysconfdir}
mv %{buildroot}/%{_datadir}/conf/sourcextractor++.conf %{buildroot}/%{_sysconfdir}/sourcextractor++.conf
rm -r %{buildroot}/%{_datadir}/conf/

%check
export ELEMENTS_AUX_PATH="%{_builddir}/SEFramework/auxdir/"
make test -C "%{_vpath_builddir}"
%{buildroot}/%{_bindir}/sourcextractor++ --help

%files
%license LICENSE
%{cmakedir}/SourceXtractorPlusPlusEnvironment.xml

%{_bindir}/sourcextractor++
%config(noreplace) %{_sysconfdir}/sourcextractor++.conf

%{_libdir}/libModelFitting.so.%{version}
%{_libdir}/libSEFramework.so.%{version}
%{_libdir}/libSEImplementation.so.%{version}
%{_libdir}/libSEMain.so.%{version}
%{_libdir}/libSEUtils.so.%{version}

%{python_sitearch}/SOURCEXTRACTORPLUSPLUS_VERSION.py*
%{python_sitearch}/SOURCEXTRACTORPLUSPLUS_INSTALL.py*
%{python_sitearch}/sourcextractor/
%{python_sitearch}/_SourceXtractorPy.so

%if 0%{?fedora} >= 30
%{python_sitearch}/__pycache__/SOURCEXTRACTORPLUSPLUS*.pyc
%endif

%files devel
%{_libdir}/libModelFitting.so
%{_libdir}/libSEFramework.so
%{_libdir}/libSEImplementation.so
%{_libdir}/libSEMain.so
%{_libdir}/libSEUtils.so

%{_includedir}/SOURCEXTRACTORPLUSPLUS_VERSION.h
%{_includedir}/SOURCEXTRACTORPLUSPLUS_INSTALL.h
%{_includedir}/ModelFitting/
%{_includedir}/SEFramework/
%{_includedir}/SEImplementation/
%{_includedir}/SEMain/
%{_includedir}/SEUtils/

%{cmakedir}/SourceXtractorPlusPlusBuildEnvironment.xml
%{cmakedir}/SourceXtractorPlusPlusExports.cmake
%{cmakedir}/SourceXtractorPlusPlusExports-relwithdebinfo.cmake
%{cmakedir}/SourceXtractorPlusPlusPlatformConfig.cmake
%{cmakedir}/SourceXtractorPlusPlusConfig.cmake
%{cmakedir}/SourceXtractorPlusPlusConfigVersion.cmake
%{cmakedir}/ModelFittingExport.cmake
%{cmakedir}/SEFrameworkExport.cmake
%{cmakedir}/SEImplementationExport.cmake
%{cmakedir}/SEMainExport.cmake
%{cmakedir}/SEUtilsExport.cmake

%files doc
%license LICENSE
%{_docdir}/sourcextractor++

%changelog
%autochangelog
