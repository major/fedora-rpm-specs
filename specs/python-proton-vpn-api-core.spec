%global         srcname         python-proton-vpn-api-core
%global         shortname       proton-vpn-api-core
%global         forgeurl        https://github.com/ProtonVPN/python-proton-vpn-api-core
Version:        0.36.6
%global         tag             v%{version}
%forgemeta

Name:           %{srcname}
Release:        %autorelease
Summary:        Expose a uniform API to available Proton VPN services

License:        GPL-3.0-or-later
URL:            %{forgeurl}
Source:         %{forgesource}

BuildRequires:  python3-devel
BuildRequires:  python3dist(pytest)
BuildRequires:  python3dist(pytest-asyncio)

BuildArch: noarch

%global _description %{expand:
The proton-vpn-core-api acts as a facade to the other Proton VPN components,
exposing a uniform API to the available Proton VPN services.}

%description %_description

%package -n python3-%{shortname}
Summary:        %{summary}

%description -n python3-%{shortname} %_description


%prep
%forgesetup
# Do not measure test coverage
sed -i '/addopts = --cov=proton\/vpn\/core\/ --cov-report html --cov-report term/d' setup.cfg 

%generate_buildrequires
%pyproject_buildrequires


%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files proton

%check
%pyproject_check_import
# Do not run test that depend on network access
k="${k-}${k+ and }not (test_ensure_configuration_file_is_created)"
k="${k-}${k+ and }not (test_ensure_configuration_file_is_deleted)"
k="${k-}${k+ and }not (test_ensure_generate_is_returning_expected_content)"
k="${k-}${k+ and }not (test_ensure_same_configuration_file_in_case_of_duplicate)"
k="${k-}${k+ and }not (test_ovpnconfig_with_settings[udp])"
k="${k-}${k+ and }not (test_ovpnconfig_with_settings[tcp])"
k="${k-}${k+ and }not (test_ovpnconfig_with_certificate[udp])"
k="${k-}${k+ and }not (test_ovpnconfig_with_certificate[tcp])"
k="${k-}${k+ and }not (test_wireguard_config_content_Generation)"
k="${k-}${k+ and }not (test_wireguard_with_non_certificate)"

%pytest -k "${k-}"

%files -n python3-%{shortname} -f %{pyproject_files}
%doc CHANGELOG.md
%doc README.md
%license LICENSE

%changelog
%autochangelog
