%global pypi_name httpx

Name:           python-%{pypi_name}
Version:        0.26.0
Release:        %autorelease
Summary:        Python HTTP client

License:        BSD
URL:            https://github.com/encode/httpx
Source0:        %{url}/archive/%{version}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch

%description
HTTPX is a fully featured HTTP client for Python, which provides sync and
async APIs, and support for both HTTP/1.1 and HTTP/2.

%package -n     python3-%{pypi_name}
Summary:        %{summary}
BuildRequires:  python3-devel
BuildRequires:  python3-setuptools

%description -n python3-%{pypi_name}
HTTPX is a fully featured HTTP client for Python, which provides sync and
async APIs, and support for both HTTP/1.1 and HTTP/2.

%prep
%autosetup -n %{pypi_name}-%{version}

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files %{pypi_name}

%files -n python3-%{pypi_name} -f %{pyproject_files}
%license LICENSE.md
%doc README.md
%attr(755, root, root) %{_bindir}/httpx

%changelog
%autochangelog

