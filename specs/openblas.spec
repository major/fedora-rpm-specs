%bcond_with system_lapack
# Version of bundled lapack
%global lapackver 3.12.0

# DO NOT "CLEAN UP" OR MODIFY THIS SPEC FILE WITHOUT ASKING THE
# MAINTAINER FIRST!
#
# OpenBLAS is hand written assembler code and it has a limited number
# of supported architectures. Don't enable any new architectures /
# processors a) without checking that it is actually supported and b)
# without modifying the target flags.
#
# The same spec is also used on the EPEL branches, meaninng that some
# "obsoleted" features are still kept in the spec.

Name:           openblas
Version:        0.3.29
Release:        2%{?dist}
Summary:        An optimized BLAS library based on GotoBLAS2

License:        BSD-3-Clause
URL:            https://github.com/OpenMathLib/OpenBLAS
Source0:        %url/archive/v%{version}/OpenBLAS-%{version}.tar.gz

# Use system lapack
Patch0:         openblas-0.2.15-system_lapack.patch
# Drop extra p from threaded library name
Patch1:         openblas-0.2.5-libname.patch
# Don't use constructor priorities on too old architectures
Patch2:         openblas-0.2.15-constructor.patch
# Supply the proper flags to the test makefile
Patch3:         openblas-0.3.11-tests.patch

BuildRequires: make
BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  gcc-gfortran
BuildRequires:  perl-devel
BuildRequires:  multilib-rpm-config

# Rblas library is no longer necessary
%if 0%{?fedora} >= 31 || 0%{?rhel} >= 8
Obsoletes:      %{name}-Rblas < %{version}-%{release}
%endif

# Do we have execstack?
%if 0%{?rhel} == 7
%ifarch ppc64le aarch64
%global execstack 0
%else
%global execstack 1
%endif
%else
%global execstack 1
%endif
%if %{execstack}
BuildRequires:  /usr/bin/execstack
%endif

# LAPACK
%if %{with system_lapack}
%if 0%{?rhel} == 5 || 0%{?rhel} == 6
BuildRequires:  lapack-devel
%else
BuildRequires:  lapack-static
%endif
# Do we have LAPACKE? (Needs at least lapack 3.4.0)
%if 0%{?fedora}
%global lapacke 1
%else
%global lapacke 0
%endif

%else
# Use bundled LAPACK
%global lapacke 1
Provides:       bundled(lapack) = %{lapackver}
%endif

# Build 64-bit interface binaries?
%if 0%{?__isa_bits} == 64
%global build64 1
%bcond_without cpp_thread_check
%else
%global build64 0
%bcond_with cpp_thread_check
%endif

%if %{with system_lapack}
%if %build64
BuildRequires:  lapack64-static
%endif
%endif

# Upstream supports the package only on these architectures.
# Runtime processor detection is not available on other archs.
ExclusiveArch:  %{openblas_arches}

%global base_description \
OpenBLAS is an optimized BLAS library based on GotoBLAS2 1.13 BSD \
version. The project is supported by the Lab of Parallel Software and \
Computational Science, ISCAS. http://www.rdcps.ac.cn


%description
%{base_description}

%package serial
Summary:        An optimized BLAS library based on GotoBLAS2, serial version
Requires:       %{name} = %{version}-%{release}

%description serial
%{base_description}

This package contains the sequential library compiled with a 32-bit
integer interface.

%package openmp
Summary:        An optimized BLAS library based on GotoBLAS2, OpenMP version
Requires:       %{name} = %{version}-%{release}

%description openmp
%{base_description}

This package contains the library compiled with OpenMP support with
32-bit integer interface.

%package threads
Summary:        An optimized BLAS library based on GotoBLAS2, pthreads version
Requires:       %{name} = %{version}-%{release}

%description threads
%{base_description}

This package contains the library compiled with threading support and
a 32-bit integer interface.

%if %build64
%package serial64
Summary:        An optimized BLAS library based on GotoBLAS2, serial version
Requires:       %{name} = %{version}-%{release}

%description serial64
%{base_description}

This package contains the sequential library compiled with a 64-bit
integer interface.

%package openmp64
Summary:        An optimized BLAS library based on GotoBLAS2, OpenMP version
Requires:       %{name} = %{version}-%{release}

%description openmp64
%{base_description}

This package contains the library compiled with OpenMP support and
64-bit integer interface.

%package threads64
Summary:        An optimized BLAS library based on GotoBLAS2, pthreads version
Requires:       %{name} = %{version}-%{release}

%description threads64
%{base_description}

This package contains the library compiled with threading support and
64-bit integer interface.

%package serial64_
Summary:        An optimized BLAS library based on GotoBLAS2, serial version
Requires:       %{name} = %{version}-%{release}

%description serial64_
%{base_description}

This package contains the sequential library compiled with a 64-bit
integer interface and a symbol name suffix.

%package openmp64_
Summary:        An optimized BLAS library based on GotoBLAS2, OpenMP version
Requires:       %{name} = %{version}-%{release}

%description openmp64_
%{base_description}

This package contains the library compiled with OpenMP support and
64-bit integer interface and a symbol name suffix.

%package threads64_
Summary:        An optimized BLAS library based on GotoBLAS2, pthreads version
Requires:       %{name} = %{version}-%{release}

%description threads64_
%{base_description}

This package contains the library compiled with threading support and
64-bit integer interface and a symbol name suffix.
%endif


