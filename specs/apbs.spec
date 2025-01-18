# Workaround for GCC-10
%define _legacy_common_support 1

%global commit %{nil}
%global shortcommit %{nil}
%global datecommit %{nil}

# To perform all tests, APBS needs to be compiled together additional sub-modules
%bcond_without check

Name: apbs
Summary: Adaptive Poisson Boltzmann Solver
Version: 3.0.0
Release: 26%{datecommit}%{shortcommit}%{?dist}
# iAPBS looks licensed with a LGPLv2+, APBS is released under BSD license.
License: LGPL-2.0-or-later AND BSD-3-Clause
URL: https://www.poissonboltzmann.org/
Source0: https://github.com/Electrostatics/apbs/archive/refs/tags/v%{version}/%{name}-%{version}.tar.gz
Source1: %{name}-LGPL_V2

Patch0: %{name}-cmake.patch

# Exclude tests because they are for features inactivated
Patch1: %{name}-exclude_tests.patch

# Porting to Python-3.11
Patch2: %{name}-python311.patch

Patch3: apbs-c99.patch

BuildRequires: gcc-c++
BuildRequires: cmake3
BuildRequires: chrpath
BuildRequires: make
BuildRequires: doxygen
BuildRequires: graphviz
BuildRequires: maloc-devel
BuildRequires: zlib-devel
Requires: %{name}-libs%{?_isa} = %{version}-%{release}
Requires: python3-%{name}

%description
APBS is a software package for the numerical solution of the
Poisson-Boltzmann equation (PBE), one of the most popular continuum
models for describing electrostatic interactions between molecular
solutes in salty, aqueous media.  APBS was designed to efficiently
evaluate electrostatic properties for such simulations for a wide
range of length scales to enable the investigation of molecules with
tens to millions of atoms. It is also widely used in molecular
visualization (in such applications as PyMOL).

%package tools
Summary: Utility programs that utilize the APBS package
Requires: %{name}%{?_isa} = %{version}-%{release}
%description tools
The apbs-tools package contains several utility programs for
conversion, analysis and preparation of files that use the adaptive
poisson boltzmann solver library.

%package libs
Summary: Libraries for APBS
%description libs
APBS solver libraries.

%package devel
Summary: Libraries and header files for the APBS package
Requires: %{name}-libs%{?_isa} = %{version}-%{release}
%description devel
The apbs-devel package contains the header files and libraries
necessary for developing programs using the adaptive poisson boltzmann
(APBS) solver library.

%package doc
Summary: Documentation for the APBS package
BuildRequires: tex(latex)
BuildRequires: texlive-multirow
BuildRequires: texlive-hanging
BuildRequires: texlive-adjustbox
BuildRequires: texlive-stackengine
BuildRequires: texlive-sectsty
BuildRequires: texlive-etoc
BuildRequires: texlive-tocloft
BuildRequires: texlive-ulem
BuildRequires: texlive-newunicodechar
BuildRequires: texlive-wasy
BuildRequires: texlive-wasysym
BuildArch: noarch
%description doc
The apbs-doc package contains API reference inforemation for
development using the adaptive poisson boltzmann (APBS) solver
library.

%package -n python3-apbs
Summary: Python interface of APBS
BuildRequires: python3-devel
BuildRequires: python3-numpy
BuildRequires: python3-sphinx
BuildRequires: swig
%{?python_provide:%python_provide python3-%{name}}
Obsoletes:     %{name}-libs < 0:3.0.0-11
%description -n python3-apbs
Python interface of APBS.

%prep
%autosetup -n %{name}-%{version} -N
%patch -P 0 -p2 -b .apbs-cmake
%patch -P 1 -p1 -b .exclude_tests

%if 0%{?python3_version_nodots} >= 311
%patch -P 2 -p1 -b .python311
%endif

%patch -P 3 -p1

cp -p contrib/iapbs/COPYING contrib/iapbs/iapbs-COPYING
cp -p %{SOURCE1} contrib/iapbs/iapbs-LGPLv2

%build
# CMake needs BUILD_SHARED_LIBS:BOOL=OFF to build Python libraries
# Using CMake rpm macro automatically enables the shared libs building  
export CFLAGS="%{build_cflags} -fopenmp -lm"
export CXXFLAGS="%{build_cxxflags} -fopenmp -lm"
mkdir -p build
cmake -S . -B build -DCMAKE_BUILD_TYPE:STRING=Release \
 -DENABLE_iAPBS:BOOL=ON -DENABLE_OPENMP:BOOL=ON -DENABLE_VERBOSE_DEBUG:BOOL=OFF \
 -DENABLE_FETK:BOOL=OFF -DCMAKE_C_FLAGS:STRING="%{build_cflags} -fopenmp -lm -DNDEBUG" \
 -DCMAKE_CXX_FLAGS:STRING="%{build_cxxflags} -fopenmp -lm -DNDEBUG" \
 -DBUILD_SHARED_LIBS:BOOL=OFF -DENABLE_PYTHON:BOOL=ON -DBUILD_DOC:BOOL=ON \
 -DBUILD_TESTING:BOOL=ON -DENABLE_TESTS:BOOL=ON \
 -DCMAKE_INSTALL_PREFIX:PATH=%{_prefix} \
 -DINCLUDE_INSTALL_DIR:PATH=%{_includedir} \
 -DLIB_INSTALL_DIR:PATH=%{_libdir} \
 -DSHARE_INSTALL_PREFIX:PATH=%{_datadir}
