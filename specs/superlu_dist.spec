# Copyright (c) 2016 Dave Love, Liverpool University
# Copyright (c) 2018 Dave Love, University of Manchester
# MIT licence, per Fedora policy.

# This flag prevents the linkage to libptscotch.so
%undefine _ld_as_needed

%bcond_without mpich

%ifnarch %{ix86}
%bcond_without python
%else
%bcond_with python
%endif

%ifarch %{ix86}
%bcond_with openmpi
%else
%bcond_without openmpi
%endif

%if 0%{?rhel} || 0%{?rhel} >= 9
%bcond_with colamd
%else
%bcond_without colamd
%endif

# Following scalapack
%bcond_without optimized_blas

%global blaslib flexiblas

# Choose if using 64-bit integers for indexing sparse matrices
%if %{?__isa_bits:%{__isa_bits}}%{!?__isa_bits:32} == 64
%bcond_with index64
%endif

%if %{with index64}
%global OPENBLASLINK -lflexiblas64
%global OPENBLASLIB /libflexiblas64.so
%else
%global OPENBLASLINK -lflexiblas
%global OPENBLASLIB /libflexiblas.so
%endif

%bcond_without check

# Enable CombBLAS support
%bcond_with CombBLAS

%if %{with index64}
BuildRequires: metis64-devel
%global METISLINK -lmetis64
%global METISLIB %{_libdir}/libmetis64.so
%global METISINC %{_includedir}/metis64.h
%else
BuildRequires: metis-devel
%global METISLINK -lmetis
%global METISLIB %{_libdir}/libmetis.so
%global METISINC %{_includedir}/metis.h
%endif

Name: superlu_dist
Version: 9.2.1
Release: 1%{?dist}
Epoch:   1
Summary: Solution of large, sparse, nonsymmetric systems of linear equations
License: BSD-3-Clause
URL: https://github.com/xiaoyeli/superlu_dist
Source0: https://github.com/xiaoyeli/superlu_dist/archive/v%{version}/%{name}-%{version}.tar.gz

Patch1: %{name}-fix_pkgconfig_creation.patch
# Longer tests take 1000 sec or timeout, so don't run them
Patch4: %{name}-only_short_tests.patch

Patch5: %{name}-fix_pythonpath.patch
Patch6: %{name}-fix_openmpi_example_path.patch
Patch7: %{name}-fix_mpich_example_path.patch

BuildRequires: scotch-devel
BuildRequires: gcc-c++
BuildRequires: make
BuildRequires: patchelf
BuildRequires: cmake
%if %{with optimized_blas}
BuildRequires: %{blaslib}-devel
%endif
%if %{with colamd}
BuildRequires: suitesparse-devel
%endif

%global desc \
SuperLU is a general purpose library for the direct solution of large,\
sparse, nonsymmetric systems of linear equations.  The library is\
written in C and is callable from either C or Fortran program.  It\
uses MPI, OpenMP and CUDA to support various forms of parallelism.  It\
supports both real and complex datatypes, both single and double\
precision, and 64-bit integer indexing.  The library routines performs\
an LU decomposition with partial pivoting and triangular system solves\
through forward and back substitution.  The LU factorization routines\
can handle non-square matrices but the triangular solves are performed\
only for square matrices.  The matrix columns may be preordered\
(before factorization) either through library or user supplied\
routines.  This preordering for sparsity is completely separate from\
the factorization.  Working precision iterative refinement subroutines\
are provided for improved backward stability.  Routines are also\
provided to equilibrate the system, estimate the condition number,\
calculate the relative backward error, and estimate error bounds for\
the refined solutions.\
\
This version uses MPI and OpenMP.

%description
%desc

%if %{with openmpi}
%package openmpi
Summary:       Solution of large, sparse, nonsymmetric systems of linear equations
BuildRequires: openmpi-devel
BuildRequires: ptscotch-openmpi-devel >= 6.0.5
BuildRequires: ptscotch-openmpi-devel-parmetis >= 6.0.5
%if %{with CombBLAS}
BuildRequires: combblas-openmpi-devel >= 2.0.0
%endif
Requires:      gcc-gfortran%{?_isa}
%description openmpi
%desc

