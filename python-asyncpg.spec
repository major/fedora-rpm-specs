# Sphinx-generated HTML documentation is not suitable for packaging; see
# https://bugzilla.redhat.com/show_bug.cgi?id=2006555 for discussion.
#
# We can generate PDF documentation as a substitute.
%bcond_without doc_pdf

Name:           python-asyncpg
Summary:        A fast PostgreSQL Database Client Library for Python/asyncio
Version:        0.26.0
Release:        %autorelease

License:        ASL 2.0
URL:            https://github.com/MagicStack/asyncpg
Source0:        %{pypi_source asyncpg}

BuildRequires:  gcc
BuildRequires:  python3-devel

%if %{with doc_pdf}
BuildRequires:  make
BuildRequires:  python3-sphinx-latex
BuildRequires:  latexmk
%endif

# For tests:
#
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

%description -n python3-asyncpg %{common_description}


%package doc
Summary:        Documentation for %{name}

BuildArch:      noarch

%description doc %{common_description}


%prep
%autosetup -n asyncpg-%{version}

# Remove pre-generated C sources from Cython to ensure they are re-generated
# and not used in the build. Note that recordobj.c is not a generated source,
# and must not be removed!
find asyncpg -type f -name '*.c' ! -name 'recordobj.c' -print -delete

# Do not put the source directory at the front of the path, as this keeps us
# from using our own PYTHONPATH setting to allow importing the compiled
# extension modules.
sed -r -i 's|(sys\.path\.)insert\(0,[[:blank:]]*|\1append\(|' \
    docs/conf.py
# Drop intersphinx mappings, since we can’t download remote inventories and
# can’t easily produce working hyperlinks from inventories in local
# documentation packages.
echo 'intersphinx_mapping.clear()' >> docs/conf.py

# Loosen SemVer pins to allow newer versions of Sphinx-related dependencies.
sed -r -i 's/([Ss]phinx.*)~=/\1>=/g' setup.py

# We will not run style linting tests since they are brittle, so we might as
# well drop the corresponding dependencies.
sed -r -i '/(pycodestyle|flake8)/d' setup.py


%generate_buildrequires
# Note dev extra includes doc and test extras
%pyproject_buildrequires -x dev


%build
%set_build_flags
%pyproject_wheel

%if %{with doc_pdf}
PYTHONPATH="%{pyproject_build_lib}" %make_build -C docs latex \
        SPHINXBUILD='sphinx-build' SPHINXOPTS='%{?_smp_mflags}'
%make_build -C docs/_build/latex LATEXMKOPTS='-quiet'
%endif


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
# flake8 and pycodestyle out of the test dependencies
k="${k-}${k+ and }not TestFlake8"

%ifarch s390x
# This appears to be associated with GCC 12.
# https://github.com/MagicStack/asyncpg/issues/877
k="${k-}${k+ and }not (TestPrepare and test_prepare_28_max_args)"
%endif

%pytest -k "${k}"


%files -n python3-asyncpg -f %{pyproject_files}


%files doc
%license LICENSE
%doc README.rst
%if %{with doc_pdf}
%doc docs/_build/latex/asyncpg.pdf
%endif


%changelog
%autochangelog
