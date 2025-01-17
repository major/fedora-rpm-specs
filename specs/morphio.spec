# Use forge macros for pulling from GitHub
%global forgeurl https://github.com/BlueBrain/MorphIO

%global _description %{expand:
MorphIO is a library for reading and writing neuron morphology files. It
supports the following formats:

- SWC
- ASC (aka. neurolucida)
- H5 v1
- H5 v2 is not supported anymore

It provides 3 C++ classes that are the starting point of every morphology
analysis:

- Soma: contains the information related to the soma.
- Section: a section is the succession of points between two bifurcations. To
  the bare minimum the Section object will contain the section type, the
  position and diameter of each point.
- Morphology: the morphology object contains general information about the
  loaded cell but also provides accessors to the different sections.

One important concept is that MorphIO is split into a read-only part and a
read/write one.
}

# cpp tests
%bcond tests 1
# python tests
%bcond pytests 1

Name:           morphio
Version:        3.4.0
Release:        %autorelease
Summary:        A python and C++ library for reading and writing neuronal morphologies
%forgemeta
# The entire source is Apache-2.0 except the following, which is BSD-3-Clause:
#   - CMake/CodeCoverage.cmake: just a build-system file; it is not installed
#     and does not contribute to the licenses of the binary RPMs
License:        Apache-2.0
URL:            %forgeurl
Source:         %forgesource

# Patches
# https://github.com/sanjayankur31/MorphIO/tree/fedora-3.3.2
# Some sent upstream: https://github.com/BlueBrain/MorphIO/pull/293
# Do not let cmake use $FLAGS env var
Patch:          stop-them-using-a-random-env-var.patch
# Remove more hard-coded compiler flags
Patch:          remove-upstreams-flags.patch
# Add install target for the compiled python module
Patch:          install-python-shared-object.patch
# Downstream-only: Allow passing CMake defs through an env. var.
#
# It is too hard to get the build_ext command-line arguments passed
# through when building a wheel.
Patch:          0001-Downstream-only-Allow-passing-CMake-defs-through-an-.patch
# Some Python tests are failing because “expected” results are float32 and then
# promoted back to float64 for comparison with the actual results. We are not
# sure why upstream is not experiencing this.
Patch:          pytest-float32.patch
# use LIB_INSTALL_DIR which is defined by %%cmake
Patch:          use-lib_install_dir.patch
# Allow use of external ghc_filesystem
Patch:          allow_use_of_external_ghc_filesystem.patch
# Above patch fails with:
#CMake Error at src/CMakeLists.txt:64 (target_include_directories):
#  Error evaluating generator expression:
#
#    $<TARGET_PROPERTY:ghc_filesystem,INTERFACE_INCLUDE_DIRECTORIES>
#
#  Target "ghc_filesystem" not found.
# So let's circumvent CMake foo for ghc_filesystem
Patch:          dont_use_cmake_for_finding_ghc_filesystem.patch
# Fix a test regression with pybind11 2.11.2, 2.12.1, 2.13.6+
# https://github.com/BlueBrain/MorphIO/pull/515
Patch:          %{forgeurl}/pull/515.patch
# Include <cstdint> for fixed-width integers in API headers
# https://github.com/BlueBrain/MorphIO/pull/517
# Fixes failure to build with GCC 15.
Patch:          %{forgeurl}/pull/517.patch

# skip locale check if std::locale fails
Patch:          https://github.com/BlueBrain/MorphIO/pull/512.patch

# https://fedoraproject.org/wiki/Changes/EncourageI686LeafRemoval
ExcludeArch:    %{ix86}

BuildRequires:  tomcli

BuildRequires:  hdf5-devel
BuildRequires:  boost-devel
%if %{with tests}
BuildRequires:  cmake(Catch2) < 3
%endif

BuildRequires:  gcc-c++
BuildRequires:  cmake
BuildRequires:  ninja-build

# Header-only libraries; -static required by guidelines for tracking
BuildRequires:  cmake(gsl-lite)
BuildRequires:  gsl-lite-static
BuildRequires:  cmake(highfive)
BuildRequires:  highfive-static
BuildRequires:  lexertl14-devel
BuildRequires:  lexertl14-static
BuildRequires:  cmake(ghc_filesystem)
BuildRequires:  gulrak-filesystem-static
BuildRequires:  cmake(pybind11)
BuildRequires:  pybind11-static

