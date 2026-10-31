%global dpcpp_major 7
%global dpcpp_minor 2
%global dpcpp_patch 0
%global llvm_major 23
%global sycl_major 9
%global llvm_version_suffix dpcpp%{dpcpp_major}
#date of the v%%{version} tag commit
%global sycl_compiler_version 20261014

# Private prefix: DPC++ ships its own clang/llvm that must not clash with the
# system toolchain. The clang driver locates SYCL headers, device libraries
# and the runtime relative to its own binary, so keep the upstream layout.
%global dpcpp_prefix %{_libdir}/dpcpp
%global dpcpp_bindir %{dpcpp_prefix}/bin
%global dpcpp_libdir %{dpcpp_prefix}/lib
%global dpcpp_includedir %{dpcpp_prefix}/include
# The private compiler-rt must not satisfy dependencies on Fedora's compiler-rt
# (libclang_rt.asan.so etc.). libsycl and the UR adapters keep their provides.
%global __provides_exclude ^libclang_rt\\..*\\.so

%ifarch x86_64
%global sycl_backends opencl;level_zero;level_zero_v2
%else
%global sycl_backends opencl
%endif

# No LTO for a full LLVM+clang+SYCL tree (build time and memory)
%global _lto_cflags %{nil}
# Makes the build go faster, while retaining Fedora's default
%global _binary_payload w19T0.zstdio

%bcond check 1

# top-level CMakeLists.txt of the monorepo
%global _vpath_srcdir llvm

# The sha's here likely need to get bumped when bumping dpcpp version
#   vc-intrinsics    llvm/lib/SYCLLowerIR/CMakeLists.txt   (LLVMGenXIntrinsics_GIT_TAG)
#   emhash           sycl/cmake/modules/FetchEmhash.cmake  (GIT_TAG)
#   umf              unified-runtime/source/common/CMakeLists.txt (UMF_TAG)
%global vc_intrinsics_commit 4fc83e12979096db72c129bd432238d5ca397e4d
%global emhash_commit 5e131ba09a5290823fe71099d9c35eb5df5345b6
%global umf_version 1.2.0

Name:           intel-dpcpp
Version:        %{dpcpp_major}.%{dpcpp_minor}.%{dpcpp_patch}
Release:        %autorelease
Summary:        Intel oneAPI DPC++/SYCL LLVM-based compiler

# LLVM: Apache-2.0 WITH LLVM-exception; vendored bits: MIT (vc-intrinsics,
# emhash), Apache-2.0 WITH LLVM-exception (UMF)
License:        Apache-2.0 WITH LLVM-exception AND MIT AND NCSA
URL:            https://github.com/intel/llvm
Source0:        %{url}/archive/refs/tags/v%{version}.tar.gz#/llvm-%{version}.tar.gz
Source10:       https://github.com/intel/vc-intrinsics/archive/%{vc_intrinsics_commit}/vc-intrinsics-%{vc_intrinsics_commit}.tar.gz
Source11:       https://github.com/ktprime/emhash/archive/%{emhash_commit}/emhash-%{emhash_commit}.tar.gz
Source12:       https://github.com/oneapi-src/unified-memory-framework/archive/v%{umf_version}/unified-memory-framework-%{umf_version}.tar.gz

Patch1:         sycl-0002-skip-usr-include-in-tests.patch
Patch4:         llvm-0001-version-symbols-of-shared-libs.patch
Patch5:         sycl-0003-fix-ambiguous-ipc-put-calls-with-gcc-16.patch
Patch6:         sycl-0004-unittests-sfinae-incomplete-not-error.patch
Patch7:         sycl-0005-load-sycl-jit-from-libsycl-dir.patch

ExclusiveArch:  x86_64 aarch64

BuildRequires:  cmake
BuildRequires:  ninja-build
BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  lld
BuildRequires:  python3
BuildRequires:  help2man
BuildRequires:  pkgconf
BuildRequires:  binutils-devel
BuildRequires:  libedit-devel
BuildRequires:  libxml2-devel
BuildRequires:  z3-devel
BuildRequires:  zlib-ng-compat-devel
BuildRequires:  libzstd-devel
BuildRequires:  ncurses-devel
BuildRequires:  hwloc-devel
BuildRequires:  tbb-devel
%ifarch x86_64
BuildRequires:  oneapi-level-zero-devel
BuildRequires:  intel-level-zero-devel
%endif
BuildRequires:  spirv-tools
BuildRequires:  spirv-tools-devel
BuildRequires:  spirv-headers-devel
BuildRequires:  opencl-headers
BuildRequires:  ocl-icd-devel
BuildRequires:  parallel-hashmap-devel

