# openmpi dropped 32 bit support, thus also drop it
%ifarch %{ix86}
%bcond_with openmpi
%else
%bcond_without openmpi
%endif

%if 0%{?fedora} >= 33
%global blaslib flexiblas
%else
%global blaslib openblas
%endif

%global _docdir_fmt %{name}

Name:           hpl
URL:            http://www.netlib.org/benchmark/hpl/
Version:        2.2
Release:        21%{?dist}
# Automatically converted from old format: BSD with advertising - review is highly recommended.
License:        LicenseRef-Callaway-BSD-with-advertising
Requires:       %{name}-common = %{version}-%{release}
BuildRequires:  mpich-devel
%if %{with openmpi}
BuildRequires:  openmpi-devel
%endif
BuildRequires:  %{blaslib}-devel
Summary:        A Portable Implementation of the High-Performance Linpack Benchmark
Source0:        http://www.netlib.org/benchmark/hpl/%{name}-%{version}.tar.gz
# setup/Make.Linux_PII_CBLAS_gm tuned for Fedora
Source1:        hpl-README.Fedora
Patch0:         hpl-2.1-fedora.patch

%description
HPL is a software package that solves a (random) dense linear system in
double precision (64 bits) arithmetic on distributed-memory computers.
It can thus be regarded as a portable as well as freely available
implementation of the High Performance Computing Linpack Benchmark.

%package common
Summary: HPL common files
BuildArch: noarch

%description common
HPL common files

%package doc
Summary: HPL documentation
Requires: %{name}-common = %{version}-%{release}
BuildArch: noarch

%description doc
HPL documentation.

%if %{with openmpi}
%package openmpi
Summary: HPL compiled against openmpi
# Require explicitly for dir ownership and to guarantee the pickup of the right runtime
Requires: %{name}-common = %{version}-%{release}

%description openmpi
This package contains HPL compiled with openmpi.
%endif

%package mpich
Summary: HPL compiled against mpich
BuildRequires: mpich-devel
BuildRequires: make
# Require explicitly for dir ownership and to guarantee the pickup of the right runtime
Requires: %{name}-common = %{version}-%{release}

%description mpich
This package contains HPL compiled with mpich.


%prep
%setup -q
%patch -P0 -p1 -b .fedora

cp %{SOURCE1} README.Fedora

# Remove executable mode from sources
find . -type f -perm /111 -exec chmod a-x {} \;

