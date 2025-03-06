# Copyright (c) 2014  Dave Love, University of Liverpool
# Copyright (c) 2018  Dave Love, University of Manchester
# MIT licence, per Fedora policy

%if 0%{?fedora} >= 40
%ifarch %{ix86}
%bcond_with openmpi
%else
%bcond_without openmpi
%endif
%else
%bcond_without openmpi
%endif

%bcond_without mpich
%bcond_without check
%bcond_without docs

%global somajor 2
%global soversion %{somajor}.1

Name:           hypre
Version:        2.32.0
Release:        %autorelease
Summary:        High performance matrix preconditioners
License:        Apache-2.0 OR MIT
URL:            http://www.llnl.gov/casc/hypre/
Source:         https://github.com/hypre-space/hypre/archive/v%version/%{name}-%{version}.tar.gz
# Don't use hostname for tests and use two MPI processes
Patch2:         hypre-2.32.0-test.patch

Patch3:         hypre-2.32.0_request_156.patch

BuildRequires:  gcc-c++
BuildRequires:  gcc-gfortran
#BuildRequires:  automake
BuildRequires:  cmake
#BuildRequires:  libtool
#BuildRequires:  libtool-ltdl-devel
BuildRequires:  make
BuildRequires:  SuperLU-devel
BuildRequires:  flexiblas-devel
%if %{with docs}
BuildRequires:  doxygen-latex
BuildRequires:  python3-sphinx
BuildRequires:  python3-sphinx-theme-alabaster
BuildRequires:  python3-sphinx_rtd_theme
BuildRequires:  python3-breathe
BuildRequires:  python3-sphinx-latex
BuildRequires:  /usr/bin/latexmk
BuildRequires:  tex(threeparttable.sty)
BuildRequires:  tex(hanging.sty)
BuildRequires:  tex(adjustbox.sty)
BuildRequires:  tex(fncychap.sty)
BuildRequires:  tex(tabulary.sty)
BuildRequires:  tex(capt-of.sty)
BuildRequires:  tex(needspace.sty)
BuildRequires:  tex(stackengine.sty)
BuildRequires:  tex(listofitems.sty)
BuildRequires:  tex(ulem.sty)
BuildRequires:  tex(etoc.sty)
%endif

%global desc \
Hypre is a set of matrix preconditioning libraries to aid in the\
solution of large systems of linear equations.

%description
%desc

%package devel
Summary:        Development files for %name
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       SuperLU-devel%{?_isa} 
Requires:       flexiblas-devel%{?_isa}

%description devel
Development files for %name

%if %{with openmpi}
%package openmpi
Summary:        High performance matrix preconditioners - openmpi
Requires:       openmpi%{?_isa}
BuildRequires:  superlu_dist-openmpi-devel
BuildRequires:  ptscotch-openmpi-devel

%description openmpi
%desc

This is the openmpi version.

%package openmpi-devel
Summary:        Development files for %name-openmpi
Requires:       %{name}-openmpi%{?_isa} = %{version}-%{release}
Requires:       openmpi-devel%{?_isa}
Requires:       superlu_dist-openmpi-devel%{?_isa}
Requires:       ptscotch-openmpi-devel%{?_isa}
Requires:       flexiblas-devel%{?_isa}

%description openmpi-devel
Development files for %name-openmpi
%endif

%if %{with mpich}
%package mpich
Summary:        High performance matrix preconditioners - mpich
Requires:       mpich%{?_isa}
BuildRequires:  superlu_dist-mpich-devel ptscotch-mpich-devel

%description mpich
%desc

This is the mpich version.

%package mpich-devel
Summary:        Development files for %name-mpich
Requires:       %{name}-mpich%{?_isa} = %{version}-%{release}
Requires:       mpich-devel%{?_isa}
Requires:       superlu_dist-mpich-devel%{?_isa}
Requires:       ptscotch-mpich-devel%{?_isa}
Requires:       flexiblas-devel%{?_isa}

%description mpich-devel
Development files for %name-mpich
%endif

