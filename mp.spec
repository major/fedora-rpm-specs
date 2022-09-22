%global __cmake_in_source_build 1

%if 0%{?fedora} && 0%{?fedora} > 36
%ifarch %{java_arches}
%global with_jacop     1
%else
%global with_jacop     0
%endif
%global with_gecode    1
%endif

%if 0%{?rhel}
%global with_jacop     0
%if 0%{?rhel} < 8
%global with_gecode    1
%else
%global with_gecode    0
%endif
%endif

%if 0%{?fedora} || 0%{?rhel} >= 9
%global blaslib flexiblas
%else
%global blaslib openblas
%endif

%if 0%{?rhel} && 0%{?rhel} < 8
%{!?_modulesdir: %global _modulesdir %{_datadir}/Modules/modulefiles}
%endif

%global  commit      7fd4828c934fccf7367499c9e01cc9a1e90a2093
%global  date        20200303
%global  shortcommit %(c=%{commit}; echo ${c:0:7})

Name: mp
Version: 3.1.0
Release: 40.%{date}git%{shortcommit}%{?dist}
License: MIT and BSD
Summary: An open-source library for mathematical programming
URL: https://github.com/ampl/mp
Source0: https://github.com/ampl/%{name}/archive/%{commit}/%{name}-%{commit}.tar.gz
Source1: %{name}.module.in
# The documentation building step wants this.  It is a git checkout of
# https://github.com/ampl/ampl.github.io.git, dated 21 Mar 2019,
# commit ccf1ff9f109d09ea0d42c60b6f26323312a99c42
Source2: ampl.github.io.tar.xz
Patch0:  %{name}-strtod.patch
# https://bugzilla.redhat.com/show_bug.cgi?id=1333344
Patch1:  %{name}-%{version}-jni.patch
# Adapt to python 3
Patch2:  %{name}-python3.patch
# Avoid crashes due to ambiguous order of destructor execution
# https://bugzilla.redhat.com/show_bug.cgi?id=1858054
Patch3:  %{name}-jvm-destructor.patch

%if 0%{?rhel} && 0%{?rhel} <= 7
Requires: config(environment-modules)
%else
Requires: environment(modules)
%endif

%if 0%{?with_jacop}
Requires: jacop
%endif

# This package bundles an old copy of fmt.  The interface has changed
# significantly since then, so porting is nontrivial.
Provides: bundled(fmt) = 3.0.1

%if 0%{?rhel} && 0%{?rhel} <= 7
BuildRequires: config(environment-modules)
%else
BuildRequires: environment(modules)
%endif
BuildRequires: chrpath
BuildRequires: cmake3
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
%endif
BuildRequires: %{blaslib}-devel
BuildRequires: pkgconfig(gsl)
%if 0%{?fedora}
BuildRequires: pkgconfig(odbc)
%endif
%if 0%{?fedora} || 0%{?rhel} == 7
BuildRequires: python%{python3_pkgversion}-breathe
BuildRequires: python%{python3_pkgversion}-sphinx
%endif
BuildRequires: python3-devel

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

%description devel
This package contains the header files for %{name}.

%package doc
Summary: Documentation for %{name}

%description doc
This package contains the developer documentation for %{name}.

%prep
%autosetup -n %{name}-%{commit} -a 2 -p1

%if 0%{?with_jacop}
jacopver=$(sed -n 's,^    <version>\(.*\)</version>,\1,p' %{_mavenpomdir}/jacop/jacop.pom)
ln -s %{_javadir}/jacop/jacop.jar thirdparty/jacop/jacop-$jacopver.jar
%endif

fixtimestamp() {
  touch -r $1.orig $1
  rm -f $1.orig
}

# Fix end of line and character encodings
for fil in $(find ampl.github.io/models -type f); do
  type=$(file $fil)
  if [[ "$type" =~ "with CRLF" ]]; then
    sed -i.orig 's/\r//' $fil
    fixtimestamp $fil
  fi
  if [[ "$type" =~ "ISO-8859" ]]; then
    mv $fil $fil.orig
    iconv -f ISO8859-1 -t UTF-8 $fil.orig > $fil
    fixtimestamp $fil
  fi
