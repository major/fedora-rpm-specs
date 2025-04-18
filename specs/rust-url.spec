# Generated by rust2rpm 27
%bcond check 1
%global debug_package %{nil}

%global crate url

Name:           rust-url
Version:        2.5.4
Release:        %autorelease
Summary:        URL library for Rust, based on the WHATWG URL Standard

License:        MIT OR Apache-2.0
URL:            https://crates.io/crates/url
Source:         %{crates_source}
# Automatically generated patch to strip dependencies and normalize metadata
Patch:          url-fix-metadata-auto.diff
# Manually created patch for downstream crate metadata changes
# * drop unused, benchmark-only bencher dev-dependency
Patch:          url-fix-metadata.diff

BuildRequires:  cargo-rpm-macros >= 24

%global _description %{expand:
URL library for Rust, based on the WHATWG URL Standard.}

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

%package     -n %{name}+expose_internals-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+expose_internals-devel %{_description}

This package contains library source intended for building other packages which
use the "expose_internals" feature of the "%{crate}" crate.

%files       -n %{name}+expose_internals-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+serde-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+serde-devel %{_description}

This package contains library source intended for building other packages which
use the "serde" feature of the "%{crate}" crate.

%files       -n %{name}+serde-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+std-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+std-devel %{_description}

This package contains library source intended for building other packages which
use the "std" feature of the "%{crate}" crate.

%files       -n %{name}+std-devel
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
