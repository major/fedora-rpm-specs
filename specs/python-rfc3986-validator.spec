Name:           python-rfc3986-validator
Version:        0.1.1
Release:        %autorelease
Summary:        Pure python RFC3986 validator

# SPDX
License:        MIT
URL:            https://github.com/naimetti/rfc3986-validator
Source:         %{pypi_source rfc3986_validator}

BuildSystem:            pyproject
BuildOption(generate_buildrequires): -x test
BuildOption(install):   -l rfc3986_validator

BuildArch:      noarch

BuildRequires:  python3-devel

# Removing deprecated pytest-runner and adding missing test dependencies
# https://github.com/naimetti/rfc3986-validator/pull/3
#
# Fixes:
#
# https://github.com/naimetti/rfc3986-validator/issues/2
# https://fedoraproject.org/wiki/Changes/DeprecatePythonPytestRunner
Patch:          0001_removing_pytest_runner_and_adding_test_requirements.patch

%global common_description %{expand:
%{summary}.}

%description %{common_description}


%package -n python3-rfc3986-validator
Summary: %summary

%description -n python3-rfc3986-validator %{common_description}


%check -a
PYTHONWARNINGS=ignore %pytest -vv tests


%files -n python3-rfc3986-validator -f %{pyproject_files}
%doc HISTORY.rst
%doc README.md


%changelog
%autochangelog