Provides:       bundled(llvm-project) = %{llvm_major}
Provides:       bundled(vc-intrinsics)
Provides:       bundled(emhash)
Provides:       bundled(unified-memory-framework) = %{umf_version}

Requires:       %{name}-filesystem%{?_isa} = %{version}-%{release}
Requires:       %{name}-libs%{?_isa} = %{version}-%{release}
Requires:       %{name}-clang-runtime-devel%{?_isa} = %{version}-%{release}
Requires:       %{name}-runtime%{?_isa} = %{version}-%{release}
Requires:       %{name}-devel%{?_isa} = %{version}-%{release}
Requires:       binutils
# clang requires gcc, clang++ requires libstdc++-devel
# - https://bugzilla.redhat.com/show_bug.cgi?id=1021645
# - https://bugzilla.redhat.com/show_bug.cgi?id=1158594
Requires:       libstdc++-devel
Requires:       gcc-c++
%ifarch x86_64
# needed for -fsycl-targets=spir64_gen ahead-of-time compilation
Requires:       intel-compute-runtime
Requires:       intel-igc
%endif

%description
DPC++ is a LLVM-based compiler project that implements compiler and runtime
support for the SYCL* language. It provides the clang-based compiler driver
(installed as dpclang / dpclang++), the SYCL runtime, and the oneAPI Unified
Runtime adapters for Level Zero and OpenCL devices.

%package        filesystem
Summary:        Directory layout of the DPC++ private toolchain prefix

%description    filesystem
Directories of the private DPC++ toolchain prefix (%{dpcpp_prefix}),
shared by all intel-dpcpp subpackages.

%package        libs
Summary:        Shared LLVM and clang libraries of the DPC++ compiler
Requires:       %{name}-filesystem%{?_isa} = %{version}-%{release}

%description    libs
Shared libraries of the DPC++ fork of LLVM and clang, used by the DPC++
compiler and by the SYCL JIT. Installed under %{dpcpp_libdir} so as not
to conflict with the system LLVM.

%package        clang-runtime-devel
Summary:        DPC++ clang resource headers and compiler runtime libraries
Requires:       %{name}-filesystem%{?_isa} = %{version}-%{release}
Provides:       %{name}-clang-runtime-static = %{version}-%{release}

%description    clang-runtime-devel
clang resource headers (stddef.h, intrinsics, offload wrappers, ...) and
compiler-rt runtime libraries used by the DPC++ compiler.

%package        runtime
Summary:        DPC++ SYCL runtime library and Unified Runtime adapters
Requires:       %{name}-filesystem%{?_isa} = %{version}-%{release}
Requires:       %{name}-libs%{?_isa} = %{version}-%{release}
Recommends:     %{name}-xptifw%{?_isa} = %{version}-%{release}

%description    runtime
SYCL runtime library (libsycl) and oneAPI Unified Runtime adapters
(Level Zero, OpenCL) needed to run applications built with the DPC++
compiler.

%package        devel
Summary:        DPC++ SYCL development files
Requires:       %{name}-filesystem%{?_isa} = %{version}-%{release}
Requires:       %{name}-runtime%{?_isa} = %{version}-%{release}
# libsycl-devicelib-host.a
Provides:       %{name}-static = %{version}-%{release}
# sycl/detail/cl.h includes <CL/cl.h>
Requires:       opencl-headers

%description    devel
SYCL headers, device libraries, and pkg-config files for developing
applications with the DPC++ compiler.

%package        llvm-tools
Summary:        LLVM tools bundled with the DPC++ compiler
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       %{name}-filesystem%{?_isa} = %{version}-%{release}
Requires:       %{name}-libs%{?_isa} = %{version}-%{release}

%description    llvm-tools
LLVM tools (llc, lli, opt, llvm-*, ...) built from the DPC++ fork
of LLVM. Installed under %{dpcpp_bindir} so as not to conflict with the
system LLVM.

