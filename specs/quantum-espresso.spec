%global         forgeurl0 https://gitlab.com/QEF/q-e
%global         version0  7.5
%global         tag0      qe-%{version0}

# Cannot de-bundle devicexlib. The project doesn't build properly and qe uses version 0.1
# https://gitlab.com/max-centre/components/devicexlib/-/issues/20
%global         forgeurl1 https://gitlab.com/max-centre/components/devicexlib
%global         commit1   a6b89ef77b1ceda48e967921f1f5488d2df9226d

# Waiting on wannier90 4.0.0 and q-e to adapt to it
%global         forgeurl2 https://github.com/wannier-developers/wannier90
%global         commit2   1d6b187374a2d50b509e5e79e2cab01a79ff7ce1

# Disabling tests for now
# TODO: Investigate why the tests are taking so long to finish on x86_64
%bcond          check     0

Name:           quantum-espresso

# This weird form is to avoid the verbose expansion when we are using a versioned tag instead of a commit snapshot
Release:        %autorelease
%forgemeta -a
Version:        %[ %{defined tag0} ? "%version0" : "%forgeversion" ]

Summary:        A suite for electronic-structure calculations and materials modeling
# Results are incorrect for s390x, upstream does not support this architecture
ExcludeArch:    %{ix86} s390x

# See bundling discussion in https://gitlab.com/QEF/q-e/-/issues/366
Provides:       bundled(FoXlibf)
Provides:       bundled(deviceXlib)

# Automatically converted from old format: GPLv2+ - review is highly recommended.
# TODO: Do a proper license re-review. Many are only SourceLicense, others are bundled
License:  %{shrink:
    GPL-2.0-or-later
}
# BSD: PP/src/bgw2pw.f90
# BSD: PP/src/pw2bgw.f90
# LGPLv2+: Modules/bspline.f90
# MIT: install/install-sh
# zlib/libpng: clib/md5.c
# zlib/libpng: clib/md5.h
URL:            http://www.quantum-espresso.org/
Source0:        %{forgesource0}

# Pseudopotentials used for tests
# Currently these are retrieved by running the ctest with network enabled and archiving pseudo/ directory
# Download issue: https://gitlab.com/QEF/q-e/-/issues/750
# License issue:  https://gitlab.com/QEF/q-e/-/issues/751
Source1:        pseudo.tar.gz
Source2:        %{forgesource1}
Source3:        %{forgesource2}

# Allow building without git
Patch:          https://gitlab.com/QEF/q-e/-/merge_requests/2561.patch

# Build system
BuildRequires:  cmake
BuildRequires:  ninja-build
BuildRequires:  gcc-gfortran
# Project dependencies
BuildRequires:  fftw3-devel
BuildRequires:  flexiblas-devel
# MPI variants
BuildRequires:  openmpi-devel
BuildRequires:  scalapack-openmpi-devel
BuildRequires:  mpich-devel
BuildRequires:  scalapack-mpich-devel
BuildRequires:  libmbd-devel
BuildRequires:  libmbd-openmpi-devel
BuildRequires:  libmbd-mpich-devel
# Testuite dependenceis
BuildRequires:  python3
# To review
#BuildRequires:  python3-numpy

%global _description %{expand:
QUANTUM ESPRESSO is an integrated suite of Open-Source computer codes for
electronic-structure calculations and materials modeling at the nanoscale.
It is based on density-functional theory, plane waves, and pseudopotentials.}

%global _description_devel %{expand:
Development files for %{name} package}

%description
%{_description}

Serial version.


%package openmpi
Summary:        %{name} - openmpi version

%description openmpi
%{_description}

OpenMPI version.


%package mpich
Summary:        %{name} - mpich version

%description mpich
%{_description}

MPICH version.

%package devel
Summary:        Development files for %{name}

Requires:       %{name}%{?_isa} = %{version}-%{release}

%description devel
%{_description_devel}

Serial version.

%package openmpi-devel
Summary:        Development files for %{name} - openmpi version

Requires:       %{name}-openmpi%{?_isa} = %{version}-%{release}

%description openmpi-devel
%{_description_devel}

OpenMPI version.

%package mpich-devel
Summary:        Development files for %{name} - mpich version

Requires:       %{name}-mpich%{?_isa} = %{version}-%{release}

%description mpich-devel
%{_description_devel}

MPICH version.


%prep
%forgeautosetup -p1
tar -xf %{SOURCE2} --strip-components=1 -C external/devxlib
tar -xf %{SOURCE3} --strip-components=1 -C external/wannier90

