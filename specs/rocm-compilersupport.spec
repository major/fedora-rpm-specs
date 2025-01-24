# The package follows LLVM's major version, but API version is still important:
%global comgr_maj_api_ver 2
# local, fedora
%global _comgr_full_api_ver %{comgr_maj_api_ver}.8
# mock, suse
%global comgr_full_api_ver %{comgr_maj_api_ver}.8.0
# Upstream tags are based on rocm releases:
%global rocm_release 6.3
%global rocm_patch 1
%global rocm_version %{rocm_release}.%{rocm_patch}
# What LLVM is upstream using (use LLVM_VERSION_MAJOR from llvm/CMakeLists.txt):
%global llvm_maj_ver 18
%global upstreamname llvm-project

%bcond_without bundled_llvm
# Build with an older gcc
# The rocm-llvm codebase is realively old and may never have been built
# with the current gcc, instead of of making many changes to rocm-llvm
# fall back to the older gcc.
%bcond_with compat_gcc
%if %{with compat_gcc}
%global compat_gcc_major 13
%global gcc_major_str -13
%else
%global compat_gcc_major %{nil}
%global gcc_major_str %{nil}
%endif

%global toolchain clang

%if %{with bundled_llvm}
%global _smp_mflags %{nil}
%global _lto_cflags %{nil}
%global bundle_prefix %{_libdir}/rocm/llvm
%global llvm_triple %{_target_platform}
%global amd_device_libs_prefix lib64/rocm/llvm/lib/clang/%{llvm_maj_ver}

# Compression type and level for source/binary package payloads.
#  "w7T0.xzdio"	xz level 7 using %%{getncpus} threads
%define _source_payload	w7T0.xzdio
%define _binary_payload	w7T0.xzdio

%else
# Used to tell cmake where to install device libs (must be relative to prefix)
# We want to install to clang_resource_dir/amdgcn for FHS compliance
%global amd_device_libs_prefix lib/clang/%{llvm_maj_ver}
%endif

%bcond_with debug
%if %{with debug}
%global build_type DEBUG
%else
%global build_type RelWithDebInfo
%global debug_package %{nil}
%endif

Name:           rocm-compilersupport
Version:        %{llvm_maj_ver}
Release:        35.rocm%{rocm_version}%{?dist}
Summary:        Various AMD ROCm LLVM related services

Url:            https://github.com/ROCm/llvm-project
# hipcc is MIT, comgr and device-libs are NCSA:
License:        NCSA and MIT
Source0:        https://github.com/ROCm/%{upstreamname}/archive/refs/tags/rocm-%{rocm_version}.tar.gz#/%{name}-%{rocm_version}.tar.gz
Source1:        rocm-compilersupport.prep.in

Patch3:         0001-Remove-err_drv_duplicate_config-check.patch
Patch4:         0001-Replace-use-of-mktemp-with-mkstemp.patch
# https://github.com/llvm/llvm-project/issues/106521
Patch5:         0001-Fix-build-with-GCC-14-on-ARM-78704.patch
# Link comgr with static versions of llvm's libraries
Patch6:         0001-comgr-link-with-static-llvm.patch
# For gcc-15
Patch7:         0001-gcc-15-cstdint-needs-to-include.patch

BuildRequires:  cmake
BuildRequires:  perl
%if 0%{?fedora} || 0%{?suse_version}
BuildRequires:  fdupes
%endif
BuildRequires:  libffi-devel
BuildRequires:  libzstd-devel
BuildRequires:  rocm-cmake
BuildRequires:  zlib-devel

%if %{without bundled_llvm}
BuildRequires:  llvm-devel(major) = %{llvm_maj_ver}
BuildRequires:  clang-devel(major) = %{llvm_maj_ver}
BuildRequires:  lld-devel(major) = %{llvm_maj_ver}
%else
BuildRequires:  binutils-devel
BuildRequires:  gcc%{compat_gcc_major}-c++
Provides:       bundled(llvm-project) = %{llvm_maj_ver}
%endif

%if 0%{?rhel} || 0%{?suse_version}
ExclusiveArch:  x86_64
%global targets_to_build "X86;AMDGPU"
%else
#Only the following architectures are useful for ROCm packages:
ExclusiveArch:  x86_64 aarch64 ppc64le
%ifarch x86_64
%global targets_to_build "X86;AMDGPU"
%endif
%ifarch aarch64
%global targets_to_build "AArch64;AMDGPU"
%endif
%ifarch ppc64le
%global targets_to_build "PowerPC;AMDGPU"
%endif
%endif

%description
%{summary}

%package macros
Summary:        ROCm Compiler RPM macros
BuildArch:      noarch

%description macros
This package contains ROCm compiler related RPM macros.

%package -n rocm-device-libs
Summary:        AMD ROCm LLVM bit code libraries
%if %{without bundled_llvm}
Requires:       clang-devel(major) = %{llvm_maj_ver}
Requires:       clang-resource-filesystem(major) = %{llvm_maj_ver}
Requires:       lld-devel(major) = %{llvm_maj_ver}
Requires:       llvm-devel(major) = %{llvm_maj_ver}
%else
Requires:       rocm-clang-devel
Requires:       rocm-llvm-static
Requires:       rocm-lld
%endif

%description -n rocm-device-libs
This package contains a set of AMD specific device-side language runtime
libraries in the form of bit code. Specifically:
 - Open Compute library controls
 - Open Compute Math library
 - Open Compute Kernel library
 - OpenCL built-in library
 - HIP built-in library
 - Heterogeneous Compute built-in library

%package -n rocm-comgr
Summary:        AMD ROCm LLVM Code Object Manager
Provides:       comgr(major) = %{comgr_maj_api_ver}
Provides:       rocm-comgr = %{comgr_full_api_ver}-%{release}
%if %{with bundled_llvm}
%endif

%description -n rocm-comgr
The AMD Code Object Manager (Comgr) is a shared library which provides
operations for creating and inspecting code objects.

%post -n rocm-comgr  -p /sbin/ldconfig
%postun -n rocm-comgr -p /sbin/ldconfig

%package -n rocm-comgr-devel
Summary:        AMD ROCm LLVM Code Object Manager
Requires:       rocm-comgr%{?_isa} = %{version}-%{release}
%if %{without bundled_llvm}
Requires:       clang-devel(major) = %{llvm_maj_ver}
Requires:       llvm-devel(major) = %{llvm_maj_ver}
%else
Requires:       rocm-device-libs
%endif

%description -n rocm-comgr-devel
The AMD Code Object Manager (Comgr) development package.

%package -n hipcc
Summary:        HIP compiler driver
Requires:       perl-base
Requires:       rocm-device-libs = %{version}-%{release}
%if %{without bundled_llvm}
Requires:       compiler-rt(major) = %{llvm_maj_ver}
%endif
Suggests:       rocminfo

%description -n hipcc
hipcc is a compiler driver utility that will call clang or nvcc, depending on
target, and pass the appropriate include and library options for the target
compiler and HIP infrastructure.

hipcc will pass-through options to the target compiler. The tools calling hipcc
must ensure the compiler options are appropriate for the target compiler.

%if %{without bundled_llvm}

%package -n rocm-llvm-devel
Summary:        Meta package for install the LLVM devel used for ROCm
Requires:       llvm-devel(major) = %{llvm_maj_ver}

%description -n rocm-llvm-devel
LLVM devel files used when building ROCm.

%package -n rocm-llvm-static
Summary:        Meta package for install the LLVM static used for ROCm
Requires:       llvm-devel(major) = %{llvm_maj_ver}
Requires:       llvm-static(major) = %{llvm_maj_ver}

%description -n rocm-llvm-static
LLVM devel files used when building ROCm.

