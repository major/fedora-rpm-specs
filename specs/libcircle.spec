Name:    libcircle
Version: 0.3
Release: 19%{?dist}

Source: https://github.com/hpc/libcircle/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
URL: http://hpc.github.io/libcircle/
Summary: A library used to distribute workloads
# Automatically converted from old format: BSD - review is highly recommended.
License: LicenseRef-Callaway-BSD
ExcludeArch:    %{ix86}

BuildRequires:  check-devel
BuildRequires:  doxygen
BuildRequires:  graphviz
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  libtool

%description
A simple interface for processing workloads using an automatically
distributed global queue.

%package openmpi
Summary:        Libcircle Open MPI libraries
BuildRequires:  openmpi-devel

%description openmpi
A simple interface for processing workloads using an automatically
distributed global queue.

libcircle compiled with Open MPI

%package mpich
Summary:        Libcircle MPICH libraries
BuildRequires:  mpich-devel
BuildRequires: make

%description mpich
A simple interface for processing workloads using an automatically
distributed global queue.

libcircle compiled with MPICH

%package doc
Summary:        Documuation for libcircle
BuildArch:      noarch

%description doc
A simple interface for processing workloads using an automatically
distributed global queue.

This package contain documenation for libcircle

%package openmpi-devel
Summary:    Development headers and libraries for Open MPI libcircle
Requires:   %{name}-openmpi%{?_isa} = %{version}-%{release}

%description openmpi-devel
A simple interface for processing workloads using an automatically
distributed global queue.

This package contains development headers and libraries for Open 
MPI ibcircle

%package mpich-devel
Summary:    Development headers and libraries for MPICH libcircle
Requires:   %{name}-mpich%{?_isa} = %{version}-%{release}

%description mpich-devel
A simple interface for processing workloads using an automatically
distributed global queue.

This package contains development headers and libraries for
MPICH ibcircle

%prep
%setup -q
./autogen.sh

%build
mkdir openmpi mpich
%global _configure ../configure


pushd openmpi
%{_openmpi_load}
%configure --enable-doxygen --enable-tests --disable-static --libdir="${MPI_LIB}" --includedir="${MPI_INCLUDE}"
%make_build
%{_openmpi_unload}
popd

pushd mpich
%{_mpich_load}
%configure --enable-tests --disable-static --libdir="${MPI_LIB}" --includedir="${MPI_INCLUDE}"
%make_build
%{_mpich_unload}
popd

%install
%make_install -C openmpi
%make_install -C mpich
rm %{buildroot}%{_libdir}/*mpi*/lib/*.la

cd openmpi
mkdir -p %{buildroot}%{_docdir}/%{name}
cp -r doc/html/* %{buildroot}%{_docdir}/%{name}

%check
%ifarch s390x %arm
export CK_TIMEOUT_MULTIPLIER=10
%endif
%{_openmpi_load}
make -C openmpi check || { cat openmpi/tests/test-suite.log && exit 1; }
%{_openmpi_unload}
%{_mpich_load}
make -C mpich check || { cat mpich/tests/test-suite.log && exit 1; }
%{_mpich_unload}

%files openmpi
%license COPYING AUTHORS
%{_libdir}/openmpi*/lib/%{name}.so.*

%files mpich
%license COPYING AUTHORS
%{_libdir}/mpich*/lib/%{name}.so.*

%files openmpi-devel
%{_libdir}/openmpi*/lib/%{name}.so
%{_libdir}/openmpi*/lib/pkgconfig/%{name}.pc
%{_includedir}/openmpi*/%{name}.h

%files mpich-devel
%{_libdir}/mpich*/lib/%{name}.so
%{_libdir}/mpich*/lib/pkgconfig/%{name}.pc
%{_includedir}/mpich*/%{name}.h

%doc
%{_docdir}/%{name}

%changelog
* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.3-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Mon Sep 02 2024 Miroslav Suchý <msuchy@redhat.com> - 0.3-18
- convert license to SPDX

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.3-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Tue Jan 30 2024 Christoph Junghans <junghans@votca.org> - 0.3-16
- exclude ix86

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.3-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.3-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.3-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.3-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.3-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.3-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Tue Aug 31 2021 Christoph Junghans <junghans@votca.org> - 0.3-9
- Rebuild for autoconf-2.71, extend time limit for arm

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.3-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.3-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Aug 04 2020 Christoph Junghans <junghans@votca.org> - 0.3-6
- Fix build on F33 (bug#1863982)

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.3-5
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Sat Feb 01 2020 Christoph Junghans <junghans@votca.org> - 0.3-3
- Remove s390x workaround

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jan 23 2020 Christoph Junghans <junghans@votca.org> - 0.3-1
- Version bump to 0.3 (bug #1794592)

* Fri Jan 17 2020 Jeff Law <law@redhat.com> - 0.2.1-0.9rc1
- Redefine _configure and use standard #configure macro

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.1-0.8rc1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Feb 14 2019 Orion Poplawski <orion@nwra.com> - 0.2.1-0.7rc1
- Rebuild for openmpi 3.1.3

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.1-0.6rc1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.1-0.5rc1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.1-0.4rc1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Tue Dec 05 2017 Christoph Junghans <junghans@votca.org> - 0.2.1-0.3rc1
- Comments from #1513733

* Wed Nov 15 2017 Christoph Junghans <junghans@votca.org> - 0.2.1-0.2rc1
- Split devel pacakge

* Wed Nov 15 2017 Christoph Junghans <junghans@votca.org> - 0.2.1-0.1rc1
- First release.
