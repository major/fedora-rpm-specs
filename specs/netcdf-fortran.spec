Name:           netcdf-fortran
Version:        4.6.1
Release:        3%{?dist}
Summary:        Fortran libraries for NetCDF-4

License:        BSD-3-Clause AND Apache-2.0
URL:            http://www.unidata.ucar.edu/software/netcdf/
Source0:        https://github.com/Unidata/%{name}/archive/v%{version}/%{name}-%{version}.tar.gz
# Use pkgconfig in nf-config to avoid multi-lib issues and remove FFLAGS
Patch1:         netcdf-fortran-pkgconfig.patch
%if 0%{?fedora} >= 38
ExcludeArch:    %{ix86}
%endif

BuildRequires:  gcc-gfortran
BuildRequires:  make
BuildRequires:  netcdf-devel >= 4.6.0
# For Patch1
BuildRequires:  libtool

%global with_mpich 1
%global with_openmpi 1

%if %{with_mpich}
%global mpi_list mpich
%endif
%if %{with_openmpi}
%global mpi_list %{?mpi_list} openmpi
%endif

%description
Fortran libraries for NetCDF-4.


%package devel
Summary:        Development files for Fortran NetCDF API
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       gcc-gfortran%{?_isa}
Requires:       pkgconfig
Requires:       netcdf-devel%{?_isa}

%description devel
This package contains the NetCDF Fortran header files, shared devel libraries,
and man pages.


%package static
Summary:        Static library for Fortran NetCDF API
Requires:       %{name}-devel%{?_isa} = %{version}-%{release}

%description static
This package contains the NetCDF Fortran static library.


%if %{with_mpich}
%package mpich
Summary: NetCDF Fortran mpich libraries
BuildRequires: mpich-devel
BuildRequires: netcdf-mpich-devel

%description mpich
NetCDF Fortran parallel mpich libraries


%package mpich-devel
Summary: NetCDF Fortran mpich development files
Requires: %{name}-mpich%{?_isa} = %{version}-%{release}
Requires: gcc-gfortran%{_isa}
Requires: pkgconfig
Requires: netcdf-mpich-devel
Requires: libcurl-devel

%description mpich-devel
NetCDF Fortran parallel mpich development files


%package mpich-static
Summary: NetCDF Fortran mpich static libraries
Requires: %{name}-mpich-devel%{?_isa} = %{version}-%{release}

%description mpich-static
NetCDF Fortran parallel mpich static libraries
%endif


%if %{with_openmpi}
%package openmpi
Summary: NetCDF Fortran openmpi libraries
BuildRequires: openmpi-devel
BuildRequires: netcdf-openmpi-devel

%description openmpi
NetCDF Fortran parallel openmpi libraries


%package openmpi-devel
Summary: NetCDF Fortran openmpi development files
Requires: %{name}-openmpi%{_isa} = %{version}-%{release}
Requires: openmpi-devel
Requires: gcc-gfortran%{_isa}
Requires: pkgconfig
Requires: netcdf-openmpi-devel
Requires: libcurl-devel

%description openmpi-devel
NetCDF Fortran parallel openmpi development files


%package openmpi-static
Summary: NetCDF Fortran openmpi static libraries
Requires: %{name}-openmpi-devel%{?_isa} = %{version}-%{release}

%description openmpi-static
NetCDF Fortran parallel openmpi static libraries
%endif


%prep
%autosetup -p1
autoreconf
sed -i -e '1i#!/bin/sh' examples/F90/run_f90_par_examples.sh


%build
#Do out of tree builds
%global _configure ../configure

# Serial build
mkdir build
pushd build
ln -s ../configure .
export F77="gfortran"
export FC="gfortran"
export FCFLAGS="$RPM_OPT_FLAGS"
export FFLAGS="$RPM_OPT_FLAGS"
%configure --enable-extra-example-tests --with-fmoddir=%{_fmoddir}
%make_build
popd

# MPI builds
for mpi in %{mpi_list}
do
  mkdir $mpi
  pushd $mpi
  module load mpi/$mpi-%{_arch}
  ln -s ../configure .
  %configure \
    CC=mpicc CPPFLAGS=-DpgiFortran F77=mpif90 FC=mpif90 \
    FCFLAGS="$FCFLAGS -I$MPI_FORTRAN_MOD_DIR" \
    --libdir=%{_libdir}/$mpi/lib \
    --bindir=%{_libdir}/$mpi/bin \
    --sbindir=%{_libdir}/$mpi/sbin \
    --includedir=%{_includedir}/$mpi-%{_arch} \
    --datarootdir=%{_libdir}/$mpi/share \
    --mandir=%{_libdir}/$mpi/share/man \
    --with-fmoddir=%{_fmoddir}/${mpi} \
    --enable-parallel \
    --enable-parallel-tests
  %make_build
  #make #{?_smp_mflags}
  module purge
  popd
