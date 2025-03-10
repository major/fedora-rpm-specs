# Generated by rust2rpm 26
%bcond_without check
%global debug_package %{nil}

%global crate gweather-sys

Name:           rust-gweather-sys
Version:        4.5.0
Release:        %autorelease
Summary:        FFI bindings for libgweather

License:        MIT
URL:            https://crates.io/crates/gweather-sys
Source:         %{crates_source}

BuildRequires:  cargo-rpm-macros >= 24
BuildRequires:  pkgconfig(gweather4) >= 4

%global _description %{expand:
FFI bindings for libgweather.}

%description %{_description}

%package        devel
Summary:        %{summary}
BuildArch:      noarch
Requires:       pkgconfig(gweather4) >= 4

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

%if %{with check}
%check
%cargo_test
%endif

%changelog
%autochangelog
