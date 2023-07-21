# CVC4 1.4 and later need a modified glpk, unavailable in Fedora.  Therefore,
# we currently build without glpk support.

Name:           cvc4
Version:        1.8
Release:        19%{?dist}
Summary:        Automatic theorem prover for SMT problems

%global jar_version %{version}.0

# License breakdown:
# - The project as a whole is BSD-3-Clause
# - Files distributed under the MIT license
#   o src/prop/bvminisat
#   o src/prop/minisat
License:        BSD-3-Clause AND MIT
URL:            https://cvc4.github.io/
Source0:        https://github.com/CVC4/CVC4/archive/%{version}/%{name}-%{version}.tar.gz
# Do not override Fedora flags
Patch0:         %{name}-flags.patch
# Adapt to cryptominisat 5.7
Patch1:         %{name}-cryptominisat.patch
# Remove duplicate declarations, leads to errors with recent LFSC versions
Patch2:         %{name}-dup-decl.patch
# Just use the default linker specified by the distro. ld.gold was the
# new kid on the block a while ago, primarily offering higher link
# speeds. But it has aged, and has less features than ld.bfd. Let's
# use ld.bfd so that package notes work without workarounds.
Patch3:         %{name}-do-not-use-gold.diff
# Use tomllib instead of the deprecated toml package
Patch4:         %{name}-toml.patch
# Turn off the bash patsub_replacement option, which breaks templating
Patch5:         %{name}-bash-patsub-replacement.patch
# Add explicit includes to make CMake-3.27 happy
# https://bugzilla.redhat.com/show_bug.cgi?id=2214406
Patch6:         %{name}-cmake327.patch

# ANTLR 3 is not available on i686.
# See https://fedoraproject.org/wiki/Changes/Drop_i686_JDKs
ExclusiveArch:  %{java_arches}

BuildRequires:  abc-devel
BuildRequires:  antlr3-C-devel
BuildRequires:  antlr3-tool
BuildRequires:  boost-devel
BuildRequires:  cadical-devel
BuildRequires:  cmake
BuildRequires:  cmake(cryptominisat5)
BuildRequires:  cxxtest
BuildRequires:  drat2er-devel
BuildRequires:  drat-trim-devel
BuildRequires:  gcc-c++
BuildRequires:  ghostscript
BuildRequires:  gmp-devel
BuildRequires:  java-devel
BuildRequires:  javapackages-tools
BuildRequires:  kissat-devel
BuildRequires:  lfsc-devel
BuildRequires:  libtool
BuildRequires:  make
BuildRequires:  perl-interpreter
BuildRequires:  pkgconfig(readline)
BuildRequires:  python3-devel
BuildRequires:  %{py3_dist cython}
BuildRequires:  %{py3_dist setuptools}
BuildRequires:  swig
BuildRequires:  symfpu-devel

Requires:       %{name}-libs%{?_isa} = %{version}-%{release}

%description
CVC4 is an efficient open-source automatic theorem prover for
satisfiability modulo theories (SMT) problems.  It can be used to prove
the validity (or, dually, the satisfiability) of first-order formulas in
a large number of built-in logical theories and their combination.

CVC4 is the fourth in the Cooperating Validity Checker family of tools
(CVC, CVC Lite, CVC3) but does not directly incorporate code from any
previous version.  A joint project of NYU and U Iowa, CVC4 aims to
support the  features of CVC3 and SMT-LIBv2 while optimizing the design
of the core system architecture and decision procedures to take
advantage of recent engineering and algorithmic advances.

CVC4 is intended to be an open and extensible SMT engine, and it can be
used as a stand-alone tool or as a library, with essentially no limit on
its use for research or commercial purposes.

%package devel
Summary:        Headers and other files for developing with %{name}
Requires:       %{name}-libs%{?_isa} = %{version}-%{release}
Requires:       gmp-devel%{?_isa}
Requires:       symfpu-devel%{?_isa}

%description devel
Header files and library links for developing applications that use %{name}.

%package libs
Summary:        Library containing an automatic theorem prover for SMT problems

%description libs
Library containing the core of the %{name} automatic theorem prover for
SMT problems.

