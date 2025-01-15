# NOTE on SAT implementations.
# Upstream wants MathSat, which is nonfree and closed source.  We can do
# without the solving capability, or we can look for an alternative:
# - glpk: either solves for floating point numbers or integers, but we need to
#   solve for rational solutions.  Looks infeasible.
# - CVC4: has a rational solver, unknown whether it accepts constraints
# - linbox: has a rational solver, unknown whether it accepts constraints
# - one of the coin-or-* packages might provide a suitable solver

%global baseurl https://cocoa.altervista.org/cocoalib

Name:           cocoalib
Version:        0.99850
Release:        %autorelease
Summary:        C++ library for computations in commutative algebra

License:        GPL-3.0-or-later
URL:            %{baseurl}/index.shtml
VCS:            git:https://github.com/cocoa-official/CoCoALib.git
Source:         %{baseurl}/tgz/CoCoALib-%{version}.tgz
# Build a shared library instead of a static library
Patch:          %{name}-shared.patch
# Fix error handling in Qsolve
Patch:          %{name}-ffelem.patch
# Fix out of bounds vector accesses
Patch:          %{name}-vec.patch
# Avoid using a variable uninitialized
Patch:          %{name}-uninit.patch
# CVC5 patch to enable tracing
Patch:          %{name}-cvc5.patch

# See https://fedoraproject.org/wiki/Changes/EncourageI686LeafRemoval
ExcludeArch:    %{ix86}

BuildRequires:  boost-devel
BuildRequires:  cddlib-devel
BuildRequires:  gcc-c++
BuildRequires:  gmp-devel
BuildRequires:  libfrobby-devel
BuildRequires:  libgfan-devel
BuildRequires:  make
BuildRequires:  pkgconfig(flexiblas)
BuildRequires:  pkgconfig(gsl)
BuildRequires:  pkgconfig(readline)
BuildRequires:  tex(latex)
BuildRequires:  tex(ulem.sty)

%description
The CoCoA C++ library offers functions to perform calculations in
Computational Commutative Algebra, and some other related areas.  The
library is designed to be pleasant to use while offering good run-time
performance.

%package devel
Summary:        Headers and library links for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       boost-devel%{?_isa}
Requires:       gmp-devel%{?_isa}
Requires:       gsl-devel%{?_isa}
Requires:       libgfan-devel%{?_isa}

%description devel
Headers and library links for developing applications that use %{name}.

%package doc
# The content is GFDL-1.2-no-invariants-only.  The remaining licenses cover the
# various fonts embedded in PDFs.
# CM: Knuth-CTAN
License:        GFDL-1.2-no-invariants-only AND Knuth-CTAN
Summary:        Documentation for %{name}
BuildArch:      noarch

%description doc
Documentation for %{name}.

%prep
%autosetup -p0 -n CoCoALib-%{version}

%conf
# Use FlexiBLAS instead of the reference lapack/blas implementation.
# Do not throw away our choice of compiler flags.
# Fix the location of the cddlib headers.
sed -e 's,-lgslcblas  -llapack,-lflexiblas,' \
    -e 's/ -Wall  -pedantic/ $CXXFLAGS/' \
    -e 's,\(CDD_INC_DIR=\)".*",\1"%{_includedir}/cddlib",' \
    -i configure

# Do not suppress compiler command lines
sed -i 's/\$(MAKE) -s/\$(MAKE)/' Makefile doc/Makefile src/Makefile \
    src/AlgebraicCore/Makefile src/AlgebraicCore/TmpFactorDir/Makefile

%build
# Use Fedora's linker flags
sed -i 's|@RPM_LD_FLAGS@|%{build_ldflags}|' src/AlgebraicCore/Makefile

# This is NOT an autoconf-generated configure script!
./configure --prefix=%{_prefix} --only-cocoalib --threadsafe-hack \
  --with-cxxflags='%{build_cxxflags} -fPIC -I%{_includedir}/frobby -I%{_includedir}/gfanlib %{build_ldflags}' \
  --with-libcddgmp=%{_libdir}/libcddgmp.so \
  --with-libfrobby=%{_libdir}/libfrobby.so \
  --with-libgfan=%{_libdir}/libgfan.so \
  --with-libgsl=%{_libdir}/libgsl.so

%make_build library
%make_build doc

%install
# The Makefile ignores DESTDIR.  Install by hand.

# Install the library
mkdir -p %{buildroot}%{_libdir}
cp -p src/AlgebraicCore/libcocoa.so.0.0.0 %{buildroot}%{_libdir}
ln -s libcocoa.so.0.0.0 %{buildroot}%{_libdir}/libcocoa.so.0
ln -s libcocoa.so.0 %{buildroot}%{_libdir}/libcocoa.so

# Install the headers
mkdir -p %{buildroot}%{_includedir}
cp -a include/CoCoA %{buildroot}%{_includedir}
rm -f %{buildroot}%{_includedir}/{MakeUnifiedHeader.sh,PREPROCESSOR_DEFNS.H-old}

# Remove files from the doc directories that we want to include in %%files
rm -f doc/CoCoALib-tasks/{HTMLTasks,HTMLTasks.C,Makefile,tasks.xml}
rm -f examples/CopyInfo
chmod a-x examples/*.sh

%check
export LD_LIBRARY_PATH=$PWD/lib
make check

%files
%license COPYRIGHT-full-text
%doc README
%{_libdir}/libcocoa.so.0*

%files devel
%{_includedir}/CoCoA
%{_libdir}/libcocoa.so

%files doc
%license doc/COPYING
%doc doc/*.html
%doc doc/*.pdf
%doc doc/CoCoALib-tasks
%doc doc/html
%doc examples

%changelog
%autochangelog
