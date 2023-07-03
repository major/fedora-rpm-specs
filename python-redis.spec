# Enable tests by default.
%bcond_without tests

%global upstream_name redis

Name:           python-%{upstream_name}
Version:        4.5.1
Release:        %autorelease
Summary:        Python interface to the Redis key-value store
License:        MIT
URL:            https://github.com/redis/redis-py
Source0:        https://github.com/redis/redis-py/archive/v%{version}/redis-py-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  python3-devel

%if %{with tests}
BuildRequires:  redis
BuildRequires:  python3dist(pytest)
BuildRequires:  python3dist(pytest-asyncio)
%endif

%global _description\
This is a Python interface to the Redis key-value store.

%description %_description

%package -n     python3-%{upstream_name}
Summary:        Python 3 interface to the Redis key-value store
%{?python_provide:%python_provide python3-%{upstream_name}}

%description -n python3-%{upstream_name}
This is a Python 3 interface to the Redis key-value store.

%prep
%setup -qn redis-py-%{version}

# This test passes locally but fails in koji...
rm tests/test_commands.py*

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files %{upstream_name}

%if %{with tests}
%check
%if 0%{?fedora} >= 37 || 0%{?rhel} > 9
# redis 7+
redis-server --enable-debug-command yes &
%else
redis-server &
%endif
# xinfo_consumers fails with redis 7.2rc2, https://bugzilla.redhat.com/2196782
%pytest -m 'not onlycluster and not redismod and not ssl' -k 'not xinfo_consumers'
kill %1
%endif

%files -n python3-%{upstream_name} -f %{pyproject_files}
%doc CHANGES README.md

%changelog
%autochangelog