%package openmpi-devel
Summary: Development files for %{name}-openmpi
Requires: openmpi-devel%{?_isa}
Requires: %{name}-openmpi%{?_isa} = %{epoch}:%{version}-%{release}
Obsoletes: %{name}-openmpi-static < 1:9.2.1
%description openmpi-devel
Development files for %{name}-openmpi

%package openmpi-examples
Summary: Example files for %{name}-openmpi
Requires: %{name}-openmpi%{?_isa} = %{epoch}:%{version}-%{release}
%description openmpi-examples
This package contains sample programs to illustrate how to use
various functions provided in SuperLU_DIST.

%if %{with python}
%package -n python3-%{name}-openmpi
Summary:   Solution of large, sparse, nonsymmetric systems of linear equations
BuildRequires: python3-devel
BuildRequires: python3-mpi4py-openmpi
BuildRequires: python3-numpy
BuildRequires: python3-scipy
Requires: %{name}-openmpi%{?_isa} = %{epoch}:%{version}-%{release}
Requires: python3-mpi4py-openmpi
Requires: python3-numpy
Requires: python3-scipy
%description -n python3-%{name}-openmpi
This package contains the Python interface routines for SuperLU_DIST.

%package -n python3-%{name}-openmpi-devel
Summary:  Solution of large, sparse, nonsymmetric systems of linear equations
Requires: python3-%{name}-openmpi%{?_isa}
%description -n python3-%{name}-openmpi-devel
This package contains the Python interface routines for SuperLU_DIST.
%endif
%endif

%package doc
Summary: Documentation for %{name}
BuildArch: noarch
%description doc
Documentation for %{name}

%if %{with mpich}
%package mpich
Summary:       Solution of large, sparse, nonsymmetric systems of linear equations
BuildRequires: mpich-devel
BuildRequires: ptscotch-mpich-devel  >= 6.0.5
BuildRequires: ptscotch-mpich-devel-parmetis  >= 6.0.5
%if %{with CombBLAS}
BuildRequires: combblas-mpich-devel >= 2.0.0
%endif
Requires:      gcc-gfortran%{?_isa}
%description mpich
%desc

%package mpich-devel
Summary: Development files for %{name}-mpich
Requires: mpich-devel%{?_isa}
Requires: ptscotch-mpich-devel%{?_isa}
Requires: ptscotch-mpich-devel-parmetis%{?_isa}
Requires: %{name}-mpich%{?_isa} = %{epoch}:%{version}-%{release}
Obsoletes: %{name}-mpich-static < 1:9.2.1
%description mpich-devel
Development files for %{name}-mpich

%package mpich-examples
Summary: Example files for %{name}-mpich
Requires: %{name}-mpich%{?_isa} = %{epoch}:%{version}-%{release}
%description mpich-examples
This package contains sample programs to illustrate how to use
various functions provided in SuperLU_DIST.

%if %{with python}
%package -n python3-%{name}-mpich
Summary:   Solution of large, sparse, nonsymmetric systems of linear equations
BuildRequires: python3-devel
BuildRequires: python3-mpi4py-mpich
BuildRequires: python3-numpy
BuildRequires: python3-scipy
Requires: %{name}-mpich%{?_isa} = %{epoch}:%{version}-%{release}
Requires: python3-mpi4py-mpich
Requires: python3-numpy
Requires: python3-scipy
%description -n python3-%{name}-mpich
This package contains the Python interface routines for SuperLU_DIST.

%package -n python3-%{name}-mpich-devel
Summary:  Solution of large, sparse, nonsymmetric systems of linear equations
Requires: python3-%{name}-mpich%{?_isa}
%description -n python3-%{name}-mpich-devel
This package contains the Python interface routines for SuperLU_DIST.
%endif
%endif

%prep
%setup -qc

pushd superlu_dist-%{version}
%patch -P 1 -p1 -b .fix_pkgconfig_creation
%patch -P 4 -p1 -b .only_short_tests
%patch -P 5 -p1 -b .pythonpath

