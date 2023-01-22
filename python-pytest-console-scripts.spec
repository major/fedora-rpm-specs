Name:           python-pytest-console-scripts
Version:        1.3.1
Release:        2%{?dist}
Summary:        Pytest plugin for testing console scripts
License:        MIT
URL:            https://github.com/kvas-it/pytest-console-scripts
Source:         %{pypi_source pytest-console-scripts}

BuildArch:      noarch
BuildRequires:  python3-devel


%global _description %{expand:
Pytest-console-scripts is a pytest plugin for running python
scripts from within tests.}


%description %_description

%package -n     python3-pytest-console-scripts
Summary:        %{summary}

%description -n python3-pytest-console-scripts %_description


%prep
%autosetup -p1 -n pytest-console-scripts-%{version}


%generate_buildrequires
%pyproject_buildrequires -t


%build
%pyproject_wheel


%install
%pyproject_install
%pyproject_save_files pytest_console_scripts


%check
%tox


%files -n python3-pytest-console-scripts -f %{pyproject_files}
%doc README.md


%changelog
* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Mon Nov 28 2022 Lumír Balhar <lbalhar@redhat.com> - 1.3.1-1
- Initial package