
%if 0%{?fedora} >= 41
# on Fedora >= 41
%undefine __brp_add_determinism
%endif
%global debug_package %{nil}
%undefine _auto_set_build_flags

%global linux_version fedora

#################################################
# Make sure these are changed for every release!
#################################################
%global swift_version 6.1.3-RELEASE
%global package_version 6.1.3

%global swift_source_location swift-source

# Set to the right version per the json file
# Run 'extract_versions.sh' to get updated
# versions.
%global yams_version 5.0.6
%global swift_argument_parser_version 1.4.0
%global swift_crypto_version 3.0.0
%global ninja_version 1.11.1
%global cmake_version 3.30.2
%global swift_atomics_version 1.2.0
%global swift_collections_version 1.1.3
%global swift_numerics_version 1.0.2
%global swift_system_version 1.3.0
%global swift_nio_version 2.65.0
%global swift_certificates_version 1.0.1
%global swift_asn1_version 1.0.0
%global wasmkit_version 0.1.2
%global wasi_version 22
%global swift_format_version 6.1
%global swift_llvm_bindings_version 6.1
%global swift_foundation_icu_version 6.1
%global swift_foundation_version 6.1
%global swift_sdk_generator_version 6.1
%global swift_async_algorithms_version 1.0.1
%global swift_log_version 1.5.4
%global swift_toolchain_sqlite_version 1.0.1
%global zlib_version 1.3.1


Name:           swift-lang
Version:        %{package_version}
Release:        %autorelease
Summary:        The Swift programming language
License:        Apache-2.0
URL:            https://www.swift.org

