# Generated by rust2rpm 24
%bcond_without check
%global debug_package %{nil}

%global crate userfaultfd-sys

Name:           rust-userfaultfd-sys
Version:        0.5.0
Release:        %autorelease
Summary:        Low-level bindings for userfaultfd functionality on Linux

License:        MIT OR Apache-2.0
URL:            https://crates.io/crates/userfaultfd-sys
Source:         %{crates_source}

BuildRequires:  rust-packaging >= 21

%global _description %{expand:
Low-level bindings for userfaultfd functionality on Linux.}

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
%{crate_instdir}/

%package     -n %{name}+default-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+default-devel %{_description}

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%files       -n %{name}+default-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+linux4_14-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+linux4_14-devel %{_description}

This package contains library source intended for building other packages which
use the "linux4_14" feature of the "%{crate}" crate.

%files       -n %{name}+linux4_14-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+linux5_7-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+linux5_7-devel %{_description}

This package contains library source intended for building other packages which
use the "linux5_7" feature of the "%{crate}" crate.

%files       -n %{name}+linux5_7-devel
%ghost %{crate_instdir}/Cargo.toml

%prep
%autosetup -n %{crate}-%{version_no_tilde} -p1
%cargo_prep

%generate_buildrequires
%cargo_generate_buildrequires

%build
%cargo_build

%install
%cargo_install

%if %{with check}
%check
%cargo_test -- -- --exact --skip=linux4_11::const_tests::consts_correct
%endif

%changelog
%autochangelog
