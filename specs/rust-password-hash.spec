# Generated by rust2rpm 24
%bcond_without check
%global debug_package %{nil}

%global crate password-hash

Name:           rust-password-hash
Version:        0.5.0
Release:        %autorelease
Summary:        Traits which describe the functionality of password hashing algorithms

License:        MIT OR Apache-2.0
URL:            https://crates.io/crates/password-hash
Source:         %{crates_source}

BuildRequires:  rust-packaging >= 21

%global _description %{expand:
Traits which describe the functionality of password hashing algorithms,
as well as a `no_std`-friendly implementation of the PHC string format
(a well-defined subset of the Modular Crypt Format a.k.a. MCF).}

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

%package     -n %{name}+alloc-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+alloc-devel %{_description}

This package contains library source intended for building other packages which
use the "alloc" feature of the "%{crate}" crate.

%files       -n %{name}+alloc-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+getrandom-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+getrandom-devel %{_description}

This package contains library source intended for building other packages which
use the "getrandom" feature of the "%{crate}" crate.

%files       -n %{name}+getrandom-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+rand_core-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+rand_core-devel %{_description}

This package contains library source intended for building other packages which
use the "rand_core" feature of the "%{crate}" crate.

%files       -n %{name}+rand_core-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+std-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+std-devel %{_description}

This package contains library source intended for building other packages which
use the "std" feature of the "%{crate}" crate.

%files       -n %{name}+std-devel
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