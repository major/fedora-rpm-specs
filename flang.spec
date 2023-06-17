%global maj_ver 16
%global min_ver 0
%global patch_ver 5
#global rc_ver 4
%global flang_version %{maj_ver}.%{min_ver}.%{patch_ver}
%global flang_srcdir flang-%{flang_version}%{?rc_ver:rc%{rc_ver}}.src

# Opt out of https://fedoraproject.org/wiki/Changes/fno-omit-frame-pointer
# https://bugzilla.redhat.com/show_bug.cgi?id=2158587
%undefine _include_frame_pointers

Name: flang
Version: %{flang_version}%{?rc_ver:~rc%{rc_ver}}
Release: 2%{?dist}
Summary: a Fortran language front-end designed for integration with LLVM

License: Apache-2.0 WITH LLVM-exception
URL:     https://flang.llvm.org
Source0: https://github.com/llvm/llvm-project/releases/download/llvmorg-%{flang_version}%{?rc_ver:-rc%{rc_ver}}/%{flang_srcdir}.tar.xz
Source1: https://github.com/llvm/llvm-project/releases/download/llvmorg-%{flang_version}%{?rc_ver:-rc%{rc_ver}}/%{flang_srcdir}.tar.xz.sig
Source2: release-keys.asc

# flang depends on one internal clang tablegen file for documentation generation.
Source3: https://raw.githubusercontent.com/llvm/llvm-project/llvmorg-%{flang_version}%{?rc_ver:-rc%{rc_ver}}/clang/include/clang/Driver/Options.td

Source4: TestAliasAnalysis.h

# Needed for documentation generation
Patch1: 0001-PATCH-flang-Disable-use-of-sphinx_markdown_tables.patch

# The Bye plugin is not distributed on Fedora.
Patch3: 0001-flang-Remove-the-dependency-on-Bye.patch

# Fedora does not distribute libclangBasic.a.
Patch4: remove-clangBasic-dependency.diff

# Fedora uses CLANG_DEFAULT_PIE_ON_LINUX=OFF.
Patch5: 0001-Match-Fedora-s-value-for-CLANG_DEFAULT_PIE_ON_LINUX.patch

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

# Avoid gcc reaching 4GB of memory on 32-bit targets and also running out of
# memory on builders with many CPUs.
%global _lto_cflags %{nil}
# The amount of RAM used per process has been set by trial and error.
# This number may increase/decrease from time to time and may require changes.
# We prefer to be on the safe side in order to avoid spurious errors.
%global _smp_mflags -j%{lua: print_max_procs(6144)}

# We don't produce debug info on ARM to avoid OOM during the build.
%ifarch %{arm}
%global debug_package %{nil}
%endif

# Link error on i686.
# s390x is not supported upstream yet.
ExcludeArch: i686 s390x

BuildRequires: gcc
BuildRequires: gcc-c++
BuildRequires: cmake
BuildRequires: zlib-devel
BuildRequires: llvm-devel = %{version}
BuildRequires: llvm-cmake-utils = %{version}
BuildRequires: llvm-test = %{version}
BuildRequires: llvm-googletest = %{version}
BuildRequires: mlir-devel = %{version}
BuildRequires: ninja-build
BuildRequires: python3-lit >= 12.0.0
BuildRequires: python3-sphinx
BuildRequires: python3-recommonmark
BuildRequires: doxygen

# The new flang drive requires clang-devel
BuildRequires: clang-devel = %{version}

# For origin certification
BuildRequires: gnupg2

%description

Flang is a ground-up implementation of a Fortran front end written in modern
C++.

%package devel
Summary: Flang header files
Requires: %{name}%{?_isa} = %{version}-%{release}

%description devel
Flang header files.

%package doc
Summary: Documentation for Flang
BuildArch: noarch
Requires: %{name} = %{version}-%{release}

%description doc
Documentation for Flang

%prep
%{gpgverify} --keyring='%{SOURCE2}' --signature='%{SOURCE1}' --data='%{SOURCE0}'
%autosetup -n %{flang_srcdir} -p2
# Copy Options.td for docs generation
mkdir -p ../clang/include/clang/Driver
cp %{SOURCE3} ../clang/include/clang/Driver

mkdir -p include/mlir/test/lib/Analysis/
cp %{SOURCE4} include/mlir/test/lib/Analysis/

