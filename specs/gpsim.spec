Name:		gpsim
Version:	0.32.1
Release:	6%{?dist}
Summary:	A simulator for Microchip (TM) PIC (TM) microcontrollers
Summary(fr):	Un simulateur pour les microcontrôleurs PIC (TM) Microchip (TM)

# Source code is GPLv2+ except src/, modules/ and eXdbm/ which are LGPLv2+
# Automatically converted from old format: GPLv2+ and LGPLv2+ - review is highly recommended.
License:	GPL-2.0-or-later AND LicenseRef-Callaway-LGPLv2+
URL:		http://gpsim.sourceforge.net/gpsim.html
Source:		http://downloads.sourceforge.net/gpsim/gpsim-%{version}.tar.gz
Source1:	gpsim.png
Patch1:		%{name}-%{version}-lcd.patch


BuildRequires:	gcc-c++
BuildRequires:	gtk2-devel, flex, readline-devel, popt-devel
BuildRequires:	autoconf gputils desktop-file-utils automake libtool
BuildRequires:	make


%description
gpsim is a simulator for Microchip (TM) PIC (TM) microcontrollers.
It supports most devices in Microchip's 12-bit, 14bit, and 16-bit
core families. In addition, gpsim supports dynamically loadable
modules such as LED's, LCD's, resistors, etc. to extend the simulation
environment beyond the PIC.

%description -l fr
gpsim est un simulateur pour les microcontrôleurs PIC (TM) Microchip (TM).
Il gère la plupart des microcontrôleurs des familles 12, 14 et 16 bits.
gpsim gère également les modules chargeables dynamiquement tels que les LED,
afficheurs LCD, résistances, etc. afin d'étendre l'environnement
de simulation des PIC.

%package	devel
Summary:	Libraries and files headers for gpsim
Summary(fr):	Bibliothèques et fichiers d'en-têtes pour gpsim
Requires:	%{name} = %{version}-%{release}

%description devel
The %{name}-devel package includes the static libraries, header files,
and documentation for compiling programs that use the gpsim library.

%description -l fr devel
Le paquetage %{name}-devel contient les bibliothèques statiques, les fichiers
d'en-têtes et la documentation nécessaires à la compilation des programmes
qui utilisent la bibliothèque gpsim.

%prep
%setup -q
mv AUTHORS AUTHORS.raw
mv ChangeLog ChangeLog.raw
iconv -f ISO88592 -t UTF8  AUTHORS.raw -o  AUTHORS
iconv -f ISO88592 -t UTF8  ChangeLog.raw -o ChangeLog
rm -f AUTHORS.raw ChangeLog.raw 
%patch 1 -p0
autoconf

%build
%configure
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%{__make} install DESTDIR=%{buildroot}
%{__rm} -f examples/Makefile
%{__rm} -f examples/modules/Makefile
%{__rm} -f examples/projects/Makefile
install -Dm 0644 -p doc/metadata/%{name}.desktop \
	%{buildroot}%{_datadir}/applications/%{name}.desktop
install -Dm 0644 -p %{SOURCE1} \
	%{buildroot}%{_datadir}/pixmaps/%{name}.png
install -Dm 0644 -p doc/metadata/%{name}.appdata.xml \
	%{buildroot}%{_datadir}/appdata/%{name}.appdata.xml
desktop-file-install --vendor=""\
	--dir=%{buildroot}/%{_datadir}/applications\
	%{buildroot}%{_datadir}/applications/%{name}.desktop


%ldconfig_scriptlets

