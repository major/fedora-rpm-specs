# Generated by rust2rpm 27
%bcond check 1
%global debug_package %{nil}

%global crate gettext-rs

Name:           rust-gettext-rs
Version:        0.7.2
Release:        %autorelease
Summary:        Safe bindings for gettext

License:        MIT
URL:            https://crates.io/crates/gettext-rs
Source:         %{crates_source}

BuildRequires:  cargo-rpm-macros >= 24

%global _description %{expand:
Safe bindings for gettext.}

%description %{_description}

%package        devel
Summary:        %{summary}
BuildArch:      noarch

%description    devel %{_description}

This package contains library source intended for building other packages which
use the "%{crate}" crate.

%files          devel
%license %{crate_instdir}/LICENSE.txt
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

%package     -n %{name}+gettext-system-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+gettext-system-devel %{_description}

This package contains library source intended for building other packages which
use the "gettext-system" feature of the "%{crate}" crate.

%files       -n %{name}+gettext-system-devel
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