done


%install
%make_install -C build
/bin/rm -f ${RPM_BUILD_ROOT}%{_libdir}/*.la
for mpi in %{mpi_list}
do
  module load mpi/$mpi-%{_arch}
  %make_install -C $mpi
  rm $RPM_BUILD_ROOT/%{_libdir}/$mpi/lib/*.la
  gzip $RPM_BUILD_ROOT/%{_libdir}/$mpi/share/man/man3/*.3
  module purge
done
/bin/rm -f ${RPM_BUILD_ROOT}%{_infodir}/dir


%check
make -C build check VERBOSE=1
# mpich tests hang on s390x
%ifnarch s390x
# Allow oversubscription with openmpi
export OMPI_MCA_rmaps_base_oversubscribe=1
# openmpi 5+
export PRTE_MCA_rmaps_default_mapping_policy=:oversubscribe
for mpi in %{mpi_list}
do
  module load mpi/$mpi-%{_arch}
  make -C $mpi check VERBOSE=1
  module purge
done
%endif


%ldconfig_scriptlets


%files
%license COPYRIGHT F03Interfaces_LICENSE
%doc README.md RELEASE_NOTES.md
%{_libdir}/*.so.*

%files devel
%doc examples
%{_bindir}/nf-config
%{_includedir}/netcdf.inc
%{_fmoddir}/*.mod
%{_libdir}/libnetcdff.settings
%{_libdir}/*.so
%{_libdir}/pkgconfig/netcdf-fortran.pc
%{_mandir}/man3/*

%files static
%{_libdir}/*.a


%if %{with_mpich}
%files mpich
%license COPYRIGHT F03Interfaces_LICENSE
%doc README.md RELEASE_NOTES.md
%{_libdir}/mpich/lib/*.so.*

%files mpich-devel
%{_libdir}/mpich/bin/nf-config
%{_includedir}/mpich-%{_arch}/*
%{_fmoddir}/mpich/*.mod
%{_libdir}/mpich/lib/libnetcdff.settings
%{_libdir}/mpich/lib/*.so
%{_libdir}/mpich/lib/pkgconfig/%{name}.pc
%{_libdir}/mpich/share/man/man3/*

%files mpich-static
%{_libdir}/mpich/lib/*.a
%endif

%if %{with_openmpi}
%files openmpi
%license COPYRIGHT F03Interfaces_LICENSE
%doc README.md RELEASE_NOTES.md
%{_libdir}/openmpi/lib/*.so.*

%files openmpi-devel
%{_libdir}/openmpi/bin/nf-config
%{_includedir}/openmpi-%{_arch}/*
%{_fmoddir}/openmpi/*.mod
%{_libdir}/openmpi/lib/libnetcdff.settings
%{_libdir}/openmpi/lib/*.so
%{_libdir}/openmpi/lib/pkgconfig/%{name}.pc
%{_libdir}/openmpi/share/man/man3/*

%files openmpi-static
%{_libdir}/openmpi/lib/*.a
%endif


%changelog
* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 4.6.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 4.6.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Thu Jan 25 2024 Orion Poplawski <orion@nwra.com> - 4.6.1-1
- Update to 4.6.1
- SPDX License

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 4.6.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 4.6.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 4.6.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Mar 30 2023 Orion Poplawski <orion@nwra.com> - 4.6.0-1
- Update to 4.6.0
- Drop i686 builds
- Cleanup spec and drop old workarounds

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 4.5.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 4.5.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Sun Jul 03 2022 Orion Poplawski <orion@nwra.com> - 4.5.4-1
- Update to 4.5.4

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 4.5.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jan 14 2022 Orion Poplawski <orion@nwra.com> - 4.5.3-1
- Update to 4.5.3

* Tue Aug 10 2021 Orion Poplawski <orion@nwra.com> - 4.5.2-8
- Rebuild for netcdf 4.8.0

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 4.5.2-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 4.5.2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Aug 10 2020 Jeff Law <law@redhat.com> - 4.5.2-5
- Disable LTO on i686 for now

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 4.5.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Feb 24 2020 Orion Poplawski <orion@nwra.com> - 4.5.2-3
- Make netcdf-fortran report module directory (bz#1738541)
- Fix FTBFS (bz#1799681)

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 4.5.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Tue Oct 1 2019 Orion Poplawski <orion@nwra.com> - 4.5.2-1
- Update to 4.5.2

* Fri Sep 13 2019 Orion Poplawski <orion@nwra.com> - 4.5.1-1
- Update to 4.5.1

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 4.4.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Mar 17 2019 Orion Poplawski <orion@nwra.com> - 4.4.5-1
- Update to 4.4.5

* Thu Feb 14 2019 Orion Poplawski <orion@nwra.com> - 4.4.4-12
- Rebuild for openmpi 3.1.3

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 4.4.4-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 4.4.4-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 4.4.4-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 4.4.4-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 4.4.4-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 4.4.4-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Feb 01 2017 Orion Poplawski <orion@cora.nwra.com> - 4.4.4-5
- Rebuild for gcc 7

* Sat Dec 31 2016 Orion Poplawski <orion@cora.nwra.com> - 4.4.4-4
- Install MPI Fortran module into proper location (bug #1409230)
- Use %%license

* Sun Dec 4 2016 Orion Poplawski <orion@cora.nwra.com> - 4.4.4-3
- Add patch to compile with -Werror=implicit-function-declaration

* Sat Oct 22 2016 Orion Poplawski <orion@cora.nwra.com> - 4.4.4-2
- Rebuild for openmpi 2.0

* Wed May 18 2016 Orion Poplawski <orion@cora.nwra.com> - 4.4.4-1
- Update to 4.4.4

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 4.4.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Jan 22 2016 Orion Poplawski <orion@cora.nwra.com> - 4.4.3-1
- Update to 4.4.3

* Wed Nov 25 2015 Orion Poplawski <orion@cora.nwra.com> - 4.4.2-3
- Use MPI_FORTRAN_MOD_DIR

* Thu Sep 17 2015 Orion Poplawski <orion@cora.nwra.com> - 4.4.2-2
- Rebuild for openmpi 1.10.0

* Wed Aug 12 2015 Orion Poplawski <orion@cora.nwra.com> - 4.4.2-1
- Update to 4.4.2
- Drop postdeps patch

* Sun Jul 26 2015 Sandro Mani <manisandro@gmail.com> - 4.4.1-6
- Rebuild for RPM MPI Requires Provides Change

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.4.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Wed May 6 2015 Orion Poplawski <orion@cora.nwra.com> - 4.4.1-4
- Rebuild without romio hack (fixed with openmpi 1.8.5)

* Mon May  4 2015 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 4.4.1-3
- Rebuild for changed mpich

* Mon Feb 16 2015 Orion Poplawski <orion@cora.nwra.com> - 4.4.1-2
- Rebuild for gcc 5 fortran module

* Tue Sep 16 2014 Orion Poplawski <orion@cora.nwra.com> - 4.4.1-1
- Update to 4.4.1

* Wed Aug 27 2014 Orion Poplawski <orion@cora.nwra.com> - 4.2-16
- Rebuild for openmpi Fortran ABI change

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.2-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Wed Jun 25 2014 Peter Robinson <pbrobinson@fedoraproject.org> 4.2-14
- Update config.guess/sub for new arch support (aarch64/ppc64le)

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.2-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Mon Feb 24 2014 Orion Poplawski <orion@cora.nwra.com> - 4.2-12
- Rebuild for mpich-3.1

* Wed Jul 31 2013 Orion Poplawski <orion@cora.nwra.com> - 4.2-11
- Build for arm

* Mon Jul 22 2013 Deji Akingunola <dakingun@gmail.com> - 4.2-10
- Rename mpich2 sub-packages to mpich and rebuild for mpich-3.0

* Wed Jul 17 2013 Orion Poplawski <orion@cora.nwra.com> - 4.2-9
- Rebuild for openmpi 1.7

* Thu Apr 4 2013 Orion Poplawski <orion@cora.nwra.com> - 4.2-8
- Fix patches to use pkg-config (bug #948640)
 
* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.2-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Mon Nov 5 2012 Orion Poplawski <orion@cora.nwra.com> - 4.2-6
- Rebuild for fixed openmpi f90 soname

* Thu Nov 1 2012 Orion Poplawski <orion@cora.nwra.com> - 4.2-5
- Rebuild for openmpi and mpich2 soname bumps
- Use new mpi module location

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Wed Mar 7 2012 Orion Poplawski <orion@cora.nwra.com> - 4.2-3
- Don't ship info/dir file
- Add needed shbangs
- Compress mpi package man pages

* Wed Mar 7 2012 Orion Poplawski <orion@cora.nwra.com> - 4.2-2
- Build parallel versions
- Ship examples with -devel

* Fri Oct 7 2011 Orion Poplawski <orion@cora.nwra.com> - 4.2-1
- Initial package
