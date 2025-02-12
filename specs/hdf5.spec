%global macrosdir %(d=%{_rpmconfigdir}/macros.d; [ -d $d ] || d=%{_sysconfdir}/rpm; echo $d)

# No more Java on i686
%ifarch %{java_arches}
%bcond_without java
%else
%bcond_with java
%endif

# Patch version?
#global snaprel -beta

Name: hdf5
Version: 1.14.6
Release: %autorelease
Summary: A general purpose library and file format for storing scientific data
License: BSD-3-Clause
URL: https://www.hdfgroup.org/solutions/hdf5/
Source0: https://github.com/HDFGroup/hdf5/archive/hdf5_%{version}/hdf5-%{version}.tar.gz

%global so_version 310

Source1: h5comp
# For man pages
Source2: http://ftp.us.debian.org/debian/pool/main/h/hdf5/hdf5_1.14.4.3+repack-1~exp3.debian.tar.xz
# Fix java build
Patch0: hdf5-build.patch
# Get size of __float128
# https://github.com/HDFGroup/hdf5/pull/4924
Patch1: hdf5-float128.patch
# Remove Fedora build flags from h5cc/h5c++/h5fc
# https://bugzilla.redhat.com/show_bug.cgi?id=1794625
Patch2: hdf5-wrappers.patch

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
BuildRequires: openssl-devel
BuildRequires: time
BuildRequires: zlib-devel
BuildRequires: hostname
# For patches/rpath
BuildRequires: automake
BuildRequires: libtool
# Needed for mpi tests
BuildRequires: openssh-clients
BuildRequires: libaec-devel
BuildRequires: gcc, gcc-c++
BuildRequires: git-core

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
Provides: %{name}-mpich2 = %{version}-%{release}
Obsoletes: %{name}-mpich2 < 1.8.11-4

%description mpich
HDF5 parallel mpich libraries


%package mpich-devel
Summary: HDF5 mpich development files
Requires: %{name}-mpich%{?_isa} = %{version}-%{release}
Requires: libaec-devel%{?_isa}
Requires: zlib-devel%{?_isa}
Requires: mpich-devel%{?_isa}
Provides: %{name}-mpich2-devel = %{version}-%{release}
Obsoletes: %{name}-mpich2-devel < 1.8.11-4

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
%autosetup -a 2 -n %{name}-%{name}_%{version} -p1


%build
%if %{with java}
# Replace jars with system versions
# hamcrest-core is obsoleted in hamcrest-2.2
# Junit tests are failing with junit-4.13.1
%if 0%{?rhel} >= 9 || 0%{?fedora}
find . ! -name junit.jar -name "*.jar" -delete
ln -s $(build-classpath hamcrest) java/lib/hamcrest-core.jar
%else
find . -name "*.jar" -delete
ln -s $(build-classpath hamcrest/core) java/lib/hamcrest-core.jar
ln -s $(build-classpath junit) java/lib/junit.jar
# Fix test output
junit_ver=$(sed -n '/<version>/{s/^.*>\([0-9]\.[0-9.]*\)<.*/\1/;p;q}' /usr/share/maven-poms/junit.pom)
sed -i -e "s/JUnit version .*/JUnit version $junit_ver/" java/test/testfiles/JUnit-*.txt
%endif
ln -s $(build-classpath slf4j/api) java/lib/slf4j-api-2.0.6.jar
ln -s $(build-classpath slf4j/nop) java/lib/ext/slf4j-nop-2.0.6.jar
ln -s $(build-classpath slf4j/simple) java/lib/ext/slf4j-simple-2.0.6.jar
%endif

