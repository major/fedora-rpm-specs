# Use GitHub sources. PyPI sources are not suitable for rebuilding.
# https://github.com/has2k1/scikit-misc/issues/27
%global forgeurl https://github.com/has2k1/scikit-misc
%global pypi_name scikit-misc
%global module_name skmisc

# Enable tests
%bcond_without tests

%global _description %{expand:
Miscellaneous tools for data analysis and scientific computing.}

Name:           python-%{pypi_name}
Version:        0.3.0
Release:        %autorelease
Summary:        Miscellaneous tools for data analysis and scientific computing
%forgemeta
# MIT License applies to doc/theme/static/bootstrap-3.4.1
# Python-2.0.1 license applies to doc/_static/copybutton.js
License:        BSD-3-Clause AND MIT AND Python-2.0.1
URL:            %forgeurl
Source0:        %forgesource
# Add meson build options to pyproject.toml
# Passing this through one of the macros appears unsupported
Patch:          use_flexiblas.patch

%description %_description

%package -n python3-%{pypi_name}
Summary:        %{summary}
BuildRequires:  python3-devel
BuildRequires:  git-core
# For optimized performance
BuildRequires:  flexiblas-devel
BuildRequires:  gcc, gcc-gfortran
BuildRequires:  cmake
BuildRequires:  patchelf
%if %{with tests}
BuildRequires:  python3-pytest
%endif


%description -n python3-%{pypi_name} %_description


%prep
%autosetup -p1 -n %{pypi_name}-%{version} -S git
# Supply the version information to mesonpy
git tag v%{version}

%py3_shebang_fix spin skmisc/_build_utils/

# Disable coverage
sed -i -e 's/--cov=skmisc --cov-report=xml//' pyproject.toml

# Do not attempt to build with an old version of numpy; this makes 
# sense for PyPI distribution (oldest-supported-numpy) but not here.
sed -r -i 's/(numpy)==/\1>=/' pyproject.toml


%generate_buildrequires
%pyproject_buildrequires -w


%build
%pyproject_wheel


%install
%pyproject_install
%pyproject_save_files %{module_name}


%check
%if %{with tests}
  %pytest
%else
  %pyproject_check_import
%endif


%files -n python3-%{pypi_name} -f %{pyproject_files}
%doc README.rst
%license LICENSE

%changelog
%autochangelog