%package        xptifw
Summary:        XPTI instrumentation framework library

%description    xptifw
XPTI (Cross-Platform Tracing Infrastructure) framework runtime used to
instrument SYCL applications.

%package        xptifw-devel
Summary:        XPTI instrumentation framework - development files
Requires:       %{name}-xptifw%{?_isa} = %{version}-%{release}
# libxpti.a
Provides:       %{name}-xptifw-static = %{version}-%{release}

%description    xptifw-devel
Headers, CMake config and pkg-config files for the XPTI framework.

%prep
%autosetup -p1 -n llvm-%{version}

# Unpack the vendored dependencies into vendor/, where the FetchContent
# overrides in %%build point to
mkdir -p vendor/{vc-intrinsics,emhash,unified-memory-framework}
tar -xzf %{SOURCE10} -C vendor/vc-intrinsics --strip-components=1
tar -xzf %{SOURCE11} -C vendor/emhash --strip-components=1
tar -xzf %{SOURCE12} -C vendor/unified-memory-framework --strip-components=1

%build
%ifarch x86_64
# CMake compiles .S files with ASMFLAGS, which %%set_build_flags does not set;
export ASMFLAGS="-fcf-protection"
%endif

%cmake \
    -DCMAKE_BUILD_TYPE=Release \
    -DCMAKE_INSTALL_PREFIX=%{dpcpp_prefix} \
    -DBUILD_SHARED_LIBS=ON \
    -DLLVM_SHLIB_SYMBOL_VERSION=LLVM_%{llvm_major}_%{llvm_version_suffix} \
    -DLLVM_TARGETS_TO_BUILD="host;SPIRV" \
    -DLLVM_ENABLE_PROJECTS="clang;sycl;llvm-spirv;opencl;xpti;xptifw;libdevice;sycl-jit" \
    -DLLVM_EXTERNAL_PROJECTS="sycl;llvm-spirv;opencl;xpti;xptifw;libdevice;sycl-jit" \
    -DLLVM_ENABLE_RUNTIMES=compiler-rt \
    -DLLVM_INCLUDE_BENCHMARKS=OFF \
    -DLLVM_VERSION_SUFFIX=%{llvm_version_suffix} \
    -DLLVM_ENABLE_RTTI=ON \
    -DLLVM_ENABLE_ZSTD=FORCE_ON \
    -DLLVM_USE_LINKER=lld \
    -DCMAKE_JOB_POOLS=link_job_pool=2 \
    -DCMAKE_JOB_POOL_LINK=link_job_pool \
    -DLLVM_BINUTILS_INCDIR=%{_includedir} \
    -DLLVM_EXTERNAL_SPIRV_HEADERS_SOURCE_DIR=%{_includedir} \
    -DBUG_REPORT_URL=https://github.com/intel/llvm/issues \
    -DSYCL_ENABLE_XPTI_TRACING=ON \
    -DSYCL_ENABLE_BACKENDS="%{sycl_backends}" \
    -DSYCL_COMPILER_VERSION=%{sycl_compiler_version} \
    -DDPCPP_VERSION_MAJOR=%{dpcpp_major} \
    -DDPCPP_VERSION_MINOR=%{dpcpp_minor} \
    -DDPCPP_VERSION_PATCH=%{dpcpp_patch} \
    -DPRE_RELEASE=0 \
    -DUR_STATIC_LOADER=ON \
    -DUR_USE_EXTERNAL_UMF=OFF \
    -DUMF_BUILD_SHARED_LIBRARY=OFF \
    -DFETCHCONTENT_FULLY_DISCONNECTED=ON \
    -DFETCHCONTENT_SOURCE_DIR_VC-INTRINSICS=$PWD/vendor/vc-intrinsics \
    -DFETCHCONTENT_SOURCE_DIR_EMHASH=$PWD/vendor/emhash \
    -DFETCHCONTENT_SOURCE_DIR_UNIFIED-MEMORY-FRAMEWORK=$PWD/vendor/unified-memory-framework

%cmake_build

