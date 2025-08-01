# Generated by rust2rpm 27
%bcond check 1
%global debug_package %{nil}

%global crate prettyplease

Name:           rust-prettyplease
Version:        0.2.36
Release:        %autorelease
Summary:        Minimal syn syntax tree pretty-printer

License:        MIT OR Apache-2.0
URL:            https://crates.io/crates/prettyplease
Source:         %{crates_source}

BuildRequires:  cargo-rpm-macros >= 24

%global _description %{expand:
A minimal `syn` syntax tree pretty-printer.}

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

%package     -n %{name}+verbatim-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+verbatim-devel %{_description}

This package contains library source intended for building other packages which
use the "verbatim" feature of the "%{crate}" crate.

%files       -n %{name}+verbatim-devel
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
