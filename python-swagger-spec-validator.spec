%global srcname swagger-spec-validator

Name:           python-%{srcname}
Version:        2.7.4
Release:        2%{?dist}
Summary:        Validation of Swagger specifications

License:        ASL 2.0
URL:            https://github.com/Yelp/swagger_spec_validator
Source0:        %{pypi_source}
Source1:        %{url}/archive/v%{version}/%{name}-%{version}.tar.gz

BuildArch:      noarch

%global _description %{expand:
%{summary}.}

%description %{_description}

%package     -n python3-%{srcname}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{srcname}}
BuildRequires:  python3-devel
BuildRequires:  python3dist(setuptools)
BuildRequires:  python3dist(jsonschema)
BuildRequires:  python3dist(pyyaml)
BuildRequires:  python3dist(six)
BuildRequires:  python3dist(pytest) >= 3.1.0
BuildRequires:  python3dist(httpretty)
BuildRequires:  python3dist(mock)

%description -n python3-%{srcname} %{_description}

Python 3 version.

%prep
%autosetup -n %{srcname}-%{version} -N
rm -vr *.egg-info
tar -xvf %{S:1} --strip-components=1 --wildcards \
  'swagger_spec_validator-%{version}/LICENSE.txt' \
  'swagger_spec_validator-%{version}/CHANGELOG.rst' \
  'swagger_spec_validator-%{version}/tests/' \
  %{nil}

%build
%py3_build

%install
%py3_install

%check
%python3 -m pytest tests

%files -n python3-%{srcname}
%license LICENSE.txt
%doc README.md CHANGELOG.rst
%{python3_sitelib}/swagger_spec_validator/
%{python3_sitelib}/swagger_spec_validator-*.egg-info/

%changelog
* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.7.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Sun Jul 10 2022 Kevin Fenzi <kevin@scrye.com> - 2.7.4-1
- Update to 2.7.4.

* Thu Jun 16 2022 Python Maint <python-maint@redhat.com> - 2.7.3-6
- Rebuilt for Python 3.11

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.7.3-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.7.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 2.7.3-3
- Rebuilt for Python 3.10

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.7.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Fri Nov 20 2020 Nils Philippsen <nils@redhat.com> - 2.7.3-1
- Update to 2.7.3

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.3-4
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 2.4.3-2
- Rebuilt for Python 3.9

* Fri Jan 31 2020 Igor Raits <ignatenkobrain@fedoraproject.org> - 2.4.3-1
- Initial package
