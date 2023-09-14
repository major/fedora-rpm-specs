%global _description %{expand:
The httpx-socks package provides proxy transports for httpx client. SOCKS4(a),
SOCKS5(h), HTTP (tunneling) proxy supported. It uses python-socks for core
proxy functionality.}

%global forgeurl https://github.com/romis2012/httpx-socks

Name:           python-httpx-socks
Version:        0.7.7
Release:        %{autorelease}
Summary:        Proxy (HTTP, SOCKS) transports for httpx
License:        Apache-2.0
%forgemeta
URL:            %{forgeurl}
Source0:        %{forgesource}

BuildArch:      noarch

%description %_description

%package -n python3-httpx-socks
Summary:        %{summary}
BuildRequires:  python3-devel
BuildRequires:  python3-pytest
BuildRequires:  python3-trustme

%description -n python3-httpx-socks %_description

%prep
%autosetup -n httpx-socks-%{version}
%forgesetup

# loosen pinned deps
sed -i -e "s/httpx>.*$/httpx',/" -e "s/httpcore>.*$/httpcore',/" setup.py

# Comment out to remove /usr/bin/env shebangs
# Can use something similar to correct/remove /usr/bin/python shebangs also
# find . -type f -name "*.py" -exec sed -i '/^#![  ]*\/usr\/bin\/env.*$/ d' {} 2>/dev/null ';'

%generate_buildrequires
%pyproject_buildrequires requirements.txt


%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files httpx_socks

%check
%pyproject_check_import

# some optional deps aren't packaged in Fedora yet: hypercorn, tiny-proxy
# %%pytest -s

%files -n python3-httpx-socks -f %{pyproject_files}
%doc README.md

%changelog
%autochangelog
