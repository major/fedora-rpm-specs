# RHEL does not include the test dependencies
%bcond tests %{undefined rhel}

Name:           python-poetry-core
Version:        1.9.0
Release:        %autorelease
Summary:        Poetry PEP 517 Build Backend
# SPDX
License:        MIT
URL:            https://github.com/python-poetry/poetry-core
Source0:        %{url}/archive/%{version}/poetry-core-%{version}.tar.gz

# This patch moves the vendored requires definition
# from vendors/pyproject.toml to pyproject.toml
# Intentionally contains the removed hunk to prevent patch aging
Patch1:         poetry-core-1.9.0-devendor.patch

BuildArch:      noarch
BuildRequires:  python3-devel
BuildRequires:  pyproject-rpm-macros

%if %{with tests}
# for tests (only specified via poetry poetry.dev-dependencies with pre-commit etc.)
BuildRequires:  python3-build
BuildRequires:  python3-pytest
BuildRequires:  python3-pytest-mock
BuildRequires:  python3-setuptools
BuildRequires:  python3-tomli-w
BuildRequires:  python3-virtualenv
BuildRequires:  gcc
BuildRequires:  git-core
%endif


%global _description %{expand:
A PEP 517 build backend implementation developed for Poetry.
This project is intended to be a light weight, fully compliant, self-contained
package allowing PEP 517 compatible build frontends to build Poetry managed
projects.}

%description %_description


%package -n python3-poetry-core
Summary:        %{summary}

# Previous versions of poetry included poetry-core in it
Conflicts:      python%{python3_version}dist(poetry) < 1.1

%description -n python3-poetry-core %_description


%prep
%autosetup -p1 -n poetry-core-%{version}


%generate_buildrequires
%pyproject_buildrequires -r


%build
# we debundle the deps after we use the bundled deps in previous step to parse the deps 🤯
rm -r src/poetry/core/_vendor

%pyproject_wheel


%install
%pyproject_install
%pyproject_save_files poetry


%check
%if %{with tests}
# don't use %%tox here because tox.ini runs "poetry install"
# TODO investigate failures in test_default_with_excluded_data, test_default_src_with_excluded_data
%pytest -k "not with_excluded_data"
%else
%pyproject_check_import
%endif


%files -n python3-poetry-core -f %{pyproject_files}
%doc README.md
%license LICENSE


%changelog
%autochangelog
