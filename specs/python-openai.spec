%global srcname openai

# Realtime support requires websockets >= 13.0.0, which is available on
# Fedora 42+.
%if 0%{?fedora} >= 42
%bcond realtime 1
%else
%bcond realtime 0
%endif

Name:           python-%{srcname}
Version:        1.95.1
Release:        %autorelease
Summary:        The official Python library for the OpenAI API

License:        Apache-2.0
URL:            https://github.com/openai/openai-python
Source:         %{pypi_source}

# Patch to relax hatchling version requirement
Patch1:         0001-Relax-hatchling-requirement.patch

BuildArch:      noarch
BuildRequires:  python3-devel

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

# The "aiohttp", "datalib" and "voice_helpers" extras are not available on
# Fedora due to missing dependencies on "httpx_aiohttp", "pandas-stubs" and
# "sounddevice", respectively. We are skipping them for now.

%prep
%autosetup -p1 -n %{srcname}-%{version}

%generate_buildrequires
%pyproject_buildrequires %{?with_realtime:-x realtime}

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files -l %{srcname}

%check
# Run import tests to verify the package can be imported
%pyproject_check_import %{srcname} -e openai.helpers -e openai.helpers.*

# Note: Full test suite requires network access and API keys
# so we only run basic import tests

%files -n python3-%{srcname} -f %{pyproject_files}
%doc README.md CHANGELOG.md CONTRIBUTING.md
%license LICENSE
%{_bindir}/openai

%changelog
%autochangelog

