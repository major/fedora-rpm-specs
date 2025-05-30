# Generated by rust2rpm 27
%bcond check 1
%global debug_package %{nil}

%global crate tikv-jemalloc-sys
%global crate_version 0.6.0+5.3.0-1-ge13ca993e8ccb9ba9847cc330696e02839f328f7

Name:           rust-tikv-jemalloc-sys
Version:        0.6.0
Release:        %autorelease
Summary:        Rust FFI bindings to jemalloc

# Upstream license specification: MIT/Apache-2.0
License:        MIT OR Apache-2.0
URL:            https://crates.io/crates/tikv-jemalloc-sys
Source:         %{crates_source %{crate} %{crate_version}}
# Automatically generated patch to strip dependencies and normalize metadata
Patch:          tikv-jemalloc-sys-fix-metadata-auto.diff
# * Downstream-only: always use the system jemalloc
Patch10:        0001-Downstream-only-always-use-the-system-jemalloc.patch

BuildRequires:  cargo-rpm-macros >= 24
BuildRequires:  tomcli
BuildRequires:  pkgconfig(jemalloc)

%global _description %{expand:
Rust FFI bindings to jemalloc.}

%description %{_description}

%package        devel
Summary:        %{summary}
BuildArch:      noarch
Requires:       pkgconfig(jemalloc)

%description    devel %{_description}

This package contains library source intended for building other packages which
use the "%{crate}" crate.

%files          devel
%license %{crate_instdir}/LICENSE-APACHE
%license %{crate_instdir}/LICENSE-MIT
%doc %{crate_instdir}/README.md
%doc %{crate_instdir}/update_jemalloc.md
%{crate_instdir}/

%package     -n %{name}+default-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+default-devel %{_description}

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%files       -n %{name}+default-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+background_threads-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+background_threads-devel %{_description}

This package contains library source intended for building other packages which
use the "background_threads" feature of the "%{crate}" crate.

%files       -n %{name}+background_threads-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+background_threads_runtime_support-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+background_threads_runtime_support-devel %{_description}

This package contains library source intended for building other packages which
use the "background_threads_runtime_support" feature of the
"%{crate}" crate.

%files       -n %{name}+background_threads_runtime_support-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+debug-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+debug-devel %{_description}

This package contains library source intended for building other packages which
use the "debug" feature of the "%{crate}" crate.

%files       -n %{name}+debug-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+profiling-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+profiling-devel %{_description}

This package contains library source intended for building other packages which
use the "profiling" feature of the "%{crate}" crate.

%files       -n %{name}+profiling-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+stats-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+stats-devel %{_description}

This package contains library source intended for building other packages which
use the "stats" feature of the "%{crate}" crate.

%files       -n %{name}+stats-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+unprefixed_malloc_on_supported_platforms-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+unprefixed_malloc_on_supported_platforms-devel %{_description}

This package contains library source intended for building other packages which
use the "unprefixed_malloc_on_supported_platforms" feature of the
"%{crate}" crate.

%files       -n %{name}+unprefixed_malloc_on_supported_platforms-devel
%ghost %{crate_instdir}/Cargo.toml

%prep
%autosetup -n %{crate}-%{crate_version} -p1
# Remove the bundled copy of jemalloc.
# It has the following licenses:
# BSD-2-Clause: everything not otherwise indicated
# BSD-3-Clause: jemalloc/bin/jeprof.in, jemalloc/test/{src,unit}/SFMT.c,
#               jemalloc/test/include/test/SFMT*.h
# FSFAP: jemalloc/m4/ax_cxx_compile_stdcxx.m4
# GPL-3.0-or-later: jemalloc/build-aux/config.{guess,sub}
# HPND-Sell: jemalloc/build-aux/install-sh
# MIT: jemalloc/test/unit/hash.c
# LicenseRef-Fedora-Public-Domain: jemalloc/include/jemalloc/internal/hash.h
#     (https://gitlab.com/fedora/legal/fedora-license-data/-/issues/660)
rm -rv jemalloc
# Remove the configure script for the bundled jemalloc.
# Its license is: FSFUL AND FSFAP
rm -rv configure
# Add unprefixed_malloc_on_supported_platforms to default features. Since
# we always use the system jemalloc, and it is unprefixed, this feature is
# effectively always enabled, so this helps dependent code with conditionals
# do the right thing, particularly some of the tests in
# rust-tikv-jemallocator.
tomcli set Cargo.toml append features.default \
    unprefixed_malloc_on_supported_platforms
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
