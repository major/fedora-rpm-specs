%global pypi_name hvac

Name:           python-%{pypi_name}
Version:        2.4.0
Release:        %autorelease
Summary:        HashiCorp Vault API client for Python

License:        Apache-2.0
URL:            https://github.com/hvac/hvac
Source:         %{pypi_source %{pypi_name}}
BuildArch:      noarch

%global _description %{expand:
This package provides a Python API client for HashiCorp Vault.}

%description %{_description}

%package -n     python3-%{pypi_name}
Summary:        %{summary}
BuildRequires:  python3-devel

%description -n python3-%{pypi_name} %{_description}

%prep
%autosetup -n %{pypi_name}-%{version}
# Remove shebangs from non-executable files
find hvac -type f ! -executable -name '*.py' -print -exec sed -r -i -e '1{\@^#!/usr/bin/(env )?python@d}' '{}' +

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files -L hvac

%check
# All test require the "vault" executable, so this is all that we can do:
%pyproject_check_import

%files -n python3-%{pypi_name} -f %{pyproject_files}
%license LICENSE.txt
%doc README.md

%changelog
%autochangelog
