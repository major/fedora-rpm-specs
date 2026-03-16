%global with_tests 0

Name:          modpoll
Version:       1.6.0
Release:       1%{?dist}
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
* Sun Dec 07 2025 Peter Robinson <pbrobinson@fedoraproject.org> - 1.6.0-1
- Update to 1.6.0

* Mon Nov 03 2025 Peter Robinson <pbrobinson@fedoraproject.org> - 1.5.1-1
- Update to 1.5.1

* Sun Nov 17 2024 Peter Robinson <pbrobinson@fedoraproject.org> - 1.4.0-1
- Update to 1.4.0

* Sun Nov 03 2024 Peter Robinson <pbrobinson@fedoraproject.org> - 1.3.3-1
- Initial package
