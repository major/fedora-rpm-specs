%global _description \
SOCKS proxy connector for aiohttp. SOCKS4(a) and SOCKS5 are supported.

Name:           python-aiohttp-socks
Version:        0.10.1
Release:        %autorelease
Summary:        SOCKS proxy connector for aiohttp

License:        Apache-2.0
URL:            https://pypi.org/project/aiohttp-socks/
Source:         %{pypi_source aiohttp_socks}

BuildArch:      noarch

%description %{_description}

%package -n python3-aiohttp-socks
Summary:        %{summary}
BuildRequires:  python3-devel
BuildRequires:  python3-setuptools

%description -n python3-aiohttp-socks %{_description}

%prep
%autosetup -n aiohttp_socks-%{version}

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files aiohttp_socks

%files -n python3-aiohttp-socks -f %{pyproject_files}
%doc README.md

%changelog
%autochangelog
