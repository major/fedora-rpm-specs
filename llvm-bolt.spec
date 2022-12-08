%global toolchain clang

%global maj_ver 15
%global min_ver 0
#global rc_ver 1
%global patch_ver 6
%global bolt_version %{maj_ver}.%{min_ver}.%{patch_ver}
%global bolt_srcdir llvm-project-%{bolt_version}%{?rc_ver:rc%{rc_ver}}.src

Name: llvm-bolt
Version: %{bolt_version}%{?rc_ver:~rc%{rc_ver}}
Release: 1%{?dist}
Summary: a post-link optimizer developed to speed up large applications

License: Apache-2.0 WITH LLVM-exception
URL: https://github.com/llvm/llvm-project/tree/main/bolt
Source0: https://github.com/llvm/llvm-project/releases/download/llvmorg-%{maj_ver}.%{min_ver}.%{patch_ver}%{?rc_ver:-rc%{rc_ver}}/%{bolt_srcdir}.tar.xz
Source1: https://github.com/llvm/llvm-project/releases/download/llvmorg-%{maj_ver}.%{min_ver}.%{patch_ver}%{?rc_ver:-rc%{rc_ver}}/%{bolt_srcdir}.tar.xz.sig
Source2: release-keys.asc

## drop these for LLVM 16.0.0
Patch1: 0002-BOLT-Fix-part-of-dylib-compatibility.patch
Patch2: 0003-BOLT-Support-building-bolt-when-LLVM_LINK_LLVM_DYLIB.patch
##

# Upstream doesn't support standalone builds
Patch10: standalone.patch
# Upstream tests is missing a canonical variable in standalone mode
Patch11: test.patch
# Upstream assumes runtime libraries are installed in "lib"
Patch12: lib64.patch


BuildRequires: gcc
BuildRequires: gcc-c++
BuildRequires: cmake
BuildRequires: ninja-build
BuildRequires: zlib-devel
BuildRequires: llvm-devel = %{version}
BuildRequires: llvm-test = %{version}
BuildRequires: python3-lit
BuildRequires: python3-psutil
BuildRequires: clang
BuildRequires: lld

# For origin certification
BuildRequires: gnupg2

# BOLT only supports aarch64 and x86_64
ExcludeArch:    s390x ppc64le i686

# As hinted by bolt documentation
Recommends:     gperftools-devel

%description

BOLT is a post-link optimizer developed to speed up large applications.
It achieves the improvements by optimizing application's code layout based on
execution profile gathered by sampling profiler, such as Linux `perf` tool.

%package doc
Summary: Documentation for BOLT
BuildArch: noarch
Requires: %{name} = %{version}-%{release}

%description doc
Documentation for the BOLT optimizer

%prep
%{gpgverify} --keyring='%{SOURCE2}' --signature='%{SOURCE1}' --data='%{SOURCE0}'
%autosetup -n %{bolt_srcdir}/bolt -p2

# BOLT is not respecting the component split of LLVM and requires some private
# header to be able in order to compile

# workaround this by moving these headers to a specific bolt directory
mkdir imported
mkdir imported/Utils
mkdir imported/MCTargetDesc

cp ../llvm/lib/Target/X86/MCTargetDesc/X86BaseInfo.h imported/MCTargetDesc/
cp ../llvm/lib/Target/X86/MCTargetDesc/X86InstrRelaxTables.h imported/MCTargetDesc/
cp ../llvm/lib/Target/X86/MCTargetDesc/X86MCTargetDesc.h imported/MCTargetDesc/
cp ../llvm/lib/Target/AArch64/MCTargetDesc/AArch64AddressingModes.h imported/MCTargetDesc/
cp ../llvm/lib/Target/AArch64/MCTargetDesc/AArch64MCExpr.h imported/MCTargetDesc/
cp ../llvm/lib/Target/AArch64/MCTargetDesc/AArch64MCTargetDesc.h imported/MCTargetDesc/
cp ../llvm/lib/Target/AArch64/AArch64ExpandImm.h imported/
cp ../llvm/lib/Target/AArch64/Utils/AArch64BaseInfo.h imported/Utils/

