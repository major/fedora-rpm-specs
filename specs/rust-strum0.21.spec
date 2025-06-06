# Generated by rust2rpm 26
%bcond_without check
%global debug_package %{nil}

%global crate strum

Name:           rust-strum0.21
Version:        0.21.0
Release:        %autorelease
Summary:        Helpful macros for working with enums and strings

License:        MIT
URL:            https://crates.io/crates/strum
Source:         %{crates_source}
# Manually created patch for downstream crate metadata changes
# * remove reference to readme file that is not included in published crates
Patch:          strum-fix-metadata.diff

BuildRequires:  cargo-rpm-macros >= 24

%global _description %{expand:
Helpful macros for working with enums and strings.}

%description %{_description}

%package        devel
Summary:        %{summary}
BuildArch:      noarch

%description    devel %{_description}

This package contains library source intended for building other packages which
use the "%{crate}" crate.

%files          devel
%license %{crate_instdir}/LICENSE
%{crate_instdir}/

%package     -n %{name}+default-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+default-devel %{_description}

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%files       -n %{name}+default-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+derive-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+derive-devel %{_description}

This package contains library source intended for building other packages which
use the "derive" feature of the "%{crate}" crate.

%files       -n %{name}+derive-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+strum_macros-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+strum_macros-devel %{_description}

This package contains library source intended for building other packages which
use the "strum_macros" feature of the "%{crate}" crate.

%files       -n %{name}+strum_macros-devel
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
%cargo_test -f derive
%endif

%changelog
%autochangelog
