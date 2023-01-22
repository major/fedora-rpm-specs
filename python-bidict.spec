%global pypi_name bidict

Name:           python-%{pypi_name}
Version:        0.22.0
Release:        4%{?dist}
Summary:        Bidirectional mapping library for Python

License:        MPLv2.0
URL:            https://bidict.readthedocs.io
Source0:        https://github.com/jab/bidict/archive/v%{version}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch

%description
Forward declarations for all the custom interpreted text roles that Sphinx
defines and that are used below. This helps Sphinx-unaware tools (e.g.
rst2html, PyPI's and GitHub's renderers, etc.

%package -n     python3-%{pypi_name}
Summary:        %{summary}

BuildRequires:  python3-devel
BuildRequires:  python3dist(coverage)
BuildRequires:  python3dist(hypothesis)
BuildRequires:  python3dist(py)
BuildRequires:  python3dist(pytest)
BuildRequires:  python3dist(pytest-benchmark)
BuildRequires:  python3dist(pytest-cov)
BuildRequires:  python3dist(setuptools)
BuildRequires:  python3dist(sortedcollections)
%{?python_provide:%python_provide python3-%{pypi_name}}

%description -n python3-%{pypi_name}
Forward declarations for all the custom interpreted text roles that Sphinx
defines and that are used below. This helps Sphinx-unaware tools (e.g.
rst2html, PyPI's and GitHub's renderers, etc.

%prep
%autosetup -n %{pypi_name}-%{version} -p1
rm -rf %{pypi_name}.egg-info

%build
%py3_build

%install
%py3_install

%check
%pytest -v tests --ignore=tests/properties/test_properties.py --ignore=tests/properties/_strategies.py

%files -n python3-%{pypi_name}
%license LICENSE
%doc CHANGELOG.rst README.rst
%{python3_sitelib}/%{pypi_name}/
%{python3_sitelib}/%{pypi_name}-%{version}-py%{python3_version}.egg-info/

%changelog
* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.22.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.22.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon Jun 13 2022 Python Maint <python-maint@redhat.com> - 0.22.0-2
- Rebuilt for Python 3.11

* Thu Mar 24 2022 Fabian Affolter <mail@fabian-affolter.ch> - 0.22.0-1
- Update to latest upstream release 0.22.0 (closes rhbz#2067604)

* Wed Jan 26 2022 Fabian Affolter <mail@fabian-affolter.ch> - 0.21.4-1
- Update to latest upstream release 0.21.4 (closes rhbz#2016795)

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.21.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Sun Sep 05 2021 Fabian Affolter <mail@fabian-affolter.ch> - 0.21.3-1
- Update to latest upstream release 0.21.3 (closes rhbz#2001344)

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.21.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 0.21.2-3
- Rebuilt for Python 3.10

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.21.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Sep 08 2020 Fabian Affolter <mail@fabian-affolter.ch> - 0.21.2-1
- Initial package for Fedora
