#region globals
#region version
%global maj_ver 21
%global min_ver 1
%global patch_ver 8
#global rc_ver rc3

%bcond_with snapshot_build
%if %{with snapshot_build}
%include %{_sourcedir}/version.spec.inc
%endif
#endregion version

# Components enabled if supported by target architecture:
%define gold_arches %{ix86} x86_64 aarch64 %{power64} s390x
%ifarch %{gold_arches}
  %bcond_without gold
%else
  %bcond_with gold
%endif

# Enable this in order to disable a lot of features and get to clang as fast
# as possible. This is useful in order to bisect issues affecting LLVM, clang
# or LLD.
%bcond_with fastclang
%if %{with fastclang}
%define bcond_override_default_lldb 0
%define bcond_override_default_offload 0
%define bcond_override_default_mlir 0
%define bcond_override_default_flang 0
%define bcond_override_default_build_bolt 0
%define bcond_override_default_polly 0
%define bcond_override_default_pgo 0
%define bcond_override_default_libcxx 0
%define bcond_override_default_lto_build 0
%define bcond_override_default_check 0
%define _find_debuginfo_dwz_opts %{nil}
%endif

# Build compat packages llvmN instead of main package for the current LLVM
# version. Used on Fedora.
%bcond_with compat_build
# Bundle compat libraries for a previous LLVM version, as part of llvm-libs and
# clang-libs. Used on RHEL.
%bcond_with bundle_compat_lib
%bcond_without check

%if %{with bundle_compat_lib}
%global compat_maj_ver 20
%global compat_ver %{compat_maj_ver}.1.8
%endif

# Compat builds do not include python-lit
%if %{with compat_build}
%bcond_with python_lit
%else
%bcond_without python_lit
%endif

%bcond_without lldb

%ifarch ppc64le
%if %{defined rhel} && 0%{?rhel} < 10
# RHEL <= 9 use the IBM long double format, which is not supported by libc.
# Since LLVM 21, parts of libc are required in order to build offload.
%bcond_with offload
%else
%bcond_without offload
%endif
%else
%ifarch %{ix86}
# libomptarget is not supported on 32-bit systems.
%bcond_with offload
%else
%bcond_without offload
%endif
%endif

# MLIR version 22 started to require nanobind >= 2.9, which is only available
# on Fedora >= 44.
%if %{without compat_build} && %{defined fedora} && (%{maj_ver} < 22 || 0%{?fedora} >= 44)
%ifarch %{ix86}
%bcond_with mlir
%else
%bcond_without mlir
%endif
%else
%bcond_with mlir
%endif

#region flang
%if %{without compat_build} && %{defined fedora} && (%{maj_ver} >= 22 && 0%{?fedora} >= 44)
# Link error on i686.
# s390x is not supported upstream yet.
%ifarch i686 s390x
%bcond_with flang
%else
%bcond_without flang
%endif
%endif

%if %{with flang}

# Sanity check for flang
# flang depends on mlir, clang, flang, openmp.
# Make sure those are being built.
%if %{without mlir}
%{error:flang must be built --with=mlir}
%endif

# Set Fortran build flags to nil because they contain flags that don't apply to flang.
%global build_fflags %{nil}

%{lua:

-- Return the maximum number of parallel jobs a build can run based on the
-- amount of maximum memory used per process (per_proc_mem).
function print_max_procs(per_proc_mem)
    local f = io.open("/proc/meminfo", "r")
    local mem = 0
    local nproc_str = nil
    for line in f:lines() do
        _, _, mem = string.find(line, "MemTotal:%s+(%d+)%s+kB")
        if mem then
           break
        end
    end
    f:close()

    local proc_handle = io.popen("nproc")
    _, _, nproc_str = string.find(proc_handle:read("*a"), "(%d+)")
    proc_handle:close()
    local nproc = tonumber(nproc_str)
    if nproc < 1 then
        nproc = 1
    end
    local mem_mb = mem / 1024
    local cpu = math.floor(mem_mb / per_proc_mem)
    if cpu < 1 then
        cpu = 1
    end

    if cpu > nproc then
        cpu = nproc
    end
    print(cpu)
end
}
%endif
#endregion flang

# The libcxx build condition also enables libcxxabi and libunwind.
%if %{without compat_build} && %{defined fedora}
%bcond_without libcxx
%else
%bcond_with libcxx
%endif

# I've called the build condition "build_bolt" to indicate that this does not
# necessarily "use" BOLT in order to build LLVM.
%if %{without compat_build} && %{defined fedora}
# BOLT only supports aarch64 and x86_64
%ifarch aarch64 x86_64
%bcond_without build_bolt
%else
%bcond_with build_bolt
%endif
%else
%bcond_with build_bolt
%endif

%if %{without compat_build} && %{defined fedora}
%bcond_without polly
%else
%bcond_with polly
%endif

#region pgo
%ifarch %{ix86}
%bcond_with pgo
%else
%if 0%{?fedora} >= 43 || 0%{?rhel} >= 9
%bcond_without pgo
%else
%bcond_with pgo
%endif
%endif

# Sanity checks for PGO and bootstrapping
#----------------------------------------
%if %{with pgo}
%ifarch %{ix86}
%{error:Your architecture is not allowed for PGO because it is in this list: %{ix86}}
%endif
%endif
#----------------------------------------
#endregion pgo

# Disable LTO on x86 and riscv in order to reduce memory consumption.
%ifarch %ix86 riscv64
%bcond_with lto_build
%else
%if %{defined rhel} && 0%{?rhel} <= 8
# LTO builds got enabled on Fedora and RHEL >= 9 only.
%bcond_with lto_build
%else
%bcond_without lto_build
%endif
%endif

# Historically, LLD was used used at the same combinations that enabled PGO.
# If this changes, we need to update the following lines.
# However, we should be able to link using LLD even if PGO is disabled.
# Reminder: RHEL8 still builds with gcc + ld.bfd.
%if %{with pgo}
%bcond_without use_lld
%else
# RHEL8 still builds with gcc + ld.bfd.
%bcond_with use_lld
%endif

# For PGO Disable LTO for now because of LLVMgold.so not found error
# Use LLVM_ENABLE_LTO:BOOL=ON flags to enable LTO instead
%if 0%{without lto_build} || 0%{with pgo}
%global _lto_cflags %nil
%endif

# We are building with clang for faster/lower memory LTO builds.
# See https://docs.fedoraproject.org/en-US/packaging-guidelines/#_compiler_macros
# Reminder: This only works on Fedora and RHEL >= 9.
%global toolchain clang

# Make sure that we are not building with a newer compiler than the targeted
# version. For example, if we build LLVM 19 with Clang 20, then we'd build
# LLVM libraries with Clang 20, and then the runtimes build would use the
# just-built Clang 19. Runtimes that link against LLVM libraries would then
# try to make Clang 19 perform LTO involving LLVM 20 bitcode.
%if %{with compat_build}
%global host_clang_maj_ver %{maj_ver}
%endif

%if %{defined host_clang_maj_ver}
%global __cc /usr/bin/clang-%{host_clang_maj_ver}
%global __cxx /usr/bin/clang++-%{host_clang_maj_ver}
%endif

# The upper bound must remain and never exceed the latest RHEL version with GTS,
# so that this does not apply to ELN or a brand new RHEL version.
%if %{defined rhel} && 0%{?rhel} <= 10
%global gts_version 15
%endif

%if %{defined rhel} && 0%{?rhel} <= 8
%bcond_with libedit
%else
%bcond_without libedit
%endif

# Opt out of https://fedoraproject.org/wiki/Changes/fno-omit-frame-pointer
# https://bugzilla.redhat.com/show_bug.cgi?id=2158587
%undefine _include_frame_pointers

# Opt out of https://fedoraproject.org/wiki/Changes/StaticLibraryPreserveDebuginfo
# Debuginfo for LLVM static libraries is huge.
%undefine _preserve_static_debuginfo
# Also make sure find-debuginfo does not waste time on these archives.
# https://bugzilla.redhat.com/show_bug.cgi?id=2390105
%if 0%{?fedora} >= 43
%define _find_debuginfo_opts --no-ar-files
%endif

# Suffixless tarball name (essentially: basename -s .tar.xz llvm-project-17.0.6.src.tar.xz)
%if %{with snapshot_build}
%global src_tarball_dir llvm-project-%{llvm_snapshot_git_revision}
%else
%global src_tarball_dir llvm-project-%{maj_ver}.%{min_ver}.%{patch_ver}%{?rc_ver:-%{rc_ver}}.src
%endif

# LLD uses "fast" as the algortithm for generating build-id
# values while ld.bfd uses "sha1" by default. We need to get lld
# to use the same algorithm or otherwise we end up with errors like thise one:
#
#   "build-id found in [...]/usr/lib64/llvm21/bin/llvm-debuginfod-find too small"
#
# NOTE: Originally this is only needed for PGO but it doesn't hurt to have it on all the time.
%global build_ldflags %{?build_ldflags} -Wl,--build-id=sha1

#region LLVM globals

%if %{with compat_build}
%global pkg_name_llvm llvm%{maj_ver}
%global pkg_suffix %{maj_ver}
%global exec_suffix -%{maj_ver}
%else
%global pkg_name_llvm llvm
%global pkg_suffix %{nil}
%global exec_suffix %{nil}
%endif

# Apart from compiler-rt and libcxx, everything is installed into a
# version-specific prefix. Non-compat packages add symlinks to this prefix.
%global install_prefix %{_libdir}/llvm%{maj_ver}
%global install_bindir %{install_prefix}/bin
%global install_includedir %{install_prefix}/include
%global install_libdir %{install_prefix}/%{_lib}
%global install_datadir %{install_prefix}/share
%global install_mandir %{install_prefix}/share/man
%global install_libexecdir %{install_prefix}/libexec
%global build_libdir llvm/%{_vpath_builddir}/%{_lib}
%global unprefixed_libdir %{_lib}

%if 0%{?rhel}
%global targets_to_build "X86;AMDGPU;PowerPC;NVPTX;SystemZ;AArch64;BPF;WebAssembly;RISCV"
%global experimental_targets_to_build ""
%else
%global targets_to_build "all"
%global experimental_targets_to_build "AVR"
%endif

%global build_install_prefix %{buildroot}%{install_prefix}

# Lower memory usage of dwz on s390x
%global _dwz_low_mem_die_limit_s390x 1
%global _dwz_max_die_limit_s390x 1000000

%global llvm_triple %{_target_platform}

# https://fedoraproject.org/wiki/Changes/PythonSafePath#Opting_out
# Don't add -P to Python shebangs
# The executable Python scripts in /usr/share/opt-viewer/ import each other
%undefine _py3_shebang_P

#endregion LLVM globals

#region CLANG globals

%global pkg_name_clang clang%{pkg_suffix}

#endregion CLANG globals

#region COMPILER-RT globals

%global pkg_name_compiler_rt compiler-rt%{pkg_suffix}

# TODO(kkleine): do these optflags hurt llvm and/or clang?

# see https://sourceware.org/bugzilla/show_bug.cgi?id=25271
%global optflags %(echo %{optflags} -D_DEFAULT_SOURCE)

# see https://gcc.gnu.org/bugzilla/show_bug.cgi?id=93615
%global optflags %(echo %{optflags} -Dasm=__asm__)

# Copy CFLAGS into ASMFLAGS, so -fcf-protection is used when compiling assembly files.
# export ASMFLAGS=$CFLAGS
#endregion COMPILER-RT globals

#region openmp globals
%global pkg_name_libomp libomp%{pkg_suffix}

%global so_suffix %{maj_ver}.%{min_ver}

%if %{with snapshot_build}
%global so_suffix %{maj_ver}.%{min_ver}%{llvm_snapshot_version_suffix}
%endif

%ifarch ppc64le
%global libomp_arch ppc64
%else
%global libomp_arch %{_arch}
%endif
#endregion openmp globals

#region LLD globals
%global pkg_name_lld lld%{pkg_suffix}
#endregion LLD globals

#region LLDB globals
%global pkg_name_lldb lldb%{pkg_suffix}
#endregion LLDB globals

#region MLIR globals
%global pkg_name_mlir mlir%{pkg_suffix}
#endregion MLIR globals

#region libcxx globals
%global pkg_name_libcxx libcxx
%global pkg_name_libcxxabi libcxxabi
%global pkg_name_llvm_libunwind llvm-libunwind
#endregion libcxx globals

#region BOLT globals
%global pkg_name_bolt llvm-bolt%{pkg_suffix}
#endregion BOLT globals

#region polly globals
%global pkg_name_polly polly%{pkg_suffix}
#endregion polly globals

#region flang globals
%global pkg_name_flang flang%{pkg_suffix}
#endregion flang globals

#endregion globals

#region packages
#region main package
Name:		%{pkg_name_llvm}
Version:	%{maj_ver}.%{min_ver}.%{patch_ver}%{?rc_ver:~%{rc_ver}}%{?llvm_snapshot_version_suffix:~%{llvm_snapshot_version_suffix}}
%if 0%{?rhel} == 8
Release:	1%{?dist}
%else
Release:	%autorelease
%endif
Summary:	The Low Level Virtual Machine

License:	Apache-2.0 WITH LLVM-exception OR NCSA
URL:		http://llvm.org

%if %{with snapshot_build}
Source0: https://github.com/llvm/llvm-project/archive/%{llvm_snapshot_git_revision}.tar.gz
%else
Source0: https://github.com/llvm/llvm-project/releases/download/llvmorg-%{maj_ver}.%{min_ver}.%{patch_ver}%{?rc_ver:-%{rc_ver}}/%{src_tarball_dir}.tar.xz
Source1: https://github.com/llvm/llvm-project/releases/download/llvmorg-%{maj_ver}.%{min_ver}.%{patch_ver}%{?rc_ver:-%{rc_ver}}/%{src_tarball_dir}.tar.xz.sig
%endif
Source6: release-keys.asc

%if %{without compat_build}
Source2005: macros.%{pkg_name_clang}
%endif

%if %{with bundle_compat_lib}
Source3000: https://github.com/llvm/llvm-project/releases/download/llvmorg-%{compat_ver}/llvm-project-%{compat_ver}.src.tar.xz
Source3001: https://github.com/llvm/llvm-project/releases/download/llvmorg-%{compat_ver}/llvm-project-%{compat_ver}.src.tar.xz.sig
%endif

# Sources we use to split up the main spec file in sections so that we can more
# easily see what specfile sections are touched by a patch.
%if %{with snapshot_build}
Source1000: version.spec.inc
%endif

# Only used on RHEL-8, where rpmautospec is not available.
Source1001: changelog

# We've established the habit of numbering patches the following way:
#
#   0-499: All patches that are unconditionally applied
#   500-1000: Patches applied under certain conditions (e.g. only on RHEL8)
#   1500-1599: Patches for LLVM 15
#   1600-1699: Patches for LLVM 16
#   1700-1799: Patches for LLVM 17
#   ...
#   2000-2099: Patches for LLVM 20
#
# The idea behind this is that the last range of patch numbers (e.g. 2000-2099) allow
# us to "deprecate" a patch instead of deleting it right away.
# Suppose llvm upstream in git is at version 20 and there's a patch living
# in some PR that has not been merged yet. You can copy that patch and put it
# in a line like:
#
#   Patch2011: upstream.patch
#
# As time goes by, llvm moves on to LLVM 21 and meanwhile the patch has landed.
# There's no need for you to remove the "Patch2011:" line. In fact, we encourage you
# to not remove it for some time. For compat libraries and compat packages we might
# still need this patch and so we're applying it automatically for you in those
# situations. Remember that a compat library is always at least one major version
# behind the latest packaged LLVM version.

#region CLANG patches
Patch101: 0001-PATCH-clang-Make-funwind-tables-the-default-on-all-a.patch
Patch102: 0003-PATCH-clang-Don-t-install-static-libraries.patch
Patch2002: 20-131099.patch

# Workaround a bug in ORC on ppc64le.
# More info is available here: https://reviews.llvm.org/D159115#4641826
Patch103: 0001-Workaround-a-bug-in-ORC-on-ppc64le.patch

# With the introduction of --gcc-include-dir in the clang config file,
# this might no longer be needed.
Patch104: 0001-Driver-Give-devtoolset-path-precedence-over-Installe.patch
#endregion CLANG patches

# Fix LLVMConfig.cmake when symlinks are used.
# (https://github.com/llvm/llvm-project/pull/124743 landed in LLVM 21)
Patch2003: 0001-cmake-Resolve-symlink-when-finding-install-prefix.patch

#region LLD patches
Patch106: 0001-19-Always-build-shared-libs-for-LLD.patch
Patch2103: 0001-lld-Adjust-compressed-debug-level-test-for-s390x-wit.patch
#endregion LLD patches

#region polly patches
Patch2102: 0001-20-polly-shared-libs.patch
Patch2202: 0001-22-polly-shared-libs.patch
Patch2302: 0001-22-polly-shared-libs.patch
#endregion polly patches

#region RHEL patches
# RHEL 8 only
Patch501: 0001-Fix-page-size-constant-on-aarch64-and-ppc64le.patch
# Backport a fix for https://github.com/llvm/llvm-project/issues/165696 from
# LLVM 22. The first patch is a requirement of the second patch.
# Apply the fix to RHEL8 only because the other distros do not need this fix
# because they already support kfunc __bpf_trap.
Patch502: 0001-BPF-Support-Jump-Table-149715.patch
Patch503: 0002-BPF-Remove-unused-weak-symbol-__bpf_trap-166003.patch
Patch504: 0003-BPF-Remove-dead-code-related-to-__bpf_trap-global-va.patch
#endregion RHEL patches

# Fix a pgo miscompilation triggered by building Rust 1.87 with pgo on ppc64le.
# https://github.com/llvm/llvm-project/issues/138208
Patch2004: 0001-CodeGenPrepare-Make-sure-instruction-get-from-SunkAd.patch
# Related CGP fix for domination, rhbz#2388223
Patch2008: 0001-CGP-Bail-out-if-Base-Scaled-Reg-does-not-dominate-in.patch

# Fix Power9/Power10 crbit spilling
# https://github.com/llvm/llvm-project/pull/146424
Patch2007: 21-146424.patch

# Fix for highway package build on ppc64le
Patch2005: 0001-PowerPC-Fix-handling-of-undefs-in-the-PPC-isSplatShu.patch
Patch2006: 0001-Add-REQUIRES-asserts-to-test-added-in-145149-because.patch

# Fix for offload builds: The DeviceRTL libraries target device code and
# don't support the mtls-dialect flag, so we need to patch the clang driver
# to ignore it for these targets.
Patch2101: 0001-clang-Add-a-hack-to-fix-the-offload-build-with-the-m.patch
Patch2201: 0001-clang-Add-a-hack-to-fix-the-offload-build-with-the-m.patch

