# The tests BR httpx-socks, Requires python-socks.
# The tests of python-socks BR tiny-proxy.
# To break the loop when bootstrapping Python, we can disable the tests here.
%bcond tests 1

%global _description %{expand:
Simple proxy (SOCKS4(a), SOCKS5(h), HTTP tunnel) server built with anyio. It is
used for testing python-socks, aiohttp-socks and httpx-socks packages.}

%global forgeurl https://github.com/romis2012/tiny-proxy

Name:           python-tiny-proxy
Version:        0.2.1
Release:        %{autorelease}
Summary:        Simple proxy server (SOCKS4(a), SOCKS5(h), HTTP tunnel)

License:        Apache-2.0
%forgemeta
URL:            %{forgeurl}
Source:         %{forgesource}

BuildArch:      noarch

%description %_description

%package -n python3-tiny-proxy
Summary:        %{summary}
BuildRequires:  python3-devel

%description -n python3-tiny-proxy %_description

%prep
%autosetup -n tiny-proxy-%{version}
%forgesetup

# https://docs.fedoraproject.org/en-US/packaging-guidelines/Python/#_linters
sed -r \
    -e 's/^(pytest-cov|flake8)\b/# &/' \
    -e 's/(==|,<).*//' \
    -e 's/^-e /# &/' \
    requirements-dev.txt |
  tee requirements-dev-filtered.txt

# Comment out to remove /usr/bin/env shebangs
# Can use something similar to correct/remove /usr/bin/python shebangs also
# find . -type f -name "*.py" -exec sed -i '/^#![  ]*\/usr\/bin\/env.*$/ d' {} 2>/dev/null ';'

%generate_buildrequires
%pyproject_buildrequires %{?with_tests:requirements-dev-filtered.txt}


%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files -l tiny_proxy

%check
%pyproject_check_import
%if %{with tests}
%{pytest}
%endif

%files -n python3-tiny-proxy -f %{pyproject_files}
%doc README.md
%doc examples/

%changelog
%autochangelog