%package java
Summary:        Java interface to %{name}
Requires:       %{name}-libs%{?_isa} = %{version}-%{release}
Requires:       java-headless
Requires:       javapackages-tools

%description java
Java interface to %{name}.

%package python3
Summary:        Python 3 interface to %{name}
Requires:       %{name}-libs%{?_isa} = %{version}-%{release}

%description python3
Python 3 interface to %{name}.

%prep
%autosetup -p0 -n CVC4-%{version}

# Adapt to way kissat is packaged for Fedora
sed -i 's,#include <kissat/kissat\.h>,#include <kissat.h>,' src/prop/kissat.h

# We want to know about use of deprecated interfaces
sed -i '/Wno-deprecated/d' CMakeLists.txt

# The Java interface uses type punning
sed -i '/include_directories/aadd_compile_options("-fno-strict-aliasing")' \
    src/bindings/java/CMakeLists.txt

# The header file installation script does not know about DESTDIR
sed -i 's/\${CMAKE_INSTALL_PREFIX}/\\$ENV{DESTDIR}&/' src/CMakeLists.txt

# Fix installation directory on 64-bit arches
if [ "%{_lib}" = "lib64" ]; then
  sed -i 's/LIBRARY_INSTALL_DIR lib/&64/' CMakeLists.txt
fi

# Python extensions should not link against libpython; see
# https://github.com/python/cpython/pull/12946
sed -i 's/ \${PYTHON_LIBRARIES}//' src/bindings/python/CMakeLists.txt \
                                   src/api/python/CMakeLists.txt

%build
pyinc=$(python3-config --includes | sed -r 's/-I([^[:blank:]]+)[[:blank:]]*.*/\1/')
pylib=$(ls -1 %{_libdir}/libpython3.*.so)
export CFLAGS='%{build_cflags} -fsigned-char -DABC_USE_STDINT_H -I%{_jvmdir}/java/include -I%{_jvmdir}/java/include/linux -I%{_includedir}/abc'
export CXXFLAGS="$CFLAGS"
%cmake \
  -DBUILD_BINDINGS_PYTHON:BOOL=ON \
  -DBUILD_SWIG_BINDINGS_JAVA:BOOL=ON \
  -DBUILD_SWIG_BINDINGS_PYTHON:BOOL=ON \
  -DCMAKE_JAVA_COMPILE_FLAGS:STRING="-source;1.8;-target;1.8" \
  -DCMAKE_SKIP_RPATH:BOOL=YES \
  -DCMAKE_SKIP_INSTALL_RPATH:BOOL=YES \
  -DENABLE_GPL:BOOL=ON \
  -DENABLE_OPTIMIZED:BOOL=ON \
  -DENABLE_PORTFOLIO:BOOL=ON \
  -DENABLE_PROOFS:BOOL=ON \
  -DENABLE_SHARED:BOOL=ON \
  -DUSE_ABC:BOOL=ON \
  -DABC_ARCH_FLAGS:FILEPATH="-I%{_includedir}/abc" \
  -DUSE_CADICAL:BOOL=ON \
  -DUSE_CRYPTOMINISAT:BOOL=ON \
  -DCryptoMiniSat_INCLUDE_DIR:FILEPATH=%{_includedir}/cryptominisat5 \
  -DUSE_DRAT2ER:BOOL=ON \
  -DDrat2Er_INCLUDE_DIR:FILEPATH=%{_includedir} \
  -DDrat2Er_LIBRARIES:STRING=-ldrat2er \
  -DDratTrim_LIBRARIES:STRING=-ldrat-trim \
  -DUSE_KISSAT:BOOL=ON \
  -DKissat_INCLUDE_DIR:FILEPATH=%{_includedir} \
  -DKissat_LIBRARIES:STRING=-lkissat \
  -DUSE_LFSC:BOOL=ON \
  -DUSE_PYTHON3:BOOL=ON \
  -DUSE_READLINE:BOOL=ON \
  -DUSE_SYMFPU:BOOL=ON \
  -DSYMFPU_DIR:FILEPATH=%{_prefix} \
  -DPYTHON_EXECUTABLE:FILEPATH=%{_bindir}/python%{python3_version} \
  -DPYTHON_LIBRARY:FILEPATH=$pylib \
  -DPYTHON_INCLUDE_DIR:FILEPATH=$pyinc