done

# Fix the invocation name for sphinx
%if 0%{?rhel} == 7
sed -i 's,sphinx-build,&-3.6,' support/build-docs.py
%endif

# python-breathe is broken in EPEL 7 and absent in EPEL 8, so skip building
# sphinx docs for those distributions.
%if 0%{?rhel}
sed -i 's,returncode == 0,False,' support/build-docs.py
%endif

%build
export LIBS="-lgsl -l%{blaslib}"
mkdir -p build && pushd build
BUILD="asl,gsl,smpswriter"
%if 0%{?with_gecode}
BUILD="gecode,$BUILD"
%endif
%if 0%{?with_jacop}
BUILD="jacop,$BUILD"
%endif
export CPPFLAGS="-I$PWD/src/asl/solvers"
export CFLAGS="%{optflags} -DNDEBUG"
export CXXFLAGS="%{optflags} -DNDEBUG"
# Let cmake create rpaths, so the jacop-using files can find libjvm.so.
# We strip out the ones we don't want with chrpath at install time.
%cmake3 -DCMAKE_INSTALL_PREFIX:PATH=%{_libdir}/%{name} \
 -DCMAKE_SHARED_LINKER_FLAGS:STRING="$LDFLAGS" \
 -DCMAKE_CXX_FLAGS_RELEASE:STRING="$CXXFLAGS" \
 -DCMAKE_C_FLAGS_RELEASE:STRING="$CFLAGS" \
 -DCMAKE_SKIP_INSTALL_RPATH:BOOL=NO \
 -DCMAKE_SKIP_RPATH:BOOL=NO \
 -DCMAKE_VERBOSE_MAKEFILE:BOOL=YES \
 -DGENERATE_ARITH:BOOL=YES \
 -DBUILD_SHARED_LIBS:BOOL=YES \
 -DBUILD:STRING=$BUILD ..
