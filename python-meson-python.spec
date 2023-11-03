%bcond tests 1

Name:           python-meson-python
Summary:        Meson Python build backend (PEP 517)
Version:        0.15.0
Release:        %autorelease

# SPDX
License:        MIT
URL:            https://github.com/mesonbuild/meson-python
Source:         %{pypi_source meson_python}

BuildArch:      noarch

BuildRequires:  python3-devel

%if %{with tests}
BuildRequires:  gcc
BuildRequires:  git-core
%endif

%global common_description %{expand:
meson-python is a Python build backend built on top of the Meson build system.
It enables to use Meson for the configuration and build steps of Python
packages. Meson is an open source build system meant to be both extremely fast,
and, even more importantly, as user friendly as possible. meson-python is best
suited for building Python packages containing extension modules implemented in
languages such as C, C++, Cython, Fortran, Pythran, or Rust. Consult the
documentation for more details.}

%description %{common_description}


%package -n     python3-meson-python
Summary:        %{summary}

# When patchelf is not in the PATH, mesonpy.get_requires_for_build_wheel() adds
# https://pypi.org/project/patchelf/ to the dependencies. We always want to use
# the system patchelf.
BuildRequires:  /usr/bin/patchelf
Requires:       /usr/bin/patchelf

# https://docs.fedoraproject.org/en-US/packaging-guidelines/Python/#_provides_for_importable_modules
%py_provides    python3-mesonpy

%description -n python3-meson-python %{common_description}


%prep
%autosetup -n meson_python-%{version}

# https://docs.fedoraproject.org/en-US/packaging-guidelines/Python/#_linters
sed -r -i "s/'pytest-cov/# &/" pyproject.toml


%generate_buildrequires
%pyproject_buildrequires -w %{?with_tests:-x test}


%build
%pyproject_wheel


%install
%pyproject_install
%pyproject_save_files mesonpy


%check
%if %{with tests}
# PEP 518 tests require network access.
# Note: tests are *not* safe for parallel execution with pytest-xdist.
%pytest --ignore=tests/test_pep518.py
%else
%pyproject_check_import
%endif


%files -n python3-meson-python -f %{pyproject_files}
# LICENSE duplicates LICENSES/MIT.txt. Currently, neither is automatically
# installed into the dist-info metadata directory.
%license LICENSES/*
%doc CHANGELOG.rst
%doc README.rst


%changelog
%autochangelog
