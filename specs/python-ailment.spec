%global pypi_name ailment

Name:           python-%{pypi_name}
Version:        9.2.158
Release:        2%{?dist}
Summary:        The angr intermediate language

License:        LicenseRef-Callaway-BSD
URL:            https://github.com/angr/ailment
Source0:        %{url}/archive/v%{version}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  python3-devel
 
%description
AIL is the angr intermediate language.

%package -n     python3-%{pypi_name}
Summary:        %{summary}

%{?python_provide:%python_provide python3-%{pypi_name}}

%description -n python3-%{pypi_name}
AIL is the angr intermediate language.

%prep
%autosetup -p1 -n %{pypi_name}-%{version}

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files %{pypi_name}

%files -n python3-%{pypi_name} -f %{pyproject_files}
%doc README.md
%license LICENSE

%changelog
* Fri Jul 25 2025 Fedora Release Engineering <releng@fedoraproject.org> - 9.2.158-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_43_Mass_Rebuild

* Wed Jul 09 2025 Fabian Affolter <mail@fabian-affolter.ch> - 9.2.158-1
- Update to latest upstream release (closes rhbz#2358329)

* Mon Jun 02 2025 Python Maint <python-maint@redhat.com> - 9.2.148-2
- Rebuilt for Python 3.14

* Tue Apr 01 2025 Fabian Affolter <mail@fabian-affolter.ch> - 9.2.148-1
- Remove -t (closes rhbz#2354090)
- Update to latest upstream release (closes rhbz#2346300)

* Sun Feb 16 2025 Fabian Affolter <mail@fabian-affolter.ch> - 9.2.141-1
- Update to latest upstream release (closes rhbz#2337858)

* Sat Jan 18 2025 Fedora Release Engineering <releng@fedoraproject.org> - 9.2.136-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Wed Jan 08 2025 Fabian Affolter <mail@fabian-affolter.ch> - 9.2.136-1
- Update to latest upstream release (closes rhbz#2336198)

* Wed Jan 01 2025 W. Michael Petullo <mike@flyn.org> - 9.2.135-1
- Update to latest upstream release (closes rhbz#2331860)

* Fri Nov 29 2024 Fabian Affolter <mail@fabian-affolter.ch> - 9.2.130-1
- Update to latest upstream release (closes rhbz#2327326)

* Wed Nov 13 2024 Fabian Affolter <mail@fabian-affolter.ch> - 9.2.128-1
- Update to latest upstream release (closes rhbz#2323900)

* Tue Oct 29 2024 Fabian Affolter <mail@fabian-affolter.ch> - 9.2.126-1
- Update to latest upstream release (closes rhbz#2322520)

* Wed Oct 16 2024 Fabian Affolter <mail@fabian-affolter.ch> - 9.2.125-1
- Update to latest upstream release (closes rhbz#2321102)

* Wed Oct 16 2024 Fabian Affolter <mail@fabian-affolter.ch> - 9.2.124-1
- Update to latest upstream release (closes rhbz#2321102)

* Wed Oct 16 2024 Fabian Affolter <mail@fabian-affolter.ch> - 9.2.123-1
- Update to latest upstream release (closes rhbz#2318835)

* Tue Oct 08 2024 Fabian Affolter <mail@fabian-affolter.ch> - 9.2.122-1
- Update to latest upstream release (closes rhbz#2317135)

* Tue Oct 01 2024 Fabian Affolter <mail@fabian-affolter.ch> - 9.2.120-1
- Update to latest upstream release (closes rhbz#2315976)

* Thu Sep 26 2024 Fabian Affolter <mail@fabian-affolter.ch> - 9.2.119-1
- Update to latest upstream release (closes rhbz#2314472)

* Wed Sep 18 2024 Fabian Affolter <mail@fabian-affolter.ch> - 9.2.118-1
- Update to latest upstream release (closes rhbz#2312978)

* Tue Sep 17 2024 Fabian Affolter <mail@fabian-affolter.ch> - 9.2.117-1
- Update to latest upstream release (closes rhbz#2174142)

* Wed Sep 04 2024 Miroslav Suchý <msuchy@redhat.com> - 9.2.39-8
- convert license to SPDX

* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 9.2.39-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Fri Jun 07 2024 Python Maint <python-maint@redhat.com> - 9.2.39-6
- Rebuilt for Python 3.13

* Fri Jan 26 2024 Fedora Release Engineering <releng@fedoraproject.org> - 9.2.39-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 9.2.39-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 9.2.39-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Wed Jun 14 2023 Python Maint <python-maint@redhat.com> - 9.2.39-2
- Rebuilt for Python 3.12

* Tue Feb 21 2023 Fabian Affolter <mail@fabian-affolter.ch> - 9.2.39-1
- Update to latest upstream release 9.2.39

* Sat Feb 11 2023 Fabian Affolter <mail@fabian-affolter.ch> - 9.2.38-1
- Update to latest upstream release 9.2.38 (closes rhbz#1999778)

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
- Update to latest upstream release 9.0.6885 (#1920600)

* Mon Apr 26 2021 Fabian Affolter <mail@fabian-affolter.ch> - 9.0.6852-1
- Update to latest upstream release 9.0.6852 (#1920600)

* Tue Mar 02 2021 Fabian Affolter <mail@fabian-affolter.ch> - 9.0.6136-1
- Update to latest upstream release 9.0.6136 (#1920600)

* Tue Feb 16 2021 Fabian Affolter <mail@fabian-affolter.ch> - 9.0.5903-1
- Update to latest upstream release 9.0.5903 (#1920600)

* Fri Feb 12 2021 Fabian Affolter <mail@fabian-affolter.ch> - 9.0.5811-1
- Update to latest upstream release 9.0.5811 (#1920600)

* Tue Feb 09 2021 Fabian Affolter <mail@fabian-affolter.ch> - 9.0.5739-1
- Update to latest upstream release 9.0.5739 (#1920600)

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 9.0.5450-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jan 20 2021 Fabian Affolter <mail@fabian-affolter.ch> - 9.0.5450-1
- Update to latest upstream release 9.0.5450 (#1905670)

* Fri Jan 08 2021 Fabian Affolter <mail@fabian-affolter.ch> - 9.0.5450-1
- Update to latest upstream release 9.0.5327 (#1905670)

* Sun Dec 27 2020 Fabian Affolter <mail@fabian-affolter.ch> - 9.0.5171-1
- Update to latest upstream release 9.0.5171 (#1905670)

* Fri Dec 18 2020 Fabian Affolter <mail@fabian-affolter.ch> - 9.0.5034-1
- Update to new upstream release 9.0.5034 (#1905670)

* Wed Dec 16 2020 Fabian Affolter <mail@fabian-affolter.ch> - 9.0.5002-1
- Update to new upstream release 9.0.5002 (#1905670)

* Wed Nov 25 2020 Fabian Affolter <mail@fabian-affolter.ch> - 9.0.4885-1
- Update to new upstream release 9.0.4885 (#1901692)

* Thu Oct 29 2020 Fabian Affolter <mail@fabian-affolter.ch> - 9.0.4663-1
- Update to new upstream release 9.0.4663 (#1891968)

* Sun Oct 04 2020 Fabian Affolter <mail@fabian-affolter.ch> - 9.0.4495-1
- Update to new upstream release 9.0.4495 (#1880185)

* Tue Jul 28 2020 Fabian Affolter <mail@fabian-affolter.ch> - 8.20.7.27-1
- Update to new upstream release 8.20.7.27 (#1858211)

* Fri Jul 17 2020 Fabian Affolter <mail@fabian-affolter.ch> - 8.20.7.6-1
- Update to new upstream release 8.20.7.6 (#1858211)

* Tue Jun 23 2020 Fabian Affolter <mail@fabian-affolter.ch> - 8.20.6.8-1
- Update to latest upstream release 8.20.6.8

* Wed Jun 03 2020 Fabian Affolter <mail@fabian-affolter.ch> - 8.20.6.1-1
- Update to new upstream release 8.20.6.1

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 8.20.1.7-2
- Rebuilt for Python 3.9

* Fri Feb 28 2020 Fabian Affolter <mail@fabian-affolter.ch> - 8.20.1.7-1
- Initial package for Fedora