%package devel
Summary:        Development headers and libraries for OpenBLAS
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       %{name}-serial%{?_isa} = %{version}-%{release}
Requires:       %{name}-openmp%{?_isa} = %{version}-%{release}
Requires:       %{name}-threads%{?_isa} = %{version}-%{release}
%if %build64
Requires:       %{name}-openmp64%{?_isa} = %{version}-%{release}
Requires:       %{name}-threads64%{?_isa} = %{version}-%{release}
Requires:       %{name}-serial64%{?_isa} = %{version}-%{release}
Requires:       %{name}-openmp64_%{?_isa} = %{version}-%{release}
Requires:       %{name}-threads64_%{?_isa} = %{version}-%{release}
Requires:       %{name}-serial64_%{?_isa} = %{version}-%{release}
%endif
Requires:       %{name}-srpm-macros

%description devel
%{base_description}

This package contains the development headers and libraries.

%package static
Summary:        Static version of OpenBLAS
Requires:       %{name}-devel%{?_isa} = %{version}-%{release}

%description static
%{base_description}

This package contains the static libraries.


%prep
%setup -q -c -T

# Untar source
tar zxf %{SOURCE0}
cd OpenBLAS-%{version}
%if %{with system_lapack}
%patch 0 -p1 -b .system_lapack
%endif
%patch 1 -p1 -b .libname
%if 0%{?rhel} == 5
%patch 2 -p1 -b .constructor
%endif
%patch 3 -p1 -b .tests

# Fix source permissions
find -name \*.f -exec chmod 644 {} \;

%if %{with system_lapack}
# Get rid of bundled LAPACK sources
rm -rf lapack-netlib
%endif

# Make serial, threaded and OpenMP versions; as well as 64-bit versions
cd ..
cp -ar OpenBLAS-%{version} openmp
cp -ar OpenBLAS-%{version} threaded
%if %build64
for d in {serial,threaded,openmp}64{,_}; do
    cp -ar OpenBLAS-%{version} $d
done
%endif
mv OpenBLAS-%{version} serial

%if %{with system_lapack}
# Setup 32-bit interface LAPACK
mkdir netliblapack
cd netliblapack
ar x %{_libdir}/liblapack_pic.a
# Get rid of duplicate functions. See list in Makefile of lapack directory
for f in laswp getf2 getrf potf2 potrf lauu2 lauum trti2 trtri getrs; do
    \rm {c,d,s,z}$f.o
done

# LAPACKE
%if %{lapacke}
ar x %{_libdir}/liblapacke.a
%endif

# Create makefile
echo "TOPDIR = .." > Makefile
echo "include ../Makefile.system" >> Makefile
echo "COMMONOBJS = \\" >> Makefile
for i in *.o; do
 echo "$i \\" >> Makefile
done
echo -e "\n\ninclude \$(TOPDIR)/Makefile.tail" >> Makefile

%if %{lapacke}
# Copy include files
cp -a %{_includedir}/lapacke .
%endif
cd ..

# Copy in place
for d in serial threaded openmp; do
    cp -pr netliblapack $d
done
rm -rf netliblapack


# Setup 64-bit interface LAPACK
%if %build64
mkdir netliblapack64
cd netliblapack64
ar x %{_libdir}/liblapack64_pic.a
# Get rid of duplicate functions. See list in Makefile of lapack directory
for f in laswp getf2 getrf potf2 potrf lauu2 lauum trti2 trtri getrs; do
    \rm {c,d,s,z}$f.o
done

# LAPACKE, no 64-bit interface
%if %{lapacke}
ar x %{_libdir}/liblapacke.a
%endif

# Create makefile
echo "TOPDIR = .." > Makefile
echo "include ../Makefile.system" >> Makefile
echo "COMMONOBJS = \\" >> Makefile
for i in *.o; do
    echo "$i \\" >> Makefile
done
echo -e "\n\ninclude \$(TOPDIR)/Makefile.tail" >> Makefile

%if %{lapacke}
# Copy include files
cp -a %{_includedir}/lapacke .
%endif
cd ..

# Copy in place
for d in {serial,threaded,openmp}64{,_}; do
    cp -pr netliblapack64 $d/netliblapack
done
rm -rf netliblapack64
%endif
%endif

%build
# openblas fails to build with LTO due to undefined symbols.  These could
# well be the result of the assembly code used in this package
%define _lto_cflags %{nil}
%if !%{lapacke}
LAPACKE="NO_LAPACKE=1"
%endif

# Maximum possible amount of processors
NMAX="NUM_THREADS=128"

%ifarch %{ix86} x86_64
TARGET="TARGET=CORE2 DYNAMIC_ARCH=1 DYNAMIC_OLDER=1"

# Compability for old versions of GCC
%if 0%{?rhel} == 5
export AVX="NO_AVX=1 NO_AVX2=1"
%endif
%if 0%{?rhel} == 6
export AVX="NO_AVX2=1"
%endif

%endif
%ifarch armv7hl
# ARM v7 still doesn't have runtime cpu detection...
TARGET="TARGET=ARMV7 DYNAMIC_ARCH=0"
%endif
%ifarch ppc64
TARGET="TARGET=POWER6 DYNAMIC_ARCH=1 DYNAMIC_OLDER=1"
%endif
%ifarch ppc64p7
TARGET="TARGET=POWER7 DYNAMIC_ARCH=1 DYNAMIC_OLDER=1"
%endif
%ifarch ppc64le
TARGET="TARGET=POWER8 DYNAMIC_ARCH=1 DYNAMIC_OLDER=1"
%endif
%ifarch aarch64
TARGET="TARGET=ARMV8 DYNAMIC_ARCH=1 DYNAMIC_OLDER=1"
%endif
%ifarch s390x
TARGET="TARGET=ZARCH_GENERIC DYNAMIC_ARCH=1 DYNAMIC_OLDER=1"
%endif
%ifarch riscv64
TARGET="TARGET=RISCV64_GENERIC DYNAMIC_ARCH=0"
%endif

