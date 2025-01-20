Name:           python-bravado
Version:        11.0.3
Release:        8%{?dist}
Summary:        Library for accessing Swagger-enabled API's

License:        BSD-3-Clause
URL:            https://github.com/Yelp/bravado
# PyPI tarball is missing tests
Source:         %{url}/archive/v%{version}/bravado-%{version}.tar.gz
# https://github.com/Yelp/bravado/pull/485
Patch:          0001-Prefer-getfullargspec-instead-of-deprecated-getargspec.patch
# https://github.com/Yelp/bravado/pull/484
Patch:          0002-Use-standard-library-mock-when-possible.patch
BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  python3-httpretty

%global _description %{expand:
Bravado is a Yelp maintained fork of digium/swagger-py for use with OpenAPI
Specification version 2.0 (previously known as Swagger).}


%description %_description


%package -n     python3-bravado
Summary:        %{summary}


%description -n python3-bravado %_description


%prep
%autosetup -n bravado-%{version} -p 1


%generate_buildrequires
%pyproject_buildrequires -x integration-tests


%build
%pyproject_wheel


%install
%pyproject_install
%pyproject_save_files bravado


%check
# Fido tests require fido, which is deprecated upstream and won't be packaged
%pytest -v \
    --ignore tests/fido_client \
    --ignore tests/integration/fido_client_test.py \
    tests


%files -n python3-bravado -f %{pyproject_files}
%doc README.rst


%changelog
* Sat Jan 18 2025 Fedora Release Engineering <releng@fedoraproject.org> - 11.0.3-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 11.0.3-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Sun Jun 16 2024 Python Maint <python-maint@redhat.com> - 11.0.3-6
- Rebuilt for Python 3.13

* Fri Jan 26 2024 Fedora Release Engineering <releng@fedoraproject.org> - 11.0.3-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 11.0.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 11.0.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Wed Jun 28 2023 Python Maint <python-maint@redhat.com> - 11.0.3-2
- Rebuilt for Python 3.12

* Mon Feb 13 2023 Carl George <carl@george.computer> - 11.0.3-1
- Update to version 11.0.3, resolves rhbz#2169596
- Convert to pyproject macros
- Run tests

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 11.0.2-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 11.0.2-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon Jun 13 2022 Python Maint <python-maint@redhat.com> - 11.0.2-6
- Rebuilt for Python 3.11

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 11.0.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 11.0.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 11.0.2-3
- Rebuilt for Python 3.10

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 11.0.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Nov 18 2020 Nils Philippsen <nils@redhat.com> - 11.0.2-1
- Version 11.0.2

* Tue Sep 08 2020 Aurelien Bompard <abompard@fedoraproject.org> - 10.6.2-1
- Initial package.
