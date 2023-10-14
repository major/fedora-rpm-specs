# Tests are disabled by default because they require network access.
# Try: fedpkg mockbuild --with tests --enable-network
%bcond tests 0

Name:           python-virtualenv-api
Version:        2.1.18
Release:        %autorelease
Summary:        An API for virtualenv/pip

License:        BSD-2-Clause
URL:            https://github.com/sjkingo/virtualenv-api
# The GitHub tarball contains tests and LICENSE absent from the PyPI sdist.
Source:         %{url}/archive/%{version}/virtualenv-api-%{version}.tar.gz

# Fix --system-site-packages tests
# https://github.com/sjkingo/virtualenv-api/pull/52
Patch:          %{url}/pull/52.patch
# Remove search test cases
# https://github.com/sjkingo/virtualenv-api/pull/48
Patch:          %{url}/pull/48.patch
# Always use the current interpreter for test_python_version
# https://github.com/sjkingo/virtualenv-api/pull/56
Patch:          %{url}/pull/56.patch
# Taken together, the above three patches fix:
#   2.1.18: pytest is failing in four units
#   https://github.com/sjkingo/virtualenv-api/issues/55

BuildArch:      noarch

BuildRequires:  python3-devel

# Upstream does not name pip and virtualenv as dependencies, but they should
# be. See also:
#   Add virtualenv package to dependencies list
#   https://github.com/sjkingo/virtualenv-api/pull/49
BuildRequires:  /usr/bin/virtualenv
BuildRequires:  /usr/bin/pip

%global common_description %{expand:
virtualenv is a tool to create isolated Python environments. Unfortunately, it
does not expose a native Python API. This package aims to provide an API in the
form of a wrapper around virtualenv.

It can be used to create and delete environments and perform package management
inside the environment.}

%description %{common_description}


%package -n     python3-virtualenv-api
Summary:        An API for virtualenv/pip

Requires:       /usr/bin/virtualenv
Requires:       /usr/bin/pip

%description -n python3-virtualenv-api %{common_description}


%prep
%autosetup -n virtualenv-api-%{version} -p1
%py3_shebang_fix example.py


%generate_buildrequires
%pyproject_buildrequires


%build
%pyproject_wheel


%install
%pyproject_install
%pyproject_save_files virtualenvapi


%check
%if %{with tests}
%{py3_test_envvars} '%{python3}' -m unittest -v tests.py
%else
%pyproject_check_import
%endif


%files -n python3-virtualenv-api -f %{pyproject_files}
%doc CHANGES.md
%doc README.rst
%doc example.py


%changelog
%autochangelog