# Tell swig to build for python 3
sed -i 's/swig -python/& -py3/' \
  %{_vpath_builddir}/src/bindings/python/CMakeFiles/CVC4_swig_compilation.dir/build.make

%cmake_build
make doc

%install
# The Python API install target ignores DESTDIR, so force the issue.
sed -e 's,"%{_prefix}","%{buildroot}%{_prefix}",g' \
    -e 's,--prefix=%{_prefix},--prefix=%{buildroot}%{_prefix},' \
    -i %{_vpath_builddir}/src/api/python/cmake_install.cmake

%cmake_install

# Link the JNI interface to where Fedora mandates it should go
mkdir -p %{buildroot}%{_jnidir}/%{name}
ln -s ../../%{_lib}/libcvc4jni.so %{buildroot}%{_jnidir}/%{name}

# Fix a symlink that points to the build directory
rm %{buildroot}%{_javadir}/%{name}/CVC4.jar
ln -s CVC4-%{jar_version}.jar %{buildroot}%{_javadir}/%{name}/CVC4.jar

# The cython interface is installed into the wrong directory
if [ "%{python3_sitelib}" != "%{python3_sitearch}" ]; then
  mv %{buildroot}%{python3_sitelib}/pycvc4* %{buildroot}%{python3_sitearch}
  rm -fr %{buildroot}%{prefix}/lib/python3*
fi

# Add a missing executable bit
chmod 0755 %{buildroot}%{python3_sitearch}/pycvc4/pycvc4.so

%check
# The tests use a large amount of stack space.
# Only do this on s390x to workaround bz 1688841.
%ifarch s390x
ulimit -s unlimited
%endif

# Fix the Java test's access to the JNI object it needs
sed 's,loadLibrary("cvc4jni"),load("%{buildroot}%{_jnidir}/%{name}/libcvc4jni.so"),' \
    -i test/system/CVC4JavaTest.java

export LC_ALL=C.UTF-8
export LD_LIBRARY_PATH=%{buildroot}%{_libdir}
%cmake_build --target check

%files
%doc AUTHORS NEWS README.md THANKS
%{_bindir}/%{name}
%{_datadir}/%{name}/
%{_mandir}/man1/%{name}.1*
%{_mandir}/man5/%{name}.5*

%files libs
%license COPYING
%{_libdir}/lib%{name}.so.7
%{_libdir}/lib%{name}parser.so.7

%files devel
%{_includedir}/%{name}/
%{_libdir}/lib%{name}.so
%{_libdir}/lib%{name}parser.so
%{_libdir}/cmake/CVC4/
%{_mandir}/man3/SmtEngine.3cvc*
%{_mandir}/man3/libcvc4*
%{_mandir}/man3/options.3cvc*

%files java
%{_javadir}/%{name}/
%{_jnidir}/%{name}/
%{_libdir}/libcvc4jni.so

%files python3
%{python3_sitearch}/CVC4.py
%{python3_sitearch}/_CVC4.so
%{python3_sitearch}/__pycache__/CVC4.*
%{python3_sitearch}/pycvc4*

%changelog
* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.8-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Fri Jul 07 2023 Python Maint <python-maint@redhat.com> - 1.8-18
- Rebuilt for Python 3.12

* Mon Jun 12 2023 Björn Esser <besser82@fedoraproject.org> - 1.8-17
- Add patch to fix build with CMake v3.27.0

