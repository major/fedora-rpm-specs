%global srcname openai

%bcond realtime 1

%bcond aiohttp %{expr: 0%{?fedora} >= 45}


Name:           python-%{srcname}
Version:        3.24.0
Release:        %autorelease
Summary:        The official Python library for the OpenAI API

License:        Apache-2.0
URL:            https://github.com/openai/openai-python
Source:         %{pypi_source}

# Patch to relax hatchling version requirement
Patch:         0001-Relax-hatchling-requirement.patch

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

# Note: Full test suite requires network access and API keys
# so we only run basic import tests

%files -n python3-%{srcname} -f %{pyproject_files}
%doc README.md CHANGELOG.md CONTRIBUTING.md
%license LICENSE

%changelog
%autochangelog

