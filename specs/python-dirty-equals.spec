# Break a circular build dependency with python-pydantic
%bcond bootstrap 0

Name:           python-dirty-equals
Version:        0.9.0
Release:        %autorelease
Summary:        Doing dirty (but extremely useful) things with equals

# SPDX
License:        MIT
URL:            https://github.com/samuelcolvin/dirty-equals
Source:         %{pypi_source dirty_equals}

BuildArch:      noarch

BuildRequires:  python3-devel

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


%if %{without bootstrap}
%pyproject_extras_subpkg -n python3-dirty-equals pydantic
%endif


%prep
%autosetup -n dirty_equals-%{version}

# Patch out coverage analysis dependencies
# https://docs.fedoraproject.org/en-US/packaging-guidelines/Python/#_linters
#
# Patch out pytest-pretty, which is purely cosmetic
#
# Patch out pytest-examples, which would enable tests in tests/test_docs.py,
# but is not yet packaged.
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
%pyproject_buildrequires %{?!with_bootstrap:-x pydantic} requirements/tests-filtered.txt


%build
%pyproject_wheel


%install
%pyproject_install
%pyproject_save_files -l dirty_equals


%check
# Tests in this module require pytest-examples; see %%prep for notes on this.
ignore="${ignore-} --ignore=tests/test_docs.py"
%if %{with bootstrap}
# Imports in this module require Pydantic.
ignore="${ignore-} --ignore=tests/test_other.py"
%endif

# Some tests require TZ == UTC; see the “test” target in the Makefile
TZ=UTC %pytest -v ${ignore-}


%files -n python3-dirty-equals -f %{pyproject_files}
%doc README.md


%changelog
%autochangelog
