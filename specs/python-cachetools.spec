Name:           python-cachetools
Version:        5.5.1
Release:        %autorelease
Summary:        Extensible memoizing collections and decorators

# SPDX
License:        MIT
URL:            https://pypi.python.org/pypi/cachetools
Source:         %{pypi_source cachetools}

BuildArch:      noarch
BuildRequires:  python3-devel

# cachetools is a direct runtime dependency of tox,
# so we don't use tox to generate test dependencies or run tests
BuildRequires:  python3-pytest

%global _description\
This module provides various memoizing collections and decorators,\
including a variant of the Python 3 Standard Library @lru_cache\
function decorator.\
\
This module provides multiple cache implementations based on different\
cache algorithms, as well as decorators for easily memoizing function\
and method calls.\


%description %_description

%package -n python3-cachetools
Summary:        %{summary}

%description -n python3-cachetools %_description

%prep
%autosetup -n cachetools-%{version}

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files -l cachetools

%check
%pytest

%files -n python3-cachetools -f %{pyproject_files}
%doc CHANGELOG.rst README.rst

%changelog
%autochangelog
