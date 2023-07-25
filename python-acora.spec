%global pypi_name acora

Name:           python-%{pypi_name}
Version:        2.2
Release:        17%{?dist}
Summary:        A Python multi-keyword text search engine

License:        BSD
URL:            https://github.com/scoder/acora
Source0:        https://github.com/scoder/acora/archive/%{pypi_name}-%{version}.tar.gz

BuildRequires:  gcc

%description
Acora is 'fgrep' for Python, a fast multi-keyword text search engine.

Based on a set of keywords and the Aho-Corasick algorithm, it generates a
search automaton and runs it over string input, either unicode or bytes.

Acora comes with both a pure Python implementation and a fast binary module
written in Cython. However, note that the current construction algorithm is
not suitable for really large sets of keywords (i.e. more than a couple of
thousand).

%package -n python3-%{pypi_name}
Summary:        %{summary}

BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
BuildRequires:  python3-Cython
%{?python_provide:%python_provide python3-%{pypi_name}}

%description -n python3-%{pypi_name}
Acora is 'fgrep' for Python, a fast multi-keyword text search engine.

Based on a set of keywords and the Aho-Corasick algorithm, it generates a
search automaton and runs it over string input, either unicode or bytes.

Acora comes with both a pure Python implementation and a fast binary module
written in Cython. However, note that the current construction algorithm is
not suitable for really large sets of keywords (i.e. more than a couple of
thousand).

%prep
%autosetup -n acora-%{pypi_name}-%{version}

%build
%py3_build

%install
%py3_install

%check
%{__python3} setup.py test

%files -n python3-%{pypi_name}
%doc README.rst
%license LICENSE.txt
%{python3_sitearch}/%{pypi_name}/
%{python3_sitearch}/%{pypi_name}*.egg-info

%changelog
* Sun Jul 23 2023 Python Maint <python-maint@redhat.com> - 2.2-17
- Rebuilt for Python 3.12

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.2-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Tue Jun 13 2023 Python Maint <python-maint@redhat.com> - 2.2-15
- Rebuilt for Python 3.12

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.2-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.2-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon Jun 13 2022 Python Maint <python-maint@redhat.com> - 2.2-12
- Rebuilt for Python 3.11

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.2-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.2-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 2.2-9
- Rebuilt for Python 3.10

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.2-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.2-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 2.2-6
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 2.2-4
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 2.2-3
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jun 20 2019 Fabian Affolter <mail@fabian-affolter.ch> - 2.2-1
- Initial package for Fedora
