Name:           earcut-hpp
Summary:        Fast, header-only polygon triangulation 
Version:        2.2.4
Release:        %autorelease

# SPDX
License:        ISC
URL:            https://github.com/mapbox/earcut.hpp
# A copy of libtess2 (https://github.com/memononen/libtess2) is bundled with
# the tests as a reference implementation (test/comparison/libtess2/).
#
# We do not treat it as a bundled system library (no virtual Provides, for
# example) because it is provably used only in the tests, and does not
# contribute to anything installed in the binary RPM. This means that its
# SGI-B-2.0 license also does not need to appear in the License tag.
#
# All of this is just as well, as libtess2 is unmaintained and we would rather
# not have to package it separately.

Source:         %{url}/archive/v%{version}/earcut.hpp-%{version}.tar.gz

BuildRequires:  gcc-c++
BuildRequires:  cmake
# Our choice; the default UNIX Makefiles backend would also work
BuildRequires:  ninja-build

# For tests (and benchmarks, if enabled):
BuildRequires:  pkgconfig(opengl)


# No compiled binaries are installed, so this would be empty.
%global debug_package %{nil}

%global common_description %{expand:
A C++ port of earcut.js, a fast, header-only polygon triangulation library.

The library implements a modified ear slicing algorithm, optimized by z-order
curve hashing and extended to handle holes, twisted polygons, degeneracies and
self-intersections in a way that doesn’t guarantee correctness of
triangulation, but attempts to always produce acceptable results for practical
data like geographical shapes.

It’s based on ideas from FIST: Fast Industrial-Strength Triangulation of
Polygons by Martin Held and Triangulation by Ear Clipping by David Eberly.}

%description %{common_description}


%package devel
Summary:        %{summary}

BuildArch:      noarch

# Header-only library
Provides:       %{name}-static = %{version}-%{release}

%description devel %{common_description}


%prep
%autosetup -n earcut.hpp-%{version} -p1
# Increase precision of test output so we can understand any failures:
sed -r -i 's/(setprecision\()6(\))/\116\2/' test/test.cpp


%build
# Disabling floating-point contraction fixes certain failures on aarch64,
# ppc64le, and s390x. See:
#
#   Test “self_touching” fails on aarch64, ppc64le, s390x
#   https://github.com/mapbox/earcut.hpp/issues/97
#
# particularly
#
#   https://github.com/mapbox/earcut.hpp/issues/97#issuecomment-1032813710
#
# and also
#
#   New test “issue142” in 2.2.4 fails on aarch64, ppc64le, s390x
#   https://github.com/mapbox/earcut.hpp/issues/103
#
# Since this library is header-only, dependent packages should be advised to
# add this flag too if they want the behavior of the library to exactly match
# upstream’s expectations.
export CXXFLAGS="${CXXFLAGS-} -ffp-contract=off"

# We do want to build the tests, but we have no use for the benchmarks or the
# visualizer program.
%cmake \
    -DEARCUT_BUILD_TESTS:BOOL=ON \
    -DEARCUT_BUILD_BENCH:BOOL=OFF \
    -DEARCUT_BUILD_VIZ:BOOL=OFF \
    -DEARCUT_WARNING_IS_ERROR:BOOL=OFF \
    -GNinja
%cmake_build


%install
# The upstream CMakeLists.txt has no install target; there is only one file to
# copy, so it is easy to do manually.
install -D -t '%{buildroot}%{_includedir}/mapbox' -p -m 0644 \
    'include/mapbox/earcut.hpp'


%check
# The upstream CMakeLists.txt is not configured to run tests via ctest; we run
# the test executable manually.
%{_vpath_builddir}/tests


%files devel
%license LICENSE
%doc CHANGELOG.md
%doc README.md

# All -devel packages for C and C++ libraries from Mapbox should co-own this
# directory.
%dir %{_includedir}/mapbox

%{_includedir}/mapbox/earcut.hpp


%changelog
%autochangelog
