%bcond tests 1
%bcond rebuild_yaml_data 0
# Now that they are committed to the repository and not tracked as a git
# submodule, we might consider not packaging the “c4project” CMake scripts
# separately.
%bcond system_c4project 1

# Upstream defaults to C++11, but gtest 1.17.0 requires C++17 or later.
%global cxx_std 17

Name:           rapidyaml
Summary:        A library to parse and emit YAML, and do it fast
Version:        0.16.0
# This is derived from the version number. To prevent undetected SONAME version
# bumps, we nevertheless express it separately.
%global so_version 0.16
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

# cmake: fix test linking with c4core when using RYML_SYSTEM_C4CORE
# https://github.com/biojppm/rapidyaml/pull/653
Patch:          %{url}/pull/653.patch

BuildSystem:    cmake
# Disable RYML_FUZZ_TEST so that we do not have to include the contents of
# https://github.com/biojppm/rapidyaml-data (and document the licenses of the
# contents). We *could* do so, and add an additional source similar to the one
# for yaml-test-suite, but running these test cases downstream doesn’t seem
# important enough to bother.
BuildOption(conf): %{shrink:
    -DRYML_CXX_STANDARD=%{cxx_std}
    -DRYML_SYSTEM_C4CORE:BOOL=ON
    -DRYML_BUILD_BENCHMARKS:BOOL=OFF
    -DRYML_BUILD_TESTS:BOOL=%{?with_tests:ON}%{?!with_tests:OFF}
    -DRYML_FUZZ_DRIVERS:BOOL=OFF
    -DRYML_FUZZ_TEST:BOOL=OFF
    }

# https://fedoraproject.org/wiki/Changes/EncourageI686LeafRemoval
ExcludeArch:    %{ix86}

BuildRequires:  gcc-c++

# Minimum versions with major.minor SONAME versioning
%if %{with system_c4project}
BuildRequires:  c4project >= 0^20260717.2db9323-1
%endif
BuildRequires:  cmake(c4core) >= 0.6.0

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

%global common_description %{expand:
Rapid YAML, or ryml, for short. ryml is a C++ library to parse and emit YAML,
and do it fast, on everything from x64 to bare-metal chips without operating
system. (If you are looking to use your programs with a YAML tree as a
configuration tree with override facilities, take a look at c4conf).}

%description %{common_description}


%package devel
Summary:        Development files for Rapid YAML

Requires:       rapidyaml%{?_isa} = %{version}-%{release}
Requires:       c4core-devel%{?_isa}

%description devel %{common_description}

The rapidyaml-devel package contains libraries and header files for developing
applications that use Rapid YAML.


%prep
%autosetup -p1

# Remove/unbundle additional dependencies

%if %{with system_c4project}
# c4project (CMake build scripts)
rm --recursive --verbose proj/c4proj
cp --recursive --preserve '%{_datadir}/cmake/c4project' proj/c4proj
%endif
# Patch out download of gtest:
'%{SOURCE10}' 'proj/c4proj/c4Project.cmake' '^    if\(_GTEST\)' '^    endif'

# Patch out download of c4fs:
'%{SOURCE10}' 'ext/testbm.cmake' 'c4_download_remote_proj\(c4fs' '\)$'
'%{SOURCE10}' 'ext/testbm.cmake' 'c4_add_library\(c4fs' '\)$'
'%{SOURCE10}' 'ext/testbm.cmake' 'ryml_testbm_link_with_c4core\(c4fs' '\)$'

# Patch out download of c4log:
'%{SOURCE10}' 'ext/testbm.cmake' 'c4_download_remote_proj\(c4log' '\)$'
'%{SOURCE10}' 'ext/testbm.cmake' 'c4_add_library\(c4log' '\)$'
'%{SOURCE10}' 'ext/testbm.cmake' 'ryml_testbm_link_with_c4core\(c4log' '\)$'

# Patch out download of yaml-test-suite:
'%{SOURCE10}' 'test/CMakeLists.txt' \
    'c4_download_remote_proj\(yaml-test-suite' '\)$'
sed --regexp-extended --in-place \
    's@([[:blank:]]*)set\(tsdir.*\).*@&\nset\(suite_dir test/extern/yaml-test-suite\)\1@' \
    'test/CMakeLists.txt'
mkdir --parents 'test/extern/'

# Original sources (including LICENSE)
%setup -q -T -D -b 1 -n rapidyaml-%{version}

# Data in the form rapidyaml needs it
%setup -q -T -D -b 2 -n rapidyaml-%{version}
mv '../yaml-test-suite-data-%{yamltest_date}' 'test/extern/yaml-test-suite'


%conf -p
%if %{with rebuild_yaml_data}
# We need to rebuild the test data before running CMake configuration, since it
# checks to be sure it is present.
pushd ../yaml-test-suite-%{yamltest_date}
mkdir --parents data
perl bin/suite-to-data.pl src/*.yaml
popd
# Remove the pre-generated data from Source2 and replace it with the data we
# rebuilt from Source1.
rm --recursive --verbose test/extern/yaml-test-suite
mv ../yaml-test-suite-%{yamltest_date}/data test/extern/yaml-test-suite
%endif


%install -a
# We don’t believe this will be useful on Linux. See:
# https://docs.microsoft.com/en-us/windows/uwp/cpp-and-winrt-apis/natvis
rm '%{buildroot}%{_includedir}/ryml.natvis'
# In some kinds of installations, this would support a cmake uninstall target,
# but it’s not relevant for a system package.
rm '%{buildroot}%{_datadir}/ryml/MANIFEST.txt'
rmdir '%{buildroot}%{_datadir}/ryml'


%check
%if %{with tests}
%cmake_build --target ryml-test-run-verbose
%endif


%files
%license LICENSE.txt
%doc README.md
%{_libdir}/libryml.so.%{so_version}
%{_libdir}/libryml.so.%{version}


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
