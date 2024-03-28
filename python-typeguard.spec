Name:           python-typeguard
Version:        4.2.1
Release:        %autorelease
Summary:        Run-time type checker for Python

# SPDX
License:        MIT
URL:            https://github.com/agronholm/typeguard
Source:         %{pypi_source typeguard}

BuildArch:      noarch

BuildRequires:  python3-devel
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


%prep
%autosetup -n typeguard-%{version}

# Downstream-only: do not treat warnings in tests as errors
#
# This makes sense for upstream development and CI, but is too strict for
# distribution packaging.
tomcli set pyproject.toml lists delitem \
    'tool.pytest.ini_options.filterwarnings' error

# https://docs.fedoraproject.org/en-US/packaging-guidelines/Python/#_linters
tomcli set pyproject.toml lists delitem --type regex \
    'project.optional-dependencies.test' 'coverage\b.*'
# Note that we *do* need mypy for some of the tests; it is not just a
# “typechecking linter.”


%generate_buildrequires
export SETUPTOOLS_SCM_PRETEND_VERSION='%{version}'
%pyproject_buildrequires -x test


%build
export SETUPTOOLS_SCM_PRETEND_VERSION='%{version}'
%pyproject_wheel


%install
export SETUPTOOLS_SCM_PRETEND_VERSION='%{version}'
%pyproject_install
%pyproject_save_files -l typeguard


%check
%pytest -v -rs


%files -n python3-typeguard -f %{pyproject_files}
%doc README.rst


%changelog
%autochangelog