%endif

%package -n hipcc-libomp-devel
Summary:        OpenMP header files for hipcc
Requires:       hipcc = %{version}-%{release}
%if %{without bundled_llvm}
Requires:       libomp-devel(major) = %{llvm_maj_ver}
%else
Requires:       libomp-devel
%endif

%description -n hipcc-libomp-devel
OpenMP header files compatible with HIPCC.

%if %{with bundled_llvm}

# ROCM LLVM
%package -n rocm-llvm-filesystem
Summary: Filesystem package that owns the rocm llvm directory

%description -n rocm-llvm-filesystem
This package owns the rocm llvm directory : %{bundle_prefix}

%package -n rocm-llvm-libs
Summary: The ROCm LLVM lib
Requires:      rocm-llvm-filesystem%{?_isa} = %{version}-%{release}
Requires:      rocm-libc++%{?_isa} = %{version}-%{release}

%description -n rocm-llvm-libs
%{summary}

%package -n rocm-llvm
Summary:       The ROCm LLVM
Requires:      rocm-llvm-libs%{?_isa} = %{version}-%{release}

%description -n rocm-llvm
%{summary}

%package -n rocm-llvm-devel
Summary:       Libraries and header files for ROCm LLVM
Requires:      rocm-llvm%{?_isa} = %{version}-%{release}

%description -n rocm-llvm-devel
%{summary}

%post -n rocm-llvm-devel -p /sbin/ldconfig
%postun -n rocm-llvm-devel -p /sbin/ldconfig

%package -n rocm-llvm-static
Summary:       Static libraries for ROCm LLVM
Requires:      rocm-llvm-devel%{?_isa} = %{version}-%{release}

%description -n rocm-llvm-static
%{summary}

# ROCM CLANG
%package -n rocm-clang-libs
Summary:       The ROCm compiler libs
Requires:      rocm-llvm-libs%{?_isa} = %{version}-%{release}

%description -n rocm-clang-libs
%{summary}

%post -n rocm-clang-libs -p /sbin/ldconfig
%postun -n rocm-clang-libs -p /sbin/ldconfig

%package -n rocm-clang-runtime-devel
Summary:       The ROCm compiler runtime

%description -n rocm-clang-runtime-devel
%{summary}

%package -n rocm-clang
Summary:       The ROCm compiler
Requires:      rocm-clang-libs%{?_isa} = %{version}-%{release}
Requires:      rocm-clang-runtime-devel%{?_isa} = %{version}-%{release}
Requires:      rocm-libc++-devel%{?_isa} = %{version}-%{release}

%description -n rocm-clang
%{summary}

%package -n rocm-clang-devel
Summary:       Libraries and header files for ROCm CLANG
Requires:      rocm-clang%{?_isa} = %{version}-%{release}

%description -n rocm-clang-devel
%{summary}

# CLANG TOOLS EXTRA
%package -n rocm-clang-tools-extra
Summary:	Extra tools for clang
Requires:	rocm-clang-libs%{?_isa} = %{version}-%{release}

%description -n rocm-clang-tools-extra
A set of extra tools built using Clang's tooling API.

%package -n rocm-clang-tools-extra-devel
Summary: Development header files for clang tools
Requires: rocm-clang-tools-extra = %{version}-%{release}

%description -n rocm-clang-tools-extra-devel
Development header files for clang tools.

# ROCM LLD
%package -n rocm-lld
Summary:        The ROCm Linker

%description -n rocm-lld
%{summary}

# ROCM LIBC++
%package -n rocm-libc++
Summary:       The ROCm libc++
Requires:      rocm-llvm-filesystem%{?_isa} = %{version}-%{release}

%description -n rocm-libc++
%{summary}

%package -n rocm-libc++-devel
Summary:       The ROCm libc++ libraries and headers
Requires:      rocm-libc++%{?_isa} = %{version}-%{release}

%description -n rocm-libc++-devel
%{summary}

%package -n rocm-libc++-static
Summary:       The ROCm libc++ static libraries
Requires:      rocm-libc++-devel%{?_isa} = %{version}-%{release}

%description -n rocm-libc++-static
%{summary}

%endif

%prep
%autosetup -p1 -n %{upstreamname}-rocm-%{rocm_version}

# rm llvm-project bits we do not need
rm -rf {bolt,flang,libc,libclc,lldb,llvm-libgcc,mlir,polly}

%if %{without bundled_llvm}
# llvm_maj_ver sanity check (we should be matching the bundled llvm major ver):
if ! grep -q "set(LLVM_VERSION_MAJOR %{llvm_maj_ver})" llvm/CMakeLists.txt; then
        echo "ERROR llvm_maj_ver macro is not correctly set"
        exit 1
fi
# Make sure we only build the AMD bits by discarding the bundled llvm code:
ls | grep -xv "amd" | xargs rm -r

##Fix issue with HIP, where compilation flags are incorrect, see issue:
#https://github.com/RadeonOpenCompute/ROCm-CompilerSupport/issues/49
#Remove redundant includes:
sed -i '/Args.push_back("-isystem");/,+3d' amd/comgr/src/comgr-compiler.cpp
#Source hard codes the libdir too:
sed -i 's/lib\(\/clang\)/%{_lib}\1/' amd/comgr/src/comgr-compiler.cpp

# CMake's find_package Config mode doesn't work if we use older llvm packages:
sed -i 's/find_package(Clang REQUIRED CONFIG)/find_package(Clang REQUIRED)/' amd/comgr/CMakeLists.txt
sed -i 's/find_package(LLD REQUIRED CONFIG)/find_package(LLD REQUIRED)/' amd/comgr/CMakeLists.txt
sed -i 's@${CLANG_CMAKE_DIR}/../../../@%{_prefix}/lib/clang/%{llvm_maj_ver}/@' amd/comgr/cmake/opencl_pch.cmake

# Fixup finding /opt/llvm
sed -i -e 's@sys::path::append(LLVMPath, "llvm");@//sys::path::append(LLVMPath, "llvm");@' amd/comgr/src/comgr-env.cpp
# Fixup finding /opt/rocm/hip
sed -i -e 's@sys::path::append(HIPPath, "hip");@//sys::path::append(HIPPath, "hip");@' amd/comgr/src/comgr-env.cpp

# Tests known to fail with upstream LLVM (as opposed to the bundled llvm):
sed -i  -e "/add_isa_test(fract/d" \
        -e "/add_isa_test(frexp/d" \
        amd/device-libs/test/compile/CMakeLists.txt
sed -i -e "/add_comgr_test(compile_source_with_device_libs_to_bc_test/d" \
        -e "/add_comgr_test(name_expression_map_test/d" \
        -e "/add_comgr_test(nested_kernel_test/d" \
        amd/comgr/test/CMakeLists.txt

# Fix script shebang (Fedora doesn't allow using "env"):
sed -i -e 's@env perl@perl@' amd/hipcc/bin/hipcc
sed -i -e 's@env perl@perl@' amd/hipcc/bin/hipcc.pl
sed -i -e 's@env perl@perl@' amd/hipcc/bin/hipconfig
sed -i -e 's@env perl@perl@' amd/hipcc/bin/hipconfig.pl
# ROCm upstream uses /opt for rocm-runtime, but Fedora uses /usr
# Don't include it again since /usr/include is already included:
sed -i '/" -isystem " + hsaPath + "\/include"/d' amd/hipcc/src/hipBin_amd.h
# Same thing for hipcc.pl:
sed -i '/^# Add paths to common HIP includes:/,/^$HIPCFLAGS/d' \
        amd/hipcc/bin/hipcc.pl

