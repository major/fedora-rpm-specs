%bcond_without test_example

Name:           python-cmake-build-extension
Version:        0.5.1
Release:        %autorelease
Summary:        Setuptools extension to build and package CMake projects

# The entire source is MIT, except example/bindings_swig/numpy.i, which is BSD.
License:        MIT and BSD
URL:            https://github.com/diegoferigo/cmake-build-extension
Source0:        %{pypi_source cmake-build-extension}

BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  cmake
BuildRequires:  ninja-build

%if %{with test_example}
BuildRequires:  gcc
BuildRequires:  gcc-c++

BuildRequires:  swig
# Even though pybind11 and eigen3 are  header-only, we don’t need to BR:
# pybind11-static nor eigen3-static, because nothing we install is built with
# them; they are only used for test-building the example.
BuildRequires:  cmake(pybind11)
BuildRequires:  cmake(Eigen3)

BuildRequires:  python3dist(pytest)
%endif

%global common_description %{expand:
This project aims to simplify the integration of C++ projects based on CMake
with Python packaging tools. CMake provides out-of-the-box support to either
SWIG and pybind11, that are two among the most used projects to create Python
bindings from C++ sources.

If you have any experience with these hybrid projects, you know the challenges
to make packaging right! This project takes inspiration from pre-existing
examples (pybind/cmake_example, among many others) and provides a simple,
flexible, and reusable setuptools extension with the following features:

  • Bridge between CMake projects and Python packaging.
  • Configure and build the CMake project from setup.py.
  • Install the CMake project in the resulting Python package.
  • Allow passing custom CMake options.
  • Allow creating a top-level __init__.py.
  • Expose C++ executables to the Python environment.
  • Provide a context manager to import reliably CPython modules on all major
    OSs.
  • Disable the C++ extension in editable installations (requiring to manually
    call CMake to install the C++ project).}

%description %{common_description}


%package -n python3-cmake-build-extension
Summary:        %{summary}

# Since this subpackage does not contain the example project, it has no
# BSD-licensed sources.
License:        MIT

Requires:       cmake
Requires:       ninja-build

%description -n python3-cmake-build-extension %{common_description}


%package -n python3-cmake-build-extension-doc
Summary:        Documentation and examples for cmake-build-extension

Requires:       python3-cmake-build-extension = %{version}-%{release}

%description -n python3-cmake-build-extension-doc %{common_description}


%prep
%autosetup -n cmake-build-extension-%{version} -p1

# We use the system cmake and ninja-build packages in lieu of the PyPI “cmake”
# and “ninja” distributions, respectively.
sed -r -i '/^[[:blank:]]*\b(cmake|ninja)\b[[:blank:]]*$/d' setup.cfg

%if %{with test_example}
# Keep the original example/ “clean” so we can install it as documentation;
# make a copy to test-build.
cp -rp example test_example
%endif


%generate_buildrequires
%pyproject_buildrequires
%if %{with test_example}
(
  cd test_example >/dev/null
  # For an unknown reason, “-x test” does not generate the appropriate BR’s
  # here. Furthermore, python3dist(pytest-icdiff) is not packaged, so we would
  # have to patch it out anyway. We just use manual BR’s for the example’s
  # tests instead.
  %pyproject_buildrequires
) | grep -Ev 'cmake-build-extension'
%endif


%build
%pyproject_wheel


%install
%pyproject_install
%pyproject_save_files cmake_build_extension


%check
# We choose to do an import “smoke test” even when we are test-building the
# example.
%pyproject_check_import

%if %{with test_example}
# Build the example project and run its tests (but do not install any compiled
# extensions as part of our RPM!)
pushd test_example >/dev/null
export PYTHONPATH='%{buildroot}%{python3_sitelib}'
%pyproject_wheel

PPBL="%{pyproject_build_lib}"
export PYTHONPATH="${PYTHONPATH}:${PPBL}"
for pathpart in $(echo "${PPBL}" | tr ':' ' ')
do
  PATH="${PATH}:${pathpart}/mymath_pybind11/bin"
  PATH="${PATH}:${pathpart}/mymath_swig/bin"
  export PATH
  find "${pathpart}" -type f -perm /0111
done
%pytest
popd >/dev/null
%endif


%files -n python3-cmake-build-extension -f %{pyproject_files}
# pyproject_files handles LICENSE; verify with “rpm -qL -p …”


%files -n python3-cmake-build-extension-doc
%doc README.md
%doc example/


%changelog
%autochangelog
