# While the headers are architecture independent, the package must be
# built separately on all architectures so that the tests are run
# properly. See also
# https://fedoraproject.org/wiki/Packaging:Guidelines#Packaging_Header_Only_Libraries
%global debug_package %{nil}

# Whether to run additional tests, enabled by default
%bcond optional_tests 1


Name:    pybind11
Version: 3.0
Release: %autorelease
Summary: Seamless operability between C++11 and Python
License: BSD-3-Clause
URL:	 https://github.com/pybind/pybind11
Source0: https://github.com/pybind/pybind11/archive/v%{version}/%{name}-%{version}.tar.gz

# Use the `/usr` prefix for the python commands
Patch1:  pybind11-2.13.6-Use_usr_prefix.patch
# tomlkit is only used when creating an upstream package
# https://github.com/pybind/pybind11/pull/5990
Patch2:  pybind11-3.0-tomlkit-dep.patch

# Needed to build the python libraries
BuildRequires: python3-devel

BuildRequires: gcc-c++
BuildRequires: cmake

# Additional optional test dependencies
%if %{with optional_tests}
# The dependencies from test/requirements.txt do not cover arbitrary python version
# Other source of the extra test depenenecies is not provided
BuildRequires: python3dist(scipy)
BuildRequires: python3dist(numpy)
# Note, normally numpy dependency is still injected due to boost-devel (rhbz#2392860) 
# For some reason boost-devel does not provide cmake(Boost) (rhbz#2407049)
BuildRequires: boost-devel
%endif

# Other test dependencies
BuildRequires: cmake(Eigen3)
BuildRequires: cmake(Catch2)

%global base_description \
pybind11 is a lightweight header-only library that exposes C++ types \
in Python and vice versa, mainly to create Python bindings of existing \
C++ code.

%description
%{base_description}

%package devel
Summary:  Development headers for pybind11
# https://fedoraproject.org/wiki/Packaging:Guidelines#Packaging_Header_Only_Libraries
Provides: %{name}-static = %{version}-%{release}

%description devel
%{base_description}

This package contains the development headers for pybind11.

%package -n     python3-%{name}
Summary:        %{summary}

Requires: %{name}-devel%{?_isa} = %{version}-%{release}

%description -n python3-%{name}
%{base_description}

This package contains the Python 3 files.

%prep
%autosetup -p1


%generate_buildrequires
%pyproject_buildrequires -g test


%build
# Have to build twice:
# - CMake: install into system paths
# - pyproject: install python metadata without the source files
%cmake \
  -DCMAKE_BUILD_TYPE:STRING=Release \
  -DUSE_PYTHON_INCLUDE_DIR=FALSE
%cmake_build
%{pyproject_wheel %{shrink:
  -C cmake.build-type=Release
  -C cmake.define.PYBIND11_INSTALL=OFF
  -C cmake.define.PYBIND11_TEST=OFF
}}


%install
%cmake_install
%pyproject_install
%pyproject_save_files -l pybind11


%check
# The project does not provide ctest or running pytest directly
# Additional tests from optional_tests are automatically skipped/picked-up by pytest
%cmake_build --target check


%files devel
%license LICENSE
%doc README.rst
%{_includedir}/pybind11/
%{_datadir}/cmake/pybind11/
%{_bindir}/pybind11-config
%{_datadir}/pkgconfig/%{name}.pc

%files -n python3-%{name} -f %{pyproject_files}


%changelog
%autochangelog
