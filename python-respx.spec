%global pypi_name respx

Name:           python-%{pypi_name}
Version:        0.19.2
Release:        %autorelease
Summary:        Utility for mocking out the HTTPX and HTTP Core libraries

License:        BSD
URL:            https://lundberg.github.io/respx/
Source0:        https://github.com/lundberg/respx/archive/%{version}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch

# Fix test failures with pytest-asyncio >= 0.19
# Resolved upstream: https://github.com/lundberg/respx/pull/201
Patch0:         fix-pytest-asyncio-ftbfs.patch

%description
An utility for mocking out the Python HTTPX and HTTP Core libraries.

%package -n     python3-%{pypi_name}
Summary:        %{summary}

BuildRequires:  python3-devel
BuildRequires:  python3dist(httpx)
BuildRequires:  python3dist(httpcore)
BuildRequires:  python3dist(flask)
BuildRequires:  python3dist(setuptools)
BuildRequires:  python3dist(starlette)
BuildRequires:  python3dist(pytest)
BuildRequires:  python3dist(pytest-cov)
BuildRequires:  python3dist(pytest-asyncio)
BuildRequires:  python3dist(trio)
%{?python_provide:%python_provide python3-%{pypi_name}}

%description -n python3-%{pypi_name}
An utility for mocking out the Python HTTPX and HTTP Core libraries.

%prep
%autosetup -n %{pypi_name}-%{version} -p1
rm -rf %{pypi_name}.egg-info
# Coverage is under 100 % due to the excluded tests
sed -i -e '/--cov-fail-under 100/d' setup.cfg

%build
%py3_build

%install
%py3_install

%check
%pytest -v tests -k "not test_pass_through" --asyncio-mode=legacy

%files -n python3-%{pypi_name}
%license LICENSE.md
%doc README.md
%{python3_sitelib}/%{pypi_name}/
%{python3_sitelib}/%{pypi_name}-%{version}-py%{python3_version}.egg-info/

%changelog
%autochangelog

