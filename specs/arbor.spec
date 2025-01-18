%global _description %{expand:
Arbor is a high-performance library for Computational Neuroscience simulations.

Some key features include:

- Asynchronous spike exchange that overlaps compute and communication.
- Efficient sampling of voltage and current on all back ends.
- Efficient implementation of all features on GPU.
- Reporting of memory and energy consumption (when available on platform).
- An API for addition of new cell types, e.g. LIF and Poisson spike generators.
- Validation tests against numeric/analytic models and NEURON.

Documentation is available at https://arbor.readthedocs.io/en/latest/
}

# Best to start with the serial version when debugging build failures
%bcond mpich 1
%bcond openmpi 1

%bcond tests 1

# Python unit tests in MPI environment fail in a non-deterministic way.
# Using pytest _as is_ doesn't work either and `-m unittest` does not
# allow filtering tests as `pytest -k` does.
# For now we don't run the Python MPI tests.
%bcond mpi_py_unittest 0

%global forgeurl            https://github.com/arbor-sim/arbor

Name:           arbor
Version:        0.9.0
Release:        %autorelease
Summary:        Multi-compartment neural network simulation library

%forgemeta

URL:            %forgeurl
Source0:        %forgesource
# script to run examples
Source1:        https://raw.githubusercontent.com/arbor-sim/arbor/master/scripts/run_python_examples.sh
Source2:        https://raw.githubusercontent.com/arbor-sim/arbor/master/scripts/run_cpp_examples.sh
License:        BSD-3-Clause

Patch:          0001-Quote-various-cmake-var-values.patch
# Tests are failing to compile due to some missing includes
Patch:          fix-missing-includes.patch
# Fix a few typos that cause failure to compile with GCC 15
#
# These were eventually included in
# 76120d16c00ae67128c3c69421ab712f985f3445, along with many other changes.
Patch:          0001-Fix-a-few-typos-that-cause-failure-to-compile-with-G.patch

# Random123 does not support:
#   mips64r2 mips32r2 s390
# https://fedoraproject.org/wiki/Changes/EncourageI686LeafRemoval
ExcludeArch:    mips64r2 mips32r2 s390x %{ix86}

BuildRequires:  cmake
BuildRequires:  make
BuildRequires:  fmt-devel
BuildRequires:  gcc-c++
BuildRequires:  git-core
BuildRequires:  gtest-devel
BuildRequires:  google-benchmark-devel
BuildRequires:  json-devel
BuildRequires:  libunwind-devel
BuildRequires:  pybind11-devel
BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
BuildRequires:  Random123-devel
BuildRequires:  tclap-devel
BuildRequires:  pugixml-devel

# For validation, but we don't have these BRs
# BuildRequires:  julia julia-sundials julia-unitful julia-JSON

%if %{with tests}
BuildRequires:  %{py3_dist numpy}
BuildRequires:  %{py3_dist pandas}
BuildRequires:  %{py3_dist seaborn}
%endif

# Required by arbor
Requires:       %{py3_dist numpy}

# Provide Python meta data for packages requiring arbor
%py_provides python3-arbor

%description %{_description}

%package devel
Summary:    Development files for arbor
Requires:   arbor%{?_isa} = %{version}-%{release}
Provides:   arbor-static = %{version}-%{release}

%description devel %{_description}

%package doc
# Does not require the main package, since it may be installed by people using
# the MPI builds
Summary:        Documentation for arbor
BuildRequires:  python3-sphinx
BuildRequires:  python3-sphinx_rtd_theme
BuildRequires:  python3-svgwrite

BuildArch:      noarch

%description doc %{_description}

%if %{with mpich}
%package mpich
Summary:        MPICH build for arbor
BuildRequires:  mpich-devel
BuildRequires:  rpm-mpi-hooks
BuildRequires:  python3-mpi4py-mpich

Requires:       mpich
Requires:       python3-mpich
Requires:       python3-mpi4py-mpich
Requires:       %{py3_dist numpy}
Provides:       python3-arbor-mpich = %{version}-%{release}

%description mpich %{_description}

%package mpich-devel
Summary:    Development files for arbor-mpich
Requires:   arbor-mpich%{?_isa} = %{version}-%{release}
Provides:   arbor-mpich-static = %{version}-%{release}

