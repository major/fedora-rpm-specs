# Architectures that have libquadmath
%ifarch %{ix86} x86_64 ppc64le
%global quadmath 1
%else
%global quadmath 0
%endif

Name:           soplex
Version:        7.0.0
Release:        %autorelease
Summary:        Sequential object-oriented simplex

%global upver   %(sed 's/\\.//g' <<< %{version})

# Apache-2.0: the project as a whole
# LGPL-2.1-or-later: src/soplex/gzstream.{cpp,h}
# MIT: the bundled fmt project
License:        Apache-2.0 AND LGPL-2.1-or-later AND MIT
URL:            https://soplex.zib.de/
VCS:            https://github.com/scipopt/soplex
Source0:        %{vcs}/archive/release-%{upver}.tar.gz
# Elevate the shared library from second-class status to first-class
Patch0:         %{name}-shared.patch
# Convert a python script from python 2 to 3
# https://github.com/scipopt/soplex/pull/32
Patch1:         %{name}-python3.patch
# Fix an error due to nondefinition declarations
# https://github.com/scipopt/soplex/pull/23
Patch2:         %{name}-nondefinition.patch
# Fix a segfault due to dereferencing an uninitialized pointer
# https://github.com/scipopt/soplex/pull/37
Patch3:         %{name}-segfault.patch

# See https://fedoraproject.org/wiki/Changes/EncourageI686LeafRemoval
ExcludeArch:    %{ix86}

BuildRequires:  boost-devel
BuildRequires:  cmake
BuildRequires:  cmake(papilo)
BuildRequires:  cmake(tbb)
BuildRequires:  gcc-c++
BuildRequires:  gcc-gfortran
%if %{quadmath}
BuildRequires:  libquadmath-devel
%endif
BuildRequires:  ninja-build
BuildRequires:  pkgconfig(gmp)
BuildRequires:  pkgconfig(mpfr)
BuildRequires:  pkgconfig(zlib)

# Documentation
BuildRequires:  doxygen
BuildRequires:  php-cli
BuildRequires:  python3

Requires:       libsoplex%{?_isa} = %{version}-%{release}

%global _desc %{expand:
SoPlex is an optimization package for solving linear programming
problems (LPs) based on an advanced implementation of the primal and
dual revised simplex algorithm.  It provides special support for the
exact solution of LPs with rational input data.  It can be used as a
standalone solver reading MPS or LP format files via a command line
interface as well as embedded into other programs via a C++ class
library.  The main features of SoPlex are:

- presolving, scaling, exploitation of sparsity, hot-starting from any
  regular basis,
- column- and row-oriented form of the simplex algorithm,
- an object-oriented software design written in C++,
- a compile-time option to use 80bit extended ("quad") precision for
  numerically difficult LPs,
- an LP iterative refinement procedure to compute high-precision
  solution, and
- routines for an exact rational LU factorization and continued fraction
  approximations in order to compute exact solutions.

SoPlex has been used in numerous research and industry projects and is
the standard LP solver linked to the mixed-integer nonlinear programming
and constraint integer programming solver SCIP.}

%description %_desc

This package contains a command-line tool to access SoPlex
functionality.

%package -n     libsoplex
Summary:        Library for sequential object-oriented simplex

# The bundled version of fmt is incompatible with version 10 in Rawhide.
Provides:       bundled(fmt) = 6.1.2

%description -n libsoplex %_desc

This package contains a library interface to SoPlex functionality.

%package -n     libsoplex-devel
Summary:        Headers and library links for libsoplex
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       libsoplex%{?_isa} = %{version}-%{release}
Requires:       boost-devel%{?_isa}
Requires:       gmp-devel%{?_isa}
Requires:       libpapilo-devel%{?_isa}
%if %{quadmath}
Requires:       libquadmath-devel%{?_isa}
%endif
Requires:       mpfr-devel%{?_isa}
Requires:       zlib-devel%{?_isa}

%description -n libsoplex-devel
This package contains headers and library links for developing
applications that use libsoplex.

%package -n     libsoplex-doc
# The content is licensed with Apache-2.0.  The other licenses are due to files
# added by doxygen.  Most such files are licensed with GPL-1.0-or-later, but
# the JavaScript files are licensed with MIT.
License:        Apache-2.0 AND GPL-1.0-or-later AND MIT
Summary:        API documentation for libsoplex
BuildArch:      noarch

%description -n libsoplex-doc
API documentation for libsoplex.

%prep
%autosetup -n %{name}-release-%{upver} -p1

# We want to know about overflow errors, as the compiler can do surprising
# things if we don't fix them!
sed -i 's/ -Wno-strict-overflow//' CMakeLists.txt Makefile

# Turn off HTML timestamps for repeatable builds
sed -i '/HTML_TIMESTAMP/s/YES/NO/' doc/soplex.dxy
sed -i 's/ on \$date//' doc/soplexfooter.html

%build
%cmake \
  -DMPFR:BOOL=ON \
  -DPAPILO:BOOL=ON \
  -DQUADMATH:BOOL=%{?quadmath:ON}%{!?quadmath:OFF}
%cmake_build

# Build documentation
cd doc
../%{_vpath_builddir}/bin/soplex --saveset=parameters.set
cd inc
python3 parser.py --linkext html
php localfaq.php > faq.inc
cd ..
doxygen soplex.dxy
cd ..

%install
%cmake_install

%check
export LD_LIBRARY_PATH=%{buildroot}%{_libdir}
%ctest

%files
%{_bindir}/soplex

%files -n libsoplex
%doc CHANGELOG README.md
%license LICENSE
%{_libdir}/libsoplex.so.7*

%files -n libsoplex-devel
%{_includedir}/soplex*
%{_libdir}/libsoplex.so
%{_libdir}/cmake/soplex/

%files -n libsoplex-doc
%doc doc/html
%license LICENSE

%changelog
%autochangelog
