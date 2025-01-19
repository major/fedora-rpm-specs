%global toolchain clang
%global maj_ver 17
%global min_ver 0
%global patch_ver 6
#global rc_ver 4
%global mlir_version %{maj_ver}.%{min_ver}.%{patch_ver}
%global mlir_srcdir mlir-%{mlir_version}%{?rc_ver:rc%{rc_ver}}.src

# Opt out of https://fedoraproject.org/wiki/Changes/fno-omit-frame-pointer
# https://bugzilla.redhat.com/show_bug.cgi?id=2158587
%undefine _include_frame_pointers

%bcond_without check
%bcond_without compat_build

%if %{with compat_build}
%global pkg_name mlir%{maj_ver}
%global install_prefix %{_libdir}/llvm%{maj_ver}
%global install_includedir %{install_prefix}/include
%global install_libdir %{install_prefix}/lib
%global install_datadir %{install_prefix}/share
%global install_bindir %{install_prefix}/bin
%else
%global pkg_name mlir
%global install_prefix /usr
%global install_includedir %{_includedir}
%global install_libdir %{_libdir}
%global install_datadir %{_datadir}
%global install_bindir %{_bindir}
%endif

Name:    %{pkg_name}
Version: %{mlir_version}%{?rc_ver:~rc%{rc_ver}}
Release: 6%{?dist}
Summary: Multi-Level Intermediate Representation Overview

License: Apache-2.0 WITH LLVM-exception
URL: http://mlir.llvm.org
Source0: https://github.com/llvm/llvm-project/releases/download/llvmorg-%{maj_ver}.%{min_ver}.%{patch_ver}%{?rc_ver:-rc%{rc_ver}}/%{mlir_srcdir}.tar.xz
Source1: https://github.com/llvm/llvm-project/releases/download/llvmorg-%{maj_ver}.%{min_ver}.%{patch_ver}%{?rc_ver:-rc%{rc_ver}}/%{mlir_srcdir}.tar.xz.sig
Source2: release-keys.asc

Patch1: 0001-mlir-python-Reuse-the-library-directory.patch

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

# The amount of RAM used per process has been set by trial and error.
# This number may increase/decrease from time to time and may require changes.
# We prefer to be on the safe side in order to avoid spurious errors.
%global _smp_mflags -j%{lua: print_max_procs(6144)}

# Support for i686 upstream is unclear with lots of tests failling.
ExcludeArch: i686

BuildRequires: clang
BuildRequires: cmake
BuildRequires: ninja-build
BuildRequires: zlib-devel
%if %{with compat_build}
BuildRequires:	llvm%{maj_ver}-devel = %{version}
BuildRequires:	llvm%{maj_ver}-cmake-utils = %{version}
%else
BuildRequires: llvm-devel = %{version}
BuildRequires: llvm-cmake-utils = %{version}
BuildRequires: llvm-googletest = %{version}
BuildRequires: llvm-test = %{version}
%endif
BuildRequires: python3-lit
BuildRequires: python3-devel
BuildRequires: python3-numpy
BuildRequires: python3-pybind11
BuildRequires: python3-pyyaml

# For origin certification
BuildRequires: gnupg2

%description
The MLIR project is a novel approach to building reusable and extensible
compiler infrastructure. MLIR aims to address software fragmentation,
improve compilation for heterogeneous hardware, significantly reduce
the cost of building domain specific compilers, and aid in connecting
existing compilers together.

%package static
Summary: MLIR static files
Requires: %{name}%{?_isa} = %{version}-%{release}

%description static
MLIR static files.

%package devel
Summary: MLIR development files
Requires: %{name}%{?_isa} = %{version}-%{release}
Requires: %{name}-static%{?_isa} = %{version}-%{release}

%description devel
MLIR development files.

%if %{without compat_build}
%package -n python3-%{name}
Summary: MLIR python bindings
Requires: python3
Requires: python3-numpy

