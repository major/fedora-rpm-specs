Name:           python-pyyaml-env-tag
Version:        0.1
Release:        13%{?dist}
Summary:        A custom YAML tag for referencing environment variables in YAML files
BuildArch:      noarch

License:        MIT
URL:            https://github.com/waylan/pyyaml-env-tag
Source0:        %{pypi_source pyyaml_env_tag}

BuildRequires:  python3-devel

%description
A custom YAML tag for referencing environment variables in YAML files.


%package -n python3-pyyaml-env-tag
Summary:        %{summary}

%description -n python3-pyyaml-env-tag
A custom YAML tag for referencing environment variables in YAML files.


%prep
%autosetup -p1 -n pyyaml_env_tag-%{version}


%generate_buildrequires
%pyproject_buildrequires -r


%build
%pyproject_wheel


%install
%pyproject_install
%pyproject_save_files yaml_env_tag


%check
%{python3} test_yaml_env_tag.py


%files -n python3-pyyaml-env-tag -f %{pyproject_files}
%doc README.md
%license LICENSE


%changelog
* Sat Jan 18 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.1-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.1-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Fri Jun 07 2024 Python Maint <python-maint@redhat.com> - 0.1-11
- Rebuilt for Python 3.13

* Fri Jan 26 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.1-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.1-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.1-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Tue Jun 13 2023 Python Maint <python-maint@redhat.com> - 0.1-7
- Rebuilt for Python 3.12

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon Jun 13 2022 Python Maint <python-maint@redhat.com> - 0.1-4
- Rebuilt for Python 3.11

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Sep 02 2021 Sandro Mani <manisandro@gmail.com> - 0.1-2
- Port to new Python guidelines

* Wed Sep 01 2021 Sandro Mani <manisandro@gmail.com> - 0.1-1
- Initial package
