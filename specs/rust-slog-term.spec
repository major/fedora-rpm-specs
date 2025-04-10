# Generated by rust2rpm 26
%bcond_without check
%global debug_package %{nil}

%global crate slog-term

Name:           rust-slog-term
Version:        2.9.1
Release:        %autorelease
Summary:        Unix terminal drain and formatter for slog-rs

License:        MPL-2.0 OR MIT OR Apache-2.0
URL:            https://crates.io/crates/slog-term
Source:         %{crates_source}

BuildRequires:  cargo-rpm-macros >= 24

%global _description %{expand:
Unix terminal drain and formatter for slog-rs.}

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
%license %{crate_instdir}/LICENSE-MPL2
%doc %{crate_instdir}/CHANGELOG.md
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

%package     -n %{name}+erased-serde-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+erased-serde-devel %{_description}

This package contains library source intended for building other packages which
use the "erased-serde" feature of the "%{crate}" crate.

%files       -n %{name}+erased-serde-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+nested-values-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+nested-values-devel %{_description}

This package contains library source intended for building other packages which
use the "nested-values" feature of the "%{crate}" crate.

%files       -n %{name}+nested-values-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+serde-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+serde-devel %{_description}

This package contains library source intended for building other packages which
use the "serde" feature of the "%{crate}" crate.

%files       -n %{name}+serde-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+serde_json-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+serde_json-devel %{_description}

This package contains library source intended for building other packages which
use the "serde_json" feature of the "%{crate}" crate.

%files       -n %{name}+serde_json-devel
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
