Name:           python-engineio
Version:        4.11.2
Release:        %autorelease
Summary:        Python Engine.IO server and client

# SPDX
License:        MIT
URL:            https://github.com/miguelgrinberg/python-engineio/
# The PyPY sdist now contains documentation and tests, but it still lacks the
# CHANGES.md file, so we continue to use a GitHub archive.
Source:         %{url}/archive/v%{version}/python-engineio-%{version}.tar.gz

# Downstream-only: patch out test coverage analysis
# https://docs.fedoraproject.org/en-US/packaging-guidelines/Python/#_linters
Patch:          0001-Downstream-only-patch-out-test-coverage-analysis.patch

BuildArch:      noarch
 
BuildRequires:  python3-devel

%global common_description %{expand:
Engine.IO is a lightweight transport protocol that enables real-time
bidirectional event-based communication between clients (typically, though not
always, web browsers) and a server. The official implementations of the client
and server components are written in JavaScript. This package provides Python
implementations of both, each with standard and asyncio variants.}

%description %{common_description}


%package -n     python3-engineio
Summary:        %{summary}

# Dropped in F41; can be removed in F45.
Obsoletes:      python-engineio-doc < 4.9.1-3

%description -n python3-engineio %{common_description}


%pyproject_extras_subpkg -n python3-engineio client asyncio_client


%prep
%autosetup -p1

# Remove pre-compiled/pre-minified browser build of
# https://github.com/socketio/engine.io from the examples, just to prove it is
# not shipped.
find examples -type f -name 'engine.io.js' -print -delete


%generate_buildrequires
%pyproject_buildrequires -x client,asyncio_client -t


%build
%pyproject_wheel


%install
%pyproject_install
%pyproject_save_files -l engineio


%check
# Since we may skip some tests, let’s do a “smoke test” for completeness. We
# omit the async drivers for eventlet (retired in Fedora 41 and later), gevent,
# and uwsgi, since there are no integration tests for them and they are not
# otherwise BuildRequires, and we don’t want to add them solely for this
# purpose.
%{pyproject_check_import \
    -e engineio.async_drivers.eventlet \
    -e engineio.async_drivers.gevent \
    -e engineio.async_drivers.gevent_uwsgi }

%pytest ${ignore-} -k "${k-}"


%files -n python3-engineio -f %{pyproject_files}
%doc CHANGES.md
%doc README.md
%doc SECURITY.md


%changelog
%autochangelog
