Name:           python-starlette
Version:        0.45.0
Release:        %autorelease
Summary:        The little ASGI library that shines

License:        BSD-3-Clause
URL:            https://www.starlette.io/
Source:         https://github.com/encode/starlette/archive/%{version}/starlette-%{version}.tar.gz

# Revert test adjustments from 5ccbc62175eece867b498115724eb8d3fa27acb0
# This allows the tests to keep passing with httpx 0.27.x.
#
# Specifically, this reverts:
# https://github.com/encode/starlette/pull/2773/commits/24de2bfc8aa99a084a9b4fcfab1e52d7a6747cd9.
#
# Fixes:
#
# Some tests fail with some supported httpx versions due to whitespace
# differences in JSON responses
# https://github.com/encode/starlette/discussions/2795
#
# We can (and must!) remove this once python-httpx is upgraded to 0.28.x.
Patch:          0001-Revert-test-adjustments-from-5ccbc62175eece867b49811.patch

BuildSystem:            pyproject
BuildOption(install):   -l starlette
BuildOption(generate_buildrequires): -x full

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
# E       trio.TrioDeprecationWarning: The `cancellable=` keyword argument to
#         `trio.to_thread.run_sync` is deprecated since Trio 0.23.0; use
#         `abandon_on_cancel=` instead
#         (https://github.com/python-trio/trio/issues/2841)
warningsfilter="${warningsfilter-} -W ignore::trio.TrioDeprecationWarning"

# E       Failed: DID NOT WARN. No warnings of type (<class
#         'DeprecationWarning'>, <class 'PendingDeprecationWarning'>) were
#         emitted.
# E       The list of emitted warnings is: [].
k="${k-}${k+ and }not test_lifespan_with_on_events"

%pytest ${warningsfilter-} -k "${k-}" -v


%files -n python3-starlette -f %{pyproject_files}
%doc README.md


%changelog
%autochangelog