# Patch docs to point to upstream sources
sed -i "s|\"hpl-%{version}.tar.gz\"|\"http://www.netlib.org/benchmark/hpl/hpl-%{version}.tar.gz\"|g" www/*.html

%build
# Have to do off-root builds to be able to build many versions at once

# To avoid replicated code define a build macro
# Cannot build in parallel (with _smp_mflags macro)
%global dobuild() \
cp setup/Make.Linux_PII_CBLAS_gm Make.$MPI_COMPILER \
make TOPdir="%{_builddir}/%{name}-%{version}" arch=$MPI_COMPILER ARCH=$MPI_COMPILER \\\
  LAlib=-l%{blaslib}

%if %{with openmpi}
# Build OpenMPI version
%{_openmpi_load}
%dobuild
%{_openmpi_unload}
%endif

# Build mpich version
%{_mpich_load}
%dobuild
%{_mpich_unload}


%install
%if %{with openmpi}
# Install OpenMPI version
%{_openmpi_load}
install -D -m 0755 bin/${MPI_COMPILER}/xhpl %{buildroot}${MPI_BIN}/xhpl${MPI_SUFFIX}
%{_openmpi_unload}
%endif

# Install MPICH version
%{_mpich_load}
install -D -m 0755 bin/${MPI_COMPILER}/xhpl %{buildroot}${MPI_BIN}/xhpl${MPI_SUFFIX}
%{_mpich_unload}

# Install HPL.dat
install -D -m 0644 testing/ptest/HPL.dat %{buildroot}%{_sysconfdir}/%{name}/HPL.dat

# Install docs
install -d -D -m 0755 %{buildroot}%{_docdir}/%{name}/html
install -p -D -m 0644 www/* %{buildroot}%{_docdir}/%{name}/html

# Install man pages
install -d -D -m 0755 %{buildroot}%{_mandir}/man3
install -p -D -m 0644 man/man3/* %{buildroot}%{_mandir}/man3


%check
%if %{with openmpi}
# Check openmpi implementation
%{_openmpi_load}
pushd bin/${MPI_COMPILER}
OMPI_MCA_rmaps_base_oversubscribe=1 mpirun -n 4 ./xhpl
popd
%{_openmpi_unload}
%endif

# Check mpich implementation
%{_mpich_load}
pushd bin/${MPI_COMPILER}
mpirun -n 4 ./xhpl
popd
%{_mpich_unload}


%files common
%exclude %{_docdir}/%{name}/html
%license COPYRIGHT
%doc BUGS HISTORY README TODO TUNING README.Fedora
%config(noreplace) %{_sysconfdir}/%{name}

%files doc
%doc %{_docdir}/%{name}/html
%{_mandir}/man3/*.3*

%if %{with openmpi}
%files openmpi
%{_libdir}/openmpi/bin/xhpl*
%endif

%files mpich
%{_libdir}/mpich/bin/xhpl*


%changelog
* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 2.2-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Mon Sep 02 2024 Miroslav Suchý <msuchy@redhat.com> - 2.2-20
- convert license to SPDX

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.2-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Tue Jan 30 2024 Jaroslav Škarvada <jskarvad@redhat.com> - 2.2-18
- Dropped openmpi support on 32 bit to fix FTBFS
  Resolves: rhbz#2261235

* Wed Jan 24 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.2-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sat Jan 20 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.2-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.2-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.2-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.2-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.2-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.2-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.2-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Aug 12 2020 Iñaki Úcar <iucar@fedoraproject.org> - 2.2-9
- https://fedoraproject.org/wiki/Changes/FlexiBLAS_as_BLAS/LAPACK_manager

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.2-8
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.2-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Wed Feb 13 2019 Orion Poplawski <orion@nwra.com> - 2.2-4
- Rebuild for openmpi 3.1.3

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Nov 29 2018 Orion Poplawski <orion@nwra.com> - 2.2-2
- Re-enable tests - seems to be okay with openmpi 2.1.6rc1

* Mon Nov 26 2018 Jaroslav Škarvada <jskarvad@redhat.com> - 2.2-1
- New version
  Resolves: rhbz#1653142

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.1-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.1-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Jan 31 2018 Jaroslav Škarvada <jskarvad@redhat.com> - 2.1-21
- Rebuilt for new fortran

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.1-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.1-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Wed Mar 15 2017 Orion Poplawski <orion@cora.nwra.com> - 2.1-18
- Enable openblas on all available architectures

* Mon Feb  6 2017 Jaroslav Škarvada <jskarvad@redhat.com> - 2.1-17
- Rebuilt for new fortran

* Fri Oct 21 2016 Orion Poplawski <orion@cora.nwra.com> - 2.1-16
- Rebuild for openmpi 2.0

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 2.1-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Tue Sep 15 2015 Orion Poplawski <orion@cora.nwra.com> - 2.1-14
- Rebuild for openmpi 1.10.0

* Sat Aug 15 2015 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 2.1-13
- Rebuild for MPI provides

* Sun Jul 26 2015 Sandro Mani <manisandro@gmail.com> - 2.1-12
- Rebuild for RPM MPI Requires Provides Change

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.1-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Tue May 19 2015 Jaroslav Škarvada <jskarvad@redhat.com> - 2.1-10
- Enabled building on ARM and other architectures by using atlas fallback

* Fri May 15 2015 Jaroslav Škarvada <jskarvad@redhat.com> - 2.1-9
- Built only on x86, due to bugs 1222075, 1222079
- Prepared makefile for using static atlas libs

* Fri May 15 2015 Jaroslav Škarvada <jskarvad@redhat.com> - 2.1-8
- Added config(noreplace) to /etc/hpl/HPL.dat

* Thu May 14 2015 Jaroslav Škarvada <jskarvad@redhat.com> - 2.1-7
- Moved HPL.dat to /etc/hpl
- Added build time check testing openmpi and mpich implementations

* Wed May 13 2015 Jaroslav Škarvada <jskarvad@redhat.com> - 2.1-6
- Added '_docdir_fmt name' for hpl-common subpackage to store its
  documentation under /usr/share/doc/hpl
- Other changes according to Fedora review

* Tue Mar  3 2015 Jaroslav Škarvada <jskarvad@redhat.com> - 2.1-5
- Moved HPL.dat to /usr/share

* Wed Jan 14 2015 Dave Love <d.love@liverpool.ac.uk> - 2.1-4
- Build against openblas on x86
- Fix doc description
- Port to current Fedora
- Drop headers and devel packages

* Thu Jul 31 2014 Jaroslav Škarvada <jskarvad@redhat.com> - 2.1-3
- Used mpich instead of mpich2

* Mon Jun 17 2013 Jaroslav Škarvada <jskarvad@redhat.com> - 2.1-2
- Moved files from the main package to the common subpackage

* Tue May 28 2013 Jaroslav Škarvada <jskarvad@redhat.com> - 2.1-1
- New version
- Re-packaged according to MPI guidelines

* Mon Jun 11 2012 Jaroslav Škarvada <jskarvad@redhat.com> - 2.0-2
- Fixed mpich2 module loading on architectures other than x86_64

* Fri Jun 08 2012 Jaroslav Škarvada <jskarvad@redhat.com> - 2.0-1
- Initial release
