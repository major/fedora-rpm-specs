%global tag 1.10.2-1

Name:		xdrawchem
Version:	1.10.2
Release:	14%{?dist}
Summary:	2D chemical structures drawing tool
URL:            https://www.woodsidelabs.com/chemistry/%{name}.php
Source0:        https://github.com/bryanherger/%{name}/archive/%{tag}/%{name}-%{tag}.tar.gz
Source1:	%{name}.desktop
# Automatically converted from old format: GPLv2+ - review is highly recommended.
License:	GPL-2.0-or-later
BuildRequires:  make
BuildRequires:  gcc-c++
BuildRequires:	desktop-file-utils
BuildRequires:  pkgconfig(openbabel-3)
BuildRequires:	qt5-qtbase-devel

Requires:       hicolor-icon-theme

# remove -O0 -g3 from CXXFLAGS
Patch0:         %{name}-cxxflags.patch
Patch1:         %{name}-warn.patch
Patch2:         %{name}-porting_to_openbabel3.patch

%description
%{name} is a two-dimensional molecule drawing program for Unix
operating systems.  It is similar in functionality to other molecule
drawing programs such as ChemDraw (TM, CambridgeSoft).  It can read
and write MDL Molfiles and CML files to allow sharing between
%{name} and other chemistry applications.

%prep
%autosetup -p1 -n %{name}-%{tag}/%{name}-qt5

%build
%qmake_qt5 PREFIX=%{_prefix}
%make_build

%install
%make_install INSTALL_ROOT=%{buildroot}

# menu
mkdir -p %{buildroot}%{_datadir}/applications
install -Dpm 644 ring/%{name}-icon.png %{buildroot}%{_datadir}/icons/hicolor/48x48/apps/%{name}.png
desktop-file-install \
	--dir %{buildroot}%{_datadir}/applications \
	%{SOURCE1}
pushd %{buildroot}%{_datadir}/%{name}
rm -f caslist.txt \
      CMakeLists.txt \
      COPYRIGHT.txt \
      GPL.txt \
      HISTORY.txt
popd

rm -rf %{buildroot}%{_datadir}/%{name}/doc

%find_lang %{name} --without-mo --with-qt

%files -f %{name}.lang
%license GPL.txt COPYRIGHT.txt
%doc doc/*
%{_bindir}/%{name}
%{_datadir}/%{name}/
%{_datadir}/applications/%{name}.desktop
%{_datadir}/icons/hicolor/*/apps/%{name}.png

%changelog
* Sun Jan 19 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.10.2-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Fri Jul 26 2024 Miroslav Suchý <msuchy@redhat.com> - 1.10.2-13
- convert license to SPDX

