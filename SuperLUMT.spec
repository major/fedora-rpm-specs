# This flag breaks the linkage among libraries
%undefine _ld_as_needed

%global genname superlumt
%global majorver 3.1

%global soname_version %{majorver}.0

%if %{?__isa_bits:%{__isa_bits}}%{!?__isa_bits:32} == 64
%global arch64 1
%global complex 1
%else
%global arch64 0
%global complex 0
%endif

%if 0%{?el7}
%global dts devtoolset-8-
%endif

Name: SuperLUMT
Version: 3.1.0
Release: 33%{?dist}
Summary: Single precision real SuperLU routines for shared memory parallel machines
License: BSD
URL: http://crd-legacy.lbl.gov/~xiaoye/SuperLU/
Source0: http://crd-legacy.lbl.gov/~xiaoye/SuperLU/superlu_mt_%{majorver}.tar.gz

BuildRequires: make
%if 0%{?fedora} >= 33
BuildRequires: pkgconfig(flexiblas)
%else
BuildRequires: openblas-devel, openblas-srpm-macros
%endif
BuildRequires: pkgconfig
BuildRequires: tcsh
BuildRequires: %{?dts}gcc

# Patches to build shared object libraries
# and files for testing
Patch0: %{name}-build_shared.patch
Patch1: %{name}-fix_testsuite.patch
Patch2: %{name}64-build_shared.patch
Patch3: %{name}64-fix_testsuite.patch
Patch4: %{name}-fix_examples.patch
Patch5: %{name}64-fix_examples.patch

Requires: %{name}-common = %{version}-%{release}

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

%if 0%{?complex}
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
%endif

%package devel
Summary: The SuperLUMT headers and development-related files

Requires: %{name}%{?_isa} = %{version}-%{release}
Requires: %{name}-double%{?_isa} = %{version}-%{release}
%if 0%{?complex}
Requires: %{name}-complex%{?_isa} = %{version}-%{release}
Requires: %{name}-complex16%{?_isa} = %{version}-%{release}
%endif
%description devel
Shared links and header files used by SuperLUMT.

########################################################
%if 0%{?rhel} >= 7 || 0%{?fedora}
%if 0%{?arch64}
%package -n SuperLUMT64
Summary: Single precision real SuperLU routines (64bit INTEGER)

%if 0%{?fedora} >= 33
BuildRequires: pkgconfig(flexiblas)
%else
BuildRequires: openblas-devel, openblas-srpm-macros
%endif
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

%if 0%{?complex}
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
%endif

%package -n SuperLUMT64-devel
Summary: The MUMPS headers and development-related files (64bit INTEGER)

Requires: SuperLUMT64%{?_isa} = %{version}-%{release}
Requires: SuperLUMT64-double%{?_isa} = %{version}-%{release}
%if 0%{?complex}
Requires: SuperLUMT64-complex%{?_isa} = %{version}-%{release}
Requires: SuperLUMT64-complex16%{?_isa} = %{version}-%{release}
%endif
%description -n SuperLUMT64-devel
Shared links, header files for %{name} (64bit INTEGER).
%endif
%endif
##########################################################

%package common
Summary: Documentation files for SuperLUMT

BuildArch: noarch
%description common
This package contains common documentation files for SuperLUMT.

%prep
%setup -q -n SuperLU_MT_%{majorver}

rm -fr SRC/mc64ad.f.bak
find . -type f | sed -e "/TESTING/d" | xargs chmod a-x
# Remove the shippped executables from EXAMPLE
find EXAMPLE -type f | while read file
do
   [ "$(file $file | awk '{print $2}')" = ELF ] && rm $file || :
done

%if 0%{?rhel} >= 7 || 0%{?fedora}
%if 0%{?arch64}
# Duplicating of examples source code
cp -a EXAMPLE EXAMPLE64
%endif
%endif

%patch0 -p0
%patch1 -p0
%patch4 -p0

%build
cp -p MAKE_INC/make.linux.openmp make.inc
sed -i -e "s|-O3|$RPM_OPT_FLAGS|" \
make.inc

## Build lib ##########################################
%if 0%{?fedora} >= 33
export LIBBLASLINK=-lflexiblas
%else
export LIBBLASLINK=-lopenblaso
%endif
export LDFLAGS="%{__global_ldflags} -lgomp $LIBBLASLINK" \

