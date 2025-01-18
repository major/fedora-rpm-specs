%bcond_with snapshot_build

%if %{with snapshot_build}
# Unlock LLVM Snapshot LUA functions
%{llvm_sb_verbose}
%{llvm_sb}
%endif

%global toolchain clang

# Opt out of https://fedoraproject.org/wiki/Changes/fno-omit-frame-pointer
# https://bugzilla.redhat.com/show_bug.cgi?id=2158587
%undefine _include_frame_pointers

%bcond_without compat_build

%global maj_ver 17
%global min_ver 0
%global patch_ver 6
#global rc_ver 4
%if %{with snapshot_build}
%global maj_ver %{llvm_snapshot_version_major}
%global min_ver %{llvm_snapshot_version_minor}
%global patch_ver %{llvm_snapshot_version_patch}
%undefine rc_ver
%endif
%global compiler_rt_version %{maj_ver}.%{min_ver}.%{patch_ver}

%global crt_srcdir compiler-rt-%{compiler_rt_version}%{?rc_ver:rc%{rc_ver}}.src

%if %{with compat_build}
%global pkg_name compiler-rt%{maj_ver}
%global llvm_pkg_name llvm%{maj_ver}
%else
%global pkg_name compiler-rt
%global llvm_pkg_name llvm
%endif

# see https://sourceware.org/bugzilla/show_bug.cgi?id=25271
%global optflags %(echo %{optflags} -D_DEFAULT_SOURCE)

# see https://gcc.gnu.org/bugzilla/show_bug.cgi?id=93615
%global optflags %(echo %{optflags} -Dasm=__asm__)

Name:		%{pkg_name}
Version:	%{compiler_rt_version}%{?rc_ver:~rc%{rc_ver}}%{?llvm_snapshot_version_suffix:~%{llvm_snapshot_version_suffix}}
Release:	8%{?dist}
Summary:	LLVM "compiler-rt" runtime libraries

License:	Apache-2.0 WITH LLVM-exception OR NCSA OR MIT
URL:		http://llvm.org
%if %{with snapshot_build}
Source0:    %{llvm_snapshot_source_prefix}compiler-rt-%{llvm_snapshot_yyyymmdd}.src.tar.xz
%{llvm_snapshot_extra_source_tags}
%else
Source0:	https://github.com/llvm/llvm-project/releases/download/llvmorg-%{compiler_rt_version}%{?rc_ver:-rc%{rc_ver}}/%{crt_srcdir}.tar.xz
Source1:	https://github.com/llvm/llvm-project/releases/download/llvmorg-%{compiler_rt_version}%{?rc_ver:-rc%{rc_ver}}/%{crt_srcdir}.tar.xz.sig
Source2:	release-keys.asc
%endif

Patch0:		0001-compiler-rt-Fix-FLOAT16-feature-detection.patch

%if %{with compat_build}
BuildRequires:	clang%{maj_ver}
%else
BuildRequires:	clang
%endif
BuildRequires:	cmake
BuildRequires:	ninja-build
BuildRequires:	python3
# We need python3-devel for %%py3_shebang_fix
BuildRequires:	python3-devel
BuildRequires:	%{llvm_pkg_name}-devel = %{version}
BuildRequires:	%{llvm_pkg_name}-cmake-utils = %{version}
BuildRequires:	zlib-devel

# For gpg source verification
BuildRequires:	gnupg2

%if %{with compat_build}
Requires: clang%{maj_ver}-resource-filesystem%{?isa} = %{version}
%else
Requires: clang-resource-filesystem%{?isa} = %{version}
%endif
Provides: %{name}(major) = %{maj_ver}

%description
The compiler-rt project is a part of the LLVM project. It provides
implementation of the low-level target-specific hooks required by
code generation, sanitizer runtimes and profiling library for code
instrumentation, and Blocks C language extension.

%prep
%{gpgverify} --keyring='%{SOURCE2}' --signature='%{SOURCE1}' --data='%{SOURCE0}'
%autosetup -n %{crt_srcdir} -p2

# compiler-rt does not allow configuring LLVM_COMMON_CMAKE_UTILS.
%if %{with compat_build}
ln -s %{_libdir}/llvm%{maj_ver}/share/llvm/cmake ../cmake
%else
ln -s %{_datadir}/llvm/cmake ../cmake
%endif

%py3_shebang_fix lib/hwasan/scripts/hwasan_symbolize

%build
# Copy CFLAGS into ASMFLAGS, so -fcf-protection is used when compiling assembly files.
export ASMFLAGS=$CFLAGS

%cmake	-GNinja \
	-DCMAKE_BUILD_TYPE=RelWithDebInfo \