# Man pages. help2man uses byte 0x80 internally and mangles UTF-8 in --help
mkdir -p h2m
while IFS=: read -r name tool desc; do
    printf '#!/bin/sh\n%%s "$@" | iconv -f UTF-8 -t ASCII//TRANSLIT\n' \
        "$PWD/%{__cmake_builddir}/bin/${tool}" > h2m/${name}
    chmod +x h2m/${name}
    help2man --no-info --version-string=%{version} --name="${desc}" \
        --output=${name}.1 h2m/${name}
done <<'MANPAGES'
dpclang:clang-%{llvm_major}:clang LLVM compiler for oneAPI DPC++
dpsycl-ls:sycl-ls:list devices and backends discovered by SYCL
dpsycl-prof:sycl-prof:profile SYCL applications (Chrome tracing JSON output)
dpsycl-sanitize:sycl-sanitize:find USM memory leaks in SYCL applications
dpsycl-trace:sycl-trace:trace SYCL and Unified Runtime API calls
dpsyclbin-dump:syclbin-dump:list the contents of a SYCLBIN file
MANPAGES

%install
%cmake_install

# sycl-jit installs its resource headers to an absolute path inside the build
# tree (mirrored under DESTDIR); drop everything outside /usr
find %{buildroot} -mindepth 1 -maxdepth 1 -not -name usr -exec rm -rf {} +

# XPTI collector plugins are dlopen()ed by bare name by sycl-trace/prof/sanitize,
# so they must live in the default library search path
mkdir -p %{buildroot}%{_libdir}
mv %{buildroot}%{dpcpp_prefix}/%{_lib}/lib*_collector.so %{buildroot}%{_libdir}/
# lib64/ and libexec/ only hold duplicates of lib/ (UR, UMF) and static libs
rm -rf %{buildroot}%{dpcpp_prefix}/%{_lib} %{buildroot}%{dpcpp_prefix}/libexec \
       %{buildroot}%{dpcpp_includedir}/xpti

# xptifw is an independent library, install in the system location
mkdir -p %{buildroot}%{_libdir}/{cmake,pkgconfig} %{buildroot}%{_includedir}
mv %{buildroot}%{dpcpp_libdir}/libxptifw.so* %{buildroot}%{dpcpp_libdir}/libxpti.a %{buildroot}%{_libdir}/
mv %{buildroot}%{dpcpp_libdir}/cmake/xpti %{buildroot}%{dpcpp_libdir}/cmake/xptifw %{buildroot}%{_libdir}/cmake/
mv %{buildroot}%{dpcpp_libdir}/pkgconfig/xptifw.pc %{buildroot}%{_libdir}/pkgconfig/
# xpti is header-only and shipped in the same -devel package; fix libdir for lib64
sed -i -e '/^Requires: xpti$/d' -e 's|^libdir=.*|libdir=%{_libdir}|' -e 's|^prefix=.*|prefix=%{_prefix}|' \
    %{buildroot}%{_libdir}/pkgconfig/xptifw.pc
cp -a xpti/include/xpti %{buildroot}%{_includedir}/

# Remove development artifacts of the private LLVM/clang that we do not ship
rm -rf %{buildroot}%{dpcpp_libdir}/cmake \
       %{buildroot}%{dpcpp_prefix}/share \
       %{buildroot}%{dpcpp_includedir}/{llvm,llvm-c,clang,clang-c,clang-tidy,lld,LLVMSPIRVLib,umf,umf.h} \
       %{buildroot}%{dpcpp_libdir}/libur_loader.a \
       %{buildroot}%{dpcpp_libdir}/libumf.a \
       %{buildroot}%{dpcpp_libdir}/libLLVM*.so \
       %{buildroot}%{dpcpp_libdir}/libclang[A-Z]*.so \
       %{buildroot}%{dpcpp_libdir}/libSYCLJITPasses.so \
       %{buildroot}%{dpcpp_libdir}/libclang-cpp.so* \
       %{buildroot}%{dpcpp_libdir}/libclang.so \
       %{buildroot}%{dpcpp_libdir}/libLTO.so* \
       %{buildroot}%{dpcpp_libdir}/libRemarks.so* \
       %{buildroot}%{dpcpp_libdir}/libear \
       %{buildroot}%{dpcpp_libdir}/libscanbuild \
       %{buildroot}%{dpcpp_libdir}/python3*
