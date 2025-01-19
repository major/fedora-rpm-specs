# This flag breaks the linkage among libraries
%undefine _ld_as_needed

%global genname superlumt
%global majorver 4.0
%global soname_version %{majorver}.1

Name: SuperLUMT
Version: %{majorver}.1
Release: %autorelease
Summary: Single precision real SuperLU routines for shared memory parallel machines
License: BSD-3-Clause
URL: https://portal.nersc.gov/project/sparse/superlu/
Source0: https://github.com/xiaoyeli/superlu_mt/archive/refs/tags/v%{majorver}.1/superlu_mt-%{majorver}.1.tar.gz

BuildRequires: make
BuildRequires: pkgconfig(flexiblas)
BuildRequires: pkgconfig
BuildRequires: tcsh
BuildRequires: gcc
Requires: %{name}-common = %{version}-%{release}

# Patches to build shared object libraries
# and files for testing
Patch0: %{name}-build_shared.patch
Patch1: %{name}-fix_testsuite.patch
Patch2: %{name}64-build_shared.patch
Patch3: %{name}64-fix_testsuite.patch
Patch4: %{name}-fix_examples.patch
Patch5: %{name}64-fix_examples.patch
Patch6: %{name}-fix_several_prototype_errors.patch

%description
Subroutines to solve sparse linear systems for shared memory parallel machines.
SuperLU contains a set of subroutines to solve a sparse linear system 
A*X=B. It uses Gaussian elimination with partial pivoting (GEPP). 
The columns of A may be preordered before factorization; the 
preordering for sparsity is completely separate from the factorization.


%package double
Summary: Double precision real SuperLU routines for shared memory parallel machines
Requires: %{name}-common = %{version}-%{release}
%description double
This package contains double precision real SuperLU routines library
by SuperLUMT.


%package complex
Summary: Single precision complex SuperLU routines for shared memory parallel machines
Requires: %{name}-common = %{version}-%{release}
%description complex
This package contains single precision complex routines library by SuperLUMT.


%package complex16
Summary: Double precision complex SuperLU routines for shared memory parallel machines
Requires: %{name}-common = %{version}-%{release}
%description complex16
This package contains double precision complex routines library by SuperLUMT.


%package devel
Summary: The SuperLUMT headers and development-related files
Requires: %{name}%{?_isa} = %{version}-%{release}
Requires: %{name}-double%{?_isa} = %{version}-%{release}
Requires: %{name}-complex%{?_isa} = %{version}-%{release}
Requires: %{name}-complex16%{?_isa} = %{version}-%{release}

%description devel
Shared links and header files used by SuperLUMT.

########################################################
%if %{?__isa_bits:%{__isa_bits}}%{!?__isa_bits:32} == 64
%package -n SuperLUMT64
Summary: Single precision real SuperLU routines (64bit INTEGER)

BuildRequires: pkgconfig(flexiblas)
Requires: %{name}-common = %{version}-%{release}
%description -n SuperLUMT64
Subroutines to solve sparse linear systems for shared memory parallel machines
(64bit INTEGER).
SuperLU contains a set of subroutines to solve a sparse linear system 
A*X=B. It uses Gaussian elimination with partial pivoting (GEPP). 
The columns of A may be preordered before factorization; the 
preordering for sparsity is completely separate from the factorization.


%package -n SuperLUMT64-double
Summary: Double precision real SuperLU routines (64bit INTEGER)

Requires: %{name}-common = %{version}-%{release}
%description -n SuperLUMT64-double
This package contains double precision real SuperLU routines library
by SuperLUMT (64bit INTEGER).


%package -n SuperLUMT64-complex
Summary: Single precision complex SuperLU routines (64bit INTEGER)
Requires: %{name}-common = %{version}-%{release}
%description -n SuperLUMT64-complex
This package contains single precision complex routines library by SuperLUMT
(64bit INTEGER).


%package -n SuperLUMT64-complex16
Summary: Double precision complex SuperLU routines (64bit INTEGER)
Requires: %{name}-common = %{version}-%{release}
%description -n SuperLUMT64-complex16
This package contains double precision complex routines library
by SuperLUMT (64bit INTEGER).

%package -n SuperLUMT64-devel
Summary: The MUMPS headers and development-related files (64bit INTEGER)
Requires: SuperLUMT64%{?_isa} = %{version}-%{release}
Requires: SuperLUMT64-double%{?_isa} = %{version}-%{release}
Requires: SuperLUMT64-complex%{?_isa} = %{version}-%{release}
Requires: SuperLUMT64-complex16%{?_isa} = %{version}-%{release}

%description -n SuperLUMT64-devel
Shared links, header files for %{name} (64bit INTEGER).
%endif
##########################################################

%package common
Summary: Documentation files for SuperLUMT

BuildArch: noarch
%description common
This package contains common documentation files for SuperLUMT.

%prep
%setup -q -n superlu_mt-%{majorver}.1

rm -fr SRC/mc64ad.f.bak
find . -type f | sed -e "/TESTING/d" | xargs chmod a-x
# Remove the shippped executables from EXAMPLE
find EXAMPLE -type f | while read file
do
   [ "$(file $file | awk '{print $2}')" = ELF ] && rm $file || :
