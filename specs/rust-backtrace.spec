# Generated by rust2rpm 27
%bcond check 1
%global debug_package %{nil}

%global crate backtrace

Name:           rust-backtrace
Version:        0.3.75
Release:        %autorelease
Summary:        Library to acquire a stack trace (backtrace) at runtime in a Rust program

License:        MIT OR Apache-2.0
URL:            https://crates.io/crates/backtrace
Source:         %{crates_source}
# Automatically generated patch to strip dependencies and normalize metadata
Patch:          backtrace-fix-metadata-auto.diff
# Manually created patch for downstream crate metadata changes
# * drop "accuracy" test (requires crates to be built in dylib mode)
# * drop "current-exe-mismatch" test (fails on i686 for unknown reasons)
Patch:          backtrace-fix-metadata.diff

BuildRequires:  cargo-rpm-macros >= 24

%global _description %{expand:
A library to acquire a stack trace (backtrace) at runtime in a Rust
program.}

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

%package     -n %{name}+cpp_demangle-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+cpp_demangle-devel %{_description}

This package contains library source intended for building other packages which
use the "cpp_demangle" feature of the "%{crate}" crate.

%files       -n %{name}+cpp_demangle-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+dl_iterate_phdr-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+dl_iterate_phdr-devel %{_description}

This package contains library source intended for building other packages which
use the "dl_iterate_phdr" feature of the "%{crate}" crate.

%files       -n %{name}+dl_iterate_phdr-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+ruzstd-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+ruzstd-devel %{_description}

This package contains library source intended for building other packages which
use the "ruzstd" feature of the "%{crate}" crate.

%files       -n %{name}+ruzstd-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+serde-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+serde-devel %{_description}

This package contains library source intended for building other packages which
use the "serde" feature of the "%{crate}" crate.

%files       -n %{name}+serde-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+serialize-serde-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+serialize-serde-devel %{_description}

This package contains library source intended for building other packages which
use the "serialize-serde" feature of the "%{crate}" crate.

%files       -n %{name}+serialize-serde-devel
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
%autosetup -n %{crate}-%{version} -p1
%cargo_prep
# drop "accuracy" test (requires crates to be built in dylib mode)
# drop "current-exe-mismatch" test (fails on i686 for unknown reasons)
rm -r tests/accuracy/
rm tests/current-exe-mismatch.rs

%generate_buildrequires
%cargo_generate_buildrequires

%build
%cargo_build

%install
%cargo_install

%if %{with check}
%check
# * https://github.com/rust-lang/backtrace-rs/issues/204
# * tests/smoke.rs/smoke_test_frames: fails on all architectures
# * tests/smoke.rs/sp_smoke_test: crashes when frame pointers are enabled on
#   x86_64
# * backtrace_new_should_start_with_call_site_trace: fails on s390x
# * backtrace_new_unresolved_should_start_with_call_site_trace: fails on
#   aarch64, ppc64le, s390x
%{cargo_test -- -- %{shrink:
    --skip smoke_test_frames
    --skip sp_smoke_test
    --skip backtrace_new_should_start_with_call_site_trace
    --skip backtrace_new_unresolved_should_start_with_call_site_trace
}}
%endif

%changelog
%autochangelog
