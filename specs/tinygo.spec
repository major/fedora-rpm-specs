%bcond check 1
# I'm not sure what this is for, as no tests seem to use it, and it introduces
# some weird license that needs review.
%bcond wasi_cli 0

%global __brp_strip_lto %{nil}
%global __brp_strip_static_archive %{nil}

# https://github.com/tinygo-org/tinygo
%global goipath         github.com/tinygo-org/tinygo
Version:                0.38.0

%global CMSIS_commit          9fe411cef1cef5de58e5957b89760759de44e393
%global avr_commit            6624554c02b237b23dc17d53e992bf54033fc228
%global bdwgc_commit          1166f11f7dee08d7ad369296b24cf8c9582f8789
%global clang_llvm_version    19
%global cmsis_svd_data_commit 05a9562ec59b87945a8d7177a4b08b7aa2f2fd58
%global compiler_rt_version   %{clang_llvm_version}.1.7
%global macos_minsdk_commit   e7c72156eac3ebf29c34cc2faa71efcb1296663f
%global mingw64_commit        8526cb618269440a94810b94b77f8bd48c5c3396
%global musl_version          1.2.3
%global net_commit            c134160ae47d38b468b1c5ade43e78ad5a1e616d
%global nrfx_commit           d779b49fc59c7a165e7da1d7cd7d57b28a059f16
%global picolibc_commit       b92edfda8ac6853772d87cadaeeeaa21b78609b6
%global wasi_libc_version     20
%global wasi_libc_tag         wasi-sdk-%{wasi_libc_version}
%global wasi_cli_version      0.2.0

# No longer matching regular Go's /usr/share/gocode because it also provides
# pre-compiled binaries, and symlinks to arch-specific clang headers.
%global tinygoroot %{_libdir}/tinygo

%gometa

%global common_description %{expand:
Go compiler for small places. Microcontrollers, WebAssembly, and command-line
tools. Based on LLVM.}

Name:           tinygo
Release:        %autorelease
Summary:        Go compiler for small places

# Main files: BSD-3-Clause
# builder/cc1as.*: Apache-2.0 WITH LLVM-exception
# corpus_test.go: MIT
# CMSIS: BSD-3-Clause (subsetted)
# avr-mcu: Apache-2.0 (packs) AND MIT (Rust code, unused by this package)
# cmsis-svd: Apache-2.0 AND (Apache-2.0 OR MIT) AND BSD-3-Clause AND BSD-Source-Code AND ISC AND MIT (subsetted)
# compiler-rt: Apache-2.0 WITH LLVM-exception OR NCSA OR MIT
# macos-minimal-sdk: APSL-2.0 AND BSD-2-Clause AND BSD-3-Clause AND BSD-4-Clause AND BSD-4-Clause-UC AND ISC AND LicenseRef-Fedora-Public-Domain
# musl: MIT
# net: BSD-2-Clause
# nrfx: BSD-3-Clause AND Apache-2.0
# picolibc: BSD-2-Clause AND BSD-2-Clause-FreeBSD AND BSD-3-Clause AND ISC AND SMLNJ AND Spencer-94 AND GPLv2 (testing code only, unused by this package)
# wasi-libc: Apache-2.0 WITH LLVM-exception AND Apache-2.0 AND MIT AND BSD-2-Clause AND CC0-1.0 (dlmalloc implementation, unused by this package)
License:        %{shrink: BSD-3-Clause AND Apache-2.0 WITH LLVM-exception AND BSD-2-Clause AND MIT AND
                Apache-2.0 AND
                (Apache-2.0 OR MIT) AND BSD-Source-Code AND ISC AND
                (Apache-2.0 WITH LLVM-exception OR NCSA OR MIT) AND
                APSL-2.0 AND BSD-2-Clause AND BSD-4-Clause AND BSD-4-Clause-UC AND LicenseRef-Fedora-Public-Domain AND
                BSD-2-Clause-FreeBSD AND SMLNJ AND Spencer-94}
