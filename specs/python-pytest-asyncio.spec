%bcond_without  tests

Name:           python-pytest-asyncio
Version:        1.3.0
Release:        %autorelease
BuildArch:      noarch
Summary:        Pytest support for asyncio
License:        Apache-2.0
URL:            https://github.com/pytest-dev/pytest-asyncio
Source:         %{pypi_source pytest_asyncio}
BuildRequires:  python3-devel
BuildRequires:  tomcli

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
tomcli set pyproject.toml lists delitem project.optional-dependencies.testing 'coverage>=.*'


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
export PYTEST_ADDOPTS="-k '\
not test_asyncio_mark_respects_parametrized_loop_policies and \
not test_asyncio_mark_respects_the_loop_policy and \
not test_can_use_explicit_event_loop_fixture and \
not test_closing_event_loop_in_sync_fixture_teardown_raises_warning and \
not test_event_loop_fixture_finalizer_raises_warning_when_fixture_leaves_loop_unclosed and \
not test_event_loop_fixture_finalizer_raises_warning_when_test_leaves_loop_unclosed and \
not test_event_loop_fixture_asyncgen_error and \
not test_event_loop_already_closed and \
not test_event_loop_fixture_handles_unclosed_async_gen and \
not test_standalone_test_does_not_trigger_warning_about_no_current_event_loop_being_set and \
not test_warns_when_scope_argument_is_present'"
%pytest
%else
%pyproject_check_import
%endif


%files -n python3-pytest-asyncio -f %{pyproject_files}
%doc README.rst


%changelog
%autochangelog
