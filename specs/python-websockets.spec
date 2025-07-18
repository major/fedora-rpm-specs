%global pypi_name websockets

Name:           python-%{pypi_name}
Version:        15.0.1
Release:        %autorelease
Summary:        Implementation of the WebSocket Protocol for Python

License:        BSD-3-Clause
URL:            https://github.com/aaugustin/websockets
Source0:        %{url}/archive/%{version}/%{pypi_name}-%{version}.tar.gz

# Fix help(websockets) when werkzeug isn't installed
# This makes %%pyproject_check_import pass without werkzeug
Patch:          https://github.com/python-websockets/websockets/commit/3128f5619d.patch
# Fix from websockets.(asyncio|sync).router import * without werkzeug
# This makes the tests pass without werkzeug as well
Patch:          https://github.com/python-websockets/websockets/pull/1639.patch

BuildRequires:  gcc
BuildRequires:  python3dist(pytest)

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

%pytest -v


%files -n python3-%{pypi_name} -f %{pyproject_files}
%doc README.rst
%license LICENSE
%{_bindir}/websockets

%changelog
%autochangelog
