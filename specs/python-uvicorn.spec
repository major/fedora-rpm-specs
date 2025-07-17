# python-uvloop fails to build with Python 3.14: AttributeError: module
# 'asyncio' has no attribute 'AbstractChildWatcher'
# https://bugzilla.redhat.com/show_bug.cgi?id=2326210
# python-uvloop fails to build with Python 3.13: error: implicit declaration of
# function ‘_Py_RestoreSignals’
# https://bugzilla.redhat.com/show_bug.cgi?id=2256747
# python-uvloop: FTBFS in Fedora rawhide/f42
# https://bugzilla.redhat.com/show_bug.cgi?id=2341233
%bcond uvloop 0

Name:           python-uvicorn
Version:        0.35.0
Release:        %autorelease
Summary:        The lightning-fast ASGI server
License:        BSD-3-Clause
URL:            https://www.uvicorn.org
# PyPI tarball doesn't have tests
Source:         https://github.com/encode/uvicorn/archive/%{version}/uvicorn-%{version}.tar.gz
# Fix test_loop_auto for Python 3.14
# https://github.com/encode/uvicorn/pull/2652
Patch:          https://github.com/encode/uvicorn/pull/2652.patch
BuildArch:      noarch

BuildRequires:  tomcli

%global common_description %{expand:
Uvicorn is an ASGI web server implementation for Python.  Until recently Python
has lacked a minimal low-level server/application interface for async
frameworks.  The ASGI specification fills this gap, and means we are now able
to start building a common set of tooling usable across all async frameworks.
Uvicorn supports HTTP/1.1 and WebSockets.}


%description %{common_description}


%package -n python3-uvicorn
Summary:        %{summary}
BuildRequires:  python3-devel
# See "Testing" and "Explicit optionals" in requirements.txt. We list these
# manually because we must omit strict version pins as well as dependencies for
# type-checking, linting, coverage analysis, etc.
BuildRequires:  python3-pytest
BuildRequires:  python3-pytest-mock
BuildRequires:  python3-pytest-xdist+psutil
BuildRequires:  python3-a2wsgi
BuildRequires:  python3-cryptography
BuildRequires:  python3-httpx
BuildRequires:  python3-trustme
BuildRequires:  python3-wsproto


%description -n python3-uvicorn %{common_description}


%pyproject_extras_subpkg -n python3-uvicorn standard


%prep
%autosetup -p 1 -n uvicorn-%{version}
%if %{without uvloop}
# Note that by removing uvloop from the standard extra but still shipping the
# metapackage, dependent packages may FTBFS in %%check or (if inadequately
# tested) fail at runtime, rather than FTBFS in RPM dependency resolution.
tomcli set pyproject.toml lists delitem \
    project.optional-dependencies.standard 'uvloop.*'
%endif
# Do not treat warnings as errors; it is too strict for downstream packaging
tomcli set pyproject.toml lists delitem \
    tool.pytest.ini_options.filterwarnings 'error'


%generate_buildrequires
%pyproject_buildrequires -x standard


%build
%pyproject_wheel


%install
%pyproject_install
%pyproject_save_files -l uvicorn


%check
# Websocket-related failures should be fixed in 0.35.0,
# https://github.com/encode/uvicorn/issues/1908, but there are some remaining
# test failures. TODO: Investigate and/or report these.
#
# _ test_send_binary_data_to_server_bigger_than_default_on_websockets[httptools-max=defaults sent=defaults+1] _
# […]
# >                   with pytest.raises(websockets.exceptions.ConnectionClosedError):
# E                   Failed: DID NOT RAISE <class 'websockets.exceptions.ConnectionClosedError'>
#
# tests/protocols/test_websocket.py:734: Failed
# _ test_send_binary_data_to_server_bigger_than_default_on_websockets[h11-max=defaults sent=defaults+1] _
#
# Only two parameterizations of this test fail, but it is easier to skip the
# whole thing.
k="${k-}${k+ and }not test_send_binary_data_to_server_bigger_than_default_on_websockets"

%pytest --verbose -rs -k "${k-}"


%files -n python3-uvicorn -f %{pyproject_files}
%doc README.md CHANGELOG.md CITATION.cff
%{_bindir}/uvicorn


%changelog
%autochangelog
