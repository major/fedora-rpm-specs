Name:           python-typing-inspection
Version:        0.4.1
Release:        %autorelease
Summary:        Runtime typing introspection tools

# SPDX
License:        MIT
URL:            https://github.com/pydantic/typing-inspection
Source:         %{pypi_source typing_inspection}

BuildSystem:            pyproject
BuildOption(generate_buildrequires): -g tests
BuildOption(install):   -l typing_inspection

BuildArch:      noarch

BuildRequires:  tomcli

%global common_description %{expand:
This module provides tools to inspect type annotations at runtime.}

%description %{common_description}


%package -n python3-typing-inspection
Summary:        %{summary}

%description -n python3-typing-inspection %{common_description}


%prep -a
# https://docs.fedoraproject.org/en-US/packaging-guidelines/Python/#_linters
tomcli set pyproject.toml lists delitem dependency-groups.tests \
    '(coverage|pytest-cov)\b.*'


%check -a
%pytest


%files -n python3-typing-inspection -f %{pyproject_files}
%doc HISTORY.md
%doc README.md


%changelog
%autochangelog
