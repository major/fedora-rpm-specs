# Generated by rust2rpm 24
# * missing dev-dependencies: http-types ^2, tide ^0.16
%bcond_with check
%global debug_package %{nil}

%global crate prometheus-client

Name:           rust-prometheus-client
Version:        0.19.0
Release:        %autorelease
Summary:        Open Metrics client library allowing users to natively instrument applications

License:        Apache-2.0 OR MIT
URL:            https://crates.io/crates/prometheus-client
Source:         %{crates_source}
# Manually created patch for downstream crate metadata changes
# * drop unused feature for protobuf support and its dependencies
Patch:          prometheus-client-fix-metadata.diff

BuildRequires:  rust-packaging >= 21

%global _description %{expand:
Open Metrics client library allowing users to natively instrument
applications.}

%description %{_description}

%package        devel
Summary:        %{summary}
BuildArch:      noarch

%description    devel %{_description}

This package contains library source intended for building other packages which
use the "%{crate}" crate.

%files          devel
%license %{crate_instdir}/LICENSE-APACHE
%license %{crate_instdir}/LICENSE-MIT
%doc %{crate_instdir}/CHANGELOG.md
%doc %{crate_instdir}/CODE_OF_CONDUCT.md
%doc %{crate_instdir}/MAINTAINERS.md
%doc %{crate_instdir}/README.md
%doc %{crate_instdir}/SECURITY.md
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