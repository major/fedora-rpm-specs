Name:           python-esp-pylib
Version:        1.1.4
Release:        %autorelease
Summary:        Library for logging, utils and constants for Espressif Systems' projects
License:        Apache-2.0
URL:            https://github.com/espressif/esp-pylib
Source:         %{pypi_source esp_pylib}

BuildArch:      noarch
BuildRequires:  python3-devel

%global _description %{expand:
Python library for logging, utils and constants for Espressif Systems'
Python projects.}

%description %_description

%package -n     python3-esp-pylib
Summary:        %{summary}

%description -n python3-esp-pylib %_description


%pyproject_extras_subpkg -n python3-esp-pylib cli,ide,serial


%prep
%autosetup -p1 -n esp_pylib-%{version}


%generate_buildrequires
%pyproject_buildrequires -x cli,ide,serial,test


%build
%pyproject_wheel


%install
%pyproject_install
%pyproject_save_files -l esp_pylib


%check
%pyproject_check_import
%pytest


%files -n python3-esp-pylib -f %{pyproject_files}
%doc README.md


%changelog
%autochangelog