%if 0%{?el7}
%{?dts:source /opt/rh/devtoolset-8/enable}
%endif

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
 CFLAGS="$RPM_OPT_FLAGS $LDFLAGS -fPIC -D__OPENMP -DPRNTlevel=0 -DDEBUGlevel=0" \
 LDFLAGS="%{__global_ldflags} -lgomp $LIBBLASLINK" \
 MATHLIB=-lm \
%if 0%{?complex}
 MPLIB= -C SRC single double complex complex16
%else
 MPLIB= -C SRC single double
%endif

cp -p SRC/libsuperlumt_*.so.%{majorver} lib/
cp -p SRC/libsuperlumt_*.so lib/

# Make example files
%if 0%{?fedora} >= 33
export LIBBLASLINK=-lflexiblas
%else
export LIBBLASLINK=-lopenblaso
%endif
export LDFLAGS="%{__global_ldflags} -lgomp $LIBBLASLINK" \

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
 CFLAGS="$RPM_OPT_FLAGS $LDFLAGS -fPIC -D__OPENMP -DPRNTlevel=0 -DDEBUGlevel=0" \
 LDFLAGS="%{__global_ldflags} -lgomp $LIBBLASLINK" \
 MATHLIB=-lm \
%if 0%{?complex}
 MPLIB= -C EXAMPLE single double complex complex16
%else
 MPLIB= -C EXAMPLE single double
%endif

make -C SRC clean
make -C TESTING/MATGEN clean
#######################################################
%if 0%{?rhel} >= 7 || 0%{?fedora}
%if 0%{?arch64}
## Build 64 ##########################################
# Reverting previous patches
# and patch again for new libraries
patch -R -p0 < %{PATCH0}
patch -R -p0 < %{PATCH1}
patch -p0 < %{PATCH2}
patch -p0 < %{PATCH3}
patch -p0 < %{PATCH5}

%if 0%{?fedora} >= 33
export LIBBLASLINK=-lflexiblas64
%else
export LIBBLASLINK=-lopenblaso64
%endif
export LDFLAGS="%{__global_ldflags} -lgomp $LIBBLASLINK" \

make -j1 \
 SONAME=%{majorver} \
 BLASLIB="-L%{_libdir} $LIBBLASLINK" \
 PREDEFS="$RPM_OPT_FLAGS $LDFLAGS -fPIC -D__OPENMP -DPRNTlevel=0 -DDEBUGlevel=0 -D_LONGINT" \
 NOOPTS="-O0 -fPIC -fopenmp $LIBBLASLINK" \
 CDEFS=-DAdd_ \
 FFLAGS="$RPM_OPT_FLAGS $LDFLAGS -fPIC -fopenmp -D__OPENMP -DPRNTlevel=0 -DDEBUGlevel=0 -fdefault-integer-8" \
 FORTRAN=gfortran \
 CFLAGS="$RPM_OPT_FLAGS $LDFLAGS -fPIC -D__OPENMP -DPRNTlevel=0 -DDEBUGlevel=0 -D_LONGINT" \
 LOADER=gcc \
 CC=gcc \
 LDFLAGS="%{__global_ldflags} -lgomp $LIBBLASLINK" \
 MATHLIB=-lm \
%if 0%{?complex}
 MPLIB= -C SRC single double complex complex16
%else
 MPLIB= -C SRC single double
%endif

cp -p SRC/libsuperlumt64_*.so.%{majorver} lib
cp -p SRC/libsuperlumt64_*.so lib

# Make example files

%if 0%{?fedora} >= 33
export LIBBLASLINK=-lflexiblas64
%else
export LIBBLASLINK=-lopenblaso64
%endif
export LDFLAGS="%{__global_ldflags} -lgomp $LIBBLASLINK" \

