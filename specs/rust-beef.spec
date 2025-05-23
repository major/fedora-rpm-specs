# Generated by rust2rpm 23
%bcond_without check
%global debug_package %{nil}

%global crate beef

Name:           rust-beef
Version:        0.5.2
Release:        %autorelease
Summary:        More compact Cow

License:        MIT OR Apache-2.0
URL:            https://crates.io/crates/beef
Source:         %{crates_source}

BuildRequires:  rust-packaging >= 21

%global _description %{expand:
More compact Cow.}

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

%package     -n %{name}+const_fn-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+const_fn-devel %{_description}

This package contains library source intended for building other packages which
use the "const_fn" feature of the "%{crate}" crate.

%files       -n %{name}+const_fn-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+impl_serde-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+impl_serde-devel %{_description}

This package contains library source intended for building other packages which
use the "impl_serde" feature of the "%{crate}" crate.

%files       -n %{name}+impl_serde-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+serde-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+serde-devel %{_description}

This package contains library source intended for building other packages which
use the "serde" feature of the "%{crate}" crate.

%files       -n %{name}+serde-devel
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
# * struct size assumptions wrong on 32-bit architectures:
#   https://github.com/maciejhirsz/beef/issues/43
# * struct size assumptions wrong with Rust 1.65+:
#   https://github.com/maciejhirsz/beef/issues/52
%cargo_test -- -- --skip src/lib.rs
%endif

%changelog
%autochangelog
