%global undername python_socks

%global _description %{expand:
The python-socks package provides a core proxy client functionality for Python.
Supports SOCKS4(a), SOCKS5, HTTP (tunneling) proxy and provides sync and async
(asyncio, trio) APIs. It is used internally by aiohttp-socks and
httpx-socks packages.
}

Name:           python-socks
Version:        2.4.3
Release:        %autorelease
Summary:        Core proxy (SOCKS4, SOCKS5, HTTP tunneling) functionality for Python

License:        Apache-2.0
URL:            https://github.com/romis2012/%{name}
Source0:        %{url}/archive/v%{version}/%{name}-%{version}.tar.gz

BuildArch:      noarch

%description %_description

%package -n python3-socks
Summary:        %{summary}
BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
# curio is discontinued upstream and not ready for Python 3.12
Obsoletes:      python3-socks+curio < 2.0.3-7

%description -n python3-socks %_description

# extras: asyncio, trio
%pyproject_extras_subpkg -n python3-socks asyncio trio

%prep
%autosetup

# remove version lock
# https://github.com/romis2012/python-socks/blob/master/requirements-dev.txt
# remove curio
# remove linters and coverage
# remove fixes
sed -i -e 's/pytest-asyncio=.*/pytest-asyncio/' \
    -e '/curio/d' \
    -e '/flake8/d' -e '/cov/d' \
    -e 's/pytest=.*$/pytest/' requirements-dev.txt

%generate_buildrequires
%pyproject_buildrequires -r requirements-dev.txt

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files %{undername}

%check
# https://github.com/romis2012/python-socks/blob/master/.travis.yml
%pytest tests/

%files -n python3-socks -f %{pyproject_files}
%doc README.md

%changelog
%autochangelog