%build
%cmake -GNinja \
       -DMLIR_TABLEGEN_EXE=%{_bindir}/mlir-tblgen \
       -DCMAKE_BUILD_TYPE=RelWithDebInfo \
       -DCMAKE_INSTALL_RPATH=";" \
       -DCLANG_DIR=%{_libdir}/cmake/clang \
       -DCLANG_LINK_CLANG_DYLIB:BOOL=ON \
       -DLLVM_MAIN_SRC_DIR=%{_datadir}/llvm/src \
       -DBUILD_SHARED_LIBS:BOOL=ON \
       -DLLVM_LINK_LLVM_DYLIB:BOOL=ON \
       -DLLVM_EXTERNAL_LIT=%{_bindir}/lit \
       -DLLVM_THIRD_PARTY_DIR=%{_datadir}/llvm/src/utils \
       -DCMAKE_PREFIX_PATH=%{_libdir}/cmake/llvm/ \
       -DLLVM_COMMON_CMAKE_UTILS=%{_datadir}/llvm/cmake \
\
       -DFLANG_INCLUDE_DOCS:BOOL=ON \
       -DLLVM_ENABLE_SPHINX:BOOL=ON \
       -DSPHINX_WARNINGS_AS_ERRORS=OFF \
       -DSPHINX_EXECUTABLE=%{_bindir}/sphinx-build-3 \
\
%if 0%{?__isa_bits} == 64
       -DLLVM_LIBDIR_SUFFIX=64
%else
       -DLLVM_LIBDIR_SUFFIX=
%endif

# Avoid gcc reaching 4GB of memory
%ifarch %{ix86} s390x
sed -i -e 's/-g /-g1 /g' %{__cmake_builddir}/build.ninja
%endif
# On ARM, disable debuginfo entirely to avoid OOM.
%ifarch %{arm}
sed -i -e 's/-g /-g0 /g' -e 's/-O2/-O1/g' %{__cmake_builddir}/build.ninja
%endif

export LD_LIBRARY_PATH=%{_builddir}/%{flang_srcdir}/%{_build}/lib
%cmake_build
%cmake_build --target docs-flang-html


%install
%cmake_install

# this is a test binary
rm -f %{buildroot}%{_bindir}/f18-parse-demo

