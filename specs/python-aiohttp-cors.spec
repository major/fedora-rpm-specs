%global srcname aiohttp-cors
%global common_desc aiohttp_cors library implements Cross Origin Resource Sharing (CORS) support \
for aiohttp asyncio-powered asynchronous HTTP server.

Name:           python-%{srcname}
Version:        0.8.1
Release:        %autorelease
Summary:        CORS (Cross Origin Resource Sharing) support for aiohttp

# Automatically converted from old format: ASL 2.0 - review is highly recommended.
License:        Apache-2.0
URL:            https://github.com/aio-libs/aiohttp-cors
Source0:        %{url}/archive/v%{version}/%{name}-%{version}.tar.gz

# Compatibility with pytest 8.4+
# Upstream PR: https://github.com/aio-libs/aiohttp-cors/pull/557
Patch:          Set-asyncio_mode-auto-for-compatibility-with-pytest-.patch

BuildArch:      noarch

%description
%{common_desc}


%package -n python3-%{srcname}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{srcname}}
BuildRequires: python3-devel
BuildRequires: python3-setuptools

# For tes suite
BuildRequires: python3-pytest
BuildRequires: python3-pytest-aiohttp
BuildRequires: python3-pytest-asyncio
BuildRequires: python3-aiohttp >= 1.1
BuildRequires: python3-anyio

# Browser tests not possible yet
# BuildRequires: python3-selenium
#
# ifarch on noarch?
# BuildRequires: chromium
# BuildRequires: chromedriver
# Chrome failed to start: exited abnormally
#     (unknown error: DevToolsActivePort file doesn't exist)
#
# BuildRequires: firefox
# BuildRequires: geckodriver -- not available

%description -n python3-%{srcname}
%{common_desc}


%prep
%autosetup -n %{srcname}-%{version} -p1

# remove non-essential pytest plugins
sed -i '/pytest-cov/d' setup.py
sed -i '/pytest-pylint/d' setup.py

# Don't treat warnings as errors, that's what upstream testing is for
# In 0.7.0, nothing else is in this config
sed -i 's/error/default/' pytest.ini

# Don't add --cov options to pytest
# In 0.7.0, nothing else is in this config
rm setup.cfg


%build
%py3_build

%install
%py3_install

%check
%{python3} -m pytest -v --ignore tests/integration/test_real_browser.py

%files -n python3-%{srcname}
%license LICENSE
%doc README.rst CHANGES.rst
%{python3_sitelib}/aiohttp_cors
%{python3_sitelib}/aiohttp_cors-*.egg-info/

%changelog
%autochangelog
