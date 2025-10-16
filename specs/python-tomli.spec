# Whether to build extension modules with mypyc:
%bcond          mypyc 1

Name:           python-tomli
Version:        2.3.0
Release:        %autorelease
Summary:        A little TOML parser for Python

License:        MIT
URL:            https://pypi.org/project/tomli/
Source0:        https://github.com/hukkin/tomli/archive/%{version}/%{name}-%{version}.tar.gz

BuildRequires:  python3-devel

%if %{with mypyc}
BuildRequires:  gcc
# scripts/use_setuptools.py uses tomli-w.
BuildRequires:  python3-tomli-w
%else
BuildArch:      noarch
%endif

# The test suite uses the stdlib's unittest framework, but we use %%pytest
# as the test runner.
BuildRequires:  python3-pytest

%global _description %{expand:
Tomli is a Python library for parsing TOML.
Tomli is fully compatible with TOML v1.0.0.}


%description %_description

%package -n python3-tomli
Summary:        %{summary}

%description -n python3-tomli %_description


%prep
%autosetup -p1 -n tomli-%{version}
%if %{with mypyc}
# Taken from .github/workflows/tests.yaml, uses tomli-w, required for mypyc.
%{python3} scripts/use_setuptools.py
%endif


%generate_buildrequires
%pyproject_buildrequires


%build
%if %{with mypyc}
export TOMLI_USE_MYPYC=1
%endif
%pyproject_wheel


%install
%pyproject_install
# There is a top-level <hash>_mypyc module:
# https://github.com/hukkin/tomli/issues/268
%pyproject_save_files tomli %{?with_mypyc:'*_mypyc'}


%check
%pyproject_check_import
%pytest


%files -n python3-tomli -f %{pyproject_files}
%doc README.md
%doc CHANGELOG.md
%license LICENSE


%changelog
%autochangelog