# Rename different README files
cp -p EXAMPLE/README EXAMPLE/README-examples
cp -p PYTHON/README PYTHON/README-python

# Remove spurious executable permissions
for i in `find SRC PYTHON EXAMPLE -name "*.c" -o -name "*.h"`; do
chmod a-x $i
done
popd

%if %{with openmpi}
cp -a superlu_dist-%{version} openmpi-build
pushd openmpi-build
%patch -P 6 -p1 -b .example_path
popd
%endif
%if %{with mpich}
cp -a superlu_dist-%{version} mpich-build
pushd mpich-build
%patch -P 7 -p1 -b .example_path
popd
%endif

%build
%if %{with openmpi}
pushd openmpi-build
%{_openmpi_load}
export CC=$MPI_BIN/mpicc
export CXX=$MPI_BIN/mpic++
export CFLAGS="%{optflags} -DPRNTlevel=0 -DDEBUGlevel=0"
export CXXFLAGS="%{optflags} -I$MPI_INCLUDE"
export LDFLAGS="%{build_ldflags} -L$MPI_LIB -lptscotch -lptscotcherr -lptscotcherrexit"
%cmake -DCMAKE_BUILD_TYPE:STRING=Release \
 -DBUILD_STATIC_LIBS:BOOL=FALSE \
 -DCMAKE_Fortran_COMPILER:FILEPATH=$MPI_BIN/mpifort \
 -DMPIEXEC_EXECUTABLE:FILEPATH=$MPI_BIN/mpiexec \
 -DCMAKE_SKIP_RPATH:BOOL=YES \
 -DCMAKE_SKIP_INSTALL_RPATH:BOOL=YES \
%if %{with CombBLAS}
 -DTPL_ENABLE_COMBBLASLIB:BOOL=ON \
 -DTPL_COMBBLAS_INCLUDE_DIRS:PATH="$MPI_INCLUDE/CombBLAS;$MPI_INCLUDE/CombBLAS/3DSpGEMM;$MPI_INCLUDE/CombBLAS/Applications;$MPI_INCLUDE/CombBLAS/BipartiteMatchings" \
 -DTPL_COMBBLAS_LIBRARIES:STRING=$MPI_LIB/libCombBLAS.so \
%endif
%if %{with colamd}
 -DTPL_ENABLE_COLAMD=ON -DTPL_COLAMD_INCLUDE_DIRS:PATH=%{_includedir}/suitesparse -DTPL_COLAMD_LIBRARIES:STRING=-lcolamd \
 -DMPI_C_LINK_FLAGS:STRING="-L$MPI_LIB -lptscotch -lptscotcherr -lptscotcherrexit -L%{_libdir} %{METISLINK} -lscotch -lcolamd" \
%else
 -DTPL_ENABLE_COLAMD=OFF \
 -DMPI_C_LINK_FLAGS:STRING="-L$MPI_LIB -lptscotch -lptscotcherr -lptscotcherrexit -L%{_libdir} %{METISLINK} -lscotch" \
%endif
 -DTPL_ENABLE_INTERNAL_BLASLIB:BOOL=OFF -DTPL_BLAS_LIBRARIES:FILEPATH=%{OPENBLASLINK} -DTPL_ENABLE_LAPACKLIB:BOOL=OFF -DTPL_LAPACK_LIBRARIES:BOOL=OFF \
 -DMPI_C_HEADER_DIR:PATH="$MPI_INCLUDE -I%{METISINC}" \
 -DMPI_CXX_LINK_FLAGS:STRING="-L$MPI_LIB -lptscotch -lptscotcherr -lptscotcherrexit -L%{_libdir} %{METISLINK} -lscotch -fopenmp" \
 -DTPL_ENABLE_PARMETISLIB:BOOL=ON -DTPL_PARMETIS_INCLUDE_DIRS:PATH=$MPI_INCLUDE/scotch \
 -DTPL_PARMETIS_LIBRARIES:STRING="-L$MPI_LIB -lptscotchparmetis %{METISLINK}" \
