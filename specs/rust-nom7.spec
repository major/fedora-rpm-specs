# Generated by rust2rpm 27
%bcond check 1
%global debug_package %{nil}

%global crate nom

Name:           rust-nom7
Version:        7.1.3
Release:        %autorelease
Summary:        Byte-oriented, zero-copy, parser combinators library

License:        MIT
URL:            https://crates.io/crates/nom
Source:         %{crates_source}
# Manually created patch for downstream crate metadata changes
# * drop references to example code that is not shipped with the crate
Patch:          nom-fix-metadata.diff

BuildRequires:  cargo-rpm-macros >= 24

%global _description %{expand:
A byte-oriented, zero-copy, parser combinators library.}

%description %{_description}

%package        devel
Summary:        %{summary}
BuildArch:      noarch

%description    devel %{_description}

This package contains library source intended for building other packages which
use the "%{crate}" crate.

%files          devel
%license %{crate_instdir}/LICENSE
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

%package     -n %{name}+alloc-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+alloc-devel %{_description}

This package contains library source intended for building other packages which
use the "alloc" feature of the "%{crate}" crate.

%files       -n %{name}+alloc-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+docsrs-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+docsrs-devel %{_description}

This package contains library source intended for building other packages which
use the "docsrs" feature of the "%{crate}" crate.

%files       -n %{name}+docsrs-devel
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
%ifarch %{ix86} %{arm}
# * skip a test with wrong overflow behaviour on 32-bit architectures:
#   https://github.com/rust-bakery/nom/issues/1278
%cargo_test -- -- --skip issue_848_overflow_incomplete_bits_to_bytes
%else
%cargo_test
%endif
%endif

%changelog
%autochangelog
