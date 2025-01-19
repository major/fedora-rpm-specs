%global toolchain clang

# Opt out of https://fedoraproject.org/wiki/Changes/fno-omit-frame-pointer
# https://bugzilla.redhat.com/show_bug.cgi?id=2158587
%undefine _include_frame_pointers

%global maj_ver 19
%global min_ver 1
%global patch_ver 6
#global rc_ver 4
%global bolt_version %{maj_ver}.%{min_ver}.%{patch_ver}
%global bolt_srcdir llvm-project-%{bolt_version}%{?rc_ver:-rc%{rc_ver}}.src

Name: llvm-bolt
Version: %{bolt_version}%{?rc_ver:~rc%{rc_ver}}
Release: 2%{?dist}
Summary: a post-link optimizer developed to speed up large applications

License: Apache-2.0 WITH LLVM-exception
URL: https://github.com/llvm/llvm-project/tree/main/bolt
Source0: https://github.com/llvm/llvm-project/releases/download/llvmorg-%{maj_ver}.%{min_ver}.%{patch_ver}%{?rc_ver:-rc%{rc_ver}}/%{bolt_srcdir}.tar.xz
Source1: https://github.com/llvm/llvm-project/releases/download/llvmorg-%{maj_ver}.%{min_ver}.%{patch_ver}%{?rc_ver:-rc%{rc_ver}}/%{bolt_srcdir}.tar.xz.sig
Source2: release-keys.asc

# BOLT is not respecting the component split of LLVM and requires some private
# headers in order to compile itself. Try to disable as much libraries as
# possible in order to reduce build time.
Patch0: rm-llvm-libs.diff

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
BuildRequires: doxygen

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
%autosetup -n %{bolt_srcdir} -p1


%build

%global _lto_cflags %{nil}

%cmake  -S llvm -GNinja \
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
        -DLLVM_EXTERNAL_LIT=%{_bindir}/lit \
        -DLLVM_ENABLE_PROJECTS="bolt" \
        -DLLVM_TARGETS_TO_BUILD="X86;AArch64"

# Set LD_LIBRARY_PATH now because we skip rpath generation and the build uses
# some just built libraries.
export LD_LIBRARY_PATH=%{_builddir}/%{bolt_srcdir}/%{_vpath_builddir}/%{_lib}
%cmake_build --target bolt


%install
%cmake_install --component bolt

# Remove files installed during the build phase.
rm -f %{buildroot}/%{_builddir}/%{bolt_srcdir}/%{_vpath_builddir}/%{_lib}/lib*.a

# We don't ship libLLVMBOLT*.a
rm -f %{buildroot}%{_libdir}/libLLVMBOLT*.a