%if %{with index64}
 -DXSDK_INDEX_SIZE=64 \
%else
 -DXSDK_INDEX_SIZE=32 \
%endif
 -Denable_double:BOOL=ON -Denable_complex16:BOOL=ON \
 -Denable_examples:BOOL=ON -Denable_tests:BOOL=ON -DBUILD_TESTING:BOOL=ON \
 -DCMAKE_INSTALL_PREFIX:PATH=%{_prefix} -DCMAKE_INSTALL_BINDIR:PATH=$MPI_BIN -DCMAKE_INSTALL_INCLUDEDIR:PATH=$MPI_INCLUDE/%{name} \
 -DCMAKE_INSTALL_LIBDIR:PATH=$MPI_LIB -DPYTHONPATH:PATH=$MPI_PYTHON3_SITEARCH \
%if %{without python}
 -Denable_python:BOOL=OFF
%endif

%cmake_build
%{_openmpi_unload}
popd
%endif

%if %{with mpich}
pushd mpich-build
%{_mpich_load}
export CC=$MPI_BIN/mpicc
export CXX=$MPI_BIN/mpic++
export CFLAGS="%{optflags} -DPRNTlevel=0 -DDEBUGlevel=0"
export CXXFLAGS="%{optflags} -I$MPI_INCLUDE"
export LDFLAGS="%{build_ldflags} -L$MPI_LIB -lptscotch -lptscotcherr -lptscotcherrexit"
%cmake -DCMAKE_BUILD_TYPE:STRING=Release \
 -DBUILD_STATIC_LIBS:BOOL=FALSE \
 -DCMAKE_Fortran_COMPILER:FILEPATH=$MPI_BIN/mpifort \
 -DMPIEXEC_EXECUTABLE:FILEPATH=$MPI_BIN/mpiexec \
 -DCMAKE_SKIP_RPATH:BOOL=YES \
 -DCMAKE_SKIP_INSTALL_RPATH:BOOL=YES \
%if %{with CombBLAS}
 -DTPL_ENABLE_COMBBLASLIB:BOOL=ON \
 -DTPL_COMBBLAS_INCLUDE_DIRS:PATH="$MPI_INCLUDE/CombBLAS;$MPI_INCLUDE/CombBLAS/3DSpGEMM;$MPI_INCLUDE/CombBLAS/Applications;$MPI_INCLUDE/CombBLAS/BipartiteMatchings" \
 -DTPL_COMBBLAS_LIBRARIES:STRING=$MPI_LIB/libCombBLAS.so \
%endif
%if %{with colamd}
 -DTPL_ENABLE_COLAMD=ON -DTPL_COLAMD_INCLUDE_DIRS:PATH=%{_includedir}/suitesparse -DTPL_COLAMD_LIBRARIES:STRING=-lcolamd \
 -DMPI_C_LINK_FLAGS:STRING="-L$MPI_LIB -lptscotch -lptscotcherr -lptscotcherrexit -L%{_libdir} %{METISLINK} -lscotch -lcolamd" \
%else
 -DTPL_ENABLE_COLAMD=OFF \
 -DMPI_C_LINK_FLAGS:STRING="-L$MPI_LIB -lptscotch -lptscotcherr -lptscotcherrexit -L%{_libdir} %{METISLINK} -lscotch" \
%endif
 -DTPL_ENABLE_INTERNAL_BLASLIB:BOOL=OFF -DTPL_BLAS_LIBRARIES:FILEPATH=%{OPENBLASLINK} -DTPL_ENABLE_LAPACKLIB:BOOL=OFF -DTPL_LAPACK_LIBRARIES:BOOL=OFF \
 -DMPI_C_HEADER_DIR:PATH="$MPI_INCLUDE -I%{METISINC}" \
 -DMPI_CXX_LINK_FLAGS:STRING="-L$MPI_LIB -lptscotch -lptscotcherr -lptscotcherrexit -L%{_libdir} %{METISLINK} -lscotch" \
 -DTPL_ENABLE_PARMETISLIB:BOOL=ON -DTPL_PARMETIS_INCLUDE_DIRS:PATH=$MPI_INCLUDE/scotch \
 -DTPL_PARMETIS_LIBRARIES:STRING="-L$MPI_LIB -lptscotchparmetis %{METISLINK}" \