# Fix segfault compiling plotters rust crate on ppc64le
Patch2104: 0001-PowerPC-Add-check-for-cast-when-shufflevector-172443.patch

# Fix for lldb python shell with python 3.14 (rbhz#2428608)
Patch2105: 43cb4631c1f42dbfce78288b8ae30b5840ed59b3.patch

# Fix for s390x vector miscompilation (rhbz#2430017)
Patch2106: 0001-SystemZ-Fix-code-in-widening-vector-multiplication-1.patch

%if 0%{?rhel} == 8
%global python3_pkgversion 3.12
%global __python3 /usr/bin/python3.12
%endif

%if %{with fastclang}
# fastclang depends on overriding default conditionals via
# bcond_override_default which is only available on RPM 4.20 and newer.
# More info:
# https://rpm-software-management.github.io/rpm/manual/conditionalbuilds.html#overriding-defaults
BuildRequires:	rpm >= 4.20
%endif
%if %{defined gts_version}
# Required for 64-bit atomics on i686.
BuildRequires: gcc-toolset-%{gts_version}-libatomic-devel
BuildRequires: gcc-toolset-%{gts_version}-gcc-c++
%endif
BuildRequires:	gcc
BuildRequires:	gcc-c++
%if %{defined host_clang_maj_ver}
BuildRequires:	clang(major) = %{host_clang_maj_ver}
%else
BuildRequires:	clang
%endif
BuildRequires:	cmake
BuildRequires:	chrpath
BuildRequires:	ninja-build
BuildRequires:	zlib-devel
BuildRequires:	libzstd-devel
BuildRequires:	libffi-devel
BuildRequires:	ncurses-devel

%if %{with pgo}
%if %{defined host_clang_maj_ver}
BuildRequires:	lld(major) = %{host_clang_maj_ver}
BuildRequires:	compiler-rt(major) = %{host_clang_maj_ver}
BuildRequires:	llvm(major) = %{host_clang_maj_ver}
%else
BuildRequires:	lld
BuildRequires:	compiler-rt
BuildRequires:	llvm
%endif

%else
%if %{with use_lld}
BuildRequires:	lld
%endif
%endif

# This intentionally does not use python3_pkgversion. RHEL 8 does not have
# python3.12-sphinx, and we are only using it as a binary anyway.
BuildRequires:	python3-sphinx
%if 0%{?rhel} != 8
# RHEL 8 does not have these packages for python3.12. However, they are only
# needed for LLDB tests.
BuildRequires:	python%{python3_pkgversion}-psutil
BuildRequires:	python%{python3_pkgversion}-pexpect
%endif
%if %{undefined rhel}
BuildRequires:	python%{python3_pkgversion}-myst-parser
%endif
# Needed for %%multilib_fix_c_header
BuildRequires:	multilib-rpm-config
%if %{with gold}
BuildRequires:	binutils-devel
%if %{undefined rhel} || 0%{?rhel} > 8
BuildRequires:	binutils-gold
%endif
%endif
%ifarch %{valgrind_arches}
# Enable extra functionality when run the LLVM JIT under valgrind.
BuildRequires:	valgrind-devel
%endif
%if %{with libedit}
# LLVM's LineEditor library will use libedit if it is available.
BuildRequires:	libedit-devel
%endif
# We need python3-devel for %%py3_shebang_fix
BuildRequires:	python%{python3_pkgversion}-devel
%if 0%{?rhel} == 8
BuildRequires:	python%{python3_pkgversion}-setuptools
BuildRequires:	python%{python3_pkgversion}-rpm-macros
%endif

# For gpg source verification
BuildRequires:	gnupg2

BuildRequires:	swig
BuildRequires:	libxml2-devel
BuildRequires:	doxygen

# For clang-offload-packager
BuildRequires: elfutils-libelf-devel
BuildRequires: perl
BuildRequires: perl-Data-Dumper
BuildRequires: perl-Encode
BuildRequires: libffi-devel

BuildRequires:	perl-generators

# According to https://fedoraproject.org/wiki/Packaging:Emacs a package
# should BuildRequires: emacs if it packages emacs integration files.
BuildRequires:	emacs

BuildRequires:	libatomic

# scan-build uses these perl modules so they need to be installed in order
# to run the tests.
BuildRequires: perl(Digest::MD5)
BuildRequires: perl(File::Copy)
BuildRequires: perl(File::Find)
BuildRequires: perl(File::Path)
BuildRequires: perl(File::Temp)
BuildRequires: perl(FindBin)
BuildRequires: perl(Hash::Util)
BuildRequires: perl(lib)
BuildRequires: perl(Term::ANSIColor)
BuildRequires: perl(Text::ParseWords)
BuildRequires: perl(Sys::Hostname)

%if %{with mlir}
BuildRequires: python%{python3_pkgversion}-numpy
BuildRequires: python%{python3_pkgversion}-pybind11
BuildRequires: python%{python3_pkgversion}-pyyaml
BuildRequires: python%{python3_pkgversion}-nanobind-devel
%endif

BuildRequires:	graphviz

# This is required because we need "ps" when running LLDB tests
BuildRequires: procps-ng

# For reproducible pyc file generation
# See https://docs.fedoraproject.org/en-US/packaging-guidelines/Python_Appendix/#_byte_compilation_reproducibility
# Since Fedora 41 this happens automatically, and RHEL 8 does not support this.
%if %{without compat_build} && (0%{?rhel} == 9 || 0%{?rhel} == 10)
BuildRequires: /usr/bin/marshalparser
%global py_reproducible_pyc_path %{buildroot}%{python3_sitelib}
%endif

Requires:	%{pkg_name_llvm}-libs%{?_isa} = %{version}-%{release}

Provides:	llvm(major) = %{maj_ver}

%description
LLVM is a compiler infrastructure designed for compile-time, link-time,
runtime, and idle-time optimization of programs from arbitrary programming
languages. The compiler infrastructure includes mirror sets of programming
tools as well as libraries with equivalent functionality.
#endregion main package

#region LLVM lit package
%if %{with python_lit}
%package -n python%{python3_pkgversion}-lit
Summary: LLVM lit test runner for Python 3

BuildArch: noarch
%if 0%{?rhel} == 8
# Became python3.12-clang in LLVM 19
Obsoletes: python3-lit < 18.9
%else
# This optional dependency is not available for python3.12 on RHEL 8.
Recommends: python%{python3_pkgversion}-psutil
%endif

%description -n python%{python3_pkgversion}-lit
lit is a tool used by the LLVM project for executing its test suites.
%endif
#endregion LLVM lit package

#region LLVM packages

%package -n %{pkg_name_llvm}-filesystem
Summary: Filesystem package that owns the versioned llvm prefix
# Was renamed immediately after introduction.
Obsoletes: %{pkg_name_llvm}-resource-filesystem < 20
%if %{with compat_build}
Conflicts: llvm-filesystem < %{maj_ver}.99
%endif

%description -n %{pkg_name_llvm}-filesystem
This packages owns the versioned llvm prefix directory: $libdir/llvm$version

%package -n %{pkg_name_llvm}-devel
Summary:	Libraries and header files for LLVM
Requires:	%{pkg_name_llvm}%{?_isa} = %{version}-%{release}
Requires:	%{pkg_name_llvm}-libs%{?_isa} = %{version}-%{release}
# The installed LLVM cmake files will add -ledit to the linker flags for any
# app that requires the libLLVMLineEditor, so we need to make sure
# libedit-devel is available.
%if %{with libedit}
Requires:	libedit-devel
%endif
Requires:	libzstd-devel
# The installed cmake files reference binaries from llvm-test, llvm-static, and
# llvm-gtest.  We tried in the past to split the cmake exports for these binaries
# out into separate files, so that llvm-devel would not need to Require these packages,
# but this caused bugs (rhbz#1773678) and forced us to carry two non-upstream
# patches.
Requires:	%{pkg_name_llvm}-static%{?_isa} = %{version}-%{release}
Requires:	%{pkg_name_llvm}-test%{?_isa} = %{version}-%{release}
Requires:	%{pkg_name_llvm}-googletest%{?_isa} = %{version}-%{release}


Requires(post):	alternatives
Requires(postun):	alternatives

Provides:	llvm-devel(major) = %{maj_ver}

%description -n %{pkg_name_llvm}-devel
This package contains library and header files needed to develop new native
programs that use the LLVM infrastructure.

%package -n %{pkg_name_llvm}-doc
Summary:	Documentation for LLVM
BuildArch:	noarch
Requires:	%{pkg_name_llvm} = %{version}-%{release}

%description -n %{pkg_name_llvm}-doc
Documentation for the LLVM compiler infrastructure.

%package -n %{pkg_name_llvm}-libs
Summary:	LLVM shared libraries
Requires:	%{pkg_name_llvm}-filesystem%{?_isa} = %{version}-%{release}

%description -n %{pkg_name_llvm}-libs
Shared libraries for the LLVM compiler infrastructure.

%package -n %{pkg_name_llvm}-static
Summary:	LLVM static libraries
Requires:	%{pkg_name_llvm}-filesystem%{?_isa} = %{version}-%{release}
Conflicts:	%{pkg_name_llvm}-devel < 8

Provides:	llvm-static(major) = %{maj_ver}

%description -n %{pkg_name_llvm}-static
Static libraries for the LLVM compiler infrastructure.

%package -n %{pkg_name_llvm}-cmake-utils
Summary: CMake utilities shared across LLVM subprojects
Requires: %{pkg_name_llvm}-filesystem%{?_isa} = %{version}-%{release}

%description -n %{pkg_name_llvm}-cmake-utils
CMake utilities shared across LLVM subprojects.
This is for internal use by LLVM packages only.

%package -n %{pkg_name_llvm}-test
Summary:	LLVM regression tests
Requires:	%{pkg_name_llvm}%{?_isa} = %{version}-%{release}
Requires:	%{pkg_name_llvm}-libs%{?_isa} = %{version}-%{release}

Provides:	llvm-test(major) = %{maj_ver}

%description -n %{pkg_name_llvm}-test
LLVM regression tests.

%package -n %{pkg_name_llvm}-googletest
Requires: %{pkg_name_llvm}-filesystem%{?_isa} = %{version}-%{release}
Summary: LLVM's modified googletest sources

%description -n %{pkg_name_llvm}-googletest
LLVM's modified googletest sources.

%if %{with snapshot_build}
%package -n %{pkg_name_llvm}-build-stats
Summary: Statistics for the RPM build

%description -n %{pkg_name_llvm}-build-stats
Statistics for the RPM build. Only available in snapshot builds.
%endif

#endregion LLVM packages

#region CLANG packages

%package -n %{pkg_name_clang}
Summary:	A C language family front-end for LLVM

Requires:	%{pkg_name_clang}-libs%{?_isa} = %{version}-%{release}

# clang requires gcc, clang++ requires libstdc++-devel
# - https://bugzilla.redhat.com/show_bug.cgi?id=1021645
# - https://bugzilla.redhat.com/show_bug.cgi?id=1158594
Requires:	libstdc++-devel
Requires:	gcc-c++

Provides:	clang(major) = %{maj_ver}

Conflicts:	compiler-rt < 11.0.0

%description -n %{pkg_name_clang}
clang: noun
    1. A loud, resonant, metallic sound.
    2. The strident call of a crane or goose.
    3. C-language family front-end toolkit.

The goal of the Clang project is to create a new C, C++, Objective C
and Objective C++ front-end for the LLVM compiler. Its tools are built
as libraries and designed to be loosely-coupled and extensible.

Install compiler-rt if you want the Blocks C language extension or to
enable sanitization and profiling options when building, and
libomp-devel to enable -fopenmp.

%package -n %{pkg_name_clang}-libs
Summary: Runtime library for clang
Requires: %{pkg_name_clang}-resource-filesystem%{?_isa} = %{version}-%{release}
%if %{defined gts_version}
Requires: gcc-toolset-%{gts_version}-gcc-c++
%endif
Recommends: %{pkg_name_compiler_rt}%{?_isa} = %{version}-%{release}
Requires: %{pkg_name_llvm}-libs = %{version}-%{release}
# atomic support is not part of compiler-rt
%if %{defined gts_version}
Recommends: gcc-toolset-%{gts_version}-libatomic-devel
%else
Recommends: libatomic%{?_isa}
%endif
# libomp-devel is required, so clang can find the omp.h header when compiling
# with -fopenmp.
Recommends: %{pkg_name_libomp}-devel%{_isa} = %{version}-%{release}
Recommends: %{pkg_name_libomp}%{_isa} = %{version}-%{release}

%description -n %{pkg_name_clang}-libs
Runtime library for clang.

%package -n %{pkg_name_clang}-devel
Summary: Development header files for clang
Requires: %{pkg_name_clang}-libs = %{version}-%{release}
Requires: %{pkg_name_clang}%{?_isa} = %{version}-%{release}
# The clang CMake files reference tools from clang-tools-extra.
Requires: %{pkg_name_clang}-tools-extra%{?_isa} = %{version}-%{release}
# The clang cmake package depends on the LLVM cmake package.
Requires: %{pkg_name_llvm}-devel%{?_isa} = %{version}-%{release}
Provides: clang-devel(major) = %{maj_ver}
# For the clangd language server contained in this subpackage,
# add a Provides so users can just run "dnf install clangd."
# This Provides is only present in the primary, unversioned clang package.
# Users who want the compat versions can install them using the full name.
%if %{without compat_build}
Provides: clangd = %{version}-%{release}
%endif

%description -n %{pkg_name_clang}-devel
Development header files for clang.

%package -n %{pkg_name_clang}-resource-filesystem
Summary: Filesystem package that owns the clang resource directory
Provides: clang-resource-filesystem(major) = %{maj_ver}
%if %{with compat_build}
Conflicts: clang-resource-filesystem < %{maj_ver}.99
%endif

%description -n %{pkg_name_clang}-resource-filesystem
This package owns the clang resouce directory: $libdir/clang/$version/

%package -n %{pkg_name_clang}-analyzer
Summary:	A source code analysis framework
License:	Apache-2.0 WITH LLVM-exception OR NCSA OR MIT
Requires:	%{pkg_name_clang} = %{version}-%{release}

%description -n %{pkg_name_clang}-analyzer
The Clang Static Analyzer consists of both a source code analysis
framework and a standalone tool that finds bugs in C and Objective-C
programs. The standalone tool is invoked from the command-line, and is
intended to run in tandem with a build of a project or code base.

%package -n %{pkg_name_clang}-tools-extra
Summary:	Extra tools for clang
Requires:	%{pkg_name_clang}-libs%{?_isa} = %{version}-%{release}
Requires:	emacs-filesystem

%description -n %{pkg_name_clang}-tools-extra
A set of extra tools built using Clang's tooling API.

%package -n %{pkg_name_clang}-tools-extra-devel
Summary: Development header files for clang tools
Requires: %{pkg_name_clang}-tools-extra = %{version}-%{release}

%description -n %{pkg_name_clang}-tools-extra-devel
Development header files for clang tools.

# Put git-clang-format in its own package, because it Requires git
# and we don't want to force users to install all those dependenices if they
# just want clang.
%package -n git-clang-format%{pkg_suffix}
Summary:	Integration of clang-format for git
Requires:	%{pkg_name_clang}-tools-extra = %{version}-%{release}
Requires:	git
Requires:	python%{python3_pkgversion}

%description -n git-clang-format%{pkg_suffix}
clang-format integration for git.

%if %{without compat_build}
%package -n python%{python3_pkgversion}-clang
Summary:       Python3 bindings for clang
Requires:      %{pkg_name_clang}-devel%{?_isa} = %{version}-%{release}
Requires:      python%{python3_pkgversion}
%if 0%{?rhel} == 8
# Became python3.12-clang in LLVM 19
Obsoletes: python3-clang < 18.9
%endif
%description -n python%{python3_pkgversion}-clang
Python3 bindings for clang.


%endif

#endregion CLANG packages

#region COMPILER-RT packages

%package -n %{pkg_name_compiler_rt}
Summary:	LLVM "compiler-rt" runtime libraries

License:	Apache-2.0 WITH LLVM-exception OR NCSA OR MIT

Requires: %{pkg_name_clang}-resource-filesystem%{?_isa} = %{version}-%{release}
Provides: compiler-rt(major) = %{maj_ver}

%description -n %{pkg_name_compiler_rt}
The compiler-rt project is a part of the LLVM project. It provides
implementation of the low-level target-specific hooks required by
code generation, sanitizer runtimes and profiling library for code
instrumentation, and Blocks C language extension.

#endregion COMPILER-RT packages

#region OPENMP packages

%package -n %{pkg_name_libomp}
Summary: OpenMP runtime for clang

URL: http://openmp.llvm.org

Requires: %{pkg_name_llvm}-libs%{?_isa} = %{version}-%{release}
Requires: elfutils-libelf%{?_isa}

Provides: libomp(major) = %{maj_ver}

%description -n %{pkg_name_libomp}
OpenMP runtime for clang.

%package  -n %{pkg_name_libomp}-devel
Summary: OpenMP header files

URL: http://openmp.llvm.org

Requires: %{pkg_name_libomp}%{?_isa} = %{version}-%{release}
Requires: %{pkg_name_clang}-resource-filesystem%{?_isa} = %{version}-%{release}

Provides: libomp-devel(major) = %{maj_ver}

%description  -n %{pkg_name_libomp}-devel
OpenMP header files.
URL: http://openmp.llvm.org

#endregion OPENMP packages

#region LLD packages

%package -n %{pkg_name_lld}
Summary:	The LLVM Linker

Requires(post): alternatives
Requires(preun): alternatives

Requires: %{pkg_name_lld}-libs = %{version}-%{release}
Provides: lld(major) = %{maj_ver}

%description -n %{pkg_name_lld}
The LLVM project linker.

%package -n %{pkg_name_lld}-devel
Summary:	Libraries and header files for LLD
Requires: %{pkg_name_lld}-libs%{?_isa} = %{version}-%{release}
%if %{without compat_build}
# lld tools are referenced in the cmake files, so we need to add lld as a
# dependency.
Requires: %{pkg_name_lld}%{?_isa} = %{version}-%{release}
%endif
Provides: lld-devel(major) = %{maj_ver}

%description -n %{pkg_name_lld}-devel
This package contains library and header files needed to develop new native
programs that use the LLD infrastructure.

%package -n %{pkg_name_lld}-libs
Summary:	LLD shared libraries

Requires:	%{pkg_name_llvm}-libs%{?_isa} = %{version}-%{release}

%description -n %{pkg_name_lld}-libs
Shared libraries for LLD.

#endregion LLD packages

#region Toolset package
%if 0%{?rhel}
%package -n %{pkg_name_llvm}-toolset
Summary:	Package that installs llvm-toolset
Requires:	%{pkg_name_clang} = %{version}-%{release}
Requires:	%{pkg_name_llvm} = %{version}-%{release}
Requires:	%{pkg_name_lld} = %{version}-%{release}

