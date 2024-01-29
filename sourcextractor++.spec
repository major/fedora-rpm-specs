Summary:        A program that extracts a catalog of sources from astronomical images, and the successor of SExtractor
Name:           sourcextractor++
Version:        0.21
Release:        3%{?dist}
License:        LGPLv3+
URL:            https://github.com/astrorama/sourcextractorplusplus
Source0:        https://github.com/astrorama/sourcextractorplusplus/archive/%{version}/%{name}-%{version}.tar.gz
# This file is used to link the documentation to cppreference.com
# It is downloaded from:
# https://upload.cppreference.com/w/File:cppreference-doxygen-web.tag.xml
Source1:        cppreference-doxygen-web.tag.xml
# These binaries are not intended for users, so we drop them from the build
Patch0:         sourcex_remove_benchmarks.patch
Patch1:         sourcex_remove_testimage.patch
# We do not want to override the compilation flags
Patch2:         sourcex_remove_custom_flags.patch
# The test has an excesive precision requirement
Patch3:         sourcex_precision_test.patch

%global elements_version 6.2.3
%global alexandria_version 2.31.0

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
License: LGPLv3+ and CC-BY-SA
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
* Sat Jan 27 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.21-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jan 18 2024 Jonathan Wakely <jwakely@redhat.com> - 0.21-2
- Rebuilt for Boost 1.83

* Wed Dec 27 2023 Alejandro Alvarez Ayllon <a.alvarezayllon@gmail.com> - 0.21-1
- Release 0.21

* Fri Nov 10 2023 Alejandro Alvarez Ayllon <a.alvarezayllon@gmail.com> - 0.19.2-6
- Rebuilt for Alexandria 2.31.0

* Thu Aug 17 2023 Alejandro Alvarez Ayllon <a.alvarezayllon@gmail.com> - 0.19.2-5
- Enable onnxruntime support

* Sat Jul 22 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.19.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Mon Jul 10 2023 Alejandro Alvarez Ayllon <a.alvarezayllon@gmail.com> - 0.19.2-3
- Rebuild SourceXtractor++

* Mon Jul 10 2023 Python Maint <python-maint@redhat.com> - 0.19.2-2
- Rebuilt for Python 3.12

* Tue Mar 14 2023 Alejandro Alvarez Ayllon <a.alvarezayllon@gmail.com> - 0.19.2-1
- SourceXtractor++ 0.19.2 

* Sat Feb 25 2023 Alejandro Alvarez Ayllon <a.alvarezayllon@gmail.com> - 0.19-6
- Fix build in Fedora 39

* Wed Feb 01 2023 Alejandro Alvarez Ayllon <a.alvarezayllon@gmail.com> - 0.19-5
- Rebuild for gcc 13

* Sat Jan 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.19-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Dec 29 2022 Maxwell G <gotmax@e.email> - 0.19-3
- Rebuild for cfitsio 4.2

* Mon Dec 12 2022 aalvarez - 0.19-2
- Requires python3-astropy

* Thu Oct 20 2022 Alejandro Alvarez Ayllon <aalvarez@fedoraproject.org> - 0.19-1
- SourceXtractor++ 0.19

* Tue Aug 23 2022 Mamoru TASAKA <mtasaka@fedoraproject.org> - 0.18-3
- Rebuild for gsl-2.7.1

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.18-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Fri Jul 15 2022 Alejandro Alvarez Ayllon <aalvarez@fedoraproject.org> - 0.18-1
- SourceXtractor++ 0.18

* Mon Jun 13 2022 Python Maint <python-maint@redhat.com> - 0.17-4
- Rebuilt for Python 3.11

* Wed May 04 2022 Thomas Rodgers <trodgers@redhat.com> - 0.17-3
- Rebuilt for Boost 1.78

* Tue Apr 26 2022 Alejandro Alvarez Ayllon <aalvarez@fedoraproject.org> - 0.17-2
- Rebuild

* Mon Apr 25 2022 Alejandro Alvarez Ayllon <aalvarez@fedoraproject.org> - 0.17-1
- SourceXtractor++ 0.17

* Sat Jan 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.16-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Mon Dec 20 2021 Alejandro Alvarez Ayllon <aalvarez@fedoraproject.org> - 0.16-1
- SourceXtractor++ 0.16

* Wed Aug 11 2021 Alejandro Alvarez Ayllon <aalvarez@fedoraproject.org> - 0.15-6
- Rebuild after f35 branching

* Mon Aug 09 2021 Alejandro Alvarez Ayllon <aalvarez@fedoraproject.org> - 0.15-5
- Patch double closing of file

* Sat Aug 07 2021 Jonathan Wakely <jwakely@redhat.com> - 0.15-4
- Rebuilt for Boost 1.76

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.15-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 0.15-2
- Rebuilt for Python 3.10

* Mon May 31 2021 Alejandro Alvarez Ayllon <aalvarez@fedoraproject.org> - 0.15-1
- Release 0.15

* Mon May 10 2021 Alejandro Alvarez Ayllon <aalvarez@fedoraproject.org> - 0.14-2
- Rebuild for gcc11.1

* Wed Apr 21 2021 Alejandro Alvarez Ayllon <aalvarez@fedoraproject.org> - 0.14-1
- Release 0.14

* Tue Feb 09 2021 Alejandro Alvarez Ayllon <aalvarez@fedoraproject.org> - 0.13-1
- Release 0.13

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.12-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Fri Jan 22 2021 Jonathan Wakely <jwakely@redhat.com> - 0.12-2
- Rebuilt for Boost 1.75

* Mon Dec 07 2020 Alejandro Alvarez Ayllon <aalvarez@fedoraproject.org> - 0.12-1
- Update for upstream release 0.12

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.11-3
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.11-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jul 21 2020 Alejandro Alvarez Ayllon <aalvarez@fedoraproject.org> - 0.11-1
- Update for upstream release 0.11

* Sat May 30 2020 Jonathan Wakely <jwakely@redhat.com> - 0.10-4
- Rebuilt for Boost 1.73

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 0.10-3
- Rebuilt for Python 3.9

* Tue Mar 17 2020 Alejandro Alvarez Ayllon <aalvarez@fedoraproject.org> - 0.10-2
- Rebuild for wcslib 7.2

* Fri Mar 13 2020 Alejandro Alvarez Ayllon <aalvarez@fedoraproject.org> - 0.10-1
- Update for upstream release 0.10

* Fri Jan 31 2020 Alejandro Alvarez Ayllon <aalvarez@fedoraproject.org> - 0.8-1
- New RPM

