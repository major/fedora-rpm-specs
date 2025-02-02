#region globals
#region version
%global maj_ver 19
%global min_ver 1
%global patch_ver 7
#global rc_ver 4

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

# Build compat packages llvmN instead of main package for the current LLVM
# version. Used on Fedora.
%bcond_with compat_build
# Bundle compat libraries for a previous LLVM version, as part of llvm-libs and
# clang-libs. Used on RHEL.
%bcond_with bundle_compat_lib
%bcond_without check

%if %{with bundle_compat_lib}
%global compat_maj_ver 18
%global compat_ver %{compat_maj_ver}.1.8
%endif

# Compat builds do not include python-lit and lldb
%if %{with compat_build}
%bcond_with python_lit
%bcond_with lldb
%else
%bcond_without python_lit
%bcond_without lldb
%endif

%if %{without compat_build} && 0%{?fedora} >= 41
%ifarch %{ix86}
%bcond_with mlir
%else
%bcond_without mlir
%endif
%else
%bcond_with mlir
%endif

# The libcxx build condition also enables libcxxabi and libunwind.
# Fedora 41 is the first version that enabled FatLTO for clang-built files.
# Without FatLTO, we can't enable ThinLTO and link using GNU LD.
%if %{without compat_build} && 0%{?fedora} >= 41
%bcond_without libcxx
%else
%bcond_with libcxx
%endif

# I've called the build condition "build_bolt" to indicate that this does not
# necessarily "use" BOLT in order to build LLVM.
%if %{without compat_build} && 0%{?fedora} >= 41
# BOLT only supports aarch64 and x86_64
%ifarch aarch64 x86_64
%bcond_without build_bolt
%else
%bcond_with build_bolt
%endif
%else
%bcond_with build_bolt
%endif

%if %{without compat_build} && 0%{?fedora} >= 41
%bcond_without polly
%else
%bcond_with polly
%endif

# Disable LTO on x86 and riscv in order to reduce memory consumption.
%ifarch %ix86 riscv64
%bcond_with lto_build
%else
%bcond_without lto_build
%endif

%if %{without lto_build}
%global _lto_cflags %nil
%endif

# We are building with clang for faster/lower memory LTO builds.
# See https://docs.fedoraproject.org/en-US/packaging-guidelines/#_compiler_macros
%global toolchain clang


%if %{defined rhel} && 0%{?rhel} < 10
%global gts_version 14
%endif

# Opt out of https://fedoraproject.org/wiki/Changes/fno-omit-frame-pointer
# https://bugzilla.redhat.com/show_bug.cgi?id=2158587
%undefine _include_frame_pointers

# Suffixless tarball name (essentially: basename -s .tar.xz llvm-project-17.0.6.src.tar.xz)
%if %{with snapshot_build}
%global src_tarball_dir llvm-project-%{llvm_snapshot_git_revision}
%else
%global src_tarball_dir llvm-project-%{maj_ver}.%{min_ver}.%{patch_ver}%{?rc_ver:-rc%{rc_ver}}.src
%endif

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
%global install_libdir %{install_prefix}/lib
%global install_datadir %{install_prefix}/share
%global install_mandir %{install_prefix}/share/man
%global install_libexecdir %{install_prefix}/libexec
%global build_libdir llvm/%{_vpath_builddir}/lib
%global unprefixed_libdir lib

%if 0%{?rhel}
%global targets_to_build "X86;AMDGPU;PowerPC;NVPTX;SystemZ;AArch64;ARM;Mips;BPF;WebAssembly"
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
%global pkg_name_lldb lldb
#endregion LLDB globals
#endregion globals

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

#region packages
#region main package
Name:		%{pkg_name_llvm}
Version:	%{maj_ver}.%{min_ver}.%{patch_ver}%{?rc_ver:~rc%{rc_ver}}%{?llvm_snapshot_version_suffix:~%{llvm_snapshot_version_suffix}}
Release:	5%{?dist}
Summary:	The Low Level Virtual Machine

License:	Apache-2.0 WITH LLVM-exception OR NCSA
URL:		http://llvm.org

%if %{with snapshot_build}
Source0: https://github.com/llvm/llvm-project/archive/%{llvm_snapshot_git_revision}.tar.gz
%else
Source0: https://github.com/llvm/llvm-project/releases/download/llvmorg-%{maj_ver}.%{min_ver}.%{patch_ver}%{?rc_ver:-rc%{rc_ver}}/%{src_tarball_dir}.tar.xz
Source1: https://github.com/llvm/llvm-project/releases/download/llvmorg-%{maj_ver}.%{min_ver}.%{patch_ver}%{?rc_ver:-rc%{rc_ver}}/%{src_tarball_dir}.tar.xz.sig
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

#region OpenMP patches
Patch1900: 0001-openmp-Add-option-to-disable-tsan-tests-111548.patch
Patch1901: 0001-openmp-Use-core_siblings_list-if-physical_package_id.patch
#endregion OpenMP patches

#region CLANG patches
Patch101: 0001-PATCH-clang-Make-funwind-tables-the-default-on-all-a.patch
Patch102: 0003-PATCH-clang-Don-t-install-static-libraries.patch
#endregion CLANG patches

# Workaround a bug in ORC on ppc64le.
# More info is available here: https://reviews.llvm.org/D159115#4641826
Patch103: 0001-Workaround-a-bug-in-ORC-on-ppc64le.patch

# With the introduction of --gcc-include-dir in the clang config file,
# this might no longer be needed.
Patch104: 0001-Driver-Give-devtoolset-path-precedence-over-Installe.patch

# Fix LLVMConfig.cmake when symlinks are used.
Patch105: 0001-cmake-Resolve-symlink-when-finding-install-prefix.patch

#region MLIR patches
# See https://github.com/llvm/llvm-project/pull/108579
Patch1904: 0001-mlir-python-Reuse-the-library-directory.patch
# See https://github.com/llvm/llvm-project/pull/108461
Patch1905: 0001-CMake-Add-missing-dependency-108461.patch
# See https://github.com/llvm/llvm-project/pull/118542
Patch1906: 0001-mlir-Specify-deps-via-LLVM_LINK_COMPONENTS.patch
# See https://github.com/llvm/llvm-project/pull/120079
Patch1907: 0001-CMake-Use-correct-exports-for-MLIR-tools.patch
Patch1908: cstdint.patch
#endregion MLIR patches

#region BOLT patches
Patch1909: 0001-19-PATCH-Bolt-CMake-Don-t-export-bolt-libraries-in-LLVM.patch
#endregion BOLT patches

#region polly patches
# See https://github.com/llvm/llvm-project/pull/122123
Patch1910: 122123.patch
Patch1911: 0001-19-polly-shared-libs.patch
Patch2001: 0001-20-polly-shared-libs.patch
Patch2101: 0001-20-polly-shared-libs.patch
#endregion polly patches

#region LLD patches
Patch1800: 0001-18-Always-build-shared-libs-for-LLD.patch
Patch1902: 0001-19-Always-build-shared-libs-for-LLD.patch
Patch2000: 0001-19-Always-build-shared-libs-for-LLD.patch
Patch2100: 0001-19-Always-build-shared-libs-for-LLD.patch
#endregion LLD patches

#region RHEL patches
# RHEL 8 only
Patch501: 0001-Fix-page-size-constant-on-aarch64-and-ppc64le.patch
#endregion RHEL patches

# Backport with modifications from
# https://github.com/llvm/llvm-project/pull/99273
# Fixes RHEL-49517.
Patch1801: 18-99273.patch

# Fix profiling after a binutils NOTE change.
# https://github.com/llvm/llvm-project/pull/114907
Patch1802: 0001-profile-Use-base-vaddr-for-__llvm_write_binary_ids-n.patch
Patch1903: 0001-profile-Use-base-vaddr-for-__llvm_write_binary_ids-n.patch

# Fix an isel error triggered by Rust 1.85 on s390x
# https://github.com/llvm/llvm-project/issues/124001
Patch1803: 0001-SystemZ-Fix-ICE-with-i128-i64-uaddo-carry-chain.patch
Patch1912: 0001-SystemZ-Fix-ICE-with-i128-i64-uaddo-carry-chain.patch

%if 0%{?rhel} == 8
%global python3_pkgversion 3.12
%global __python3 /usr/bin/python3.12
%endif

%if %{defined gts_version}
# Required for 64-bit atomics on i686.
BuildRequires: gcc-toolset-%{gts_version}-libatomic-devel
BuildRequires: gcc-toolset-%{gts_version}-gcc-c++
%endif
BuildRequires:	gcc
BuildRequires:	gcc-c++
BuildRequires:	clang
BuildRequires:	cmake
BuildRequires:	chrpath
BuildRequires:	ninja-build
BuildRequires:	zlib-devel
BuildRequires:	libzstd-devel
BuildRequires:	libffi-devel
BuildRequires:	ncurses-devel
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
# LLVM's LineEditor library will use libedit if it is available.
BuildRequires:	libedit-devel
# We need python3-devel for %%py3_shebang_fix
BuildRequires:	python%{python3_pkgversion}-devel
BuildRequires:	python%{python3_pkgversion}-setuptools
%if 0%{?rhel} == 8
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
%if %{maj_ver} >= 20
BuildRequires: python%{python3_pkgversion}-nanobind-devel
%endif
%endif

BuildRequires:	graphviz

# This is required because we need "ps" when running LLDB tests
BuildRequires: procps-ng

# For reproducible pyc file generation
# See https://docs.fedoraproject.org/en-US/packaging-guidelines/Python_Appendix/#_byte_compilation_reproducibility
# Since Fedora 41 this happens automatically, and RHEL 8 does not support this.
%if %{without compat_build} && ((%{defined fedora} && 0%{?fedora} < 41) || 0%{?rhel} == 9 || 0%{?rhel} == 10)
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
Requires: python%{python3_pkgversion}-setuptools
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