done

mkdir -p lib

# Duplicating of examples source code
%if %{?__isa_bits:%{__isa_bits}}%{!?__isa_bits:32} == 64
cp -a EXAMPLE EXAMPLE64
%endif

%patch -P 0 -p0
%patch -P 1 -p0
%patch -P 4 -p0
%patch -P 6 -p1

%build
cp -p MAKE_INC/make.linux.openmp make.inc
sed -i -e "s|-O3|$RPM_OPT_FLAGS -std=gnu17|" \
make.inc

## Build lib ##########################################
export LIBBLASLINK=-lflexiblas
export LDFLAGS="%{__global_ldflags} -lgomp $LIBBLASLINK"

make -j1 \
 SONAME=%{majorver} \
 BLASLIB="-L%{_libdir} $LIBBLASLINK" \
 PREDEFS="$RPM_OPT_FLAGS $LDFLAGS -fPIC -D__OPENMP -DPRNTlevel=0 -DDEBUGlevel=0" \
 NOOPTS="-O0 -fPIC -fopenmp $LIBBLASLINK" \
 CDEFS=-DAdd_ \
 FFLAGS="$RPM_OPT_FLAGS $LDFLAGS -fPIC -fopenmp -D__OPENMP -DPRNTlevel=0 -DDEBUGlevel=0" \
 FORTRAN=gfortran \
 LOADER=gcc \
 CC=gcc \
 CFLAGS="$RPM_OPT_FLAGS -std=gnu17 $LDFLAGS -fPIC -D__OPENMP -DPRNTlevel=0 -DDEBUGlevel=0" \
 LDFLAGS="%{__global_ldflags} -lgomp $LIBBLASLINK" \
 MATHLIB=-lm \
 MPLIB= -C SRC single double complex complex16
 
cp -p SRC/libsuperlumt_*.so.%{majorver} lib/
cp -p SRC/libsuperlumt_*.so lib/

# Make example files
export LIBBLASLINK=-lflexiblas
export LDFLAGS="%{__global_ldflags} -lgomp $LIBBLASLINK"

make -j1 \
 SONAME=%{majorver} \
 BLASLIB="-L%{_libdir} $LIBBLASLINK" \
 PREDEFS="$RPM_OPT_FLAGS $LDFLAGS -fPIC -D__OPENMP -DPRNTlevel=0 -DDEBUGlevel=0" \
 NOOPTS="-O0 -fPIC -fopenmp $LIBBLASLINK" \
 CDEFS=-DAdd_ \
 FFLAGS="$RPM_OPT_FLAGS $LDFLAGS -fPIC -fopenmp -D__OPENMP -DPRNTlevel=0 -DDEBUGlevel=0" \
 FORTRAN=gfortran \
 LOADER=gcc \
 LOADOPTS="$RPM_OPT_FLAGS $LDFLAGS -fPIC -D__OPENMP -DPRNTlevel=0 -DDEBUGlevel=0" \
 CC=gcc \
 CFLAGS="$RPM_OPT_FLAGS -std=gnu17 $LDFLAGS -fPIC -D__OPENMP -DPRNTlevel=0 -DDEBUGlevel=0" \
 LDFLAGS="%{__global_ldflags} -lgomp $LIBBLASLINK" \
 MATHLIB=-lm \
 MPLIB= -C EXAMPLE single double complex complex16

make -C SRC clean
make -C TESTING/MATGEN clean
#######################################################

## Build 64 ##########################################
%if %{?__isa_bits:%{__isa_bits}}%{!?__isa_bits:32} == 64
# Reverting previous patches
# and patch again for new libraries
patch -R -p0 < %{PATCH0}
patch -R -p0 < %{PATCH1}
patch -p0 < %{PATCH2}
patch -p0 < %{PATCH3}
patch -p0 < %{PATCH5}

export LIBBLASLINK=-lflexiblas64
export LDFLAGS="%{__global_ldflags} -lgomp $LIBBLASLINK"

make -j1 \
 SONAME=%{majorver} \
 BLASLIB="-L%{_libdir} $LIBBLASLINK" \
 PREDEFS="$RPM_OPT_FLAGS $LDFLAGS -fPIC -D__OPENMP -DPRNTlevel=0 -DDEBUGlevel=0 -D_LONGINT" \
 NOOPTS="-O0 -fPIC -fopenmp $LIBBLASLINK" \
 CDEFS=-DAdd_ \
 FFLAGS="$RPM_OPT_FLAGS $LDFLAGS -fPIC -fopenmp -D__OPENMP -DPRNTlevel=0 -DDEBUGlevel=0 -fdefault-integer-8" \
 FORTRAN=gfortran \
 CFLAGS="$RPM_OPT_FLAGS -std=gnu17 $LDFLAGS -fPIC -D__OPENMP -DPRNTlevel=0 -DDEBUGlevel=0 -D_LONGINT" \
 LOADER=gcc \
 CC=gcc \
 LDFLAGS="%{__global_ldflags} -lgomp $LIBBLASLINK" \
 MATHLIB=-lm \
 MPLIB= -C SRC single double complex complex16

