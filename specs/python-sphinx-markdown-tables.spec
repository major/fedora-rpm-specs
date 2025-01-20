%global srcname sphinx-markdown-tables

Name:           python-%{srcname}
Version:        0.0.17
Release:        9%{?dist}
Summary:        Sphinx extension for rendering markdown tables
License:        GPL-3.0-only

URL:            https://github.com/ryanfox/%{srcname}
Source0:        %{pypi_source %srcname}
BuildArch:      noarch

BuildRequires:  python3-devel


%description
A Sphinx extension for rendering tables written in markdown.


%package -n python3-%{srcname}
Summary:        Sphinx extension for rendering markdown tables

%description -n python3-%{srcname}
A Sphinx extension for rendering tables written in markdown.


%prep
%autosetup -p1 -n %{srcname}-%{version}
# Fix exec perms on LICENSE
chmod -x LICENSE


%generate_buildrequires
%pyproject_buildrequires -r


%build
%pyproject_wheel


%install
%pyproject_install
%pyproject_save_files sphinx_markdown_tables

# Drop incorrectly installed LICENSE
rm -f %{buildroot}%{_prefix}/LICENSE


%check
%pyproject_check_import


%files -n python3-%{srcname} -f %{pyproject_files}
%license LICENSE
%doc README.md


%changelog
* Sat Jan 18 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.17-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.17-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Fri Jun 07 2024 Python Maint <python-maint@redhat.com> - 0.0.17-7
- Rebuilt for Python 3.13

* Fri Jan 26 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.17-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.17-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.17-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Tue Jun 13 2023 Python Maint <python-maint@redhat.com> - 0.0.17-3
- Rebuilt for Python 3.12

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.17-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Sun Aug 14 2022 Sandro Mani <manisandro@gmail.com> - 0.0.17-1
- Update to 0.0.17

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.15-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon Jun 13 2022 Python Maint <python-maint@redhat.com> - 0.0.15-4
- Rebuilt for Python 3.11

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.15-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Tue Nov 16 2021 Sandro Mani <manisandro@gmail.com> - 0.0.15-2
- Use pyproject_check_import

* Sun Nov 14 2021 Sandro Mani <manisandro@gmail.com> - 0.0.15-1
- Initial package
