%global pypi_name mdit-py-plugins

Name:           python-%{pypi_name}
Version:        0.3.1
Release:        1%{?dist}
Summary:        Collection of plugins for markdown-it-py

# Both the package and its plugins are licensed under MIT
License:        MIT
URL:            https://github.com/executablebooks/mdit-py-plugins
Source0:        %{url}/archive/v%{version}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3dist(pytest)

%global _description %{expand:
Collection of core plugins for markdown-it-py.
}

%description %_description

%package -n     python3-%{pypi_name}
Summary:        %{summary}

%description -n python3-%{pypi_name} %_description

%prep
%autosetup -p1 -n %{pypi_name}-%{version}

%generate_buildrequires
%pyproject_buildrequires -r

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files mdit_py_plugins

%check
# Skip tests using pytest-regression which is not available in Fedora
%pytest -k "not test_plugin_parse and not test_no_new_line_issue and not test_tokens"

%files -n python3-%{pypi_name} -f %{pyproject_files}
%license LICENSE
%doc README.md

%changelog
* Mon Oct 03 2022 Karolina Surma <ksurma@redhat.com> - 0.3.1-1
- Update to 0.3.1
Resolves: rhbz#2130161

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed Jun 15 2022 Python Maint <python-maint@redhat.com> - 0.3.0-3
- Rebuilt for Python 3.11

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Mon Dec 06 2021 Karolina Surma <ksurma@redhat.com> - 0.3.0-1
- Update to 0.3.0

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.8-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 0.2.8-2
- Rebuilt for Python 3.10

* Thu May 13 2021 Karolina Surma <ksurma@redhat.com> - 0.2.8-1
- Initial package.