Source0:        https://github.com/apple/swift/archive/refs/tags/swift-%{swift_version}.tar.gz#/swift.tar.gz
Source1:        https://github.com/apple/swift-corelibs-libdispatch/archive/swift-%{swift_version}.tar.gz#/corelibs-libdispatch.tar.gz
Source2:        https://github.com/apple/swift-corelibs-foundation/archive/swift-%{swift_version}.tar.gz#/corelibs-foundation.tar.gz
Source3:        https://github.com/apple/swift-integration-tests/archive/swift-%{swift_version}.tar.gz#/swift-integration-tests.tar.gz
Source4:        https://github.com/apple/swift-corelibs-xctest/archive/swift-%{swift_version}.tar.gz#/corelibs-xctest.tar.gz
Source5:        https://github.com/apple/swift-package-manager/archive/swift-%{swift_version}.tar.gz#/package-manager.tar.gz
Source6:        https://github.com/apple/swift-llbuild/archive/swift-%{swift_version}.tar.gz#/llbuild.tar.gz
Source7:        https://github.com/apple/swift-cmark/archive/swift-%{swift_version}.tar.gz#/cmark.tar.gz
Source8:        https://github.com/apple/swift-xcode-playground-support/archive/swift-%{swift_version}.tar.gz#/swift-xcode-playground-support.tar.gz
Source9:        https://github.com/apple/sourcekit-lsp/archive/swift-%{swift_version}.tar.gz#/sourcekit-lsp.tar.gz
Source10:       https://github.com/apple/indexstore-db/archive/swift-%{swift_version}.tar.gz#/indexstore-db.tar.gz
Source11:       https://github.com/apple/llvm-project/archive/swift-%{swift_version}.tar.gz#/llvm-project.tar.gz
Source12:       https://github.com/apple/swift-tools-support-core/archive/swift-%{swift_version}.tar.gz#/swift-tools-support-core.tar.gz
Source13:       https://github.com/apple/swift-argument-parser/archive/%{swift_argument_parser_version}.tar.gz#/swift-argument-parser.tar.gz
Source14:       https://github.com/apple/swift-driver/archive/swift-%{swift_version}.tar.gz#/swift-driver.tar.gz
Source15:       https://github.com/apple/swift-syntax/archive/swift-%{swift_version}.zip#/swift-syntax.tar.gz
Source16:       https://github.com/jpsim/Yams/archive/%{yams_version}.tar.gz#/yams.tar.gz
Source17:       https://github.com/apple/swift-crypto/archive/refs/tags/%{swift_crypto_version}.tar.gz#/swift-crypto.tar.gz
Source18:       https://github.com/ninja-build/ninja/archive/refs/tags/v%{ninja_version}.tar.gz#/ninja.tar.gz
Source19:       https://github.com/KitWare/CMake/archive/refs/tags/v%{cmake_version}.tar.gz#/cmake.tar.gz
Source20:       https://github.com/apple/swift-atomics/archive/%{swift_atomics_version}.tar.gz#/swift-atomics.tar.gz
Source21:       https://github.com/apple/swift-stress-tester/archive/swift-%{swift_version}.tar.gz#/swift-stress-tester.tar.gz
Source22:       https://github.com/apple/swift-docc/archive/swift-%{swift_version}.tar.gz#/swift-docc.tar.gz
Source23:       https://github.com/apple/swift-docc-render-artifact/archive/swift-%{swift_version}.tar.gz#/swift-docc-render-artifact.tar.gz
Source24:       https://github.com/apple/swift-docc-symbolkit/archive/swift-%{swift_version}.tar.gz#/swift-docc-symbolkit.tar.gz
Source25:       https://github.com/apple/swift-collections/archive/%{swift_collections_version}.tar.gz#/swift-collections.tar.gz
Source26:       https://github.com/apple/swift-numerics/archive/%{swift_numerics_version}.tar.gz#/swift-numerics.tar.gz
Source27:       https://github.com/apple/swift-system/archive/%{swift_system_version}.tar.gz#/swift-system.tar.gz
Source28:       https://github.com/apple/swift-nio/archive/%{swift_nio_version}.tar.gz#/swift-nio.tar.gz
Source29:       https://github.com/apple/swift-sdk-generator/archive/refs/tags/swift-%{swift_sdk_generator_version}-RELEASE.tar.gz#/swift-sdk-generator.tar.gz
Source30:       https://github.com/apple/swift-format/archive/refs/heads/release/%{swift_format_version}.zip#/swift-format.zip
Source31:       https://github.com/apple/swift-lmdb/archive/swift-%{swift_version}.tar.gz#/swift-lmdb.tar.gz
Source32:       https://github.com/apple/swift-markdown/archive/swift-%{swift_version}.tar.gz#/swift-markdown.tar.gz
Source33:       https://github.com/apple/swift-experimental-string-processing/archive/swift-%{swift_version}.tar.gz#/swift-experimental-string-processing.tar.gz
Source34:       https://github.com/apple/swift-certificates/archive/%{swift_certificates_version}.tar.gz#/swift-certificates.tar.gz
Source35:       https://github.com/apple/swift-asn1/archive/%{swift_asn1_version}.tar.gz#/swift-asn1.tar.gz
Source36:       https://github.com/apple/swift-async-algorithms/archive/refs/tags/%{swift_async_algorithms_version}.tar.gz#/swift-async-algorithms.tar.gz
Source37:       https://github.com/swiftwasm/WasmKit/archive/refs/tags/%{wasmkit_version}.tar.gz#/wasm.tar.gz
Source38:       https://github.com/WebAssembly/wasi-libc/archive/refs/tags/wasi-sdk-%{wasi_version}.tar.gz#/wasi-sdk.tar.gz
Source39:       https://github.com/apple/swift-llvm-bindings/archive/refs/heads/swift/release/%{swift_llvm_bindings_version}.zip#/swift-llvm-bindings.zip
Source40:       https://github.com/apple/swift-foundation-icu/archive/refs/heads/release/%{swift_foundation_icu_version}.zip#/swift-foundation-icu.zip
Source41:       https://github.com/apple/swift-foundation/archive/refs/heads/release/%{swift_foundation_version}.zip#/swift-foundation.zip
Source42:       https://github.com/apple/swift-testing/archive/refs/tags/swift-%{swift_version}.tar.gz#/swift-testing.tar.gz
Source43:       https://github.com/madler/zlib/releases/download/v%{zlib_version}/zlib131.zip
Source44:       swiftlang.conf
Source45:       https://github.com/apple/swift-log/archive/refs/tags/%{swift_log_version}.tar.gz#/swift-log.tar.gz
Source46:       https://github.com/swiftlang/swift-toolchain-sqlite/archive/refs/tags/%{swift_toolchain_sqlite_version}.tar.gz#/swift-toolchain-sqlite.tar.gz

Patch1:         need_pic.patch
Patch2:         no_pipes.patch
Patch3:         enable_lzma.patch
Patch5:         remove_termio.diff
Patch6:         fix_chain_comparison.patch
Patch7:         disable_warning.patch
Patch8:         no_testable_package.patch
Patch9:         clang_crash_fix.patch
Patch10:        need_cstdint.patch
Patch11:        fix_foundation_cmath.patch

BuildRequires:  clang
BuildRequires:  swig
BuildRequires:  rsync
BuildRequires:  python3
BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
BuildRequires:  libxml2-devel
BuildRequires:  sqlite-devel
BuildRequires:  libcurl-devel
BuildRequires:  libuuid-devel
BuildRequires:  libedit-devel
BuildRequires:  perl-podlators
BuildRequires:  swiftlang
BuildRequires:  lld

Requires:       glibc-devel
Requires:       binutils-gold
Requires:       gcc

Recommends:     libstdc++-devel
Recommends:     gcc-c++

ExclusiveArch:  x86_64 aarch64 