%if %{with docs}
%package doc
Summary:        Documentation for hypre
BuildArch:      noarch

%description doc
Documentation for hypre
%endif


%prep
%setup -q -n %name-%version
%patch -P 2 -p1 -b .test
%patch -P 3 -p1 -b .backup

find \( -name \*.[ch] -o -name \*.cxx \) -perm /=x -exec chmod 0644 {} \;

%if %{with openmpi}
cp -a src openmpi
%endif
%if %{with mpich}
cp -a src mpich
%endif

%build
%if %{with docs}
pushd src
%configure
make -C docs
rm docs/usr-manual-html/.buildinfo
popd
%endif

pushd src/cmbuild
%cmake -S .. \
       -DHYPRE_WITH_EXTRA_CFLAGS:STRING=" -O3" -DCMAKE_SHARED_LINKER_FLAGS_RELEASE:STRING="%{__global_ldflags} -lsuperlu -fopenmp" \
       -DHYPRE_BUILD_EXAMPLES:BOOL=ON -DHYPRE_BUILD_TESTS:BOOL=ON -DHYPRE_BUILD_TYPE:STRING=Release \
       -DHYPRE_ENABLE_SHARED:BOOL=ON -DHYPRE_WITH_OPENMP:BOOL=ON \
       -DHYPRE_SEQUENTIAL:BOOL=ON -DHYPRE_WITH_MPI:BOOL=OFF -DHYPRE_WITH_DSUPERLU:BOOL=OFF \
       -DHYPRE_WITH_SUPERLU:BOOL=ON -DTPL_SUPERLU_INCLUDE_DIRS:FILEPATH=%{_includedir}/SuperLU -DTPL_SUPERLU_LIBRARIES:STRING=%{_libdir}/libsuperlu.so \
       -DTPL_BLAS_LIBRARIES:STRING=-lflexiblas \
       -DHYPRE_WITH_OPENMP:BOOL=ON -DHYPRE_TIMING:BOOL=ON -DHYPRE_INSTALL_PREFIX:PATH=%{_libdir} -DHYPRE_INSTALL_INCLUDEDIR:PATH=%{_includedir}/%{name}
%cmake_build
popd

%if %{with openmpi}
pushd openmpi/cmbuild
%_openmpi_load
export CC=$MPI_BIN/mpicc
%cmake -S .. \
       -DHYPRE_WITH_EXTRA_CFLAGS:STRING=" -O3" -DCMAKE_SHARED_LINKER_FLAGS_RELEASE:STRING="%{__global_ldflags} -fopenmp -lsuperlu_dist -lptscotch" \
       -DHYPRE_BUILD_EXAMPLES:BOOL=ON -DHYPRE_BUILD_TESTS:BOOL=ON -DHYPRE_BUILD_TYPE:STRING=Release \
       -DHYPRE_ENABLE_SHARED:BOOL=ON -DHYPRE_WITH_OPENMP:BOOL=ON \
       -DHYPRE_SEQUENTIAL:BOOL=OFF -DHYPRE_WITH_MPI:BOOL=ON -DMPI_C_COMPILER:FILEPATH=$MPI_BIN/mpicc \
       -DHYPRE_WITH_SUPERLU:BOOL=ON -DTPL_SUPERLU_INCLUDE_DIRS:FILEPATH=$MPI_INCLUDE/superlu_dist -DTPL_SUPERLU_LIBRARIES:STRING=$MPI_LIB/libsuperlu_dist.so \
       -DTPL_BLAS_LIBRARIES:STRING=-lflexiblas \
       -DHYPRE_WITH_OPENMP:BOOL=ON -DHYPRE_TIMING:BOOL=ON -DHYPRE_INSTALL_PREFIX:PATH=%{_libdir}/openmpi/lib  -DHYPRE_INSTALL_INCLUDEDIR:PATH=$MPI_INCLUDE/%{name}
%cmake_build
popd
%_openmpi_unload
%endif

