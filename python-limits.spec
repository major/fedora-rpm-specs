# Run (limited set of) tests
%bcond tests 1
# Specific test conditionals
# Requires `hiro`
%bcond hiro 0
# Requires `lovely-pytest-docker` and not suitable for mock
%bcond docker 0
# Requires `pytest-benchmark[histogram]` (we are not interested in benchmarks)
%bcond benchmark 0

# Don't build extras with missing dependencies
%bcond redis 1
%bcond rediscluster 1
%bcond memcached 1
%bcond mongodb 1
%bcond etcd 1
# async-redis needs `coredis`
%bcond async_redis 0
# async-memcached needs `emcache`
%bcond async_memcached 0
# async-mongodb needs `motor` 0
%bcond async_mongodb 0
# async-etcd needs `aetcd`
%bcond async_etcd 0

# Sphinx-generated HTML documentation is not suitable for packaging; see
# https://bugzilla.redhat.com/show_bug.cgi?id=2006555 for discussion.
#
# Using Sphinx for generating documentation, pulls in a myriad of
# dependencies. Instead we simply provide the source `.rst` files.
%bcond doc 1

# Use forge macros for pulling from GitHub
%global forgeurl https://github.com/alisaifee/limits

%global pypi_name limits

%global _description %{expand:
This package is a python library to perform rate limiting with commonly used
storage backends (Redis, Memcached, MongoDB & Etcd).}

Name:           python-%{pypi_name}
Version:        3.9.0
Release:        %autorelease
Summary:        Rate limiting utilities
%global tag %{version}
%forgemeta
# SPDX
License:        MIT
URL:            %forgeurl
Source:         %forgesource

# Remove unnecessary use of importlib_resources
# https://github.com/alisaifee/limits/commit/d9a8fba0616f6736c845a156e669b7d1e13cbd86
Patch:          %{forgeurl}/commit/d9a8fba0616f6736c845a156e669b7d1e13cbd86.patch

BuildArch:      noarch

%description %_description

%package -n python3-%{pypi_name}
Summary:        %{summary}

BuildRequires:  python3-devel

%description -n python3-%{pypi_name} %_description

%if %{with doc}
%package doc
Summary:        %{summary}
Requires:       python3-limits = %{?epoch:%{epoch}:}%{version}-%{release}

%description doc
Documentation for %{name}.
%endif

# We cannot build all extras due to missing dependencies.
# Conditionalize extras based on what is available (see bcond above)
%if %{with redis}
%pyproject_extras_subpkg -n python3-%{pypi_name} redis
%endif
%if %{with rediscluster}
%pyproject_extras_subpkg -n python3-%{pypi_name} rediscluster
%endif
%if %{with memcached}
%pyproject_extras_subpkg -n python3-%{pypi_name} memcached
%endif
%if %{with mongodb}
%pyproject_extras_subpkg -n python3-%{pypi_name} mongodb
%endif
%if %{with etcd}
%pyproject_extras_subpkg -n python3-%{pypi_name} etcd
%endif
%if %{with async_redis}
%pyproject_extras_subpkg -n python3-%{pypi_name} async-redis
%endif
%if %{with async_memcached}
%pyproject_extras_subpkg -n python3-%{pypi_name} async-memcached
%endif
%if %{with async_mongodb}
%pyproject_extras_subpkg -n python3-%{pypi_name} async-mongodb
%endif
%if %{with async_etcd}
%pyproject_extras_subpkg -n python3-%{pypi_name} async-etcd
%endif

%prep
%autosetup -p1 %{forgesetupargs}

# Remove requirements for extras we cannot build
%if %{without redis}
sed -i '/redis.txt/d' requirements/test.txt
%endif
%if %{without rediscluster}
sed -i '/rediscluster.txt/d' requirements/test.txt
%endif
%if %{without memcached}
sed -i '/memcached.txt/d' requirements/test.txt
%endif
%if %{without mongodb}
sed -i '/mongodb.txt/d' requirements/test.txt
%endif
%if %{without etcd}
sed -i '/etcd.txt/d' requirements/test.txt
%endif
%if %{without async_redis}
sed -i '/async-redis.txt/d' requirements/test.txt
%endif
%if %{without async_memcached}
sed -i '/async-memcached.txt/d' requirements/test.txt
%endif
%if %{without async_mongodb}
sed -i '/async-mongodb.txt/d' requirements/test.txt
%endif
%if %{without async_etcd}
sed -i '/async-etcd.txt/d' requirements/test.txt
%endif

# Also remove requirements for missing test dependencies as well as
# dependencies for tests we cannot run
%if %{without hiro}
sed -i '/hiro/d' requirements/test.txt
%endif
%if %{without docker}
sed -i '/lovely-pytest-docker/d' requirements/test.txt
# The -K option is for lovely-pytest-docker.
sed -r -i '/^[[:blank:]]*-K[[:blank:]]*/d' pytest.ini
%endif
%if %{without benchmark}
sed -i '/pytest-benchmark/d' requirements/test.txt
%endif

# Unpin pytest-asyncio
sed -r -i 's/^(pytest-asyncio).*$/\1/' requirements/test.txt

# filterwarnings = error is too strict for distribution packaging
# Thanks @music!
sed -r -i '/^[[:blank:]]*error[[:blank:]]*/d' pytest.ini

# https://docs.fedoraproject.org/en-US/packaging-guidelines/Python/#_linters
sed -r -i '/(pytest-cov|coverage)/d' requirements/test.txt
sed -r -i '/--cov/d' pytest.ini


%generate_buildrequires
# We cannot build all extras due to missing dependencies.
# Conditionalize extras based on what is available (see bcond above)
%if %{with redis}
x="${x-}${x+,}redis"
%endif
%if %{with rediscluster}
x="${x-}${x+,}rediscluster"
%endif
%if %{with memcached}
x="${x-}${x+,}memcached"
%endif
%if %{with mongodb}
x="${x-}${x+,}mongodb"
%endif
%if %{with etcd}
x="${x-}${x+,}etcd"
%endif
%if %{with async_redis}
x="${x-}${x+,}async-redis"
%endif
%if %{with async_memcached}
x="${x-}${x+,}async-memcached"
%endif
%if %{with async_mongodb}
x="${x-}${x+,}async-mongodb"
%endif
%if %{with async_etcd}
x="${x-}${x+,}async-etcd"
%endif

# In a similar fashion conditionalize additional requirements
%if %{with tests}
reqs="${reqs-}${reqs+ }requirements/test.txt"
%endif

%pyproject_buildrequires ${x+-x }${x-} ${reqs-}


%build
%pyproject_wheel


%install
%pyproject_install
%pyproject_save_files -l limits


%check
%if %{with tests}

# Disable tests that are not useful / feasible
k="${k-}${k+ and }not TestConcreteStorages"
k="${k-}${k+ and }not TestWindow"
k="${k-}${k+ and }not TestAsyncWindow"
k="${k-}${k+ and }not TestConcurrency"
k="${k-}${k+ and }not TestAsyncConcurrency"

%pytest -v ${k+-k }"${k-}"
%endif

# Since quite a few tests cannot be run, run the import "smoke test" too.
%pyproject_check_import


%files -n python3-%{pypi_name} -f %{pyproject_files}
%doc ./*.rst


%if %{with doc}
%files doc
%doc doc/source/*.rst
%endif


%changelog
%autochangelog