make -O -j1 V=1 -C build

%install
%make_install -C build

# Tools
for bin in %{buildroot}%{_bindir}/{coulomb,born,mgmesh,dxmath,mergedx2,mergedx,value,uhbd_asc2bin,smooth,dx2mol,dx2uhbd,similarity,multivalue,benchmark,analysis,del2dx,tensor2dx}; do
    cp -p $bin %{buildroot}%{_bindir}/apbs-`basename $bin`
    rm -f $bin
done

# Remove rpaths
for bin in %{buildroot}%{_bindir}/apbs-{coulomb,born,mgmesh,dxmath,mergedx2,mergedx,value,uhbd_asc2bin,smooth,dx2mol,dx2uhbd,similarity,multivalue,benchmark,analysis,del2dx,tensor2dx}; do
    chrpath -d $bin
    chrpath -d %{buildroot}%{_bindir}/apbs
done

chrpath -d %{buildroot}%{_libdir}/libapbs.so.1

# Move Python libraries under Python's tree directories
mkdir -p %{buildroot}%{python3_sitearch}/apbs
install -pm 755 tools/manip/psize.py %{buildroot}%{python3_sitearch}/apbs/
%{__python3} %{_rpmconfigdir}/redhat/pathfix.py -pn -i "%{__python3}" %{buildroot}%{python3_sitearch}/apbs/psize.py
ln -s %{python3_sitearch}/apbs/psize.py %{buildroot}%{_bindir}/apbs-psize.py
install -pm 755 build/lib/_apbslib.so %{buildroot}%{python3_sitearch}/apbs/

# Remove redundant tools binary files in /usr/share
rm -rf %{buildroot}%{_datadir}/apbs

# Remove static libraries
for i in `find %{buildroot} -type f \( -name "*.a" \)`; do
 rm -f $i
done

%if %{with check}
%check
pushd tests
export LD_LIBRARY_PATH=%{buildroot}%{_libdir}
%{__python3} ./apbs_tester.py
%endif

%files
%{_bindir}/apbs

%files libs
%license LICENSE.md COPYING contrib/iapbs/iapbs-COPYING contrib/iapbs/iapbs-LGPLv2
%doc README.md
%{_libdir}/libapbs.so.1

%files -n python3-apbs
%{python3_sitearch}/apbs/

%files devel
%{_libdir}/libapbs.so
%{_includedir}/iapbs/
%{_includedir}/apbs

%files tools
%{_bindir}/apbs-psize.py
%{_bindir}/apbs-coulomb
%{_bindir}/apbs-born
%{_bindir}/apbs-mgmesh
%{_bindir}/apbs-dxmath
%{_bindir}/apbs-mergedx2
%{_bindir}/apbs-mergedx
%{_bindir}/apbs-value
%{_bindir}/apbs-uhbd_asc2bin
%{_bindir}/apbs-smooth
%{_bindir}/apbs-dx2mol
%{_bindir}/apbs-dx2uhbd
%{_bindir}/apbs-similarity
%{_bindir}/apbs-multivalue
%{_bindir}/apbs-benchmark
%{_bindir}/apbs-analysis
%{_bindir}/apbs-del2dx
%{_bindir}/apbs-tensor2dx

%files doc
%license LICENSE.md
%doc build/doc

%changelog
* Thu Jan 16 2025 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.0-26
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Wed Jul 17 2024 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.0-25
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Sat Jun 08 2024 Python Maint <python-maint@redhat.com> - 3.0.0-24
- Rebuilt for Python 3.13

* Sat May 25 2024 Antonio Trande <sagitter@fedoraproject.org> - 3.0.0-23
- Fix patch commands

* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.0-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.0-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.0-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Wed Jun 14 2023 Python Maint <python-maint@redhat.com> - 3.0.0-19
- Rebuilt for Python 3.12

* Mon Feb 06 2023 Florian Weimer <fweimer@redhat.com> - 3.0.0-18
- Fix C99 compatibility issue

