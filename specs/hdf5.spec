# No more Java on i686
%ifarch %{java_arches}
%bcond_without java
%else
%bcond_with java
%endif

# Patch version?
#global snaprel -beta

Name: hdf5
Version: 2.1.1
Release: %autorelease
Summary: A general purpose library and file format for storing scientific data
License: BSD-3-Clause
URL: https://www.hdfgroup.org/solutions/hdf5/
Source0: https://github.com/HDFGroup/hdf5/archive/%{version}/hdf5-%{version}.tar.gz

%global so_version 320
%global plugin_dir %{_libdir}/hdf5/plugin

Source1: h5comp
# For man pages
Source2: http://ftp.us.debian.org/debian/pool/main/h/hdf5/hdf5_1.14.4.3+repack-1~exp3.debian.tar.xz
# Fix libhdf5.settings location in wrappers for MPI builds
# https://github.com/HDFGroup/hdf5/issues/6373
Patch: hdf5-wrappers.patch
# Change jar names
Patch: hdf5-jarname.patch
# Fix JNI install directory
# https://github.com/HDFGroup/hdf5/pull/6344
Patch: hdf5-jni.patch
# Fix Fortran module directory
Patch: hdf5-fmoddir.patch

BuildRequires: cmake
BuildRequires: gcc-gfortran
%if %{with java}
BuildRequires: java-devel
BuildRequires: javapackages-tools
BuildRequires: hamcrest
BuildRequires: junit
BuildRequires: slf4j
%else
Obsoletes:     java-hdf5 < %{version}-%{release}
%endif
BuildRequires: krb5-devel
BuildRequires: perl-interpreter
BuildRequires: openssl-devel
BuildRequires: time
BuildRequires: zlib-devel
BuildRequires: zlib-static
BuildRequires: hostname
# Needed for mpi tests
BuildRequires: openssh-clients
BuildRequires: libaec-devel
BuildRequires: libaec-static
BuildRequires: gcc, gcc-c++
BuildRequires: git-core

# Provide a more relaxed version that other packages depend on
%global _hdf5_compat_version %(v=%{version}; echo ${v%.*})
Provides: %{name} = %{_hdf5_compat_version}
Provides: %{name}%{?_isa} = %{_hdf5_compat_version}

%global with_mpich %{undefined flatpak}
%if 0%{?fedora} >= 40
%ifarch %{ix86}
%global with_openmpi 0
%else
%global with_openmpi %{undefined flatpak}
%endif
%else
%global with_openmpi %{undefined flatpak}
%endif

%if %{with_mpich}
%global mpi_list mpich
%endif
%if %{with_openmpi}
%global mpi_list %{?mpi_list} openmpi
%endif

%description
HDF5 is a general purpose library and file format for storing scientific data.
HDF5 can store two primary objects: datasets and groups. A dataset is
essentially a multidimensional array of data elements, and a group is a
structure for organizing objects in an HDF5 file. Using these two basic
objects, one can create and store almost any kind of scientific data
structure, such as images, arrays of vectors, and structured and unstructured
grids. You can also mix and match them in HDF5 files according to your needs.


%package devel
Summary: HDF5 development files
Requires: %{name}%{?_isa} = %{version}-%{release}
Requires: libaec-devel%{?_isa}
Requires: zlib-devel%{?_isa}
Requires: gcc-gfortran%{?_isa}

%description devel
HDF5 development headers and libraries.

%if %{with java}
%package -n java-hdf5
Summary: HDF5 java library
Requires: %{name}%{?_isa} = %{version}-%{release}
Requires:  slf4j
Obsoletes: jhdf5 < 3.3.2^

%description -n java-hdf5
HDF5 java library
%endif

%package static
Summary: HDF5 static libraries
Requires: %{name}-devel = %{version}-%{release}

%description static
HDF5 static libraries.


