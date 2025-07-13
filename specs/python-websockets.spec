%global pypi_name websockets

%ifarch x86_64
%bcond_without tests
%endif

Name:           python-%{pypi_name}
Version:        15.0.1
Release:        %autorelease
Summary:        Implementation of the WebSocket Protocol for Python

License:        BSD-3-Clause
URL:            https://github.com/aaugustin/websockets
Source0:        %{url}/archive/%{version}/%{pypi_name}-%{version}.tar.gz

BuildRequires:  gcc

%if %{with tests}
BuildRequires:  python3dist(pytest)
%endif

%global _description %{expand:
websockets is a library for developing WebSocket servers and clients in
Python. It implements RFC 6455 with a focus on correctness and simplicity. It
passes the Autobahn Testsuite.

Built on top of Python’s asynchronous I/O support introduced in PEP 3156, it
provides an API based on coroutines, making it easy to write highly concurrent
applications.}

%description %{_description}

%package -n     python3-%{pypi_name}
Summary:        %{summary}
BuildRequires:  python3-devel
BuildRequires:  python3dist(werkzeug)
Requires:       python3dist(werkzeug)

%description -n python3-%{pypi_name} %{_description}

%prep
%autosetup -n %{pypi_name}-%{version} -p1

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files websockets

%check
%pyproject_check_import

%if %{with tests}
# Skip some tests that require network connectivity and/or a running daemon.
# Investigate: test_server_shuts_down_* tests hang or fail on Python 3.12
%pytest -v --ignore compliance --ignore tests/sync -k "not test_explicit_host_port and not test_server_shuts_down and not test_keepalive_is_enabled and not test_close_waits and not test_close_server_keeps_handlers_running and not test_keepalive and not test_keepalive_times_out and not test_close_server_keeps_connections_open and not test_basic_auth_invalid_password"
%endif


%files -n python3-%{pypi_name} -f %{pyproject_files}
%doc README.rst
%license LICENSE
%{_bindir}/websockets

%changelog
%autochangelog
