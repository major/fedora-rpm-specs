# Run tests with uvloop?
%bcond uvloop 1

Name:           python-asyncpg
Summary:        A fast PostgreSQL Database Client Library for Python/asyncio
Version:        0.29.0
Release:        %autorelease

# The entire source is Apache-2.0, except:
#
# PSF-2.0:
#   asyncpg/protocol/record/recordobj.c
#   asyncpg/_asyncio_compat.py
License:        Apache-2.0 AND PSF-2.0
URL:            https://github.com/MagicStack/asyncpg
Source:         %{pypi_source asyncpg}

# Downstream-only: use uvloop for tests even on Python 3.12+
#
# Upstream has disabled it because uvloop has not released binary wheels
# for Python 3.12 yet, but we use the python3-uvloop package
Patch:          0001-Downstream-only-use-uvloop-for-tests-even-on-Python-.patch

# Allow Cython 3
# https://github.com/MagicStack/asyncpg/pull/1101
#
# Fixes:
#
# RFE: please provide cython 3.x support
# https://github.com/MagicStack/asyncpg/issues/1083
Patch:          %{url}/pull/1101.patch

BuildRequires:  gcc
BuildRequires:  python3-devel

# For tests:
BuildRequires:  %{py3_dist pytest}
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


%prep
%autosetup -n asyncpg-%{version} -p1

# Remove pre-generated C sources from Cython to ensure they are re-generated
# and not used in the build. Note that recordobj.c is not a generated source,
# and must not be removed!
find asyncpg -type f -name '*.c' ! -name 'recordobj.c' -print -delete

# We will not run style linting tests since they are brittle, so we might as
# well drop the corresponding dependencies.
sed -r -i '/(flake8)/d' pyproject.toml

%if %{without uvloop}
sed -r -i 's/^([[:blank:]])(.*uvloop)/\1# \2/' pyproject.toml
%endif


%generate_buildrequires
export ASYNCPG_BUILD_CYTHON_ALWAYS=1
%pyproject_buildrequires -x test


%build
export ASYNCPG_BUILD_CYTHON_ALWAYS=1
%pyproject_wheel


%install
%pyproject_install
%pyproject_save_files asyncpg


%check
# It is not clear why the tests always import asyncpg as ../asyncpg/__init__.py
# even if we set PYTHONPATH to the installed sitearch directory. This
# workaround is ugly, but there is nothing actually wrong with it, as the
# install is already done by the time the check section runs:
rm -rf asyncpg
ln -s %{buildroot}%{python3_sitearch}/asyncpg/

# Do not run flake8 code style tests, which may fail; besides, we have patched
# flake8 out of the test dependencies.
k="${k-}${k+ and }not TestFlake8"

# Test failure in test_executemany_server_failure_during_writes
# https://github.com/MagicStack/asyncpg/issues/1099
# This may be flaky and/or arch-dependent.
k="${k-}${k+ and }not test_executemany_server_failure_during_writes"

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