%if %{without compat_build}
	-DCMAKE_MODULE_PATH=%{_libdir}/cmake/llvm \
%else
	-DLLVM_CMAKE_DIR="%{_libdir}/llvm%{maj_ver}/lib/cmake/llvm" \
	-DCMAKE_CXX_COMPILER=%{_bindir}/clang++-%{maj_ver} \
	-DCMAKE_C_COMPILER=%{_bindir}/clang-%{maj_ver} \
%endif
	-DCMAKE_SKIP_RPATH:BOOL=ON \
	-DCOMPILER_RT_INSTALL_PATH=%{_prefix}/lib/clang/%{maj_ver} \
	-DLLVM_ENABLE_PER_TARGET_RUNTIME_DIR=ON \
	\
%if %{with snapshot_build}
	-DLLVM_VERSION_SUFFIX="%{llvm_snapshot_version_suffix}" \
%endif
	\
%if 0%{?__isa_bits} == 64
	-DLLVM_LIBDIR_SUFFIX=64 \
%else
	-DLLVM_LIBDIR_SUFFIX= \
%endif
	-DCOMPILER_RT_INCLUDE_TESTS:BOOL=OFF # could be on?

%cmake_build

%install

%cmake_install
%ifarch ppc64le
# Fix install path on ppc64le so that the directory name matches the triple used
# by clang.
mv %{buildroot}%{_prefix}/lib/clang/%{maj_ver}/lib/powerpc64le-redhat-linux-gnu %{buildroot}%{_prefix}/lib/clang/%{maj_ver}/lib/ppc64le-redhat-linux-gnu
%endif
%ifarch %{ix86}
# Fix install path on ix86 so that the directory name matches the triple used
# by clang on both actual ix86 and on x86_64 with -m32:
%if "%{_target_cpu}" != "i386"
ln -s i386-redhat-linux-gnu %{buildroot}%{_prefix}/lib/clang/%{maj_ver}/lib/%{_target_cpu}-redhat-linux-gnu
%endif
%endif

%check
#%%cmake_build --target check-compiler-rt

