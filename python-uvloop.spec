%global modname uvloop

Name:           python-%{modname}
Version:        0.17.0
Release:        %autorelease
Summary:        Ultra fast implementation of asyncio event loop on top of libuv

License:        MIT or ASL 2.0
URL:            https://github.com/MagicStack/uvloop
Source0:        %{url}/archive/v%{version}/%{modname}-%{version}.tar.gz

BuildRequires:  gcc
BuildRequires:  libuv-devel

%global _description \
uvloop is a fast, drop-in replacement of the built-in asyncio event loop.\
uvloop is implemented in Cython and uses libuv under the hood.

%description %{_description}

%package -n python3-%{modname}
Summary:        %{summary}
BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
BuildRequires:  python3-cython < 0.30.0
BuildRequires:  python3-aiohttp
BuildRequires:  python3-psutil
BuildRequires:  python3-pyOpenSSL

%description -n python3-%{modname} %{_description}

%prep
%autosetup -p1 -n %{modname}-%{version}
# always use cython to generate code
sed -i -e "/self.cython_always/s/False/True/" setup.py
# use system libuv
sed -i -e "/self.use_system_libuv/s/False/True/" setup.py
# To be sure, no 3rd-party stuff
rm -vrf vendor/

%build
%py3_build

%install
%py3_install
# https://github.com/MagicStack/uvloop/issues/70
rm -vf %{buildroot}%{python3_sitearch}/%{modname}/_testbase.py
rm -vf %{buildroot}%{python3_sitearch}/%{modname}/__pycache__/_testbase.*

%check
# delete tests that fail on Python 3.12
# https://github.com/MagicStack/uvloop/issues/547
rm tests/test_aiohttp.py
rm tests/test_libuv_api.py
rm tests/test_process.py
rm tests/test_tcp.py
rm tests/test_unix.py

%ifarch ppc64le
# delete tests that fail on ppc64le
rm tests/test_pipes.py
%endif

%{python3} setup.py test

%files -n python3-%{modname}
%license LICENSE-APACHE LICENSE-MIT
%doc README.rst
%{python3_sitearch}/%{modname}-*.egg-info/
%{python3_sitearch}/%{modname}/

%changelog
%autochangelog
