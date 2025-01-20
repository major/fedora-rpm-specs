## Debug builds?
%bcond_with debug
#

ExcludeArch: %{ix86}

%global optflags %(echo '%optflags' | sed s/-Wp,-D_GLIBCXX_ASSERTIONS//)

# Upstream uses two method for calling psblas3 libraries,
# this one is adapted to use psblas3 shared libraries.
# Call ../configure_n instead of ./configure
%global _configure ./configure_n

%global with_mpich 1
%global with_openmpi 1
%global with_serial 0
%global with_check 1

##
%bcond_without superludist
#

%global major_version 1
%global major_minor %{major_version}.1
%global postrelease_version -1

%if 0%{?fedora}
%global blaslib flexiblas
%else
%global blaslib openblas
%endif

# -Werror=format-security flag is not valid for Fortran
%global fc_optflags $(echo "%optflags" | sed -e 's/-Werror=format-security//')

%global libname libamg_prec

Name: amg4psblas
Summary: Algebraic Multigrid Package based on PSBLAS
Version: %{major_minor}.2
Release: 8%{?dist}
License: MIT-CMU AND BSD-3-Clause
URL: https://psctoolkit.github.io/products/amg4psblas/
Source0: https://github.com/sfilippone/amg4psblas/archive/V%{version}%{?postrelease_version}/amg4psblas-%{version}%{?postrelease_version}.tgz
BuildRequires: gcc-gfortran
BuildRequires: gcc, gcc-c++
BuildRequires: suitesparse-devel
BuildRequires: %{blaslib}-devel
BuildRequires: make
BuildRequires: metis-devel

%description
AMG4PSBLAS (Algebraic MultiGrid Preconditioners Package
based on PSBLAS) is a package of parallel algebraic
multilevel preconditioners included in the PSCToolkit
(Parallel Sparse Computation Toolkit) software framework.

%if 0%{?with_serial}
%package serial
Summary: %{name} serial mode
BuildRequires: psblas3-serial-devel
BuildRequires: MUMPS-devel
BuildRequires: MUMPS-srpm-macros
BuildRequires: SuperLU-devel
Requires: %{name}-doc = %{version}-%{release}
Obsoletes: mld2p4-serial < 0:2.2.2-9

%description serial
AMG4PSBLAS (Algebraic MultiGrid Preconditioners Package
based on PSBLAS) is a package of parallel algebraic
multilevel preconditioners included in the PSCToolkit
(Parallel Sparse Computation Toolkit) software framework.


%package serial-devel
Summary: Development files for %{name}
Requires: %{name}-serial%{?_isa} = %{version}-%{release}
Requires: psblas3-serial-devel%{?_isa}
Obsoletes: mld2p4-serial-devel < 0:2.2.2-9
Requires: gcc-gfortran%{?_isa}

%description serial-devel
Shared links and header files of serial %{name}.
%endif

########################################################
%if 0%{?with_openmpi}
%package openmpi
Summary: OpenMPI %{name}
BuildRequires: MUMPS-openmpi-devel
BuildRequires: openmpi-devel
BuildRequires: psblas3-openmpi-devel
BuildRequires: superlu_dist-openmpi-devel
BuildRequires: MUMPS-srpm-macros
%if 0%{?rhel} && 0%{?rhel} < 8
BuildRequires: blacs-openmpi-devel
%endif
Obsoletes: %{name}-serial < 0:1.1.2-1

Requires: openmpi%{?_isa}
Requires: %{name}-doc = %{version}-%{release}
Obsoletes: mld2p4-openmpi < 0:2.2.2-9

%description openmpi
AMG4PSBLAS (Algebraic MultiGrid Preconditioners Package
based on PSBLAS) is a package of parallel algebraic
multilevel preconditioners included in the PSCToolkit
(Parallel Sparse Computation Toolkit) software framework.

%package openmpi-static
Summary: Static OpenMPI libraries of %{name}
Requires: mpich%{?_isa}

%description openmpi-static
AMG4PSBLAS (Algebraic MultiGrid Preconditioners Package
based on PSBLAS) is a package of parallel algebraic
multilevel preconditioners included in the PSCToolkit
(Parallel Sparse Computation Toolkit) software framework.


%package openmpi-devel
Summary: The %{name} headers and development-related files
Requires: %{name}-openmpi%{?_isa} = %{version}-%{release}
Requires: psblas3-openmpi-devel%{?_isa} >= 0:3.8.1
Obsoletes: mld2p4-openmpi-devel < 0:2.2.2-9

%description openmpi-devel
Shared links, header files for OpenMPI %{name}.
%endif
##########################################################
########################################################
%if 0%{?with_mpich}
%package mpich
Summary: MPICH %{name}
BuildRequires: MUMPS-mpich-devel
BuildRequires: mpich-devel
BuildRequires: psblas3-mpich-devel
BuildRequires: superlu_dist-mpich-devel
BuildRequires: MUMPS-srpm-macros
%if 0%{?rhel} && 0%{?rhel} < 8
BuildRequires: blacs-mpich-devel
%endif
Obsoletes: %{name}-serial < 0:1.1.2-1

Requires: mpich%{?_isa}
Requires: %{name}-doc = %{version}-%{release}
Obsoletes: mld2p4-mpich < 0:2.2.2-9

%description mpich
AMG4PSBLAS (Algebraic MultiGrid Preconditioners Package
based on PSBLAS) is a package of parallel algebraic
multilevel preconditioners included in the PSCToolkit
(Parallel Sparse Computation Toolkit) software framework.

%package mpich-static
Summary: Static MPICH libraries of %{name}
Requires: mpich%{?_isa}

%description mpich-static
AMG4PSBLAS (Algebraic MultiGrid Preconditioners Package
based on PSBLAS) is a package of parallel algebraic
multilevel preconditioners included in the PSCToolkit
(Parallel Sparse Computation Toolkit) software framework.


%package mpich-devel
Summary: The %{name} headers and development-related files
Requires: %{name}-mpich%{?_isa} = %{version}-%{release}
Requires: psblas3-mpich-devel%{?_isa}
Obsoletes: mld2p4-mpich-devel < 0:2.2.2-9
%description mpich-devel
Shared links, header files for MPICH %{name}.
%endif
##########################################################

%package doc
Summary: Documentation files for %{name}
BuildArch: noarch
BuildRequires: texlive-tex4ht, texlive-latex, doxygen, ghostscript
BuildRequires: texlive-fancybox, texlive-kpathsea, texlive-metafont
BuildRequires: texlive-mfware
%description doc
HTML, PDF and license files of %{name}.

%prep
%setup -qc -n %{name}-%{version}%{?postrelease_version}

mv amg-%{version}%{?postrelease_version} serial-build

pushd serial-build
# Remove pre-fixed -lstdc++ flags
sed -e 's|-lstdc++||g' -i Make.inc.in
sed -e 's|-lstdc++||g' -i Make_n.inc.in
mkdir -p include
mkdir -p modules
popd

#######################################################
## Copy source for MPI versions
%if 0%{?with_openmpi}
cp -a serial-build openmpi-build
%endif
%if 0%{?with_mpich}
cp -a serial-build mpich-build
%endif
######################################################

%build
%if 0%{?with_serial}
cd serial-build

export LIBBLAS=-l%{blaslib}
export INCBLAS=-I%{_includedir}/%{blaslib}
export FCFLAGS="%{?fc_optflags} -fdec-blank-format-item %{__global_ldflags} -fPIC"

%if %{with debug}
./configure_n --enable-serial --with-fcopt="-O0 -g -fPIC -I%{_fmoddir}" --with-ccopt="-O0 -g -fPIC" \
  --with-cxxopt="-O0 -g -fPIC" LDFLAGS="%{__global_ldflags} -fPIC" CPPFLAGS="$INCBLAS" \
  FCFLAGS="-O0 -g -fPIC" CFLAGS="-O0 -g -fPIC" \
%else
%_configure --enable-serial --with-fcopt="$FCFLAGS" --with-ccopt="%{optflags} %{__global_ldflags} -fPIC" \
  --with-cxxopt="%{optflags} %{__global_ldflags} -fPIC" LDFLAGS="%{__global_ldflags} %{__global_ldflags}" CPPFLAGS="$INCBLAS" \
  FCFLAGS="$FCFLAGS" CFLAGS="%{optflags} %{__global_ldflags} -fPIC" \
%endif
  FC=gfortran CC=gcc CXX=g++ --with-lpk=4 \
  --with-psblas-libdir=%{_libdir} --with-psblas-moddir=%{_fmoddir}/psblas3-serial --with-psblas-incdir=%{_includedir}/psblas3-serial \
  --with-blas=$LIBBLAS --with-lapack=$LIBLAPACK --with-metis=-lmetis --with-metisincfile=metis.h --with-metisincdir=%{_includedir} \
  --with-mumps="-ldmumps -lcmumps -lsmumps -lzmumps" --with-mumpsincdir="%{_includedir}/MUMPS" \
  --with-mumpsmoddir=%{_fmoddir}/MUMPS-%{_MUMPS_version} \
  --with-superlu=-lsuperlu --with-superluincdir=%{_includedir}/SuperLU \
  --with-umfpack=-lumfpack --with-umfpackincdir=%{_includedir}/suitesparse
#cat config.log
#exit 1

cp -p Make_n.inc Make.inc
# Reduce number of jobs for preventing failures
make %{?fedora: -O} %{?el8: -O} -j1 V=1
make %{?fedora: -O} %{?el8: -O} -j1 V=1 -C cbind

# Make shared libraries
pushd lib
gfortran -shared %{__global_ldflags} -Wl,--whole-archive %{libname}.a -Wl,-no-whole-archive -Wl,-Bdynamic -L%{_libdir} $LIBBLAS $LIBLAPACK -lpsb_base -lpsb_prec -lpsb_krylov -lpsb_cbind -ldmumps -lcmumps -lsmumps -lzmumps -lumfpack -lsuperlu -lmetis -lgfortran -lm -lstdc++ -Wl,-soname,%{libname}.so.%{major_minor} -o %{libname}.so.%{major_minor}
ln -sf %{libname}.so.%{major_minor} ./%{libname}.so.%{major_version}
ln -sf %{libname}.so.%{major_minor} ./%{libname}.so
popd

cd ../
%endif

#######################################################
## Build MPI versions
%if 0%{?with_openmpi}
pushd openmpi-build

%{_openmpi_load}
export CC=mpicc
export CXX=mpic++
export FC=mpifort
export LIBBLAS=-l%{blaslib}
export INCBLAS=-I%{_includedir}/%{blaslib}
export FCFLAGS="%{?fc_optflags} -fdec-blank-format-item %{__global_ldflags} -lstdc++ -fPIC"

%if %{with debug}
./configure --with-fcopt="-O0 -g -fPIC -I${MPI_FORTRAN_MOD_DIR} $INCBLAS" --with-ccopt="-O0 -g -fPIC $INCBLAS" \
  --with-cxxopt="-O0 -g -fPIC" LDFLAGS="%{__global_ldflags} -fPIC" CPPFLAGS="-I$MPI_INCLUDE/psblas3 $INCBLAS" \
  FCFLAGS="-O0 -g -fPIC" CFLAGS="-O0 -g -fPIC" \
%else
%configure --with-fcopt="$FCFLAGS $INCBLAS" --with-ccopt="%{optflags} %{__global_ldflags} -fPIC $INCBLAS" \
  --with-cxxopt="%{optflags} %{__global_ldflags} -fPIC" LDFLAGS="%{__global_ldflags}" CPPFLAGS="-I$MPI_INCLUDE/psblas3 $INCBLAS" \
  FCFLAGS="$FCFLAGS" CFLAGS="%{optflags} %{__global_ldflags} -fPIC $INCBLAS" \
%endif
  MPIFC=mpif90 MPICC=mpicc MPICXX=mpic++ --with-lpk=4 \
  --with-psblas-libdir=$MPI_LIB --with-psblas-moddir=$MPI_FORTRAN_MOD_DIR/psblas3 --with-psblas-incdir=$MPI_INCLUDE/psblas3 \
  --with-blas=$LIBBLAS --with-lapack=$LIBLAPACK --with-metis=-lmetis --with-metisincfile=metis.h --with-metisincdir=%{_includedir} \
  --with-mumps="-ldmumps -lcmumps -lsmumps -lzmumps" --with-mumpsincdir="$MPI_INCLUDE/MUMPS" \
  --with-mumpsmoddir=$MPI_FORTRAN_MOD_DIR/MUMPS-%{_MUMPS_version} \
%if %{with superludist}
  --with-superludist=-lsuperlu_dist --with-superludistincdir=$MPI_INCLUDE/superlu_dist \
%else
  --without-superludist \
%endif
  --with-umfpack=-lumfpack --with-umfpackincdir=%{_includedir}/suitesparse
#cat config.log && exit 1

cp -p Make_n.inc Make.inc
# Reduce number of jobs for preventing failures
make %{?fedora: -O} %{?el8: -O} -j1 V=1
make %{?fedora: -O} %{?el8: -O} -j1 V=1 -C cbind 

# Make shared libraries
cd lib
mpic++ %{optflags} -fPIC -shared %{__global_ldflags} -Wl,-Bdynamic -L%{_libdir} $LIBBLAS $LIBLAPACK -lstdc++ -lmetis -lumfpack -lgfortran -lm -L$MPI_LIB -Wl,-rpath -Wl,$MPI_LIB -Wl,--enable-new-dtags -lmpi -lmpi_mpifh -L$MPI_LIB -lpsb_base -lpsb_prec -lpsb_krylov -ldmumps -lcmumps -lsmumps -lzmumps %{?with_superludist:-lsuperlu_dist} -Wl,-soname,%{libname}.so.%{major_minor} -o %{libname}.so.%{major_minor} -Wl,--whole-archive %{libname}.a -Wl,-no-whole-archive
ln -sf %{libname}.so.%{major_minor} ./%{libname}.so.%{major_version}
ln -sf %{libname}.so.%{major_minor} ./%{libname}.so
cd ../
%{_openmpi_unload}
popd
%endif

%if 0%{?with_mpich}
pushd mpich-build

%if 0%{?el7}
%{?dts:source /opt/rh/devtoolset-6/enable}
%endif

%{_mpich_load}
export CC=mpicc
export CXX=mpic++
export FC=mpif90
export LIBBLAS=-l%{blaslib}
export INCBLAS=-I%{_includedir}/%{blaslib}
export FCFLAGS="%{?fc_optflags} -fdec-blank-format-item %{__global_ldflags} -lstdc++ -fPIC"

%if %{with debug}
./configure --with-fcopt="-O0 -g -fPIC -I${MPI_FORTRAN_MOD_DIR} $INCBLAS" --with-ccopt="-O0 -g -fPIC $INCBLAS" \
  --with-cxxopt="-O0 -g -fPIC" LDFLAGS="%{__global_ldflags} -fPIC" CPPFLAGS="-I$MPI_INCLUDE/psblas3 $INCBLAS" \
  FCFLAGS="-O0 -g -fPIC -std=gnu++17" CFLAGS="-O0 -g -fPIC" \
%else
%configure --with-fcopt="$FCFLAGS $INCBLAS" --with-ccopt="%{optflags} %{__global_ldflags} -fPIC $INCBLAS" \
  --with-cxxopt="%{optflags} %{__global_ldflags} -fPIC" LDFLAGS="%{__global_ldflags} %{__global_ldflags}" CPPFLAGS="-I$MPI_INCLUDE/psblas3 $INCBLAS" \
  FCFLAGS="$FCFLAGS" CFLAGS="%{optflags} %{__global_ldflags} -fPIC $INCBLAS" \
%endif
 MPIFC=mpif90 MPICC=mpicc MPICXX=mpic++ --with-lpk=4 \
  --with-psblas-libdir=$MPI_LIB --with-psblas-moddir=$MPI_FORTRAN_MOD_DIR/psblas3 --with-psblas-incdir=$MPI_INCLUDE/psblas3 \
  --with-blas=$LIBBLAS --with-lapack=$LIBLAPACK --with-metis=-lmetis --with-metisincfile=metis.h --with-metisincdir=%{_includedir} \
  --with-mumps="-ldmumps -lcmumps -lsmumps -lzmumps" --with-mumpsincdir="$MPI_FORTRAN_MOD_DIR/MUMPS-%{_MUMPS_version} -I$MPI_INCLUDE/MUMPS" \
  --with-mumpsmoddir=$MPI_FORTRAN_MOD_DIR/MUMPS-%{_MUMPS_version} \
%if %{with superludist}
  --with-superludist=-lsuperlu_dist --with-superludistincdir=$MPI_INCLUDE/superlu_dist \
%else
  --without-superludist \
%endif
  --with-umfpack=-lumfpack --with-umfpackincdir=%{_includedir}/suitesparse
  
cp -p Make_n.inc Make.inc
# Reduce number of jobs for preventing failures
make %{?fedora: -O} %{?el8: -O} -j1 V=1
make %{?fedora: -O} %{?el8: -O} -j1 V=1 -C cbind 

# Make shared libraries
cd lib

%if 0%{?fedora}
export MPIFLIB=" -lmpifort"
%else
export MPIFLIB=" -lmpich -lfmpich " 
%endif

mpic++ %{optflags} -fPIC -shared %{__global_ldflags} -Wl,-Bdynamic -L%{_libdir} $LIBBLAS $LIBLAPACK -lstdc++ -lumfpack -lmetis -lgfortran -lm -L$MPI_LIB -Wl,-rpath -Wl,$MPI_LIB -Wl,-z,noexecstack $MPIFLIB -L$MPI_LIB -lpsb_base -lpsb_prec -lpsb_krylov -ldmumps -lcmumps -lsmumps -lzmumps %{?with_superludist:-lsuperlu_dist} -Wl,-soname,%{libname}.so.%{major_minor} -o %{libname}.so.%{major_minor} -Wl,--whole-archive %{libname}.a -Wl,-no-whole-archive
ln -sf %{libname}.so.%{major_minor} ./%{libname}.so.%{major_version}
ln -sf %{libname}.so.%{major_minor} ./%{libname}.so
cd ../
%{_mpich_unload}
popd
%endif

%install
%if 0%{?with_serial}
pushd serial-build
mkdir -p $RPM_BUILD_ROOT%{_libdir}
mkdir -p $RPM_BUILD_ROOT%{_includedir}/%{name}-serial
mkdir -p $RPM_BUILD_ROOT%{_fmoddir}/%{name}-serial

pushd lib
cp --preserve=all -P *.so* $RPM_BUILD_ROOT%{_libdir}/
install -pm 644 *.a $RPM_BUILD_ROOT%{_libdir}/
popd

install -pm 644 modules/*.mod $RPM_BUILD_ROOT%{_fmoddir}/%{name}-serial/
install -pm 644 include/*.h $RPM_BUILD_ROOT%{_includedir}/%{name}-serial/
popd
%endif

#######################################################
## Install MPI versions
%if 0%{?with_openmpi}
pushd openmpi-build
%{_openmpi_load}
mkdir -p $RPM_BUILD_ROOT$MPI_LIB
mkdir -p $RPM_BUILD_ROOT$MPI_INCLUDE/%{name}
mkdir -p $RPM_BUILD_ROOT$MPI_FORTRAN_MOD_DIR/%{name}

cd lib
cp --preserve=all -P *.so* $RPM_BUILD_ROOT$MPI_LIB/
cp --preserve=all -P *.a $RPM_BUILD_ROOT$MPI_LIB/
cd ../

install -pm 644 modules/*.mod $RPM_BUILD_ROOT$MPI_FORTRAN_MOD_DIR/%{name}/
install -pm 644 include/*.h $RPM_BUILD_ROOT$MPI_INCLUDE/%{name}/
%{_openmpi_unload}
popd
%endif

%if 0%{?with_mpich}
pushd mpich-build
%{_mpich_load}
mkdir -p $RPM_BUILD_ROOT$MPI_LIB
mkdir -p $RPM_BUILD_ROOT$MPI_INCLUDE/%{name}
mkdir -p $RPM_BUILD_ROOT$MPI_FORTRAN_MOD_DIR/%{name}

cd lib
cp --preserve=all -P *.so* $RPM_BUILD_ROOT$MPI_LIB/
cp --preserve=all -P *.a $RPM_BUILD_ROOT$MPI_LIB/
cd ../

install -pm 644 modules/*.mod $RPM_BUILD_ROOT$MPI_FORTRAN_MOD_DIR/%{name}/
install -pm 644 include/*.h $RPM_BUILD_ROOT$MPI_INCLUDE/%{name}/
%{_mpich_unload}
popd
%endif
#######################################################

%if 0%{?with_check}
%check
%if 0%{?with_serial}
pushd serial-build
export LD_LIBRARY_PATH=$RPM_BUILD_ROOT%{_libdir}
make check
popd
%endif

%if 0%{?with_openmpi}
pushd openmpi-build
%{_openmpi_load}
export LD_LIBRARY_PATH=$RPM_BUILD_ROOT$MPI_LIB
export CC=mpicc
export CXX=mpic++
export FC=mpif90
make check LINKOPT="%{__global_ldflags} -lstdc++ -L$MPI_LIB -lmpi"
%{_openmpi_unload}
popd
%endif

%if 0%{?with_mpich}
pushd mpich-build
%{_mpich_load}
export LD_LIBRARY_PATH=$RPM_BUILD_ROOT$MPI_LIB
export CC=mpicc
export CXX=mpic++
export FC=mpif90
make check LINKOPT="%{__global_ldflags} -lstdc++ -L$MPI_LIB -lmpi"
%{_mpich_unload}
popd
%endif
%endif

#######################################################

%if 0%{?with_serial}
%files serial
%{_libdir}/*.so.%{major_minor}
%{_libdir}/*.so.%{major_version}

%files serial-devel
%{_libdir}/*.so
%{_includedir}/%{name}-serial/
%{_fmoddir}/%{name}-serial/
%endif

#######################################################
## MPI versions
%if 0%{?with_openmpi}
%files openmpi
%{_libdir}/openmpi/lib/*.so.%{major_minor}
%{_libdir}/openmpi/lib/*.so.%{major_version}

%files openmpi-static
%{_libdir}/openmpi/lib/*.a

%files openmpi-devel
%{_libdir}/openmpi/lib/*.so
%{_includedir}/openmpi-%{_arch}/%{name}/
%if 0%{?fedora} || 0%{?rhel} > 7
%{_fmoddir}/openmpi/%{name}/
%else
%{_fmoddir}/openmpi-%{_arch}/%{name}/
%endif
%endif

%if 0%{?with_mpich}
%files mpich
%{_libdir}/mpich/lib/*.so.%{major_minor}
%{_libdir}/mpich/lib/*.so.%{major_version}

%files mpich-static
%{_libdir}/mpich/lib/*.a

%files mpich-devel
%{_libdir}/mpich/lib/*.so
%{_includedir}/mpich-%{_arch}/%{name}/
%if 0%{?fedora} || 0%{?rhel} > 7
%{_fmoddir}/mpich/%{name}/
%else
%{_fmoddir}/mpich-%{_arch}/%{name}/
%endif
%endif
######################################################

%files doc
%doc serial-build/README* serial-build/Changelog
%doc serial-build/docs/html serial-build/docs/*.pdf
%doc serial-build/ReleaseNews
%license serial-build/LICENSE

%changelog
* Sat Jan 18 2025 Antonio Trande <sagitter@fedoraproject.org> - 1.1.2-8
- Fix GCC15 builds

* Thu Jan 16 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.2-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Wed Jul 17 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Sun Feb 04 2024 Orion Poplawski <orion@nwra.com> - 1.1.2-5
- Rebuild with suitesparse 7.6.0

* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sat Jan 06 2024 Antonio Trande <sagitter@fedoraproject.org> - 1.1.2-2
- Rebuild for MUMPS-5.6.2

* Sat Dec 16 2023 Antonio Trande <sagitter@fedoraproject.org> - 1.1.2-1
- Release 1.1.2
- Exclude serial libraries (not fully supported)

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Fri Jul 07 2023 Antonio Trande <sagitter@fedoraproject.org> - 1.1.0-6
- Rebuild for SuperLU-6.0

* Tue Feb 07 2023 Antonio Trande <sagitter@fedoraproject.org> - 1.1.0-5
- Drop OpenMPI support on i686

* Wed Jan 18 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Wed Jul 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Sun Jul 17 2022 Antonio Trande <sagitter@fedoraproject.org> - 1.1.0-2
- Rebuild for MUMPS-5.5.0

* Fri Jun 17 2022 Antonio Trande <sagitter@fedoraproject.org> - 1.1.0-1
- Release 1.1.0

* Sat Apr 23 2022 Antonio Trande <sagitter@fedoraproject.org> - 1.0.1-2
- Rebuild for superlu_dist-7.2.0

* Mon Apr 18 2022 Antonio Trande <sagitter@fedoraproject.org> - 1.0.1-1
- Release 1.0.1

* Wed Jan 19 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Sat Oct 30 2021 Antonio Trande <sagitter@fedoraproject.org> - 1.0.0-5
- Rebuild for SuperLU-5.3.0

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Sat Jul 17 2021 Antonio Trande <sagitter@fedoraproject.org> - 1.0.0-3
- Rebuild for MUMPS-5.4.0

* Fri May 21 2021 Antonio Trande <sagitter@fedoraproject.org> - 1.0.0-2
- Fix installation issue

* Thu May 20 2021 Antonio Trande <sagitter@fedoraproject.org> - 1.0.0-1
- First package
