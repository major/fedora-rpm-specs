# Generated by rust2rpm 26
%bcond_without check
%global debug_package %{nil}

%global crate pollster

Name:           rust-pollster
Version:        0.3.0
Release:        %autorelease
Summary:        Synchronously block the thread until a future completes

# Upstream license specification: Apache-2.0/MIT
License:        Apache-2.0 OR MIT
URL:            https://crates.io/crates/pollster
Source:         %{crates_source}

BuildRequires:  cargo-rpm-macros >= 24

%global _description %{expand:
Synchronously block the thread until a future completes.}

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

%package     -n %{name}+macro-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+macro-devel %{_description}

This package contains library source intended for building other packages which
use the "macro" feature of the "%{crate}" crate.

%files       -n %{name}+macro-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+pollster-macro-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+pollster-macro-devel %{_description}

This package contains library source intended for building other packages which
use the "pollster-macro" feature of the "%{crate}" crate.

%files       -n %{name}+pollster-macro-devel
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
