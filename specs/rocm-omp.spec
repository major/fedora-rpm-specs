# Upstream tags are based on rocm releases:
%global rocm_release 6.3
%global rocm_patch 1
%global rocm_version %{rocm_release}.%{rocm_patch}

# What LLVM is upstream using (use LLVM_VERSION_MAJOR from llvm/CMakeLists.txt):
%global llvm_maj_ver 18
%global upstreamname llvm-project

%global toolchain clang

%global bundle_prefix %{_libdir}/rocm/llvm
%global llvm_triple %{_target_platform}

%bcond_with debug
%if %{with debug}
%global build_type DEBUG
%else
%global build_type RelWithDebInfo
%endif

Name:           rocm-omp
Version:        %{rocm_version}
Release:        1%{?dist}
Summary:        ROCm OpenMP

Url:            https://github.com/ROCm/%{upstreamname}
License:        Apache-2.0 WITH LLVM-exception OR NCSA AND MIT
Source0:        %{url}/archive/rocm-%{rocm_version}.tar.gz#/%{name}-%{rocm_version}.tar.gz

Patch3:         0001-Remove-err_drv_duplicate_config-check.patch

BuildRequires:  binutils-devel
BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  fdupes
BuildRequires:  libffi-devel
BuildRequires:  libzstd-devel
BuildRequires:  perl
BuildRequires:  rocm-compilersupport-macros
BuildRequires:  rocm-device-libs
BuildRequires:  rocm-runtime-devel
BuildRequires:  zlib-devel

Requires:       rocm-llvm-filesystem

ExclusiveArch:  x86_64
%global targets_to_build "X86;AMDGPU"

%description
%{summary}

%package devel
Summary:        Libraries and headers for %{name}
Requires:       rocm-omp%{?_isa} = %{version}-%{release}

%description devel
%{summary}

%package static
Summary:        Static Libraries for %{name}
Requires:       rocm-omp-devel%{?_isa} = %{version}-%{release}

%description static
%{summary}

%prep
%autosetup -p1 -n %{upstreamname}-rocm-%{rocm_version}

# no nvidia
sed -i -e 's@LIBOMPTARGET_DEVICE_ARCHITECTURES "all"@LIBOMPTARGET_DEVICE_ARCHITECTURES "${all_amdgpu_architectures}"@' openmp/libomptarget/DeviceRTL/CMakeLists.txt

# rm llvm-project bits we do not need
rm -rf {bolt,clang,compiler-rt,flang,libc,libclc,libcxx,libcxxabi,libunwind,lld,lldb,llvm-libgcc,mlir,polly,pst,runtimes,utils}

%build

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

cd openmp
%cmake %{llvmrocm_cmake_config} \
       -DBUILD_SHARED=ON \
       -DClang_DIR=%{rocmllvm_cmakedir}/../clang \
       -DCMAKE_AR=%{rocmllvm_bindir}/llvm-ar \
       -DCMAKE_INSTALL_RPATH=%{rocmllvm_libdir} \
       -DCMAKE_LINKER=%{rocmllvm_bindir}/ld.lld \
       -DCMAKE_RANLIB=%{rocmllvm_bindir}/llvm-ranlib \
       -DCMAKE_CXX_COMPILER=%{rocmllvm_bindir}/clang++ \
       -DCMAKE_C_COMPILER=%{rocmllvm_bindir}/clang \
       -DCMAKE_C_COMPILER_AR=%{rocmllvm_bindir}/llvm-ar \
       -DCMAKE_C_COMPILER_RANLIB=%{rocmllvm_bindir}/llvm-ranlib \
       -DLIBOMPTARGET_AMDGPU_ARCH=%{rocmllvm_bindir}/amdgpu-arch \
       -DCMAKE_INSTALL_PREFIX=%{bundle_prefix} \
       -DCMAKE_INSTALL_LIBDIR=lib \
       -DLLD_DIR=%{rocmllvm_cmakedir}/../lld \
       -DLLVM_DIR=%{rocmllvm_cmakedir} \
       -DLLVM_ENABLE_PROJECTS="openmp" \
       -DLLVM_ENABLE_RUNTIMES="" \
       -DLIBOMPTARGET_NVPTX_ENABLE_BCLIB=OFF \
       -DLIBOMPTARGET_NVPTX_CUDA_COMPILER="" \
       -DLIBOMPTARGET_NVPTX_BC_LINKER="" \
       -DLIBOMP_OMPD_GDB_SUPPORT=OFF \
       -DLIBOMPTARGET_BUILD_AMDGPU_PLUGIN=ON \
       -DLIBOMPTARGET_BUILD_CUDA_PLUGIN=OFF \
       -DLIBOMPTARGET_BUILD_DEVICERTL_BCLIB=ON \
       -DLIBOMPTARGET_NVPTX_ENABLE_BCLIB=OFF \
       -DLIBOMP_INSTALL_ALIASES=OFF \
       -DLIBOMP_ARCHER_SUPPORT=OFF \
       -DOPENMP_STANDALONE_BUILD=ON \
       -DOPENMP_LLVM_TOOLS_DIR=%{rocmllvm_bindir}

export LD_LIBRARY_PATH=%{rocmllvm_libdir}

%cmake_build

%install

cd openmp
%cmake_install

# Clean up dupes:
%fdupes %{buildroot}%{_prefix}

if [ -d %{buildroot}%{bundle_prefix}/lib/omptest ]; then
    rm -rf %{buildroot}%{bundle_prefix}/lib/omptest
fi
if [ -d %{buildroot}%{bundle_prefix}/lib/cmake/omptest ]; then
    rm -rf %{buildroot}%{bundle_prefix}/lib/cmake/omptest
fi
    
%files
%{bundle_prefix}/bin/llvm-omp*
%{bundle_prefix}/bin/prep-libomptarget-bc
%{bundle_prefix}/lib/libomp*.so.*

%files devel
%{bundle_prefix}/include/omp*.h
%{bundle_prefix}/lib/clang/%{llvm_maj_ver}/include/hostexec.h
%{bundle_prefix}/lib/cmake/openmp/
%{bundle_prefix}/lib/disable_dynamic_devmem.ll
%{bundle_prefix}/lib/libdevice/
%{bundle_prefix}/lib/*.bc
%{bundle_prefix}/lib/libomp*.so

%files static
%{bundle_prefix}/lib/libomptarget.devicertl.a

%changelog
* Thu Dec 26 2024 Tom Rix <Tom.Rix@amd.com> - 6.3.1-1
- Initial version
