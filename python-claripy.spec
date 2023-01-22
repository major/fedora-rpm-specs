%global pypi_name claripy

Name:           python-%{pypi_name}
Version:        9.0.6885
Release:        7%{?dist}
Summary:        Abstraction layer for constraint solvers

License:        BSD
URL:            https://github.com/angr/claripy
Source0:        %{url}/archive/v%{version}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch

%description
Claripy is an abstracted constraint-solving wrapper.

%package -n     python3-%{pypi_name}
Summary:        %{summary}

BuildRequires:  python3-devel
BuildRequires:  python3-setuptools

Requires:       python3-z3
%{?python_provide:%python_provide python3-%{pypi_name}}

%description -n python3-%{pypi_name}
Claripy is an abstracted constraint-solving wrapper.

%prep
%autosetup -n %{pypi_name}-%{version}
rm -rf %{pypi_name}.egg-info
# Remove installation requirement. Fedora is using a different name, see above
sed -i -e '/z3-solver/d' setup.py
# Remove shebangs
sed -i -e '/^#!\//, 1d' claripy/{*.py,frontend_mixins/*.py,frontends/*.py}

%build
%py3_build

%install
%py3_install

%files -n python3-%{pypi_name}
%license LICENSE
%doc README.md
%{python3_sitelib}/%{pypi_name}/
%{python3_sitelib}/%{pypi_name}-%{version}-py*.egg-info/

%changelog
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
