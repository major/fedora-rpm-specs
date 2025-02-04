%if 0%{?fedora}
%ifarch %{java_arches}
%global with_jacop     0
%else
%global with_jacop     0
%endif
%global with_gecode    1
%global with_highs     1
%global with_scip      1
%endif

%if 0%{?rhel}
%global with_jacop     0
%global with_gecode    0
%global with_highs     0
%global with_scip      0
%endif

%if 0%{?fedora} || 0%{?rhel} >= 9
%global blaslib flexiblas
%else
%global blaslib openblas
%endif

# Upstream has stopped tagging releases.  For a list of recent releases, see
# CHANGES.mp.md.
%global commit      9646be4f2d9ba3c59d3025b0a317dc8084973ed5
%global date        20240319
%global forgeurl    https://github.com/ampl/mp

Name: mp
Version: 20240319
Summary: An open-source library for mathematical programming

%forgemeta

# SMLNJ: the project as a whole
# BSD-2-Clause: src/{format,rstparser}.cc,
#               include/mp/{format,rstparser,safeint}.h
# GPL-2.0-or-later: src/asl/mkstemps.c (not included in the binary RPM)
# GPL-3.0-or-later: src/gsl/default.c (not included in the binary RPM)
License: SMLNJ AND BSD-2-Clause
Release: 10%{?dist}
URL: https://mp.ampl.com/
VCS: git:%{forgeurl}.git
Source0: %{forgesource}
# Unbundle asl
Patch0:  %{name}-unbundle-asl.patch
# https://bugzilla.redhat.com/show_bug.cgi?id=1333344
Patch1:  %{name}-3.1.0-jni.patch
# Adapt to python 3
Patch2:  %{name}-python3.patch
# Remove redundant calls to std::move
Patch3:  %{name}-redundant-move.patch
# Complete an incomplete name change from ProblemInfo to NLProblemInfo
Patch4:  %{name}-probleminfo.patch
# Fix use of an int where a member of an enum is needed
Patch5:  %{name}-enum-cast.patch
# Fix a name clash on "obj_name"
Patch6:  %{name}-obj-name.patch
# Fix FTBFS due to ambiguous names in expr-writer.h
Patch7:  %{name}-expr-writer.patch

# See https://fedoraproject.org/wiki/Changes/EncourageI686LeafRemoval
ExcludeArch: %{ix86}

# This package bundles an old copy of fmt.  The interface has changed
# significantly since then, so porting is nontrivial.
Provides: bundled(fmt) = 3.0.1

BuildRequires: asl-devel
BuildRequires: cmake
%if 0%{?with_scip}
BuildRequires: cmake(scip)
%endif
BuildRequires: doxygen
BuildRequires: gcc-c++
%if 0%{?fedora} || 0%{?rhel} >= 8
BuildRequires: gdb-headless
%else
BuildRequires: gdb
%endif
%if 0%{?with_gecode}
BuildRequires: gecode-devel
%endif
# Need git to satisfy a cmake test if building modules (gsl)
BuildRequires: git-core
%if 0%{?with_jacop}
BuildRequires: jacop
BuildRequires: java-devel
BuildRequires: make
Requires: jacop
%endif
BuildRequires: %{blaslib}-devel
%if 0%{?with_highs}
BuildRequires: pkgconfig(highs)
%endif
BuildRequires: pkgconfig(gsl)
BuildRequires: python3-devel

# This can be removed when F43 reaches EOL
Obsoletes:     %{name}-doc < 20240115

%global majver %(cut -d. -f1 <<< %{version})

%description
An open-source library for mathematical programming.
Features
  * Reusable high-performance .nl reader
  * Efficient type-safe C++ API for connecting solvers to AMPL and
    other systems: source
  * Interfaces to solvers supporting AMPL extensions for logic and
    constraint programming:
      * IBM ILOG CPLEX and CPLEX CP Optimizer (ilogcp)
      * Gecode
      * JaCoP
  * Interfaces to the following solvers:
      * LocalSolver
      * Sulum
  * Interfaces to other solvers via AMPL Solver Library
  * Cross-platform build support with CMake and continuous
    integration systems. This includes third-party solvers and
    libraries (COIN-OR solvers with CMake support are available
    in the ampl/coin repository).
  * AMPLGSL, an AMPL function library providing access to the GNU
    Scientific Library (GSL) functions. See the AMPLGSL
    documentation.
  * Database support on Linux and MacOS X. See Database and
    spreadsheet connection guide.
  * SMPSWriter, a converter from deterministic equivalent of a
    two-stage stochastic programming (SP) problem written in AMPL
    to an SP problem in SMPS format.

