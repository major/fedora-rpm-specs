%bcond ctest 1

Name:           earcut-hpp
Summary:        Fast, header-only polygon triangulation 
Version:        3.2.3
Release:        %autorelease

# SPDX
License:        ISC
URL:            https://github.com/mapbox/earcut.hpp

Source0:        %{url}/archive/v%{version}/earcut.hpp-%{version}.tar.gz
# The %%check section uses test fixtures from the JavaScript implementation,
# normally downloaded at built time. This source is also licensed ISC, and does
# not contribute to the binary RPMs.
Source1:        https://github.com/mapbox/earcut/archive/v%{version}/earcut-%{version}.tar.gz

BuildSystem:    cmake
# We do want to build the tests, but we have no use for the benchmarks or the
# visualizer program.
BuildOption(conf): %{shrink:
    -DFETCHCONTENT_FULLY_DISCONNECTED:BOOL=ON
    -DEARCUT_BUILD_TESTS:BOOL=%{?with_ctest:ON}%{?!with_ctest:OFF}
    -DEARCUT_BUILD_BENCH:BOOL=OFF
    -DEARCUT_BUILD_VIZ:BOOL=OFF
    -DEARCUT_WARNING_IS_ERROR:BOOL=OFF
    }

BuildRequires:  gcc-c++
# We need picojson for a “fixtures” convenience library that is used by tests,
# benchmarks, and the visualization tool. Of these, we only build tests, and
# these are conditional, but the fixtures library is built unconditionally.
BuildRequires:  picojson-devel
%if %{with ctest}
# This, at least, is only required when tests are actually enabled.
BuildRequires:  cmake(gtest)
%endif

# No compiled binaries are installed, so this would be empty.
%global debug_package %{nil}

%global common_description %{expand:
A fast, header-only C++ port of earcut.js, the fastest and smallest JavaScript
polygon triangulation library.

Earcut favors raw speed and simplicity over triangulation quality, while being
robust enough to handle most practical datasets without crashing or producing
garbage, with an option to refine the result to Delaunay quality at a small
cost. Originally built for Mapbox GL, it’s a good fit for real-time
triangulation of geographical shapes and other practical data.

It implements a modified ear slicing algorithm, optimized by z-order curve and
spatial hashing and extended to handle holes, twisted polygons, degeneracies
and self-intersections in a way that doesn’t guarantee correctness of
triangulation, but attempts to always produce acceptable results for practical
data. It’s based on ideas from FIST: Fast Industrial-Strength Triangulation of
Polygons by Martin Held and Triangulation by Ear Clipping by David Eberly.}

%description %{common_description}


%package devel
Summary:        %{summary}

BuildArch:      noarch

# Header-only library
Provides:       %{name}-static = %{version}-%{release}

%description devel %{common_description}


%if %{with ctest}
%check -p
# Tests require certain fixtures (sample data files) from the JavaScript
# implementation’s sources. Mimic CMake’s FetchContent:
# https://cmake.org/cmake/help/latest/module/FetchContent.html
# By extracting this only in %%check, we prove it is not used in the build.
xdir='%{_vpath_builddir}/_deps/earcut_js-src'
mkdir --parents "${xdir}"
tar --extract --gzip --verbose '--file=%{SOURCE1}' \
    "--directory=${xdir}" --strip-components=1 \
    'earcut-%{version}/bench/tiles-fixture.bin' \
    'earcut-%{version}/test/expected.json' \
    'earcut-%{version}/test/fixtures/'
%endif

%files devel
%license LICENSE
%doc README.md

# All -devel packages for C and C++ libraries from Mapbox should co-own this
# directory.
%dir %{_includedir}/mapbox

%{_includedir}/mapbox/earcut.hpp
%{_datadir}/cmake/earcut_hpp/


%changelog
%autochangelog
