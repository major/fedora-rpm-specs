%bcond tests 1
# Where possible, re-generate test data files?
%bcond regenerate_test_data 1

Name:           libsonata
Version:        0.1.29
# The SONAME version is constructed from the version number (MAJOR.MINOR), but
# we repeat it here to avoid undected SONAME version bumps.
%global so_version 0.1
Release:        %autorelease
Summary:        A Python and C++ interface to the SONATA format

# The entire package is LGPL-3.0-only, except:
#
# BSL-1.0:
# - include/bbp/sonata/optional.hpp, removed in %%prep and replaced with a
#   dependency on optional-lite; but this is a header-only library, which we
#   must treat the same as a static library, so its license still contributes
#   to the licenses of the binary RPMs
# - include/bbp/sonata/variant.hpp, removed in %%prep and replaced with a
#   dependency on variant-lite; a header-only library like optional-lite
# MIT AND CC0-1.0
# - extlib/nlohmann/nlohmann/json.hpp, removed in %%prep and replaced with a
#   dependency on json, another header-only library; the CC0-1.0 portion is a
#   bundled copy of hedley, another header-only library. While CC0-1.0 is
#   not-allowed for code in Fedora, hedley falls under the following blanket
#   exception: “Existing uses of CC0-1.0 on code files in Fedora packages prior
#   to 2022-08-01, and subsequent upstream versions of those files in those
#   packages, continue to be allowed. We encourage Fedora package maintainers
#   to ask upstreams to relicense such files.”
# BSD-3-Clause:
# - CMake/CodeCoverage.cmake, a build-system file that does not contribute to
#   the licenses of the binary RPMs
License:        LGPL-3.0-only AND BSL-1.0 AND MIT AND CC0-1.0
# Additionally, the following are present in the source archive, but do not
# contribute to the licenses of the binary RPMs.
#
# MIT:
# - extlib/filesystem.hpp, corresponding to gulrak-filesystem: removed in
#   %%prep, and made unnecessary by a patch to use std::filesystem instead
SourceLicense:  %{license} AND BSD-3-Clause
URL:            https://github.com/openbraininstitute/libsonata
Source:         %{url}/archive/v%{version}/%{name}-%{version}.tar.gz

# Downstream-only: TODO: can/should this be upstreamed?
Patch:          0001-Remove-pybind-redeclarations.patch

# Use std::filesystem
# https://github.com/BlueBrain/libsonata/pull/372
#
# This also bumps the minimum C++ standard to C++17 and supports (and requires)
# Catch2 >= 3.x rather than 2.x.
#
# Rebased on v0.1.23.
Patch:          0002-Use-std-filesystem.patch
Patch:          0003-Substitute-ghc-in-tests.patch
# Additional necessary adjustments suggested in
# https://github.com/BlueBrain/libsonata/pull/372#issuecomment-2631574780
Patch:          0004-Include-catch-catch_all.hpp-instead-of-catch-catch.h.patch
Patch:          0005-Link-Catch2-Catch2WithMain-instead-of-Catch2-Catch2.patch

# Use GNUInstallDirs
# https://github.com/openbraininstitute/libsonata/pull/1
Patch:          %{url}/pull/1.patch

# https://fedoraproject.org/wiki/Changes/EncourageI686LeafRemoval
ExcludeArch:    %{ix86}

# Used in %%prep:
BuildRequires:  git-core
BuildRequires:  tomcli

BuildRequires:  cmake
# Faster than make, with no disadvantages:
BuildRequires:  ninja-build
BuildRequires:  gcc-c++
BuildRequires:  python3-devel

BuildRequires:  cmake(Catch2)
BuildRequires:  cmake(fmt)
BuildRequires:  cmake(HighFive)
BuildRequires:  hdf5-devel
BuildRequires:  cmake(pybind11)

# Header-only libraries unbundled in %%prep; -static prescribed by guidelines
# for tracking of header-only libraries.
BuildRequires:  (cmake(nlohmann_json) with json-static)
BuildRequires:  optional-lite-static
BuildRequires:  variant-lite-static

# Test dependencies
%if %{with regenerate_test_data}
BuildRequires:  %{py3_dist h5py}
%endif
# Tests don’t explicitly require pytest, but it’s a convenient runner.
BuildRequires:  %{py3_dist pytest}


