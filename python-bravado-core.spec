Name:           python-bravado-core
Version:        5.17.1
Release:        2%{?dist}
Summary:        Library for adding Swagger support to clients and servers

License:        BSD-3-Clause
URL:            https://github.com/Yelp/bravado-core
# PyPI tarball is missing tests
Source:         %{url}/archive/v%{version}/bravado-core-%{version}.tar.gz
# https://github.com/Yelp/bravado-core/pull/393
Patch:          0001-Use-standard-library-mock-when-possible.patch
BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  python3-pytest

%global _description %{expand:
bravado-core is a Python library that adds client-side and server-side support
for the OpenAPI Specification v2.0.}


%description %_description


%package -n     python3-bravado-core
Summary:        %{summary}


%description -n python3-bravado-core %_description


%prep
%autosetup -n bravado-core-%{version} -p 1


%generate_buildrequires
%pyproject_buildrequires


%build
%pyproject_wheel


%install
%pyproject_install
%pyproject_save_files bravado_core


%check
# Recursive tests seem to hang forever, skip for now
# Profiling tests require pytest-benchmark[histogram], skip for now
%pytest -v \
    -k 'not recursive' \
    --ignore tests/profiling


%files -n python3-bravado-core -f %{pyproject_files}
%doc README.rst


%changelog
* Tue Jun 27 2023 Python Maint <python-maint@redhat.com> - 5.17.1-2
- Rebuilt for Python 3.12

* Mon Feb 13 2023 Carl George <carl@george.computer> - 5.17.1-1
- Update to version 5.17.1, resolves rhbz#2169589
- Convert to pyproject macros
- Run tests

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 5.17.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 5.17.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon Jun 13 2022 Python Maint <python-maint@redhat.com> - 5.17.0-6
- Rebuilt for Python 3.11

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 5.17.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 5.17.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 5.17.0-3
- Rebuilt for Python 3.10

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 5.17.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Sep 08 2020 Aurelien Bompard <abompard@fedoraproject.org> - 5.17.0-1
- Initial package.
