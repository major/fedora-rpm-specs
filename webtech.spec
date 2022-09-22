Name:           webtech
Version:        1.2.11
Release:        4%{?dist}
Summary:        Tool to identify technologies used on websites

License:        GPLv3+
URL:            https://github.com/ShielderSec/webtech
Source0:        https://github.com/ShielderSec/webtech/archive/%{version}/%{name}-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  python3-setuptools

Requires:       %{py3_dist requests}

%description
WebTech is a Python software that can identify web technologies by visiting
a given website, parsing a single response file or replaying a request 
described in a text file. This way you can have reproducible results and
minimize the requests you need to make to a target website.

%prep
%autosetup -n %{name}-%{version}
sed -i -e '/^#!\//, 1d' webtech/*.py

%build
%py3_build

%install
%py3_install

%files
%doc README.md
%license LICENSE
%{_bindir}/%{name}
%{python3_sitelib}/%{name}-*.egg-info/
%{python3_sitelib}/%{name}/

%changelog
* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.11-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon Jun 13 2022 Python Maint <python-maint@redhat.com> - 1.2.11-3
- Rebuilt for Python 3.11

* Sat Jan 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.11-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Aug 25 2021 Fabian Affolter <mail@fabian-affolter.ch> - 1.2.11-1%{?dist}
- Update to latest upstream release 1.2.11 (rhbz#1937553)

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.9-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 1.2.9-3
- Rebuilt for Python 3.10

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.9-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Dec 29 2020 Fabian Affolter <mail@fabian-affolter.ch> - 1.2.9-1
- Update to latest upstream release 1.2.9

* Sun Aug 09 2020 Fabian Affolter <mail@fabian-affolter.ch> - 1.2.8-1
- Update to latest upstream release 1.2.8

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.7-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 1.2.7-7
- Rebuilt for Python 3.9

* Fri Feb 07 2020 Fabian Affolter <mail@fabian-affolter.ch> - 1.2.7-6
- Update source URL

* Fri Jan 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.7-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 1.2.7-4
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 1.2.7-3
- Rebuilt for Python 3.8

* Sat Jul 27 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.7-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun May 12 2019 Fabian Affolter <mail@fabian-affolter.ch> - 1.2.7-1
- Update to latest upstream relase 1.2.7

* Sun Apr 28 2019 Fabian Affolter <mail@fabian-affolter.ch> - 1.2.6-1
- Update to latest upstream relase 1.2.6

* Thu Apr 11 2019 Fabian Affolter <mail@fabian-affolter.ch> - 1.2.5-1
- Initial package
