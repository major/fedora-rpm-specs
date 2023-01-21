# THIS SPECFILE IS FOR F9+ ONLY!
# Sorry, it is just too different for conditionals to be worth it.

# Compile only atlantikdesigner
%define donotcompilelist doc kaddressbook-plugins kate kfile-plugins kicker-applets knewsticker-scripts konq-plugins ksig noatun-plugins renamedlgplugins

Name:    kdeaddons
Summary: K Desktop Environment - Plugins
Version: 3.5.10
Release: 32%{?dist}
License: GPLv2
Url: http://www.kde.org/
Source0: ftp://ftp.kde.org/pub/kde/stable/%{version}/src/%{name}-%{version}.tar.bz2
Patch0: kdeaddons-configure-c99.patch

BuildRequires:  gcc gcc-c++
BuildRequires: kdelibs3-devel >= %{version}
BuildRequires: kdegames3-devel >= %{version}
BuildRequires: make

%description
Plugins for some KDE applications.

%package atlantikdesigner
Summary: Atlantik Designer
Requires: kdelibs3 >= %{version}
Requires: kdegames3 >= %{version}
# directory ownership
Requires: hicolor-icon-theme

Obsoletes: kdeaddons-extras < %{version}-%{release}

%description atlantikdesigner
This package includes a game board designer for Atlantik.

%prep
%autosetup -p1 -n kdeaddons-%{version}

# Prevent rerunning autotools.
touch -r aclocal.m4 acinclude.m4 configure*

sed -i -e 's/-lkdegames//g' atlantikdesigner/designer/Makefile.in


%build
unset QTDIR || : ; . /etc/profile.d/qt.sh
export DO_NOT_COMPILE="%{donotcompilelist}"

%configure \
  --includedir=%{_includedir}/kde \
  --disable-rpath \
  --enable-new-ldflags \
  --disable-debug --disable-warnings \
  --disable-dependency-tracking --enable-final

make %{?_smp_mflags}


%install
rm -rf %{buildroot}

export DO_NOT_COMPILE="%{donotcompilelist}"
make install DESTDIR=%{buildroot}

# Stop check-rpaths from complaining about standard runpaths.
export QA_RPATHS=0x0001


%files atlantikdesigner
%doc README COPYING-DOCS atlantikdesigner/TODO
%{_bindir}/atlantikdesigner
%{_datadir}/apps/atlantikdesigner/
%{_datadir}/icons/hicolor/*/*/atlantikdesigner*
%{_datadir}/applications/kde/atlantikdesigner.desktop


%changelog
* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 3.5.10-32
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Sat Dec 17 2022 Florian Weimer <fweimer@redhat.com> - 3.5.10-31
- Port configure script to C99

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 3.5.10-30
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 3.5.10-29
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Tue Jul 27 2021 Than Ngo <than@redhat.com> - 3.5.10-28
- Fix FTBFS

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 3.5.10-27
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 3.5.10-26
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.5.10-25
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.5.10-24
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.5.10-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.5.10-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Mon Jul 23 2018 Than Ngo <than@redhat.com> - 3.5.10-21
- fixed FTBFS

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.5.10-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.5.10-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jan 11 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 3.5.10-18
- Remove obsolete scriptlets

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.5.10-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.5.10-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.5.10-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 3.5.10-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.5.10-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat May 02 2015 Kalev Lember <kalevlember@gmail.com> - 3.5.10-12
- Rebuilt for GCC 5 C++11 ABI change

* Sat Aug 16 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.5.10-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.5.10-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.5.10-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.5.10-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.5.10-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.5.10-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Mon Feb 07 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.5.10-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.5.10-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.5.10-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Wed Sep 17 2008 Kevin Kofler <Kevin@tigcc.ticalc.org> 3.5.10-2
- build without libkdegames.so symlink

* Sat Aug 30 2008 Kevin Kofler <Kevin@tigcc.ticalc.org> 3.5.10-1
- update to 3.5.10

* Fri Feb 15 2008 Kevin Kofler <Kevin@tigcc.ticalc.org> 3.5.9-1
- update to 3.5.9

* Sat Feb 09 2008 Kevin Kofler <Kevin@tigcc.ticalc.org> 3.5.8-5
- rebuild for GCC 4.3

* Fri Dec 14 2007 Kevin Kofler <Kevin@tigcc.ticalc.org> 3.5.8-4
- rename (yet again) to kdeaddons as there's no kdeaddons4
- 3.5.8
- change License to GPLv2
- bump Release to be greater than last full kdeaddons build
- kdeaddons-atlantikdesigner Obsoletes kdeaddons-extras

