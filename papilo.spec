# Architectures that have libquadmath
%ifarch x86_64 ppc64le
%global quadmath 1
%else
%global quadmath 0
%endif

Name:           papilo
Version:        2.2.0
Release:        %autorelease
Summary:        Parallel presolve for integer and linear optimization

# LGPL-3.0-or-later: the project as a whole
# BSL-1.0: src/papilo/misc/extended_euclidean.hpp
# Zlib: the header-only pdqsort project
# MIT: the bundled fmt project
License:        LGPL-3.0-or-later AND BSL-1.0 AND Zlib AND MIT
URL:            https://www.scipopt.org/
VCS:            https://github.com/scipopt/papilo/
Source0:        %{vcs}/archive/v%{version}/%{name}-%{version}.tar.gz
# Unbundle catch, LUSOL, pdqsort, and ska
Patch0:         %{name}-unbundle.patch
# Build a shared library instead of a static library
Patch1:         %{name}-shared.patch
# The list of tests in CMakeLists.txt doesn't match the actual tests
Patch2:         %{name}-test.patch
# Avoid out-of-bounds vector access
Patch3:         %{name}-vector-bounds.patch

# See https://fedoraproject.org/wiki/Changes/EncourageI686LeafRemoval
ExcludeArch:    %{ix86}

BuildRequires:  boost-devel
BuildRequires:  cmake
BuildRequires:  cmake(catch2)
BuildRequires:  cmake(tbb)
BuildRequires:  gcc-c++
BuildRequires:  help2man
%if %{quadmath}
BuildRequires:  libquadmath-devel
%endif
BuildRequires:  lusol-devel
BuildRequires:  pdqsort-static
BuildRequires:  pkgconfig(gmp)

Requires:       libpapilo%{?_isa} = %{version}-%{release}

# The bundled version of fmt is incompatible with version 10 in Rawhide.
Provides:       bundled(fmt) = 6.1.2

%global _desc %{expand:
PaPILO provides parallel presolve routines for (mixed integer) linear
programming problems.  The routines are implemented using templates
which allows switching to higher precision or rational arithmetic using
the boost multiprecision package.}

%description %_desc

%package     -n libpapilo
Summary:        Library interface to PaPILO

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
  -n 'check for duplicate optimization problem instances' ./duplicates > \
  %{buildroot}%{_mandir}/man1/duplicates.1
help2man -N -h '' --version-string %{version} \
  -n 'parallel presolve for integer and linear optimization' ./papilo > \
  %{buildroot}%{_mandir}/man1/papilo.1
cd -

# Fix up the man pages a little
sed -e 's,\./check_\(duplicates\),\1,' \
    -e '/^\\&/i.TP' \
    -i %{buildroot}%{_mandir}/man1/duplicates.1
sed -i 's,\./\(papilo\),\1,' %{buildroot}%{_mandir}/man1/papilo.1

%check
%ctest

%files
%doc CHANGELOG README.md parameters.txt
%{_bindir}/duplicates
%{_bindir}/papilo
%{_mandir}/man1/duplicates.1*
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
