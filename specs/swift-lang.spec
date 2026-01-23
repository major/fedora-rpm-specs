
%if 0%{?fedora} >= 41
# on Fedora >= 41
%undefine __brp_add_determinism
%endif
%global debug_package %{nil}
%undefine _auto_set_build_flags

Version: 6.2

# Main swift source and version
%global forgeurl0  https://github.com/swiftlang/swift
%global version0   %{version}
%global tag0       swift-%{version0}-RELEASE
%global subdir0    swift

# Begin forge sources
%global forgeurl1  https://github.com/apple/swift-atomics
%global tag1       1.2.0
%global subdir1    swift-atomics

%global forgeurl2  https://github.com/swiftlang/sourcekit-lsp
%global tag2       swift-%{version0}-RELEASE
%global subdir2    sourcekit-lsp

%global forgeurl3  https://github.com/swiftlang/swift-corelibs-xctest
%global tag3       swift-%{version0}-RELEASE
%global subdir3    swift-corelibs-xctest

%global forgeurl4  https://github.com/apple/swift-log
%global tag4       1.5.4
%global subdir4    swift-log

%global forgeurl5  https://github.com/swiftlang/swift-llbuild
%global tag5       swift-%{version0}-RELEASE
%global subdir5    llbuild

%global forgeurl6  https://github.com/swiftlang/swift-corelibs-foundation
%global tag6       swift-%{version0}-RELEASE
%global subdir6    swift-corelibs-foundation

%global forgeurl7  https://github.com/swiftlang/swift-package-manager
%global tag7       swift-%{version0}-RELEASE
%global subdir7    swiftpm

%global forgeurl8  https://github.com/swiftlang/swift-lmdb
%global tag8       swift-%{version0}-RELEASE
%global subdir8    swift-lmdb

%global forgeurl9  https://github.com/KitWare/CMake
%global tag9       v3.30.2
%global subdir9    cmake

%global forgeurl10  https://github.com/apple/swift-collections
%global tag10       1.1.3
%global subdir10    swift-collections

%global forgeurl11  https://github.com/swiftlang/swift-driver
%global tag11       swift-%{version0}-RELEASE
%global subdir11    swift-driver

%global forgeurl12  https://github.com/swiftlang/swift-docc-symbolkit
%global tag12       swift-%{version0}-RELEASE
%global subdir12    swift-docc-symbolkit

%global forgeurl13  https://github.com/swiftlang/swift-foundation
%global tag13       swift-%{version0}-RELEASE
%global subdir13    swift-foundation

%global forgeurl14  https://github.com/microsoft/mimalloc
%global tag14       v3.0.1
%global subdir14    mimalloc

%global forgeurl15  https://github.com/swiftlang/swift-cmark
%global tag15       gfm
%global subdir15    cmark

%global forgeurl16  https://github.com/gnome/libxml2
%global tag16       v2.11.5
%global subdir16    libxml2

%global forgeurl17  https://github.com/swiftlang/swift-toolchain-sqlite
%global tag17       1.0.1
%global subdir17    swift-toolchain-sqlite

%global forgeurl18  https://github.com/WebAssembly/wasi-libc
%global tag18       wasi-sdk-24
%global subdir18    wasi-libc

%global forgeurl19  https://github.com/swiftlang/swift-format
%global tag19       swift-%{version0}-RELEASE
%global subdir19    swift-format

%global forgeurl20  https://github.com/apple/swift-argument-parser
%global tag20       1.4.0
%global subdir20    swift-argument-parser

%global forgeurl21  https://github.com/swiftlang/swift-llvm-bindings
%global tag21       swift-%{version0}-RELEASE
%global subdir21    swift-llvm-bindings

%global forgeurl22  https://github.com/swiftwasm/WasmKit
%global tag22       0.1.2
%global subdir22    wasmkit

%global forgeurl23  https://github.com/swiftlang/swift-syntax
%global tag23       swift-%{version0}-RELEASE
%global subdir23    swift-syntax

%global forgeurl24  https://github.com/ninja-build/ninja
%global tag24       v1.11.1
%global subdir24    ninja

%global forgeurl25  https://github.com/swiftlang/swift-corelibs-libdispatch
%global tag25       swift-%{version0}-RELEASE
%global subdir25    swift-corelibs-libdispatch

