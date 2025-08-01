# Generated by rust2rpm 27
%bcond check 1
%global debug_package %{nil}

%global crate tree-sitter-config

Name:           rust-tree-sitter-config
Version:        0.25.8
Release:        %autorelease
Summary:        User configuration of tree-sitter's command line programs

License:        MIT
URL:            https://crates.io/crates/tree-sitter-config
Source:         %{crates_source}
# * Upstream license file - tree-sitter/tree-sitter#1520
Source2:        https://github.com/tree-sitter/tree-sitter/raw/v%{version}/LICENSE#/LICENSE.upstream
# Manually created patch for downstream crate metadata changes
# * Update etcetera to 0.10:
#   https://github.com/tree-sitter/tree-sitter/pull/4392
Patch:          tree-sitter-config-fix-metadata.diff

BuildRequires:  cargo-rpm-macros >= 24

%global _description %{expand:
User configuration of tree-sitter's command line programs.}

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

%prep
%autosetup -n %{crate}-%{version} -p1
%cargo_prep
cp -pav %{SOURCE2} LICENSE

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