%if 0%{?rhel} == 5
# Gfortran too old to recognize -frecursive
COMMON="%{optflags} -fPIC"
FCOMMON="%{optflags} -fPIC"
%else
COMMON="%{optflags} -fPIC"
FCOMMON="%{optflags} -fPIC -frecursive"
%endif
# Use Fedora linker flags
export LDFLAGS="%{__global_ldflags}"

# Declare some necessary build flags
COMMON="%{optflags} -fPIC"
FCOMMON="$COMMON -frecursive"
make -C serial     $TARGET USE_THREAD=0 USE_LOCKING=1 USE_OPENMP=0 FC=gfortran CC=gcc COMMON_OPT="$COMMON" FCOMMON_OPT="$FCOMMON" $NMAX LIBPREFIX="libopenblas"      $AVX $LAPACKE INTERFACE64=0
make -C threaded   $TARGET USE_THREAD=1 USE_OPENMP=0 FC=gfortran CC=gcc COMMON_OPT="$COMMON" FCOMMON_OPT="$FCOMMON" $NMAX LIBPREFIX="libopenblasp"     $AVX $LAPACKE INTERFACE64=0

# USE_THREAD determines use of SMP, not of pthreads
COMMON="%{optflags} -fPIC -fopenmp -pthread"
FCOMMON="$COMMON -frecursive"
make -C openmp     $TARGET USE_THREAD=1 USE_OPENMP=1 FC=gfortran CC=gcc COMMON_OPT="$COMMON" FCOMMON_OPT="$FCOMMON" $NMAX LIBPREFIX="libopenblaso"     $AVX $LAPACKE INTERFACE64=0 %{with cpp_thread_check:CPP_THREAD_SAFETY_TEST=1}
make -C openmp     $TARGET USE_THREAD=1 USE_OPENMP=1 FC=gfortran CC=gcc COMMON_OPT="$COMMON" FCOMMON_OPT="$FCOMMON" $NMAX LIBPREFIX="libopenblaso"     $AVX $LAPACKE INTERFACE64=0 %{with cpp_thread_check:CPP_THREAD_SAFETY_TEST=1} lapack-test

%if %build64
COMMON="%{optflags} -fPIC"
FCOMMON="$COMMON -frecursive -fdefault-integer-8"
make -C serial64   $TARGET USE_THREAD=0 USE_LOCKING=1 USE_OPENMP=0 FC=gfortran CC=gcc COMMON_OPT="$COMMON" FCOMMON_OPT="$FCOMMON" $NMAX LIBPREFIX="libopenblas64"    $AVX $LAPACKE INTERFACE64=1
make -C threaded64 $TARGET USE_THREAD=1 USE_OPENMP=0 FC=gfortran CC=gcc COMMON_OPT="$COMMON" FCOMMON_OPT="$FCOMMON" $NMAX LIBPREFIX="libopenblasp64"   $AVX $LAPACKE INTERFACE64=1

COMMON="%{optflags} -fPIC -fopenmp -pthread"
FCOMMON="$COMMON -frecursive -fdefault-integer-8"
make -C openmp64   $TARGET USE_THREAD=1 USE_OPENMP=1 FC=gfortran CC=gcc COMMON_OPT="$COMMON" FCOMMON_OPT="$FCOMMON" $NMAX LIBPREFIX="libopenblaso64"   $AVX $LAPACKE INTERFACE64=1 CPP_THREAD_SAFETY_TEST=1

COMMON="%{optflags} -fPIC"
FCOMMON="$COMMON -frecursive  -fdefault-integer-8"
make -C serial64_   $TARGET USE_THREAD=0 USE_LOCKING=1 USE_OPENMP=0 FC=gfortran CC=gcc COMMON_OPT="$COMMON" FCOMMON_OPT="$FCOMMON" $NMAX LIBPREFIX="libopenblas64_"  $AVX $LAPACKE INTERFACE64=1 SYMBOLSUFFIX=64_
make -C threaded64_ $TARGET USE_THREAD=1 USE_OPENMP=0 FC=gfortran CC=gcc COMMON_OPT="$COMMON" FCOMMON_OPT="$FCOMMON" $NMAX LIBPREFIX="libopenblasp64_" $AVX $LAPACKE INTERFACE64=1 SYMBOLSUFFIX=64_

COMMON="%{optflags} -fPIC -fopenmp -pthread"
FCOMMON="$COMMON -frecursive -fdefault-integer-8"
make -C openmp64_   $TARGET USE_THREAD=1 USE_OPENMP=1 FC=gfortran CC=gcc COMMON_OPT="$COMMON" FCOMMON_OPT="$FCOMMON" $NMAX LIBPREFIX="libopenblaso64_" $AVX $LAPACKE INTERFACE64=1 SYMBOLSUFFIX=64_ CPP_THREAD_SAFETY_TEST=1
%endif

%install
rm -rf %{buildroot}
# Install serial library and headers
make -C serial USE_THREAD=0 PREFIX=%{buildroot} OPENBLAS_LIBRARY_DIR=%{buildroot}%{_libdir} OPENBLAS_INCLUDE_DIR=%{buildroot}%{_includedir}/%name OPENBLAS_BINARY_DIR=%{buildroot}%{_bindir} OPENBLAS_CMAKE_DIR=%{buildroot}%{_libdir}/cmake install

