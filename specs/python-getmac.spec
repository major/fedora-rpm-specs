%global srcname getmac

Name:           python-%{srcname}
Version:        0.9.5
Release:        %autorelease
Summary:        Python module to get the MAC address of local network interfaces and LAN hosts

License:        MIT
URL:            https://github.com/GhostofGoes/getmac
Source0:        %pypi_source

BuildArch:      noarch
BuildRequires:  python3-devel
# For tests
BuildRequires:  python3-pytest
BuildRequires:  python3-pytest-mock
BuildRequires:  python3-pytest-benchmark

%description
Pure-python module to get the MAC address of remote hosts or network interfaces.
It provides a platform-independent interface to get the MAC addresses of network
interfaces on the local system(by interface name) and remote hosts on the local
network (by IPv4/IPv6 address or host-name).

%package -n python3-%{srcname}
Summary:        %{summary}

%description -n python3-%{srcname}
Pure-python module to get the MAC address of remote hosts or network interfaces.
It provides a platform-independent interface to get the MAC addresses of network
interfaces on the local system(by interface name) and remote hosts on the local
network (by IPv4/IPv6 address or host-name).

%prep
%autosetup -n %{srcname}-%{version}
# Remove shebang from __main__.py
sed -i '1{/^#!\//d}' getmac/__main__.py

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files %{srcname}

%check
%pyproject_check_import
%pytest -k "not test_initialize_method_cache_valid_types"

%files -n python3-%{srcname} -f %{pyproject_files}
%doc README.md
%{_bindir}/getmac

%changelog
%autochangelog
