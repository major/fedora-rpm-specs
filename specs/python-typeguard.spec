# Note that we *do* need mypy for some of the tests; it is not just a
# “typechecking linter.” However, we can optionally skip those tests.
%bcond mypy 1

Name:           python-typeguard
Version:        4.4.1
Release:        %autorelease
Summary:        Run-time type checker for Python

# SPDX
License:        MIT
URL:            https://github.com/agronholm/typeguard
Source:         %{pypi_source typeguard}

# Fixes for Python 3.14 and PEP 649
# https://github.com/agronholm/typeguard/pull/492
# Rebased on 4.4.1, with documentation changes removed
Patch:          typeguard-4.4.1-python-3.14.patch

BuildSystem:            pyproject
BuildOption(install):   -l typeguard
BuildOption(generate_buildrequires):  -x test

BuildArch:      noarch

BuildRequires:  tomcli

%global common_description %{expand:
This library provides run-time type checking for functions defined with PEP 484
argument (and return) type annotations.}

%description %{common_description}


%package -n python3-typeguard
Summary:        %{summary}

# Removed for F41:
Obsoletes:      python-typeguard-doc < 4.2.1-2

%description -n python3-typeguard %{common_description}


%prep -a
# Downstream-only: do not treat warnings in tests as errors
#
# This makes sense for upstream development and CI, but is too strict for
# distribution packaging.
tomcli set pyproject.toml lists delitem \
    'tool.pytest.ini_options.filterwarnings' error

# https://docs.fedoraproject.org/en-US/packaging-guidelines/Python/#_linters
tomcli set pyproject.toml lists delitem --type regex \
    'project.optional-dependencies.test' 'coverage\b.*'

%if %{without mypy}
tomcli set pyproject.toml lists delitem --type regex \
    project.optional-dependencies.test 'mypy\b.*'
%endif


%generate_buildrequires -p
export SETUPTOOLS_SCM_PRETEND_VERSION='%{version}'


%build -p
export SETUPTOOLS_SCM_PRETEND_VERSION='%{version}'


%check -a
%if %{without mypy}
k="${k-}${k+ and }not test_negative"
k="${k-}${k+ and }not test_positive"
%endif

%pytest -k "${k-}" -v -rs


%files -n python3-typeguard -f %{pyproject_files}
%doc README.rst


%changelog
%autochangelog
