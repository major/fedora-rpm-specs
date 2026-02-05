%global extras cli,rich,ws

Name:           python-mcp
Version:        1.26.0
Release:        %autorelease
Summary:        Model Context Protocol SDK

License:        MIT
URL:            https://modelcontextprotocol.io
Source:         %{pypi_source mcp}

# The uv-dynamic-version library is not present in Fedora 43, only Fedora 44.
# The below patch is replacing the dependency for `hatch-vcs`, as the sole
# purpose is to detect the version for this library.
Patch:          replace-uv-dynamic-version-with-hatchling-vcs.diff
# While pytest-xdist is available to use, it makes the logs of %%pytest very
# confusing to follow, so, it's better to just drop the CLI args that uses in
# the pytest invocation.
Patch1:         remove-pytest-xdist-cli-args.diff
# The test `test_lifespan_cleanup_executed` works correctly when executed
# locally inside a virtual env, but it fails in CI as we have a custom
# `PYTHONPATH` during the build, the test can't find the "mcp" library. That
# test in particular writes a python script to a temporary directory and tries
# to execute with.
Patch2:         pass_pythonpath_for_subprocess.diff
# The `subject` parameter was never by the pyjwt library to decode the jwt
# request, thus, causing a failure in Fedora 43 in the tests. This doesn't
# affect the testing itself.
Patch3:         remove-subject-from-exchange-request-test.diff

BuildArch:      noarch
BuildRequires:  python3-devel
BuildRequires:  tomcli
# Test dependencies
BuildRequires:  python3-pytest
BuildRequires:  python3-requests
BuildRequires:  python3-inline-snapshot
BuildRequires:  python3-dirty-equals

%global _description %{expand:
The Model Context Protocol allows applications to provide context for LLMs in a
standardized way, separating the concerns of providing context from the actual
LLM interaction. This Python SDK implements the full MCP specification.}

%description %_description

%package -n     python3-mcp
Summary:        %{summary}

%description -n python3-mcp %_description

%pyproject_extras_subpkg -n python3-mcp %{extras}


%prep
%autosetup -p1 -n mcp-%{version}

# relax dependency for pyjwt[crypto] as f43 has 2.8.0 and rawhide has 2.10+.
tomcli set pyproject.toml arrays replace project.dependencies '^pyjwt\[crypto\].*$' "pyjwt[crypto]>=2.8.0,<=2.11.0"


%generate_buildrequires
%pyproject_buildrequires -x %{extras}


%build
%pyproject_wheel


%install
%pyproject_install
%pyproject_save_files -l mcp


%check
%pyproject_check_import
# The following tests are ignored/disbaled due to:
#   * test_examples.py - Mainly verifying that the examples provided are
#   working as expected. No real coverage of code.
#
#   * test_command_execution - Tries to launch a mcp server that will reach out
#   to internet (python website), for that, it's disabled.
%pytest --ignore tests/test_examples.py -k "not test_command_execution"


%files -n python3-mcp -f %{pyproject_files}
%license LICENSE
%doc README.md
%doc SECURITY.md
%doc CODE_OF_CONDUCT.md
%{_bindir}/mcp

%changelog
%autochangelog