# Copy lapacke include files
%if %{with system_lapack} && %{lapacke}
cp -a %{_includedir}/lapacke %{buildroot}%{_includedir}/%{name}
%endif

# Fix i686-x86_64 multilib difference
%multilib_fix_c_header --file %{_includedir}/openblas/openblas_config.h

# Fix name of libraries: runtime CPU detection has none
suffix=""
# but archs that don't have it do have one
%ifarch armv7hl
suffix="_armv7"
%endif
%ifarch riscv64
suffix="_riscv64_generic"
%endif
slibname=`basename %{buildroot}%{_libdir}/libopenblas${suffix}-*.so .so`
mv %{buildroot}%{_libdir}/${slibname}.a %{buildroot}%{_libdir}/lib%{name}.a
if [[ "$suffix" != "" ]]; then
   sname=$(echo $slibname | sed "s|$suffix||g")
   mv %{buildroot}%{_libdir}/${slibname}.so %{buildroot}%{_libdir}/${sname}.so
else
   sname=${slibname}
fi

# Install the OpenMP library
olibname=`echo ${slibname} | sed "s|lib%{name}|lib%{name}o|g"`
install -D -p -m 644 openmp/${olibname}.a %{buildroot}%{_libdir}/lib%{name}o.a
if [[ "$suffix" != "" ]]; then
   oname=$(echo $olibname | sed "s|$suffix||g")
else
   oname=${olibname}
fi
install -D -p -m 755 openmp/${olibname}.so %{buildroot}%{_libdir}/${oname}.so

# Install the threaded library
plibname=`echo ${slibname} | sed "s|lib%{name}|lib%{name}p|g"`
install -D -p -m 644 threaded/${plibname}.a %{buildroot}%{_libdir}/lib%{name}p.a
if [[ "$suffix" != "" ]]; then
   pname=$(echo $plibname | sed "s|$suffix||g")
else
   pname=${plibname}
fi
install -D -p -m 755 threaded/${plibname}.so %{buildroot}%{_libdir}/${pname}.so

# Install the 64-bit interface libraries
%if %build64
slibname64=`echo ${slibname} | sed "s|lib%{name}|lib%{name}64|g"`
install -D -p -m 644 serial64/${slibname64}.a %{buildroot}%{_libdir}/lib%{name}64.a
slibname64_=`echo ${slibname} | sed "s|lib%{name}|lib%{name}64_|g"`
install -D -p -m 644 serial64_/${slibname64_}.a %{buildroot}%{_libdir}/lib%{name}64_.a

if [[ "$suffix" != "" ]]; then
   sname64=$(echo ${slibname64} | sed "s|$suffix||g")
   sname64_=$(echo ${slibname64_} | sed "s|$suffix||g")
else
   sname64=${slibname64}
   sname64_=${slibname64_}
fi
install -D -p -m 755 serial64/${slibname64}.so %{buildroot}%{_libdir}/${sname64}.so
install -D -p -m 755 serial64_/${slibname64_}.so %{buildroot}%{_libdir}/${sname64_}.so

olibname64=`echo ${slibname} | sed "s|lib%{name}|lib%{name}o64|g"`
install -D -p -m 644 openmp64/${olibname64}.a %{buildroot}%{_libdir}/lib%{name}o64.a
olibname64_=`echo ${slibname} | sed "s|lib%{name}|lib%{name}o64_|g"`
install -D -p -m 644 openmp64_/${olibname64_}.a %{buildroot}%{_libdir}/lib%{name}o64_.a

if [[ "$suffix" != "" ]]; then
   oname64=$(echo ${olibname64} | sed "s|$suffix||g")
   oname64_=$(echo ${olibname64_} | sed "s|$suffix||g")
else
   oname64=${olibname64}
   oname64_=${olibname64_}
fi
install -D -p -m 755 openmp64/${olibname64}.so %{buildroot}%{_libdir}/${oname64}.so
install -D -p -m 755 openmp64_/${olibname64_}.so %{buildroot}%{_libdir}/${oname64_}.so

plibname64=`echo ${slibname} | sed "s|lib%{name}|lib%{name}p64|g"`
install -D -p -m 644 threaded64/${plibname64}.a %{buildroot}%{_libdir}/lib%{name}p64.a
plibname64_=`echo ${slibname} | sed "s|lib%{name}|lib%{name}p64_|g"`
install -D -p -m 644 threaded64_/${plibname64_}.a %{buildroot}%{_libdir}/lib%{name}p64_.a

if [[ "$suffix" != "" ]]; then
   pname64=$(echo $plibname64 | sed "s|$suffix||g")
   pname64_=$(echo $plibname64_ | sed "s|$suffix||g")
else
   pname64=${plibname64}
   pname64_=${plibname64_}
fi
install -D -p -m 755 threaded64/${plibname64}.so %{buildroot}%{_libdir}/${pname64}.so
install -D -p -m 755 threaded64_/${plibname64_}.so %{buildroot}%{_libdir}/${pname64_}.so
%endif

# Fix symlinks
pushd %{buildroot}%{_libdir}
# Serial libraries
ln -sf ${sname}.so lib%{name}.so
ln -sf ${sname}.so lib%{name}.so.0
# OpenMP libraries
ln -sf ${oname}.so lib%{name}o.so
ln -sf ${oname}.so lib%{name}o.so.0
# Threaded libraries
ln -sf ${pname}.so lib%{name}p.so
ln -sf ${pname}.so lib%{name}p.so.0

