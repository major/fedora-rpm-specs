# Upstream defaults to C++11, but gtest 1.17.0 requires C++17 or later.
# Even though we don’t build tests in this compat package, we keep using the
# same C++ standard as the base rapidyaml package and as the c4core0.2.8 compat
# package, which *does* build tests.
%global cxx_std 17

Name:           rapidyaml0.10.0
Summary:        A library to parse and emit YAML, and do it fast
Version:        0.10.0
# This is the same as the version number. To prevent undetected soversion
# bumps, we nevertheless express it separately.
%global so_version 0.10.0
Release:        %autorelease

# SPDX
License:        MIT
URL:            https://github.com/biojppm/rapidyaml
Source0:        %{url}/archive/v%{version}/rapidyaml-%{version}.tar.gz
# Helper script to patch out unconditional download of dependencies in CMake
Source10:       patch-no-download

# c4_project(): ensure RYML_VERSION is set
# https://github.com/biojppm/rapidyaml/commit/1173e113180a652f9ad5744f8dccdbee58c730ef
#
# Fixes:
#
# - rymlConfig.cmake doesn't set version string
#   https://bugzilla.redhat.com/show_bug.cgi?id=2451572
# - In rymlConfig.cmake, RYML_VERSION is not set from the project version
#   https://github.com/biojppm/rapidyaml/issues/584
#
# This is just the CMakeLists.txt change, not the changelog entry or the c4core
# submodule update.
Patch:          rapidyaml-0.11.0-set-RYML_VERSION.patch

# https://fedoraproject.org/wiki/Changes/EncourageI686LeafRemoval
ExcludeArch:    %{ix86}

BuildRequires:  gcc-c++
BuildRequires:  cmake
# Minimum version with fix to ensure ${upper_prefix}_VERSION is set, eg
# RYML_VERSION or C4CORE_VERSION.
BuildRequires:  c4project >= 0^20260326.1e65b7b-1
# CMake builds in Fedora now use the ninja backend by default, but the Python
# extension build unconditionally uses ninja, so we’re explicit:
BuildRequires:  ninja-build

BuildRequires:  c4core0.2.8-devel

# A Python 3 interpreter is required unconditionally for the patch-no-download
# script.
BuildRequires:  python3-devel

%global common_description %{expand: \
Rapid YAML, or ryml, for short. ryml is a C++ library to parse and emit YAML,
and do it fast, on everything from x64 to bare-metal chips without operating
system. (If you are looking to use your programs with a YAML tree as a
configuration tree with override facilities, take a look at c4conf).}

%description
%{common_description}


%package devel
Summary:        Development files for Rapid YAML

Requires:       %{name}%{?_isa} = %{version}-%{release}
# https://docs.fedoraproject.org/en-US/packaging-guidelines/Conflicts/#_compat_package_conflicts
Conflicts:      rapidyaml-devel
Requires:       c4core0.2.8-devel%{?_isa}

%description devel
%{common_description}

The rapidyaml-devel package contains libraries and header files for developing
applications that use Rapid YAML.


%prep
%autosetup -n rapidyaml-%{version} -p1

# Remove/unbundle additional dependencies

# c4project (CMake build scripts)
rm -rvf ext/c4core/cmake
cp -rvp %{_datadir}/cmake/c4project ext/c4core/cmake
# Patch out download of gtest:
'%{SOURCE10}' 'ext/c4core/cmake/c4Project.cmake' \
    '^    if\(_GTEST\)' '^    endif'

# Patch out download of c4core:
'%{SOURCE10}' 'CMakeLists.txt' 'c4_require_subproject\(c4core' '\)$'
# Use external c4core
sed -r -i '/INCORPORATE c4core/d' 'CMakeLists.txt'


%conf
# Disable RYML_TEST_FUZZ so that we do not have to include the contents of
# https://github.com/biojppm/rapidyaml-data (and document the licenses of the
# contents). We *could* do so, and add an additional source similar to the one
# for yaml-test-suite, but running these test cases downstream doesn’t seem
# important enough to bother.
%cmake \
    -DRYML_CXX_STANDARD=%{cxx_std} \
    -DRYML_BUILD_TESTS:BOOL=OFF \
    -DRYML_TEST_FUZZ:BOOL=OFF


%build
%cmake_build


%install
%cmake_install

# Fix wrong installation paths for multilib; it would be nontrivial to patch
# the source to get this right in the first place. The installation path is
# determined by the scripts in https://github.com/biojppm/cmake, packaged as
# c4project.
#
# Installation directory on Linux 64bit OS
# https://github.com/biojppm/rapidyaml/issues/256
if [ '%{_libdir}' != '%{_prefix}/lib' ]
then
  mkdir -p '%{buildroot}%{_libdir}'
  mv -v %{buildroot}%{_prefix}/lib/libryml.so* '%{buildroot}%{_libdir}/'
  mkdir -p '%{buildroot}%{_libdir}/cmake'
  mv -v %{buildroot}%{_prefix}/lib/cmake/ryml '%{buildroot}%{_libdir}/cmake/'
  find %{buildroot}%{_libdir}/cmake/ryml -type f -name '*.cmake' -print0 |
    xargs -r -t -0 sed -r -i "s@/lib/@/$(basename '%{_libdir}')/@"
fi

# We don’t believe this will be useful on Linux. See:
# https://docs.microsoft.com/en-us/windows/uwp/cpp-and-winrt-apis/natvis
rm -vf '%{buildroot}%{_includedir}/ryml.natvis'


%check
# We do not attempt to build and run the tests in this compat package because
# we want to avoid needing compat versions of c4fs and c4log, built against the
# c4core0.2.8 compat package. Not only would this be two more compat packages
# to maintain, but it would be awkward to name them since they are
# snapshot-versioned.


%files
%license LICENSE.txt
%doc README.md
%{_libdir}/libryml.so.%{so_version}


%files devel
%{_includedir}/ryml.hpp
%{_includedir}/ryml_std.hpp
# %%{_includedir}/c4 is owned by c4core0.2.8-devel, upon which this package depends
%{_includedir}/c4/yml/

%{_libdir}/libryml.so

%dir %{_libdir}/cmake/ryml
%{_libdir}/cmake/ryml/*.cmake


%changelog
%autochangelog
