Name:           libcxl
Version:        1.7
Release:        17%{?dist}
Summary:        Coherent accelerator interface
License:        Apache-2.0
URL:            https://github.com/ibm-capi/libcxl
Source0:        https://github.com/ibm-capi/libcxl/archive/v%{version}.tar.gz
Patch1:         remove_2_backslashes_in_shell_call.patch
ExclusiveArch:  %{power64}
BuildRequires:  gcc
BuildRequires: make

%description
The coherent accelerator interface is designed to allow the coherent
connection of accelerators (FPGAs and other devices) to a POWER system.
Coherent in this context means that the accelerator and CPUs can both access
system memory directly and with the same effective addresses. IBM refers to
this as the Coherent Accelerator Processor Interface (CAPI). In the Linux
world it is referred to by the name CXL to avoid confusion with the ISDN
CAPI subsystem.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
The %{name}-devel package contains header file and man pages for
developing applications that use %{name}.


%prep
%setup -q
%patch 1 -p1

%build
%make_build
mkdir -p build/man3
cp -p man3/*.3 build/man3

%install
%make_install prefix=/usr
mkdir -p $RPM_BUILD_ROOT%{_mandir}
cp -a build/man3 $RPM_BUILD_ROOT%{_mandir}/

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%files
%license LICENSE
%doc README.md
%{_libdir}/libcxl.so.*

%files devel
%{_includedir}/*
%{_mandir}/man3/*
%{_libdir}/libcxl.so

%changelog
* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.7-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.7-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.7-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Tue Mar 28 2023 Than Ngo <than@redhat.com> - 1.7-14
- Migrated to SPDX license
- Fixed deprecated patch rpm macro


* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.7-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.7-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.7-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.7-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Mon May 17 2021 Timm Bäder <tbaeder@redhat.com> - 1.7-9
- Remove unused soname macro
- Remove unused patches
- Use make macros

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.7-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.7-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jun 24 2020 Michel Normand <normand@linux.vnet.ibm.com> 1.7-6
  Add remove_2_backslashes_in_shell_call.patch
  to avoid rawhide build failure.

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.7-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.7-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.7-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.7-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu May 17 2018 Michel Normand <normand@linux.vnet.ibm.com> 1.7-1
- Update v1.7
  New api cxl_get_tunneled_ops_supported
- Update v1.6
  new functions cxl_afu_host_thread_wait(), cxl_work_disable_wait(),
  cxl_work_enable_wait() and cxl_work_get_tid() are now unconditionally
  built and exported.
- remove libcxl_sysmacros.patch embeded upstream.

* Thu Mar 08 2018 Than Ngo <than@redhat.com> - 1.5-4
- fixed bz#1552648 - libcxl: Incomplete Fedora build flags injection

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.5-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.5-1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Thu Jun 8 2017 Michel Normand <normand@linux.vnet.ibm.com> 1.5-0
- Update v1.5
  * libcxl: Check afu link when read from PSA mmio return all FFs
  * Makefile: add -Werror
  * Use _DEFAULT_SOURCE rather than _BSD_SOURCE
  * Fix sparse warnings
  * Added #include <asm/types.h>
  * Man pages: document flags CXL_MMIO_{BIG,HOST,LITTLE}_ENDIAN
  * Makefile: do not fail if target symlink already exists.
  * Man pages: clarify mmio read/write alignment constraints.
  * Create LIBSONAME link
  * sysfs: Fix a boundary condition check for OUT_OF_RANGE macro
- remove libcxl_create_soname_link.patch part of above update.
- add libcxl_sysmacros.patch to avoid warning at build time

* Fri Jun 10 2016 Than Ngo <than@redhat.com> - 1.4-5
- cleanup specfile
- upload the tarball

* Thu Jun 2 2016 michel normand <normand@linux.vnet.ibm.com> 1.4-4
- Update v1.4
  * New API function cxl_get_psl_timebase_synced.
  * Simplify implementation of OUT_OF_RANGE macro
  * libcxl add install target
  * use LDFLAGS from the env
  * libcxl set default soname and interface version
  * Add extern "C" to libcxl.h for compatibility with C++ projects
  * typo error in 3 man pages
  * Add SONAME support in Makefile
- remove embeded patches:
  libcxl_typo_correction_man_pages.patch
  libcxl_add_soname_in_Makefile.patch
- new libcxl_create_soname_link.patch

* Thu Mar 17 2016 michel normand <normand@linux.vnet.ibm.com> 1.3-4
- do cp -p of man page in build section, and add empty lines below.
- this is the initial version before git commit.

* Fri Mar 11 2016 michel normand <normand@linux.vnet.ibm.com> 1.3-3
- add libcxl.so in devel package

* Thu Mar 03 2016 michel normand <normand@linux.vnet.ibm.com> 1.3-2
- do not use releease in VERS_LIB

* Fri Jan 29 2016 michel normand <normand@linux.vnet.ibm.com> 1.3-1
- new package and spec file of libcxl from upstream
  url: https://github.com/ibm-capi/libcxl
