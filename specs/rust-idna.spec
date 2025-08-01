# Generated by rust2rpm 27
%bcond check 1
%global debug_package %{nil}

%global crate idna

Name:           rust-idna
Version:        1.0.3
Release:        %autorelease
Summary:        IDNA (Internationalizing Domain Names in Applications) and Punycode

License:        MIT OR Apache-2.0
URL:            https://crates.io/crates/idna
Source:         %{crates_source}
# Manually created patch for downstream crate metadata changes
# * drop unused, benchmark-only bencher dev-dependency
# * exclude tests/IdnaTestV2.txt to avoid needing a Unicode-3.0 term in the
#   licenses of the binary RPMs
Patch:          idna-fix-metadata.diff
# * Cherry-pick “Update tests to Unicode 16.0,”
#   https://github.com/servo/rust-url/commit/68f151c01682d620605b749b61684084150a6c41,
#   to idna-v1.0.3; see also https://github.com/servo/rust-url/pull/1045. Omit
#   changes to the upstream CI configuration, which is outside of the part of
#   the source tree corresponding to the released idna crates anyway. Fixes test
#   compatibiility with idna_adapter 1.2.1 / ICU4X 2.0.
Patch10:        0001-Update-tests-to-Unicode-16.0-1045.patch

BuildRequires:  cargo-rpm-macros >= 24

%global _description %{expand:
IDNA (Internationalizing Domain Names in Applications) and Punycode.}

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

%package     -n %{name}+alloc-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+alloc-devel %{_description}

This package contains library source intended for building other packages which
use the "alloc" feature of the "%{crate}" crate.

%files       -n %{name}+alloc-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+compiled_data-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+compiled_data-devel %{_description}

This package contains library source intended for building other packages which
use the "compiled_data" feature of the "%{crate}" crate.

%files       -n %{name}+compiled_data-devel
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
