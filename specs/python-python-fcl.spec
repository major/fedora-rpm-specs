# The libccd dependency can be built in single-precision or double-precision
# mode, but not both at the same time. This is awkward and not conducive to
# system packaging. The goal is to build libccd in double-precision mode in
# Fedora, as discussed in:
#   Build libccd with double-precision?
#   https://bugzilla.redhat.com/show_bug.cgi?id=2236527
# This actually reduces the number of (ignored) test failures in the fcl
# package, and it’s absolutely necessary for this package: with a
# single-precision libccd (and an fcl built using that single-precision
# libccd), one of the tests hangs forever.
#
# Until the system libccd is double-precision (and after that in stable
# branches, since this will be an ABI-breaking change), we must therefore
# bundle and build our own libccd and fcl.
#
# See:
#
# Build libccd with double-precision?
# https://bugzilla.redhat.com/show_bug.cgi?id=2236527
%bcond system_fcl 0
# See build_dependencies/install_linux.sh for the versions used upstream to
# build PyPI wheels.
%global libccd_version 2.1
%global fcl_version 0.7.0

# Note that this is https://pypi.org/project/python-fcl/; the canonical project
# name fcl, https://pypi.org/project/fcl/, belongs to a different and
# apparently defunct project. See
#   https://docs.fedoraproject.org/en-US/packaging-guidelines/Python/#_library_naming
Name:           python-python-fcl
Version:        0.7.0.8
Release:        %autorelease
Summary:        Python bindings for the Flexible Collision Library

# Conveniently, both libccd and fcl are BSD-3-Clause, so the License does not
# change when we bundle them.
License:        BSD-3-Clause
URL:            https://github.com/BerkeleyAutomation/python-fcl
# No sdists are released on PyPI; we must use the GitHub archive
#
# Source distribution is not available on pypi after 0.6.1
# https://github.com/BerkeleyAutomation/python-fcl/issues/55
Source0:        %{url}/archive/v%{version}/python-fcl-%{version}.tar.gz
%global libccd_forgeurl https://github.com/danfis/libccd
Source1:        %{libccd_forgeurl}/archive/v%{libccd_version}/libccd-%{libccd_version}.tar.gz
%global fcl_forgeurl https://github.com/ambi-robotics/fcl
Source2:        %{fcl_forgeurl}/archive/v%{fcl_version}/fcl-%{fcl_version}.tar.gz

# https://fedoraproject.org/wiki/Changes/EncourageI686LeafRemoval
ExcludeArch:    %{ix86}

# Downstream-only patch to *allow* bundling libccd/fcl:
# Add environment variables to control bundling
Patch0:         0001-Add-environment-variables-to-control-bundling.patch

# Patches for bundled libccd, based on https://src.fedoraproject.org/rpms/libccd/
#
# This patch integrates additional programs that are present in
# the testsuites folder into CMake, via CTest.
# It also increments the version number to match the release.
# Not yet submitted  upstream
Patch1001:      https://src.fedoraproject.org/rpms/libccd/raw/80bc68bb9f9644aec2e8dbf036e3ac84be918eef/f/libccd-2.1-ctest.patch
# (We do not need libccd-2.1-pkgconfig.patch, because we are not using or installing the .pc file from the bundled libccd.)
# Convert check_regressions to python3
# Not submitted upstream
Patch1002:      https://src.fedoraproject.org/rpms/libccd/raw/80bc68bb9f9644aec2e8dbf036e3ac84be918eef/f/libccd-2.1-py3.patch
 
BuildRequires:  python3-devel

BuildRequires:  gcc-c++

BuildRequires:  octomap-devel
# https://docs.fedoraproject.org/en-US/packaging-guidelines/#_packaging_header_only_libraries 
BuildRequires:  eigen3-static
%if %{with system_fcl}
BuildRequires:  fcl-devel
%else
# For bundled libccd:
BuildRequires:  cmake
BuildRequires:  ninja-build
# For bundled libccd (testing):
%ifarch %{valgrind_arches}
BuildRequires:  valgrind
%endif
%endif

BuildRequires:  %{py3_dist pytest}

%global common_description %{expand:
Python-FCL is an (unofficial) Python interface for the Flexible Collision
Library (FCL), an excellent C++ library for performing proximity and collision
queries on pairs of geometric models.

This package supports three types of proximity queries for pairs of geometric
models:

  • Collision Detection: Detecting whether two models overlap (and optionally
    where).
  • Distance Computation: Computing the minimum distance between a pair of
    models.
  • Continuous Collision Detection: Detecting whether two models overlap during
    motion (and optionally the time of contact).

This package also supports most of FCL’s object shapes, including:

  • TriangleP
  • Box
  • Sphere
  • Ellipsoid
  • Capsule
  • Cone
  • Convex
  • Cylinder
  • Half-Space
  • Plane
  • Mesh
  • OcTree}

%description %{common_description}


%package -n     python3-python-fcl
Summary:        %{summary}

# https://docs.fedoraproject.org/en-US/packaging-guidelines/Python/#_provides_for_importable_modules
%py_provides python3-fcl

%if %{without system_fcl}
Provides:       bundled(libccd) = %{libccd_version}
Provides:       bundled(fcl) = %{fcl_version}
%endif

%description -n python3-python-fcl %{common_description}


%prep
%autosetup -n python-fcl-%{version} -N
%autopatch -M999 -p1

%if %{without system_fcl}
%setup -q -T -D -b 1 -n python-fcl-%{version}
pushd ../libccd-%{libccd_version}/
%autopatch -m1000 -M1999 -p0
popd
cp -p ../libccd-%{libccd_version}/BSD-LICENSE libccd-LICENSE

