# Testing needs to be online
%global with_check 0

%if 0%{?el7}
%global dts devtoolset-9-
%endif

Name: qrmumps
Version: 3.0.2
Release: 5%{?dist}
Summary: A multithreaded multifrontal QR solver
License: LGPLv3+
URL: http://buttari.perso.enseeiht.fr/qr_mumps/

# This is a private source link provided by upstream directly
Source0: http://buttari.perso.enseeiht.fr/qr_mumps/releases/qr_mumps-%{version}.tgz

BuildRequires: %{?dts}gcc-gfortran, %{?dts}gcc-c++, %{?dts}gcc
BuildRequires: cmake3 >= 3.11.4
BuildRequires: metis-devel >= 5.1.0-12
BuildRequires: scotch-devel
BuildRequires: suitesparse-devel
BuildRequires: perl-devel
%if 0%{?fedora} >= 33 || 0%{?rhel} >= 9
BuildRequires: perl-generators
BuildRequires: flexiblas-devel
%global blaslib flexiblas
%global cmake_blas_flags -DBLA_VENDOR=FlexiBLAS
%else
BuildRequires: openblas-devel
%global blaslib openblas
%global blasvar o
%global cmake_blas_flags -DBLAS_LIBRARIES=%{_libdir}/lib%{blaslib}%{blasvar}.so -DBLAS_LDFLAGS_USER:STRING=-l%{blaslib}
%endif

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
%if 0%{?el7}
%{?dts:source /opt/rh/devtoolset-9/enable}
%endif
%cmake3 -Wno-dev -S . -DQRM_VERSION:STRING=%{version} \
 -DARITH="d;s;z;c" -DCMAKE_BUILD_TYPE:STRING=Release \
 -DQRM_ORDERING_AMD:BOOL=ON -DQRM_ORDERING_METIS:BOOL=ON \
 -DQRM_ORDERING_SCOTCH:BOOL=ON -DQRM_WITH_STARPU:BOOL=OFF \
 -DQRM_WITH_CUDA:BOOL=OFF -DAMD_INCLUDE_DIRS:PATH=%{_includedir}/suitesparse \
 %{cmake_blas_flags} \
 -DBLAS_VERBOSE:BOOL=ON -DCMAKE_VERBOSE_MAKEFILE:BOOL=TRUE \
 -DCMAKE_SKIP_RPATH:BOOL=YES -DCMAKE_SKIP_INSTALL_RPATH:BOOL=YES

%cmake3_build

%install
%cmake3_install

%if 0%{?with_check}
%check
export LD_LIBRARY_PATH=%{buildroot}%{_libdir}
%ctest
%endif

%files
%license doc/COPYING.LESSER
%doc Changelog.org README.org
%{_libdir}/lib*qrm.so.*
%{_libdir}/libqrm_common.so.*

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
* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jul 13 2021 Björn Esser <besser82@fedoraproject.org> - 3.0.2-2
- Properly set BLA_VENDOR to FlexiBLAS for cmake >= 3.19
- Remove troublesome vendor modified versions of CMake modules

* Thu May 06 2021 Antonio Trande <sagitter@fedoraproject.org> - 3.0.2-1
- Release 3.0.2

* Fri Feb 19 2021 Antonio Trande <sagitter@fedoraproject.org> - 3.0.1-1
- Release 3.0.1

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 3.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Nov 18 2020 Antonio Trande <sagitter@fedoraproject.org> - 3.0-2
- Adapt the package to epel8

* Mon Nov 16 2020 Antonio Trande <sagitter@fedoraproject.org> - 3.0-1
- Release 3.0

* Sun Aug 16 2020 Antonio Trande <sagitter@fedoraproject.org> - 2.0-21
- https://fedoraproject.org/wiki/Changes/FlexiBLAS_as_BLAS/LAPACK_manager
- Exclude examples
- Fix Flexiblas include dir flags

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.0-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Feb 03 2020 Antonio Trande <sagitter@fedoraproject.org> - 2.0-19
- Patched for GCC 10

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.0-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sun Jan 26 2020 Antonio Trande <sagitter@fedoraproject.org> - 2.0-17
- Workaround for GCC 10 (-fallow-argument-mismatch)

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.0-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.0-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Jul 19 2018 Sandro Mani <manisandro@gmail.com> - 2.0-14
- Rebuild (scotch)

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.0-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Sat Feb 17 2018 Antonio Trande <sagitter@fedoraproject.org> - 2.0-12
- Use %%ldconfig_scriptlets

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.0-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Jan 31 2018 Antonio Trande <sagitterATfedoraproject.org> - 2.0-10
- Rebuild for GCC-8
- Disable tests

* Sat Nov 04 2017 Antonio Trande <sagitterATfedoraproject.org> - 2.0-9
- Rebuild against openblas except s390x/arm arches
- Set a custom macro for openblas arches
- Rebuild against COLAMD

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Tue Jan 31 2017 Antonio Trande <sagitterATfedoraproject.org> - 2.0-5
- Rebuild for gcc-gfortran

* Sun Dec 04 2016 Antonio Trande <sagitterATfedoraproject.org> - 2.0-4
- Package renamed as qrmumps for packaging needs
- Set Provides Obsoletes tags
- License changed to LGPLv3+

* Thu Jul 07 2016 Antonio Trande <sagitterATfedoraproject.org> - 2.0-3
- Fix symbolic links
- Fix unused-direct-shlib-dependency warnings

* Thu Jul 07 2016 Antonio Trande <sagitterATfedoraproject.org> - 2.0-2
- Fix %%doc line

* Thu Jul 07 2016 Antonio Trande <sagitterATfedoraproject.org> - 2.0-1
- Update to 2.0

* Mon Mar 07 2016 Antonio Trande <sagitterATfedoraproject.org> - 1.2-3
- Fixed ln commands

* Fri Feb 19 2016 Antonio Trande <sagitterATfedoraproject.org> - 1.2-2
- Use Conditional Builds macro
- Remove pkgconfig BR

* Sat Feb 13 2016 Antonio Trande <sagitterATfedoraproject.org> - 1.2-1
- Initial package