# Default rocm path is _prefix
sed -i -e 's@/opt/rocm@%{_prefix}@' amd/hipcc/bin/hipvars.pm
sed -i -e 's@/opt/rocm@%{_prefix}@' amd/hipcc/src/hipBin_base.h

LLVM_BINDIR=`llvm-config-%{llvm_maj_ver} --bindir`
if [ ! -x ${LLVM_BINDIR}/clang++ ]; then
    echo "Something wrong with llvm-config"
    false
fi

echo "s@\$ROCM_PATH/lib/llvm/bin@${LLVM_BINDIR}@" > pm.sed
sed -i -f pm.sed amd/hipcc/bin/hipvars.pm

echo "s@hipClangPath /= \"lib/llvm/bin\"@hipClangPath = \"${LLVM_BINDIR}\"@" > h.sed
sed -i -f h.sed amd/hipcc/src/hipBin_amd.h

# Fix up the location AMD_DEVICE_LIBS_PREFIX
sed -i 's|@AMD_DEVICE_LIBS_PREFIX_CODE@|set(AMD_DEVICE_LIBS_PREFIX "%{_prefix}/%{amd_device_libs_prefix}")|' amd/device-libs/AMDDeviceLibsConfig.cmake.in

%else

install -pm 755 %{SOURCE1} prep.sh
sed -i -e 's@%%{_prefix}@%{_prefix}@' prep.sh
sed -i -e 's@%%{_lib}@%{_lib}@' prep.sh
sed -i -e 's@%%{amd_device_libs_prefix}@%{amd_device_libs_prefix}@' prep.sh
sed -i -e 's@%%{bundle_prefix}@%{bundle_prefix}@' prep.sh
grep -v '%%{' prep.sh

. ./prep.sh

%endif

%build
CLANG_VERSION=%llvm_maj_ver
%if %{without bundled_llvm}
LLVM_BINDIR=`llvm-config-%{llvm_maj_ver} --bindir`
LLVM_LIBDIR=`llvm-config-%{llvm_maj_ver} --libdir`
LLVM_CMAKEDIR=`llvm-config-%{llvm_maj_ver} --cmakedir`
%else
LLVM_BINDIR=%{bundle_prefix}/bin
LLVM_LIBDIR=%{bundle_prefix}/lib
LLVM_CMAKEDIR=%{bundle_prefix}/lib/cmake/llvm
%endif

echo "%%rocmllvm_version $CLANG_VERSION"   > macros.rocmcompiler
echo "%%rocmllvm_bindir $LLVM_BINDIR"     >> macros.rocmcompiler
echo "%%rocmllvm_libdir $LLVM_LIBDIR"     >> macros.rocmcompiler
echo "%%rocmllvm_cmakedir $LLVM_CMAKEDIR" >> macros.rocmcompiler

%if %{without bundled_llvm}

# SYSTEM LLVM
export PATH=%{_libdir}/llvm%{llvm_maj_ver}/bin:$PATH
export INCLUDE_PATH=%{_libdir}/llvm%{llvm_maj_ver}/include

pushd amd/device-libs
#TODO ROCM_DEVICE_LIBS_BITCODE_INSTALL_LOC_* should be removed in ROCm 7.0:
%cmake -DROCM_DEVICE_LIBS_BITCODE_INSTALL_LOC_NEW="%{amd_device_libs_prefix}/amdgcn" \
        -DROCM_DEVICE_LIBS_BITCODE_INSTALL_LOC_OLD="" \
        -DCMAKE_BUILD_TYPE=%{build_type}
%cmake_build
# Used by comgr to find device libs when building:
export ROCM_PATH=$(realpath %__cmake_builddir/%{amd_device_libs_prefix})
popd

pushd amd/comgr
%cmake -DCMAKE_PREFIX_PATH=../device-libs/%__cmake_builddir \
  -DCMAKE_MODULE_PATH=%{_libdir}/llvm%{llvm_maj_ver}/lib \
  -DCMAKE_BUILD_TYPE=%{build_type} -DBUILD_TESTING=ON
%cmake_build
popd

pushd amd/hipcc
%cmake -DHIPCC_BACKWARD_COMPATIBILITY=OFF
%cmake_build
popd

%else
# BUNDLED LLVM

# Real cores, No hyperthreading
COMPILE_JOBS=`cat /proc/cpuinfo | grep -m 1 'cpu cores' | awk '{ print $4 }'`
if [ ${COMPILE_JOBS}x = x ]; then
    COMPILE_JOBS=1
fi
# Take into account memmory usage per core, do not thrash real memory
LINK_MEM=4
MEM_KB=`cat /proc/meminfo | grep MemTotal | awk '{ print $2 }'`
MEM_MB=`eval "expr ${MEM_KB} / 1024"`
MEM_GB=`eval "expr ${MEM_MB} / 1024"`
LINK_JOBS=`eval "expr 1 + ${MEM_GB} / ${LINK_MEM}"`
JOBS=${COMPILE_JOBS}
if [ "$LINK_JOBS" -lt "$JOBS" ]; then
    JOBS=$LINK_JOBS
fi

%global llvm_projects "llvm;clang;clang-tools-extra;lld"
%global llvm_runtimes "compiler-rt;libcxx;libcxxabi"

p=$PWD

#
# BASE LLVM
#
%global llvmrocm_cmake_config \\\
 -DBUILD_SHARED_LIBS=OFF \\\
 -DBUILD_TESTING=OFF \\\
 -DCLANG_ENABLE_STATIC_ANALYZER=OFF \\\
 -DCLANG_ENABLE_ARCMT=OFF \\\
 -DCLANG_TOOL_CLANG_FUZZER_BUILD=OFF \\\
 -DCMAKE_BUILD_TYPE=%{build_type} \\\
 -DCMAKE_INSTALL_DO_STRIP=ON \\\
 -DCMAKE_INSTALL_PREFIX=%{bundle_prefix} \\\
 -DCOMPILER_RT_BUILD_BUILTINS=ON \\\
 -DCOMPILER_RT_BUILD_GWP_ASAN=OFF \\\
 -DCOMPILER_RT_BUILD_LIBFUZZER=OFF \\\
 -DCOMPILER_RT_BUILD_MEMPROF=OFF \\\
 -DCOMPILER_RT_BUILD_ORC=OFF \\\
 -DCOMPILER_RT_BUILD_PROFILE=OFF \\\
 -DCOMPILER_RT_BUILD_SANITIZERS=OFF \\\
 -DCOMPILER_RT_BUILD_XRAY=OFF \\\
 -DENABLE_LINKER_BUILD_ID=ON \\\
 -DLIBCXX_INCLUDE_BENCHMARKS=OFF \\\
 -DLIBCXXABI_USE_LLVM_UNWINDER=OFF \\\
 -DLLVM_BINUTILS_INCDIR=%{_includedir} \\\
 -DLLVM_BUILD_RUNTIME=ON \\\
 -DLLVM_DEFAULT_TARGET_TRIPLE=%{llvm_triple} \\\
 -DLLVM_ENABLE_EH=ON \\\
 -DLLVM_ENABLE_FFI=ON \\\
 -DLLVM_ENABLE_LIBCXX=ON \\\
 -DLLVM_ENABLE_OCAMLDOC=OFF \\\
 -DLLVM_ENABLE_RTTI=ON \\\
 -DLLVM_ENABLE_ZLIB=ON \\\
 -DLLVM_ENABLE_ZSTD=ON \\\
 -DLLVM_INCLUDE_BENCHMARKS=OFF \\\
 -DLLVM_INCLUDE_EXAMPLES=OFF \\\
 -DLLVM_INCLUDE_TESTS=OFF \\\
 -DLLVM_TARGETS_TO_BUILD=%{targets_to_build} \\\
 -DLLVM_TOOL_LLVM_AS_FUZZER_BUILD=OFF \\\
 -DLLVM_TOOL_LLVM_DIS_FUZZER_BUILD=OFF \\\
 -DLLVM_TOOL_LLVM_DLANG_DEMANGLE_FUZZER_BUILD=OFF \\\
 -DLLVM_TOOL_LLVM_ISEL_FUZZER_BUILD=OFF \\\
 -DLLVM_TOOL_LLVM_ITANIUM_DEMANGLE_FUZZER_BUILD=OFF \\\
 -DLLVM_TOOL_LLVM_MC_ASSEMBLE_FUZZER_BUILD=OFF \\\
 -DLLVM_TOOL_LLVM_MC_DISASSEMBLE_FUZZER_BUILD=OFF \\\
 -DLLVM_TOOL_LLVM_MICROSOFT_DEMANGLE_FUZZER_BUILD=OFF \\\
 -DLLVM_TOOL_LLVM_OPT_FUZZER_BUILD=OFF \\\
 -DLLVM_TOOL_LLVM_RUST_DEMANGLE_FUZZER_BUILD=OFF \\\
 -DLLVM_TOOL_LLVM_SPECIAL_CASE_LIST_FUZZER_BUILD=OFF \\\
 -DLLVM_TOOL_LLVM_YAML_NUMERIC_PARSER_FUZZER_BUILD=OFF \\\
 -DLLVM_TOOL_LLVM_YAML_PARSER_FUZZER_BUILD=OFF \\\
 -DLLVM_TOOL_VFABI_DEMANGLE_FUZZER_BUILD=OFF \\\
 -DMLIR_INSTALL_AGGREGATE_OBJECTS=OFF \\\
 -DLLVM_BUILD_LLVM_DYLIB=ON \\\
 -DLLVM_LINK_LLVM_DYLIB=ON \\\
 -DLLVM_BUILD_TOOLS=ON \\\
 -DLLVM_BUILD_UTILS=ON \\\
 -DMLIR_BUILD_MLIR_C_DYLIB=ON

