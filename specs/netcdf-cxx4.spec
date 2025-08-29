%bcond_without mpich
%if 0%{?fedora}
%ifarch %{ix86}
%bcond_with openmpi
%else
%bcond_without openmpi
%endif
%else
%bcond_without openmpi
%endif

Name:           netcdf-cxx4
Version:        4.3.1
Release:        %autorelease
Summary:        NetCDF-4 C++ library

# Automatically converted from old format: NetCDF - review is highly recommended.
License:        BSD-3-Clause
URL:            http://www.unidata.ucar.edu/software/netcdf/
Source0:        https://github.com/Unidata/netcdf-cxx4/archive/v%{version}/%{name}-%{version}.tar.gz
# Fix tests on big-endian
# https://github.com/Unidata/netcdf-cxx4/issues/45
Patch0:         netcdf-cxx4-bigendian.patch
# Do not use netcdf logging if not enabled
# https://github.com/Unidata/netcdf-cxx4/pull/162
Patch1:         netcdf-cxx4-logging.patch

BuildRequires:  gcc-c++
BuildRequires:  make
BuildRequires:  netcdf-devel
#mpiexec segfaults if ssh is not present
#https://trac.mcs.anl.gov/projects/mpich2/ticket/1576
BuildRequires:  openssh-clients

%if %{with mpich}
%global mpi_list mpich
%endif
%if %{with openmpi}
%global mpi_list %{?mpi_list} openmpi
%endif

%description
netCDF-4 C++ library.


%package devel
Summary:        Development files for netCDF-4 C++ API
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       pkgconfig
Requires:       netcdf-devel%{?_isa}

%description devel
Development files for netCDF-4 C++ API.


%package static
Summary:        Static library for netCDF-4 C++ API
Requires:       %{name}-devel%{?_isa} = %{version}-%{release}

%description static
Static library for netCDF-4 C++ API.


%if %{with mpich}
%package mpich
Summary: NetCDF mpich libraries
BuildRequires: mpich-devel
BuildRequires: netcdf-mpich-devel
Provides: %{name}-mpich2 = %{version}-%{release}
Obsoletes: %{name}-mpich2 < 4.2-8

%description mpich
NetCDF parallel mpich libraries


%package mpich-devel
Summary: NetCDF mpich development files
Requires: %{name}-mpich%{?_isa} = %{version}-%{release}
Requires: pkgconfig
Requires: netcdf-mpich-devel
Requires: libcurl-devel
Provides: %{name}-mpich2-devel = %{version}-%{release}
Obsoletes: %{name}-mpich2-devel < 4.2-8

%description mpich-devel
NetCDF parallel mpich development files


%package mpich-static
Summary: NetCDF mpich static libraries
Requires: %{name}-mpich-devel%{?_isa} = %{version}-%{release}
Provides: %{name}-mpich2-static = %{version}-%{release}
Obsoletes: %{name}-mpich2-static < 4.2-8

%description mpich-static
NetCDF parallel mpich static libraries
%endif


%if %{with openmpi}
%package openmpi
Summary: NetCDF openmpi libraries
BuildRequires: openmpi-devel
BuildRequires: netcdf-openmpi-devel

%description openmpi
NetCDF parallel openmpi libraries


%package openmpi-devel
Summary: NetCDF openmpi development files
Requires: %{name}-openmpi%{_isa} = %{version}-%{release}
Requires: openmpi-devel
Requires: pkgconfig
Requires: netcdf-openmpi-devel
Requires: libcurl-devel

%description openmpi-devel
NetCDF parallel openmpi development files


%package openmpi-static
Summary: NetCDF openmpi static libraries
Requires: %{name}-openmpi-devel%{?_isa} = %{version}-%{release}

%description openmpi-static
NetCDF parallel openmpi static libraries
%endif


%prep
%autosetup -p1
# Fix line endings
sed -i -e 's/\r//' examples/*.cpp


%build
#Do out of tree builds
%global _configure ../configure

# Serial build
mkdir build
pushd build
ln -s ../configure .
%configure
make %{?_smp_mflags}
popd

# MPI builds
export CC=mpicc
export CXX=mpicxx
for mpi in %{mpi_list}
do
  mkdir $mpi
  pushd $mpi
  module load mpi/$mpi-%{_arch}
  ln -s ../configure .
  %configure \
    --libdir=%{_libdir}/$mpi/lib \
    --bindir=%{_libdir}/$mpi/bin \
    --sbindir=%{_libdir}/$mpi/sbin \
    --includedir=%{_includedir}/$mpi-%{_arch} \
    --datarootdir=%{_libdir}/$mpi/share \
    --mandir=%{_libdir}/$mpi/share/man
  make %{?_smp_mflags}
  module purge
  popd
done


%install
make -C build install DESTDIR=${RPM_BUILD_ROOT}
/bin/rm ${RPM_BUILD_ROOT}%{_libdir}/*.la
# https://github.com/Unidata/netcdf-cxx4/issues/75
/bin/rm ${RPM_BUILD_ROOT}%{_libdir}/libh5bzip2.so
for mpi in %{mpi_list}
do
  module load mpi/$mpi-%{_arch}
  make -C $mpi install DESTDIR=${RPM_BUILD_ROOT}
  rm $RPM_BUILD_ROOT/%{_libdir}/$mpi/lib/*.la
  # https://github.com/Unidata/netcdf-cxx4/issues/75
  rm $RPM_BUILD_ROOT/%{_libdir}/$mpi/lib/libh5bzip2.so
  module purge
done


%check
make -C build check || ( cat build/*/test-suite.log && exit 1 )
for mpi in %{mpi_list}
do
  module load mpi/$mpi-%{_arch}
  make -C $mpi check || ( cat ${mpi}/*/test-suite.log && exit 1 )
  module purge
done



%ldconfig_scriptlets


%files
%doc COPYRIGHT
%{_libdir}/libnetcdf_c++4.so.*

%files devel
%doc examples
%{_bindir}/ncxx4-config
%{_includedir}/*
%{_libdir}/libnetcdf_c++4.so
%{_libdir}/pkgconfig/netcdf-cxx4.pc

%files static
%{_libdir}/libnetcdf_c++4.a


%if %{with mpich}
%files mpich
%doc COPYRIGHT
%{_libdir}/mpich/lib/*.so.*

%files mpich-devel
%{_libdir}/mpich/bin/ncxx4-config
%{_includedir}/mpich-%{_arch}/*
%{_libdir}/mpich/lib/*.so
%{_libdir}/mpich/lib/pkgconfig/%{name}.pc

%files mpich-static
%{_libdir}/mpich/lib/*.a
%endif

%if %{with openmpi}
%files openmpi
%doc COPYRIGHT
%{_libdir}/openmpi/lib/*.so.*

%files openmpi-devel
%{_libdir}/openmpi/bin/ncxx4-config
%{_includedir}/openmpi-%{_arch}/*
%{_libdir}/openmpi/lib/*.so
%{_libdir}/openmpi/lib/pkgconfig/%{name}.pc

%files openmpi-static
%{_libdir}/openmpi/lib/*.a
%endif


%changelog
%autochangelog
