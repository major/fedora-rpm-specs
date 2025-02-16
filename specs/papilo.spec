# Architectures that have libquadmath
%ifarch x86_64 ppc64le
%global quadmath 1
%else
%global quadmath 0
%endif

# The papilo binary depends on several solvers that transitively depend on the
# papilo library.  In a bootstrap situation, first build the binary without
# solver support, build the solvers, then do a non-bootstrap build.
%bcond bootstrap 0

%global giturl  https://github.com/scipopt/papilo/

Name:           papilo
Version:        2.4.1
Release:        %autorelease
Summary:        Parallel presolve for integer and linear optimization

# LGPL-3.0-or-later: the project as a whole
# BSL-1.0: src/papilo/misc/extended_euclidean.hpp
# Zlib: the header-only pdqsort project
# MIT: the bundled fmt project
License:        LGPL-3.0-or-later AND BSL-1.0 AND Zlib AND MIT
URL:            https://www.scipopt.org/
VCS:            git:%{giturl}.git
Source:         %{giturl}/archive/v%{version}/%{name}-%{version}.tar.gz
# Unbundle catch, LUSOL, pdqsort, and ska
Patch:          %{name}-unbundle.patch
# Build a shared library instead of a static library
Patch:          %{name}-shared.patch
# Avoid out-of-bounds vector access
# https://github.com/scipopt/papilo/pull/48
Patch:          %{name}-vector-bounds.patch

# See https://fedoraproject.org/wiki/Changes/EncourageI686LeafRemoval
ExcludeArch:    %{ix86}

BuildRequires:  boost-devel
BuildRequires:  catch-devel
BuildRequires:  cmake
BuildRequires:  cmake(tbb)
BuildRequires:  gcc-c++
BuildRequires:  help2man
BuildRequires:  libatomic
%if %{quadmath}
BuildRequires:  libquadmath-devel
%endif
BuildRequires:  lusol-devel
BuildRequires:  pdqsort-static
BuildRequires:  pkgconfig(gmp)

%if %{without bootstrap}
# Solver support
BuildRequires:  cmake(scip)
BuildRequires:  cmake(soplex)
%endif

Requires:       libpapilo%{?_isa} = %{version}-%{release}

%global _desc %{expand:
PaPILO provides parallel presolve routines for (mixed integer) linear
programming problems.  The routines are implemented using templates
which allows switching to higher precision or rational arithmetic using
the boost multiprecision package.}

%description %_desc

%package     -n libpapilo
Summary:        Library interface to PaPILO

# The bundled version of fmt is incompatible with version 10 in Rawhide.
Provides:       bundled(fmt) = 7.1.3

%description -n libpapilo %_desc

This package provides a library interface to the PaPILO functionality.

%package     -n libpapilo-devel
Summary:        Headers and library links for libpapilo
Requires:       libpapilo%{?_isa} = %{version}-%{release}
Requires:       boost-devel%{?_isa}
Requires:       lusol-devel%{?_isa}
Requires:       pdqsort-static
Requires:       tbb-devel%{?_isa}

%description -n libpapilo-devel %_desc

This package contains headers and library links to develop applications
that use libpapilo.

%prep
%autosetup -p1

%conf
# Ensure none of the bundled code but fmt can be used
rm -fr src/papilo/external/{catch,lusol,pdqsort,ska}

# Fix installation directories
if [ '%{_lib}' != 'lib' ]; then
    sed -i 's,\(DESTINATION \)lib,\1%{_lib},g' CMakeLists.txt
fi

%build
%cmake -DQUADMATH:BOOL=%{?quadmath:ON}%{!?quadmath:OFF}
%cmake_build

%install
%cmake_install

# Generate man pages
mkdir -p %{buildroot}%{_mandir}/man1
export LD_LIBRARY_PATH=$PWD/%{_vpath_builddir}
cd %{_vpath_builddir}/bin
help2man -N -h '' --version-string %{version} \
  -n 'parallel presolve for integer and linear optimization' ./papilo > \
  %{buildroot}%{_mandir}/man1/papilo.1
cd -

# Fix up the man page a little
sed -i 's,\./\(papilo\),\1,' %{buildroot}%{_mandir}/man1/papilo.1

%check
# Temporarily skip a test that is broken in the 2.3.1 release
%ctest -E 'q-solve-rgn\.mps-default\.set'

%files
%doc CHANGELOG README.md parameters.txt
%{_bindir}/papilo
%{_mandir}/man1/papilo.1*

%files -n libpapilo
%license COPYING COPYING.LESSER
%{_libdir}/libpapilo-core.so.0*

%files -n libpapilo-devel
%{_includedir}/papilo/
%{_libdir}/cmake/papilo/
%{_libdir}/libpapilo-core.so

%changelog
%autochangelog
