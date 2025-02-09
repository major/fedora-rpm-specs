%global sover 19

Name:           netcdf
Version:        4.9.2
Release:        %autorelease
Summary:        Libraries for the Unidata network Common Data Form

License:        BSD-3-Clause
URL:            http://www.unidata.ucar.edu/software/netcdf/
Source0:        https://github.com/Unidata/netcdf-c/archive/v%{version}/%{name}-%{version}.tar.gz
# Remove sonames from plugins
Patch0:         https://patch-diff.githubusercontent.com/raw/Unidata/netcdf-c/pull/2431.patch
# Fix blosc test - https://github.com/Unidata/netcdf-c/issues/2572
Patch1:         netcdf-tst-blosc.patch
# Fix segfault in octave-netcdf on exit
Patch2:         https://github.com/Unidata/netcdf-c/pull/2827.patch
# Fix incompatible types
Patch3:         https://github.com/Unidata/netcdf-c/pull/2850.patch

BuildRequires:  libtool
BuildRequires:  make
BuildRequires:  doxygen
BuildRequires:  blosc-devel
BuildRequires:  bzip2-devel
BuildRequires:  hdf-static
BuildRequires:  hdf5-devel
BuildRequires:  gawk
BuildRequires:  libcurl-devel
BuildRequires:  libxml2-devel
BuildRequires:  libzip-devel
BuildRequires:  libzstd-devel
BuildRequires:  m4
BuildRequires:  zlib-devel
%ifarch %{valgrind_arches}
BuildRequires:  valgrind
%endif
#mpiexec segfaults if ssh is not present
#https://trac.mcs.anl.gov/projects/mpich2/ticket/1576
BuildRequires:  openssh-clients
Requires:       hdf5%{?_isa} = %{_hdf5_version}

%global with_mpich %{undefined flatpak}
%if 0%{?fedora} >= 40
%ifarch %{ix86}
    # No OpenMPI support on these arches
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

# mpich parallel tests are hanging on s390x
%ifarch s390x
%bcond_with parallel_tests
%else
%bcond_without parallel_tests
%endif

%description
NetCDF (network Common Data Form) is an interface for array-oriented 
data access and a freely-distributed collection of software libraries 
for C, Fortran, C++, and perl that provides an implementation of the 
interface.  The NetCDF library also defines a machine-independent 
format for representing scientific data.  Together, the interface, 
library, and format support the creation, access, and sharing of 
scientific data. The NetCDF software was developed at the Unidata 
Program Center in Boulder, Colorado.

NetCDF data is: 

   o Self-Describing: A NetCDF file includes information about the
     data it contains.

   o Network-transparent:  A NetCDF file is represented in a form that
     can be accessed by computers with different ways of storing
     integers, characters, and floating-point numbers.

   o Direct-access:  A small subset of a large dataset may be accessed
     efficiently, without first reading through all the preceding
     data.

   o Appendable:  Data can be appended to a NetCDF dataset along one
     dimension without copying the dataset or redefining its
     structure. The structure of a NetCDF dataset can be changed,
     though this sometimes causes the dataset to be copied.

   o Sharable:  One writer and multiple readers may simultaneously
     access the same NetCDF file.


%package devel
Summary:        Development files for netcdf
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       pkgconfig%{?_isa}
Requires:       hdf5-devel%{?_isa}
Requires:       libcurl-devel%{?_isa}

%description devel
This package contains the netCDF C header files, shared devel libs, and 
man pages.


%package static
Summary:        Static libs for netcdf
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description static
This package contains the netCDF C static libs.


%if %{with_mpich}
%package mpich
Summary: NetCDF mpich libraries
Requires: hdf5-mpich%{?_isa} = %{_hdf5_version}
BuildRequires: mpich-devel
BuildRequires: hdf5-mpich-devel >= 1.8.4
Provides: %{name}-mpich2 = %{version}-%{release}
Obsoletes: %{name}-mpich2 < 4.3.0-4

%description mpich
NetCDF parallel mpich libraries


%package mpich-devel
Summary: NetCDF mpich development files
Requires: %{name}-mpich%{?_isa} = %{version}-%{release}
Requires: pkgconfig%{?_isa}
Requires: hdf5-mpich-devel%{?_isa}
Requires: libcurl-devel%{?_isa}
Provides: %{name}-mpich2-devel = %{version}-%{release}
Obsoletes: %{name}-mpich2-devel < 4.3.0-4

%description mpich-devel
NetCDF parallel mpich development files


%package mpich-static
Summary: NetCDF mpich static libraries
Requires: %{name}-mpich-devel%{?_isa} = %{version}-%{release}
Provides: %{name}-mpich2-static = %{version}-%{release}
Obsoletes: %{name}-mpich2-static < 4.3.0-4

%description mpich-static
NetCDF parallel mpich static libraries
%endif


