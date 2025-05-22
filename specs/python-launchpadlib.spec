%global pypi_name launchpadlib
Name:           python-%{pypi_name}
Version:        2.1.0
Release:        %autorelease
Summary:        Script Launchpad through its web services interfaces

License:        LGPL-3.0-only
URL:            https://launchpad.net/launchpadlib 
Source0:        %{pypi_source}
BuildArch:      noarch

%global _description %{expand:
Launchpadlib is an open-source Python library that lets you treat the HTTP
resources published by Launchpad's web service as Python objects responding
to a standard set of commands. With launchpadlib you can integrate your
applications into Launchpad without knowing a lot about HTTP client
programming.}

%description %_description

%package -n     python3-%{pypi_name}
Summary:        %{summary}

BuildRequires:  python3-devel

%description -n python3-%{pypi_name} %_description

%prep
%autosetup -n %{pypi_name}-%{version}

%generate_buildrequires
%pyproject_buildrequires -x keyring,testing

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files -l %{pypi_name}

%check
%pyproject_check_import
%{py3_test_envvars} %{python3} -m unittest src/%{pypi_name}/tests/*py

%files -n python3-%{pypi_name} -f %{pyproject_files}
%doc README.rst

%changelog
%autochangelog
