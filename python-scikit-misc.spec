%global pypi_name scikit-misc
%global module_name skmisc

# Enable tests
%bcond_without tests

# Use releases published on GitHub since the PyPI sources contains a
# pregenerated C file as well as a precompiled library.
# Moreover, provided setup.py skips cythonize when run on the PyPI source
%global forgeurl https://github.com/has2k1/scikit-misc
%global tag v0.1.4
%forgemeta

%global _description %{expand:
Miscellaneous tools for data analysis and scientific computing.}

Name:           python-%{pypi_name}
Version:        0.1.4
Release:        1%{?dist}
Summary:        Miscellaneous tools for data analysis and scientific computing

# MIT License applies to doc/theme/static/bootstrap-3.4.1
# Python-2.0.1 license applies to doc/_static/copybutton.js
License:        BSD-3-Clause AND MIT AND Python-2.0.1
URL:            %{forgeurl}
Source0:        %{forgesource}
# %%pyproject_buildrequires uses contextlib.redirect_stdout, which
# does not support stdout of subprocesses
Patch:          have_subprocess_print_to_stderr.patch

%description %_description

%package -n python3-%{pypi_name}
Summary:        %{summary}
BuildRequires:  python3-devel
BuildRequires:  git-core
BuildRequires:  python3-numpy
BuildRequires:  python3-Cython
# For optimized performance
BuildRequires:  flexiblas-devel
BuildRequires:  gcc, gcc-gfortran
%if %{with tests}
BuildRequires:  python3-pytest
%endif

%description -n python3-%{pypi_name} %_description


%prep
%autosetup -p1 -n %{pypi_name}-%{version} -S git

# Disable coverage
sed -i -e 's/--cov --cov-report=xml//' pytest.ini


%generate_buildrequires
%pyproject_buildrequires


%build
%pyproject_wheel


%install
%pyproject_install
%pyproject_save_files %{module_name}


%check
%if %{with tests}
  # Thanks to @music for figuring out how to run tests
  mkdir test_env
  pushd test_env
  ln -s ../pytest.ini ../tox.ini %{buildroot}/%{python3_sitearch}/skmisc ./
  %{pytest}
  popd
%else
  %pyproject_check_import
%endif

%files -n python3-%{pypi_name} -f %{pyproject_files}
%doc README.rst
%license LICENSE

%changelog
%autochangelog
