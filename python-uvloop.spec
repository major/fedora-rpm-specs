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
BuildRequires:  python3-Cython
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
# fix path for test_libuv_api.py
sed -i "s:import sys:import sys\nsys.path.append\(os.path.abspath\(os.path.dirname\(__file__\)\)\)\n:" tests/__main__.py

# test_write_buffer_full (tests.test_pipes.Test_AIO_Pipes.test_write_buffer_full) ... FAIL
# test_write_buffer_full (tests.test_pipes.Test_UV_Pipes.test_write_buffer_full) ... FAIL
%ifnarch ppc64le
%{__python3} setup.py test
%endif

%files -n python3-%{modname}
%license LICENSE-APACHE LICENSE-MIT
%doc README.rst
%{python3_sitearch}/%{modname}-*.egg-info/
%{python3_sitearch}/%{modname}/

%changelog
%autochangelog
