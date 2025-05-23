# Generated by rust2rpm 27
%bcond check 1
%global debug_package %{nil}

%global crate pnet_sys

Name:           rust-pnet_sys
Version:        0.35.0
Release:        %autorelease
Summary:        Access to network related system function and calls

License:        MIT OR Apache-2.0
URL:            https://crates.io/crates/pnet_sys
Source:         %{crates_source}
# Automatically generated patch to strip dependencies and normalize metadata
Patch:          pnet_sys-fix-metadata-auto.diff

BuildRequires:  cargo-rpm-macros >= 24

%global _description %{expand:
Access to network related system function and calls.}

%description %{_description}

%package        devel
Summary:        %{summary}
BuildArch:      noarch

%description    devel %{_description}

This package contains library source intended for building other packages which
use the "%{crate}" crate.

%files          devel
%license %{crate_instdir}/LICENSE-APACHE
%license %{crate_instdir}/LICENSE-MIT
%doc %{crate_instdir}/README.md
%{crate_instdir}/

%package     -n %{name}+default-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+default-devel %{_description}

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%files       -n %{name}+default-devel
%ghost %{crate_instdir}/Cargo.toml

%prep
%autosetup -n %{crate}-%{version} -p1
%cargo_prep

%generate_buildrequires
%cargo_generate_buildrequires

%build
%cargo_build

%install
%cargo_install

%if %{with check}
%check
# * get_socket_receive_timeout resulted in error: Bad file descriptor (os error
#   9)
# * https://github.com/libpnet/libpnet/issues/412
%{cargo_test -- -- --exact %{shrink:
    --skip tests::test_get_socket_receive_timeout
    --skip tests::test_set_socket_receive_timeout_1500ms
    --skip tests::test_set_socket_receive_timeout_1s
    --skip tests::test_set_socket_receive_timeout_500ms
}}
%endif

%changelog
%autochangelog
