Name:		gputils
Version:	1.5.2
Release:	8%{?dist}
Summary:	Development utilities for Microchip (TM) PIC (TM) microcontrollers
Summary(fr):	Outils de développement pour les microcontrôleurs PIC (TM) de Microchip (TM)

# Automatically converted from old format: GPLv2+ - review is highly recommended.
License:	GPL-2.0-or-later
URL:		http://gputils.sourceforge.net
Source:		http://downloads.sourceforge.net/%{name}/%{name}-%{version}.tar.bz2
Patch1:		gpasm_%{version}.patch
Patch2:		libgputils-%{version}.patch
Provides:	bundled(libiberty)

BuildRequires:	gcc
BuildRequires:	autoconf flex bison
BuildRequires: make

%description
This is a collection of development tools for Microchip (TM) PIC (TM)
microcontrollers.

Gputils includes gpasm, gplink and gplib as well as the utilities
gpdasm, gpstrip, gpvc, gpvo. 

%description -l fr
Ce paquetage contient une collection d'outils de développement pour les
microcontrôleurs PIC (TM) de Microchip (TM).

%package doc
Summary: Gputils documentation
Requires: gputils = %{version}-%{release}
BuildArch: noarch
%description doc
This package containes gputils documentation and HTML documentation for supported processors.

%prep
%setup -q
%patch -P 1 -p0
%patch -P 2 -p1

%build
autoconf -f -i
%configure --enable-gdb-debuginfo
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf $RPM_BUILD_ROOT
%{__make} install DESTDIR=$RPM_BUILD_ROOT
mkdir -p %{buildroot}/usr/share/doc/%{name}-doc
mv -f %{buildroot}/usr/share/doc/%{name}-%{version}/html %{buildroot}/usr/share/doc/%{name}-doc/html
cp -f doc/%{name}.p* %{buildroot}/usr/share/doc/%{name}-doc/