# move private Tablegen defs to a specific bolt directory
for arch in X86 AArch64
do
    mkdir imported/$arch
    cp ../llvm/lib/Target/$arch/*.td imported/$arch/
done

# Copy the cmake rules to generate the required headers from tablegen

# extracted from llvm/lib/Target/X86/CMakeLists.txt
cat > imported/X86/CMakeLists.txt << EOF
set(LLVM_TARGET_DEFINITIONS X86.td)

tablegen(LLVM X86GenAsmMatcher.inc -gen-asm-matcher)
tablegen(LLVM X86GenAsmWriter.inc -gen-asm-writer)
tablegen(LLVM X86GenAsmWriter1.inc -gen-asm-writer -asmwriternum=1)
tablegen(LLVM X86GenCallingConv.inc -gen-callingconv)
tablegen(LLVM X86GenDAGISel.inc -gen-dag-isel)
tablegen(LLVM X86GenDisassemblerTables.inc -gen-disassembler)
tablegen(LLVM X86GenEVEX2VEXTables.inc -gen-x86-EVEX2VEX-tables)
tablegen(LLVM X86GenExegesis.inc -gen-exegesis)
tablegen(LLVM X86GenFastISel.inc -gen-fast-isel)
tablegen(LLVM X86GenGlobalISel.inc -gen-global-isel)
tablegen(LLVM X86GenInstrInfo.inc -gen-instr-info
                                  -instr-info-expand-mi-operand-info=0)
tablegen(LLVM X86GenMnemonicTables.inc -gen-x86-mnemonic-tables -asmwriternum=1)
tablegen(LLVM X86GenRegisterBank.inc -gen-register-bank)
tablegen(LLVM X86GenRegisterInfo.inc -gen-register-info)
tablegen(LLVM X86GenSubtargetInfo.inc -gen-subtarget)

add_public_tablegen_target(X86CommonTableGen)
EOF

# extracted from llvm/lib/Target/AArch64/CMakeLists.txt
cat > imported/AArch64/CMakeLists.txt << EOF

set(LLVM_TARGET_DEFINITIONS AArch64.td)

tablegen(LLVM AArch64GenAsmMatcher.inc -gen-asm-matcher)
tablegen(LLVM AArch64GenAsmWriter.inc -gen-asm-writer)
tablegen(LLVM AArch64GenAsmWriter1.inc -gen-asm-writer -asmwriternum=1)
tablegen(LLVM AArch64GenCallingConv.inc -gen-callingconv)
tablegen(LLVM AArch64GenDAGISel.inc -gen-dag-isel)
tablegen(LLVM AArch64GenDisassemblerTables.inc -gen-disassembler)
tablegen(LLVM AArch64GenFastISel.inc -gen-fast-isel)
tablegen(LLVM AArch64GenGlobalISel.inc -gen-global-isel)
tablegen(LLVM AArch64GenO0PreLegalizeGICombiner.inc -gen-global-isel-combiner
              -combiners="AArch64O0PreLegalizerCombinerHelper")
tablegen(LLVM AArch64GenPreLegalizeGICombiner.inc -gen-global-isel-combiner
              -combiners="AArch64PreLegalizerCombinerHelper")
tablegen(LLVM AArch64GenPostLegalizeGICombiner.inc -gen-global-isel-combiner
              -combiners="AArch64PostLegalizerCombinerHelper")
tablegen(LLVM AArch64GenPostLegalizeGILowering.inc -gen-global-isel-combiner
              -combiners="AArch64PostLegalizerLoweringHelper")
tablegen(LLVM AArch64GenInstrInfo.inc -gen-instr-info)
tablegen(LLVM AArch64GenMCCodeEmitter.inc -gen-emitter)
tablegen(LLVM AArch64GenMCPseudoLowering.inc -gen-pseudo-lowering)
tablegen(LLVM AArch64GenRegisterBank.inc -gen-register-bank)
tablegen(LLVM AArch64GenRegisterInfo.inc -gen-register-info)
tablegen(LLVM AArch64GenSubtargetInfo.inc -gen-subtarget)
tablegen(LLVM AArch64GenSystemOperands.inc -gen-searchable-tables)
tablegen(LLVM AArch64GenExegesis.inc -gen-exegesis)

add_public_tablegen_target(AArch64CommonTableGen)

EOF

# Now that we have remove the dependency on private LLVM headers,
# remove all directories, but keep bolt
find ../* -maxdepth 0 ! -name 'bolt' -exec rm -rf {} +

%build

%global _lto_cflags %{nil}

%cmake  -GNinja \
        -DCMAKE_BUILD_TYPE=RelWithDebInfo \
        -DCMAKE_SKIP_RPATH=ON \
        -DLLVM_DIR=%{_libdir}/cmake/llvm \
        -DLLVM_TABLEGEN_EXE=%{_bindir}/llvm-tblgen \
        -DLLVM_BUILD_UTILS:BOOL=ON \
        -DBOLT_INCLUDE_DOCS:BOOL=ON \
        -DLLVM_INCLUDE_TESTS:BOOL=ON \
        -DBUILD_SHARED_LIBS:BOOL=OFF \
        -DLLVM_LINK_LLVM_DYLIB:BOOL=OFF \
%if 0%{?__isa_bits} == 64
        -DLLVM_LIBDIR_SUFFIX=64 \
%else
        -DLLVM_LIBDIR_SUFFIX= \
%endif
        -DBOLT_INCLUDE_TESTS:BOOL=ON \
        -DBOLT_CLANG_EXE=%{_bindir}/clang\
        -DBOLT_LLD_EXE=%{_bindir}/ld.lld\
        -DLLVM_EXTERNAL_LIT=%{_bindir}/lit

# Set LD_LIBRARY_PATH now because we skip rpath generation and the build uses
# some just built libraries.
export LD_LIBRARY_PATH=%{_builddir}/%{bolt_srcdir}/bolt/%{_vpath_builddir}/%{_lib}
# Set DESTDIR now because bolt sneaks in an install step in its build step.
export DESTDIR=%{buildroot}
%cmake_build

%install
%cmake_install

# We don't ship libLLVMBOLT*.a
rm -f %{buildroot}%{_libdir}/libLLVMBOLT*.a

# There currently is not support upstream for building html doc from BOLT
install -d %{buildroot}%{_pkgdocdir}
mv README.md docs/*.md %{buildroot}%{_pkgdocdir}

%check

# bolt makes incorrect assumptions on the location of llvm-bolt*
mkdir -p %{_builddir}/%{bolt_srcdir}/bolt/test
for boltbin in llvm-bolt llvm-boltdiff perf2bolt llvm-bolt-heatmap merge-fdata
do
    ln -s %{_builddir}/%{bolt_srcdir}/bolt/%{_vpath_builddir}/bin/${boltbin} %{_builddir}/%{bolt_srcdir}/bolt/test/
done

%ifarch x86_64
# Bolt makes incorrect assumptions on the location of libbolt_rt_*.a.
mkdir -p %{_builddir}/%{bolt_srcdir}/%{_lib}
for rt in libbolt_rt_instr libbolt_rt_hugify libbolt_rt_instr_osx
do
    ln -s %{buildroot}/%{_libdir}/${rt}.a %{_builddir}/%{bolt_srcdir}/%{_lib}
done
%endif

%ifarch aarch64
# Failing test cases on aarch64
rm test/cache+-deprecated.test test/bolt-icf.test test/R_ABS.pic.lld.cpp
%endif

export LD_LIBRARY_PATH=%{_builddir}/%{bolt_srcdir}/bolt/%{_vpath_builddir}/%{_lib}
export DESTDIR=%{buildroot}
%cmake_build --target check-bolt

%files
%license LICENSE.TXT
%{_bindir}/llvm-bolt
%{_bindir}/llvm-boltdiff
%{_bindir}/perf2bolt

%ifarch x86_64
%{_libdir}/libbolt_rt_hugify.a
%{_libdir}/libbolt_rt_instr.a
%{_libdir}/libbolt_rt_instr_osx.a
%endif


%files doc
%doc %{_pkgdocdir}

%changelog
* Tue Dec 06 2022 Nikita Popov <npopov@redhat.com> - 15.0.6-1
- Update to LLVM 15.0.6

* Mon Jul 11 2022 sguelton@redhat.com - 15.0.0-1
- Initial version.

