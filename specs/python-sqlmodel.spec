# This package corresponds to two PyPI projects (sqlmodel-slim, and sqlmodel)
# co-developed in one repository. Since the two are versioned identically and
# released at the same time, it makes sense to build them from a single source
# package.

Name:           python-sqlmodel
Version:        0.0.23
Release:        %autorelease
Summary:        SQL databases in Python, designed for simplicity, compatibility, and robustness

# SPDX
License:        MIT
URL:            https://github.com/fastapi/sqlmodel
Source:         %{url}/archive/%{version}/sqlmodel-%{version}.tar.gz

# Downstream-only: Patch for running tests without coverage
#
# https://docs.fedoraproject.org/en-US/packaging-guidelines/Python/#_linters
Patch:          0001-Downstream-only-Patch-for-running-tests-without-cove.patch

BuildArch:      noarch

BuildRequires:  python3-devel

# Since requirements-tests.txt and requirements-docs-tests.txt contain
# overly-strict version bounds and many unwanted
# linting/coverage/typechecking/formatting dependencies
# (https://docs.fedoraproject.org/en-US/packaging-guidelines/Python/#_linters),
# we just list the test dependencies we *do* want manually rather than trying
# to patch the requirements files. We preserve upstream’s lower bounds but
# remove upper bounds, as we must try to make do with what we have.
#
# requirements-docs-tests.txt: (contains only linters/formatters/etc.)
# requirements-tests.txt:
BuildRequires:  %{py3_dist pytest} >= 7.0.1
# There is a test-dependency loop with fastapi; break it with the bootstrap
# conditional in that package.
BuildRequires:  %{py3_dist fastapi} >= 0.103.2
BuildRequires:  %{py3_dist httpx} >= 0.24.1
BuildRequires:  %{py3_dist dirty-equals} >= 0.6
BuildRequires:  %{py3_dist jinja2} >= 3.1.4

%global common_description %{expand: \
SQLModel is a library for interacting with SQL databases from Python code, with
Python objects. It is designed to be intuitive, easy to use, highly compatible,
and robust.

SQLModel is based on Python type annotations, and powered by Pydantic and
SQLAlchemy.

The key features are:

  • Intuitive to write: Great editor support. Completion everywhere. Less time
    debugging. Designed to be easy to use and learn. Less time reading docs.
  • Easy to use: It has sensible defaults and does a lot of work underneath to
    simplify the code you write.
  • Compatible: It is designed to be compatible with FastAPI, Pydantic, and
    SQLAlchemy.
  • Extensible: You have all the power of SQLAlchemy and Pydantic underneath.
  • Short: Minimize code duplication. A single type annotation does a lot of
    work. No need to duplicate models in SQLAlchemy and Pydantic.}

%description %{common_description}


%package -n     python3-sqlmodel
Summary:        %{summary}

# https://docs.fedoraproject.org/en-US/packaging-guidelines/#_requiring_base_package
Requires:       python3-sqlmodel-slim = %{version}-%{release}

%description -n python3-sqlmodel %{common_description}


%package -n     python3-sqlmodel-slim
Summary:        %{summary}

%description -n python3-sqlmodel-slim %{common_description}


%prep
%autosetup -n sqlmodel-%{version} -p1

# Remove bundled js-termynal 0.0.1; since we are not building documentation, we
# do this very bluntly:
rm -rvf docs/*/docs/js docs/*/docs/css


%generate_buildrequires
export TIANGOLO_BUILD_PACKAGE='sqlmodel-slim'
(
  export TIANGOLO_BUILD_PACKAGE='sqlmodel'
  %pyproject_buildrequires
) | grep -vE '\bsqlmodel-slim\b'


%build
export TIANGOLO_BUILD_PACKAGE='sqlmodel-slim'
%pyproject_wheel
export TIANGOLO_BUILD_PACKAGE='sqlmodel'
%pyproject_wheel


%install
%pyproject_install


%check
# Ignore tutorial tests that are specifically associated with older Python
# versions; a few of these fail on later versions, and that is OK.
for pyver in 39 310
do
  if [ '%{python3_version_nodots}' != "${pyver}" ]
  then
    ignore="${ignore-} --ignore-glob=*tutorial/*/*_py${pyver}[/._]*"
  fi
done

# This test uses black to format Python code generated via a Jinja2 template,
# and it appears to depend on the exact formatted output; this is the
# brittleness cautioned against in
# https://docs.fedoraproject.org/en-US/packaging-guidelines/Python/#_linters,
# so we skip the test.
k="${k-}${k+ and }not test_select_gen"

# Ignore all DeprecationWarning messages, as they pop up from various
# dependencies in practice. Upstream deals with this by tightly controlling
# dependency versions in CI.
warningsfilter="${warningsfilter-} -W ignore::DeprecationWarning"

# We need the working directory in the path so that certain tests can execute
# things like:
#   python3 -m docs_src.tutorial.create_db_and_table.tutorial001
export PYTHONPATH="%{buildroot}%{python3_sitelib}:${PWD}"

%pytest ${warningsfilter-} -k "${k-}" ${ignore-} -v -rs


%files -n python3-sqlmodel
%{python3_sitelib}/sqlmodel-%{version}.dist-info/


%files -n python3-sqlmodel-slim
%license LICENSE
%doc CITATION.cff
%doc README.md

%{python3_sitelib}/sqlmodel/
%{python3_sitelib}/sqlmodel_slim-%{version}.dist-info/


%changelog
%autochangelog
