Name:           python-aiohttp-retry
Version:        2.8.3
Release:        %autorelease
Summary:        Simple retry client for aiohttp

License:        MIT
URL:            https://github.com/inyutin/aiohttp_retry
Source:         %{url}/archive/v%{version}/aiohttp_retry-%{version}.tar.gz

BuildArch:      noarch
BuildRequires:  python3-devel
# For testing:
BuildRequires:  python3dist(pytest)
BuildRequires:  python3dist(pytest-aiohttp)
BuildRequires:  python3dist(pytest-asyncio)

%global _description %{expand:
Simple retry client for aiohttp}

%description %_description

%package -n python3-aiohttp-retry
Summary:        %{summary}

%description -n python3-aiohttp-retry %_description


%prep
%autosetup -p1 -n aiohttp_retry-%{version}
# The package looks unmaintained, so no issue was filled
sed -i "s/from tests.app import/from app import/g" tests/test_client.py


%generate_buildrequires
%pyproject_buildrequires


%build
%pyproject_wheel


%install
%pyproject_install
%pyproject_save_files aiohttp_retry


%check
%pytest --asyncio-mode=auto


%files -n python3-aiohttp-retry -f %{pyproject_files}
%doc README.md


%changelog
%autochangelog
