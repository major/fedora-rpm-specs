%global toolchain clang
%global libcxxabi_version 15.0.0
#global rc_ver 3
%global libcxxabi_srcdir libcxxabi-%{libcxxabi_version}%{?rc_ver:rc%{rc_ver}}.src


Name:		libcxxabi
Version:	%{libcxxabi_version}%{?rc_ver:~rc%{rc_ver}}
Release:	2%{?dist}
Summary:	Low level support for a standard C++ library
License:	MIT or NCSA
URL:		http://libcxxabi.llvm.org/
Source0:	https://github.com/llvm/llvm-project/releases/download/llvmorg-%{libcxxabi_version}%{?rc_ver:-rc%{rc_ver}}/%{libcxxabi_srcdir}.tar.xz
Source1:	https://github.com/llvm/llvm-project/releases/download/llvmorg-%{libcxxabi_version}%{?rc_ver:-rc%{rc_ver}}/%{libcxxabi_srcdir}.tar.xz.sig
Source2:	release-keys.asc

Patch0:		0001-PATCH-libcxxabi-Include-refstring.h-from-system-incl.patch
Patch1:		0001-Fixup-libcxx-include-path.patch

BuildRequires:	clang llvm-devel cmake llvm-static ninja-build
BuildRequires:	libcxx-devel >= %{version}
%if 0%{?rhel}
# libcxx-devel has this, so we need to as well.
ExcludeArch:	ppc64 ppc64le
%endif

# For origin certification
BuildRequires:	gnupg2

%description
libcxxabi provides low level support for a standard C++ library.

%package devel
Summary:	Headers and libraries for libcxxabi devel
Requires:	%{name}%{?_isa} = %{version}-%{release}

%description devel
%{summary}.

%package static
Summary:	Static libraries for libcxxabi

%description static
%{summary}.

%prep
%{gpgverify} --keyring='%{SOURCE2}' --signature='%{SOURCE1}' --data='%{SOURCE0}'
%autosetup -n %{libcxxabi_srcdir} -p2

%build
%ifarch armv7hl
# Disable LTO on ARM. bfd crashes during some of the CMake compiler checks with:
# /usr/bin/ld: BFD version 2.35-10.fc33 internal error, aborting at elfcode.h:224 in bfd_elf32_swap_symbol_out
%global _lto_cflags %{nil}
# disable ARM exception handling
sed -i 's|#define _LIBCXXABI_ARM_EHABI||g' include/__cxxabi_config.h
%endif

%ifarch s390 s390x
%if 0%{?fedora} < 26
# clang requires z10 at minimum
# workaround until we change the defaults for Fedora
%global optflags %(echo %{optflags} | sed 's/-march=z9-109 /-march=z10 /')
%endif
%endif

%cmake	-GNinja \
	-DCMAKE_C_COMPILER=/usr/bin/clang \
	-DCMAKE_CXX_COMPILER=/usr/bin/clang++ \
	-DCMAKE_MODULE_PATH=%{_libdir}/cmake/llvm \
	-DLIBCXXABI_LIBCXX_INCLUDES=%{_includedir}/c++/v1/ \
%if 0%{?__isa_bits} == 64
	-DLIBCXXABI_LIBDIR_SUFFIX:STRING=64 \
%endif
	-DCMAKE_BUILD_TYPE=RelWithDebInfo


%cmake_build

%install
%cmake_install

%ldconfig_scriptlets

%files
%license LICENSE.TXT
%doc CREDITS.TXT
%{_libdir}/libc++abi.so.*

