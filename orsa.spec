%if 0%{?fedora} >= 40
%ifarch %{ix86}
%bcond_with openmpi
%else
%bcond_without openmpi
%endif
%else
%bcond_without openmpi
%endif

Name:           orsa
Version:        0.7.0
Release:        %autorelease
Summary:        Orbit Reconstruction, Simulation and Analysis

License:        GPL-2.0-or-later
URL:            http://orsa.sourceforge.net
Source0:        http://downloads.sourceforge.net/%{name}/%{name}-%{version}.tar.gz
Source1:        ORSA_MPI
# Patch to build with GCC 4.3
# Reported into upstream bugtracker as
# http://sourceforge.net/tracker/index.php?func=detail&aid=2099077&group_id=44502&atid=439768
Patch0:         orsa-gcc43.patch
# Patching configure in order to:
# - make it find the fftw2 library properly (-lm was missing but needed)
# - make it find the cln and ginac libraries properly as they do not use 
# {cln,ginac}-config anymore but rely on pkg-config instead in F9 and higher
# Reported into upstream bugtracker as
# http://sourceforge.net/tracker/index.php?func=detail&aid=2099054&group_id=44502&atid=439768
Patch1:         orsa-configure.patch
# Patch that prevents orsa from printing many errors on startup because of missing
# configuration files.
# Reported into upstream bugtracker as
# http://sourceforge.net/tracker/?func=detail&aid=2741094&group_id=44502&atid=439768
Patch2:         orsa-file.patch
# https://bugzilla.redhat.com/show_bug.cgi?id=1282004
Patch3:         orsa-gsl-2.patch

Patch4:         orsa-linking.patch
Patch5:         orsa-configure-c99.patch

# Files copied in from rpm-build-4.15.1 since they are gone in later versions.
Source2:        config.guess
Source3:        config.sub

BuildRequires:  make
BuildRequires:  gcc-c++
BuildRequires:  readline-devel
BuildRequires:  qt3-devel
BuildRequires:  mesa-libGL-devel
BuildRequires:  fftw2-devel
BuildRequires:  gsl-devel
BuildRequires:  cln-devel
BuildRequires:  ginac-devel
BuildRequires:  autoconf
BuildRequires:  libtool

Requires:       %{name}-common = %{version}-%{release}

%description
ORSA is an interactive tool for scientific grade Celestial Mechanics
computations. Asteroids, comets, artificial satellites, Solar and extra-Solar
planetary systems can be accurately reproduced, simulated, and analyzed. 

%package devel
Summary:        Development files for %{name}

Requires:       fftw2-devel
Requires:       gsl-devel
Requires:       zlib-devel
Requires:       %{name} = %{version}-%{release}
Requires:       %{name}-headers = %{version}-%{release}

%description devel
This package contains development files for %{name}.

%if %{with openmpi}
%package openmpi
Summary:        A build of %{name} with support for OpenMPI

BuildRequires: openmpi-devel
Requires:       %{name}-common = %{version}-%{release}

%description openmpi
This package contains a build of %{name} with support for OpenMPI.

%package openmpi-devel
Summary:        Development files for %{name} build with support for OpenMPI

Requires: %{name}-openmpi = %{version}-%{release}
Requires: %{name}-headers = %{version}-%{release}

%description openmpi-devel
This package contains development files for a build of %{name}
 with support for OpenMPI.
%endif

%package mpich
Summary:        A build of %{name} with support for MPICH MPI

BuildRequires:  mpich-devel-static
Requires:       %{name}-common = %{version}-%{release}
Provides:       %{name}-mpich2 = %{version}-%{release}
Obsoletes:      %{name}-mpich2 < 0.7.0-24

%description mpich
This package contains a build of %{name} with support for MPICH MPI.

%package mpich-devel
Summary:        Development files for %{name} build with support for MPICH MPI

Requires:       %{name}-mpich = %{version}-%{release}
Requires:       %{name}-headers = %{version}-%{release}
Provides:       %{name}-mpich2-devel = %{version}-%{release}
Obsoletes:      %{name}-mpich2-devel < 0.7.0-24

%description mpich-devel
This package contains development files for a build of %{name}
with support for MPICH MPI.

%package headers
Summary:        Headers for development with %{name}

%description headers
This package contains C++ header files for development with %{name}.

