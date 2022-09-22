Name:           python-mapbox-earcut
Version:        1.0.0
Release:        %autorelease
Summary:        Python bindings to the mapbox earcut C++ library

# SPDX
License:        ISC
URL:            https://github.com/skogler/mapbox_earcut_python
# The GitHub archive contains tests; the PyPI archive does not
Source0:        %{url}/archive/v%{version}/mapbox_earcut_python-%{version}.tar.gz

BuildRequires:  python3-devel

BuildRequires:  gcc-c++
BuildRequires:  cmake
BuildRequires:  make

# Header-only libraries; -static is for tracking, required by guidelines
# Minimum version added downstream to ensure the latest bug fixes are present
BuildRequires:  earcut-hpp-devel >= 2.2.4
BuildRequires:  earcut-hpp-static
# An extension built with pybind11 uses the pybind11 C++ libraries, which are
# header-only—so, strictly speaking, we need this as well:
BuildRequires:  pybind11-static

BuildRequires:  dos2unix

%global common_description %{expand:
Python bindings for the C++ implementation of the Mapbox Earcut library, which
provides very fast and quite robust triangulation of 2D polygons.

Original code: earcut.hpp

Original description:

    The library implements a modified ear slicing algorithm, optimized by
    z-order curve hashing and extended to handle holes, twisted polygons,
    degeneracies and self-intersections in a way that doesn’t guarantee
    correctness of triangulation, but attempts to always produce acceptable
    results for practical data like geographical shapes.}

%description %{common_description}


%package -n python3-mapbox-earcut
Summary:        %{summary}

%description -n python3-mapbox-earcut %{common_description}


%prep
%autosetup -n mapbox_earcut_python-%{version}

# Remove bundled earcut.hpp library
rm -rvf include

%if 0%{?fc34} || 0%{?fc35}
# Keep pybind11 from automatically disabling debugging symbols.
sed -r -i \
    's/^(setup\()/ext_modules[0]\.extra_compile_args.remove\("-g0"\)\n\1/' \
    setup.py
%endif

# Fix CRLF line endings in files that will be installed.
dos2unix *.md


%generate_buildrequires
%pyproject_buildrequires -x test


%build
%set_build_flags

# See comments in the earcut-hpp spec file, as well as:
# https://github.com/mapbox/earcut.hpp/issues/97
# https://github.com/mapbox/earcut.hpp/issues/103
export CFLAGS="${CFLAGS-} -ffp-contract=off"
export CXXFLAGS="${CXXFLAGS-} -ffp-contract=off"

%pyproject_wheel


%install
%pyproject_install
%pyproject_save_files mapbox_earcut


%check
%pytest


%files -n python3-mapbox-earcut -f %{pyproject_files}
# pyproject-rpm-macros handles LICENSE.md; verify with “rpm -qL -p …”
%doc README.md


%changelog
%autochangelog