%description -n python3-%{name}
%{summary}
%endif

%prep
%{gpgverify} --keyring='%{SOURCE2}' --signature='%{SOURCE1}' --data='%{SOURCE0}'
%autosetup -n %{mlir_srcdir} -p2


%build

%ifarch %ix86
%global debug_package %{nil}
%global _lto_cflags %{nil}
%endif

# On aarch64, dwz can take very long to process all the files. It either fails
# reaching a timeout or consumes too much RAM.  Restrict its resources in
# order to stop dwz early. We prefer to miss the DWARF optimization than not
# not being able to build this package on aarch64.
%global _dwz_low_mem_die_limit_aarch64 1
%global _dwz_max_die_limit_aarch64 1000000

# On s390x, dwz consumes too much RAM.  Restrict its resources in
# order to stop dwz early. We prefer to miss the DWARF optimization than not
# not being able to build this package on aarch64.
%global _dwz_low_mem_die_limit_s390x 1
%global _dwz_max_die_limit_s390x 1000000

%cmake  -GNinja \
        -DCMAKE_BUILD_TYPE=RelWithDebInfo \
        -DCMAKE_SKIP_RPATH=ON \
        -DLLVM_LINK_LLVM_DYLIB:BOOL=ON \
        -DLLVM_BUILD_LLVM_DYLIB=ON \
	-DCMAKE_INSTALL_PREFIX=%{install_prefix} \
        -DCMAKE_PREFIX_PATH=%{install_datadir}/cmake/llvm/ \
        -DLLVM_EXTERNAL_LIT=%{_bindir}/lit \
        -DLLVM_THIRD_PARTY_DIR=%{install_datadir}/llvm/src/utils \
        -DLLVM_COMMON_CMAKE_UTILS=%{install_datadir}/llvm/cmake \
        -DLLVM_BUILD_TOOLS:BOOL=ON \
        -DLLVM_BUILD_UTILS:BOOL=ON \
        -DLLVM_LIBRARY_OUTPUT_INTDIR="." \
        -DLLVM_SHLIB_OUTPUT_INTDIR="%{_builddir}/%{mlir_srcdir}/%{__cmake_builddir}/lib/ExecutionEngine/" \
        -DMLIR_INCLUDE_DOCS:BOOL=ON \
        -DMLIR_INCLUDE_TESTS:BOOL=ON \
        -DMLIR_INCLUDE_INTEGRATION_TESTS:BOOL=OFF \
        -DBUILD_SHARED_LIBS=OFF \
        -DMLIR_INSTALL_AGGREGATE_OBJECTS=OFF \
        -DMLIR_BUILD_MLIR_C_DYLIB=ON \
%ifarch aarch64 %ix86 ppc64le x86_64
        -DLLVM_PARALLEL_LINK_JOBS=1 \
%endif
%ifarch %ix86
        -DMLIR_RUN_X86VECTOR_TESTS:BOOL=OFF \
%endif
%if %{with compat_build}
	-DLLVM_CMAKE_DIR=%{install_libdir}/cmake/llvm \
%else
        -DMLIR_ENABLE_BINDINGS_PYTHON:BOOL=ON \
%if 0%{?__isa_bits} == 64
        -DLLVM_LIBDIR_SUFFIX=64
%else
        -DLLVM_LIBDIR_SUFFIX=
%endif
%endif
# build process .exe tools normally use rpath or static linkage
export LD_LIBRARY_PATH=%{_builddir}/%{mlir_srcdir}/%{name}/%{_build}/%{_lib}
%cmake_build

%install
%cmake_install
%if %{without compat_build}
mkdir -p %{buildroot}/%{python3_sitearch}
mv %{buildroot}/usr/python_packages/mlir_core/mlir %{buildroot}/%{python3_sitearch}
# These directories should be empty now.
rmdir %{buildroot}/usr/python_packages/mlir_core %{buildroot}/usr/python_packages
# Unneeded files.
rm -rf %{buildroot}/usr/src/python
%endif

