# Switch them off if you want
# Best to start with the serial version
%bcond_without mpich
%bcond_without openmpi

# Do not currently use system sundials
# https://bugzilla.redhat.com/show_bug.cgi?id=1820991
# https://github.com/CNS-OIST/STEPS/issues/23
%bcond_with system_sundials

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
http://steps.sourceforge.net/manual/manual_index.html}

Name:           python-steps
Version:        3.6.0
Release:        %autorelease
Summary:        STochastic Engine for Pathway Simulation

# Automatically converted from old format: GPLv2 - review is highly recommended.
License:        GPL-2.0-only
URL:            http://steps.sourceforge.net/
Source0:        https://github.com/CNS-OIST/STEPS/archive/%{version}/STEPS-%{version}.tar.gz

%if %{without system_sundials}
# Version based on path: src/third_party/cvode-VERSION
%global sundials_version 2.6.0
%endif

# Patches generated from: https://github.com/sanjayankur31/STEPS/tree/fedora-3.5.0
# use system gtest
Patch:          0001-Unbundle-gtest.patch
# Remove flags they set
Patch:          0003-Remove-flags-set-by-project.patch
# Remove pysteps flags
Patch:          0004-Remove-pysteps-flags.patch
# We'll install manually, much easier and cleaner
Patch:          0005-Disable-pyinstall.patch
# Use pytest instead of NOSE
# Sent upstream: https://github.com/CNS-OIST/STEPS/pull/24
Patch:          0001-feat-replace-nose-invocations-with-pytest.patch
# libstepsutil is not meant to be a separate shared object
Patch:          0002-Make-libstepsutil-static.patch
# Add more template function to match
Patch:          0007-template-matching-collections_hpp.patch
# Add a missing #include directive
# Fixes failure to compile with GCC 13.
# https://github.com/CNS-OIST/STEPS/pull/29
Patch:          https://github.com/CNS-OIST/STEPS/pull/29.patch
# Fix build with Cython >= 3.1
# Partial backport from upstream:
# https://github.com/CNS-OIST/STEPS/pull/47
Patch:          fix-cython-3.1-build.patch
# https://fedoraproject.org/wiki/Changes/EncourageI686LeafRemoval
ExcludeArch:    %{ix86}

BuildRequires:  make
BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  pkgconfig(gtest_main)
BuildRequires:  petsc-devel
BuildRequires:  python3-devel
BuildRequires:  %{py3_dist Cython}
BuildRequires:  %{py3_dist matplotlib}
BuildRequires:  %{py3_dist numpy}
BuildRequires:  %{py3_dist pytest}
BuildRequires:  %{py3_dist scipy}
BuildRequires:  %{py3_dist setuptools}
BuildRequires:  flexiblas-devel
BuildRequires:  Random123-devel
# The -static BR is required for tracking of header-only libraries
BuildRequires:  pkgconfig(easyloggingpp)
BuildRequires:  easyloggingpp-static

%if %{with system_sundials}
BuildRequires:  sundials2-devel
%endif

%description
%{_description}


%package -n python3-steps
Summary:        STochastic Engine for Pathway Simulation

Provides:       steps = %{version}-%{release}
%if %{without system_sundials}
Provides:       bundled(sundials2) = %{sundials_version}
%endif

%description -n python3-steps %{_description}


%if %{with openmpi}
%package -n python3-steps-openmpi
Summary:        steps built with openmpi

BuildRequires:  openmpi-devel
BuildRequires:  petsc-openmpi-devel
BuildRequires:  rpm-mpi-hooks
%if %{with system_sundials}
BuildRequires:  sundials2-openmpi-devel
%endif

Requires:       openmpi

%if %{without system_sundials}
Provides:       bundled(sundials2) = %{sundials_version}
%endif

%description -n python3-steps-openmpi %{_description}
%endif


%if %{with mpich}
%package -n python3-steps-mpich
Summary:        steps built with mpich

BuildRequires:  mpich-devel
BuildRequires:  petsc-mpich-devel
BuildRequires:  rpm-mpi-hooks
%if %{with system_sundials}
BuildRequires:  sundials2-mpich-devel
%endif

Requires:       mpich

%if %{without system_sundials}
Provides:       bundled(sundials2) = %{sundials_version}
%endif

%description -n python3-steps-mpich
%{_description}
%endif


%prep
%autosetup -n STEPS-%{version} -N
# use the copy that cmake ships instead of the older outdated copy that
# upstream bundles
rm -rf CMake/FindBLAS.cmake
%autopatch -p1

# gtest/gmock 1.17.0 requires C++17 or later
sed -r -i 's/(CXX_DIALECT_OPT_CXX)11/\117/' CMakeLists.txt

%if %{with system_sundials}
# We add %%{_includedir}/sundials2 to the CXXFLAGS in %%build; we must also
# alter any includes that start with sundials/ in order to use the sundials2
# compatibility package. The find-then-modify pattern preserves mtimes on
# sources that did not need to be modified.
find 'src' -type f \( -name '*.c*' -o -name '*.h*' \) -exec gawk \
    '/^#include +[<"]sundials\// { print FILENAME; nextfile }' '{}' '+' |
  xargs -r sed -r -i 's@^(#include +[<"])sundials/@\1@'
%endif

# Remove bundled dependencies that we have unbundled:
rm -rvf \
%if %{with system_sundials}
    src/third_party/cvode* \
%endif
    src/third_party/easyloggingpp \
    src/third_party/superlu* \
    src/third_party/Random123*

