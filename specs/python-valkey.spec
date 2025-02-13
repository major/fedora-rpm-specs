Name:           python-valkey
Version:        6.1.0b2
Release:        %autorelease
Summary:        The Python interface to the Valkey key-value store
License:        MIT
URL:            https://github.com/valkey-io/valkey-py
Source:         %{url}/archive/v%{version}/python-valkey-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  valkey
BuildRequires:  python3dist(pytest)
BuildRequires:  python3dist(pytest-asyncio)
BuildRequires:  python3dist(pytest-timeout)
BuildRequires:  python3dist(cachetools)

%global _description %{expand:
This is a Python interface to the Valkey key-value store.}

%description %_description

%package -n     python3-valkey

Summary:        %{summary}

%description -n python3-valkey %_description

This is a Python 3 interface to the Valkey key-value store.


%prep
%autosetup -p1 -n valkey-py-%{version}
# Upstream pins this dependency, but we need to be more flexible.
sed -e '/ocsp/ s/pyopenssl==/pyopenssl>=/' \
    -i setup.py


%generate_buildrequires
# pyOpenSSL version on Fedora prior to 41 is 23.2.0
# while ocsp extra requires >= 23.2.1
%if 0%{?fedora} >= 41
%pyproject_buildrequires -x ocsp
%endif
%if 0%{?fedora} < 41
%pyproject_buildrequires
%endif


%build
%pyproject_wheel


%install
%pyproject_install
%pyproject_save_files valkey


%check
# pyOpenSSL version on Fedora prior to 41 is 23.2.0
# while ocsp extra requires >= 23.2.1
%if 0%{?fedora} >= 41
%pyproject_check_import
%endif
%if 0%{?fedora} < 41
%pyproject_check_import -e valkey.ocsp
%endif

echo 'enable-module-command yes' | valkey-server --port 6379 --enable-debug-command yes - &
%pytest -m 'not onlycluster and not redismod and not ssl' -k 'not get_from_cache and not test_cache_decode_response[sentinel_setup0] and not psync and not test_geopos and not geosearch and not georadius'
kill %1


%files -n python3-valkey -f %{pyproject_files}
%doc README.md


%changelog
%autochangelog
