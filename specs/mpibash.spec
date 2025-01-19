Name:           mpibash
Version:        1.4
Release:        4%{?dist}
Summary:        Parallel scripting right from the Bourne-Again Shell
# Automatically converted from old format: GPLv3+ - review is highly recommended.
License:        GPL-3.0-or-later
Url:            https://github.com/lanl/MPI-Bash
Source0:        https://github.com/lanl/MPI-Bash/releases/download/v%{version}/mpibash-%{version}.tar.gz
BuildRequires: make
BuildRequires:  bash-devel >= 4.4
ExcludeArch:    %{ix86}

# Prevent generation of a file dependency on ourselves
# https://bugzilla.redhat.com/show_bug.cgi?id=2229948
%global __requires_exclude ^%{_libdir}/.*/bin/.*

%global _description %{expand:
This package makes it possible to parallelize bash scripts which run a set of
Linux commands independently over a large number of input files. Because mpibash
includes various MPI functions for data transfer and synchronization, it is not
limited to parallel workloads, but can incorporate phased operations where all
workers must finish operation X before any worker is allowed to begin
operation Y.}

%description %_description

%package openmpi
Summary:        Mpibash Open MPI binaries and libraries
BuildRequires:  openmpi-devel
BuildRequires:  libcircle-openmpi-devel

%description openmpi  %_description

mpibash compiled with Open MPI, package incl. binaries and libraries.

%package mpich
Summary:        Mpibash MPICH binaries and libraries
BuildRequires:  mpich-devel
BuildRequires:  libcircle-mpich-devel

%description mpich  %_description

mpibash compiled with MPICH, package incl. binaries and libraries.

%package openmpi-examples
Summary:        Example Scripts for Open MPI %{name}
Requires:       %{name}-openmpi = %{version}

%description openmpi-examples
MPI-Bash makes it possible to parallelize Bash scripts which run a set of
Linux commands independently over a large number of input files.

This package contains example scripts for mpibash compiled with Open MPI.

%package mpich-examples
Summary:        Example Scripts for MPICH %{name}
Requires:       %{name}-mpich = %{version}

%description mpich-examples
MPI-Bash makes it possible to parallelize Bash scripts which run a set of
Linux commands independently over a large number of input files.

This package contains example scripts for mpibash compiled with MPICH.


%prep
%autosetup -p1

%build
mkdir openmpi mpich
%global _configure ../configure


pushd openmpi
%{_openmpi_load}
%configure --with-bashdir=/usr/include/bash --docdir=${MPI_LIB}/share/%{name} --with-plugindir=${MPI_LIB}/%{name}/ --bindir=${MPI_BIN} --mandir=${MPI_MAN} --program-suffix=${MPI_SUFFIX} CC=mpicc
%make_build
%{_openmpi_unload}
popd

pushd mpich
%{_mpich_load}
%configure --with-bashdir=/usr/include/bash --docdir=${MPI_LIB}/share/%{name} --with-plugindir=${MPI_LIB}/%{name}/ --bindir=${MPI_BIN} --mandir=${MPI_MAN} --program-suffix=${MPI_SUFFIX} CC=mpicc
%make_build
%{_mpich_unload}
popd

%install
%make_install -C openmpi
%make_install -C mpich
# Fix shebang
sed -i '1s@/usr/bin/env bash@/bin/bash@' %{buildroot}/%{_libdir}/*mpi*/bin/mpibash*
sed -i '1s@/usr/bin/env mpibash@%{_libdir}/openmpi/bin/mpibash_openmpi@' %{buildroot}/%{_libdir}/openmpi/lib/share/%{name}/examples/* %{buildroot}/%{_libdir}/openmpi/bin/m*
sed -i '1s@/usr/bin/env mpibash@%{_libdir}/mpich/bin/mpibash_mpich@' %{buildroot}/%{_libdir}/mpich/lib/share/%{name}/examples/* %{buildroot}/%{_libdir}/mpich/bin/m*

%files openmpi
%{_libdir}/openmpi/bin/m*
%{_mandir}/openmpi*/man1/m*
%{_libdir}/openmpi/lib/%{name}

%files openmpi-examples
%{_libdir}/openmpi/lib/share/%{name}/examples

%files mpich
%{_libdir}/mpich/bin/m*
%{_mandir}/mpich*/man1/m*
%{_libdir}/mpich/lib/%{name}

%files mpich-examples
%{_libdir}/mpich/lib/share/%{name}/examples

%changelog
* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.4-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Thu Jul 25 2024 Miroslav Suchý <msuchy@redhat.com> - 1.4-3
- convert license to SPDX

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Fri Feb 02 2024 Christoph Junghans <junghans@votca.org> - 1.4-1
- Version bump v1.4 (bug #2262350)
- exclude ix86

* Tue Jan 30 2024 Zbigniew Jedrzejewski-Szmek <zbyszek@in.waw.pl> - 1.3-19
- Suppress internal file depedency

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.3-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.3-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.3-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.3-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.3-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.3-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.3-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.3-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.3-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.3-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jan 17 2020 Jeff Law <law@redhat.com> - 1.3-e
- Redefine _configure and use standard %configure macro

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.3-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Feb 14 2019 Orion Poplawski <orion@nwra.com> - 1.3-6
- Rebuild for openmpi 3.1.3

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.3-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Mon Dec 11 2017 Christoph Junghans <junghans@votca.org> - 1.3-2
- Fix shebang in scripts to contain _${MPI_SUFFIX}

* Thu Dec 07 2017 Christoph Junghans <junghans@votca.org> - 1.3-1
- Version bump to v1.3, enable libcircle support

* Tue Nov 14 2017 Christoph Junghans <junghans@votca.org> - 1.2-1
- Initial commit of v1.2 