Provides:       swiftlang = %{version}-%{release}

# https://bugzilla.redhat.com/show_bug.cgi?id=2291122
# (python3-swiftclient provides a program called "swift" 
# that clashes with the binary created by this package)
# This is currently for all versions, so we don't
# specify one
Conflicts:      python3-swiftclient


# Per https://bugzilla.redhat.com/show_bug.cgi?id=2324076 we
# need to exclude all of the LLVM libraries, basically everything
# we bundle, from being picked up by the RPM dependency 
# generator for "provides" (i.e. we don't want to have our
# version of liblldb.so found when someone is searching for 
# general version of LLDB).
%global __provides_exclude ^(libLTO[.]so.*|libclang_rt.*.so.*|liblldb[.]so.*)$
%global __requires_exclude ^(libLTO[.]so.*|libclang_rt.*.so.*|liblldb[.]so.*)$


%description
Swift is a general-purpose programming language built using 
a modern approach to safety, performance, and software design 
patterns.

The goal of the Swift project is to create the best available 
language for uses ranging from systems programming, to mobile 
and desktop apps, scaling up to cloud services. Most 
importantly, Swift is designed to make writing and maintaining 
correct programs easier for the developer. 


%prep
%setup -q -c -n %{swift_source_location} -a 0 -a 1 -a 2 -a 3 -a 4 -a 5 -a 6 -a 7 -a 8 -a 9 -a 10 -a 11 -a 12 -a 13 -a 14 -a 15 -a 16 -a 17 -a 18 -a 19 -a 20 -a 21 -a 22 -a 23 -a 24 -a 25 -a 26 -a 27 -a 28 -a 29 -a 30 -a 31 -a 32 -a 33 -a 34 -a 35 -a 36 -a 37 -a 38 -a 39 -a 40 -a 41 -a 42 -a 43 -a 45 -a 46
# The Swift build script requires directories to be named
# in a specific way so renaming the source directories is
# necessary
mv swift-cmark-swift-%{swift_version} cmark
mv swift-testing-swift-%{swift_version} swift-testing
mv swift-corelibs-foundation-swift-%{swift_version} swift-corelibs-foundation
mv swift-corelibs-libdispatch-swift-%{swift_version} swift-corelibs-libdispatch
mv swift-corelibs-xctest-swift-%{swift_version} swift-corelibs-xctest
mv swift-integration-tests-swift-%{swift_version} swift-integration-tests
mv swift-llbuild-swift-%{swift_version} llbuild
mv swift-package-manager-swift-%{swift_version} swiftpm
mv swift-swift-%{swift_version} swift
mv swift-xcode-playground-support-swift-%{swift_version} swift-xcode-playground-support
mv sourcekit-lsp-swift-%{swift_version} sourcekit-lsp
mv indexstore-db-swift-%{swift_version} indexstore-db
mv llvm-project-swift-%{swift_version} llvm-project
mv swift-syntax-swift-%{swift_version} swift-syntax
mv swift-tools-support-core-swift-%{swift_version} swift-tools-support-core
mv swift-argument-parser-%{swift_argument_parser_version} swift-argument-parser
mv swift-driver-swift-%{swift_version} swift-driver
mv swift-crypto-%{swift_crypto_version} swift-crypto
mv CMake-%{cmake_version} cmake
mv swift-atomics-%{swift_atomics_version} swift-atomics
mv swift-docc-swift-%{swift_version} swift-docc
mv swift-docc-render-artifact-swift-%{swift_version} swift-docc-render-artifact
mv swift-docc-symbolkit-swift-%{swift_version} swift-docc-symbolkit
mv swift-collections-%{swift_collections_version} swift-collections
mv swift-numerics-%{swift_numerics_version} swift-numerics
mv swift-system-%{swift_system_version} swift-system
mv swift-nio-%{swift_nio_version} swift-nio
mv swift-format-release-%{swift_format_version} swift-format
mv swift-lmdb-swift-%{swift_version} swift-lmdb
mv swift-markdown-swift-%{swift_version} swift-markdown
mv swift-stress-tester-swift-%{swift_version} swift-stress-tester
mv swift-experimental-string-processing-swift-%{swift_version} swift-experimental-string-processing
mv swift-certificates-%{swift_certificates_version} swift-certificates
mv swift-asn1-%{swift_asn1_version} swift-asn1
mv swift-llvm-bindings-swift-release-%{swift_llvm_bindings_version} swift-llvm-bindings
mv swift-foundation-icu-release-%{swift_foundation_icu_version} swift-foundation-icu
mv swift-foundation-release-%{swift_foundation_version} swift-foundation
mv swift-sdk-generator-swift-%{swift_sdk_generator_version}-RELEASE swift-sdk-generator
mv swift-async-algorithms-%{swift_async_algorithms_version} swift-async-algorithms
mv swift-log-%{swift_log_version} swift-log
mv swift-toolchain-sqlite-%{swift_toolchain_sqlite_version} swift-toolchain-sqlite

