%global package_name	psycopg
%global src_name		%{package_name}3

%global pool_version	3.2.8
%global pool_name		pool-%{pool_version}

%if 0%{?fedora}
%bcond_without			cython
%bcond_without			pypy
%bcond_without			tests
%else
# EL9 does not have pypy, and cython build failed
%bcond_with			cython
%bcond_with			pypy
# postgresql-test-rpm-macros built but not published in CRB
# https://kojihub.stream.centos.org/koji/buildinfo?buildID=59955
# requested in https://issues.redhat.com/browse/RHEL-32610
%bcond_with			tests
%endif

%global desc \
Psycopg 3 is a PostgreSQL database adapter for the Python programming language. \
Psycopg 3 presents a familiar interface for everyone who has used Psycopg 2 or \
any other DB-API 2.0 database adapter, but allows to use more modern PostgreSQL \
and Python features.

Name:		python-%{src_name}
Version:	3.2.13
Release:	%autorelease
Summary:	Psycopg 3 is a modern implementation of a PostgreSQL adapter for Python

License:	LGPL-3.0-only
URL:		https://www.psycopg.org/%{src_name}/
Source0:	https://github.com/%{package_name}/%{package_name}/archive/refs/tags/%{version}.tar.gz
Source1:	https://github.com/%{package_name}/%{package_name}/archive/refs/tags/%{pool_name}.tar.gz

%if %{without cython}
BuildArch:		noarch
%endif

# https://fedoraproject.org/wiki/Changes/EncourageI686LeafRemoval
ExcludeArch:	%{ix86}

BuildRequires:	python3-devel
BuildRequires:	libpq openssl
BuildRequires:	postgresql-static postgresql-server-devel
BuildRequires:	python3-pip python3-wheel python3-tomli
%if %{with pypy}
BuildRequires:	pypy
%endif

%if %{with tests}
# Required for running tests
BuildRequires:	postgresql-test-rpm-macros
BuildRequires:	python3-anyio python3-mypy pytest python3-pytest-cov python3-pytest-randomly
%endif

%if %{with cython}
# Required for Cython
BuildRequires:	cython gcc
%endif

# Runtime dependency
# https://github.com/psycopg/psycopg/blob/master/README.rst
Requires:		libpq

%description %{desc}

%package -n python3-%{src_name}

Summary:		%{summary}
BuildArch:		noarch
Requires:		libpq

%description -n python3-%{src_name} %{desc}

%package -n python3-%{src_name}_pool
Summary:		Connection pooling for Psycopg 3
Requires:		python-%{src_name}
BuildArch:		noarch
Requires:		libpq

%description -n python3-%{src_name}_pool
This package contains the pooling functionality for Psycopg 3.

%if %{with cython}
%package -n python3-%{src_name}_c
Summary:		C extensions for Psycopg 3
Requires:		libpq

%description -n python3-%{src_name}_c
This package contains the C extensions for enhanced performance in Psycopg 3.
%endif

%prep
%autosetup -p1 -n %{package_name}-%{version}

# Remove old psycopg_pool folder
rm -rf psycopg_pool/*

# Unpack upstream psycopg_pool
tar -xzf %{SOURCE1} -C psycopg_pool/ --strip-components=2 %{package_name}-%{pool_name}/psycopg_pool/

%build
pushd psycopg
%pyproject_wheel
popd

pushd psycopg_pool
%pyproject_wheel
popd

%if %{with cython}
pushd psycopg_c
%pyproject_wheel
popd
%endif

%install
pushd psycopg
%pyproject_install
popd

pushd psycopg_pool
%pyproject_install
popd

%if %{with cython}
pushd psycopg_c
%pyproject_install
popd
%endif

%if %{with tests}
%check
export PGTESTS_LOCALE=C.UTF-8
%postgresql_tests_run

export PSYCOPG_TEST_DSN="port=$PGPORT dbname=${PGTESTS_DATABASES##*:} sslmode=disable"

# Remove tests that need to use internet or specific settings
# Disable test_psycopg_dbapi20.py for riscv64
# https://github.com/psycopg/psycopg/issues/883
%pytest tests/ -k "not (\
%ifarch riscv64
		test_psycopg_dbapi20.py or \
%endif
		test_typing or \
		test_module or \
		test_conninfo_attempts_async or \
		test_connection_async or \
		test_connection or \
		test_conninfo_attempts or \
		test_pool_async or \
		test_null_pool_async or \
		test_pool or \
		test_null_pool or \
		test_client_cursor_async or \
		test_cursor_async or \
		sched_async or \
		sched or \
		test_pipeline_async or \
		test_copy_async or \
		test_pipeline or \
		test_multirange or \
		test_datetime or \
		test_range or \
		test_string or \
		test_notify or \
		test_break_attempts or \
		test_waiting\
)"
%endif


%files -n python3-%{src_name}
%{python3_sitelib}/psycopg/
%{python3_sitelib}/psycopg-%{version}.dist-info/
%license psycopg/LICENSE.txt
%doc psycopg/README.rst

%files -n python3-%{src_name}_pool
%{python3_sitelib}/psycopg_pool/
%{python3_sitelib}/psycopg_pool-%{pool_version}.dist-info/
%license psycopg_pool/LICENSE.txt
%doc psycopg_pool/README.rst

%if %{with cython}
%files -n python3-%{src_name}_c
%{python3_sitearch}/psycopg_c/
%{python3_sitearch}/psycopg_c-%{version}.dist-info/
%license psycopg_c/LICENSE.txt
%doc psycopg_c/README.rst
%endif

%changelog
%autochangelog