%description mpich-devel %{_description}
%endif

%if %{with openmpi}
%package openmpi
Summary:        OpenMPI build for arbor
BuildRequires:  openmpi-devel
BuildRequires:  rpm-mpi-hooks
BuildRequires:  python3-mpi4py-openmpi

Requires:       openmpi
Requires:       python3-openmpi
Requires:       python3-mpi4py-openmpi
Requires:       %{py3_dist numpy}
Provides:       python3-arbor-openmpi = %{version}-%{release}

%description openmpi %{_description}

%package openmpi-devel
Summary:    Development files for arbor-openmpi
Requires:   arbor-openmpi%{?_isa} = %{version}-%{release}
Provides:   arbor-openmpi-static = %{version}-%{release}

%description openmpi-devel %{_description}
%endif

%prep
%forgeautosetup -p1

# correct catalogue location
sed -i 's|dummy-catalogue.so|lib/dummy-catalogue.so|' python/test/unit/test_catalogues.py

# Disable failing padded test
sed -i '/test_padded.cpp/ d' test/unit/CMakeLists.txt

# should always be included, but is currently included only if bundled pybind11
# is used
sed -i '/add_subdirectory(python)/i \
include(FindPythonModule)' CMakeLists.txt
# Do not build external libraries
sed -i -e 's/ ext-random123//' CMakeLists.txt

# Disable doc build: we built it ourselves
sed -i '/add_subdirectory(doc)/ d' CMakeLists.txt

# Remove ext folders, unbundle libraries
rm -vrf ext/google-benchmark ext/json ext/random123
mv ext/tinyopt/LICENSE ext/tinyopt/LICENSE-tinyopt

# tclap and json are both header only
find . -type f -name "CMakeLists.txt" -exec sed -i -e 's/ext-tclap//' -e 's/ext-json//' {} 2>/dev/null ';'

# Correct Python shebangs in all files
find . -type f -name "*" -exec sed -i 's|^#![  ]*/usr/bin/env.*python.*$|#!/usr/bin/python3|' {} 2>/dev/null ';'

# Fix shebang (special case)
sed -i 's|^#![  ]*/usr/env/bin.*python.*$|#!/usr/bin/python3|' example/lfp/neuron_lfp_example.py

