# Generated by rust2rpm 23
# * tests need internet access
%bcond_with check
%global debug_package %{nil}

%global crate tokio-native-tls

Name:           rust-tokio-native-tls
Version:        0.3.1
Release:        %autorelease
Summary:        Implementation of TLS/SSL streams for Tokio using native-tls

License:        MIT
URL:            https://crates.io/crates/tokio-native-tls
Source:         %{crates_source}
# Automatically generated patch to strip foreign dependencies
Patch:          tokio-native-tls-fix-metadata-auto.diff
# Manually created patch for downstream crate metadata changes
# * drop feature for using vendored dependencies
Patch:          tokio-native-tls-fix-metadata.diff

BuildRequires:  rust-packaging >= 21

%global _description %{expand:
Implementation of TLS/SSL streams for Tokio using native-tls giving an
implementation of TLS for nonblocking I/O streams.}

%description %{_description}

%package        devel
Summary:        %{summary}
BuildArch:      noarch

%description    devel %{_description}

This package contains library source intended for building other packages which
use the "%{crate}" crate.

%files          devel
%license %{crate_instdir}/LICENSE
%doc %{crate_instdir}/CHANGELOG.md
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