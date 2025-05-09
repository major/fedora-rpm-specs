%bcond tests 1

Name:           python-rfc3339-validator
Version:        0.1.4
Release:        %autorelease
Summary:        Pure python RFC3339 validator

# SPDX
License:        MIT
URL:            https://github.com/naimetti/rfc3339-validator
Source:         %{pypi_source rfc3339_validator}

BuildSystem:            pyproject
BuildOption(install):   -l rfc3339_validator

BuildArch:      noarch

# Drop the pytest-runner test dependency and “setup.py test” support
# https://github.com/naimetti/rfc3339-validator/pull/7
#
# Fixes:
#
# Consider dropping the pytest-runner test dependency
# https://github.com/naimetti/rfc3339-validator/issues/6
#
# See also the deprecation notice at https://pypi.org/project/pytest-runner/.
#
# This version of the patch has been modified to apply to the PyPI sdist, which
# does not contain requirements_dev.txt; see:
#
# Include files for tox testing in the sdist
# https://github.com/naimetti/rfc3339-validator/pull/8
Patch:          rfc3339-validator-0.1.4-drop-pytest-runner.patch

%if %{with tests}
# We use manual BR’s rather than generating dependencies from tox (which uses
# requirements_dev.txt) because dependencies there are pinned to exact versions
# and most of them are linter, coverage, and other tools that we would need to
# patch out.
BuildRequires:  %{py3_dist pytest}
BuildRequires:  %{py3_dist hypothesis}
BuildRequires:  %{py3_dist strict-rfc3339}
%endif

%global common_description %{expand:
A pure python RFC3339 validator.}

%description %{common_description}


%package -n python3-rfc3339-validator
Summary:        %{summary}

%description -n python3-rfc3339-validator %{common_description}


%check -a
%if %{with tests}
%pytest
%endif


%files -n python3-rfc3339-validator -f %{pyproject_files}
%doc CONTRIBUTING.rst
%doc HISTORY.rst
%doc README.md


%changelog
%autochangelog
