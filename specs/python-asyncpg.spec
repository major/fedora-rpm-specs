# Run tests with uvloop? It was retired due to RHBZ#2372190.
%bcond uvloop 0

Name:           python-asyncpg
Summary:        A fast PostgreSQL Database Client Library for Python/asyncio
Version:        0.31.0
Release:        %autorelease

# The entire source is Apache-2.0, except:
#
# 0BSD:
# - asyncpg/protocol/record/pythoncapi_compat.h (unbundled in %%prep, but
#   header-only libraries are treated like static libraries, so this still
#   affects the License expression)
# PSF-2.0:
# - asyncpg/protocol/record/recordobj.c
# - asyncpg/_asyncio_compat.py
License:        Apache-2.0 AND 0BSD AND PSF-2.0
URL:            https://github.com/MagicStack/asyncpg
Source:         %{pypi_source asyncpg}

BuildSystem:            pyproject
BuildOption(install):   -l asyncpg
BuildOption(generate_buildrequires): -x gssauth -g test

BuildRequires:  gcc
BuildRequires:  tomcli

# Unbundled header-only library. Dependency on -static per guidelines,
# https://docs.fedoraproject.org/en-US/packaging-guidelines/#_packaging_header_only_libraries.
BuildRequires:  pythoncapi-compat-static

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
tomcli set pyproject.toml lists delitem \
    'dependency-groups.test' '(flake8|mypy)\b.*'

# Do not upper-bound the Python interpreter version for the uvloop test
# dependency. First, a missing uvloop breaks the test if we do not adjust the
# uvloop bcond; second, we may have a working python3-uvloop packaged even if
# there is no corresponding binary wheel on PyPI. We use sed since "tomcli set
# ... lists replace ..." only supports a fixed replacement string.
sed -r -i "s/('uvloop\\b.*);.*'/\\1'/" pyproject.toml
%if %{without uvloop}
tomcli set pyproject.toml lists delitem 'dependency-groups.test' '(uvloop)\b.*'
%endif

# Unbundle pythoncapi-compat.
ln -svf /usr/include/pythoncapi_compat.h \
    asyncpg/protocol/record/pythoncapi_compat.h


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

%if v"0%{?python3_version}" >= v"3.15"
# Test failure in test_pool_handles_transaction_exit_in_asyncgen_2 with Python
# 3.15.0a5, PYTHONASYNCIODEBUG=1
# https://github.com/MagicStack/asyncpg/issues/1300
k="${k-}${k+ and }not (TestPool and test_pool_handles_transaction_exit_in_asyncgen_2)"
%endif

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
