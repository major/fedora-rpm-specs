Name:           python-dirty-equals
Version:        0.7.0
Release:        %autorelease
Summary:        Doing dirty (but extremely useful) things with equals

# SPDX
License:        MIT
URL:            https://github.com/samuelcolvin/dirty-equals
# 0.7.0 was not published to PyPI
# https://github.com/samuelcolvin/dirty-equals/issues/79
# Source:         %%{pypi_source dirty_equals}
Source:         %{url}/archive/v%{version}/dirty-equals-%{version}.tar.gz

# fix pydantic version checking
# https://github.com/samuelcolvin/dirty-equals/commit/9ea7e27853c08096090abd5dcc3bb5234afa509c
Patch:          %{url}/commit/9ea7e27853c08096090abd5dcc3bb5234afa509c.patch

BuildArch:      noarch

BuildRequires:  python3-devel

# For Pydantic version check:
BuildRequires:  %{py3_dist packaging}

%global common_description %{expand:
The dirty-equals Python library (mis)uses the __eq__ method to make python code
(generally unit tests) more declarative and therefore easier to read and write.

You can use dirty-equals in whatever context you like, but it comes into its
own when writing unit tests for applications where you’re commonly checking the
response to API calls and the contents of a database.}

%description %{common_description}


%package -n python3-dirty-equals
Summary:        %{summary}

%description -n python3-dirty-equals %{common_description}


%pyproject_extras_subpkg -n python3-dirty-equals pydantic


%prep
%autosetup -n dirty-equals-%{version} -p1

# Patch out coverage analysis dependencies
# https://docs.fedoraproject.org/en-US/packaging-guidelines/Python/#_linters
#
# Patch out pytest-pretty, which is purely cosmetic
#
# Patch out pytest-examples, which would enable tests in tests/test_docs.py,
# but which has a hard dependency on ruff, a Python linter written in Rust that
# would be useful but nontrivial to package.
sed -r 's/^(coverage|pytest-(pretty|examples))/# \1/' requirements/tests.in |
  tee requirements/tests-filtered.txt

# Erroring on DeprecationWarnings makes sense upstream, but is probably too
# strict for distribution packaging.
#
# This specifically works around:
#
# DeprecationWarning for datetime.utcfromtimestamp() in Python 3.12
# https://github.com/samuelcolvin/dirty-equals/issues/71
sed -r -i 's/^filterwarnings = "error"$/# &/' pyproject.toml


%generate_buildrequires
%pyproject_buildrequires -x pydantic requirements/tests-filtered.txt


%build
%pyproject_wheel


%install
%pyproject_install
%pyproject_save_files dirty_equals


%check
# Tests in this module require pytest-examples; see %%prep for notes on this.
ignore="${ignore-} --ignore=tests/test_docs.py"

# Testing the Pydantic version at build time allows us to run all tests on
# Pydantic v1 while using the same spec file to prepare for Pydantic v2. The
# version test can be removed once Pydantic v2 is in Rawhide.
if '%{python3}' -c 'from pydantic import VERSION
from packaging.version import Version
yes, no = 0, 1
raise SystemExit(no if Version(VERSION) < Version("2") else yes)'
then
  # IsUrl seems to be broken with pydantic-2
  # https://github.com/samuelcolvin/dirty-equals/issues/72
  k="${k-}${k+ and }not test_is_url_true[https://example.com-IsUrl]"
  k="${k-}${k+ and }not test_is_url_true[https://example.com-dirty1]"
fi

# unix datetime tests fail if TZ != UTC
TZ=utc %pytest -v ${ignore-} -k "${k-}"


%files -n python3-dirty-equals -f %{pyproject_files}
# pyproject_files handles LICENSE; verify with “rpm -qL -p …”
%doc README.md


%changelog
%autochangelog
