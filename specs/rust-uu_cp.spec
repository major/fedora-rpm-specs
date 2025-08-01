# Generated by rust2rpm 27
%bcond check 1
%global debug_package %{nil}

# prevent executables from being installed
%global cargo_install_bin 0

%global crate uu_cp

Name:           rust-uu_cp
Version:        0.0.27
Release:        %autorelease
Summary:        cp ~ (uutils) copy SOURCE to DESTINATION

License:        MIT
URL:            https://crates.io/crates/uu_cp
Source:         %{crates_source}
# Manually created patch for downstream crate metadata changes
# * Allow indicatif 0.18: https://github.com/uutils/coreutils/pull/8313
Patch:          uu_cp-fix-metadata.diff

BuildRequires:  cargo-rpm-macros >= 26

%global _description %{expand:
cp ~ (uutils) copy SOURCE to DESTINATION.}

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
%doc %{crate_instdir}/cp.md
%{crate_instdir}/

%package     -n %{name}+default-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+default-devel %{_description}

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%files       -n %{name}+default-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+exacl-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+exacl-devel %{_description}

This package contains library source intended for building other packages which
use the "exacl" feature of the "%{crate}" crate.

%files       -n %{name}+exacl-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+feat_acl-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+feat_acl-devel %{_description}

This package contains library source intended for building other packages which
use the "feat_acl" feature of the "%{crate}" crate.

%files       -n %{name}+feat_acl-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+feat_selinux-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+feat_selinux-devel %{_description}

This package contains library source intended for building other packages which
use the "feat_selinux" feature of the "%{crate}" crate.

%files       -n %{name}+feat_selinux-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+selinux-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+selinux-devel %{_description}

This package contains library source intended for building other packages which
use the "selinux" feature of the "%{crate}" crate.

%files       -n %{name}+selinux-devel
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
