%bcond_without mpich
%if 0%{?fedora} >= 40
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
Release:        15%{?dist}
Summary:        NetCDF-4 C++ library

# Automatically converted from old format: NetCDF - review is highly recommended.
License:        BSD-3-Clause
URL:            http://www.unidata.ucar.edu/software/netcdf/
Source0:        https://github.com/Unidata/netcdf-cxx4/archive/v%{version}/%{name}-%{version}.tar.gz
# Fix tests on big-endian
# https://github.com/Unidata/netcdf-cxx4/issues/45
Patch0:         netcdf-cxx4-bigendian.patch

BuildRequires:  gcc-c++
BuildRequires:  make
BuildRequires:  netcdf-devel
#mpiexec segfaults if ssh is not present
#https://trac.mcs.anl.gov/projects/mpich2/ticket/1576
BuildRequires:  openssh-clients

%if 0%{?rhel} <= 6
%ifarch ppc64
# No mpich on ppc64 in EL6
%global with_mpich 0
%endif
%endif

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
%setup -q
%patch -P0 -p1 -b .bigendian
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
* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 4.3.1-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Wed Aug 07 2024 Miroslav Suchý <msuchy@redhat.com> - 4.3.1-14
- convert license to SPDX

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 4.3.1-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 4.3.1-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 4.3.1-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Oct 29 2023 Orion Poplawski <orion@nwra.com> - 4.3.1-10
- Rebuild for openmpi 5.0.0, drops i686 and C++ API

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 4.3.1-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 4.3.1-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 4.3.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 4.3.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 4.3.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 4.3.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 4.3.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 4.3.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Sep 13 2019 Orion Poplawski <orion@nwra.com> - 4.3.1-1
- Update to 4.3.1

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 4.3.0-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Mon Mar 18 2019 Orion Poplawski <orion@nwra.com> - 4.3.0-10
- Rebuild for netcdf 4.6.3

* Thu Feb 14 2019 Orion Poplawski <orion@nwra.com> - 4.3.0-9
- Rebuild for openmpi 3.1.3

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 4.3.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 4.3.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 4.3.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 4.3.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 4.3.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Tue Feb 14 2017 Orion Poplawski <orion@cora.nwra.com> - 4.3.0-3
- Fix test on big-endian (ppc64)

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 4.3.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Sat Oct 22 2016 Orion Poplawski <orion@cora.nwra.com> - 4.3.0-2
- Rebuild for openmpi 2.0

* Wed May 18 2016 Orion Poplawski <orion@cora.nwra.com> - 4.3.0-1
- Update to 4.3.0

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 4.2.1-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Jan 22 2016 Orion Poplawski <orion@cora.nwra.com> - 4.2.1-11
- Rebuild for netcdf 4.4.0

* Thu Sep 17 2015 Orion Poplawski <orion@cora.nwra.com> - 4.2.1-10
- Rebuild for openmpi 1.10.0

* Sun Aug 16 2015 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 4.2.1-9
- Rebuild for MPI provides

* Sun Jul 26 2015 Sandro Mani <manisandro@gmail.com> - 4.2.1-8
- Rebuild for RPM MPI Requires Provides Change

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.2.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat May 02 2015 Kalev Lember <kalevlember@gmail.com> - 4.2.1-6
- Rebuilt for GCC 5 C++11 ABI change

* Sun Apr 5 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.2.1-5
- Rebuild for mpich soname change

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.2.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.2.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Mon Feb 24 2014 Orion Poplawski <orion@cora.nwra.com> - 4.2.1-2
- Rebuild for mpich-3.1

* Thu Feb 6 2014 Orion Poplawski <orion@cora.nwra.com> - 4.2.1-1
- Update to 4.2.1

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.2-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Mon Jul 22 2013 Deji Akingunola <dakingun@gmail.com> - 4.2-8
- Rename mpich2 sub-packages to mpich and rebuild for mpich-3.0

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.2-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Fri Nov 2 2012 Orion Poplawski <orion@cora.nwra.com> - 4.2-6
- Rebuild for mpich2 1.5
- Use new mpi module location

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Wed Mar 7 2012 Orion Poplawski <orion@cora.nwra.com> - 4.2-4
- Fix line endings

* Wed Mar 7 2012 Orion Poplawski <orion@cora.nwra.com> - 4.2-3
- Build parallel versions
- Ship examples with -devel

* Mon Oct 3 2011 Orion Poplawski <orion@cora.nwra.com> - 4.2-2
- Use %%{?_isa} in Requires
- Make -static sub-package require the -devel package

* Fri Sep 30 2011 Orion Poplawski <orion@cora.nwra.com> - 4.2-1
- Initial package
