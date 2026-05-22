%global genname superlumt
%global majorver 4.0
%global soname_version %{version}

%ifarch %{ix86}
%bcond_with longint
%else
%bcond_without longint
%endif

%bcond_without check

Name: SuperLUMT
Version: %{majorver}.2
Release: %autorelease
Summary: Single precision real SuperLU routines for shared memory parallel machines
License: BSD-3-Clause
URL: https://portal.nersc.gov/project/sparse/superlu/
Source0: https://github.com/xiaoyeli/superlu_mt/archive/refs/tags/v%{version}/superlu_mt-%{version}.tar.gz

BuildRequires: cmake
BuildRequires: make
BuildRequires: pkgconfig(flexiblas)
BuildRequires: pkgconfig
BuildRequires: tcsh
BuildRequires: gcc
BuildRequires: gcc-gfortran
Requires: %{name}-common = %{version}-%{release}

# This patch removes the `_OPENMP` suffix and produces a versioned library
Patch0: %{name}-rename_shared_libraries.patch

# This patch produces a versioned 64bit library
Patch1: %{name}64-build_shared.patch

# https://github.com/xiaoyeli/superlu_mt/commit/e60ed2c1dd491e1832d783f519c1851288f9d422
Patch2: %{name}64-resolve_prototype_mismatches.patch

%description
Subroutines to solve sparse linear systems for shared memory parallel machines.
SuperLU contains a set of subroutines to solve a sparse linear system 
A*X=B. It uses Gaussian elimination with partial pivoting (GEPP). 
The columns of A may be preordered before factorization; the 
preordering for sparsity is completely separate from the factorization.


%package devel
Summary: The SuperLUMT headers and development-related files
Requires: %{name}%{?_isa} = %{version}-%{release}
Obsoletes: SuperLUMT-double < 0:4.0.2-1
Obsoletes: SuperLUMT-complex < 0:4.0.2-1
Obsoletes: SuperLUMT-complex16 < 0:4.0.2-1
%description devel
Shared links and header files used by SuperLUMT.

########################################################
%if %{with longint}
%package -n SuperLUMT64
Summary: Single precision real SuperLU routines (64bit INTEGER)
# Upstream: SuperLU_MT always uses 32-bit BLAS, even when LONINT is defined.
BuildRequires: pkgconfig(flexiblas)
Requires: %{name}-common = %{version}-%{release}
%description -n SuperLUMT64
Subroutines to solve sparse linear systems for shared memory parallel machines
(64bit INTEGER).
SuperLU contains a set of subroutines to solve a sparse linear system 
A*X=B. It uses Gaussian elimination with partial pivoting (GEPP). 
The columns of A may be preordered before factorization; the 
preordering for sparsity is completely separate from the factorization.

%package -n SuperLUMT64-devel
Summary: The SuperLUMT64 headers and development-related files (64bit INTEGER)
Obsoletes: SuperLUMT64-double < 0:4.0.2-1
Obsoletes: SuperLUMT64-complex < 0:4.0.2-1
Obsoletes: SuperLUMT64-complex16 < 0:4.0.2-1
%description -n SuperLUMT64-devel
Shared links, header files for SuperLUMT (64bit INTEGER).
%endif
##########################################################

%package common
Summary: Documentation files for SuperLUMT

BuildArch: noarch
%description common
This package contains common documentation files for SuperLUMT.

%prep
%setup -qc

find . -type f | sed -e "/TESTING/d" | xargs chmod a-x

# Remove the shippped executables from EXAMPLE
find EXAMPLE -type f | while read file
do
   [ "$(file $file | awk '{print $2}')" = ELF ] && rm $file || :
done

# Remove bundled CBLAS source files
rm -rf CBLAS

pushd superlu_mt-%{version}
%patch -P 0 -p1 -b .backup0
%patch -P 2 -p1 -b .backup2
popd

%if %{with longint}
cp -a superlu_mt-%{version} superlu_mt64-%{version}
pushd superlu_mt64-%{version}
%patch -P 1 -p1 -b .backup1
popd
%endif

%build
## Build 32bit library ##
pushd superlu_mt-%{version}
export LDFLAGS="%{__global_ldflags} -fPIC"
export CFLAGS="$RPM_OPT_FLAGS -std=gnu17 -fPIC -fopenmp -I%{_includedir}/flexiblas"
%cmake -DPLAT:STRING=_OPENMP -DSUPERLUMT_INSTALL_INCLUDEDIR:STRING=%{_includedir}/%{name} \
       -Denable_fortran:BOOL=ON -DCMAKE_EXE_LINKER_FLAGS:STRING=-Wl,--copy-dt-needed-entries \
       -DBLAS_flexiblas_LIBRARY:FILEPATH=%{_libdir}/libflexiblas.so \
       -DCMAKE_SKIP_RPATH:BOOL=ON -DCMAKE_SKIP_INSTALL_RPATH:BOOL=ON -DLONGINT:BOOL=OFF \
%if %{without check}
       -Denable_tests:BOOL=OFF -Denable_examples:BOOL=OFF
%endif
%cmake_build
popd
#########################

## Build 64bit library ##
%if %{with longint}
pushd superlu_mt64-%{version}
export LDFLAGS="%{__global_ldflags} -fPIC -lflexiblas"
export CFLAGS="$RPM_OPT_FLAGS -std=gnu17 -fPIC -fopenmp -I%{_includedir}/flexiblas"
%cmake -DPLAT:STRING=_OPENMP -DSUPERLUMT_INSTALL_INCLUDEDIR:STRING=%{_includedir}/%{name}64 \
       -Denable_fortran:BOOL=ON -DCMAKE_EXE_LINKER_FLAGS:STRING=-Wl,--copy-dt-needed-entries \
       -DLONGINT:BOOL=ON -DBLAS_flexiblas_LIBRARY:FILEPATH=%{_libdir}/libflexiblas.so \
       -DCMAKE_SKIP_RPATH:BOOL=ON -DCMAKE_SKIP_INSTALL_RPATH:BOOL=ON \
%if %{without check}
       -Denable_tests:BOOL=OFF -Denable_examples:BOOL=OFF
%endif
%cmake_build
popd
%endif
##########################

%if %{with check}
%check
pushd superlu_mt-%{version}
export LD_LIBRARY_PATH=%{buildroot}%{_libdir}:MATGEN
%ctest
popd

%if %{with longint}
pushd superlu_mt64-%{version}
export LD_LIBRARY_PATH=%{buildroot}%{_libdir}:MATGEN
%ctest
popd
%endif
%endif

%install
pushd superlu_mt-%{version}
%cmake_install
popd

%if %{with longint}
pushd superlu_mt64-%{version}
%cmake_install
popd
%endif

%files
%{_libdir}/libsuperlu_mt.so.4
%{_libdir}/libsuperlu_mt.so.%{majorver}

%files devel
%{_includedir}/%{name}/
%{_libdir}/libsuperlu_mt.so

%if %{with longint}
%files -n SuperLUMT64
%{_libdir}/libsuperlu_mt64.so.4
%{_libdir}/libsuperlu_mt64.so.%{majorver}

%files -n SuperLUMT64-devel
%{_includedir}/%{name}64/
%{_libdir}/libsuperlu_mt64.so
%endif

%files common
%license superlu_mt-%{version}/License.txt
%doc superlu_mt-%{version}/DOC superlu_mt-%{version}/README

%changelog
%autochangelog
