%global commit0 01a0c815d1a98eb9b38341cf63546f234fbcc43b
%global shortcommit0 %(c=%{commit0}; echo ${c:0:7})
%global date0 20230824
# MPI build based on spec file dbcsr by Orion
%global mpi_list openmpi mpich
# $mpi will be evaluated in the loops below
%global _vpath_builddir %{_vendor}-%{_target_os}-build-${mpi:-serial}

Summary:        Communications library for AI/ML
Name:           gloo
License:        BSD-3-Clause
Version:        0.5.0^git%{date0}.%{shortcommit0}
Release:        8%{?dist}

URL:            https://github.com/facebookincubator/%{name}
Source0:        %{url}/archive/%{commit0}/%{name}-%{shortcommit0}.tar.gz
Patch0:         0001-gloo-fedora-cmake-changes.patch
Patch1:         0002-gloo-fedora-cmake-libuv.patch
# See CMakeLists, gloo only builds on 64 bit systems
ExcludeArch:    i686

BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  hiredis-devel
BuildRequires:  libibverbs
BuildRequires:  libuv-devel
BuildRequires:  libuv-static
BuildRequires:  mpich-devel
BuildRequires:  openmpi-devel
BuildRequires:  rdma-core-devel
BuildRequires:  redis-devel
# Needed for tests
BuildRequires:  gmock-devel
BuildRequires:  gtest-devel
BuildRequires:  openssl1.1-devel

Requires:       %{name}-docs

%global base_description \
Gloo is a collective communications library. It comes with a number of\
collective algorithms useful for machine learning applications. These\
include a barrier, broadcast, and allreduce.\
\
Transport of data between participating machines is abstracted so that\
IP can be used at all times, or InifiniBand (or RoCE) when available.\
In the latter case, if the InfiniBand transport is used, GPUDirect can\
be used to accelerate cross machine GPU-to-GPU memory transfers.\
\
Where applicable, algorithms have an implementation that works with\
system memory buffers, and one that works with NVIDIA GPU memory buffers.\
In the latter case, it is not necessary to copy memory between host and\
device; this is taken care of by the algorithm implementations.

%description
%{base_description}

%package docs
Summary: Documentation and license for %{name}
Buildarch: noarch

%description docs
Documentation only package used by other packages for
%{name}.

%package devel
Summary:        Headers and libraries for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description devel
Libraries and headers for developing applications that
use %{name}.

%package openmpi
Summary: Gloo - openmpi version
BuildRequires:  openmpi-devel
Requires: %{name}-docs

%description openmpi
%{base_description}

This package can use openmpi as a backend.

%package openmpi-devel
Summary:   Development libraries and headers
Requires: %{name}-openmpi%{?_isa} = %{version}-%{release}

%description openmpi-devel
Libraries and header files for developing applications
that use %{name}-openmpi.

%package mpich
Summary: Gloo - mpich version
BuildRequires:  mpich-devel
Requires: %{name}-docs

%description mpich
%{base_description}

This package can use mpich as a backend.

%package mpich-devel
Summary: Development libraries and headers
BuildRequires:  mpich-devel
Requires: %{name}-mpich%{?_isa} = %{version}-%{release}

%description mpich-devel
Libraries and header files for developing applications
that use %{name}-mpich.

%prep
%autosetup -p1 -n %{name}-%{commit0}

%build
%define gloo_cmake_options -DUSE_IBVERBS=ON -DUSE_LIBUV=ON -DUSE_TCP_OPENSSL_LINK=ON -DUSE_REDIS=ON -DBUILD_EXAMPLES=ON

%cmake %gloo_cmake_options \
       -DUSE_MPI=OFF \
       -DCMAKE_INSTALL_PREFIX=%{_prefix} \
       -DCMAKE_INSTALL_LIBDIR=lib64

%cmake_build

for mpi in %{mpi_list}
do
  module load mpi/$mpi-%{_arch}
  %cmake %gloo_cmake_options \
         -DUSE_MPI=ON \
         -DCMAKE_INSTALL_PREFIX=$MPI_HOME \
	 -DCMAKE_INSTALL_LIBDIR=lib

   %cmake_build
   module purge
done

%install
%cmake_install
mkdir -p %{buildroot}%{_datadir}/Gloo/docs
cp -p -r docs/* %{buildroot}%{_datadir}/Gloo/docs
for mpi in %{mpi_list}
do
  module load mpi/$mpi-%{_arch}
  %cmake_install
  module purge
done

%check
# Test needs to generate an SSL certificate, which fails
# /%{__cmake_builddir}/gloo/test/gloo_test 
# Smoke test, need to figure out how to get looks_like_mpi to run
PREFIX=test1 SIZE=1 RANK=0 ./%{__cmake_builddir}/gloo/examples/example1

%files docs
%license LICENSE
%doc README.md
%dir %{_datadir}/Gloo
%doc %{_datadir}/Gloo/docs/

%files
%{_libdir}/lib%{name}.so.0*

%files devel
%{_includedir}/%{name}/
%{_libdir}/cmake/Gloo/
%{_libdir}/lib%{name}.so

%files mpich
%{_libdir}/mpich/lib/lib%{name}.so.0*

%files mpich-devel
%{_libdir}/mpich/lib/lib%{name}.so
%{_libdir}/mpich/lib/cmake/
%{_libdir}/mpich/include/

%files openmpi
%{_libdir}/openmpi/lib/lib%{name}.so.0*

%files openmpi-devel
%{_libdir}/openmpi/lib/lib%{name}.so
%{_libdir}/openmpi/lib/cmake/
%{_libdir}/openmpi/include/

%changelog
* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.0^git20230824.01a0c81-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Oct 29 2023 Orion Poplawski <orion@nwra.com> - 0.5.0^git20230824.01a0c81-7
- Rebuild for openmpi 5.0.0, drops C++ API

* Wed Oct 11 2023 Tom Rix <trix@redhat.com> - 0.5.0^git20230824.01a0c81-6
- Package the mpi includes

* Tue Oct 10 2023 Tom Rix <trix@redhat.com> - 0.5.0^git20230824.01a0c81-5
- Put the subpackages back.
- Fix MPI configure
- change so version to 0.0.230824

* Sun Oct 8 2023 Tom Rix <trix@redat.com> - 0.5.0^git20230824.01a0c81-4
- Rework to remove subpackages

* Fri Oct 6 2023 Benson Muite <benson_muite@emailplus.org> - 0.5.0^git20230824.01a0c81-3
- Add mpi subpackages
- Add docs subpackage
- Add example to check

* Sun Sep 24 2023 Tom Rix <trix@redhat.com> - 0.5.0^git20230824.01a0c81-2
- Address review comments
- No testing because tests depend on a very old openssl
- No libuv yet because needing a PR to its package to get cmake infra
- Do not build for i686

* Fri Sep 22 2023 Tom Rix <trix@redhat.com> - 0.5.0^git20230824.01a0c81-1
- Initial package
