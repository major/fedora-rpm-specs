%global modname pyongc

Name:           python-%{modname}
Version:        1.2.0
Release:        %autorelease
Summary:        A python interface for accessing OpenNGC database data
# Code license is MIT, database is CC-BY-SA-4.0
License:        MIT AND CC-BY-SA-4.0
URL:            https://pypi.python.org/pypi/PyOngc
Source:         %{pypi_source pyongc}

BuildArch:      noarch
BuildRequires:  python3-devel

# For tests
BuildRequires:  python3dist(pytest)

%global _description %{expand:
PyOngc provides a python module to access astronomical data about
NGC and IC objects from the OpenNGC database.}

%description %_description


%package -n     python3-%{modname}
Summary:        %{summary}

%description -n python3-%{modname} %_description


%pyproject_extras_subpkg -n python3-pyongc data


%prep
%autosetup -n %{modname}-%{version} -p1

%generate_buildrequires
%pyproject_buildrequires -x data


%build
%pyproject_wheel


%install
%pyproject_install
%pyproject_save_files %{modname} -l


%check
%pyproject_check_import
%pytest tests


%files -n python3-%{modname} -f %{pyproject_files}
%doc README.rst
%{_bindir}/ongc


%changelog
%autochangelog