%description -n %{pkg_name_llvm}-toolset
This is the main package for llvm-toolset.
%endif
#endregion Toolset package

#region LLDB packages
%if %{with lldb}
%package -n %{pkg_name_lldb}
Summary:	Next generation high-performance debugger
License:	Apache-2.0 WITH LLVM-exception OR NCSA
URL:		http://lldb.llvm.org/

Requires:	%{pkg_name_clang}-libs%{?_isa} = %{version}-%{release}
%if %{without compat_build}
Requires:	python%{python3_pkgversion}-lldb
%endif

%description -n %{pkg_name_lldb}
LLDB is a next generation, high-performance debugger. It is built as a set
of reusable components which highly leverage existing libraries in the
larger LLVM Project, such as the Clang expression parser and LLVM
disassembler.

%package -n %{pkg_name_lldb}-devel
Summary:	Development header files for LLDB
Requires:	%{pkg_name_lldb}%{?_isa} = %{version}-%{release}

%description -n %{pkg_name_lldb}-devel
The package contains header files for the LLDB debugger.

%if %{without compat_build}
%package -n python%{python3_pkgversion}-lldb
Summary:	Python module for LLDB

Requires:	%{pkg_name_lldb}%{?_isa} = %{version}-%{release}

%if 0%{?rhel} == 8
# Became python3.12-lldb in LLVM 19
Obsoletes: python3-lldb < 18.9
%endif

%description -n python%{python3_pkgversion}-lldb
The package contains the LLDB Python module.
%endif
%endif
#endregion LLDB packages

#region MLIR packages
%if %{with mlir}
%package -n %{pkg_name_mlir}
Summary:	Multi-Level Intermediate Representation Overview
License:	Apache-2.0 WITH LLVM-exception
URL:		http://mlir.llvm.org
Requires: %{pkg_name_llvm}-libs = %{version}-%{release}

%description -n %{pkg_name_mlir}
The MLIR project is a novel approach to building reusable and extensible
compiler infrastructure. MLIR aims to address software fragmentation,
improve compilation for heterogeneous hardware, significantly reduce
the cost of building domain specific compilers, and aid in connecting
existing compilers together.

%package -n %{pkg_name_mlir}-static
Summary:	MLIR static files
Requires:	%{pkg_name_mlir}%{?_isa} = %{version}-%{release}

%description -n %{pkg_name_mlir}-static
MLIR static files.

%package -n %{pkg_name_mlir}-devel
Summary:	MLIR development files
Requires: %{pkg_name_mlir}%{?_isa} = %{version}-%{release}
Requires: %{pkg_name_mlir}-static%{?_isa} = %{version}-%{release}

%description -n %{pkg_name_mlir}-devel
MLIR development files.

%package -n python%{python3_pkgversion}-mlir
Summary:	MLIR python bindings

Requires: python%{python3_pkgversion}
Requires: python%{python3_pkgversion}-numpy

%description -n python%{python3_pkgversion}-mlir
MLIR python bindings.
%endif
#endregion MLIR packages

#region libcxx packages
%if %{with libcxx}
%package -n %{pkg_name_libcxx}
Summary:	C++ standard library targeting C++11
License:	Apache-2.0 WITH LLVM-exception OR MIT OR NCSA
URL:		http://libcxx.llvm.org/

Requires: %{pkg_name_libcxxabi}%{?_isa} = %{version}-%{release}

%description -n %{pkg_name_libcxx}
libc++ is a new implementation of the C++ standard library, targeting C++11 and above.


%package -n %{pkg_name_libcxx}-devel
Summary:	Headers and libraries for %{pkg_name_libcxx} devel
Requires:	%{pkg_name_libcxx}%{?_isa} = %{version}-%{release}
Requires:	%{pkg_name_libcxxabi}-devel

%description -n %{pkg_name_libcxx}-devel
Headers and libraries for %{pkg_name_libcxx} devel.

%package -n %{pkg_name_libcxx}-static
Summary:	Static libraries for %{pkg_name_libcxx}

%description -n %{pkg_name_libcxx}-static
Static libraries for %{pkg_name_libcxx}.

%package -n %{pkg_name_libcxxabi}
Summary:	Low level support for a standard C++ library

%description -n %{pkg_name_libcxxabi}
libcxxabi provides low level support for a standard C++ library.

%package -n %{pkg_name_libcxx}abi-devel
Summary:	Headers and libraries for %{pkg_name_libcxxabi} devel
Requires:	%{pkg_name_libcxxabi}%{?_isa} = %{version}-%{release}

%description -n %{pkg_name_libcxxabi}-devel
Headers and libraries for %{pkg_name_libcxxabi} devel.

%package -n %{pkg_name_libcxxabi}-static
Summary:	Static libraries for %{pkg_name_libcxxabi}

%description -n %{pkg_name_libcxxabi}-static
Static libraries for %{pkg_name_libcxxabi}.

%package -n %{pkg_name_llvm_libunwind}
Summary:    LLVM libunwind

%description -n %{pkg_name_llvm_libunwind}

LLVM libunwind is an implementation of the interface defined by the HP libunwind
project. It was contributed Apple as a way to enable clang++ to port to
platforms that do not have a system unwinder. It is intended to be a small and
fast implementation of the ABI, leaving off some features of HP's libunwind
that never materialized (e.g. remote unwinding).

%package -n %{pkg_name_llvm_libunwind}-devel
Summary:    LLVM libunwind development files
Provides:   %{pkg_name_llvm_libunwind}(major) = %{maj_ver}
Requires:   %{pkg_name_llvm_libunwind}%{?_isa} = %{version}-%{release}

%description -n %{pkg_name_llvm_libunwind}-devel
Unversioned shared library for LLVM libunwind

%package -n %{pkg_name_llvm_libunwind}-static
Summary: Static library for LLVM libunwind

%description -n %{pkg_name_llvm_libunwind}-static
Static library for LLVM libunwind.

%endif
#endregion libcxx packages

#region BOLT packages
%if %{with build_bolt}
%package -n %{pkg_name_bolt}
Summary:	A post-link optimizer developed to speed up large applications
License:	Apache-2.0 WITH LLVM-exception
URL:		https://github.com/llvm/llvm-project/tree/main/bolt
Requires:	%{pkg_name_llvm}-filesystem%{?_isa} = %{version}-%{release}

# As hinted by bolt documentation
Recommends:     gperftools-devel

%description -n %{pkg_name_bolt}

BOLT is a post-link optimizer developed to speed up large applications.
It achieves the improvements by optimizing application's code layout based on
execution profile gathered by sampling profiler, such as Linux `perf` tool.
%endif
#endregion BOLT packages

#region polly packages
%if %{with polly}
%package -n %{pkg_name_polly}
Summary:	LLVM Framework for High-Level Loop and Data-Locality Optimizations
License:	Apache-2.0 WITH LLVM-exception
URL:	http://polly.llvm.org
Requires: %{pkg_name_llvm}-libs = %{version}-%{release}

# We no longer ship polly-doc.
Obsoletes: %{pkg_name_polly}-doc < 20

%description -n %{pkg_name_polly}

Polly is a high-level loop and data-locality optimizer and optimization
infrastructure for LLVM. It uses an abstract mathematical representation based
on integer polyhedron to analyze and optimize the memory access pattern of a
program.

%package -n %{pkg_name_polly}-devel
Summary: Polly header files
Requires: %{pkg_name_polly} = %{version}-%{release}

%description  -n %{pkg_name_polly}-devel
Polly header files.
%endif
#endregion polly packages

#region flang packages
%if %{with flang}
%package -n %{pkg_name_flang}
Summary: a Fortran language front-end designed for integration with LLVM
Requires: %{pkg_name_flang}-runtime%{?_isa} = %{version}-%{release}
# flang installs headers in the clang resource directory
Requires: %{pkg_name_clang}-resource-filesystem%{?_isa} = %{version}-%{release}
# flang implicitly calls ld.bfd when linking and depends on the gcc runtime objects.
Requires: binutils
Requires: gcc
# Up to version 17.0.6-1, flang used to provide a flang-devel package.
# This changed in 17.0.6-2 and all development-related files are now
# distributed in the main flang package.
Obsoletes: %{pkg_name_flang}-devel < 17.0.6-2

# We no longer ship flang-doc.
Obsoletes: %{pkg_name_flang}-doc < 22

License: Apache-2.0 WITH LLVM-exception
URL:     https://flang.llvm.org

%description -n %{pkg_name_flang}

Flang is a ground-up implementation of a Fortran front end written in modern
C++.

%package -n %{pkg_name_flang}-runtime
Summary: Flang runtime libraries
Conflicts: %{pkg_name_flang} < 17.0.6-2

%description -n %{pkg_name_flang}-runtime
Flang runtime libraries.

%endif
#endregion flang packages

#endregion packages

#region prep
%prep
%if %{without snapshot_build}
# llvm
%{gpgverify} --keyring='%{SOURCE6}' --signature='%{SOURCE1}' --data='%{SOURCE0}'
%endif

%if %{with bundle_compat_lib}
%{gpgverify} --keyring='%{SOURCE6}' --signature='%{SOURCE3001}' --data='%{SOURCE3000}'
%setup -T -q -b 3000 -n llvm-project-%{compat_ver}.src

# Apply all patches with number < 500 (unconditionally)
# See https://rpm-software-management.github.io/rpm/manual/autosetup.html
%autopatch -M499 -p1

# automatically apply patches based on LLVM version
%autopatch -m%{compat_maj_ver}00 -M%{compat_maj_ver}99 -p1

%endif

# -T     : Do Not Perform Default Archive Unpacking (without this, the <n>th source would be unpacked twice)
# -b <n> : Unpack The nth Sources Before Changing Directory
# -n     : Set Name of Build Directory
#
# see http://ftp.rpm.org/max-rpm/s1-rpm-inside-macros.html
%autosetup -N -T -b 0 -n %{src_tarball_dir}

# Apply all patches with number < 500 (unconditionally)
# See https://rpm-software-management.github.io/rpm/manual/autosetup.html
%autopatch -M499 -p1

# automatically apply patches based on LLVM version
%autopatch -m%{maj_ver}00 -M%{maj_ver}99 -p1

%if %{defined rhel} && 0%{?rhel} == 8
%patch -p1 -P501
%if %{maj_ver} < 22
# The following patches have been backported from LLVM 22.
%patch -p1 -P502
%patch -p1 -P503
%patch -p1 -P504
%endif
%endif

#region LLVM preparation

