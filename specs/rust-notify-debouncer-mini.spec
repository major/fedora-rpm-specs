# Generated by rust2rpm 27
%bcond check 1
%global debug_package %{nil}

%global crate notify-debouncer-mini

Name:           rust-notify-debouncer-mini
Version:        0.6.0
Release:        %autorelease
Summary:        Notify mini debouncer for events

License:        MIT OR Apache-2.0
URL:            https://crates.io/crates/notify-debouncer-mini
Source:         %{crates_source}
# Manually created patch for downstream crate metadata changes
# * remove macOS-specific features
Patch:          notify-debouncer-mini-fix-metadata.diff

BuildRequires:  cargo-rpm-macros >= 24

%global _description %{expand:
Notify mini debouncer for events.}

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

%package     -n %{name}+crossbeam-channel-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+crossbeam-channel-devel %{_description}

This package contains library source intended for building other packages which
use the "crossbeam-channel" feature of the "%{crate}" crate.

%files       -n %{name}+crossbeam-channel-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+serde-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+serde-devel %{_description}

This package contains library source intended for building other packages which
use the "serde" feature of the "%{crate}" crate.

%files       -n %{name}+serde-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+serialization-compat-6-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+serialization-compat-6-devel %{_description}

This package contains library source intended for building other packages which
use the "serialization-compat-6" feature of the "%{crate}" crate.

%files       -n %{name}+serialization-compat-6-devel
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
