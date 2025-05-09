%if %{defined fedora}
# CentOS/RHEL missing mysql-connector-python3
%bcond_without mysql_tests
%endif
%bcond_without postgres_tests

Name:           python-peewee
Version:        3.18.1
Release:        %autorelease
Summary:        A simple and small ORM

License:        MIT
URL:            https://github.com/coleifer/peewee
# PyPI tarball doesn't have tests
Source:         %{url}/archive/%{version}/peewee-%{version}.tar.gz

BuildRequires:  gcc
BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
BuildRequires:  python3-Cython
BuildRequires:  sqlite-devel

# documentation
BuildRequires:  python3-sphinx
BuildRequires:  python3-sphinx_rtd_theme

# tests
BuildRequires:  python3-apsw
%if %{with mysql_tests}
BuildRequires:  mysql-connector-python3
%endif
%if %{with postgres_tests}
BuildRequires:  python3-psycopg2
BuildRequires:  postgresql-test-rpm-macros
BuildRequires:  postgresql-contrib
%endif


%global _description %{expand:
Peewee is a simple and small ORM. It has few (but expressive) concepts, making
it easy to learn and intuitive to use.}


%description %{_description}


%package -n python3-peewee
Summary:        %{summary}


%description -n python3-peewee %{_description}


%package docs
Summary:        Documentation for %{name}
Conflicts:      python3-peewee < 3.15.1-3


%description docs
Documentation for %{name}.


%prep
%autosetup -n peewee-%{version} -p 1


%generate_buildrequires
%pyproject_buildrequires


%build
%pyproject_wheel

# Test suite requires an in-place build of the compiled extensions.
# https://github.com/coleifer/peewee/blob/3.15.2/.github/workflows/tests.yaml#L49
%{set_build_flags}
%{python3} %{py_setup} %{?py_setup_args} build_ext --inplace

# Build the documentation
sphinx-build docs html
rm -rf html/.{doctrees,buildinfo}


%install
%pyproject_install
%pyproject_save_files peewee playhouse pwiz
mv %{buildroot}%{_bindir}/{pwiz.py,pwiz}


%check
%if %{with postgres_tests}
export PGTESTS_LOCALE="C.UTF-8"
%postgresql_tests_run
createdb peewee_test
psql -c "CREATE EXTENSION hstore" peewee_test
%endif
%{python3} runtests.py


%files -n python3-peewee -f %{pyproject_files}
%doc README.rst CHANGELOG.md
%{_bindir}/pwiz


%files docs
%doc html


%changelog
%autochangelog
