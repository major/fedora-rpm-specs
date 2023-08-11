# CVC5 wants a modified glpk (glpk-cut-log), unavailable in Fedora.  Therefore,
# we currently build without glpk support.

# The cvc5_pythonic_api project needs cvc5 to build, and cvc5 needs
# cvc5_pythonic_api to build.  See cmake/FindCVC5PythonicAPI.cmake for the git
# commit needed by this version of cvc5.
%global pcommit a04093e60036b83681c6f2cf5cca42bb631b6ce4

Name:           cvc5
Version:        1.0.5
Release:        %autorelease
Summary:        Automatic theorem prover for SMT problems

# BSD-3-Clause: the project as a whole, including cvc5_pythonic_api
# MIT: the bundled version of minisat2 in src/prop/minisat, and the
#      cvc5_pythonic_api code derived from Z3
License:        BSD-3-Clause AND MIT
URL:            https://cvc5.github.io/
Source0:        https://github.com/cvc5/cvc5/archive/%{name}-%{version}.tar.gz
Source1:        https://github.com/cvc5/cvc5_pythonic_api/archive/%{pcommit}/%{pcommit}.zip
# Do not override Fedora flags
Patch0:         %{name}-flags.patch
# Adapt to the way ANTLR3 is packaged in Fedora
Patch1:         %{name}-antlr3.patch
# Just use the default linker specified by the distro. ld.gold was the
# new kid on the block a while ago, primarily offering higher link
# speeds. But it has aged, and has less features than ld.bfd. Let's
# use ld.bfd so that package notes work without workarounds.
Patch2:         %{name}-do-not-use-gold.patch
# Do not add rpaths to libraries and executables
Patch3:         %{name}-rpath.patch
# Use tomllib instead of the deprecated toml package
# https://github.com/cvc5/cvc5/pull/9913
Patch4:         %{name}-toml.patch
# Skip tests that require huge amounts of memory
# Patch courtesy of Scott Talbert
Patch5:         %{name}-skip-himem-tests.patch
# Fix out-of-bounds access to a vector
# https://github.com/cvc5/cvc5/pull/9921
Patch6:         %{name}-vec.patch

# ANTLR 3 is not available on i686
# See https://fedoraproject.org/wiki/Changes/Drop_i686_JDKs
ExclusiveArch:  %{java_arches}

BuildRequires:  antlr3-C-devel
BuildRequires:  antlr3-tool
BuildRequires:  cadical
BuildRequires:  cadical-devel
BuildRequires:  chrpath
BuildRequires:  cmake
BuildRequires:  cmake(cryptominisat5)
BuildRequires:  cocoalib-devel
BuildRequires:  drat2er-devel
BuildRequires:  drat-trim-devel
BuildRequires:  flex
BuildRequires:  gcc-c++
BuildRequires:  git-core
BuildRequires:  java-devel
BuildRequires:  javapackages-tools
BuildRequires:  kissat-devel
BuildRequires:  lfsc-devel
BuildRequires:  libfl-devel
BuildRequires:  libpoly-devel
BuildRequires:  pkgconfig(gmp)
BuildRequires:  pkgconfig(libedit)
BuildRequires:  pkgconfig(m4ri)
BuildRequires:  pkgconfig(sqlite3)
BuildRequires:  procps-ng
BuildRequires:  python3-devel
BuildRequires:  %{py3_dist cython}
BuildRequires:  %{py3_dist pyparsing}
BuildRequires:  %{py3_dist scikit-build}
BuildRequires:  %{py3_dist setuptools}
BuildRequires:  symfpu-devel
BuildRequires:  yosyshq-abc-devel

Requires:       %{name}-libs%{?_isa} = %{version}-%{release}

# Minisat has been altered for better integration with CVC5
# See src/prop/minisat/CVC4-README
Provides:       bundled(minisat2) = 2.2.0

# This can be removed when F42 reaches EOL
Obsoletes:      cvc4 < 1.9

%description
CVC5 is a tool for determining the satisfiability of a first order
formula modulo a first order theory (or a combination of such theories).
It is the fifth in the Cooperating Validity Checker family of tools
(CVC, CVC Lite, CVC3, CVC4) but does not directly incorporate code from
any previous version prior to CVC4.

CVC5 is intended to be an open and extensible SMT engine.  It can be
used as a stand-alone tool or as a library.  It has been designed to
increase the performance and reduce the memory overhead of its
predecessors.

%package        devel
Summary:        Headers and other files for developing with %{name}
Requires:       %{name}-libs%{?_isa} = %{version}-%{release}
Requires:       gmp-devel%{?_isa}
Requires:       symfpu-devel%{?_isa}

# This can be removed when F42 reaches EOL
Obsoletes:      cvc4-devel < 1.9

%description    devel
Header files and library links for developing applications that use %{name}.

%package        libs
Summary:        Library containing an automatic theorem prover for SMT problems

# This can be removed when F42 reaches EOL
Obsoletes:      cvc4-libs < 1.9

%description    libs
Library containing the core of the %{name} automatic theorem prover for
SMT problems.

%package        java
Summary:        Java interface to %{name}
Requires:       %{name}-libs%{?_isa} = %{version}-%{release}
Requires:       java-headless
Requires:       javapackages-tools

