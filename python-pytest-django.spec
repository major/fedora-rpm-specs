%global pypi_name pytest-django

Name:           python-%{pypi_name}
Version:        4.1.0
Release:        10%{?dist}
Summary:        A Django plugin for pytest

License:        BSD
URL:            https://pytest-django.readthedocs.io/
Source0:        %{pypi_source}
BuildArch:      noarch

%description
pytest-django allows you to test your Django project/applications with the
pytest testing tool.

%package -n     python3-%{pypi_name}
Summary:        %{summary}

BuildRequires:  python3-devel
BuildRequires:  python3-django
BuildRequires:  python3-django-configurations
BuildRequires:  python3-pytest
BuildRequires:  python3-setuptools
BuildRequires:  python3-setuptools_scm
BuildRequires:  python3-six
%{?python_provide:%python_provide python3-%{pypi_name}}

%description -n python3-%{pypi_name}
pytest-django allows you to test your Django project/applications with the
pytest testing tool.

%package -n python-%{pypi_name}-doc
Summary:        Documentation for %{name}

BuildRequires:  python3-sphinx
BuildRequires:  python3-sphinx_rtd_theme

%description -n python-%{pypi_name}-doc
Documentation for %{name}.

%prep
%autosetup -n %{pypi_name}-%{version}
rm -rf %{pypi_name}.egg-info
sed -i -e '/NAME/s|/|/var/tmp/|' pytest_django_test/settings_sqlite{,_file}.py

%build
%py3_build
PYTHONPATH=${PWD} sphinx-build-3 docs html
rm -rf html/.{doctrees,buildinfo}

%install
%py3_install

#%check
#export PYTHONPATH="%{buildroot}%{python3_sitelib}:$PWD"
#for settings in sqlite sqlite_file; do
#  export DJANGO_SETTINGS_MODULE=pytest_django_test.settings_${settings}
#  %python3 -m pytest -v tests
#done

%files -n python3-%{pypi_name}
%license LICENSE
%doc README.rst
%{python3_sitelib}/pytest_django/
%{python3_sitelib}/pytest_django-%{version}-py*.egg-info/

%files -n python-%{pypi_name}-doc
%doc html
%license LICENSE

%changelog
* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 4.1.0-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jun 29 2023 Python Maint <python-maint@redhat.com> - 4.1.0-9
- Rebuilt for Python 3.12

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 4.1.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 4.1.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Tue Jun 14 2022 Python Maint <python-maint@redhat.com> - 4.1.0-6
- Rebuilt for Python 3.11

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 4.1.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 4.1.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 4.1.0-3
- Rebuilt for Python 3.10

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 4.1.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Fri Nov 13 2020 Joel Capitao <jcapitao@redhat.com> - 4.1.0-1
- Update to 4.1.0

* Thu Aug 13 2020 Fabian Affolter <mail@fabian-affolter.ch> - 3.8.0-6
- Remove pathlib2

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.8.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 3.8.0-4
- Rebuilt for Python 3.9

* Sat Mar 21 2020 Fabian Affolter <mail@fabian-affolter.ch> - 3.8.0-3
- Disable tests

* Sat Feb 01 2020 Fabian Affolter <mail@fabian-affolter.ch> - 3.8.0-2
- Bump release

* Fri Jan 31 2020 Igor Raits <ignatenkobrain@fedoraproject.org> - 3.8.0-1
- Enable tests
- Update to 3.8.0

* Tue Jan 07 2020 Fabian Affolter <mail@fabian-affolter.ch> - 3.7.0-2
- Use var for source URL
- Better use of wildcards (rhbz#1786920)

* Sat Dec 28 2019 Fabian Affolter <mail@fabian-affolter.ch> - 3.7.0-1
- Initial package for Fedora