* Sat Jul 28 2007 Kevin Kofler <Kevin@tigcc.ticalc.org> 3.5.7-5
- fix post and postun scriptlets to run for the subpackage
- don't run update-desktop-database because no MIME types are touched

* Fri Jul 27 2007 Kevin Kofler <Kevin@tigcc.ticalc.org> 3.5.7-4
- rename (again) to kdeaddons3
- build (only) kdeaddons3-atlantikdesigner subpackage
- Conflicts with pre-KDE-4 kdeaddons-extras
- add Requires on hicolor-icon-theme for directory ownership
- remove Requires({pre,post}): ldconfig because no shared libs are shipped

* Tue Jul 17 2007 Kevin Kofler <Kevin@tigcc.ticalc.org> 3.5.7-3
- rename to atlantikdesigner
- package only atlantikdesigner, remove everything else
- change R/BR to kde{libs,games}3(-devel)
- add mkdir %%{buildroot} after the rm -rf %%{buildroot}

* Sat Jun 16 2007 Rex Dieter <rdieter[AT]fedoraproject.org> 3.5.7-2
- use versioned Obsoletes
- drop Conflicts: akregator

* Mon Jun 11 2007 Rex Dieter <rdieter[AT]fedoraproject.org> 3.5.7-1
- minor cleanups

* Thu Jun 07 2007 Than Ngo <than@redhat.com> - 3.5.7-0.1.fc7
- 3.5.7

* Mon Mar 12 2007 Than Ngo <than@redhat.com> - 3.5.6-4.fc7
- fix broken dependencies 

* Wed Mar 07 2007 Than Ngo <than@redhat.com> - 3.5.6-3.fc7
- %%doc COPYING-DOCS
- Requires(post,postun): xdg-utils

* Tue Feb 27 2007 Than Ngo <than@redhat.com> - 3.5.6-2.fc7
- cleanup specfile
- kde* package splitting in -extras
- fedora as metabar default setting

* Wed Feb 07 2007 Than Ngo <than@redhat.com> 3.5.6-1.fc7
- 3.5.6

* Thu Aug 10 2006 Than Ngo <than@redhat.com> 3.5.4-1
- rebuild

* Mon Jul 24 2006 Than Ngo <than@redhat.com> 3.5.4-0.pre1
- prerelease of 3.5.4 (from the first-cut tag)

* Wed Jul 12 2006 Jesse Keating <jkeating@redhat.com> - 3.5.3-2.1
- rebuild

* Tue Jun 06 2006 Than Ngo <than@redhat.com> 3.5.3-2
- BR on libtool, automake

* Tue Jun 06 2006 Than Ngo <than@redhat.com> 3.5.3-1
- update to 3.5.3

