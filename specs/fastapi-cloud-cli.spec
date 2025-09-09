Name:           fastapi-cloud-cli
Version:        0.1.5
Release:        %autorelease
Summary:        Deploy and manage FastAPI Cloud apps from the command line

License:        MIT
URL:            https://github.com/fastapilabs/fastapi-cloud-cli
# The GitHub archive contains a few useful files that the PyPI sdist does not,
# such as the release notes.
Source:         %{url}/archive/%{version}/%{name}-%{version}.tar.gz

# Downstream-only; patch out coverage from script test
# https://docs.fedoraproject.org/en-US/packaging-guidelines/Python/#_linters
Patch:          0001-Downstream-only-patch-out-coverage-from-script-test.patch

BuildSystem:            pyproject
BuildOption(install):   -L fastapi_cloud_cli
BuildOption(generate_buildrequires): -x standard

BuildArch:      noarch

%py_provides python3-fastapi-cloud-cli

# Since requirements-tests.txt contains overly-strict version bounds and
# unwanted linting/coverage/typechecking/formatting dependencies
# (https://docs.fedoraproject.org/en-US/packaging-guidelines/Python/#_linters),
# we just list the few test dependencies we *do* want manually rather than
# trying to patch the requirements file. We preserve upstream’s lower bounds
# but remove upper bounds, as we must try to make do with what we have.
BuildRequires:  %{py3_dist pytest} >= 4.4
BuildRequires:  %{py3_dist respx} >= 0.22

%global common_description %{expand:
%{summary}.}

%description %{common_description}


%pyproject_extras_subpkg -n fastapi-cloud-cli standard


%check
# Difficulties running the tests?
# https://github.com/fastapilabs/fastapi-cloud-cli/discussions/76
k="${k-}${k+ and }not test_asks_for_app_name_after_team"
k="${k-}${k+ and }not test_asks_for_name_and_value"
k="${k-}${k+ and }not test_can_skip_waiting"
k="${k-}${k+ and }not test_creates_app_on_backend"
k="${k-}${k+ and }not test_creates_config_folder_and_creates_git_ignore"
k="${k-}${k+ and }not test_creates_environment_variables_during_app_setup"
k="${k-}${k+ and }not test_does_not_duplicate_entry_in_git_ignore"
k="${k-}${k+ and }not test_exits_successfully_when_deployment_is_done"
k="${k-}${k+ and }not test_handles_invalid_auth"
k="${k-}${k+ and }not test_rejects_invalid_environment_variable_names"
k="${k-}${k+ and }not test_shows_error_for_invalid_waitlist_form_data"
k="${k-}${k+ and }not test_shows_error_when_trying_to_get_teams"
k="${k-}${k+ and }not test_shows_no_apps_found_message_when_team_has_no_apps"
k="${k-}${k+ and }not test_shows_selector_for_environment_variables"
k="${k-}${k+ and }not test_shows_teams"
k="${k-}${k+ and }not test_shows_waitlist_form_when_not_logged_in"
k="${k-}${k+ and }not test_shows_waitlist_form_when_not_logged_in_longer_flow"
k="${k-}${k+ and }not test_uses_existing_app"
# Unlike those listed above, this doesn’t fail in a git checkout, but the way
# in which it fails is similar to the above tests:
#   >           assert result.exit_code == 0
#   E           AssertionError: assert 1 == 0
#   E            +  where 1 = <Result OSError(6, 'No such device or address')>.exit_code
k="${k-}${k+ and }not test_asks_to_setup_the_app"

%pytest -k "${k-}" -v


%files -f %{pyproject_files}
%license LICENSE
%doc README.md
%doc release-notes.md


%changelog
%autochangelog