%if %{with index64}
 -DXSDK_INDEX_SIZE=64 \
%else
 -DXSDK_INDEX_SIZE=32 \
%endif
 -Denable_double:BOOL=ON -Denable_complex16:BOOL=ON \
 -Denable_examples:BOOL=ON -Denable_tests:BOOL=ON -DBUILD_TESTING:BOOL=ON \
 -DCMAKE_INSTALL_PREFIX:PATH=%{_prefix} -DCMAKE_INSTALL_BINDIR:PATH=$MPI_BIN -DCMAKE_INSTALL_INCLUDEDIR:PATH=$MPI_INCLUDE/%{name} \
 -DCMAKE_INSTALL_LIBDIR:PATH=$MPI_LIB -DPYTHONPATH:PATH=$MPI_PYTHON3_SITEARCH \
%if %{without python}
 -Denable_python:BOOL=OFF
%endif

%cmake_build
%{_mpich_unload}
popd
%endif


%install
%if %{with openmpi}
pushd openmpi-build
%{_openmpi_load}
%cmake_install

# Fix rpaths of example files
patchelf --force-rpath --set-rpath $MPI_LIB %{buildroot}%{_libexecdir}/superlu_dist-openmpi/*drive*

# Disable INT64 if 64bit integer is not used (require superlu_dist to be compiled with 64-bit indexing)
%if %{with python}
%if %{without index64}
sed -i -e 's|INT64 = 1|INT64 = 0|' %{buildroot}$MPI_PYTHON3_SITEARCH/%{name}/pddrive.py
sed -i -e 's|INT64 = 1|INT64 = 0|' %{buildroot}$MPI_PYTHON3_SITEARCH/%{name}/pddrive_master.py
%endif
%endif
%{_openmpi_unload}
popd
%endif

%if %{with mpich}
pushd mpich-build
%{_mpich_load}
%cmake_install

# Fix rpaths of example files
patchelf --force-rpath --set-rpath $MPI_LIB %{buildroot}%{_libexecdir}/superlu_dist-mpich/*drive*

# Disable INT64 if 64bit integer is not used (require superlu_dist to be compiled with 64-bit indexing)
%if %{with python}
%if %{without index64}
sed -i -e 's|INT64 = 1|INT64 = 0|' %{buildroot}$MPI_PYTHON3_SITEARCH/%{name}/pddrive.py
sed -i -e 's|INT64 = 1|INT64 = 0|' %{buildroot}$MPI_PYTHON3_SITEARCH/%{name}/pddrive_master.py
%endif
%endif
%{_mpich_unload}
popd
%endif

%if %{with check}
%check
%if %{with openmpi}
pushd openmpi-build
%{_openmpi_load}
export LD_LIBRARY_PATH=%{buildroot}$MPI_LIB
%ctest --timeout 3000

%if %{with python}
export SUPERLU_PYTHON_LIB_PATH=%{buildroot}$MPI_PYTHON3_SITEARCH/%{name}
export LD_LIBRARY_PATH=%{buildroot}$MPI_LIB
# Disable INT64 if 64bit integer is not used (require superlu_dist to be compiled with 64-bit indexing)
%if %{without index64}
sed -i -e 's|INT64 = 1|INT64 = 0|' PYTHON/pddrive.py
sed -i -e 's|INT64 = 1|INT64 = 0|' PYTHON/pddrive_master.py
%endif
mpirun --wdir PYTHON -np 2 %{__python3} pddrive.py -c 2 -r 1
%endif
%{_openmpi_unload}
popd
%endif

%ifnarch s390x
%if %{with mpich}
pushd mpich-build
%{_mpich_load}
export LD_LIBRARY_PATH=%{buildroot}$MPI_LIB
%ctest --timeout 3000

%if %{with python}
export SUPERLU_PYTHON_LIB_PATH=%{buildroot}$MPI_PYTHON3_SITEARCH/%{name}
export LD_LIBRARY_PATH=%{buildroot}$MPI_LIB
# Disable INT64 if 64bit integer is not used (require superlu_dist to be compiled with 64-bit indexing)
%if %{without index64}
sed -i -e 's|INT64 = 1|INT64 = 0|' PYTHON/pddrive.py
sed -i -e 's|INT64 = 1|INT64 = 0|' PYTHON/pddrive_master.py
%endif
mpirun --wdir PYTHON -np 2 %{__python3} pddrive.py -c 2 -r 1
%endif
%{_mpich_unload}
popd
%endif
%endif
%endif
# Check

%if %{with openmpi}
%files openmpi
%license superlu_dist-%{version}/License.txt
%doc superlu_dist-%{version}/README.md
%{_libdir}/openmpi/lib/*.so.9
%{_libdir}/openmpi/lib/*.so.%{version}

%files openmpi-devel
%{_libdir}/openmpi/lib/*.so
%{_libdir}/openmpi/lib/pkgconfig/*.pc
%{_includedir}/openmpi-%{_arch}/superlu_dist/

%files openmpi-examples
%doc superlu_dist-%{version}/EXAMPLE/README-examples
%{_libexecdir}/superlu_dist-openmpi/

%if %{with python}
%files -n python3-%{name}-openmpi
%license superlu_dist-%{version}/License.txt
%doc superlu_dist-%{version}/PYTHON/README-python
%dir %{python3_sitearch}/openmpi/%{name}
%{python3_sitearch}/openmpi/%{name}/libsuperlu_dist_python.so.%{version}
%{python3_sitearch}/openmpi/%{name}/__pycache__/

%files -n python3-%{name}-openmpi-devel
%{python3_sitearch}/openmpi/%{name}/libsuperlu_dist_python.so
%{python3_sitearch}/openmpi/%{name}/libsuperlu_dist_python.so.9
%{python3_sitearch}/openmpi/%{name}/*.py
%{python3_sitearch}/openmpi/%{name}/pdbridge.h
%endif
%endif

%files doc
%license superlu_dist-%{version}/License.txt
%doc superlu_dist-%{version}/DOC

%if %{with mpich}
%files mpich
%license superlu_dist-%{version}/License.txt
%doc superlu_dist-%{version}/README.md
%{_libdir}/mpich/lib/*.so.9
%{_libdir}/mpich/lib/*.so.%{version}

%files mpich-devel
%{_libdir}/mpich/lib/*.so
%{_libdir}/mpich/lib/pkgconfig/*.pc
%{_includedir}/mpich-%{_arch}/superlu_dist/

%files mpich-examples
%doc superlu_dist-%{version}/EXAMPLE/README-examples
%{_libexecdir}/superlu_dist-mpich/

%if %{with python}
%files -n python3-%{name}-mpich
%license superlu_dist-%{version}/License.txt
%doc superlu_dist-%{version}/PYTHON/README-python
%dir %{python3_sitearch}/mpich/%{name}
%{python3_sitearch}/mpich/%{name}/libsuperlu_dist_python.so.%{version}
%{python3_sitearch}/mpich/%{name}/__pycache__/

%files -n python3-%{name}-mpich-devel
%{python3_sitearch}/mpich/%{name}/libsuperlu_dist_python.so
%{python3_sitearch}/mpich/%{name}/libsuperlu_dist_python.so.9
%{python3_sitearch}/mpich/%{name}/*.py
%{python3_sitearch}/mpich/%{name}/pdbridge.h
%endif
%endif


%changelog
* Wed Apr 01 2026 Antonio Trande <sagitter@fedoraproject.org> - 1:9.2.1-1
- Release 9.2.1
- Fix License expression
- Exclude static libraries
- Add Python libraries as sub-packages
- Add EXAMPLE files as sub-packages

* Sat Jan 17 2026 Fedora Release Engineering <releng@fedoraproject.org> - 1:8.2.0-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_44_Mass_Rebuild

* Tue Aug 12 2025 Dave Love <loveshack@fedoraproject.org> - 1:8.2.0-10
- Fix #2276427

* Fri Jul 25 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1:8.2.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_43_Mass_Rebuild

* Tue Jan 21 2025 Antonio Trande <sagitter@fedoraproject.org> - 1:8.2.0-8
- Fix GCC15 builds

* Sun Jan 19 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1:8.2.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Wed Sep 04 2024 Miroslav Suchý <msuchy@redhat.com> - 1:8.2.0-6
- convert license to SPDX

* Fri Aug 16 2024 Sandro Mani <manisandro@gmail.com> - 1:8.2.0-5
- Rebuild (scotch-7.0.4)

* Sat Jul 20 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1:8.2.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Sun Feb 04 2024 Orion Poplawski <orion@nwra.com> - 1:8.2.0-3
- Rebuild with suitesparse 7.6.0

* Sat Jan 27 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1:8.2.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Dec 15 2023 Antonio Trande <sagitter@fedoraproject.org> - 1:8.2.0-1
- Release 8.2.0

* Thu Aug 17 2023 Antonio Trande <sagitter@fedoraproject.org> - 1:8.1.2-6
- Rebuild for scotch-7.0.4

* Sun Aug 06 2023 Antonio Trande <sagitter@fedoraproject.org> - 1:8.1.2-5
- Remove manual build method
- Modernize patch commands

* Sun Aug 06 2023 Antonio Trande <sagitter@fedoraproject.org> - 1:8.1.2-4
- Exclude mpich tests on s390x

* Sat Jul 22 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1:8.1.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Tue Apr 18 2023 Antonio Trande <sagitter@fedoraproject.org> - 1:8.1.2-2
- Disable index64 builds

* Thu Apr 13 2023 Antonio Trande <sagitter@fedoraproject.org> - 1:8.1.2-1
- Release 8.1.2

* Sat Jan 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1:8.1.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Sat Dec 31 2022 Antonio Trande <sagitter@fedoraproject.org> - 1:8.1.1-2
- Disable colamd support in epel9

* Sun Oct 02 2022 Antonio Trande <sagitter@fedoraproject.org> - 1:8.1.1-1
- Release 8.1.1
- Enable colamd support

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1:8.1.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jul 07 2022 Antonio Trande <sagitter@fedoraproject.org> - 1:8.1.0-1
- Release 8.1.0
- Remove obsolete conditional macros

* Sun May 29 2022 Antonio Trande <sagitter@fedoraproject.org> - 1:8.0.0-1
- Release 8.0.0
- Provide static libraries

* Sat Apr 16 2022 Antonio Trande <sagitter@fedoraproject.org> - 1:7.2.0-3
- Enable complex16 libraries

* Fri Apr 15 2022 Antonio Trande <sagitter@fedoraproject.org> - 1:7.2.0-2
- Make sure installing all header libraries

* Sat Apr 02 2022 Antonio Trande <sagitter@fedoraproject.org> - 1:7.2.0-1
- Release 7.2.0
- Enable CombBLAS support
- Add CMake build method
- Specific index_size

* Sat Jan 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1:6.1.1-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1:6.1.1-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1:6.1.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Fri Aug 28 2020 Iñaki Úcar <iucar@fedoraproject.org> - 1:6.1.1-6
- https://fedoraproject.org/wiki/Changes/FlexiBLAS_as_BLAS/LAPACK_manager

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1:6.1.1-5
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1:6.1.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Apr 13 2020 Dave Love <loveshack@fedoraproject.org> - 1:6.1.1-3
- Introduce epoch and revert incompatible change to 6.3.1

* Thu Apr  9 2020 Dave Love <loveshack@fedoraproject.org> - 6.3.1-1
- New version

* Fri Jan 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 6.1.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Sep 12 2019 Dave Love <loveshack@fedoraproject.org> - 6.1.1-1
- New version

* Sat Jul 27 2019 Fedora Release Engineering <releng@fedoraproject.org> - 6.1.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Feb 14 2019 Orion Poplawski <orion@nwra.com> - 6.1.0-2
- Rebuild for openmpi 3.1.3

* Sun Feb 03 2019 Antonio Trande <sagitter@fedoraproject.org> - 6.1.0-1
- Release 6.1.0

* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 6.0.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sun Dec 16 2018 Orion Poplawski <orion@cora.nwra.com> - 6.0.0-3
- libsuperlu_dist is a C++ library, link with mpicxx
- Allow oversubscription with openmpi in tests

* Thu Nov 29 2018 Orion Poplawski <orion@cora.nwra.com> - 6.0.0-2
- Re-enable tests - seem to be working with openmpi 2.1.6rc1

* Wed Nov 21 2018 Dave Love <loveshack@fedoraproject.org> - 6.0.0-1
- New version
- Avoid tests

* Thu Jul 19 2018 Sandro Mani <manisandro@gmail.com> - 5.4.0-3
- Rebuild (scotch)

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 5.4.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jul 10 2018 Dave Love <loveshack@fedoraproject.org> - 5.4.0-1
- New version

* Thu Apr 26 2018 Dave Love <loveshack@fedoraproject.org> - 5.3.0-3
- Require ptscotch-mpich-devel-parmetis

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 5.3.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Tue Jan 30 2018 Dave Love <loveshack@fedoraproject.org> - 5.3.0-1
- New version
- Update sovar
- Drop patch

* Sun Nov  5 2017 Dave Love <loveshack@fedoraproject.org> - 5.2.2-2
- Link againt ptscothmetis et al

* Tue Oct 31 2017 Dave Love <loveshack@fedoraproject.org> - 5.2.2-1
- New version
- Drop output and cmake patches
- Update soname minor version (added function)

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 5.1.3-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 5.1.3-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Jun  9 2017 Dave Love <loveshack@fedoraproject.org> - 5.1.3-6
- Maybe use openblas_arches instead

* Thu Jun  8 2017 Dave Love <loveshack@fedoraproject.org> - 5.1.3-5
- Fix up mpich-devel requirement for el7 7.3
- Avoid openblas on s3909(x)

* Sat Jun  3 2017 Dave Love <loveshack@fedoraproject.org> - 5.1.3-4
- Fix mpich conditional
- Build for openmpi on s390 f25+

* Tue Apr 18 2017 Dave Love <loveshack@fedoraproject.org> - 5.1.3-3
- Rebuild for fix to rhbz #1435690

* Wed Apr 12 2017 Dave Love <loveshack@fedoraproject.org> - 5.1.3-2
- Fix EXAMPLES clean up

* Wed Apr 12 2017 Dave Love <loveshack@fedoraproject.org> - 5.1.3-1
- Exclude check on power64 and fix the mpich conditional

* Wed Mar  8 2017 Dave Love <loveshack@fedoraproject.org> - 5.1.3-1
- New version

* Fri Nov 25 2016 Dave Love <loveshack@fedoraproject.org> - 5.1.2-3
- Use optflags, __global_ldflags

* Thu Nov 17 2016 Dave Love <loveshack@fedoraproject.org> - 5.1.2-2
- Patch to avoid large diagnostic output

* Thu Oct 27 2016 Dave Love <loveshack@fedoraproject.org> - 5.1.2-1
- New version
- Drop the OpenMP patch

* Sat Oct 22 2016 Dave Love <loveshack@fedoraproject.org> - 5.1.1-3
- Fix soname

* Wed Oct 19 2016 Dave Love <loveshack@fedoraproject.org> - 5.1.1-2
- Conditionalize openmpi

* Mon Oct 17 2016 Dave Love <loveshack@fedoraproject.org> - 5.1.1-1
- New version
- Drop some patches and use ptscotch to replace parmetis
- Add mpich version
- Make -doc package

* Fri Nov 20 2015 Dave Love <loveshack@fedoraproject.org> - 4.2-1
- Initial version
