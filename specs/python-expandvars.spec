Name:           python-expandvars
Version:        1.1.1
Release:        %autorelease
Summary:        Expand system variables Unix style

# SPDX
License:        MIT
URL:            https://github.com/sayanarijit/expandvars
Source:         %{pypi_source expandvars}

BuildSystem:            pyproject
BuildOption(install):   -l expandvars

BuildArch:      noarch

# Most of the dependencies in the “test” extra and almost everything tox.ini
# pertain to linting and coverage analysis. Rather than working around all of
# these, it is simpler to BR and invoke pytest manually.
# https://docs.fedoraproject.org/en-US/packaging-guidelines/Python/#_linters
BuildRequires:  %{py3_dist pytest}

%global common_description %{expand:
This module is inspired by GNU bash’s variable expansion features. It can be
used as an alternative to Python’s os.path.expandvars function.

A good use case is reading config files with the flexibility of reading values
from environment variables using advanced features like returning a default
value if some variable is not defined.}

%description %{common_description}


%package -n python3-expandvars
Summary:        %{summary}

%description -n python3-expandvars %{common_description}


%prep -a
# https://docs.fedoraproject.org/en-US/packaging-guidelines/Python/#_linters
sed -r -i "s/--cov[^[:blank:]'\"]*[[:blank:]]*//g" pyproject.toml


%check -a
%pytest


%files -n python3-expandvars -f %{pyproject_files}
%doc README.md


%changelog
%autochangelog
