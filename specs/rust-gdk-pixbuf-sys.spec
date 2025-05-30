# Generated by rust2rpm 27
# * tests are broken: https://github.com/gtk-rs/gtk-rs-core/issues/64
%bcond check 0
%global debug_package %{nil}

%global crate gdk-pixbuf-sys

Name:           rust-gdk-pixbuf-sys
Version:        0.20.10
Release:        %autorelease
Summary:        FFI bindings to libgdk_pixbuf-2.0

License:        MIT
URL:            https://crates.io/crates/gdk-pixbuf-sys
Source:         %{crates_source}

BuildRequires:  cargo-rpm-macros >= 24
BuildRequires:  pkgconfig(gdk-pixbuf-2.0) >= 2.36.8

%global _description %{expand:
FFI bindings to libgdk_pixbuf-2.0.}

%description %{_description}

%package        devel
Summary:        %{summary}
BuildArch:      noarch
Requires:       pkgconfig(gdk-pixbuf-2.0) >= 2.36.8

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

%package     -n %{name}+v2_40-devel
Summary:        %{summary}
BuildArch:      noarch
Requires:       pkgconfig(gdk-pixbuf-2.0) >= 2.40

%description -n %{name}+v2_40-devel %{_description}

This package contains library source intended for building other packages which
use the "v2_40" feature of the "%{crate}" crate.

%files       -n %{name}+v2_40-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+v2_42-devel
Summary:        %{summary}
BuildArch:      noarch
Requires:       pkgconfig(gdk-pixbuf-2.0) >= 2.42

%description -n %{name}+v2_42-devel %{_description}

This package contains library source intended for building other packages which
use the "v2_42" feature of the "%{crate}" crate.

%files       -n %{name}+v2_42-devel
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
