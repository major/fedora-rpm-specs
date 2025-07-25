# Generated by rust2rpm 27
%bcond check 1
%global debug_package %{nil}

%global crate rust-embed-utils

Name:           rust-rust-embed-utils
Version:        8.7.2
Release:        %autorelease
Summary:        Utilities for rust-embed

License:        MIT
URL:            https://crates.io/crates/rust-embed-utils
Source:         %{crates_source}
# Manually created patch for downstream crate metadata changes
# * drop unused mime-guess feature
Patch:          rust-embed-utils-fix-metadata.diff

BuildRequires:  cargo-rpm-macros >= 24

%global _description %{expand:
Utilities for rust-embed.}

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

%package     -n %{name}+globset-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+globset-devel %{_description}

This package contains library source intended for building other packages which
use the "globset" feature of the "%{crate}" crate.

%files       -n %{name}+globset-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+include-exclude-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+include-exclude-devel %{_description}

This package contains library source intended for building other packages which
use the "include-exclude" feature of the "%{crate}" crate.

%files       -n %{name}+include-exclude-devel
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
