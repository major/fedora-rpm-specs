%global pypi_name mirakuru

Name:           python-%{pypi_name}
Version:        2.6.0
Release:        %autorelease
Summary:        A process orchestration tool designed for functional and integration tests

License:        LGPL-3.0-or-later
URL:            https://github.com/ClearcodeHQ/mirakuru
Source0:        https://github.com/ClearcodeHQ/mirakuru/archive/v%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  pyproject-rpm-macros

# for check
BuildRequires:  netcat
BuildRequires:  procps-ng
BuildRequires:  python-unversioned-command
BuildRequires:  python3dist(pytest)
BuildRequires:  python3dist(pytest-rerunfailures)
BuildRequires:  python3dist(python-daemon)


%description
A python library that starts your subprocess and waits for a clear indication,
that it's running (process orchestrator)

%package -n     python3-%{pypi_name}
Summary:        %{summary}

%description -n python3-%{pypi_name}
Mirakuru is a process orchestration tool designed for functional and
integration tests

%prep
%autosetup -n %{pypi_name}-%{version}

%generate_buildrequires
%pyproject_buildrequires -r -x tests

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files %{pypi_name}

%check
# Skip test_forgotten_stop and test_daemons_killing as are failing with python 3.13
%pytest -k 'not test_forgotten_stop and not test_daemons_killing'

%files -n python3-%{pypi_name} -f %{pyproject_files}
%license LICENSE
%doc AUTHORS.rst CHANGES.rst README.rst

%changelog
%autochangelog
