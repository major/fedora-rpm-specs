# Generated by rust2rpm 24
%bcond_without check
%global debug_package %{nil}

%global crate probe

Name:           rust-probe
Version:        0.5.1
Release:        %autorelease
Summary:        Static instrumentation probes

License:        Apache-2.0 OR MIT
URL:            https://crates.io/crates/probe
Source:         %{crates_source}

BuildRequires:  rust-packaging >= 21

# error[E0658]: inline assembly is not stable yet on this architecture
# https://github.com/rust-lang/rust/issues/93335
ExcludeArch:    ppc64le s390x

%global _description %{expand:
Static instrumentation probes.}

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
%doc %{crate_instdir}/AUTHORS.txt
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
