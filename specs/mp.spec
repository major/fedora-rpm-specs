%global with_jacop     0
%global with_gecode    0

%if 0%{?fedora}
%global with_highs     1
%global with_scip      1
%else
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
%global commit      d66148218b3557708f7f2271c43d30ac6ee1935c
%global date        20260210
%global forgeurl    https://github.com/ampl/mp

Name: mp
Version: %{date}
Summary: An open-source library for mathematical programming

%forgemeta

# SMLNJ: the project as a whole
# BSD-2-Clause: src/{format,rstparser}.cc,
#               include/mp/{format,rstparser,safeint}.h
# GPL-2.0-or-later: src/asl/mkstemps.c (not included in the binary RPM)
# GPL-3.0-or-later: src/gsl/default.c (not included in the binary RPM)
License: SMLNJ AND BSD-2-Clause
Release: %autorelease
URL: https://mp.ampl.com/
VCS: git:%{forgeurl}.git
# Downloaded from https://github.com/ampl/mp/archive/%%commit.tar.gz
Source0: %{forgesource}
# Unbundle asl
Patch0:  %{name}-unbundle-asl.patch
# https://bugzilla.redhat.com/show_bug.cgi?id=1333344
Patch1:  %{name}-3.1.0-jni.patch
# Adapt to python 3
Patch2:  %{name}-python3.patch
# Fix for CMake-4.0
Patch8: %{name}-rhbz2380479.patch

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
BuildRequires: java-25-devel
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
%{_libdir}/libaslmp.so.4
%{_libdir}/libmp.so.4
%{_libdir}/libaslmp.so.4.0.3
%{_libdir}/libmp.so.4.0.3
%{_libexecdir}/mp/

%files devel
%{_libdir}/libaslmp.so
%{_libdir}/libmp.so
%{_includedir}/asl
%{_includedir}/mp

%changelog
%autochangelog
