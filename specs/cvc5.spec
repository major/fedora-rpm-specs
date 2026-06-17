# CVC5 wants a modified glpk (glpk-cut-log), unavailable in Fedora.  Therefore,
# we currently build without glpk support.

# Whether to run tests
%bcond ctest 1

# The cvc5_pythonic_api project needs cvc5 to build, and cvc5 needs
# cvc5_pythonic_api to build.  See cmake/FindCVC5PythonicAPI.cmake for the git
# commit needed by this version of cvc5.
%global pcommit cdcac7cb2da79d922fc44628c1c3c5f60c2eeec4

%global giturl  https://github.com/cvc5/cvc5

Name:           cvc5
Version:        1.3.4
Release:        %autorelease
Summary:        Automatic theorem prover for SMT problems

# BSD-3-Clause: the project as a whole, including cvc5_pythonic_api
# MIT: the bundled version of minisat2 in src/prop/minisat, and the
#      cvc5_pythonic_api code derived from Z3
License:        BSD-3-Clause AND MIT
URL:            https://cvc5.github.io/
VCS:            git:%{giturl}.git
Source0:        %{giturl}/archive/%{name}-%{version}.tar.gz
Source1:        https://github.com/cvc5/cvc5_pythonic_api/archive/%{pcommit}/%{pcommit}.zip
# Do not override Fedora flags
Patch:          %{name}-flags.patch
# Skip tests that require huge amounts of memory
# Patch courtesy of Scott Talbert
Patch:          %{name}-skip-himem-tests.patch
# Adapt to cocoalib 0.99850
Patch:          %{name}-cocoalib.patch
# Adapt to cadical 2.2.0
Patch:          %{name}-cadical.patch

# See https://fedoraproject.org/wiki/Changes/EncourageI686LeafRemoval
ExcludeArch:    %{ix86}
BuildSystem:    cmake
BuildOption(conf): --debug-find
BuildOption(conf): -DBUILD_BINDINGS_JAVA:BOOL=ON
BuildOption(conf): -DBUILD_BINDINGS_PYTHON:BOOL=ON
BuildOption(conf): -DBUILD_DOCS:BOOL=OFF
BuildOption(conf): -DBUILD_SHARED_LIBS:BOOL=ON
BuildOption(conf): -DENABLE_GPL:BOOL=ON
BuildOption(conf): -DENABLE_IPO:BOOL=ON
BuildOption(conf): -DONLY_PYTHON_EXT_SRC:BOOL=ON
BuildOption(conf): -DSKIP_SET_RPATH:BOOL=ON
BuildOption(conf): -DUSE_COCOA:BOOL=ON
BuildOption(conf): -DUSE_CRYPTOMINISAT:BOOL=ON
BuildOption(conf): -DUSE_DEFAULT_LINKER:BOOL=ON
BuildOption(conf): -DUSE_EDITLINE:BOOL=ON
BuildOption(conf): -DUSE_KISSAT:BOOL=ON
BuildOption(conf): -DUSE_POLY:BOOL=ON

BuildRequires:  cadical-devel
BuildRequires:  chrpath
BuildRequires:  cmake(cryptominisat5)
BuildRequires:  cocoalib-devel
BuildRequires:  gcc-c++
BuildRequires:  git-core
BuildRequires:  java-25-devel
BuildRequires:  javapackages-tools
BuildRequires:  kissat-devel
BuildRequires:  libpoly-devel
BuildRequires:  pkgconfig(gmp)
BuildRequires:  pkgconfig(libedit)
BuildRequires:  pkgconfig(sqlite3)
BuildRequires:  procps-ng
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
BuildRequires:  %{py3_dist cython}
BuildRequires:  %{py3_dist packaging}
BuildRequires:  %{py3_dist pexpect}
BuildRequires:  %{py3_dist pip}
BuildRequires:  %{py3_dist pyparsing}
BuildRequires:  %{py3_dist setuptools}
BuildRequires:  %{py3_dist wheel}
BuildRequires:  symfpu-devel

# Needed for some of the tests; we do not currently execute those tests
#BuildRequires:  ethos
#BuildRequires:  lfsc-devel

