%bcond tests 1
%global forgeurl https://github.com/pydantic/pydantic-settings

Name:           python-pydantic-settings
Version:        2.0.3
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
%pyproject_buildrequires


%build
%pyproject_wheel


%install
%pyproject_install
%pyproject_save_files pydantic_settings


%check
%if %{with tests}
%pytest --ignore=tests/test_docs.py
%endif


%files -n python3-pydantic-settings -f %{pyproject_files}
%doc README.md
%license LICENSE


%changelog
* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Tue Sep 12 2023 Maxwell G <maxwell@gtmx.me> - 2.0.3-1
- Initial package. Closes rhbz#2249134.
