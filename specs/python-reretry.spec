Name:           python-reretry
Version:        0.11.8
Release:        %autorelease
Summary:        Easy to use retry decorator

License:        Apache-2.0
URL:            https://github.com/leshchenko1979/reretry
# Missing release 0.11.2 on PyPI
# https://github.com/leshchenko1979/reretry/issues/7
# Source:         %%{pypi_source reretry}
Source:         %{url}/archive/%{version}/reretry-%{version}.tar.gz

BuildSystem:            pyproject
BuildOption(generate_buildrequires): tests/test-requirements.txt
BuildOption(install):   -l reretry

BuildArch:      noarch

# Optional dependency; allows preserving function signatures. Add a BR to make
# sure it is available, and so that we test with it.
BuildRequires:  %{py3_dist decorator}

# Depend explicitly on pytest, not just indirectly via pytest-asyncio in
# tests/requirements.txt.
BuildRequires:  %{py3_dist pytest}

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
Recommends:     %{py3_dist decorator}

%description -n python3-reretry %{common_description}


%check -a
%pytest


%files -n python3-reretry -f %{pyproject_files}
%doc README.md


%changelog
%autochangelog
