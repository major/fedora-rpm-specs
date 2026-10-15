Name:           python-valkey
Version:        6.2.0
Release:        %autorelease
Summary:        The Python interface to the Valkey key-value store
License:        MIT
URL:            https://github.com/valkey-io/valkey-py
Source:         %{url}/archive/v%{version}/python-valkey-%{version}.tar.gz
# Fix: correctly parse module load error for
# Valkey server >= 9.2 
# Upstream issue:
# https://github.com/valkey-io/valkey-py/pull/360
Patch0:         pr-360.patch
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


%generate_buildrequires
%pyproject_buildrequires -x ocsp


%build
%pyproject_wheel


%install
%pyproject_install
%pyproject_save_files valkey


%check
%pyproject_check_import

valkey-server --port 6379 --enable-debug-command yes --enable-module-command yes --daemonize yes --logfile ""
%pytest -m 'not onlycluster and not redismod and not ssl' -k 'not get_from_cache and not test_cache_decode_response[sentinel_setup0] and not psync and not test_geopos and not geosearch and not georadius'
kill %1


%files -n python3-valkey -f %{pyproject_files}
%doc README.md


%changelog
* Fri Jul 25 2025 Fedora Release Engineering <releng@fedoraproject.org> - 6.1.1-0.2.b1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_43_Mass_Rebuild

%autochangelog