# This can be removed when F42 reaches EOL
Obsoletes:      cvc4-java < 1.9

%description    java
Java interface to %{name}.

%package     -n python3-cvc5
Summary:        Python 3 interface to %{name}
Requires:       %{name}-libs%{?_isa} = %{version}-%{release}

# This can be removed when F42 reaches EOL
Obsoletes:      cvc4-python3 < 1.9

%description -n python3-cvc5
Python 3 interface to %{name}.

%prep
%autosetup -n %{name}-%{name}-%{version} -p1
mkdir -p %{_vpath_builddir}/deps/src/CVC5PythonicAPI
cp -p %{SOURCE1} %{_vpath_builddir}/deps/src

# FIXME: cmake fails to find a version in the Fedora cryptominisat package
# cmake files, causing the version check to fail
sed -i 's/ \${CryptoMiniSat_FIND_VERSION}//' cmake/FindCryptoMiniSat.cmake

# The Fedora editline library does not need libbsd
sed -i 's/ bsd//' cmake/FindEditline.cmake

# Adapt to the way kissat is packaged for Fedora
sed -i 's,#include <kissat/kissat\.h>,#include <kissat.h>,' src/prop/kissat.h
sed -i 's,kissat/kissat\.h,kissat.h,' cmake/FindKissat.cmake

# The header file installation script does not know about DESTDIR
sed -i 's/\${CMAKE_INSTALL_PREFIX}/\\$ENV{DESTDIR}&/' src/CMakeLists.txt

# Build the Java interface so that JDK 1.8 can use it
sed -i 's/\${Java_JAVAC_EXECUTABLE}/& -source 1.8 -target 1.8/' \
  src/api/java/CMakeLists.txt

# Allow use of python 3.12
sed -i 's/3\.10\.999/3.12.999/' cmake/Helpers.cmake

%generate_buildrequires
ln -s . src/api/python/cvc5
ln -s . src/api/python/pythonic
cd src/api/python
sed -e 's/\${CVC5_VERSION}/%{version}/' \
    -e "s,\${CMAKE_CURRENT_BINARY_DIR},$PWD," \
    setup.py.in > setup.py
%pyproject_buildrequires
rm -fr cvc5 cvc5.egg-info pythonic setup.py

%build
export CFLAGS='%{build_cflags} -DABC_USE_STDINT_H -I%{_jvmdir}/java/include -I%{_jvmdir}/java/include/linux -I%{_includedir}/abc -I%{_includedir}/cryptominisat5'
export CXXFLAGS="$CFLAGS"
%cmake --debug-find \
  -DBUILD_BINDINGS_JAVA:BOOL=ON \
  -DBUILD_BINDINGS_PYTHON:BOOL=ON \
  -DBUILD_DOCS:BOOL=OFF \
  -DBUILD_SHARED_LIBS:BOOL=ON \
  -DENABLE_GPL:BOOL=ON \
  -DENABLE_IPO:BOOL=ON \
  -DUSE_COCOA:BOOL=ON \
  -DUSE_CRYPTOMINISAT:BOOL=ON \
  -DUSE_EDITLINE:BOOL=ON \
  -DUSE_KISSAT:BOOL=ON \
  -DUSE_POLY:BOOL=ON
%cmake_build

# Build the python interface the Fedora way
cd %{_vpath_builddir}/src/api/python
%pyproject_wheel
cd -

%install
%cmake_install

# Link the JNI interface to where Fedora mandates it should go
mkdir -p %{buildroot}%{_jnidir}/%{name}
ln -s ../../%{_lib}/libcvc5jni.so %{buildroot}%{_jnidir}/%{name}

# Install the python interface the Fedora way
cd %{_vpath_builddir}/src/api/python
%pyproject_install
cd -

# The python interface is incorrectly installed in the noarch directory
if [ "%{_lib}" != "lib" ]; then
  mv %{buildroot}%{_prefix}/lib/python* %{buildroot}%{_libdir}
fi

# FIXME: What is causing an rpath to be added in the first place?
chrpath -d %{buildroot}%{python3_sitearch}/cvc5/*.so

# FIXME: 2 tests fail on s390x
# - regress4/C880mul.miter.shuffled-as.sat03-348.smtv1.smt2
# - regress4/instance_1151.smtv1.smt2
%ifnarch s390x
%check
cd %{_vpath_builddir}/test/api
make
cd -
%ctest
%endif

%files
%doc AUTHORS NEWS.md README.md THANKS
%{_bindir}/%{name}

%files libs
%license COPYING
%{_libdir}/libcvc5.so.1
%{_libdir}/libcvc5parser.so.1

%files devel
%{_includedir}/%{name}/
%{_libdir}/libcvc5.so
%{_libdir}/libcvc5parser.so
%{_libdir}/cmake/%{name}/

%files java
%{_javadir}/cvc5.jar
%{_javadir}/cvc5-%{version}.jar
%{_jnidir}/%{name}/
%{_libdir}/libcvc5jni.so

%files -n python3-cvc5
%{python3_sitearch}/cvc5/
%{python3_sitearch}/cvc5-%{version}.dist-info/

%changelog
%autochangelog