pushd .
%if 0%{?suse_version}
%define __sourcedir llvm
%define __builddir build-llvm
%else
%define _vpath_srcdir llvm
%define _vpath_builddir build-llvm
%endif

# Mixing use of gcc and clang in the build conflicts with rpm's setting of flags.
# Set them manually as CMAKE_<LANG>_FLAGS
export CFLAGS=""
export CXXFLAGS=""
export LDFLAGS=""

# So just built tools can find their *.so's
export LD_LIBRARY_PATH=$PWD/build-llvm/lib
export CC=/usr/bin/gcc%{gcc_major_str}
export CXX=/usr/bin/g++%{gcc_major_str}

%if 0%{?suse_version}
%cmake \
%else
%__cmake -S llvm -B build-llvm \
%endif
       %{llvmrocm_cmake_config} \
       -DCMAKE_CXX_COMPILER=/usr/bin/g++%{gcc_major_str} \
       -DCMAKE_C_COMPILER=/usr/bin/gcc%{gcc_major_str} \
       -DCMAKE_INSTALL_PREFIX=%{bundle_prefix} \
       -DCMAKE_INSTALL_LIBDIR=lib \
       -DLLVM_ENABLE_PROJECTS=%{llvm_projects}

%if 0%{?suse_version}
%cmake_build -j ${JOBS}
%else
%make_build -C build-llvm -j ${JOBS}
%endif

popd

build_stage1=$p/build-llvm

%global llvmrocm_stage1_config \\\
    -DCMAKE_AR=$build_stage1/bin/llvm-ar \\\
    -DCMAKE_C_COMPILER=$build_stage1/bin/clang \\\
    -DCMAKE_CXX_COMPILER=$build_stage1/bin/clang++ \\\
    -DCMAKE_LINKER=$build_stage1/bin/ld.lld \\\
    -DCMAKE_RANLIB=$build_stage1/bin/llvm-ranlib \\\
    -DLLVM_DIR=$build_stage1/lib/cmake/llvm \\\
    -DClang_DIR=$build_stage1/lib/cmake/clang \\\
    -DLLD_DIR=$build_stage1/lib/cmake/lld

#
# Rebuild and add libc++
#
pushd .
%if 0%{?suse_version}
%define __sourcedir llvm
%define __builddir build-llvm-2
%else
%define _vpath_srcdir llvm
%define _vpath_builddir build-llvm-2
%endif

export LD_LIBRARY_PATH=$PWD/build-llvm-2/lib

%cmake \
       %{llvmrocm_cmake_config} \
       %{llvmrocm_stage1_config} \
       -DCMAKE_INSTALL_PREFIX=%{bundle_prefix} \
       -DCMAKE_INSTALL_RPATH=%{bundle_prefix}/lib \
       -DCMAKE_INSTALL_LIBDIR=lib \
       -DCLANG_DEFAULT_LINKER=%{bundle_prefix}/bin/ld.lld \
       -DLLVM_ENABLE_LLD=ON \
       -DLLVM_TOOL_COMPILER_RT_BUILD=ON \
       -DLLVM_TOOL_LIBCXXABI_BUILD=ON \
       -DLLVM_TOOL_LIBCXX_BUILD=ON \
       -DLLVM_ENABLE_PROJECTS=%{llvm_projects} \
       -DLLVM_ENABLE_RUNTIMES=%{llvm_runtimes}
       
%cmake_build -j ${JOBS}
popd

build_stage2=$p/build-llvm-2

%global llvmrocm_tools_config \\\
       -DLLVM_DIR=$build_stage2/lib/cmake/llvm \\\
       -DClang_DIR=$build_stage2/lib/cmake/clang \\\
       -DLLD_DIR=$build_stage2/lib/cmake/lld

export CC=$build_stage2/bin/clang
export CXX=$build_stage2/bin/clang++
export LD=$build_stage2/bin/ld.lld

#
# DEVICE LIBS
#
pushd .
%if 0%{?suse_version}
%define __sourcedir amd/device-libs
%define __builddir build-devicelibs
%else
%define _vpath_srcdir amd/device-libs
%define _vpath_builddir build-devicelibs
%endif

%cmake \
       %{llvmrocm_cmake_config} \
       %{llvmrocm_tools_config} \
       -DCMAKE_INSTALL_PREFIX=%{_prefix} \
       -DCMAKE_INSTALL_LIBDIR=%{_lib} \
       -DROCM_DEVICE_LIBS_BITCODE_INSTALL_LOC_NEW="%{amd_device_libs_prefix}/amdgcn" \
       -DROCM_DEVICE_LIBS_BITCODE_INSTALL_LOC_OLD=""

%cmake_build -j ${JOBS}
popd

build_devicelibs=$p/build-devicelibs
%global llvmrocm_devicelibs_config \\\
	-DAMDDeviceLibs_DIR=$build_devicelibs/%{_lib}/cmake/AMDDeviceLibs

#
# HIPCC
#
pushd .
%if 0%{?suse_version}
%define __sourcedir amd/hipcc
%define __builddir build-hipcc
%else
%define _vpath_srcdir amd/hipcc
%define _vpath_builddir build-hipcc
%endif

%cmake \
       %{llvmrocm_cmake_config} \
       %{llvmrocm_tools_config} \
       %{llvmrocm_devicelibs_config} \
       -DCMAKE_INSTALL_RPATH=%{bundle_prefix}/lib \
       -DCMAKE_INSTALL_PREFIX=%{_prefix} \
       -DCMAKE_INSTALL_LIBDIR=%{_lib}

%cmake_build -j ${JOBS}
popd