%py3_shebang_fix \
	llvm/test/BugPoint/compile-custom.ll.py \
	llvm/tools/opt-viewer/*.py \
	llvm/utils/update_cc_test_checks.py

#endregion LLVM preparation

#region CLANG preparation

%py3_shebang_fix \
	clang-tools-extra/clang-tidy/tool/ \
	clang-tools-extra/clang-include-fixer/find-all-symbols/tool/run-find-all-symbols.py

%py3_shebang_fix \
	clang/tools/clang-format/ \
	clang/tools/clang-format/git-clang-format \
	clang/utils/hmaptool/hmaptool \
	clang/tools/scan-view/bin/scan-view \
	clang/tools/scan-view/share/Reporter.py \
	clang/tools/scan-view/share/startfile.py \
	clang/tools/scan-build-py/bin/* \
	clang/tools/scan-build-py/libexec/*

#endregion CLANG preparation

#region COMPILER-RT preparation

%py3_shebang_fix compiler-rt/lib/hwasan/scripts/hwasan_symbolize

#endregion COMPILER-RT preparation

#region lldb preparation
# Compat builds don't build python bindings, but should still build man pages.
%if %{with compat_build}
sed -i 's/LLDB_ENABLE_PYTHON/TRUE/' lldb/docs/CMakeLists.txt
%endif
#endregion

#region libcxx preparation
%if %{with libcxx}
%py3_shebang_fix libcxx/utils/
%endif
#endregion libcxx preparation

#endregion prep

#region python buildrequires
%if %{with python_lit}
%if 0%{?rhel} != 8
%generate_buildrequires

cd llvm/utils/lit
%pyproject_buildrequires
%endif
%endif
#endregion python buildrequires

#region build
%build
# TODO(kkleine): In clang we had this %ifarch s390 s390x aarch64 %ix86 ppc64le
# Decrease debuginfo verbosity to reduce memory consumption during final library linking.
%global reduce_debuginfo 0
%ifarch %ix86
%global reduce_debuginfo 1
%endif
%if 0%{?rhel} == 8 || %{with fastclang}
%global reduce_debuginfo 1
%endif

%if %reduce_debuginfo == 1
# Decrease debuginfo verbosity to reduce memory consumption during final library linking
%global optflags %(echo %{optflags} | sed 's/-g /-g1 /')
%endif

%global projects clang;clang-tools-extra;lld
%global runtimes compiler-rt;openmp

%if %{with lldb}
%global projects %{projects};lldb
%endif

%if %{with mlir}
%global projects %{projects};mlir
%endif

%if %{with build_bolt}
%global projects %{projects};bolt
%endif

%if %{with polly}
%global projects %{projects};polly
%endif

%if %{with flang}
%global projects %{projects};flang
%global runtimes %{runtimes};flang-rt
%endif

%if %{with libcxx}
%global runtimes %{runtimes};libcxx;libcxxabi;libunwind
%endif

%if %{with offload}
%global runtimes %{runtimes};offload
%endif

%global gcc_triple --gcc-triple=%{_target_cpu}-redhat-linux

%global cfg_file_content %{gcc_triple}
%global cfg_file_content_flang %{gcc_triple}

# We want to use DWARF-5 on all snapshot builds.
%if %{without snapshot_build} && %{defined rhel} && 0%{?rhel} < 10
%global cfg_file_content %{cfg_file_content} -gdwarf-4 -g0
%endif

%if %{defined gts_version}
%global cfg_file_content %{cfg_file_content} --gcc-install-dir=/opt/rh/gcc-toolset-%{gts_version}/root/%{_exec_prefix}/lib/gcc/%{_target_cpu}-redhat-linux/%{gts_version}
%endif

# Already use the new clang config file for the current build. This ensures
# consistency between the runtimes and non-runtimes builds and makes sure that
# the new configuration will work without going through a rebuild cycle.
# Don't do this on RHEL 8, which does not build using clang.
%if %{defined gts_version} && 0%{?rhel} != 8
echo "%{cfg_file_content}" > /tmp/clang.cfg
%global optflags  %{optflags} --config /tmp/clang.cfg
%endif

# Copy CFLAGS into ASMFLAGS, so -fcf-protection is used when compiling assembly files.
export ASMFLAGS="%{build_cflags}"

# We set CLANG_DEFAULT_PIE_ON_LINUX=OFF and PPC_LINUX_DEFAULT_IEEELONGDOUBLE=ON to match the
# defaults used by Fedora's GCC.

# Disable dwz on aarch64, because it takes a huge amount of time to decide not to optimize things.
# This is copied from clang.
%ifarch aarch64
%define _find_debuginfo_dwz_opts %{nil}
%endif

cd llvm

# Remember old values to reset to
OLD_PATH="$PATH"
OLD_LD_LIBRARY_PATH="$LD_LIBRARY_PATH"
OLD_CWD="$PWD"

%global builddir_instrumented $RPM_BUILD_DIR/instrumented-llvm

#region LLVM lit
%if %{with python_lit}
pushd utils/lit
%if 0%{?rhel} == 8
%py3_build
%else
%pyproject_wheel
%endif
popd
%endif
#endregion LLVM lit

%if 0%{?rhel} == 8
%undefine __cmake_in_source_build
%endif

#region cmake options

# Common cmake arguments used by both the normal build and bundle_compat_lib.
# Any ABI-affecting flags should be in here.
%global cmake_common_args \\\
    -DCMAKE_BUILD_TYPE=RelWithDebInfo \\\
    -DLLVM_ENABLE_RTTI=ON \\\
    -DLLVM_USE_PERF=ON \\\
    -DLLVM_TARGETS_TO_BUILD=%{targets_to_build} \\\
    -DBUILD_SHARED_LIBS=OFF \\\
    -DLLVM_BUILD_LLVM_DYLIB=ON \\\
    -DLLVM_LINK_LLVM_DYLIB=ON \\\
    -DCLANG_LINK_CLANG_DYLIB=ON \\\
    -DLLVM_ENABLE_FFI:BOOL=ON

%if %{maj_ver} >= 22
%global cmake_common_args %{cmake_common_args} \\\
    -DLLVM_ENABLE_EH=OFF
%else
%global cmake_common_args %{cmake_common_args} \\\
    -DLLVM_ENABLE_EH=ON
%endif

%if 0%{?rhel} == 8
# On RHEL 8 we build with gcc, but the runtimes are built with the just built
# clang, so we need to pass clang supported compiler flags to the runtimes
# build.  If we pass the gcc flags, some of the cmake feature checkes will
# fail, because they use -Werror and emit an error when passed gcc specific
# compiler flags like -specs.
# Specifically, this is required in order to fix the libomptest.so build.

function strip_specs {
  echo $1 | sed -e 's/-specs=[^ ]\+//g'
}

CLANG_CC_CONFIG=$(pwd)/redhat-hardened-clang.cfg
CLANG_LD_CONFIG=$(pwd)/redhat-hardened-clang-ld.cfg
echo "-fPIE" >> $CLANG_CC_CONFIG
echo "-pie" >> $CLANG_LD_CONFIG
CLANG_CCFLAGS_EXTRA=--config=$CLANG_CC_CONFIG
CLANG_LDFLAGS_EXTRA=--config=$CLANG_LD_CONFIG

CLANG_CXXFLAGS=$(strip_specs "$CXXFLAGS $CLANG_CCFLAGS_EXTRA")
CLANG_CFLAGS=$(strip_specs "$CFLAGS $CLANG_CCFLAGS_EXTRA")
CLANG_LDFLAGS=$(strip_specs "$LDFLAGS $CLANG_LDFLAGS_EXTRA")
%global cmake_common_args %{cmake_common_args} \\\
    -DRUNTIMES_CMAKE_ARGS="-DCMAKE_C_FLAGS=$CLANG_C_FLAGS;-DCMAKE_CXX_FLAGS=$CLANG_CXX_FLAGS;-DCMAKE_SHARED_LINKER_FLAGS=$CLANG_LD_FLAGS"
%endif

%if %reduce_debuginfo == 1
	%global cmake_common_args %{cmake_common_args} -DCMAKE_C_FLAGS_RELWITHDEBINFO="%{optflags} -DNDEBUG"
	%global cmake_common_args %{cmake_common_args} -DCMAKE_CXX_FLAGS_RELWITHDEBINFO="%{optflags} -DNDEBUG"
%endif

%global cmake_config_args %{cmake_common_args}

#region clang options
%global cmake_config_args %{cmake_config_args} \\\
	-DCLANG_BUILD_EXAMPLES:BOOL=OFF \\\
	-DCLANG_CONFIG_FILE_SYSTEM_DIR=%{_sysconfdir}/%{pkg_name_clang}/ \\\
	-DCLANG_DEFAULT_PIE_ON_LINUX=OFF \\\
	-DCLANG_DEFAULT_UNWINDLIB=libgcc \\\
	-DCLANG_ENABLE_ARCMT:BOOL=ON \\\
	-DCLANG_ENABLE_STATIC_ANALYZER:BOOL=ON \\\
	-DCLANG_INCLUDE_DOCS:BOOL=ON \\\
	-DCLANG_INCLUDE_TESTS:BOOL=ON \\\
	-DCLANG_PLUGIN_SUPPORT:BOOL=ON \\\
	-DCLANG_REPOSITORY_STRING="%{?dist_vendor} %{version}-%{release}" \\\
	-DLLVM_EXTERNAL_CLANG_TOOLS_EXTRA_SOURCE_DIR=../clang-tools-extra

%if %{with compat_build}
%global cmake_config_args %{cmake_config_args} \\\
	-DCLANG_RESOURCE_DIR=../../../lib/clang/%{maj_ver}
%else
%global cmake_config_args %{cmake_config_args} \\\
	-DCLANG_RESOURCE_DIR=../lib/clang/%{maj_ver}
%endif
#endregion clang options

#region compiler-rt options
%global cmake_config_args %{cmake_config_args} \\\
	-DCOMPILER_RT_INCLUDE_TESTS:BOOL=OFF \\\
	-DCOMPILER_RT_INSTALL_PATH=%{_prefix}/lib/clang/%{maj_ver} \\\
	-DLLVM_BUILD_EXTERNAL_COMPILER_RT:BOOL=ON
#endregion compiler-rt options

#region docs options

# Add all *enabled* documentation targets (no doxygen but sphinx)
%global cmake_config_args %{cmake_config_args} \\\
	-DLLVM_ENABLE_DOXYGEN:BOOL=OFF \\\
	-DLLVM_ENABLE_SPHINX:BOOL=ON \\\
	-DLLVM_BUILD_DOCS:BOOL=ON

# Configure sphinx:
# Build man-pages but no HTML docs using sphinx
%global cmake_config_args %{cmake_config_args} \\\
	-DSPHINX_EXECUTABLE=/usr/bin/sphinx-build-3 \\\
	-DSPHINX_OUTPUT_HTML:BOOL=OFF \\\
	-DSPHINX_OUTPUT_MAN:BOOL=ON \\\
	-DSPHINX_WARNINGS_AS_ERRORS=OFF
#endregion docs options

#region lldb options
%if %{with lldb}
%if %{with compat_build}
	%global cmake_config_args %{cmake_config_args} -DLLDB_ENABLE_PYTHON=OFF
%endif
%ifarch ppc64le
	%global cmake_config_args %{cmake_config_args} -DLLDB_TEST_USER_ARGS=--skip-category=watchpoint
%endif
%if 0%{?rhel} == 8
	%global cmake_config_args %{cmake_config_args} -DLLDB_INCLUDE_TESTS:BOOL=OFF
%else
	%global cmake_config_args %{cmake_config_args} -DLLDB_ENFORCE_STRICT_TEST_REQUIREMENTS:BOOL=ON
%endif
%endif
#endregion lldb options

#region libcxx options
%if %{with libcxx}
%global cmake_config_args %{cmake_config_args}  \\\
	-DCMAKE_POSITION_INDEPENDENT_CODE=ON \\\
	-DLIBCXX_INCLUDE_BENCHMARKS=OFF \\\
	-DLIBCXX_STATICALLY_LINK_ABI_IN_STATIC_LIBRARY=ON \\\
	-DLIBCXX_ENABLE_ABI_LINKER_SCRIPT=ON \\\
	-DLIBCXXABI_USE_LLVM_UNWINDER=OFF \\\
	-DLIBUNWIND_INSTALL_INCLUDE_DIR=%{_includedir}/llvm-libunwind

# If we don't set the .._INSTALL_LIBRARY_DIR variables,
# the *.so files will be placed in a subdirectory that includes the triple
%global cmake_config_args %{cmake_config_args}  \\\
	-DLIBCXX_INSTALL_LIBRARY_DIR=%{_libdir} \\\
	-DLIBCXXABI_INSTALL_LIBRARY_DIR=%{_libdir} \\\
	-DLIBUNWIND_INSTALL_LIBRARY_DIR=%{_libdir}

# If we don't adjust this, we will install into this unwanted location:
# /usr/include/i686-redhat-linux-gnu/c++/v1/__config_site
%global cmake_config_args %{cmake_config_args}  \\\
  -DLIBCXX_INSTALL_INCLUDE_TARGET_DIR=%{_includedir}/c++/v1 \\\
  -DLIBCXX_INSTALL_INCLUDE_DIR=%{_includedir}/c++/v1 \\\
  -DLIBCXX_INSTALL_MODULES_DIR=%{_datadir}/libc++/v1 \\\
  -DLIBCXXABI_INSTALL_INCLUDE_DIR=%{_includedir}/c++/v1

%endif
#endregion libcxx options

#region llvm options
%global cmake_config_args %{cmake_config_args}  \\\
	-DLLVM_APPEND_VC_REV:BOOL=OFF \\\
	-DLLVM_BUILD_EXAMPLES:BOOL=OFF \\\
	-DLLVM_BUILD_RUNTIME:BOOL=ON \\\
	-DLLVM_BUILD_TOOLS:BOOL=ON \\\
	-DLLVM_BUILD_UTILS:BOOL=ON \\\
	-DLLVM_DEFAULT_TARGET_TRIPLE=%{llvm_triple} \\\
	-DLLVM_ENABLE_LIBCXX:BOOL=OFF \\\
	-DLLVM_ENABLE_PER_TARGET_RUNTIME_DIR=ON \\\
	-DLLVM_ENABLE_PROJECTS="%{projects}" \\\
	-DLLVM_ENABLE_RUNTIMES="%{runtimes}" \\\
	-DLLVM_ENABLE_ZLIB:BOOL=FORCE_ON \\\
	-DLLVM_ENABLE_ZSTD:BOOL=FORCE_ON \\\
	-DLLVM_EXPERIMENTAL_TARGETS_TO_BUILD=%{experimental_targets_to_build} \\\
	-DLLVM_INCLUDE_BENCHMARKS=OFF \\\
	-DLLVM_INCLUDE_EXAMPLES:BOOL=OFF \\\
	-DLLVM_INCLUDE_TOOLS:BOOL=ON \\\
	-DLLVM_INCLUDE_UTILS:BOOL=ON \\\
	-DLLVM_INSTALL_TOOLCHAIN_ONLY:BOOL=OFF \\\
	-DLLVM_INSTALL_UTILS:BOOL=ON \\\
	-DLLVM_PARALLEL_LINK_JOBS=1 \\\
	-DLLVM_TOOLS_INSTALL_DIR:PATH=bin \\\
	-DLLVM_UNREACHABLE_OPTIMIZE:BOOL=OFF \\\
	-DLLVM_UTILS_INSTALL_DIR:PATH=bin
#endregion llvm options

#region mlir options
%if %{with mlir}
%global cmake_config_args %{cmake_config_args} \\\
        -DMLIR_INCLUDE_DOCS:BOOL=ON \\\
        -DMLIR_INCLUDE_TESTS:BOOL=ON \\\
        -DMLIR_INCLUDE_INTEGRATION_TESTS:BOOL=OFF \\\
        -DMLIR_INSTALL_AGGREGATE_OBJECTS=OFF \\\
        -DMLIR_BUILD_MLIR_C_DYLIB=ON \\\
        -DMLIR_ENABLE_BINDINGS_PYTHON:BOOL=ON

%endif
#endregion mlir options

#region openmp options
%global cmake_config_args %{cmake_config_args} \\\
	-DOPENMP_INSTALL_LIBDIR=%{unprefixed_libdir} \\\
	-DLIBOMP_INSTALL_ALIASES=OFF

%if %{maj_ver} >= 22 && %{with offload}
# We reset the cxxflags to "" here because this is compiling for a GPU
# target, where our cflags are either questionable or actively wrong.
%global cmake_config_args %{cmake_config_args} \\\
	-DLLVM_RUNTIME_TARGETS='default;amdgcn-amd-amdhsa;nvptx64-nvidia-cuda' \\\
	-DRUNTIMES_nvptx64-nvidia-cuda_LLVM_ENABLE_RUNTIMES=openmp \\\
	-DRUNTIMES_amdgcn-amd-amdhsa_LLVM_ENABLE_RUNTIMES=openmp \\\
	-DRUNTIMES_amdgcn-amd-amdhsa_CMAKE_CXX_FLAGS="" \\\
	-DRUNTIMES_nvptx64-nvidia-cuda_CMAKE_CXX_FLAGS=""

%if 0%{?__isa_bits} == 64
# The following shouldn't be required, but due to a bug, we have to be
# explicit about LLVM_LIBDIR_SUFFIX for nvptx64-nvidia-cuda.
# TODO: Remove this after fixing
# https://github.com/llvm/llvm-project/issues/159762
%global cmake_config_args %{cmake_config_args} \\\
	-DRUNTIMES_nvptx64-nvidia-cuda_LLVM_LIBDIR_SUFFIX=64
%endif
%endif
#endregion openmp options

#region polly options
%if %{with polly}
%global cmake_config_args %{cmake_config_args} \\\
  -DLLVM_POLLY_LINK_INTO_TOOLS=OFF
%endif
#endregion polly options

#region flang options
%if %{with flang}
%global cmake_config_args %{cmake_config_args} \\\
  -DFLANG_INCLUDE_DOCS:BOOL=ON
# Build both, shared and static flang runtime objects.
# See also https://llvm.org/devmtg/2025-04/slides/quick_talk/kruse_flang-rt.pdf
%global cmake_config_args %{cmake_config_args} \\\
  -DFLANG_RT_ENABLE_SHARED:BOOL=ON \\\
  -DFLANG_RT_ENABLE_STATIC:BOOL=ON
# The amount of RAM used per process has been set by trial and error.
# This number may increase/decrease from time to time and may require changes.
# We prefer to be on the safe side in order to avoid spurious errors.
%global cmake_config_args %{cmake_config_args} \\\
  -DFLANG_PARALLEL_COMPILE_JOBS=%{lua: print_max_procs(3072)}
%endif
#endregion flang options


#region test options
%global cmake_config_args %{cmake_config_args} \\\
	-DLLVM_BUILD_TESTS:BOOL=ON \\\
	-DLLVM_INCLUDE_TESTS:BOOL=ON \\\
	-DLLVM_INSTALL_GTEST:BOOL=ON \\\
	-DLLVM_LIT_ARGS="-vv"

%if %{with lto_build}
	%global cmake_config_args %{cmake_config_args} -DLLVM_UNITTEST_LINK_FLAGS="-fno-lto"
%endif
#endregion test options

#region misc options
%global cmake_config_args %{cmake_config_args} \\\
	-DCMAKE_INSTALL_PREFIX=%{install_prefix} \\\
	-DENABLE_LINKER_BUILD_ID:BOOL=ON \\\
	-DPython3_EXECUTABLE=%{__python3}

%if %{with offload}
%global cmake_config_args %{cmake_config_args} \\\
	-DOFFLOAD_INSTALL_LIBDIR=%{unprefixed_libdir}
%endif

# During the build, we use both the system clang and the just-built clang, and
# they need to use the system and just-built shared objects respectively. If
# we use LD_LIBRARY_PATH to point to our build directory, the system clang
# may use the just-built shared objects instead, which may not be compatible
# even if the version matches (e.g. when building compat libs or different rcs).
# Instead, we make use of rpath during the build and only strip it on
# installation using the CMAKE_SKIP_INSTALL_RPATH option.
%global cmake_config_args %{cmake_config_args} -DCMAKE_SKIP_INSTALL_RPATH:BOOL=ON

%if 0%{?fedora} || 0%{?rhel} > 9
	%global cmake_config_args %{cmake_config_args} -DPPC_LINUX_DEFAULT_IEEELONGDOUBLE=ON
%endif

%if 0%{?__isa_bits} == 64
	%global cmake_config_args %{cmake_config_args} -DLLVM_LIBDIR_SUFFIX=64
%endif

%if %{with gold}
	%global cmake_config_args %{cmake_config_args} -DLLVM_BINUTILS_INCDIR=%{_includedir}
%endif

%if %{with snapshot_build}
	%global cmake_config_args %{cmake_config_args} -DLLVM_VERSION_SUFFIX="%{llvm_snapshot_version_suffix}"
%else
%if %{without compat_build}
	%global cmake_config_args %{cmake_config_args} -DLLVM_VERSION_SUFFIX=''
%endif
%endif

%ifarch x86_64
	%global cmake_config_args %{cmake_config_args} -DCMAKE_SHARED_LINKER_FLAGS="$LDFLAGS -Wl,-z,cet-report=error"
%endif

%if 0%{?rhel} == 8
%ifnarch s390x
	# This option uses the NUMBER_OF_LOGICAL_CORES query in CMake which doesn't
	# work on s390x.
	# https://gitlab.kitware.com/cmake/cmake/-/issues/26619
	# The value 4096 was used after we've seen cases of memory exhaustion on a
	# system with 64GiB RAM and 16 jobs. It worked a few times after applied,
	# but we can't guarantee it's enough. It's important to remember that RHEL8
	# uses GCC. This value should not be applied to a build using clang.
	%global cmake_config_args %{cmake_config_args} -DLLVM_RAM_PER_COMPILE_JOB=4096
%endif
%endif
#endregion misc options

extra_cmake_args=''
# TSan does not support 5-level page tables (https://github.com/llvm/llvm-project/issues/111492)
# so do not run tests using tsan on systems that potentially use 5-level page tables.
if grep 'flags.*la57' /proc/cpuinfo; then
  extra_cmake_args="$extra_cmake_args -DOPENMP_TEST_ENABLE_TSAN=OFF"
fi
#endregion cmake options

%if %{with pgo}
#region Instrument LLVM
%global __cmake_builddir %{builddir_instrumented}

# For -Wno-backend-plugin see https://llvm.org/docs/HowToBuildWithPGO.html
#%%global optflags_for_instrumented %(echo %{optflags} -Wno-backend-plugin)

%global cmake_config_args_instrumented %{cmake_config_args} \\\
  -DLLVM_ENABLE_PROJECTS:STRING="clang;lld" \\\
  -DLLVM_ENABLE_RUNTIMES="compiler-rt" \\\
  -DLLVM_TARGETS_TO_BUILD=Native \\\
  -DCMAKE_BUILD_TYPE:STRING=Release \\\
  -DCMAKE_INSTALL_PREFIX=%{builddir_instrumented} \\\
  -DCLANG_INCLUDE_DOCS:BOOL=OFF  \\\
  -DLLVM_BUILD_DOCS:BOOL=OFF  \\\
  -DLLVM_BUILD_UTILS:BOOL=OFF  \\\
  -DLLVM_ENABLE_DOXYGEN:BOOL=OFF  \\\
  -DLLVM_ENABLE_SPHINX:BOOL=OFF  \\\
  -DLLVM_INCLUDE_DOCS:BOOL=OFF  \\\
  -DLLVM_INCLUDE_TESTS:BOOL=OFF  \\\
  -DLLVM_INSTALL_UTILS:BOOL=OFF  \\\
  -DCLANG_BUILD_EXAMPLES:BOOL=OFF \\\
   \\\
  -DLLVM_BUILD_INSTRUMENTED=IR \\\
  -DLLVM_BUILD_RUNTIME=No \\\
  -DLLVM_ENABLE_LTO:BOOL=Thin \\\
  -DLLVM_USE_LINKER=lld

# CLANG_INCLUDE_TESTS=ON is needed to make the target "generate-profdata" available
%global cmake_config_args_instrumented %{cmake_config_args_instrumented} \\\
  -DCLANG_INCLUDE_TESTS:BOOL=ON

# LLVM_INCLUDE_UTILS=ON is needed because the tests enabled by CLANG_INCLUDE_TESTS=ON
# require "FileCheck", "not", "count", etc.
%global cmake_config_args_instrumented %{cmake_config_args_instrumented} \\\
  -DLLVM_INCLUDE_UTILS:BOOL=ON

# LLVM Profile Warning: Unable to track new values: Running out of static counters.
# Consider using option -mllvm -vp-counters-per-site=<n> to allocate more value profile
# counters at compile time.
%global cmake_config_args_instrumented %{cmake_config_args_instrumented} \\\
  -DLLVM_VP_COUNTERS_PER_SITE=8

%if %{defined host_clang_maj_ver}
%global cmake_config_args_instrumented %{cmake_config_args_instrumented} \\\
  -DLLVM_PROFDATA=%{_bindir}/llvm-profdata-%{host_clang_maj_ver}
%else
%global cmake_config_args_instrumented %{cmake_config_args_instrumented} \\\
  -DLLVM_PROFDATA=%{_bindir}/llvm-profdata
%endif

# TODO(kkleine): Should we see warnings like:
# "function control flow change detected (hash mismatch)"
# then read https://issues.chromium.org/issues/40633598 again.
%cmake -G Ninja %{cmake_config_args_instrumented} $extra_cmake_args

# Build all the tools we need in order to build generate-profdata and llvm-profdata
%cmake_build --target libclang-cpp.so
%cmake_build --target clang
%cmake_build --target lld
%cmake_build --target llvm-ar
%cmake_build --target llvm-ranlib
#endregion Instrument LLVM

#region Perf training
%cmake_build --target generate-profdata

# Show top 10 functions in the profile
llvm-profdata show --topn=10 %{builddir_instrumented}/tools/clang/utils/perf-training/clang.profdata | llvm-cxxfilt

cp %{builddir_instrumented}/tools/clang/utils/perf-training/clang.profdata $RPM_BUILD_DIR/result.profdata

#endregion Perf training
%endif

#region Final stage

#region reset paths and globals
function reset_paths {
	export PATH="$OLD_PATH"
	export LD_LIBRARY_PATH="$OLD_LD_LIBRARY_PATH"
}
reset_paths

cd $OLD_CWD
%global _vpath_srcdir .
%global __cmake_builddir %{_vpath_builddir}
#endregion reset paths and globals

%global extra_cmake_opts %{nil}

%if %{with pgo}
  %global extra_cmake_opts %{extra_cmake_opts} -DLLVM_PROFDATA_FILE=$RPM_BUILD_DIR/result.profdata
  # There were a couple of errors that I ran into. One basically said:
  #
  #  Error: LLVM Profile Warning: Unable to track new values: Running out of
  #  static counters. Consider using option -mllvm -vp-counters-per-site=<n> to
  #  allocate more value profile counters at compile time.
  #
  # As a solution I’ve added the --vp-counters-per-site option but this resulted
  # in a follow-up error:
  #
  #   Error: clang (LLVM option parsing): for the --vp-counters-per-site option:
  #   may only occur zero or one times!
  #
  # The solution was to modify vp-counters-per-site option through
  # LLVM_VP_COUNTERS_PER_SITE instead of adding it, hence the
  # -DLLVM_VP_COUNTERS_PER_SITE=8.
  %global extra_cmake_opts %{extra_cmake_opts} -DLLVM_VP_COUNTERS_PER_SITE=8
%endif

%if 0%{with lto_build}
  %global extra_cmake_opts %{extra_cmake_opts} -DLLVM_ENABLE_LTO:BOOL=Thin
  %global extra_cmake_opts %{extra_cmake_opts} -DLLVM_ENABLE_FATLTO=ON
%endif

%if 0%{with use_lld}
%global extra_cmake_opts %{extra_cmake_opts} -DLLVM_USE_LINKER=lld
%endif

%cmake -G Ninja %{cmake_config_args} %{extra_cmake_opts} $extra_cmake_args

# Build libLLVM.so first.  This ensures that when libLLVM.so is linking, there
# are no other compile jobs running.  This will help reduce OOM errors on the
# builders without having to artificially limit the number of concurrent jobs.
%cmake_build --target LLVM

# Also build libclang-cpp.so separately to avoid OOM errors.
# This is to fix occasional OOM errors on the ppc64le COPR builders.
%cmake_build --target libclang-cpp.so

# Same for the three large MLIR dylibs.
%if %{with mlir}
%cmake_build --target libMLIR.so
%cmake_build --target libMLIR-C.so
%cmake_build --target libMLIRPythonCAPI.so
%endif

%cmake_build

# If we don't build the runtimes target here, we'll have to wait for the %%check
# section until these files are available but they need to be installed.
#
#   /usr/lib64/libomptarget.devicertl.a
#   /usr/lib64/libomptarget-amdgpu-*.bc
#   /usr/lib64/libomptarget-nvptx-*.bc
%cmake_build --target runtimes
#endregion Final stage

#endregion Performance comparison

#region compat lib
cd ..

%if %{with bundle_compat_lib}

%if %{compat_maj_ver} >= 22
%global compat_lib_cmake_args -DLLVM_ENABLE_EH=OFF
%else
%global compat_lib_cmake_args -DLLVM_ENABLE_EH=ON
%endif

# MIPS and Arm targets were disabled in LLVM 20, but we still need them
# enabled for the compat libraries.
%cmake -S ../llvm-project-%{compat_ver}.src/llvm -B ../llvm-compat-libs -G Ninja \
    -DCMAKE_INSTALL_PREFIX=%{buildroot}%{_libdir}/llvm%{compat_maj_ver}/ \
    -DCMAKE_SKIP_RPATH=ON \
    -DLLVM_ENABLE_PROJECTS="clang;lldb" \
    -DLLVM_INCLUDE_BENCHMARKS=OFF \
    -DLLVM_INCLUDE_TESTS=OFF \
    %{cmake_common_args} \
    %{compat_lib_cmake_args}



%ninja_build -C ../llvm-compat-libs LLVM
%ninja_build -C ../llvm-compat-libs libclang.so
%ninja_build -C ../llvm-compat-libs libclang-cpp.so
%ninja_build -C ../llvm-compat-libs liblldb.so

%endif
#endregion compat lib
#endregion build

#region install
%install
#region LLVM installation

pushd llvm

%if %{with python_lit}
pushd utils/lit
%if 0%{?rhel} == 8
%py3_install
%else
%pyproject_install
%endif

# Strip out #!/usr/bin/env python
sed -i -e '1{\@^#!/usr/bin/env python@d}' %{buildroot}%{python3_sitelib}/lit/*.py
popd
%endif

%cmake_install

%if %{with flang}
# Create ld.so.conf.d entry
mkdir -p %{buildroot}%{_sysconfdir}/ld.so.conf.d
cat >> %{buildroot}%{_sysconfdir}/ld.so.conf.d/%{pkg_name_flang}-%{_arch}.conf << EOF
%{_prefix}/lib/clang/%{maj_ver}/lib/%{llvm_triple}/
EOF
%endif

popd

mkdir -p %{buildroot}/%{_bindir}

# Install binaries needed for lit tests
%global test_binaries llvm-isel-fuzzer llvm-opt-fuzzer

for f in %{test_binaries}
do
    install -m 0755 llvm/%{_vpath_builddir}/bin/$f %{buildroot}%{install_bindir}
    chrpath --delete %{buildroot}%{install_bindir}/$f
done

# Install libraries needed for unittests
install %{build_libdir}/libLLVMTestingSupport.a %{buildroot}%{install_libdir}
install %{build_libdir}/libLLVMTestingAnnotations.a %{buildroot}%{install_libdir}

# Fix multi-lib
%multilib_fix_c_header --file %{install_includedir}/llvm/Config/llvm-config.h

%if %{without compat_build}

%if %{with gold}
# Add symlink to lto plugin in the binutils plugin directory.
%{__mkdir_p} %{buildroot}%{_libdir}/bfd-plugins/
ln -s -t %{buildroot}%{_libdir}/bfd-plugins/ ../LLVMgold.so
%endif

%else

# Create ld.so.conf.d entry
mkdir -p %{buildroot}%{_sysconfdir}/ld.so.conf.d
cat >> %{buildroot}%{_sysconfdir}/ld.so.conf.d/%{pkg_name_llvm}-%{_arch}.conf << EOF
%{install_libdir}
EOF

%endif

mkdir -p %{buildroot}%{install_datadir}/llvm-cmake
cp -Rv cmake/* %{buildroot}%{install_datadir}/llvm-cmake

# Install a placeholder to redirect users of the formerly shipped
# HTML documentation to the upstream HTML documentation.
mkdir -pv %{buildroot}%{_pkgdocdir}/html
cat <<EOF > %{buildroot}%{_pkgdocdir}/html/index.html
<!doctype html>
<html lang=en>
  <head>
    <title>LLVM %{maj_ver}.%{min_ver} documentation</title>
  </head>
  <body>
  <h1>
    LLVM %{maj_ver}.%{min_ver} Documentation
  </h1>
  <ul>
    <li>
      <a href="https://releases.llvm.org/%{maj_ver}.%{min_ver}.0/docs/index.html">
        Click here for the upstream documentation of LLVM %{maj_ver}.%{min_ver}.
      </a>
    </li>
    <li>
      <a href="https://llvm.org/docs/">
        Click here for the latest upstream documentation of LLVM.
      </a>
    </li>
  </ul>
  </body>
</html>
EOF

#endregion LLVM installation

#region CLANG installation

# Add a symlink in bindir to clang-format-diff
ln -s ../share/clang/clang-format-diff.py %{buildroot}%{install_bindir}/clang-format-diff

# Install the PGO profile that was used to build this LLVM into the clang package
%if 0%{with pgo}
cp -v $RPM_BUILD_DIR/result.profdata %{buildroot}%{install_datadir}/llvm-pgo.profdata
%endif

# File in the macros file for other packages to use.  We are not doing this
# in the compat package, because the version macros would # conflict with
# eachother if both clang and the clang compat package were installed together.
%if %{without compat_build}
install -p -m0644 -D %{SOURCE2005} %{buildroot}%{_rpmmacrodir}/macros.%{pkg_name_clang}
sed -i -e "s|@@CLANG_MAJOR_VERSION@@|%{maj_ver}|" \
       -e "s|@@CLANG_MINOR_VERSION@@|%{min_ver}|" \
       -e "s|@@CLANG_PATCH_VERSION@@|%{patch_ver}|" \
       %{buildroot}%{_rpmmacrodir}/macros.%{pkg_name_clang}

# install clang python bindings
mkdir -p %{buildroot}%{python3_sitelib}/clang/
# If we don't default to true here, we'll see this error:
# install: omitting directory 'bindings/python/clang/__pycache__'
# NOTE: this only happens if we include the gdb plugin of libomp.
# Remove the plugin with command and we're good: rm -rf %{buildroot}/%{_datarootdir}/gdb
install -p -m644 clang/bindings/python/clang/* %{buildroot}%{python3_sitelib}/clang/
%py_byte_compile %{__python3} %{buildroot}%{python3_sitelib}/clang

# install scanbuild-py to python sitelib.
mv %{buildroot}%{install_prefix}/lib/{libear,libscanbuild} %{buildroot}%{python3_sitelib}
# Cannot use {libear,libscanbuild} style expansion in py_byte_compile.
%py_byte_compile %{__python3} %{buildroot}%{python3_sitelib}/libear
%py_byte_compile %{__python3} %{buildroot}%{python3_sitelib}/libscanbuild

# Move emacs integration files to the correct directory
mkdir -p %{buildroot}%{_emacs_sitestartdir}
for f in clang-format.el clang-include-fixer.el; do
mv %{buildroot}{%{install_datadir}/clang,%{_emacs_sitestartdir}}/$f
done

%else

# Not sure where to put these python modules for the compat build.
rm -Rf %{buildroot}%{install_prefix}/lib/{libear,libscanbuild}
rm %{buildroot}%{install_bindir}/scan-build-py

# Not sure where to put the emacs integration files for the compat build.
rm -Rf %{buildroot}%{install_datadir}/clang/*.el

%endif

# Create manpage symlink for clang++
ln -s clang-%{maj_ver}.1 %{buildroot}%{install_mandir}/man1/clang++.1

# Fix permissions of scan-view scripts
chmod a+x %{buildroot}%{install_datadir}/scan-view/{Reporter.py,startfile.py}

# multilib fix
%multilib_fix_c_header --file %{install_includedir}/clang/Config/config.h

# remove editor integrations (bbedit, sublime, emacs, vim)
rm -vf %{buildroot}%{install_datadir}/clang/clang-format-bbedit.applescript
rm -vf %{buildroot}%{install_datadir}/clang/clang-format-sublime.py*

# Remove unpackaged files
rm -Rvf %{buildroot}%{install_datadir}/clang-doc

# TODO: What are the Fedora guidelines for packaging bash autocomplete files?
rm -vf %{buildroot}%{install_datadir}/clang/bash-autocomplete.sh

%if %{without compat_build}
# Move clang resource directory to default prefix.
mkdir -p %{buildroot}%{_prefix}/lib/clang
mv %{buildroot}%{install_prefix}/lib/clang/%{maj_ver} %{buildroot}%{_prefix}/lib/clang/%{maj_ver}
%endif
# Create any missing sub-directories in the clang resource directory.
mkdir -p %{buildroot}%{_prefix}/lib/clang/%{maj_ver}/{bin,include,lib,share}/

# Add versioned resource directory macro
mkdir -p %{buildroot}%{_rpmmacrodir}/
echo "%%clang%{maj_ver}_resource_dir %%{_prefix}/lib/clang/%{maj_ver}" >> %{buildroot}%{_rpmmacrodir}/macros.%{pkg_name_clang}

mkdir -p %{buildroot}%{_sysconfdir}/%{pkg_name_clang}/
echo " %{cfg_file_content}" >> %{buildroot}%{_sysconfdir}/%{pkg_name_clang}/%{_target_platform}-clang.cfg
echo " %{cfg_file_content}" >> %{buildroot}%{_sysconfdir}/%{pkg_name_clang}/%{_target_platform}-clang++.cfg
%ifarch x86_64
# On x86_64, install an additional set of config files so -m32 works.
echo " %{cfg_file_content}" >> %{buildroot}%{_sysconfdir}/%{pkg_name_clang}/i386-redhat-linux-gnu-clang.cfg
echo " %{cfg_file_content}" >> %{buildroot}%{_sysconfdir}/%{pkg_name_clang}/i386-redhat-linux-gnu-clang++.cfg
%endif


#endregion CLANG installation

#region COMPILER-RT installation

# Triple where compiler-rt libs are installed. If it differs from llvm_triple, then there is
# also a symlink llvm_triple -> compiler_rt_triple.
%global compiler_rt_triple %{llvm_triple}

%ifarch ppc64le
# Fix install path on ppc64le so that the directory name matches the triple used
# by clang.
mkdir -pv %{buildroot}%{_prefix}/lib/clang/%{maj_ver}/lib/%{llvm_triple}
mv %{buildroot}%{_prefix}/lib/clang/%{maj_ver}/lib/powerpc64le-redhat-linux-gnu/* %{buildroot}%{_prefix}/lib/clang/%{maj_ver}/lib/%{llvm_triple}
%endif

%ifarch %{ix86}
# Fix install path on ix86 so that the directory name matches the triple used
# by clang on both actual ix86 (i686) and on x86_64 with -m32 (i386):
%global compiler_rt_triple i386-redhat-linux-gnu
%if "%{llvm_triple}" != "%{compiler_rt_triple}"
ln -s %{compiler_rt_triple} %{buildroot}%{_prefix}/lib/clang/%{maj_ver}/lib/%{llvm_triple}
%endif
%endif

#endregion COMPILER-RT installation

#region OPENMP installation

# Remove static libraries with equivalent shared libraries
rm -rf %{buildroot}%{install_libdir}/libarcher_static.a

# Remove the openmp gdb plugin for now
rm -rf %{buildroot}/%{install_datadir}/gdb
# # TODO(kkleine): These was added to avoid a permission issue
# chmod go+w %{buildroot}/%{_datarootdir}/gdb/python/ompd/ompdModule.so
# chmod +w %{buildroot}/%{_datarootdir}/gdb/python/ompd/ompdModule.so

%if %{with offload}
# Remove files that we don't package, yet.
rm %{buildroot}%{install_bindir}/llvm-offload-device-info
rm %{buildroot}%{install_bindir}/llvm-omp-kernel-replay
%endif

#endregion OPENMP installation

#region LLD installation

%if %{without compat_build}
# Required when using update-alternatives:
# https://docs.fedoraproject.org/en-US/packaging-guidelines/Alternatives/
touch %{buildroot}%{_bindir}/ld
%endif

install -D -m 644 -t  %{buildroot}%{install_mandir}/man1/ lld/docs/ld.lld.1

#endregion LLD installation

#region LLDB installation
%if %{with lldb}
%multilib_fix_c_header --file %{install_includedir}/lldb/Host/Config.h

%if %{without compat_build}
# Move python package out of llvm prefix.
mkdir -p %{buildroot}%{python3_sitearch}
mv %{buildroot}%{install_prefix}/%{_lib}/python%{python3_version}/site-packages/lldb %{buildroot}/%{python3_sitearch}
rmdir %{buildroot}%{install_prefix}/%{_lib}/python%{python3_version}/site-packages
rmdir %{buildroot}%{install_prefix}/%{_lib}/python%{python3_version}

# python: fix binary libraries location
liblldb=$(basename $(readlink -e %{buildroot}%{install_libdir}/liblldb.so))
ln -vsf "../../../${liblldb}" %{buildroot}%{python3_sitearch}/lldb/_lldb.so
%py_byte_compile %{__python3} %{buildroot}%{python3_sitearch}/lldb
%endif
%endif
#endregion LLDB installation

#region mlir installation
%if %{with mlir}
mkdir -p %{buildroot}/%{python3_sitearch}
mv %{buildroot}%{install_prefix}/python_packages/mlir_core/mlir %{buildroot}/%{python3_sitearch}
# These directories should be empty now.
rmdir %{buildroot}%{install_prefix}/python_packages/mlir_core %{buildroot}%{install_prefix}/python_packages
# Unneeded files.
rm -rf %{buildroot}%{install_prefix}/src/python
%endif
#endregion mlir installation

#region flang installation
%if %{with flang}
# Remove unnecessary files.
rm -rfv %{buildroot}%{install_libdir}/cmake/flang

# Remove runtime development headers (see https://github.com/llvm/llvm-project/pull/165610)
rm -rfv %{buildroot}%{install_includedir}/flang-rt

rm -v %{buildroot}%{install_libdir}/libFIRAnalysis.a \
      %{buildroot}%{install_libdir}/libFIRBuilder.a \
      %{buildroot}%{install_libdir}/libFIRCodeGen.a \
      %{buildroot}%{install_libdir}/libFIRCodeGenDialect.a \
      %{buildroot}%{install_libdir}/libFIRDialect.a \
      %{buildroot}%{install_libdir}/libFIRDialectSupport.a \
      %{buildroot}%{install_libdir}/libFIROpenACCSupport.a \
      %{buildroot}%{install_libdir}/libFIROpenMPSupport.a \
      %{buildroot}%{install_libdir}/libFIRSupport.a \
      %{buildroot}%{install_libdir}/libFIRTestAnalysis.a \
      %{buildroot}%{install_libdir}/libFIRTestOpenACCInterfaces.a \
      %{buildroot}%{install_libdir}/libFIRTransforms.a \
      %{buildroot}%{install_libdir}/libflangFrontend.a \
      %{buildroot}%{install_libdir}/libflangFrontendTool.a \
      %{buildroot}%{install_libdir}/libflangPasses.a \
      %{buildroot}%{install_libdir}/libFlangOpenMPTransforms.a \
      %{buildroot}%{install_libdir}/libFortranEvaluate.a \
      %{buildroot}%{install_libdir}/libFortranLower.a \
      %{buildroot}%{install_libdir}/libFortranParser.a \
      %{buildroot}%{install_libdir}/libFortranSemantics.a \
      %{buildroot}%{install_libdir}/libFortranSupport.a \
      %{buildroot}%{install_libdir}/libHLFIRDialect.a \
      %{buildroot}%{install_libdir}/libHLFIRTransforms.a \
      %{buildroot}%{install_libdir}/libCUFAttrs.a \
      %{buildroot}%{install_libdir}/libCUFDialect.a \
      %{buildroot}%{install_libdir}/libFortranDecimal.a
%if %{maj_ver} >= 22
rm -v %{buildroot}%{install_libdir}/libFortranUtils.a \
      %{buildroot}%{install_libdir}/libFIROpenACCAnalysis.a \
      %{buildroot}%{install_libdir}/libFIROpenACCTransforms.a \
      %{buildroot}%{install_libdir}/libMIFDialect.a
%endif

find %{buildroot}%{install_includedir}/flang -type f -a ! -iname '*.mod' -delete

# this is a test binary
rm -v %{buildroot}%{install_bindir}/f18-parse-demo

# Probably this directory already existed before
mkdir -pv %{buildroot}%{_sysconfdir}/%{pkg_name_clang}/
echo " %{cfg_file_content_flang}" >> %{buildroot}%{_sysconfdir}/%{pkg_name_clang}/%{_target_platform}-flang.cfg
%ifarch x86_64
# On x86_64, install an additional config file.
echo " %{cfg_file_content_flang}" >> %{buildroot}%{_sysconfdir}/%{pkg_name_clang}/i386-redhat-linux-gnu-flang.cfg
%endif
%endif
#endregion flang installation

#region libcxx installation
%if %{with libcxx}
# We can't install the unversionned path on default location because that would conflict with
# https://src.fedoraproject.org/rpms/libunwind
#
# The versionned path has a different soname (libunwind.so.1 compared to
# libunwind.so.8) so they can live together in %%{_libdir}
#
# ABI wise, even though llvm-libunwind's library is named libunwind, it doesn't
# have the exact same ABI as gcc's libunwind (it actually provides a subset).
rm %{buildroot}%{_libdir}/libunwind.so
mkdir -p %{buildroot}/%{_libdir}/llvm-unwind/

pushd %{buildroot}/%{_libdir}/llvm-unwind
ln -s ../libunwind.so.1.0 libunwind.so
popd
%endif
#endregion libcxx installation

#region BOLT installation
# We don't ship libLLVMBOLT*.a
rm -f %{buildroot}%{install_libdir}/libLLVMBOLT*.a
#endregion BOLT installation

# Move files from src to dest and replace the old files in src with relative
# symlinks.
move_and_replace_with_symlinks() {
    local src="$1"
    local dest="$2"
    mkdir -p "$dest"

    # Change to source directory to simplify relative paths
    (cd "$src" && \
        find * -type d -exec mkdir -p "$dest/{}" \; && \
        find * \( -type f -o -type l \) -exec mv "$src/{}" "$dest/{}" \; \
             -exec ln -s --relative "$dest/{}" "$src/{}" \;)
}

%if %{without compat_build}
# Move files from the llvm prefix to the system prefix and replace them with
# symlinks. We do it this way around because symlinks between multilib packages
# would conflict otherwise.
move_and_replace_with_symlinks %{buildroot}%{install_bindir} %{buildroot}%{_bindir}
move_and_replace_with_symlinks %{buildroot}%{install_libdir} %{buildroot}%{_libdir}
move_and_replace_with_symlinks %{buildroot}%{install_libexecdir} %{buildroot}%{_libexecdir}
move_and_replace_with_symlinks %{buildroot}%{install_includedir} %{buildroot}%{_includedir}
move_and_replace_with_symlinks %{buildroot}%{install_datadir} %{buildroot}%{_datadir}
%endif

# Create versioned symlinks for binaries.
# Do this at the end so it includes any files added by preceding steps.
mkdir -p %{buildroot}%{_bindir}
for f in %{buildroot}%{install_bindir}/*; do
  filename=`basename $f`
  if [[ "$filename" =~ ^(lit|ld|clang-%{maj_ver}|flang-%{maj_ver})$ ]]; then
    continue
  fi
  %if %{with compat_build}
    ln -s ../../%{install_bindir}/$filename %{buildroot}/%{_bindir}/$filename-%{maj_ver}
  %else
    # clang-NN and flang-NN are already created by the build system.
    if [[ "$filename" =~ ^(clang|flang)$ ]]; then
      continue
    fi
    ln -s $filename %{buildroot}/%{_bindir}/$filename-%{maj_ver}
  %endif
done

mkdir -p %{buildroot}%{_mandir}/man1
for f in %{buildroot}%{install_mandir}/man1/*; do
  filename=`basename $f`
  filename=${filename%.1}
  %if %{with compat_build}
    # Move man pages to system install prefix.
    mv $f %{buildroot}%{_mandir}/man1/$filename-%{maj_ver}.1
  %else
    # Create suffixed symlink.
    ln -s $filename.1 %{buildroot}%{_mandir}/man1/$filename-%{maj_ver}.1
  %endif
done
rm -rf %{buildroot}%{install_mandir}

# As an exception, always keep llvm-config in the versioned prefix.
# The llvm-config in the default prefix will be managed by alternatives.
%if %{without compat_build}
rm %{buildroot}%{install_bindir}/llvm-config
mv %{buildroot}%{_bindir}/llvm-config %{buildroot}%{install_bindir}/llvm-config
%endif

# ghost presence for llvm-config, managed by alternatives.
touch %{buildroot}%{_bindir}/llvm-config-%{maj_ver}
%if %{without compat_build}
touch %{buildroot}%{_bindir}/llvm-config
%endif

%if %{with bundle_compat_lib}
install -m 0755 ../llvm-compat-libs/lib/libLLVM.so.%{compat_maj_ver}* %{buildroot}%{_libdir}
install -m 0755 ../llvm-compat-libs/lib/libclang.so.%{compat_maj_ver}* %{buildroot}%{_libdir}
install -m 0755 ../llvm-compat-libs/lib/libclang-cpp.so.%{compat_maj_ver}* %{buildroot}%{_libdir}
install -m 0755 ../llvm-compat-libs/lib/liblldb.so.%{compat_maj_ver}* %{buildroot}%{_libdir}
%endif
#endregion install

#region check
%check
# TODO(kkleine): Instead of deleting test files we should mark them as expected
# to fail. See https://llvm.org/docs/CommandGuide/lit.html#cmdoption-lit-xfail

# Tell if the GTS version used by the newly built clang is equal to the
# expected version.
function is_gts_equal {
    local gts_used=$(`pwd`/%{_vpath_builddir}/bin/clang -v 2>&1 | grep "Selected GCC installation" | sed 's|.*/\([0-9]\+\)$|\1|')
    if [[ -z "%{gts_version}" ]]; then
      return 0
    fi
    test "x$gts_used" = "x%{gts_version}"
    return $?
}