%files
%license LICENSE.TXT
%ifarch x86_64 aarch64
%{_prefix}/lib/clang/%{maj_ver}/bin/*
%endif
%{_prefix}/lib/clang/%{maj_ver}/include/*
%{_prefix}/lib/clang/%{maj_ver}/lib/*
%{_prefix}/lib/clang/%{maj_ver}/share/*
#%ifarch x86_64 aarch64
#{_bindir}/hwasan_symbolize
#%endif

%changelog
* Thu Jan 16 2025 Fedora Release Engineering <releng@fedoraproject.org> - 17.0.6-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Wed Jul 17 2024 Fedora Release Engineering <releng@fedoraproject.org> - 17.0.6-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Sat Mar 02 2024 Tom Stellard <tstellar@redhat.com> - 17.0.6-6
- Depend on clang-resource-filesystem from clang compat

* Wed Jan 24 2024 Fedora Release Engineering <releng@fedoraproject.org> - 17.0.6-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 17.0.6-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

%{?llvm_snapshot_changelog_entry}

* Mon Dec 18 2023 Jeremy Newton <alexjnewt at hotmail dot com> - 17.0.6-3
- Add compiler-rt(major) provides

* Wed Dec 13 2023 Miro Hrončok <mhroncok@redhat.com> - 17.0.6-2
- Fix install path on i686

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

* Tue Aug 29 2023 Tom Stellard <tstellar@redhat.com> - 17.0.0~rc3-2
- Fix FLOAT16 detection

* Fri Aug 25 2023 Tulio Magno Quites Machado Filho <tuliom@redhat.com> - 17.0.0~rc3-1
- Update to LLVM 17.0.0 RC3

* Wed Aug 23 2023 Tulio Magno Quites Machado Filho <tuliom@redhat.com> - 17.0.0~rc2-1
- Update to LLVM 17.0.0 RC2

* Thu Aug 03 2023 Tom Stellard <tstellar@redhat.com> - 17.0.0~rc1-2
- Fix for ppc64le

* Thu Aug 03 2023 Tulio Magno Quites Machado Filho <tuliom@redhat.com> - 17.0.0~rc1-1
- Update to LLVM 17.0.0 RC1

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 16.0.6-2
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

* Tue Mar 21 2023 Tulio Magno Quites Machado Filho <tuliom@redhat.com> - 16.0.0-1
- Update to LLVM 16.0.0

* Wed Mar 15 2023 Tulio Magno Quites Machado Filho <tuliom@redhat.com> - 16.0.0~rc4-1
- Update to LLVM 16.0.0 RC4

* Mon Mar 06 2023 Tulio Magno Quites Machado Filho <tuliom@redhat.com> - 16.0.0~rc3-2
- Fix the path of the libraries

* Thu Feb 23 2023 Tulio Magno Quites Machado Filho <tuliom@redhat.com> - 16.0.0~rc3-1
- Update to LLVM 16.0.0 RC3

* Wed Feb 15 2023 Tulio Magno Quites Machado Filho <tuliom@redhat.com> - 16.0.0~rc1-1
- Update to LLVM 16.0.0 RC1

* Wed Feb 01 2023 Tom Stellard <tstellar@redhat.com> - 15.0.7-4
- Omit frame pointers when building

* Thu Jan 19 2023 Tulio Magno Quites Machado Filho <tuliom@redhat.com> - 15.0.7-3
- Include the Apache license adopted in 2019.

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 15.0.7-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jan 13 2023 Nikita Popov <npopov@redhat.com> - 15.0.7-1
- Update to LLVM 15.0.7

* Thu Dec 15 2022 Nikita Popov <npopov@redhat.com> - 15.0.6-2
- Remove ppc64le ieeelongdouble workaround

* Tue Dec 06 2022 Nikita Popov <npopov@redhat.com> - 15.0.6-1
- Update to LLVM 15.0.6

* Mon Nov 07 2022 Nikita Popov <npopov@redhat.com> - 15.0.4-1
- Update to LLVM 15.0.4

* Fri Sep 23 2022 Nikita Popov <npopov@redhat.com> - 15.0.0-3
- Switch to building with clang

* Tue Sep 13 2022 Nikita Popov <npopov@redhat.com> - 15.0.0-2
- Make sure asm files are built with -fcf-protection

* Tue Sep 06 2022 Nikita Popov <npopov@redhat.com> - 15.0.0-1
- Update to LLVM 15.0.0

* Wed Jul 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 14.0.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon Jun 20 2022 Timm Bäder <tbaeder@redhat.com> - 14.0.5-1
- Update to 14.0.5

* Fri Apr 29 2022 Timm Bäder <tbaeder@redhat.com> - 14.0.0-2
- Remove llvm-cmake-devel BR

* Thu Mar 24 2022 Timm Bäder <tbaeder@redhat.com> - 14.0.0-1
- Update to 14.0.0

* Thu Feb 03 2022 Nikita Popov <npopov@redhat.com> - 13.0.1-1
- Update to LLVM 13.0.1 final

* Wed Jan 19 2022 Fedora Release Engineering <releng@fedoraproject.org> - 13.0.1~rc2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jan 14 2022 Nikita Popov <npopov@redhat.com> - 13.0.1~rc2-1
- Update to LLVM 13.0.1rc2

* Wed Jan 12 2022 Nikita Popov <npopov@redhat.com> - 13.0.1~rc1-1
- Update to LLVM 13.0.1rc1

* Fri Oct 01 2021 Tom Stellard <tstellar@redhat.com> - 13.0.0-1
- 13.0.0 Release

* Wed Sep 22 2021 Tom Stellard <tsellar@redhat.com> - 13.0.0~rc3-1
- 13.0.0-rc3 Release

* Mon Aug 09 2021 Tom Stellard <tstellar@redhat.com> - 13.0.0~rc1-1
- 13.0.0-rc1 Release

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 12.0.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jul 13 2021 Tom Stellard <tstellar@redhat.com> - 12.0.1
- 12.0.1 Release

* Wed Jun 30 2021 Tom Stellard <tstellar@redhat.com> - 12.0.1~rc3-1
- 12.0.1-rc3 Release

* Fri Jun 04 2021 Tom Stellard <tstellar@redhat.com> - 12.0.1~rc1-2
- Fix installation paths

* Tue Jun 01 2021 Tom Stellard <tstellar@redhat.com> - 12.0.1~rc1-1
- 12.0.1-rc1 Release

* Fri May 21 2021 sguelton@redhat.com - 12.0.0-3
- Update removal of C++ dep to follow upstream
- Backport linux/cyclade.h removal patch

* Mon May 10 2021 sguelton@redhat.com - 12.0.0-2
- Backport 82150606fb11d28813ae6

* Fri Apr 16 2021 Tom Stellard <tstellar@redhat.com> - 12.0.0-1
- 12.0.0 Release

* Thu Apr 08 2021 sguelton@redhat.com - 12.0.0-0.6.rc5
- New upstream release candidate

* Fri Apr 02 2021 sguelton@redhat.com - 12.0.0-0.5.rc4
- New upstream release candidate

* Thu Mar 11 2021 sguelton@redhat.com - 12.0.0-0.4.rc3
- LLVM 12.0.0 rc3

* Tue Mar 09 2021 sguelton@redhat.com - 12.0.0-0.3.rc2
- rebuilt

* Thu Feb 25 2021 Serge Guelton - 12.0.0-0.2.rc2
- 12.0.0-rc2 release

* Tue Feb 16 2021 Serge Guelton - 12.0.0-0.1.rc1
- 12.0.0-rc1 release

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 11.1.0-0.3.rc2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Fri Jan 22 2021 Serge Guelton - 11.1.0-0.2.rc2
- 11.1.0-rc2 release

* Thu Jan 14 2021 Serge Guelton - 11.1.0-0.1.rc1
- 11.1.0-rc1 release

* Wed Jan 06 2021 Serge Guelton - 11.0.1-3
- LLVM 11.0.1 final

* Tue Dec 22 2020 sguelton@redhat.com - 11.0.1-2.rc2
- llvm 11.0.1-rc2

* Tue Dec 01 2020 sguelton@redhat.com - 11.0.1-1.rc1
- llvm 11.0.1-rc1

* Thu Oct 29 2020 Tom Stellard <tstellar@redhat.com> - 11.0.0-2
- Add dependency on clang-resource-filesystem

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
- 11.0.0-rc2 Release

* Mon Aug 10 2020 Tom Stellard <tstellar@redhat.com> - 11.0.0-0.1.rc1
- 11.0.0-rc1 Release

* Wed Jul 29 2020 sguelton@redhat.com - 10.0.0-9
- use %%license macro

* Mon Jul 27 2020 sguelton@redhat.com - 10.0.0-8
- Remove now obsolete debuginfo package limitation

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 10.0.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Jul 20 2020 sguelton@redhat.com - 10.0.0-6
- Use modern cmake macros

* Wed Jul 15 2020 sguelton@redhat.com - 10.0.0-5
- Fix multilib runtime links, see rhbz#1855379

* Wed Jul 15 2020 sguelton@redhat.com - 10.0.0-4
- Correctly use gpg verification

* Thu Jul 09 2020 Tom Stellard <tstellar@redhat.com> - 10.0.0-3
- Drop dependency on llvm-static

* Thu Jun 11 2020 sguelton@redhat.com - 10.0.0-2
- Fix msan compilation warnings, see af38074874c605f9 upstream

* Mon Mar 30 2020 sguelton@redhat.com - 10.0.0-1
- 10.0.0 final

* Wed Mar 25 2020 sguelton@redhat.com - 10.0.0-0.6.rc6
- 10.0.0 rc6

* Fri Mar 20 2020 sguelton@redhat.com - 10.0.0-0.5.rc5
- 10.0.0 rc5

* Sun Mar 15 2020 sguelton@redhat.com - 10.0.0-0.4.rc4
- 10.0.0 rc4

* Thu Mar 5 2020 sguelton@redhat.com - 10.0.0-0.3.rc3
- 10.0.0 rc3

* Fri Feb 14 2020 sguelton@redhat.com - 10.0.0-0.1.rc2
- 10.0.0 rc2

* Wed Feb 12 2020 sguelton@redhat.com - 10.0.0-0.2.rc1
- Ship blacklist files in the proper directory, see rhbz#1794936

* Fri Jan 31 2020 sguelton@redhat.com - 10.0.0-0.1.rc1
- 10.0.0 rc1

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 9.0.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Sep 19 2019 Tom Stellard <tstellar@redhat.com> - 9.0.0-1
- 9.0.0 Release

* Thu Aug 22 2019 Tom Stellard <tstellar@redhat.com> - 9.0.0-0.1.rc3
- 9.0.0-rc3 Release

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 8.0.0-2.1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Tue Jun 18 2019 sguelton@redhat.com - 8.0.0-2
- Fix rhbz#1678240

* Wed Mar 20 2019 sguelton@redhat.com - 8.0.0-1
- 8.0.0 final

* Tue Mar 12 2019 sguelton@redhat.com - 8.0.0-0.4.rc4
- 8.0.0 Release candidate 4

* Mon Mar 4 2019 sguelton@redhat.com - 8.0.0-0.3.rc3
- 8.0.0 Release candidate 3

* Fri Feb 22 2019 sguelton@redhat.com - 8.0.0-0.2.rc2
- 8.0.0 Release candidate 2

* Mon Feb 11 2019 sguelton@redhat.com - 8.0.0-0.1.rc1
- 8.0.0 Release candidate 1

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 7.0.1-2.1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jan 18 2019 sguelton@redhat.com - 7.0.1-2
- GCC-9 compatibility

* Mon Dec 17 2018 sguelton@redhat.com - 7.0.1-1
- 7.0.1 Release

* Tue Dec 04 2018 sguelton@redhat.com - 7.0.0-2
- Ensure rpmlint passes on specfile

* Mon Sep 24 2018 Tom Stellard <tstellar@redhat.com> - 7.0.0-1
- 7.0.0-1 Release

* Wed Sep 12 2018 Tom Stellard <tstellar@redhat.com> - 7.0.0-0.4.rc3
- 7.0.0-rc3 Release

* Fri Sep 07 2018 Tom Stellard <tstellar@redhat.com> - 7.0.0-0.3.rc1
- Use python3 for build scripts

* Thu Sep 06 2018 Tom Stellard <tstellar@redhat.com> - 7.0.0-0.2.rc1
- Drop BuildRequires: python2

* Tue Aug 14 2018 Tom Stellard <tstellar@redhat.com> - 7.0.0-0.1.rc1
- 7.0.0-rc1 Release

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 6.0.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Jun 28 2018 Tom Stellard <tstellar@redhat.com> - 6.0.1-1
- 6.0.1 Release

* Mon Mar 19 2018 Iryna Shcherbina <ishcherb@redhat.com> - 6.0.0-2
- Update Python 2 dependency declarations to new packaging standards
  (See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3)

* Thu Mar 08 2018 Tom Stellard <tstellar@redhat.com> - 6.0.0-1
- 6.0.0 Release

* Tue Feb 13 2018 Tom Stellard <tstellar@redhat.com> - 6.0.0-0.4.rc2
- 6.0.0-rc2 Release

* Tue Feb 13 2018 Tom Stellard <tstellar@redhat.com> - 6.0.0-0.3.rc1
- Fix build on AArch64

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 6.0.0-0.2.rc1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jan 25 2018 Tom Stellard <tstellar@redhat.com> - 6.0.0-0.1.rc1
- 6.0.0-rc1 Release

* Wed Jan 17 2018 Tom Stellard <tstellar@redhat.com> - 5.0.1-2
- Build libFuzzer with gcc

* Wed Dec 20 2017 Tom Stellard <tstellar@redhat.com> - 5.0.1-1
- 5.0.1 Release

* Fri Oct 13 2017 Tom Stellard <tstellar@redhat.com> - 5.0.0-1
- 5.0.0 Release

* Mon Sep 25 2017 Tom Stellard <tstellar@redhat.com> - 4.0.1-6
- Fix AArch64 build with glibc 2.26

* Tue Sep 12 2017 Tom Stellard <tstellar@redhat.com> - 4.0.1-5
- Package libFuzzer

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 4.0.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 4.0.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Jun 23 2017 Tom Stellard <tstelar@redhat.com> - 4.0.1-2
- Fix build with newer glibc

* Fri Jun 23 2017 Tom Stellard <tstellar@redhat.com> - 4.0.1-1
- 4.0.1 Release

* Tue Mar 14 2017 Tom Stellard <tstellar@redhat.com> - 4.0.0-1
- compiler-rt 4.0.0 Final Release

* Thu Mar 02 2017 Dave Airlie <airlied@redhat.com> - 3.9.1-1
- compiler-rt 3.9.1

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.9.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Nov 21 2016 Dan Horák <dan[at]danny.cz> - 3.9.0-3
- disable debuginfo on s390(x)

* Wed Nov 02 2016 Dave Airlie <airlied@redhat.com> - 3.9.0-2
- build for new arches.

* Wed Oct 26 2016 Dave Airlie <airlied@redhat.com> - 3.9.0-1
- compiler-rt 3.9.0 final release

* Mon May  2 2016 Tom Callaway <spot@fedoraproject.org> 3.8.0-2
- make symlinks to where the linker thinks these libs are

* Thu Mar 10 2016 Dave Airlie <airlied@redhat.com> 3.8.0-1
- compiler-rt 3.8.0 final release

* Thu Mar 03 2016 Dave Airlie <airlied@redhat.com> 3.8.0-0.2
- compiler-rt 3.8.0rc3

* Thu Feb 18 2016 Dave Airlie <airlied@redhat.com> - 3.8.0-0.1
- compiler-rt 3.8.0rc2

* Fri Feb 05 2016 Dave Airlie <airlied@redhat.com> 3.7.1-3
- fix compiler-rt paths - from rwindz0@gmail.com - #1304605

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 3.7.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Tue Oct 06 2015 Jan Vcelak <jvcelak@fedoraproject.org> 3.7.0-100
- initial version using cmake build system
