# Run tests with uvloop? Currently unavailable in EPEL10
%bcond uvloop %{expr:!0%{?el10}}

Name:           python-asyncpg
Summary:        A fast PostgreSQL Database Client Library for Python/asyncio
Version:        0.30.0
Release:        %autorelease

# The entire source is Apache-2.0, except:
#
# PSF-2.0:
#   asyncpg/protocol/record/recordobj.c
#   asyncpg/_asyncio_compat.py
License:        Apache-2.0 AND PSF-2.0
URL:            https://github.com/MagicStack/asyncpg
Source:         %{pypi_source asyncpg}

BuildSystem:            pyproject
BuildOption(install):   -l asyncpg
BuildOption(generate_buildrequires): -x gssauth,test

BuildRequires:  gcc
BuildRequires:  tomcli

# For tests:
BuildRequires:  %{py3_dist pytest}
# For krb5-config binary
BuildRequires:  krb5-devel
# For /usr/sbin/kdb5_util binary
BuildRequires:  krb5-server
# For kinit binary
BuildRequires:  krb5-workstation
# For pg_config binary
BuildRequires:  libpq-devel
# For pg_ctl binary
BuildRequires:  postgresql-server
# For citext extension
BuildRequires:  postgresql-contrib

# Note that asyncpg/pgproto comes from a git submodule referencing a separate
# project, https://github.com/MagicStack/py-pgproto. However, we do not treat
# it as a bundled dependency because it contains only sources; it has no build
# system and is not designed for separate installation; and it is managed as a
# part of the asyncpg package, as evidenced by the comment “This module is part
# of asyncpg” in the file headers.

%global common_description %{expand:
asyncpg is a database interface library designed specifically for PostgreSQL
and Python/asyncio. asyncpg is an efficient, clean implementation of PostgreSQL
server binary protocol for use with Python’s asyncio framework. You can read
more about asyncpg in an introductory blog post
http://magic.io/blog/asyncpg-1m-rows-from-postgres-to-python/.}

%description %{common_description}


%package -n     python3-asyncpg
Summary:        %{summary}

Obsoletes:      %{name}-doc < 0.27.0-5

%description -n python3-asyncpg %{common_description}


%pyproject_extras_subpkg -n python3-asyncpg gssauth


%prep -a
# Remove pre-generated C sources from Cython to ensure they are re-generated
# and not used in the build. Note that recordobj.c is not a generated source,
# and must not be removed!
find asyncpg -type f -name '*.c' ! -name 'recordobj.c' -print -delete

# https://docs.fedoraproject.org/en-US/packaging-guidelines/Python/#_linters
tomcli set pyproject.toml lists delitem --no-first --type regex \
    'project.optional-dependencies.test' '(flake8|mypy)\b.*'

%if %{without uvloop}
tomcli set pyproject.toml lists delitem --no-first --type regex \
    'project.optional-dependencies.test' '(uvloop)\b.*'
%endif


%generate_buildrequires -p
export ASYNCPG_BUILD_CYTHON_ALWAYS=1


%build -p
export ASYNCPG_BUILD_CYTHON_ALWAYS=1


%check -a
# It is not clear why the tests always import asyncpg as ../asyncpg/__init__.py
# even if we set PYTHONPATH to the installed sitearch directory. This
# workaround is ugly, but there is nothing actually wrong with it, as the
# install is already done by the time the check section runs:
rm -rf asyncpg
ln -s %{buildroot}%{python3_sitearch}/asyncpg/

# https://docs.fedoraproject.org/en-US/packaging-guidelines/Python/#_linters
k="${k-}${k+ and }not TestFlake8"

# Test failure in test_executemany_server_failure_during_writes
# https://github.com/MagicStack/asyncpg/issues/1099
# This may be flaky and/or arch-dependent.
k="${k-}${k+ and }not test_executemany_server_failure_during_writes"

# Python 3.13.2: TestConnectParams.test_connect_params fails with ValueError:
# Invalid IPv6 URL
# https://github.com/MagicStack/asyncpg/issues/1236
k="${k-}${k+ and }not (TestConnectParams and test_connect_params)"

# See the “test” target in the Makefile:
PYTHONASYNCIODEBUG=1 %pytest -k "${k-}"
%pytest -k "${k-}"
%if %{with uvloop}
USE_UVLOOP=1 %pytest -k "${k-}"
%endif


%files -n python3-asyncpg -f %{pyproject_files}
%doc README.rst


%changelog
%autochangelog
