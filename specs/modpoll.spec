%global with_tests 0

Name:          modpoll
Version:       1.6.1
Release:       %autorelease
Summary:       A command line tool for Modbus and MQTT
License:       MIT
URL:           https://github.com/gavinying/modpoll
Source0:       %{url}/archive/v%{version}/%{name}-%{version}.tar.gz

BuildArch:     noarch
BuildRequires: python3-devel
BuildRequires: python3-setuptools
# For tests
%if 0%{?with_tests}
BuildRequires: python3-pytest
BuildRequires: python3-prettytable
BuildRequires: python3-pymodbus
%endif

%description
A command line tool for Modbus and MQTT

%prep
%autosetup -p1

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%if 0%{?with_tests}
%check
%pytest
%endif

%install
%pyproject_install
%pyproject_save_files modpoll

%files -f %{pyproject_files}
%license LICENSE
%doc README.md
%{_bindir}/modpoll

%changelog
%autochangelog
