%global pypi_name pytzdata

%global _description %{expand:
The Olson timezone database for Python.}

Name: python-%{pypi_name}
Version: 2020.1
Release: 9%{?dist}

License: MIT
Summary: Timezone database for Python
URL: https://github.com/sdispater/%{pypi_name}
Source0: %{pypi_source}
# Cleo was updated to 1.0.0a5 because the latest version of poetry needed it.
# It changed the way how some modules are imported and this patch should fix it.
Patch: 0001-Adapt-imports-to-the-latest-version-of-cleo.patch
BuildArch: noarch

BuildRequires: python3-devel

%description %_description

%package -n python3-%{pypi_name}
Summary: %{summary}

%description -n python3-%{pypi_name} %_description

%prep
%autosetup -n %{pypi_name}-%{version} -p1

%generate_buildrequires
%pyproject_buildrequires -r

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files %{pypi_name}

%check
%pyproject_check_import

%files -n python3-%{pypi_name} -f %{pyproject_files}
%license LICENSE
%doc README.rst

%changelog
* Mon Oct 10 2022 Tomáš Hrnčiar <thrnciar@redhat.com> - 2020.1-9
- Add patch to fix cleo imports

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2020.1-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jun 16 2022 Python Maint <python-maint@redhat.com> - 2020.1-7
- Rebuilt for Python 3.11

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2020.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Sun Dec 12 2021 Vitaly Zaitsev <vitaly@easycoding.org> - 2020.1-5
- Converted SPEC to 201x-era guidelines.

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2020.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 2020.1-3
- Rebuilt for Python 3.10

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2020.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Dec 14 2020 Vitaly Zaitsev <vitaly@easycoding.org> - 2020.1-1
- Updated to version 2020.1.

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2019.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jun 24 2020 Vitaly Zaitsev <vitaly@easycoding.org> - 2019.3-2
- Added python3-setuptools to build requirements.

* Thu Jun 18 2020 Vitaly Zaitsev <vitaly@easycoding.org> - 2019.3-1
- Initial SPEC release.
