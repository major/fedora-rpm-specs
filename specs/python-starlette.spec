Name:           python-starlette
Version:        0.48.0
Release:        %autorelease
Summary:        The little ASGI library that shines

License:        BSD-3-Clause
URL:            https://www.starlette.io/
Source:         https://github.com/encode/starlette/archive/%{version}/starlette-%{version}.tar.gz

BuildSystem:            pyproject
BuildOption(generate_buildrequires): -x full
BuildOption(install):   -l starlette

BuildArch:      noarch

# The file requirements.txt pins exact versions and contains many unwanted
# dependencies, e.g. linters and typecheckers (see
# https://docs.fedoraproject.org/en-US/packaging-guidelines/Python/#_linters).
# It’s easier to maintain BuildRequires for testing manually than to heavily
# patch or process the requirements file.
BuildRequires:  %{py3_dist pytest}
BuildRequires:  %{py3_dist trio}
BuildRequires:  %{py3_dist typing_extensions}

%global common_description %{expand:
Starlette is a lightweight ASGI framework/toolkit, which is ideal for building
async web services in Python.

It is production-ready, and gives you the following:

  • A lightweight, low-complexity HTTP web framework.
  • WebSocket support.
  • In-process background tasks.
  • Startup and shutdown events.
  • Test client built on requests.
  • CORS, GZip, Static Files, Streaming responses.
  • Session and Cookie support.
  • 100%% test coverage.
  • 100%% type annotated codebase.
  • Few hard dependencies.
  • Compatible with asyncio and trio backends.
  • Great overall performance against independent benchmarks.}

%description %{common_description}


%package -n     python3-starlette
Summary:        %{summary}

%description -n python3-starlette %{common_description}


%pyproject_extras_subpkg -n python3-starlette full


%check -a
%pytest -v


%files -n python3-starlette -f %{pyproject_files}
%doc README.md


%changelog
%autochangelog