# Increase open file limit while running tests.
if [[ $(ulimit -n) -lt 10000 ]]; then
  ulimit -n 10000
fi

%ifarch ppc64le
# TODO: Re-enable when ld.gold fixed its internal error.
rm llvm/test/tools/gold/PowerPC/mtriple.ll
%endif

# non reproducible errors
# TODO(kkleine): Add this to XFAIL instead?
rm llvm/test/tools/dsymutil/X86/swift-interface.test

cd llvm

%if %{with check}

#region Helper functions
# Call this function before setting up a next component to test.
function reset_test_opts()
{
    # See https://llvm.org/docs/CommandGuide/lit.html#general-options
    export LIT_OPTS="-vv --time-tests"
    # --timeout needs psutil package, so disable it on RHEL 8.
    %if %{undefined rhel} || 0%{?rhel} > 8
    export LIT_OPTS="$LIT_OPTS --timeout=600"
    %endif

    # Set to mark tests as expected to fail.
    # See https://llvm.org/docs/CommandGuide/lit.html#cmdoption-lit-xfail
    unset LIT_XFAIL

    # Set to mark tests to not even run.
    # See https://llvm.org/docs/CommandGuide/lit.html#cmdoption-lit-filter-out
    # Unfortunately LIT_FILTER_OUT is not accepting a list but a regular expression.
    # To make this easily maintainable, we'll create an associate array in bash,
    # to which you can append and later we'll join that array and escape dots (".")
    # in your test paths. The following line resets this array.
    # See also the function "test_list_to_regex".
    test_list_filter_out=()
    unset LIT_FILTER_OUT

    # Set for filtering out unit tests.
    # See http://google.github.io/googletest/advanced.html#running-a-subset-of-the-tests
    unset GTEST_FILTER

    # Some test (e.g. mlir) require this to be set.
    unset PYTHONPATH
}

