# Generated by rust2rpm 26
%bcond_without check
%global debug_package %{nil}

%global crate libbpf-rs

Name:           rust-libbpf-rs
Version:        0.24.4
Release:        %autorelease
Summary:        Safe, idiomatic, and opinionated wrapper around libbpf-sys

License:        LGPL-2.1-only OR BSD-2-Clause
URL:            https://crates.io/crates/libbpf-rs
Source:         %{crates_source}
# Manually created patch for downstream crate metadata changes
# * bump probe from 0.3 to 0.5
Patch:          libbpf-rs-fix-metadata.diff
# * probe needs feature(asm_experimental_arch) on ppc64le and s390x
# * https://github.com/rust-lang/rust/issues/93335
# * https://github.com/libbpf/libbpf-rs/pull/944
Patch:          libbpf-rs-disable-probe-tests-on-ppc64le-s390x.diff

BuildRequires:  cargo-rpm-macros >= 24

%global _description %{expand:
Libbpf-rs is a safe, idiomatic, and opinionated wrapper around libbpf-
sys.}

%description %{_description}

%package        devel
Summary:        %{summary}
BuildArch:      noarch

%description    devel %{_description}

This package contains library source intended for building other packages which
use the "%{crate}" crate.

%files          devel
%license %{crate_instdir}/LICENSE
%license %{crate_instdir}/LICENSE.BSD-2-Clause
%license %{crate_instdir}/LICENSE.LGPL-2.1
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

%package     -n %{name}+dont-generate-test-files-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+dont-generate-test-files-devel %{_description}

This package contains library source intended for building other packages which
use the "dont-generate-test-files" feature of the "%{crate}" crate.

%files       -n %{name}+dont-generate-test-files-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+generate-test-files-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+generate-test-files-devel %{_description}

This package contains library source intended for building other packages which
use the "generate-test-files" feature of the "%{crate}" crate.

%files       -n %{name}+generate-test-files-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+libbpf-sys-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+libbpf-sys-devel %{_description}

This package contains library source intended for building other packages which
use the "libbpf-sys" feature of the "%{crate}" crate.

%files       -n %{name}+libbpf-sys-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+static-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+static-devel %{_description}

This package contains library source intended for building other packages which
use the "static" feature of the "%{crate}" crate.

%files       -n %{name}+static-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+vendored-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+vendored-devel %{_description}

This package contains library source intended for building other packages which
use the "vendored" feature of the "%{crate}" crate.

%files       -n %{name}+vendored-devel
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
# * tests tagged as "root" fail, RLIMIT_MEMLOCK does not work in mock
# * tests loading tests/bin/runqslower.bpf.o fail, as it's not built
%cargo_test -- -- --skip :root: --skip test_object_build_from_memory --skip test_object_build_from_memory_empty_name --skip test_object_name --skip test_object_link_files
%endif

%changelog
%autochangelog
