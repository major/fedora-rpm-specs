Name:           python-zeroconf
Version:        0.118.0
Release:        %autorelease
Summary:        Pure Python Multicast DNS Service Discovery Library

License:        LGPL-2.1-or-later
URL:            https://github.com/jstasiak/python-zeroconf
Source0:        %{url}/archive/%{version}/zeroconf-%{version}.tar.gz

BuildRequires:  gcc
BuildRequires:  python3-devel
BuildRequires:  python3-pytest
BuildRequires:  python3-pytest-asyncio


%description
A pure Python implementation of multicast DNS service discovery
supporting Bonjour/Avahi.

%package -n     python3-zeroconf
Summary:        %{summary}

%description -n python3-zeroconf
A pure Python 3 implementation of multicast DNS service discovery
supporting Bonjour/Avahi.


%prep
%autosetup -p1
# Upstream requires this for https://github.com/python-poetry/poetry/issues/7505
# But it's not relevant for the RPM package
sed -i 's/poetry-core>=1.5.2/poetry-core/' pyproject.toml
# We don't measure coverage in tests
sed -Ei 's/--cov(-|=)[^ "]+//g' pyproject.toml


%generate_buildrequires
%pyproject_buildrequires


%build
# Explicitly choose to compile the Cython extensions
export REQUIRE_CYTHON=1
%pyproject_wheel


%install
%pyproject_install
%pyproject_save_files zeroconf


%check
# IPv6 tests fail in Koji/mock, test_sending_unicast uses IPv6
%pytest -v -k "not test_sending_unicast and not test_integration_with_listener_ipv6"


%files -n python3-zeroconf -f %{pyproject_files}
%doc README.rst


%changelog
%autochangelog
