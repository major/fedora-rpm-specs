# Generated by rust2rpm 26
%bcond_without check
%global debug_package %{nil}

%global crate below-btrfs

Name:           rust-below-btrfs
Version:        0.8.1
Release:        %autorelease
Summary:        A crate for reading btrfs

License:        Apache-2.0
URL:            https://crates.io/crates/below-btrfs
Source:         %{crates_source}
# Manually created patch for downstream crate metadata changes
# * bump nix from 0.25 to 0.26
Patch:          below-btrfs-fix-metadata.diff

# bindgen code does not work on 32-bit architectures;
# multiple btrfs_api::open_source::btrfs_sys::bindgen_test_layout_btrfs_ioctl_* test failures
ExcludeArch:    %{arm32} %{ix86}

BuildRequires:  cargo-rpm-macros >= 24

%global _description %{expand:
A crate for reading btrfs.}

%description %{_description}

%package        devel
Summary:        %{summary}
BuildArch:      noarch

%description    devel %{_description}

This package contains library source intended for building other packages which
use the "%{crate}" crate.

%files          devel
%license %{crate_instdir}/LICENSE
%doc %{crate_instdir}/README
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
%cargo_build

%install
%cargo_install

%if %{with check}
%check
# sudotest tests fail on koji
%cargo_test -- -- --skip btrfs_api::sudotest::
%endif

%changelog
%autochangelog