%check
# Remove tablegen tests, as they rely on includes from llvm/.
rm -rf test/mlir-tblgen

%ifarch s390x
# s390x does not support half-float
rm test/python/execution_engine.py
%endif

%ifarch %{ix86}
# TODO: Test currently fails on i686.
rm test/IR/file-metadata-resources.mlir

# TODO: There's two issues here (see https://github.com/llvm/llvm-project/issues/58357):
# 1. The async dialect hardcodes a 64-bit assumption.
# 2. The cpu runner tests call mlir-opt without awareness of the host index size.
# For this reason, skip mlir-cpu-runner tests on 32-bit.
rm -rf test/mlir-cpu-runner

# The following test requires AVX2.
rm -rf test/Dialect/Math/polynomial-approximation.mlir

# TODO: Can these vector tests pass on i386?
rm -rf test/Conversion/MathToLibm/convert-to-libm.mlir
rm -rf test/Dialect/Vector/canonicalize.mlir
rm -rf test/Dialect/Vector/vector-unroll-options.mlir
rm -rf test/Dialect/SparseTensor/sparse_vector_ops.mlir

# TODO: Investigate the following issues.
rm -rf test/mlir-pdll-lsp-server/compilation_database.test
rm -rf test/mlir-pdll-lsp-server/completion.test
rm -rf test/mlir-pdll-lsp-server/definition-split-file.test
rm -rf test/mlir-pdll-lsp-server/definition.test
rm -rf test/mlir-pdll-lsp-server/document-links.test
rm -rf test/mlir-pdll-lsp-server/document-symbols.test
rm -rf test/mlir-pdll-lsp-server/exit-eof.test
rm -rf test/mlir-pdll-lsp-server/exit-with-shutdown.test
rm -rf test/mlir-pdll-lsp-server/exit-without-shutdown.test
rm -rf test/mlir-pdll-lsp-server/hover.test
rm -rf test/mlir-pdll-lsp-server/initialize-params-invalid.test
rm -rf test/mlir-pdll-lsp-server/initialize-params.test
rm -rf test/mlir-pdll-lsp-server/inlay-hints.test
rm -rf test/mlir-pdll-lsp-server/references.test
rm -rf test/mlir-pdll-lsp-server/signature-help.test
rm -rf test/mlir-pdll-lsp-server/textdocument-didchange.test
rm -rf test/mlir-pdll-lsp-server/view-output.test
%endif

%if %{without compat_build}
# Test execution normally relies on RPATH, so set LD_LIBRARY_PATH instead.
export LD_LIBRARY_PATH=%{buildroot}/%{install_libdir}:%{buildroot}/%{python3_sitearch}/mlir/_mlir_libs
export PYTHONPATH=%{buildroot}/%{python3_sitearch}
%else
export LD_LIBRARY_PATH=%{buildroot}/%{install_libdir}
%endif
%cmake_build --target check-mlir

%files
%license LICENSE.TXT
%{install_libdir}/libMLIR*.so.%{maj_ver}*
%{install_libdir}/libmlir_async_runtime.so.%{maj_ver}*
%{install_libdir}/libmlir_c_runner_utils.so.%{maj_ver}*
%{install_libdir}/libmlir_float16_utils.so.%{maj_ver}*
%{install_libdir}/libmlir_runner_utils.so.%{maj_ver}*

%files static
%{install_libdir}/libMLIR*.a

