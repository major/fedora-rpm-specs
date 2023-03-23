%global toolchain clang

# Opt out of https://fedoraproject.org/wiki/Changes/fno-omit-frame-pointer
# https://bugzilla.redhat.com/show_bug.cgi?id=2158587
%undefine _include_frame_pointers

%global maj_ver 16
%global libomp_version %{maj_ver}.0.0
#global rc_ver 4
%global libomp_srcdir openmp-%{libomp_version}%{?rc_ver:rc%{rc_ver}}.src
%global cmake_srcdir cmake-%{libomp_version}%{?rc_ver:rc%{rc_ver}}.src


%ifarch ppc64le
%global libomp_arch ppc64
%else
%global libomp_arch %{_arch}
%endif

Name: libomp
Version: %{libomp_version}%{?rc_ver:~rc%{rc_ver}}
Release: 1%{?dist}
Summary: OpenMP runtime for clang

License: Apache-2.0 WITH LLVM-exception OR NCSA
URL: http://openmp.llvm.org
Source0: https://github.com/llvm/llvm-project/releases/download/llvmorg-%{libomp_version}%{?rc_ver:-rc%{rc_ver}}/%{libomp_srcdir}.tar.xz
Source1: https://github.com/llvm/llvm-project/releases/download/llvmorg-%{libomp_version}%{?rc_ver:-rc%{rc_ver}}/%{libomp_srcdir}.tar.xz.sig
Source2: release-keys.asc
Source3: run-lit-tests
Source4: lit.fedora.cfg.py
Source5:	https://github.com/llvm/llvm-project/releases/download/llvmorg-%{libomp_version}%{?rc_ver:-rc%{rc_ver}}/%{cmake_srcdir}.tar.xz
Source6:	https://github.com/llvm/llvm-project/releases/download/llvmorg-%{libomp_version}%{?rc_ver:-rc%{rc_ver}}/%{cmake_srcdir}.tar.xz.sig

BuildRequires: clang
# For clang-offload-packager
BuildRequires: clang-tools-extra
BuildRequires: cmake
BuildRequires: ninja-build
BuildRequires: elfutils-libelf-devel
BuildRequires: perl
BuildRequires: perl-Data-Dumper
BuildRequires: perl-Encode
BuildRequires: libffi-devel

# For gpg source verification
BuildRequires:	gnupg2

# libomptarget needs the llvm cmake files
BuildRequires: llvm-devel

Requires: elfutils-libelf%{?isa}

# libomp does not support s390x.
ExcludeArch: s390x

%description
OpenMP runtime for clang.

%package devel
Summary: OpenMP header files
Requires: %{name}%{?isa} = %{version}-%{release}
Requires: clang-resource-filesystem%{?isa} = %{version}

%description devel
OpenMP header files.

%package test
Summary: OpenMP regression tests
Requires: %{name}%{?isa} = %{version}-%{release}
Requires: %{name}-devel%{?isa} = %{version}-%{release}
Requires: clang
Requires: llvm
Requires: python3-lit

%description test
OpenMP regression tests

%prep
%{gpgverify} --keyring='%{SOURCE2}' --signature='%{SOURCE1}' --data='%{SOURCE0}'
%{gpgverify} --keyring='%{SOURCE2}' --signature='%{SOURCE6}' --data='%{SOURCE5}'
%setup -T -q -b 5 -n %{cmake_srcdir}
# TODO: It would be more elegant to set -DLLVM_COMMON_CMAKE_UTILS=%{_builddir}/%{cmake_srcdir},
# but this is not a CACHED variable, so we can't actually set it externally :(
cd ..
mv %{cmake_srcdir} cmake
%autosetup -n %{libomp_srcdir} -p2

%build
# TODO: LIBOMP_HAVE_VERSION_SCRIPT_FLAG should be set automatically.
%cmake	-GNinja \
	-DLIBOMP_INSTALL_ALIASES=OFF \
	-DCMAKE_MODULE_PATH=%{_libdir}/cmake/llvm \
	-DLLVM_DIR=%{_libdir}/cmake/llvm \
	-DCMAKE_INSTALL_INCLUDEDIR=%{_libdir}/clang/%{maj_ver}/include \
%if 0%{?__isa_bits} == 64
	-DOPENMP_LIBDIR_SUFFIX=64 \
%else
	-DOPENMP_LIBDIR_SUFFIX= \
%endif
	-DCMAKE_SKIP_RPATH:BOOL=ON \
	-DLIBOMP_HAVE_VERSION_SCRIPT_FLAG:BOOL=ON

