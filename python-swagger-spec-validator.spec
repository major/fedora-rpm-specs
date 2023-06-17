Name:           python-swagger-spec-validator
Version:        3.0.3
Release:        2%{?dist}
Summary:        Validation of Swagger specifications

License:        Apache-2.0
URL:            https://github.com/Yelp/swagger_spec_validator
Source:         %{url}/archive/v%{version}/swagger-spec-validator-%{version}.tar.gz
# https://github.com/Yelp/swagger_spec_validator/pull/163
Patch:          0001-Add-missing-setuptools-dependency.patch

BuildArch:      noarch
BuildRequires:  python3-devel
BuildRequires:  python3-pytest

%global _description %{expand:
Swagger Spec Validator is a Python library that validates Swagger Specs against
the Swagger 1.2 or Swagger 2.0 specification. The validator aims to check for
full compliance with the Specification.}


%description %{_description}

%package     -n python3-swagger-spec-validator
Summary:        %{summary}


%description -n python3-swagger-spec-validator %{_description}


%prep
%autosetup -n swagger_spec_validator-%{version} -p 1


%generate_buildrequires
%pyproject_buildrequires


%build
%pyproject_wheel


%install
%pyproject_install
%pyproject_save_files swagger_spec_validator


%check
%pytest -v tests


%files -n python3-swagger-spec-validator -f %{pyproject_files}
%doc README.md CHANGELOG.rst


%changelog
* Thu Jun 15 2023 Python Maint <python-maint@redhat.com> - 3.0.3-2
- Rebuilt for Python 3.12

* Tue Feb 14 2023 Carl George <carl@george.computer> - 3.0.3-1
- Update to version 3.0.3, resolves rhbz#2169878
- Convert to pyproject macros
- Add setuptools dependency

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.7.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

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
