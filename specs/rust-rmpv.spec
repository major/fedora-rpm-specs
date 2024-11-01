# Generated by rust2rpm 26
%bcond_without check
%global debug_package %{nil}

%global crate rmpv

Name:           rust-rmpv
Version:        1.3.0
Release:        %autorelease
Summary:        Value variant for RMP

License:        MIT
URL:            https://crates.io/crates/rmpv
Source:         %{crates_source}

BuildRequires:  cargo-rpm-macros >= 24

%global _description %{expand:
Value variant for RMP.}

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

%package     -n %{name}+serde-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+serde-devel %{_description}

This package contains library source intended for building other packages which
use the "serde" feature of the "%{crate}" crate.

%files       -n %{name}+serde-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+serde_bytes-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+serde_bytes-devel %{_description}

This package contains library source intended for building other packages which
use the "serde_bytes" feature of the "%{crate}" crate.

%files       -n %{name}+serde_bytes-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+with-serde-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+with-serde-devel %{_description}

This package contains library source intended for building other packages which
use the "with-serde" feature of the "%{crate}" crate.

%files       -n %{name}+with-serde-devel
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
