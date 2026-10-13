Name:           python-proxy-py
Version:        2.4.10
Release:        %autorelease
Summary:        Lightweight, pluggable HTTP proxy server and framework

License:        BSD-3-Clause
URL:            https://github.com/abhinavsingh/proxy.py
Source:         %{pypi_source proxy_py}
# Fix the test suite with pytest-asyncio >= 1.0
# Not yet submitted upstream
Patch:          proxy-py-pytest-asyncio-1.patch

BuildArch:      noarch
BuildRequires:  python3-devel
# Test dependencies; the upstream "testing" extra pins exact versions and
# pulls in linters and release tooling, so it is not used here
BuildRequires:  python3dist(pytest)
BuildRequires:  python3dist(pytest-asyncio)
BuildRequires:  python3dist(pytest-mock)
BuildRequires:  python3dist(httpx)
BuildRequires:  python3dist(h2)
BuildRequires:  python3dist(requests)
BuildRequires:  openssl

%global _description %{expand:
proxy.py is a fast, lightweight, pluggable proxy server written in Python
with no external dependencies. Features include HTTP, HTTPS and HTTP/2
proxying, TLS interception, reverse proxy, a built-in web server, SOCKS,
DNS-over-HTTPS and a plugin framework for writing custom proxy and web
server extensions, plus PubSub and work acceptor/executor frameworks.}

%description %_description

%package -n     python3-proxy-py
Summary:        %{summary}
# Used to generate certificates for TLS interception
Recommends:     openssl
Recommends:     python3-proxy-py-bin

%description -n python3-proxy-py %_description

%pyproject_extras_subpkg -n python3-proxy-py metrics tunnel

%package -n     python3-proxy-py-bin
Summary:        Command line interface of the proxy.py server
Requires:       python3-proxy-py = %{version}-%{release}
# Both ship /usr/bin/proxy
Conflicts:      libproxy-bin
# Retired in Fedora 45, but still ships /usr/bin/proxy in older releases
Conflicts:      golang-github-google-martian

%description -n python3-proxy-py-bin %_description

This package contains the proxy command to run the proxy.py server.


%prep
%autosetup -p1 -n proxy_py-%{version}
# Upstream pins exact versions of optional dependencies; relax them and drop
# the typing stubs, which are not needed at runtime
sed --in-place --expression='s/==/>=/' \
               --expression='/types-paramiko/d' \
               setup.cfg
# Do not install the .gitignore with the package data
rm proxy/common/.gitignore
# setup.cfg points to a non-existent LICENSE.md
sed --in-place 's/LICENSE\.md/LICENSE/' setup.cfg
# Do not install /usr/bin/grout: it only bootstraps a client for the hosted
# jaxl.io tunneling service, executing Python code downloaded from it, and it
# conflicts with the grout package
sed --in-place '/grout = proxy:grout/d' setup.cfg
# Drop coverage, junit and warnings-as-errors options from pytest config
sed --in-place --expression='/-p pytest_cov/,/--cov-config/d' \
               --expression='/--junitxml/d' \
               --expression='/^filterwarnings/,/^  error/d' \
               pytest.ini


%generate_buildrequires
%pyproject_buildrequires -x metrics,tunnel


%build
%pyproject_wheel


%install
%pyproject_install
%pyproject_save_files -l proxy


%check
# These tests need network access
%pytest \
    --ignore tests/integration \
    --deselect tests/test_grout.py \
    --deselect tests/http/proxy/test_http2.py \
    --deselect tests/http/test_client.py::TestClient::test_http \
    --deselect tests/http/test_client.py::TestClient::test_client \
    --deselect tests/test_main.py::TestProxyContextManager::test_proxy_context_manager


%files -n python3-proxy-py -f %{pyproject_files}
%doc README.md CHANGELOG.md

%files -n python3-proxy-py-bin
%{_bindir}/proxy


%changelog
%autochangelog
