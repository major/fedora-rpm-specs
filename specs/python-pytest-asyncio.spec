%global _without_tests 1
%bcond_without  tests

Name:           python-pytest-asyncio
Version:        0.26.0
Release:        %autorelease
Summary:        Pytest support for asyncio
License:        Apache-2.0
URL:            https://github.com/pytest-dev/pytest-asyncio
Source:         %{pypi_source pytest_asyncio}
BuildArch:      noarch
BuildRequires:  python3-devel

%global _description %{expand:
pytest-asyncio is a pytest plugin.  It facilitates testing of code that uses the
asyncio library.  Specifically, pytest-asyncio provides support for coroutines
as test functions.  This allows users to await code inside their tests.}


%description %{_description}


%package -n python3-pytest-asyncio
Summary:        %{summary}


%description -n python3-pytest-asyncio %{_description}


%prep
%autosetup -n pytest_asyncio-%{version}

# disable code quality checks in "testing" extras
sed -e '/coverage >=/d' \
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
%pyproject_save_files -l pytest_asyncio


%check
%if %{with tests}
# Some of the upstream tests are really picky about the number of warnings
# emitted.  This can cause failures for us in rawhide with the latest versions
# of pytest and pre-release versions of python, so we'll skip those tests.
export PYTEST_ADDOPTS="-k 'not test_can_use_explicit_event_loop_fixture and \
not test_event_loop_fixture_finalizer_raises_warning_when_fixture_leaves_loop_unclosed and \
not test_event_loop_fixture_finalizer_raises_warning_when_test_leaves_loop_unclosed and \
not test_event_loop_fixture_asyncgen_error and \
not test_event_loop_already_closed and \
not test_event_loop_fixture_handles_unclosed_async_gen'"
%pytest
%else
%pyproject_check_import
%endif


%files -n python3-pytest-asyncio -f %{pyproject_files}
%doc README.rst


%changelog
%autochangelog
