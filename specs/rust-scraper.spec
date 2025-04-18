# Generated by rust2rpm 27
%bcond check 1
%global debug_package %{nil}

# prevent executables from being installed
%global cargo_install_bin 0

%global crate scraper

Name:           rust-scraper
Version:        0.19.1
Release:        %autorelease
Summary:        HTML parsing and querying with CSS selectors

License:        ISC
URL:            https://crates.io/crates/scraper
Source:         %{crates_source}
# Manually created patch for downstream crate metadata changes
# * Bump ego-tree dependency from 0.6.2 to 0.9.0
# * Relax html5ever dependency from 0.27 to 0.26
Patch:          scraper-fix-metadata.diff

BuildRequires:  cargo-rpm-macros >= 26

%global _description %{expand:
HTML parsing and querying with CSS selectors.}

%description %{_description}

%package        devel
Summary:        %{summary}
BuildArch:      noarch

%description    devel %{_description}

This package contains library source intended for building other packages which
use the "%{crate}" crate.

%files          devel
%license %{crate_instdir}/LICENSE
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

%package     -n %{name}+atomic-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+atomic-devel %{_description}

This package contains library source intended for building other packages which
use the "atomic" feature of the "%{crate}" crate.

%files       -n %{name}+atomic-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+deterministic-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+deterministic-devel %{_description}

This package contains library source intended for building other packages which
use the "deterministic" feature of the "%{crate}" crate.

%files       -n %{name}+deterministic-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+errors-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+errors-devel %{_description}

This package contains library source intended for building other packages which
use the "errors" feature of the "%{crate}" crate.

%files       -n %{name}+errors-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+getopts-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+getopts-devel %{_description}

This package contains library source intended for building other packages which
use the "getopts" feature of the "%{crate}" crate.

%files       -n %{name}+getopts-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+indexmap-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+indexmap-devel %{_description}

This package contains library source intended for building other packages which
use the "indexmap" feature of the "%{crate}" crate.

%files       -n %{name}+indexmap-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+main-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+main-devel %{_description}

This package contains library source intended for building other packages which
use the "main" feature of the "%{crate}" crate.

%files       -n %{name}+main-devel
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
