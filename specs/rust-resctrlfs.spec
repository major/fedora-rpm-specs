# Generated by rust2rpm 27
%bcond check 1
%global debug_package %{nil}

%global crate resctrlfs

# compile and run tests only on supported architectures
%global unsupported_arches %{ix86}

Name:           rust-resctrlfs
Version:        0.9.0
Release:        %autorelease
Summary:        A crate for reading resctrl fs data

License:        Apache-2.0
URL:            https://crates.io/crates/resctrlfs
Source:         %{crates_source}

BuildRequires:  cargo-rpm-macros >= 24

%global _description %{expand:
A crate for reading resctrl fs data.}

%description %{_description}

%package        devel
Summary:        %{summary}
BuildArch:      noarch

%description    devel %{_description}

This package contains library source intended for building other packages which
use the "%{crate}" crate.

%files          devel
%license %{crate_instdir}/LICENSE
%doc %{crate_instdir}/README
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
%ifnarch %{unsupported_arches}
%cargo_build
%endif

%install
%cargo_install

%if %{with check}
%ifnarch %{unsupported_arches}
%check
%cargo_test
%endif
%endif

%changelog
%autochangelog
