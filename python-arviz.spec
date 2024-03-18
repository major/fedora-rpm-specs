
%global srcname arviz

Name:           python-%{srcname}
Version:        0.17.1
Release:        %autorelease
Summary:        Exploratory analysis of Bayesian models

License:        Apache-2.0
URL:            https://python.arviz.org/
Source0:        %{pypi_source}

BuildArch:      noarch
BuildRequires:  python3-devel

%global _description %{expand:
ArviZ is a Python package for exploratory analysis of Bayesian models. 
Includes functions for posterior analysis, sample diagnostics, 
model checking, and comparison.}

%description %_description

%package -n python3-%{srcname}
Summary:        %{summary}
BuildRequires:  python3-setuptools
# Some optional dependencies
Recommends:  python3dist(bokeh)
Recommends:  python3dist(ujson)

%description -n python3-%{srcname} %_description

%prep
%autosetup -n %{srcname}-%{version}

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install

%pyproject_save_files arviz

%check
%pyproject_check_import -t


%files -n python3-%{srcname} -f %{pyproject_files}
%doc README.md

%changelog
%autochangelog
