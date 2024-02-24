%bcond tests 1
%global forgeurl https://github.com/pydantic/pydantic-settings

Name:           python-pydantic-settings
Version:        2.2.0
%forgemeta
Release:        1%{?dist}
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
%pyproject_buildrequires -x yaml,toml


%build
%pyproject_wheel


%install
%pyproject_install
%pyproject_save_files -l pydantic_settings


%check
%if %{with tests}
%pytest --ignore=tests/test_docs.py
%endif


%files -n python3-pydantic-settings -f %{pyproject_files}
%doc README.md


%pyproject_extras_subpkg -n python3-pydantic-settings yaml toml


%changelog
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
