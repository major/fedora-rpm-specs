%global pypi_name spyder-kernels

%global forgeurl https://github.com/spyder-ide/spyder-kernels
Version:        3.1.6
%global tag     v%{version}
%forgemeta

Name:           python-%{pypi_name}
Release:        %autorelease
Epoch:          2
Summary:        Jupyter kernels for Spyder's console

# SPDX
License:        MIT
URL:            %forgeurl
Source0:        %forgesource

# Allow ipykernel 7
Patch:          https://github.com/spyder-ide/spyder-kernels/pull/589.patch

BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  python3-anyio
BuildRequires:  python3-cython
BuildRequires:  python3-dask
BuildRequires:  python3-distributed
BuildRequires:  python3-django
BuildRequires:  python3-flaky
BuildRequires:  python3-h5py
BuildRequires:  python3-ipython
BuildRequires:  python3-matplotlib
BuildRequires:  python3-numpy
BuildRequires:  python3-pandas
BuildRequires:  python3-pillow
BuildRequires:  python3-pyarrow
BuildRequires:  python3-pydicom
BuildRequires:  python3-pytest
BuildRequires:  python3-scipy
BuildRequires:  python3-xarray

%global _description %{expand:
Package that provides Jupyter kernels for use with the consoles of
Spyder, the Scientific Python Development Environment.

These kernels can launched either through Spyder itself or in an
independent Python session, and allow for interactive or file-based
execution of Python code inside Spyder.}

%description %_description


%package -n     python3-%{pypi_name}
Summary:        %{summary}

%description -n python3-%{pypi_name} %_description


%prep
%autosetup -n %{pypi_name}-%{version} -p1


%generate_buildrequires
%pyproject_buildrequires


%build
%pyproject_wheel


%install
%pyproject_install
%pyproject_save_files -l spyder_kernels


%check
%pyproject_check_import
%pytest -k "not test_get_value_with_polars and not test_polars_dataframe"


%files -n python3-%{pypi_name} -f %{pyproject_files}
%doc README.md


%changelog
%autochangelog