%package -n %{pkg_name_llvm}-devel
Summary:	Libraries and header files for LLVM
Requires:	%{pkg_name_llvm}%{?_isa} = %{version}-%{release}
Requires:	%{pkg_name_llvm}-libs%{?_isa} = %{version}-%{release}
# The installed LLVM cmake files will add -ledit to the linker flags for any
# app that requires the libLLVMLineEditor, so we need to make sure
# libedit-devel is available.
Requires:	libedit-devel
Requires:	libzstd-devel
# The installed cmake files reference binaries from llvm-test, llvm-static, and
# llvm-gtest.  We tried in the past to split the cmake exports for these binaries
# out into separate files, so that llvm-devel would not need to Require these packages,
# but this caused bugs (rhbz#1773678) and forced us to carry two non-upstream
# patches.
Requires:	%{pkg_name_llvm}-static%{?_isa} = %{version}-%{release}
Requires:	%{pkg_name_llvm}-test%{?_isa} = %{version}-%{release}
Requires:	%{pkg_name_llvm}-googletest%{?_isa} = %{version}-%{release}


Requires(post):	%{_sbindir}/alternatives
Requires(postun):	%{_sbindir}/alternatives

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

%description -n %{pkg_name_llvm}-libs
Shared libraries for the LLVM compiler infrastructure.

%package -n %{pkg_name_llvm}-static
Summary:	LLVM static libraries
Conflicts:	%{pkg_name_llvm}-devel < 8

Provides:	llvm-static(major) = %{maj_ver}

%description -n %{pkg_name_llvm}-static
Static libraries for the LLVM compiler infrastructure.

%package -n %{pkg_name_llvm}-cmake-utils
Summary: CMake utilities shared across LLVM subprojects

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
Recommends: libatomic%{?_isa}
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

Requires: clang-resource-filesystem%{?_isa} = %{version}-%{release}
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
Requires: clang-resource-filesystem%{?_isa} = %{version}-%{release}

Provides: libomp-devel(major) = %{maj_ver}

%description  -n %{pkg_name_libomp}-devel
OpenMP header files.
URL: http://openmp.llvm.org

#endregion OPENMP packages

#region LLD packages

%package -n %{pkg_name_lld}
Summary:	The LLVM Linker

Requires(post): %{_sbindir}/update-alternatives
Requires(preun): %{_sbindir}/update-alternatives

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
Requires:	clang = %{version}-%{release}
Requires:	llvm = %{version}-%{release}
Requires:	lld = %{version}-%{release}

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
Requires:	python%{python3_pkgversion}-lldb

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

%package -n python%{python3_pkgversion}-lldb
%{?python_provide:%python_provide python%{python3_pkgversion}-lldb}
Summary:	Python module for LLDB

Requires:	%{pkg_name_lldb}%{?_isa} = %{version}-%{release}

%if 0%{?rhel} == 8
# Became python3.12-lldb in LLVM 19
Obsoletes: python3-lldb < 18.9
%endif

%description -n python%{python3_pkgversion}-lldb
The package contains the LLDB Python module.
%endif
#endregion LLDB packages

#region MLIR packages
%if %{with mlir}
%package -n %{pkg_name_mlir}
Summary:	Multi-Level Intermediate Representation Overview
License:	Apache-2.0 WITH LLVM-exception
URL:		http://mlir.llvm.org

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
%{?python_provide:%python_provide python%{python3_pkgversion}-mlir}
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

#region libcxx preparation
%if %{with libcxx}
%py3_shebang_fix libcxx/utils/
%endif
#endregion libcxx preparation

#endregion prep

#region build
%build
# TODO(kkleine): In clang we had this %ifarch s390 s390x aarch64 %ix86 ppc64le
# Decrease debuginfo verbosity to reduce memory consumption during final library linking.
%global reduce_debuginfo 0
%ifarch %ix86
%global reduce_debuginfo 1
%endif
%if 0%{?rhel} == 8
%global reduce_debuginfo 1
%endif

%if %reduce_debuginfo == 1
# Decrease debuginfo verbosity to reduce memory consumption during final library linking
%global optflags %(echo %{optflags} | sed 's/-g /-g1 /')
%endif

%global projects clang;clang-tools-extra;lld
%global runtimes compiler-rt;openmp;offload

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

%if %{with libcxx}
%global runtimes %{runtimes};libcxx;libcxxabi;libunwind
%endif

%global cfg_file_content --gcc-triple=%{_target_cpu}-redhat-linux

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

#region LLVM lit
%if %{with python_lit}
pushd utils/lit
%py3_build
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
    -DLLVM_ENABLE_EH=ON \\\
    -DLLVM_ENABLE_RTTI=ON \\\
    -DLLVM_USE_PERF=ON \\\
    -DLLVM_TARGETS_TO_BUILD=%{targets_to_build} \\\
    -DBUILD_SHARED_LIBS=OFF \\\
    -DLLVM_BUILD_LLVM_DYLIB=ON

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
	-DCLANG_LINK_CLANG_DYLIB=ON \\\
	-DCLANG_PLUGIN_SUPPORT:BOOL=ON \\\
	-DCLANG_REPOSITORY_STRING="%{?dist_vendor} %{version}-%{release}" \\\
	-DLLVM_EXTERNAL_CLANG_TOOLS_EXTRA_SOURCE_DIR=../clang-tools-extra \\\
	-DCLANG_RESOURCE_DIR=../../../lib/clang/%{maj_ver}
#endregion clang options

#region compiler-rt options
%global cmake_config_args %{cmake_config_args} \\\
	-DCOMPILER_RT_INCLUDE_TESTS:BOOL=OFF \\\
	-DCOMPILER_RT_INSTALL_PATH=%{_prefix}/lib/clang/%{maj_ver}
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
	-DSPHINX_EXECUTABLE=%{_bindir}/sphinx-build-3 \\\
	-DSPHINX_OUTPUT_HTML:BOOL=OFF \\\
	-DSPHINX_OUTPUT_MAN:BOOL=ON \\\
	-DSPHINX_WARNINGS_AS_ERRORS=OFF
#endregion docs options

#region lldb options
%if %{with lldb}
	%global cmake_config_args %{cmake_config_args} -DLLDB_DISABLE_CURSES:BOOL=OFF
	%global cmake_config_args %{cmake_config_args} -DLLDB_DISABLE_LIBEDIT:BOOL=OFF
	%global cmake_config_args %{cmake_config_args} -DLLDB_DISABLE_PYTHON:BOOL=OFF
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
	-DLLVM_BUILD_EXTERNAL_COMPILER_RT:BOOL=ON \\\
	-DLLVM_BUILD_RUNTIME:BOOL=ON \\\
	-DLLVM_BUILD_TOOLS:BOOL=ON \\\
	-DLLVM_BUILD_UTILS:BOOL=ON \\\
	-DLLVM_DEFAULT_TARGET_TRIPLE=%{llvm_triple} \\\
	-DLLVM_DYLIB_COMPONENTS="all" \\\
	-DLLVM_ENABLE_FFI:BOOL=ON \\\
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
	-DLLVM_LINK_LLVM_DYLIB:BOOL=ON \\\
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
#endregion openmp options

#region polly options
%if %{with polly}
%global cmake_config_args %{cmake_config_args} \\\
  -DLLVM_POLLY_LINK_INTO_TOOLS=OFF
%endif
#endregion polly options


#region test options
%global cmake_config_args %{cmake_config_args} \\\
	-DLLVM_BUILD_TESTS:BOOL=ON \\\
	-DLLVM_INCLUDE_TESTS:BOOL=ON \\\
	-DLLVM_INSTALL_GTEST:BOOL=ON \\\
	-DLLVM_LIT_ARGS="-vv"

%if %{with lto_build}
%if 0%{?fedora} >= 41
	%global cmake_config_args %{cmake_config_args} -DLLVM_UNITTEST_LINK_FLAGS="-fno-lto"
%else
	%global cmake_config_args %{cmake_config_args} -DLLVM_UNITTEST_LINK_FLAGS="-Wl,-plugin-opt=O0"
%endif
%endif
#endregion test options

#region misc options
%global cmake_config_args %{cmake_config_args} \\\
	-DCMAKE_BUILD_TYPE=RelWithDebInfo \\\
	-DCMAKE_INSTALL_PREFIX=%{install_prefix} \\\
	-DENABLE_LINKER_BUILD_ID:BOOL=ON \\\
	-DOFFLOAD_INSTALL_LIBDIR=%{unprefixed_libdir} \\\
	-DPython3_EXECUTABLE=%{__python3}

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

%if %reduce_debuginfo == 1
	%global cmake_config_args %{cmake_config_args} -DCMAKE_C_FLAGS_RELWITHDEBINFO="%{optflags} -DNDEBUG"
	%global cmake_config_args %{cmake_config_args} -DCMAKE_CXX_FLAGS_RELWITHDEBINFO="%{optflags} -DNDEBUG"
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
	%global cmake_config_args %{cmake_config_args} -DLLVM_RAM_PER_COMPILE_JOB=2048
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

%cmake -G Ninja %cmake_config_args $extra_cmake_args

# Build libLLVM.so first.  This ensures that when libLLVM.so is linking, there
# are no other compile jobs running.  This will help reduce OOM errors on the
# builders without having to artificially limit the number of concurrent jobs.
%cmake_build --target LLVM

# Also build libclang-cpp.so separately to avoid OOM errors.
# This is to fix occasional OOM errors on the ppc64le COPR builders.
%cmake_build --target libclang-cpp.so

%cmake_build

# If we don't build the runtimes target here, we'll have to wait for the %%check
# section until these files are available but they need to be installed.
#
#   /usr/lib64/libomptarget.devicertl.a
#   /usr/lib64/libomptarget-amdgpu-*.bc
#   /usr/lib64/libomptarget-nvptx-*.bc

%cmake_build --target runtimes

#region compat lib
cd ..

%if %{with bundle_compat_lib}
%cmake -S ../llvm-project-%{compat_ver}.src/llvm -B ../llvm-compat-libs -G Ninja \
    -DCMAKE_INSTALL_PREFIX=%{buildroot}%{_libdir}/llvm%{compat_maj_ver}/ \
    -DCMAKE_SKIP_RPATH=ON \
    -DCMAKE_BUILD_TYPE=Release \
    -DLLVM_ENABLE_PROJECTS="clang;lldb" \
    -DLLVM_INCLUDE_BENCHMARKS=OFF \
    -DLLVM_INCLUDE_TESTS=OFF \
    %{cmake_common_args}

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
%py3_install