install -d %{buildroot}%{_pkgdocdir}/html
cp -r %{_vpath_builddir}/docs/html/* %{buildroot}%{_pkgdocdir}/html/

%check

%ifarch s390x
rm test/Evaluate/folding07.f90
rm test/Evaluate/fold-nearest.f90
# s390x is not yet supported as a lowering target, so remove all related tests.
rm -rf test/Driver/
rm -rf test/Fir/
rm -rf test/Lower/
%endif

# These tests fail on 32-bit targets.
%ifarch %{ix86} %{arm}
rm -f test/Fir/fir-ops.fir
rm -f test/Semantics/assign03.f90
rm -f test/Semantics/data05.f90
rm -f test/Semantics/offsets01.f90
rm -f test/Semantics/offsets02.f90
rm -f test/Semantics/typeinfo01.f90
rm -f test/Semantics/spec-expr.f90
rm -f test/Evaluate/folding19.f90
%endif

export LD_LIBRARY_PATH=%{_builddir}/%{flang_srcdir}/%{_build}/lib
%cmake_build --target check-flang 

%files
%license LICENSE.TXT
%{_bindir}/tco
%{_bindir}/bbc
%{_bindir}/flang-to-external-fc
%{_bindir}/fir-opt
%{_bindir}/flang-new
%{_libdir}/libFortranLower.so.%{maj_ver}*
%{_libdir}/libFortranSemantics.so.%{maj_ver}*
%{_libdir}/libFortranCommon.so.%{maj_ver}*
%{_libdir}/libFortranRuntime.so.%{maj_ver}*
%{_libdir}/libFortranDecimal.so.%{maj_ver}*
%{_libdir}/libFortranEvaluate.so.%{maj_ver}*
%{_libdir}/libFortranParser.so.%{maj_ver}*
%{_libdir}/libflangFrontend.so.%{maj_ver}*
%{_libdir}/libflangFrontendTool.so.%{maj_ver}*
%{_libdir}/libFIRAnalysis.so.%{maj_ver}
%{_libdir}/libFIRBuilder.so.%{maj_ver}
%{_libdir}/libFIRCodeGen.so.%{maj_ver}
%{_libdir}/libFIRDialect.so.%{maj_ver}
%{_libdir}/libFIRSupport.so.%{maj_ver}
%{_libdir}/libFIRTestAnalysis.so.%{maj_ver}
%{_libdir}/libFIRTransforms.so.%{maj_ver}
%{_libdir}/libHLFIRDialect.so.%{maj_ver}
%{_libdir}/libHLFIRTransforms.so.%{maj_ver}

%files devel
%{_libdir}/libFortranLower.so
%{_libdir}/libFortranParser.so
%{_libdir}/libFortranCommon.so
%{_libdir}/libFortranSemantics.so
%{_libdir}/libFortran_main.a
%{_libdir}/libFIRAnalysis.so
%{_libdir}/libFIRBuilder.so
%{_libdir}/libFIRCodeGen.so
%{_libdir}/libFIRDialect.so
%{_libdir}/libFIRSupport.so
%{_libdir}/libFIRTestAnalysis.so
%{_libdir}/libFIRTransforms.so
%{_libdir}/libFortranDecimal.so
%{_libdir}/libFortranRuntime.so
%{_libdir}/libFortranEvaluate.so
%{_libdir}/libflangFrontend.so
%{_libdir}/libflangFrontendTool.so
%{_libdir}/libHLFIRDialect.so
%{_libdir}/libHLFIRTransforms.so
%{_includedir}/flang
%{_libdir}/cmake/

%files doc
%dir %{_pkgdocdir}
%doc %{_pkgdocdir}/html/

%changelog
* Thu Jun 15 2023 Nikita Popov <npopov@redhat.com> - 16.0.5-2
- Use llvm-cmake-utils package

* Tue Jun 06 2023 Tulio Magno Quites Machado Filho <tuliom@redhat.com> - 16.0.5-1
- Update to LLVM 16.0.5

* Sat May 20 2023 Tulio Magno Quites Machado Filho <tuliom@redhat.com> - 16.0.4-1
- Update to LLVM 16.0.4

* Mon May 15 2023 Tulio Magno Quites Machado Filho <tuliom@redhat.com> - 16.0.3-2
- Remove patch for ppc64le triple in favor of https://reviews.llvm.org/D149746

* Thu May 11 2023 Tulio Magno Quites Machado Filho <tuliom@redhat.com> - 16.0.3-1
- Update to LLVM 16.0.3

* Thu Apr 27 2023 Tulio Magno Quites Machado Filho <tuliom@redhat.com> - 16.0.2-1
- Update to LLVM 16.0.2

* Thu Apr 13 2023 Tulio Magno Quites Machado Filho <tuliom@redhat.com> - 16.0.1-1
- Update to LLVM 16.0.1

* Thu Apr 06 2023 Tulio Magno Quites Machado Filho <tuliom@redhat.com> - 16.0.0-3
- Set the amount of jobs dynamically

* Mon Apr 03 2023 Tulio Magno Quites Machado Filho <tuliom@redhat.com> - 16.0.0-2
- Fix mlir header path

* Tue Mar 21 2023 Tulio Magno Quites Machado Filho <tuliom@redhat.com> - 16.0.0-1
- Update to LLVM 16.0.0

* Thu Mar 16 2023 Tulio Magno Quites Machado Filho <tuliom@redhat.com> - 16.0.0~rc4-1
- Update to LLVM 16.0.0 RC4

* Tue Mar 14 2023 Tulio Magno Quites Machado Filho <tuliom@redhat.com> - 16.0.0~rc3-2
- Stop building on s390x

* Mon Feb 27 2023 Tulio Magno Quites Machado Filho <tuliom@redhat.com> - 16.0.0~rc3-1
- Update to LLVM 16.0.0 RC3

* Thu Jan 19 2023 Nikita Popov <npopov@redhat.com> - 15.0.7-3
- Fix build with GCC 13

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 15.0.7-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jan 13 2023 Nikita Popov <npopov@redhat.com> - 15.0.7-1
- Update to LLVM 15.0.7

* Fri Jan 13 2023 Nikita Popov <npopov@redhat.com> - 15.0.6-2
- Omit frame pointers when building

* Tue Dec 06 2022 Nikita Popov <npopov@redhat.com> - 15.0.6-1
- Update to LLVM 15.0.6

* Mon Nov 07 2022 Nikita Popov <npopov@redhat.com> - 15.0.4-1
- Update to LLVM 15.0.4

* Tue Sep 13 2022 Nikita Popov <npopov@redhat.com> - 15.0.0-2
- Build with -O2 on s390x

* Tue Sep 06 2022 Nikita Popov <npopov@redhat.com> - 15.0.0-1
- Update to LLVM 15.0.0

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 14.0.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon Jun 20 2022 Timm Bäder <tbaeder@redhat.com> - 14.0.5-1
- Update to 14.0.5

* Thu Mar 24 2022 Timm Bäder <tbaeder@redhat.com> - 14.0.0-1
- Update to 14.0.0

* Tue Feb 08 2022 Nikita Popov <npopov@redhat.com> - 13.0.1-2
- Enable arm build, now that mlir supports arm

* Thu Feb 03 2022 Nikita Popov <npopov@redhat.com> - 13.0.1-1
- Update to LLVM 13.0.1 final

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 13.0.1~rc2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jan 14 2022 Nikita Popov <npopov@redhat.com> - 13.0.1~rc2-1
- Update to LLVM 13.0.1rc2

* Wed Jan 12 2022 Nikita Popov <npopov@redhat.com> - 13.0.1~rc1-1
- Update to LLVM 13.0.1rc1

* Fri Oct 01 2021 Tom Stellard <tstellar@rehat.com> - 13.0.0-1
- 13.0.0 Release

* Tue Sep 21 2021 Tom Stellard <tstlelar@redhat.com> - 13.0.1~rc3-1
- 13.0.0-rc3 Release

* Mon Aug 09 2021 Tom Stellard <tstellar@redhat.com> - 13.0.1~rc1-1
- 13.0.0-rc1 Release

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 12.0.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Jul 14 2021 Tom Stellard <tstellar@redhat.com> - 12.0.1-1
- 12.0.1 Release

* Wed Jun 30 2021 Tom Stellard <tstellar@redhat.com> - 12.0.1~rc3-1
- 12.0.1-rc3 Release

* Thu Jun 03 2021 Tom Stellard <tstellar@redhat.com> - 12.0.1~rc1-1
- 12.0.1-rc1 Release

* Fri Apr 16 2021 Tom Stellard <tstellar@redhat.com> - 12.0.0-1
- 12.0.0 Release

* Thu Apr 08 2021 sguelton@redhat.com - 12.0.0-0.6.rc5
- New upstream release candidate

* Fri Apr 02 2021 sguelton@redhat.com - 12.0.0-0.5.rc4
- New upstream release candidate

* Thu Mar 11 2021 sguelton@redhat.com - 12.0.0-0.4.rc3
- LLVM 12.0.0 rc3

* Wed Mar 10 2021 sguelton@redhat.com - 12.0.0-0.3.rc2
- rebuilt

* Wed Feb 24 2021 sguelton@redhat.com - 12.0.0-0.2.rc2
- 12.0.0-rc2 Release

* Fri Feb 19 2021 Tom Stellard <tsellar@redhat.com> - 12.0.0-0.1.rc1
- 12.0.0-rc1 Release

* Wed Feb 10 2021 Jeff Law <law@redhat.com> - 11.1.0-0.3.rc1
- Fix missing #include for gcc-11

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 11.1.0-0.2.rc1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

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

* Mon Oct 12 2020 sguelton@redhat.com - 11.0.0-0.5
- llvm 11.0.0 - final release

* Thu Oct 08 2020 sguelton@redhat.com - 11.0.0-0.4.rc6
- 11.0.0-rc6

* Fri Oct 02 2020 sguelton@redhat.com - 11.0.0-0.3.rc5
- 11.0.0-rc5 Release

* Sun Sep 27 2020 sguelton@redhat.com - 11.0.0-0.2.rc3
- Fix NVR

* Thu Sep 24 2020 sguelton@redhat.com - 11.0.0-0.1.rc3
- 11.0.0-rc3 Release

* Tue Sep 01 2020 sguelton@redhat.com - 11.0.0-0.1.rc2
- Initial version.