%files devel
%{install_bindir}/mlir-cpu-runner
%{install_bindir}/mlir-linalg-ods-yaml-gen
%{install_bindir}/mlir-lsp-server
%{install_bindir}/mlir-opt
%{install_bindir}/mlir-pdll
%{install_bindir}/mlir-pdll-lsp-server
%{install_bindir}/mlir-reduce
%{install_bindir}/mlir-tblgen
%{install_bindir}/mlir-translate
%{install_bindir}/tblgen-lsp-server
%{install_libdir}/libMLIR*.so
%{install_libdir}/libmlir_async_runtime.so
%{install_libdir}/libmlir_c_runner_utils.so
%{install_libdir}/libmlir_float16_utils.so
%{install_libdir}/libmlir_runner_utils.so
%{install_includedir}/mlir
%{install_includedir}/mlir-c
%{install_libdir}/cmake/mlir

%if %{without compat_build}
%files -n python3-%{name}
%{python3_sitearch}/mlir/
%endif

%changelog
* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 17.0.6-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 17.0.6-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Wed May 1 2024 Tom Rix <trix@redhat.com> - 17.0.6-4
- Add compat_build logic

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 17.0.6-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 17.0.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Nov 29 2023 Tulio Magno Quites Machado Filho <tuliom@redhat.com> - 17.0.6-1
- Update to LLVM 17.0.6

* Wed Nov 01 2023 Tulio Magno Quites Machado Filho <tuliom@redhat.com> - 17.0.4-1
- Update to LLVM 17.0.4

* Wed Oct 18 2023 Tulio Magno Quites Machado Filho <tuliom@redhat.com> - 17.0.3-1
- Update to LLVM 17.0.3

* Wed Oct 04 2023 Tulio Magno Quites Machado Filho <tuliom@redhat.com> - 17.0.2-1
- Update to LLVM 17.0.2

* Sat Sep 23 2023 Tulio Magno Quites Machado Filho <tuliom@redhat.com> - 17.0.1-1
- Update to LLVM 17.0.1

* Sun Sep 10 2023 Tulio Magno Quites Machado Filho <tuliom@redhat.com> - 17.0.0~rc4-1
- Update to LLVM 17.0.0 RC4

* Tue Sep 05 2023 Tulio Magno Quites Machado Filho <tuliom@redhat.com> - 17.0.0~rc3-3
- Enable python bindings. Fixes rhbz#2221241

* Mon Aug 28 2023 Tulio Magno Quites Machado Filho <tuliom@redhat.com> - 17.0.0~rc3-2
- Restrict link jobs on x86_64

* Fri Aug 25 2023 Tulio Magno Quites Machado Filho <tuliom@redhat.com> - 17.0.0~rc3-1
- Update to LLVM 17.0.0 RC3

* Wed Aug 23 2023 Tulio Magno Quites Machado Filho <tuliom@redhat.com> - 17.0.0~rc2-1
- Update to LLVM 17.0.0 RC2

* Wed Aug 02 2023 Tulio Magno Quites Machado Filho <tuliom@redhat.com> - 17.0.0~rc1-1
- Update to LLVM 17.0.0 RC1

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 16.0.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Mon Jul 10 2023 Tulio Magno Quites Machado Filho <tuliom@redhat.com> - 16.0.6-1
- Update to LLVM 16.0.6

* Thu Jun 15 2023 Nikita Popov <npopov@redhat.com> - 16.0.5-2
- Use llvm-cmake-utils package

* Tue Jun 06 2023 Tulio Magno Quites Machado Filho <tuliom@redhat.com> - 16.0.5-1
- Update to LLVM 16.0.5

* Fri May 19 2023 Tulio Magno Quites Machado Filho <tuliom@redhat.com> - 16.0.4-1
- Update to LLVM 16.0.4

* Wed May 10 2023 Tulio Magno Quites Machado Filho <tuliom@redhat.com> - 16.0.3-1
- Update to LLVM 16.0.3

* Thu Apr 27 2023 Tulio Magno Quites Machado Filho <tuliom@redhat.com> - 16.0.2-1
- Update to LLVM 16.0.2

* Thu Apr 13 2023 Tulio Magno Quites Machado Filho <tuliom@redhat.com> - 16.0.1-1
- Update to LLVM 16.0.1

