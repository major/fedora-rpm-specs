
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

# Fix python to python3 
%py3_shebang_fix swift/utils/api_checker/swift-api-checker.py
%py3_shebang_fix llvm-project/compiler-rt/lib/hwasan/scripts/hwasan_symbolize

# Build wasmkit using current swift-tools-version
sed -i 's/swift-tools-version:999.0.0/swift-tools-version:6.1.3/' wasmkit/Package@swift-6.1.swift

%global buildsubdir %{nil}
%build
# Work around broken symlink in BuildRequires swiftlang by ensuring PATH finds the versioned swift
export PATH=%{_libexecdir}/swift/%{version}/bin:$PATH
export VERBOSE=1
%{builddir}/swift/utils/build-script --preset=buildbot_linux,no_test \
    skip-early-swiftsyntax=true \
    install_destdir=%{_builddir} \
    installable_package=%{_builddir}/swift-%{version}-f%{fedora}.tar.gz


%install
mkdir -p %{buildroot}%{_libexecdir}/swift/%{version}
cp -r %{_builddir}/usr/* %{buildroot}%{_libexecdir}/swift/%{version}
mkdir -p %{buildroot}%{_bindir}
ln -fs %{_libexecdir}/swift/%{version}/bin/swift %{buildroot}%{_bindir}/swift
ln -fs %{_libexecdir}/swift/%{version}/bin/swiftc %{buildroot}%{_bindir}/swiftc
ln -fs %{_libexecdir}/swift/%{version}/bin/swift-build %{buildroot}%{_bindir}/swift-build
ln -fs %{_libexecdir}/swift/%{version}/bin/swift-run %{buildroot}%{_bindir}/swift-run
ln -fs %{_libexecdir}/swift/%{version}/bin/sourcekit-lsp %{buildroot}%{_bindir}/sourcekit-lsp
mkdir -p %{buildroot}%{_mandir}/man1
cp %{_builddir}/usr/share/man/man1/swift.1 %{buildroot}%{_mandir}/man1/swift.1
mkdir -p %{buildroot}/usr/lib
ln -fs %{_libexecdir}/swift/%{version}/lib/swift %{buildroot}/usr/lib/swift
mkdir -p %{buildroot}%{_libdir}
ln -fs %{_libexecdir}/swift/%{version}/lib/libIndexStore.so %{buildroot}%{_libdir}/
ln -fs %{_libexecdir}/swift/%{version}/lib/libIndexStore.so.17 %{buildroot}%{_libdir}/
ln -fs %{_libexecdir}/swift/%{version}/lib/libsourcekitdInProc.so %{buildroot}%{_libdir}/
ln -fs %{_libexecdir}/swift/%{version}/lib/libswiftDemangle.so %{buildroot}%{_libdir}/
mkdir -p %{buildroot}%{_includedir}/swift
cp -r %{_builddir}/swift/include/swift/SwiftDemangle %{buildroot}%{_includedir}/swift/
mkdir -p %{buildroot}/%{_sysconfdir}/ld.so.conf.d/
install -m 0644 %{SOURCE99} %{buildroot}/%{_sysconfdir}/ld.so.conf.d/swiftlang.conf


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
%{_includedir}/swift/
%{_sysconfdir}/ld.so.conf.d/swiftlang.conf


%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig


%changelog
%autochangelog
