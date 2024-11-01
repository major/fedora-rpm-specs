# Generated by rust2rpm 26
%bcond_without check
%global debug_package %{nil}

%global crate keyframe_derive

Name:           rust-keyframe_derive
Version:        1.0.0
Release:        %autorelease
Summary:        Implements #[derive(CanTween)] for keyframe

License:        MIT
URL:            https://crates.io/crates/keyframe_derive
Source0:        %{crates_source}

# No longer needed after https://github.com/hannesmann/keyframe/pull/19
Source1:        https://raw.githubusercontent.com/hannesmann/keyframe/master/LICENSE

BuildRequires:  cargo-rpm-macros >= 24

%global _description %{expand:
Implements #[derive(CanTween)] for keyframe.}

%description %{_description}

%package        devel
Summary:        %{summary}
BuildArch:      noarch

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

%prep
%autosetup -n %{crate}-%{version} -p1
%cargo_prep

%generate_buildrequires
%cargo_generate_buildrequires

%build
%cargo_build

%install
%cargo_install

# Manually copy the license file from upstream
install -Dpm644 %{SOURCE1} %{buildroot}%{crate_instdir}/LICENSE

%if %{with check}
%check
%cargo_test
%endif

%changelog
%autochangelog