%if %build64
# Serial libraries
ln -sf ${sname64}.so lib%{name}64.so
ln -sf ${sname64}.so lib%{name}64.so.0
ln -sf ${sname64_}.so lib%{name}64_.so
ln -sf ${sname64_}.so lib%{name}64_.so.0
# OpenMP libraries
ln -sf ${oname64}.so lib%{name}o64.so
ln -sf ${oname64}.so lib%{name}o64.so.0
ln -sf ${oname64_}.so lib%{name}o64_.so
ln -sf ${oname64_}.so lib%{name}o64_.so.0
# Threaded libraries
ln -sf ${pname64}.so lib%{name}p64.so
ln -sf ${pname64}.so lib%{name}p64.so.0
ln -sf ${pname64_}.so lib%{name}p64_.so
ln -sf ${pname64_}.so lib%{name}p64_.so.0
%endif

%if %{execstack}
# Get rid of executable stacks
for lib in %{buildroot}%{_libdir}/libopenblas*.so; do
 execstack -c $lib
done
%endif

# Get rid of generated CMake config
rm -rf %{buildroot}%{_libdir}/cmake
# Get rid of generated pkgconfig
rm -rf %{buildroot}%{_libdir}/pkgconfig

%ldconfig_scriptlets

%ldconfig_scriptlets openmp

%ldconfig_scriptlets threads

%if %build64
%ldconfig_scriptlets openmp64
%ldconfig_scriptlets openmp64_

%ldconfig_scriptlets serial64
%ldconfig_scriptlets serial64_

%ldconfig_scriptlets threads64
%ldconfig_scriptlets threads64_
%endif

%files
%license serial/LICENSE
%doc serial/Changelog.txt serial/GotoBLAS* 

%files serial
%{_libdir}/lib%{name}-*.so
%{_libdir}/lib%{name}.so.*

%files openmp
%{_libdir}/lib%{name}o-*.so
%{_libdir}/lib%{name}o.so.*

%files threads
%{_libdir}/lib%{name}p-*.so
%{_libdir}/lib%{name}p.so.*

%if %build64
%files serial64
%{_libdir}/lib%{name}64-*.so
%{_libdir}/lib%{name}64.so.*

%files openmp64
%{_libdir}/lib%{name}o64-*.so
%{_libdir}/lib%{name}o64.so.*

%files threads64
%{_libdir}/lib%{name}p64-*.so
%{_libdir}/lib%{name}p64.so.*

%files serial64_
%{_libdir}/lib%{name}64_-*.so
%{_libdir}/lib%{name}64_.so.*

%files openmp64_
%{_libdir}/lib%{name}o64_-*.so
%{_libdir}/lib%{name}o64_.so.*

%files threads64_
%{_libdir}/lib%{name}p64_-*.so
%{_libdir}/lib%{name}p64_.so.*
%endif

%files devel
%{_includedir}/%{name}/
%{_libdir}/lib%{name}.so
%{_libdir}/lib%{name}o.so
%{_libdir}/lib%{name}p.so
%if %build64
%{_libdir}/lib%{name}64.so
%{_libdir}/lib%{name}o64.so
%{_libdir}/lib%{name}p64.so
%{_libdir}/lib%{name}64_.so
%{_libdir}/lib%{name}o64_.so
%{_libdir}/lib%{name}p64_.so
%endif

%files static
%{_libdir}/lib%{name}.a
%{_libdir}/lib%{name}o.a
%{_libdir}/lib%{name}p.a
%if %build64
%{_libdir}/lib%{name}64.a
%{_libdir}/lib%{name}o64.a
%{_libdir}/lib%{name}p64.a
%{_libdir}/lib%{name}64_.a
%{_libdir}/lib%{name}o64_.a
%{_libdir}/lib%{name}p64_.a
%endif

%changelog
* Thu Jul 24 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.29-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_43_Mass_Rebuild

* Fri Jan 24 2025 Iñaki Úcar <iucar@fedoraproject.org> - 0.3.29-1
- Update to 0.3.29
  Resolves: BZ#2273704
  Resolves: BZ#2329491

* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.28-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Wed Dec 04 2024 David Abdurachmanov <davidlt@rivosinc.com> - 0.3.28-2
- Add support for riscv64

* Wed Oct 02 2024 Pavel Simovec <psimovec@redhat.com> - 0.3.28-1
- Update to 0.3.28
  Resolves: BZ#2273704
  Resolves: RHEL-54180

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.26-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Fri Feb 09 2024 Honza Horak <hhorak@redhat.com> - 0.3.26-4
- Fix FTBFS on ppc64le and s390x
  Resolves: BZ#2261415
  Resolves: RHEL-24745

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.26-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.26-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 07 2024 İsmail Dönmez <ismail@i10z.com> - 0.3.26-1
- Update to 0.3.26

* Thu Nov 30 2023 İsmail Dönmez <ismail@i10z.com> - 0.3.25-1
- Update to 0.3.25

* Fri Oct 27 2023 Ali Erdinc Koroglu <aekoroglu@fedoraproject.org> - 0.3.24-1
- Update to 0.3.24

