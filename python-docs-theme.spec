Name:           python-docs-theme
Version:        2023.3.1
Release:        1%{?dist}
Summary:        The Sphinx theme for the CPython docs and related projects

License:        PSF-2.0
URL:            https://github.com/python/python-docs-theme/
Source:         %{url}archive/%{version}/%{name}-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  python3-devel

%global _description Python Docs Sphinx Theme is the theme for the Python documentation.

%description
%_description

%package -n     python3-docs-theme
Summary:        %{summary}

%description -n python3-docs-theme
%_description

%prep
%autosetup

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files python_docs_theme

%files -n python3-docs-theme -f %{pyproject_files}
%license LICENSE
%doc README.rst

%changelog
* Mon Mar 27 2023 Karolina Surma <ksurma@redhat.com> - 2023.3.1-1
- Update to 2023.3.1
Resolves: rhbz#2177169

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2022.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2022.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon Jun 13 2022 Python Maint <python-maint@redhat.com> - 2022.1-3
- Rebuilt for Python 3.11

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2022.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Mon Jan 17 2022 Miro Hrončok <mhroncok@redhat.com> - 2022.1-1
- Update to 2022.1
Resolves: rhbz#2039234

* Tue Nov 02 2021 Karolina Surma <ksurma@redhat.com> - 2021.11.1-1
- Update to 2021.11.1
Resolves: rhbz#2011890

* Wed Sep 01 2021 Karolina Surma <ksurma@redhat.com> - 2021.8-1
- Update to 2021.8
Resolves: rhbz#1998331

* Tue Jul 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2021.5-3
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 2021.5-2
- Rebuilt for Python 3.10

* Tue May 18 2021 Karolina Surma <ksurma@redhat.com> - 2021.5-1
- Update to 2021.05
Resolves: rhbz#1958505

* Thu Mar 04 2021 Karolina Surma <ksurma@redhat.com> - 2020.12-1
- Initial package.