%if %{with mpich}
pushd mpich/cmbuild
%_mpich_load
export CC=$MPI_BIN/mpicc
%cmake -S .. \
       -DHYPRE_WITH_EXTRA_CFLAGS:STRING=" -O3" -DCMAKE_SHARED_LINKER_FLAGS_RELEASE:STRING="%{__global_ldflags} -fopenmp -lsuperlu_dist -lptscotch" \
       -DHYPRE_BUILD_EXAMPLES:BOOL=ON -DHYPRE_BUILD_TESTS:BOOL=ON -DHYPRE_BUILD_TYPE:STRING=Release \
       -DHYPRE_ENABLE_SHARED:BOOL=ON -DHYPRE_WITH_OPENMP:BOOL=ON \
       -DHYPRE_SEQUENTIAL:BOOL=OFF -DHYPRE_WITH_MPI:BOOL=ON -DMPI_C_COMPILER:FILEPATH=$MPI_BIN/mpicc \
       -DHYPRE_WITH_SUPERLU:BOOL=ON -DTPL_SUPERLU_INCLUDE_DIRS:FILEPATH=$MPI_INCLUDE/superlu_dist -DTPL_SUPERLU_LIBRARIES:STRING=$MPI_LIB/libsuperlu_dist.so \
       -DTPL_BLAS_LIBRARIES:STRING=-lflexiblas \
       -DHYPRE_WITH_OPENMP:BOOL=ON -DHYPRE_TIMING:BOOL=ON -DHYPRE_INSTALL_PREFIX:PATH=%{_libdir}/mpich/lib -DHYPRE_INSTALL_INCLUDEDIR:PATH=$MPI_INCLUDE/%{name}
%cmake_build
%_mpich_unload
popd
%endif


%check
%if %{with check}
pushd src/cmbuild/%_vpath_builddir/test
export LD_LIBRARY_PATH=%{buildroot}%{_libdir}
./ij*
popd
%if %{with openmpi}
pushd openmpi/cmbuild/%_vpath_builddir/test
export LD_LIBRARY_PATH=%{buildroot}%{_libdir}/openmpi/lib
%_openmpi_load
./ij*
%_openmpi_unload
popd
%endif
%if %{with mpich}
pushd mpich/cmbuild/%_vpath_builddir/test
export LD_LIBRARY_PATH=%{buildroot}%{_libdir}/mpich/lib
%_mpich_load
./ij*
%_mpich_unload
popd
%endif
%endif


%install
pushd src/cmbuild
%cmake_install
popd

%if %{with openmpi}
pushd openmpi/cmbuild
%_openmpi_load
%cmake_install
%_openmpi_unload
popd
%endif

%if %{with mpich}
pushd mpich/cmbuild
%_mpich_load
%cmake_install
%_mpich_unload
popd
%endif

%files
%doc CHANGELOG README.md
%license COPYRIGHT LICENSE-*
%{_libdir}/libHYPRE.so.%{somajor}*

%files devel
%{_libdir}/libHYPRE.so
%{_includedir}/%{name}/
%{_libdir}/cmake/HYPRE/

%if %{with openmpi}
%files openmpi
%doc CHANGELOG README.md
%license COPYRIGHT LICENSE-*
%{_libdir}/openmpi/lib/libHYPRE.so.%{somajor}*

%files openmpi-devel
%{_libdir}/openmpi/lib/libHYPRE.so
%{_includedir}/openmpi-%_arch/%{name}
%{_libdir}/openmpi/lib/cmake/HYPRE/
%endif

%if %{with mpich}
%files mpich
%doc CHANGELOG README.md
%license COPYRIGHT LICENSE-*
%{_libdir}/mpich/lib/libHYPRE.so.%{somajor}*

%files mpich-devel
%{_libdir}/mpich/lib/libHYPRE.so
%{_includedir}/mpich-%_arch/%{name}
%{_libdir}/mpich/lib/cmake/HYPRE/
%endif

%if %{with docs}
%files doc
%doc CHANGELOG README.md src/examples
%license COPYRIGHT LICENSE-*
%doc src/docs/usr-manual/*.pdf src/docs/*-manual-html
%endif

%changelog
%autochangelog
