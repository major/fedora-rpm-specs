%global pretty_name RangeHTTPServer
%global pypi_name rangehttpserver

%global desc %{expand: \
SimpleHTTPServer with support for Range requests.}

Name:           python-%{pypi_name}
Version:        1.2.0
Release:        18%{?dist}
Summary:        SimpleHTTPServer with support for Range requests

License:        ASL 2.0
URL:            https://github.com/danvk/RangeHTTPServer
Source0:        %{url}/archive/%{version}/%{pretty_name}-%{version}.tar.gz
BuildArch:      noarch
 
BuildRequires: python3-devel
BuildRequires: python3dist(pytest)
BuildRequires: python3dist(requests)
BuildRequires: python3dist(setuptools)
BuildRequires: python3dist(nose)

%description
%{desc}

%package -n python3-%{pypi_name}
Summary: %{summary}
%{?python_provide:%python_provide python3-%{pypi_name}}
 
Requires: python3dist(requests)
%description -n python3-%{pypi_name}
%{desc}

%prep
%autosetup -n %{pretty_name}-%{version}
rm -rf %{pretty_name}.egg-info

find . -type f -name "*.py" -exec sed -i '/^#![  ]*\/usr\/bin\/env.*$/ d' {} ';'

# the server_test removed because need network
# Upstream Issue
# https://github.com/danvk/RangeHTTPServer/issues/21
rm -rf tests/server_test.py

chmod 0644 RangeHTTPServer/__init__.py RangeHTTPServer/__main__.py

%build
%py3_build

%install
%py3_install

%check
PYTHONPATH=. pytest-3

%files -n python3-%{pypi_name}
%license LICENSE
%doc README
%{python3_sitelib}/%{pretty_name}
%{python3_sitelib}/rangehttpserver-%{version}-py%{python3_version}.egg-info

%changelog
* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.0-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.0-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon Jun 13 2022 Python Maint <python-maint@redhat.com> - 1.2.0-16
- Rebuilt for Python 3.11

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.0-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.0-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 1.2.0-13
- Rebuilt for Python 3.10

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.0-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.0-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 1.2.0-10
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 1.2.0-8
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 1.2.0-7
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 15 2019 Luis Bazan <lbazan@fedoraproject.org> - 1.2.0-5
- Fix comment #15 in BZ 1665563.

* Mon Jan 21 2019 Luis Bazan <lbazan@fedoraproject.org> - 1.2.0-4
- Fix comment #6 in BZ 1665563.

* Mon Jan 14 2019 Luis Bazan <lbazan@fedoraproject.org> - 1.2.0-3
- Fix comment #1 in BZ 1665563.

* Fri Jan 11 2019 Luis Bazan <lbazan@fedoraproject.org> - 1.2.0-2
- Initial package.

* Sat Oct 15 2016 Mathieu Bridon <bochecha@daitauha.fr> - 1.2.0-1
- Initial package for Fedora.