* Fri May 05 2006 Petr Rockai <prockai@redhat.com> - 3.5.2-2
- fix path to rgb.txt in kolourpicker (#174139)

* Thu Apr 06 2006 Than Ngo <than@redhat.com> 3.5.2-1
- update to 3.5.2

* Fri Feb 10 2006 Jesse Keating <jkeating@redhat.com> - 3.5.1-1.2
- bump again for double-long bug on ppc(64)

* Tue Feb 07 2006 Jesse Keating <jkeating@redhat.com> - 3.5.1-1.1
- rebuilt for new gcc4.1 snapshot and glibc changes

* Fri Feb 03 2006 Than Ngo <than@redhat.com> 3.5.1-1 
- 3.5.1

* Fri Dec 09 2005 Jesse Keating <jkeating@redhat.com>
- rebuilt

* Tue Nov 29 2005 Than Ngo <than@redhat.com> 3.5.0-1
- 3.5 final

* Tue Oct 25 2005 Than Ngo <than@redhat.com> 3.4.92-1
- update to KDE 3.5 beta 2

* Thu Oct 06 2005 Than Ngo <than@redhat.com> 3.4.91-1
- update to KDE 3.5 beta 1

* Tue Aug 09 2005 Than Ngo <than@redhat.com> 3.4.2-1
- update to 3.4.2

* Tue Jun 28 2005 Than Ngo <than@redhat.com> 3.4.1-1
- 3.4.1

* Tue Apr 05 2005 Than Ngo <than@redhat.com> 3.4.0-2
- xmms is removed in fc4, rebuild without xmms support

* Thu Mar 17 2005 Than Ngo <than@redhat.com> 3.4.0-1
- 3.4.0 release

* Sun Mar 06 2005 Than Ngo <than@redhat.com> 3.4.0-0.rc1.2
- rebuilt against gcc-4

* Tue Mar 01 2005 Than Ngo <than@redhat.com> 3.4.0-0.rc1.1
- 3.4.0 rc1

* Wed Feb 16 2005 Than Ngo <than@redhat.com> 3.3.92-0.1
- KDE 3.4 Beta2

* Tue Feb 08 2005 Than Ngo <than@redhat.com> 3.3.2-0.2
- disable vimpart

* Fri Dec 03 2004 Than Ngo <than@redhat.com> 3.3.2-0.1
- update to 3.3.2

* Mon Oct 18 2004 Than Ngo <than@redhat.com> 3.3.1-2
- rebuilt

* Wed Oct 13 2004 Than Ngo <than@redhat.com> 3.3.1-1
- update to 3.3.1

* Sun Sep 26 2004 Than Ngo <than@redhat.com> 3.3.0-2
- cleanup menu

* Thu Aug 19 2004 Than Ngo <than@redhat.com> 3.3.0-1
- update to 3.3.0 release

* Tue Aug 10 2004 Than Ngo <than@redhat.com> 3.3.0-0.1.rc2
- update to 3.3.0 rc2

* Tue Aug 10 2004 Than Ngo <than@redhat.com> 3.3.0-0.1.rc1
- update to 3.3 rc1
- remove unneeded patch file

* Mon Jun 28 2004 Than Ngo <than@redhat.com> 3.2.3-3
- add gcc34 patch

* Mon Jun 28 2004 Than Ngo <than@redhat.com> 3.2.3-2
- rebuilt

* Mon Jun 21 2004 Than Ngo <than@redhat.com> 3.2.3-1
- 3.2.3 release

* Tue Apr 13 2004 Than Ngo <than@redhat.com> 3.2.2-1
- 3.2.2 release

* Sun Mar 07 2004 Than Ngo <than@redhat.com> 3.2.1-1
- 3.2.1 release

* Tue Mar 02 2004 Elliot Lee <sopwith@redhat.com>
- rebuilt

* Tue Feb 24 2004 Than Ngo <than@redhat.com> 3.2.0-1.6
- gcc 3.4 build problem

* Tue Feb 17 2004 Than Ngo <than@redhat.com> 3.2.0-1.5
- fix typo bug, _smp_mflags instead smp_mflags

* Sat Feb 14 2004 Than Ngo <than@redhat.com> 3.2.0-1.4
- fix rpm file list

* Fri Feb 13 2004 Elliot Lee <sopwith@redhat.com>
- rebuilt

* Thu Feb 05 2004 Than Ngo <than@redhat.com> 3.2.0-0.3
- 3.2.0 release
- built against qt 3.3.0

* Mon Jan 19 2004 Than Ngo <than@redhat.com> 3.1.95-0.1
- KDE 3.2 RC1
- add correct requires

* Mon Dec 15 2003 Than Ngo <than@redhat.com> 3.1.94-0.4
- fixed dependencies problem

* Thu Dec 11 2003 Than Ngo <than@redhat.com> 3.1.94-0.3
- add missing kaddressbook config files

* Wed Dec 03 2003 Than Ngo <than@redhat.com> 3.1.94-0.2
- make atlantikdesigner as sub package,
  get rid of requires kdegames (bug #82742, #111323, #99375)

* Mon Dec 01 2003 Than Ngo <than@redhat.com> 3.1.94-0.1
- KDE 3.2 Beta2
- remove kdeaddons-3.1.93-typo.patch, which is in new upstream

* Thu Nov 27 2003 Than Ngo <than@redhat.com> 3.1.93-0.3
- fixed typo

* Thu Nov 27 2003 Than Ngo <than@redhat.com> 3.1.93-0.2
- get rid of rpath

* Tue Nov 11 2003 Than Ngo <than@redhat.com> 3.1.93-0.1
- KDE 3.2 Beta1
- cleanup specfile
- remove some unneeded patch files

* Thu Oct 23 2003 Than Ngo <than@redhat.com> 3.1.4-2
- rebuild

* Tue Sep 30 2003 Than Ngo <than@redhat.com> 3.1.4-1
- 3.1.4

* Wed Aug 13 2003 Than Ngo <than@redhat.com> 3.1.3-2
- rebuilt

* Sun Aug 03 2003 Than Ngo <than@redhat.com> 3.1.3-1
- 3.1.3

* Fri Jun 27 2003 Than Ngo <than@redhat.com> 3.1.2-4
- rebuilt

* Wed Jun 04 2003 Elliot Lee <sopwith@redhat.com>
- rebuilt

* Mon May 18 2003 Than Ngo <than@redhat.com> 3.1.2-2
- 3.1.2

* Wed Mar 19 2003 Than Ngo <than@redhat.com> 3.1.1-1
- 3.1.1

* Mon Feb 24 2003 Elliot Lee <sopwith@redhat.com>
- debuginfo rebuild

* Fri Feb 21 2003 Than Ngo <than@redhat.com> 3.1-3
- get rid of gcc path from dependency_libs

* Thu Feb 13 2003 Than Ngo <than@redhat.com> 3.1-2
- rebuild against new arts

* Mon Jan 27 2003 Than Ngo <than@redhat.com> 3.1-1
- 3.1 final
- cleanup specfile
- remove unneeded size_t check patch

* Thu Jan 23 2003 Tim Powers <timp@redhat.com> 3.1-0.6
- rebuild

* Tue Jan 14 2003 Thomas Woerner <twoerner@redhat.com> 3.1-0.5
- removed size_t check
- excluded ia64

* Mon Jan 13 2003 Thomas Woerner <twoerner@redhat.com> 3.1-0.4
- rc6
- added atlantikdesignerui.rc

* Tue Jan 07 2003 Elliot Lee <sopwith@redhat.com> 3.1-0.3
- Don't exclude Alpha "temporarily"

* Sat Dec 28 2002 Than Ngo <than@redhat.com> 3.1-0.2
- disable smp_flags

* Wed Nov 27 2002 Than Ngo <than@redhat.com> 3.1-0.1
- update to 3.1 rc4
- get rid of sub packages

* Sun Nov 10 2002 Than Ngo <than@redhat.com> 3.0.5-1
- update to 3.0.5

* Thu Nov  7 2002 Than Ngo <than@redhat.com> 3.0.4-2
- fix some build problem
- umask of 077 issue (bug #73946)

* Tue Oct 15 2002 Than Ngo <than@redhat.com> 3.0.4-1
- 3.0.4

* Wed Sep 11 2002 Than Ngo <than@redhat.com> 3.0.3-1.1
- clean up specfile

* Mon Aug 12 2002 Than Ngo <than@redhat.com> 3.0.3-1
- 3.0.3
- don't strip binaries

* Tue Jul 23 2002 Tim Powers <timp@redhat.com> 3.0.2-3
- build using gcc-3.2-0.1

* Sat Jul 20 2002 Than Ngo <than@redhat.com> 3.0.2-2
- fix desktop files issue

* Wed Jul 10 2002 Than Ngo <than@redhat.com> 3.0.2-1
- 3.0.2
- use desktop-file-install

* Fri Jun 21 2002 Tim Powers <timp@redhat.com>
- automated rebuild

* Thu May 23 2002 Tim Powers <timp@redhat.com>
- automated rebuild

* Tue May 14 2002 Bernhard Rosenkraenzer <bero@redhat.com> 3.0.1-1
- 3.0.1

* Wed Apr 17 2002 Bernhard Rosenkraenzer <bero@redhat.com> 3.0.0-4
- BuildRequire the correct version of kdemultimedia

* Tue Apr 16 2002 Bernhard Rosenkraenzer <bero@redhat.com> 3.0.0-3
- Rebuild

* Wed Mar 27 2002 Bernhard Rosenkraenzer <bero@redhat.com> 3.0.0-1
- 3.0.0 final

* Sat Mar  9 2002 Tim Powers <timp@redhat.com>
- change kdemultimedia-noatun requirement to noatun

* Fri Mar  8 2002 Bernhard Rosenkraenzer <bero@redhat.com> 3.0.0-0.cvs20020308.1
- Update
- Adapt spec file to changes
- Exclude alpha temporarily

* Thu Jan 31 2002 Tim Powers <timp@redhat.com>
- knewsticker should require kdenetwork-libs and not kdenetwork

* Tue Jan 29 2002 Bernhard Rosenkraenzer <bero@redhat.com> 3.0.0-0.cvs20020129.1
- Update

* Tue Jul 24 2001 Bernhard Rosenkraenzer <bero@redhat.com> 2.2-0.cvs20010724.1
- Require kdemultimedia-devel >= 2.2 rather than just kdemultimedia-devel
- Update

* Mon Jul 23 2001 Bernhard Rosenkraenzer <bero@redhat.com> 2.2-0.cvs20010723.1
- Update
- Split in subpackages

* Thu Apr 26 2001 Bernhard Rosenkraenzer <bero@redhat.com>
- Initial release

