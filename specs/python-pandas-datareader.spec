%bcond_without check

%global srcname pandas-datareader
%global summary Data readers from the pandas codebase

%global common_description                                                   \
Data readers extracted from the pandas codebase, should be compatible with   \
recent pandas versions.

Name: python-%{srcname}
Version: 0.11.1
Release: %autorelease
Summary: %{summary}
License: BSD-3-Clause

URL: https://github.com/pydata/pandas-datareader
Source0: %{pypi_source}

BuildArch: noarch
BuildRequires: python3-devel
BuildRequires: python3-setuptools

%description
%{common_description}

%package -n python3-%{srcname}
Summary: %{summary}

%if %{with check}
BuildRequires: python3-pytest
BuildRequires: python3-numpy
BuildRequires: python3-pandas
BuildRequires: python3-requests
BuildRequires: python3-wrapt
%endif

%{?python_provide:%python_provide python3-%{srcname}}

%description -n python3-%{srcname}
%{common_description}

%prep
%autosetup -n %{srcname}-%{version} -p1
# Adjust setuptools_scm conditional
sed -i 's/,<9//' pyproject.toml

%generate_buildrequires
export SETUPTOOLS_SCM_PRETEND_VERSION=%{version}
%pyproject_buildrequires 

%build
export SETUPTOOLS_SCM_PRETEND_VERSION=%{version}
%pyproject_wheel

%install
%pyproject_install

# Remove build-time utility scripts that leak into site-packages
rm -rf %{buildroot}%{python3_sitelib}/docs/ %{buildroot}%{python3_sitelib}/__pycache__/ \
%{buildroot}%{python3_sitelib}/tests/ %{buildroot}%{python3_sitelib}/conftest.py

%pyproject_save_files pandas_datareader

%check
# Most tests require network
%pyproject_check_import pandas_datareader


%files -n python3-%{srcname} -f %{pyproject_files}
%doc README.md

%changelog
%autochangelog
