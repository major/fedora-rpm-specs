%global pretty_name STEPS
%global module_name steps

# Switch them off if you want
# Best to start with the serial version
%bcond_without mpich
%bcond_without openmpi

%if 0%{?fedora} >= 33 || 0%{?rhel} >= 9
%global blaslib flexiblas
%else
%global blaslib openblas
%endif

# Do not currently use system sundials
# https://bugzilla.redhat.com/show_bug.cgi?id=1820991
# https://github.com/CNS-OIST/STEPS/issues/23
%global system_sundials  0

%global _description %{expand:
STEPS is a package for exact stochastic simulation of reaction-diffusion
systems in arbitrarily complex 3D geometries. Our core simulation algorithm is
an implementation of Gillespie's SSA, extended to deal with diffusion of
molecules over the elements of a 3D tetrahedral mesh.

While it was mainly developed for simulating detailed models of neuronal
signaling pathways in dendrites and around synapses, it is a general tool and
can be used for studying any biochemical pathway in which spatial gradients and
morphology are thought to play a role.

STEPS also supports accurate and efficient computational of local membrane
potentials on tetrahedral meshes, with the addition of voltage-gated channels
and currents. Tight integration between the reaction-diffusion calculations and
the tetrahedral mesh potentials allows detailed coupling between molecular
activity and local electrical excitability.

We have implemented STEPS as a set of Python modules, which means STEPS users
can use Python scripts to control all aspects of setting up the model,
generating a mesh, controlling the simulation and generating and analyzing
output. The core computational routines are still implemented as C/C++
extension modules for maximal speed of execution.

STEPS 3.0.0 and above provide early parallel solution for stochastic spatial
reaction-diffusion and electric field simulation.

Documentation can be found here:
http://steps.sourceforge.net/manual/manual_index.html
}

Name:           python-%{module_name}
Version:        3.6.0

Release:        %autorelease
Summary:        STochastic Engine for Pathway Simulation

License:        GPLv2
URL:            http://steps.sourceforge.net/
Source0:        https://github.com/CNS-OIST/STEPS/archive/%{version}/%{pretty_name}-%{version}.tar.gz

# Header only library, needs cc file
# https://raw.githubusercontent.com/amrayn/easyloggingpp/master/src/easylogging%2B%2B.cc
Source1:        easylogging++.cc
# https://raw.githubusercontent.com/amrayn/easyloggingpp/master/src/easylogging%2B%2B.h
Source2:        easylogging++.h

# Patches generated from: https://github.com/sanjayankur31/STEPS/tree/fedora-3.5.0
# use system gtest
Patch0:         0001-Unbundle-gtest.patch
# Remove flags they set
Patch1:         0003-Remove-flags-set-by-project.patch
# Remove pysteps flags
Patch2:         0004-Remove-pysteps-flags.patch
# We'll install manually, much easier and cleaner
Patch3:         0005-Disable-pyinstall.patch
# Use pytest instead of NOSE
# Sent upstream: https://github.com/CNS-OIST/STEPS/pull/24
Patch4:         0001-feat-replace-nose-invocations-with-pytest.patch
# Try to make compatible with Sundials-5.7.0
%if "%{system_sundials}" == "1"
# Tweak cmake file to stop looking for SUNDIALS_DIR
Patch5:         %{name}-sundials.5.7.0.patch
%endif
# libstepsutil is not meant to be a separate shared object
Patch6:         0002-Make-libstepsutil-static.patch
# Add more template function to match
Patch7:         0007-template-matching-collections_hpp.patch

BuildRequires:  make
BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  git-core
BuildRequires:  gtest-devel
BuildRequires:  petsc-devel
BuildRequires:  python3-devel
BuildRequires:  %{py3_dist Cython}
BuildRequires:  %{py3_dist matplotlib}
BuildRequires:  %{py3_dist numpy}
BuildRequires:  %{py3_dist pytest}
BuildRequires:  %{py3_dist scipy}
BuildRequires:  %{py3_dist setuptools}
BuildRequires:  %{blaslib}-devel
BuildRequires:  Random123-devel

%if "%{system_sundials}" == "1"
BuildRequires:  sundials-devel
%endif


%description
%{_description}

%package -n python3-%{module_name}
Summary:        STochastic Engine for Pathway Simulation
Provides:       %{module_name} = %{version}-%{release}

%description -n python3-%{module_name}
%{_description}


