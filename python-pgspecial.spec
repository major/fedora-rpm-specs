Name:           python-pgspecial
Version:        1.13.1
Release:        %autorelease
Summary:        Python implementation of postgres meta (backslash) commands

License:        BSD-3-Clause
URL:            https://www.dbcli.com
Source0:        %{pypi_source pgspecial}
BuildArch:      noarch

# Add @dbtest decorator for test_slash_dp_pattern_schema
# https://github.com/dbcli/pgspecial/pull/126
Patch:          https://github.com/dbcli/pgspecial/pull/126.patch

BuildRequires:  python3-devel

%global common_description %{expand:
This package provides an API to execute meta-commands (AKA “special”, or
“backslash commands”) on PostgreSQL.}

%description %{common_description}


%package -n     python3-pgspecial
Summary:        %{summary}

%description -n python3-pgspecial %{common_description}


%prep
%autosetup -p1 -n pgspecial-%{version}


%generate_buildrequires
%pyproject_buildrequires -t


%build
%pyproject_wheel


%install
%pyproject_install
%pyproject_save_files pgspecial


%check
# Note that most tests will be skipped since there is not a postgres database
# we can connect to.
%pytest


%files -n python3-pgspecial -f %{pyproject_files}
%license License.txt
%doc README.rst
%doc changelog.rst
%doc DEVELOP.rst


%changelog
%autochangelog
