%global major_soversion 2
%global minor_soversion 6

Name:           stellarsolver
Version:        2.6
Release:        %autorelease
Summary:        The Cross Platform Sextractor and Internal Astrometric Solver
License:        BSD-3-Clause and GPL-2.0-or-later and GPL-3.0-or-later and LGPL-2.0-or-later and LGPL-3.0-or-later and MIT
# License breakdown
#
# Whole work according to LICENSE: GPLv3+
#
# Below: Files with explicitly different license
#
# BSD 3-clause:
#   stellarsolver/astrometry/* EXCEPT files mentioned below,
#          check stellarsolver/astrometry/LICENSE
#
# GPLv2+:
#   stellarsolver/*.{cpp,h}
#   stellarsolver/astrometry/include/astrometry/*qfits*.h
#   stellarsolver/astrometry/qfits-an/*
#   stellarsolver/astrometry/util/md5.c
#   tester/{mainwindow,nan}.*
#   testerutils/{dms,stretch}.*
#
# LGPLv2+:
#   testerutils/bayer.*
#
# LGPLv3+ and BSD and MIT:
#   stellarsolver/sep/*
#          check stellarsolver/sep/README.md for details
#
# MIT:
#   stellarsolver/astrometry/blind/windirent.h
#   
URL:            https://github.com/rlancaste/%{name}/
Source0:        %{url}/archive/%{version}/%{name}-%{version}.tar.gz


# Buildtime tools
BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  desktop-file-utils
# Libraries
BuildRequires:  cfitsio-devel
BuildRequires:  gsl-devel
BuildRequires:  qt6-qtbase-devel
BuildRequires:  wcslib-devel

# The source code bundles modified code from astrometry.net and SEP
Provides:       bundled(astrometry) = 0.89
Provides:       bundled(sep) = 1.2.0

# We split shared libs into subpackage, thus we should require its exact
# version here
Requires:       %{name}-libs%{?_isa} = %{version}-%{release}

%description
StellarSolver is the Cross Platform Sextractor and Internal Astrometric Solver:
* An Astrometric Plate Solver for Mac, Linux, and Windows, built on
  Astrometry.net and SEP (sextractor)
* Meant to be an internal library for use in a program like KStars for internal
  plate solving on all supported operating systems

%package        libs
Summary:        Shared library of StellarSolver

%description    libs
Shared library of Stellarsolver, meant to be an internal library for use in
a program like KStars for internal plate solving on all supported operating
systems.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}-libs%{?_isa} = %{version}-%{release}

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.


%prep
%forgesetup


%build
%cmake -DBUILD_TESTER=ON \
       -DBUILD_BATCH_SOLVER=ON \
       -DUSE_QT5=OFF
%cmake_build


%install
%cmake_install


%check
desktop-file-validate %{buildroot}%{_datadir}/applications/com.github.rlancaste.%{name}.desktop
desktop-file-validate %{buildroot}%{_datadir}/applications/com.github.rlancaste.stellarbatchsolver.desktop


%files
%license LICENSE
%doc README.md
%{_bindir}/StellarSolverTester
%{_bindir}/StellarBatchSolver
%{_datadir}/applications/com.github.rlancaste.stellarsolver.desktop
%{_datadir}/applications/com.github.rlancaste.stellarbatchsolver.desktop
%{_datadir}/icons/*/*/*/StellarSolverIcon.png
%{_datadir}/icons/*/*/*/StellarBatchSolverIcon.png

%files libs
%license LICENSE
%doc README.md
%{_libdir}/*.so.%{major_soversion}
%{_libdir}/*.so.%{major_soversion}.%{minor_soversion}

%files devel
%{_includedir}/*
%{_libdir}/*.so
%{_libdir}/cmake/StellarSolver/
%{_libdir}/pkgconfig/stellarsolver.pc


%changelog
%autochangelog