%package devel
Summary: Development files for %{name}
Requires: %{name}%{?_isa} = %{version}-%{release}
Requires: asl-devel%{?_isa}

%description devel
This package contains the header files for %{name}.

%prep
%forgeautosetup -p1

%if 0%{?with_jacop}
jacopver=$(sed -n 's,^    <version>\(.*\)</version>,\1,p' %{_mavenpomdir}/jacop/jacop.pom)
ln -s %{_javadir}/jacop/jacop.jar thirdparty/jacop/jacop-$jacopver.jar
%endif

# Fix library installation location
if [ '%{_lib}' != 'lib' ]; then
  sed -i 's/\(DESTINATION \)lib/\1%{_lib}/' CMakeLists.txt src/asl/CMakeLists.txt
fi

# Install the AMPL function libraries in libexec
sed -i 's,\(AMPL_LIBRARY_DIR \)bin,\1libexec/mp,' CMakeLists.txt

# Link with an optimized blas library
sed -i 's/gslcblas/%{blaslib}/' src/gsl/CMakeLists.txt

# Enable the gsl interface
sed -i '/add_subdirectory(solvers)/i\\tadd_subdirectory(src/gsl)' CMakeLists.txt

# Link the HiGHS interface with the actual HiGHS library
%if 0%{?with_highs}
sed -i '/target_link_libraries/s/\${RT_LIBRARY}/& -lhighs/' CMakeLists.txt
%endif

# Link the SCIP interface with the actual SCIP library
%if 0%{?with_scip}
sed -i '/target_link_libraries/s/\${RT_LIBRARY}/& -lscip/' CMakeLists.txt
%endif

# Build the jacop interface for JDK 8 at a minimum
%if 0%{?with_jacop}
sed -i 's/1\.7/1.8/g' solvers/jacop/CMakeLists.txt
%endif

%build
BUILD='asl,smpswriter'
%if 0%{?with_gecode}
BUILD="gecode,$BUILD"
%endif
%if 0%{?with_jacop}
BUILD="jacop,$BUILD"
%endif
%if 0%{?with_highs}
BUILD="highsmp,$BUILD"
%endif
%if 0%{?with_scip}
BUILD="scipmp,$BUILD"
%endif
commonflags="-I%{_includedir}/asl -I$PWD/src/asl/solvers -I%{_includedir}/highs -I%{_includedir}/scip -DNDEBUG"
export CFLAGS="%{build_cflags} $commonflags"
export CXXFLAGS="%{build_cxxflags} $commonflags"
%cmake \
 -DCMAKE_SHARED_LINKER_FLAGS:STRING="$LDFLAGS" \
 -DCMAKE_CXX_FLAGS_RELEASE:STRING="$CXXFLAGS" \
 -DCMAKE_C_FLAGS_RELEASE:STRING="$CFLAGS" \
 -DCMAKE_SKIP_INSTALL_RPATH:BOOL=NO \
 -DCMAKE_SKIP_RPATH:BOOL=NO \
 -DCMAKE_VERBOSE_MAKEFILE:BOOL=YES \
 -DBUILD_SHARED_LIBS:BOOL=YES \
 -DBUILD:STRING=$BUILD
%cmake_build

%install
%cmake_install

# We install the license file elsewhere
rm -rf %{buildroot}%{_datadir}

# There are numerous tests that no longer match the behavior of the code.
# Upstream appears to have allowed the test suite to bitrot.  Do not run
# the tests until upstream gets them back in shape.
#%%check
# Some of the tests use the SAME FILENAME to store temporary results, so
# running the tests in parallel leads to intermittent test failures, generally
# in either os-test or solver-test.  Do not pass the parallel flags to ctest.
#%%ctest -j1