%setup -q -T -D -b 2 -n python-fcl-%{version}
pushd ../fcl-%{fcl_version}/
%autopatch -m2000 -M2999 -p1
popd
cp -p ../fcl-%{fcl_version}/LICENSE fcl-LICENSE
%endif


%generate_buildrequires
%pyproject_buildrequires


%build
%if %{without system_fcl}
BUNDLEROOT="%{_vpath_builddir}/_bundled"
mkdir -p "${BUNDLEROOT}"
# Ensure we have an absolute path
pushd "${BUNDLEROOT}"
BUNDLEROOT="${PWD}"
popd
# For each bundled dependency, we build a static library so we can link it into
# the Python extension shared library. We must force PIC so that the static
# library can be linked into a shared library. We also build and run the tests
# of the bundled dependencies for added confidence.

pushd ../libccd-%{libccd_version}/
%cmake -GNinja \
    -DBUILD_SHARED_LIBS:BOOL=OFF \
    -DBUILD_STATIC_LIBS:BOOL=ON \
    -DCMAKE_POSITION_INDEPENDENT_CODE:BOOL=ON \
    -DBUILD_TESTING:BOOL=ON \
    -DENABLE_DOUBLE_PRECISION:BOOL=ON
%cmake_build
# Like %%cmake_install, but without DESTDIR="%%{buildroot}":
DESTDIR="${BUNDLEROOT}" %__cmake --install "%{_vpath_builddir}"
# We needed to “install” the bundled library because FCL needs headers from the
# source tree AND the generated config.h, but accepts only a single
# CCD_INCLUDE_DIR. Installing combines these headers in a single path.
popd

pushd ../fcl-%{fcl_version}/
%cmake -GNinja \
    -DCCD_LIBRARY:PATH="${BUNDLEROOT}%{_libdir}/libccd.a" \
    -DCCD_INCLUDE_DIR:PATH="${BUNDLEROOT}%{_includedir}" \
    -DCMAKE_POSITION_INDEPENDENT_CODE:BOOL=ON \
    -DFCL_STATIC_LIBRARY:BOOL=ON \
    -DFCL_NO_DEFAULT_RPATH:BOOL=OFF \
    -DFCL_USE_HOST_NATIVE_ARCH:BOOL=OFF \
    -DFCL_USE_X64_SSE:BOOL=OFF
%cmake_build
DESTDIR="${BUNDLEROOT}" %__cmake --install "%{_vpath_builddir}"
popd

export PYTHON_FCL_EXTRA_INCLUDE_DIRS="${BUNDLEROOT}%{_includedir}"
# Linking order matters!
XO="${XO-}${XO+ }${BUNDLEROOT}%{_libdir}/libfcl.a"
XO="${XO-}${XO+ }${BUNDLEROOT}%{_libdir}/libccd.a"
export PYTHON_FCL_EXTRA_OBJECTS="${XO-}"
# No -lfcl:
export PYTHON_FCL_OMIT_LIBRARIES='fcl'
%endif

# For importing fcl.__version__
#export PYTHONPATH="${PWD}/src"

%pyproject_wheel


%install
%pyproject_install
%pyproject_save_files -l fcl

# Do not install Cython-generated C++ sources that were used to compile the
# extension. This is pretty hard to fix upstream in setup.cfg (see various
# issues like https://github.com/pypa/setuptools/issues/2710), and no patch has
# been attempted.
find '%{buildroot}%{python3_sitearch}' -type f -name '*.cpp' -print -delete
sed -r -i '/\.cpp$/d' %{pyproject_files}


%check
%if %{without system_fcl}

pushd ../libccd-%{libccd_version}/
skips='^($.'
%ifarch %{valgrind_arches}
skips="${skips}|.*-valgrind.*"
%endif
skips="${skips})$"
%ctest --exclude-regex "${skips}"
popd

pushd ../fcl-%{fcl_version}/
# Run the gtest-based executables manually rather than via the ctest harness so
# that we can skip individual tests within individual executables.
for exe in %{_vpath_builddir}/test/test_*
do
  # See: https://bugzilla.redhat.com/show_bug.cgi?id=2236527#c2
  unset filter
  case "$(basename "${exe}")" in
  test_fcl_capsule_capsule)
%ifarch aarch64
    filter="${filter--}${filter+:}CapsuleCapsuleSegmentTest/1.NominalSeparatedCase"
%endif
%ifarch aarch64 ppc64le
    filter="${filter--}${filter+:}CapsuleCapsuleSegmentTest/0.OverlappingCenterLines"
%endif
    ;;
  test_gjk_libccd-inl_gjk_doSimplex2)
%ifarch aarch64 ppc64le
    filter="${filter--}${filter+:}DoSimplex2Test.NeedMoreComputing"
    filter="${filter--}${filter+:}DoSimplex2Test.OriginInSimplex"
%endif
    ;;
  test_gjk_libccd-inl_epa)
%ifarch aarch64 ppc64le s390x
    filter="${filter--}${filter+:}FCL_GJK_EPA.ComputeVisiblePatchColinearNewVertex"
%endif
    ;;
  test_fcl_math)
%ifarch s390x
    filter="${filter--}${filter+:}FCL_MATH.rss_conversion"
%endif
    ;;
  esac
  "${exe}" --gtest_filter="${filter}"
done
popd
%endif

rm -rvf fcl
%pytest --verbose


%files -n python3-python-fcl -f %{pyproject_files}
%if %{without system_fcl}
%license libccd-LICENSE fcl-LICENSE
%endif
%doc README.md
%doc examples/


%changelog
%autochangelog
