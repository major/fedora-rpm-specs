# Testing needs to be online
%global with_check 0

Name: qrmumps
Version: 3.1
Release: %autorelease
Summary: A multithreaded multifrontal QR solver
License: LGPL-3.0-or-later
URL: http://buttari.perso.enseeiht.fr/qr_mumps/
Source0: https://gitlab.com/qr_mumps/qr_mumps/-/archive/%{version}/qr_mumps-%{version}.tar.gz

BuildRequires: gcc-gfortran, gcc-c++, gcc
BuildRequires: cmake
BuildRequires: metis-devel >= 5.1.0-12
BuildRequires: scotch-devel
BuildRequires: suitesparse-devel
BuildRequires: perl-devel
BuildRequires: perl-generators
BuildRequires: flexiblas-devel
Requires: gcc-gfortran%{?_isa}

Provides: qr_mumps = 0:%{version}-%{release}
Obsoletes: qr_mumps < 0:3.0-1

# Add libraries soname and fix the installation paths
Patch0:   %{name}-fix_libpaths+libsoname.patch

%description
qr_mumps is a software package for the solution of sparse,
linear systems on multicore computers.
It implements a direct solution method based on the QR
factorization of the input matrix. Therefore, it is suited
to solving sparse least-squares problems and to computing
the minimum-norm solution of sparse, underdetermined problems.
It can obviously be used for solving square problems in which
case the stability provided by the use of orthogonal transformations
comes at the cost of a higher operation count with respect to solvers
based on, e.g., the LU factorization.
qr_mumps supports real and complex, single or double precision arithmetic.

%package devel
Summary: Development files for %{name}
Requires: %{name}%{?_isa} = %{version}-%{release}
%description devel
Shared links and header files of %{name}.

%package benchmarks
Summary: Benchmark files for %{name}
Requires: %{name}%{?_isa} = %{version}-%{release}
%description benchmarks
Benchamrks to evaluate the performance of QRM are provided in
the =timing/= directory. These allow for running experiments on the
solution of dense and sparse linear systems through the $QR$ and
Cholesky factorizations. Use the =-h= command line argument to get
help on using these benchmarks.

%package doc
Summary: PDF/HTML documentation files of %{name}
BuildArch: noarch
%description doc
PDF documentation files of %{name}.

########################################################

%prep
%autosetup -n qr_mumps-%{version} -p1

# Those files should actually be the ones provided by CMake itself.
rm -f aux/find/Find{BLAS,LAPACK}.cmake

%build
%cmake -Wno-dev -DQRM_VERSION:STRING=%{version} \
 -DARITH="d;s;z;c" -DCMAKE_BUILD_TYPE:STRING=Release \
 -DQRM_ORDERING_AMD:BOOL=ON -DQRM_ORDERING_METIS:BOOL=ON \
 -DQRM_ORDERING_SCOTCH:BOOL=ON -DQRM_WITH_STARPU:BOOL=OFF \
 -DQRM_WITH_CUDA:BOOL=OFF -DAMD_INCLUDE_DIRS:PATH=%{_includedir}/suitesparse \
 -DBLA_VENDOR=FlexiBLAS \
 -DBLAS_VERBOSE:BOOL=ON -DCMAKE_VERBOSE_MAKEFILE:BOOL=TRUE \
 -DCMAKE_SKIP_RPATH:BOOL=YES -DCMAKE_SKIP_INSTALL_RPATH:BOOL=YES \
 -DINCLUDE_INSTALL_DIR:PATH=%{_includedir}/qrm -DLIB_INSTALL_DIR:PATH=%{_libdir}

%cmake_build

%install
%cmake_install

%if 0%{?with_check}
%check
export LD_LIBRARY_PATH=%{buildroot}%{_libdir}
%ctest
%endif

%files
%license doc/COPYING.LESSER
%doc Changelog.org README.org
%{_libdir}/lib*qrm.so.3
%{_libdir}/libqrm_common.so.3
%{_libdir}/lib*qrm.so.%{version}
%{_libdir}/libqrm_common.so.%{version}

%files devel
%{_includedir}/qrm/
%{_fmoddir}/qrm/
%{_libdir}/lib*qrm.so
%{_libdir}/libqrm_common.so
%{_libdir}/cmake/qrm/

%files benchmarks
%{_bindir}/*qrm_*

%files doc
%license doc/COPYING.LESSER
%doc doc/*

%changelog
%autochangelog
