# Test data is stored in a separate git repository. We should always use the
# latest commit at the time of the release we are packaging.
%global stf_commit 7cc512a7c60361ebe1baf54991d7905efdc62aa0
%global stf_url https://github.com/fastfloat/supplemental_test_files

# Build and run exhaustive tests?
#
# These really do take a long time—at least an hour on the fastest machines,
# and over ten hours on s390x (affected also by limited parallelism). Some
# tests cover the entire single-precision domain, about four billion inputs.
# Still, we can finish before we hit any timeouts, and running the exhaustive
# tests brings peace of mind.
%bcond_without exhaustive

Name:           fast_float
Summary:        Fast & exact implementation of C++ from_chars for float/double
Version:        5.0.0
Release:        %autorelease

URL:            https://github.com/fastfloat/fast_float
# README.md:
#   Licensed under either of Apache License, Version 2.0 or MIT license or
#   BOOST license.
# Supplemental test files (Source1) are Apache-2.0 only (no MIT option); they
# do not contribute to the binary RPMs.
License:        Apache-2.0 OR MIT OR BSL-1.0

Source0:        %{url}/archive/v%{version}/fast_float-%{version}.tar.gz
Source1:        %{stf_url}/archive/%{stf_commit}/supplemental_test_files-%{stf_commit}.tar.gz

BuildRequires:  gcc-c++
BuildRequires:  cmake
# Our choice; the default make backend should work just as well
BuildRequires:  ninja-build

BuildRequires:  doctest-devel
# Doctest is header-only, so we must BR:
BuildRequires:  doctest-static

# No compiled binaries are installed, so this would be empty.
%global debug_package %{nil}

%global common_description %{expand:
The fast_float library provides fast header-only implementations for the C++
from_chars functions for float and double types. These functions convert ASCII
strings representing decimal values (e.g., 1.3e10) into binary types. We
provide exact rounding (including round to even). In our experience, these
fast_float functions many times faster than comparable number-parsing functions
from existing C++ standard libraries.}

%description %{common_description}


%package devel
Summary:        %{summary}

BuildArch:      noarch

# Header-only library
Provides:       fast_float-static = %{version}-%{release}

%description devel %{common_description}


%prep
%autosetup
%setup -q -T -D -b 1
# Compiling with -Werror makes sense for upstream CI, but is excessively strict
# for downstream builds across a variety of compiler versions.
sed -r -i 's/-Werror//' tests/CMakeLists.txt


%build
# Partially emulate the activity of FetchContent_Declare() in
# tests/CMakeLists.txt so that we can run the tests offline.
mkdir -p '%{_vpath_builddir}/_deps'
ln -s "${PWD}/../supplemental_test_files-%{stf_commit}/" \
    '%{_vpath_builddir}/_deps/supplemental_test_files-src'

%cmake \
    -GNinja \
    -DFETCHCONTENT_FULLY_DISCONNECTED:BOOL=ON \
    -DSYSTEM_DOCTEST:BOOL=ON \
    -DFASTFLOAT_TEST:BOOL=ON \
    -DFASTFLOAT_EXHAUSTIVE:BOOL=%{?with_exhaustive:ON}%{?!with_exhaustive:OFF}
%cmake_build


%install
%cmake_install


%check
%ctest


%files devel
%license LICENSE-APACHE
%license LICENSE-MIT
%license LICENSE-BOOST
%doc AUTHORS
%doc CONTRIBUTORS
%doc README.md

%{_includedir}/fast_float/

%{_datadir}/cmake/FastFloat/


%changelog
%autochangelog
