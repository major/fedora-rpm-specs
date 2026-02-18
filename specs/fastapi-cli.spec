Name:           fastapi-cli
Version:        0.0.23
Release:        %autorelease
Summary:        Run and manage FastAPI apps from the command line with FastAPI CLI

License:        MIT
URL:            https://github.com/fastapi/fastapi-cli
Source0:        %{url}/archive/%{version}/%{name}-%{version}.tar.gz

# Downstream-only: run test_script without coverage
# https://docs.fedoraproject.org/en-US/packaging-guidelines/Python/#_linters
Patch:          0001-Downstream-only-run-test_script-without-coverage.patch

BuildSystem:            pyproject
BuildOption(generate_buildrequires): -x standard,standard-no-fastapi-cloud-cli,new
BuildOption(install):   -l fastapi_cli

BuildArch:      noarch

%py_provides python3-fastapi-cli

%if %{defined fc44} || %{defined fc45} || %{defined fc46}
# Removed in F44 after upstream deprecated fastapi-slim
Obsoletes:      fastapi-cli-slim < 0.0.21-1
%endif

# Since the “tests” dependency group contains overly-strict version bounds and
# many unwanted linting/coverage/typechecking/formatting dependencies
# (https://docs.fedoraproject.org/en-US/packaging-guidelines/Python/#_linters),
# we just list the few test dependencies we *do* want manually rather than
# trying to patch pyproject.toml. We preserve upstream’s lower bounds but
# remove upper bounds, as we must try to make do with what we have.
BuildRequires:  %{py3_dist pytest} >= 4.4
BuildRequires:  %{py3_dist fastapi} >= 0.128
BuildRequires:  %{py3_dist uvicorn} >= 0.39

%global common_description %{expand:
FastAPI CLI is a command line program fastapi that you can use to serve your
FastAPI app, manage your FastAPI project, and more.}

%description %{common_description}


%if %{defined fc44} || %{defined fc45} || %{defined fc46}
# We don’t use “%%pyproject_extras_subpkg -n fastapi-cli …” because we want
# to Obsolete the corresponding fastapi-cli-slim extras.

%package -n fastapi-cli+standard
Summary: Metapackage for fastapi-cli: standard extras
Requires: fastapi-cli = %{version}-%{release}
Obsoletes: fastapi-cli-slim+standard < 0.0.21-1
%description -n fastapi-cli+standard
This is a metapackage bringing in standard extras requires for fastapi-cli.
It makes sure the dependencies are installed.

%files -n fastapi-cli+standard
%ghost %dir %{python3_sitelib}/*.dist-info

%package -n fastapi-cli+standard-no-fastapi-cloud-cli
Summary: Metapackage for fastapi-cli: standard-no-fastapi-cloud-cli extras
Requires: fastapi-cli = %{version}-%{release}
Obsoletes: fastapi-cli-slim+standard-no-fastapi-cloud-cli < 0.0.21-1
%description -n fastapi-cli+standard-no-fastapi-cloud-cli
This is a metapackage bringing in standard-no-fastapi-cloud-cli extras requires
for fastapi-cli. It makes sure the dependencies are installed.

%files -n fastapi-cli+standard-no-fastapi-cloud-cli
%ghost %dir %{python3_sitelib}/*.dist-info

%package -n fastapi-cli+new
Summary: Metapackage for fastapi-cli: new extras
Requires: fastapi-cli = %{version}-%{release}
Obsoletes: fastapi-cli-slim+new < 0.0.21-1
%description -n fastapi-cli+new
This is a metapackage bringing in new extras requires for fastapi-cli.
It makes sure the dependencies are installed.

%files -n fastapi-cli+new
%ghost %dir %{python3_sitelib}/*.dist-info
%else
%pyproject_extras_subpkg -n fastapi-cli standard standard-no-fastapi-cloud-cli new
%endif


%check -a
%pytest -v


%files -f %{pyproject_files}
%doc CITATION.cff
%doc README.md
%doc release-notes.md


%changelog
%autochangelog
