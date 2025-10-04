Name:           gcg
Version:        3.7.2
Release:        %autorelease
Summary:        Branch-and-price and column generation

%global upver   %(sed 's/\\.//g' <<< %{version})
%global giturl  https://github.com/scipopt/gcg

License:        LGPL-3.0-or-later
URL:            https://gcg.or.rwth-aachen.de/
VCS:            git:%{giturl}.git
Source:         %{giturl}/archive/v%{upver}/%{name}-%{upver}.tar.gz
# Increase the cmake minimum version to avoid deprecation warnings
Patch:          %{name}-cmake-minimum.patch
# Find libnauty with pkgconfig rather than cmake
Patch:          %{name}-nauty-pkgconfig.patch
# Link with flexiblas instead of gslcblas for GSL
Patch:          %{name}-gsl-flexiblas.patch

# See https://fedoraproject.org/wiki/Changes/EncourageI686LeafRemoval
ExcludeArch:    %{ix86}

BuildRequires:  cmake
BuildRequires:  cmake(gtest)
BuildRequires:  cmake(scip)
BuildRequires:  gcc-c++
BuildRequires:  pkgconfig(flexiblas)
BuildRequires:  pkgconfig(gmp)
BuildRequires:  pkgconfig(gsl)
BuildRequires:  pkgconfig(libcliquer)
BuildRequires:  pkgconfig(libnauty)

Requires:       libgcg%{?_isa} = %{version}-%{release}

%global _desc %{expand:
GCG: Generic Column Generation

Welcome to what is currently one of the only available open-source solvers for
mixed integer programming (MIP) that applies a comprehensive and expandable
Branch-Price-and-Cut framework.  By making use of detection algorithms, GCG is
able to apply Dantzig-Wolfe reformulation and Benders decomposition to solve
(potentially) structured MIPs faster.  It builds upon SCIP and thus allows for
total control of the solution process and the access of detailed information
down to the guts of the solver.}

%description
%_desc

This package contains a command-line tool to access GCG functionality.

%package -n     libgcg
Summary:        Library for branch-and-price and column generation

%description -n libgcg
%_desc

This package contains a library interface to GCG functionality.

%package -n     libgcg-devel
Summary:        Headers and library links for libgcg
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       libgcg%{?_isa} = %{version}-%{release}

%description -n libgcg-devel
This package contains headers and library links for developing applications
that use libgcg.

%prep
%autosetup -p1 -n %{name}-%{upver}

%conf
# Remove the prebuilt hmetis executable
rm hmetis

# Fix installation directories
if [ "%{_lib}" != "lib" ]; then
  sed -i 's,\(DESTINATION \)lib,\1%{_lib},' src/CMakeLists.txt
fi

# Disable unwanted rpaths
sed -e '/INSTALL_RPATH_USE_LINK_PATH/s/TRUE/FALSE/' \
    -e '/INSTALL_RPATH.*CMAKE_INSTALL_PREFIX/d' \
    -i src/CMakeLists.txt

%build
export CFLAGS='%{build_cflags} -DNDEBUG'
export CXXFLAGS='%{build_cxxflags} -DNDEBUG'
%cmake -DOPENMP:BOOL=ON
%cmake_build

%install
%cmake_install

%check
export LD_LIBRARY_PATH=%{buildroot}%{_libdir}
%ctest

%files
%{_bindir}/gcg

%files -n libgcg
%doc CHANGELOG README.md
%license LICENSE
%{_libdir}/libgcg.so.3.7*

%files -n libgcg-devel
%{_includedir}/gcg/
%{_includedir}/graph/
%{_libdir}/libgcg.so
%{_libdir}/cmake/gcg/

%changelog
%autochangelog