make -j1 \
 SONAME=%{majorver} \
 BLASLIB="-L%{_libdir} $LIBBLASLINK" \
 PREDEFS="$RPM_OPT_FLAGS $LDFLAGS -fPIC -D__OPENMP -DPRNTlevel=0 -DDEBUGlevel=0 -D_LONGINT" \
 NOOPTS="-O0 -fPIC -fopenmp $LIBBLASLINK" \
 CDEFS=-DAdd_ \
 FFLAGS="$RPM_OPT_FLAGS $LDFLAGS -fPIC -fopenmp -D__OPENMP -DPRNTlevel=0 -DDEBUGlevel=0 -fdefault-integer-8" \
 FORTRAN=gfortran \
 CFLAGS="$RPM_OPT_FLAGS $LDFLAGS -fPIC -D__OPENMP -DPRNTlevel=0 -DDEBUGlevel=0 -D_LONGINT" \
 LOADER=gcc \
 LOADOPTS="$RPM_OPT_FLAGS $LDFLAGS -fPIC -D__OPENMP -DPRNTlevel=0 -DDEBUGlevel=0 -D_LONGINT" \
 CC=gcc \
 LDFLAGS="%{__global_ldflags} -lgomp $LIBBLASLINK" \
 MATHLIB=-lm \
%if 0%{?complex}
 MPLIB= -C EXAMPLE64 single double complex complex16
%else
 MPLIB= -C EXAMPLE64 single double
%endif
%endif
%endif
#######################################################

%ldconfig_scriptlets
%ldconfig_scriptlets double

%if 0%{?complex}
%ldconfig_scriptlets complex
%ldconfig_scriptlets complex16
%endif

%if 0%{?rhel} >= 7 || 0%{?fedora}
%if 0%{?arch64}
%ldconfig_scriptlets -n SuperLUMT64
%ldconfig_scriptlets -n SuperLUMT64-double

%if 0%{?complex}
%ldconfig_scriptlets -n SuperLUMT64-complex
%ldconfig_scriptlets -n SuperLUMT64-complex16
%endif
%endif
%endif

%check
pushd EXAMPLE
export LD_LIBRARY_PATH=%{buildroot}%{_libdir}:%{_libdir}
./pslinsol < big.rua
./pdlinsol < big.rua
%if 0%{?complex}
./pclinsol < cmat
./pzlinsol < cmat
%endif
./pslinsolx < big.rua
./pdlinsolx < big.rua
%if 0%{?complex}
./pclinsolx < cmat
./pzlinsolx < cmat
%endif
./pslinsolx1 < big.rua
./pdlinsolx1 < big.rua
%if 0%{?complex}
./pclinsolx1 < cmat
./pzlinsolx1 < cmat
%endif
popd

%if 0%{?rhel} >= 7 || 0%{?fedora}
%if 0%{?arch64}
pushd EXAMPLE64
export LD_LIBRARY_PATH=%{buildroot}%{_libdir}:%{_libdir}
./pslinsol < big.rua
./pdlinsol < big.rua
%if 0%{?complex}
./pclinsol < cmat
./pzlinsol < cmat
%endif
popd
%endif
%endif

