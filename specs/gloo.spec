%global commit0 dc507d1eb822c4396aaca284efff498aba33c7dc
%global shortcommit0 %(c=%{commit0}; echo ${c:0:7})
%global date0 20241203
# MPI build based on spec file dbcsr by Orion
%global mpi_list openmpi mpich
# $mpi will be evaluated in the loops below
%global _vpath_builddir %{_vendor}-%{_target_os}-build-${mpi:-serial}

Summary:        Communications library for AI/ML
Name:           gloo
License:        BSD-3-Clause
Version:        0.5.0^git%{date0}.%{shortcommit0}
Release:        %autorelease

URL:            https://github.com/facebookincubator/%{name}
Source0:        %{url}/archive/%{commit0}/%{name}-%{shortcommit0}.tar.gz
Patch0:         0001-gloo-fedora-cmake-changes.patch
Patch1:         0002-gloo-fedora-cmake-libuv.patch
Patch2:         0001-gloo-gcc-15-cstdint.patch
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
%define gloo_cmake_options -DUSE_IBVERBS=ON -DUSE_LIBUV=OFF -DUSE_REDIS=ON

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

%files docs
%license LICENSE
%doc README.md
%dir %{_datadir}/Gloo
%doc %{_datadir}/Gloo/docs/

%files
%{_libdir}/lib%{name}.so.*

%files devel
%{_includedir}/%{name}/
%{_libdir}/cmake/Gloo/
%{_libdir}/lib%{name}.so

%files mpich
%{_libdir}/mpich/lib/lib%{name}.so.*

%files mpich-devel
%{_libdir}/mpich/lib/lib%{name}.so
%{_libdir}/mpich/lib/cmake/
%{_libdir}/mpich/include/

%files openmpi
%{_libdir}/openmpi/lib/lib%{name}.so.*

%files openmpi-devel
%{_libdir}/openmpi/lib/lib%{name}.so
%{_libdir}/openmpi/lib/cmake/
%{_libdir}/openmpi/include/

%changelog
%autochangelog