rm -f  %{buildroot}%{dpcpp_bindir}/{amdgpu-arch,nvptx-arch,scan-build*,scan-view,analyze-build,intercept-build,c-index-test,git-clang-format,hmaptool,clang-format-diff.py,clang-tblgen,llvm-tblgen,llvm-c-test,llvm-ir2vec}

# llvm-* tools run by the driver stay in the main package
find %{buildroot}%{dpcpp_bindir} -name 'llvm-*' \
    -not -name llvm-foreach -not -name llvm-link -not -name llvm-spirv \
    -not -name llvm-objcopy -not -name llvm-offload-binary -not -name llvm-offload-wrapper \
    -printf '%{dpcpp_bindir}/%%f\n' > llvm-tools.files

# Launchers in PATH. Upstream ships dp-prefixed argv[0] shims (dpllvm) next to
# the real tools; point at those so the compiler finds its siblings.
mkdir -p %{buildroot}%{_bindir}
for tool in dpclang dpclang++ dpclang-cpp dpclang-cl dpsycl-ls dpsycl-prof dpsycl-sanitize dpsycl-trace dpsyclbin-dump; do
    ln -s ../%{_lib}/dpcpp/bin/${tool} %{buildroot}%{_bindir}/${tool}
done

# Man pages
mkdir -p %{buildroot}%{_mandir}/man1
install -p -m 0644 dpclang.1 dpsycl-ls.1 dpsycl-prof.1 dpsycl-sanitize.1 \
    dpsycl-trace.1 dpsyclbin-dump.1 %{buildroot}%{_mandir}/man1/
for m in dpclang++ dpclang-cpp dpclang-cl; do
    echo ".so man1/dpclang.1" > %{buildroot}%{_mandir}/man1/${m}.1
done

# libsycl must stay next to the UR adapters (the UR loader resolves adapters
# relative to the libsycl path); expose it in the system libdir
# through a symlink.
ln -s dpcpp/lib/libsycl.so.%{sycl_major} %{buildroot}%{_libdir}/libsycl.so.%{sycl_major}
ln -s libsycl.so.%{sycl_major} %{buildroot}%{_libdir}/libsycl.so

# pkg-config for the SYCL runtime
cat > %{buildroot}%{_libdir}/pkgconfig/sycl-dpcpp-%{dpcpp_major}.pc <<'EOF'
prefix=%{dpcpp_prefix}
includedir=${prefix}/include
libdir=%{_libdir}
sycl_version=%{sycl_major}.0.0

Name: sycl-dpcpp-%{dpcpp_major}
Description: Intel DPC++ compiler SYCL runtime library
Version: %{version}
Libs: -L${libdir} -lsycl
Cflags: -I${includedir}
EOF
ln -s sycl-dpcpp-%{dpcpp_major}.pc %{buildroot}%{_libdir}/pkgconfig/sycl-dpcpp.pc

%check
%if %{with check}
%cmake_build --target SYCLUnitTests
find %{__cmake_builddir}/tools/sycl/unittests -type f -name '*Tests*' -perm /111 -printf '%%h\n' | sort -u |
    xargs -I{} ln -sf $PWD/%{__cmake_builddir}/lib/libur_adapter_mock.so.0 {}/libur_adapter_mock.so.0
export LIT_FILTER_OUT='include_deps/sycl_(detail_core|khr_includes_(handler|kernel_bundle|queue|reduction|stream|usm))\.hpp\.cpp|tools/abi_check_positive\.cpp'
%ifarch aarch64
LIT_FILTER_OUT+='|esimd|invoke_simd|basic_tests/(interop-level-zero-2020|generic_type_traits|no_math_in_global_ns|builtins/builtin_unit_tests)\.cpp|gdb/printers\.cpp|BindlessImagesExtensionTests-(Non_)?Preview_Tests'
%endif
%cmake_build --target check-sycl
%endif

