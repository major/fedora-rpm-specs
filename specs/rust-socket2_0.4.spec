# Generated by rust2rpm 25
%bcond_without check
%global debug_package %{nil}

%global crate socket2

Name:           rust-socket2_0.4
Version:        0.4.10
Release:        %autorelease
Summary:        Utilities for handling networking sockets

License:        MIT OR Apache-2.0
URL:            https://crates.io/crates/socket2
Source:         %{crates_source}
# Automatically generated patch to strip dependencies and normalize metadata
Patch:          socket2-fix-metadata-auto.diff

BuildRequires:  cargo-rpm-macros >= 24

%global _description %{expand:
Utilities for handling networking sockets with a maximal amount of
configuration possible intended.}

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

%package     -n %{name}+all-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+all-devel %{_description}

This package contains library source intended for building other packages which
use the "all" feature of the "%{crate}" crate.

%files       -n %{name}+all-devel
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