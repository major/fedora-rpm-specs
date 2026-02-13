%bcond_without tests

%global pypi_name steam

Name:       python-%{pypi_name}
Version:    1.6.1
Release:    %autorelease
Summary:    Python package for interacting with Steam. Fork of ValvePython/steam
BuildArch:  noarch

License:    MIT
URL:        https://github.com/solsticegamestudios/steam
# Tests works only woth GitHub sources
Source:     %{url}/archive/v%{version}/%{pypi_name}-%{version}.tar.gz

BuildRequires: python3-devel
%if %{with tests}
BuildRequires: python3dist(gevent-eventemitter) >= 2.1
BuildRequires: python3dist(gevent) >= 1.3.0
BuildRequires: python3dist(protobuf) >= 3.0.0
BuildRequires: python3dist(pytest-cov)
BuildRequires: python3dist(pytest)
BuildRequires: python3dist(vcrpy)
%endif
# For client
#Requires:   python3dist(gevent-eventemitter) >= 2.1
#Requires:   python3dist(gevent) >= 1.3.0
#Requires:   python3dist(protobuf) >= 3.0.0

%global _description %{expand:
A python module for interacting with various parts of Steam.

A fork of ValvePython/steam, which has apparently been abandoned.}

%description %{_description}


%package -n python3-%{pypi_name}
Summary:    %{summary}
%{?python_provide:%python_provide python3-%{pypi_name}}

%description -n python3-%{pypi_name} %{_description}


%prep
%autosetup -n %{pypi_name}-%{version}
sed -i 's/urllib3<2/urllib3/' \
    setup.py
%generate_buildrequires
%pyproject_buildrequires


%build
%pyproject_wheel


%install
%pyproject_install
%pyproject_save_files -l %{pypi_name}


%if %{with tests}
%check
%pyproject_check_import
%dnl %pytest
%endif


%files -n python3-%{pypi_name} -f %{pyproject_files}
%license LICENSE
%doc README.rst CHANGES.md


%changelog
%autochangelog
