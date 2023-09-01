# Extra dependencies are needed for testing
%bcond      check 1

Name:       wasi-libc
Summary:    C library implementation for WebAssembly System Interface
Version:    20
Release:    %autorelease

License:    Apache-2.0 WITH LLVM-exception AND Apache-2.0 AND MIT AND BSD-2-Clause
URL:        https://github.com/WebAssembly/wasi-libc/
Source:     %{url}/archive/refs/tags/wasi-sdk-%{version}.tar.gz#/%{name}-wasi-sdk-%{version}.tar.gz
Source1:    smoke-test.c

# Allow using artifacts from %%build in %%install instead of recompiling
Patch:      0001-make-don-t-rebuild-files-on-make-install.patch

# emmalloc uses a lot of pointer type-punning, which is UB under strict aliasing.
# https://github.com/WebAssembly/wasi-libc/pull/424
Patch:      0001-Use-fno-strict-aliasing-for-emmalloc-424.patch

# This contains parts of the musl C library; specify as bundled so we get notified about potential vulnerabilities
%global     musl_version 1.2.3

# Although these packages provide binary files, they are not targeted
# for the build platform, but for wasm32-wasi.
# See the relevant discussion (for similar case) here:
# https://www.redhat.com/archives/fedora-devel-list/2009-February/msg02261.html
%global     _binaries_in_noarch_packages_terminate_build 0
BuildArch:  noarch

BuildRequires:  clang >= 10
BuildRequires:  git-core
BuildRequires:  llvm >= 10
BuildRequires:  make
%if %{with check}
# can be replaced with another CLI WASM execution method
BuildRequires:  wasmedge
%endif

%global     toolchain clang
# Re-packaging the static library tends to overwrite files
# (and effectively undefine symbols like errno). Disable it.
# See rhbz#2228297 for details.
%global     __brp_llvm_compile_lto_elf %{nil}

# WASI is a specific architecture; host (build machine) arch flags should not apply by default
%global     build_cflags --target=wasm32-wasi -fstack-protector
# Define cross-compiling prefix
%global     wasi_prefix %{_prefix}/wasm32-wasi
%global     wasi_datadir %{wasi_prefix}/share
%global     wasi_includedir %{wasi_prefix}/include
%global     wasi_libdir %{wasi_prefix}/lib
%global     wasi_make_flags MALLOC_IMPL=emmalloc INSTALL_DIR='%{buildroot}%{wasi_prefix}' SYSROOT='%{_builddir}/sysroot'

%global _description %{expand:
WASI Libc is a libc for WebAssembly programs built on top of WASI system calls.
It provides a wide array of POSIX-compatible C APIs, including support for
standard I/O, file I/O, filesystem manipulation, memory management, time,
string, environment variables, program startup, and many other APIs.}

%description %{_description}

%package static
Provides: bundled(musl) = %{musl_version}
Summary:  C library for WASI - static libraries

%description static %{_description}

%package devel
Requires: %{name}-static  = %{version}-%{release}
Provides: bundled(musl) = %{musl_version}
Summary:  C library for WASI - headers and development files

%description devel %{_description}


%prep
%autosetup -n %{name}-wasi-sdk-%{version} -S git_am
# Pull additional license text
cp -p libc-bottom-half/cloudlibc/LICENSE LICENSE-cloudlibc

%build
%make_build %{wasi_make_flags}
make %{?_smp_mflags} %{wasi_make_flags} check-symbols

%install
%make_install %{wasi_make_flags}

# brp-strip-static-archive breaks the archive index for wasm
%global __os_install_post %{expand:
    %__os_install_post
    find %{buildroot}%{wasi_libdir} -type f -regex '.*\\.\\(a\\|rlib\\)' -print -exec llvm-ranlib '{}' ';'
}

%check
# Bundled version checks
xargs test '%{musl_version}' = <libc-top-half/musl/VERSION
# Basic smoke test
%if %{with check}
# -> Smoke test is compilable and linkable against the built version
clang --target=wasm32-wasi --sysroot=%{buildroot}%{wasi_prefix} -nodefaultlibs -lc -o smoke-test.wasm %{SOURCE1}
# -> Smoke test works as expected (exit code 0, outputs 'smoke-test-ok')
wasmedge smoke-test.wasm | grep -q --fixed-strings smoke-test-ok
%endif

%files static
%doc README.md
%license LICENSE LICENSE-APACHE LICENSE-APACHE-LLVM LICENSE-MIT LICENSE-cloudlibc
%dir %{wasi_prefix}
%{wasi_libdir}

%files devel
%doc README.md
%license LICENSE LICENSE-APACHE LICENSE-APACHE-LLVM LICENSE-MIT LICENSE-cloudlibc
%dir %{wasi_prefix}
%{wasi_datadir}
%{wasi_includedir}

%changelog
%autochangelog