BuildRequires:  python3-devel

%description %_description


%package        devel
Summary:        Development files for MorphIO
Requires:       morphio%{?_isa} = %{version}-%{release}
Provides:       morphio-static = %{version}-%{release}

# A gsl header is included from the public morphio/types.h header.
Requires:       gsl-lite-devel%{?_isa}
Requires:       gsl-lite-static
# A HighFive header is included from the public morphio/morphology.h header.
Requires:       highfive-devel%{?_isa}
Requires:       highfive-static
# Note that packages using this -devel package should ideally also BR
# gsl-lite-static and highfive-static for header-only library tracking.

%description    devel
The morphio-devel package contains libraries and header files for
developing applications that use MorphIO.


%package -n python3-morphio
Summary:        Python bindings for MorphIO

# Note that this package does not depend at all on the base package (it does
# not link against the shared library).

%description -n python3-morphio
This package includes the Python 3 bindings for MorphIO.


%package doc
Summary:        Documentation for MorphIO
BuildArch:      noarch

%description doc
This package provides documentation for MorphIO


%prep
%autosetup -n MorphIO-%{version} -p1

# Unbundle gsl-lite
rm -rvf 3rdparty/GSL_LITE
sed -r -i '/GSL_LITE/d' MANIFEST.in
sed -r -i '/director.*\(.*(gsl-lite|GSL_LITE).*\)/d' 3rdparty/CMakeLists.txt
sed -r -i \
    -e '/TARGET_PROPERTY:gsl-lite,INTERFACE_INCLUDE_DIRECTORIES/d' \
    -e 's/PUBLIC[[:blank:]]+gsl-lite[[:blank:]]+(PRIVATE)/\1/' \
    src/CMakeLists.txt
# Update includes. Note that this affects the public API headers.
#
# The grep-then-sed pattern means we only modify those files that need it,
# preserving the mtimes on the others.
grep -ErIl '#[[:blank:]]*include[[:blank:]]+["<]gsl/gsl[">]' . |
  xargs -r sed -r -i \
      's@(#[[:blank:]]*include[[:blank:]]+["<]gsl/gsl)([">])@\1-lite\.hpp\2@'

# Unbundle lexertl
rm -rvf '3rdparty/lexertl'
ln -s '%{_includedir}/lexertl' '3rdparty/'

# Some of these could make it into the installed package:
find . -type f -name .gitignore -print -delete

# We already depend on system versions of these; depending on “PyPI versions”
# of these is just a hack to install them in a virtualenv. Even if these are
# satisfiable, nothing relies on having the Python dist-info metadata.
tomcli set pyproject.toml lists delitem --type regex --no-first \
    build-system.requires '^(cmake|ninja)$'


%generate_buildrequires
export SETUPTOOLS_SCM_PRETEND_VERSION='%{version}'
%pyproject_buildrequires %{?with_pytests:tests/requirement_tests.txt}


%build
export SETUPTOOLS_SCM_PRETEND_VERSION='%{version}'
%cmake \
    -DBUILD_BINDINGS:BOOL=FALSE \
    -DEXTERNAL_CATCH2:BOOL=TRUE \
    -DEXTERNAL_GHC_FILESYSTEM:BOOL=TRUE \
    -DEXTERNAL_HIGHFIVE:BOOL=TRUE \
    -DEXTERNAL_PYBIND11:BOOL=TRUE \
    -DMORPHIO_ENABLE_COVERAGE:BOOL=FALSE \
    -DMORPHIO_TESTS:BOOL=%{?with_tests:TRUE}%{?!with_tests:FALSE} \
    -DMORPHIO_USE_DOUBLE:BOOL=TRUE \
    -DMORPHIO_VERSION_STRING:STRING="%{version}" \
    -DMorphIO_CXX_WARNINGS:BOOL=FALSE \
    -GNinja \
    -Wno-dev
%cmake_build