%global forgeurl26  https://github.com/swiftlang/swift-markdown
%global tag26       swift-%{version0}-RELEASE
%global subdir26    swift-markdown

%global forgeurl27  https://github.com/swiftlang/swift-foundation-icu
%global tag27       swift-%{version0}-RELEASE
%global subdir27    swift-foundation-icu

%global forgeurl28  https://github.com/madler/zlib
%global tag28       v1.3.1
%global subdir28    zlib

%global forgeurl29  https://github.com/apple/swift-system
%global tag29       1.5.0
%global subdir29    swift-system

%global forgeurl30  https://github.com/apple/swift-asn1
%global tag30       1.0.0
%global subdir30    swift-asn1

%global forgeurl31  https://github.com/swiftlang/swift-tools-support-core
%global tag31       swift-%{version0}-RELEASE
%global subdir31    swift-tools-support-core

%global forgeurl32  https://github.com/swiftlang/swift-stress-tester
%global tag32       swift-%{version0}-RELEASE
%global subdir32    swift-stress-tester

%global forgeurl33  https://github.com/apple/swift-nio
%global tag33       2.65.0
%global subdir33    swift-nio

%global forgeurl34  https://github.com/swiftlang/indexstore-db
%global tag34       swift-%{version0}-RELEASE
%global subdir34    indexstore-db

%global forgeurl35  https://github.com/swiftlang/swift-build
%global tag35       swift-%{version0}-RELEASE
%global subdir35    swift-build

%global forgeurl36  https://github.com/apple/swift-certificates
%global tag36       1.0.1
%global subdir36    swift-certificates

%global forgeurl37  https://github.com/swiftlang/swift-installer-scripts
%global tag37       swift-%{version0}-RELEASE
%global subdir37    swift-installer-scripts

%global forgeurl38  https://github.com/swiftlang/swift-testing
%global tag38       swift-%{version0}-RELEASE
%global subdir38    swift-testing

%global forgeurl39  https://github.com/swiftlang/swift-docc-render-artifact
%global tag39       swift-%{version0}-RELEASE
%global subdir39    swift-docc-render-artifact

%global forgeurl40  https://github.com/apple/swift-async-algorithms
%global tag40       1.0.1
%global subdir40    swift-async-algorithms

%global forgeurl41  https://github.com/swiftlang/swift-integration-tests
%global tag41       swift-%{version0}-RELEASE
%global subdir41    swift-integration-tests

%global forgeurl42  https://github.com/apple/swift-crypto
%global tag42       3.0.0
%global subdir42    swift-crypto

%global forgeurl43  https://github.com/swiftlang/swift-sdk-generator
%global tag43       swift-%{version0}-RELEASE
%global subdir43    swift-sdk-generator

%global forgeurl44  https://github.com/swiftlang/llvm-project
%global tag44       swift-%{version0}-RELEASE
%global subdir44    llvm-project

%global forgeurl45  https://github.com/curl/curl
%global tag45       curl-8_9_1
%global subdir45    curl

%global forgeurl46  https://github.com/apple/swift-xcode-playground-support
%global tag46       swift-%{version0}-RELEASE
%global subdir46    swift-xcode-playground-support

%global forgeurl47  https://github.com/swiftlang/swift-experimental-string-processing
%global tag47       swift-%{version0}-RELEASE
%global subdir47    swift-experimental-string-processing

%global forgeurl48  https://github.com/apple/swift-numerics
%global tag48       1.0.2
%global subdir48    swift-numerics

%global forgeurl49  https://github.com/swiftlang/swift-docc
%global tag49       swift-%{version0}-RELEASE
%global subdir49    swift-docc

# End forge sources

Name:           swift-lang
Release:        %autorelease
%forgemeta -a

Summary:        The Swift programming language
License:        Apache-2.0
URL:            https://www.swift.org

%{lua:
for i = 0, 49 do
  local forgesource = rpm.expand("%{?forgesource" .. i .. "}")
  if forgesource ~= "" then
    print("Source" .. i .. ":    " .. forgesource .. "\n")
  end
end
}
Source99:       swiftlang.conf
Source100:      fedora-presets.ini

