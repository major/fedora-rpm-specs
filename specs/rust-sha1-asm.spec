# Generated by rust2rpm 26
%bcond_without check
%global debug_package %{nil}

%global crate sha1-asm

# compile and run tests only on supported architectures
%global supported_arches x86_64 %{ix86} aarch64

Name:           rust-sha1-asm
Version:        0.5.3
Release:        %autorelease
Summary:        Assembly implementation of SHA-1 compression function

License:        MIT
URL:            https://crates.io/crates/sha1-asm
Source:         %{crates_source}

BuildRequires:  cargo-rpm-macros >= 24

%global _description %{expand:
Assembly implementation of SHA-1 compression function.}

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
%{crate_instdir}/

%package     -n %{name}+default-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+default-devel %{_description}

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%files       -n %{name}+default-devel
%ghost %{crate_instdir}/Cargo.toml

%prep
%autosetup -n %{crate}-%{version} -p1
%cargo_prep

%generate_buildrequires
%cargo_generate_buildrequires

%build
%ifarch %{supported_arches}
%cargo_build
%endif

%install
%cargo_install

%if %{with check}
%ifarch %{supported_arches}
%check
%cargo_test
%endif
%endif

%changelog
%autochangelog