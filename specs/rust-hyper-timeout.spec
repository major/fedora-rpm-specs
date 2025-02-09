# Generated by rust2rpm 27
%bcond check 1
%global debug_package %{nil}

%global crate hyper-timeout

Name:           rust-hyper-timeout
Version:        0.5.2
Release:        %autorelease
Summary:        Connect, read and write timeout aware connector to be used with hyper Client

License:        MIT OR Apache-2.0
URL:            https://crates.io/crates/hyper-timeout
Source:         %{crates_source}

BuildRequires:  cargo-rpm-macros >= 24

%global _description %{expand:
A connect, read and write timeout aware connector to be used with hyper
Client.}

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
# * tests::test_read_timeout: Probably failing because of DNS resolution
# * test_upload_timeout: Flaky test
%{cargo_test -- -- %{shrink:
    --skip tests::test_read_timeout
    --skip test_upload_timeout
}}
%endif

%changelog
%autochangelog