%files
%doc README.rst
%license LICENSE.rst
%if 0%{?with_gecode}
%{_bindir}/gecode
%endif
%if 0%{?with_highs}
%{_bindir}/highsmp
%endif
%if 0%{?with_jacop}
%{_bindir}/jacop
%endif
%{_bindir}/scipmp
%{_bindir}/smpswriter
%{_libdir}/libaslmp.so.3*
%{_libdir}/libmp.so.3*
%{_libexecdir}/mp/

%files devel
%{_libdir}/libaslmp.so
%{_libdir}/libmp.so
%{_includedir}/asl
%{_includedir}/mp

%changelog
* Sun Feb 02 2025 Orion Poplawski <orion@nwra.com> - 20240319-10
- Rebuild with gsl 2.8

* Thu Jan 30 2025 Antonio Trande <sagitter@fedoraproject.org.com> - 20240319-9
- Make Jacop conditionally required (rhbz#2343005)
- Disable Jacop (currently unmaintained)
- Fix packaging of installed files

* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 20240319-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Tue Dec  3 2024 Jerry James <loganjerry@gmail.com> - 20240319-7
- Rebuild for asl 20241111 and coin-or-HiGHS 1.8.1

* Sat Oct 19 2024 Jerry James <loganjerry@gmail.com> - 20240319-6
- Rebuild for coin-or-HiGHS 1.8.0

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 20240319-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Wed Jul  3 2024 Jerry James <loganjerry@gmail.com> - 20240319-4
- Rebuild for coin-or-HiGHS 1.7.2

* Mon Jun 24 2024 Jerry James <loganjerry@gmail.com> - 20240319-3
- Rebuild for scip 9.1.0

* Wed Jun 19 2024 Jerry James <loganjerry@gmail.com> - 20240319-2
- Rebuild for coin-or-HiGHS 1.7.1 and scip 9.0.1

* Tue Mar 19 2024 Jerry James <loganjerry@gmail.com> - 20240319-1
- Update to release 20240319
- Add obj-name and expr-writer patches to fix FTBFS

* Wed Mar 13 2024 Jerry James <loganjerry@gmail.com> - 20240115-3
- Rebuild for soplex 7.0.0 and scip 9.0.0
- Build the jacop interface for JDK 1.8 (rhbz#2266676)

* Tue Feb 27 2024 Jiri Vanek <jvanek@redhat.com> - 20240115-2
- Rebuilt for java-21-openjdk as system jdk

* Wed Feb  7 2024 Jerry James <loganjerry@gmail.com> - 20240115-1
- Update to latest release, with new version scheme
- Unbundle asl
- Stop building documentation
- Drop support for Fedora < 37
- Build with support for HiGHS and SCIP
- Remove unused ODBC dependency
- Remove unnecessary environment module; install to libexec instead
- Stop building for 32-bit x86

* Sat Feb 03 2024 Antonio Trande <sagitter@fedoraproject.org.com> - 3.1.0-45.20200303git7fd4828
- Patched for GCC-14 (rhbz#2261393)
- Switch to SPDX

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.0-44.20200303git7fd4828
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.0-43.20200303git7fd4828
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.0-42.20200303git7fd4828
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.0-41.20200303git7fd4828
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Tue Aug 23 2022 Mamoru TASAKA <mtasaka@fedoraproject.org> - 3.1.0-40.20200303git7fd4828
- Rebuild for gsl-2.7.1

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.0-39.20200303git7fd4828
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Tue Jul 05 2022 Antonio Trande <sagitter@fedoraproject.org.com> - 3.1.0-38.20200303git7fd4828
- Drop JDK in i686 builds

* Sat Feb 05 2022 Jiri Vanek <jvanek@redhat.com> - 3.1.0-37.20200303git7fd4828
- Rebuilt for java-17-openjdk as system jdk

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.0-36.20200303git7fd4828
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.0-35.20200303git7fd4828
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri May 21 2021 Antonio Trande <sagitter@fedoraproject.org.com> - 3.1.0-34.20200303git7fd4828
- Add python3-devel as BR package

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.0-33.20200303git7fd4828
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Fri Jan 15 2021 Jerry James <loganjerry@gmail.com> - 3.1.0-32.20200303git7fd4828
- Add -jvm-destructor to fix jacop-related crashes (bz 1858054)
- Remove RHEL 6 support

* Thu Aug 27 2020 Iñaki Úcar <iucar@fedoraproject.org> - 3.1.0-31.20200303git7fd4828
- https://fedoraproject.org/wiki/Changes/FlexiBLAS_as_BLAS/LAPACK_manager

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.0-30.20200303git7fd4828
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild
- Enable __cmake_in_source_build
- Exclude jacop-test on ppc64le (rhbz#1859925)

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.0-29.20200303git7fd4828
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Sat Jul 11 2020 Jiri Vanek <jvanek@redhat.com> - 3.1.0-28.20200303git7fd4828
- Rebuilt for JDK-11, see https://fedoraproject.org/wiki/Changes/Java11

* Mon Apr 27 2020 Jerry James <loganjerry@gmail.com> - 3.1.0-27.20200303git7fd4828
- Update git snapshot for gecode 6.x support
- Drop upstreamed -gecode5 patch

* Fri Feb 21 2020 Jerry James <loganjerry@gmail.com> - 3.1.0-26.20200215git71c21a5
- Update to latest git snapshot for bug fixes
- Add -doc subpackage
- Add gecode 5 support, enabling gecode support for all releases
- Add -python3 patch to adapt to python3
- Jacop support did not work at all.  Add Requires: jacop, symlink to jacop.jar
  where mp expects to find it, and fix rpath handling so libjvm.so can be found
- Do not invoke rpm to get the jacop version; that is not guaranteed to work
- Build with openblas instead of atlas
- Run all tests on Fedora and EPEL 7+
- Numerous small spec file cleanups

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.0-25.20161124git1f39801
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Tue Aug 20 2019 Susi Lehtola <jussilehtola@fedoraproject.org> - 3.1.0-24.20161124git1f39801
- Rebuilt for GSL 2.6.

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.0-23.20161124git1f39801
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Tue May 07 2019 Antonio Trande <sagitter@fedoraproject.org.com> - 3.1.0-22.20160810git1f39801
- Set _modulesdir macro for rhel

* Tue May 07 2019 Antonio Trande <sagitter@fedoraproject.org.com> - 3.1.0-21.20160810git1f39801
- Some improvements

* Fri Feb 22 2019 Orion Poplawski <orion@nwra.com> - 3.1.0-20.20161124git1f3980
- Install modulefile in proper location

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.0-19.20161124git1f3980
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.0-18.20161124git1f3980
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Sun Mar 11 2018 Antonio Trande <sagitter@fedoraproject.org.com> - 3.1.0-17.20160810git1f3980
- Rebuild for Java

* Sat Feb 17 2018 Antonio Trande <sagitter@fedoraproject.org> - 3.1.0-16.20161124git1f3980
- Use %%ldconfig_scriptlets

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.0-15.20161124git1f3980
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Sun Jan 14 2018 Antonio Trande <sagitter@fedoraproject.org.com> - 3.1.0-14.20160810git1f3980
- Use versioned Python2 packages

* Wed Nov 15 2017 Antonio Trande <sagitter@fedoraproject.org.com> - 3.1.0-13.20160810git1f3980
- Enable jacop on f27+

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.0-12.20161124git1f3980
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Sun Jul 30 2017 Antonio Trande <sagitter@fedoraproject.org.com> - 3.1.0-11.20160810git1f3980
- Disable jacop (bz#1423750)

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.0-10.20161124git1f3980
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Mar 25 2017 Antonio Trande <sagitter@fedoraproject.org.com> - 3.1.0-9.20160810git1f3980
- Gecode support temporarily disabled on fedora (upstream bug#109)

* Thu Mar 16 2017 Antonio Trande <sagitter@fedoraproject.org.com> - 3.1.0-8.20160810git1f3980
- Rebuild for gecode-5.0.0

* Sun Feb 26 2017 Antonio Trande <sagitter@fedoraproject.org.com> - 3.1.0-7.20160810git1f3980
- Fix environment-modules required on epel7
- Skip gsl-test always (upstream issue #103)

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.0-6.20161124git1f3980
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Nov 24 2016 Antonio Trande <sagitter@fedoraproject.org.com> - 3.1.0-5.20160810git1f3980
- Skip gsl-test on epel6 (upstream issue #103)

* Thu Nov 24 2016 Antonio Trande <sagitter@fedoraproject.org.com> - 3.1.0-4.20160810git1f3980
- Update to commit #1f3980 (fmt updated to 3.0.1)
- Patched for PPC64

* Thu Jun 30 2016 Antonio Trande <sagitter@fedoraproject.org.com> - 3.1.0-3
- Fix cmake version for EPEL
- libmp installed in a private lib directory on epel6
- Pached to remove gtest
- Set to disable tests on EPEL6

* Thu May 05 2016 Dan Horák <dan[at]danny.cz> - 3.1.0-2
- fix build on secondary arches (thirdparty/benchmark) (#1333344)
- fix JNI detection (#1333344)

* Wed Mar 30 2016 Antonio Trande <sagitter@fedoraproject.org.com> - 3.1.0-1
- Update to 3.1.0

* Wed Mar 16 2016 pcpa <paulo.cesar.pereira.de.andrade@gmail.com> - 3.0.1-0.2
- Avoid incorrect system detection and use of strtod_ASL wrapper
- Install extra headers required by coin-or-Couenne

* Fri Mar 04 2016 Antonio Trande <sagitter@fedoraproject.org.com> - 3.0.1-0.1
- Update to 3.0.1 prerelease (commit #9fdb514)

* Thu Mar 03 2016 Antonio Trande <sagitter@fedoraproject.org.com> - 3.0.0-1
- Update to 3.0.0

* Wed Mar 02 2016 Antonio Trande <sagitter@fedoraproject.org.com> - 2.1.1-0.2
- Built with cmake3 on EPEL

* Tue Mar 01 2016 Antonio Trande <sagitter@fedoraproject.org.com> - 2.1.1-0.1
- Update to 2.1.0
- Dropped old patches for 1.3.0
- Jacop support disabled on EPEL
- Patched for GCC6
- Patched for GSL-2.1
- fpinit patched for ARM 

* Mon Feb 22 2016 Orion Poplawski <orion@cora.nwra.com> - 1.3.0-10
- Rebuild for gsl 2.1 

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jan 6 2016 Orion Poplawski <orion@cora.nwra.com> - 1.3.0-8
- Require environment(modules)

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sun Jun 14 2015 pcpa <paulo.cesar.pereira.de.andrade@gmail.com> - 1.3.0-6
- Rebuild for new gecode.

* Sat May 02 2015 Kalev Lember <kalevlember@gmail.com> - 1.3.0-5
- Rebuilt for GCC 5 C++11 ABI change

* Sun Feb 22 2015 pcpa <paulo.cesar.pereira.de.andrade@gmail.com> - 1.3.0-4
- Add recomended extra libs for gsl.

* Wed Jan 28 2015 pcpa <paulo.cesar.pereira.de.andrade@gmail.com> - 1.3.0-3
- Enable the jacop interface.
- Use a better patch for non x86 fpinit (#1186162)
- Correct check on bigendian.

* Fri Jan 23 2015 pcpa <paulo.cesar.pereira.de.andrade@gmail.com> - 1.3.0-2
- Use the license macro for the LICENSE.rst file (#1181793#c3)
- environment-modules is a Requires not BuildRequires (#1181793#c3)

* Tue Jan 13 2015 pcpa <paulo.cesar.pereira.de.andrade@gmail.com> - 1.3.0-1
- Update package to use new 1.3.0 release

* Mon Dec 22 2014 pcpa <paulo.cesar.pereira.de.andrade@gmail.com> - v20141006-4
- Update to version that works with rawide gecode
- Add jacop support, works but disabled, missing from rawhide
- Build smpswriter

* Fri Dec 19 2014 pcpa <paulo.cesar.pereira.de.andrade@gmail.com> - v20141006-3
- Switch to newer git commit as base of package
- Add conditional to build gecode
- Build documentation

* Wed Dec 17 2014 pcpa <paulo.cesar.pereira.de.andrade@gmail.com> - v20141006-2
- Use environment-modules to follow upstream conventions.

* Sat Dec 13 2014 pcpa <paulo.cesar.pereira.de.andrade@gmail.com> - v20141006-1
- Initial mp spec.

