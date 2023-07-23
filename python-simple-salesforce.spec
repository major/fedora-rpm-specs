%global pypi_name simple-salesforce
%global pypi_version 1.12.4
%global commit e3393bbcaf3d9651f11e3014c3c8cdc44d39a305
%global shortcommit %(c=%{commit}; echo ${c:0:7})

Name:           python-%{pypi_name}
Version:        %{pypi_version}
Release:        2%{?dist}
Summary:        Simple Salesforce is a basic Salesforce.com REST API client built for Python
License:        ASL 2.0
URL:            https://github.com/%{pypi_name}/%{pypi_name}
Source0:        %{url}/archive/%{commit}/%{pypi_name}-%{shortcommit}.tar.gz

BuildArch:      noarch
BuildRequires:  python3-devel
BuildRequires:  python3dist(setuptools)
# Tests requirements:
BuildRequires:  python3dist(cryptography)
BuildRequires:  python3dist(pytest)
BuildRequires:  python3dist(pytz)
BuildRequires:  python3dist(responses)

%global _description %{expand:
Simple Salesforce is a basic Salesforce.com REST API client built for Python.
The goal is to provide a very low-level interface to the REST Resource and APEX
API, returning a dictionary of the API JSON response. }

%description %{_description}

%package -n     python3-%{pypi_name}
Summary:        %{summary}

%description -n python3-%{pypi_name}
%{_description}

%prep
%autosetup -p1 -n %{pypi_name}-%{commit}
%generate_buildrequires
%pyproject_buildrequires -r

%build
%pyproject_wheel

%check
%pytest

%install
%pyproject_install
%pyproject_save_files simple_salesforce

%files -n python3-%{pypi_name} -f %{pyproject_files}
%doc README.rst docs/user_guide docs/changes.rst docs/conf.py
%license LICENSE.txt

%changelog
* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.12.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jul 06 2023 Roman Inflianskas <rominf@aiven.io> - 1.12.4-1
- Update to 1.12.4
- Rebuilt for Python 3.12 (resolve rhbz#2220501)
- Simplify testing

* Mon Jul 03 2023 Python Maint <python-maint@redhat.com> - 1.11.5-5
- Rebuilt for Python 3.12

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.11.5-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.11.5-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed Jun 15 2022 Python Maint <python-maint@redhat.com> - 1.11.5-2
- Rebuilt for Python 3.11

* Mon Feb 28 2022 Paul Wouters <paul.wouters@aiven.io> - 1.11.5-1
- Initial package