%files
%license llvm/LICENSE.TXT
%doc README.md sycl/ReleaseNotes.md
%{_bindir}/dpclang
%{_bindir}/dpclang++
%{_bindir}/dpclang-cpp
%{_bindir}/dpclang-cl
%{_bindir}/dpsycl-ls
%{_bindir}/dpsycl-prof
%{_bindir}/dpsycl-sanitize
%{_bindir}/dpsycl-trace
%{_bindir}/dpsyclbin-dump
%{_mandir}/man1/dp*
%{dpcpp_bindir}/dp*
%{dpcpp_bindir}/clang*
%{dpcpp_bindir}/sycl-*
%{dpcpp_bindir}/syclbin-dump
%{dpcpp_bindir}/spirv-to-ir-wrapper
%{dpcpp_bindir}/append-file
%{dpcpp_bindir}/file-table-tform
%{dpcpp_bindir}/llvm-foreach
%{dpcpp_bindir}/llvm-link
%{dpcpp_bindir}/llvm-spirv
%{dpcpp_bindir}/llvm-objcopy
%{dpcpp_bindir}/llvm-offload-binary
%{dpcpp_bindir}/llvm-offload-wrapper
%{dpcpp_bindir}/opencl-aot
%{dpcpp_bindir}/offload-arch
%{dpcpp_libdir}/LLVMgold.so
%{_libdir}/libsycl_profiler_collector.so
%{_libdir}/libsycl_sanitizer_collector.so
%{_libdir}/libsycl_ur_trace_collector.so
%ifarch x86_64
%{_libdir}/libze_trace_collector.so
%endif

%files filesystem
%dir %{dpcpp_prefix}
%dir %{dpcpp_bindir}
%dir %{dpcpp_libdir}
%dir %{dpcpp_libdir}/clang
%dir %{dpcpp_libdir}/clang/%{llvm_major}
%dir %{dpcpp_includedir}

%files libs
%license llvm/LICENSE.TXT
%{dpcpp_libdir}/libLLVM*.so.%{llvm_major}.*
%{dpcpp_libdir}/libclang*.so.%{llvm_major}.*
%{dpcpp_libdir}/libSYCLJITPasses.so.%{llvm_major}.*

%files clang-runtime-devel
%license llvm/LICENSE.TXT
%{dpcpp_libdir}/clang/%{llvm_major}/*

%files runtime
%license llvm/LICENSE.TXT
%{_libdir}/libsycl.so.%{sycl_major}
%{dpcpp_libdir}/libsycl.so.%{sycl_major}*
%{dpcpp_libdir}/libsycl-preview.so.%{sycl_major}*
%{dpcpp_libdir}/libsycl-jit.so
%{dpcpp_libdir}/libsycl-jit.so.*
%{dpcpp_libdir}/SYCLJITPassesPlugin.so
%ifnarch aarch64
%{dpcpp_libdir}/libur_adapter_*.so.*
%endif
%{dpcpp_libdir}/libur_sanitizer_layer.so.*

%files devel
%{_libdir}/libsycl.so
%{dpcpp_libdir}/libsycl.so
%{dpcpp_libdir}/libsycl-preview.so
%ifnarch aarch64
%{dpcpp_libdir}/libur_adapter_*.so
%endif
%{dpcpp_libdir}/libur_sanitizer_layer.so
%{dpcpp_libdir}/libsycl-devicelib-host.a
%{dpcpp_libdir}/dpcpp-%{dpcpp_major}/
%{dpcpp_libdir}/pkgconfig/
%{_libdir}/pkgconfig/sycl-dpcpp-%{dpcpp_major}.pc
%{_libdir}/pkgconfig/sycl-dpcpp.pc
%{dpcpp_includedir}/sycl/
%{dpcpp_includedir}/CL/
%{dpcpp_includedir}/std/
%{dpcpp_includedir}/unified-runtime/

%files llvm-tools -f llvm-tools.files
%{dpcpp_bindir}/llubi
%{dpcpp_bindir}/diagtool
%{dpcpp_bindir}/dsymutil
%{dpcpp_bindir}/llc
%{dpcpp_bindir}/lli
%{dpcpp_bindir}/opt
%{dpcpp_bindir}/reduce-chunk-list
%{dpcpp_bindir}/sancov
%{dpcpp_bindir}/sanstats
%{dpcpp_bindir}/verify-uselistorder

%files xptifw
%license llvm/LICENSE.TXT
%{_libdir}/libxptifw.so.*

%files xptifw-devel
%{_libdir}/libxptifw.so
%{_libdir}/libxpti.a
%{_includedir}/xpti/
%{_libdir}/cmake/xpti/
%{_libdir}/cmake/xptifw/
%{_libdir}/pkgconfig/xptifw.pc

%changelog
%autochangelog
