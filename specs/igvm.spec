%global __brp_strip_static_archive %{nil}

Name:           igvm
Version:        0.4.0
Release:        %autorelease
Summary:        IGVM library

License:        MIT
URL:            https://github.com/microsoft/igvm
Source:         https://github.com/microsoft/igvm/archive/refs/tags/igvm-v%{version}.tar.gz

ExcludeArch: %{ix86}

BuildRequires:  cargo-rpm-macros >= 24
BuildRequires:  CUnit-devel cbindgen cargo-c make gcc

# Bump bitfield struct to version 0.11
Patch1: 0001-update-bitfield-struct-to-version-0.11.patch
Patch2: 0002-switch-to-cbuild.patch

%description
Igvm is an implementation of a parser for the Independent Guest Virtual Machine

%package libs
Summary: IGVM shared library

%description libs
Contains a shared library that applications that use %{name} will link to

%package devel
Provides: igvm-static = %{version}-%{release}
Summary: IGVM library header files

%description devel
Contains header files and a static library for developing applications that use %{name}

%package tools
Summary: IGVM tools

%description tools
The %{name}-tools package contains tools for
developing applications that use %{name}

%prep
%autosetup -n igvm-igvm-v%{version} -p1
%cargo_prep

%generate_buildrequires
%cargo_generate_buildrequires

%define igvm_makeflags EXTRA_PARAMS="--profile rpm" TARGET_DIR="target" PROFILE=rpm
%define igvm_makeenv CARGO_HOME='.cargo' RUSTFLAGS='%{build_rustflags} -Csymbol-mangling-version=v0'

%build
%cargo_license_summary
%{cargo_license} > LICENSE.dependencies

# -Csymbol-mangling-version=v0 is from the upstream .cargo/config.toml.
# Enable v0 symbols to get better output from `perf` and related tools.
%{igvm_makeenv} %make_build -C igvm_c build %{igvm_makeflags}

%check
%{igvm_makeenv} %make_build -C igvm_c test %{igvm_makeflags}

%install
%{igvm_makeenv} %make_install -C igvm_c PREFIX=/usr DESTDIR=%{buildroot} %{igvm_makeflags}

%files libs
%{_libdir}/libigvm.so.*

%files devel
%{_includedir}/igvm
%license LICENSE
%license LICENSE.dependencies
%doc README.md
%{_libdir}/libigvm.a
%{_libdir}/libigvm.so
%{_libdir}/pkgconfig/igvm.pc

%files tools
%{_bindir}/dump_igvm
%doc README.md

%changelog
%autochangelog
