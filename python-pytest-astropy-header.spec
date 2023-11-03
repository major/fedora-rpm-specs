%global srcname pytest-astropy-header

Name: python-%{srcname}
Version: 0.2.2
Release: %autorelease
Summary: pytest plugin to add diagnostic info to the header of output

License: BSD-3-Clause
URL: https://github.com/astropy/pytest-astropy-header
Source0: %{pypi_source}
BuildRequires:  python3-devel

BuildArch: noarch

%global _description %{expand:
This plugin package provides a way to include information about the system, 
Python installation, and select dependencies in the header of the output 
when running pytest. It can be used with packages that are not affiliated 
with the Astropy project, but is optimized for use with 
astropy-related projects.}

%description %_description

%package -n python3-%{srcname}
Summary: %{summary}
BuildRequires: %{py3_dist setuptools}
BuildRequires: %{py3_dist setuptools_scm}

%description -n python3-%{srcname} 
%_description

%prep
%autosetup -n %{srcname}-%{version}

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install

%pyproject_save_files pytest_astropy_header

%check
%pyproject_check_import 

%files -n python3-%{srcname} -f %{pyproject_files}
%license LICENSE.rst
%doc CHANGES.rst README.rst

%changelog
%autochangelog
