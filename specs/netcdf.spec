%global sover 22

Name:           netcdf
Version:        4.10.0
Release:        %autorelease
Summary:        Libraries for the Unidata network Common Data Form

License:        BSD-3-Clause
URL:            http://www.unidata.ucar.edu/software/netcdf/
Source0:        https://github.com/Unidata/netcdf-c/archive/v%{version}/%{name}-%{version}.tar.gz
# https://github.com/Unidata/netcdf-c/pull/3300
Patch:          netcdf-mfhdf.patch
# Incomplete fix for rpaths
# https://github.com/Unidata/netcdf-c/issues/3302
Patch:          netcdf-rpath.patch
# big-endian fixes
Patch:          https://github.com/Unidata/netcdf-c/pull/3285.patch
# Do not assume that CMAKE_INSTALL_INCLUDEDIR and CMAKE_INSTALL_LIBDIR are relative paths
Patch:          https://github.com/Unidata/netcdf-c/pull/3350.patch

# Hack for now
BuildRequires:  chrpath
BuildRequires:  cmake
BuildRequires:  doxygen
BuildRequires:  gcc-c++
BuildRequires:  blosc-devel
BuildRequires:  bzip2-devel
BuildRequires:  hdf-devel
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
%endif


%prep
%autosetup -p1 -n %{name}-c-%{version}


%conf
# $mpi will be evaluated in the loops below
%global _vpath_builddir %{_vendor}-%{_target_os}-build-${mpi:-serial}

# Options
%global cmake_opts \\\
  -DMFHDF_H_INCLUDE_DIR=%{_includedir}/hdf \\\
  -DNETCDF_ENABLE_DAP_REMOTE_TESTS=OFF \\\
  -DNETCDF_ENABLE_EXTRA_TESTS=ON \\\
  -DNETCDF_ENABLE_HDF4=ON \\\
  -DNETCDF_ENABLE_S3_INTERNAL=ON \\\
  -DNETCDF_PLUGIN_INSTALL=ON

# Serial build
%cmake %{cmake_opts} \
  -DNETCDF_WITH_PLUGIN_DIR=%{_libdir}/hdf5/plugin

# MPI builds
export CC=mpicc
export CXX=mpic++
for mpi in %{?mpi_list}
do
  module load mpi/$mpi-%{_arch}
  %cmake %{cmake_opts} \
    -DCMAKE_PREFIX_PATH:PATH=$MPI_HOME \
    -DCMAKE_INSTALL_PREFIX:PATH=$MPI_HOME \
    -DCMAKE_INSTALL_INCLUDEDIR=%{_includedir}/$mpi-%{_arch} \
    -DCMAKE_INSTALL_LIBDIR:PATH=lib \
    -DCMAKE_INSTALL_JNILIBDIR:PATH=lib/%{name} \
    %{?with_parallel_tests:-DNETCDF_ENABLE_PARALLEL_TESTS=ON} \
    -DNETCDF_WITH_PLUGIN_DIR=%{_libdir}/$mpi/hdf5/plugin
  module purge
done


%build
%cmake_build
for mpi in %{mpi_list}
do
  module load mpi/$mpi-%{_arch}
  %cmake_build
  module purge
done


%install
%cmake_install
for mpi in %{?mpi_list}
do
  module load mpi/$mpi-%{_arch}
  %cmake_install
  module purge
done
# rpaths are still present in MPI builds
chrpath --delete %{buildroot}%{_libdir}/*/hdf5/plugin/lib__*.so %{buildroot}%{_libdir}/*/bin/nc[cdg]*


