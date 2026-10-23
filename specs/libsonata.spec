%bcond tests 1

Name:           libsonata
Version:        0.2.2
# The SONAME version is constructed from the version number (MAJOR.MINOR), but
# we repeat it here to avoid undected SONAME version bumps.
%global so_version 0.2
Release:        %autorelease
Summary:        A Python and C++ interface to the SONATA format

# The binary RPMs are LGPL-3.0-only. The following licenses apply only to
# bundled source files used at build time, and do not contribute to the
# licenses of the binary RPMs:
#
# MIT (source only)
# - extlib/nlohmann/nlohmann/json.hpp, a header-only library
# BSD-3-Clause (source only)
# - CMake/CodeCoverage.cmake, a build-system file
License:        LGPL-3.0-only
SourceLicense:  %{license} AND MIT AND BSD-3-Clause
URL:            https://github.com/openbraininstitute/libsonata
Source:         %{url}/archive/v%{version}/%{name}-%{version}.tar.gz

Patch:          0001-use-gnuinstall-dirs.patch

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
BuildRequires:  fmt-devel
BuildRequires:  cmake(HighFive)
BuildRequires:  hdf5-devel
BuildRequires:  cmake(pybind11)
BuildRequires:  pybind11-devel

# Header-only libraries unbundled in %%prep; -static prescribed by guidelines
# for tracking of header-only libraries.
BuildRequires:  (cmake(nlohmann_json) with json-static)

# Test dependencies
# Tests don’t explicitly require pytest, but it’s a convenient runner.
BuildRequires:  %{py3_dist pytest}


%global _description %{expand:
C++ / Python reader for SONATA circuit files. SONATA guide:
https://github.com/AllenInstitute/sonata/blob/master/docs/SONATA_DEVELOPER_GUIDE.md
}

%description %_description


%package devel
Summary:        Development files for %{name}
License:        LGPL-3.0-only

Requires:       %{name}%{?_isa} = %{version}-%{release}

%description devel %_description


%package -n python3-libsonata
Summary:        %{summary}

%description -n python3-libsonata %_description


%prep
%autosetup -n libsonata-%{version} -S git


# Comment out to remove /usr/bin/env shebangs
# Can use something similar to correct/remove /usr/bin/python shebangs also
# find . -type f -name "*.py" -exec sed -i '/^#![  ]*\/usr\/bin\/env.*$/ d' {} 2>/dev/null ';'

cat pyproject.toml


%generate_buildrequires
%pyproject_buildrequires


%build
# Equivalent to passing -GNinja, but this way we can also affect CMake while it
# is building the Python extension.
export CMAKE_GENERATOR='Ninja'

# tests/CMakeLists.txt pulls Catch2 via FetchContent, but mock chroots have no
# network access. Ask FetchContent to try find_package() first, so the packaged
# cmake(Catch2) is used instead of cloning from GitHub.
%cmake \
    -DEXTLIB_FROM_SUBMODULES:BOOL=OFF \
    -DFETCHCONTENT_TRY_FIND_PACKAGE_MODE:STRING=ALWAYS \
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
# scikit-build-core re-runs CMake for the wheel without the options passed to
# %%cmake above, which would fall back to the extlib/fmt and python/pybind11
# submodules removed in %%prep. Forward the same options so the wheel build
# uses the system fmt and pybind11 instead.
export CMAKE_ARGS='-DEXTLIB_FROM_SUBMODULES:BOOL=OFF -DSONATA_CXX_WARNINGS:BOOL=OFF -DSONATA_VERSION="%{version}"'
%pyproject_wheel


%install
%cmake_install

# remove static lib
rm -rfv %{buildroot}/%{_libdir}/libsonata.a

%pyproject_install

# remove static lib
rm -fv %{buildroot}/%{python3_sitearch}/%{_lib}/libsonata.a

%pyproject_save_files -L libsonata


%check

# Skip known failing tests on s390x architecture
# These fail because of issues with the tests data that is included in the sources
# Filed upstream: https://github.com/openbraininstitute/libsonata/issues/73
%ifarch s390x
%ctest tests -E "NodePopulation|NodePopulationmatchAttributeValues|NodePopulationmatchAttributeValues|NodePopulationmatchAttributeValues|NodePopulationmatchAttributeValues|NodePopulationmatchAttributeValues|NodePopulationmatchAttributeValues|NodePopulationmatchAttributeValues|NodePopulationmatchAttributeValues|NodePopulationmatchAttributeValues|NodeSetBasic|NodeSetCompound"
%else
%ctest tests
%endif

# We need the contents of python/tests to be at a parallel path (same depth
# from the top-level directory), but we need to ensure that the tests cannot
# find an "un-built" copy of libsonata in the parent directory.
mkdir _empty
cp -rp python/tests _empty/
%ifarch s390x
%pytest -v _empty/tests -k "not (test_BasicScalarAnded or test_BasicScalarInt or test_BasicScalarString or test_NodeSetCompound or test_enumeration_values or test_get_attribute or test_get_dynamics_attribute or test_match_values or test_library_enumeration or test_extend)"
%else
%pytest -v _empty/tests
%endif


%files
%license COPYING.LESSER
%doc README.rst
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
%license COPYING.LESSER
%doc README.rst


%changelog
%autochangelog
