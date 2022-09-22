# Created by pyp2rpm-3.3.2
%global pkg_name jaraco-classes
%global pypi_name jaraco.classes
# waiting on jaraco-packaging and rst-linker to build docs
%bcond_with doc

Name:           python-%{pkg_name}
Version:        3.2.1
Release:        8%{?dist}
Summary:        Utility functions for Python class constructs

License:        MIT
URL:            https://github.com/jaraco/jaraco.classes
Source0:        %{pypi_source %{pypi_name}}
BuildArch:      noarch
 
%description
Utility functions for Python class constructs.

%package -n python3-%{pkg_name}
Summary:        %{summary}
Requires:       python3-jaraco
Requires:       python3dist(six)

BuildConflicts: python3dist(pytest) = 3.7.3
BuildRequires:  python3-devel
BuildRequires:  python3dist(pytest) >= 3.4
BuildRequires:  python3dist(more-itertools)

BuildRequires:  python3dist(setuptools)
BuildRequires:  python3dist(setuptools-scm) >= 1.15

%{?python_provide:%python_provide python3-%{pkg_name}}

%description -n python3-%{pkg_name}
Utility functions for Python class constructs.

%if %{with docs}
%package -n python-%{pkg_name}-doc
Summary:        jaraco-classes documentation

BuildRequires:  python3dist(pytest-checkdocs)
BuildRequires:  python3dist(sphinx)
BuildRequires:  python3dist(jaraco-packaging) >= 3.2
BuildRequires:  python3dist(rst-linker) >= 1.9

%description -n python-%{pkg_name}-doc
Documentation for jaraco-classes
%endif

%prep
%autosetup -n jaraco.classes-%{version}
# disable flake8 in the tests, need a newer version of pytest-flake8
# https://src.fedoraproject.org/rpms/python-pytest-flake8/pull-request/2
# AttributeError: 'Application' object has no attribute 'make_notifier'
sed -i 's/ --flake8//' pytest.ini
sed -i 's/ --black//' pytest.ini
sed -i 's/ --cov//' pytest.ini

%build
%py3_build
%if %{with docs}
# generate html docs 
PYTHONPATH=${PWD} sphinx-build-3 docs html
# remove the sphinx-build leftovers
rm -rf html/.{doctrees,buildinfo}
%endif

%install
%py3_install

%check
LANG=C.utf-8 %{__python3} -m pytest --ignore=build

%files -n python3-%{pkg_name}
%license LICENSE
%doc README.rst
%{python3_sitelib}/jaraco/classes
%{python3_sitelib}/jaraco.classes-%{version}-py%{python3_version}.egg-info
# These excludes are provided by python3-jaraco
%exclude %{python3_sitelib}/jaraco/__init__*
%exclude %{python3_sitelib}/jaraco/__pycache__/__init__*
%exclude %dir %{python3_sitelib}/jaraco/__pycache__
%exclude %dir %{python3_sitelib}/jaraco

%if %{with docs}
%files -n python-%{pkg_name}-doc
%doc html
%license LICENSE
%endif

%changelog
* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 3.2.1-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon Jun 13 2022 Python Maint <python-maint@redhat.com> - 3.2.1-7
- Rebuilt for Python 3.11

* Wed Feb 09 2022 Dan Radez <dradez@redhat.com> - 3.2.1-6
- Don't delete egginfo

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 3.2.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 3.2.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 3.2.1-3
- Rebuilt for Python 3.10

* Thu Mar 04 2021 Miro Hrončok <mhroncok@redhat.com> - 3.2.1-2
- Don't co-own /usr/lib/python3.X/site-packages/jaraco

* Tue Feb 23 2021 Dan Radez <dradez@redhat.com> - 3.2.1-1
- Update to 3.2.1

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 3.1.0-2
- Rebuilt for Python 3.9

* Wed Feb 12 2020 Dan Radez <dan@radez.net> - 3.1.0
- update to 3.1.0

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Mon Nov 11 2019 Ken Dreyer <kdreyer@redhat.com> - 2.0-7
- Set minimum pytest version to 3.4 for compatibility with el8

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 2.0-6
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Thu Aug 22 2019 Dan Radez <dradez@redhat.com> - 2.0-5
- Removing the sed . to _ it's confusing and not needed

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 2.0-4
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Mon Apr 08 2019 Dan Radez <dradez@redhat.com> - 2.0-2
- fixed egg info

* Tue Apr 02 2019 Dan Radez <dradez@redhat.com> - 2.0-1
- Initial package.