# Set unique build directories for each serial/mpi variant
# $MPI_SUFFIX will be evaluated in the loops below, set by mpi modules
%global _vpath_builddir %{_vendor}-%{_target_os}-build${MPI_SUFFIX:-_serial}


%conf
# Temporary fix to the "executable .note.GNU-stack section" issue
export LDFLAGS="$LDFLAGS -z noexecstack"

cmake_common_args=(
  "-G Ninja"
  "-DQE_ENABLE_TEST:BOOL=ON"
  "-DQE_MBD_INTERNAL:BOOL=OFF"
  "-DQE_FFTW_VENDOR:STRING=FFTW3"
  "-DQE_ENABLE_OPENMP:BOOL=ON"
  "-DQE_ENABLE_DOC:BOOL=OFF"
  # Disable many external package support for now
  "-DQE_ENABLE_PLUGINS:STRING=''"
  "-DQE_ENABLE_FOX=OFF"
  "-DQE_ENABLE_ENVIRON=OFF"
  # TODO: review other flags
)
for mpi in '' mpich openmpi; do
  if [ -n "$mpi" ]; then
    module load mpi/${mpi}-%{_arch}
    cmake_mpi_args=(
      "-DQE_ENABLE_MPI:BOOL=ON"
      "-DCMAKE_INSTALL_PREFIX:PATH=${MPI_HOME}"
      "-DQE_INSTALL_Fortran_MODULES:PATH=${MPI_FORTRAN_MOD_DIR}"
      "-DCMAKE_INSTALL_LIBDIR:PATH=lib"
    )
  else
    cmake_mpi_args=(
      "-DQE_ENABLE_MPI:BOOL=OFF"
      "-DQE_INSTALL_Fortran_MODULES:PATH=%{_fmoddir}"
    )
  fi

  %cmake \
    ${cmake_common_args[@]} \
    ${cmake_mpi_args[@]}

  [ -n "$mpi" ] && module unload mpi/${mpi}-%{_arch}
done


%build
for mpi in '' mpich openmpi; do
  [ -n "$mpi" ] && module load mpi/${mpi}-%{_arch}
  %cmake_build
  [ -n "$mpi" ] && module unload mpi/${mpi}-%{_arch}
done


%install
for mpi in '' mpich openmpi; do
  [ -n "$mpi" ] && module load mpi/${mpi}-%{_arch}
  %cmake_install
  [ -n "$mpi" ] && module unload mpi/${mpi}-%{_arch}
done
# Deduplicate python files
rm -r %{buildroot}%{_libdir}/openmpi/bin/epw_pp.py
rm -r %{buildroot}%{_libdir}/mpich/bin/epw_pp.py
# Drop share/GUI: That thing is not packaged according to guidelines
rm -r %{buildroot}%{_datadir}/GUI
rm -r %{buildroot}%{_libdir}/openmpi/share/GUI
rm -r %{buildroot}%{_libdir}/mpich/share/GUI


%check
%if %{with check}
tar -xf %{SOURCE1}
# Some tests could require more cpu slots than available on the builder
# Make sure mpi variants run oversubscribed
export PRTE_MCA_rmaps_default_mapping_policy=:oversubscribe

CTEST_ARGS=""
# Skip pw_plugins: Seems the associated tests were not added
CTEST_ARGS="$CTEST_ARGS -LE pw_plugins"

for mpi in '' mpich openmpi; do
  [ -n "$mpi" ] && module load mpi/${mpi}-%{_arch}
  %ctest $CTEST_ARGS
  [ -n "$mpi" ] && module unload mpi/${mpi}-%{_arch}
done
%endif


%files
%license License
%{_bindir}/*.x
%{_bindir}/epw_pp.py
%{_libdir}/*.so.*

%files openmpi
%license License
%{_libdir}/openmpi/bin/*.x
%{_libdir}/openmpi/lib/*.so.*

%files mpich
%license License
%{_libdir}/mpich/bin/*.x
%{_libdir}/mpich/lib/*.so.*

%files devel
%{_includedir}/qe
%{_fmoddir}/qe
%{_libdir}/*.so
%{_libdir}/cmake
%{_libdir}/pkgconfig

%files openmpi-devel
%{_libdir}/openmpi/lib/*.so
%{_libdir}/openmpi/lib/cmake
%{_libdir}/openmpi/lib/pkgconfig
%{_fmoddir}/openmpi/qe
%{_libdir}/openmpi/include/qe

%files mpich-devel
%{_libdir}/mpich/lib/*.so
%{_libdir}/mpich/lib/cmake
%{_libdir}/mpich/lib/pkgconfig
%{_fmoddir}/mpich/qe
%{_libdir}/mpich/include/qe

%changelog
%autochangelog