%package common
Summary:        Common files for %{name}

%description common
This package contains files shared across the MPI/non-MPI builds of %{name}.

%prep
%autosetup -p1

# Install user hints for MPI support
install -p -m644 %{SOURCE1} .

# Update config.guess/sub to fix builds on new architectures (aarch64/ppc64le)
cp %{SOURCE2} %{SOURCE3} .

%build
# We need to rebuild generated files after updating Makefile.am. Let's
# use a big hammer.
autoreconf -iv

# honor $RPM_OPT_FLAGS
sed -i 's|-g -Wall -W -pipe -ftemplate-depth-64 -O3 -fno-exceptions -funroll-loops -fstrict-aliasing -fno-gcse|$CXXFLAGS|' configure

%global _configure ../configure

# To avoid replicated code define a build macro
%global dobuild() \
mkdir $MPI_COMPILER && \
pushd $MPI_COMPILER && \
%configure $WITH_MPI --prefix=$MPI_HOME --bindir=$MPI_BIN --libdir=$MPI_LIB --program-suffix=$MPI_SUFFIX \\\
           --disable-dependency-tracking --disable-static \\\
           "CLN_CONFIG=`which pkg-config` cln" \\\
           "GINACLIB_CONFIG=`which pkg-config` ginac" \\\
           CXXFLAGS="$CXXFLAGS -DHAVE_INLINE -DINLINE_FUN=inline" && \
sed -i 's|^hardcode_libdir_flag_spec=.*|hardcode_libdir_flag_spec=""|g' libtool && \
sed -i 's|^runpath_var=LD_RUN_PATH|runpath_var=DIE_RPATH_DIE|g' libtool && \
%make_build && \
popd

%global openmpi_bin %{_libdir}/openmpi/bin
%global openmpi_lib %{_libdir}/openmpi/lib
%global mpich_bin %{_libdir}/mpich/bin
%global mpich_lib %{_libdir}/mpich/lib

################################
echo -e "\n##############################\nNow making the non-MPI version\n##############################\n"
################################

# Build serial version, dummy arguments
MPI_COMPILER=serial MPI_SUFFIX= WITH_MPI=--without-mpi MPI_HOME=%{_prefix} MPI_BIN=%{_bindir} MPI_LIB=%{_libdir} %dobuild

# Build parallel versions: set compiler variables to MPI wrappers
export CC=mpicc
export CXX=mpicxx
export FC=mpif90
export F77=mpif77

%if %{with openmpi}
################################
echo -e "\n##############################\nNow making the OpenMPI version\n##############################\n"
################################

%{_openmpi_load}
WITH_MPI=--with-mpi %dobuild
%{_openmpi_unload}
%endif

################################
echo -e "\n##############################\nNow making the MPICH version\n##############################\n"
################################
%{_mpich_load}
WITH_MPI=--with-mpi %dobuild
%{_mpich_unload}

%install
# Install serial version
%make_install -C serial CPPROG="cp -p"
rm %{buildroot}%{_libdir}/{liborsa.la,libxorsa.la}

%if %{with openmpi}
# Install OpenMPI version
%{_openmpi_load}
%make_install -C $MPI_COMPILER CPPROG="cp -p"
rm %{buildroot}$MPI_LIB/{liborsa.la,libxorsa.la}
%{_openmpi_unload}
%endif

# Install MPICH version
%{_mpich_load}
%make_install -C $MPI_COMPILER CPPROG="cp -p"
rm %{buildroot}$MPI_LIB/{liborsa.la,libxorsa.la}
%{_mpich_unload}

%files
%{_bindir}/xorsa
%{_libdir}/liborsa.so.*
%{_libdir}/libxorsa.so.*

%files devel
%{_libdir}/*.so

%files headers
%{_includedir}/*

%if %{with openmpi}
%files openmpi
%{openmpi_lib}/liborsa.so.*
%{openmpi_lib}/libxorsa.so.*
%{openmpi_bin}/*

%files openmpi-devel
%{openmpi_lib}/*.so
%endif

%files mpich
%{mpich_lib}/liborsa.so.*
%{mpich_lib}/libxorsa.so.*
%{mpich_bin}/*

%files mpich-devel
%{mpich_lib}/*.so

%files common
%license COPYING
%doc DEVELOPERS ORSA_MPI

%changelog
%autochangelog
