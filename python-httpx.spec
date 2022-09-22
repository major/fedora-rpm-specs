%global pypi_name httpx

Name:           python-%{pypi_name}
Version:        0.23.0
Release:        %autorelease
Summary:        Python HTTP client

License:        BSD
URL:            https://github.com/encode/httpx
Source0:        %{pypi_source}
BuildArch:      noarch

%description
HTTPX is a fully featured HTTP client for Python, which provides sync and
async APIs, and support for both HTTP/1.1 and HTTP/2.

%package -n     python3-%{pypi_name}
Summary:        %{summary}

BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
%{?python_provide:%python_provide python3-%{pypi_name}}

%description -n python3-%{pypi_name}
HTTPX is a fully featured HTTP client for Python, which provides sync and
async APIs, and support for both HTTP/1.1 and HTTP/2.

%prep
%autosetup -n %{pypi_name}-%{version}
rm -rf %{pypi_name}.egg-info

%build
%py3_build

%install
%py3_install

%files -n python3-%{pypi_name}
%license LICENSE.md
%doc README.md
%{python3_sitelib}/%{pypi_name}/
%{python3_sitelib}/%{pypi_name}-%{version}-py%{python3_version}.egg-info/
%attr(755, root, root) %{_bindir}/httpx

%changelog
%autochangelog

