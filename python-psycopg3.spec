%global package_name	psycopg
%global src_name	%{package_name}3
%global _description %{expand:
Psycopg 3 is a PostgreSQL database adapter for the Python programming language.
Psycopg 3 presents a familiar interface for everyone who has used Psycopg 2 or
any other DB-API 2.0 database adapter, but allows to use more modern PostgreSQL
and Python features.}

Name:		python-%{src_name}
Version:	3.1.8
Release:	1%{?dist}
Summary:	Psycopg 3 is a modern implementation of a PostgreSQL adapter for Python

License:	LGPLv3
URL:		https://www.psycopg.org/%{src_name}/
Source0:	https://github.com/%{package_name}/%{package_name}/archive/refs/tags/%{version}.tar.gz

BuildRequires:	python3-devel

# Required for running tests
BuildRequires:	libpq
BuildRequires:	postgresql-test-rpm-macros

BuildArch:	noarch

%description %_description

%package -n python3-%{src_name}
Requires:	libpq
Summary:	%{SUMMARY}

%description -n python3-%{src_name} %_description

%prep
%autosetup -p3 -n %{package_name}-%{version}/%{package_name}

# disable remove deps for typechecking and linting
sed -r -i 's/("(black|flake8|pytest-cov)\b.*",)/# \1/' setup.py
# remove pproxy dep, only used for tests
sed -r -i 's/("(pproxy)\b.*",)/# \1/' setup.py

%generate_buildrequires
%pyproject_buildrequires -x test

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files %{package_name}

# Prepare the test folder for pytest
pushd ../tests/

# Remove all files in pool/ folder except the fix_pool.py.
# The pool/fix_pool.py is in conftest.py as plugin
find pool/ ! -name 'fix_pool.py' -type f -exec rm -f {} +

popd

%check
export PGTESTS_LOCALE=C.UTF-8
%postgresql_tests_run
export PSYCOPG_TEST_DSN="host=$PGHOST port=$PGPORT dbname=${PGTESTS_DATABASES##*:}"

%pytest ../tests/ -k "not test_typing and not test_module"

%files -n python3-%{src_name} -f %{pyproject_files}
%doc ../README.rst
%license LICENSE.txt


%changelog
* Fri Jan 20 2023 Ondrej Sloup <osloup@redhat.com>  - 3.1.8-1
- Rebase to the latest upstream version (rhbz#2161450)

* Wed Dec 21 2022 Mikel Olasagasti Uranga <mikel@olasagasti.info> - 3.1.7-1
- Release bump rhbz#2155285
- Enable postgresql server for tests

* Fri Oct 14 2022 Ondrej Sloup <osloup@redhat.com> - 3.0.16-2
- Release bump

* Thu Aug 04 2022 Ondrej Sloup <osloup@redhat.com> - 3.0.16-1
- Rebase to the latest upstream version
- Create patch files instead of sed
- Fix release numbering

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.11-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Tue Jun 14 2022 Python Maint <python-maint@redhat.com> - 3.0.11-3
- Rebuilt for Python 3.11

* Fri May 13 2022 Ondrej Sloup <osloup@redhat.com> - 3.0.11-2
- Add support for Fedora 35 and 36
- Remove spaces at the end of the file
- Pray that Friday 13 will not break anything

* Thu Apr 28 2022 Ondrej Sloup <osloup@redhat.com> - 3.0.11-1
- Create package from git source (#2079251)
