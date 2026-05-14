%bcond check 1

Name:           arapuca
Version:        0.2.2
Release:        %autorelease
Summary:        Cross-platform process sandbox with kernel-enforced isolation

SourceLicense:  Apache-2.0
# Apache-2.0
# Apache-2.0 OR BSD-3-Clause
# Apache-2.0 OR MIT
# Apache-2.0 WITH LLVM-exception OR Apache-2.0 OR MIT
# MIT
# MIT OR Apache-2.0
# MIT OR Apache-2.0 OR LGPL-2.1-or-later
License:        %{shrink:
    Apache-2.0 AND
    MIT AND
    (Apache-2.0 OR BSD-3-Clause) AND
    (Apache-2.0 WITH LLVM-exception OR Apache-2.0 OR MIT) AND
    (MIT OR Apache-2.0 OR LGPL-2.1-or-later)
}
# LICENSE.dependencies contains a full license breakdown

URL:            https://github.com/sergio-correia/arapuca
Source0:        %{url}/archive/v%{version}/arapuca-%{version}.tar.gz
# The vendor tarball is created using cargo-vendor-filterer to remove
# non-Linux platform files (https://github.com/cgwalters/cargo-vendor-filterer)
#   tar xf arapuca-%%{version}.tar.gz
#   cd arapuca-%%{version}
#   cargo vendor-filterer --platform x86_64-unknown-linux-gnu \
#       --platform powerpc64le-unknown-linux-gnu \
#       --platform aarch64-unknown-linux-gnu \
#       --platform i686-unknown-linux-gnu \
#       --platform s390x-unknown-linux-gnu \
#       --prefix=vendor --format=tar.zstd
#   mv vendor.tar.zstd arapuca-%%{version}-vendor.tar.zstd
# NOTE: The vendor tarball includes stubs for optional microvm feature deps
# (krun-sys, openssl, reqwest, etc.) to satisfy Cargo.lock. These are not
# compiled or linked — the microvm feature is not enabled in this build.
# cargo-vendor-filterer stubs them; %%cargo_vendor_manifest lists them in
# bundled() provides regardless. This is a known limitation.
Source1:        arapuca-%{version}-vendor.tar.zstd

ExclusiveArch:  %{rust_arches}

BuildRequires:  cargo-rpm-macros
BuildRequires:  pandoc
BuildRequires:  git-core

%description
arapuca applies OS-level sandbox restrictions to processes using
kernel security primitives. On Linux: Landlock LSM filesystem
confinement, seccomp BPF syscall filtering, cgroup v2 resource
limits, and network namespace isolation.

Provides a C-compatible static library (libarapuca.a) with header
and pkg-config file for embedding in C, Go, and other FFI-capable
languages.

# Per Rust guidelines "Using vendor tarballs": the prohibition on -devel
# subpackages applies to Rust crate interfaces (crate sources + crate()
# Provides). This subpackage ships only C-ABI artifacts.
# No Requires on base package: the static library is self-contained and
# usable without the CLI binary.
%package        devel
Summary:        Development files for arapuca
Provides:       %{name}-static = %{version}-%{release}

%description    devel
Static library, C header, and pkg-config file for linking against
libarapuca.

%prep
%autosetup -S git -a1
%cargo_prep -v vendor

%generate_buildrequires
# Vendored dependencies: do not call %%cargo_generate_buildrequires
# (see Rust Packaging Guidelines, "Using vendor tarballs")

%build
%cargo_build

# Generate license info
%{cargo_license_summary}
%{cargo_license} > LICENSE.dependencies

# Generate vendor manifest for bundled provides
%cargo_vendor_manifest

# Generate man page
pandoc doc/arapuca.1.md -s -t man -o doc/arapuca.1

# Metadata-only query — the library was already built by %%cargo_build.
# Picks up .cargo/config.toml written by %%cargo_prep.
NATIVE_LIBS=$(CARGO_TERM_COLOR=never cargo rustc --release --lib \
    -- --print native-static-libs 2>&1 \
    | grep 'native-static-libs:' \
    | sed 's/.*native-static-libs: //')
sed -e 's|@PREFIX@|%{_prefix}|g' \
    -e 's|@LIBDIR@|%{_libdir}|g' \
    -e "s|@VERSION@|%{version}|g" \
    -e "s|@NATIVE_LIBS@|${NATIVE_LIBS}|g" \
    -e 's|@INSTALL_FEATURES@||g' \
    arapuca.pc.in > arapuca.pc

%install
# Binary
install -Dpm 0755 target/rpm/arapuca -t %{buildroot}%{_bindir}

# Static library
install -Dpm 0644 target/rpm/libarapuca.a -t %{buildroot}%{_libdir}

# Header
install -Dpm 0644 include/arapuca.h -t %{buildroot}%{_includedir}

# pkg-config
install -Dpm 0644 arapuca.pc -t %{buildroot}%{_libdir}/pkgconfig

# Man page
install -Dpm 0644 doc/arapuca.1 -t %{buildroot}%{_mandir}/man1

%check
%if %{with check}
# Integration tests require root/capabilities; run unit and doc tests only
%cargo_test -- --lib
%cargo_test -- --doc
%endif

%files
%license LICENSE
%license LICENSE.dependencies
%license cargo-vendor.txt
%doc README.md
%{_bindir}/arapuca
%{_mandir}/man1/arapuca.1*

%files devel
%license LICENSE
%license LICENSE.dependencies
%license cargo-vendor.txt
%{_includedir}/arapuca.h
%{_libdir}/libarapuca.a
%{_libdir}/pkgconfig/arapuca.pc

%changelog
%autochangelog