* Thu Apr 06 2023 Nikita Popov <npopov@redhat.com> - 16.0.0-4
- Build with clang

* Mon Apr 03 2023 Tulio Magno Quites Machado Filho <tuliom@redhat.com> - 16.0.0-3
- Re-enable s390x builds
- Link ppc64le serially in order to avoid hitting memory limits

* Mon Apr 03 2023 Tulio Magno Quites Machado Filho <tuliom@redhat.com> - 16.0.0-2
- Disable s390x builds temporarily

* Tue Mar 21 2023 Tulio Magno Quites Machado Filho <tuliom@redhat.com> - 16.0.0-1
- Update to LLVM 16.0.0

* Wed Mar 15 2023 Tulio Magno Quites Machado Filho <tuliom@redhat.com> - 16.0.0~rc4-1
- Update to LLVM 16.0.0 RC4

* Thu Feb 23 2023 Tulio Magno Quites Machado Filho <tuliom@redhat.com> - 16.0.0~rc3-1
- Update to LLVM 16.0.0 RC3

* Wed Feb 15 2023 Tulio Magno Quites Machado Filho <tuliom@redhat.com> - 16.0.0~rc1-1
- Update to LLVM 16.0.0 RC1

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 15.0.7-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jan 13 2023 Nikita Popov <npopov@redhat.com> - 15.0.7-1
- Update to LLVM 15.0.7

* Fri Jan 13 2023 Nikita Popov <npopov@redhat.com> - 15.0.6-3
- Omit frame pointers when building

* Thu Dec 22 2022 Nikita Popov <npopov@redhat.com> - 15.0.6-2
- rhbz#2127916: Add mlir tools to mlir-devel

* Mon Dec 05 2022 Nikita Popov <npopov@redhat.com> - 15.0.6-1
- Update to LLVM 15.0.6

* Mon Nov 07 2022 Nikita Popov <npopov@redhat.com> - 15.0.4-1
- Update to LLVM 15.0.4

* Thu Sep 15 2022 Nikita Popov <npopov@redhat.com> - 15.0.0-4
- Rebuild

* Wed Sep 14 2022 Nikita Popov <npopov@redhat.com> - 15.0.0-3
- Run tests during the build

* Mon Sep 12 2022 Nikita Popov <npopov@redhat.com> - 15.0.0-2
- Add explicit requires from mlir-devel to mlir

* Tue Sep 06 2022 Nikita Popov <npopov@redhat.com> - 15.0.0-1
- Update to LLVM 15.0.0

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 14.0.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon Jun 20 2022 Timm Bäder <tbaeder@redhat.com> - 14.0.5-1
- Update to 14.0.5

* Thu Mar 24 2022 Timm Bäder <tbaeder@redhat.com> - 14.0.0-1
- Update to 14.0.0

* Mon Feb 07 2022 Nikita Popov <npopov@redhat.com> - 13.0.1-2
- Reenable build on armv7hl

* Thu Feb 03 2022 Nikita Popov <npopov@redhat.com> - 13.0.1-1
- Update to LLVM 13.0.1 final

* Tue Feb 01 2022 Nikita Popov <npopov@redhat.com> - 13.0.1~rc3-1
- Update to LLVM 13.0.1rc3

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 13.0.1~rc2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jan 14 2022 Nikita Popov <npopov@redhat.com> - 13.0.1~rc2-1
- Update to LLVM 13.0.1rc2

* Wed Jan 12 2022 Nikita Popov <npopov@redhat.com> - 13.0.1~rc1-1
- Update to LLVM 13.0.1rc1

* Wed Oct 06 2021 Tom Stellard <tstellar@redhat.com> - 13.0.0-2
- Rebuild for llvm soname bump

* Fri Oct 01 2021 Tom Stellard <tstellar@redhat.com> - 13.0.0-1
- 13.0.0 Release