%if %{with_openmpi}
%package openmpi
Summary: NetCDF openmpi libraries
Requires: hdf5-openmpi%{?_isa} = %{_hdf5_version}
BuildRequires: openmpi-devel
BuildRequires: hdf5-openmpi-devel >= 1.8.4

%description openmpi
NetCDF parallel openmpi libraries


%package openmpi-devel
Summary: NetCDF openmpi development files
Requires: %{name}-openmpi%{_isa} = %{version}-%{release}
Requires: openmpi-devel%{?_isa}
Requires: pkgconfig%{?_isa}
Requires: hdf5-openmpi-devel%{?_isa}
Requires: libcurl-devel%{?_isa}

%description openmpi-devel
NetCDF parallel openmpi development files


%package openmpi-static
Summary: NetCDF openmpi static libraries
Requires: %{name}-openmpi-devel%{?_isa} = %{version}-%{release}

%description openmpi-static
NetCDF parallel openmpi static libraries
%endif


%prep
%autosetup -p1 -n %{name}-c-%{version}
# For Patch0
./bootstrap


%build
#Do out of tree builds
%global _configure ../configure
#Common configure options
export LDFLAGS="%{__global_ldflags} -L%{_libdir}/hdf"
export CFLAGS="%{optflags} -fno-strict-aliasing"
%global configure_opts \\\
           --enable-shared \\\
           --enable-netcdf-4 \\\
           --enable-dap \\\
           --enable-extra-example-tests \\\
           CPPFLAGS="-I%{_includedir}/hdf" \\\
           LIBS="-ltirpc" \\\
           --enable-hdf4 \\\
           --disable-dap-remote-tests \\\
%{nil}

# Serial build
mkdir build
pushd build
ln -s ../configure .
%configure %{configure_opts} \
  --with-plugin-dir=%{_libdir}/hdf5/plugin
# Workaround libtool reordering -Wl,--as-needed after all the libraries.
sed -e 's|CC="\(.*g..\)"|CC="\1 -Wl,--as-needed"|' -i libtool
%make_build
popd

# MPI builds
for mpi in %{?mpi_list}
do
  mkdir $mpi
  pushd $mpi
  module load mpi/$mpi-%{_arch}
  ln -s ../configure .
  # parallel tests hang on s390(x)
  %configure %{configure_opts} \
    CC=mpicc \
    --libdir=%{_libdir}/$mpi/lib \
    --bindir=%{_libdir}/$mpi/bin \
    --sbindir=%{_libdir}/$mpi/sbin \
    --includedir=%{_includedir}/$mpi-%{_arch} \
    --datarootdir=%{_libdir}/$mpi/share \
    --mandir=%{_libdir}/$mpi/share/man \
    --with-plugin-dir=%{_libdir}/$mpi/hdf5/plugin \
    %{?with_parallel_tests:--enable-parallel-tests}
  # Workaround libtool reordering -Wl,--as-needed after all the libraries.
  sed -e 's|CC="\(.*g..\)"|CC="\1 -Wl,--as-needed"|' -i libtool
  %make_build
  module purge
  popd
done


%install
make -C build install DESTDIR=${RPM_BUILD_ROOT}
/bin/rm -f ${RPM_BUILD_ROOT}%{_infodir}/dir
for mpi in %{?mpi_list}
do
  module load mpi/$mpi-%{_arch}
  make -C $mpi install DESTDIR=${RPM_BUILD_ROOT}
  module purge
done
find $RPM_BUILD_ROOT/%{_libdir} -name \*.la -delete


%check
# Set to 1 to fail if tests fail
%ifarch %{ix86} s390x
# tst_filter fails on s390x
# https://github.com/Unidata/netcdf-c/issues/1338
# i686 - Testing parallel I/O with zlib compression...malloc(): invalid size (unsorted)
# https://github.com/Unidata/netcdf-c/issues/1685
fail=0
%else
fail=1
%endif
make -C build check || ( cat build/*/test-suite.log && exit $fail )
# Allow openmpi to run with more processes than cores
export OMPI_MCA_rmaps_base_oversubscribe=1
# openmpi 5+
export PRTE_MCA_rmaps_default_mapping_policy=:oversubscribe
# openmpi test hangs on armv7hl in h5_test after tst_h_rename
%ifnarch armv7hl
for mpi in %{?mpi_list}
do
  module load mpi/$mpi-%{_arch}
  make -C $mpi check || ( cat $mpi/*/test-suite.log && exit $fail )
  module purge
done
%endif


%ldconfig_scriptlets