%if %{with openmpi}
%package -n python3-%{module_name}-openmpi
Summary:        %{module_name} built with openmpi
BuildRequires:  openmpi-devel
BuildRequires:  petsc-openmpi-devel
BuildRequires:  rpm-mpi-hooks
%if "%{system_sundials}" == "1"
BuildRequires:  sundials-openmpi-devel
%endif
Requires:       openmpi

%description -n python3-%{module_name}-openmpi
%{_description}
%endif

%if %{with mpich}
%package -n python3-%{module_name}-mpich
Summary:        %{module_name} built with mpich
BuildRequires:  mpich-devel
BuildRequires:  petsc-mpich-devel
BuildRequires:  rpm-mpi-hooks
%if "%{system_sundials}" == "1"
BuildRequires:  sundials-mpich-devel
%endif
Requires:       mpich

%description -n python3-%{module_name}-mpich
%{_description}

%endif

%prep
%autosetup -n %{pretty_name}-%{version} -S git -N

# use the copy that cmake ships instead of the older outdated copy that upstream bundles
rm -rf CMake/FindBLAS.cmake

%patch0 -p1 -b .backup
%patch1 -p1 -b .backup
%patch2 -p1 -b .backup
%patch3 -p1 -b .backup
%patch4 -p1 -b .backup
%patch6 -p1 -b .backup
%patch7 -p1 -b .backup

# Easyloggingpp
mkdir -pv src/third_party/easyloggingpp/src/
cp %{SOURCE1} src/third_party/easyloggingpp/src/ -v
cp %{SOURCE2} src/third_party/easyloggingpp/src/ -v


# Correct for sundials2
# sed -i.orig 's|^#include.*<cvode/|#include <sundials2/cvode/|g' src/steps/tetode/tetode.cpp
%if "%{system_sundials}" == "1"
%patch5 -p1 -b .backup
rm -rf src/third_party/cvode-2.6.0
%endif


# Build directories
mkdir build
%if %{with openmpi}
mkdir build-openmpi
%endif

%if %{with mpich}
mkdir build-mpich
%endif

%build
# Best to use && so that if anything in the chain fails, the build also fails
# straight away
%global do_cmake_config %{expand: \
echo
echo "*** BUILDING %{module_name}-%{version}$MPI_COMPILE_TYPE ***"
echo
%set_build_flags
export CXXFLAGS="%{build_cxxflags} -lpthread -lgtest -lgtest_main"
pushd build$MPI_COMPILE_TYPE  &&
    cmake \\\
        -DUSE_BUNDLE_EASYLOGGINGPP:BOOL="ON" \\\
        -DUSE_BUNDLE_RANDOM123:BOOL="OFF" \\\
%if "%{system_sundials}" == "1"
        -DUSE_BUNDLE_SUNDIALS:BOOL="OFF" \\\
%else
        -DUSE_BUNDLE_SUNDIALS:BOOL="ON" \\\
        -DSUNDIALS_DIR:PATH=../src/third_party/cvode-2.6.0 \\\
        -DSUNDIALS_INCLUDE_DIR:PATH=../src/third_party/cvode-2.6.0/include \\\
%endif
        -DCMAKE_C_FLAGS_RELEASE:STRING="-DNDEBUG" \\\
        -DCMAKE_CXX_FLAGS_RELEASE:STRING="-DNDEBUG" \\\
        -DCMAKE_Fortran_FLAGS_RELEASE:STRING="-DNDEBUG" \\\
        -DCMAKE_VERBOSE_MAKEFILE:BOOL=ON \\\
        -DINCLUDE_INSTALL_DIR:PATH=%{_includedir} \\\
        -DLIB_INSTALL_DIR:PATH=%{_libdir} \\\
        -DSYSCONF_INSTALL_DIR:PATH=%{_sysconfdir} \\\
        -DSHARE_INSTALL_PREFIX:PATH=%{_datadir} \\\
        -DPYTHON_INSTALL_PREFIX:PATH=$MPI_PYTHON3_SITEARCH \\\
        -DCMAKE_SKIP_RPATH:BOOL=ON \\\
        -DUSE_MPI:BOOL=$MPI_YES \\\
        -DUSE_PETSC:BOOL=False \\\
        -DBLA_VENDOR:STRING=FlexiBLAS \\\
        -DBLA_PREFER_PKGCONFIG:BOOL=True \\\
        -DCMAKE_INSTALL_PREFIX:PATH=$MPI_HOME \\\
        -DBUILD_SHARED_LIBS:BOOL=ON \\\
%if "%{_lib}" == "lib64"
        -DLIB_SUFFIX=64 ../ &&
%else
        -DLIB_SUFFIX=""  ../ &&
%endif
popd || exit -1;
}

