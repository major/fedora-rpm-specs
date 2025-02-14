# Break a circular test dependency on python-tiny-proxy
%bcond bootstrap 0
%bcond tests %{expr:%{without bootstrap} && 0%{?fedora} > 39}

%global _description %{expand:
The httpx-socks package provides proxy transports for httpx client. SOCKS4(a),
SOCKS5(h), HTTP (tunneling) proxy supported. It uses python-socks for core
proxy functionality.}

%global forgeurl https://github.com/romis2012/httpx-socks

Name:           python-httpx-socks
Version:        0.10.0
Release:        %{autorelease}
Summary:        Proxy (HTTP, SOCKS) transports for httpx
License:        Apache-2.0
%forgemeta
URL:            %{forgeurl}
Source:         %{forgesource}

BuildArch:      noarch

BuildRequires:  python3-devel

%description %_description

%package -n python3-httpx-socks
Summary:        %{summary}

%description -n python3-httpx-socks %_description

%pyproject_extras_subpkg -n python3-httpx-socks asyncio trio

%prep
%autosetup -n httpx-socks-%{version}
%forgesetup

# loosen pinned deps
sed -i -e "s/httpx>.*$/httpx',/" -e "s/httpcore>.*$/httpcore',/" setup.py

# https://docs.fedoraproject.org/en-US/packaging-guidelines/Python/#_linters
sed -r \
    -e 's/^(pytest-cov|coveralls|flake8)\b/# &/' \
    -e 's/(==|,<).*//' \
    requirements-dev.txt |
  tee requirements-dev-filtered.txt

# Comment out to remove /usr/bin/env shebangs
# Can use something similar to correct/remove /usr/bin/python shebangs also
# find . -type f -name "*.py" -exec sed -i '/^#![  ]*\/usr\/bin\/env.*$/ d' {} 2>/dev/null ';'

%generate_buildrequires
%pyproject_buildrequires -x asyncio,trio %{?with_tests:requirements-dev-filtered.txt}


%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files -l httpx_socks

%check
%pyproject_check_import
%if %{with tests}
%pytest -v
%endif

%files -n python3-httpx-socks -f %{pyproject_files}
%doc README.md

%changelog
%autochangelog