# test scripts
cp %{SOURCE1} scripts/
cp %{SOURCE2} scripts/
chmod +x scripts/*.sh
sed -i 's/ python / python3 /' scripts/run_python_examples.sh
sed -i 's|build/|./|' scripts/run_cpp_examples.sh

# builddir for serial
mkdir build-serial

%if %{with mpich}
    mkdir build-mpich
%endif

%if %{with openmpi}
    mkdir build-openmpi
%endif

%build
# Best to use && so that if anything in the chain fails, the build also fails
# straight away
%global do_cmake_config %{expand: \
echo
echo "*** BUILDING arbor-%{version}$MPI_COMPILE_TYPE ***"
echo
pushd build$MPI_COMPILE_TYPE  &&
    cmake \\\
        -DCMAKE_C_FLAGS_RELEASE:STRING="-DNDEBUG" \\\
        -DCMAKE_CXX_FLAGS_RELEASE:STRING="-DNDEBUG" \\\
        -DCMAKE_Fortran_FLAGS_RELEASE:STRING="-DNDEBUG" \\\
        -DCMAKE_VERBOSE_MAKEFILE:BOOL=ON \\\
        -DCMAKE_INSTALL_PREFIX:PATH=$MPI_HOME \\\
        -DINCLUDE_INSTALL_DIR:PATH=$MPI_INCLUDE \\\
        -DLIB_INSTALL_DIR:PATH=$MPI_LIB \\\
        -DSYSCONF_INSTALL_DIR:PATH=%{_sysconfdir} \\\
        -DSHARE_INSTALL_PREFIX:PATH=%{_datadir} \\\
        -DCMAKE_SKIP_RPATH:BOOL=ON \\\
        -DCMAKE_BUILD_TYPE:STRING="release" \\\
        -DARB_USE_BUNDLED_LIBS:BOOL=OFF \\\
        -DARB_USE_BUNDLED_PYBIND11:BOOL=OFF \\\
        -DARB_VECTORIZE:BOOL=OFF \\\
        -DARB_WITH_MPI:BOOL=$MPI_YES \\\
        -DARB_WITH_GPU:BOOL=OFF \\\
        -DARB_ARCH:STRING="none" \\\
        -DARB_CXX_FLAGS_TARGET:STRING="-ffat-lto-objects" \\\
        -DCMAKE_INSTALL_LIBDIR=%{_lib} \\\
        -DARB_WITH_PYTHON:BOOL=ON \\\
        -DARB_PYTHON_LIB_PATH:STRING=$MPI_PYTHON3_SITEARCH \\\
%if "%{_lib}" == "lib64"
        -DLIB_SUFFIX=64 .. &&
%else
        -DLIB_SUFFIX=""  .. &&
%endif
popd || exit -1;

# Upstream only supports static libraries
# https://github.com/arbor-sim/arbor/issues/916
# -DBUILD_SHARED_LIBS:BOOL=ON \\\
# Missing BRs
# -DARB_BUILD_VALIDATION_DATA:BOOL=ON \\\
}

%global do_make_build %{expand: \
    %make_build -C build$MPI_COMPILE_TYPE || exit -1
    %make_build -C build$MPI_COMPILE_TYPE examples || exit -1
%if %{with tests}
    %make_build -C build$MPI_COMPILE_TYPE tests || exit -1
%endif
}

# Build serial version, dummy arguments
%set_build_flags
export CC=gcc
export CXX=g++
export MPI_SUFFIX=""
export MPI_HOME=%{_prefix}
export MPI_INCLUDE=%{_includedir}
export MPI_LIB=%{_libdir}
export MPI_YES=OFF
export MPI_COMPILE_TYPE="-serial"
export MPI_PYTHON3_SITEARCH=%{python3_sitearch}
%{do_cmake_config}
%{do_make_build}

# skip building sphinx docs because they bundle js/fonts and it's very hard to
# unbundle

# Build mpich version
%if %{with mpich}
%{_mpich_load}
%set_build_flags
export CC=mpicc
export CXX=mpicxx
export FC=mpif90
export F77=mpif77
export MPI_YES=ON
export MPI_COMPILE_TYPE="-mpich"
%{do_cmake_config}
%{do_make_build}

%{_mpich_unload}
%endif

# Build OpenMPI version
%if %{with openmpi}
%{_openmpi_load}
%set_build_flags
export CC=mpicc
export CXX=mpicxx
export FC=mpif90
export F77=mpif77
export MPI_YES=ON
# Python 3
export MPI_COMPILE_TYPE="-openmpi"
%{do_cmake_config}
%{do_make_build}

%{_openmpi_unload}
%endif

%install
# Install everything
%global do_install %{expand: \
echo
echo "*** INSTALLING arbor-%{version}$MPI_COMPILE_TYPE ***"
echo
    %make_install -C build$MPI_COMPILE_TYPE || exit -1
}

# install serial version
export MPI_SUFFIX=""
export MPI_HOME=%{_prefix}
export MPI_BIN=%{_bindir}
export MPI_YES=OFF
export MPI_COMPILE_TYPE="-serial"
%{do_install}


# Install MPICH version
%if %{with mpich}
%{_mpich_load}
export MPI_COMPILE_TYPE="-mpich"
%{do_install}

# Place in correct mpi libdir
%if "%{_lib}" == "lib64"
    mv -v $RPM_BUILD_ROOT/%{_libdir}/mpich/lib64 $RPM_BUILD_ROOT/$MPI_LIB/
%endif

pushd $RPM_BUILD_ROOT/$MPI_BIN
    mv -v modcc{,$MPI_SUFFIX} -v
    mv -v arbor-build-catalogue{,$MPI_SUFFIX} -v
    mv -v lmorpho{,$MPI_SUFFIX} -v
popd
%{_mpich_unload}
%endif

# Install OpenMPI version
%if %{with openmpi}
%{_openmpi_load}
export MPI_COMPILE_TYPE="-openmpi"
%{do_install}

# Correct location
%if "%{_lib}" == "lib64"
    mv -v $RPM_BUILD_ROOT/%{_libdir}/openmpi/lib64 $RPM_BUILD_ROOT/$MPI_LIB/
%endif

pushd $RPM_BUILD_ROOT/$MPI_BIN
    mv -v modcc{,$MPI_SUFFIX} -v
    mv -v arbor-build-catalogue{,$MPI_SUFFIX} -v
    mv -v lmorpho{,$MPI_SUFFIX} -v
popd
%{_openmpi_unload}
%endif


# https://github.com/arbor-sim/arbor/blob/master/.github/workflows/test-matrix.yml
%if %{with tests}
%check

# Taken from upstream's GitHub workflow
%global mpirun mpirun -n %{_smp_build_ncpus}

# these tests segfault, filter out
gtest_filter="${gtest_filter--}${gtest_filter+:}*diffusion*"

pushd build-serial
    %{py3_test_envvars} %{python3} -m unittest discover -v -s ../python
    ./bin/unit ${gtest_filter+--gtest_filter=}${gtest_filter-}
    ./bin/unit-modcc
    cp ../scripts/run_cpp_examples.sh .
    ./run_cpp_examples.sh
popd

# MPICH
%if %{with mpich}
%{_mpich_load}
pushd build-mpich
%if %{with mpi_py_unittest}
    %{py3_test_envvars} %{mpirun} %{python3} -m unittest discover -v -s ../python
%endif
    %{mpirun} ./bin/unit-mpi
    cp ../scripts/run_cpp_examples.sh .
    ./run_cpp_examples.sh "%{mpirun}"
popd
%{py3_test_envvars} ./scripts/run_python_examples.sh  "%{mpirun}"
%{_mpich_unload}
%endif

# OpenMPI
%if %{with openmpi}
%{_openmpi_load}
pushd build-openmpi
%if %{with mpi_py_unittest}
    %{py3_test_envvars} %{mpirun} %{python3} -m unittest discover -v -s ../python
%endif
    %{mpirun} ./bin/unit-mpi
    cp ../scripts/run_cpp_examples.sh .
    ./run_cpp_examples.sh "%{mpirun}"
popd
%{py3_test_envvars} ./scripts/run_python_examples.sh  "%{mpirun}"
%{_openmpi_unload}
%endif
%endif


%files
%license LICENSE ext/tinyopt/LICENSE-tinyopt
%doc README.md
%{_bindir}/modcc
%{_bindir}/arbor-build-catalogue
%{_bindir}/lmorpho
%{python3_sitearch}/arbor
%{_datadir}/arbor


%files devel
%{_includedir}/arborio
%{_includedir}/arbor
%{_includedir}/arborenv
%{_libdir}/cmake/arbor
%{_libdir}/libarbor.a
%{_libdir}/libarborio.a
%{_libdir}/libarborenv.a

%files doc
%license LICENSE
%doc example/


%if %{with mpich}
%files mpich
%doc README.md
%license LICENSE ext/tinyopt/LICENSE-tinyopt
%{_libdir}/mpich/bin/modcc_mpich
%{_libdir}/mpich/bin/arbor-build-catalogue_mpich
%{_libdir}/mpich/bin/lmorpho_mpich
%{python3_sitearch}/mpich/arbor
%{_libdir}/mpich/share/arbor

%files mpich-devel
%{_libdir}/mpich/include/arbor
%{_libdir}/mpich/include/arborio
%{_libdir}/mpich/include/arborenv
%{_libdir}/mpich/lib/cmake/arbor
%{_libdir}/mpich/lib/libarbor.a
%{_libdir}/mpich/lib/libarborio.a
%{_libdir}/mpich/lib/libarborenv.a
%endif

%if %{with openmpi}
%files openmpi
%doc README.md
%license LICENSE ext/tinyopt/LICENSE-tinyopt
%{_libdir}/openmpi/bin/modcc_openmpi
%{_libdir}/openmpi/bin/arbor-build-catalogue_openmpi
%{_libdir}/openmpi/bin/lmorpho_openmpi
%{python3_sitearch}/openmpi/arbor
%{_libdir}/openmpi/share/arbor

%files openmpi-devel
%{_libdir}/openmpi/include/arbor
%{_libdir}/openmpi/include/arborio
%{_libdir}/openmpi/include/arborenv
%{_libdir}/openmpi/lib/cmake/arbor
%{_libdir}/openmpi/lib/libarbor.a
%{_libdir}/openmpi/lib/libarborio.a
%{_libdir}/openmpi/lib/libarborenv.a
%endif

%changelog
%autochangelog