%files devel
%{_includedir}/c++/v1/*.h
%{_libdir}/libc++abi.so

%files static
%{_libdir}/libc++abi.a

%changelog
* Mon Sep 12 2022 Nikita Popov <npopov@redhat.com> - 15.0.0-2
- Don't pass explicit CMAKE_CXX_FLAGS

* Tue Sep 06 2022 Nikita Popov <npopov@redhat.com> - 15.0.0-1
- Update to LLVM 15.0.0

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 14.0.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon Jun 20 2022 Timm Bäder <tabeder@redhat.com> - 14.0.5-1
- Update to 14.0.5

* Fri Apr 29 2022 Timm Bäder <tbaeder@redhat.com> - 14.0.0-2
- Remove llvm-cmake-devel BR

* Thu Mar 24 2022 Timm Bäder <tbaeder@redhat.com> - 14.0.0-1
- Update to 14.0.0

* Thu Feb 03 2022 Nikita Popov <npopov@redhat.com> - 13.0.1-1
- Update to LLVM 13.0.1 final

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 13.0.1~rc2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jan 14 2022 Nikita Popov <npopov@redhat.com> - 13.0.1~rc2-1
- Update to LLVM 13.0.1rc2

* Wed Jan 12 2022 Nikita Popov <npopov@redhat.com> - 13.0.1~rc1-1
- Update to LLVM 13.0.1rc1

* Fri Oct 01 2021 Tom Stellard <tstellar@redhat.com> - 13.0.0-1
- 13.0.0 Release

* Mon Aug 09 2021 Tom Stellard <tstellar@redhat.com> - 13.0.0~rc1-1
- 13.0.0-rc1 Release

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 12.0.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jul 13 2021 Tom Stellard <tstellar@redhat.com> - 12.0.1-1
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

* Tue Mar 09 2021 sguelton@redhat.com - 12.0.0-0.3.rc2
- rebuilt

* Wed Feb 24 2021 sguelton@redhat.com - 12.0.0-0.2.rc2
- 12.0.0-rc2 release

* Wed Feb 17 2021 Tom Stellard <tstellar@redhat.com> - 12.0.0-0.1.rc1
- 12.0.0-rc1 Release

* Wed Feb 03 2021 Timm Bäder <tbaeder@redhat.com> - 11.1.0-0.4.rc2
- Fix passing the llvm config

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

* Tue Aug 11 2020 Tom Stellard <tstellar@redhat.com> - 11.0.0-0.1.rc1
- 11.0.0-rc1 Release

* Thu Aug 06 2020 Jeff Law <law@redhat.com> - 10.0.0-5
- Set toolchain to clang

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 10.0.0-4
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 10.0.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Jul 20 2020 sguelton@redhat.com - 10.0.0-2
- Use modern cmake macro
- Finalize source verification

* Tue Mar 31 2020 sguelton@redhat.com - 10.0.0-1
- 10.0.0 final

* Wed Mar 25 2020 sguelton@redhat.com - 10.0.0-0.5.rc6
- 10.0.0 rc6

* Sat Mar 21 2020 sguelton@redhat.com - 10.0.0-0.4.rc5
- 10.0.0 rc5

* Sun Mar 15 2020 sguelton@redhat.com - 10.0.0-0.3.rc4
- 10.0.0 rc4

* Thu Mar 05 2020 sguelton@redhat.com - 10.0.0-0.2.rc3
- 10.0.0 rc3

* Fri Feb 14 2020 sguelton@redhat.com - 10.0.0-0.1.rc2
- 10.0.0 rc2

* Fri Jan 31 2020 sguelton@redhat.com - 10.0.0-0.1.rc1
- 10.0.0 rc1

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 9.0.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jan 16 2020 Tom Stellard <tstellar@redhat.com> - 9.0.1-1
- 9.0.1 Release

* Mon Sep 23 2019 Tom Stellard <tstellar@redhat.com> - 9.0.0-1
- 9.0.0 Release

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 8.0.0-1.1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Mon Mar 25 2019 sguelton@redhat.com - 8.0.0-1
- 8.0.0 Release

* Tue Mar 12 2019 sguelton@redhat.com - 8.0.0-0.4.rc4
- 8.0.0 Release candidate 4

* Mon Mar 4 2019 sguelton@redhat.com - 8.0.0-0.3.rc3
- 8.0.0 Release candidate 3

* Sun Feb 24 2019 sguelton@redhat.com - 8.0.0-0.2.rc2
- 8.0.0 Release candidate 2

* Mon Feb 11 2019 sguelton@redhat.com - 8.0.0-0.1.rc1
- 8.0.0 Release candidate 1

* Wed Feb  6 2019 Tom Callaway <spot@fedoraproject.org> - 7.0.1-2
- remove -fstack-clash-protection

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 7.0.1-1.1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Mon Dec 17 2018 sguelton@redhat.com - 7.0.1-1
- 7.0.1 Release

* Mon Dec 10 2018 sguelton@redhat.com - 7.0.1-0.1.rc3
- 7.0.1-rc3 Release

* Tue Dec 04 2018 sguelton@redhat.com - 7.0.0-2
- Ensure rpmlint passes on specfile

* Tue Sep 25 2018 Tom Stellard <tstellar@redhat.com> - 7.0.0-1
- 7.0.0 Release

* Wed Sep 12 2018 Tom Stellard <tstellar@redhat.com> - 7.0.0-0.1.rc3
- 7.0.0-rc3 Release

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 6.0.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 26 2018 Tom Callaway <spot@fedoraproject.org> - 6.0.1-1
- update to 6.0.1

* Wed Mar 21 2018 Tom Stellard <tstellar@redhat.com> - 6.0.0-2
- Use default LDFLAGS/CXXFLAGS/CFLAGS and filter out flags not supported by
  clang

* Wed Mar 14 2018 Tom Callaway <spot@fedoraproject.org> - 6.0.0-1
- update to 6.0.0 final

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 6.0.0-0.2.rc1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Dec 21 2017 Tom Stellard <tstellar@redhat.com> - 6.0.0-0.1.rc1
- 6.0.1-rc1 Release

* Thu Dec 21 2017 Tom Stellard <tstellar@redhat.com> - 5.0.1-1
- 5.0.1 Release

* Tue Dec 19 2017 Tom Stellard <tstellar@redhat.com> - 5.0.0-2
- Fix disabling of ARM exception handling

* Fri Sep  8 2017 Tom Callaway <spot@fedoraproject.org> - 5.0.0-1
- update to 5.0.0

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 4.0.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 4.0.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Jun 23 2017 Tom Callaway <spot@fedoraproject.org> - 4.0.1-1
- update to 4.0.1

* Sat Apr 22 2017 Tom Callaway <spot@fedoraproject.org> - 4.0.0-1
- update to 4.0.0

* Mon Feb 20 2017 Tom Callaway <spot@fedoraproject.org> - 3.9.0-1
- update to 3.9.0
- apply fixes from libcxx

* Wed Sep  7 2016 Tom Callaway <spot@fedoraproject.org> - 3.8.1-1
- update to 3.8.1

* Mon Jul 25 2016 Tom Callaway <spot@fedoraproject.org> - 3.8.0-2
- make static subpackage

* Tue May 3 2016 Tom Callaway <spot@fedoraproject.org> - 3.8.0-1
- initial package
