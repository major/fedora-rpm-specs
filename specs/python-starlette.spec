Name:           python-starlette
Version:        1.7.0
Release:        %autorelease
Summary:        The little ASGI library that shines

License:        BSD-3-Clause
URL:            https://www.starlette.io/
%global forgeurl https://github.com/encode/starlette
Source:         %{forgeurl}/archive/%{version}/starlette-%{version}.tar.gz

# Make it possible to run the tests without blockbuster
# https://github.com/Kludex/starlette/pull/3576
Patch:          %{forgeurl}/pull/3576.patch

BuildSystem:    pyproject
BuildOption(generate_buildrequires): --extras full
BuildOption(install): --assert-license starlette

BuildArch:      noarch

# The “dev” dependency group pins exact versions and contains many unwanted
# dependencies, e.g. linters and typecheckers (see
# https://docs.fedoraproject.org/en-US/packaging-guidelines/Python/#_linters).
# It’s easier to maintain BuildRequires for testing manually.
BuildRequires:  %{py3_dist httpx2[zstd]}
BuildRequires:  %{py3_dist pytest}
BuildRequires:  %{py3_dist trio}
BuildRequires:  %{py3_dist typing_extensions}
# For blockbuster, see https://github.com/cbornet/blockbuster/issues/46 for why
# we would prefer not to package it.

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


%package -n python3-starlette
Summary:        %{summary}

%description -n python3-starlette %{common_description}


%pyproject_extras_subpkg --name python3-starlette full


%check -a
# Requires python3dist(opentelemetry-sdk), formerly built from
# https://src.fedoraproject.org/rpms/python-opentelemetry, now retired and
# neither simple nor pleasant to bring back.
ignore="${ignore-} --ignore=tests/middleware/test_opentelemetry.py"

%pytest ${ignore-} --verbose


%files -n python3-starlette -f %{pyproject_files}
%doc README.md


%changelog
%autochangelog