# NOTE: The patch number corresponds to the source it's packaging. For example,
# Patch25 is patching Source25, swift-foundation.
Patch0:         swift.patch
Patch44:        llvm-project.patch
Patch15:        cmark.patch
Patch5:         llbuild.patch
Patch7:         swiftpm.patch
Patch13:        swift-foundation.patch
Patch25:        swift-corelibs-libdispatch.patch
Patch24:        ninja.patch
Patch9:         cmake.patch

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
BuildRequires:  lld
BuildRequires:  binutils-gold

Requires:       glibc-devel
Requires:       lld
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
%forgesetup -a
cd %{builddir}
%{lua:
for i = 0, 49 do
  local subdir = rpm.expand("%{?subdir" .. i .. "}")
  if subdir ~= "" then
    print(rpm.expand("mv %{archivename" .. i .. "} " .. subdir .. "\n"))
  end
end
}

%patch 0
%patch 44
%patch 15
%patch 5
%patch 7
%patch 13
%patch 25
%patch 24
%patch 9

# Install custom Fedora preset
cp %{SOURCE100} swift/utils/fedora-presets.ini

# Fix python to python3 
%py3_shebang_fix swift/utils/api_checker/swift-api-checker.py
%py3_shebang_fix llvm-project/compiler-rt/lib/hwasan/scripts/hwasan_symbolize

# Build wasmkit using current swift-tools-version
sed -i 's/swift-tools-version:999.0.0/swift-tools-version:6.1.3/' wasmkit/Package@swift-6.1.swift

%global buildsubdir %{nil}
%build
export VERBOSE=1

# Four-stage bootstrap to build Swift from scratch without external Swift compiler
# Stage 0: Build minimal Swift toolchain from C++ using gold linker
#          Produces: Swift compiler with C++ legacy driver (no SwiftPM, no swift-driver)
#          Stage 0 clang defaults to gold
# Stage 1: Rebuild Swift compiler using Stage 0 with gold linker
#          Produces: Swift compiler with macros support + Foundation + Dispatch
#          Stage 1 clang is compiled with lld as its default linker
# Stage 2: Build Swift compiler using Stage 1 with lld linker
#          Produces: Swift compiler + SwiftPM + basic tools (still no swift-driver)
#          Stage 2 clang defaults to lld
# Stage 3: Build final production toolchain using Stage 2
#          Produces: Complete toolchain with swift-driver, sourcekit-lsp, swift-format, etc.
#          This matches upstream first-party distributions

echo "=== Bootstrap Stage 0: Building minimal Swift from C++ ==="
%{builddir}/swift/utils/build-script --preset=bootstrap_stage0 \
    build_subdir=bootstrap_stage0 \
    install_destdir=%{_builddir}/stage0 \
    installable_package=%{_builddir}/swift-%{version}-stage0.tar.gz \
    extra-cmake-options="-DLLVM_USE_LINKER=gold -DCLANG_DEFAULT_LINKER=gold"

echo "=== Bootstrap Stage 1: Rebuilding Swift with Stage 0 ==="
export PATH=%{_builddir}/stage0/usr/bin:$PATH
%{builddir}/swift/utils/build-script --preset=bootstrap_stage1 \
    build_subdir=bootstrap_stage1 \
    install_destdir=%{_builddir}/stage1 \
    installable_package=%{_builddir}/swift-%{version}-stage1.tar.gz \
    extra-cmake-options="-DLLVM_USE_LINKER=gold -DCLANG_DEFAULT_LINKER=lld"

echo "=== Bootstrap Stage 2: Building toolchain with SwiftPM ==="
export PATH=%{_builddir}/stage1/usr/bin:%{_builddir}/stage0/usr/bin:$PATH
%{builddir}/swift/utils/build-script --preset=bootstrap_stage2 \
    build_subdir=bootstrap_stage2 \
    install_destdir=%{_builddir}/stage2 \
    installable_package=%{_builddir}/swift-%{version}-stage2.tar.gz \
    extra-cmake-options="-DLLVM_USE_LINKER=lld -DCLANG_DEFAULT_LINKER=lld"