%cmake_build


%install
%cmake_install

# Test package setup
%global libomp_srcdir %{_datadir}/libomp/src/
%global libomp_testdir %{libomp_srcdir}/runtime/test/
%global lit_cfg %{libomp_testdir}/%{_arch}.site.cfg.py
%global lit_fedora_cfg %{_datadir}/libomp/lit.fedora.cfg.py

install -d %{buildroot}%{libomp_srcdir}/runtime
cp -R runtime/test  %{buildroot}%{libomp_srcdir}/runtime
cp -R runtime/src  %{buildroot}%{libomp_srcdir}/runtime

# Generate lit config files.  Strip off the last line that initiates the
# test run, so we can customize the configuration.
head -n -1 %{_vpath_builddir}/runtime/test/lit.site.cfg >> %{buildroot}%{lit_cfg}

# Install custom fedora config file
cp %{SOURCE4} %{buildroot}%{lit_fedora_cfg}

# Patch lit config files to load custom fedora config
echo "lit_config.load_config(config, '%{lit_fedora_cfg}')" >> %{buildroot}%{lit_cfg}

# Install test script
install -d %{buildroot}%{_libexecdir}/tests/libomp
install -m 0755 %{SOURCE3} %{buildroot}%{_libexecdir}/tests/libomp

# Remove static libraries with equivalent shared libraries
rm -rf %{buildroot}%{_libdir}/libarcher_static.a

%check
%cmake_build --target check-openmp

%files
%license LICENSE.TXT
%{_libdir}/libomp.so
%{_libdir}/libompd.so
%ifnarch %{arm}
%{_libdir}/libarcher.so
%endif
%ifnarch %{ix86} %{arm}
# libomptarget is not supported on 32-bit systems.
%{_libdir}/libomptarget.rtl.amdgpu.so.%{maj_ver}
%{_libdir}/libomptarget.rtl.amdgpu.nextgen.so.%{maj_ver}
%{_libdir}/libomptarget.rtl.cuda.so.%{maj_ver}
%{_libdir}/libomptarget.rtl.cuda.nextgen.so.%{maj_ver}
%{_libdir}/libomptarget.rtl.%{libomp_arch}.so.%{maj_ver}
%{_libdir}/libomptarget.rtl.%{libomp_arch}.nextgen.so.%{maj_ver}
%{_libdir}/libomptarget.so.%{maj_ver}
%endif

%files devel
%{_libdir}/clang/%{maj_ver}/include/omp.h
%{_libdir}/cmake/openmp/FindOpenMPTarget.cmake
%ifnarch %{arm}
%{_libdir}/clang/%{maj_ver}/include/omp-tools.h
%{_libdir}/clang/%{maj_ver}/include/ompt.h
%{_libdir}/clang/%{maj_ver}/include/ompt-multiplex.h
%endif
%ifnarch %{ix86} %{arm}
# libomptarget is not supported on 32-bit systems.
%{_libdir}/libomptarget.rtl.amdgpu.so
%{_libdir}/libomptarget.rtl.amdgpu.nextgen.so
%{_libdir}/libomptarget.rtl.cuda.so
%{_libdir}/libomptarget.rtl.cuda.nextgen.so
%{_libdir}/libomptarget.rtl.%{libomp_arch}.so
%{_libdir}/libomptarget.rtl.%{libomp_arch}.nextgen.so
%{_libdir}/libomptarget.devicertl.a
%{_libdir}/libomptarget-amdgpu-*.bc
%{_libdir}/libomptarget-nvptx-*.bc
%{_libdir}/libomptarget.so
%endif

%files test
%{_datadir}/libomp
%{_libexecdir}/tests/libomp/

%changelog
* Tue Mar 21 2023 Tulio Magno Quites Machado Filho <tuliom@redhat.com> - 16.0.0-1
- Update to LLVM 16.0.0

* Wed Mar 15 2023 Tulio Magno Quites Machado Filho <tuliom@redhat.com> - 16.0.0~rc4-1
- Update to LLVM 16.0.0 RC4

* Thu Feb 23 2023 Tulio Magno Quites Machado Filho <tuliom@redhat.com> - 16.0.0~rc3-1
- Update to LLVM 16.0.0 RC3

* Tue Feb 14 2023 Tulio Magno Quites Machado Filho <tuliom@redhat.com> - 16.0.0~rc1-1
- Update to LLVM 16.0.0 RC1

