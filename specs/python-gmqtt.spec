%global pypi_name gmqtt
%bcond_with network

Name:           python-%{pypi_name}
Version:        0.7.0
Release:        %autorelease
Summary:        Client for the MQTT protocol

License:        MIT
URL:            https://github.com/wialon/gmqtt
Source0:        %{pypi_source}
BuildArch:      noarch

%description
Asynchronous Python MQTT client implementation.

%package -n     python3-%{pypi_name}
Summary:        %{summary}

BuildRequires:  python3-devel

%if %{with network}
BuildRequires:  python3dist(pytest)
%endif

%description -n python3-%{pypi_name}
Asynchronous Python MQTT client implementation.

%prep
%autosetup -n %{pypi_name}-%{version}

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install

%pyproject_save_files -l %{pypi_name}

# Requires access to a third-party MQTT Broker
%if %{with network}
%check
%{__python3} setup.py test
%endif

%files -n %files -n python3-%{pypi_name} -f %{pyproject_files}
%license LICENSE
%doc README.md

%changelog
%autochangelog
