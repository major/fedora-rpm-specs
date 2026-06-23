Name:           python-httpx-aiohttp
Version:        0.1.12
Release:        %autorelease
Summary:        Aiohttp transport for HTTPX

License:        BSD-3-Clause
URL:            https://karpetrosyan.github.io/httpx-aiohttp/
Source:         %{pypi_source httpx_aiohttp}

BuildArch:      noarch
BuildRequires:  python3-devel


%global _description %{expand:
httpx-aiohttp - provides transports for httpx to work on top of aiohttp,
handling all high-level features like authentication, retries, and cookies
through httpx, while delegating low-level socket-level HTTP messaging to
aiohttp.}

%description %_description

%package -n     python3-httpx-aiohttp
Summary:        %{summary}

%description -n python3-httpx-aiohttp %_description


%prep
%autosetup -p1 -n httpx_aiohttp-%{version}


%generate_buildrequires
%pyproject_buildrequires


%build
%pyproject_wheel


%install
%pyproject_install
%pyproject_save_files -l httpx_aiohttp


%check
# Do not run the tests. Network is required.
%pyproject_check_import


%files -n python3-httpx-aiohttp -f %{pyproject_files}
%doc README.md CONTRIBUTING.md CHANGELOG.md


%changelog
%autochangelog