#
# COMGR
#
pushd .
%if 0%{?suse_version}
%define __sourcedir amd/comgr
%define __builddir build-comgr
%else
%define _vpath_srcdir amd/comgr
%define _vpath_builddir build-comgr
%endif

%cmake \
       %{llvmrocm_cmake_config} \
       %{llvmrocm_tools_config} \
       %{llvmrocm_devicelibs_config} \
       -DBUILD_SHARED_LIBS=ON \
       -DCMAKE_INSTALL_PREFIX=%{_prefix} \
       -DCMAKE_INSTALL_LIBDIR=%{_lib}

# cmake produces a link.txt that includes libLLVM*.so, hack it out
%if 0%{?suse_version}
sed -i -e 's@libLLVM-%{llvm_maj_ver}git.so@libLLVMCore.a@' CMakeFiles/amd_comgr.dir/link.txt
# Order of link is wrong include some missing libs
sed -i -e 's@-lm -lrt@-lLLVMCoverage -lLLVMFrontendDriver -lLLVMFrontendHLSL -lLLVMLTO -lLLVMOption -lLLVMSymbolize -lLLVMWindowsDriver -lm -lrt@' CMakeFiles/amd_comgr.dir/link.txt
%else
sed -i -e 's@libLLVM-%{llvm_maj_ver}git.so@libLLVMCore.a@' build-comgr/CMakeFiles/amd_comgr.dir/link.txt
# Order of link is wrong include some missing libs
sed -i -e 's@-lm -lrt@-lLLVMCoverage -lLLVMFrontendDriver -lLLVMFrontendHLSL -lLLVMLTO -lLLVMOption -lLLVMSymbolize -lLLVMWindowsDriver -lm -lrt@' build-comgr/CMakeFiles/amd_comgr.dir/link.txt
%endif

%cmake_build -j ${JOBS}

# Check that static linking happened
# ldd build-comgr/libamd_comgr.so

popd

%endif

%if %{without bundled_llvm}
%check
pushd amd/device-libs
# Workaround for bug in cmake tests not finding amdgcn:
ln -s %{amd_device_libs_prefix}/amdgcn %__cmake_builddir/amdgcn
%ctest
popd

pushd amd/comgr
%ctest
popd

# HIPCC sanity check
touch t.hip
# Build ROCM_PATH in a way that hipcc expects it when installed:
export ROCM_PATH=$(realpath amd/device-libs/%__cmake_builddir)
mkdir -p $ROCM_PATH/bin
ln -s %{_bindir}/clang++-%{llvm_maj_ver} $ROCM_PATH/bin
# Dummy rocm_agent_enumerator so it doesn't error:
touch $ROCM_PATH/bin/rocm_agent_enumerator
chmod a+x $ROCM_PATH/bin/rocm_agent_enumerator
amd/hipcc/%__cmake_builddir/hipcc -c t.hip

%endif

%install
install -Dpm 644 macros.rocmcompiler \
    %{buildroot}%{_rpmmacrodir}/macros.rocmcompiler

%if %{without bundled_llvm}
# SYSTEM LLVM

pushd amd/device-libs
%cmake_install
popd

pushd amd/comgr
%cmake_install
popd

pushd amd/hipcc
%cmake_install
popd

%else
# BUNDLED

#
# BASE LLVM
#
pushd .
%if 0%{?suse_version}
%define __builddir build-llvm-2
%else
%define _vpath_builddir build-llvm-2
%endif

%cmake_install

popd

#
# DEVICE LIBS
#
pushd .
%if 0%{?suse_version}
%define __builddir build-devicelibs
%else
%define _vpath_builddir build-devicelibs
%endif

%cmake_install
popd

#
# COMGR
#
pushd .
%if 0%{?suse_version}
%define __builddir build-comgr
%else
%define _vpath_builddir build-comgr
%endif

%cmake_install
popd

#
# HIPCC
#
pushd .
%if 0%{?suse_version}
%define __builddir build-hipcc
%else
%define _vpath_builddir build-hipcc
%endif

%cmake_install
popd

# Make directories users of rocm-rpm-modules will install to
%global modules_gpu_list gfx8 gfx9 gfx10 gfx11 gfx12 gfx906 gfx908 gfx90a gfx942 gfx1031 gfx1036 gfx1100 gfx1101 gfx1102 gfx1103
for gpu in %{modules_gpu_list}
do
    mkdir -p %{buildroot}%{_libdir}/rocm/$gpu/lib/cmake
    mkdir -p %{buildroot}%{_libdir}/rocm/$gpu/bin
    mkdir -p %{buildroot}%{_libdir}/rocm/$gpu/include
done

rm -rf %{buildroot}%{_prefix}/hip
if [ -f %{buildroot}%{_prefix}/share/doc/packages/rocm-compilersupport/LICENSE.TXT ]; then
    rm %{buildroot}%{_prefix}/share/doc/packages/rocm-compilersupport/LICENSE.*
fi
if [ -f %{buildroot}%{_prefix}/share/doc/packages/rocm-compilersupport/NOTICES.txt ]; then
    rm %{buildroot}%{_prefix}/share/doc/packages/rocm-compilersupport/NOTICES.txt
fi
if [ -f %{buildroot}%{_prefix}/share/doc/packages/rocm-compilersupport/README.md ]; then
    rm %{buildroot}%{_prefix}/share/doc/packages/rocm-compilersupport/README.md
fi

%if 0%{?suse_version}
find %{buildroot}%{bundle_prefix}/bin -type f -executable -exec strip {} \;
find %{buildroot}%{_bindir}           -type f -executable -exec strip {} \;
find %{buildroot}%{bundle_prefix}/lib -type f -name '*.so*' -exec strip {} \;
find %{buildroot}%{_libdir}           -type f -name '*.so*' -exec strip {} \;
%endif

# Remove lld's libs
rm -rf %{buildroot}%{bundle_prefix}/include/lld
rm -rf %{buildroot}%{bundle_prefix}/lib/cmake/lld
rm -rf %{buildroot}%{bundle_prefix}/lib/liblld*

# Remove exec perm
chmod a-x %{buildroot}%{bundle_prefix}/share/opt-viewer/optpmap.py
chmod a-x %{buildroot}%{bundle_prefix}/share/opt-viewer/style.css

%endif

# Fix perl module files installation:
# Eventually upstream plans to deprecate Perl usage, see README.md
mkdir -p %{buildroot}%{perl_vendorlib}
mv %{buildroot}%{_bindir}/hip*.pm %{buildroot}%{perl_vendorlib}

#Clean up dupes:
%if 0%{?fedora} || 0%{?suse_version}
%fdupes %{buildroot}%{_prefix}
%endif

%files macros
%{_rpmmacrodir}/macros.rocmcompiler