* Tue Aug 01 2023 Pavel Šimovec <psimovec@redhat.com> - 0.3.23-1
- Update to 0.3.23 (RHBZ #2182038)

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.21-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.21-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Nov 18 2022 Florian Weimer <fweimer@redhat.com> - 0.3.21-4
- Apply upstream patches to support building in stricter C99 mode

* Fri Aug 26 2022 Honza Horak <hhorak@redhat.com> - 0.3.21-3
- Re-add flags for tests

* Wed Aug 24 2022 Honza Horak <hhorak@redhat.com> - 0.3.21-2
- Fix SBGEMM test to work with INTERFACE64
  Resolves: #2120974

* Mon Aug 08 2022 Ali Erdinc Koroglu <aekoroglu@fedoraproject.org> - 0.3.21-1
- Update to 0.3.21 (RHBZ #2116398)

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.20-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Tue Mar 08 2022 Susi Lehtola <jussilehtola@fedoraproject.org> - 0.3.20-1
- Update to 0.3.20.

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.19-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Mon Jan 03 2022 Susi Lehtola <jussilehtola@fedoraproject.org> - 0.3.19-2
- Fix BZ#1982856.

* Sun Dec 19 2021 Susi Lehtola <jussilehtola@fedoraproject.org> - 0.3.19-1
- Update to 0.3.19.

* Mon Oct 11 2021 Susi Lehtola <jussilehtola@fedoraproject.org> - 0.3.18-1
- Update to 0.3.18.

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.17-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Mon Jul 19 2021 Susi Lehtola <jussilehtola@fedoraproject.org> - 0.3.17-1
- Update to 0.3.17.

* Mon Jul 12 2021 Susi Lehtola <jussilehtola@fedoraproject.org> - 0.3.16-1
- Update to 0.3.16.

* Mon May 03 2021 Susi Lehtola <jussilehtola@fedoraproject.org> - 0.3.15-1
- Update to 0.3.15.

* Thu Mar 18 2021 Susi Lehtola <jussilehtola@fedoraproject.org> - 0.3.14-1
- Update to 0.3.14.

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.12-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Sun Oct 25 2020 Susi Lehtola <jussilehtola@fedoraproject.org> - 0.3.12-1
- Update to 0.3.12.

* Sun Oct 18 2020 Susi Lehtola <jussilehtola@fedoraproject.org> - 0.3.11-1
- Update to 0.3.11.

* Fri Sep 18 2020 Susi Lehtola <jussilehtola@fedoraproject.org> - 0.3.10-6
- Fix incorrect result of cblas_zdotc_sub on ppc64le (BZ #1878449).

* Sat Aug 29 2020 Susi Lehtola <jussilehtola@fedoraproject.org> - 0.3.10-5
- Fix unresolved bfloat16 datatype (BZ #1873667).

* Fri Aug 14 2020 Susi Lehtola <jussilehtola@fedoraproject.org> - 0.3.10-4
- Obsolete Rblas package (BZ #1849966).

* Tue Aug 11 2020 Jeff Law <law@redhat.com> - 0.3.10-3
- Disable LTO

* Tue Jul 28 2020 Susi Lehtola <jussilehtola@fedoraproject.org> - 0.3.10-2
- Include upstream patch 2672 to fix test suite on systems with few CPUs.

* Mon Jun 15 2020 Susi Lehtola <jussilehtola@fedoraproject.org> - 0.3.10-1
- Update to 0.3.10.

* Thu May 28 2020 Susi Lehtola <jussilehtola@fedoraproject.org> - 0.3.9-3
- Enable USE_LOCKING in the sequential versions of the library for
  thread safety.

* Thu Apr 02 2020 Susi Lehtola <jussilehtola@fedoraproject.org> - 0.3.9-2
- Patch for BZ #1820131.

* Mon Mar 02 2020 Susi Lehtola <jussilehtola@fedoraproject.org> - 0.3.9-1
- Update to 0.3.9.

* Tue Feb 11 2020 Susi Lehtola <jussilehtola@fedoraproject.org> - 0.3.8-1
- Update to 0.3.8; dynamic runtime cpu detection on all architectures.
- Also updates bundled LAPACK to 3.9.0.

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.7-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Dec 11 2019 Dominik Mierzejewski <rpm@greysector.net> - 0.3.7-2
- enable C++ thread safety test where possible

* Mon Aug 12 2019 Susi Lehtola <jussilehtola@fedoraproject.org> - 0.3.7-1
- Update to 0.3.7.

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.6-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Tue Jul 02 2019 Susi Lehtola <jussilehtola@fedoraproject.org> - 0.3.6-2
- Rebuild since older build doesn't show up in updates system.

* Tue Apr 30 2019 Susi Lehtola <jussilehtola@fedoraproject.org> - 0.3.6-1
- Update to 0.3.6.

* Tue Feb 26 2019 Susi Lehtola <jussilehtola@fedoraproject.org> - 0.3.5-5
- Even more assembly kernel patches.

* Mon Feb 25 2019 Susi Lehtola <jussilehtola@fedoraproject.org> - 0.3.5-4
- Another assembly kernel patch.

* Sun Feb 17 2019 Susi Lehtola <jussilehtola@fedoraproject.org> - 0.3.5-3
- Patch assembly kernels to satisfy gcc 9 demands.

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Mon Jan 07 2019 Susi Lehtola <jussilehtola@fedoraproject.org> - 0.3.5-1
- Update to 0.3.5, with dynamic CPU detection on aarch64.

* Fri Nov 09 2018 Nikola Forró <nforro@redhat.com> - 0.3.3-3
- Fix i686-x86_64 multilib difference.
- Get rid of executable stack in libRblas.so.

* Sat Sep 29 2018 Susi Lehtola <jussilehtola@fedoraproject.org> - 0.3.3-2
- Fix segfault (BZ #1634060).

* Sun Sep 09 2018 Susi Lehtola <jussilehtola@fedoraproject.org> - 0.3.3-1
- Update to 0.3.3.

* Wed Aug 29 2018 Dan Horák <dan[at]danny.cz> - 0.3.2-5
- Fix precision in generic target on s390x

* Fri Aug 24 2018 Susi Lehtola <jussilehtola@fedoraproject.org> - 0.3.2-4
- Patch to avoid threading issues.

* Fri Aug 24 2018 Susi Lehtola <jussilehtola@fedoraproject.org> - 0.3.2-3
- Add missing %%{optflags} to COMMON (see discussion in #1619074).

* Wed Aug 15 2018 Dan Horák <dan[at]danny.cz> - 0.3.2-2
- Explicitly set the target to generic on s390x to avoid surprises (#1615760)

* Thu Aug 02 2018 Susi Lehtola <jussilehtola@fedoraproject.org> - 0.3.2-1
- Update to 0.3.2.

* Sun Jul 22 2018 Susi Lehtola <jussilehtola@fedoraproject.org> - 0.3.1-3
- Fix crash with multiple instances (BZ #1605231).

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Sun Jul 01 2018 Susi Lehtola <jussilehtola@fedoraproject.org> - 0.3.1-1
- Update to 0.3.1.

* Mon Jun 11 2018 Susi Lehtola <jussilehtola@fedoraproject.org> - 0.3.0-2
- Split sequential libraries from core package to openblas-serial.

* Thu May 24 2018 Susi Lehtola <jussilehtola@fedoraproject.org> - 0.3.0-1
- Update to 0.3.0.

* Thu Mar 22 2018 Susi Lehtola <jussilehtola@fedoraproject.org> - 0.2.20-10
- Disable CPU affinity unintentionally enabled upstream (BZ #1558091).

* Sun Mar 04 2018 Susi Lehtola <jussilehtola@fedoraproject.org> - 0.2.20-9
- Clean up obsolete conditionals for 64 bit builds in spec file.

* Tue Feb 27 2018 Susi Lehtola <jussilehtola@fedoraproject.org> - 0.2.20-8
- Use %%__global_ldflags instead of %%build_ldflags that doesn't work on
  all distributions.

* Tue Feb 27 2018 Susi Lehtola <jussilehtola@fedoraproject.org> - 0.2.20-7
- Honor Fedora linker flags (BZ #1548750).

* Wed Feb 14 2018 Susi Lehtola <jussilehtola@fedoraproject.org> - 0.2.20-6
- Drop arch-dependent buildrequires (BZ #1545201); no changes to package
  (only affects packages custom built with --with system_lapack).

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.20-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Tue Jan 30 2018 Florian Weimer <fweimer@redhat.com> - 0.2.20-4
- Rebuild for GCC 8

* Thu Sep 14 2017 Susi Lehtola <jussilehtola@fedoraproject.org> - 0.2.20-3
- Simplify spec, dropping extra lib arguments.

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.20-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Fri Jul 28 2017 Susi Lehtola <jussilehtola@fedoraproject.org> - 0.2.20-1
- Update to 0.2.20.

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.19-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Mon May 29 2017 Dan Horák <dan[at]danny.cz> - 0.2.19-11
- add generic s390x support (#1442048)

* Mon Mar 20 2017 Orion Poplawski <orion@cora.nwra.com> - 0.2.19-10
- Drop openblas-srpm-macros version requirement

* Mon Mar 20 2017 Orion Poplawski <orion@cora.nwra.com> - 0.2.19-9
- Move openblas-srpm-macros to separate package

* Wed Mar 15 2017 Orion Poplawski <orion@cora.nwra.com> - 0.2.19-8
- Define %%openblas_arches for dependent packages to use

* Mon Feb 13 2017 Björn Esser <besser82@fedoraproject.org> - 0.2.19-7
- Upgrade Patch4 to hopefully fully fix the issues on PPC64LE

* Fri Feb 03 2017 Björn Esser <besser82@fedoraproject.org> - 0.2.19-6
- Add Patch4 to fix register clobbers (BZ #1417385)

* Sat Jan 28 2017 Björn Esser <besser82@fedoraproject.org> - 0.2.19-5
- Rebuilt for GCC-7

* Wed Dec 14 2016 Tom Callaway <spot@fedoraproject.org> - 0.2.19-4
- build a copy of openblas that thinks it is Rblas
  There are no code changes, except for libname and soname, it is identical to libopenblas.so.0
  Unfortunately, while R itself is fine using a symlink from libopenblas.so.0 to libRblas.so
  the larger R ecosystem becomes unhappy in this scenario.

* Thu Nov 03 2016 Susi Lehtola <jussilehtola@fedoraproject.org> - 0.2.19-3
- Fix linkage of OpenMP libraries (BZ #1391491).

* Thu Oct 20 2016 Susi Lehtola <jussilehtola@fedoraproject.org> - 0.2.19-2
- Actually use 8-bit integers in 64-bit interfaces (BZ #1382916).

* Tue Oct 18 2016 Susi Lehtola <jussilehtola@fedoraproject.org> - 0.2.19-1
- Update to 0.2.19.

* Wed Aug 17 2016 Susi Lehtola <jussilehtola@fedoraproject.org> - 0.2.18-5
- Revert "minor spec cleanups" by Peter Robinson.

* Wed Jul 13 2016 Peter Robinson <pbrobinson@fedoraproject.org> 0.2.18-4
- aarch64 has execstack in Fedora
- Minor spec cleanups

* Wed Jul 13 2016 Susi Lehtola <jussilehtola@fedoraproject.org> - 0.2.18-3
- Enable ppc64 and ppc64p7 architectures
  based on Dan Horák's patch (BZ #1356189).
- Supply proper make flags to the tests.

* Tue Jul 12 2016 Jeff Bastian <jbastian@redhat.com> - 0.2.18-2
- update for aarch64

* Tue Apr 12 2016 Susi Lehtola <jussilehtola@fedoraproject.org> - 0.2.18-1
- Update to 0.2.18.

* Wed Apr 6 2016 Orion Poplawski <orion@cora.nwra.com> - 0.2.17-1
- Update to 0.2.17

* Fri Mar 18 2016 Susi Lehtola <jussilehtola@fedoraproject.org> - 0.2.16-3
- Include deprecated LAPACK functions.

* Wed Mar 16 2016 Susi Lehtola <jussilehtola@fedoraproject.org> - 0.2.16-2
- Fix library suffix on ppc64le.

* Tue Mar 15 2016 Susi Lehtola <jussilehtola@fedoraproject.org> - 0.2.16-1
- Update to 0.2.16.

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.15-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Tue Jan 12 2016 Susi Lehtola <jussilehtola@fedoraproject.org> - 0.2.15-5
- Need to use -frecursive to make LAPACK thread safe.

* Tue Jan 12 2016 Susi Lehtola <jussilehtola@fedoraproject.org> - 0.2.15-4
- Add version to bundled lapack provide.

* Mon Jan 11 2016 Orion Poplawski <orion@cora.nwra.com> - 0.2.15-3
- Allow conditional build with or without system lapack, default to without

* Tue Dec 01 2015 Susi Lehtola <jussilehtola@fedoraproject.org> - 0.2.15-2
- Enable armv7hl and ppc64le architectures.
- Build versions of the 64-bit libraries with an additional suffix
  (BZ #1287541).

* Wed Oct 28 2015 Susi Lehtola <jussilehtola@fedoraproject.org> - 0.2.15-1
- Update to 0.2.15.

* Tue Aug 04 2015 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 0.2.14-4
- Use new execstack (#1247795)

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2.14-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sun May  3 2015 Peter Robinson <pbrobinson@fedoraproject.org> 0.2.14-2
- Run ldconfig on 64 builds too

* Wed Mar 25 2015 Susi Lehtola <jussilehtola@fedoraproject.org> - 0.2.14-1
- Update to 0.2.14.

* Fri Dec 19 2014 Susi Lehtola <jussilehtola@fedoraproject.org> - 0.2.13-2
- Bump spec due to LAPACK rebuild.

* Fri Dec 05 2014 Susi Lehtola <jussilehtola@fedoraproject.org> - 0.2.13-1
- Update to 0.2.13.

* Mon Oct 13 2014 Susi Lehtola <jussilehtola@fedoraproject.org> - 0.2.12-1
- Update to 0.2.12.

* Mon Aug 18 2014 Susi Lehtola <jussilehtola@fedoraproject.org> - 0.2.11-1
- Update to 0.2.11.

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2.10-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Wed Jul 16 2014 Susi Lehtola <jussilehtola@fedoraproject.org> - 0.2.10-1
- Update to 0.2.10.

* Wed Jun 11 2014 Susi Lehtola <jussilehtola@fedoraproject.org> - 0.2.9-1
- Increase maximum amount of cores from 32 to 128.
- Add 64-bit interface support. (BZ #1088256)
- Update to 0.2.9. (BZ #1043083)

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2.8-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Wed Aug 07 2013 Susi Lehtola <jussilehtola@fedoraproject.org> - 0.2.8-1
- Update to 0.2.8.

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2.7-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Tue Jul 23 2013 Susi Lehtola <jussilehtola@fedoraproject.org> - 0.2.7-1
- Update to 0.2.7.
- Use OpenBLAS versions of LAPACK functions, as they seem to be
  working now.

* Mon Jul 08 2013 Susi Lehtola <jussilehtola@fedoraproject.org> - 0.2.5-10
- Due to long standing bug, replace all OpenBLAS LAPACK functions with
  generic ones, so that package can finally be released in stable.

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2.5-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Tue Jan 15 2013 Susi Lehtola <jussilehtola@fedoraproject.org> - 0.2.5-8
- Added LAPACKE include files.

* Mon Jan 14 2013 Susi Lehtola <jussilehtola@fedoraproject.org> - 0.2.5-7
- Fix build on RHEL5 and ppc architecture.

* Mon Dec 24 2012 Susi Lehtola <jussilehtola@fedoraproject.org> - 0.2.5-6
- Review fixes.

* Fri Dec 21 2012 Susi Lehtola <jussilehtola@fedoraproject.org> - 0.2.5-5
- Disable LAPACKE support on distributions where it is not available due to
  a too old version of lapack.

* Mon Dec 17 2012 Susi Lehtola <jussilehtola@fedoraproject.org> - 0.2.5-4
- Don't use reference LAPACK functions that have optimized implementation.

* Wed Dec 12 2012 Susi Lehtola <jussilehtola@fedoraproject.org> - 0.2.5-3
- Use system version of LAPACK.

* Mon Nov 26 2012 Susi Lehtola <jussilehtola@fedoraproject.org> - 0.2.5-2
- Fixed 32-bit build, and build on EPEL 5.

* Mon Nov 26 2012 Susi Lehtola <jussilehtola@fedoraproject.org> - 0.2.5-1
- Update to 0.2.5.

* Thu Oct 06 2011 Jussi Lehtola <jussilehtola@fedoraproject.org> - 0.1-2.alpha2.4
- Added documentation.

* Sun Sep 18 2011 Jussi Lehtola <jussilehtola@fedoraproject.org> - 0.1-1.alpha2.4
- First release.
