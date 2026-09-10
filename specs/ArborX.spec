# Stolen from eigen spec
# The (empty) main package is arch, to have the package built and tests run
# on all arches, but the actual result package is the noarch -devel subpackge.
# Debuginfo packages are disabled to prevent rpmbuild from generating an empty
# debuginfo package for the empty main package.
%global debug_package %{nil}

Name:           ArborX
Version:        2.1
%global         sover 0
Release:        2%{?dist}
Summary:        Performance-portable geometric search library
# no support for 32-bit archs https://github.com/kokkos/kokkos/issues/2312
# mpi is broken on s390x see: bug#2322073 
ExcludeArch: i686 armv7hl s390x

License:        BSD-3-Clause
URL:            https://github.com/arborx/%{name}
Source0:        %{url}/archive/v%{version}/%{name}-%{version}.tar.gz

BuildRequires:  gcc-c++
BuildRequires:  cmake >= 3.16
BuildRequires:  kokkos-devel
BuildRequires:  openmpi-devel
BuildRequires:  mpich-devel
BuildRequires:  boost-devel
BuildRequires:  google-benchmark-devel

%global arborx_desc \
ArborX is an open-source library designed to provide performance portable \
algorithms for geometric search, similarly to nanoflann and Boost Geometry.

%description
%{arborx_desc}

%package devel
Summary:        Development package for  %{name} packages
BuildArch:      noarch
%description devel
%{arborx_desc}

This package contains the development files of %{name}.

%package openmpi-devel
Summary:    openmpi development headers and libraries for %{name}
Requires:   openmpi-devel

%description openmpi-devel
%{arborx_desc}

This package contains openmpi development files of %{name}.

%package mpich-devel
Summary:    mpich development headers and libraries for %{name}
Requires:   mpich-devel

%description mpich-devel
%{arborx_desc}

This package contains mpich development files of %{name}.

%prep
%autosetup -p1

%build
# save memory
%global _smp_mflags -j1
%global _vpath_builddir %{_target_platform}-${mpi:-serial}

for mpi in '' mpich openmpi; do
  test -n "${mpi}" && module load mpi/${mpi}-%{_arch}
  %cmake \
    -DARBORX_ENABLE_TESTS=ON \
    -DARBORX_ENABLE_EXAMPLES=OFF \
    -DARBORX_ENABLE_BENCHMARKS=OFF \
    $(test -z "${mpi}" && echo -DARBORX_ENABLE_MPI=OFF || echo -DARBORX_ENABLE_MPI=ON) \
    -DCMAKE_INSTALL_DATADIR=${MPI_LIB:-%{_datadir}} \
    -DCMAKE_INSTALL_INCLUDEDIR=${MPI_INCLUDE:-%{_includedir}} \
    %{nil}
  %cmake_build
  test -n "${mpi}" && module unload mpi/${mpi}-%{_arch}
done

%install
for mpi in '' mpich openmpi; do
  test -n "${mpi}" && module load mpi/${mpi}-%{_arch}
  %cmake_install
  test -n "${mpi}" && module unload mpi/${mpi}-%{_arch}
done

%check
# https://github.com/arborx/ArborX/issues/1241 - unstable test
%ifarch aarch64
%global testargs --exclude-regex '\(ArborX_Test_DetailsClusteringHelpers\|ArborX_Test_SpecializedTraversals\)'
%endif
%ifarch ppc64le
%global testargs --exclude-regex '\(ArborX_Test_DetailsClusteringHelpers\|ArborX_Test_InterpMovingLeastSquares\)'
%endif

for mpi in '' mpich openmpi; do
  test -n "${mpi}" && module load mpi/${mpi}-%{_arch}
  %ctest %{?testargs}
  test -n "${mpi}" && module unload mpi/${mpi}-%{_arch}
done

%files devel
%doc README.md
%license LICENSE
%{_includedir}/%{name}
%{_datadir}/cmake/%{name}

%files openmpi-devel
%doc README.md
%license LICENSE
%{_includedir}/openmpi*/%{name}
%{_libdir}/openmpi*/lib/cmake/%{name}

%files mpich-devel
%doc README.md
%license LICENSE
%{_includedir}/mpich*/%{name}
%{_libdir}/mpich*/lib/cmake/%{name}

%changelog
* Wed Sep 09 2026 Christoph Junghans <junghans@votca.org> - 2.1-2
- Initial import
- Fixes: rhbz#2457814

* Thu Jun 04 2026 Christoph Junghans <junghans@votca.org> - 2.1-1
- Version bump to v2.1

* Mon Apr 13 2026 Christoph Junghans <junghans@votca.org> - 2.0.1-1
- Version bump to v2.0.1

* Thu Apr 17 2025 Christoph Junghans <junghans@votca.org> - 2.0-1
- Version bump to v2.0

* Wed Oct 02 2024 Christoph Junghans <junghans@votca.org> - 0.7.0-1
- Initial commit