echo "=== Stage 3: Building final production toolchain with swift-driver ==="
export PATH=%{_builddir}/stage2/usr/bin:%{_builddir}/stage1/usr/bin:%{_builddir}/stage0/usr/bin:$PATH
%{builddir}/swift/utils/build-script --preset=fedora_final \
    --preset-file=%{builddir}/swift/utils/fedora-presets.ini \
    build_subdir=fedora_final \
    install_destdir=%{_builddir} \
    installable_package=%{_builddir}/swift-%{version}-f%{fedora}.tar.gz \
    extra-cmake-options="-DLLVM_USE_LINKER=lld -DCLANG_DEFAULT_LINKER=lld -DCMAKE_EXE_LINKER_FLAGS=-Wl,-z,relro,-z,now -DCMAKE_SHARED_LINKER_FLAGS=-Wl,-z,relro,-z,now"


%install
# Create directory structure
mkdir -p %{buildroot}%{_bindir}
mkdir -p %{buildroot}%{_libdir}
mkdir -p %{buildroot}%{_libexecdir}/swift/%{version}/bin
mkdir -p %{buildroot}%{_libexecdir}/swift/%{version}/lib
mkdir -p %{buildroot}%{_libexecdir}/swift/%{version}/include
mkdir -p %{buildroot}%{_includedir}/swift
mkdir -p %{buildroot}%{_datadir}/swift
mkdir -p %{buildroot}%{_mandir}/man1
mkdir -p %{buildroot}%{_sysconfdir}/ld.so.conf.d

