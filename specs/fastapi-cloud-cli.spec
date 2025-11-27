Name:           fastapi-cloud-cli
Version:        0.5.2
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
BuildRequires:  %{py3_dist time-machine} >= 2.15

%global common_description %{expand:
%{summary}.}

%description %{common_description}


%pyproject_extras_subpkg -n fastapi-cloud-cli standard


%check
%pytest -v


%files -f %{pyproject_files}
%license LICENSE
%doc README.md
%doc release-notes.md


%changelog
%autochangelog