# Yams
mv Yams-%{yams_version} yams

# Ninja
mv ninja-%{ninja_version} ninja

# WasmKit
mv WasmKit-%{wasmkit_version} wasmkit
mv wasi-libc-wasi-sdk-%{wasi_version} wasi-libc

# zlib
mv zlib-%{zlib_version} zlib

# Fix python to python3 
%py3_shebang_fix swift/utils/api_checker/swift-api-checker.py
%py3_shebang_fix llvm-project/compiler-rt/lib/hwasan/scripts/hwasan_symbolize

# Enable PIC for cmark
%patch -P1 -p0

# Pipes has been removed in Python
%patch -P2 -p0

# Enable LZMA
%patch -P3 -p0

# Remove references to obsolete termio struct
%patch -P5 -p0

# Fix a chained comparison discrepancy
%patch -P6 -p0

# disable warning treated as error in libdispatch
%patch -P7 -p0

# Disable integration tests as they are causing the packaging
# to fail (after Swift has been successfully built)
%patch -P8 -p0

# The clang compiler crashes on Fedora 42 and Rawhide
# on x86_64 on a particular file
%if 0%{?fedora} >= 42 
%ifarch x86_64 
%patch -P9 -p0
%endif
%endif

# Explicitly include <cstdint> for int64
%patch -P10 -p0

# Fix C/C++ math header conflicts in Foundation
%patch -P11 -p0


%build
export VERBOSE=1
# Here we go!
swift/utils/build-script --preset=buildbot_linux,no_test skip-early-swiftsyntax=true install_destdir=%{_builddir} installable_package=%{_builddir}/swift-%{version}-%{linux_version}.tar.gz


%install
mkdir -p %{buildroot}%{_libexecdir}/swift/%{package_version}
cp -r %{_builddir}/usr/* %{buildroot}%{_libexecdir}/swift/%{package_version}
mkdir -p %{buildroot}%{_bindir}
ln -fs %{_libexecdir}/swift/%{package_version}/bin/swift %{buildroot}%{_bindir}/swift
ln -fs %{_libexecdir}/swift/%{package_version}/bin/swiftc %{buildroot}%{_bindir}/swiftc
ln -fs %{_libexecdir}/swift/%{package_version}/bin/swift-build %{buildroot}%{_bindir}/swift-build
ln -fs %{_libexecdir}/swift/%{package_version}/bin/swift-run %{buildroot}%{_bindir}/swift-run
ln -fs %{_libexecdir}/swift/%{package_version}/bin/sourcekit-lsp %{buildroot}%{_bindir}/sourcekit-lsp
mkdir -p %{buildroot}%{_mandir}/man1
cp %{_builddir}/usr/share/man/man1/swift.1 %{buildroot}%{_mandir}/man1/swift.1
mkdir -p %{buildroot}/usr/lib
ln -fs %{_libexecdir}/swift/%{package_version}/lib/swift %{buildroot}/usr/lib/swift
mkdir -p %{buildroot}%{_libdir}
ln -fs %{_libexecdir}/swift/%{package_version}/lib/libIndexStore.so %{buildroot}%{_libdir}/
ln -fs %{_libexecdir}/swift/%{package_version}/lib/libIndexStore.so.17 %{buildroot}%{_libdir}/
ln -fs %{_libexecdir}/swift/%{package_version}/lib/libsourcekitdInProc.so %{buildroot}%{_libdir}/
ln -fs %{_libexecdir}/swift/%{package_version}/lib/libswiftDemangle.so %{buildroot}%{_libdir}/
mkdir -p %{buildroot}/%{_sysconfdir}/ld.so.conf.d/
install -m 0644 %{SOURCE44} %{buildroot}/%{_sysconfdir}/ld.so.conf.d/swiftlang.conf


# This is to fix an issue with check-rpaths complaining about
# how the Swift binaries use RPATH
export QA_SKIP_RPATHS=1


%files
%license swift/LICENSE.txt
%{_bindir}/swift
%{_bindir}/swiftc
%{_bindir}/swift-build
%{_bindir}/swift-run
%{_bindir}/sourcekit-lsp
%{_mandir}/man1/swift.1.gz
%{_libexecdir}/swift/
%{_usr}/lib/swift
%{_libdir}/libIndexStore.so*
%{_libdir}/libsourcekitdInProc.so
%{_libdir}/libswiftDemangle.so
%{_sysconfdir}/ld.so.conf.d/swiftlang.conf


%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig


%changelog
%autochangelog
