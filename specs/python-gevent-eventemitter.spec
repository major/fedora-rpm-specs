%global pypi_name gevent-eventemitter

Name:       python-%{pypi_name}
Version:    2.1
Release:    %autorelease
Summary:    EventEmitter using gevent
BuildArch:  noarch

# https://github.com/rossengeorgiev/gevent-eventemitter/pull/3
License:    MIT
URL:        https://github.com/rossengeorgiev/gevent-eventemitter
# Tests works only woth GitHub sources
Source:     %{url}/archive/v%{version}/%{pypi_name}-%{version}.tar.gz
# Add LICENSE file
Patch:      %{url}/pull/3/commits/58a4b15852980a231a08e5a0d45e71f7fa47aa02.patch

BuildRequires: python3-devel
BuildRequires: python3dist(pytest)

%global _description %{expand:
This module implements EventEmitter with gevent.}

%description %{_description}


%package -n python3-%{pypi_name}
Summary:    %{summary}
%{?python_provide:%python_provide python3-%{pypi_name}}

%description -n python3-%{pypi_name} %{_description}


%prep
%autosetup -n %{pypi_name}-%{version} -p1
%generate_buildrequires
%pyproject_buildrequires


%build
%pyproject_wheel


%install
%pyproject_install
%pyproject_save_files -l eventemitter


%check
%pyproject_check_import
%pytest


%files -n python3-%{pypi_name} -f %{pyproject_files}
%doc README.rst
%license LICENSE


%changelog
%autochangelog