# Install executables to %{_libexecdir} to maintain Swift's internal directory structure
cp -a %{_builddir}/usr/bin/* %{buildroot}%{_libexecdir}/swift/%{version}/bin/

# Create symlinks in %{_bindir} for user-facing tools
TOOLS="swift swiftc swift-build swift-run swift-package swift-test sourcekit-lsp swift-format swift-demangle"
for tool in ${TOOLS}; do
    if [ -f %{buildroot}%{_libexecdir}/swift/%{version}/bin/$tool ]; then
        ln -sf %{_libexecdir}/swift/%{version}/bin/$tool %{buildroot}%{_bindir}/$tool
    fi
done

# Install Swift runtime libraries to %{_libdir}
if [ -d %{_builddir}/usr/lib/swift/linux ]; then
    for lib in %{_builddir}/usr/lib/swift/linux/*.so*; do
        [ -L "$lib" ] && continue  # Skip symlinks, we'll handle them later
        [ -f "$lib" ] && install -m 0755 "$lib" %{buildroot}%{_libdir}/
    done
    # Now create symlinks
    for link in %{_builddir}/usr/lib/swift/linux/*.so*; do
        [ -L "$link" ] || continue
        target=$(readlink "$link")
        linkname=$(basename "$link")
        ln -sf "$target" %{buildroot}%{_libdir}/$linkname
    done
fi

# Install libsourcekitdInProc.so from build directory to %%{_builddir}/usr/lib (it's not installed by CMake)
if [ -f %{_builddir}/build/fedora_final/swift-linux-%{_arch}/lib/libsourcekitdInProc.so ]; then
    cp -a %{_builddir}/build/fedora_final/swift-linux-%{_arch}/lib/libsourcekitdInProc.so %{_builddir}/usr/lib/
fi

# Install SourceKit/IndexStore public libraries
for lib in libIndexStore.so libIndexStore.so.17.0 libsourcekitdInProc.so libswiftDemangle.so; do
    if [ -f %{_builddir}/usr/lib/$lib ]; then
        install -m 0755 %{_builddir}/usr/lib/$lib %{buildroot}%{_libdir}/
    fi
done
# Create any missing version symlinks
if [ -f %{buildroot}%{_libdir}/libIndexStore.so.17.0 ] && [ ! -e %{buildroot}%{_libdir}/libIndexStore.so ]; then
    ln -sf libIndexStore.so.17.0 %{buildroot}%{_libdir}/libIndexStore.so
fi

# Install lldb libraries to %{_libexecdir} (private, bundled with Swift toolchain)
if [ -d %{_builddir}/usr/lib ]; then
    for lib in %{_builddir}/usr/lib/liblldb.so*; do
        if [ -e "$lib" ]; then
            mkdir -p %{buildroot}%{_libexecdir}/swift/%{version}/lib
            cp -a "$lib" %{buildroot}%{_libexecdir}/swift/%{version}/lib/
        fi
    done
fi

# Install lldb Python bindings
if [ -d %{_builddir}/usr/lib64/python%{python3_version}/site-packages/lldb ]; then
    mkdir -p %{buildroot}%{_libexecdir}/swift/%{version}/lib64/python%{python3_version}/site-packages
    cp -a %{_builddir}/usr/lib64/python%{python3_version}/site-packages/lldb \
          %{buildroot}%{_libexecdir}/swift/%{version}/lib64/python%{python3_version}/site-packages/
fi

# Install compiler private libraries and modules to %{_libexecdir}
mkdir -p %{buildroot}%{_libexecdir}/swift/%{version}/lib/swift
cp -a %{_builddir}/usr/lib/swift/* %{buildroot}%{_libexecdir}/swift/%{version}/lib/swift/
# Remove the runtime .so files we already installed to %{_libdir}
if [ -d %{buildroot}%{_libexecdir}/swift/%{version}/lib/swift/linux ]; then
    find %{buildroot}%{_libexecdir}/swift/%{version}/lib/swift/linux -name '*.so*' -type f -delete
    find %{buildroot}%{_libexecdir}/swift/%{version}/lib/swift/linux -name '*.so*' -type l -delete
fi

# Install clang resource directory (sanitizer libraries, builtins)
# Keep only what Swift needs internally
if [ -d %{_builddir}/usr/lib/clang ]; then
    mkdir -p %{buildroot}%{_libexecdir}/swift/%{version}/lib/clang
    cp -a %{_builddir}/usr/lib/clang/* %{buildroot}%{_libexecdir}/swift/%{version}/lib/clang/
fi

# Install SwiftDemangle headers (public API)
if [ -d %{_builddir}/swift/include/swift/SwiftDemangle ]; then
    cp -a %{_builddir}/swift/include/swift/SwiftDemangle %{buildroot}%{_includedir}/swift/
fi

# Install Swift headers and modulemaps (for C interop)
if [ -d %{_builddir}/usr/include ]; then
    cp -a %{_builddir}/usr/include/* %{buildroot}%{_libexecdir}/swift/%{version}/include/
fi

# Install data files
if [ -d %{_builddir}/usr/share/swift ]; then
    cp -a %{_builddir}/usr/share/swift/* %{buildroot}%{_datadir}/swift/
fi

# Install man pages
if [ -f %{_builddir}/usr/share/man/man1/swift.1 ]; then
    install -m 0644 %{_builddir}/usr/share/man/man1/swift.1 %{buildroot}%{_mandir}/man1/
fi

# Create compatibility symlink for module lookup
ln -sf %{_libexecdir}/swift/%{version}/lib/swift %{buildroot}%{_libdir}/swift

# Install ld.so.conf.d configuration
install -m 0644 %{SOURCE99} %{buildroot}%{_sysconfdir}/ld.so.conf.d/swiftlang.conf


# This is to fix an issue with check-rpaths complaining about
# how the Swift binaries use RPATH
export QA_SKIP_RPATHS=1


%files
%license swift/LICENSE.txt

# User-facing executables (symlinks to %%{_libexecdir}/swift/%%{version}/bin/)
%{_bindir}/swift
%{_bindir}/swiftc
%{_bindir}/swift-build
%{_bindir}/swift-run
%{_bindir}/swift-package
%{_bindir}/swift-test
%{_bindir}/sourcekit-lsp
%{_bindir}/swift-format
%{_bindir}/swift-demangle

# Man pages
%{_mandir}/man1/swift.1.gz

# Swift runtime libraries (what users link against)
%{_libdir}/libswift*.so*
%{_libdir}/libFoundation*.so*
%{_libdir}/libdispatch.so*
%{_libdir}/libBlocksRuntime.so*
%{_libdir}/libTesting.so*
%{_libdir}/libXCTest.so*
%{_libdir}/lib_*.so*

# SourceKit/IndexStore public libraries
%{_libdir}/libIndexStore.so*
%{_libdir}/libsourcekitdInProc.so*
%{_libdir}/libswiftDemangle.so*

# Compatibility symlink for module lookup
%{_libdir}/swift

# Backend tools and compiler internals
%{_libexecdir}/swift/

# Public headers
%{_includedir}/swift/

# Data files (diagnostics, features.json, etc.)
%{_datadir}/swift/

# Dynamic linker configuration
%{_sysconfdir}/ld.so.conf.d/swiftlang.conf


%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig


%changelog
%autochangelog
