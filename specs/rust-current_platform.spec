# Generated by rust2rpm 26
%bcond_without check
%global debug_package %{nil}

%global crate current_platform

Name:           rust-current_platform
Version:        0.2.0
Release:        %autorelease
Summary:        Find out what platform your code is running on

License:        MIT OR Apache-2.0 OR Zlib
URL:            https://crates.io/crates/current_platform
Source:         %{crates_source}

BuildRequires:  cargo-rpm-macros >= 24

%global _description %{expand:
Find out what platform your code is running on.}

%description %{_description}

%package        devel
Summary:        %{summary}
BuildArch:      noarch

%description    devel %{_description}

This package contains library source intended for building other packages which
use the "%{crate}" crate.

%files          devel
%license %{crate_instdir}/LICENSE-APACHE.md
%license %{crate_instdir}/LICENSE-MIT.md
%license %{crate_instdir}/LICENSE-ZLIB.md
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