# Generated by rust2rpm 27
%bcond check 1
%global debug_package %{nil}

%global crate getrandom

Name:           rust-getrandom0.2
Version:        0.2.16
Release:        %autorelease
Summary:        Small cross-platform library for retrieving random data from system source

License:        MIT OR Apache-2.0
URL:            https://crates.io/crates/getrandom
Source:         %{crates_source}
# Automatically generated patch to strip dependencies and normalize metadata
Patch:          getrandom-fix-metadata-auto.diff
# Manually created patch for downstream crate metadata changes
# * drop dependencies on compiler internals
Patch:          getrandom-fix-metadata.diff

BuildRequires:  cargo-rpm-macros >= 24

%global _description %{expand:
A small cross-platform library for retrieving random data from system
source.}

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
%doc %{crate_instdir}/CHANGELOG.md
%doc %{crate_instdir}/README.md
%doc %{crate_instdir}/SECURITY.md
%{crate_instdir}/

%package     -n %{name}+default-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+default-devel %{_description}

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%files       -n %{name}+default-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+custom-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+custom-devel %{_description}

This package contains library source intended for building other packages which
use the "custom" feature of the "%{crate}" crate.

%files       -n %{name}+custom-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+linux_disable_fallback-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+linux_disable_fallback-devel %{_description}

This package contains library source intended for building other packages which
use the "linux_disable_fallback" feature of the "%{crate}" crate.

%files       -n %{name}+linux_disable_fallback-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+rdrand-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+rdrand-devel %{_description}

This package contains library source intended for building other packages which
use the "rdrand" feature of the "%{crate}" crate.

%files       -n %{name}+rdrand-devel
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
