%bcond tests 1
# The python-pytest-mock and wheel dependencies are unwanted on RHEL;
# we can omit them and still run most of the tests.
%bcond pytest_mock %{undefined rhel}
%bcond wheel %{undefined rhel}
# RHEL will not have patchelf (which is used for adjusting RPATH in shared
# libraries bundled in wheels); that is OK because the package is
# buildroot-only there and the packages built with python-meson-python will not
# bundle shared libraries. In Fedora and EPEL, we must depend on patchelf to
# ship a full-featured package.
%bcond patchelf %{expr:%{undefined rhel} || %{defined epel}}

Name:           python-meson-python
Summary:        Meson Python build backend (PEP 517)
Version:        0.18.0
Release:        %autorelease

# SPDX
License:        MIT
URL:            https://github.com/mesonbuild/meson-python
Source:         %{pypi_source meson_python}

# Downstream-only patch to remove the patchelf dependency (and corresponding
# functionality), controlled by the patchelf build conditional
Patch100:       meson-python-0.18.0-remove-patchelf.patch

BuildSystem:            pyproject
BuildOption(generate_buildrequires): -p %{?with_tests:-x test}
# LICENSE duplicates LICENSES/MIT.txt, which is handled automatically.
BuildOption(install):   -l mesonpy

BuildArch:      noarch

# for %%pyproject_buildrequires -p
BuildRequires:  pyproject-rpm-macros >= 1.15.1

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
%if %{with patchelf}
BuildRequires:  /usr/bin/patchelf
Requires:       /usr/bin/patchelf
%endif

# https://docs.fedoraproject.org/en-US/packaging-guidelines/Python/#_provides_for_importable_modules
%py_provides    python3-mesonpy

%description -n python3-meson-python %{common_description}


%prep
# We need “-S git” because test_reproducible uses “meson dist,” which only
# works in a git or mercurial repo.
%autosetup -n meson_python-%{version} -N -S git
%autopatch -M 99 -p1
%if %{without patchelf}
%patch 100 -p1
%endif
# build: used only by skipped PEP 518 test
# pytest-cov: https://docs.fedoraproject.org/en-US/packaging-guidelines/Python/#_linters
sed -r -i "s/^  '(build|pytest-cov)/#&/" pyproject.toml
%if %{without pytest_mock}
sed -r -i "s/^  '(pytest-mock)/#&/" pyproject.toml
%endif
%if %{without wheel}
sed -r -i "s/^  '(wheel)/#&/" pyproject.toml
%endif


%check -a
%if %{with tests}
# Note: tests are *not* safe for parallel execution with pytest-xdist.

# PEP 518 tests require network access.
ignore="${ignore-} --ignore=tests/test_pep518.py"

%if %{without pytest_mock}
k="${k-}${k+ and }not test_invalid_build_dir"
k="${k-}${k+ and }not test_use_ansi_escapes"
%endif
%if %{without wheel}
ignore="${ignore-} --ignore=tests/test_editable.py"
ignore="${ignore-} --ignore=tests/test_wheel.py"
ignore="${ignore-} --ignore=tests/test_wheelfile.py"
%endif
%if %{without patchelf}
k="${k-}${k+ and }not test_contents"
k="${k-}${k+ and }not test_local_lib"
k="${k-}${k+ and }not test_rpath"
k="${k-}${k+ and }not test_get_requires_for_build_wheel"
k="${k-}${k+ and }not test_uneeded_rpath"
%endif

%pytest ${ignore-} -k "${k-}"
%endif


%files -n python3-meson-python -f %{pyproject_files}
%doc CHANGELOG.rst
%doc README.rst


%changelog
%autochangelog
