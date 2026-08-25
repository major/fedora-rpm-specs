%global forgeurl https://github.com/oprypin/pytest-golden
Version:        1.0.1
%forgemeta

Name:           python-pytest-golden
Release:        %autorelease
Summary:        Plugin for pytest that offloads expected outputs to data files

License:        MIT
URL:            %{forgeurl}
Source:         %{forgesource}

BuildArch:      noarch
BuildRequires:  python3-devel
BuildRequires:  python3-pytest

%global _description %{expand:
This package provides a plugin for pytest that offloads expected outputs to
data files.}

%description %_description

%package -n     python3-pytest-golden
Summary:        %{summary}

%description -n python3-pytest-golden %_description

%prep
%forgeautosetup -p1

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files -L pytest_golden

%check
%pyproject_check_import
%pytest -v

%files -n python3-pytest-golden -f %{pyproject_files}
%license LICENSE.md
%doc README.md

%changelog
%autochangelog