* Wed Sep 22 2021 Tom Stellard <tstellar@redhat.com> - 13.0.0~rc3-1
- 13.0.0-rc3 Release

* Tue Aug 10 2021 Tom Stellard <tstellar@redhat.com> - 13.0.0~rc1-3
- Add -static requires back to -devel package

* Tue Aug 10 2021 Tom Stellard <tstellar@redhat.com> - 13.0.0~rc1-2
- Add back the -static sub-package

* Mon Aug 09 2021 Tom Stellard <tstellar@redhat.com> - 13.0.0~rc1-1
- 13.0.0-rc1 Release

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 12.0.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jul 13 2021 Tom Stellard <tstellar@redhat.com> - 12.0.1-1
- 12.0.1 Release

* Thu Jul 01 2021 Tom Stellard <tstellar@redhat.com> - 12.0.1~rc3-1
- 12.0.1-rc3 Release

* Wed Jun 02 2021 Tom Stellard <tstellar@redhat.com> - 12.0.1~rc1-1
- 12.0.1-rc1 Release

* Fri Apr 16 2021 Tom Stellard <tstellar@redhat.com> - 12.0.0-1
- 12.0.0 Release

* Thu Apr 08 2021 sguelton@redhat.com - 12.0.0-0.7.rc5
- New upstream release candidate

* Fri Apr 02 2021 sguelton@redhat.com - 12.0.0-0.6.rc4
- New upstream release candidate

* Wed Mar 31 2021 Jonathan Wakely <jwakely@redhat.com> - 12.0.0-0.5.rc3
- Rebuilt for removed libstdc++ symbols (#1937698)

* Thu Mar 11 2021 sguelton@redhat.com - 12.0.0-0.4.rc3
- LLVM 12.0.0 rc3

* Wed Mar 10 2021 sguelton@redhat.com - 12.0.0-0.3.rc2
- rebuilt

* Wed Feb 24 2021 sguelton@redhat.com - 12.0.0-0.2.rc2
- llvm 12.0.0-rc2 release

* Thu Feb 18 2021 sguelton@redhat.com - 12.0.0-0.1.rc1
- llvm 12.0.0-rc1 release

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 11.1.0-0.3.rc2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Fri Jan 22 2021 Serge Guelton - 11.1.0-0.2.rc2
- llvm 11.1.0-rc2 release

* Thu Jan 14 2021 Serge Guelton - 11.1.0-0.1.rc1
- 11.1.0-rc1 release

* Wed Jan 06 2021 Serge Guelton - 11.0.1-3
- LLVM 11.0.1 final

* Tue Dec 22 2020 sguelton@redhat.com - 11.0.1-2.rc2
- llvm 11.0.1-rc2

* Tue Dec 01 2020 sguelton@redhat.com - 11.0.1-1.rc1
- llvm 11.0.1-rc1

* Thu Oct 15 2020 sguelton@redhat.com - 11.0.0-1
- Fix NVR

* Mon Oct 12 2020 sguelton@redhat.com - 11.0.0-0.6
- llvm 11.0.0 - final release

* Thu Oct 08 2020 sguelton@redhat.com - 11.0.0-0.5.rc6
- 11.0.0-rc6

* Fri Oct 02 2020 sguelton@redhat.com - 11.0.0-0.4.rc5
- 11.0.0-rc5 Release

* Sun Sep 27 2020 sguelton@redhat.com - 11.0.0-0.3.rc3
- Fix NVR

* Thu Sep 24 2020 sguelton@redhat.com - 11.0.0-0.1.rc3
- 11.0.0-rc3 Release

* Wed Sep 02 2020 sguelton@redhat.com - 11.0.0-0.2.rc2
- Package mlir-tblgen

* Wed Aug 12 2020 Cristian Balint <cristian.balint@gmail.com> - 11.0.0-0.1.rc1
- Initial version.

