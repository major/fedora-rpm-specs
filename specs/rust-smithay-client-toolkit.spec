# Generated by rust2rpm 27
%bcond check 1
%global debug_package %{nil}

%global crate smithay-client-toolkit

Name:           rust-smithay-client-toolkit
Version:        0.19.2
Release:        %autorelease
Summary:        Toolkit for making client wayland applications

License:        MIT
URL:            https://crates.io/crates/smithay-client-toolkit
Source:         %{crates_source}
# Manually created patch for downstream crate metadata changes
# * Drop examples with unpackaged dependencies
# * Drop leftover dependencies of the removed examples
# * Allow xkbcommon 0.8 (https://github.com/Smithay/client-toolkit/pull/484)
Patch:          smithay-client-toolkit-fix-metadata.diff

BuildRequires:  cargo-rpm-macros >= 24

%global _description %{expand:
Toolkit for making client wayland applications.}

%description %{_description}

%package        devel
Summary:        %{summary}
BuildArch:      noarch
Requires:       libxkbcommon-devel

%description    devel %{_description}

This package contains library source intended for building other packages which
use the "%{crate}" crate.

%files          devel
%license %{crate_instdir}/LICENSE.txt
%doc %{crate_instdir}/CHANGELOG.md
%doc %{crate_instdir}/CONTRIBUTING.md
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

%package     -n %{name}+bytemuck-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+bytemuck-devel %{_description}

This package contains library source intended for building other packages which
use the "bytemuck" feature of the "%{crate}" crate.

%files       -n %{name}+bytemuck-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+calloop-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+calloop-devel %{_description}

This package contains library source intended for building other packages which
use the "calloop" feature of the "%{crate}" crate.

%files       -n %{name}+calloop-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+calloop-wayland-source-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+calloop-wayland-source-devel %{_description}

This package contains library source intended for building other packages which
use the "calloop-wayland-source" feature of the "%{crate}" crate.

%files       -n %{name}+calloop-wayland-source-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+pkg-config-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+pkg-config-devel %{_description}

This package contains library source intended for building other packages which
use the "pkg-config" feature of the "%{crate}" crate.

%files       -n %{name}+pkg-config-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+xkbcommon-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+xkbcommon-devel %{_description}

This package contains library source intended for building other packages which
use the "xkbcommon" feature of the "%{crate}" crate.

%files       -n %{name}+xkbcommon-devel
%ghost %{crate_instdir}/Cargo.toml

%prep
%autosetup -n %{crate}-%{version} -p1
%cargo_prep
# Drop examples with unpackaged dependencies
rm -f examples/{relative_pointer.rs,wgpu.rs}

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