* Thu May 11 2023 Jerry James <loganjerry@gmail.com> - 1.8-16
- Add missing Requires to the devel subpackage (rhbz#2203174)

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.8-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Mon Dec 19 2022 Jerry James <loganjerry@gmail.com> - 1.8-14
- BR setuptools to fix FTBFS (rhbz#2154858)

* Tue Oct 11 2022 Jerry James <loganjerry@gmail.com> - 1.8-13
- Add -bash-patsub-replacement patch to fix build with bash 5.2 (bz 2133760)
- Add -toml patch and drop python3-toml BR

* Mon Aug 15 2022 Jerry James <loganjerry@gmail.com> - 1.8-12
- Convert License tag to SPDX

* Wed Jul 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.8-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Tue Jul 19 2022 Jerry James <loganjerry@gmail.com> - 1.8-11
- Drop support for i686 due to ANTLR unavailability

* Mon Jun 13 2022 Python Maint <python-maint@redhat.com> - 1.8-11
- Rebuilt for Python 3.11

* Fri Mar  4 2022 Jerry James <loganjerry@gmail.com> - 1.8-10
- Remove . from %%cmake invocation to fix FTBFS (rhbz#2060821)
- Drop -const-map-key patch now that gcc has been fixed

* Sat Feb 05 2022 Jiri Vanek <jvanek@redhat.com> - 1.8-9
- Rebuilt for java-17-openjdk as system jdk

* Sat Jan 22 2022 Jerry James <loganjerry@gmail.com> - 1.8-8
- Add -const-map-key patch to fix FTBFS

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.8-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild
- Use the default linker

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.8-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 1.8-6
- Rebuilt for Python 3.10

* Wed Jun  2 2021 Jerry James <loganjerry@gmail.com> - 1.8-5
- Remove spurious rpaths (bz 1967190)
- Fix broken jar symlink
- Add missing executable bit to python shared object

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.8-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jan 20 2021 Jerry James <loganjerry@gamil.com> - 1.8-3
- Add -dup-decl patch to fix FTBFS with recent LFSC versions

* Fri Nov 27 2020 Jerry James <loganjerry@gmail.com> - 1.8-2
- Rebuild for cryptominisat 5.8.0

* Mon Aug  3 2020 Jerry James <loganjerry@gmail.com> - 1.8-1
- Version 1.8
- Drop upstreamed patches: -abc, -swig4, -drat
- Run the testsuite on 64-bit architectures only

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.7-15
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.7-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Jul 10 2020 Jiri Vanek <jvanek@redhat.com> - 1.7-13
- Rebuilt for JDK-11, see https://fedoraproject.org/wiki/Changes/Java11

* Fri May 29 2020 Jonathan Wakely <jwakely@redhat.com> - 1.7-12
- Rebuilt for Boost 1.73

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 1.7-11
- Rebuilt for Python 3.9

* Fri May 15 2020 Jerry James <loganjerry@gmail.com> - 1.7-10
- Do not link against libpython

* Sat Apr 25 2020 Jerry James <loganjerry@gmail.com> - 1.7-9
- Rebuild for cryptominisat 5.7.0
- Add -cryptominisat patch to adapt to changes in 5.7.0

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.7-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Mon Nov 11 2019 Jerry James <loganjerry@gmail.com> - 1.7-7
- Rebuild for cadical 1.2.1

* Mon Sep  9 2019 Jerry James <loganjerry@gmail.com> - 1.7-6
- Add -drat patch to fix build with latest lfsc

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 1.7-5
- Rebuilt for Python 3.8

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.7-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jul 18 2019 Jerry James <loganjerry@gmail.com> - 1.7-3
- Rebuild for cadical 1.0.3 (bz 1731031)

* Sat Jun 29 2019 Jerry James <loganjerry@gmail.com> - 1.7-2
- Fix finding the python include dir and lib (bz 1724142)

* Wed Jun 12 2019 Jerry James <loganjerry@gmail.com> - 1.7-1
- New upstream release
- Drop -autoconf, -cadical, -doxygen, -symfpu, and -vec patches
- Drop -doc subpackage; upstream no longer supports doxygen
- Build with python 3 instead of python 2
- Build with drat2er support
- Add -abc and -flags patches
- Add -swig4 patch (bz 1707353)

* Sun Feb 17 2019 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 1.6-6
- Rebuild for readline 8.0

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.6-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Tue Jan 29 2019 Jonathan Wakely <jwakely@redhat.com> - 1.6-4
- Rebuilt for Boost 1.69

* Mon Nov 26 2018 Jerry James <loganjerry@gmail.com> - 1.6-3
- Rebuild for updated abc

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jul 10 2018 Jerry James <loganjerry@gmail.com> - 1.6-1
- New upstream release

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.5-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Feb  1 2018 Jerry James <loganjerry@gmail.com> - 1.5-5
- Fix FTBFS with automake 1.5.1 (bz 1482152)

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.5-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.5-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Jul 21 2017 Kalev Lember <klember@redhat.com> - 1.5-2
- Rebuilt for Boost 1.64

* Sat Jul 15 2017 Jerry James <loganjerry@gmail.com> - 1.5-1
- New upstream release
- Drop upstreamed patches: -signed, -boolean, -minisat
- Add -constant patch to fix undefined symbols in the JNI shared object
- Add cryptominisat4 support

* Mon May 15 2017 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_27_Mass_Rebuild

* Fri Mar  3 2017 Jerry James <loganjerry@gmail.com> - 1.4-14
- Fix FTBFS (bz 1427891)

* Tue Feb 07 2017 Kalev Lember <klember@redhat.com> - 1.4-13
- Rebuilt for Boost 1.63

* Thu Jan 12 2017 Igor Gnatenko <ignatenko@redhat.com> - 1.4-12
- Rebuild for readline 7.x

* Tue May 17 2016 Jonathan Wakely <jwakely@redhat.com> - 1.4-11
- Rebuilt for linker errors in boost (#1331983)

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.4-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Jan 15 2016 Jonathan Wakely <jwakely@redhat.com> - 1.4-9
- Rebuilt for Boost 1.60

* Thu Aug 27 2015 Jonathan Wakely <jwakely@redhat.com> - 1.4-8
- Rebuilt for Boost 1.59

* Wed Jul 29 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4-7
- Rebuilt for https://fedoraproject.org/wiki/Changes/F23Boost159

* Wed Jul 22 2015 David Tardon <dtardon@redhat.com> - 1.4-6
- rebuild for Boost 1.58

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat May 02 2015 Kalev Lember <kalevlember@gmail.com> - 1.4-4
- Rebuilt for GCC 5 C++11 ABI change

* Fri Mar 20 2015 Jerry James <loganjerry@gmail.com> - 1.4-3
- Don't use perftools at all due to random weirdness on multiple platforms
- Also Obsoletes/Provides lfsc-devel

* Wed Mar 11 2015 Jerry James <loganjerry@gmail.com> - 1.4-2
- Add -boolean, -minisat, and -signed patches to fix test failures
- Fix boost detection with g++ 5.0
- Fix access to an uninitialized variable
- Help the documentation generator find COPYING
- Build with -fsigned-char to fix the arm build
- Prevent rebuilds while running checks
- Remove i686 from have_perftools due to test failures

* Tue Jan 27 2015 Petr Machata <pmachata@redhat.com> - 1.4-2
- Rebuild for boost 1.57.0

* Thu Jan  1 2015 Jerry James <loganjerry@gmail.com> - 1.4-1
- New upstream release
- Drop updated test files, now included upstream
- Drop obsolete workarounds for glpk compatibility
- Drop lfsc BR/R, as it has been incorporated into cvc4

* Fri Aug 22 2014 Jerry James <loganjerry@gmail.com> - 1.3-7
- Remove arm platforms from have_perftools due to bz 1109309

* Sat Aug 16 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Fri May 23 2014 David Tardon <dtardon@redhat.com> - 1.3-5
- rebuild for boost 1.55.0

* Thu Mar  6 2014 Jerry James <loganjerry@gmail.com> - 1.3-4
- Merge changes from Dan Horák to fix secondary arch builds

* Tue Feb  4 2014 Jerry James <loganjerry@gmail.com> - 1.3-3
- glibc Provides /sbin/ldconfig, not /usr/sbin/ldconfig

* Mon Jan 27 2014 Jerry James <loganjerry@gmail.com> - 1.3-2
- Install JNI objects in %%{_jnidir}
- The documentation is arch-specific after all

* Wed Jan 22 2014 Jerry James <loganjerry@gmail.com> - 1.3-1
- Initial RPM
