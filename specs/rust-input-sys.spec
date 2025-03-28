# Generated by rust2rpm 24
%bcond_without check
%global debug_package %{nil}

%global crate input-sys

Name:           rust-input-sys
Version:        1.17.0
Release:        %autorelease
Summary:        Bindgen generated unsafe libinput wrapper

License:        MIT
URL:            https://crates.io/crates/input-sys
Source:         %{crates_source}
# https://github.com/Smithay/input.rs/pull/56
Source:         https://github.com/Smithay/input.rs/raw/v0.8.3/LICENSE
# Manually created patch for downstream crate metadata changes
# * bump bindgen to 0.63: https://github.com/Smithay/input.rs/pull/57
# * default to gen feature
Patch:          input-sys-fix-metadata.diff

BuildRequires:  rust-packaging >= 21
BuildRequires:  sed

%global _description %{expand:
Bindgen generated unsafe libinput wrapper.}

%description %{_description}

%package        devel
Summary:        %{summary}
BuildArch:      noarch
Requires:       pkgconfig(libinput)
Requires:       pkgconfig(libudev)

%description    devel %{_description}

This package contains library source intended for building other packages which
use the "%{crate}" crate.

%files          devel
%license %{crate_instdir}/LICENSE
%{crate_instdir}/

%package     -n %{name}+default-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+default-devel %{_description}

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%files       -n %{name}+default-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+bindgen-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+bindgen-devel %{_description}

This package contains library source intended for building other packages which
use the "bindgen" feature of the "%{crate}" crate.

%files       -n %{name}+bindgen-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+gen-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+gen-devel %{_description}

This package contains library source intended for building other packages which
use the "gen" feature of the "%{crate}" crate.

%files       -n %{name}+gen-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+update_bindings-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+update_bindings-devel %{_description}

This package contains library source intended for building other packages which
use the "update_bindings" feature of the "%{crate}" crate.

%files       -n %{name}+update_bindings-devel
%ghost %{crate_instdir}/Cargo.toml

%prep
%autosetup -n %{crate}-%{version_no_tilde} -p1
cp -p %SOURCE1 .
sed -i 's/whitelist/allowlist/g' build.rs
%cargo_prep

%generate_buildrequires
%cargo_generate_buildrequires
echo 'pkgconfig(libinput)'
echo 'pkgconfig(libudev)'

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
