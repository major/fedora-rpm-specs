# Generated by rust2rpm 26
# * tests can only be run in-tree
%bcond_with check
%global debug_package %{nil}

%global crate actix

Name:           rust-actix
Version:        0.13.5
Release:        %autorelease
Summary:        Actor framework for Rust

License:        MIT OR Apache-2.0
URL:            https://crates.io/crates/actix
Source:         %{crates_source}

BuildRequires:  cargo-rpm-macros >= 24

%global _description %{expand:
Actor framework for Rust.}

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
%doc %{crate_instdir}/CHANGES.md
%doc %{crate_instdir}/MIGRATION.md
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

%package     -n %{name}+actix-macros-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+actix-macros-devel %{_description}

This package contains library source intended for building other packages which
use the "actix-macros" feature of the "%{crate}" crate.

%files       -n %{name}+actix-macros-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+actix_derive-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+actix_derive-devel %{_description}

This package contains library source intended for building other packages which
use the "actix_derive" feature of the "%{crate}" crate.

%files       -n %{name}+actix_derive-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+macros-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+macros-devel %{_description}

This package contains library source intended for building other packages which
use the "macros" feature of the "%{crate}" crate.

%files       -n %{name}+macros-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+mailbox_assert-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+mailbox_assert-devel %{_description}

This package contains library source intended for building other packages which
use the "mailbox_assert" feature of the "%{crate}" crate.

%files       -n %{name}+mailbox_assert-devel
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
