# Generated by rust2rpm 27
%bcond check 1
%global debug_package %{nil}

%global crate libcryptsetup-rs-sys

Name:           rust-libcryptsetup-rs-sys
Version:        0.6.0
Release:        %autorelease
Summary:        Low level bindings for libcryptsetup

License:        MPL-2.0
URL:            https://crates.io/crates/libcryptsetup-rs-sys
Source:         %{crates_source}

BuildRequires:  cargo-rpm-macros >= 24
BuildRequires:  pkgconfig(libcryptsetup)

%global _description %{expand:
Low level bindings for libcryptsetup.}

%description %{_description}

%package        devel
Summary:        %{summary}
BuildArch:      noarch
Requires:       pkgconfig(libcryptsetup)

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

%package     -n %{name}+static-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+static-devel %{_description}

This package contains library source intended for building other packages which
use the "static" feature of the "%{crate}" crate.

%files       -n %{name}+static-devel
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
