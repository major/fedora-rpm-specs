# Generated by rust2rpm 27
%bcond check 1
%global debug_package %{nil}

%global crate rust-embed-impl

Name:           rust-rust-embed-impl
Version:        8.7.2
Release:        %autorelease
Summary:        Custom Derive Macro which loads files into the rust binary

License:        MIT
URL:            https://crates.io/crates/rust-embed-impl
Source:         %{crates_source}
# Manually created patch for downstream crate metadata changes
# * drop unused compression and mime-guess features
Patch:          rust-embed-impl-fix-metadata.diff

BuildRequires:  cargo-rpm-macros >= 24

%global _description %{expand:
Rust Custom Derive Macro which loads files into the rust binary at
compile time during release and loads the file from the fs during dev.}

%description %{_description}

%package        devel
Summary:        %{summary}
BuildArch:      noarch

%description    devel %{_description}

This package contains library source intended for building other packages which
use the "%{crate}" crate.

%files          devel
%license %{crate_instdir}/license
%doc %{crate_instdir}/readme.md
%{crate_instdir}/

%package     -n %{name}+default-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+default-devel %{_description}

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%files       -n %{name}+default-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+debug-embed-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+debug-embed-devel %{_description}

This package contains library source intended for building other packages which
use the "debug-embed" feature of the "%{crate}" crate.

%files       -n %{name}+debug-embed-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+deterministic-timestamps-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+deterministic-timestamps-devel %{_description}

This package contains library source intended for building other packages which
use the "deterministic-timestamps" feature of the "%{crate}" crate.

%files       -n %{name}+deterministic-timestamps-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+include-exclude-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+include-exclude-devel %{_description}

This package contains library source intended for building other packages which
use the "include-exclude" feature of the "%{crate}" crate.

%files       -n %{name}+include-exclude-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+interpolate-folder-path-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+interpolate-folder-path-devel %{_description}

This package contains library source intended for building other packages which
use the "interpolate-folder-path" feature of the "%{crate}" crate.

%files       -n %{name}+interpolate-folder-path-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+shellexpand-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+shellexpand-devel %{_description}

This package contains library source intended for building other packages which
use the "shellexpand" feature of the "%{crate}" crate.

%files       -n %{name}+shellexpand-devel
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