%files
%doc ANNOUNCE AUTHORS COPYING ChangeLog HISTORY NEWS
%doc README README.EXAMPLES README.MODULES TODO
%doc doc/gpsim.lyx doc/gpsim.pdf
%doc examples/
%{_bindir}/*
%{_libdir}/*.so.*
%{_datadir}/pixmaps/gpsim.png
%{_datadir}/applications/gpsim.desktop
%{_datadir}/appdata/gpsim.appdata.xml



%files devel
%doc COPYING
%{_libdir}/*.so
%{_libdir}/pkgconfig/gpsim.pc
%exclude %{_libdir}/*.a
%{_includedir}/*

%changelog
* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.32.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Mon Sep 02 2024 Miroslav Suchý <msuchy@redhat.com> - 0.32.1-5
- convert license to SPDX

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.32.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Tue Mar 12 2024 Roy Rankin <rrankin@ihug.com.au> - 0.32.1-3
- add patch to fix lcd module

* Wed Jan 24 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.32.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sat Jan 20 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.32.1-1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Tue Nov 14 2023 Roy Rankin <rrankin@ihug.com.au> - 0.32.1-0
- Added processors and bug fixes

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.31.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.31.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.31.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.31.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.31.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.31.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.31.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.31.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.31.0-1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Wed Jun 26 2019 Roy Rankin <rrankin@ihug.com.au> - 0.31.0-0
- Upstream release, bug fixes, new devices supported

* Sun Feb 17 2019 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.30.0-7
- Rebuild for readline 8.0

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.30.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sun Jul 15 2018 Roy Rankin <rrankin@ihug.com.au> - 0.30.0-5
- Change buildrequires from gcc to gcc-c++

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.30.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.30.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.30.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.30.0-1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Mon Jun 19 2017 Roy Rankin <rrankin@ihug.com.au> - 0.30.0-0
- Upstream update to 0.30.0

* Mon May 15 2017 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.29.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_27_Mass_Rebuild

* Sat Feb 18 2017 Roy Rankin <rrankin@ihug.com.au> - 0.29.0-4
- Patch for new compiler errors

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.29.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Jan 12 2017 Igor Gnatenko <ignatenko@redhat.com> - 0.29.0-2
- Rebuild for readline 7.x

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.29.0-1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Mon Aug 17 2015 Roy Rankin <rrankin@ihug.com.au> - 0.29.0-0
- Upstream update to 0.29.0

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.28.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat May 02 2015 Kalev Lember <kalevlember@gmail.com> - 0.28.1-2
- Rebuilt for GCC 5 C++11 ABI change

* Wed Nov 19 2014 Roy Rankin <rrankin@ihug.com.au> - 0.28.1-1
- Fix CTRL+C crash
- use website icon

* Sat Nov 15 2014 Roy Rankin <rrankin@ihug.com.au> - 0.28.1-0
- Upstream update to 0.28.1
- metadata from upstream

* Sat Nov 15 2014 Roy Rankin <rrankin@ihug.com.au> - 0.28.0-1
- Add appdata file

* Thu Nov 13 2014 Roy Rankin <rrankin@ihug.com.au> - 0.28.0-0
- Upstream update to 0.28.0
- Add desktop file

* Tue Oct 28 2014 Lubomir Rintel <lkundrak@v3.sk> - 0.27.0-4
- Fix CTRL+C crash
- Fix command line option parsing

* Sat Aug 16 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.27.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.27.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Mon Sep 02 2013 Roy Rankin <rrankin@ihug.com.au> - 0.27.0-1
- Upstream update to 0.27.0

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.26.1-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.26.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.26.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Tue Feb 28 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.26.1-5
- Rebuilt for c++ ABI breakage

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.26.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Wed Dec 07 2011 Roy Rankin <rrankin@ihug.com.au> 0.26.1-3
- patch for glib

* Tue Dec 06 2011 Adam Jackson <ajax@redhat.com> - 0.26.1-2
- Rebuild for new libpng

* Tue May 03 2011 Roy Rankin <rrankin@ihug.com.au> 0.26.1-1
- upstream release of gpsim 0.26.1 - bug fixes and see ANNOUNCE for
  new features and processors.

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.25.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Sun Jun 27 2010 Roy Rankin <rrankin@ihug.com.au> 0.25.0-2
- upstream release of gpsim 0.25.0 - bug fixes and see ANNOUNCE for
  new features and processors.

* Tue Jan 26 2010 Roy Rankin <rrankin@ihug.com.au> 0.24.0-2
- do not include *.a files BZ 556053

* Tue Sep 15 2009 Roy Rankin <rrankin@ihug.com.au> 0.24.0-1
- upstream release of gpsim 0.24.0 - bug fixes and see ANNOUNCE for
  new features and processors.

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.23.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Sat Mar 21 2009 Roy Rankin <rrankin@ihug.com.au> 0.23.0-4
- upstream release of gpsim 0.23.0 - bug fixes and see ANNOUNCE for
  new features and processors.

* Thu Mar 05 2009 Roy Rankin <rrankin@ihug.com.au> 0.23.0-3.20090302svn2042
- RC1 of gpsim-0.23.0 see ANNOUNCE file for new features

* Tue Feb 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.23.0-2.20090215svn2034
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Sun Feb 15 2009 Roy Rankin <rrankin@ihug.com.au> 0.23.0-1
- SVN vesion with bug fixes, more suported chips, new ADC, fix needed for GCC 4.4

* Sun Sep 07 2008 Kevin Kofler <Kevin@tigcc.ticalc.org> 0.22.0-7
- Fix build with GCC 4.3 (#434061), patch by Vasile Gaburici, simpler fix for
  the "list" name conflict from the Debian patch
- PPC build fix (acinclude readline problem) by Mamoru Tasaka

* Mon Feb 18 2008 Fedora Release Engineering <rel-eng@fedoraproject.org> - 0.22.0-6
- Autorebuild for GCC 4.3

* Thu Sep 27 2007 Alain Portal <aportal[AT]univ-montp2[DOT]fr> 0.22.0-5
  - Add BR popt-devel

* Tue Aug 21 2007 Alain Portal <aportal[AT]univ-montp2[DOT]fr> 0.22.0-4
  - Licence tag clarification

* Tue Feb 13 2007 Alain Portal <aportal[AT]univ-montp2[DOT]fr> 0.22.0-3
- Remove Makefiles that are in conflict between i386 and x86_64 arch 
  Fix #228362

* Mon Feb  5 2007 Alain Portal <aportal[AT]univ-montp2[DOT]fr> 0.22.0-2
  - FE7 rebuild

* Tue Nov 14 2006 Alain Portal <aportal[AT]univ-montp2[DOT]fr> 0.22.0-1
  - New upstream version
  - Remove patches that are no more needed (applied by upstream)

* Thu Oct 05 2006 Christian Iseli <Christian.Iseli@licr.org> 0.21.11-9
 - rebuilt for unwind info generation, broken in gcc-4.1.1-21

* Sat Sep 23 2006 Alain Portal <aportal[AT]univ-montp2[DOT]fr> 0.21.11-8
- Add patch to fix a ktechlab crash, a ktechlab upstream contribution
  See http://ktechlab.org/download/gpsim.php
- Use macros for rm and make
- Use macro style instead of variable style

* Fri Sep  1 2006 Alain Portal <aportal[AT]univ-montp2[DOT]fr> 0.21.11-7
  - FE6 rebuild

* Wed Mar 15 2006 Alain Portal <aportal[AT]univ-montp2[DOT]fr> 0.21.11-6
  - Update Patch

* Wed Mar 15 2006 Alain Portal <aportal[AT]univ-montp2[DOT]fr> 0.21.11-5
  - Update Patch

* Tue Mar 14 2006 Alain Portal <aportal[AT]univ-montp2[DOT]fr> 0.21.11-4
  - Patch to make gcc-4.1.0 happy

* Mon Mar 13 2006 Alain Portal <aportal[AT]univ-montp2[DOT]fr> 0.21.11-3
  - Rebuild for FE5

* Thu Oct  6 2005 Alain Portal <aportal[AT]univ-montp2[DOT]fr> 0.21.11-2
  - Remove useless Requires

* Wed Oct  5 2005 Alain Portal <aportal[AT]univ-montp2[DOT]fr> 0.21.11-1
  - New version
  - Improve download url

* Fri Sep 30 2005 Alain Portal <aportal[AT]univ-montp2[DOT]fr> 0.21.4-5
- Improve prep section to make rpmlint happy
- Contributions of Jose Pedro Oliveira <jpo[AT]di[DOT]uminho[DOT]pt>
  Thanks to him.

* Mon Sep 19 2005 Alain Portal <aportal[AT]univ-montp2[DOT]fr> 0.21.4-4
  - Add missing a rm -rf RPM_BUILD_ROOT statement in the install section

* Thu Sep 15 2005 Alain Portal <aportal[AT]univ-montp2[DOT]fr> 0.21.4-3
  - Exclude .la file
  -  Add examples

* Tue Sep 13 2005 Alain Portal <aportal[AT]univ-montp2[DOT]fr> 0.21.4-2
  - License is GPL
  - Add french summary and description

* Mon Sep 12 2005 Alain Portal <aportal[AT]univ-montp2[DOT]fr> 0.21.4-1
  - New version

* Mon Nov  8 2004 Alain Portal <aportal[AT]univ-montp2[DOT]fr> 0:0.21.2-0.fdr.2
  - Add BuildRequires flex, readline-devel

* Wed Oct 27 2004 Alain Portal <aportal[AT]univ-montp2[DOT]fr> 0:0.21.2-0.fdr.1
  - Initial Fedora RPM
