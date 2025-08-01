# Generated by rust2rpm 27
# * tests can only be run in-tree
%bcond check 0
%global debug_package %{nil}

%global crate bytemuck_derive

Name:           rust-bytemuck_derive
Version:        1.10.0
Release:        %autorelease
Summary:        Derive proc-macros for bytemuck

License:        Zlib OR Apache-2.0 OR MIT
URL:            https://crates.io/crates/bytemuck_derive
Source:         %{crates_source}

BuildRequires:  cargo-rpm-macros >= 24

%global _description %{expand:
Derive proc-macros for `bytemuck`.}

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
%license %{crate_instdir}/LICENSE-ZLIB
%doc %{crate_instdir}/README.md
%doc %{crate_instdir}/changelog.md
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
%cargo_test
%endif

%changelog
%autochangelog