Requires:       %{name}-libs%{?_isa} = %{version}-%{release}

Suggests:       ethos

# Minisat has been altered for better integration with CVC5
# See src/prop/minisat/CVC4-README
Provides:       bundled(minisat2) = 2.2.0

%description
CVC5 is a tool for determining the satisfiability of a first order formula
modulo a first order theory (or a combination of such theories).  It is the
fifth in the Cooperating Validity Checker family of tools (CVC, CVC Lite,
CVC3, CVC4) but does not directly incorporate code from any previous version
prior to CVC4.

CVC5 is intended to be an open and extensible SMT engine.  It can be used as a
stand-alone tool or as a library.  It has been designed to increase the
performance and reduce the memory overhead of its predecessors.

%package        devel
Summary:        Headers and other files for developing with %{name}
Requires:       %{name}-libs%{?_isa} = %{version}-%{release}
Requires:       gmp-devel%{?_isa}
Requires:       symfpu-devel

%description    devel
Header files and library links for developing applications that use %{name}.

%package        libs
Summary:        Library containing an automatic theorem prover for SMT problems

%description    libs
Library containing the core of the %{name} automatic theorem prover for
SMT problems.

%package        java
Summary:        Java interface to %{name}
Requires:       %{name}-libs%{?_isa} = %{version}-%{release}
Requires:       java-25-headless
Requires:       javapackages-tools

%description    java
Java interface to %{name}.

%package     -n python3-cvc5
Summary:        Python 3 interface to %{name}
Requires:       %{name}-libs%{?_isa} = %{version}-%{release}

%description -n python3-cvc5
Python 3 interface to %{name}.

%prep
%autosetup -n %{name}-%{name}-%{version} -p1

mkdir -p %{_vpath_builddir}/deps/src/CVC5PythonicAPI
cp -p %{SOURCE1} %{_vpath_builddir}/deps/src

# Adapt to the way kissat is packaged for Fedora
sed -i 's,#include <kissat/kissat\.h>,#include <kissat.h>,' src/prop/kissat.h
sed -i 's,kissat/kissat\.h,kissat.h,' cmake/FindKissat.cmake

# Fix the path to ethos
sed -e 's,\(--ethos-binary \).*,\1%{_bindir}/ethos,' \
    -i test/regress/cli/CMakeLists.txt

# Without this, the python interface has version 0.0.0
sed -i 's/CVC5_WHEEL_VERSION/CVC5_VERSION/' src/api/python/__init__.py.in

%conf -p
export BUILDFLAGS='-DABC_USE_STDINT_H -I%{_jvmdir}/java/include -I%{_jvmdir}/java/include/linux -I%{_includedir}/abc -I%{_includedir}/cryptominisat5'
export CFLAGS="%{build_cflags} $BUILDFLAGS"
export CXXFLAGS="%{build_cxxflags} $BUILDFLAGS"

%build -a
# Build the python interface the Fedora way
cd %{_vpath_builddir}/src/api/python
%pyproject_wheel
cd -

%install -a
# Link the JNI interface to where Fedora mandates it should go
mkdir -p %{buildroot}%{_jnidir}/%{name}
ln -s ../../%{_lib}/libcvc5jni.so %{buildroot}%{_jnidir}/%{name}

# Install the python interface the Fedora way
cd %{_vpath_builddir}/src/api/python
%pyproject_install
cd -

# FIXME: What is causing an rpath to be added in the first place?
chrpath -d %{buildroot}%{python3_sitearch}/cvc5/*.so

%check -p
%if %{with ctest}
# Increase the test timeout for slow builders
export TEST_TIMEOUT=2000

# The tests break without this
cp -p %{_vpath_builddir}/src/api/python/build/lib.*/cvc5/cvc5_python_base.*.so \
      %{_vpath_builddir}/src/api/python/cvc5

%cmake_build -t build-tests
%endif

%files
%doc AUTHORS NEWS.md README.md THANKS
%{_bindir}/%{name}

%files libs
%license COPYING
%{_libdir}/libcvc5.so.1{,.*}
%{_libdir}/libcvc5parser.so.1{,.*}

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