%if %{with_mpich}
%package mpich
Summary: HDF5 mpich libraries
BuildRequires: mpich-devel
# Provide a more relaxed version that other packages depend on
Provides: %{name}-mpich = %{_hdf5_compat_version}
Provides: %{name}-mpich%{?_isa} = %{_hdf5_compat_version}

%description mpich
HDF5 parallel mpich libraries


%package mpich-devel
Summary: HDF5 mpich development files
Requires: %{name}-mpich%{?_isa} = %{version}-%{release}
Requires: libaec-devel%{?_isa}
Requires: zlib-devel%{?_isa}
Requires: mpich-devel%{?_isa}

%description mpich-devel
HDF5 parallel mpich development files


%package mpich-static
Summary: HDF5 mpich static libraries
Requires: %{name}-mpich-devel%{?_isa} = %{version}-%{release}
Provides: %{name}-mpich2-static = %{version}-%{release}
Obsoletes: %{name}-mpich2-static < 1.8.11-4

%description mpich-static
HDF5 parallel mpich static libraries
%endif


%if %{with_openmpi}
%package openmpi
Summary: HDF5 openmpi libraries
BuildRequires: openmpi-devel
BuildRequires: make
# Provide a more relaxed version that other packages depend on
Provides: %{name}-openmpi = %{_hdf5_compat_version}
Provides: %{name}-openmpi%{?_isa} = %{_hdf5_compat_version}

%description openmpi
HDF5 parallel openmpi libraries


%package openmpi-devel
Summary: HDF5 openmpi development files
Requires: %{name}-openmpi%{?_isa} = %{version}-%{release}
Requires: libaec-devel%{?_isa}
Requires: zlib-devel%{?_isa}
Requires: openmpi-devel%{?_isa}

%description openmpi-devel
HDF5 parallel openmpi development files


%package openmpi-static
Summary: HDF5 openmpi static libraries
Requires: %{name}-openmpi-devel%{?_isa} = %{version}-%{release}

%description openmpi-static
HDF5 parallel openmpi static libraries
%endif


%prep
%autosetup -a 2 -n %{name}-%{version}%{?snaprel} -p1


%if %{with java}
# Replace jars with system versions
# hamcrest-core is obsoleted in hamcrest-2.2
# Junit tests are failing with junit-4.13.1
%if 0%{?rhel} >= 9 || 0%{?fedora}
find . ! -name junit.jar -name "*.jar" -delete
ln -s $(build-classpath hamcrest) java/lib/hamcrest-core.jar
ln -s $(build-classpath junit) java/lib/org.junit.jar
%else
find . -name "*.jar" -delete
ln -s $(build-classpath hamcrest/core) java/lib/hamcrest-core.jar
ln -s $(build-classpath junit) java/lib/org.junit.jar
# Fix test output
junit_ver=$(sed -n '/<version>/{s/^.*>\([0-9]\.[0-9.]*\)<.*/\1/;p;q}' /usr/share/maven-poms/junit.pom)
sed -i -e "s/JUnit version .*/JUnit version $junit_ver/" java/test/testfiles/JUnit-*.txt
%endif
ln -s $(build-classpath slf4j/api) java/lib/slf4j-api-2.0.16.jar
ln -s $(build-classpath slf4j/nop) java/lib/ext/slf4j-nop-2.0.16.jar
ln -s $(build-classpath slf4j/simple) java/lib/ext/slf4j-simple-2.0.16.jar
export JAVA_HOME=%{java_home}
%endif

