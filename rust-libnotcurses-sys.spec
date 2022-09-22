%bcond_without check
%global debug_package %{nil}

%global crate libnotcurses-sys

Name:           rust-%{crate}
Version:        3.0.5
Release:        %autorelease
Summary:        Low-level Rust bindings for the notcurses C library

# Upstream license specification: Apache-2.0
License:        ASL 2.0
URL:            https://crates.io/crates/libnotcurses-sys
Source:         %{crates_source}

ExclusiveArch:  %{rust_arches}
%if %{__cargo_skip_build}
BuildArch:      noarch
%endif

BuildRequires:  rust-packaging
BuildRequires:  pkgconfig(notcurses)
BuildRequires:  (crate(cty/default) == 0.2.1)
BuildRequires:  (crate(bindgen/default) >= 0.59.0)
BuildRequires:  (crate(pkg-config/default) >= 0.3.18)
BuildRequires:  (crate(serial_test/default) >= 0.5.0)
BuildRequires:  (crate(serial_test_derive/default) >= 0.5.0)

%global _description %{expand:
Low-level Rust bindings for the notcurses C library.}

%description %{_description}

%package        devel
Summary:        %{summary}
BuildArch:      noarch

%description    devel %{_description}

This package contains library source intended for building other packages
which use "%{crate}" crate.

%files          devel
%license LICENSE-APACHE LICENSE-MIT
%doc README.md
%{cargo_registry}/%{crate}-%{version_no_tilde}/

%package     -n %{name}+default-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+default-devel %{_description}

This package contains library source intended for building other packages
which use "default" feature of "%{crate}" crate.

%files       -n %{name}+default-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%prep
%autosetup -n %{crate}-%{version_no_tilde} -p1
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