* Wed Jan 18 2023 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.0-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Wed Jul 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.0-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon Jun 13 2022 Python Maint <python-maint@redhat.com> - 3.0.0-15
- Rebuilt for Python 3.11

* Wed Jan 19 2022 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.0-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Tue Jan 04 2022 Antonio Trande <sagitter@fedoraproject.org> - 3.0.0-13
- Patched for Python-3.11

* Mon Nov 01 2021 Antonio Trande <sagitter@fedoraproject.org> - 3.0.0-12
- Re-enable tests

* Mon Nov 01 2021 Antonio Trande <sagitter@fedoraproject.org> - 3.0.0-11
- Fix installation conflict of python package

* Sun Oct 31 2021 Antonio Trande <sagitter@fedoraproject.org> - 3.0.0-10
- Compile from a new source archive

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 3.0.0-8
- Rebuilt for Python 3.10

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Fri Jan 01 2021 Antonio Trande <sagitter@fedoraproject.org> - 3.0.0-6
- Use cmake3 options

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.0-5
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jun 17 2020 Antonio Trande <sagitter@fedoraproject.org> - 3.0.0-3
- Use cmake3 macro

* Wed Jun 17 2020 Antonio Trande <sagitter@fedoraproject.org> - 3.0.0-2
- Use cmake3

* Sun May 31 2020 Antonio Trande <sagitter@fedoraproject.org> - 3.0.0-1
- Release 3.0.0

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 3.0.0-0.3.20200512gitdfb858d
- Rebuilt for Python 3.9

* Wed May 13 2020 Antonio Trande <sagitter@fedoraproject.org> - 3.0.0-0.2.20200512gitdfb858d
- Fix release tag

* Wed May 13 2020 Antonio Trande <sagitter@fedoraproject.org> - 3.0.0-0.1.20200512.gitdfb858d
- Pre-release 3.0.0 (rhbz#1752306, rhbz#1799157)
- Add libs sub-package
- Add workaround for GCC-10
- Use Python3

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.5-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.5-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.5-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Sat May 19 2018 Tim Fenn <tim.fenn@gmail.com> - 1.5-1
- update to 1.5

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.4-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.4-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.4-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.4-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.4-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Fri Aug 15 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Thu Jun 19 2014 Tim Fenn <tim.fenn@gmail.com> - 1.4-1
- update to 1.4

* Wed Jun 18 2014 Tim Fenn <tim.fenn@gmail.com> - 1.3-8
- fix for bug 1105956 (apbslib.c patch for format-security error)

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Wed Oct 30 2013 Tim Fenn <tim.fenn@gmail.com> - 1.3-7
- rebuild for atlas 3.10.1 (consolidates lapack and blas)

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Wed Jul 18 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Thu Jan 12 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Mon Feb 07 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Mon Nov 15 2010 Tim Fenn <fenn@stanford.edu> - 1.3-1
- update to 1.3

* Wed Jul 21 2010 David Malcolm <dmalcolm@redhat.com> - 1.2.1-3
- Rebuilt for https://fedoraproject.org/wiki/Features/Python_2.7/MassRebuild

* Tue Dec 01 2009 Tim Fenn <fenn@stanford.edu> - 1.2.1-2
- add RPM_OPT_FLAGS

* Wed Nov 25 2009 Tim Fenn <fenn@stanford.edu> - 1.2.1-1
- update to 1.2.1

* Tue Nov 24 2009 Tim Fenn <fenn@stanford.edu> - 1.2.0-2
- fix broken source

* Thu Nov 04 2009 Tim Fenn <fenn@stanford.edu> - 1.2.0-1
- update to 1.2.0

* Mon Jul 27 2009 Tim Fenn <fenn@stanford.edu> - 1.1.0-7
- remove python byte compiled files in bindir
- loop to add tools

* Sun Jul 26 2009 Tim Fenn <fenn@stanford.edu> - 1.1.0-6
- remove check macro

* Fri Jul 24 2009 Tim Fenn <fenn@stanford.edu> - 1.1.0-5
- enable and add arpack, python to buildrequires, fix files section accordingly
- add check macro
- move tools to a subpackage
- move doc into subpackage
- spec cleanup

* Thu Jul 23 2009 Tim Fenn <fenn@stanford.edu> - 1.1.0-4
- merge aqua and pmgZ into libapbs

* Fri Jul 10 2009 Tim Fenn <fenn@stanford.edu> - 1.1.0-3
- separate aqua and pmgZ into separate libraries/packages
- add maloc BuildRequires

* Mon May 04 2009 Tim Fenn <fenn@stanford.edu> - 1.1.0-2
- fix RPM_BUILD_ROOT
- rename patches
- add "-q" to setup
- add README to doc
- edit description
- edit license

* Fri Apr 24 2009 Tim Fenn <fenn@stanford.edu> - 1.1.0-1
- initial build
