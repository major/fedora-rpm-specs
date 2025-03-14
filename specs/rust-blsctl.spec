# Generated by rust2rpm 24
%bcond_without check

%global crate blsctl

Name:           rust-blsctl
Version:        0.2.3
Release:        %autorelease
Summary:        Manages BLS entries and kernel cmdline options

License:        LGPL-2.1-or-later
URL:            https://crates.io/crates/blsctl
Source:         %{crates_source}
# Manually created patch for downstream crate metadata changes
# * drop unused "cdylib" build target
Patch:          blsctl-fix-metadata.diff

BuildRequires:  rust-packaging >= 23

%global _description %{expand:
Manages BLS entries and kernel cmdline options.}

%description %{_description}

%package     -n %{crate}
Summary:        %{summary}
License:        LGPL-2.1-or-later
# LICENSE.dependencies contains a full license breakdown

%description -n %{crate} %{_description}

%files       -n %{crate}
%license LICENSE.gpl3
%license LICENSE.lgpl2
%license LICENSE.dependencies
%{_bindir}/blsctl

%package        devel
Summary:        %{summary}
BuildArch:      noarch
Requires:       rpm-devel

%description    devel %{_description}

This package contains library source intended for building other packages which
use the "%{crate}" crate.

%files          devel
%license %{crate_instdir}/LICENSE.gpl3
%license %{crate_instdir}/LICENSE.lgpl2
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
%autosetup -n %{crate}-%{version_no_tilde} -p1
%cargo_prep

%generate_buildrequires
%cargo_generate_buildrequires
echo 'rpm-devel'

%build
%cargo_build
%cargo_license_summary
%{cargo_license} > LICENSE.dependencies

%install
%cargo_install

%if %{with check}
%check
%cargo_test
%endif

%changelog
%autochangelog
