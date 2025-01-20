%bcond tests 1
# The azure-key-vault extra needs python-azure-keyvault-secrets>=4.8.0, but
# azure-cli is not ready:
# https://src.fedoraproject.org/rpms/python-azure-keyvault-secrets/pull-request/1
%bcond azure_key_vault 0

%global forgeurl https://github.com/pydantic/pydantic-settings

Name:           python-pydantic-settings
Version:        2.7.1
%forgemeta
Release:        2%{?dist}
Summary:        Settings management using pydantic

License:        MIT
URL:            %{forgeurl}
Source:         %{forgesource}

BuildArch:      noarch

BuildRequires:  python3-devel
%if %{with tests}
BuildRequires:  %{py3_dist pytest}
BuildRequires:  %{py3_dist pytest-mock}
%endif

%global _description %{expand:
Settings management using pydantic.}

%description %_description


%package -n python3-pydantic-settings
Summary:        %{summary}

%description -n python3-pydantic-settings %_description


%prep
%autosetup -p1 %{forgesetupargs}


%generate_buildrequires
%pyproject_buildrequires -x yaml,toml%{?with_azure_key_vault:,azure-key-vault}


%build
%pyproject_wheel


%install
%pyproject_install
%pyproject_save_files -l pydantic_settings


%check
%if %{with tests}
ignore="${ignore-} --ignore=tests/test_docs.py"
%if %{without azure_key_vault}
ignore="${ignore-} --ignore tests/test_source_azure_key_vault.py"
%endif

%pytest ${ignore-} -rs -v
%endif


%files -n python3-pydantic-settings -f %{pyproject_files}
%doc README.md


%pyproject_extras_subpkg -n python3-pydantic-settings yaml toml %{?with_azure_key_vault:azure-key-vault}


%changelog
* Sat Jan 18 2025 Fedora Release Engineering <releng@fedoraproject.org> - 2.7.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Tue Dec 31 2024 Benjamin A. Beasley <code@musicinmybrain.net> - 2.7.1-1
- Update to 2.7.1 (close RHBZ#2335052)

* Fri Dec 13 2024 Benjamin A. Beasley <code@musicinmybrain.net> - 2.7.0-1
- Update to 2.7.0 (close RHBZ#2332265)

* Mon Nov 11 2024 Benjamin A. Beasley <code@musicinmybrain.net> - 2.6.1-1
- Update to 2.6.1 (close RHBZ#2319359)

* Wed Sep 11 2024 Benjamin A. Beasley <code@musicinmybrain.net> - 2.5.2-1
- Update to 2.5.2 (close RHBZ#2311161)

* Tue Jul 30 2024 Benjamin A. Beasley <code@musicinmybrain.net> - 2.4.0-1
- Update to 2.4.0 (close RHBZ#2301611)

* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.4-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Sun Jun 30 2024 Benjamin A. Beasley <code@musicinmybrain.net> - 2.3.4-3
- Fix regex flags accidentally passed as count in test code (fix RHBZ#2291856)

* Sat Jun 29 2024 Python Maint <python-maint@redhat.com> - 2.3.4-2
- Rebuilt for Python 3.13

* Mon Jun 24 2024 Benjamin A. Beasley <code@musicinmybrain.net> - 2.3.4-1
- Update to 2.3.4 (close RHBZ#2293966)

* Sat Jun 15 2024 Benjamin A. Beasley <code@musicinmybrain.net> - 2.3.3-1
- Update to 2.3.3 (close RHBZ#2292137)

* Wed Jun 12 2024 Benjamin A. Beasley <code@musicinmybrain.net> - 2.3.2-1
- Update to 2.3.2 (close RHBZ#2291331)

* Wed Jun 05 2024 Benjamin A. Beasley <code@musicinmybrain.net> - 2.3.1-1
- Update to 2.3.1 (close RHBZ#2290582)

* Tue Jun 04 2024 Benjamin A. Beasley <code@musicinmybrain.net> - 2.3.0-1
- Update to 2.3.0 (close RHBZ#2284609)

* Thu Feb 22 2024 Benjamin A. Beasley <code@musicinmybrain.net> - 2.2.1-1
- Update to 2.2.1

* Mon Feb 19 2024 Benjamin A. Beasley <code@musicinmybrain.net> - 2.2.0-1
- Update to 2.2.0 (close RHBZ#2264579)
- Add metapackages for new yaml and toml extras
- Do not package a duplicate LICENSE file

* Fri Jan 26 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Tue Sep 12 2023 Maxwell G <maxwell@gtmx.me> - 2.0.3-1
- Initial package. Closes rhbz#2249134.