URL:            %{gourl}
Source0:        %{gosource}
Source1:        clean_tarballs.sh
Source2:        cmsis-%{CMSIS_commit}-clean.tar.xz
Source3:        https://github.com/avr-rust/avr-mcu/archive/%{avr_commit}/avr-%{avr_commit}.tar.gz
Source4:        cmsis_svd_data-%{cmsis_svd_data_commit}-clean.tar.xz
Source50:       https://github.com/llvm/llvm-project/releases/download/llvmorg-%{compiler_rt_version}/compiler-rt-%{compiler_rt_version}.src.tar.xz
Source51:       https://github.com/llvm/llvm-project/releases/download/llvmorg-%{compiler_rt_version}/compiler-rt-%{compiler_rt_version}.src.tar.xz.sig
Source52:       https://src.fedoraproject.org/rpms/compiler-rt/raw/f8e98d51f0c3fdbaa9ce5d99816930e4fcbe504b/f/release-keys.asc#/compiler-rt-release-keys.asc
Source60:       https://musl.libc.org/releases/musl-%{musl_version}.tar.gz
Source61:       https://musl.libc.org/releases/musl-%{musl_version}.tar.gz.asc
Source62:       https://musl.libc.org/musl.pub
Source7:        https://github.com/aykevl/macos-minimal-sdk/archive/%{macos_minsdk_commit}/macos-minimal-sdk-%{macos_minsdk_commit}.tar.gz
Source8:        https://github.com/NordicSemiconductor/nrfx/archive/%{nrfx_commit}/nrfx-%{nrfx_commit}.tar.gz
Source9:        https://github.com/keith-packard/picolibc/archive/%{picolibc_commit}/picolibc-%{picolibc_commit}.tar.gz
Source10:       https://github.com/WebAssembly/wasi-libc/archive/%{wasi_libc_tag}/wasi-libc-%{wasi_libc_tag}.tar.gz
Source11:       https://github.com/mingw-w64/mingw-w64/archive/%{mingw64_commit}/mingw64-%{mingw64_commit}.tar.gz
Source12:       https://github.com/tinygo-org/net/archive/%{net_commit}/net-%{net_commit}.tar.gz
%if %{with wasi_cli}
Source13:       https://github.com/WebAssembly/wasi-cli/archive/v%{wasi_cli_version}/wasi-cli-%{wasi_cli_version}.tar.gz
%endif
Source14:       https://github.com/ivmai/bdwgc/archive/%{bdwgc_commit}/bdwgc-%{bdwgc_commit}.tar.gz

#
# Unnumbered patches are applied to the main source tree.
# Patches that are 1X00-1X99 are applied to the subdirectory for source X.
#

# We don't have wasmtime to run these.
Patch:          0001-Skip-WASI-tests.patch
# We set GO111MODULE=off during tests, so can't run a few of them.
Patch:          0002-Skip-tests-that-require-Go-module-mode.patch
# Better search paths for non-default LLVM.
Patch:          0003-Set-LLVM-search-paths-for-Fedora.patch
# We can't include these due to poor licensing.
# https://github.com/tinygo-org/tinygo/pull/4962
Patch:          0004-Add-flag-to-skip-Renesas-SVD-builds.patch
#https://github.com/tinygo-org/tinygo/pull/4677
Patch:          0005-Normalize-expected-path-for-chdir-tests.patch
# https://github.com/tinygo-org/tinygo/pull/4958
Patch:          https://github.com/tinygo-org/tinygo/commit/1b5d312c689a004434cb77f161f65b9615c98036.patch
# https://github.com/tinygo-org/tinygo/issues/4969
Patch:          0006-Skip-x86-tests-on-ARM.patch

# Fix CVE-2025-26519 in musl.
Patch1600:      https://www.openwall.com/lists/musl/2025/02/13/1/1#/musl-cve-2025-26519-1.patch
Patch1601:      https://www.openwall.com/lists/musl/2025/02/13/1/2#/musl-cve-2025-26519-2.patch

# Not supported upstream yet.
ExcludeArch:    ppc64le s390x
# https://fedoraproject.org/wiki/Changes/EncourageI686LeafRemoval
ExcludeArch:    %{ix86}