# Convert array of test names into a regex.
# Call this function with an indexed array.
#
# Example:
#
#    testlist=()
#    testlist+=("foo")
#    testlist+=("bar")
#    export LIT_FILTER_OUT=$(test_list_to_regex testlist)
#
# Then $LIT_FILTER_OUT should evaluate to: (foo|bar)
function test_list_to_regex()
{
    local -n arr=$1
    # Prepare LIT_FILTER_OUT regex from index bash array
    # Join each element with a pipe symbol (regex for "or")
    arr=$(printf "|%s" "${arr[@]}")
    # Remove the initial pipe symbol
    arr=${arr:1}
    # Properly escape path dots (".") for use in regular expression
    arr=$(echo $arr | sed 's/\./\\./g')
    # Add enclosing parenthesis
    echo "($arr)"
}

# Similar to test_list_to_regex() except that this function exports
# the LIT_FILTER_OUT if there are tests in the given list.
# If there are no tests, the LIT_FILTER_OUT is unset in order to
# avoid issues with the llvm test system.
function adjust_lit_filter_out()
{
  local -n arr=$1
  local res=$(test_list_to_regex test_list_filter_out)
  if [[ "$res" != "()" ]]; then
    export LIT_FILTER_OUT=$res
  else
    unset LIT_FILTER_OUT
  fi
}
#endregion Helper functions

#region Test LLVM lit
# It's fine to always run this, even if we're not shipping python-lit.
reset_test_opts
%cmake_build --target check-lit
#endregion Test LLVM lit

#region Test LLVM
reset_test_opts
# Xfail testing of update utility tools
export LIT_XFAIL="tools/UpdateTestChecks"
%cmake_build --target check-llvm
#endregion Test LLVM

#region Test CLANG
reset_test_opts
export LIT_XFAIL="$LIT_XFAIL;clang/test/CodeGen/profile-filter.c"

%cmake_build --target check-clang
#endregion Test Clang

#region Test Clang Tools
reset_test_opts
%ifarch %ix86
# Clang Tools :: clang-tidy/checkers/altera/struct-pack-align.cpp
export LIT_XFAIL="$LIT_XFAIL;clang-tidy/checkers/altera/struct-pack-align.cpp"
%endif
%cmake_build --target check-clang-tools
#endregion Test Clang Tools

#region Test OPENMP
reset_test_opts

# TODO(kkleine): OpenMP tests are currently not run on rawhide (see https://bugzilla.redhat.com/show_bug.cgi?id=2252966):
#
# + /usr/bin/cmake --build redhat-linux-build -j6 --verbose --target check-openmp
# Change Dir: '/builddir/build/BUILD/openmp-17.0.6.src/redhat-linux-build'
# Run Build Command(s): /usr/bin/ninja-build -v -j 6 check-openmp
# [1/1] cd /builddir/build/BUILD/openmp-17.0.6.src/redhat-linux-build && /usr/bin/cmake -E echo check-openmp\ does\ nothing,\ dependencies\ not\ found.
#
# We're marking the tests that are failing with the follwing error as expected to fail (XFAIL):
#
#   gdb.error: No symbol "ompd_sizeof____kmp_gtid" in current context
#
# NOTE: It could be a different symbol in some tests.
export LIT_XFAIL="api_tests/test_ompd_get_curr_task_handle.c"
export LIT_XFAIL="$LIT_XFAIL;api_tests/test_ompd_get_enclosing_parallel_handle.c"
export LIT_XFAIL="$LIT_XFAIL;api_tests/test_ompd_get_generating_task_handle.c"
export LIT_XFAIL="$LIT_XFAIL;api_tests/test_ompd_get_icv_from_scope.c"
export LIT_XFAIL="$LIT_XFAIL;api_tests/test_ompd_get_scheduling_task_handle.c"
export LIT_XFAIL="$LIT_XFAIL;api_tests/test_ompd_get_state.c"
export LIT_XFAIL="$LIT_XFAIL;api_tests/test_ompd_get_task_frame.c"
export LIT_XFAIL="$LIT_XFAIL;api_tests/test_ompd_get_task_function.c"
export LIT_XFAIL="$LIT_XFAIL;api_tests/test_ompd_get_task_in_parallel.c"
export LIT_XFAIL="$LIT_XFAIL;api_tests/test_ompd_get_task_parallel_handle.c"
export LIT_XFAIL="$LIT_XFAIL;api_tests/test_ompd_get_thread_id.c"
export LIT_XFAIL="$LIT_XFAIL;api_tests/test_ompd_get_thread_in_parallel.c"
export LIT_XFAIL="$LIT_XFAIL;api_tests/test_ompd_parallel_handle_compare.c"
export LIT_XFAIL="$LIT_XFAIL;api_tests/test_ompd_rel_parallel_handle.c"
export LIT_XFAIL="$LIT_XFAIL;api_tests/test_ompd_rel_task_handle.c"
export LIT_XFAIL="$LIT_XFAIL;api_tests/test_ompd_rel_thread_handle.c"
export LIT_XFAIL="$LIT_XFAIL;api_tests/test_ompd_task_handle_compare.c"
export LIT_XFAIL="$LIT_XFAIL;api_tests/test_ompd_thread_handle_compare.c"
export LIT_XFAIL="$LIT_XFAIL;openmp_examples/ompd_icvs.c"
export LIT_XFAIL="$LIT_XFAIL;api_tests/test_ompd_get_curr_parallel_handle.c"
export LIT_XFAIL="$LIT_XFAIL;api_tests/test_ompd_get_display_control_vars.c"
export LIT_XFAIL="$LIT_XFAIL;api_tests/test_ompd_get_thread_handle.c"

%if %{with pgo}
# TODO(kkleine): I unset LIT_XFAIL here because the tests above unexpectedly passed since Aug 16th on fedora-40-x86_64
unset LIT_XFAIL
%endif

# The following test is flaky and we'll filter it out
test_list_filter_out+=("libomp :: affinity/kmp-abs-hw-subset.c")
test_list_filter_out+=("libomp :: ompt/teams/distribute_dispatch.c")

# These tests fail more often than not, but not always.
test_list_filter_out+=("libomp :: worksharing/for/omp_collapse_many_GELTGT_int.c")
test_list_filter_out+=("libomp :: worksharing/for/omp_collapse_many_GTGEGT_int.c")
test_list_filter_out+=("libomp :: worksharing/for/omp_collapse_many_LTLEGE_int.c")
test_list_filter_out+=("libomp :: worksharing/for/omp_collapse_one_int.c")

%ifarch s390x
test_list_filter_out+=("libomp :: flush/omp_flush.c")
test_list_filter_out+=("libomp :: worksharing/for/omp_for_schedule_guided.c")
%endif

# The following tests seem pass on ppc64le and x86_64 and aarch64 only:
%ifnarch ppc64le x86_64 s390x aarch64
# Passes on ppc64le:
#   libomptarget :: powerpc64le-ibm-linux-gnu :: mapping/target_derefence_array_pointrs.cpp
#   libomptarget :: powerpc64le-ibm-linux-gnu-LTO :: mapping/target_derefence_array_pointrs.cpp
# Passes on x86_64:
#   libomptarget :: x86_64-pc-linux-gnu :: mapping/target_derefence_array_pointrs.cpp
#   libomptarget :: x86_64-pc-linux-gnu-LTO :: mapping/target_derefence_array_pointrs.cpp
# Passes on s390x:
#   libomptarget :: s390x-ibm-linux-gnu :: mapping/target_derefence_array_pointrs.cpp
#   libomptarget :: s390x-ibm-linux-gnu-LTO :: mapping/target_derefence_array_pointrs.cpp
export LIT_XFAIL="$LIT_XFAIL;mapping/target_derefence_array_pointrs.cpp"
%endif

%ifnarch x86_64
# Passes on x86_64:
#   libomptarget :: x86_64-pc-linux-gnu :: api/ompx_3d.c
#   libomptarget :: x86_64-pc-linux-gnu :: api/ompx_3d.cpp
#   libomptarget :: x86_64-pc-linux-gnu-LTO :: api/ompx_3d.c
#   libomptarget :: x86_64-pc-linux-gnu-LTO :: api/ompx_3d.cpp
# libomptarget :: aarch64-unknown-linux-gnu ::
export LIT_XFAIL="$LIT_XFAIL;api/ompx_3d.c"
export LIT_XFAIL="$LIT_XFAIL;api/ompx_3d.cpp"
%endif

%ifarch ppc64le
export LIT_XFAIL="$LIT_XFAIL;barrier/barrier.c"
export LIT_XFAIL="$LIT_XFAIL;critical/critical.c"
export LIT_XFAIL="$LIT_XFAIL;critical/lock-nested.c"
export LIT_XFAIL="$LIT_XFAIL;critical/lock.c"
export LIT_XFAIL="$LIT_XFAIL;parallel/parallel-firstprivate.c"
export LIT_XFAIL="$LIT_XFAIL;parallel/parallel-nosuppression.c"
export LIT_XFAIL="$LIT_XFAIL;parallel/parallel-simple.c"
export LIT_XFAIL="$LIT_XFAIL;parallel/parallel-simple2.c"
export LIT_XFAIL="$LIT_XFAIL;races/critical-unrelated.c"
export LIT_XFAIL="$LIT_XFAIL;races/lock-nested-unrelated.c"
export LIT_XFAIL="$LIT_XFAIL;races/lock-unrelated.c"
export LIT_XFAIL="$LIT_XFAIL;races/parallel-simple.c"
export LIT_XFAIL="$LIT_XFAIL;races/task-dependency.c"
export LIT_XFAIL="$LIT_XFAIL;races/task-taskgroup-unrelated.c"
export LIT_XFAIL="$LIT_XFAIL;races/task-two.c"
export LIT_XFAIL="$LIT_XFAIL;races/taskwait-depend.c"
export LIT_XFAIL="$LIT_XFAIL;races/task-taskwait-nested.c"
export LIT_XFAIL="$LIT_XFAIL;reduction/parallel-reduction-nowait.c"
export LIT_XFAIL="$LIT_XFAIL;reduction/parallel-reduction.c"
export LIT_XFAIL="$LIT_XFAIL;task/omp_task_depend_all.c"
export LIT_XFAIL="$LIT_XFAIL;task/task-barrier.c"
export LIT_XFAIL="$LIT_XFAIL;task/task-create.c"
export LIT_XFAIL="$LIT_XFAIL;task/task-dependency.c"
export LIT_XFAIL="$LIT_XFAIL;task/task-taskgroup-nested.c"
export LIT_XFAIL="$LIT_XFAIL;task/task-taskgroup.c"
export LIT_XFAIL="$LIT_XFAIL;task/task-taskwait-nested.c"
export LIT_XFAIL="$LIT_XFAIL;task/task-taskwait.c"
export LIT_XFAIL="$LIT_XFAIL;task/task_early_fulfill.c"
export LIT_XFAIL="$LIT_XFAIL;task/task_late_fulfill.c"
export LIT_XFAIL="$LIT_XFAIL;task/taskwait-depend.c"
export LIT_XFAIL="$LIT_XFAIL;worksharing/ordered.c"
export LIT_XFAIL="$LIT_XFAIL;api/omp_dynamic_shared_memory.c"
export LIT_XFAIL="$LIT_XFAIL;jit/empty_kernel_lvl1.c"
export LIT_XFAIL="$LIT_XFAIL;jit/empty_kernel_lvl2.c"
export LIT_XFAIL="$LIT_XFAIL;jit/type_punning.c"
export LIT_XFAIL="$LIT_XFAIL;offloading/barrier_fence.c"
export LIT_XFAIL="$LIT_XFAIL;offloading/bug49334.cpp"
export LIT_XFAIL="$LIT_XFAIL;offloading/default_thread_limit.c"
export LIT_XFAIL="$LIT_XFAIL;offloading/ompx_bare.c"
export LIT_XFAIL="$LIT_XFAIL;offloading/ompx_coords.c"
export LIT_XFAIL="$LIT_XFAIL;offloading/ompx_saxpy_mixed.c"
export LIT_XFAIL="$LIT_XFAIL;offloading/small_trip_count.c"
export LIT_XFAIL="$LIT_XFAIL;offloading/small_trip_count_thread_limit.cpp"
export LIT_XFAIL="$LIT_XFAIL;offloading/spmdization.c"
export LIT_XFAIL="$LIT_XFAIL;offloading/target_critical_region.cpp"
export LIT_XFAIL="$LIT_XFAIL;offloading/thread_limit.c"
export LIT_XFAIL="$LIT_XFAIL;api/omp_dynamic_shared_memory.c"
export LIT_XFAIL="$LIT_XFAIL;jit/empty_kernel_lvl1.c"
export LIT_XFAIL="$LIT_XFAIL;jit/empty_kernel_lvl2.c"
export LIT_XFAIL="$LIT_XFAIL;jit/type_punning.c"
export LIT_XFAIL="$LIT_XFAIL;offloading/barrier_fence.c"
export LIT_XFAIL="$LIT_XFAIL;offloading/bug49334.cpp"
export LIT_XFAIL="$LIT_XFAIL;offloading/default_thread_limit.c"
export LIT_XFAIL="$LIT_XFAIL;offloading/ompx_bare.c"
export LIT_XFAIL="$LIT_XFAIL;offloading/ompx_coords.c"
export LIT_XFAIL="$LIT_XFAIL;offloading/ompx_saxpy_mixed.c"
export LIT_XFAIL="$LIT_XFAIL;offloading/small_trip_count.c"
export LIT_XFAIL="$LIT_XFAIL;offloading/small_trip_count_thread_limit.cpp"
export LIT_XFAIL="$LIT_XFAIL;offloading/spmdization.c"
export LIT_XFAIL="$LIT_XFAIL;offloading/target_critical_region.cpp"
export LIT_XFAIL="$LIT_XFAIL;offloading/thread_limit.c"
export LIT_XFAIL="$LIT_XFAIL;mapping/auto_zero_copy.cpp"
export LIT_XFAIL="$LIT_XFAIL;mapping/auto_zero_copy_globals.cpp"
export LIT_XFAIL="$LIT_XFAIL;offloading/workshare_chunk.c"
export LIT_XFAIL="$LIT_XFAIL;ompt/target_memcpy.c"
export LIT_XFAIL="$LIT_XFAIL;ompt/target_memcpy_emi.c"
%endif

