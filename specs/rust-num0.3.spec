# Generated by rust2rpm 24
%bcond_without check
%global debug_package %{nil}

%global crate num

Name:           rust-num0.3
Version:        0.3.1
Release:        %autorelease
Summary:        Collection of numeric types and traits for Rust

License:        MIT OR Apache-2.0
URL:            https://crates.io/crates/num
Source:         %{crates_source}

BuildRequires:  rust-packaging >= 21

%global _description %{expand:
A collection of numeric types and traits for Rust, including bigint,
complex, rational, range iterators, generic integers, and more!.}

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
%doc %{crate_instdir}/RELEASES.md
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

%package     -n %{name}+libm-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+libm-devel %{_description}

This package contains library source intended for building other packages which
use the "libm" feature of the "%{crate}" crate.

%files       -n %{name}+libm-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+num-bigint-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+num-bigint-devel %{_description}

This package contains library source intended for building other packages which
use the "num-bigint" feature of the "%{crate}" crate.

%files       -n %{name}+num-bigint-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+rand-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+rand-devel %{_description}

This package contains library source intended for building other packages which
use the "rand" feature of the "%{crate}" crate.

%files       -n %{name}+rand-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+serde-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+serde-devel %{_description}

This package contains library source intended for building other packages which
use the "serde" feature of the "%{crate}" crate.

%files       -n %{name}+serde-devel
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
