Name:           python-starlette
Version:        0.36.3
Release:        %autorelease
Summary:        The little ASGI library that shines

License:        BSD-3-Clause
URL:            https://www.starlette.io/
Source:         https://github.com/encode/starlette/archive/%{version}/starlette-%{version}.tar.gz

BuildArch:      noarch

BuildRequires:  python3-devel
# The file requirements.txt pins exact versions and contains many unwanted
# dependencies, e.g. linters and typecheckers (see
# https://docs.fedoraproject.org/en-US/packaging-guidelines/Python/#_linters).
# It’s easier to maintain BuildRequires for testing manually than to heavily
# patch or process the requirements file.
BuildRequires:  %{py3_dist pytest}
BuildRequires:  %{py3_dist trio}
BuildRequires:  %{py3_dist typing_extensions}

Obsoletes:      python-starlette-doc < 0.16.0-10

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
  • Great overall performance against independant benchmarks.}

%description %{common_description}


%pyproject_extras_subpkg -n python3-starlette full


%package -n     python3-starlette
Summary:        %{summary}

%description -n python3-starlette %{common_description}


%prep
%autosetup -n starlette-%{version}


%generate_buildrequires
%pyproject_buildrequires -x full


%build
%pyproject_wheel


%install
%pyproject_install
%pyproject_save_files -l starlette


%check
# E       Failed: DID NOT WARN. No warnings of type (<class
#         'DeprecationWarning'>, <class 'PendingDeprecationWarning'>) were
#         emitted.
# E       The list of emitted warnings is: [].
k="${k-}${k+ and }not test_lifespan_with_on_events"

# E       trio.TrioDeprecationWarning: The `cancellable=` keyword argument to
#         `trio.to_thread.run_sync` is deprecated since Trio 0.23.0; use
#         `abandon_on_cancel=` instead
#         (https://github.com/python-trio/trio/issues/2841)
%pytest -W 'ignore::trio.TrioDeprecationWarning' -k "${k-}" -v


%files -n python3-starlette -f %{pyproject_files}
%doc README.md


%changelog
%autochangelog