%ifarch s390x ppc64le
export LIT_XFAIL="$LIT_XFAIL;offloading/thread_state_1.c"
export LIT_XFAIL="$LIT_XFAIL;offloading/thread_state_2.c"
%endif

adjust_lit_filter_out test_list_filter_out

# This allows openmp tests to be re-run 4 times. Once they pass
# after being re-run, they are marked as FLAKYPASS.
# See https://github.com/llvm/llvm-project/pull/141851 for the
# --max-retries-per-test option.
# We don't know if 4 is the right number to use here we just
# need to start with some number.
# Once https://github.com/llvm/llvm-project/pull/142413 landed
# we can see the exact number of attempts the tests needed
# to pass. And then we can adapt this number.
export LIT_OPTS="$LIT_OPTS --max-retries-per-test=4"

%if %{with flang}
# Without this we run into a libflang_rt.runtime.so not found error.
# See https://github.com/llvm/llvm-project/pull/150722 for why this only
# happens when flang is found.
export LD_LIBRARY_PATH=%{buildroot}%{_prefix}/lib/clang/%{maj_ver}/lib/%{llvm_triple}
%endif

%if 0%{?rhel}
# libomp tests are often very slow on s390x brew builders
%ifnarch s390x riscv64
# Rarely, the system clang uses a GCC installation directory that is
# different from what we'd like to build with.
# Our newly built clang ends up using that old GCC because of the config
# files under /etc/clang pointing to the old GCC. We won't be able to run all
# tests because the installed libatomic cannot be found due to our newly built
# clang using the wrong GCC directory, e.g. we installed the libatomic from
# the latest GTS, but the installed GCC is 1 version earlier.
if is_gts_equal; then
    %cmake_build --target check-openmp
fi
%endif
%else
%cmake_build --target check-openmp
%endif
#endregion Test OPENMP

%if %{with lldb}
# Don't run LLDB tests on s390x because more than 150 tests are failing there
%ifnarch s390x
## TODO(kkleine): Come back and re-enable testing for LLDB
## #region LLDB unit tests
## reset_test_opts
## %%cmake_build --target check-lldb-unit
## #endregion LLDB unit tests
##
## #region LLDB SB API tests
## reset_test_opts
## %%cmake_build --target check-lldb-api
## #endregion LLDB SB API tests
##
## #region LLDB shell tests
## reset_test_opts
## %%cmake_build --target check-lldb-shell
## #endregion LLDB shell tests
%endif
%endif

#region test libcxx
# TODO(kkleine): Fedora rawhide didn't contain check runs. Evaluate if we want them here.
#endregion test libcxx


#region Test LLD
reset_test_opts
%cmake_build --target check-lld
#endregion Test LLD

#region Test MLIR
%if %{with mlir}
reset_test_opts

%ifarch s390x
# s390x does not support half-float
test_list_filter_out+=("MLIR :: python/ir/array_attributes.py")
test_list_filter_out+=("MLIR :: python/execution_engine.py")
%endif

%ifarch ppc64le
# Medium code model can result in relocation failures, see:
# https://github.com/llvm/llvm-project/issues/129499

# Additionally, support for converting to/from fp16 was added on
# Power9 processors (aka. Power ISA 3.0). Even if the above issue
# is fixed, avoid running execution_engine.py on servers that do
# not support this ISA level, using the following condition:
# if ! LD_SHOW_AUXV=1 /bin/true | grep -q arch_3_00; then
test_list_filter_out+=("MLIR :: python/execution_engine.py")
test_list_filter_out+=("MLIR :: python/multithreaded_tests.py")
%endif

%if %{with flang}
# TODO(kkleine): This test needs to be re-enabled. I currently only fails when building with flang.
# Here's the test failure: https://gist.github.com/kwk/5d551e27a28dfc1b34a09dca781f91df
test_list_filter_out+=("MLIR :: mlir-pdll-lsp-server/view-output.test")
%endif

adjust_lit_filter_out test_list_filter_out

export PYTHONPATH=%{buildroot}/%{python3_sitearch}
%cmake_build --target check-mlir
%endif
#endregion Test MLIR

#region BOLT tests
%if %{with build_bolt}
reset_test_opts

# Beginning with LLVM 20 this test has the "non-root-user" requirement
# and then the test should pass. But now it is flaky, hence we can only
# filter it out.
test_list_filter_out+=("BOLT :: unreadable-profile.test")

%ifarch aarch64
# Failing test cases on aarch64
# TODO(kkleine): The following used to fail on aarch64 but passed today.
#export LIT_XFAIL="$LIT_XFAIL;cache+-deprecated.test"
#export LIT_XFAIL="$LIT_XFAIL;bolt-icf.test"
#export LIT_XFAIL="$LIT_XFAIL;R_ABS.pic.lld.cpp"

# The following tests require LSE in order to run.
# More info at: https://github.com/llvm/llvm-project/issues/86485
if ! grep -q atomics /proc/cpuinfo; then
  test_list_filter_out+=("BOLT :: runtime/AArch64/basic-instrumentation.test")
  test_list_filter_out+=("BOLT :: runtime/AArch64/hook-fini.test")
  test_list_filter_out+=("BOLT :: runtime/AArch64/instrumentation-ind-call.c")
  test_list_filter_out+=("BOLT :: runtime/exceptions-instrumentation.test")
  test_list_filter_out+=("BOLT :: runtime/instrumentation-indirect-2.c")
  test_list_filter_out+=("BOLT :: runtime/pie-exceptions-split.test")
fi
%endif

adjust_lit_filter_out test_list_filter_out

%cmake_build --target check-bolt
%endif
#endregion BOLT tests

#region polly tests
%if %{with polly}
reset_test_opts
%cmake_build --target check-polly
%endif
#endregion polly tests

#region flang tests
%if %{with flang}
reset_test_opts

# https://github.com/llvm/llvm-project/issues/126051
test_list_filter_out+=("Flang :: Driver/linker-flags.f90")

# We filter our the location.f90 test for now because with LTO+PGO enabled,
# We miss the location.f90 entry in the loc_kind_array[ base, inclusion] entry.
# https://github.com/llvm/llvm-project/issues/156629
test_list_filter_out+=("Flang :: Lower/location.f90")

adjust_lit_filter_out test_list_filter_out

%cmake_build --target check-flang
%cmake_build --target check-flang-rt

%endif
#endregion flang tests

%endif

%if %{with snapshot_build}
# Do this here instead of in install so the check targets are also included.
cp %{_vpath_builddir}/.ninja_log %{buildroot}%{_datadir}
%endif

#endregion check

#region misc
%ldconfig_scriptlets -n %{pkg_name-llvm}-libs

%if %{without compat_build}
%ldconfig_scriptlets -n %{pkg_name_lld}-libs
%endif

%post -n %{pkg_name_llvm}-devel
update-alternatives --install %{_bindir}/llvm-config-%{maj_ver} llvm-config-%{maj_ver} %{install_bindir}/llvm-config %{__isa_bits}
%if %{without compat_build}
# Prioritize newer LLVM versions over older and 64-bit over 32-bit.
update-alternatives --install %{_bindir}/llvm-config llvm-config %{install_bindir}/llvm-config $((%{maj_ver}*100+%{__isa_bits}))

# Remove old llvm-config-%{__isa_bits} alternative. This will only do something during the
# first upgrade from a version that used it. In all other cases it will error, so suppress the
# expected error message.
update-alternatives --remove llvm-config %{_bindir}/llvm-config-%{__isa_bits} 2>/dev/null ||:

# During the upgrade from LLVM 16 (F38) to LLVM 17 (F39), we found out the
# main llvm-devel package was leaving entries in the alternatives system.
# Try to remove them now.
for v in 14 15 16; do
  if [[ -e %{_bindir}/llvm-config-$v
        && "x$(%{_bindir}/llvm-config-$v --version | awk -F . '{ print $1 }')" != "x$v" ]]; then
    update-alternatives --remove llvm-config-$v %{install_bindir}/llvm-config%{exec_suffix}-%{__isa_bits}
  fi
done
%endif

%postun -n %{pkg_name_llvm}-devel
if [ $1 -eq 0 ]; then
  update-alternatives --remove llvm-config%{exec_suffix} %{install_bindir}/llvm-config
fi
%if %{without compat_build}
# There are a number of different cases here:
# Uninstall: Remove alternatives.
# Patch version upgrade: Keep alternatives.
# Major version upgrade with installation of compat package: Keep alternatives for compat package.
# Major version upgrade without installation of compat package: Remove alternatives. However, we
# can't distinguish it from the previous case, so we conservatively leave it behind.
if [ $1 -eq 0 ]; then
  update-alternatives --remove llvm-config-%{maj_ver} %{install_bindir}/llvm-config
fi
%endif

%if %{without compat_build}
%post -n %{pkg_name_lld}
update-alternatives --install %{_bindir}/ld ld %{_bindir}/ld.lld 1

%postun -n %{pkg_name_lld}
if [ $1 -eq 0 ] ; then
  update-alternatives --remove ld %{_bindir}/ld.lld
fi
%endif
#endregion misc

#region files
%define expand_bins() %{lua:
  local bindir = rpm.expand("%{_bindir}")
  local install_bindir = rpm.expand("%{install_bindir}")
  local maj_ver = rpm.expand("%{maj_ver}")
  for arg in rpm.expand("%*"):gmatch("%S+") do
    print(install_bindir .. "/" .. arg .. "\\n")
    print(bindir .. "/" .. arg .. "-" .. maj_ver .. "\\n")
    if rpm.expand("%{without compat_build}") == "1" then
      print(bindir .. "/" .. arg .. "\\n")
    end
  end
}

%define expand_mans() %{lua:
  local mandir = rpm.expand("%{_mandir}")
  local maj_ver = rpm.expand("%{maj_ver}")
  for arg in rpm.expand("%*"):gmatch("%S+") do
    print(mandir .. "/man1/" .. arg .. "-" .. maj_ver .. ".1.gz\\n")
    if rpm.expand("%{without compat_build}") == "1" then
      print(mandir .. "/man1/" .. arg .. ".1.gz\\n")
    end
  end
}

%define expand_generic(d:i:) %{lua:
  local dir = rpm.expand("%{-d*}")
  local install_dir = rpm.expand("%{-i*}")
  for arg in rpm.expand("%*"):gmatch("%S+") do
    print(install_dir .. "/" .. arg .. "\\n")
    if rpm.expand("%{without compat_build}") == "1" then
      print(dir .. "/" .. arg .. "\\n")
    end
  end
}

%define expand_libs() %{expand_generic -d %{_libdir} -i %{install_libdir}  %*}
%define expand_libexecs() %{expand_generic -d %{_libexecdir} -i %{install_libexecdir} %*}
%define expand_includes() %{expand_generic -d %{_includedir} -i %{install_includedir} %*}
%define expand_datas() %{expand_generic -d %{_datadir} -i %{install_datadir} %*}

#region LLVM lit files
%if %{with python_lit}
%files -n python%{python3_pkgversion}-lit
%license llvm/utils/lit/LICENSE.TXT
%doc llvm/utils/lit/README.rst
%{python3_sitelib}/lit/
%{python3_sitelib}/lit-*-info/
%{_bindir}/lit
%endif
#endregion LLVM lit files

#region LLVM files

%files -n %{pkg_name_llvm}-filesystem
%dir %{install_prefix}
%dir %{install_bindir}
%dir %{install_includedir}
%dir %{install_libdir}
%dir %{install_libdir}/cmake
%dir %{install_libexecdir}
%dir %{install_datadir}

%files -n %{pkg_name_llvm}
%license llvm/LICENSE.TXT

%{expand_bins %{expand:
    bugpoint
    dsymutil
    FileCheck
    llc
    lli
    llvm-addr2line
    llvm-ar
    llvm-as
    llvm-bcanalyzer
    llvm-bitcode-strip
    llvm-c-test
    llvm-cat
    llvm-cfi-verify
    llvm-cgdata
    llvm-cov
    llvm-ctxprof-util
    llvm-cvtres
    llvm-cxxdump
    llvm-cxxfilt
    llvm-cxxmap
    llvm-debuginfo-analyzer
    llvm-debuginfod
    llvm-debuginfod-find
    llvm-diff
    llvm-dis
    llvm-dlltool
    llvm-dwarfdump
    llvm-dwarfutil
    llvm-dwp
    llvm-exegesis
    llvm-extract
    llvm-gsymutil
    llvm-ifs
    llvm-install-name-tool
    llvm-jitlink
    llvm-jitlink-executor
    llvm-lib
    llvm-libtool-darwin
    llvm-link
    llvm-lipo
    llvm-lto
    llvm-lto2
    llvm-mc
    llvm-mca
    llvm-ml
    llvm-ml64
    llvm-modextract
    llvm-mt
    llvm-nm
    llvm-objcopy
    llvm-objdump
    llvm-opt-report
    llvm-otool
    llvm-pdbutil
    llvm-PerfectShuffle
    llvm-profdata
    llvm-profgen
    llvm-ranlib
    llvm-rc
    llvm-readelf
    llvm-readobj
    llvm-readtapi
    llvm-reduce
    llvm-remarkutil
    llvm-rtdyld
    llvm-sim
    llvm-size
    llvm-split
    llvm-stress
    llvm-strings
    llvm-strip
    llvm-symbolizer
    llvm-tblgen
    llvm-tli-checker
    llvm-undname
    llvm-windres
    llvm-xray
    reduce-chunk-list
    obj2yaml
    opt
    sancov
    sanstats
    split-file
    UnicodeNameMappingGenerator
    verify-uselistorder
    yaml2obj
}}

%if %{maj_ver} >= 22
%{expand_bins %{expand:
    llvm-ir2vec
    llvm-offload-wrapper
    llvm-offload-binary
}}
%endif

%{expand_mans %{expand:
    bugpoint
    clang-tblgen
    dsymutil
    FileCheck
    lit
    llc
    lldb-tblgen
    lli
    llvm-addr2line
    llvm-ar
    llvm-as
    llvm-bcanalyzer
    llvm-cgdata
    llvm-cov
    llvm-cxxfilt
    llvm-cxxmap
    llvm-debuginfo-analyzer
    llvm-diff
    llvm-dis
    llvm-dwarfdump
    llvm-dwarfutil
    llvm-exegesis
    llvm-extract
    llvm-ifs
    llvm-install-name-tool
    llvm-lib
    llvm-libtool-darwin
    llvm-link
    llvm-lipo
    llvm-locstats
    llvm-mc
    llvm-mca
    llvm-nm
    llvm-objcopy
    llvm-objdump
    llvm-opt-report
    llvm-otool
    llvm-pdbutil
    llvm-profdata
    llvm-profgen
    llvm-ranlib
    llvm-readelf
    llvm-readobj
    llvm-reduce
    llvm-remarkutil
    llvm-size
    llvm-stress
    llvm-strings
    llvm-strip
    llvm-symbolizer
    llvm-tblgen
    llvm-tli-checker
    mlir-tblgen
    opt
    tblgen
}}

%if %{maj_ver} >= 22
%{expand_mans %{expand:
    llvm-ir2vec
    llvm-offload-binary
}}
%endif

%expand_datas opt-viewer

%files -n %{pkg_name_llvm}-libs
%license llvm/LICENSE.TXT
%{expand_libs %{expand:
    libLLVM-%{maj_ver}%{?llvm_snapshot_version_suffix}.so
    libLLVM.so.%{maj_ver}.%{min_ver}%{?llvm_snapshot_version_suffix}
    libLTO.so*
    libRemarks.so*
}}
%if %{with gold}
%expand_libs LLVMgold.so
%if %{without compat_build}
%{_libdir}/bfd-plugins/LLVMgold.so
%endif
%endif

%if %{with compat_build}
%config(noreplace) %{_sysconfdir}/ld.so.conf.d/%{pkg_name_llvm}-%{_arch}.conf
%endif
%if %{with bundle_compat_lib}
%{_libdir}/libLLVM.so.%{compat_maj_ver}*
%endif

%files -n %{pkg_name_llvm}-devel
%license llvm/LICENSE.TXT

%{install_bindir}/llvm-config
%ghost %{_bindir}/llvm-config-%{maj_ver}
%if %{without compat_build}
%ghost %{_bindir}/llvm-config
%endif

%expand_mans llvm-config
%expand_includes llvm llvm-c
%{expand_libs %{expand:
    libLLVM.so
    cmake/llvm
}}

