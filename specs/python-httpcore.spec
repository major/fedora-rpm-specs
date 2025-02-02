%global pypi_name httpcore

%if %{defined fedora}
%bcond_without tests
%endif

Name:           python-%{pypi_name}
Version:        1.0.7
Release:        %autorelease
Summary:        Minimal low-level HTTP client

# Automatically converted from old format: BSD - review is highly recommended.
License:        LicenseRef-Callaway-BSD
URL:            https://github.com/encode/httpcore
Source0:        %{url}/archive/%{version}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch

%description
The HTTP Core package provides a minimal low-level HTTP client, which does
one thing only: Sending HTTP requests. It does not provide any high level
model abstractions over the API, does not handle redirects, multipart uploads,
building authentication headers, transparent HTTP caching, URL parsing, etc.

%package -n     python3-%{pypi_name}
Summary:        %{summary}

BuildRequires:  python3-devel
BuildRequires:  python3-setuptools

%if %{with tests}
BuildRequires:  %{py3_dist pytest pytest-asyncio pytest-httpbin pytest-trio anyio}
%endif

%description -n python3-%{pypi_name}
The HTTP Core package provides a minimal low-level HTTP client, which does
one thing only: Sending HTTP requests. It does not provide any high level
model abstractions over the API, does not handle redirects, multipart uploads,
building authentication headers, transparent HTTP caching, URL parsing, etc.

%pyproject_extras_subpkg -n python3-httpcore http2,socks

%prep
%autosetup -n %{pypi_name}-%{version}
rm -rf %{pypi_name}.egg-info

%generate_buildrequires
%pyproject_buildrequires -x http2,socks

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files %{pypi_name}

%check
%if %{with tests}
%pytest -Wdefault
%endif

%files -n python3-%{pypi_name} -f %{pyproject_files}
%license LICENSE.md
%doc README.md

%changelog
%autochangelog
