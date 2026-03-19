%global extras openai

Name:           python-fastmcp
Version:        2.14.5
Release:        %autorelease
Summary:        The fast, Pythonic way to build MCP servers and clients

License:        Apache-2.0
URL:            https://gofastmcp.com
Source:         %{pypi_source fastmcp}

# The uv-dynamic-version library is not present in Fedora 43, only Fedora 44.
# The below patch is replacing the dependency for `hatch-vcs`, as the sole
# purpose is to detect the version for this library.
Patch:          replace-uv-dynamic-version-with-hatchling-vcs.diff
# The following patches exists to fix either the `command` or `env` properties
# of some FastMCP transports.
#
#  * Fixes for the `command` property:
#       - The tests were trying to use `python`, and while this is a valid
#       binary in most cases, during the build we are expecting to use
#       `python3`, and to be more precise and avoid problems later, we are
#       using the full binary path `/usr/bin/python3` for this fix.
#
#  * Fixes for the `env` property:
#       - Some tests create a small python script that require importing
#       `fastmcp`, where they create a simple tool calling program for the
#       test. To fix those, we are passing the full `os.environ` copy to the
#       sub-process spawned by `fastmcp`. We could just pass `PYTHONPATH`, as
#       this is really the only thing that is required for the test, but to be
#       more complete, we are passing the all the available environments down
#       to the sub-process.
Patch1:         fix-python-stdio-trasnport-with-env-vars.diff
Patch2:         fix-command-for-python3-instead-of-python.diff
Patch3:         fix-environment-for-test-server.diff
Patch4:         fix-temporary-settings-test.diff
Patch5:         fix-environment-for-test-run.diff

BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  tomcli

# Test dependencies
BuildRequires:  python3-pytest
BuildRequires:  python3-pytest-httpx
BuildRequires:  python3-pytest-asyncio
BuildRequires:  python3-inline-snapshot
BuildRequires:  python3-dirty-equals
BuildRequires:  python3-fastapi
BuildRequires:  python3-psutil


%global _description %{expand:
FastMCP is the standard framework for building MCP applications, providing the
fastest path from idea to production.

The Model Context Protocol (MCP) is a standardized way to provide context and
tools to LLMs. FastMCP makes building production-ready MCP servers simple, with
enterprise auth, deployment tools, and a complete ecosystem built in.}


%description %_description

%package -n     python3-fastmcp
Summary:        %{summary}

%description -n python3-fastmcp %_description

%pyproject_extras_subpkg -n python3-fastmcp %{extras}


%prep
%autosetup -p1 -n fastmcp-%{version}

# Relax authlib version
tomcli set pyproject.toml arrays replace "project.dependencies" "authlib.*" "authlib >=1.4.0,<1.6.5"

# Relax pyperclip version
tomcli set pyproject.toml arrays replace "project.dependencies" "pyperclip.*" "pyperclip >=1.8.2,<1.9.0"
tomcli set pyproject.toml arrays replace "dependency-groups.dev" "pyperclip.*" "pyperclip >=1.8.2,<1.9.0"

# Relax openai optional dependency
# tomcli set pyproject.toml arrays replace "project.optional-dependencies.openai" "openai.*" "openai>=1.95"

%generate_buildrequires
%pyproject_buildrequires -x %{extras}


%build
%pyproject_wheel


%install
%pyproject_install
%pyproject_save_files -l fastmcp


%check
# Ignore anthropic as it is not present in Fedora and we are ignoring this
# extra.
%pyproject_check_import -e fastmcp.client.sampling.handlers.anthropic

# This test tries to reach out to github to download the full GitHub API
# schema, and while we could add this as `SourceX` to the spec, not sure if
# that would be worth it to enable just this test.
#
# The test in case is only checking if fastmcp can parse the schema quick
# enough, which is around 10mb~.
k="${k-}not test_github_api_schema_performance"

# Ignore the test that test the anthropic handler, which is not present in
# Fedora and not being packaged as a extra.
ignore="${ignore-} --ignore tests/client/sampling/handlers/test_anthropic_handler.py"
# The tests under `test_uv_transport` require the `uv` tool to be installed.
# While this is present in Fedora, the test will try to pull other dependencies
# when running through `uv`. Instead of modifying the test itself to run in
# isolation, we are ignoring it as our idea is to test the framework itself.
ignore="${ignore-} --ignore tests/client/transports/test_uv_transport.py"

%pytest --inline-snapshot=disable -v -k "${k-}" ${ignore-}


%files -n python3-fastmcp -f %{pyproject_files}
%doc SECURITY.md
%doc CODE_OF_CONDUCT.md
%doc README.md
%{_bindir}/fastmcp


%changelog
%autochangelog