%global _description %{expand:
C++ / Python reader for SONATA circuit files. SONATA guide:
https://github.com/AllenInstitute/sonata/blob/master/docs/SONATA_DEVELOPER_GUIDE.md
}

%description %_description


%package devel
Summary:        Development files for %{name}

# Since optional-lite and variant-lite are unbundled, they do not appear in the
# devel package and do not contribute to its license, even though they are part
# of the public API; other header-only dependencies are only used to build
# libraries and would not appear in the API (and therefore in the -devel
# package) even if they *were* bundled.
License:        LGPL-3.0-only

Requires:       %{name}%{?_isa} = %{version}-%{release}
# These header-only dependencies are part of the public API. Very formally,
# dependent packages should probably depend on the -static packages for these,
# although this is getting a bit out of hand.
Requires:       optional-lite-devel optional-lite-static
Requires:       variant-lite-devel variant-lite-static

%description devel %_description


%package -n python3-libsonata
Summary:        %{summary}

%description -n python3-libsonata %_description


%prep
%autosetup -n libsonata-%{version} -S git
rm -rf libsonata.egg-info
rm -rf extlib/{Catch2,Highfive,fmt,nlohmann}

# Unbundle gulrak-filesystem
echo '#include <ghc/filesystem.hpp>' > extlib/filesystem.hpp
# Unbundle optional-lite
echo '#include <nonstd/optional.hpp>' > include/bbp/sonata/optional.hpp
# Unbundle variant-lite
echo '#include <nonstd/variant.hpp>' > include/bbp/sonata/variant.hpp

# Avoid bundling in the Python extension. We must use a patch since we cannot
# pass CMake options directly to the build system for the Python extension.
sed -r -i 's/(-DEXTLIB_FROM_SUBMODULES=)ON/\1OFF/' setup.py

# Comment out to remove /usr/bin/env shebangs
# Can use something similar to correct/remove /usr/bin/python shebangs also
# find . -type f -name "*.py" -exec sed -i '/^#![  ]*\/usr\/bin\/env.*$/ d' {} 2>/dev/null ';'

# Upstream builds against an old numpy for binary compatibility on PyPI, but we
# just build with the system numpy.
tomcli set pyproject.toml lists replace build-system.requires \
    oldest-supported-numpy numpy

%if %{with regenerate_test_data}
# These are the files that generate.py actually writes:
pushd tests/data
rm nodes1.h5 edges1.h5 spikes.h5 somas.h5 elements.h5
popd
%endif


%generate_buildrequires
%pyproject_buildrequires


%build
# Equivalent to passing -GNinja, but this way we can also affect CMake while it
# is building the Python extension.
export CMAKE_GENERATOR='Ninja'

%cmake \
    -DEXTLIB_FROM_SUBMODULES:BOOL=OFF \
    -DSONATA_CXX_WARNINGS:BOOL=OFF \
    -DSONATA_PYTHON:BOOL=OFF \
    -DSONATA_TESTS:BOOL=ON \
    -DSONATA_VERSION="%{version}"
%cmake_build

export SETUPTOOLS_SCM_PRETEND_VERSION=%{version}
# This environment variable affects (only) the Python bindings.
export SONATA_BUILD_TYPE='RelWithDebInfo'
# CMake environment variables
export VERBOSE=''
%pyproject_wheel


%install
%cmake_install
# remove static lib
rm -rf %{buildroot}/%{_libdir}/libsonata.a

%pyproject_install
%pyproject_save_files -l libsonata


%check
%if %{with regenerate_test_data}
pushd tests/data
%{py3_test_envvars} %{python3} generate.py
popd
%endif

%ctest tests

# We need the contents of python/tests to be at a parallel path (same depth
# from the top-level directory), but we need to ensure that the tests cannot
# find an “un-built” copy of libsonata in the parent directory.
mkdir _empty
cp -rp python/tests _empty/
%pytest -v _empty/tests


%files
%license COPYING.LESSER
%doc README.rst CHANGELOG.md
%{_libdir}/libsonata.so.%{so_version}
%{_libdir}/libsonata.so.%{version}


%files devel
# Potentially co-owned with other Blue Brain Project packages:
%dir %{_includedir}/bbp/
# Exclusively owned by this package:
%{_includedir}/bbp/sonata/
%{_datadir}/sonata/
%{_libdir}/libsonata.so


%files -n python3-libsonata -f %{pyproject_files}
%doc README.rst CHANGELOG.md


%changelog
%autochangelog
