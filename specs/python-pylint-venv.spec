Name:           python-pylint-venv
Version:        3.0.4
Release:        %autorelease
Summary:        Make pylint respect virtualenvs

%global forgeurl https://github.com/jgosmann/pylint-venv/
%global tag v%{version}
%forgemeta

License:        MIT
URL:            %forgeurl
Source:         %forgesource

BuildArch:      noarch
BuildRequires:  python3-devel
BuildRequires:  pylint

%global _description %{expand:
Pylint does not respect the currently activated virtualenv if it is not
installed in every virtual environment individually. This module provides a
Pylint init-hook to use the same Pylint installation with different virtual
environments.}

%description %_description


%package -n python3-pylint-venv
Summary:        %{summary}
%description -n python3-pylint-venv %_description


%prep
%forgeautosetup -p1


%generate_buildrequires
%pyproject_buildrequires


%build
%pyproject_wheel


%install
%pyproject_install
%pyproject_save_files -L pylint_venv


%check
%{py3_test_envvars} test/test.sh
%pyproject_check_import


%files -n python3-pylint-venv -f %{pyproject_files}
%license LICENSE.txt
%doc README.rst CHANGES.md


%changelog
%autochangelog