%install
mkdir -p %{buildroot}%{_libdir}
mkdir -p %{buildroot}%{_includedir}/%{name}
cp -P lib/libsuperlumt_*.so.%{majorver} %{buildroot}%{_libdir}
install -p SRC/*.h %{buildroot}%{_includedir}/%{name}
chmod -x %{buildroot}%{_includedir}/%{name}/*.h
cp -P lib/libsuperlumt_*.so %{buildroot}%{_libdir}

%if 0%{?complex}
for i in s d c z
%else
for i in s d
%endif
do
 ln -sf  %{_libdir}/libsuperlumt_${i}.so.%{majorver} %{buildroot}%{_libdir}/libsuperlumt_${i}.so
done

%if 0%{?rhel} >= 7 || 0%{?fedora}
%if 0%{?arch64}
cp -P lib/libsuperlumt64_*.so.%{majorver} %{buildroot}%{_libdir}
cp -P lib/libsuperlumt64_*.so %{buildroot}%{_libdir}

%if 0%{?complex}
for i in s d c z
%else
for i in s d
%endif
do
 ln -sf  %{_libdir}/libsuperlumt64_${i}.so.%{majorver} %{buildroot}%{_libdir}/libsuperlumt64_${i}.so
done
%endif
%endif

%files
%{_libdir}/libsuperlumt_s.so.%{majorver}

%files double
%{_libdir}/libsuperlumt_d.so.%{majorver}

%if 0%{?complex}
%files complex
%{_libdir}/libsuperlumt_c.so.%{majorver}

%files complex16
%{_libdir}/libsuperlumt_z.so.%{majorver}
%endif

%files devel
%{_includedir}/%{name}/
%{_libdir}/libsuperlumt_*.so

########################################################
%if 0%{?rhel} >= 7 || 0%{?fedora}
%if 0%{?arch64}
%files -n SuperLUMT64
%{_libdir}/libsuperlumt64_s.so.%{majorver}

%files -n SuperLUMT64-double
%{_libdir}/libsuperlumt64_d.so.%{majorver}

%if 0%{?complex}
%files -n SuperLUMT64-complex
%{_libdir}/libsuperlumt64_c.so.%{majorver}

%files -n SuperLUMT64-complex16
%{_libdir}/libsuperlumt64_z.so.%{majorver}
%endif

%files -n SuperLUMT64-devel
%{_includedir}/%{name}/
%{_libdir}/libsuperlumt64_*.so
%endif
%endif
#######################################################

%files common
%license License.txt
%doc DOC README

%changelog
* Wed Jul 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.0-33
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed Jan 19 2022 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.0-32
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.0-31
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Mon Jan 25 2021 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.0-30
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.0-29
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.0-28
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Sat Jul 25 2020 Iñaki Úcar <iucar@fedoraproject.org> - 3.1.0-27
- https://fedoraproject.org/wiki/Changes/FlexiBLAS_as_BLAS/LAPACK_manager

* Sat Mar 21 2020 Antonio Trande <sagitterATfedoraproject.org> - 3.1.0-26
- Do not mix-up pthread and openmp support

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.0-25
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 24 2019 Antonio Trande <sagitterATfedoraproject.org> - 3.1.0-24
- Optimize OpenMP flags

* Wed Oct 23 2019 Antonio Trande <sagitterATfedoraproject.org> - 3.1.0-23
- Undefine --as-needed link option

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.0-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Jun 29 2019 Antonio Trande <sagitterATfedoraproject.org> - 3.1.0-21
- Use devtoolset-8 on epel
- Downgrading Make's jobs

* Tue Feb 19 2019 Antonio Trande <sagitterATfedoraproject.org> - 3.1.0-20
- Use openblas always

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.0-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Aug 23 2018 Peter Robinson <pbrobinson@fedoraproject.org> 3.1.0-18
- Drop group
- Build on all arches

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.0-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 21 2018 Antonio Trande <sagitterATfedoraproject.org> - 3.1.0-16
- Add gcc BR

* Thu Feb 15 2018 Antonio Trande <sagitterATfedoraproject.org> - 3.1.0-15
- Use %%ldconfig_scriptlets

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.0-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Mon Oct 30 2017 Antonio Trande <sagitterATfedoraproject.org> - 3.1.0-13
- Rebuild against openblas

* Wed Aug 16 2017 Antonio Trande <sagitterATfedoraproject.org> - 3.1.0-12
- Rebuild for lapack 3.7.1 (moved to 64_ suffix)

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.0-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.0-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Oct 05 2016 Antonio Trande <sagitterATfedoraproject.org> - 3.1.0-8
- Built against blas on s390x (bz#1382071)

* Fri Aug 12 2016 Peter Robinson <pbrobinson@fedoraproject.org> 3.1.0-7
- Update to the latest openblas arch list

* Tue May 03 2016 Antonio Trande <sagitterATfedoraproject.org> - 3.1.0-6
- Dropped Fortran dependencies

* Thu Apr 14 2016 Antonio Trande <sagitterATfedoraproject.org> - 3.1.0-5
- Excluded ppc64le arch

* Tue Apr 12 2016 Antonio Trande <sagitterATfedoraproject.org> - 3.1.0-4
- Some minor fixes

* Sun Apr 03 2016 Antonio Trande <sagitterATfedoraproject.org> - 3.1.0-3
- Source archive redistributed with License file

* Wed Mar 30 2016 Antonio Trande <sagitterATfedoraproject.org> - 3.1.0-2
- Build libraries with 64-bit integers
- Set ExclusiveArch because of openblas

* Wed Mar 30 2016 Antonio Trande <sagitterATfedoraproject.org> - 3.1.0-1
- Update to 3.1.0
- Build against openblas

* Tue Mar 29 2016 Antonio Trande <sagitterATfedoraproject.org> - 3.0.0-3
- Build Single and Double precision routines

* Mon Mar 28 2016 Antonio Trande <sagitterATfedoraproject.org> - 3.0.0-2
- Build 'Single precision real SuperLU routines' library only

* Mon Mar 28 2016 Antonio Trande <sagitterATfedoraproject.org> - 3.0.0-1
- Initial package.
