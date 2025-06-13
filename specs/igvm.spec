%global __brp_strip_static_archive %{nil}

Name:           igvm
Version:        0.3.4
Release:        %autorelease
Summary:        IGVM library

License:        MIT
URL:            https://github.com/microsoft/igvm
Source:         https://github.com/microsoft/igvm/archive/refs/tags/igvm-v%{version}.tar.gz

ExcludeArch: %{ix86}

BuildRequires:  cargo-rpm-macros >= 24
BuildRequires:  CUnit-devel cbindgen gettext-envsubst make gcc

# All these patches are already available upstream, can be safely dropped _after_ version 0.3.4
# They bump dependencies version and fix an issue in the makefile
Patch0: 0001-zerocopy-update-from-0.7.x-to-0.8.x.-77.patch
Patch1: 0002-Add-test-for-SnpVpContext-82.patch
Patch2: 0003-repo-update-dependencies-83.patch
Patch3: 0004-igvm_c-Makefile-Fix-dependency-path-84.patch
Patch4: 0005-igvm-fix-1.86-clippy-lints-87.patch
Patch5: 0006-igvm_c-Makefile-add-two-new-external-parameters-86.patch
Patch6: 0001-igvm_c-Makefile-Separate-build-and-test-target.patch
Patch7: 0001-igvm_c-Makefile-add-CFLAGS-LDFLAGS-CC-and-.PHONY-tar.patch

# Bump bitfield struct to version 0.11
Patch8: 0001-update-bitfield-struct-to-version-0.11.patch

%description
Igvm is an implementation of a parser for the Independent Guest Virtual Machine

%package devel
Provides: igvm-static = %{version}-%{release}
Summary: IGVM library header files

%description devel
Contains header files for developing applications that use the %{name}

%package tools
Summary: IGVM static library tools

%description tools
The %{name}-tools package contains tools for
developing applications that use %{name}

%prep
%autosetup -n igvm-igvm-v%{version} -p1
%cargo_prep

%generate_buildrequires
%cargo_generate_buildrequires

%build
%cargo_license_summary
%{cargo_license} > LICENSE.dependencies

export EXTRA_PARAMS="--profile rpm"
export TARGET_DIR="target"
export RELEASE=1

# -Csymbol-mangling-version=v0 is from the upstream .cargo/config.toml.
# Enable v0 symbols to get better output from `perf` and related tools.
CARGO_HOME='.cargo' RUSTFLAGS='%{build_rustflags} -Csymbol-mangling-version=v0' %make_build -C igvm_c build

%check
export EXTRA_PARAMS="--profile rpm"
export TARGET_DIR="target"
export RELEASE=1

CARGO_HOME='.cargo' RUSTFLAGS='%{build_rustflags} -Csymbol-mangling-version=v0' %make_build -C igvm_c test

%install
export TARGET_DIR="target"
export RELEASE=1

%make_install -C igvm_c PREFIX=/usr DESTDIR=%{buildroot}

%files devel
%{_includedir}/igvm
%license LICENSE
%license LICENSE.dependencies
%doc README.md
%{_libdir}/libigvm.a
%{_libdir}/pkgconfig/igvm.pc

%files tools
%{_bindir}/dump_igvm
%doc README.md

%changelog
%autochangelog
