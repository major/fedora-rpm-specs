Name:           wafw00f
Version:        2.1.0
Release:        10%{?dist}
Summary:        Tool to identifies and fingerprints Web Application Firewall (WAF)


License:        BSD
URL:            https://github.com/sandrogauci/wafw00f
Source0:        %{url}/archive/v%{version}/%{name}-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  python3-setuptools

%description
WAFW00F identifies and fingerprints Web Application Firewall (WAF) products.

%prep
%autosetup -n %{name}-%{version}
sed -i -e '/^#!\//, 1d' {wafw00f/*.py,wafw00f/*/*.py}

%build
%py3_build

%install
%py3_install

%files
%doc CREDITS.txt README.md
%license LICENSE
%{_bindir}/%{name}
%{python3_sitelib}/%{name}-*.egg-info/
%{python3_sitelib}/%{name}/

%changelog
* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.0-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon Jun 13 2022 Python Maint <python-maint@redhat.com> - 2.1.0-9
- Rebuilt for Python 3.11

* Sat Jan 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 2.1.0-6
- Rebuilt for Python 3.10

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Jun 26 2020 Fabian Affolter <mail@fabian-affolter.ch> - 2.1.0-3
- Add python3-setuptools as BR

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 2.1.0-2
- Rebuilt for Python 3.9

* Fri Feb 07 2020 Fabian Affolter <mail@fabian-affolter.ch> - 2.1.0-1
- Update to latest upstream release 2.1.0

* Fri Jan 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Dec 18 2019 Fabian Affolter <mail@fabian-affolter.ch> - 2.0.0-1
- Update to latest upstream release 2.0.0
- Fix installation issue (rhbz#1770879)
- Remove patch

* Mon Oct 07 2019 Fabian Affolter <mail@fabian-affolter.ch> - 1.0.0-3
- Add patch to remove release pinning

* Wed Sep 11 2019 Fabian Affolter <mail@fabian-affolter.ch> - 1.0.0-2
- Remane BRs

* Sun May 05 2019 Fabian Affolter <mail@fabian-affolter.ch> - 1.0.0-1
- Fix files section and add tests
- Update to latest upstream release 1.0.0

* Thu Apr 11 2019 Fabian Affolter <mail@fabian-affolter.ch> - 0.9.6-1
- Update to latest upstream release 0.9.6

* Mon Nov 14 2016 Fabian Affolter <mail@fabian-affolter.ch> - 0.9.4-1
- Update to latest upstream release 0.9.4

* Sun Oct 12 2014 Fabian Affolter <mail@fabian-affolter.ch> - 0.9.1-1
- Initial package for Fedora
