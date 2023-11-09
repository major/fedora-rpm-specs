%global pypi_name pytest-httpx

Name:           python-%{pypi_name}
Version:        0.26.0
Release:        %autorelease
Summary:        Send responses to httpx

License:        MIT
URL:            https://colin-b.github.io/pytest_httpx/
Source0:        https://github.com/Colin-b/pytest_httpx/archive/v%{version}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch

%description
httpx_mock pytest fixture will make sure every httpx request will be
replied to with user provided responses.

%package -n     python3-%{pypi_name}
Summary:        %{summary}

BuildRequires:  python3-devel
BuildRequires:  python3dist(setuptools)
BuildRequires:  python3dist(httpx)
BuildRequires:  python3dist(pytest)
BuildRequires:  python3dist(pytest-asyncio)
%{?python_provide:%python_provide python3-%{pypi_name}}

%description -n python3-%{pypi_name}
httpx_mock pytest fixture will make sure every httpx request will be
replied to with user provided responses.

%prep
%autosetup -n pytest_httpx-%{version}
rm -rf %{pypi_name}.egg-info

%build
%py3_build

%install
%py3_install

%check
%pytest -v tests

%files -n python3-%{pypi_name}
%doc README.md
%license LICENSE
%{python3_sitelib}/pytest_httpx/
%{python3_sitelib}/pytest_httpx-%{version}-py%{python3_version}.egg-info/

%changelog
%autochangelog