* Tue Jan 31 2023 Tulio Magno Quites Machado Filho <tuliom@redhat.com> - 15.0.7-5
- Include the Apache license adopted in 2019.

* Fri Jan 20 2023 Tom Stellard <tstellar@redhat.com> - 15.0.7-4
- Omit frame pointers when building

* Fri Jan 20 2023 Nikita Popov <npopov@redhat.com> - 15.0.7-3
- Fix build against GCC 13

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 15.0.7-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jan 13 2023 Nikita Popov <npopov@redhat.com> - 15.0.7-1
- Update to LLVM 15.0.7

* Tue Dec 06 2022 Nikita Popov <npopov@redhat.com> - 15.0.6-1
- Update to LLVM 15.0.6

* Mon Nov 07 2022 Nikita Popov <npopov@redhat.com> - 15.0.4-1
- Update to LLVM 15.0.4

* Mon Sep 12 2022 Nikita Popov <npopov@redhat.com> - 15.0.0-3
- Re-enable LTO build

* Mon Sep 12 2022 Nikita Popov <npopov@redhat.com> - 15.0.0-2
- Add explicit requires from libomp-devel to libomp

* Tue Sep 06 2022 Nikita Popov <npopov@redhat.com> - 15.0.0-1
- Update to LLVM 15.0.0

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 14.0.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon Jun 20 2022 Timm Bäder <tbaeder@redhat.com> - 14.0.5-1
- 14.0.5 Release

* Thu Mar 24 2022 Timm Bäder <tbaeder@redhat.com> - 14.0.0-1
- 14.0.0 Release

* Thu Feb 03 2022 Nikita Popov <npopov@redhat.com> - 13.0.1-1
- Update to LLVM 13.0.1 final

* Tue Jan 25 2022 Nikita Popov <npopov@redhat.com> - 13.0.1~rc3-2
- Update to LLVM 13.0.1rc3

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 13.0.1~rc2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jan 13 2022 Nikita Popov <npopov@redhat.com> - 13.0.1~rc2-1
- Update to LLVM 13.0.1rc2

* Mon Jan 10 2022 Nikita Popov <npopov@redhat.com> - 13.0.1~rc1-1
- Update to LLVM 13.0.1rc1

* Sat Jan 08 2022 Miro Hrončok <mhroncok@redhat.com> - 13.0.0-2
- Rebuilt for https://fedoraproject.org/wiki/Changes/LIBFFI34

* Mon Oct 04 2021 Tom Stellard <tstellar@redhat.com> - 13.0.0-1
- 13.0.0 Release

* Tue Sep 21 2021 Tom Stellard <tstellar@redhat.com> - 13.0.0~rc3-1
- 13.0.0-rc3 Release

* Mon Aug 09 2021 Tom Stellard <tstellar@redhat.com> - 13.0.0~rc1-1
- 13.0.0-rc1 Release

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 12.0.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jul 13 2021 Tom Stellard <tstellar@redhat.com> - 12.0.1-1
- 12.0.1 Release

* Thu Jul 01 2021 Tom Stellard <tstellar@redhat.com> - 12.0.1~rc3-1
- Fix install path

* Fri Jun 04 2021 Tom Stellard <tstellar@redhat.com> - 12.0.1~rc1-2
- Fix install path

* Tue Jun 01 2021 Tom Stellard <tstellar@redhat.com> - 12.0.1~rc1-1
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

* Tue Mar 09 2021 sguelton@redhat.com - 12.0.0-0.3.rc2
- rebuilt

* Wed Feb 24 2021 sguelton@redhat.com - 12.0.0-0.2.rc2
- 12.0.0-rc2 release

* Mon Feb 22 2021 sguelton@redhat.com - 12.0.0-0.1.rc1
- 12.0.0-rc1 release

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

* Wed Oct 28 2020 Tom Stellard <tstellar@redhat.com> - 11.0.0-2
- Replace clang-devel dependency with clang-resource-filesystem

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

* Mon Aug 10 2020 sguelton@redhat.com - 10.0.0-8
- Make gcc dependency explicit, see https://fedoraproject.org/wiki/Packaging:C_and_C%2B%2B#BuildRequires_and_Requires
- use %%license macro

* Sat Aug 08 2020 Jeff Law <releng@fedoraproject.org> - 10.0.0-7
- Disable LTO for now

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 10.0.0-6
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 10.0.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Jul 20 2020 sguelton@redhat.com - 10.0.0-4
- Use modern cmake macro
- Use gnupg verify

