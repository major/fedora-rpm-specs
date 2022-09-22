%global srcname   enrich
%global pkgname   python-enrich
%global forge_url https://github.com/pycontribs/%{srcname}
%global common_description %{expand:
rich library functionality with a set of changes that were not accepted
to rich itself.
}

%bcond_without tests

Name:           %{pkgname}
Version:        1.2.7
%forgemeta
Release:        %autorelease
Summary:        Enrich adds few missing features to the wonderful rich library
URL:            %{forge_url}
Source:         %{pypi_source}
License:        MIT
BuildArch:      noarch
patch:          0001-remove-unsuported-pytest-option.patch
patch:          0002_remove_pytest_plus_dependency.patch

BuildRequires:  python3-devel
BuildRequires:  pyproject-rpm-macros

%description %{common_description}

%package -n python3-%{srcname}
Summary: %summary

%description -n python3-%{srcname} %{common_description}

%prep
%autosetup -p1 -n %{srcname}-%{version}

%generate_buildrequires
%pyproject_buildrequires -r %{?with_tests: -x test}

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files %{srcname}

%if %{with tests}
%check
PYTHONPATH=src %{python3} -m pytest src/enrich/test -v -k "not test_rich_console_ex"
%endif

%files -n python3-%{srcname}
%license LICENSE
%{python3_sitelib}/enrich/
%{python3_sitelib}/enrich-%{version}.dist-info/

%changelog
* Fri Sep 16 2022 Chedi Toueiti <chedi.toueiti@gmail.com> - 1.2.7-5
- Disabling faulty test and modernizing the spec file

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.7-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Tue Jun 14 2022 Python Maint <python-maint@redhat.com> - 1.2.7-3
- Rebuilt for Python 3.11

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.7-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jan 13 2022 Chedi Toueiti <chedi.toueiti@gmail.com> - 1.2.7-1
- Update to version 1.2.7 (#2038962)

* Tue Jul 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.6-4
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 1.2.6-3
- Rebuilt for Python 3.10

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Dec 22 2020 Chedi Toueiti <chedi.toueiti@gmail.com> - 1.2.6-1
- Initial commit