%global do_make_build %{expand: \
make %{?_smp_mflags} -C build$MPI_COMPILE_TYPE &&
pushd pysteps &&
    CFLAGS="%{optflags}" LDFLAGS="%{__global_ldflags}" %{__python3}  ../build$MPI_COMPILE_TYPE/pysteps/cmake_setup.py build --executable="/usr/bin/python3 -s" --build-base=../build$MPI_COMPILE_TYPE/pysteps/build/  &&
popd || exit -1
}

# Build serial version, dummy arguments
export MPI_COMPILE_TYPE=""
export MPI_COMPILER=serial
export MPI_SUFFIX=""
export MPI_HOME=%{_prefix}
export MPI_BIN=%{_bindir}
export MPI_PYTHON3_SITEARCH=%{python3_sitearch}
export MPI_YES="False"
%{do_cmake_config}
%{do_make_build}



# Build mpich version
%if %{with mpich}
%{_mpich_load}
export CC=mpicc
export CXX=mpicxx
export FC=mpif90
export F77=mpif77
export MPI_YES="True"
export MPI_COMPILE_TYPE="-mpich"
%{do_cmake_config}
%{do_make_build}

%{_mpich_unload}
%endif

# Build OpenMPI version
%if %{with openmpi}
%{_openmpi_load}
export CC=mpicc
export CXX=mpicxx
export FC=mpif90
export F77=mpif77
export MPI_YES="True"
export MPI_COMPILE_TYPE="-openmpi"
%{do_cmake_config}
%{do_make_build}

%{_openmpi_unload}
%endif

%install
# Install everything
%global do_install %{expand: \
echo
echo "*** INSTALLING %{module_name}-%{version}$MPI_COMPILE_TYPE ***"
echo
    make install DESTDIR=$RPM_BUILD_ROOT INSTALL="install -p" CPPROG="cp -p" -C build$MPI_COMPILE_TYPE || exit -1
    pushd pysteps &&
        CFLAGS="%{optflags}" LDFLAGS="%{__global_ldflags}" %{__python3}  ../build$MPI_COMPILE_TYPE/pysteps/cmake_setup.py build --executable="/usr/bin/python3 -s" --build-base=../build$MPI_COMPILE_TYPE/pysteps/build/ install --install-lib=$MPI_PYTHON3_SITEARCH -O1 --skip-build --root $RPM_BUILD_ROOT &&
    popd || exit -1
}

# install serial version
export MPI_COMPILE_TYPE=""
export MPI_SUFFIX=""
export MPI_HOME=%{_prefix}
export MPI_BIN=%{_bindir}
export MPI_YES="False"
export MPI_COMPILE_TYPE=""
export MPI_PYTHON3_SITEARCH="%{python3_sitearch}"
%{do_install}

# Install MPICH version
%if %{with mpich}
%{_mpich_load}
export MPI_YES="True"
export MPI_COMPILE_TYPE="-mpich"
%{do_install}
%{_mpich_unload}
%endif

# Install OpenMPI version
%if %{with openmpi}
%{_openmpi_load}
export MPI_YES="True"
export MPI_COMPILE_TYPE="-openmpi"
%{do_install}
%{_openmpi_unload}
%endif


%files -n python3-%{module_name}
%license LICENSE.md
%{python3_sitearch}/%{module_name}
%{python3_sitearch}/%{module_name}-%{version}-py%{python3_version}.egg-info

%if %{with mpich}
%files -n python3-%{module_name}-mpich
%license LICENSE.md
%{python3_sitearch}/mpich/%{module_name}
%{python3_sitearch}/mpich/%{module_name}-%{version}-py%{python3_version}.egg-info
%endif

%if %{with openmpi}
%files -n python3-%{module_name}-openmpi
%license LICENSE.md
%{python3_sitearch}/openmpi/%{module_name}
%{python3_sitearch}/openmpi/%{module_name}-%{version}-py%{python3_version}.egg-info
%endif

%changelog
%autochangelog
