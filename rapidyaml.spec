%bcond_without tests
%bcond_without python

# Upstream defaults to C++11, but gtest 1.13.0 requires C++14 or later.
%global cxx_std 14

Name:           rapidyaml
Summary:        A library to parse and emit YAML, and do it fast
Version:        0.5.0
# This is the same as the version number. To prevent undetected soversion
# bumps, we nevertheless express it separately.
%global so_version 0.5.0
Release:        %autorelease

# SPDX
License:        MIT
URL:            https://github.com/biojppm/rapidyaml
Source0:        %{url}/archive/v%{version}/rapidyaml-%{version}.tar.gz
# Read this from the unpatched original test/CMakeLists.txt:
#   c4_download_remote_proj(yaml-test-suite … GIT_TAG <USE THIS>)
%global yamltest_url https://github.com/yaml/yaml-test-suite
%global yamltest_tag data-2022-01-17
# Data for testing the correctness of YAML processors. This is used only for
# testing; it is not bundled in the binary RPMs.
Source1:        %{yamltest_url}/archive/%{yamltest_tag}/yaml-test-suite-%{yamltest_tag}.tar.gz
# Helper script to patch out unconditional download of dependencies in CMake
Source10:       patch-no-download

# [fix] Add missing Python runtime dep. on deprecation
# https://github.com/biojppm/rapidyaml/pull/347
Patch:          %{url}/pull/347.patch

BuildRequires:  gcc-c++
BuildRequires:  cmake
BuildRequires:  c4project
# Our choice—the default make backend should work just as well—but note that
# the Python extension build unconditionally uses ninja.
BuildRequires:  ninja-build

BuildRequires:  cmake(c4core)

%if %{with tests}
BuildRequires:  cmake(c4fs)
BuildRequires:  cmake(c4log)
BuildRequires:  cmake(gtest)
%endif

# A Python 3 interpreter is required unconditionally for the patch-no-download
# script.
BuildRequires:  python3-devel
%if %{with python}
BuildRequires:  swig
BuildRequires:  python3dist(pytest)
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

%description devel
%{common_description}

The rapidyaml-devel package contains libraries and header files for developing
applications that use Rapid YAML.


%if %{with python}
%package -n python3-rapidyaml
Summary:        %{summary}

# The Python extension contains its own statically linked copy of rapidyaml
# (acceptable since both are built from the same source RPM), so we don’t need
# to depend on the base package. It would be nice—for installation size
# savings, if nothing else—if we could link dynamically against base package’s
# shared library, but upstream’s build system doesn’t make this very practical.

%description -n python3-rapidyaml
%{common_description}

The python3-rapidyaml package contains Python bindings for Rapid YAML.
%endif


%prep
%autosetup

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

# Patch out downlaod of c4fs:
'%{SOURCE10}' 'ext/testbm.cmake' 'c4_require_subproject\(c4fs' '\)$'

# Patch out download of c4log
'%{SOURCE10}' 'test/CMakeLists.txt' \
    'c4_download_remote_proj\(yaml-test-suite' '\)$'

# Patch out download of yaml-test-suite:
'%{SOURCE10}' 'test/CMakeLists.txt' \
    'c4_require_subproject\(c4(log)' '\)$'
sed -r -i \
    's@([[:blank:]]*)set\(tsdir.*\).*@&\nset\(suite_dir test/extern/yaml-test-suite\)\1@' \
    'test/CMakeLists.txt'
%setup -q -T -D -b 1 -n rapidyaml-%{version}
mkdir -p 'test/extern/'
mv '../yaml-test-suite-%{yamltest_tag}' 'test/extern/yaml-test-suite'

# We use the system ninja-build package rather than the PyPI ninja
# distribution.
sed -r -i '/^[[:blank:]]*"ninja",[[:blank:]]*$/d' pyproject.toml

# Link the unbundled c4core from the Python SWIG wrapper extension.
sed -r -i 's/\b(swig_link_libraries\(.*)\)/\1 c4core\)/' \
    api/CMakeLists.txt

# We don’t really need python-setuptools_git, and it’s not packaged in the
# EPELs, so there is a benefit to patching it out.
sed -r -i '/setuptools-git/d' requirements.txt pyproject.toml setup.py