# Strip out #!/usr/bin/env python
sed -i -e '1{\@^#!/usr/bin/env python@d}' %{buildroot}%{python3_sitelib}/lit/*.py
popd
%endif

%cmake_install

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
mv %{buildroot}%{install_libdir}/{libear,libscanbuild} %{buildroot}%{python3_sitelib}
# Cannot use {libear,libscanbuild} style expansion in py_byte_compile.
%py_byte_compile %{__python3} %{buildroot}%{python3_sitelib}/libear
%py_byte_compile %{__python3} %{buildroot}%{python3_sitelib}/libscanbuild

# Move emacs integration files to the correct directory
mkdir -p %{buildroot}%{_emacs_sitestartdir}
for f in clang-format.el clang-include-fixer.el; do
mv %{buildroot}{%{install_datadir}/clang,%{_emacs_sitestartdir}}/$f
done
%if %{maj_ver} < 20
mv %{buildroot}{%{install_datadir}/clang,%{_emacs_sitestartdir}}/clang-rename.el
%endif

%else

# Not sure where to put these python modules for the compat build.
rm -Rf %{buildroot}%{install_libdir}/{libear,libscanbuild}

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

# Create sub-directories in the clang resource directory that will be
# populated by other packages
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
mv %{buildroot}%{_prefix}/lib/clang/%{maj_ver}/lib/powerpc64le-redhat-linux-gnu %{buildroot}%{_prefix}/lib/clang/%{maj_ver}/lib/%{llvm_triple}
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

%ifnarch %{ix86}
# Remove files that we don't package, yet.
%if %{maj_ver} >= 20
rm %{buildroot}%{install_bindir}/llvm-offload-device-info
%else
rm %{buildroot}%{install_bindir}/llvm-omp-device-info
%endif
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

# Move python package out of llvm prefix.
mkdir -p %{buildroot}%{python3_sitearch}
mv %{buildroot}%{install_prefix}/%{_lib}/python%{python3_version}/site-packages/lldb %{buildroot}/%{python3_sitearch}
rmdir %{buildroot}%{install_prefix}/%{_lib}/python%{python3_version}/site-packages
rmdir %{buildroot}%{install_prefix}/%{_lib}/python%{python3_version}

# python: fix binary libraries location
liblldb=$(basename $(readlink -e %{buildroot}%{install_libdir}/liblldb.so))
ln -vsf "../../../llvm%{maj_ver}/lib/${liblldb}" %{buildroot}%{python3_sitearch}/lldb/_lldb.so
%py_byte_compile %{__python3} %{buildroot}%{python3_sitearch}/lldb
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

# Create symlinks from the system install prefix to the llvm install prefix.
# Do this at the end so it includes any files added by preceding steps.
mkdir -p %{buildroot}%{_bindir}
for f in %{buildroot}%{install_bindir}/*; do
  filename=`basename $f`
  if [[ "$filename" == "clang-%{maj_ver}" ]]; then
    continue
  fi
  # Add symlink for binaries with version suffix.
  ln -s ../../%{install_bindir}/$filename %{buildroot}/%{_bindir}/$filename-%{maj_ver}
  # For non-compat builds, also add a symlink without version suffix.
  %if %{without compat_build}
    ln -s ../../%{install_bindir}/$filename %{buildroot}/%{_bindir}/$filename
  %endif
done

# Move man pages to system install prefix.
mkdir -p %{buildroot}%{_mandir}/man1
for f in %{buildroot}%{install_mandir}/man1/*; do
  filename=`basename $f`
  filename=${filename%.1}
  mv $f %{buildroot}%{_mandir}/man1/$filename-%{maj_ver}.1
  %if %{without compat_build}
    ln -s $filename-%{maj_ver}.1 %{buildroot}%{_mandir}/man1/$filename.1
  %endif
done
rmdir %{buildroot}%{install_mandir}/man1
rmdir %{buildroot}%{install_mandir}

%if %{without compat_build}
# Add symlinks for libraries.
mkdir -p %{buildroot}%{_libdir}
for f in %{buildroot}%{install_libdir}/*; do
  filename=`basename $f`
  if [ "$filename" != "cmake" ]; then
    ln -s ../../%{install_libdir}/$filename %{buildroot}/%{_libdir}/$filename
  fi
done
# Special handling for cmake, as we don't own the cmake directory itself.
mkdir -p %{buildroot}%{_libdir}/cmake
for f in %{buildroot}%{install_libdir}/cmake/*; do
  filename=`basename $f`
  ln -s ../../../%{install_libdir}/cmake/$filename %{buildroot}/%{_libdir}/cmake/$filename
done
mkdir -p %{buildroot}%{_libexecdir}
for f in %{buildroot}%{install_libexecdir}/*; do
  filename=`basename $f`
  ln -s ../../%{install_libexecdir}/$filename %{buildroot}/%{_libexecdir}/$filename
done
# Add symlinks for include directories.
mkdir -p %{buildroot}%{_includedir}
for f in %{buildroot}%{install_includedir}/*; do
  filename=`basename $f`
  ln -s ../../%{install_includedir}/$filename %{buildroot}/%{_includedir}/$filename
done
# Add symlinks for data directories.
mkdir -p %{buildroot}%{_datadir}
for f in %{buildroot}%{install_datadir}/*; do
  filename=`basename $f`
  ln -s ../../%{install_datadir}/$filename %{buildroot}/%{_datadir}/$filename
done
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

# The following test is flaky and we'll filter it out
test_list_filter_out+=("libomp :: ompt/teams/distribute_dispatch.c")
test_list_filter_out+=("libomp :: affinity/kmp-abs-hw-subset.c")
test_list_filter_out+=("libomp :: parallel/bug63197.c")
test_list_filter_out+=("libomp :: tasking/issue-69733.c")
test_list_filter_out+=("libarcher :: races/task-taskgroup-unrelated.c")

# These tests fail more often than not, but not always.
test_list_filter_out+=("libomp :: worksharing/for/omp_collapse_many_GELTGT_int.c")
test_list_filter_out+=("libomp :: worksharing/for/omp_collapse_many_GTGEGT_int.c")
test_list_filter_out+=("libomp :: worksharing/for/omp_collapse_many_LTLEGE_int.c")
test_list_filter_out+=("libomp :: worksharing/for/omp_collapse_one_int.c")

%ifarch s390x
test_list_filter_out+=("libomp :: flush/omp_flush.c")
test_list_filter_out+=("libomp :: worksharing/for/omp_for_schedule_guided.c")
%endif

%ifarch aarch64 s390x
# The following test has been failing intermittently on aarch64 and s390x.
# Re-enable it after https://github.com/llvm/llvm-project/issues/117773
# gets fixed.
test_list_filter_out+=("libarcher :: races/taskwait-depend.c")
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
export LIT_XFAIL="$LIT_XFAIL;races/task-taskwait-nested.c"
export LIT_XFAIL="$LIT_XFAIL;races/task-two.c"
export LIT_XFAIL="$LIT_XFAIL;races/taskwait-depend.c"
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

%if 0%{?rhel}
# libomp tests are often very slow on s390x brew builders
%ifnarch s390x
%cmake_build --target check-openmp
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

%if %{maj_ver} < 20
# The ml_dtypes python module required by mlir/test/python/execution_engine.py
# isn't packaged. But in LLVM 20 the execution_engine.py is modified to only
# run certain tests if ml_dtypes is present.
test_list_filter_out+=("MLIR :: python/execution_engine.py")
test_list_filter_out+=("MLIR :: python/multithreaded_tests.py")
%endif

%ifarch s390x
# s390x does not support half-float
test_list_filter_out+=("MLIR :: python/ir/array_attributes.py")
test_list_filter_out+=("MLIR :: python/execution_engine.py")
%endif

adjust_lit_filter_out test_list_filter_out

export PYTHONPATH=%{buildroot}/%{python3_sitearch}
%cmake_build --target check-mlir
%endif
#endregion Test MLIR

#region BOLT tests
%if %{with build_bolt}
reset_test_opts
%if %{maj_ver} < 20
export LIT_XFAIL="$LIT_XFAIL;AArch64/build_id.c"
export LIT_XFAIL="$LIT_XFAIL;AArch64/plt-call.test"
export LIT_XFAIL="$LIT_XFAIL;X86/linux-static-keys.s"
export LIT_XFAIL="$LIT_XFAIL;X86/plt-call.test"
%endif

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

%if %{maj_ver} < 20
%ifarch x86_64
# BOLT-ERROR: instrumentation of static binary currently does not support profile output on binary
# finalization, so it requires -instrumentation-sleep-time=N (N>0) usage
export LIT_XFAIL="$LIT_XFAIL;X86/internal-call-instrument.s"
%endif
%endif

%cmake_build --target check-bolt
%endif
#endregion BOLT tests

#region polly tests
%if %{with polly}
reset_test_opts
%cmake_build --target check-polly
%endif
#endregion polly tests


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
%{_sbindir}/update-alternatives --install %{_bindir}/llvm-config-%{maj_ver} llvm-config-%{maj_ver} %{install_bindir}/llvm-config %{__isa_bits}
%if %{without compat_build}
%{_sbindir}/update-alternatives --install %{_bindir}/llvm-config llvm-config %{install_bindir}/llvm-config %{__isa_bits}

# During the upgrade from LLVM 16 (F38) to LLVM 17 (F39), we found out the
# main llvm-devel package was leaving entries in the alternatives system.
# Try to remove them now.
for v in 14 15 16; do
  if [[ -e %{_bindir}/llvm-config-$v
        && "x$(%{_bindir}/llvm-config-$v --version | awk -F . '{ print $1 }')" != "x$v" ]]; then
    %{_sbindir}/update-alternatives --remove llvm-config-$v %{install_bindir}/llvm-config%{exec_suffix}-%{__isa_bits}
  fi
done
%endif

%postun -n %{pkg_name_llvm}-devel
if [ $1 -eq 0 ]; then
  %{_sbindir}/update-alternatives --remove llvm-config%{exec_suffix} %{install_bindir}/llvm-config
fi
%if %{without compat_build}
# When upgrading between minor versions (i.e. from x.y.1 to x.y.2), we must
# not remove the alternative.
# However, during a major version upgrade (i.e. from 16.x.y to 17.z.w), the
# alternative must be removed in order to give priority to a newly installed
# compat package.
if [[ $1 -eq 0
      || "x$(%{_bindir}/llvm-config%{exec_suffix} --version | awk -F . '{ print $1 }')" != "x%{maj_ver}" ]]; then
  %{_sbindir}/update-alternatives --remove llvm-config-%{maj_ver} %{install_bindir}/llvm-config%{exec_suffix}-%{__isa_bits}
fi
%endif

%if %{without compat_build}
%post -n %{pkg_name_lld}
%{_sbindir}/update-alternatives --install %{_bindir}/ld ld %{_bindir}/ld.lld 1

%postun -n %{pkg_name_lld}
if [ $1 -eq 0 ] ; then
  %{_sbindir}/update-alternatives --remove ld %{_bindir}/ld.lld
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


# The pretrans_rpmmove_dirs macro exists for packages to replace directories
# with symbolic links which normally is not possible with RPM. The trick is to
# use the generated scriptlet below to rename existing directories before
# replacing them with a symbolic link.
#
# Make sure you call this macro at the end of a %%files section for a package.
# This macro will then automatically add the %%ghost entries for the moved
# paths for you.
#
# When building in compat mode, the pretrans_rpmmove_dirs macro does nothing.
#
# See this page for a detailed problem description:
# https://docs.fedoraproject.org/en-US/packaging-guidelines/Directory_Replacement/
%if %{with compat_build}
%define pretrans_rpmmove_dirs(n:) %{nil}
%else
%define pretrans_rpmmove_dirs(n:) %{lua:
local packagename = string.gsub(rpm.expand("%{-n*}"), "%s*", "")
local paths_str = '"'..string.gsub(rpm.expand("%*"), "%s+", '",\\n"')
paths_str = string.sub(paths_str,0,-4)

for i = 1, rpm.expand("%#") do
    print('%ghost '..string.gsub(rpm.expand([[%]]..i), "%s+", "")..'.rpmmoved\\n') \
end

print("\\n%pretrans -n " .. packagename .. " -p <lua> \\n")
print("local paths={\\n")
print(paths_str..'\\n')
print("}\\n")
print([[
for _, path in ipairs(paths) do
  st = posix.stat(path)
  if st and st.type == "directory" then
    status = os.rename(path, path .. ".rpmmoved")
    if not status then
      suffix = 0
      while not status do
        suffix = suffix + 1
        status = os.rename(path .. ".rpmmoved", path .. ".rpmmoved." .. suffix)
      end
      os.rename(path, path .. ".rpmmoved")
    end
  end
end
]])
-- Remove the following "end" and you'll get this error:
-- error: invalid syntax in lua scriptlet: [string "%pretrans"]:20: unexpected symbol near '#'
print("\\n%end")
}
%endif

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
    llvm-cov
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
%if %{maj_ver} >= 20
%{expand_bins %{expand:
    llvm-cgdata
    llvm-ctxprof-util
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
%if %{maj_ver} >= 20
%expand_mans llvm-cgdata
%endif

%expand_datas opt-viewer

%{pretrans_rpmmove_dirs -n %{pkg_name_llvm}
  %{_datadir}/opt-viewer
}

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

%{pretrans_rpmmove_dirs -n %{pkg_name_llvm}-devel
  %{_includedir}/llvm-c
  %{_includedir}/llvm
  %{_libdir}/cmake/llvm
}

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

%{pretrans_rpmmove_dirs -n %{pkg_name_llvm}-googletest
  %{_includedir}/llvm-gmock
  %{_includedir}/llvm-gtest
}

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
}}
%{install_bindir}/clang-%{maj_ver}

%{_sysconfdir}/%{pkg_name_clang}/%{_target_platform}-clang.cfg
%{_sysconfdir}/%{pkg_name_clang}/%{_target_platform}-clang++.cfg
%ifarch x86_64
%{_sysconfdir}/%{pkg_name_clang}/i386-redhat-linux-gnu-clang.cfg
%{_sysconfdir}/%{pkg_name_clang}/i386-redhat-linux-gnu-clang++.cfg
%endif
%{expand_mans clang clang++}

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
%{_datadir}/clang
%endif

%{pretrans_rpmmove_dirs -n %{pkg_name_clang}-devel
  %{_includedir}/clang-c
  %{_includedir}/clang
  %{_libdir}/cmake/clang
  %{_datadir}/clang
}

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
    scan-build-py
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
%{python3_sitelib}/libear
%{python3_sitelib}/libscanbuild
%endif

%{pretrans_rpmmove_dirs -n %{pkg_name_clang}-analyzer
  %{_datadir}/scan-build
  %{_datadir}/scan-view
}

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
    clang-scan-deps
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
}}
%if %{maj_ver} >= 20
%expand_bins clang-sycl-linker
%endif
%if %{maj_ver} < 20
%expand_bins clang-pseudo clang-rename
%endif
%if %{without compat_build}
%{_emacs_sitestartdir}/clang-format.el
%if %{maj_ver} < 20
%{_emacs_sitestartdir}/clang-rename.el
%endif
%{_emacs_sitestartdir}/clang-include-fixer.el
%endif
%expand_mans diagtool extraclangtools
# Do not use expand_datas here, as we'll create a symlink for the clang dir.
%{install_datadir}/clang/clang-format.py*
%{install_datadir}/clang/clang-format-diff.py*
%{install_datadir}/clang/clang-include-fixer.py*
%{install_datadir}/clang/clang-tidy-diff.py*
%{install_datadir}/clang/run-find-all-symbols.py*
%if %{maj_ver} < 20
%{install_datadir}/clang/clang-rename.py*
%endif


%files -n %{pkg_name_clang}-tools-extra-devel
%license clang-tools-extra/LICENSE.TXT
%expand_includes clang-tidy

%{pretrans_rpmmove_dirs -n %{pkg_name_clang}-tools-extra-devel
  %{_includedir}/clang-tidy
}

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

%ifnarch s390x
%{_prefix}/lib/clang/%{maj_ver}/lib/%{compiler_rt_triple}/clang_rt.crtbegin.o
%{_prefix}/lib/clang/%{maj_ver}/lib/%{compiler_rt_triple}/clang_rt.crtend.o
%endif

%ifnarch %{ix86} s390x
%{_prefix}/lib/clang/%{maj_ver}/lib/%{compiler_rt_triple}/liborc_rt.a
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
%ifnarch %{ix86}
# libomptarget is not supported on 32-bit systems.
# s390x does not support the offloading plugins.
%expand_libs libomptarget.so.%{so_suffix}
%if %{maj_ver} >= 20
%expand_libs libLLVMOffload.so.%{so_suffix}
%endif
%endif

%files -n %{pkg_name_libomp}-devel
%license openmp/LICENSE.TXT
%{_prefix}/lib/clang/%{maj_ver}/include/omp.h
%{_prefix}/lib/clang/%{maj_ver}/include/ompx.h
%{_prefix}/lib/clang/%{maj_ver}/include/omp-tools.h
%{_prefix}/lib/clang/%{maj_ver}/include/ompt.h
%{_prefix}/lib/clang/%{maj_ver}/include/ompt-multiplex.h
%expand_libs cmake/openmp
%ifnarch %{ix86}
# libomptarget is not supported on 32-bit systems.
# s390x does not support the offloading plugins.
%expand_libs libomptarget.devicertl.a
%if %{maj_ver} >= 20
%expand_libs libomptarget-amdgpu*.bc
%expand_libs libomptarget-nvptx*.bc
%else
%expand_libs libomptarget-amdgpu-*.bc
%expand_libs libomptarget-nvptx-*.bc
%endif
%expand_libs libomptarget.so
%if %{maj_ver} >= 20
%expand_libs libLLVMOffload.so
%expand_includes offload
%endif
%endif

%{pretrans_rpmmove_dirs -n %{pkg_name_libomp}-devel
  %{_includedir}/offload
  %{_libdir}/cmake/openmp
}

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

%{pretrans_rpmmove_dirs -n %{pkg_name_lld}-devel
  %{_includedir}/lld
  %{_libdir}/cmake/lld
}

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

%{pretrans_rpmmove_dirs -n %{pkg_name_lldb}-devel
  %{_includedir}/lldb
}

%files -n python%{python3_pkgversion}-lldb
%{python3_sitearch}/lldb
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
    mlir-tblgen
    mlir-translate
    tblgen-lsp-server
    tblgen-to-irdl
}}
%if %{maj_ver} >= 20
%expand_bins mlir-rewrite mlir-runner
%else
%expand_bins mlir-cpu-runner
%endif
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

%{pretrans_rpmmove_dirs -n %{pkg_name_mlir}-devel
  %{_includedir}/mlir-c
  %{_includedir}/mlir
  %{_libdir}/cmake/mlir
}

%files -n python%{python3_pkgversion}-%{pkg_name_mlir}
%{python3_sitearch}/mlir/
%endif
#endregion MLIR files

#region libcxx files
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
    llvm-bolt-heatmap
    merge-fdata
    perf2bolt
}}
%if %{maj_ver} >= 20
%expand_bins llvm-bolt-binary-analysis
%endif

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

%{pretrans_rpmmove_dirs -n %{pkg_name_polly}-devel
  %{_includedir}/polly
  %{_libdir}/cmake/polly
}

%endif
#endregion polly files

#endregion files

#region changelog
%changelog
* Fri Jan 31 2025 Konrad Kleine <kkleine@redhat.com> - 19.1.7-5
- Address installability issue with directories that were turned into symlinks

* Thu Jan 30 2025 Josh Stone <jistone@redhat.com> - 19.1.7-4
- Fix an isel error triggered by Rust 1.85 on s390x

* Wed Jan 22 2025 Konrad Kleine <kkleine@redhat.com> - 19.1.7-3
- Add polly

* Mon Jan 20 2025 Konrad Kleine <kkleine@redhat.com> - 19.1.7-2
- Add bolt

* Mon Jan 20 2025 Timm Bäder <tbaeder@redhat.com> - 19.1.7-1
- Update to 19.1.7

* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 19.1.6-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Tue Dec 24 2024 Konrad Kleine <kkleine@redhat.com> - 19.1.6-3
- Add libcxx

* Thu Dec 19 2024 Nikita Popov <npopov@redhat.com> - 19.1.6-2
- Fix mlir exports

* Wed Dec 18 2024 Timm Bäder <tbaeder@redhat.com> - 19.1.6-1
- Update to 19.1.6

* Fri Dec 06 2024 Konrad Kleine <kkleine@redhat.com> - 19.1.5-3
- Fix mlir and openmp tests
- Disable libomp tests on s390x RHEL entirely.

* Wed Dec 04 2024 Konrad Kleine <kkleine@redhat.com> - 19.1.5-2
- Add mlir

* Tue Dec 03 2024 Timm Bäder <tbaeder@redhat.com> - 19.1.5-1
- Update to 19.1.5

* Tue Nov 26 2024 Tulio Magno Quites Machado Filho <tuliom@redhat.com> - 19.1.4-2
- Enable LLVM_ENABLE_ZSTD (rhbz#2321848)

* Thu Nov 21 2024 Timm Bäder <tbaeder@redhat.com> - 19.1.4-1
- Update to 19.1.4

* Tue Nov 19 2024 Konrad Kleine <kkleine@redhat.com> - 19.1.3-4
- Remove HTML documentation
- Add lldb man pages

* Mon Nov 18 2024 Josh Stone <jistone@redhat.com> - 19.1.3-3
- Fix profiling after a binutils NOTE change (rhbz#2322754)

* Mon Nov 18 2024 Timm Bäder <tbaeder@redhat.com> - 19.1.3-2
- Install i386 config files on x86_64

* Tue Nov 05 2024 Timm Bäder <tbaeder@redhat.com> - 19.1.3-1
- Update to 19.1.3

* Tue Sep 24 2024 Maxwell G <maxwell@gtmx.me> - 19.1.0-2
- Add 'Provides: clangd' to the clang-tools-extra subpackage

* Thu Sep 19 2024 Timm Bäder <tbaeder@redhat.com> - 19.1.0-1
- Update to LLVM 19.1.0

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 18.1.8-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Thu Jul 11 2024 Jesus Checa Hidalgo <jchecahi@redhat.com> - 18.1.8-1
- Update to LLVM 18.1.8

* Fri Jun 07 2024 Tom Stellard <tstellar@redhat.com> - 18.1.7-1
- 18.1.7 Release

* Tue May 28 2024 Nikita Popov <npopov@redhat.com> - 18.1.6-2
- Fix use after free on ppc64le (rhbz#2283525)

* Sat May 18 2024 Tom Stellard <tstellar@redhat.com> - 18.1.6-1
- 18.1.6 Release

* Tue May 14 2024 Tom Stellard <tstellar@redhat.com> - 18.1.3-2
- Backport fix for rhbz#2275090

* Thu Apr 25 2024 Tom Stellard <tstellar@redhat.com> - 18.1.4-1
- 18.1.4 Release

* Fri Apr 12 2024 Tom Stellard <tstellar@redhat.com> - 18.1.3-1
- 18.1.3 Release

* Thu Mar 21 2024 Zhengyu He <hezhy472013@gmail.com> - 18.1.2-2
- Add support for riscv64

* Thu Mar 21 2024 Tom Stellard <tstellar@redhat.com> - 18.1.2-1
- 18.1.2 Release

* Mon Mar 11 2024 Tom Stellard <tstellar@redhat.com> - 18.1.1-1
- 18.1.1 Release

* Tue Feb 27 2024 Tom Stellard <tstellar@redhat.com> - 18.1.0~rc4-1
- 18.1.0-rc4 Release

* Tue Feb 20 2024 Tom Stellard <tstellar@redhat.com> - 18.1.0~rc3-1
- 18.1.0-rc3 Release

* Thu Feb 01 2024 Nikita Popov <npopov@redhat.com> - 17.0.6-6
- Fix crash with -fzero-call-used-regs (rhbz#2262260)

* Mon Jan 29 2024 Nikita Popov <npopov@redhat.com> - 17.0.6-5
- Only use cet-report=error on x86_64

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 17.0.6-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 17.0.6-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Nov 30 2023 Tulio Magno Quites Machado Filho <tuliom@redhat.com> - 17.0.6-2
- Fix rhbz #2248872

* Tue Nov 28 2023 Tulio Magno Quites Machado Filho <tuliom@redhat.com> - 17.0.6-1
- Update to LLVM 17.0.6

* Tue Nov 14 2023 Tulio Magno Quites Machado Filho <tuliom@redhat.com> - 17.0.5-1
- Update to LLVM 17.0.5

* Tue Oct 31 2023 Tulio Magno Quites Machado Filho <tuliom@redhat.com> - 17.0.4-1
- Update to LLVM 17.0.4

* Tue Oct 17 2023 Tulio Magno Quites Machado Filho <tuliom@redhat.com> - 17.0.3-1
- Update to LLVM 17.0.3

* Tue Oct 03 2023 Tulio Magno Quites Machado Filho <tuliom@redhat.com> - 17.0.2-1
- Update to LLVM 17.0.2

* Fri Sep 22 2023 Tulio Magno Quites Machado Filho <tuliom@redhat.com> - 17.0.1~rc4-1
- Update to LLVM 17.0.1

* Tue Sep 05 2023 Tulio Magno Quites Machado Filho <tuliom@redhat.com> - 17.0.0~rc4-1
- Update to LLVM 17.0.0 RC4

* Thu Aug 24 2023 Tulio Magno Quites Machado Filho <tuliom@redhat.com> - 17.0.0~rc3-1
- Update to LLVM 17.0.0 RC3

* Thu Aug 24 2023 Tulio Magno Quites Machado Filho <tuliom@redhat.com> - 17.0.0~rc2-2
- Temporarily disable a failing test on ppc64le

* Thu Aug 17 2023 Tulio Magno Quites Machado Filho <tuliom@redhat.com> - 17.0.0~rc2-1
- Update to LLVM 17.0.0 RC2

* Wed Aug 16 2023 Tulio Magno Quites Machado Filho <tuliom@redhat.com> - 17.0.0~rc1-4
- Disable LTO on i686

* Mon Aug 14 2023 Tulio Magno Quites Machado Filho <tuliom@redhat.com> - 17.0.0~rc1-3
- Re-add patch removed by mistake

* Tue Aug 01 2023 Tulio Magno Quites Machado Filho <tuliom@redhat.com> - 17.0.0~rc1-2
- Enable LLVM_UNREACHABLE_OPTIMIZE temporarily

* Mon Jul 31 2023 Tulio Magno Quites Machado Filho <tuliom@redhat.com> - 17.0.0~rc1-1
- Update to LLVM 17.0.0 RC1

* Mon Jul 31 2023 Tulio Magno Quites Machado Filho <tuliom@redhat.com> - 16.0.6-6
- Fix rhbz #2224885

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 16.0.6-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Mon Jul 10 2023 Tulio Magno Quites Machado Filho <tuliom@redhat.com> - 16.0.6-4
- Use LLVM_UNITTEST_LINK_FLAGS to reduce link times for unit tests

* Mon Jul 03 2023 Tulio Magno Quites Machado Filho <tuliom@redhat.com> - 16.0.6-3
- Improve error messages for unsupported relocs on s390x (rhbz#2216906)
- Disable LLVM_UNREACHABLE_OPTIMIZE

* Wed Jun 14 2023 Tulio Magno Quites Machado Filho <tuliom@redhat.com> - 16.0.6-1
- Update to LLVM 16.0.6

* Fri Jun 09 2023 Nikita Popov <npopov@redhat.com> - 16.0.5-2
- Split off llvm-cmake-utils package

* Mon Jun 05 2023 Tulio Magno Quites Machado Filho <tuliom@redhat.com> - 16.0.5-1
- Update to LLVM 16.0.5

* Fri May 19 2023 Yaakov Selkowitz <yselkowi@redhat.com> - 16.0.4-2
- Avoid recommonmark dependency in RHEL builds

* Thu May 18 2023 Tulio Magno Quites Machado Filho <tuliom@redhat.com> - 16.0.4-1
- Update to LLVM 16.0.4

* Tue May 09 2023 Tulio Magno Quites Machado Filho <tuliom@redhat.com> - 16.0.3-1
- Update to LLVM 16.0.3

* Tue Apr 25 2023 Tulio Magno Quites Machado Filho <tuliom@redhat.com> - 16.0.2-1
- Update to LLVM 16.0.2

* Tue Apr 11 2023 Tulio Magno Quites Machado Filho <tuliom@redhat.com> - 16.0.1-1
- Update to LLVM 16.0.1

* Thu Mar 23 2023 Tulio Magno Quites Machado Filho <tuliom@redhat.com> - 16.0.0-2
- Distribute libllvm_gtest.a and libllvm_gtest_main.a with llvm-googletest
- Stop distributing /usr/share/llvm/src/utils

* Mon Mar 20 2023 Tulio Magno Quites Machado Filho <tuliom@redhat.com> - 16.0.0-1
- Update to LLVM 16.0.0

* Thu Mar 16 2023 Tulio Magno Quites Machado Filho <tuliom@redhat.com> - 16.0.0~rc4-2
- Fix the ppc64le triple

* Tue Mar 14 2023 Tulio Magno Quites Machado Filho <tuliom@redhat.com> - 16.0.0~rc4-1
- Update to LLVM 16.0.0 RC4

* Fri Mar 10 2023 Tulio Magno Quites Machado Filho <tuliom@redhat.com> - 16.0.0~rc3-2
- Fix llvm-exegesis failures on s390x

* Wed Feb 22 2023 Tulio Magno Quites Machado Filho <tuliom@redhat.com> - 16.0.0~rc3-1
- Update to LLVM 16.0.0 RC3

* Wed Feb 01 2023 Tulio Magno Quites Machado Filho <tuliom@redhat.com> - 16.0.0~rc1-1
- Update to LLVM 16.0.0 RC1

* Thu Jan 19 2023 Tulio Magno Quites Machado Filho <tuliom@redhat.com> - 15.0.7-3
- Update license to SPDX identifiers.
- Include the Apache license adopted in 2019.

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 15.0.7-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Jan 12 2023 Nikita Popov <npopov@redhat.com> - 15.0.7-1
- Update to LLVM 15.0.7

* Mon Jan 09 2023 Tom Stellard <tstellar@redhat.com> - 15.0.6-3
- Omit frame pointers when building

* Mon Dec 19 2022 Nikita Popov <npopov@redhat.com> - 15.0.6-2
- Remove workaround for rbhz#2048440

* Mon Dec 05 2022 Nikita Popov <npopov@redhat.com> - 15.0.6-1
- Update to LLVM 15.0.6

* Fri Nov 11 2022 Nikita Popov <npopov@redhat.com> - 15.0.4-2
- Copy CFLAGS to ASMFLAGs to enable CET in asm files

* Wed Nov 02 2022 Nikita Popov <npopov@redhat.com> - 15.0.4-1
- Update to LLVM 15.0.4

* Tue Sep 27 2022 Nikita Popov <npopov@redhat.com> - 15.0.0-2
- Export GetHostTriple.cmake

* Tue Sep 06 2022 Nikita Popov <npopov@redhat.com> - 15.0.0-1
- Update to LLVM 15.0.0

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 14.0.5-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Fri Jun 17 2022 Timm Bäder <tbaeder@redhat.com> - 14.0.5-2
- Release bump for new redhat-rpm-config

* Mon Jun 13 2022 Timm Bäder <tbaeder@redhat.com> - 14.0.5-1
- 14.0.5 Release

* Wed May 18 2022 Tom Stellard <tstellar@redhat.com> - 14.0.3-1
- 14.0.3 Release

* Fri Apr 29 2022 Timm Bäder <tbaeder@redhat.com> - 14.0.0-2
- Remove llvm-cmake-devel package

* Wed Mar 23 2022 Timm Bäder <tbaeder@redhat.com> - 14.0.0-1
- Update to LLVM 14.0.0

* Wed Feb 02 2022 Nikita Popov <npopov@redhat.com> - 13.0.1-1
- Update to LLVM 13.0.1 final

* Tue Jan 25 2022 Nikita Popov <npopov@redhat.com> - 13.0.1~rc3-1
- Update to LLVM 13.0.1rc3

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 13.0.1~rc2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jan 13 2022 Nikita Popov <npopov@redhat.com> - 13.0.1~rc2-1
- Update to LLVM 13.0.1rc2

* Mon Jan 10 2022 Nikita Popov <npopov@redhat.com> - 13.0.1~rc1-1
- Upstream 13.0.1 rc1 release

* Sat Jan 08 2022 Miro Hrončok <mhroncok@redhat.com> - 13.0.0-8
- Rebuilt for https://fedoraproject.org/wiki/Changes/LIBFFI34

* Thu Nov 11 2021 Tom Stellard <tstellar@redhat.com> - 13.0.0-7
- Enable lto on s390x and arm

* Mon Oct 25 2021 Tom Stellard <tstellar@redhat.com> - 13.0.0-6
- Build with Thin LTO

* Mon Oct 18 2021 Tom Stellard <tstellar@redhat.com> - 13.0.0-5
- Build with clang

* Fri Oct 08 2021 Tom Stellard <tstellar@redhat.com> - 13.0.0-4
- Fix default triple on arm

* Wed Oct 06 2021 Tom Stellard <tstellar@redhat.com> - 13.0.0-3
- Set default triple

* Mon Oct 04 2021 Tom Stellard <tstellar@redhat.com> - 13.0.0-2
- Drop abi_revision from soname

* Thu Sep 30 2021 Tom Stellard <tstellar@redhat.com> - 13.0.0-1
- 13.0.0 Release

* Thu Sep 30 2021 Tom Stellard <tstellar@redhat.com> - 13.0.0~rc4-2
- Restore config.guess for host triple detection

* Fri Sep 24 2021 Tom Stellard <tstellar@redhat.com> - 13.0.0~rc4-1
- 13.0.0-rc4 Release

* Fri Sep 17 2021 Tom Stellard <tstellar@redhta.com> - 13.0.0~rc3-1
- 13.0.0-rc3 Release

* Mon Sep 13 2021 Tom Stellard <tstellar@redhat.com> - 13.0.0~rc1-3
- Pass LLVM_DEFAULT_TARGET_TRIPLE to cmake

* Mon Sep 13 2021 Konrad Kleine <kkleine@redhat.com> - 13.0.0~rc1-2
- Add --without=check option

* Wed Aug 04 2021 Tom Stellard <tstellar@redhat.com> - 13.0.0~rc1-1
- 13.0.0-rc1 Release

* Thu Jul 22 2021 sguelton@redhat.com - 12.0.1-3
- Maintain versionned link to llvm-config

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 12.0.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Mon Jul 12 2021 Tom Stellard <tstellar@redhat.com> - 12.0.1-1
- 12.0.1 Release

* Wed Jun 30 2021 Tom Stellard <tstellar@redhat.com> - llvm-12.0.1~rc3-1
- 12.0.1-rc3 Release

* Fri May 28 2021 Tom Stellard <tstellar@redhat.com> - 12.0.1~rc1-2
- Stop installing lit tests

* Wed May 26 2021 Tom Stellard <tstellar@redhat.com> - llvm-12.0.1~rc1-1
- 12.0.1-rc1 Release

* Mon May 17 2021 sguelton@redhat.com - 12.0.0-7
- Fix handling of llvm-config

* Mon May 03 2021 kkleine@redhat.com - 12.0.0-6
- More verbose builds thanks to python3-psutil

* Sat May 01 2021 sguelton@redhat.com - 12.0.0-5
- Fix llvm-config install

* Tue Apr 27 2021 sguelton@redhat.com - 12.0.0-4
- Provide default empty value for exec_suffix when not in compat mode

* Tue Apr 27 2021 sguelton@redhat.com - 12.0.0-3
- Fix llvm-config install

* Tue Apr 20 2021 sguelton@redhat.com - 12.0.0-2
- Backport compat package fix

* Thu Apr 15 2021 Tom Stellard <tstellar@redhat.com> - 12.0.0-1
- 12.0.0 Release

* Thu Apr 08 2021 sguelton@redhat.com - 12.0.0-0.11.rc5
- New upstream release candidate

* Tue Apr 06 2021 sguelton@redhat.com - 12.0.0-0.10.rc4
- Patch test case for compatibility with llvm-test latout

* Fri Apr 02 2021 sguelton@redhat.com - 12.0.0-0.9.rc4
- New upstream release candidate

* Wed Mar 31 2021 Jonathan Wakely <jwakely@redhat.com> - 12.0.0-0.8.rc3
- Rebuilt for removed libstdc++ symbols (#1937698)

* Thu Mar 11 2021 sguelton@redhat.com - 12.0.0-0.7.rc3
- LLVM 12.0.0 rc3

* Wed Mar 10 2021 Kalev Lember <klember@redhat.com> - 12.0.0-0.6.rc2
- Add llvm-static(major) provides to the -static subpackage

* Tue Mar 09 2021 sguelton@redhat.com - 12.0.0-0.5.rc2
- rebuilt

* Tue Mar 02 2021 sguelton@redhat.com - 12.0.0-0.4.rc2
- Change CI working dir

* Wed Feb 24 2021 sguelton@redhat.com - 12.0.0-0.3.rc2
- 12.0.0-rc2 release

* Tue Feb 16 2021 Dave Airlie <airlied@redhat.com> - 12.0.0-0.2.rc1
- Enable LLVM_USE_PERF to allow perf integration

* Tue Feb 2 2021 Serge Guelton - 12.0.0-0.1.rc1
- 12.0.0-rc1 release

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 11.1.0-0.3.rc2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Fri Jan 22 2021 Serge Guelton - 11.1.0-0.2.rc2
- 11.1.0-rc2 release

* Thu Jan 14 2021 Serge Guelton - 11.1.0-0.1.rc1
- 11.1.0-rc1 release

* Tue Jan 05 2021 Serge Guelton - 11.0.1-3.rc2
- Waive extra test case

* Sun Dec 20 2020 sguelton@redhat.com - 11.0.1-2.rc2
- 11.0.1-rc2 release

* Tue Dec 01 2020 sguelton@redhat.com - 11.0.1-1.rc1
- 11.0.1-rc1 release

* Sat Oct 31 2020 Jeff Law <law@redhat.com> - 11.0.0-2
- Fix missing #include for gcc-11

* Wed Oct 14 2020 Josh Stone <jistone@redhat.com> - 11.0.0-1
- Fix coreos-installer test crash on s390x (rhbz#1883457)

* Mon Oct 12 2020 sguelton@redhat.com - 11.0.0-0.11
- llvm 11.0.0 - final release

* Thu Oct 08 2020 sguelton@redhat.com - 11.0.0-0.10.rc6
- 11.0.0-rc6

* Fri Oct 02 2020 sguelton@redhat.com - 11.0.0-0.9.rc5
- 11.0.0-rc5 Release

* Sun Sep 27 2020 sguelton@redhat.com - 11.0.0-0.8.rc3
- Fix NVR

* Thu Sep 24 2020 sguelton@redhat.com - 11.0.0-0.2.rc3
- Obsolete patch for rhbz#1862012

* Thu Sep 24 2020 sguelton@redhat.com - 11.0.0-0.1.rc3
- 11.0.0-rc3 Release

* Wed Sep 02 2020 sguelton@redhat.com - 11.0.0-0.7.rc2
- Apply upstream patch for rhbz#1862012

* Tue Sep 01 2020 sguelton@redhat.com - 11.0.0-0.6.rc2
- Fix source location

* Fri Aug 21 2020 Tom Stellard <tstellar@redhat.com> - 11.0.0-0.5.rc2
- 11.0.0-rc2 Release

* Wed Aug 19 2020 Tom Stellard <tstellar@redhat.com> - 11.0.0-0.4.rc1
- Fix regression-tests CI tests

* Tue Aug 18 2020 Tom Stellard <tstellar@redhat.com> - 11.0.0-0.3.rc1
- Fix rust crash on ppc64le compiling firefox
- rhbz#1862012

* Tue Aug 11 2020 Tom Stellard <tstellar@redhat.com> - 11.0.0-0.2.rc1
- Install update_cc_test_checks.py script

* Thu Aug 06 2020 Tom Stellard <tstellar@redhat.com> - 11.0.0-0.1-rc1
- LLVM 11.0.0-rc1 Release
- Make llvm-devel require llvm-static and llvm-test

* Tue Aug 04 2020 Tom Stellard <tstellar@redhat.com> - 10.0.0-10
- Backport upstream patch to fix build with -flto.
- Disable LTO on s390x to work-around unit test failures.

* Sat Aug 01 2020 sguelton@redhat.com - 10.0.0-9
- Fix update-alternative uninstall script

* Sat Aug 01 2020 sguelton@redhat.com - 10.0.0-8
- Fix gpg verification and update macro usage.

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 10.0.0-7
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 10.0.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild
* Thu Jun 11 2020 sguelton@redhat.com - 10.0.0-5
- Make llvm-test.tar.gz creation reproducible.

* Tue Jun 02 2020 sguelton@redhat.com - 10.0.0-4
- Instruct cmake not to generate RPATH

* Thu Apr 30 2020 Tom Stellard <tstellar@redhat.com> - 10.0.0-3
- Install LLVMgold.so symlink in bfd-plugins directory

* Tue Apr 07 2020 sguelton@redhat.com - 10.0.0-2
- Do not package UpdateTestChecks tests in llvm-tests
- Apply upstream patch bab5908df to pass gating tests

* Wed Mar 25 2020 sguelton@redhat.com - 10.0.0-1
- 10.0.0 final

* Mon Mar 23 2020 sguelton@redhat.com - 10.0.0-0.6.rc6
- 10.0.0 rc6

* Thu Mar 19 2020 sguelton@redhat.com - 10.0.0-0.5.rc5
- 10.0.0 rc5

* Sat Mar 14 2020 sguelton@redhat.com - 10.0.0-0.4.rc4
- 10.0.0 rc4

* Thu Mar 05 2020 sguelton@redhat.com - 10.0.0-0.3.rc3
- 10.0.0 rc3

* Fri Feb 28 2020 sguelton@redhat.com - 10.0.0-0.2.rc2
- Remove *_finite support, see rhbz#1803203

* Fri Feb 14 2020 sguelton@redhat.com - 10.0.0-0.1.rc2
- 10.0.0 rc2

* Fri Jan 31 2020 sguelton@redhat.com - 10.0.0-0.1.rc1
- 10.0.0 rc1

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 9.0.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Tue Jan 21 2020 Tom Stellard <tstellar@redhat.com> - 9.0.1-4
- Rebuild after previous build failed to strip binaries

* Fri Jan 17 2020 Tom Stellard <tstellar@redhat.com> - 9.0.1-3
- Add explicit Requires from sub-packages to llvm-libs

* Fri Jan 10 2020 Tom Stellard <tstellar@redhat.com> - 9.0.1-2
- Fix crash with kernel bpf self-tests

* Thu Dec 19 2019 tstellar@redhat.com - 9.0.1-1
- 9.0.1 Release

* Mon Nov 25 2019 sguelton@redhat.com - 9.0.0-4
- Activate AVR on all architectures

* Mon Sep 30 2019 Tom Stellard <tstellar@redhat.com> - 9.0.0-3
- Build libLLVM.so first to avoid OOM errors

* Fri Sep 27 2019 Tom Stellard <tstellar@redhat.com> - 9.0.0-2
- Remove unneeded BuildRequires: libstdc++-static

* Thu Sep 19 2019 sguelton@redhat.com - 9.0.0-1
- 9.0.0 Release

* Wed Sep 18 2019 sguelton@redhat.com - 9.0.0-0.5.rc3
- Support avr target, see rhbz#1718492

* Tue Sep 10 2019 Tom Stellard <tstellar@redhat.com> - 9.0.0-0.4.rc3
- Split out test executables into their own export file

* Fri Sep 06 2019 Tom Stellard <tstellar@redhat.com> - 9.0.0-0.3.rc3
- Fix patch for splitting out static library exports

* Fri Aug 30 2019 Tom Stellard <tstellar@redhat.com> - 9.0.0-0.2.rc3
- 9.0.0-rc3 Release

* Thu Aug 01 2019 Tom Stellard <tstellar@redhat.com> - 9.0.0-0.1.rc2
- 9.0.0-rc2 Release

* Tue Jul 30 2019 Tom Stellard <tstellar@redhat.com> - 8.0.0-9
- Sync with llvm8.0 spec file

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 8.0.0-8.1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Wed Jul 17 2019 Tom Stellard <tstellar@redhat.com> - 8.0.0-8
- Add provides for the major version of sub-packages

* Fri May 17 2019 sguelton@redhat.com - 8.0.0-7
- Fix conflicts between llvm-static = 8 and llvm-dev < 8 around LLVMStaticExports.cmake

* Wed Apr 24 2019 Tom Stellard <tstellar@redhat.com> - 8.0.0-6
- Make sure we aren't passing -g on s390x

* Sat Mar 30 2019 Tom Stellard <tstellar@redhat.com> - 8.0.0-5
- Enable build rpath while keeping install rpath disabled

* Wed Mar 27 2019 Tom Stellard <tstellar@redhat.com> - 8.0.0-4
- Backport r351577 from trunk to fix ninja check failures

* Tue Mar 26 2019 Tom Stellard <tstellar@redhat.com> - 8.0.0-3
- Fix ninja check

* Fri Mar 22 2019 Tom Stellard <tstellar@redhat.com> - 8.0.0-2
- llvm-test fixes

* Wed Mar 20 2019 sguelton@redhat.com - 8.0.0-1
- 8.0.0 final

* Fri Mar 15 2019 sguelton@redhat.com - 8.0.0-0.6.rc4
- Activate all backends (rhbz#1689031)

* Tue Mar 12 2019 sguelton@redhat.com - 8.0.0-0.5.rc4
- 8.0.0 Release candidate 4

* Mon Mar 4 2019 sguelton@redhat.com - 8.0.0-0.4.rc3
- Move some binaries to -test package, cleanup specfile

* Mon Mar 4 2019 sguelton@redhat.com - 8.0.0-0.3.rc3
- 8.0.0 Release candidate 3

* Fri Feb 22 2019 sguelton@redhat.com - 8.0.0-0.2.rc2
- 8.0.0 Release candidate 2

* Sat Feb 9 2019 sguelton@redhat.com - 8.0.0-0.1.rc1
- 8.0.0 Release candidate 1

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 7.0.1-2.1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Mon Jan 21 2019 Josh Stone <jistone@redhat.com> - 7.0.1-2
- Fix discriminators in metadata, rhbz#1668033

* Mon Dec 17 2018 sguelton@redhat.com - 7.0.1-1
- 7.0.1 release

* Tue Dec 04 2018 sguelton@redhat.com - 7.0.0-5
- Ensure rpmlint passes on specfile

* Sat Nov 17 2018 Tom Stellard <tstellar@redhat.com> - 7.0.0-4
- Install testing libraries for unittests

* Sat Oct 27 2018 Tom Stellard <tstellar@redhat.com> - 7.0.0-3
- Fix running unittests as not-root user

* Thu Sep 27 2018 Tom Stellard <tstellar@redhat.com> - 7.0.0-2
- Fixes for llvm-test package:
- Add some missing Requires
- Add --threads option to run-lit-tests script
- Set PATH so lit can find tools like count, not, etc.
- Don't hardcode tools directory to /usr/lib64/llvm
- Fix typo in yaml-bench define
- Only print information about failing tests

* Fri Sep 21 2018 Tom Stellard <tstellar@redhat.com> - 7.0.0-1
- 7.0.0 Release

* Thu Sep 13 2018 Tom Stellard <tstellar@redhat.com> - 7.0.0-0.15.rc3
- Disable rpath on install LLVM and related sub-projects

* Wed Sep 12 2018 Tom Stellard <tstellar@redhat.com> - 7.0.0-0.14.rc3
- Remove rpath from executables and libraries

* Tue Sep 11 2018 Tom Stellard <tstellar@redhat.com> - 7.0.0-0.13.rc3
- Re-enable arm and aarch64 targets on x86_64

* Mon Sep 10 2018 Tom Stellard <tstellar@redhat.com> - 7.0.0-0.12.rc3
- 7.0.0-rc3 Release

* Fri Sep 07 2018 Tom Stellard <tstellar@redhat.com> - 7.0.0-0.11.rc2
- Use python3 shebang for opt-viewewr scripts

* Thu Aug 30 2018 Tom Stellard <tstellar@redhat.com> - 7.0.0-0.10.rc2
- Drop all uses of python2 from lit tests

* Thu Aug 30 2018 Tom Stellard <tstellar@redhat.com> - 7.0.0-0.9.rc2
- Build the gold plugin on all supported architectures

* Wed Aug 29 2018 Kevin Fenzi <kevin@scrye.com> - 7.0.0-0.8.rc2
- Re-enable debuginfo to avoid 25x size increase.

* Tue Aug 28 2018 Tom Stellard <tstellar@redhat.com> - 7.0.0-0.7.rc2
- 7.0.0-rc2 Release

* Tue Aug 28 2018 Tom Stellard <tstellar@redhat.com> - 7.0.0-0.6.rc1
- Guard valgrind usage with valgrind_arches macro

* Thu Aug 23 2018 Tom Stellard <tstellar@redhat.com> - 7.0.0-0.5.rc1
- Package lit tests and googletest sources.

* Mon Aug 20 2018 Tom Stellard <tstellar@redhat.com> - 7.0.0-0.4.rc1
- Re-enable AMDGPU target on ARM rhbz#1618922

* Mon Aug 13 2018 Tom Stellard <tstellar@redhat.com> - 7.0.0-0.3.rc1
- Drop references to TestPlugin.so from cmake files

* Fri Aug 10 2018 Tom Stellard <tstellar@redhat.com> - 7.0.0-0.2.rc1
- Fixes for lit tests

* Fri Aug 10 2018 Tom Stellard <tstellar@redhat.com> - 7.0.0-0.1.rc1
- 7.0.0-rc1 Release
- Reduce number of enabled targets on all arches.
- Drop s390 detection patch, LLVM does not support s390 codegen.

* Mon Aug 06 2018 Tom Stellard <tstellar@redhat.com> - 6.0.1-6
- Backport some fixes needed by mesa and rust

* Thu Jul 26 2018 Tom Stellard <tstellar@redhat.com> - 6.0.1-5
- Move libLLVM-6.0.so to llvm6.0-libs.

* Mon Jul 23 2018 Tom Stellard <tstellar@redhat.com> - 6.0.1-4
- Rebuild because debuginfo stripping failed with the previous build

* Fri Jul 13 2018 Tom Stellard <tstellar@redhat.com> - 6.0.1-3
- Sync specfile with llvm6.0 package

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 6.0.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Mon Jun 25 2018 Tom Stellard <tstellar@redhat.com> - 6.0.1-1
- 6.0.1 Release

* Thu Jun 07 2018 Tom Stellard <tstellar@redhat.com> - 6.0.1-0.4.rc2
- 6.0.1-rc2

* Wed Jun 06 2018 Tom Stellard <tstellar@redhat.com> - 6.0.1-0.3.rc1
- Re-enable all targets to avoid breaking the ABI.

* Mon Jun 04 2018 Tom Stellard <tstellar@redhat.com> - 6.0.1-0.2.rc1
- Reduce the number of enabled targets based on the architecture

* Thu May 10 2018 Tom Stellard <tstellar@redhat.com> - 6.0.1-0.1.rc1
- 6.0.1 rc1

* Tue Mar 27 2018 Tom Stellard <tstellar@redhat.com> - 6.0.0-11
- Re-enable arm tests that used to hang

* Thu Mar 22 2018 Tom Stellard <tstellar@redhat.com> - 6.0.0-10
- Fix testcase in backported patch

* Tue Mar 20 2018 Tom Stellard <tstellar@redhat.com> - 6.0.0-9
- Prevent external projects from linking against both static and shared
  libraries.  rhbz#1558657

* Mon Mar 19 2018 Tom Stellard <tstellar@redhat.com> - 6.0.0-8
- Backport r327651 from trunk rhbz#1554349

* Fri Mar 16 2018 Tom Stellard <tstellar@redhat.com> - 6.0.0-7
- Filter out cxxflags and cflags from llvm-config that aren't supported by clang
- rhbz#1556980

* Wed Mar 14 2018 Tom Stellard <tstellar@redhat.com> - 6.0.0-6
- Enable symbol versioning in libLLVM.so

* Wed Mar 14 2018 Tom Stellard <tstellar@redhat.com> - 6.0.0-5
- Stop statically linking libstdc++.  This is no longer required by Steam
  client, but the steam installer still needs a work-around which should
  be handled in the steam package.
* Wed Mar 14 2018 Tom Stellard <tstellar@redhat.com> - 6.0.0-4
- s/make check/ninja check/

* Fri Mar 09 2018 Tom Stellard <tstellar@redhat.com> - 6.0.0-3
- Backport fix for compile time regression on rust rhbz#1552915

* Thu Mar 08 2018 Tom Stellard <tstellar@redhat.com> - 6.0.0-2
- Build with Ninja: This reduces RPM build time on a 6-core x86_64 builder
  from 82 min to 52 min.

* Thu Mar 08 2018 Tom Stellard <tstellar@redhat.com> - 6.0.0-1
- 6.0.0 Release

* Thu Mar 08 2018 Tom Stellard <tstellar@redhat.com> - 6.0.0-0.5.rc2
- Reduce debuginfo size on i686 to avoid OOM errors during linking

* Fri Feb 09 2018 Tom Stellard <tstellar@redhat.com> - 6.0.0-0.4.rc2
- 6.0.1 rc2

* Fri Feb 09 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 6.0.0-0.3.rc1
- Escape macros in %%changelog

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 6.0.0-0.2.rc1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Fri Jan 19 2018 Tom Stellard <tstellar@redhat.com> - 6.0.0-0.1.rc1
- 6.0.1 rc1

* Tue Dec 19 2017 Tom Stellard <tstellar@redhat.com> - 5.0.1-1
- 5.0.1 Release

* Mon Nov 20 2017 Tom Stellard <tstellar@redhat.com> - 5.0.0-5
- Backport debuginfo fix for rust

* Fri Nov 03 2017 Tom Stellard <tstellar@redhat.com> - 5.0.0-4
- Reduce debuginfo size for ARM

* Tue Oct 10 2017 Tom Stellard <tstellar@redhat.com> - 5.0.0-2
- Reduce memory usage on ARM by disabling debuginfo and some non-ARM targets.

* Mon Sep 25 2017 Tom Stellard <tstellar@redhat.com> - 5.0.0-1
- 5.0.0 Release

* Mon Sep 18 2017 Tom Stellard <tstellar@redhat.com> - 4.0.1-6
- Add Requires: libedit-devel for llvm-devel

* Fri Sep 08 2017 Tom Stellard <tstellar@redhat.com> - 4.0.1-5
- Enable libedit backend for LineEditor API

* Fri Aug 25 2017 Tom Stellard <tstellar@redhat.com> - 4.0.1-4
- Enable extra functionality when run the LLVM JIT under valgrind.

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 4.0.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 4.0.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Wed Jun 21 2017 Tom Stellard <tstellar@redhat.com> - 4.0.1-1
- 4.0.1 Release

* Thu Jun 15 2017 Tom Stellard <tstellar@redhat.com> - 4.0.0-6
- Install llvm utils

* Thu Jun 08 2017 Tom Stellard <tstellar@redhat.com> - 4.0.0-5
- Fix docs-llvm-man target

* Mon May 01 2017 Tom Stellard <tstellar@redhat.com> - 4.0.0-4
- Make cmake files no longer depend on static libs (rhbz 1388200)

* Tue Apr 18 2017 Josh Stone <jistone@redhat.com> - 4.0.0-3
- Fix computeKnownBits for ARMISD::CMOV (rust-lang/llvm#67)

* Mon Apr 03 2017 Tom Stellard <tstellar@redhat.com> - 4.0.0-2
- Simplify spec with rpm macros.

* Thu Mar 23 2017 Tom Stellard <tstellar@redhat.com> - 4.0.0-1
- LLVM 4.0.0 Final Release

* Wed Mar 22 2017 tstellar@redhat.com - 3.9.1-6
- Fix %%postun sep for -devel package.

* Mon Mar 13 2017 Tom Stellard <tstellar@redhat.com> - 3.9.1-5
- Disable failing tests on ARM.

* Sun Mar 12 2017 Peter Robinson <pbrobinson@fedoraproject.org> 3.9.1-4
- Fix missing mask on relocation for aarch64 (rhbz 1429050)

* Wed Mar 01 2017 Dave Airlie <airlied@redhat.com> - 3.9.1-3
- revert upstream radeonsi breaking change.

* Thu Feb 23 2017 Josh Stone <jistone@redhat.com> - 3.9.1-2
- disable sphinx warnings-as-errors

* Fri Feb 10 2017 Orion Poplawski <orion@cora.nwra.com> - 3.9.1-1
- llvm 3.9.1

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.9.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Tue Nov 29 2016 Josh Stone <jistone@redhat.com> - 3.9.0-7
- Apply backports from rust-lang/llvm#55, #57

* Tue Nov 01 2016 Dave Airlie <airlied@gmail.com - 3.9.0-6
- rebuild for new arches

* Wed Oct 26 2016 Dave Airlie <airlied@redhat.com> - 3.9.0-5
- apply the patch from -4

* Wed Oct 26 2016 Dave Airlie <airlied@redhat.com> - 3.9.0-4
- add fix for lldb out-of-tree build

* Mon Oct 17 2016 Josh Stone <jistone@redhat.com> - 3.9.0-3
- Apply backports from rust-lang/llvm#47, #48, #53, #54

* Sat Oct 15 2016 Josh Stone <jistone@redhat.com> - 3.9.0-2
- Apply an InstCombine backport via rust-lang/llvm#51

* Wed Sep 07 2016 Dave Airlie <airlied@redhat.com> - 3.9.0-1
- llvm 3.9.0
- upstream moved where cmake files are packaged.
- upstream dropped CppBackend

* Wed Jul 13 2016 Adam Jackson <ajax@redhat.com> - 3.8.1-1
- llvm 3.8.1
- Add mips target
- Fix some shared library mispackaging

* Tue Jun 07 2016 Jan Vcelak <jvcelak@fedoraproject.org> - 3.8.0-2
- fix color support detection on terminal

* Thu Mar 10 2016 Dave Airlie <airlied@redhat.com> 3.8.0-1
- llvm 3.8.0 release

* Wed Mar 09 2016 Dan Horák <dan[at][danny.cz> 3.8.0-0.3
- install back memory consumption workaround for s390

* Thu Mar 03 2016 Dave Airlie <airlied@redhat.com> 3.8.0-0.2
- llvm 3.8.0 rc3 release

* Fri Feb 19 2016 Dave Airlie <airlied@redhat.com> 3.8.0-0.1
- llvm 3.8.0 rc2 release

* Tue Feb 16 2016 Dan Horák <dan[at][danny.cz> 3.7.1-7
- recognize s390 as SystemZ when configuring build

* Sat Feb 13 2016 Dave Airlie <airlied@redhat.com> 3.7.1-6
- export C++ API for mesa.

* Sat Feb 13 2016 Dave Airlie <airlied@redhat.com> 3.7.1-5
- reintroduce llvm-static, clang needs it currently.

* Fri Feb 12 2016 Dave Airlie <airlied@redhat.com> 3.7.1-4
- jump back to single llvm library, the split libs aren't working very well.

* Fri Feb 05 2016 Dave Airlie <airlied@redhat.com> 3.7.1-3
- add missing obsoletes (#1303497)

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 3.7.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Jan 07 2016 Jan Vcelak <jvcelak@fedoraproject.org> 3.7.1-1
- new upstream release
- enable gold linker

* Wed Nov 04 2015 Jan Vcelak <jvcelak@fedoraproject.org> 3.7.0-100
- fix Requires for subpackages on the main package

* Tue Oct 06 2015 Jan Vcelak <jvcelak@fedoraproject.org> 3.7.0-100
- initial version using cmake build system

#endregion changelog
