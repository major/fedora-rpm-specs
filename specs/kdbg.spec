Name: kdbg
Summary: A GUI for gdb, the GNU debugger, and KDE
Version: 3.1.0
Release: 5%{?dist}
Epoch: 1
Source: http://download.sourceforge.net/kdbg/%{name}-%{version}.tar.gz
# No version specified.
License: GPL-1.0-or-later
URL: http://www.kdbg.org/

Requires: gdb
Requires: xterm

BuildRequires: qt5-qtbase-devel
BuildRequires: kf5-rpm-macros
BuildRequires: kf5-ki18n-devel
BuildRequires: kf5-kconfig-devel
BuildRequires: kf5-kiconthemes-devel
BuildRequires: kf5-kxmlgui-devel
BuildRequires: kf5-kwindowsystem-devel
BuildRequires: extra-cmake-modules
BuildRequires: desktop-file-utils
BuildRequires: gettext
BuildRequires: make

%description
KDbg is a K Desktop Environment (KDE) GUI for gdb, the GNU debugger.
KDbg provides the programmer with an intuitive interface for setting
breakpoints, inspecting variables, and stepping through code. KDbg
requires X and KDE to be installed in order to run.

%prep
%setup -q

%build
# don't install icons, which are included in oxygen-icon-theme
rm -f kdbg/pics/*action-debug-run*

%cmake_kf5

%cmake_build

%install
%cmake_install

%find_lang %{name}

%files -f %{name}.lang
%doc BUGS COPYING README TODO ReleaseNotes-*
%config (noreplace) /etc/xdg/kdbgrc
%{_bindir}/*
%{_datadir}/kxmlgui5/%{name}
%{_datadir}/applications/*
%{_kf5_datadir}/%{name}
%{_datadir}/icons/*/*/*/*
%lang(de) %{_docdir}/HTML/de/%{name}
%lang(en) %{_docdir}/HTML/en/%{name}
%lang(ru) %{_docdir}/HTML/ru/%{name}

%changelog
* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1:3.1.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1:3.1.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Wed Jan 24 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1:3.1.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1:3.1.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Mon Dec 04 2023 Than Ngo <than@redhat.com> - 3.1.0-1
- 3.1.0

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1:3.0.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Tue Feb 21 2023 Than Ngo <than@redhat.com> - 1:3.0.1-4
- migrated to SPDX license

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1:3.0.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1:3.0.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon May 30 2022 Than Ngo <than@redhat.com> - 3.0.1-1
- bz#1787789, update to 3.0.1

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1:3.0.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1:3.0.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1:3.0.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1:3.0.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1:3.0.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1:3.0.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1:3.0.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1:3.0.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Mon Jun 11 2018 Than Ngo <than@redhat.com> - 3.0.0-1
- update to 3.0.0

* Fri Feb 09 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 1:2.5.5-12
- Escape macros in %%changelog

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1:2.5.5-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jan 18 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 1:2.5.5-10
- Remove obsolete scriptlets

* Thu Jan 11 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 1:2.5.5-9
- Remove obsolete scriptlets

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1:2.5.5-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1:2.5.5-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1:2.5.5-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Tue Feb 16 2016 Than Ngo <than@redhat.com> - 1:2.5.5-5
- FTBFS in rawhide
- fix build issue with cmake

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1:2.5.5-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1:2.5.5-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat May 02 2015 Kalev Lember <kalevlember@gmail.com> - 1:2.5.5-2
- Rebuilt for GCC 5 C++11 ABI change

* Thu Feb 26 2015 Than Ngo <than@redhat.com> 2.5.5-1
- 2.5.5

* Sat Aug 16 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1:2.5.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1:2.5.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Thu Feb 27 2014 Lukáš Tinkl <ltinkl@redhat.com> - 1:2.5.4-1
- update to latest stable release 2.5.4
- fixes rhbz#879328: can't open any executable

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1:2.5.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1:2.5.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Thu Dec 13 2012 Than Ngo <than@redhat.com> - 1:2.5.2-1
- 2.5.2
- add requirement on xterm for program output

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1:2.5.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Tue Jan 24 2012 Than Ngo <than@redhat.com> - 2.5.1-1
- 2.5.1

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1:2.1.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Mon Feb 07 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1:2.1.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Mon Aug 10 2009 Ville Skyttä <ville.skytta@iki.fi> - 1:2.1.1-3
- Convert specfile to UTF-8.

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1:2.1.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Fri Feb 27 2009 Than Ngo <than@redhat.com> - 2.1.1-1
- 2.1.1
- fix build issue against gcc-4.4

* Tue Aug  5 2008 Tom "spot" Callaway <tcallawa@redhat.com> 2.1.0-3
- fix license tag

* Fri Feb 15 2008 Than Ngo <than@redhat.com> 2.1.0-2
- rebuilt against gcc 4.3

* Tue Jan 08 2008 Than Ngo <than@redhat.com> 2.1.0-1
- 2.1.0

* Mon Mar 12 2007 Than Ngo <than@redhat.com> - 1:2.0.5-2.fc7
- cleanup specfile

* Wed Mar 07 2007 Than Ngo <than@redhat.com> - 1:2.0.5-1.fc7
- 2.0.5

* Wed Jul 12 2006 Jesse Keating <jkeating@redhat.com> - 1:2.0.2-1.2.1
- rebuild

* Fri Feb 10 2006 Jesse Keating <jkeating@redhat.com> - 1:2.0.2-1.2
- bump again for double-long bug on ppc(64)

* Tue Feb 07 2006 Jesse Keating <jkeating@redhat.com> - 1:2.0.2-1.1
- rebuilt for new gcc4.1 snapshot and glibc changes

* Fri Dec 16 2005 Than Ngo <than@redhat.com> 1:2.0.2-1
- update to 2.0.2

* Fri Dec 09 2005 Jesse Keating <jkeating@redhat.com>
- rebuilt

* Tue Nov 15 2005 Than Ngo <than@redhat.com> 1:2.0.0-2 
- fix for modular X

* Mon Jul 18 2005 Than Ngo <than@redhat.com> 1:2.0.0-1
- 2.0.0

* Sat Mar 05 2005 Than Ngo <than@redhat.com> 1:1.2.10-2
- rebuilt

* Wed Feb 09 2005 Than Ngo <than@redhat.com> 1.2.10-1
- 1.2.10
- drop kdbg-1.2.9-warning.patch, it's included in new upstream

* Tue Jun 15 2004 Elliot Lee <sopwith@redhat.com>
- rebuilt

* Thu May 13 2004 Than Ngo <than@redhat.com> 1.2.9-5
- get rid of rpath
- add correct smp flags

* Fri Feb 13 2004 Elliot Lee <sopwith@redhat.com>
- rebuilt

* Tue Feb 03 2004 Than Ngo <than@redhat.com> 1.2.9-3 
- added patch file from Marcelo Roberto

* Thu Nov 27 2003 Than Ngo <than@redhat.com> 1:1.2.9-2
- rebuild against KDE 3.2

* Tue Sep 09 2003 Than Ngo <than@redhat.com> 1:1.2.9-1
- 1.2.9

* Tue Aug 12 2003 Than Ngo <than@redhat.com> 1:1.2.8-3
- rebuilt

* Tue Aug 12 2003 Than Ngo <than@redhat.com> 1:1.2.8-2
- rebuilt

* Wed Jun 25 2003 Than Ngo <than@redhat.com> 1.2.8-1
- 1.2.8

* Wed Jun 04 2003 Elliot Lee <sopwith@redhat.com>
- rebuilt

* Wed May  7 2003 Than Ngo <than@redhat.com> 1.2.7-1
- 1.2.7

* Wed Jan 22 2003 Tim Powers <timp@redhat.com>
- rebuilt

* Mon Dec  9 2002 Than Ngo <than@redhat.com> 1.2.6-1
- update to 1.2.6
- use %%configure
- remove a patch file, which is in new upstream

* Sun Nov 10 2002 Than Ngo <than@redhat.com> 1.2.4-10.1
- clean up specfile

* Mon Aug 12 2002 Tim Powers <timp@redhat.com>
- rebuilt with gcc-3.2

* Tue Jul 23 2002 Than Ngo <than@redhat.com> 1.2.4-8
- fixed desktop file issue
- rebuild against gcc-3.2-0.1

* Tue Jul 09 2002 Than Ngo <than@redhat.com> 1.2.4-7
- use desktop-file-install

* Fri Jun 21 2002 Tim Powers <timp@redhat.com>
- automated rebuild

* Thu May 23 2002 Tim Powers <timp@redhat.com>
- automated rebuild

* Tue Apr 16 2002 Than Ngo <than@redhat.com> 1.2.4-4
- rebuild

* Thu Mar  7 2002 Than Ngo <than@redhat.com> 1.2.4-3
- fix to build in new enviroment

* Mon Jan 21 2002 Than Ngo <than@redhat.com> 1.2.4-1
- update to 1.2.4
- fix to build against kde3

* Fri Dec  7 2001 Than Ngo <than@redhat.com> 1.2.2-1
- update to 1.2.2, a stable release
- add missing po files bug #55957

* Tue Aug 14 2001 Than Ngo <than@redhat.com> 1.2.1-5
- add patch from leon@geon.donetsk.ua fixing broken russian desktop file (bug #51645)

* Tue Jul 24 2001 Bernhard Rosenkraenzer <bero@redhat.com> 1.2.1-4
- Rebuild with new kdelibs, remove kdesupport dependency

* Sun Jun 24 2001 Than Ngo <than@redhat.com>
- add buildprereq

* Wed Jun 20 2001 Than Ngo <than@redhat.com>
- rebuild in new enviroment

* Sun Apr 29 2001 Than Ngo <than@redhat.com>
- update to 1.2.1
- use %%lang

* Wed Feb 28 2001 Trond Eivind Glomsrød <teg@redhat.com>
- rebuild

* Tue Dec 26 2000 Than Ngo <than@redhat.com>
- fixed dependency with kde-i18n

* Mon Dec 25 2000 Bernhard Rosenkraenzer <bero@redhat.com>
- 1.2.0
- bzip2 source

* Sun Nov 12 2000 Than Ngo <than@redhat.com>
- update to 1.1.7beta1
- build with kde2 final

* Wed Aug 2 2000 Tim Powers <timp@redhat.com>
- rebuilt against libpng-1.0.8
 
* Wed Aug 02 2000 Than Ngo <than@redhat.de>
- move back to powertools (kde1 ist now installed as default)
- rebuilt against the kde1
 
* Sun Jun 11 2000 Than Ngo <than@redhat.de>
- rebuild for 7.0
- use %%configure
- FHS fxies
- clean up specfile
- fix to build against new libstdc++
 
* Tue Feb 22 2000 Preston Brown <pbrown@redhat.com>
- fix kde_htmldir
 
* Thu Jan 13 2000 Ngo Than <than@redhat.de>
- updated to 1.0.2

* Fri Sep 10 1999 Preston Brown <pbrown@redhat.com>
- built for KDE 1.1.2 / RHL 6.1.

* Wed Apr 21 1999 Preston Brown <pbrown@redhat.com>
- initial RPM for PowerTools 6.0







