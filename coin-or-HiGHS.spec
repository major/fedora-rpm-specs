# NOTE: The C# and Fortran interfaces are not currently built.  If you need
# either interface, file a bug requesting it.

# The build runs git to get a commit, but we don't have a git checkout
%global commit 50670fd4c

Name:           coin-or-HiGHS
Version:        1.7.0
Release:        %autorelease
Summary:        Linear optimization software

License:        MIT
URL:            https://highs.dev/
VCS:            https://github.com/ERGO-Code/HiGHS
Source0:        %{vcs}/archive/v%{version}/HiGHS-%{version}.tar.gz
# Do not add rpaths to libraries and binaries
Patch0:         %{name}-rpath.patch
# Do not try to download pybind11
Patch1:         %{name}-pybind11.patch
# Check availability of the popcount instruction at runtime
Patch2:         %{name}-popcount.patch
# Fix out-of-bounds vector accesses
Patch3:         %{name}-vector.patch
# Update the examples to fix FTBFS
# https://github.com/ERGO-Code/HiGHS/pull/1680
Patch4:         %{name}-examples.patch

# See https://fedoraproject.org/wiki/Changes/EncourageI686LeafRemoval
ExcludeArch:    %{ix86}

BuildRequires:  cmake
BuildRequires:  cmake(catch2)
BuildRequires:  cmake(pybind11)
BuildRequires:  doctest-static
BuildRequires:  gcc-c++
BuildRequires:  ninja-build
BuildRequires:  pdqsort-static
BuildRequires:  pkgconfig(coindatanetlib)
BuildRequires:  pkgconfig(coindatasample)
BuildRequires:  pkgconfig(zlib)
BuildRequires:  python3-devel
BuildRequires:  zstr-static

# A bundled version of FilereaderLP is included, but it has been modified
# extensively from the upstream version:
# https://github.com/feldmeier/FilereaderLP/
Provides:       bundled(FilereaderLP)

%description
HiGHS is a high performance serial and parallel solver for large scale
sparse linear optimization problems of the form

    Minimize (1/2) x^TQx + c^Tx subject to L <= Ax <= U; l <= x <= u

where Q must be positive semi-definite and, if Q is zero, there may be a
requirement that some of the variables take integer values.  Thus HiGHS
can solve linear programming (LP) problems, convex quadratic programming
(QP) problems, and mixed integer programming (MIP) problems.  It is
mainly written in C++, but also has some C.

HiGHS has primal and dual revised simplex solvers, originally written by
Qi Huangfu and further developed by Julian Hall.  It also has an
interior point solver for LP written by Lukas Schork, an active set
solver for QP written by Michael Feldmeier, and a MIP solver written by
Leona Gottwald.  Other features have been added by Julian Hall and Ivet
Galabova, who manages the software engineering of HiGHS and interfaces
to C, C#, FORTRAN, Julia and Python.

Although HiGHS is freely available under the MIT license, we would be
pleased to learn about users' experience and give advice via email sent
to highsopt@gmail.com.

%package        devel
Summary:        Header files and library links for HiGHS
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       zlib-devel%{?_isa}

%description    devel
Header files and library links for developing applications that use
HiGHS.

%package     -n python3-highspy
Summary:        Python interface to coin-or-HiGHS
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description -n python3-highspy
This package contains a Python 3 interface to coin-or-HiGHS.

%prep
%autosetup -n HiGHS-%{version} -p1

# Substitute the release git hash; see note above
sed -i 's,n/a,%{commit},' CMakeLists.txt

# Unbundle catch
rm extern/catch.hpp
ln -s %{_includedir}/catch2/catch_all.hpp extern/catch.hpp

# Unbundle pdqsort
rm extern/pdqsort/pdqsort.h
ln -s %{_includedir}/pdqsort.h extern/pdqsort

# Unbundle zstr
rm -fr extern/zstr
ln -s %{_includedir}/zstr extern

# The Fedora cmake package does not advertise its python interface
sed -i '/cmake/d' pyproject.toml

%generate_buildrequires
%pyproject_buildrequires -x test

%build
%cmake
%cmake_build

# Build the python interface
%pyproject_wheel

%install
%cmake_install

# Install the python interface
%pyproject_install
%pyproject_save_files highspy

# Instead of linking with and installing a private copy of the library,
# fix up the installed python tree to use the installed library
cd highspy
rm -fr %{buildroot}%{python3_sitearch}/.highspy.mesonpy.libs
g++ %{build_cxxflags} -fPIC -shared -I ../src -I ../%{_vpath_builddir} \
  -I %{_includedir}/python%{python3_version} highs_bindings.cpp \
  -o %{buildroot}%{python3_sitearch}/highspy%{python3_ext_suffix} \
  %{build_ldflags} -L %{buildroot}%{_libdir} -lhighs
cd -

%check
%ctest
export LD_LIBRARY_PATH=%{buildroot}%{_libdir}
%pytest

%files
%doc AUTHORS MODS.md README.md
%license LICENSE.txt
%{_bindir}/highs
%{_libdir}/libhighs.so.1*

%files devel
%{_includedir}/highs_export.h
%{_includedir}/highs/
%{_libdir}/cmake/highs/
%{_libdir}/libhighs.so
%{_libdir}/pkgconfig/highs.pc

%files -n python3-highspy -f %{pyproject_files}

%changelog
%autochangelog
