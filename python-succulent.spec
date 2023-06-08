%bcond_without tests
# we do not build docs since current docs are immature

%global pypi_name succulent

%global _description %{expand:
Sending sensor measurements, data, or GPS positions from embedded devices,
microcontrollers, and smartwatches to the central server is sometimes
complicated and tricky. Setting up the primary data collection scripts
can be time-consuming (selecting a protocol, framework, API, testing it, etc.).
Usually, scripts are written for a specific task; thus, they are not easily
adaptive to other tasks. succulent is a pure Python framework that simplifies
the configuration, management, collection, and preprocessing of data collected
via POST requests. }

Name:           python-%{pypi_name}
Version:        0.2.2
Release:        1%{?dist}
Summary:        Collect POST requests

License:        MIT
URL:            https://github.com/firefly-cpp/%{pypi_name}
Source0:        %{url}/archive/%{version}/%{pypi_name}-%{version}.tar.gz

BuildArch:      noarch

BuildRequires:  python3-devel

BuildRequires:  python3-toml-adapt
BuildRequires:  python3-pytest


%description %_description

%package -n python3-%{pypi_name}
Summary:        %{summary}

%description -n python3-%{pypi_name} %_description

%prep
%autosetup -n %{pypi_name}-%{version}
rm -rf %{pypi_name}.egg-info

# optional step but let's ensure that there is no problems with python, pandas and Flask versions
toml-adapt -path pyproject.toml -a change -dep python -ver X
toml-adapt -path pyproject.toml -a change -dep flask -ver X
toml-adapt -path pyproject.toml -a change -dep pandas -ver X

%generate_buildrequires
%pyproject_buildrequires -r

%build
%pyproject_wheel

%install
%pyproject_install

%pyproject_save_files succulent

%check
%if %{with tests}
%pytest
%endif

%files -n python3-%{pypi_name} -f %{pyproject_files}
%license LICENSE
%doc README.md CHANGELOG.md CODE_OF_CONDUCT.md

%changelog
* Mon Jun 5 2023 Iztok Fister Jr. <iztokf AT fedoraproject DOT org> - 0.2.2-1
- Update to 0.2.2

* Fri Jun 2 2023 Iztok Fister Jr. <iztokf AT fedoraproject DOT org> - 0.2.1-1
- Initial package