%make_build
make doc
rm doc/ampl.github.io/models/*/.depend
popd

%install
mkdir -p %{buildroot}%{_modulesdir}
sed 's#@BINDIR@#'%{_libdir}/%{name}'#g;' < %{SOURCE1} > \
    %{buildroot}%{_modulesdir}/%{name}-%{_arch}

mkdir -p %{buildroot}%{_libdir}/%{name}/bin/lib
mkdir -p %{buildroot}%{_includedir}/asl
cp -a include %{buildroot}%{_prefix}
install -pm 644 src/asl/*.h %{buildroot}%{_includedir}/asl
install -pm 644 src/asl/solvers/*.h build/src/asl/*.h %{buildroot}%{_includedir}/asl

# Required by coin-or-Couenne
install -pm 644 src/asl/solvers/{opcode,r_opn}.hd %{buildroot}%{_includedir}/asl

%if 0%{?with_jacop}
jacopver=$(sed -n 's,^    <version>\(.*\)</version>,\1,p' %{_mavenpomdir}/jacop/jacop.pom)
install -pm 644 build/bin/ampljacop.jar %{buildroot}%{_libdir}/%{name}/bin
install -pm 755 build/bin/jacop %{buildroot}%{_libdir}/%{name}/bin
ln -s %{_javadir}/jacop/jacop.jar %{buildroot}%{_libdir}/%{name}/bin/lib/jacop-$jacopver.jar
install -pm 755 build/bin/libampljacop.so %{buildroot}%{_libdir}/%{name}/bin
%endif
install -pm 755 build/bin/amplgsl.dll %{buildroot}%{_libdir}/%{name}/bin
install -pm 755 build/bin/ampltabl.dll %{buildroot}%{_libdir}/%{name}/bin
install -pm 755 build/bin/arithchk %{buildroot}%{_libdir}/%{name}/bin
install -pm 755 build/bin/cp.dll %{buildroot}%{_libdir}/%{name}/bin
install -pm 755 build/bin/fullbit.dll %{buildroot}%{_libdir}/%{name}/bin
%if 0%{?with_gecode}
install -pm 755 build/bin/gecode %{buildroot}%{_libdir}/%{name}/bin
install -pm 755 build/bin/libamplgecode.so %{buildroot}%{_libdir}/%{name}/bin
%endif
install -pm 755 build/bin/gen-expr-info %{buildroot}%{_libdir}/%{name}/bin
install -pm 755 build/bin/gjh %{buildroot}%{_libdir}/%{name}/bin
install -pm 755 build/bin/gsl-info %{buildroot}%{_libdir}/%{name}/bin
install -pm 755 build/bin/libamplsmpswriter.so %{buildroot}%{_libdir}/%{name}/bin
install -pm 755 build/bin/simpbit.dll %{buildroot}%{_libdir}/%{name}/bin
install -pm 755 build/bin/smpswriter %{buildroot}%{_libdir}/%{name}/bin
install -pm 755 build/bin/tableproxy%{__isa_bits} %{buildroot}%{_libdir}/%{name}/bin

## Fix symbolic links
install -pm 755 build/bin/libasl.so* %{buildroot}%{_libdir}
ln -sf libasl.so.%{version} %{buildroot}%{_libdir}/libasl.so.%{majver}
ln -sf libasl.so.%{majver} %{buildroot}%{_libdir}/libasl.so

install -pm 755 build/bin/libmp.so* %{buildroot}%{_libdir}
ln -sf libmp.so.%{version} %{buildroot}%{_libdir}/libmp.so.%{majver}
ln -sf libmp.so.%{majver} %{buildroot}%{_libdir}/libmp.so

chrpath --delete %{buildroot}%{_libdir}/libasl.so.%{version}
chrpath --delete %{buildroot}%{_libdir}/%{name}/bin/amplgsl.dll
chrpath --delete %{buildroot}%{_libdir}/%{name}/bin/ampltabl.dll
chrpath --delete %{buildroot}%{_libdir}/%{name}/bin/arithchk
chrpath --delete %{buildroot}%{_libdir}/%{name}/bin/cp.dll
chrpath --delete %{buildroot}%{_libdir}/%{name}/bin/fullbit.dll
%if 0%{?with_gecode}
chrpath --delete %{buildroot}%{_libdir}/%{name}/bin/gecode
chrpath --delete %{buildroot}%{_libdir}/%{name}/bin/libamplgecode.so
%endif
chrpath --delete %{buildroot}%{_libdir}/%{name}/bin/gen-expr-info
chrpath --delete %{buildroot}%{_libdir}/%{name}/bin/gjh
chrpath --delete %{buildroot}%{_libdir}/%{name}/bin/gsl-info
%if 0%{?with_jacop}
rpath=$(dirname $(find %{_jvmdir}/jre/lib -name libjvm.so))
chrpath --replace $rpath %{buildroot}%{_libdir}/%{name}/bin/jacop
chrpath --delete %{buildroot}%{_libdir}/%{name}/bin/libampljacop.so
%endif
chrpath --delete %{buildroot}%{_libdir}/%{name}/bin/libamplsmpswriter.so
chrpath --delete %{buildroot}%{_libdir}/%{name}/bin/simpbit.dll
chrpath --delete %{buildroot}%{_libdir}/%{name}/bin/smpswriter
chrpath --delete %{buildroot}%{_libdir}/%{name}/bin/tableproxy%{__isa_bits}
##

%check
pushd build
# Some of the tests use the SAME FILENAME to store temporary results, so
# running the tests in parallel leads to intermittent test failures, generally
# in either os-test or solver-test.  Do not pass the parallel flags to ctest.
ctest --force-new-ctest-process -j1
popd

%ldconfig_scriptlets

%files
%doc README.rst
%license LICENSE.rst
%dir %{_libdir}/%{name}
%{_libdir}/%{name}/bin/
%{_libdir}/libasl.so.3*
%{_libdir}/libmp.so.3*
%{_modulesdir}/%{name}-%{_arch}

%files devel
%{_libdir}/libasl.so
%{_libdir}/libmp.so
%{_includedir}/asl
%{_includedir}/mp

%files doc
%license LICENSE.rst
%doc build/doc/ampl.github.io/*

%changelog
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

