%global _description %{expand:
Simple proxy (SOCKS4(a), SOCKS5(h), HTTP tunnel) server built with anyio. It is
used for testing python-socks, aiohttp-socks and httpx-socks packages.}

%global forgeurl https://github.com/romis2012/tiny-proxy

Name:           python-tiny-proxy
Version:        0.2.0
Release:        %{autorelease}
Summary:        Simple proxy server (SOCKS4(a), SOCKS5(h), HTTP tunnel)

License:        Apache-2.0
%forgemeta
URL:            %{forgeurl}
Source0:        %{forgesource}

BuildArch:      noarch

%description %_description

%package -n python3-tiny-proxy
Summary:        %{summary}
BuildRequires:  python3-devel

%description -n python3-tiny-proxy %_description

%prep
%autosetup -n tiny-proxy-%{version}
%forgesetup

# tweak dev requirements to remove linters, loosen versions
sed -i -e 's/==.*$//' -e '/flake8/ d' -e '/-cov/ d' -e '/^-e/ d' requirements-dev.txt

cat requirements-dev.txt

# Comment out to remove /usr/bin/env shebangs
# Can use something similar to correct/remove /usr/bin/python shebangs also
# find . -type f -name "*.py" -exec sed -i '/^#![  ]*\/usr\/bin\/env.*$/ d' {} 2>/dev/null ';'

%generate_buildrequires
%pyproject_buildrequires -r requirements-dev.txt


%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files tiny_proxy

%check
%{pytest}

%files -n python3-tiny-proxy -f %{pyproject_files}
%doc README.md

%changelog
%autochangelog