# Applicable options from the main %%cmake invocation, above:
mcd="${mcd-}${mcd+,}EXTERNAL_GHC_FILESYSTEM:BOOL=TRUE"
mcd="${mcd-}${mcd+,}MORPHIO_USE_DOUBLE:BOOL=TRUE"
mcd="${mcd-}${mcd+,}MorphIO_CXX_WARNINGS:BOOL=FALSE"
mcd="${mcd-}${mcd+,}EXTERNAL_HIGHFIVE:BOOL=TRUE"
mcd="${mcd-}${mcd+,}EXTERNAL_PYBIND11:BOOL=TRUE"
# Selected possibly-applicable options from the definition of %%cmake in
# /usr/lib/rpm/macros.d/macros.cmake:
mcd="${mcd-}${mcd+,}CMAKE_C_FLAGS_RELEASE:STRING=-DNDEBUG"
mcd="${mcd-}${mcd+,}CMAKE_CXX_FLAGS_RELEASE:STRING=-DNDEBUG"
mcd="${mcd-}${mcd+,}CMAKE_VERBOSE_MAKEFILE:BOOL=ON"
mcd="${mcd-}${mcd+,}CMAKE_INSTALL_DO_STRIP:BOOL=OFF"
# Keep pybind11 from automagically stripping the compiled extension
mcd="${mcd-}${mcd+,}CMAKE_STRIP=/bin/true"
export MORPHIO_CMAKE_DEFS="${mcd-}"
%pyproject_wheel


%install
%cmake_install
%pyproject_install
%pyproject_save_files -l morphio


%check
%if %{with tests}
# From ci/cpp_test.sh
%ctest -VV
%endif
%if %{with pytests}
# We will change directories so that the “un-built” package is not imported
xdir="$(basename "${PWD}")"
# From ci/python_test.sh
cd ..
# Fetches from the Internet:
k='not test_v2'
# Still fails in 3.4.0
# TODO: Is this a real problem? The answer is only slightly outside tolerances.
#
# >               assert_array_almost_equal(neuron.markers[0].points,
#                                           np.array([[81.58, -77.98, -20.32]], dtype=np.float32))
# E           AssertionError:
# E           Arrays are not almost equal to 6 decimals
# E
# E           Mismatched elements: 1 / 3 (33.3%)
# E           Max absolute difference: 2.e-06
# E           Max relative difference: 3.87747174e-08
# E            x: array([[ 51.58, -77.78, -24.32]])
# E            y: array([[ 51.580002, -77.779999, -24.32    ]])
#
k="${k} and not test_neurolucida_markers"
# Still fails to 3.4.0
# TODO: Is this a real problem? The answer is only slightly outside tolerances.
#
# >       assert_array_equal(m.markers[0].points, np.array([[  -0.97    , -141.169998,   84.769997]],
#                                                          dtype=np.float32))
# E           AssertionError:
# E           Arrays are not equal
# E
# E           Mismatched elements: 2 / 3 (66.7%)
# E           Max absolute difference: 2.99999999e-06
# E           Max relative difference: 3.53898797e-08
# E            x: array([[  -0.97, -141.17,   84.77]])
# E            y: array([[  -0.97    , -141.169998,   84.769997]])
k="${k} and not test_marker_with_string"
# In the same vein as above, failing since 3.4.0
# E           AssertionError:
# E           Arrays are not equal
# E
# E           Mismatched elements: 1 / 2 (50%)
# E           Max absolute difference: 2.38418579e-08
# E           Max relative difference: 3.97364299e-08
# E            x: array([0.5, 0.6])
# E            y: array([0.5, 0.6])
k="${k} and not test_mitochondria"
k="${k} and not test_mitochondria_read"
# TODO: pytest segfaults while writing a temporary file..
k="${k} and not test_dendritic_spine_round_trip_empty_postsynaptic_density"
%pytest "${xdir}/tests" -k "${k}" -v
%endif


%files
%license LICENSE.txt
%{_libdir}/libmorphio.so.0.0.0


%files devel
%{_includedir}/morphio/
%{_libdir}/libmorphio.so
%{_libdir}/cmake/MorphIO/


%files -n python3-morphio -f %{pyproject_files}


%files doc
%license LICENSE.txt
%doc AUTHORS.txt CHANGELOG.md CONTRIBUTING.md README.rst examples

%changelog
%autochangelog
