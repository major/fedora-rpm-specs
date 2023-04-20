%global pypi_name scikit-misc
%global archive_name scikit_misc
%global module_name skmisc

# Enable tests
%bcond_without tests

%global _description %{expand:
Miscellaneous tools for data analysis and scientific computing.}

Name:           python-%{pypi_name}
Version:        0.2.0
Release:        %autorelease
Summary:        Miscellaneous tools for data analysis and scientific computing

# MIT License applies to doc/theme/static/bootstrap-3.4.1
# Python-2.0.1 license applies to doc/_static/copybutton.js
License:        BSD-3-Clause AND MIT AND Python-2.0.1
URL:            https://github.com/has2k1/scikit-misc
Source0:        %{pypi_source %{archive_name}}

%description %_description

%package -n python3-%{pypi_name}
Summary:        %{summary}
BuildRequires:  python, python3-devel
BuildRequires:  python3-numpy
BuildRequires:  python3-Cython
# For optimized performance
BuildRequires:  flexiblas-devel
BuildRequires:  gcc, gcc-gfortran
BuildRequires:  meson
BuildRequires:  git-core
%if %{with tests}
BuildRequires:  python3-pytest
%endif


%description -n python3-%{pypi_name} %_description


%prep
%autosetup -p1 -n %{archive_name}-%{version}

# Disable coverage
sed -i -e 's/--cov=skmisc --cov-report=xml//' pyproject.toml


%build
%meson -Dblas=flexiblas -Dlapack=flexiblas
%meson_build


%install
%meson_install


%check
%if %{with tests}
  %pytest
%else
  %pyproject_check_import
%endif


# %check
# Testing not implemented in Meson (yet?)


%files -n python3-%{pypi_name}
%{python3_sitearch}/%{module_name}/
%doc README.rst
%license LICENSE

%changelog
%autochangelog
