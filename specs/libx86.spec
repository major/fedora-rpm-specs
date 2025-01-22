Name:           libx86
Version:        1.1
Release:        46%{?dist}
Summary:        Library for making real-mode x86 calls

License:        MIT
URL:            http://www.codon.org.uk/~mjg59/libx86
Source0:        http://www.codon.org.uk/~mjg59/libx86/downloads/%{name}-%{version}.tar.gz
# does not build on ppc, ppc64 and s390* yet, due to the lack of port i/o
# redirection and video routing
ExcludeArch:    ppc %{power64} s390 s390x %{sparc} aarch64 armv7hl

Patch0: libx86-add-pkgconfig.patch
Patch1: libx86-mmap-offset.patch
# patch from  https://bugs.debian.org/cgi-bin/bugreport.cgi?msg=34;filename=libx86-libc-test.patch.txt;att=1;bug=570676
# debian control portion removed as it fails to apply and we do not need it anyway
Patch2: libx86-libc-test.patch
Patch3: libx86-fix_processor_flags.patch
Patch4: libx86-ld_flags.patch
Patch5: libx86-1.1-24-fix-invalid-hlt-opcode.patch
Patch6: libx86-c99.patch
Patch7: libx86-c99-2.patch

BuildRequires:  gcc
BuildRequires: make
%description
A library to provide support for making real-mode x86 calls with an emulated
x86 processor.

%package devel
Summary:        Development tools for programs which will use libx86
Requires:       %{name} = %{version}-%{release}

%description devel
This package contains the static library and header file necessary for
development of programs that will use libx86 to make real-mode x86 calls.

%prep
%autosetup


%build
CFLAGS="$RPM_OPT_FLAGS" LDFLAGS="$RPM_LD_FLAGS" make BACKEND=x86emu LIBDIR=%{_libdir} %{?_smp_mflags}


%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT LIBDIR=%{_libdir}
rm $RPM_BUILD_ROOT/%{_libdir}/*.a

%ldconfig_scriptlets

%files
%doc COPYRIGHT
%{_libdir}/lib*.so.*

%files devel
%{_libdir}/lib*.so
%{_includedir}/*.h
%{_libdir}/pkgconfig/x86.pc

%changelog
* Mon Jan 20 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.1-46
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.1-45
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.1-44
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.1-43
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.1-42
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jan 04 2024 Florian Weimer <fweimer@redhat.com> - 1.1-41
- C compatibility fixes (#2256772)

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.1-40
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Wed May 3 2023 Pat Riehecky <riehecky@fnal.gov> 1.1-39
- Try to address invalid opcode crash

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.1-38
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.1-37
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.1-36
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Mon Dec 13 2021 Pat Riehecky <riehecky@fnal.gov> - 1.1-35
- Fix hardening flags

* Mon Dec 13 2021 Pat Riehecky <riehecky@fnal.gov> - 1.1-34
- sync up with Debian patch set

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.1-33
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.1-32
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.1-31
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.1-30
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.1-29
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.1-28
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.1-27
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.1-26
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.1-25
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.1-24
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Sun Aug 14 2016 Peter Robinson <pbrobinson@fedoraproject.org> 1.1-23
- Update Power64 macro

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.1-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Tue Jul 08 2014 Yaakov Selkowitz <yselkowi@redhat.com> - 1.1-19
- ExcludeArch: aarch64 due to missing sys/io.h

* Tue Jun 24 2014 Dennis Gilmore <dennis@ausil.us> - 1.1-18
- add patch from debian for ftbfs

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Sun Apr 14 2013 Matthew Garrett <mjg59@srcf.ucam.org> .1-15
- Revert previous change

* Sun Apr 14 2013 Peter Robinson <pbrobinson@fedoraproject.org> 1.1-14
- Make ExclusiveArch x86

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Wed Nov 04 2009 Dennis Gilmore <dennis@ausil.us> - 1.1-9
- Exclude sparc arches

* Tue Oct 27 2009 Adam Jackson <ajax@redhat.com> 1.1-8
- libx86-mmap-offset.patch: Attempt to make selinux happy by not mmap'ing
  the zero page.

* Thu Sep 03 2009 Karsten Hopp <karsten@redhat.com> 1.1-7
- excludearch s390, s390x where we don't have sys/io.h

* Tue Aug 04 2009 Dave Airlie <airlied@redhat.com> 1.1-6
- add pkgconfig support

* Sat Jul 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Tue May 20 2008 Matthew Garrett <mjg@redhat.com> 1.1-3
- Fix bizarre provides/obsoletes thinko 

* Tue May 20 2008 Matthew Garrett <mjg@redhat.com> 1.1-2
- Ensure RPM_OPT_FLAGS are passed. Patch from Till Maas.

* Mon May 19 2008 Matthew Garrett <mjg@redhat.com> 1.1-1
- Initial packaging of libx86
