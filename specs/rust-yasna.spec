# Generated by rust2rpm 26
%bcond_without check
%global debug_package %{nil}

%global crate yasna

Name:           rust-yasna
Version:        0.5.2
Release:        %autorelease
Summary:        ASN.1 library for Rust

License:        MIT OR Apache-2.0
URL:            https://crates.io/crates/yasna
Source:         %{crates_source}
# * https://github.com/qnighy/yasna.rs/issues/76
Source1:        https://github.com/qnighy/yasna.rs/raw/yasna-0.5.0/LICENSE-APACHE
Source2:        https://github.com/qnighy/yasna.rs/raw/yasna-0.5.0/LICENSE-MIT
# Manually created patch for downstream crate metadata changes
# * ensure license files are included in repackaged crate sources
Patch:          yasna-fix-metadata.diff
# * include downstream patch to fix test failure on i686
Patch2:         https://github.com/qnighy/yasna.rs/pull/73.patch

BuildRequires:  cargo-rpm-macros >= 24

%global _description %{expand:
ASN.1 library for Rust.}

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

%package     -n %{name}+bit-vec-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+bit-vec-devel %{_description}

This package contains library source intended for building other packages which
use the "bit-vec" feature of the "%{crate}" crate.

%files       -n %{name}+bit-vec-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+num-bigint-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+num-bigint-devel %{_description}

This package contains library source intended for building other packages which
use the "num-bigint" feature of the "%{crate}" crate.

%files       -n %{name}+num-bigint-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+std-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+std-devel %{_description}

This package contains library source intended for building other packages which
use the "std" feature of the "%{crate}" crate.

%files       -n %{name}+std-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+time-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+time-devel %{_description}

This package contains library source intended for building other packages which
use the "time" feature of the "%{crate}" crate.

%files       -n %{name}+time-devel
%ghost %{crate_instdir}/Cargo.toml

%prep
%autosetup -n %{crate}-%{version} -p1
%cargo_prep
cp -pav %{SOURCE1} %{SOURCE2} .

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
