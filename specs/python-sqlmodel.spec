Name:           python-sqlmodel
Version:        0.0.38
Release:        %autorelease
Summary:        SQL databases in Python, designed for simplicity, compatibility, and robustness

License:        MIT
URL:            https://github.com/fastapi/sqlmodel
Source:         %{url}/archive/%{version}/sqlmodel-%{version}.tar.gz

# Downstream-only: Patch for running tests without coverage
# https://docs.fedoraproject.org/en-US/packaging-guidelines/Python/#_linters
Patch:          0001-Downstream-only-Patch-for-running-tests-without-cove.patch

BuildSystem:            pyproject
BuildOption(install):   -l sqlmodel

BuildArch:      noarch

# Since dependency groups contain overly-strict version bounds and some
# unwanted linting/coverage/typechecking/formatting dependencies
# (https://docs.fedoraproject.org/en-US/packaging-guidelines/Python/#_linters),
# we just list the test dependencies we *do* want manually rather than trying
# to patch pyproject.toml. We preserve upstream’s lower bounds but remove upper
# bounds, as we must try to make do with what we have.
#
# Since requirements-tests.txt and requirements-docs-tests.txt contain
# overly-strict version bounds and many unwanted
# linting/coverage/typechecking/formatting dependencies
# (https://docs.fedoraproject.org/en-US/packaging-guidelines/Python/#_linters),
# we just list the test dependencies we *do* want manually rather than trying
# to patch the requirements files. We preserve upstream’s lower bounds but
# remove upper bounds, as we must try to make do with what we have.
#
# tests:
# - Omitted due to
#   https://docs.fedoraproject.org/en-US/packaging-guidelines/Python/#_linters:
#   black, coverage[toml], mypy, pre-commit, ruff
# - Already a direct dependency, perhaps with different version bounds:
#   typing-extensions
# - Only needed for ignored tests/test_select_gen.py: black, jinja2
BuildRequires:  %{py3_dist dirty-equals} >= 0.11
BuildRequires:  %{py3_dist fastapi} >= 0.128
BuildRequires:  %{py3_dist httpx} >= 0.28.1
BuildRequires:  %{py3_dist pytest} >= 7.0.1

%global common_description %{expand:
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

%if %{defined fc43} || %{defined fc44} || %{defined fc45}
# Removed when the package was unretired, after upstream deprecated
# sqlalchemy-slim. Because retirement happened for F43, the -slim package last
# appeared in F42, so we only need an upgrade path through F45.
Obsoletes:      python3-sqlmodel-slim < 0.0.37-1
%endif

%description -n python3-sqlmodel %{common_description}


%prep -a
# Remove bundled js-termynal 0.0.1; since we are not building documentation, we
# do this very bluntly:
rm -rvf docs/*/docs/js docs/*/docs/css


%check -a
# Ignore tutorial tests that are specifically associated with older Python
# versions; a few of these fail on later versions, and that is OK.
for pyver in 310
do
  if [ '%{python3_version_nodots}' != "${pyver}" ]
  then
    ignore="${ignore-} --ignore-glob=*tutorial/*/*_py${pyver}[/._]*"
  fi
done

# This uses black to format Python code generated via a Jinja2 template, and it
# appears to depend on the exact formatted output, which is the brittleness
# cautioned against in
# https://docs.fedoraproject.org/en-US/packaging-guidelines/Python/#_linters.
ignore="${ignore-} --ignore=tests/test_select_gen.py"

# Ignore all DeprecationWarning messages, as they pop up from various
# dependencies in practice. Upstream deals with this by tightly controlling
# dependency versions in CI.
warningsfilter="${warningsfilter-} -W ignore::DeprecationWarning"

# We need the working directory in the path so that certain tests can execute
# things like:
#   python3 -m docs_src.tutorial.something_or_other
export PYTHONPATH="%{buildroot}%{python3_sitelib}:${PWD}"

%pytest ${warningsfilter-} -k "${k-}" ${ignore-} -v -rs


%files -n python3-sqlmodel -f %{pyproject_files}
%doc CITATION.cff
%doc README.md


%changelog
%autochangelog
