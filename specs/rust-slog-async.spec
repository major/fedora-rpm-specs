# Generated by rust2rpm 24
%bcond_without check
%global debug_package %{nil}

%global crate slog-async

Name:           rust-slog-async
Version:        2.8.0
Release:        %autorelease
Summary:        Asynchronous drain for slog-rs

License:        MPL-2.0 OR MIT OR Apache-2.0
URL:            https://crates.io/crates/slog-async
Source:         %{crates_source}

BuildRequires:  rust-packaging >= 21

%global _description %{expand:
Asynchronous drain for slog-rs.}

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

%package     -n %{name}+dynamic-keys-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+dynamic-keys-devel %{_description}

This package contains library source intended for building other packages which
use the "dynamic-keys" feature of the "%{crate}" crate.

%files       -n %{name}+dynamic-keys-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+nested-values-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+nested-values-devel %{_description}

This package contains library source intended for building other packages which
use the "nested-values" feature of the "%{crate}" crate.

%files       -n %{name}+nested-values-devel
%ghost %{crate_instdir}/Cargo.toml

%prep
%autosetup -n %{crate}-%{version_no_tilde} -p1
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