* Tue Jun 16 2020 sguelton@redhat.com - 10.0.0-3
- Add Requires: libomp = %%{version}-%%{release} to libomp-test to avoid
  the need to test interoperability between the various combinations of old
  and new subpackages.

* Mon Jun 01 2020 sguelton@redhat.com - 10.0.0-2
- Add Requires: libomp-devel = %%{version}-%%{release} to libomp-test to avoid
  the need to test interoperability between the various combinations of old
  and new subpackages.

* Mon Mar 30 2020 sguelton@redhat.com - 10.0.0-1
- 10.0.0 final

* Wed Mar 25 2020 sguelton@redhat.com - 10.0.0-0.6.rc6
- 10.0.0 rc6

* Fri Mar 20 2020 sguelton@redhat.com - 10.0.0-0.5.rc5
- 10.0.0 rc5

* Sun Mar 15 2020 sguelton@redhat.com - 10.0.0-0.4.rc4
- 10.0.0 rc4

* Thu Mar 05 2020 sguelton@redhat.com - 10.0.0-0.3.rc3
- 10.0.0 rc3

* Fri Feb 14 2020 sguelton@redhat.com - 10.0.0-0.2.rc2
- 10.0.0 rc2

* Fri Jan 31 2020 sguelton@redhat.com - 10.0.0-0.1.rc1
- 10.0.0 rc1

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 9.0.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Dec 19 2019 Tom Stellard <tstellar@redhat.com> - 9.0.1-1
- 9.0.1 Release

* Thu Sep 19 2019 Tom Stellard <tstellar@redhat.com> - 9.0.0-1
- 9.0.0 Release

* Thu Aug 22 2019 Tom Stellard <tstellar@redhat.com> - 9.0.0-0.1.rc3
- 9.0.0-rc3 Release

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 8.0.0-2.1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Apr 25 2019 Tom Stellard <tstellar@redhat.com> - 8.0.0-2
- Simplify libomp-test package

* Wed Mar 20 2019 sguelton@redhat.com - 8.0.0-1
- 8.0.0 final

* Tue Mar 12 2019 sguelton@redhat.com - 8.0.0-0.3.rc4
- 8.0.0 Release candidate 4

* Mon Feb 11 2019 sguelton@redhat.com - 8.0.0-0.2.rc2
- 8.0.0 Release candidate 2

* Mon Feb 11 2019 sguelton@redhat.com - 8.0.0-0.1.rc1
- 8.0.0 Release candidate 1

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 7.0.1-1.1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Mon Dec 17 2018 sguelton@redhat.com - 7.0.1-1
- 7.0.1 Release

* Wed Sep 12 2018 Tom Stellard <tstellar@redhat.com> - 7.0.0-1
- 7.0.1 Release

* Wed Sep 12 2018 Tom Stellard <tstellar@redhat.com> - 7.0.0-0.2.rc3
- 7.0.0-rc3 Release

* Tue Aug 14 2018 Tom Stellard <tstellar@redhat.com> - 7.0.0-0.1.rc1
- 7.0.1-rc1 Release

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 6.0.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Mon Jul 02 2018 Tom Stellard <tstellar@redhat.com> - 6.0.1-2
- Add -threads option to runtest.sh

* Thu Jun 28 2018 Tom Stellard <tstellar@redhat.com> - 6.0.1-1
- 6.0.1 Release

* Fri May 11 2018 Tom Stellard <tstellar@redhat.com> - 6.0.0-0.1.rc1
- 6.0.1-rc1 Release

* Wed Mar 28 2018 Tom Stellard <tstellar@redhat.com> - 6.0.0-3
- Add test package

* Wed Mar 28 2018 Tom Stellard <tstellar@redhat.com> - 6.0.0-2
- Enable libomptarget plugins

* Fri Mar 09 2018 Tom Stellard <tstellar@redhat.com> - 6.0.0-1
- 6.0.0 Release

* Tue Feb 13 2018 Tom Stellard <tstellar@redhat.com> - 6.0.0-0.3.rc2
- 6.0.0-rc2 Release

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 6.0.0-0.2.rc1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jan 25 2018 Tom Stellard <tstellar@redhat.com> - 6.0.0-0.1.rc1
- 6.0.0-rc1 Release

* Thu Dec 21 2017 Tom Stellard <tstellar@redhat.com> - 5.0.1-1
- 5.0.1 Release.

* Mon May 15 2017 Tom Stellard <tstellar@redhat.com> - 5.0.0-1
- Initial version.
