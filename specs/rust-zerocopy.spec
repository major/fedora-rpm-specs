# Generated by rust2rpm 27
# * missing dev-dependencies: elain ^0.3
%bcond check 0
%global debug_package %{nil}

%global crate zerocopy

Name:           rust-zerocopy
Version:        0.8.26
Release:        %autorelease
Summary:        Makes zero-cost memory manipulation effortless

License:        BSD-2-Clause OR Apache-2.0 OR MIT
URL:            https://crates.io/crates/zerocopy
Source:         %{crates_source}

BuildRequires:  cargo-rpm-macros >= 24

%global _description %{expand:
Zerocopy makes zero-cost memory manipulation effortless. We write
"unsafe" so you don't have to.}

%description %{_description}

%package        devel
Summary:        %{summary}
BuildArch:      noarch

%description    devel %{_description}

This package contains library source intended for building other packages which
use the "%{crate}" crate.

%files          devel
%license %{crate_instdir}/LICENSE-APACHE
%license %{crate_instdir}/LICENSE-BSD
%license %{crate_instdir}/LICENSE-MIT
%doc %{crate_instdir}/CHANGELOG.md
%doc %{crate_instdir}/CONTRIBUTING.md
%doc %{crate_instdir}/POLICIES.md
%doc %{crate_instdir}/README.md
%{crate_instdir}/
%exclude %{crate_instdir}/ci/
%exclude %{crate_instdir}/githooks/
%exclude %{crate_instdir}/testdata/
%exclude %{crate_instdir}/cargo.sh
%exclude %{crate_instdir}/clippy.toml
%exclude %{crate_instdir}/rustfmt.toml
%exclude %{crate_instdir}/win-cargo.bat

%package     -n %{name}+default-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+default-devel %{_description}

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%files       -n %{name}+default-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+__internal_use_only_features_that_work_on_stable-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+__internal_use_only_features_that_work_on_stable-devel %{_description}

This package contains library source intended for building other packages which
use the "__internal_use_only_features_that_work_on_stable" feature of the "%{crate}" crate.

%files       -n %{name}+__internal_use_only_features_that_work_on_stable-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+alloc-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+alloc-devel %{_description}

This package contains library source intended for building other packages which
use the "alloc" feature of the "%{crate}" crate.

%files       -n %{name}+alloc-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+derive-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+derive-devel %{_description}

This package contains library source intended for building other packages which
use the "derive" feature of the "%{crate}" crate.

%files       -n %{name}+derive-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+float-nightly-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+float-nightly-devel %{_description}

This package contains library source intended for building other packages which
use the "float-nightly" feature of the "%{crate}" crate.

%files       -n %{name}+float-nightly-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+simd-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+simd-devel %{_description}

This package contains library source intended for building other packages which
use the "simd" feature of the "%{crate}" crate.

%files       -n %{name}+simd-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+simd-nightly-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+simd-nightly-devel %{_description}

This package contains library source intended for building other packages which
use the "simd-nightly" feature of the "%{crate}" crate.

%files       -n %{name}+simd-nightly-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+std-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+std-devel %{_description}

This package contains library source intended for building other packages which
use the "std" feature of the "%{crate}" crate.

%files       -n %{name}+std-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+zerocopy-derive-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+zerocopy-derive-devel %{_description}

This package contains library source intended for building other packages which
use the "zerocopy-derive" feature of the "%{crate}" crate.

%files       -n %{name}+zerocopy-derive-devel
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
