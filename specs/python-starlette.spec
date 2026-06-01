Name:           python-starlette
Version:        1.2.1
Release:        %autorelease
Summary:        The little ASGI library that shines

License:        BSD-3-Clause
URL:            https://www.starlette.io/
Source:         https://github.com/encode/starlette/archive/%{version}/starlette-%{version}.tar.gz

# Since https://github.com/Kludex/starlette/pull/3291, Starlette prefers
# httpx2, a maintained fork of httpx by the Pydantic people, when it is
# available. Once we have a python-httpx2 package, we can update the
# BuildRequires accordingly. Until then, we (downstream-only) revert the part
# of https://github.com/Kludex/starlette/pull/3295 that adjusted test
# expectations around the accept-encoding header to match httpx2.
Patch:          python-starlette-1.2.0-PR3295-undo.patch

BuildSystem:    pyproject
BuildOption(generate_buildrequires): --extras full
BuildOption(install): --assert-license starlette

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
%pytest --verbose


%files -n python3-starlette -f %{pyproject_files}
%doc README.md


%changelog
%autochangelog
