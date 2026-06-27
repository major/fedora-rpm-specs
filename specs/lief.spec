# Python API needs some more work
# - does not pick up the cmake configs
%bcond python 0
# ctest did not work properly
# - fail to build unittest
%bcond ctest  0

%global         soversion 0

%global         forgeurl0 https://github.com/lief-project/LIEF
%global         version0  %{soversion}.17.6
%global         tag0      %{version0}
%forgemeta

Name:           lief
Version:        %forgeversion -p
Release:        %autorelease
Summary:        Library to Instrument Executable Formats

# Main project is Apache-2.0
# Some bundled CMake files come from Kitware
# - cmake/ios.toolchain.cmake
SourceLicense:  Apache-2.0 AND BSD-3-Clause
License:        Apache-2.0

URL:            https://lief.re
Source:         %{forgesource0}

BuildRequires:  cmake
BuildRequires:  ninja-build
BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  json-devel
BuildRequires:  spdlog-devel
BuildRequires:  expected-devel
BuildRequires:  utf8cpp-devel
BuildRequires:  mbedtls-devel
BuildRequires:  frozen-devel
BuildRequires:  span-devel
BuildRequires:  catch-devel
%if %{with python}
BuildRequires:  python3-devel
BuildRequires:  python3-nanobind
%endif

%global _description %{expand:
The purpose of this project is to provide a cross-platform library to parse,
modify and abstract ELF, PE and MachO formats.}

%description %{_description}

%package devel
Summary:        Development files for lief
Requires:       lief = %{version}-%{release}

%description devel %{_description}

This package contains the development files.

%if %{with python}
%package -n python3-lief
Summary:        Python API for lief
Requires:       lief = %{version}-%{release}

%description -n python3-lief %{_description}

This package contains python API.
%endif


%prep
%forgeautosetup -p1
rm -rf third-party/*
%if %{with python}
# Unpin the python dependencies, these are used only for build, so if there is an issue, we will see it
pushd api/python
%pyproject_patch_dependency tomli:drop_constraints
%pyproject_patch_dependency scikit-build-core:drop_constraints
%pyproject_patch_dependency setuptools:drop_constraints
%pyproject_patch_dependency pydantic:drop_constraints
%pyproject_patch_dependency pathspec:drop_constraints
%pyproject_patch_dependency build:drop_constraints
%pyproject_patch_dependency wheel:drop_constraints
popd
%endif


%generate_buildrequires
%if %{with python}
pushd api/python > /dev/null
%pyproject_buildrequires
popd > /dev/null
%endif


%conf
%cmake \
  -G Ninja \
  -DCMAKE_BUILD_TYPE:STRING=RelWithDebInfo \
  -DFETCHCONTENT_TRY_FIND_PACKAGE_MODE:STRING=ALWAYS \
  -DLIEF_TESTS:BOOL=%{with ctest} \
  -DLIEF_EXAMPLES:BOOL=OFF \
  -DLIEF_C_API:BOOL=ON \
  -DLIEF_PYTHON_API:BOOL=OFF \
  -DLIEF_RUST_API:BOOL=OFF \
  -DLIEF_SO_VERSION:BOOL=ON \
  -DLIEF_LOGGING_DEBUG:BOOL=OFF \
  -DLIEF_USE_MELKOR:BOOL=OFF \
  -DLIEF_OPT_NLOHMANN_JSON_EXTERNAL:BOOL=ON \
  -DLIEF_EXTERNAL_SPDLOG:BOOL=ON \
  -DLIEF_OPT_EXTERNAL_EXPECTED:BOOl=ON \
  -DLIEF_OPT_UTFCPP_EXTERNAL:BOOL=ON \
  -DLIEF_OPT_MBEDTLS_EXTERNAL:BOOL=ON \
  -DLIEF_OPT_FROZEN_EXTERNAL:BOOL=ON \
  -DLIEF_OPT_EXTERNAL_SPAN:BOOL=ON


%build
%cmake_build

%if %{with python}
build_dir=$(pwd)/%_vpath_builddir
pushd api/python
%{pyproject_wheel %{shrink:
  -C cmake.build-type=RelWithDebInfo
  -C cmake.define.LIEF_ROOT=${build_dir}
  -C cmake.define.LIEF_EXTERNAL_NANOBIND=true
  -C cmake.define.LIEF_PY_LIEF_EXT=true
  -C cmake.define.LIEF_PY_LIEF_EXT_SHARED=true
}}
popd
%endif


%install
%cmake_install
%if %{with python}
pushd api/python
%pyproject_install
%pyproject_save_files -l lief
popd
%endif


%check
%if %{with ctest}
%ctest
%endif


%files
%license LICENSE
%{_libdir}/libLIEF.so.%{soversion}
%{_libdir}/libLIEF.so.%{soversion}.*

%files devel
%{_includedir}/LIEF
%{_libdir}/pkgconfig/LIEF.pc
%{_libdir}/cmake/LIEF
%{_libdir}/libLIEF.so

%if %{with python}
%files -n python3-lief -f %{pyproject_files}
%endif


%changelog
%autochangelog
