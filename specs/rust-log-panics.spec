# Generated by rust2rpm 24
%bcond_without check
%global debug_package %{nil}

%global crate log-panics

Name:           rust-log-panics
Version:        2.1.0
Release:        %autorelease
Summary:        Panic hook which logs panic messages rather than printing them

# Upstream license specification: MIT/Apache-2.0
License:        MIT OR Apache-2.0
URL:            https://crates.io/crates/log-panics
Source:         %{crates_source}

BuildRequires:  rust-packaging >= 21

%global _description %{expand:
A panic hook which logs panic messages rather than printing them.}

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

%package     -n %{name}+backtrace-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+backtrace-devel %{_description}

This package contains library source intended for building other packages which
use the "backtrace" feature of the "%{crate}" crate.

%files       -n %{name}+backtrace-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+with-backtrace-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+with-backtrace-devel %{_description}

This package contains library source intended for building other packages which
use the "with-backtrace" feature of the "%{crate}" crate.

%files       -n %{name}+with-backtrace-devel
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
