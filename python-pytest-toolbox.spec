%global pypi_name pytest-toolbox

Name:           python-%{pypi_name}
Version:        0.4
Release:        13%{?dist}
Summary:        Numerous useful plugins for pytest

License:        MIT
URL:            https://github.com/samuelcolvin/pytest-toolbox
Source0:        https://github.com/samuelcolvin/pytest-toolbox/archive/v%{version}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch

%description
Numerous useful plugins for pytest.

%package -n     python3-%{pypi_name}
Summary:        %{summary}
 
BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
BuildRequires:  python3-pytest
BuildRequires:  python3-pytest-isort
BuildRequires:  python3-pytest-timeout
BuildRequires:  python3-pydantic
%{?python_provide:%python_provide python3-%{pypi_name}}

%description -n python3-%{pypi_name}
Numerous useful plugins for pytest.

%prep
%autosetup -n %{pypi_name}-%{version}
rm -rf %{pypi_name}.egg-info

%build
%py3_build

%install
%py3_install

%check
PYTHONPATH=%{buildroot}%{python3_sitelib} pytest-%{python3_version} -v tests \
  -k "not test_any_int_false and not test_is_uuid_false" \
  -W default::DeprecationWarning
rm -rf %{buildroot}%{python3_sitelib}/pytest_toolbox/__pycache__/*.cpython-%{python3_version_nodots}-PYTEST.pyc

%files -n python3-%{pypi_name}
%doc README.rst
%{python3_sitelib}/pytest_toolbox/
%{python3_sitelib}/pytest_toolbox-%{version}-py%{python3_version}.egg-info

%changelog
* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.4-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.4-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Tue Jun 14 2022 Python Maint <python-maint@redhat.com> - 0.4-11
- Rebuilt for Python 3.11

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.4-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.4-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jun 08 2021 Benjamin A. Beasley <code@musicinmybrain.net> - 0.4-8
- Add python3-pytest-timeout BR
- Do not error out on DeprecationWarning in the tests; in this case, the
  DeprecationWarning was due to
  https://github.com/samuelcolvin/pydantic/issues/2786
- Fixes RHBZ#1928054

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 0.4-7
- Rebuilt for Python 3.10

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.4-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.4-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 0.4-4
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Mon Jan 06 2020 Fabian Affolter <mail@fabian-affolter.ch> - 0.4-2
- Update removal of test files (rhbz#1787450)

* Thu Jan 02 2020 Fabian Affolter <mail@fabian-affolter.ch> - 0.4-1
- Initial package for Fedora
