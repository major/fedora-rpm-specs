# Generated by rust2rpm 26
# * bindgen tests fail on 32-bit architectures:
#   https://github.com/rbspy/rbspy/issues/341
%ifarch %{ix86}
%bcond_with check
%else
%bcond_without check
%endif
%global debug_package %{nil}

%global crate rbspy-ruby-structs

Name:           rust-rbspy-ruby-structs
Version:        0.24.0
Release:        %autorelease
Summary:        Helper crate for rbspy

License:        MIT
URL:            https://crates.io/crates/rbspy-ruby-structs
Source:         %{crates_source}

BuildRequires:  cargo-rpm-macros >= 24

%global _description %{expand:
Helper crate for rbspy. Contains Rust bindings for various internal Ruby
structures for version 1.9.3 to 3.x.}

%description %{_description}

%package        devel
Summary:        %{summary}
BuildArch:      noarch

%description    devel %{_description}

This package contains library source intended for building other packages which
use the "%{crate}" crate.

%files          devel
%license %{crate_instdir}/License.md
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