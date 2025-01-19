Summary: POSIX regexp functions
Name: librx
Version: 1.5
Release: 50%{?dist}
# Automatically converted from old format: GPLv2+ - review is highly recommended.
License: GPL-2.0-or-later
URL: http://www.gnu.org/software/rx/rx.html
# Originally downloaded from ftp://ftp.gnu.org/gnu/rx/rx-1.5.tar.bz2
# The FSF no longer offers this code.
Source0: rx-%{version}.tar.bz2
Patch0: rx-1.5-shared.patch
Patch1: rx-1.5-texinfo.patch
Patch2: librx-1.5-libdir64.patch
Patch3: rx-1.5-libtoolmode.patch
BuildRequires: texinfo, libtool
BuildRequires: make

%description
Rx is, among other things, an implementation of the interface
specified by POSIX for programming with regular expressions.  Some
other implementations are GNU regex.c and Henry Spencer's regex
library.

%package devel
Summary: POSIX regexp functions, developers library
Requires: %{name} = %{version}-%{release}

%description devel
Rx is, among other things, an implementation of the interface
specified by POSIX for programming with regular expressions.  Some
other implementations are GNU regex.c and Henry Spencer's regex
library.

This package contains files needed for development with librx.

%prep
%setup -q -n rx-%{version}
%patch -P0 -p1
%patch -P1 -p1 -b .texipatch
%ifarch x86_64 s390x ia64 %{power64} alpha sparc64 aarch64 %{mips64} riscv64
%patch -P2 -p1 -b .64bit
%endif
%patch -P3 -p1 -b .libtoolmode

%build
# The package has many C99 compatibility issues.  It relies on
# implicit function declarations.  It may not work on 64-bit
# architectures because some pointers are truncated to 32 bits.
%global build_type_safety_c 0
%set_build_flags
CC="$CC -std=gnu89"
%configure
make %{?_smp_mflags}
make doc/rx.info

%install
rm -rf ${RPM_BUILD_ROOT}
mkdir -p ${RPM_BUILD_ROOT}%{_infodir}
mkdir -p ${RPM_BUILD_ROOT}%{_libdir}
mkdir -p ${RPM_BUILD_ROOT}%{_includedir}
make install DESTDIR=${RPM_BUILD_ROOT}
install -m 644 doc/rx.info ${RPM_BUILD_ROOT}%{_infodir}
rm -rf ${RPM_BUILD_ROOT}%{_libdir}/librx.la
rm -rf ${RPM_BUILD_ROOT}%{_libdir}/librx.a
chmod -x ${RPM_BUILD_ROOT}%{_includedir}/rxposix.h

%ldconfig_scriptlets

%files
%{_libdir}/*.so.*

%files devel
%doc ANNOUNCE BUILDING COOKOFF rx/ChangeLog
%{_includedir}/*
%{_infodir}/*
%{_libdir}/*.so

%changelog
* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.5-50
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Fri Jul 26 2024 Miroslav Suchý <msuchy@redhat.com> - 1.5-49
- convert license to SPDX

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.5-48
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Fri Mar 01 2024 David Abdurachmanov <davidlt@rivosinc.com> - 1.5-47
- Enable libdir64 patch for riscv64

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.5-46
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.5-45
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Aug 16 2023 Florian Weimer <fweimer@redhat.com> - 1.5-44
- Set build_type_safety_c to 0 (#2192889)

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.5-43
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Wed May 03 2023 Florian Weimer <fweimer@redhat.com> - 1.5-42
- Build in C89 mode (#2192889)

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.5-41
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.5-40
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.5-39
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.5-38
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.5-37
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.5-36
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.5-35
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.5-34
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.5-33
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.5-32
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.5-31
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.5-30
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.5-29
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.5-28
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri Aug 12 2016 Michal Toman <mtoman@fedoraproject.org> - 1.5-27
- Use lib64 on 64-bit MIPS

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.5-26
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.5-25
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.5-24
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.5-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Tue May 20 2014 Brent Baude <baude@us.ibm.com> - 1.5-22
- Update 64bit arch list

* Wed Jan 15 2014 Jason L Tibbitts III <tibbs@math.uh.edu> - 1.5-21
- Remove single trailing space in -devel post scriptlet which caused a file
  named " " in / to appear on install.

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.5-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed May 29 2013 Peter Robinson <pbrobinson@fedoraproject.org> 1.5-19
- Update 64bit arch list

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.5-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.5-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.5-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.5-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Wed Jan 20 2010 Tom "spot" Callaway <tcallawa@redhat.com> - 1.5-15
- don't package static lib (resolves bz 556072)

* Wed Aug 19 2009 Tom "spot" Callaway <tcallawa@redhat.com> - 1.5-14
- take URL out of Source0

* Sat Jul 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.5-13.1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Fri Apr 24 2009 Karsten Hopp <karsten@redhat.com> 1.5-12.1
- add s390x to 64bit archs

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.5-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Mon Feb 16 2009 Tom "spot" Callaway <tcallawa@redhat.com> 1.5-11
- pass modes to libtool

* Tue Feb 19 2008 Fedora Release Engineering <rel-eng@fedoraproject.org> - 1.5-10
- Autorebuild for GCC 4.3

* Thu Aug 23 2007 Tom "spot" Callaway <tcallawa@redhat.com> 1.5-9
- fix license, rebuild for BuildID

* Mon Sep 11 2006 Tom "spot" Callaway <tcallawa@redhat.com> 1.5-8
- fix bz 200090

* Mon Sep 11 2006 Tom "spot" Callaway <tcallawa@redhat.com> 1.5-7
- fix bz 197717
- bump for FC-6

* Tue Feb 28 2006 Tom "spot" Callaway <tcallawa@redhat.com> 1.5-6
- bump for FC-5

* Mon May  9 2005 Tom "spot" Callaway <tcallawa@redhat.com> 1.5-5
- remove hardcoded dist tags

* Sun May  8 2005 Tom "spot" Callaway <tcallawa@redhat.com> 1.5-4
- Fix 64 bit arches to install to the right libdir

* Thu May  5 2005 Tom "spot" Callaway <tcallawa@redhat.com> 1.5-3
- add BuildRequires: texinfo

* Sun Apr 24 2005 Tom "spot" Callaway <tcallawa@redhat.com> 1.5-2
- use dist tag

* Sat Apr 23 2005 Tom "spot" Callaway <tcallawa@redhat.com> 1.5-1
- new package, based on Alexey Voinov's package from AltLinux
