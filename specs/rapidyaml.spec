%bcond tests 1
%bcond rebuild_yaml_data 0

# Upstream defaults to C++11, but gtest 1.17.0 requires C++17 or later.
%global cxx_std 17

Name:           rapidyaml
Summary:        A library to parse and emit YAML, and do it fast
Version:        0.11.1
# This is the same as the version number. To prevent undetected soversion
# bumps, we nevertheless express it separately.
%global so_version 0.11.1
Release:        %autorelease

# SPDX
License:        MIT
URL:            https://github.com/biojppm/rapidyaml
Source0:        %{url}/archive/v%{version}/rapidyaml-%{version}.tar.gz
# Read this from the unpatched original test/CMakeLists.txt:
#   c4_download_remote_proj(yaml-test-suite … GIT_TAG <USE THIS>)
%global yamltest_url https://github.com/yaml/yaml-test-suite
%global yamltest_date 2022-01-17
# Data for testing the correctness of YAML processors. This is used only for
# testing; it is not bundled in the binary RPMs. This is “are available in 2
# forms. Files in the src directory encode all the data for YAML using YAML.
# The data from these tests is also available in a form where each test has its
# own directory.” We use the latter form, but the former is the original source
# and contains the (MIT) LICENSE file.
# Data for testing the correctness of YAML processors. This is used only for
Source1:        %{yamltest_url}/archive/data-%{yamltest_date}/yaml-test-suite-data-%{yamltest_date}.tar.gz
Source2:        %{yamltest_url}/archive/v%{yamltest_date}/yaml-test-suite-%{yamltest_date}.tar.gz
# Helper script to patch out unconditional download of dependencies in CMake
Source10:       patch-no-download

# https://fedoraproject.org/wiki/Changes/EncourageI686LeafRemoval
ExcludeArch:    %{ix86}

BuildRequires:  gcc-c++
BuildRequires:  cmake
# Minimum version with proper multilib (GNUInstallDirs) support
BuildRequires:  c4project >= 0^20260428.fa85cab-1
# CMake builds in Fedora now use the ninja backend by default, but the Python
# extension build unconditionally uses ninja, so we’re explicit:
BuildRequires:  ninja-build

BuildRequires:  cmake(c4core) >= 0.2.10

%if %{with tests}
BuildRequires:  cmake(c4fs)
BuildRequires:  cmake(c4log)
BuildRequires:  cmake(gtest)
%endif

# A Python 3 interpreter is required unconditionally for the patch-no-download
# script.
BuildRequires:  python3-devel
# The Python bindings, https://pypi.org/project/rapidyaml/, were moved to a
# separate repository, https://github.com/biojppm/rapidyaml-python, as of
# rapidyaml 0.11.1. Since python3-rapidyaml was a leaf (sub)package in Fedora,
# we have dropped it beginning with Fedora 45. This upgrade path can be removed
# after Fedora 47. If it turns out that the Python bindings are needed for
# something in the future, then they should be submitted and reviewed as a
# separate python-rapidyaml source package.
Obsoletes:      python3-rapidyaml < 0.11.1-1

%if %{with rebuild_yaml_data}
# See bin/suite-to-data in Source1.
BuildRequires:  bash >= 4.4
BuildRequires:  perl >= 5.28
BuildRequires:  perl(YAML::PP) >= 0.030
%endif

%global common_description %{expand: \
Rapid YAML, or ryml, for short. ryml is a C++ library to parse and emit YAML,
and do it fast, on everything from x64 to bare-metal chips without operating
system. (If you are looking to use your programs with a YAML tree as a
configuration tree with override facilities, take a look at c4conf).}

%description
%{common_description}


%package devel
Summary:        Development files for Rapid YAML

Requires:       rapidyaml%{?_isa} = %{version}-%{release}
Requires:       c4core-devel%{?_isa}
# https://docs.fedoraproject.org/en-US/packaging-guidelines/Conflicts/#_compat_package_conflicts
Conflicts:      rapidyaml0.10.0-devel

%description devel
%{common_description}

The rapidyaml-devel package contains libraries and header files for developing
applications that use Rapid YAML.


%prep
%autosetup -p1

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

# Patch out download of c4fs:
'%{SOURCE10}' 'ext/testbm.cmake' 'c4_download_remote_proj\(c4fs' '\)$'
'%{SOURCE10}' 'ext/testbm.cmake' 'c4_add_library\(c4fs' '\)$'

# Patch out download of c4log
'%{SOURCE10}' 'test/CMakeLists.txt' \
    'c4_require_subproject\(c4(log)' '\)$'

# Patch out download of yaml-test-suite:
'%{SOURCE10}' 'test/CMakeLists.txt' \
    'c4_download_remote_proj\(yaml-test-suite' '\)$'
sed -r -i \
    's@([[:blank:]]*)set\(tsdir.*\).*@&\nset\(suite_dir test/extern/yaml-test-suite\)\1@' \
    'test/CMakeLists.txt'
mkdir -p 'test/extern/'

# Original sources (including LICENSE)
%setup -q -T -D -b 1 -n rapidyaml-%{version}

# Data in the form rapidyaml needs it
%setup -q -T -D -b 2 -n rapidyaml-%{version}
mv '../yaml-test-suite-data-%{yamltest_date}' 'test/extern/yaml-test-suite'


%conf
%if %{with rebuild_yaml_data}
# We need to rebuild the test data before running CMake configuration, since it
# checks to be sure it is present.
pushd ../yaml-test-suite-%{yamltest_date}
mkdir -p data
perl bin/suite-to-data.pl src/*.yaml
popd
# Remove the pre-generated data from Source2 and replace it with the data we
# rebuilt from Source1.
rm -rv test/extern/yaml-test-suite
mv ../yaml-test-suite-%{yamltest_date}/data test/extern/yaml-test-suite
%endif

# Disable RYML_TEST_FUZZ so that we do not have to include the contents of
# https://github.com/biojppm/rapidyaml-data (and document the licenses of the
# contents). We *could* do so, and add an additional source similar to the one
# for yaml-test-suite, but running these test cases downstream doesn’t seem
# important enough to bother.
%cmake -GNinja \
    -DRYML_CXX_STANDARD=%{cxx_std} \
    -DRYML_BUILD_TESTS:BOOL=%{?with_tests:ON}%{?!with_tests:OFF} \
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
#
# TODO: Why was this not fixed by https://github.com/biojppm/cmake/pull/16,
# which worked for c4core?
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
%if %{with tests}
%cmake_build --target ryml-test-run-verbose
%endif


%files
%license LICENSE.txt
%doc README.md
%{_libdir}/libryml.so.%{so_version}


%files devel
%{_includedir}/ryml.hpp
%{_includedir}/ryml_std.hpp
# %%{_includedir}/c4 is owned by c4core-devel, upon which this package depends
%{_includedir}/c4/yml/

%{_libdir}/libryml.so

%dir %{_libdir}/cmake/ryml
%{_libdir}/cmake/ryml/*.cmake


%changelog
%autochangelog