BuildRequires:  clang-devel(major) = %{clang_llvm_version}
BuildRequires:  golang(github.com/aykevl/go-wasm)
BuildRequires:  golang(github.com/blakesmith/ar)
BuildRequires:  chromium
BuildRequires:  golang(github.com/chromedp/chromedp) >= 0.7.6
BuildRequires:  golang(github.com/chromedp/cdproto/cdp)
BuildRequires:  golang(github.com/gofrs/flock) >= 0.8.1
BuildRequires:  golang(github.com/google/shlex)
BuildRequires:  golang(github.com/inhies/go-bytesize)
BuildRequires:  golang(github.com/marcinbor85/gohex)
BuildRequires:  golang(github.com/mattn/go-colorable) >= 0.1.13
BuildRequires:  golang(github.com/mattn/go-tty) >= 0.0.4
BuildRequires:  golang(github.com/tetratelabs/wazero) >= 1.6
BuildRequires:  golang(golang.org/x/net/http/httpguts) >= 0.35
BuildRequires:  golang(github.com/sigurn/crc16)
BuildRequires:  golang(go.bug.st/serial) >= 1.6.0
BuildRequires:  golang(golang.org/x/tools/go/ast/astutil)
BuildRequires:  golang(golang.org/x/tools/go/ssa) >= 0.30
BuildRequires:  golang(gopkg.in/yaml.v2) >= 2.4.0
BuildRequires:  golang(tinygo.org/x/go-llvm)
BuildRequires:  golang-tests
BuildRequires:  llvm-devel(major) = %{clang_llvm_version}
BuildRequires:  make

BuildRequires:  binaryen >= 116
# We don't have glibc for arm, so skip these.
#BuildRequires:  gcc-arm-linux-gnu
#BuildRequires:  gcc-aarch64-linux-gnu
BuildRequires:  lld(major) = %{clang_llvm_version}
# BuildRequires:  mingw64-crt
# BuildRequires:  mingw64-headers
BuildRequires:  nodejs >= 18
BuildRequires:  qemu-system-arm-core
BuildRequires:  qemu-system-riscv-core
BuildRequires:  qemu-user

# For GPG signature verification
BuildRequires:  gnupg2

Requires:       clang(major) = %{clang_llvm_version}
Requires:       golang
Requires:       lld(major) = %{clang_llvm_version}
# Add this when LLVM supports ESP natively.
# Recommends:     esptool
# Recommends:     mingw64-crt
# Recommends:     mingw64-headers
Recommends:     qemu-system-arm-core
Recommends:     qemu-system-riscv-core
Recommends:     qemu-user

# Make note of bundled libc's
Provides:       bundled(bdwgc) = %{bdwgc_commit}
Provides:       bundled(gc) = %{bdwgc_commit}
Provides:       bundled(compiler-rt) = %{compiler_rt_version}
Provides:       bundled(musl) = %{musl_version}
Provides:       bundled(picolibc) = %{picolibc_commit}
Provides:       bundled(wasi-libc) = %{wasi_libc_version}

%description
%{common_description}


%prep
%goprep
%autopatch -q -p1 -M 999

tar -C lib -xf %{SOURCE2}
rmdir lib/CMSIS
mv lib/CMSIS-%{CMSIS_commit} lib/CMSIS
pushd lib/CMSIS
%autopatch -q -p1 -m 1200 -M 1299
popd

tar -C lib -xf %{SOURCE3}
rmdir lib/avr
mv lib/avr-mcu-%{avr_commit} lib/avr
pushd lib/avr
%autopatch -q -p1 -m 1300 -M 1399
popd

tar -C lib -xf %{SOURCE4}
rmdir lib/cmsis-svd
mv lib/cmsis-svd-data-%{cmsis_svd_data_commit} lib/cmsis-svd
pushd lib/cmsis-svd
%autopatch -q -p1 -m 1400 -M 1499
popd

# Verify *before* actually unpacking!
%{gpgverify} --keyring='%{SOURCE52}' --signature='%{SOURCE51}' --data='%{SOURCE50}'
tar -C lib -xf %{SOURCE50}
mv lib/compiler-rt-%{compiler_rt_version}.src/lib/builtins lib/compiler-rt-builtins
mv lib/compiler-rt-%{compiler_rt_version}.src/README.txt lib/compiler-rt-builtins/
mv lib/compiler-rt-%{compiler_rt_version}.src/LICENSE.TXT lib/compiler-rt-builtins/
pushd lib/compiler-rt-builtins
%autopatch -q -p1 -m 1500 -M 1599
popd

