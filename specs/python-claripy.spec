%global pypi_name claripy

Name:           python-%{pypi_name}
Version:        9.2.136
Release:        2%{?dist}
Summary:        Abstraction layer for constraint solvers

License:        LicenseRef-Callaway-BSD
URL:            https://github.com/angr/claripy
Source0:        %{url}/archive/v%{version}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  python3-devel

%description
Claripy is an abstracted constraint-solving wrapper.

%package -n     python3-%{pypi_name}
Summary:        %{summary}

Requires:       python3-z3

%description -n python3-%{pypi_name}
Claripy is an abstracted constraint-solving wrapper.

%prep
%autosetup -p1 -n %{pypi_name}-%{version}
# Remove installation requirement. Fedora is using a different name, see above
sed -i 's/, "z3-solver==4.13.0.0"//' pyproject.toml

%generate_buildrequires
%pyproject_buildrequires -t

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files %{pypi_name}

%files -n python3-%{pypi_name} -f %{pyproject_files}
%license LICENSE
%doc README.md

%changelog
* Sat Jan 18 2025 Fedora Release Engineering <releng@fedoraproject.org> - 9.2.136-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Wed Jan 08 2025 Fabian Affolter <mail@fabian-affolter.ch> - 9.2.136-1
- Update to latest upstream release (closes rhbz#2336203)

* Wed Jan 01 2025 W. Michael Petullo <mike@flyn.org> - 9.2.135-1
- Update to latest upstream release (closes rhbz#2331861)

* Fri Nov 29 2024 Fabian Affolter <mail@fabian-affolter.ch> - 9.2.130-1
- Update to latest upstream release (closes rhbz#2327388)

* Wed Nov 13 2024 Fabian Affolter <mail@fabian-affolter.ch> - 9.2.128-1
- Update to latest upstream release (closes rhbz#2323962)

* Tue Oct 29 2024 Fabian Affolter <mail@fabian-affolter.ch> - 9.2.126-1
- Update to latest upstream release (closes rhbz#2322510)

* Sat Oct 26 2024 Fabian Affolter <mail@fabian-affolter.ch> - 9.2.125-1
- Update to latest upstream release (closes rhbz#2321105)

* Wed Oct 16 2024 Fabian Affolter <mail@fabian-affolter.ch> - 9.2.124-1
- Update to latest upstream release (closes rhbz#2321105)

* Wed Oct 16 2024 Fabian Affolter <mail@fabian-affolter.ch> - 9.2.123-1
- Update to new upstream version (closes rhbz#2318933)

* Tue Oct 08 2024 Fabian Affolter <mail@fabian-affolter.ch> - 9.2.122-1
- Update to new upstream version (closes rhbz#2317137)

* Wed Oct 02 2024 Fabian Affolter <mail@fabian-affolter.ch> - 9.2.120-1
- Update to new upstream version (closes rhbz#2315969)

* Thu Sep 26 2024 Fabian Affolter <mail@fabian-affolter.ch> - 9.2.119-1
- Update to new upstream version (closes rhbz#2314473)

* Wed Sep 18 2024 Fabian Affolter <mail@fabian-affolter.ch> - 9.2.118-1
- Update to new upstream version (closes rhbz#2174149)

* Wed Sep 04 2024 Miroslav Suchý <msuchy@redhat.com> - 9.2.39-8
- convert license to SPDX

* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 9.2.39-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Fri Jun 07 2024 Python Maint <python-maint@redhat.com> - 9.2.39-6
- Rebuilt for Python 3.13

* Fri Jan 26 2024 Fedora Release Engineering <releng@fedoraproject.org> - 9.2.39-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 9.2.39-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 9.2.39-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Wed Jun 14 2023 Python Maint <python-maint@redhat.com> - 9.2.39-2
- Rebuilt for Python 3.12

* Tue Feb 21 2023 Fabian Affolter <mail@fabian-affolter.ch> - 9.2.39-1
- Update to latest upstream release 9.2.39

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 9.0.6885-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 9.0.6885-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon Jun 13 2022 Python Maint <python-maint@redhat.com> - 9.0.6885-5
- Rebuilt for Python 3.11

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 9.0.6885-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 9.0.6885-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 9.0.6885-2
- Rebuilt for Python 3.10

* Tue Apr 27 2021 Fabian Affolter <mail@fabian-affolter.ch> - 9.0.6885-1
- Update to latest upstream release 9.0.6885 (#1929355)

* Mon Apr 26 2021 Fabian Affolter <mail@fabian-affolter.ch> - 9.0.6852-1
- Update to latest upstream release 9.0.6852 (#1929355)

* Tue Mar 02 2021 Fabian Affolter <mail@fabian-affolter.ch> - 9.0.6136-1
- Update to latest upstream release 9.0.6136 (#1929355)

* Tue Feb 16 2021 Fabian Affolter <mail@fabian-affolter.ch> - 9.0.5903-1
- Update to latest upstream release 9.0.5903 (#1929355)

* Fri Feb 12 2021 Fabian Affolter <mail@fabian-affolter.ch> - 9.0.5811-1
- Update to latest upstream release 9.0.5811 (#1920625)

* Tue Feb 09 2021 Fabian Affolter <mail@fabian-affolter.ch> - 9.0.5739-1
- Update to latest upstream release 9.0.5739 (#1920625)

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 9.0.5450-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jan 20 2021 Fabian Affolter <mail@fabian-affolter.ch> - 9.0.5450-1
- Update to latest upstream release 9.0.5450 (#1905653)

* Fri Jan 08 2021 Fabian Affolter <mail@fabian-affolter.ch> - 9.0.5327-1
- Update to latest upstream release 9.0.5327 (#1905653)

* Sun Dec 27 2020 Fabian Affolter <mail@fabian-affolter.ch> - 9.0.5171-1
- Update to latest upstream release 9.0.5171 (#1905653)

* Fri Dec 18 2020 Fabian Affolter <mail@fabian-affolter.ch> - 9.0.5034-1
- Update to new upstream release 9.0.5034 (#1905653)

* Wed Dec 16 2020 Fabian Affolter <mail@fabian-affolter.ch> - 9.0.5002-1
- Update to new upstream release 9.0.5002 (#1905653)

* Wed Nov 25 2020 Fabian Affolter <mail@fabian-affolter.ch> - 9.0.4885-1
- Update to new upstream release 9.0.4885 (#1901717)

* Thu Oct 29 2020 Fabian Affolter <mail@fabian-affolter.ch> - 9.0.4663-1
- Update to new upstream release 9.0.4663 (#1891935)

* Fri Oct 02 2020 Fabian Affolter <mail@fabian-affolter.ch> - 9.0.4495-1
- Update to new upstream release 9.0.4495 (#1880182)

* Fri Sep 25 2020 Fabian Affolter <mail@fabian-affolter.ch> - 9.0.4446-1
- Update to new upstream release 9.0.4446 (#1880182)

* Wed Sep 23 2020 Fabian Affolter <mail@fabian-affolter.ch> - 9.0.4378-1
- Update to new upstream release 9.0.4378 (#1880182)

* Fri Jul 31 2020 Fabian Affolter <mail@fabian-affolter.ch> - 8.20.7.27-1
- Update to new upstream release 8.20.7.27

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 8.20.7.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Jul 17 2020 Fabian Affolter <mail@fabian-affolter.ch> - 8.20.7.6-1
- Update to new upstream release 8.20.7.6

* Tue Jun 23 2020 Fabian Affolter <mail@fabian-affolter.ch> - 8.20.6.8-1
- Update to latest upstream release 8.20.6.8

* Sat Jun 06 2020 Fabian Affolter <mail@fabian-affolter.ch> - 8.20.6.1-1
- Don't delete a specific line
- Update to latest upstream release 8.20.6.1

* Mon May 18 2020 Fabian Affolter <mail@fabian-affolter.ch> - 8.20.1.7-2
- Fix installation requirements (#1815670)

* Fri Feb 28 2020 Fabian Affolter <mail@fabian-affolter.ch> - 8.20.1.7-1
- Initial package for Fedora
