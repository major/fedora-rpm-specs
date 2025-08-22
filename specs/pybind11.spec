# While the headers are architecture independent, the package must be
# built separately on all architectures so that the tests are run
# properly. See also
# https://fedoraproject.org/wiki/Packaging:Guidelines#Packaging_Header_Only_Libraries
%global debug_package %{nil}

# Whether to run the tests, enabled by default
%bcond tests 1

Name:    pybind11
Version: 2.13.6
Release: %autorelease
Summary: Seamless operability between C++11 and Python
License: BSD-3-Clause
URL:	 https://github.com/pybind/pybind11
Source0: https://github.com/pybind/pybind11/archive/v%{version}/%{name}-%{version}.tar.gz

# Use the `/usr` prefix for the python commands
Patch1:  pybind11-2.13.6-Use_usr_prefix.patch
# Drop cmake and ninja from build-requires
Patch2:  pybind11-2.13.6-Drop_some_build-requires.patch

# Needed to build the python libraries
BuildRequires: python3-devel
# Test depdendencies are not exposed
%if %{with tests}
BuildRequires: python3-pytest
BuildRequires: python3-numpy
BuildRequires: python3-scipy
%endif

BuildRequires: eigen3-devel
BuildRequires: gcc-c++
BuildRequires: cmake

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
%pyproject_buildrequires


%build
# Build with CMake first to install the devel files in OS native paths
# When -DCMAKE_BUILD_TYPE is set to Release, the tests in %%check might segfault.
# However, we do not ship any binaries, and therefore Debug
# build type does not affect the results.
# https://bugzilla.redhat.com/show_bug.cgi?id=1921199
%cmake \
  -DCMAKE_BUILD_TYPE=Debug \
  %{!?with_tests:-DPYBIND11_TEST=OFF} \
  -DUSE_PYTHON_INCLUDE_DIR=FALSE
%cmake_build

# Build again with the python build system to get the python files
%pyproject_wheel


%install
%cmake_install
%pyproject_install
%pyproject_save_files pybind11

# Remove the devel files in the python package
rm -rf %{buildroot}%{python3_sitelib}/pybind11/include/
rm -rf %{buildroot}%{python3_sitelib}/pybind11/share/
sed -i '/pybind11\/include/d' %{pyproject_files}
sed -i '/pybind11\/share/d' %{pyproject_files}


%if %{with tests}
%check
%ctest
%endif


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
