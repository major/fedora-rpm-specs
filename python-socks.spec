%global undername python_socks

%global _description %{expand:
The python-socks package provides a core proxy client functionality for Python.
Supports SOCKS4(a), SOCKS5, HTTP (tunneling) proxy and provides sync and async
(asyncio, trio, curio) APIs. It is used internally by aiohttp-socks and
httpx-socks packages.
}

Name:           python-socks
Version:        2.0.3
Release:        %autorelease
Summary:        Core proxy (SOCKS4, SOCKS5, HTTP tunneling) functionality for Python

License:        ASL 2.0
URL:            https://github.com/romis2012/%{name}
Source0:        %{url}/archive/v%{version}/%{name}-%{version}.tar.gz

BuildArch:      noarch

%description %_description

%package -n python3-socks
Summary:        %{summary}
BuildRequires:  python3-devel
BuildRequires:  python3-setuptools

%description -n python3-socks %_description

# extras: asyncio, curio, trio
%pyproject_extras_subpkg -n python3-socks asyncio curio trio

%prep
%autosetup

# remove version lock
# https://github.com/romis2012/python-socks/blob/master/requirements-dev.txt
sed -i 's/pytest-asyncio>.*/pytest-asyncio/' requirements-dev.txt

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