cp -p SRC/libsuperlumt64_*.so.%{majorver} lib/
cp -p SRC/libsuperlumt64_*.so lib/

# Make example files

export LIBBLASLINK=-lflexiblas64
export LDFLAGS="%{__global_ldflags} -lgomp $LIBBLASLINK"

make -j1 \
 SONAME=%{majorver} \
 BLASLIB="-L%{_libdir} $LIBBLASLINK" \
 PREDEFS="$RPM_OPT_FLAGS $LDFLAGS -fPIC -D__OPENMP -DPRNTlevel=0 -DDEBUGlevel=0 -D_LONGINT" \
 NOOPTS="-O0 -fPIC -fopenmp $LIBBLASLINK" \
 CDEFS=-DAdd_ \
 FFLAGS="$RPM_OPT_FLAGS $LDFLAGS -fPIC -fopenmp -D__OPENMP -DPRNTlevel=0 -DDEBUGlevel=0 -fdefault-integer-8" \
 FORTRAN=gfortran \
 CFLAGS="$RPM_OPT_FLAGS -std=gnu17 $LDFLAGS -fPIC -D__OPENMP -DPRNTlevel=0 -DDEBUGlevel=0 -D_LONGINT" \
 LOADER=gcc \
 LOADOPTS="$RPM_OPT_FLAGS $LDFLAGS -fPIC -D__OPENMP -DPRNTlevel=0 -DDEBUGlevel=0 -D_LONGINT" \
 CC=gcc \
 LDFLAGS="%{__global_ldflags} -lgomp $LIBBLASLINK" \
 MATHLIB=-lm \
 MPLIB= -C EXAMPLE64 single double complex complex16
%endif

%check
pushd EXAMPLE
export LD_LIBRARY_PATH=%{buildroot}%{_libdir}:%{_libdir}
./pslinsol < big.rua
./pdlinsol < big.rua
./pclinsol < cmat
./pzlinsol < cmat
./pslinsolx < big.rua
./pdlinsolx < big.rua
./pclinsolx < cmat
./pzlinsolx < cmat
./pslinsolx1 < big.rua
./pdlinsolx1 < big.rua
./pclinsolx1 < cmat
./pzlinsolx1 < cmat
popd

%if %{?__isa_bits:%{__isa_bits}}%{!?__isa_bits:32} == 64
pushd EXAMPLE64
export LD_LIBRARY_PATH=%{buildroot}%{_libdir}:%{_libdir}
./pslinsol < big.rua
./pdlinsol < big.rua
./pclinsol < cmat
./pzlinsol < cmat
popd
%endif

%install
mkdir -p %{buildroot}%{_libdir}
mkdir -p %{buildroot}%{_includedir}/%{name}
cp -P lib/libsuperlumt_*.so.%{majorver} %{buildroot}%{_libdir}/
install -p SRC/*.h %{buildroot}%{_includedir}/%{name}/
chmod a-x %{buildroot}%{_includedir}/%{name}/*.h
cp -P lib/libsuperlumt_*.so %{buildroot}%{_libdir}/

for i in s d c z
do
 ln -sf  libsuperlumt_${i}.so.%{majorver} %{buildroot}%{_libdir}/libsuperlumt_${i}.so
done

%if %{?__isa_bits:%{__isa_bits}}%{!?__isa_bits:32} == 64
cp -P lib/libsuperlumt64_*.so.%{majorver} %{buildroot}%{_libdir}/
cp -P lib/libsuperlumt64_*.so %{buildroot}%{_libdir}/

for i in s d c z
do
 ln -sf  libsuperlumt64_${i}.so.%{majorver} %{buildroot}%{_libdir}/libsuperlumt64_${i}.so
done
%endif

%files
%{_libdir}/libsuperlumt_s.so.%{majorver}

%files double
%{_libdir}/libsuperlumt_d.so.%{majorver}

%files complex
%{_libdir}/libsuperlumt_c.so.%{majorver}

%files complex16
%{_libdir}/libsuperlumt_z.so.%{majorver}

%files devel
%{_includedir}/%{name}/
%{_libdir}/libsuperlumt_*.so

########################################################
%if %{?__isa_bits:%{__isa_bits}}%{!?__isa_bits:32} == 64
%files -n SuperLUMT64
%{_libdir}/libsuperlumt64_s.so.%{majorver}

%files -n SuperLUMT64-double
%{_libdir}/libsuperlumt64_d.so.%{majorver}

%files -n SuperLUMT64-complex
%{_libdir}/libsuperlumt64_c.so.%{majorver}

%files -n SuperLUMT64-complex16
%{_libdir}/libsuperlumt64_z.so.%{majorver}

%files -n SuperLUMT64-devel
%{_includedir}/%{name}/
%{_libdir}/libsuperlumt64_*.so
%endif
#######################################################

%files common
%license License.txt
%doc DOC README

%changelog
%autochangelog