%files 
%doc AUTHORS ChangeLog COPYING README TODO 
%{_bindir}/*
%{_datadir}/%{name}/
%{_mandir}/man1/*
%{_mandir}/fr/man1/*

%files doc
%{_docdir}/%{name}-doc/



%changelog
* Mon Jan 27 2025 Roy Rankin <rrankin[AT]ihug[DOT]com[DOT]au> 1.5.2-8
- patch to build with gcc C23

* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.2-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Fri Jul 26 2024 Miroslav Suchý <msuchy@redhat.com> - 1.5.2-6
- convert license to SPDX

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Wed Jan 24 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sat Jan 20 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.2-1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Sun Jan 01 2023 Roy Rankin <rrankin[AT]ihug[DOT]com[DOT]au> 1.5.2-0
- Upstream release

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.0-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Aug 10 2018 Roy Rankin <rrankin[AT]ihug[DOT]com[DOT]au> 1.5.0-2
-  Patch for gplink assert on undefined symbol

* Fri Jul 20 2018 Roy Rankin <rrankin[AT]ihug[DOT]com[DOT]au> 1.5.0-1
-  Add patches to fix bugs found by gpsim

* Mon Jul 16 2018 Roy Rankin <rrankin[AT]ihug[DOT]com[DOT]au> 1.5.0-0
- Upstream release, Add debug flag to configure

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.2-1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu May 26 2016 Roy Rankin <rrankin[AT]ihug[DOT]com[DOT]au> 1.4.2-0
- Upstream release

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Aug 16 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.0-1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Wed Jun 25 2014 Roy Rankin <rrankin[AT]ihug[DOT]com[DOT]au> 1.3.0-0
- New upstream version, add flex, bison  to build requires

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Fri Aug 16 2013 Roy Rankin <rrankin[AT]ihug[DOT]com[DOT]au> 1.2.0-3
- Make gputils-doc a noarch package

* Thu Aug 15 2013 Roy Rankin <rrankin[AT]ihug[DOT]com[DOT]au> 1.2.0-2
- Break out documentation into seperate sub-package.
- Fix issue caused by doc macro change.
- Correct Source URL
  
* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.0-1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Jun 05 2013 Roy Rankin <rrankin[AT]ihug[DOT]com[DOT]au> 1.2.0-0
- New upstream version. 

* Mon Apr 29 2013 Roy Rankin <rrankin[AT]ihug[DOT]com[DOT]au> 1.1.0-0
- New upstream version. Modify package description.

* Sat Apr 20 2013 Shakthi Kannan <shakthimaan [AT] fedoraproject.org> - 0.14.3-3
- Use autoreconf for ARM

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.14.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Mon Nov  5 2012 Alain Portal <alain.portal[AT]univ-montp2[DOT]fr> 0.14.3-1
- New upstream version

* Mon Oct 15 2012 Jon Ciesla <limburgher@gmail.com> 0.14.2-1
- Provides: bundled(libiberty)

* Sat Jul 28 2012 Roy Rankin <rrankin[AT]ihug[DOT]com[DOT]au> 0.14.2-0
  - New upstream version with bug and documentation fixes

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.14.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sun Mar  4 2012 Alain Portal <alain.portal[AT]univ-montp2[DOT]fr> 0.14.1-1
- New upstream version
- Fix typo in gpdasm help message
- Update man pages

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.13.7-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.13.7-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.13.7-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Mon May 04 2009 Roy Rankin <rrankin[AT]ihug[DOT]com[DOT]au> 0.13.7-1
  - New upstream version with
    Added support for all processors supported by MPLAB 8.20 (except eeprom16 and related).
    Added support for "LIST M=?" directive.
    Fixed several bugs.

* Tue Feb 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.13.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Mon Sep 15 2008 Roy Rankin <rrankin[AT]ihug[DOT]com[DOT]au> 0.13.6-1
  - New upstream version

* Sun Oct 28 2007 Alain Portal <aportal[AT]univ-montp2[DOT]fr> 0.13.5-1
  - New upstream version
  - Patches to improve man pages formatting
  - Use macros for rm and make

* Tue Aug 21 2007 Alain Portal <aportal[AT]univ-montp2[DOT]fr> 0.13.4-4
  - Really change licence tag

* Tue Aug 21 2007 Alain Portal <aportal[AT]univ-montp2[DOT]fr> 0.13.4-3
  - Licence tag clarification

* Thu Oct 05 2006 Christian Iseli <Christian.Iseli@licr.org> 0.13.4-2
 - rebuilt for unwind info generation, broken in gcc-4.1.1-21

* Thu Sep 21 2006 Alain Portal <aportal[AT]univ-montp2[DOT]fr> 0.13.4-1
  - New upstream version
  - Add french summary and description

* Fri Sep  1 2006 Alain Portal <aportal[AT]univ-montp2[DOT]fr> 0.13.3-3
  - FE6 rebuild

* Mon Mar 13 2006 Alain Portal <aportal[AT]univ-montp2[DOT]fr> 0.13.3-2
  - Rebuild for FE5

* Mon Sep 12 2005 Alain Portal <aportal[AT]univ-montp2[DOT]fr> 0.13.3-1
  - New version
  - Patch to update french man pages

* Mon May 23 2005 Alain Portal <aportal[AT]univ-montp2[DOT]fr> 0.13.2-1
  - New version

* Thu Jan 6 2005 Alain Portal <aportal[AT]univ-montp2[DOT]fr> 0:0.13.0-0.fdr.2
  - Patch to update french man pages

* Tue Jan 4 2005 Alain Portal <aportal[AT]univ-montp2[DOT]fr> 0:0.13.0-0.fdr.1
  - New version

* Thu Oct 7 2004 Alain Portal <aportal[AT]univ-montp2[DOT]fr> 0:0.12.4-0.fdr.2
  - Use Licence instead of copyright
  - Use full name and release in Source URL instead of macro
  - Package should own full directory /usr/share/gputils
  - Remove usefulness generic file INSTALL
  - Remove doc source file gputils.lyx

* Wed Oct 6 2004 Alain Portal <aportal[AT]univ-montp2[DOT]fr> 0:0.12.4-0.fdr.1
  - Initial Fedora RPM