# Finding an unbundled easylogging++ via pkg_check_modules() doesn’t work quite
# the way upstream intended. The CMake variable EASYLOGGINGPP_INCLUDE_DIRS is
# not set, but upstream expects to use that to find the source file
# easylogging++.cc, and defining it manually
# (-DEASYLOGGINGPP_INCLUDE_DIRS:PATH=…) without a corresponding set() in a
# CMakeLists.txt somewhere does not seem to work.
#
# We could patch in “set(EASYLOGGINGPP_INCLUDE_DIRS %%{_includedir})” to the
# top-level CMakeLists.txt in the case where USE_BUNDLE_EASYLOGGINGPP is false,
# but it’s easier just to symlink the system files to the expected bundled
# location and let the build system think it is stil bundled.
mkdir -p src/third_party/easyloggingpp/src
ln -s %{_includedir}/easylogging++.h %{_includedir}/easylogging++.cc \
    src/third_party/easyloggingpp/src/

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
echo "*** BUILDING steps-%{version}$MPI_COMPILE_TYPE ***"
echo
%set_build_flags
export CXXFLAGS="${CXXFLAGS-} $(pkgconf --cflags gtest_main) $(pkgconf --libs gtest_main)"
%if %{with system_sundials}
# Correct for sundials2
export CXXFLAGS="${CXXFLAGS-} -I%{_includedir}/sundials2"
%endif
pushd build$MPI_COMPILE_TYPE &&
  cmake \\\
      -DUSE_BUNDLE_EASYLOGGINGPP:BOOL="ON" \\\
      -DUSE_BUNDLE_RANDOM123:BOOL="OFF" \\\
%if %{with system_sundials}
      -DUSE_BUNDLE_SUNDIALS:BOOL="OFF" \\\
      -DSUNDIALS_DIR:PATH=%{_prefix} \\\
      -DSUNDIALS_INCLUDE_DIR:PATH=%{_includedir} \\\
      -DSUNDIALS_LIBRARY_DIR:PATH=%{_libdir} \\\
%else
      -DUSE_BUNDLE_SUNDIALS:BOOL="ON" \\\
      -DSUNDIALS_DIR:PATH=../src/third_party/cvode-2.6.0 \\\
      -DSUNDIALS_INCLUDE_DIR:PATH=../src/third_party/cvode-2.6.0/include \\\
%endif
      -DCMAKE_C_FLAGS_RELEASE:STRING="-DNDEBUG" \\\
      -DCMAKE_CXX_FLAGS_RELEASE:STRING="-DNDEBUG" \\\
      -DCMAKE_Fortran_FLAGS_RELEASE:STRING="-DNDEBUG" \\\
      -DCMAKE_VERBOSE_MAKEFILE:BOOL=ON \\\
      -DCMAKE_INSTALL_DO_STRIP:BOOL=OFF \\\
      -DCMAKE_INSTALL_PREFIX:PATH=$MPI_HOME \\\
      -DINCLUDE_INSTALL_DIR:PATH=%{_includedir} \\\
      -DLIB_INSTALL_DIR:PATH=%{_libdir} \\\
      -DSYSCONF_INSTALL_DIR:PATH=%{_sysconfdir} \\\
      -DSHARE_INSTALL_PREFIX:PATH=%{_datadir} \\\
      -DPYTHON_INSTALL_PREFIX:PATH=$MPI_PYTHON3_SITEARCH \\\
      -DCMAKE_SKIP_RPATH:BOOL=ON \\\
      -DUSE_MPI:BOOL=$MPI_YES \\\
      -DUSE_PETSC:BOOL="OFF" \\\
      -DBLA_VENDOR:STRING=FlexiBLAS \\\
      -DBLA_PREFER_PKGCONFIG:BOOL=True \\\
      -DBUILD_SHARED_LIBS:BOOL="ON" \\\
%if "%{_lib}" == "lib64"
      -DLIB_SUFFIX=64 ../ &&
%else
      -DLIB_SUFFIX="" ../ &&
%endif
  popd || exit -1
}

%global do_make_build %{expand: \
%make_build -C build$MPI_COMPILE_TYPE &&
  pushd pysteps &&
  CFLAGS="%{optflags}" \\\
      LDFLAGS="%{__global_ldflags}" \\\
      %{python3} \\\
      "../build$MPI_COMPILE_TYPE/pysteps/cmake_setup.py" \\\
      build \\\
      --executable="%{python3} %{py3_shbang_opts}" \\\
      --build-base="../build$MPI_COMPILE_TYPE/pysteps/build/" &&
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
echo "*** INSTALLING steps-%{version}$MPI_COMPILE_TYPE ***"
echo
%make_install CPPROG="cp -p" -C build$MPI_COMPILE_TYPE || exit -1
pushd pysteps &&
  CFLAGS="%{optflags}" \\\
      LDFLAGS="%{__global_ldflags}" \\\
      %{python3} \\\
      "../build$MPI_COMPILE_TYPE/pysteps/cmake_setup.py" \\\
      build \\\
      --executable="%{python3} %{py3_shbang_opts}" \\\
      --build-base="../build$MPI_COMPILE_TYPE/pysteps/build/" \\\
      install \\\
      --install-lib=$MPI_PYTHON3_SITEARCH \\\
      -O1 \\\
      --skip-build \\\
      --root $RPM_BUILD_ROOT &&
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


%files -n python3-steps
%license LICENSE.md
%{python3_sitearch}/steps
%{python3_sitearch}/steps-%{version}-py%{python3_version}.egg-info


%if %{with mpich}
%files -n python3-steps-mpich
%license LICENSE.md
%{python3_sitearch}/mpich/steps
%{python3_sitearch}/mpich/steps-%{version}-py%{python3_version}.egg-info
%endif


%if %{with openmpi}
%files -n python3-steps-openmpi
%license LICENSE.md
%{python3_sitearch}/openmpi/steps
%{python3_sitearch}/openmpi/steps-%{version}-py%{python3_version}.egg-info
%endif


%changelog
%autochangelog
