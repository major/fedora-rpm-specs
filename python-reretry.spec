Name:           python-reretry
Version:        0.11.2
Release:        %autorelease
Summary:        Easy to use retry decorator

License:        Apache-2.0
URL:            https://github.com/leshchenko1979/reretry
# Missing release 0.11.2 on PyPI
# https://github.com/leshchenko1979/reretry/issues/7
# Source0:        %%{pypi_source reretry}
Source0:        %{url}/archive/%{version}/reretry-%{version}.tar.gz

BuildArch:      noarch

BuildRequires:  python3-devel
# Optional dependency; allows preserving function signatures. Add a BR to make
# sure it is available, and so that we test with it.
BuildRequires:  python3dist(decorator)

# Depend explicitly on pytest, not just indirectly via pytest-asyncio in
# tests/requirements.txt.
BuildRequires:  python3dist(pytest)

%global common_description %{expand:
An easy to use retry decorator.

This package is a fork from the retry package, but with some of added
community-sourced features.

Features

New features in reretry:

  • Log traceback of an error that lead to a failed attempt.
  • Call a custom callback after each failed attempt.
  • Can be used with async functions.

From original retry:

  • Retry on specific exceptions.
  • Set a maximum number of retries.
  • Set a delay between retries.
  • Set a maximum delay between retries.
  • Set backoff and jitter parameters.
  • Use a custom logger.
  • No external dependencies (stdlib only).
  • (Optionally) Preserve function signatures (pip install decorator).}

%description %{common_description}


%package -n python3-reretry
Summary:        %{summary}

# Optional dependency; allows preserving function signatures.
Recommends:     python3dist(decorator)

%description -n python3-reretry %{common_description}


%prep
%autosetup -n reretry-%{version}


%generate_buildrequires
export PBR_VERSION='%{version}'
%pyproject_buildrequires tests/test-requirements.txt


%build
export PBR_VERSION='%{version}'
%pyproject_wheel


%install
%pyproject_install
%pyproject_save_files reretry


%check
%pytest


%files -n python3-reretry -f %{pyproject_files}
# pyproject-rpm-macros takes care of LICENSE.txt; verify with “rpm -qL -p …”
%doc README.md


%changelog
%autochangelog
