%global srcname pytest-asyncio
%global _description %{expand:
pytest-asyncio is an Apache2 licensed library, written in Python, for testing
asyncio code with pytest.

asyncio code is usually written in the form of coroutines, which makes it
slightly more difficult to test using normal testing tools. pytest-asyncio
provides useful fixtures and markers to make testing easier.}

%if %{undefined el9}
# EL9 missing pytest-trio
%bcond_without  tests
%endif

Name:           python-%{srcname}
Version:        0.20.1
Release:        %autorelease
Summary:        Pytest support for asyncio
License:        ASL 2.0
URL:            https://github.com/pytest-dev/pytest-asyncio
Source:         %pypi_source
BuildArch:      noarch
BuildRequires:  python3-devel


%description %{_description}


%package -n python3-%{srcname}
Summary:        %{summary}


%description -n python3-%{srcname} %{_description}


%prep
%autosetup -n %{srcname}-%{version}

# disable code quality checks in "testing" extras
sed -e '/coverage==/d' \
    -e '/mypy ==/d' \
    -i setup.cfg

%if %{defined el9}
# EL9 has setuptools_scm 6.0.1 that works
sed -e '/setuptools_scm/ s/>=6.2//' -i pyproject.toml
%endif


%generate_buildrequires
# upstream also has tox that invokes make that invokes pytest...
# we install the [testing] extra and will invoke pytest directly instead
%pyproject_buildrequires %{?with_tests:-x testing}


%build
%pyproject_wheel


%install
%pyproject_install
%pyproject_save_files pytest_asyncio


%check
%if %{with tests}
# tests/modes/test_legacy_mode.py fails when pytest is invoked by /usr/bin/pytest
# using python -m pytest works:
%global __pytest %{python3} -m pytest
%pytest
%else
%pyproject_check_import
%endif


%files -n python3-%{srcname} -f %{pyproject_files}
%doc README.rst CHANGELOG.rst


%changelog
%autochangelog
