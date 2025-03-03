Name:           ALL
Version:        0.9.3
%global         sover 0
Release:        5%{?dist}
Summary:        A Load Balancing Library (ALL)

# stb_arr.h is public domain
License:        BSD-3-Clause AND LicenseRef-Fedora-Public-Domain
URL:            http://slms.pages.jsc.fz-juelich.de/websites/all-website/ 
Source0:        https://gitlab.jsc.fz-juelich.de/SLMS/loadbalancing/-/archive/v%{version}/loadbalancing-v%{version}.tar.gz#/%{name}-%{version}.tar.gz
Patch0:         https://gitlab.jsc.fz-juelich.de/SLMS/loadbalancing/-/merge_requests/32.patch

# no openmpi on ix86
# https://fedoraproject.org/wiki/Changes/EncourageI686LeafRemoval
# mpi is broken on s390x see: bug#2322073 
ExcludeArch: %{ix86} s390x

BuildRequires:  gcc-c++
BuildRequires:  gcc-fortran
BuildRequires:  cmake >= 3.16
BuildRequires:  openmpi-devel
BuildRequires:  vtk-openmpi-devel
BuildRequires:  mpich-devel
BuildRequires:  vtk-mpich-devel
BuildRequires:  voro++-devel
BuildRequires:  doxygen
BuildRequires:  python3-sphinx_rtd_theme
BuildRequires:  python3-breathe
BuildRequires:  python3-sphinx
BuildRequires:  fdupes
Provides:       Bundled(stb_arr)

%global all_desc \
The library aims to provide an easy way to include dynamic domain-based \
load balancing into particle based simulation codes. 

%description
%{all_desc}

%package openmpi
Summary:    Openmpi libraries for %{name}

%description openmpi
%{all_desc}

This package contains %{name} libraries compiled with openmpi.

%package openmpi-devel
Summary:    Openmpi development headers and libraries for %{name}
Requires:   %{name}-openmpi%{?_isa} = %{version}-%{release}
Requires:   openmpi-devel
Requires:   vtk-openmpi-devel

%description openmpi-devel
%{all_desc}

This package contains openmpi development files of %{name}.

%package mpich
Summary:    Mpich libraries for %{name}

%description mpich
%{all_desc}

This package contains %{name} libraries compiled with mpich.

%package mpich-devel
Summary:    Mpich development headers and libraries for %{name}
Requires:   %{name}-mpich%{?_isa} = %{version}-%{release}
Requires:   mpich-devel
Requires:   vtk-mpich-devel

%description mpich-devel
%{all_desc}

This package contains mpich development files of %{name}.

%package doc
Summary:    Documentation for %{name}
BuildArch:  noarch

%description doc
%{all_desc}

This package contains the documentation for %{name}.

%prep
%autosetup -p1 -n loadbalancing-v%{version}
rm -rf contrib/voro++

%build
%global _vpath_builddir %{_target_platform}-${mpi}

for mpi in mpich openmpi; do
  test -n "${mpi}" && module load mpi/${mpi}-%{_arch}
  %cmake \
    -DCM_ALL_VTK_OUTPUT=ON \
    -DCM_ALL_FORTRAN=ON \
    -DCM_ALL_USE_F08=ON \
    -DCM_ALL_EXTERNAL_VORONOI=ON \
    -DCM_ALL_TESTS=ON \
    -DCM_ALL_TESTS_INTEGRATION=ON \
    -DCM_ALL_AUTO_DOC=ON \
    -DCMAKE_INSTALL_LIBDIR=${MPI_LIB:-%{_libdir}} \
    -DCMAKE_INSTALL_INCLUDEDIR=${MPI_INCLUDE:-%{_includedir}} \
    %{nil}
  mkdir -p %{_vpath_builddir}/docs/doc/doxygen/html
  mkdir -p %{_vpath_builddir}/docs/doc/doxygen/xml
  %cmake_build
  test -n "${mpi}" && module unload mpi/${mpi}-%{_arch}
done

%install
for mpi in mpich openmpi; do
  test -n "${mpi}" && module load mpi/${mpi}-%{_arch}
  %cmake_install
  test -n "${mpi}" && module unload mpi/${mpi}-%{_arch}
done
rm -rv %{buildroot}/%{_docdir}/%{name}/sphinx/{.doctrees,.buildinfo}
%fdupes %{buildroot}/%{_docdir}/%{name}

%check
for mpi in mpich openmpi; do
  test -n "${mpi}" && module load mpi/${mpi}-%{_arch}
  %ctest
  test -n "${mpi}" && module unload mpi/${mpi}-%{_arch}
done

%files openmpi
%doc README.md
%license LICENSE
%{_libdir}/openmpi*/lib/lib%{name}*.so.%{sover}

%files openmpi-devel
%{_includedir}/openmpi*/%{name}*
%{_libdir}/openmpi*/lib/cmake/%{name}
%dir %{_libdir}/openmpi*/lib/make
%{_libdir}/openmpi*/lib/make/Makefile*
%{_libdir}/openmpi*/lib/lib%{name}*.so
%{_libdir}/openmpi*/lib/all*.mod

%files mpich
%doc README.md
%license LICENSE
%{_libdir}/mpich*/lib/lib%{name}*.so.%{sover}

%files mpich-devel
%{_includedir}/mpich*/%{name}*
%{_libdir}/mpich*/lib/cmake/%{name}
%dir %{_libdir}/mpich*/lib/make
%{_libdir}/mpich*/lib/make/Makefile*
%{_libdir}/mpich*/lib/lib%{name}*.so
%{_libdir}/mpich*/lib/all*.mod

%files doc
%dir %{_docdir}/%{name}
%{_docdir}/%{name}/sphinx
%{_docdir}/%{name}/html

%changelog
* Sat Mar 01 2025 Christoph Junghans <junghans@votca.org> - 0.9.3-5
- Add missing vtk-devel dep

* Sun Feb 23 2025 Christoph Junghans <junghans@votca.org> - 0.9.3-4
- Fix duplicated files and stb usage

* Wed Feb 12 2025 Christoph Junghans <junghans@votca.org> - 0.9.3-3
- Fix doc build

* Fri Feb 07 2025 Christoph Junghans <junghans@votca.org> - 0.9.3-2
- Improvements from bug #2333125

* Wed Oct 02 2024 Christoph Junghans <junghans@votca.org> - 0.9.2-1
- Initial commit

