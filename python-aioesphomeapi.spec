%global pypi_name aioesphomeapi

Name:           python-%{pypi_name}
Version:        13.0.0
Release:        1%{?dist}
Summary:        Library to interact with devices flashed with esphome

License:        MIT
URL:            https://esphome.io/
Source0:        https://github.com/esphome/aioesphomeapi/archive/v%{version}/%{pypi_name}-%{version}.tar.gz

BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  python3-async-timeout
BuildRequires:  python3-pytest
BuildRequires:  python3-pytest-asyncio
BuildRequires:  sed

%global _description %{expand:
aioesphomeapi allows you to interact with devices flashed with esphome.}

%description %_description

%package -n python3-%{pypi_name}
Summary:        %{summary}

%description -n python3-%{pypi_name} %_description

%prep
%autosetup -p1 -n %{pypi_name}-%{version}

# Use builtin mock
sed -i 's/from mock/from unittest.mock/' tests/*.py

%generate_buildrequires
%pyproject_buildrequires -r

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files %{pypi_name}

%check
%pytest

%files -n python3-%{pypi_name} -f %{pyproject_files}
%license LICENSE
%doc README.rst

%changelog
* Sat Dec 03 2022 Fabian Affolter <mail@fabian-affolter.ch> - 13.0.0-1
- Update to latest upstream release 13.0.0 (closes rhbz#2132834)

* Mon Oct 03 2022 Fabian Affolter <mail@fabian-affolter.ch> - 11.1.0-1
- Update to latest upstream release 11.1.0 (closes rhbz#2132834)

* Wed Sep 28 2022 Fabian Affolter <mail@fabian-affolter.ch> - 10.14.0-1
- Update to latest upstream release 10.14.0 (closes rhbz#2130658)

* Mon Aug 22 2022 Fabian Affolter <mail@fabian-affolter.ch> - 10.13.0-1
- Update to latest upstream release 10.13.0 (closes rhbz#2120169)

* Fri Aug 19 2022 Fabian Affolter <mail@fabian-affolter.ch> - 10.11.0-1
- Update to latest upstream release 10.11.0 (closes rhbz#2087567)

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 10.8.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Tue Jun 14 2022 Python Maint <python-maint@redhat.com> - 10.8.2-2
- Rebuilt for Python 3.11

* Wed Feb 23 2022 Fabian Affolter <mail@fabian-affolter.ch> - 10.8.2-1
- Update to latest upstream release 10.8.2 (closes rhbz#2052583)

* Tue Jan 25 2022 Fabian Affolter <mail@fabian-affolter.ch> - 10.8.1-1
- Update to latest upstream release 10.8.1 (closes rhbz#2044086)

* Fri Jan 21 2022 Fabian Affolter <mail@fabian-affolter.ch> - 10.8.0-1
- Update to latest upstream release 10.8.0 (closes rhbz#2042679)

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 10.6.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Sun Dec 05 2021 Fabian Affolter <mail@fabian-affolter.ch> - 10.6.0-1
- Update to latest upstream release 10.6.0 (closes rhbz#2002494)

* Tue Nov 09 2021 Davide Cavalca <dcavalca@fedoraproject.org> - 10.2.0-1
- Update to 10.2.0 (rhbz#2002494)
- Convert to pyproject macros and run tests

* Wed Aug 25 2021 Fabian Affolter <mail@fabian-affolter.ch> - 8.0.0-1
- Update to latest upstream release 8.0.0 (rhbz#1939523)

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.6.6-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 2.6.6-2
- Rebuilt for Python 3.10

* Tue Mar 16 2021 Fabian Affolter <mail@fabian-affolter.ch> - 2.6.6-1
- Update to latest upstream release 2.6.6 (#1939523)

* Mon Feb 15 2021 Fabian Affolter <mail@fabian-affolter.ch> - 2.6.5-1
- Update to latest upstream release 2.6.5 (#1928793)

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.6.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Dec 14 2020 Fabian Affolter <mail@fabian-affolter.ch> - 2.6.4-1
- Update to latest upstream release 2.6.4

* Tue Sep 08 2020 Fabian Affolter <mail@fabian-affolter.ch> - 2.6.3-1
- Update to latest upstream release 2.6.3

* Sat Aug 22 2020 Fabian Affolter <mail@fabian-affolter.ch> - 2.6.2-1
- Update to latest upstream release 2.6.2

* Fri Jun 19 2020 Fabian Affolter <mail@fabian-affolter.ch> - 2.6.1-1
- Initial package for Fedora
