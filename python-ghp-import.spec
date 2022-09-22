Name:           python-ghp-import
Version:        2.1.0
Release:        3%{?dist}
Summary:        GitHub Pages Import
BuildArch:      noarch

License:        ASL 2.0
URL:            https://github.com/c-w/ghp-import
Source0:        %{pypi_source ghp-import}

BuildRequires:  python3-devel


%description
GitHub Pages Import.


%package -n python3-ghp-import
Summary:        %{summary}
Obsoletes:      python3-ghp-import2 < 1.0.1-12
Provides:       python3-ghp-import2 = %{version}-%{release}

%description -n python3-ghp-import
GitHub Pages Import.


%prep
%autosetup -p1 -n ghp-import-%{version}


%generate_buildrequires
%pyproject_buildrequires -r


%build
%pyproject_wheel


%install
%pyproject_install
%pyproject_save_files ghp_import

# Remove shebang on non-executable script
sed -i '1{/^#!/d}' %{buildroot}%{python3_sitelib}/ghp_import.py


%check
%py3_check_import ghp_import


%files -n python3-ghp-import -f %{pyproject_files}
%doc README.md
%license LICENSE
%{_bindir}/ghp-import



%changelog
* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon Jun 13 2022 Python Maint <python-maint@redhat.com> - 2.1.0-2
- Rebuilt for Python 3.11

* Tue May 03 2022 Sandro Mani <manisandro@gmail.com> - 2.1.0-1
- Update to 2.1.0

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Jan 05 2022 Sandro Mani <manisandro@gmail.com> - 2.0.2-1
- Update to 2.0.2

* Mon Sep 27 2021 Sandro Mani <manisandro@gmail.com> - 2.0.1-4
- Fix ASL2.0 -> ASL 2.0
- Strip shebang on non-executable script

* Fri Sep 03 2021 Sandro Mani <manisandro@gmail.com> - 2.0.1-3
- Run %%py3_check_import ghp_import in %%check

* Thu Sep 02 2021 Sandro Mani <manisandro@gmail.com> - 2.0.1-2
- Port to new Python guidelines
- Obsolete/provide python3-ghp-import2

* Wed Sep 01 2021 Sandro Mani <manisandro@gmail.com> - 2.0.1-1
- Initial package
