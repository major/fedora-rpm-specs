# Generated by rust2rpm 26
%bcond_without check
%global debug_package %{nil}

%global crate coolor

Name:           rust-coolor
Version:        1.0.0
Release:        %autorelease
Summary:        Conversion between color formats

License:        MIT
URL:            https://crates.io/crates/coolor
Source:         %{crates_source}

BuildRequires:  cargo-rpm-macros >= 24

%global _description %{expand:
Conversion between color formats.}

%description %{_description}

%package        devel
Summary:        %{summary}
BuildArch:      noarch

%description    devel %{_description}

This package contains library source intended for building other packages which
use the "%{crate}" crate.

%files          devel
%license %{crate_instdir}/LICENSE
%doc %{crate_instdir}/README.md
%doc %{crate_instdir}/features.md
%{crate_instdir}/

%package     -n %{name}+default-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+default-devel %{_description}

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%files       -n %{name}+default-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+crossterm-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+crossterm-devel %{_description}

This package contains library source intended for building other packages which
use the "crossterm" feature of the "%{crate}" crate.

%files       -n %{name}+crossterm-devel
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