# Force shared by default for compiler wrappers (bug #1266645)
sed -i -e '/^STATIC_AVAILABLE=/s/=.*/=no/' */*/h5[cf]*.in
sh ./autogen.sh

# Modify low optimization level for gnu compilers
sed -e 's|-O -finline-functions|-O3 -finline-functions|g' -i config/gnu-flags

#Do out of tree builds
%global _configure ../configure
#Common configure options
%global configure_opts \\\
  --disable-silent-rules \\\
  --enable-fortran \\\
  --enable-hl \\\
  --enable-shared \\\
  --with-szlib \\\
%{nil}
# --enable-cxx and --enable-parallel flags are incompatible
# --with-mpe=DIR Use MPE instrumentation [default=no]
# --enable-cxx/fortran/parallel and --enable-threadsafe flags are incompatible

#Serial build
export CC=gcc
export CXX=g++
export F9X=gfortran
export LDFLAGS="%{__global_ldflags} -fPIC -Wl,-z,now -Wl,--as-needed"
mkdir build
pushd build
ln -s ../configure .
%configure \
  %{configure_opts} \
  --enable-cxx \
%if %{with java}
  --enable-java \
%endif
  --with-default-plugindir=%{_libdir}/hdf5/plugin \
  --with-fmoddir=%{_fmoddir}
sed -i -e 's| -shared | -Wl,--as-needed\0|g' libtool
sed -r -i 's|^prefix=/usr|prefix=%{buildroot}/usr|' java/test/junit.sh
%make_build LDFLAGS="%{__global_ldflags} -fPIC -Wl,-z,now -Wl,--as-needed"
popd

#MPI builds
export LDFLAGS="%{__global_ldflags} -fPIC -Wl,-z,now -Wl,--as-needed"
for mpi in %{?mpi_list}
do
  mkdir $mpi
  pushd $mpi
  module load mpi/$mpi-%{_arch}
  ln -s ../configure .
  %configure \
    %{configure_opts} \
    CC=mpicc CXX=mpicxx F9X=mpif90 \
    FCFLAGS="$FCFLAGS -I$MPI_FORTRAN_MOD_DIR" \
    --enable-parallel \
    --exec-prefix=%{_libdir}/$mpi \
    --libdir=%{_libdir}/$mpi/lib \
    --bindir=%{_libdir}/$mpi/bin \
    --sbindir=%{_libdir}/$mpi/sbin \
    --includedir=%{_includedir}/$mpi-%{_arch} \
    --datarootdir=%{_libdir}/$mpi/share \
    --mandir=%{_libdir}/$mpi/share/man \
    --with-default-plugindir=%{_libdir}/$mpi/hdf5/plugin \
    --with-fmoddir=${MPI_FORTRAN_MOD_DIR}
  sed -i -e 's! -shared ! -Wl,--as-needed\0!g' libtool
  %make_build LDFLAGS="%{__global_ldflags} -fPIC -Wl,-z,now -Wl,--as-needed"
  module purge
  popd
done


%install
# Fortran modules
mkdir -p %{buildroot}%{_fmoddir}
%make_install -C build
rm %{buildroot}%{_libdir}/*.la
# Plugin directory
mkdir -p %{buildroot}%{_libdir}/hdf5/plugin
for mpi in %{?mpi_list}
do
  module load mpi/$mpi-%{_arch}
  # Fortran modules
  mkdir -p %{buildroot}${MPI_FORTRAN_MOD_DIR}
  %make_install -C $mpi
  rm %{buildroot}/%{_libdir}/$mpi/lib/*.la
  # Plugin directory
  mkdir -p %{buildroot}%{_libdir}/$mpi/hdf5/plugin
  module purge
done

#Fixup headers and scripts for multiarch
%ifarch x86_64 ppc64 ia64 s390x sparc64 alpha
sed -i -e s/H5pubconf.h/H5pubconf-64.h/ %{buildroot}%{_includedir}/H5public.h
mv %{buildroot}%{_includedir}/H5pubconf.h \
   %{buildroot}%{_includedir}/H5pubconf-64.h
for x in h5c++ h5cc h5fc
do
  mv %{buildroot}%{_bindir}/${x} \
     %{buildroot}%{_bindir}/${x}-64
  install -m 0755 %SOURCE1 %{buildroot}%{_bindir}/${x}
done
%else
sed -i -e s/H5pubconf.h/H5pubconf-32.h/ %{buildroot}%{_includedir}/H5public.h
mv %{buildroot}%{_includedir}/H5pubconf.h \
   %{buildroot}%{_includedir}/H5pubconf-32.h
for x in h5c++ h5cc h5fc
do
  mv %{buildroot}%{_bindir}/${x} \
     %{buildroot}%{_bindir}/${x}-32
  install -m 0755 %SOURCE1 %{buildroot}%{_bindir}/${x}
done
%endif
# rpm macro for version checking
mkdir -p %{buildroot}%{macrosdir}
cat > %{buildroot}%{macrosdir}/macros.hdf5 <<EOF
# HDF5 compatble version is
%%_hdf5_version %(v=%{version}; echo ${v%.*})
EOF

# Install man pages from debian
mkdir -p %{buildroot}%{_mandir}/man1
cp -p debian/man/*.1 %{buildroot}%{_mandir}/man1/
rm %{buildroot}%{_mandir}/man1/*gif*
for mpi in %{?mpi_list}
do
  mkdir -p %{buildroot}%{_libdir}/$mpi/share/man/man1
  cp -p debian/man/h5p[cf]c.1 %{buildroot}%{_libdir}/$mpi/share/man/man1/
done
rm %{buildroot}%{_mandir}/man1/h5p[cf]c*.1

%if %{with java}
# Java
mkdir -p %{buildroot}%{_libdir}/%{name}
mv %{buildroot}%{_libdir}/libhdf5_java.so %{buildroot}%{_libdir}/%{name}/
%endif


%check
%ifarch %{ix86}
# i686: t_bigio test segfaults - https://github.com/HDFGroup/hdf5/issues/2510
fail=0
%else
fail=1
%endif
make -C build check || exit $fail
%ifarch %{ix86} s390x
# i686: t_bigio test segfaults - https://github.com/HDFGroup/hdf5/issues/2510
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
  # t_pmulti_dset hangs sometimes with mpich-aarch64 so do not test on that architecture
  # https://github.com/HDFGroup/hdf5/issues/3768
#  if [ "$mpi-%{_arch}" != mpich-aarch64 ]
#  then
    module load mpi/$mpi-%{_arch}
    make -C $mpi check || exit $fail
    module purge
#  fi
done

# I have no idea why those get installed. But it's easier to just
# delete them, than to fight with the byzantine build system.
# And yes, it's using /usr/lib not %_libdir.
if [ %_libdir != /usr/lib ]; then
   rm -vf \
      %{buildroot}/usr/lib/*.jar \
      %{buildroot}/usr/lib/*.la  \
      %{buildroot}/usr/lib/*.lai \
      %{buildroot}/usr/lib/libhdf5*
fi


%files
%license COPYING
%doc ACKNOWLEDGMENTS README.md release_docs/RELEASE.txt
%{_bindir}/h5clear
%{_bindir}/h5copy
%{_bindir}/h5debug
%{_bindir}/h5diff
%{_bindir}/h5delete
%{_bindir}/h5dump
%{_bindir}/h5format_convert
%{_bindir}/h5fuse
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
%dir %{_libdir}/%{name}
%{_libdir}/%{name}/plugin/
%{_libdir}/libhdf5.so.%{so_version}*
%{_libdir}/libhdf5_cpp.so.%{so_version}*
%{_libdir}/libhdf5_fortran.so.%{so_version}*
%{_libdir}/libhdf5hl_fortran.so.%{so_version}*
%{_libdir}/libhdf5_hl.so.%{so_version}*
%{_libdir}/libhdf5_hl_cpp.so.%{so_version}*
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
%{macrosdir}/macros.hdf5
%{_bindir}/h5c++*
%{_bindir}/h5cc*
%{_bindir}/h5fc*
%{_bindir}/h5redeploy
%{_includedir}/*.h
%{_includedir}/*.inc
%{_libdir}/*.so
%{_libdir}/*.settings
%{_fmoddir}/*.mod
%{_mandir}/man1/h5c++.1*
%{_mandir}/man1/h5cc.1*
%{_mandir}/man1/h5debug.1*
%{_mandir}/man1/h5fc.1*
%{_mandir}/man1/h5redeploy.1*

%files static
%{_libdir}/*.a

%if %{with java}
%files -n java-hdf5
%{_jnidir}/hdf5.jar
%{_libdir}/%{name}/*
%endif

%if %{with_mpich}
%files mpich
%license COPYING
%doc README.md release_docs/RELEASE.txt
%{_libdir}/mpich/bin/h5clear
%{_libdir}/mpich/bin/h5copy
%{_libdir}/mpich/bin/h5debug
%{_libdir}/mpich/bin/h5delete
%{_libdir}/mpich/bin/h5diff
%{_libdir}/mpich/bin/h5dump
%{_libdir}/mpich/bin/h5format_convert
%{_libdir}/mpich/bin/h5fuse
%{_libdir}/mpich/bin/h5import
%{_libdir}/mpich/bin/h5jam
%{_libdir}/mpich/bin/h5ls
%{_libdir}/mpich/bin/h5mkgrp
%{_libdir}/mpich/bin/h5redeploy
%{_libdir}/mpich/bin/h5repack
%{_libdir}/mpich/bin/h5perf
%{_libdir}/mpich/bin/h5perf_serial
%{_libdir}/mpich/bin/h5repart
%{_libdir}/mpich/bin/h5stat
%{_libdir}/mpich/bin/h5unjam
%{_libdir}/mpich/bin/h5watch
%{_libdir}/mpich/bin/ph5diff
%{_libdir}/mpich/%{name}/
%{_libdir}/mpich/lib/*.so.%{so_version}*

%files mpich-devel
%{_includedir}/mpich-%{_arch}
%{_fmoddir}/mpich/*.mod
%{_libdir}/mpich/bin/h5pcc
%{_libdir}/mpich/bin/h5pfc
%{_libdir}/mpich/lib/lib*.so
%{_libdir}/mpich/lib/lib*.settings
%{_libdir}/mpich/share/man/man1/h5pcc.1*
%{_libdir}/mpich/share/man/man1/h5pfc.1*

%files mpich-static
%{_libdir}/mpich/lib/*.a
%endif

%if %{with_openmpi}
%files openmpi
%license COPYING
%doc README.md release_docs/RELEASE.txt
%{_libdir}/openmpi/bin/h5clear
%{_libdir}/openmpi/bin/h5copy
%{_libdir}/openmpi/bin/h5debug
%{_libdir}/openmpi/bin/h5delete
%{_libdir}/openmpi/bin/h5diff
%{_libdir}/openmpi/bin/h5dump
%{_libdir}/openmpi/bin/h5format_convert
%{_libdir}/openmpi/bin/h5fuse
%{_libdir}/openmpi/bin/h5import
%{_libdir}/openmpi/bin/h5jam
%{_libdir}/openmpi/bin/h5ls
%{_libdir}/openmpi/bin/h5mkgrp
%{_libdir}/openmpi/bin/h5perf
%{_libdir}/openmpi/bin/h5perf_serial
%{_libdir}/openmpi/bin/h5redeploy
%{_libdir}/openmpi/bin/h5repack
%{_libdir}/openmpi/bin/h5repart
%{_libdir}/openmpi/bin/h5stat
%{_libdir}/openmpi/bin/h5unjam
%{_libdir}/openmpi/bin/h5watch
%{_libdir}/openmpi/bin/ph5diff
%{_libdir}/openmpi/%{name}/
%{_libdir}/openmpi/lib/*.so.%{so_version}*

%files openmpi-devel
%{_includedir}/openmpi-%{_arch}
%{_fmoddir}/openmpi/*.mod
%{_libdir}/openmpi/bin/h5pcc
%{_libdir}/openmpi/bin/h5pfc
%{_libdir}/openmpi/lib/lib*.so
%{_libdir}/openmpi/lib/lib*.settings
%{_libdir}/openmpi/share/man/man1/h5pcc.1*
%{_libdir}/openmpi/share/man/man1/h5pfc.1*

%files openmpi-static
%{_libdir}/openmpi/lib/*.a
%endif


%changelog
%autochangelog
