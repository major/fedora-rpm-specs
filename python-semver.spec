%global modname semver

Name:           python-%{modname}
Version:        2.13.0
Release:        10%{?dist}
Summary:        Python helper for Semantic Versioning

License:        BSD
URL:            https://github.com/k-bx/python-semver
Source0:        %{url}/archive/%{version}/%{modname}-%{version}.tar.gz

BuildArch:      noarch

%global _description \
Python module for semantic versioning. Simplifies comparing versions.

%description %{_description}

%package     -n python3-%{modname}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{modname}}
BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
BuildRequires:  python3-pytest

%description -n python3-%{modname} %{_description}

Python 3 version.

%prep
%autosetup
# Remove settings for coverage from setup.cfg
sed -i '/-cov[=-]/d' setup.cfg
# Fix tests for Python 3.10
# Proposed upstream: https://github.com/python-semver/python-semver/pull/336
sed -i 's/TypeError: __init__() got an unexpected/TypeError: ...__init__() got an unexpected/' docs/usage.rst

%build
%py3_build

%install
%py3_install

%check
py.test-%{python3_version} -v

%files -n python3-%{modname}
%license LICENSE.txt
%doc README.rst CHANGELOG.rst
%{_bindir}/py%{modname}
%{python3_sitelib}/%{modname}-*.egg-info/
%{python3_sitelib}/%{modname}.py
%{python3_sitelib}/__pycache__/%{modname}.*

%changelog
* Thu Jun 15 2023 Python Maint <python-maint@redhat.com> - 2.13.0-10
- Rebuilt for Python 3.12

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.13.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.13.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon Jun 13 2022 Python Maint <python-maint@redhat.com> - 2.13.0-7
- Rebuilt for Python 3.11

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.13.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.13.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 2.13.0-4
- Rebuilt for Python 3.10

* Tue Feb 16 2021 Lumír Balhar <lbalhar@redhat.com> - 2.13.0-3
- Fixed tests for Python 3.10
Resolves: rhbz#1906368

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.13.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Dec 08 2020 Lumír Balhar <lbalhar@redhat.com> - 2.13.0-1
- Update to 2.13.0 (#1767192)

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.8.1-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 2.8.1-7
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.8.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 2.8.1-5
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 2.8.1-4
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.8.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.8.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Aug 10 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 2.8.1-1
- Update to 2.8.1

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.8.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Sun Jul 08 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 2.8.0-1
- Update to 2.8.0

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 2.7.8-3
- Rebuilt for Python 3.7

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.7.8-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Sun Aug 27 2017 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 2.7.8-1
- Update to 2.7.8

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.7.7-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Thu Jun 08 2017 Igor Gnatenko <ignatenko@redhat.com> - 2.7.7-1
- Update to 2.7.7

* Thu Feb 09 2017 Igor Gnatenko <ignatenko@redhat.com> - 2.7.5-1
- Update to 2.7.5

* Sat Jan 28 2017 Igor Gnatenko <ignatenko@redhat.com> - 2.7.4-1
- Initial package