%if %{with python}
%generate_buildrequires
export SETUPTOOLS_SCM_PRETEND_VERSION='%{version}'
%pyproject_buildrequires
%endif


%build
%set_build_flags
export SETUPTOOLS_SCM_PRETEND_VERSION='%{version}'

%cmake -GNinja \
    -DRYML_CXX_STANDARD=%{cxx_std} \
    -DRYML_BUILD_TESTS:BOOL=%{?with_tests:ON}%{?!with_tests:OFF}
%cmake_build

%if %{with python}
# We could set -DRYML_BUILD_API_PYTHON:BOOL=ON in the library build above, but
# the resulting ryml.py and _ryml.so would be installed in the wrong place and
# without necessary metadata. Instead we rebuild the library indirectly via the
# usual Python tooling to get the Python bindings.

# Here we can apply any necessary CMake flags from the definition of %%cmake in
# %%{_rpmmacrodir}/macros.cmake. It’s not clear that there is any reasonable
# way to do this automatically without using %%cmake. Additonally, we must make
# some adjustments:
#
# - Do an in-source build (no -S and -B options) because things break if we try
#   to do an out-of-source build. This is just as well: the main library build
#   is out-of-source, so this in-source build will not clobber it.
# - Do not set CMAKE_INSTALL_PREFIX, because this is set in setup.py to the
#   Python package directory, i.e., %%{python3_sitearch/ryml, and overriding it
#   will only break things. Similarly, we needn’t bother setting
#   INCLUDE_INSTALL_DIR, LIB_INSTALL_DIR, SYSCONF_INSTALL_DIR, or any other
#   paths; nothing will be installed there, and fiddling with them can do no
#   good in this case.
# - For conciseness, we refrain from setting flags specific to C and Fortran
#   and flags for the “UNIX Makefiles” backend.
# - We omit CMAKE_INSTALL_DO_STRIP, which is not used here.
#
# Not much is left!
CF="${CF-} -DCMAKE_CXX_FLAGS_RELEASE:STRING='-DNDEBUG'"
CF="${CF-} %{?_cmake_shared_libs}"

CF="${CF-} -DRYML_CXX_STANDARD=%{cxx_std}"
CF="${CF-} -DRYML_BUILD_TESTS:BOOL=%{?with_tests:ON}%{?!with_tests:OFF}"
export CMAKE_FLAGS="${CF}"
# We can’t easily pass options to the CMake build invocation, but we can
# control it somewhat with environment variables:
# https://cmake.org/cmake/help/latest/manual/cmake-env-variables.7.html
export VERBOSE=''
export CMAKE_BUILD_PARALLEL_LEVEL='%{_smp_build_ncpus}'
%pyproject_wheel
%endif


%install
export SETUPTOOLS_SCM_PRETEND_VERSION='%{version}'
%cmake_install

# Fix wrong installation paths for multilib; it would be nontrivial to patch
# the source to get this right in the first place.
if [ '%{_libdir}' != '%{_prefix}/lib' ]
then
  mkdir -p '%{buildroot}%{_libdir}'
  mv -v %{buildroot}%{_prefix}/lib/libryml.so* '%{buildroot}%{_libdir}/'
  mkdir -p '%{buildroot}%{_libdir}/cmake'
  mv -v %{buildroot}%{_prefix}/lib/cmake/ryml '%{buildroot}%{_libdir}/cmake/'
fi

# We don’t believe this will be useful on Linux. See:
# https://docs.microsoft.com/en-us/windows/uwp/cpp-and-winrt-apis/natvis
rm -vf '%{buildroot}%{_includedir}/ryml.natvis'

%if %{with python}
%pyproject_install
%pyproject_save_files ryml
%endif



%check
%if %{with tests}
%cmake_build --target ryml-test-run-verbose
%if %{with python}
%pytest -v
%endif
%else
%if %{with python}
%pyproject_check_import
%endif
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


%if %{with python}
%files -n python3-rapidyaml -f %{pyproject_files}
# pyproject_files takes care of LICENSE.txt; verify with “rpm -qL -p …”
%doc README.md
%endif


%changelog
%autochangelog