%files -n rocm-device-libs
%dir %{_libdir}/cmake/AMDDeviceLibs
%license amd/device-libs/LICENSE.TXT
%doc amd/device-libs/README.md amd/device-libs/doc/*.md
%{_libdir}/cmake/AMDDeviceLibs/*.cmake
%{_prefix}/%{amd_device_libs_prefix}/amdgcn
%if 0%{?rhel} || 0%{?fedora}
%exclude %{_docdir}/ROCm-Device-Libs
%endif


%files -n rocm-comgr
%license amd/comgr/LICENSE.txt
%license amd/comgr/NOTICES.txt
%doc amd/comgr/README.md
%{_libdir}/libamd_comgr.so.*
%if 0%{?rhel} || 0%{?fedora}
%exclude %{_docdir}/amd_comgr
%endif

%files -n rocm-comgr-devel
%dir %{_includedir}/amd_comgr
%dir %{_libdir}/cmake/amd_comgr
%{_includedir}/amd_comgr/amd_comgr.h
%{_libdir}/libamd_comgr.so
%{_libdir}/cmake/amd_comgr/*.cmake

%files -n hipcc
%license amd/hipcc/LICENSE.txt
%doc amd/hipcc/README.md
%{_bindir}/hipcc{,.pl,.bin}
%{_bindir}/hipconfig{,.pl,.bin}
%{perl_vendorlib}/hip*.pm
%if 0%{?rhel} || 0%{?fedora}
%exclude %{_docdir}/hipcc
%endif

%if %{without bundled_llvm}
# SYSTEM LLVM

%files -n rocm-llvm-devel
%files -n rocm-llvm-static

%endif

%files -n hipcc-libomp-devel

%if %{with bundled_llvm}

# ROCM LLVM
%files -n rocm-llvm-filesystem
%dir %{_libdir}/rocm
# For rocm-rpm-modules
%dir %{_libdir}/rocm/gfx8
%dir %{_libdir}/rocm/gfx8/bin
%dir %{_libdir}/rocm/gfx8/include
%dir %{_libdir}/rocm/gfx8/lib
%dir %{_libdir}/rocm/gfx8/lib/cmake
%dir %{_libdir}/rocm/gfx9
%dir %{_libdir}/rocm/gfx9/bin
%dir %{_libdir}/rocm/gfx9/include
%dir %{_libdir}/rocm/gfx9/lib
%dir %{_libdir}/rocm/gfx9/lib/cmake
%dir %{_libdir}/rocm/gfx10
%dir %{_libdir}/rocm/gfx10/bin
%dir %{_libdir}/rocm/gfx10/include
%dir %{_libdir}/rocm/gfx10/lib
%dir %{_libdir}/rocm/gfx10/lib/cmake
%dir %{_libdir}/rocm/gfx11
%dir %{_libdir}/rocm/gfx11/bin
%dir %{_libdir}/rocm/gfx11/include
%dir %{_libdir}/rocm/gfx11/lib
%dir %{_libdir}/rocm/gfx11/lib/cmake
%dir %{_libdir}/rocm/gfx12
%dir %{_libdir}/rocm/gfx12/bin
%dir %{_libdir}/rocm/gfx12/include
%dir %{_libdir}/rocm/gfx12/lib
%dir %{_libdir}/rocm/gfx12/lib/cmake
%dir %{_libdir}/rocm/gfx906
%dir %{_libdir}/rocm/gfx906/bin
%dir %{_libdir}/rocm/gfx906/include
%dir %{_libdir}/rocm/gfx906/lib
%dir %{_libdir}/rocm/gfx906/lib/cmake
%dir %{_libdir}/rocm/gfx908
%dir %{_libdir}/rocm/gfx908/bin
%dir %{_libdir}/rocm/gfx908/include
%dir %{_libdir}/rocm/gfx908/lib
%dir %{_libdir}/rocm/gfx908/lib/cmake
%dir %{_libdir}/rocm/gfx90a
%dir %{_libdir}/rocm/gfx90a/bin
%dir %{_libdir}/rocm/gfx90a/include
%dir %{_libdir}/rocm/gfx90a/lib
%dir %{_libdir}/rocm/gfx90a/lib/cmake
%dir %{_libdir}/rocm/gfx942
%dir %{_libdir}/rocm/gfx942/bin
%dir %{_libdir}/rocm/gfx942/include
%dir %{_libdir}/rocm/gfx942/lib
%dir %{_libdir}/rocm/gfx942/lib/cmake
%dir %{_libdir}/rocm/gfx1031
%dir %{_libdir}/rocm/gfx1031/bin
%dir %{_libdir}/rocm/gfx1031/include
%dir %{_libdir}/rocm/gfx1031/lib
%dir %{_libdir}/rocm/gfx1031/lib/cmake
%dir %{_libdir}/rocm/gfx1036
%dir %{_libdir}/rocm/gfx1036/bin
%dir %{_libdir}/rocm/gfx1036/include
%dir %{_libdir}/rocm/gfx1036/lib
%dir %{_libdir}/rocm/gfx1036/lib/cmake
%dir %{_libdir}/rocm/gfx1100
%dir %{_libdir}/rocm/gfx1100/bin
%dir %{_libdir}/rocm/gfx1100/include
%dir %{_libdir}/rocm/gfx1100/lib
%dir %{_libdir}/rocm/gfx1100/lib/cmake
%dir %{_libdir}/rocm/gfx1101
%dir %{_libdir}/rocm/gfx1101/bin
%dir %{_libdir}/rocm/gfx1101/include
%dir %{_libdir}/rocm/gfx1101/lib
%dir %{_libdir}/rocm/gfx1101/lib/cmake
%dir %{_libdir}/rocm/gfx1102
%dir %{_libdir}/rocm/gfx1102/bin
%dir %{_libdir}/rocm/gfx1102/include
%dir %{_libdir}/rocm/gfx1102/lib
%dir %{_libdir}/rocm/gfx1102/lib/cmake
%dir %{_libdir}/rocm/gfx1103
%dir %{_libdir}/rocm/gfx1103/bin
%dir %{_libdir}/rocm/gfx1103/include
%dir %{_libdir}/rocm/gfx1103/lib
%dir %{_libdir}/rocm/gfx1103/lib/cmake
# For llvm
%dir %{bundle_prefix}
%dir %{bundle_prefix}/bin
%dir %{bundle_prefix}/include
%dir %{bundle_prefix}/include/clang
%dir %{bundle_prefix}/include/clang-c
%dir %{bundle_prefix}/include/llvm
%dir %{bundle_prefix}/include/llvm-c
%dir %{bundle_prefix}/lib
%dir %{bundle_prefix}/lib/clang
%dir %{bundle_prefix}/lib/clang/%{llvm_maj_ver}
%dir %{bundle_prefix}/lib/clang/%{llvm_maj_ver}/include
%dir %{bundle_prefix}/lib/clang/%{llvm_maj_ver}/include/cuda_wrappers
%dir %{bundle_prefix}/lib/clang/%{llvm_maj_ver}/include/llvm_libc_wrappers
%dir %{bundle_prefix}/lib/clang/%{llvm_maj_ver}/include/openmp_wrappers
%dir %{bundle_prefix}/lib/clang/%{llvm_maj_ver}/include/ppc_wrappers
%dir %{bundle_prefix}/lib/clang/%{llvm_maj_ver}/lib
%dir %{bundle_prefix}/lib/clang/%{llvm_maj_ver}/lib/linux
%dir %{bundle_prefix}/lib/cmake
%dir %{bundle_prefix}/lib/cmake/clang
%dir %{bundle_prefix}/lib/cmake/llvm
%dir %{bundle_prefix}/share
%dir %{bundle_prefix}/share/clang
%dir %{bundle_prefix}/share/opt-viewer

%files -n rocm-llvm-libs
%{bundle_prefix}/lib/libLLVM-*.so
%{bundle_prefix}/lib/libLTO.so.*
%{bundle_prefix}/lib/libRemarks.so.*

%post -n rocm-llvm-libs -p /sbin/ldconfig
%postun -n rocm-llvm-libs -p /sbin/ldconfig

%files -n rocm-llvm
%license llvm/LICENSE.TXT
%{bundle_prefix}/bin/bugpoint
%{bundle_prefix}/bin/llc
%{bundle_prefix}/bin/lli
%{bundle_prefix}/bin/amdgpu-arch
%{bundle_prefix}/bin/amdgpu-offload-arch
%{bundle_prefix}/bin/dsymutil
%{bundle_prefix}/bin/llvm*
%{bundle_prefix}/bin/nvidia-arch
%{bundle_prefix}/bin/opt
%{bundle_prefix}/bin/offload-arch
%{bundle_prefix}/bin/sancov
%{bundle_prefix}/bin/sanstats
%{bundle_prefix}/bin/verify-uselistorder
%{bundle_prefix}/share/opt-viewer/*

%files -n rocm-llvm-devel
%license llvm/LICENSE.TXT
%{bundle_prefix}/include/llvm/*
%{bundle_prefix}/include/llvm-c/*
%{bundle_prefix}/lib/cmake/llvm/*
%{bundle_prefix}/lib/libLLVM.so
%{bundle_prefix}/lib/libLTO.so
%{bundle_prefix}/lib/libRemarks.so
%{bundle_prefix}/lib/LLVMgold.so

%files -n rocm-llvm-static
%license llvm/LICENSE.TXT
%{bundle_prefix}/lib/libLLVM*.a

# ROCM CLANG
%files -n rocm-clang-libs
%{bundle_prefix}/lib/libclang*.so.*

%files -n rocm-clang-runtime-devel
%{bundle_prefix}/lib/clang/%{llvm_maj_ver}/include/*
%{bundle_prefix}/lib/clang/%{llvm_maj_ver}/lib/linux/clang_rt.*
%{bundle_prefix}/lib/clang/%{llvm_maj_ver}/lib/linux/libclang_rt.*

%files -n rocm-clang
%license clang/LICENSE.TXT
%{bundle_prefix}/bin/c-index-test
%{bundle_prefix}/bin/clang*
%{bundle_prefix}/bin/diagtool
%{bundle_prefix}/bin/find-all-symbols
%{bundle_prefix}/bin/flang
%{bundle_prefix}/bin/git-clang-format
%{bundle_prefix}/bin/hmaptool
%{bundle_prefix}/bin/modularize
%{bundle_prefix}/bin/nvptx-arch
%{bundle_prefix}/bin/pp-trace
%{bundle_prefix}/share/clang/*

%files -n rocm-clang-devel
%license clang/LICENSE.TXT
%{bundle_prefix}/include/clang/*
%{bundle_prefix}/include/clang-c/*
%{bundle_prefix}/lib/cmake/clang/*
%{bundle_prefix}/lib/libclang*.so

# ROCM CLANG TOOLS EXTRA
%files -n rocm-clang-tools-extra
%license clang-tools-extra/LICENSE.TXT
%{bundle_prefix}/bin/run-clang-tidy

%files -n rocm-clang-tools-extra-devel
%license clang-tools-extra/LICENSE.TXT
%{bundle_prefix}/include/clang-tidy/

# ROCM LLD
%files -n rocm-lld
%license lld/LICENSE.TXT
%{bundle_prefix}/bin/ld.lld
%{bundle_prefix}/bin/ld64.lld
%{bundle_prefix}/bin/lld
%{bundle_prefix}/bin/lld-link
%{bundle_prefix}/bin/wasm-ld

# ROCM LIBC++
%files -n rocm-libc++
%license libcxx/LICENSE.TXT
%{bundle_prefix}/lib/libc++.so.*
%{bundle_prefix}/lib/libc++abi.so.*

%files -n rocm-libc++-devel
%{bundle_prefix}/include/c++/
%{bundle_prefix}/lib/libc++.so
%{bundle_prefix}/lib/libc++abi.so

%files -n rocm-libc++-static
%{bundle_prefix}/lib/libc++.a
%{bundle_prefix}/lib/libc++abi.a
%{bundle_prefix}/lib/libc++experimental.a

%endif

%changelog
* Tue Jan 21 2025 Tom Rix <Tom.Rix@amd.com> - 18-35.rocm6.3.1
- Add module include dirs for kokkos
- switch from release to relwithdebinfo
- clean up some shebangs

* Mon Jan 20 2025 Tom Rix <Tom.Rix@amd.com> - 18-34.rocm6.3.1
- do dir creation for rocm-rpm-macros-modules
- fix suse build

* Sat Jan 11 2025 Tom Rix <Tom.Rix@amd.com> - 18-33.rocm6.3.1
- remove the requires gcc-c++
- build and use the libc++ runtime
- remove mlir
- add rocm-llvm-filesystem package

* Thu Jan 9 2025 Tom Rix <Tom.Rix@amd.com> - 18-32.rocm6.3.1
- Use compat gcc, gcc 15 breaks us.

* Sun Dec 29 2024 Tom Rix <Tom.Rix@amd.com> - 18-31.rocm6.3.1
- Remove excludes,provides filter for rocm-omp
- Fix packaging of clang extra tools

* Sat Dec 28 2024 Tom Rix <Tom.Rix@amd.com> - 18-30.rocm6.3.1
- Add clang-extra-tools package

* Sun Dec 22 2024 Tom Rix <Tom.Rix@amd.com> - 18-29.rocm6.3.1
- Update to 6.3.1

* Wed Dec 18 2024 Tom Rix <Tom.Rix@amd.com> - 18-28.rocm6.3.0
- Statically link comgr
- Remove lld-devel

* Thu Dec 12 2024 Jeremy Newton <alexjnewt at hotmail dot com> - 18-27.rocm6.3.0
- Excludes filtering

* Fri Dec 6 2024 Tom Rix <Tom.Rix@amd.com> - 18-26.rocm6.3.0
- Update to 6.3
- default bundled llvm on fedora

* Wed Nov 20 2024 Tom Rix <Tom.Rix@amd.com> - 18-25.rocm6.2.4
- Disable bundled mlir

* Tue Nov 19 2024 Tom Rix <Tom.Rix@amd.com> - 18-24.rocm6.2.4
- Clean up bundled install

* Thu Nov 14 2024 Tom Rix <Tom.Rix@amd.com> - 18-23.rocm6.2.4
- Add mlir to bundled

* Tue Nov 12 2024 Tom Rix <Tom.Rix@amd.com> - 18-22.rocm6.2.4
- Split up bundled to subpackages

* Sat Nov 9 2024 Tom Rix <Tom.Rix@amd.com> - 18-21.rocm6.2.4
- Fix version
- Rework bundle llvm to use existing package layouts.

* Fri Nov 8 2024 Tom Rix <Tom.Rix@amd.com> - 18-2.rocm6.2.4
- Perl is needed for RHEL.

* Thu Nov 7 2024 Tom Rix <Tom.Rix@amd.com> - 18-1.rocm6.2.4
- Update to 6.2.4

* Wed Nov 6 2024 Tom Rix <Tom.Rix@amd.com> - 18-20.rocm6.2.0
- Remove double config check

* Mon Nov 4 2024 Tom Rix <Tom.Rix@amd.com> - 18-19.rocm6.2.0
- Fix c++ isystem.
- Build LLVMgold.so
- Remove link to comgr cmake

* Fri Nov 1 2024 Tom Rix <Tom.Rix@amd.com> - 18-18.rocm6.2.0
- Mockable rocm llvm.

* Thu Oct 31 2024 Tom Rix <Tom.Rix@amd.com> - 18-17.rocm6.2.0
- Change bundle llvm to build rocm llvm.

* Wed Oct 30 2024 Tom Rix <Tom.Rix@amd.com> - 18-16.rocm6.2.0
- Improve macros

* Wed Oct 30 2024 Tom Rix <Tom.Rix@amd.com> - 18-15.rocm6.2.0
- RHEL is only x86_64

* Tue Oct 29 2024 Tom Rix <Tom.Rix@amd.com> - 18-14.rocm6.2.0
- Force device-libs location on bundling

* Tue Oct 29 2024 Tom Rix <Tom.Rix@amd.com> - 18-13.rocm6.2.0
- Fix opt/rocm path

* Tue Oct 29 2024 Tom Rix <Tom.Rix@amd.com> - 18-12.rocm6.2.0
- Use system clang with bundled llvm

* Sun Oct 27 2024 Tom Rix <Tom.Rix@amd.com> - 18-11.rocm6.2.0
- bundle llvm

* Thu Oct 10 2024 Tom Rix <Tom.Rix@amd.com> - 18-10.rocm6.2.0
- Fix hipcc-libomp-devel

* Mon Oct 07 2024 Tom Rix <Tom.Rix@amd.com> - 18-9.rocm6.2.0
- Work around broken clang++-18 link

* Tue Oct 01 2024 Jeremy Newton <alexjnewt at hotmail dot com> - 18-8.rocm6.2.0
- Drop compat build option (be more agnostic to llvm packaging)
- Add hip sanity test
- Spec cleanup

* Thu Sep 19 2024 Jeremy Newton <alexjnewt at hotmail dot com> - 18-7.rocm6.2.0
- Spec cleanup
- Add rocm-llvm-devel
- Build with clang (fixes builds on EL9)

* Sat Sep 07 2024 Tom Rix <Tom.Rix@amd.com> - 18-6.rocm6.2.0
- Revert change to location of amdgcn

* Fri Sep 06 2024 Tom Rix <Tom.Rix@amd.com> - 18-5.rocm6.2.0
- Fix finding hip path
- Fix dangling -isystem

* Thu Sep 05 2024 Tom Rix <Tom.Rix@amd.com> - 18-4.rocm6.2.0
- location of amdgcn/ changed in llvm18
- Fix the finding of the llvm root path

* Mon Sep 02 2024 Tom Rix <Tom.Rix@amd.com> - 18-3.rocm6.2.0
- -mlink-builtin-bitcode-postopt is not a system clang option

* Fri Aug 09 2024 Jeremy Newton <alexjnewt at hotmail dot com> - 18-2.rocm6.2.0
- Fix hipcc.bin patch for finding clang

* Thu Aug 08 2024 Jeremy Newton <alexjnewt at hotmail dot com> - 18-1.rocm6.2.0
- Update to 6.2

* Thu Aug 01 2024 Jeremy Newton <alexjnewt at hotmail dot com> - 17.3-7.rocm6.1.2
- Add libomp package

* Tue Jul 23 2024 Tom Rix <trix@redhat.com> - 17.3-6.rocm6.1.2
- Fix AMD_DEVICE_LIBS_PREFIX

* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 17.3-5.rocm6.1.2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Thu Jun 06 2024 Jeremy Newton <alexjnewt at hotmail dot com> - 17.3-4.rocm6.1.2
- Update to 6.1.2

* Thu May 16 2024 Jeremy Newton <alexjnewt at hotmail dot com> - 17.3-3.rocm6.1.1
- Fix rocminfo requires

* Thu May 09 2024 Jeremy Newton <alexjnewt at hotmail dot com> - 17.3-2.rocm6.1.1
- Fix rocm-device-libs requires

* Thu May 09 2024 Jeremy Newton <alexjnewt at hotmail dot com> - 17.3-1.rocm6.1.1
- Bump version to override existing rocm-device-libs package

* Thu May 09 2024 Jeremy Newton <alexjnewt at hotmail dot com> - 17.1-9.rocm6.1.1
- Add macros package

* Thu May 09 2024 Jeremy Newton <alexjnewt at hotmail dot com> - 17.1-8.rocm6.1.1
- Fix requires

* Thu May 09 2024 Jeremy Newton <alexjnewt at hotmail dot com> - 17.1-7.rocm6.1.1
- Update to ROCm 6.1.1
- Fix devel requires (should be on rocm-comgr-devel instead of hipcc)

* Mon May 06 2024 Jeremy Newton <alexjnewt at hotmail dot com> - 17.1-6.rocm6.1.0
- Update to ROCm 6.1
- This package now owns hipcc and rocm-device-libs subpackages

* Sat Mar 9 2024 Tom Rix <trix@redhat.com> - 17.1-5
- Fix mock build

* Thu Mar 7 2024 Tom Rix <trix@redhat.com> - 17.1-4
- Add with compat_build for llvm17

* Fri Jan 26 2024 Fedora Release Engineering <releng@fedoraproject.org> - 17.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 17.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Dec 14 2023 Jeremy Newton <alexjnewt at hotmail dot com> - 17.1-1
- Update to 17.1

* Fri Oct 20 2023 Jeremy Newton <alexjnewt at hotmail dot com> - 17.0-3
- Rebuild against rocm-device-libs 17.1

* Wed Sep 06 2023 Tulio Magno Quites Machado Filho <tuliom@redhat.com> - 17.0-2
- Rebuild against LLVM 17.0.0

* Tue Aug 15 2023 Jeremy Newton <alexjnewt at hotmail dot com> - 17.0-1
- Update to 17.0

* Tue Aug 08 2023 Jeremy Newton <alexjnewt at hotmail dot com> - 16.2-3
- Rebuild against rocm-device-libs 16.4

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 16.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Tue Jul 18 2023 Jeremy Newton <alexjnewt at hotmail dot com> - 16.2-1
- Update to 16.2

* Thu May 25 2023 Jeremy Newton <alexjnewt at hotmail dot com> - 16.1-4
- Roll back last change, as it didn't work

* Thu May 25 2023 Jeremy Newton <alexjnewt at hotmail dot com> - 16.1-3
- Add fix for RHBZ#2207599

* Wed Apr 19 2023 Jeremy Newton <alexjnewt at hotmail dot com> - 16.1-2
- Rebuild against 16.1 rocm-device-libs

* Wed Apr 19 2023 Jeremy Newton <alexjnewt at hotmail dot com> - 16.1-1
- Update to 16.1
- Add rocm-comgr full api provides (currently 2.5.0)

* Tue Apr 11 2023 Jeremy Newton <alexjnewt at hotmail dot com> - 16.0-2
- Fix comgr provides (should be major api version of comgr), for RHBZ#2185838

* Wed Mar 29 2023 Jeremy Newton <alexjnewt at hotmail dot com> - 16.0-1
- Update to 16.0 (forked sources for Fedora)

* Mon Feb 27 2023 Jeremy Newton <alexjnewt at hotmail dot com> - 5.4.1-3
- Use patch from Gentoo to improve test failures

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 5.4.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Sun Dec 18 2022 Jeremy Newton <alexjnewt at hotmail dot com> - 5.4.1-1
- Update to 5.4.1

* Tue Oct 04 2022 Jeremy Newton <alexjnewt at hotmail dot com> - 5.3.0-1
- Update to 5.3.0

* Mon Sep 19 2022 Jeremy Newton <alexjnewt at hotmail dot com> - 5.2.0-3
- Rebuilt against LLVM 15

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 5.2.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Sun Jul 03 2022 Jeremy Newton <alexjnewt at hotmail dot com> - 5.2.0-1
- Update to 5.2.0

* Fri Jun 10 2022 Jeremy Newton <alexjnewt at hotmail dot com> - 5.1.0-3
- Add comgr(rocm) provide

* Tue Apr 05 2022 Jeremy Newton <alexjnewt at hotmail dot com> - 5.1.0-2
- Enable ppc64le

* Tue Mar 29 2022 Jeremy Newton <alexjnewt at hotmail dot com> - 5.1.0-1
- Update to 5.1.0

* Fri Feb 11 2022 Jeremy Newton <alexjnewt at hotmail dot com> - 5.0.0-1
- Update to 5.0.0

* Mon Jan 24 2022 Jeremy Newton <alexjnewt at hotmail dot com> - 4.5.2-1
- Initial package
