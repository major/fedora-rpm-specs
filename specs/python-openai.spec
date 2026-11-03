%global srcname openai

%bcond realtime 1

%bcond aiohttp %{expr: 0%{?fedora} >= 45}


Name:           python-%{srcname}
Version:        3.42.1
Release:        %autorelease
Summary:        The official Python library for the OpenAI API

License:        Apache-2.0
URL:            https://github.com/openai/openai-python
Source:         %{pypi_source}

# Patch to relax hatchling version requirement
Patch:         0001-Relax-hatchling-requirement.patch

BuildArch:      noarch
BuildRequires:  python3-devel

# Test-suite-only dependencies
BuildRequires:  git-core
# provides /etc/mime.types (the tests expect .wav -> audio/wav)
BuildRequires:  mailcap
# the tests use the ps(1) command to check process state
BuildRequires:  procps-ng
# needed by the tests for the optional Bedrock provider (offline, mocked)
BuildRequires:  python3dist(botocore)
BuildRequires:  python3dist(inline-snapshot)
BuildRequires:  python3dist(pytest)
BuildRequires:  python3dist(pytest-asyncio)
BuildRequires:  python3dist(pytest-xdist)
BuildRequires:  python3dist(rich)
BuildRequires:  python3dist(trio)
BuildRequires:  python3dist(websockets)

%global _description %{expand:
The OpenAI Python library provides convenient access to the OpenAI REST API
from any Python 3.8+ application. The library includes type definitions for
all request params and response fields, and offers both synchronous and
asynchronous clients powered by httpx. It is generated from OpenAI's OpenAPI
specification with Stainless.}

%description %_description

%package -n python3-%{srcname}
Summary:        %{summary}

%description -n python3-%{srcname} %_description

# Include realtime support subpackage for WebSocket connections
%if %{with realtime}
%pyproject_extras_subpkg -n python3-%{srcname} realtime
%endif

# Include aiohttp support
%if %{with aiohttp}
%pyproject_extras_subpkg -n python3-%{srcname} aiohttp
%endif

# The "datalib" and "voice_helpers" extras are not available on
# Fedora due to missing dependencies on "pandas-stubs" and
# "sounddevice", respectively. We are skipping them for now.

%prep
%autosetup -p1 -n %{srcname}-%{version}

%generate_buildrequires
%pyproject_buildrequires %{?with_realtime:-x realtime} %{?with_aiohttp: -x aiohttp}

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files -l %{srcname}

%check
# Run import tests to verify the package can be imported
%pyproject_check_import %{srcname} -e openai.helpers -e openai.helpers.*

# Run the offline parts of the test suite.
#
# Tests that cannot run in the build environment are excluded:
# * tests/api_resources/ and tests/lib/test_fine_tuning_positional_arguments.py
#   require a running OpenAPI mock server (Prism) listening on
#   TEST_API_BASE_URL (http://127.0.0.1:4010 by default), i.e. network
#   access to a service that is not available during the package build.
# * tests/lib/responses/test_websocket_live.py connects to the live
#   OpenAI Responses WebSocket API and requires a real OPENAI_API_KEY.
# * tests/lib/test_vertex_live.py connects to the live Google Vertex AI
#   API and requires real GCP credentials.
# * tests/lib/chat/test_completions_streaming.py requires the
#   inline-snapshot external snapshot storage (.inline-snapshot/),
#   which is not shipped in the sdist.
# * tests/test_breaking_change_reexports.py requires griffe, which is
#   not packaged in Fedora.
# * The deselected tests/test_uv_workflows.py tests read workflow files
#   from the .github/ directory, which is not shipped in the sdist.
%pytest \
    --ignore=tests/api_resources \
    --ignore=tests/lib/chat/test_completions_streaming.py \
    --ignore=tests/lib/responses/test_websocket_live.py \
    --ignore=tests/lib/test_fine_tuning_positional_arguments.py \
    --ignore=tests/lib/test_vertex_live.py \
    --ignore=tests/test_breaking_change_reexports.py \
    --deselect tests/test_uv_workflows.py::test_fork_build_provenance_uses_immutable_pull_request_identity \
    --deselect tests/test_uv_workflows.py::test_routine_dependency_updates_preserve_lock_only_strategy \
    --deselect tests/test_uv_workflows.py::test_security_dependency_policy_is_directly_testable_after_the_trusted_gate \
    --deselect tests/test_uv_workflows.py::test_source_builds_only_allowed_in_trusted_experimental_compatibility

%files -n python3-%{srcname} -f %{pyproject_files}
%doc README.md CHANGELOG.md CONTRIBUTING.md
%license LICENSE

%changelog
%autochangelog

