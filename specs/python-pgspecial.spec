Name:           python-pgspecial
Version:        2.2.1
Release:        %autorelease
Summary:        Python implementation of postgres meta (backslash) commands

License:        BSD-3-Clause
URL:            https://www.dbcli.com
Source:         %{pypi_source pgspecial}

BuildSystem:            pyproject
BuildOption(install):   -L pgspecial

BuildArch:      noarch

# See the dev extra; but it has too many linters, etc., so we list these
# manually.
BuildRequires:  %{py3_dist pytest}
BuildRequires:  %{py3_dist configobj}

%global common_description %{expand:
This package provides an API to execute meta-commands (AKA “special”, or
“backslash commands”) on PostgreSQL.}

%description %{common_description}


%package -n     python3-pgspecial
Summary:        %{summary}

%description -n python3-pgspecial %{common_description}


%check -a
# Note that most tests will be skipped since there is not a postgres database
# we can connect to.
%pytest


%files -n python3-pgspecial -f %{pyproject_files}
%license License.txt
%doc README.rst
%doc changelog.rst


%changelog
%autochangelog
