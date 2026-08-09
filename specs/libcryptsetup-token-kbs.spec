%bcond check 0

%global crate libcryptsetup-token-kbs

Name:           %{crate}
Version:        2.0.0
Release:        %autorelease
Summary:        LUKS2 token plugin for TEE/KBS attestation-based volume unlock

License:        GPL-3.0-or-later AND MIT AND Unicode-3.0
URL:            https://github.com/MatiasVara/%{crate}
Source0:        %{url}/archive/v%{version}/%{crate}-%{version}.tar.gz

ExclusiveArch:  x86_64

BuildRequires:  cargo-rpm-macros >= 24
BuildRequires:  gcc
BuildRequires:  cryptsetup-devel

Requires:       cryptsetup-libs
Requires:       trustee-guest-components

%global _description %{expand:
LUKS2 external token plugin that unlocks encrypted volumes via TEE
attestation against a Key Broker Service (KBS). Tested with Intel TDX
but compatible with any TEE supported by trustee-attester.

Also ships repart-kbs-helper, a first-boot attestation helper used by
systemd-repart to obtain the LUKS encryption key.}

%description %{_description}

%prep
%autosetup -n %{crate}-%{version} -p1
%cargo_prep

%generate_buildrequires
%cargo_generate_buildrequires

%build
%cargo_build
%{cargo_license_summary}
%{cargo_license} > LICENSE.dependencies

%set_build_flags
%make_build

%install
%make_install INSTALL_DIR=%{_libdir}/cryptsetup
install -D -p -m 0755 target/release/repart-kbs-helper \
    %{buildroot}%{_libexecdir}/repart-kbs-helper

%files
%license LICENSE
%license LICENSE.dependencies
%doc README.md
%{_libdir}/cryptsetup/%{crate}.so
%{_libexecdir}/repart-kbs-helper

%changelog
%autochangelog
