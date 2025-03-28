# Generated by rust2rpm 27
%bcond check 1
%global debug_package %{nil}

%global crate typenum

Name:           rust-typenum
Version:        1.18.0
Release:        %autorelease
Summary:        Type-level numbers evaluated at compile time

License:        MIT OR Apache-2.0
URL:            https://crates.io/crates/typenum
Source:         %{crates_source}
# Manually created patch for downstream crate metadata changes
# * exclude some files from published crates:
#   https://github.com/paholg/typenum/pull/223
Patch:          typenum-fix-metadata.diff

BuildRequires:  cargo-rpm-macros >= 24

%global _description %{expand:
Typenum is a Rust library for type-level numbers evaluated at compile
time. It currently supports bits, unsigned integers, and signed
integers. It also provides a type-level array of type-level numbers, but
its implementation is incomplete.}

%description %{_description}

%package        devel
Summary:        %{summary}
BuildArch:      noarch

%description    devel %{_description}

This package contains library source intended for building other packages which
use the "%{crate}" crate.

%files          devel
%license %{crate_instdir}/LICENSE
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

%package     -n %{name}+const-generics-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+const-generics-devel %{_description}

This package contains library source intended for building other packages which
use the "const-generics" feature of the "%{crate}" crate.

%files       -n %{name}+const-generics-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+force_unix_path_separator-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+force_unix_path_separator-devel %{_description}

This package contains library source intended for building other packages which
use the "force_unix_path_separator" feature of the "%{crate}" crate.

%files       -n %{name}+force_unix_path_separator-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+i128-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+i128-devel %{_description}

This package contains library source intended for building other packages which
use the "i128" feature of the "%{crate}" crate.

%files       -n %{name}+i128-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+no_std-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+no_std-devel %{_description}

This package contains library source intended for building other packages which
use the "no_std" feature of the "%{crate}" crate.

%files       -n %{name}+no_std-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+strict-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+strict-devel %{_description}

This package contains library source intended for building other packages which
use the "strict" feature of the "%{crate}" crate.

%files       -n %{name}+strict-devel
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
