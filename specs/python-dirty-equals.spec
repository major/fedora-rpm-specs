# Break a circular build dependency with python-pydantic
%bcond bootstrap 0

Name:           python-dirty-equals
Version:        0.11
Release:        %autorelease
Summary:        Doing dirty (but extremely useful) things with equals

# SPDX
License:        MIT
URL:            https://github.com/samuelcolvin/dirty-equals
Source:         %{pypi_source dirty_equals}

BuildSystem:            pyproject
%if %{without bootstrap}
BuildOption(generate_buildrequires): -x pydantic
%endif
BuildOption(install):   -l dirty_equals

BuildArch:      noarch

# See dependency-groups.dev in pyproject.toml, but there are coverage analysis
# tools, linters, and other unwanted dependencies
# (https://docs.fedoraproject.org/en-US/packaging-guidelines/Python/#_linters)
# mixed in, so we list the real test dependencies manually.
BuildRequires:  %{py3_dist packaging} >= 25
BuildRequires:  %{py3_dist pydantic} >= 2.10.6
BuildRequires:  %{py3_dist pytest} >= 8.3.5
# Not packaged: python-pytest-examples; would enable tests/test_docs.py
# BuildRequires:  %%{py3_dist pytest-examples} >= 0.0.18
# pytest-pretty is purely cosmetic

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


%prep -a
# Erroring on DeprecationWarnings makes sense upstream, but is probably too
# strict for distribution packaging.
#
# This specifically works around:
#
# DeprecationWarning for datetime.utcfromtimestamp() in Python 3.12
# https://github.com/samuelcolvin/dirty-equals/issues/71
sed -r -i 's/^filterwarnings = "error"$/# &/' pyproject.toml


%check -a
# Tests in this module require pytest-examples; see %%prep for notes on this.
ignore="${ignore-} --ignore=tests/test_docs.py"

%if %{with bootstrap}
# Imports in this module require Pydantic.
ignore="${ignore-} --ignore=tests/test_other.py"
%endif

%if v"0%{?python3_version}" >= v"3.14"
# Two test regressions related to IP addresses in Python 3.14
# https://github.com/samuelcolvin/dirty-equals/issues/112
k="${k-}${k+ and }not test_is_ip_true[other1-dirty1]"
k="${k-}${k+ and }not test_is_ip_true[other3-dirty3]"
%endif

# Some tests require TZ == UTC; see the “test” target in the Makefile
TZ=UTC %pytest ${ignore-} -k "${k-}" -v


%files -n python3-dirty-equals -f %{pyproject_files}
%doc README.md


%changelog
%autochangelog