* Sat Jul 20 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.10.2-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Sat Jan 27 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.10.2-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sat Jul 22 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.10.2-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Sat Jan 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.10.2-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.10.2-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Sat Jan 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.10.2-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Sat Nov 06 2021 Antonio Trande <sagitter@fedoraproject.org> - 1.10.2-6
- Porting to openbabel3

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.10.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.10.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.10.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Jan 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.10.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Nov 27 2019 Dominik Mierzejewski <rpm@greysector.net> - 1.10.2-1
- update to 1.10.2 (#1777310)
- update URLs
- upstream switched to QT5
- drop obsolete patches
- mark translations using find_lang

* Sat Jul 27 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.9.9-41
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.9.9-40
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.9.9-39
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.9.9-38
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jan 18 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 1.9.9-37
- Remove obsolete scriptlets

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.9.9-36
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.9.9-35
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.9.9-34
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri Oct 14 2016 Dominik Mierzejewski <rpm@greysector.net> - 1.9.9-33
- rebuild for openbabel-2.4.1

* Sat Feb 20 2016 Dominik Mierzejewski <rpm@greysector.net> - 1.9.9-32
- Rebuild for openbabel

* Wed Feb 17 2016 Dominik Mierzejewski <rpm@greysector.net> - 1.9.9-31
- fix build with gcc-6 (bug #1308250)
- use license macro
- drop unnecessary attr

* Fri Feb 05 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.9.9-30
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Jun 19 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.9.9-29
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat May 02 2015 Kalev Lember <kalevlember@gmail.com> - 1.9.9-28
- Rebuilt for GCC 5 C++11 ABI change

* Wed Feb 25 2015 Dominik Mierzejewski <rpm@greysector.net> - 1.9.9-27
- rebuilt for openbabel-2.3.90

* Mon Aug 18 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.9.9-26
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.9.9-25
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Mar 15 2014 Dominik Mierzejewski <rpm@greysector.net> 1.9.9-24
- enable aarch64 support (bug #1019042)
- fix bogus dates in changelog
- add missing BRs
- fix linking
- fix doc build
- drop Group: tag

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.9.9-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Sun Feb 10 2013 Parag Nemade <paragn AT fedoraproject DOT org> - 1.9.9-22
- Remove vendor tag from desktop file as per https://fedorahosted.org/fesco/ticket/1077
- Cleanup spec as per recently changed packaging guidelines

* Mon Jan 21 2013 Adam Tkac <atkac redhat com> - 1.9.9-21
- rebuild due to "jpeg8-ABI" feature drop

* Fri Dec 21 2012 Adam Tkac <atkac redhat com> - 1.9.9-20
- rebuild against new libjpeg

* Wed Aug  1 2012 Mamoru Tasaka <mtasaka@fedoraproject.org> - 1.9.9-19
- Fix build error by including needed header

* Sun Jul 22 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.9.9-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Tue Feb 28 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.9.9-17
- Rebuilt for c++ ABI breakage

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.9.9-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Mon Feb 07 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.9.9-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Thu Nov 25 2010 Dominik Mierzejewski <rpm@greysector.net> 1.9.9-14
- rebuild for new openbabel
- fix source URL
- add `0' to unnumbered source and patch
- fix some compiler warnings
- use a nicer icon included in the sources, put it into hicolor icons
  directory and add appropriate scriptlets and Requires:
- fix desktop file

* Mon Jul 27 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.9.9-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Thu Feb 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.9.9-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Mon Jul 07 2008 Dominik Mierzejewski <rpm@greysector.net> 1.9.9-11
- rebuild for new openbabel

* Sun Jun 01 2008 Dominik Mierzejewski <rpm@greysector.net> 1.9.9-10
- fix segfault (#447531), patch by Mamoru Tasaka
- don't use %%makeinstall

* Fri Apr 04 2008 Dominik Mierzejewski <rpm@greysector.net> 1.9.9-9
- qt-devel -> qt3-devel (thanks to Rex Dieter)
- port to openbabel-2.2

* Tue Feb 19 2008 Fedora Release Engineering <rel-eng@fedoraproject.org> - 1.9.9-8
- Autorebuild for GCC 4.3

* Mon Jan 07 2008 Dominik Mierzejewski <rpm@greysector.net> 1.9.9-7
- fix build with gcc-4.3

* Wed Aug 29 2007 Dominik Mierzejewski <rpm@greysector.net> 1.9.9-6
- rebuild for BuildID
- fix license tag

* Tue Dec 19 2006 Dominik Mierzejewski <rpm@greysector.net> 1.9.9-5
- rebuild against new openbabel in devel
- simplify d-f-i call

* Tue Aug 29 2006 Dominik Mierzejewski <rpm@greysector.net> 1.9.9-4
- mass rebuild

* Thu Aug 10 2006 Dominik Mierzejewski <rpm@greysector.net> 1.9.9-3
- added dist tag

* Mon Aug 07 2006 Dominik Mierzejewski <rpm@greysector.net> 1.9.9-2
- simplified file list

* Sun Jan 08 2006 Dominik Mierzejewski <rpm@greysector.net> 1.9.9-1
- Updated to 1.9.9

* Thu Aug 11 2005 Dominik Mierzejewski <rpm@greysector.net>
- Updated to 1.9.8

* Sat Nov 29 2003 Gunner Poulsen <gunner@gnuskole.dk>
- Updated to require openbabel.

* Sun Jun 22 2003 Gunner Poulsen <gunner@gnuskole.dk> 1.7.2-1RH9
- Modyfied to fit Red Hat 9 and 8.

* Sat Apr 05 2003 Eduardo Sanchez <sombragris@sombragris.org> 1.6.9-1mdk
- 1.6.9

* Wed Mar 12 2003 Eduardo Sanchez <sombragris@sombragris.org> 1.6.8-1mdk
- 1.6.8
- resumed compilation after a long series of unsuccessful trials ;)

* Tue Jan 07 2003 Eduardo Sanchez <sombragris@sombragris.org> 1.6.3-1mdk
- 1.6.3

* Fri Dec 27 2002 Eduardo Sanchez <sombragris@sombragris.org> 1.6.2b-1mdk
- 1.6.2b
- Built on MDK 9.0 and qt 3.1
- Spec file reworked to take account of differences with Cooker packages
- Thanks to Bryan for his help in building this package!

* Thu Nov 07 2002 Eduardo Sanchez <sombragris@sombragris.org> 1.6-1mdk
- 1.6

* Tue Oct 15 2002 Eduardo Sanchez <sombragris@sombragris.org> 1.5.5-1mdk
- 1.5.5

* Mon Oct 07 2002 Eduardo Sanchez <sombragris@sombragris.org> 1.5.4-2mdk
- dir was locked; fixed

* Mon Oct 07 2002 Eduardo Sanchez <sombragris@sombragris.org> 1.5.4-1mdk
- 1.5.4

* Thu Oct 03 2002 Eduardo Sanchez <sombragris@sombragris.org> 1.5.3-1mdk
- 1.5.3
- streamlined spec file; removed references to old patch

* Fri Sep 20 2002 Eduardo Sanchez <sombragris@sombragris.org> 1.5.2-1mdk
- 1.5.2
- First build with autoconf, let's see :)

* Tue Sep 10 2002 Eduardo Sanchez <sombragris@sombragris.org> 1.5.1-1mdk
- 1.5.1
- 1.5 didn't work, let hope this one does!

* Fri Aug 02 2002 Eduardo Sanchez <sombragris@sombragris.org> 1.4.2-1mdk
- 1.4.2

* Thu Jul 18 2002 Eduardo Sanchez <sombragris@sombragris.org> 1.4.1-1mdk
- 1.4.1

* Thu Jul 04 2002 Eduardo Sanchez <sombragris@sombragris.org> 1.4-1mdk
- 1.4
- built against KDE 3.0.2

* Fri Jun 07 2002 Eduardo Sanchez <sombragris@sombragris.org> 1.3.2-1mdk
- 1.3.2

* Tue Jun 04 2002 Eduardo Sanchez <sombragris@sombragris.org> 1.3.1-1mdk
- 1.3.1

* Wed May 29 2002 Eduardo Sanchez <sombragris@sombragris.org> 1.3-1mdk
- 1.3

* Thu May 23 2002 Eduardo Sanchez <sombragris@sombragris.org> 1.2-2mdk
- rebuilt against standard Mandrake KDE 3.0.1 packages 

* Wed May 22 2002 Eduardo Sanchez <sombragris@sombragris.org> 1.2-1mdk
- 1.2

* Wed May 1 2002 Eduardo Sanchez <sombragris@sombragris.org> 1.1.1-1mdk
- 1.1.1

* Sun Apr 14 2002 Eduardo Sanchez <sombragris@sombragris.org> 1.1-2mdk
- 1.1
- patched Makefile only for Qt3 (libqt-mt)
- build with Qt3

* Thu Mar 28 2002 Laurent MONTEL <lmontel@mandrakesoft.com> 1.0.2-1mdk
- 1.0.2
- Fix hard coded path

* Thu Mar 21 2002 Lenny Cartier <lenny@mandrakesoft.com> 1.0.1-1mdk
- 1.0.1

* Tue Feb 26 2002 Lenny Cartier <lenny@mandrakesoft.com> 1.0-1mdk
- 1.0
- fix menu
- remove useless ldconfig

* Wed Feb 06 2002 Lenny Cartier <lenny@mandrakesoft.com> 0.99.9-1mdk
- 0.99.9

* Mon Jan 28 2002 Lenny Cartier <lenny@mandrakesoft.com> 0.99.8-1mdk
- 0.99.8

* Tue Dec 18 2001 Laurent MONTEL <lmontel@mandrakesoft.com> 0.99.7-1mdk
- 0.99.7

* Wed Dec 05 2001 Lenny Cartier <lenny@mandrakesoft.com> 0.99.6-1mdk
- 0.99.6

* Thu Nov 15 2001 Lenny Cartier <lenny@mandrakesoft.com> 0.99.4-1mdk
- 0.99.4

* Fri Oct 12 2001 Lenny Cartier <lenny@mandrakesoft.com> 0.99.3-1mdk
- rebuild against new libpng
- 0.99.3

* Thu Sep 27 2001 Laurent MONTEL <lmontel@mandrakesoft.com> 0.99.1-1mdk
- Update code (0.99.1)

* Mon Sep 24 2001 Laurent MONTEL <lmontel@mandrakesoft.com> 0.99-1mdk
- Update code (0.99)

* Wed Sep 12 2001 Laurent MONTEL <lmontel@mandrakesoft.com> 0.96-3mdk
- Fix icon 

* Wed Sep 12 2001 Laurent MONTEL <lmontel@mandrakesoft.com> 0.96-2mdk
-Rebuild

* Tue Aug 28 2001 Lenny Cartier <lenny@mandrakesoft.com> 0.96-1mdk
- 0.96

* Thu Aug 23 2001 Etienne Faure <etienne@mandrakesoft.com> 0.94-1mdk
- updated from Thomas Leclerc <leclerc@linux-mandrake.com> 0.94-1mdk
	- version 0.94
	- add menu entry

* Wed Jul 18 2001 Lenny Cartier <lenny@mandrakesoft.com> 0.92-1mdk

- added in contribs by Thomas Leclerc <leclerc@linux-mandrake.com> :
        - version 0.92
	
* Tue Jul 10 2001 Thomas Leclerc <leclerc@linux-mandrake.com> 0.91-1mdk
- version 0.91
- remove matherr-patch (obsolete)

* Mon Jun 18 2001 Thomas Leclerc <leclerc@linux-mandrake.com> 0.9-1mdk
- initial mandrake release
- patch errors in libm usage

# end of file