# Verify *before* actually unpacking!
%{gpgverify} --keyring='%{SOURCE62}' --signature='%{SOURCE61}' --data='%{SOURCE60}'
tar -C lib -xf %{SOURCE60}
rmdir lib/musl
mv lib/musl-%{musl_version} lib/musl
pushd lib/musl
%autopatch -q -p1 -m 1600 -M 1699
popd

tar -C lib -xf %{SOURCE7}
rmdir lib/macos-minimal-sdk
mv lib/macos-minimal-sdk-%{macos_minsdk_commit} lib/macos-minimal-sdk
pushd lib/macos-minimal-sdk
%autopatch -q -p1 -m 1700 -M 1799
popd

tar -C lib -xf %{SOURCE8}
rmdir lib/nrfx
mv lib/nrfx-%{nrfx_commit} lib/nrfx
rm lib/nrfx/.gitignore
chmod -x lib/nrfx/doc/generate_html_doc.sh
pushd lib/nrfx
%autopatch -q -p1 -m 1800 -M 1899
popd

tar -C lib -xf %{SOURCE9}
rmdir lib/picolibc
mv lib/picolibc-%{picolibc_commit} lib/picolibc
pushd lib/picolibc
%autopatch -q -p1 -m 1900 -M 1999
popd

tar -C lib -xf %{SOURCE10}
rmdir lib/wasi-libc
mv lib/wasi-libc-%{wasi_libc_tag} lib/wasi-libc
pushd lib/wasi-libc
%autopatch -q -p1 -m 11000 -M 11099
popd

tar -C lib -xf %{SOURCE11}
rmdir lib/mingw-w64
mv lib/mingw-w64-%{mingw64_commit} lib/mingw-w64
pushd lib/mingw-w64
%autopatch -q -p1 -m 11100 -M 11199
popd

tar -C src -xf %{SOURCE12}
rmdir src/net
mv src/net-%{net_commit} src/net
pushd src/net
%autopatch -q -p1 -m 11200 -M 11299
popd

%if %{with wasi_cli}
tar -C lib -xf %{SOURCE13}
rmdir lib/wasi-cli
mv lib/wasi-cli-%{wasi_cli_version} lib/wasi-cli
pushd lib/wasi-cli
%autopatch -q -p1 -m 11300 -M 11399
popd
%endif

tar -C lib -xf %{SOURCE14}
rmdir lib/bdwgc
mv lib/bdwgc-%{bdwgc_commit} lib/bdwgc
pushd lib/bdwgc
%autopatch -q -p1 -m 11400 -M 11499
popd

%build
export GO_BUILDTAGS="llvm%{clang_llvm_version}" GO_LDFLAGS="-X github.com/tinygo-org/tinygo/goenv.TINYGOROOT=%{tinygoroot} "
%gobuild -o %{gobuilddir}/bin/tinygo %{goipath}
GO111MODULE=off %make_build gen-device RENESAS=0 STM32=0