%check
# hdf4_test_run_get_hdf4_files - requires network
# nczarr_test_run_external - requires network
# nczarr_test_run_s3_credentials - requires network
exclude="hdf4_test_run_get_hdf4_files|nczarr_test_run_(external|s3_credentials)"
exclude_arch=""
%ifarch s390x
# s390x - tst_h5_endians fails - Little_Endian Float/Int
# https://github.com/Unidata/netcdf-c/issues/3062
# Various other failures - https://github.com/Unidata/netcdf-c/issues/2696
exclude_arch="nc_test4_tst_h5_endians|dap4_test_test_raw|dap4_test_test_data|nczarr_test_run_ut_mapapi|nczarr_test_run_jsonconvention|nczarr_test_run_oldkeys|nc_test4_run_par_test|h5_test_run_par_tests"
exclude="$exclude|$exclude_arch"
%endif
%ifarch %{ix86}
# i686 - tst_netcdf4_4 fails - var5:_Filter difference
# https://github.com/Unidata/netcdf-c/issues/2433
exclude_arch="ncdump_tst_netcdf4_4"
exclude="$exclude|$exclude_arch"
%endif
%ctest --verbose -E "$exclude"
# Keep track of the status of failing tests
%ctest --verbose -R "$exclude_arch" || :

# Allow openmpi to run with more processes than cores
export PRTE_MCA_rmaps_default_mapping_policy=:oversubscribe
for mpi in %{?mpi_list}
do
  module load mpi/$mpi-%{_arch}
  %ctest --verbose -E "$exclude"
  %ctest --verbose -R "$exclude_arch" || :
  module purge
done


%files
%license COPYRIGHT
%doc README.md RELEASE_NOTES.md
%{_bindir}/nccopy
%{_bindir}/ncdump
%{_bindir}/ncgen
%{_bindir}/ncgen3
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
%{_includedir}/netcdf_json.h
%{_includedir}/netcdf_meta.h
%{_includedir}/netcdf_mem.h
%{_includedir}/netcdf_proplist.h
%{_includedir}/netcdf_vutils.h
%{_libdir}/libnetcdf.settings
%{_libdir}/*.so
%{_libdir}/cmake/
%{_libdir}/pkgconfig/netcdf.pc
%{_mandir}/man3/*

%if %{with_mpich}
%files mpich
%license COPYRIGHT
%doc README.md RELEASE_NOTES.md
%{_libdir}/mpich/bin/nccopy
%{_libdir}/mpich/bin/ncdump
%{_libdir}/mpich/bin/ncgen
%{_libdir}/mpich/bin/ncgen3
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
%{_includedir}/mpich-%{_arch}/netcdf_json.h
%{_includedir}/mpich-%{_arch}/netcdf_meta.h
%{_includedir}/mpich-%{_arch}/netcdf_mem.h
%{_includedir}/mpich-%{_arch}/netcdf_par.h
%{_includedir}/mpich-%{_arch}/netcdf_proplist.h
%{_includedir}/mpich-%{_arch}/netcdf_vutils.h
%{_libdir}/mpich/lib/libnetcdf.settings
%{_libdir}/mpich/lib/*.so
%{_libdir}/mpich/lib/cmake/
%{_libdir}/mpich/lib/pkgconfig/%{name}.pc
%doc %{_libdir}/mpich/share/man/man3/*.3*
%endif

%if %{with_openmpi}
%files openmpi
%license COPYRIGHT
%doc README.md RELEASE_NOTES.md
%{_libdir}/openmpi/bin/nccopy
%{_libdir}/openmpi/bin/ncdump
%{_libdir}/openmpi/bin/ncgen
%{_libdir}/openmpi/bin/ncgen3
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
%{_includedir}/openmpi-%{_arch}/netcdf_json.h
%{_includedir}/openmpi-%{_arch}/netcdf_meta.h
%{_includedir}/openmpi-%{_arch}/netcdf_mem.h
%{_includedir}/openmpi-%{_arch}/netcdf_par.h
%{_includedir}/openmpi-%{_arch}/netcdf_proplist.h
%{_includedir}/openmpi-%{_arch}/netcdf_vutils.h
%{_libdir}/openmpi/lib/libnetcdf.settings
%{_libdir}/openmpi/lib/*.so
%{_libdir}/openmpi/lib/cmake/
%{_libdir}/openmpi/lib/pkgconfig/%{name}.pc
%doc %{_libdir}/openmpi/share/man/man3/*.3*
%endif


%changelog
%autochangelog