%files -n %{pkg_name_llvm}-doc
%license llvm/LICENSE.TXT
%doc %{_pkgdocdir}/html/index.html

%files -n %{pkg_name_llvm}-static
%license llvm/LICENSE.TXT
%expand_libs libLLVM*.a
%exclude %{install_libdir}/libLLVMTestingSupport.a
%exclude %{install_libdir}/libLLVMTestingAnnotations.a
%if %{without compat_build}
%exclude %{_libdir}/libLLVMTestingSupport.a
%exclude %{_libdir}/libLLVMTestingAnnotations.a
%endif

%files -n %{pkg_name_llvm}-cmake-utils
%license llvm/LICENSE.TXT
%expand_datas llvm-cmake

%files -n %{pkg_name_llvm}-test
%license llvm/LICENSE.TXT
%{expand_bins %{expand:
    not
    count
    yaml-bench
    lli-child-target
    llvm-isel-fuzzer
    llvm-opt-fuzzer
    llvm-test-mustache-spec
}}
%if %{maj_ver} >= 22
%{expand_bins %{expand:
    llvm-cas
}}
%endif
%{expand_mans %{expand:
    llvm-test-mustache-spec
}}

%files -n %{pkg_name_llvm}-googletest
%license llvm/LICENSE.TXT
%{expand_libs %{expand:
    libLLVMTestingSupport.a
    libLLVMTestingAnnotations.a
    libllvm_gtest.a
    libllvm_gtest_main.a
}}
%expand_includes llvm-gtest llvm-gmock

%if %{with snapshot_build}
%files -n %{pkg_name_llvm}-build-stats
%{_datadir}/.ninja_log
%endif

#endregion LLVM files

#region CLANG files

%files -n %{pkg_name_clang}
%license clang/LICENSE.TXT
%{expand_bins %{expand:
    clang
    clang++
    clang-cl
    clang-cpp
    clang-scan-deps
}}
%{install_bindir}/clang-%{maj_ver}

%{_sysconfdir}/%{pkg_name_clang}/%{_target_platform}-clang.cfg
%{_sysconfdir}/%{pkg_name_clang}/%{_target_platform}-clang++.cfg
%ifarch x86_64
%{_sysconfdir}/%{pkg_name_clang}/i386-redhat-linux-gnu-clang.cfg
%{_sysconfdir}/%{pkg_name_clang}/i386-redhat-linux-gnu-clang++.cfg
%endif
%{expand_mans clang clang++}

%if 0%{with pgo}
%{expand_datas %{expand: llvm-pgo.profdata }}
%endif


%files -n %{pkg_name_clang}-libs
%license clang/LICENSE.TXT
%{_prefix}/lib/clang/%{maj_ver}/include/*
# Part of compiler-rt:
%exclude %{_prefix}/lib/clang/%{maj_ver}/include/fuzzer
%exclude %{_prefix}/lib/clang/%{maj_ver}/include/orc
%exclude %{_prefix}/lib/clang/%{maj_ver}/include/profile
%exclude %{_prefix}/lib/clang/%{maj_ver}/include/sanitizer
%exclude %{_prefix}/lib/clang/%{maj_ver}/include/xray
# Part of libomp-devel:
%exclude %{_prefix}/lib/clang/%{maj_ver}/include/omp*.h

%expand_libs libclang.so.%{maj_ver}*
%expand_libs libclang-cpp.so.%{maj_ver}*
%if %{with bundle_compat_lib}
%{_libdir}/libclang.so.%{compat_maj_ver}*
%{_libdir}/libclang-cpp.so.%{compat_maj_ver}*
%endif

%files -n %{pkg_name_clang}-devel
%license clang/LICENSE.TXT
%{expand_libs %{expand:
    cmake/clang
    libclang-cpp.so
    libclang.so
}}
%expand_includes clang clang-c
%expand_bins clang-tblgen
%dir %{install_datadir}/clang/
%if %{without compat_build}
%dir %{_datadir}/clang
%endif

%files -n %{pkg_name_clang}-resource-filesystem
%license clang/LICENSE.TXT
%dir %{_prefix}/lib/clang/
%dir %{_prefix}/lib/clang/%{maj_ver}/
%dir %{_prefix}/lib/clang/%{maj_ver}/bin/
%dir %{_prefix}/lib/clang/%{maj_ver}/include/
%dir %{_prefix}/lib/clang/%{maj_ver}/lib/
%dir %{_prefix}/lib/clang/%{maj_ver}/share/
%{_rpmmacrodir}/macros.%{pkg_name_clang}

%files -n %{pkg_name_clang}-analyzer
%license clang/LICENSE.TXT
%{expand_bins %{expand:
    scan-view
    scan-build
    analyze-build
    intercept-build
}}
%{expand_libexecs %{expand:
    ccc-analyzer
    c++-analyzer
    analyze-c++
    analyze-cc
    intercept-c++
    intercept-cc
}}
%expand_datas scan-view scan-build
%expand_mans scan-build
%if %{without compat_build}
%expand_bins scan-build-py
%{python3_sitelib}/libear
%{python3_sitelib}/libscanbuild
%endif

%files -n %{pkg_name_clang}-tools-extra
%license clang-tools-extra/LICENSE.TXT
%{expand_bins %{expand:
    amdgpu-arch
    clang-apply-replacements
    clang-change-namespace
    clang-check
    clang-doc
    clang-extdef-mapping
    clang-format
    clang-include-cleaner
    clang-include-fixer
    clang-installapi
    clang-move
    clang-offload-bundler
    clang-offload-packager
    clang-linker-wrapper
    clang-nvlink-wrapper
    clang-query
    clang-refactor
    clang-reorder-fields
    clang-repl
    clang-sycl-linker
    clang-tidy
    clangd
    diagtool
    hmaptool
    nvptx-arch
    pp-trace
    c-index-test
    find-all-symbols
    modularize
    clang-format-diff
    run-clang-tidy
    offload-arch
}}

%if %{without compat_build}
%{_emacs_sitestartdir}/clang-format.el
%{_emacs_sitestartdir}/clang-include-fixer.el
%endif
%expand_mans diagtool extraclangtools
%{expand_datas %{expand:
    clang/clang-format.py*
    clang/clang-format-diff.py*
    clang/clang-include-fixer.py*
    clang/clang-tidy-diff.py*
    clang/run-find-all-symbols.py*
}}

%files -n %{pkg_name_clang}-tools-extra-devel
%license clang-tools-extra/LICENSE.TXT
%expand_includes clang-tidy

%files -n git-clang-format%{pkg_suffix}
%license clang/LICENSE.TXT
%expand_bins git-clang-format

%if %{without compat_build}
%files -n python%{python3_pkgversion}-clang
%license clang/LICENSE.TXT
%{python3_sitelib}/clang/
%endif

#endregion CLANG files

#region COMPILER-RT files

%files -n %{pkg_name_compiler_rt}
%license compiler-rt/LICENSE.TXT
%ifarch x86_64 aarch64 riscv64
%{_prefix}/lib/clang/%{maj_ver}/bin/hwasan_symbolize
%endif
%{_prefix}/lib/clang/%{maj_ver}/include/fuzzer
%{_prefix}/lib/clang/%{maj_ver}/include/orc
%{_prefix}/lib/clang/%{maj_ver}/include/profile
%{_prefix}/lib/clang/%{maj_ver}/include/sanitizer
%{_prefix}/lib/clang/%{maj_ver}/include/xray

%{_prefix}/lib/clang/%{maj_ver}/share/*.txt

# Files that appear on all targets
%{_prefix}/lib/clang/%{maj_ver}/lib/%{compiler_rt_triple}/libclang_rt.*
%{_prefix}/lib/clang/%{maj_ver}/lib/%{compiler_rt_triple}/clang_rt.crtbegin.o
%{_prefix}/lib/clang/%{maj_ver}/lib/%{compiler_rt_triple}/clang_rt.crtend.o

%ifnarch %{ix86} s390x riscv64
%{_prefix}/lib/clang/%{maj_ver}/lib/%{compiler_rt_triple}/liborc_rt.a
%endif
%ifarch s390x
%if %{maj_ver} >= 22
%{_prefix}/lib/clang/%{maj_ver}/lib/%{compiler_rt_triple}/liborc_rt.a
%endif
%endif

# Additional symlink if two triples are in use.
%if "%{llvm_triple}" != "%{compiler_rt_triple}"
%{_prefix}/lib/clang/%{maj_ver}/lib/%{llvm_triple}
%endif

#endregion COMPILER-RT files

#region OPENMP files

%files -n %{pkg_name_libomp}
%license openmp/LICENSE.TXT
%{expand_libs %{expand:
    libomp.so
    libompd.so
    libarcher.so
}}
%if %{with offload}
%expand_libs libomptarget.so.%{so_suffix}
%expand_libs libLLVMOffload.so.%{so_suffix}
%endif

%files -n %{pkg_name_libomp}-devel
%license openmp/LICENSE.TXT
%{_prefix}/lib/clang/%{maj_ver}/include/omp.h
%{_prefix}/lib/clang/%{maj_ver}/include/ompx.h
%{_prefix}/lib/clang/%{maj_ver}/include/omp-tools.h
%{_prefix}/lib/clang/%{maj_ver}/include/ompt.h
%{_prefix}/lib/clang/%{maj_ver}/include/ompt-multiplex.h
%expand_libs cmake/openmp
%if %{with offload}
%{expand_libs %{expand:
    libomptarget.so
    libLLVMOffload.so
}}

%{expand_libs %{expand:
    amdgcn-amd-amdhsa/libompdevice.a
    amdgcn-amd-amdhsa/libomptarget-amdgpu.bc
    nvptx64-nvidia-cuda/libompdevice.a
    nvptx64-nvidia-cuda/libomptarget-nvptx.bc
}}

%expand_includes offload
%endif
#endregion OPENMP files

#region LLD files

%files -n %{pkg_name_lld}
%license lld/LICENSE.TXT
%ghost %{_bindir}/ld
%{expand_bins %{expand:
    lld
    lld-link
    ld.lld
    ld64.lld
    wasm-ld
}}
%expand_mans ld.lld

%files -n %{pkg_name_lld}-devel
%license lld/LICENSE.TXT
%expand_includes lld
%{expand_libs %{expand:
    liblldCOFF.so
    liblldCommon.so
    liblldELF.so
    liblldMachO.so
    liblldMinGW.so
    liblldWasm.so
    cmake/lld
}}

%files -n %{pkg_name_lld}-libs
%license lld/LICENSE.TXT
%{expand_libs %{expand:
    liblldCOFF.so.*
    liblldCommon.so.*
    liblldELF.so.*
    liblldMachO.so.*
    liblldMinGW.so.*
    liblldWasm.so.*
}}

#endregion LLD files

#region Toolset files
%if 0%{?rhel}
%files -n %{pkg_name_llvm}-toolset
%license LICENSE.TXT
%endif
#endregion Toolset files

#region LLDB files
%if %{with lldb}
%files -n %{pkg_name_lldb}
%license lldb/LICENSE.TXT
%{expand_bins %{expand:
    lldb
    lldb-argdumper
    lldb-dap
    lldb-instr
    lldb-server
}}
%if %{maj_ver} >= 22
%{expand_bins %{expand:
    lldb-mcp
}}
%endif
# Usually, *.so symlinks are kept in devel subpackages. However, the python
# bindings depend on this symlink at runtime.
%{expand_libs %{expand:
    liblldb*.so
    liblldb.so.*
    liblldbIntelFeatures.so.*
}}
%expand_mans lldb-server lldb
%if %{with bundle_compat_lib}
%{_libdir}/liblldb.so.%{compat_maj_ver}*
%endif

%files -n %{pkg_name_lldb}-devel
%expand_includes lldb
%if %{maj_ver} >= 22
%{expand_bins %{expand:
    lldb-tblgen
    yaml2macho-core
}}
%endif

%if %{without compat_build}
%files -n python%{python3_pkgversion}-lldb
%{python3_sitearch}/lldb
%endif
%endif
#endregion LLDB files


#region MLIR files
%if %{with mlir}
%files -n %{pkg_name_mlir}
%license LICENSE.TXT
%{expand_libs %{expand:
    libmlir_arm_runner_utils.so.%{maj_ver}*
    libmlir_arm_sme_abi_stubs.so.%{maj_ver}*
    libmlir_async_runtime.so.%{maj_ver}*
    libmlir_c_runner_utils.so.%{maj_ver}*
    libmlir_float16_utils.so.%{maj_ver}*
    libmlir_runner_utils.so.%{maj_ver}*
    libMLIR*.so.%{maj_ver}*
}}

%if %{maj_ver} >= 22
%{expand_libs %{expand:
    libmlir_apfloat_wrappers.so.%{maj_ver}*
}}
%endif

%files -n %{pkg_name_mlir}-static
%expand_libs libMLIR*.a

%files -n %{pkg_name_mlir}-devel
%{expand_bins %{expand:
    mlir-linalg-ods-yaml-gen
    mlir-lsp-server
    mlir-opt
    mlir-pdll
    mlir-pdll-lsp-server
    mlir-query
    mlir-reduce
    mlir-rewrite
    mlir-runner
    mlir-tblgen
    mlir-translate
    tblgen-lsp-server
    tblgen-to-irdl
}}
%expand_includes mlir mlir-c
%{expand_libs %{expand:
    cmake/mlir
    libmlir_arm_runner_utils.so
    libmlir_arm_sme_abi_stubs.so
    libmlir_async_runtime.so
    libmlir_c_runner_utils.so
    libmlir_float16_utils.so
    libmlir_runner_utils.so
    libMLIR*.so
}}

%if %{maj_ver} >= 22
%{expand_libs %{expand:
    libmlir_apfloat_wrappers.so
}}
%endif

%files -n python%{python3_pkgversion}-%{pkg_name_mlir}
%{python3_sitearch}/mlir/
%endif
#endregion MLIR files

#region libcxx files

#region flang files
%if %{with flang}
%files -n %{pkg_name_flang}
%license flang/LICENSE.TXT
%{expand_mans flang}
%{expand_bins %{expand:
    tco
    bbc
    fir-opt
    fir-lsp-server
    flang
    flang-new
}}
%{install_bindir}/flang-%{maj_ver}
%{expand_includes %{expand:
    flang/__cuda_builtins.mod
    flang/__cuda_device.mod
    flang/__fortran_builtins.mod
    flang/__fortran_ieee_exceptions.mod
    flang/__fortran_type_info.mod
    flang/__ppc_intrinsics.mod
    flang/__ppc_types.mod
    flang/cooperative_groups.mod
    flang/ieee_arithmetic.mod
    flang/ieee_exceptions.mod
    flang/ieee_features.mod
    flang/iso_c_binding.mod
    flang/iso_fortran_env.mod
    flang/mma.mod
    flang/cudadevice.mod
    flang/iso_fortran_env_impl.mod
    flang/omp_lib.mod
    flang/omp_lib_kinds.mod
    flang/flang_debug.mod
}}
%{_sysconfdir}/%{pkg_name_clang}/%{_target_platform}-flang.cfg
%ifarch x86_64
%{_sysconfdir}/%{pkg_name_clang}/i386-redhat-linux-gnu-flang.cfg
%endif

%{_prefix}/lib/clang/%{maj_ver}/include/ISO_Fortran_binding.h

%files -n %{pkg_name_flang}-runtime
%{_prefix}/lib/clang/%{maj_ver}/lib/%{llvm_triple}/libflang_rt.runtime.a
%{_prefix}/lib/clang/%{maj_ver}/lib/%{llvm_triple}/libflang_rt.runtime.so
%config(noreplace) %{_sysconfdir}/ld.so.conf.d/%{pkg_name_flang}-%{_arch}.conf

%endif
#region flang files

%if %{with libcxx}

%files -n %{pkg_name_libcxx}
%license libcxx/LICENSE.TXT
%doc libcxx/CREDITS.TXT libcxx/TODO.TXT
%{_libdir}/libc++.so.*

%files -n %{pkg_name_libcxx}-devel
%{_includedir}/c++/
%exclude %{_includedir}/c++/v1/cxxabi.h
%exclude %{_includedir}/c++/v1/__cxxabi_config.h
%{_libdir}/libc++.so
%{_libdir}/libc++.modules.json
%{_datadir}/libc++/v1/*

%files -n %{pkg_name_libcxx}-static
%license libcxx/LICENSE.TXT
%{_libdir}/libc++.a
%{_libdir}/libc++experimental.a

%files -n %{pkg_name_libcxxabi}
%license libcxxabi/LICENSE.TXT
%doc libcxxabi/CREDITS.TXT
%{_libdir}/libc++abi.so.*

%files -n %{pkg_name_libcxxabi}-devel
%{_includedir}/c++/v1/cxxabi.h
%{_includedir}/c++/v1/__cxxabi_config.h
%{_libdir}/libc++abi.so

%files -n %{pkg_name_libcxxabi}-static
%{_libdir}/libc++abi.a

%files -n %{pkg_name_llvm_libunwind}
%license libunwind/LICENSE.TXT
%{_libdir}/libunwind.so.1
%{_libdir}/libunwind.so.1.0

%files -n %{pkg_name_llvm_libunwind}-devel
%{_includedir}/llvm-libunwind/__libunwind_config.h
%{_includedir}/llvm-libunwind/libunwind.h
%{_includedir}/llvm-libunwind/libunwind.modulemap
%{_includedir}/llvm-libunwind/mach-o/compact_unwind_encoding.h
%{_includedir}/llvm-libunwind/unwind.h
%{_includedir}/llvm-libunwind/unwind_arm_ehabi.h
%{_includedir}/llvm-libunwind/unwind_itanium.h
%dir %{_libdir}/llvm-unwind
%{_libdir}/llvm-unwind/libunwind.so

%files -n %{pkg_name_llvm_libunwind}-static
%{_libdir}/libunwind.a
%endif
#endregion libcxx files

#region BOLT files
%if %{with build_bolt}
%files -n %{pkg_name_bolt}
%license bolt/LICENSE.TXT
%{expand_bins %{expand:
    llvm-bolt
    llvm-boltdiff
    llvm-bolt-binary-analysis
    llvm-bolt-heatmap
    merge-fdata
    perf2bolt
}}

%{expand_libs %{expand:
    libbolt_rt_hugify.a
    libbolt_rt_instr.a
}}
%endif
#endregion BOLT files

#region polly files
%if %{with polly}
%files -n %{pkg_name_polly}
%license polly/LICENSE.TXT
%{expand_libs %{expand:
  LLVMPolly.so
  libPolly.so.*
  libPollyISL.so
}}
%expand_mans polly

%files -n %{pkg_name_polly}-devel
%expand_libs libPolly.so
%expand_includes polly
%expand_libs cmake/polly

%endif
#endregion polly files

#endregion files

%changelog
%{?autochangelog}
%{!?autochangelog:%include %{_sourcedir}/changelog}