%files
%license COPYRIGHT
%doc README.md RELEASE_NOTES.md
%{_bindir}/nccopy
%{_bindir}/ncdump
%{_bindir}/ncgen
%{_bindir}/ncgen3
%{_bindir}/nc4print
%{_bindir}/ocprint
%{_libdir}/hdf5/plugin/lib__nch5deflate.so
%{_libdir}/hdf5/plugin/lib__nch5shuffle.so
%{_libdir}/hdf5/plugin/lib__nch5bzip2.so
%{_libdir}/hdf5/plugin/lib__nch5zstd.so
%{_libdir}/hdf5/plugin/lib__nch5szip.so
%{_libdir}/hdf5/plugin/lib__nczhdf5filters.so
%{_libdir}/hdf5/plugin/lib__nczstdfilters.so
%{_libdir}/hdf5/plugin/lib__nch5fletcher32.so
%{_libdir}/hdf5/plugin/lib__nch5blosc.so
%{_libdir}/*.so.%{sover}*
%{_mandir}/man1/*

%files devel
%doc examples
%{_bindir}/nc-config
%{_includedir}/netcdf.h
%{_includedir}/netcdf_aux.h
%{_includedir}/netcdf_dispatch.h
%{_includedir}/netcdf_filter.h
%{_includedir}/netcdf_filter_build.h
%{_includedir}/netcdf_filter_hdf5_build.h
%{_includedir}/netcdf_json.h
%{_includedir}/netcdf_meta.h
%{_includedir}/netcdf_mem.h
%{_libdir}/libnetcdf.settings
%{_libdir}/*.so
%{_libdir}/pkgconfig/netcdf.pc
%{_mandir}/man3/*

%files static
%{_libdir}/*.a

%if %{with_mpich}
%files mpich
%license COPYRIGHT
%doc README.md RELEASE_NOTES.md
%{_libdir}/mpich/bin/nccopy
%{_libdir}/mpich/bin/ncdump
%{_libdir}/mpich/bin/ncgen
%{_libdir}/mpich/bin/ncgen3
%{_libdir}/mpich/bin/nc4print
%{_libdir}/mpich/bin/ocprint
%{_libdir}/mpich/hdf5/plugin/*
%{_libdir}/mpich/lib/*.so.%{sover}*
%doc %{_libdir}/mpich/share/man/man1/*.1*

%files mpich-devel
%{_libdir}/mpich/bin/nc-config
%{_includedir}/mpich-%{_arch}/netcdf.h
%{_includedir}/mpich-%{_arch}/netcdf_aux.h
%{_includedir}/mpich-%{_arch}/netcdf_dispatch.h
%{_includedir}/mpich-%{_arch}/netcdf_filter.h
%{_includedir}/mpich-%{_arch}/netcdf_filter_build.h
%{_includedir}/mpich-%{_arch}/netcdf_filter_hdf5_build.h
%{_includedir}/mpich-%{_arch}/netcdf_json.h
%{_includedir}/mpich-%{_arch}/netcdf_meta.h
%{_includedir}/mpich-%{_arch}/netcdf_mem.h
%{_includedir}/mpich-%{_arch}/netcdf_par.h
%{_libdir}/mpich/lib/libnetcdf.settings
%{_libdir}/mpich/lib/*.so
%{_libdir}/mpich/lib/pkgconfig/%{name}.pc
%doc %{_libdir}/mpich/share/man/man3/*.3*

%files mpich-static
%{_libdir}/mpich/lib/*.a
%endif

%if %{with_openmpi}
%files openmpi
%license COPYRIGHT
%doc README.md RELEASE_NOTES.md
%{_libdir}/openmpi/bin/nccopy
%{_libdir}/openmpi/bin/ncdump
%{_libdir}/openmpi/bin/ncgen
%{_libdir}/openmpi/bin/ncgen3
%{_libdir}/openmpi/bin/nc4print
%{_libdir}/openmpi/bin/ocprint
%{_libdir}/openmpi/hdf5/plugin/*
%{_libdir}/openmpi/lib/*.so.%{sover}*
%doc %{_libdir}/openmpi/share/man/man1/*.1*

%files openmpi-devel
%{_libdir}/openmpi/bin/nc-config
%{_includedir}/openmpi-%{_arch}/netcdf.h
%{_includedir}/openmpi-%{_arch}/netcdf_aux.h
%{_includedir}/openmpi-%{_arch}/netcdf_dispatch.h
%{_includedir}/openmpi-%{_arch}/netcdf_filter.h
%{_includedir}/openmpi-%{_arch}/netcdf_filter_build.h
%{_includedir}/openmpi-%{_arch}/netcdf_filter_hdf5_build.h
%{_includedir}/openmpi-%{_arch}/netcdf_json.h
%{_includedir}/openmpi-%{_arch}/netcdf_meta.h
%{_includedir}/openmpi-%{_arch}/netcdf_mem.h
%{_includedir}/openmpi-%{_arch}/netcdf_par.h
%{_libdir}/openmpi/lib/libnetcdf.settings
%{_libdir}/openmpi/lib/*.so
%{_libdir}/openmpi/lib/pkgconfig/%{name}.pc
%doc %{_libdir}/openmpi/share/man/man3/*.3*

%files openmpi-static
%{_libdir}/openmpi/lib/*.a
%endif


%changelog
%autochangelog