%install
install -vdm 0755                     %{buildroot}%{_bindir}
install -vpm 0755 %{gobuilddir}/bin/* %{buildroot}%{_bindir}/

install -vdm 0755 %{buildroot}%{tinygoroot}
install -vdm 0755 %{buildroot}%{tinygoroot}/lib
install -vdm 0755 %{buildroot}%{tinygoroot}/lib/bdwgc
cp -rp lib/bdwgc/* %{buildroot}%{tinygoroot}/lib/bdwgc
install -vdm 0755 %{buildroot}%{tinygoroot}/lib/CMSIS
install -vpm 0644 lib/CMSIS/README.md %{buildroot}%{tinygoroot}/lib/CMSIS/
install -vdm 0755 %{buildroot}%{tinygoroot}/lib/CMSIS/CMSIS/Include
install -vpm 0644 lib/CMSIS/CMSIS/Include/* %{buildroot}%{tinygoroot}/lib/CMSIS/CMSIS/Include/
cp -rp lib/compiler-rt-builtins %{buildroot}%{tinygoroot}/lib
install -vdm 0755 %{buildroot}%{tinygoroot}/lib/macos-minimal-sdk
cp -rp lib/macos-minimal-sdk/* %{buildroot}%{tinygoroot}/lib/macos-minimal-sdk
install -vdm 0755 %{buildroot}%{tinygoroot}/lib/mingw-w64/mingw-w64-crt
cp -rp lib/mingw-w64/mingw-w64-crt/def-include %{buildroot}%{tinygoroot}/lib/mingw-w64/mingw-w64-crt
cp -rp lib/mingw-w64/mingw-w64-crt/gdtoa %{buildroot}%{tinygoroot}/lib/mingw-w64/mingw-w64-crt
cp -rp lib/mingw-w64/mingw-w64-crt/include %{buildroot}%{tinygoroot}/lib/mingw-w64/mingw-w64-crt
cp -rp lib/mingw-w64/mingw-w64-crt/misc %{buildroot}%{tinygoroot}/lib/mingw-w64/mingw-w64-crt
cp -rp lib/mingw-w64/mingw-w64-crt/stdio %{buildroot}%{tinygoroot}/lib/mingw-w64/mingw-w64-crt
install -vdm 0755 %{buildroot}%{tinygoroot}/lib/mingw-w64/mingw-w64-crt/crt
cp -rp lib/mingw-w64/mingw-w64-crt/crt/pseudo-reloc.c %{buildroot}%{tinygoroot}/lib/mingw-w64/mingw-w64-crt/crt
install -vdm 0755 %{buildroot}%{tinygoroot}/lib/mingw-w64/mingw-w64-crt/math
cp -rp lib/mingw-w64/mingw-w64-crt/math/x86 %{buildroot}%{tinygoroot}/lib/mingw-w64/mingw-w64-crt/math
install -vdm 0755 %{buildroot}%{tinygoroot}/lib/mingw-w64/mingw-w64-crt/lib-common
cp -rp lib/mingw-w64/mingw-w64-crt/lib-common/api-ms-win-crt-* %{buildroot}%{tinygoroot}/lib/mingw-w64/mingw-w64-crt/lib-common
cp -rp lib/mingw-w64/mingw-w64-crt/lib-common/advapi32.def.in %{buildroot}%{tinygoroot}/lib/mingw-w64/mingw-w64-crt/lib-common
cp -rp lib/mingw-w64/mingw-w64-crt/lib-common/kernel32.def.in %{buildroot}%{tinygoroot}/lib/mingw-w64/mingw-w64-crt/lib-common
cp -rp lib/mingw-w64/mingw-w64-crt/lib-common/msvcrt.def.in %{buildroot}%{tinygoroot}/lib/mingw-w64/mingw-w64-crt/lib-common
install -vdm 0755 %{buildroot}%{tinygoroot}/lib/mingw-w64/mingw-w64-headers/defaults
cp -rp lib/mingw-w64/mingw-w64-headers/crt/ %{buildroot}%{tinygoroot}/lib/mingw-w64/mingw-w64-headers
cp -rp lib/mingw-w64/mingw-w64-headers/include %{buildroot}%{tinygoroot}/lib/mingw-w64/mingw-w64-headers
cp -rp lib/mingw-w64/mingw-w64-headers/defaults/include %{buildroot}%{tinygoroot}/lib/mingw-w64/mingw-w64-headers/defaults
install -vdm 0755 %{buildroot}%{tinygoroot}/lib/musl
cp -rp lib/musl/COPYRIGHT %{buildroot}%{tinygoroot}/lib/musl
cp -rp lib/musl/include %{buildroot}%{tinygoroot}/lib/musl
install -vdm 0755 %{buildroot}%{tinygoroot}/lib/musl/arch
cp -rp lib/musl/arch/aarch64 %{buildroot}%{tinygoroot}/lib/musl/arch
cp -rp lib/musl/arch/arm %{buildroot}%{tinygoroot}/lib/musl/arch
cp -rp lib/musl/arch/generic %{buildroot}%{tinygoroot}/lib/musl/arch
cp -rp lib/musl/arch/i386 %{buildroot}%{tinygoroot}/lib/musl/arch
cp -rp lib/musl/arch/mips %{buildroot}%{tinygoroot}/lib/musl/arch
cp -rp lib/musl/arch/x86_64 %{buildroot}%{tinygoroot}/lib/musl/arch
install -vdm 0755 %{buildroot}%{tinygoroot}/lib/musl/crt
cp -rp lib/musl/crt/crt1.c %{buildroot}%{tinygoroot}/lib/musl/crt
install -vdm 0755 %{buildroot}%{tinygoroot}/lib/musl/src
cp -rp lib/musl/src/conf %{buildroot}%{tinygoroot}/lib/musl/src
cp -rp lib/musl/src/ctype %{buildroot}%{tinygoroot}/lib/musl/src
cp -rp lib/musl/src/env %{buildroot}%{tinygoroot}/lib/musl/src
cp -rp lib/musl/src/errno %{buildroot}%{tinygoroot}/lib/musl/src
cp -rp lib/musl/src/exit %{buildroot}%{tinygoroot}/lib/musl/src
cp -rp lib/musl/src/fcntl %{buildroot}%{tinygoroot}/lib/musl/src
cp -rp lib/musl/src/include %{buildroot}%{tinygoroot}/lib/musl/src
cp -rp lib/musl/src/internal %{buildroot}%{tinygoroot}/lib/musl/src
cp -rp lib/musl/src/legacy %{buildroot}%{tinygoroot}/lib/musl/src
cp -rp lib/musl/src/linux %{buildroot}%{tinygoroot}/lib/musl/src
cp -rp lib/musl/src/locale %{buildroot}%{tinygoroot}/lib/musl/src
cp -rp lib/musl/src/malloc %{buildroot}%{tinygoroot}/lib/musl/src
cp -rp lib/musl/src/mman %{buildroot}%{tinygoroot}/lib/musl/src
cp -rp lib/musl/src/math %{buildroot}%{tinygoroot}/lib/musl/src
cp -rp lib/musl/src/misc %{buildroot}%{tinygoroot}/lib/musl/src
cp -rp lib/musl/src/multibyte %{buildroot}%{tinygoroot}/lib/musl/src
cp -rp lib/musl/src/sched %{buildroot}%{tinygoroot}/lib/musl/src
cp -rp lib/musl/src/signal %{buildroot}%{tinygoroot}/lib/musl/src
cp -rp lib/musl/src/stdio %{buildroot}%{tinygoroot}/lib/musl/src
cp -rp lib/musl/src/stdlib %{buildroot}%{tinygoroot}/lib/musl/src
cp -rp lib/musl/src/string %{buildroot}%{tinygoroot}/lib/musl/src
cp -rp lib/musl/src/thread %{buildroot}%{tinygoroot}/lib/musl/src
cp -rp lib/musl/src/time %{buildroot}%{tinygoroot}/lib/musl/src
cp -rp lib/musl/src/unistd %{buildroot}%{tinygoroot}/lib/musl/src
cp -rp lib/musl/src/process %{buildroot}%{tinygoroot}/lib/musl/src
cp -rp lib/nrfx %{buildroot}%{tinygoroot}/lib/
install -vdm 0755 %{buildroot}%{tinygoroot}/lib/wasi-libc
install -vdm 0755 %{buildroot}%{tinygoroot}/lib/wasi-libc/dlmalloc
cp -rp lib/wasi-libc/dlmalloc/src %{buildroot}%{tinygoroot}/lib/wasi-libc/dlmalloc
install -vdm 0755 %{buildroot}%{tinygoroot}/lib/wasi-libc/libc-bottom-half
cp -rp lib/wasi-libc/libc-bottom-half/cloudlibc %{buildroot}%{tinygoroot}/lib/wasi-libc/libc-bottom-half
cp -rp lib/wasi-libc/libc-bottom-half/headers %{buildroot}%{tinygoroot}/lib/wasi-libc/libc-bottom-half
cp -rp lib/wasi-libc/libc-bottom-half/sources %{buildroot}%{tinygoroot}/lib/wasi-libc/libc-bottom-half
install -vdm 0755 %{buildroot}%{tinygoroot}/lib/wasi-libc/libc-top-half
cp -rp lib/wasi-libc/libc-top-half/headers %{buildroot}%{tinygoroot}/lib/wasi-libc/libc-top-half
cp -rp lib/wasi-libc/libc-top-half/sources %{buildroot}%{tinygoroot}/lib/wasi-libc/libc-top-half
install -vdm 0755 %{buildroot}%{tinygoroot}/lib/wasi-libc/libc-top-half/musl
cp -rp lib/wasi-libc/libc-top-half/musl/include %{buildroot}%{tinygoroot}/lib/wasi-libc/libc-top-half/musl
install -vdm 0755 %{buildroot}%{tinygoroot}/lib/wasi-libc/libc-top-half/musl/arch
cp -rp lib/wasi-libc/libc-top-half/musl/arch/generic %{buildroot}%{tinygoroot}/lib/wasi-libc/libc-top-half/musl/arch
cp -rp lib/wasi-libc/libc-top-half/musl/arch/wasm32 %{buildroot}%{tinygoroot}/lib/wasi-libc/libc-top-half/musl/arch
install -vdm 0755 %{buildroot}%{tinygoroot}/lib/wasi-libc/libc-top-half/musl/src
cp -rp lib/wasi-libc/libc-top-half/musl/src/conf %{buildroot}%{tinygoroot}/lib/wasi-libc/libc-top-half/musl/src
cp -rp lib/wasi-libc/libc-top-half/musl/src/dirent %{buildroot}%{tinygoroot}/lib/wasi-libc/libc-top-half/musl/src
cp -rp lib/wasi-libc/libc-top-half/musl/src/env %{buildroot}%{tinygoroot}/lib/wasi-libc/libc-top-half/musl/src
cp -rp lib/wasi-libc/libc-top-half/musl/src/errno %{buildroot}%{tinygoroot}/lib/wasi-libc/libc-top-half/musl/src
cp -rp lib/wasi-libc/libc-top-half/musl/src/exit %{buildroot}%{tinygoroot}/lib/wasi-libc/libc-top-half/musl/src
cp -rp lib/wasi-libc/libc-top-half/musl/src/fcntl %{buildroot}%{tinygoroot}/lib/wasi-libc/libc-top-half/musl/src
cp -rp lib/wasi-libc/libc-top-half/musl/src/fenv %{buildroot}%{tinygoroot}/lib/wasi-libc/libc-top-half/musl/src
cp -rp lib/wasi-libc/libc-top-half/musl/src/include %{buildroot}%{tinygoroot}/lib/wasi-libc/libc-top-half/musl/src
cp -rp lib/wasi-libc/libc-top-half/musl/src/internal %{buildroot}%{tinygoroot}/lib/wasi-libc/libc-top-half/musl/src
cp -rp lib/wasi-libc/libc-top-half/musl/src/legacy %{buildroot}%{tinygoroot}/lib/wasi-libc/libc-top-half/musl/src
cp -rp lib/wasi-libc/libc-top-half/musl/src/locale %{buildroot}%{tinygoroot}/lib/wasi-libc/libc-top-half/musl/src
cp -rp lib/wasi-libc/libc-top-half/musl/src/math %{buildroot}%{tinygoroot}/lib/wasi-libc/libc-top-half/musl/src
cp -rp lib/wasi-libc/libc-top-half/musl/src/misc %{buildroot}%{tinygoroot}/lib/wasi-libc/libc-top-half/musl/src
cp -rp lib/wasi-libc/libc-top-half/musl/src/multibyte %{buildroot}%{tinygoroot}/lib/wasi-libc/libc-top-half/musl/src
cp -rp lib/wasi-libc/libc-top-half/musl/src/network %{buildroot}%{tinygoroot}/lib/wasi-libc/libc-top-half/musl/src
cp -rp lib/wasi-libc/libc-top-half/musl/src/stat %{buildroot}%{tinygoroot}/lib/wasi-libc/libc-top-half/musl/src
cp -rp lib/wasi-libc/libc-top-half/musl/src/stdio %{buildroot}%{tinygoroot}/lib/wasi-libc/libc-top-half/musl/src
cp -rp lib/wasi-libc/libc-top-half/musl/src/stdlib %{buildroot}%{tinygoroot}/lib/wasi-libc/libc-top-half/musl/src
cp -rp lib/wasi-libc/libc-top-half/musl/src/string %{buildroot}%{tinygoroot}/lib/wasi-libc/libc-top-half/musl/src
cp -rp lib/wasi-libc/libc-top-half/musl/src/thread %{buildroot}%{tinygoroot}/lib/wasi-libc/libc-top-half/musl/src
cp -rp lib/wasi-libc/libc-top-half/musl/src/time %{buildroot}%{tinygoroot}/lib/wasi-libc/libc-top-half/musl/src
cp -rp lib/wasi-libc/libc-top-half/musl/src/unistd %{buildroot}%{tinygoroot}/lib/wasi-libc/libc-top-half/musl/src
%if %{with wasi_cli}
install -vdm 0755 %{buildroot}%{tinygoroot}/lib/wasi-cli
cp -rp lib/wasi-cli/wit %{buildroot}%{tinygoroot}/lib/wasi-cli/wit
%endif
install -vdm 0755 %{buildroot}%{tinygoroot}/lib/picolibc/newlib/libc
cp -rp lib/picolibc/newlib/libc/ctype %{buildroot}%{tinygoroot}/lib/picolibc/newlib/libc
chmod -x %{buildroot}%{tinygoroot}/lib/picolibc/newlib/libc/ctype/{mkcaseconv,mkcategories,mkunidata}
cp -rp lib/picolibc/newlib/libc/include %{buildroot}%{tinygoroot}/lib/picolibc/newlib/libc
cp -rp lib/picolibc/newlib/libc/locale %{buildroot}%{tinygoroot}/lib/picolibc/newlib/libc
cp -rp lib/picolibc/newlib/libc/string %{buildroot}%{tinygoroot}/lib/picolibc/newlib/libc
chmod -x %{buildroot}%{tinygoroot}/lib/picolibc/newlib/libc/string/{mkunidata,mkwide,mkwidthA,uniset}
cp -rp lib/picolibc/newlib/libc/tinystdio %{buildroot}%{tinygoroot}/lib/picolibc/newlib/libc
chmod -x %{buildroot}%{tinygoroot}/lib/picolibc/newlib/libc/tinystdio/make-dtoa-data
install -vdm 0755 %{buildroot}%{tinygoroot}/lib/picolibc/newlib/libm
cp -rp lib/picolibc/newlib/libm/common %{buildroot}%{tinygoroot}/lib/picolibc/newlib/libm
cp -rp lib/picolibc/newlib/libm/math %{buildroot}%{tinygoroot}/lib/picolibc/newlib/libm
cp -rp lib/picolibc-stdio.c %{buildroot}%{tinygoroot}/lib
cp -rp src %{buildroot}%{tinygoroot}/
rm %{buildroot}%{tinygoroot}/src/examples/wasm/.gitignore
cp -rp targets %{buildroot}%{tinygoroot}/


%if %{with check}
%global gotestflags %gocompilerflags -v -tags="llvm%{clang_llvm_version}" -timeout 30m
%check
export TINYGOROOT=%{buildroot}%{tinygoroot}
export GOPATH=%{buildroot}%{tinygoroot}:%{gopath}
export PATH=%{buildroot}%{_bindir}:$PATH
export GO111MODULE=off
export XDG_CACHE_HOME="${PWD}/$(mktemp -d tinygo.XXXXXX)"
%gocheck -v -t src -t tests
( cd _build/src/%{goipath} && GOPATH=%{currentgosourcedir}/_build:$GOPATH make smoketest STM32=0 XTENSA=0 )
%ifnarch aarch64
make wasmtest
%endif
make tinygo-test
%endif


%files
%doc README.md CHANGELOG.md CONTRIBUTING.md
%license LICENSE
%{_bindir}/tinygo
%{tinygoroot}
%doc %{tinygoroot}/lib/bdwgc/README.md
%license %{tinygoroot}/lib/bdwgc/LICENSE
%doc %{tinygoroot}/lib/CMSIS/README.md
%license %{tinygoroot}/lib/compiler-rt-builtins/LICENSE.TXT
%doc %{tinygoroot}/lib/compiler-rt-builtins/README.txt
%license %{tinygoroot}/lib/nrfx/LICENSE
%doc %{tinygoroot}/lib/nrfx/README.md
%license %{tinygoroot}/lib/musl/COPYRIGHT


%changelog
%autochangelog
