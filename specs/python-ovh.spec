Name:           python-ovh
Version:        1.1.2
Release:        3%{?dist}
Summary:        Lightweight wrapper around OVHcloud's APIs

License:        BSD
URL:            https://github.com/ovh/python-ovh
Source:         %{url}/archive/v%{version}/python-ovh-%{version}.tar.gz

BuildArch:      noarch
BuildRequires:  python3-devel
# For building man pages
BuildRequires:  make
BuildRequires:  python3dist(sphinx)
BuildRequires:  python3dist(pytest)

%global _description %{expand:
Lightweight wrapper around OVHcloud's APIs. Handles all the hard work
including credential creation and requests signing.
}

%description %_description

%package -n python3-ovh
Summary:        %{summary}

%description -n python3-ovh %_description


%prep
%autosetup -p1 -n python-ovh-%{version}


%generate_buildrequires
%pyproject_buildrequires -r


%build
%pyproject_wheel
cd docs/ && make man


%install
%pyproject_install
%pyproject_save_files ovh

mkdir -p %{buildroot}/%{_mandir}/man1/
install -m 0644 docs/_build/man/python-ovh.1* %{buildroot}/%{_mandir}/man1/


%check
# Deselect network-dependent tests
%pytest --deselect tests/test_client.py::TestClient::test_endpoints


%files -n python3-ovh -f %{pyproject_files}
%doc examples/ README.rst
%{_mandir}/man1/python-ovh.1*


%changelog
* Sat Jan 18 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Wed Jun 26 2024 Packit <hello@packit.dev> - 1.1.2-1
- Update to version 1.1.2
- Resolves: rhbz#2290895

* Fri Jun 07 2024 Python Maint <python-maint@redhat.com> - 1.1.0-6
- Rebuilt for Python 3.13

* Fri Jan 26 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Wed Jun 14 2023 Python Maint <python-maint@redhat.com> - 1.1.0-2
- Rebuilt for Python 3.12

* Wed May 03 2023 Roman Inflianskas <rominf@aiven.io> - 1.1.0-1
- Update to 1.1.0

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Aug 12 2022 Roman Inflianskas <rominf@aiven.io> - 1.0.0-2
- Add documentation

* Mon Jul 11 2022 Roman Inflianskas <rominf@aiven.io> - 1.0.0-1
- Initial package (rhbz#2106063)

