%global         srcname         python-proton-vpn-network-manager
%global         shortname       proton-vpn-network-manager
%global         forgeurl        https://github.com/ProtonVPN/python-proton-vpn-network-manager
Version:        0.10.2
%global         tag             v%{version}
%forgemeta

Name:           %{srcname}
Release:        %autorelease
Summary:        Enable interaction with NetworkManager

License:        GPL-3.0-or-later
URL:            %{forgeurl}
Source:         %{forgesource}

BuildRequires:  NetworkManager
BuildRequires:  NetworkManager-openvpn
BuildRequires:  NetworkManager-openvpn-gnome
BuildRequires:  gobject-introspection
BuildRequires:  python3-devel
BuildRequires:  python3dist(pytest)
BuildRequires:  python3dist(pytest-asyncio)
Requires:  NetworkManager
Requires:  NetworkManager-openvpn
Requires:  NetworkManager-openvpn-gnome
Requires:  gobject-introspection

BuildArch: noarch

%global _description %{expand:
The proton-vpn-network-manager component provides the necessary functionality
for other components to interact with NetworkManager.}

%description %_description

%package -n python3-%{shortname}
Summary:        %{summary}

%description -n python3-%{shortname} %_description


%prep
%forgesetup
# Do not measure test coverage
sed -i '/addopts = --cov=proton\/vpn\/backend\/linux\/networkmanager --cov-report html --cov-report term/d' \
    setup.cfg 

%generate_buildrequires
%pyproject_buildrequires


%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files proton

%check
# local agent functionality not yet implemented
skip="proton.vpn.backend.linux.networkmanager.protocol.wireguard.local_agent.external_local_agent"
%pyproject_check_import -e ${skip}

%pytest

%files -n python3-%{shortname} -f %{pyproject_files}
%doc README.md
%license LICENSE

%changelog
%autochangelog
