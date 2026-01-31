Name:           python-httpx-sse
Version:        0.4.3
Release:        %autorelease
Summary:        Consume Server-Sent Event (SSE) messages with HTTPX.
License:        MIT
URL:            https://github.com/florimondmanca/httpx-sse
Source:         %{pypi_source httpx_sse}

# Patch setup.cfg to remove --cov options from the pytest cli args.
Patch:          remove-coverage-options-from-pytest.diff

BuildArch:      noarch
BuildRequires:  python3-devel
BuildRequires:  python3-httpx
BuildRequires:  python3-sse-starlette
# Dependencies for testing
BuildRequires:  python3-pytest
BuildRequires:  python3-pytest-asyncio


%global _description %{expand:
Consume Server-Sent Event (SSE) messages with HTTPX.}

%description %_description

%package -n     python3-httpx-sse
Summary:        %{summary}

%description -n python3-httpx-sse %_description


%prep
%autosetup -p1 -n httpx_sse-%{version}


%generate_buildrequires
%pyproject_buildrequires


%build
%pyproject_wheel


%install
%pyproject_install
# Add top-level Python module names here as arguments, you can use globs
%pyproject_save_files -l httpx_sse


%check
%pyproject_check_import
%pytest

%files -n python3-httpx-sse -f %{pyproject_files}
%license LICENSE


%changelog
%autochangelog
