# Generated by rust2rpm 26
%bcond_without check
%global debug_package %{nil}

%global crate fat-macho

Name:           rust-fat-macho
Version:        0.4.9
Release:        %autorelease
Summary:        Mach-O Fat Binary Reader and Writer

License:        MIT
URL:            https://crates.io/crates/fat-macho
Source:         %{crates_source}
# Manually created patch for downstream crate metadata changes
# * exclude tests and binary test fixtures from installed files
Patch:          fat-macho-fix-metadata.diff

BuildRequires:  cargo-rpm-macros >= 24

%global _description %{expand:
Mach-O Fat Binary Reader and Writer.}

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

%package     -n %{name}+bitcode-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+bitcode-devel %{_description}

This package contains library source intended for building other packages which
use the "bitcode" feature of the "%{crate}" crate.

%files       -n %{name}+bitcode-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+llvm-bitcode-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+llvm-bitcode-devel %{_description}

This package contains library source intended for building other packages which
use the "llvm-bitcode" feature of the "%{crate}" crate.

%files       -n %{name}+llvm-bitcode-devel
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