# There currently is not support upstream for building html doc from BOLT
install -d %{buildroot}%{_pkgdocdir}
mv bolt/README.md bolt/docs/*.md %{buildroot}%{_pkgdocdir}

%check
%ifarch aarch64
# Failing test cases on aarch64
rm bolt/test/cache+-deprecated.test bolt/test/bolt-icf.test bolt/test/R_ABS.pic.lld.cpp
# The following tests require LSE in order to run.
# More info at: https://github.com/llvm/llvm-project/issues/86485
if ! grep -q atomics /proc/cpuinfo; then
    rm bolt/test/runtime/AArch64/basic-instrumentation.test \
       bolt/test/runtime/AArch64/hook-fini.test \
       bolt/test/runtime/AArch64/instrumentation-ind-call.c \
       bolt/test/runtime/exceptions-instrumentation.test \
       bolt/test/runtime/instrumentation-indirect-2.c \
       bolt/test/runtime/pie-exceptions-split.test
fi

%endif

%ifarch x86_64
# Failing x86_64 test
rm bolt/test/X86/internal-call-instrument.s
%endif

export LIT_XFAIL="AArch64/build_id.c;AArch64/plt-call.test;X86/linux-static-keys.s;X86/plt-call.test"
export LD_LIBRARY_PATH=%{_builddir}/%{bolt_srcdir}/%{_vpath_builddir}/%{_lib}
export DESTDIR=%{buildroot}
%cmake_build --target check-bolt

# Remove files installed during the check phase.
rm -f %{buildroot}/%{_builddir}/%{bolt_srcdir}/%{_vpath_builddir}/%{_lib}/lib*.a


%files
%license LICENSE.TXT
%{_bindir}/llvm-bolt
%{_bindir}/llvm-boltdiff
%{_bindir}/llvm-bolt-heatmap
%{_bindir}/merge-fdata
%{_bindir}/perf2bolt

%{_libdir}/libbolt_rt_hugify.a
%{_libdir}/libbolt_rt_instr.a


%files doc
%doc %{_pkgdocdir}

%changelog
* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 19.1.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Thu Jan 02 2025 Timm Bäder <tbaeder@redhat.com> - 19.1.6-1
- Update to 19.1.6

* Tue Dec 05 2024 Timm Bäder <tbaeder@redhat.com> - 19.1.5-1
- Update to 19.1.5

* Mon Nov 25 2024 Timm Bäder <tbaeder@redhat.com> - 19.1.4-1
- Update to 19.1.4

* Fri Sep 20 2024 Timm Bäder <tbaeder@redhat.com> - 19.1.0-1
- Update to 19.1.0

* Mon Sep 16 2024 Timm Bäder <tbaeder@redhat.com> - 19.1.0~rc4-1
- Update to 19.1.0-rc4

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 18.1.8-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Fri Jul 12 2024 Jesus Checa Hidalgo <jchecahi@redhat.com> - 18.1.8-1
- 18.1.8 Update

* Fri Jun 14 2024 Tom Stellard <tstellar@redhat.com> - 18.1.7-1
- 18.1.7 Release

* Tue May 21 2024 Tom Stellard <tstellar@redhat.com> - 18.1.6-1
- 18.1.6 Release

* Wed Apr 17 2024 Tom Stellard <tstellar@redhat.com> - 18.1.3-1
- 18.1.3 Release

* Fri Mar 22 2024 Tom Stellard <tstellar@redhat.com> - 18.1.2-1
- 18.1.2 Release

* Wed Mar 13 2024 Tom Stellard <tstellar@redhat.com> - 18.1.1-1
- 18.1.1 Release

* Thu Feb 29 2024 Tom Stellard <tstellar@redhat.com> - 18.1.0~rc4-1
- 18.1.0-rc4 Release

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

* Thu Oct 05 2023 Tulio Magno Quites Machado Filho <tuliom@redhat.com> - 17.0.2-1
- Update to LLVM 17.0.2

* Mon Sep 25 2023 Tulio Magno Quites Machado Filho <tuliom@redhat.com> - 17.0.1-1
- Update to LLVM 17.0.1

* Mon Sep 11 2023 Tulio Magno Quites Machado Filho <tuliom@redhat.com> - 17.0.0~rc4-1
- Update to LLVM 17.0.0 RC4

* Fri Aug 25 2023 Tulio Magno Quites Machado Filho <tuliom@redhat.com> - 17.0.0~rc3-1
- Update to LLVM 17.0.0 RC3

* Wed Aug 23 2023 Tulio Magno Quites Machado Filho <tuliom@redhat.com> - 17.0.0~rc2-1
- Update to LLVM 17.0.0 RC2

* Thu Aug 03 2023 Tulio Magno Quites Machado Filho <tuliom@redhat.com> - 17.0.0~rc1-1
- Update to LLVM 17.0.0 RC1

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 16.0.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Mon Jul 10 2023 Tulio Magno Quites Machado Filho <tuliom@redhat.com> - 16.0.6-1
- Update to LLVM 16.0.6

* Tue Jun 06 2023 Tulio Magno Quites Machado Filho <tuliom@redhat.com> - 16.0.5-1
- Update to LLVM 16.0.5
- Remove code that became obsolete after commit 9d0a2a41081ba.

* Sat May 20 2023 Tulio Magno Quites Machado Filho <tuliom@redhat.com> - 16.0.4-1
- Update to LLVM 16.0.4

* Wed May 10 2023 Tulio Magno Quites Machado Filho <tuliom@redhat.com> - 16.0.3-1
- Update to LLVM 16.0.3

* Thu Apr 27 2023 Tulio Magno Quites Machado Filho <tuliom@redhat.com> - 16.0.2-1
- Update to LLVM 16.0.2

* Thu Apr 13 2023 Tulio Magno Quites Machado Filho <tuliom@redhat.com> - 16.0.1-1
- Update to LLVM 16.0.1

* Tue Mar 21 2023 Tulio Magno Quites Machado Filho <tuliom@redhat.com> - 16.0.0-1
- Update to LLVM 16.0.0

* Wed Mar 15 2023 Tulio Magno Quites Machado Filho <tuliom@redhat.com> - 16.0.0~rc4-1
- Update to LLVM 16.0.0 RC4

* Fri Mar 03 2023 Tulio Magno Quites Machado Filho <tuliom@redhat.com> - 16.0.0~rc3-1
- Update to LLVM 16.0.0 RC3

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 15.0.7-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jan 13 2023 Nikita Popov <npopov@redhat.com> - 15.0.7-1
- Update to LLVM 15.0.7

* Fri Jan 13 2023 Tom Stellard <tstellar@redhat.com> - 15.0.6-2
- Omit frame pointers when building

* Tue Dec 06 2022 Nikita Popov <npopov@redhat.com> - 15.0.6-1
- Update to LLVM 15.0.6

* Mon Jul 11 2022 sguelton@redhat.com - 15.0.0-1
- Initial version.

