# Generated by rust2rpm 25
%bcond_without check

%global crate asahi-wifisync

Name:           rust-asahi-wifisync
Version:        0.2.0
Release:        %autorelease
Summary:        Tool to sync Wifi passwords with macos on ARM Macs

License:        MIT
URL:            https://crates.io/crates/asahi-wifisync
Source:         %{crates_source}

BuildRequires:  cargo-rpm-macros >= 24

%global _description %{expand:
A tool to sync Wifi passwords with macos on ARM Macs.}

%description %{_description}

%package     -n %{crate}
Summary:        %{summary}
# Apache-2.0 OR MIT
# MIT
# MIT OR Apache-2.0
# Unlicense OR MIT
# Zlib
License:        MIT AND Zlib AND (Apache-2.0 OR MIT) AND (Unlicense OR MIT)
# LICENSE.dependencies contains a full license breakdown

%description -n %{crate} %{_description}

%files       -n %{crate}
%license LICENSE
%license LICENSE.dependencies
%{_bindir}/asahi-wifisync

%prep
%autosetup -n %{crate}-%{version} -p1
%cargo_prep

%generate_buildrequires
%cargo_generate_buildrequires

%build
%cargo_build
%{cargo_license_summary}
%{cargo_license} > LICENSE.dependencies

%install
%cargo_install

%if %{with check}
%check
%cargo_test
%endif

%changelog
%autochangelog