# Force shared by default for compiler wrappers (bug #1266645)
sed -i -e '/^STATIC_AVAILABLE=/s/=.*/=no/' */*/h5[cf]*.in


%conf
%if %{with java}
export JAVA_HOME=%{java_home}
%endif
%global cmake_opts \\\
  -DH5_DEFAULT_PLUGINDIR=%{plugin_dir} \\\
  -DHDF5_BUILD_FORTRAN:BOOL=ON \\\
  -DHDF5_BUILD_HL_LIB:BOOL=ON \\\
  -DHDF5_BUILD_TOOLS:BOOL=ON \\\
  -DHDF5_ENABLE_SZIP_SUPPORT:BOOL=ON \\\
  -DHDF5_ENABLE_ZLIB_SUPPORT:BOOL=ON \\\
  -DBUILD_TESTING:BOOL=ON \\\
%{nil}
# HDF5_BUILD_CPP_LIBa and HDF5_ENABLE_PARALLEL are incompatible
# HDF5_ENABLE_THREADSAFE is only active on Windows currently, and incompatible with HDF5_ENABLE_PARALLEL

#Serial build
export CC=gcc
export CXX=g++
export FC=gfortran
mkdir build-serial
pushd build-serial
%cmake .. \
  %{cmake_opts} \
  ${libopt} \
  -DHDF5_BUILD_CPP_LIB:BOOL=ON \
%ifnarch %{ix86}
  -DHDF5_BUILD_JAVA:BOOL=ON \
%endif
  -DHDF5_INSTALL_CMAKE_DIR=%{_lib}/cmake/%{name} \
  -DHDF5_INSTALL_DATA_DIR=share/%{name} \
  -DHDF5_INSTALL_JAR_DIR=%{_jnidir} \
  -DHDF5_INSTALL_JNI_LIB_DIR=%{_lib}/%{name} \
  -DHDF5_INSTALL_LIB_DIR=%{_lib} \
  -DHDF5_INSTALL_MODULE_DIR=%{_fmoddir}
popd

#MPI builds
export CC=mpicc
export CXX=mpicxx
export FC=mpif90
for mpi in %{?mpi_list}
do
  mkdir $mpi
  pushd $mpi
  module load mpi/$mpi-%{_arch}
  export FCFLAGS="%{build_fflags} -I$MPI_FORTRAN_MOD_DIR"
  export FFLAGS="%{build_fflags} -I$MPI_FORTRAN_MOD_DIR"
  %cmake .. \
    %{cmake_opts} \
    ${libopt} \
    -DMPIEXEC_MAX_NUMPROCS=4 \
    -DHDF5_ENABLE_PARALLEL:BOOL=ON \
    -DHDF5_INSTALL_LIB_DIR=%{_lib}/$mpi/lib \
    -DHDF5_INSTALL_BIN_DIR=%{_lib}/$mpi/bin \
    -DHDF5_INSTALL_INCLUDE_DIR=include/$mpi-%{_arch} \
    -DHDF5_INSTALL_DATA_DIR=%{_lib}/$mpi/share/%{name} \
    -DHDF5_INSTALL_CMAKE_DIR=%{_lib}/$mpi/lib/cmake/%{name} \
    -DHDF5_INSTALL_MAN_DIR=%{_lib}/$mpi/share/man \
    -DHDF5_INSTALL_MODULE_DIR=%{_fmoddir}/$mpi
  module purge
  popd
done


%build
%if %{with java}
export JAVA_HOME=%{java_home}
%endif

#Serial build
pushd build-serial
%cmake_build
popd

#MPI builds
for mpi in %{?mpi_list}
do
  pushd $mpi
  module load mpi/$mpi-%{_arch}
  %cmake_build
  module purge
  popd
done


%install
cd build-serial
%cmake_install
cd -
# Plugin directory
mkdir -p %{buildroot}%{plugin_dir}
for mpi in %{?mpi_list}
do
  pushd $mpi
  module load mpi/$mpi-%{_arch}
  %cmake_install
  # Plugin directory
  mkdir -p %{buildroot}%{_libdir}/$mpi/hdf5/plugin
  module purge
  popd
done

#Fixup headers and scripts for multiarch
%ifarch x86_64 ppc64 ia64 s390x sparc64 alpha
sed -i -e s/H5pubconf.h/H5pubconf-64.h/ ${RPM_BUILD_ROOT}%{_includedir}/H5public.h
mv ${RPM_BUILD_ROOT}%{_includedir}/H5pubconf.h \
   ${RPM_BUILD_ROOT}%{_includedir}/H5pubconf-64.h
for x in h5c++ h5cc h5fc
do
  mv ${RPM_BUILD_ROOT}%{_bindir}/${x} \
     ${RPM_BUILD_ROOT}%{_bindir}/${x}-64
  install -m 0755 %SOURCE1 ${RPM_BUILD_ROOT}%{_bindir}/${x}
done
%else
sed -i -e s/H5pubconf.h/H5pubconf-32.h/ ${RPM_BUILD_ROOT}%{_includedir}/H5public.h
mv ${RPM_BUILD_ROOT}%{_includedir}/H5pubconf.h \
   ${RPM_BUILD_ROOT}%{_includedir}/H5pubconf-32.h
for x in h5c++ h5cc h5fc
do
  mv ${RPM_BUILD_ROOT}%{_bindir}/${x} \
     ${RPM_BUILD_ROOT}%{_bindir}/${x}-32
  install -m 0755 %SOURCE1 ${RPM_BUILD_ROOT}%{_bindir}/${x}
done
%endif
# rpm macro for version checking
mkdir -p %{buildroot}%{_rpmmacrodir}
cat >%{buildroot}%{_rpmmacrodir}/macros.hdf5 <<EOF
# HDF5 compatble version is
%%_hdf5_version %{_hdf5_compat_version}
%%_hdf5_plugin_dir %{plugin_dir}
EOF

# Install man pages from debian
mkdir -p %{buildroot}%{_mandir}/man1
rm -f debian/man/*gif* debian/man/h5redeploy.1
cp -p debian/man/*.1 %{buildroot}%{_mandir}/man1/
rm %{buildroot}%{_mandir}/man1/h5p[cf]c*.1
for mpi in %{?mpi_list}
do
  mkdir -p %{buildroot}%{_libdir}/${mpi}/share/man/man1
  cp -p debian/man/h5p[cf]c*.1 %{buildroot}%{_libdir}/${mpi}/share/man/man1/
done

%if %{with java}
# Java
rm %{buildroot}%{_jnidir}/slf*.jar
%endif


%check
%ifarch %{ix86} ppc64le
# i686: t_bigio test segfaults - https://github.com/HDFGroup/hdf5/issues/2510
# ppc64le - t_multi_dset is flaky on ppc64le
fail=0
%else
fail=1
%endif
cd build-serial
ctest -V %{?_smp_mflags} || exit $fail
cd -
%ifarch %{ix86} ppc64le s390x
# i686: t_bigio test segfaults - https://github.com/HDFGroup/hdf5/issues/2510
# ppc64le - t_pmulti_dset is flaky on ppc64le
# s390x t_mpi fails with mpich
fail=0
%else
fail=1
%endif
# This will preserve generated .c files on errors if needed
#export HDF5_Make_Ignore=yes
export OMPI_MCA_rmaps_base_oversubscribe=1
# openmpi 5+
export PRTE_MCA_rmaps_default_mapping_policy=:oversubscribe
# mpich test is taking longer
export HDF5_ALARM_SECONDS=8000
for mpi in %{?mpi_list}
do
  # t_pmulti_dset hangs sometimes with mpich-aarch64/ppc64le/riscv64 so do not test on those architectures
  # https://github.com/HDFGroup/hdf5/issues/3768
  if [ "$mpi-%{_arch}" != mpich-aarch64 -a "$mpi-%{_arch}" != mpich-ppc64le -a "$mpi-%{_arch}" != mpich-riscv64 ]
  then
    module load mpi/$mpi-%{_arch}
    cd build-serial
    ctest -V %{?_smp_mflags} || exit $fail
    cd -
    module purge
  fi
done

# I have no idea why those get installed. But it's easier to just
# delete them, than to fight with the byzantine build system.
# And yes, it's using /usr/lib not %_libdir.
#if [ %_libdir != /usr/lib ]; then
#   rm -vf \
#      %{buildroot}/usr/lib/*.jar \
#      %{buildroot}/usr/lib/*.la  \
#      %{buildroot}/usr/lib/*.lai \
#      %{buildroot}/usr/lib/libhdf5*
#fi


%files
%license LICENSE
%doc ACKNOWLEDGMENTS README.md
%{_bindir}/h5clear
%{_bindir}/h5copy
%{_bindir}/h5debug
%{_bindir}/h5diff
%{_bindir}/h5delete
%{_bindir}/h5dump
%{_bindir}/h5format_convert
%{_bindir}/h5import
%{_bindir}/h5jam
%{_bindir}/h5ls
%{_bindir}/h5mkgrp
%{_bindir}/h5perf_serial
%{_bindir}/h5repack
%{_bindir}/h5repart
%{_bindir}/h5stat
%{_bindir}/h5unjam
%{_bindir}/h5watch
%{_datadir}/%{name}/
%dir %{_libdir}/%{name}
%{plugin_dir}/
%{_libdir}/libhdf5.so.%{so_version}*
%{_libdir}/libhdf5_cpp.so.%{so_version}*
%{_libdir}/libhdf5_fortran.so.%{so_version}*
%{_libdir}/libhdf5_f90cstub.so.%{so_version}*
%{_libdir}/libhdf5_hl_f90cstub.so.%{so_version}*
%{_libdir}/libhdf5_hl_fortran.so.%{so_version}*
%{_libdir}/libhdf5_hl.so.%{so_version}*
%{_libdir}/libhdf5_hl_cpp.so.%{so_version}*
%{_libdir}/libhdf5_tools.so.%{so_version}*
%{_mandir}/man1/h5copy.1*
%{_mandir}/man1/h5diff.1*
%{_mandir}/man1/h5dump.1*
%{_mandir}/man1/h5import.1*
%{_mandir}/man1/h5jam.1*
%{_mandir}/man1/h5ls.1*
%{_mandir}/man1/h5mkgrp.1*
%{_mandir}/man1/h5perf_serial.1*
%{_mandir}/man1/h5repack.1*
%{_mandir}/man1/h5repart.1*
%{_mandir}/man1/h5stat.1*
%{_mandir}/man1/h5unjam.1*

%files devel
%{_rpmmacrodir}/macros.hdf5
%{_bindir}/h5c++*
%{_bindir}/h5cc*
%{_bindir}/h5fc*
%{_includedir}/*.h
%{_includedir}/*.inc
%{_libdir}/lib*.so
%{_libdir}/lib*.settings
%{_fmoddir}/*.mod
%{_libdir}/cmake/%{name}/
%exclude %{_libdir}/cmake/%{name}/*_java*.cmake
%exclude %{_libdir}/cmake/%{name}/*_static*.cmake
%{_libdir}/pkgconfig/*.pc
%{_mandir}/man1/h5c++.1*
%{_mandir}/man1/h5cc.1*
%{_mandir}/man1/h5debug.1*
%{_mandir}/man1/h5fc.1*

%files static
%{_libdir}/*.a
%{_libdir}/cmake/%{name}/*_static*.cmake

%if %{with java}
%files -n java-hdf5
%{_jnidir}/hdf5.jar
%{_libdir}/cmake/%{name}/*_java*.cmake
%{_libdir}/%{name}/lib%{name}_java.so
%endif


%if %{with_mpich}
%files mpich
%license LICENSE
%doc README.md
%{_libdir}/mpich/bin/h5clear
%{_libdir}/mpich/bin/h5copy
%{_libdir}/mpich/bin/h5debug
%{_libdir}/mpich/bin/h5delete
%{_libdir}/mpich/bin/h5diff
%{_libdir}/mpich/bin/h5dump
%{_libdir}/mpich/bin/h5format_convert
%{_libdir}/mpich/bin/h5import
%{_libdir}/mpich/bin/h5jam
%{_libdir}/mpich/bin/h5ls
%{_libdir}/mpich/bin/h5mkgrp
%{_libdir}/mpich/bin/h5perf
%{_libdir}/mpich/bin/h5perf_serial
%{_libdir}/mpich/bin/h5repack
%{_libdir}/mpich/bin/h5repart
%{_libdir}/mpich/bin/h5stat
%{_libdir}/mpich/bin/h5unjam
%{_libdir}/mpich/bin/h5watch
%{_libdir}/mpich/bin/ph5diff
%{_libdir}/mpich/%{name}/
%{_libdir}/mpich/lib/*.so.%{so_version}*
%{_libdir}/mpich/share/%{name}/

%files mpich-devel
%{_includedir}/mpich-%{_arch}
%{_fmoddir}/mpich/*.mod
%{_libdir}/mpich/bin/h5cc
%{_libdir}/mpich/bin/h5fc
%{_libdir}/mpich/bin/h5pcc
%{_libdir}/mpich/bin/h5pfc
%{_libdir}/mpich/lib/lib*.so
%{_libdir}/mpich/lib/lib*.settings
%{_libdir}/mpich/lib/cmake/%{name}/
%exclude %{_libdir}/mpich/lib/cmake/%{name}/*_static*.cmake
%{_libdir}/mpich/lib/pkgconfig/*.pc
%{_libdir}/mpich/share/man/man1/h5p[cf]c*.1*

%files mpich-static
%{_libdir}/mpich/lib/*.a
%{_libdir}/mpich/lib/cmake/%{name}/*_static*.cmake
%endif

%if %{with_openmpi}
%files openmpi
%license LICENSE
%doc README.md
%{_libdir}/openmpi/bin/h5clear
%{_libdir}/openmpi/bin/h5copy
%{_libdir}/openmpi/bin/h5debug
%{_libdir}/openmpi/bin/h5delete
%{_libdir}/openmpi/bin/h5diff
%{_libdir}/openmpi/bin/h5dump
%{_libdir}/openmpi/bin/h5format_convert
%{_libdir}/openmpi/bin/h5import
%{_libdir}/openmpi/bin/h5jam
%{_libdir}/openmpi/bin/h5ls
%{_libdir}/openmpi/bin/h5mkgrp
%{_libdir}/openmpi/bin/h5perf
%{_libdir}/openmpi/bin/h5perf_serial
%{_libdir}/openmpi/bin/h5repack
%{_libdir}/openmpi/bin/h5repart
%{_libdir}/openmpi/bin/h5stat
%{_libdir}/openmpi/bin/h5unjam
%{_libdir}/openmpi/bin/h5watch
%{_libdir}/openmpi/bin/ph5diff
%{_libdir}/openmpi/%{name}/
%{_libdir}/openmpi/lib/*.so.%{so_version}*
%{_libdir}/openmpi/share/%{name}/

%files openmpi-devel
%{_includedir}/openmpi-%{_arch}
%{_fmoddir}/openmpi/*.mod
%{_libdir}/openmpi/bin/h5cc
%{_libdir}/openmpi/bin/h5fc
%{_libdir}/openmpi/bin/h5pcc
%{_libdir}/openmpi/bin/h5pfc
%{_libdir}/openmpi/lib/lib*.so
%{_libdir}/openmpi/lib/lib*.settings
%{_libdir}/openmpi/lib/cmake/%{name}/
%exclude %{_libdir}/openmpi/lib/cmake/%{name}/*_static*.cmake
%{_libdir}/openmpi/lib/pkgconfig/*.pc
%{_libdir}/openmpi/share/man/man1/h5p[cf]c*.1*

%files openmpi-static
%{_libdir}/openmpi/lib/*.a
%{_libdir}/openmpi/lib/cmake/%{name}/*_static*.cmake
%endif


%changelog
%autochangelog
