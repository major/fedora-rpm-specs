# Generated by rust2rpm 24
%bcond_without check
%global debug_package %{nil}

%global crate daemonize

Name:           rust-daemonize
Version:        0.5.0
Release:        %autorelease
Summary:        Library to enable your code run as a daemon process on Unix-like systems

# Upstream license specification: MIT/Apache-2.0
License:        MIT OR Apache-2.0
URL:            https://crates.io/crates/daemonize
Source0:        %{crates_source}
# https://github.com/knsd/daemonize/pull/52
Source1:        https://github.com/knsd/daemonize/raw/%{version}/LICENSE-APACHE
Source2:        https://github.com/knsd/daemonize/raw/%{version}/LICENSE-MIT

BuildRequires:  rust-packaging >= 21

%global _description %{expand:
Library to enable your code run as a daemon process on Unix-like
systems.}

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
cp -pav %{SOURCE1} %{SOURCE2} .

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