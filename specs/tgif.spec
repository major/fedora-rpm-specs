Name:		tgif
Version:	4.2.5
Release:	33%{?dist}
Summary:	2-D drawing tool

# convkinput.c	HPND
# convxim.c	HPND
# rmcast/rmchat/rmchat.c	GPL-2.0-or-later	unused
# Overall	QPL-1.0
# SPDX confirmed
License:	QPL-1.0 AND HPND
URL:		http://bourbon.usc.edu/tgif/
Source0:	http://downloads.sourceforge.net/%{name}/%{name}-QPL-%{version}.tar.gz
# http://tyche.pu-toyama.ac.jp/~a-urasim/tgif/
Patch10:	tgif-textcursor-a-urasim.patch
# Check below later
Patch101:	tgif-QPL-4.1.45-size-debug.patch
Patch102:	tgif-QPL-4.2.5-format-security.patch
Patch103:	tgif-c99.patch
Patch104:	tgif-QPL-4.2.5-c23-prototype.patch

BuildRequires: make
BuildRequires:	gcc
BuildRequires:	imake
BuildRequires:	desktop-file-utils
BuildRequires:	gettext
BuildRequires:	libXmu-devel
BuildRequires:	libidn-devel
BuildRequires:	zlib-devel
Requires:	ghostscript
Requires:	netpbm-progs
Requires:	xorg-x11-fonts-75dpi
Requires:	xorg-x11-fonts-ISO8859-1-75dpi

%description
Tgif  -  Xlib based interactive 2-D drawing facility under
X11.  Supports hierarchical construction of  drawings  and
easy  navigation  between  sets  of drawings.  It's also a
hyper-graphics (or hyper-structured-graphics)  browser  on
the World-Wide-Web.

%prep
%setup -q -n %{name}-QPL-%{version}
# Upstream says the below is wrong, for now dropping
#%%patch10 -p0 -b textcursor
# Check later
#%%patch101 -p1 -b .size
%patch -P102 -p1 -b .format
%patch -P103 -p1 -b .c99
%patch -P104 -p1 -b .c23

%{__perl} -pi \
	-e 's,JISX-0208-1983-0,EUC-JP,g' \
	po/ja/ja.po
sed -i \
	-e 's|charset= koi8-r|charset=ISO-8859-1|' \
	po/fr/fr.po

# use scalable bitmap font
%{__sed} \
	-e s,alias\-mincho,misc\-mincho,g \
	-e s,alias\-gothic,jis\-fixed,g \
	-i po/ja/Tgif.ad

# Fix desktop file
%{__sed} -i.icon -e 's|Icon=tgif|Icon=tgificon|' \
	po/ja/tgif.desktop

# Fix installation path for icon files
%{__sed} -i.path \
	-e '/InstallNonExec.*hicolor/s|\$(TGIFDIR)|\$(DATADIR)/icons/|' \
	-e '/MakeDirectories.*hicolor/s|\$(TGIFDIR)|\$(DATADIR)/icons/|' \
	Imakefile

%build
%{__cp} -pf Tgif.tmpl-linux Tgif.tmpl
%{__sed} -i.mode -e 's|0664|0644|' Tgif.tmpl

xmkmf
%{__sed} -i.mode -e 's|0444|0644|' Makefile
DEFOPTS='-DOVERTHESPOT -DUSE_XT_INITIALIZE -D_ENABLE_NLS -DPRINT_CMD=\"lpr\" -DA4PAPER'
%{__make} %{?_smp_mflags} \
	CC="%{__cc} %{optflags}" \
	MOREDEFINES="$DEFOPTS" \
	TGIFDIR=%{_datadir}/tgif/ \
	LOCAL_LIBRARIES="-lXmu -lXt -lX11" \
	tgif

pushd po
xmkmf 
%{__sed} -i.mode -e 's|0444|0644|' Makefile
%{__make} \
	Makefile \
	Makefiles \
	depend \
	all
popd

%install
%{__rm} -rf $RPM_BUILD_ROOT/

%{__make} \
	DESTDIR=$RPM_BUILD_ROOT/ \
	BINDIR=%{_libexecdir}/ \
	TGIFDIR=%{_datadir}/tgif/ \
	INSTALLFLAGS="-cp" \
	DATADIR=%{_datadir} \
	install \
	install.man

# wrap tgif
%{__mkdir_p} $RPM_BUILD_ROOT%{_bindir}/
%{__install} -cpm 0755 po/ja/tgif-wrapper.sh \
	$RPM_BUILD_ROOT%{_bindir}/%{name}

%{__rm} -f $RPM_BUILD_ROOT%{_datadir}/tgif/*.obj
%{__install} -cpm 0644 *.obj \
	$RPM_BUILD_ROOT%{_datadir}/tgif/


# Japanese specific
%{__mkdir_p} $RPM_BUILD_ROOT%{_datadir}/X11/ja/app-defaults/
%{__install} -cpm 0644 \
	po/ja/Tgif.ad \
	$RPM_BUILD_ROOT%{_datadir}/X11/ja/app-defaults/Tgif

pushd po
%{__make} \
	DESTDIR=$RPM_BUILD_ROOT/ \
	INSTALLFLAGS="-cp" \
	install
popd

# desktop file & icon
%{__mkdir_p} $RPM_BUILD_ROOT%{_datadir}/applications/
desktop-file-install \
	--remove-category 'Application' \
	--remove-category 'X-Fedora' \
	--dir $RPM_BUILD_ROOT%{_datadir}/applications/ \
	po/ja/tgif.desktop


%{find_lang} tgif

%files -f %{name}.lang
%doc AUTHORS
%doc ChangeLog
%license Copyright
%doc HISTORY
%license LICENSE.QPL
%doc README*
%doc VMS_MAKE_TGIF.COM 
%doc example.tex 
%doc po/ja/README.jp

%{_bindir}/%{name}
%{_libexecdir}/%{name}
%{_mandir}/man1/%{name}.1x*

%{_datadir}/%{name}/
# Currently no package owns the following directories
%dir %{_datadir}/X11/ja/
%dir %{_datadir}/X11/ja/app-defaults/
%{_datadir}/X11/ja/app-defaults/Tgif

%{_datadir}/icons/hicolor/*/apps/%{name}icon.png
%{_datadir}/applications/*%{name}.desktop

%changelog
* Sun Jan 19 2025 Fedora Release Engineering <releng@fedoraproject.org> - 4.2.5-33
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Thu Jan 16 2025 Mamoru TASAKA <mtasaka@fedoraproject.org> - 4.2.5-32
- Support C23

* Sat Jul 20 2024 Fedora Release Engineering <releng@fedoraproject.org> - 4.2.5-31
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Sat Jan 27 2024 Fedora Release Engineering <releng@fedoraproject.org> - 4.2.5-30
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan  5 2024 Mamoru TASAKA <mtasaka@fedoraproject.org> - 4.2.5-29
- SPDX migration

* Sat Jul 22 2023 Mamoru TASAKA <mtasaka@fedoraproject.org> - 4.2.5-28
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild
- Fix fr.po encoding

* Sat Jan 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 4.2.5-27
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Nov 25 2022 Florian Weimer <fweimer@redhat.com> - 4.2.5-26
- Avoid implicit int for C99 compatibility (#2148487)

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 4.2.5-25
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Sat Jan 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 4.2.5-24
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 4.2.5-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 4.2.5-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 4.2.5-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Jan 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 4.2.5-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sat Jul 27 2019 Fedora Release Engineering <releng@fedoraproject.org> - 4.2.5-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 4.2.5-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 4.2.5-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Mar 07 2018 Adam Williamson <awilliam@redhat.com> - 4.2.5-16
- Rebuild to fix GCC 8 mis-compilation
  See https://da.gd/YJVwk ("GCC 8 ABI change on x86_64")

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 4.2.5-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jan 18 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 4.2.5-14
- Remove obsolete scriptlets

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 4.2.5-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 4.2.5-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 4.2.5-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri Feb 05 2016 Fedora Release Engineering <releng@fedoraproject.org> - 4.2.5-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Jun 19 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.2.5-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Mon Aug 18 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.2.5-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.2.5-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Wed Dec  4 2013 Mamoru TASAKA <mtasaka@fedoraproject.org> - 4.2.5-6
- Support -Werror=format-security

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.2.5-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Sat Feb  9 2013 Mamoru TASAKA <mtasaka@fedoraproject.org> - 4.2.5-4
- F-19: kill vendorization of desktop file (fpc#247)

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.2.5-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Thu Jan  5 2012 Mamoru Tasaka <mtasaka@fedoraproject.org> - 4.2.5-2
- F-17: rebuild against gcc47

* Thu Jun 30 2011 Mamoru Tasaka <mtasaka@fedoraproject.org> - 4.2.5-1
- 4.2.5

* Sun Jun 26 2011 Mamoru Tasaka <mtasaka@fedoraproject.org> - 4.2.4-1
- 4.2.4

* Wed Jun 01 2011 Mamoru Tasaka <mtasaka@fedoraproject.org> - 4.2.3-1
- 4.2.3

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.2.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Sat Nov 21 2009 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp> - 4.2.2-1
- 4.2.2

* Thu Oct 15 2009 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp> - 4.2.1-1
- Bug fix release 4.2.1

* Thu Oct  8 2009 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp> - 4.2-1
- Update to 4.2
  * Almost all patches/sources/etc in Fedora rpms (actually borrowed
    from Vine Project) were applied upstream
  * Stop to apply 1 left patch for now
  * 1 patch does not apply, check later

* Sat Jul 25 2009 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp> - 4.1.45-10
- F-12: Mass rebuild

* Tue Feb 24 2009 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp> - 4.1.45-9
- F-11: Mass rebuild

* Sat Nov 15 2008 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp> - 4.1.45-8
- Add fonts Requirement against xorg-x11-fonts-ISO8859-1-75dpi

* Fri Aug 29 2008 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp> - 4.1.45-7
- Fuzz up

* Mon Mar 17 2008 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp> - 4.1.45-6
- Require xorg-x11-fonts-75dpi
- Try to clean up size difference 
- Don't ship Japanese related Tgif.ad for non Japanese
  locale (may fix bug 436644, 427806?)

* Sat Feb  9 2008 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp>
- Rebuild against gcc43 (F-9)

* Wed Aug 22 2007 TASAKA Mamoru <mtasaka@ioa.s.u-tokyo.ac.jp> - 4.1.45-5
- Set mode explicitly when open(2) is used with O_CREAT
  due to recent glibc change

* Wed Aug 22 2007 TASAKA Mamoru <mtasaka@ioa.s.u-tokyo.ac.jp> - 4.1.45-4.dist.1
- Mass rebuild (buildID or binutils issue)

* Wed Jul 11 2007 MATSUURA Takanori <t.matsuu at gmail.com> - 4.1.45-4
- based on tgif-4.1.44-0vl6.src.rpm from VineSeed main
- use scalable bitmap font

* Mon Jul  9 2007 TASAKA Mamoru <mtasaka@ioa.s.u-tokyo.ac.jp> - 4.1.45-3
- Clean up BuildRequires

* Thu Jul  5 2007 TASAKA Mamoru <mtasaka@ioa.s.u-tokyo.ac.jp> - 4.1.45-2
- Explicitly set LANG=ja_JP.eucJP on ja_JP locale
- Add needed Requires

* Thu Jul  5 2007 TASAKA Mamoru <mtasaka@ioa.s.u-tokyo.ac.jp> - 4.1.45-1
- Clean up for Fedora

* Sat Apr 07 2007 MATSUBAYASHI Kohji <shaolin@vinelinux.org> 4.1.44-0vl6
- add Patch20 to fix problems with {scim,uim}-anthy (<BTS:512>)

* Thu Jan  4 2007 MATSUURA Takanori <t.matsuu at gmail.com> - 4.1.45-0vl5.1
- based on tgif-4.1.44-0vl5.src.rpm from VineSeed main
- update to 4.1.45
- some ajustments for Fedora Core

* Wed Dec 27 2006 KAZUKI SHIMURA <kazuki@ma.ccnw.ne.jp> 4.1.44-0vl5
- add tgificon.png (source4)
- update tgif.desktop (source3)

* Wed Oct 11 2006 Daisuke SUZUKI <daisuke@linux.or.jp> 4.1.44-0vl4
- add Patch10 to fix text cursor problem (<BTS:250>)
  http://tyche.pu-toyama.ac.jp/~a-urasim/tgif/

* Fri Sep 08 2006 KAZUKI SHIMURA <kazuki@ma.ccnw.ne.jp> 4.1.44-0vl3
- add and update desktop file (source3)
- move desktop file to %%{_datadir}/applications
- exec update-desktop-database at %%post,%%postun
- add Requires(post,postun): desktop-file-utils

* Sat Sep 02 2006 KAZUKI SHIMURA <kazuki@ma.ccnw.ne.jp> 4.1.44-0vl2
- add BuildRequires: XOrg-devel

* Mon Jan 17 2005 Daisuke SUZUKI <daisuke@linux.or.jp> 4.1.44-0vl1
- switch to QPL version

* Thu Jun 10 2004 KOBAYASHI R. Taizo <tkoba@vinelinux.org> 4.1.43-0vl1
- source update

* Thu Jun 12 2003 Ryoichi INAGAKI <ryo1@bc.wakwak.com> 4.1.42-0vl2
- rebuild with new toolchains

* Fri Mar 29 2002 Jun Nishii <jun@vinelinux.org> 4.1.41-0vl3
- add Tate-gaki entry for Ricoh fonts

* Sun Mar 17 2002 Shoji Matsumoto <shom@vinelinux.org> 4.1.41-0vl2
- refine Tgif.ad for Vine 2.5

* Fri Oct 19 2001 Jun Nishii <jun@vinelinux.org> 4.1.41-0vl1
- ver.up 

* Thu Jul 28 2001 Shoji Matsumoto <shom@vinelinux.org>
- 4.1.40-0vl2
- tgif-4.1ja6 (-aliastt-{mincho,gothic}- -> -alias-{mincho,gothic}-)

* Thu Dec  7 2000 Jun Nishii <jun@vinelinux.org>
- 4.1.40-0vl1

* Tue Oct  3 2000 Jun Nishii <jun@vinelinux.org>
- 4.1.39-0vl2
- added documents

* Sun Sep 10 2000 Jun Nishii <jun@vinelinux.org>
- 4.1.39-0vl1

* Thu Aug 17 2000 Yasuyuki Furukawa <furukawa@vinelinux.org>
- added overthespot_fix patch for XIM with OverTheSpot style.

* Fri Aug 11 2000 Jun Nishii <jun@vinelinux.org>
- 4.1.36-0vl1

* Mon Aug  7 2000 Jun Nishii <jun@vinelinux.org>
- 4.1.35-0vl1

* Sat Jul 15 2000 MATSUBAYASHI 'Shaolin' Kohji <shaolin@rhythmaning.org>
- 4.1.34-0vl2
- modified %%files section to handle compressed man page

* Mon May  8 2000 Jun Nishii <jun@vinelinux.org>
- updated 4.0.33

* Thu Apr 20 2000 Yasuyuki Furukawa <furukawa@vinelinux.org>
- updated 4.0.29
- modified fontcheck patch to check signgle byte font, too.

* Thu Mar  9 2000 Yasuyuki Furukawa <furukawa@vinelinux.org>
- updated 4.0.28

* Mon Feb 28 2000 Yasuyuki Furukawa <furukawa@vinelinux.org>
- updated 4.0.27

* Thu Feb 24 2000 Yasuyuki Furukawa <furukawa@vinelinux.org>
- added tgif wmconfig, desktop file

* Fri Feb 18 2000 Yasuyuki Furukawa <furukawa@vinelinux.org>
- added xim unofficial patch from fj.sources to fix a bug about XIM.

* Wed Feb 16 2000 Jun Nishii <jun@vinelinux.org>
- 4.1.26-0vl3
- bug fix in tgif-4.1.26-fontcheck.patch 

* Mon Feb 14 2000 Jun Nishii <jun@vinelinux.org>
- 4.1.26-0vl2
- merge tgif-4.1.26-fontcheck.patch by Mr. Yasuyuki Furukawa 
  which obsoletes trigger for Dynafonts and TrueTypeFonts !

* Thu Jan 20 2000 Jun Nishii <jun@vinelinux.org>
- 4.1.26-0vl2
- added trigger for Dynafonts and TrueTypeFonts

* Thu Jan 20 2000 Yasuyuki Furukawa <furukawa@vinelinux.org>
- updated to 4.1.26
- change ja resource from ja_JP.ujis/app-defaults to ja/app-defaults
- modified font setting

* Wed Nov 17 1999 Jun Nishii <jun@flatout.org>
- updated to 4.1.25

* Thu Nov 4 1999 Jun Nishii <jun@flatout.org>
- updated to 4.1.23

* Thu Oct 28 1999 Jun Nishii <jun@flatout.org>
- rel.4
- update ja.po
- more gettextize in choice.c and menu.c

* Wed Oct 27 1999 Jun Nishii <jun@flatout.org>
- rel.3 
- merge messages in strtbl.c and added japanese catalog

* Tue Oct 26 1999 Jun Nishii <jun@flatout.org>
- rel.2
- enable nls in status buffer and added japanese catalog

* Tue Oct 26 1999 Jun Nishii <jun@flatout.org>
- updated to 4.1.22

* Sun Aug 8 1999 Norihito Ohmori <ohmori@flatout.org>
- archive format change to bzip2
- rebuild for glibc-2.1.x

* Wed Jun 30 1999 Jun Nishii <jun@flatout.org>
- updated to 4.1.16

* Tue Apr 15 1999 Jun Nishii <jun@flatout.org>
- updated to 4.1.7

* Tue Apr 8 1999 Jun Nishii <jun@flatout.org>
- updated to 4.1.6
- Our menufontset-nls patch and xim patch were merged in original source!

* Tue Mar  9 1999 MATSUMOTO Shoji <vine@flatout.org>
- vertical font indicator bug fix
- modify resource and tgif.sh

* Mon Mar 8 1999 Jun Nishii <jun@flatout.org>
- updated to 4.1

* Mon Mar 8 1999 Jun Nishii <jun@flatout.org>
- bug fix in showing shortcut key in menu
- modify document

* Wed Mar  4 1999 MATSUMOTO Shoji <vine@flatout.org>
- set Tgif.InitialFont Ryumin

* Wed Mar  3 1999 MATSUMOTO Shoji <vine@flatout.org>
- add XIM OverTheSpot patch
- modify Tgif-ja.ad

* Mon Mar 2 1999 Jun Nishii <jun@flatout.org>
- updated to 4.0.18

* Mon Mar 1 1999 Jun Nishii <jun@flatout.org>
- make patch to support fontset and nls
- change version name as 4.0.17_jp 

* Sat Feb 27 1999 Jun Nishii <jun@flatout.org>
- modify Tgif-ja.ad (use A4,cm,color-icon,etc...)
- correct document

* Wed Feb 24 1999 Jun Nishii <jun@flatout.org>
- updated to ver. 4.0.17 
- make wrapper to read Tgif-ja

* Sat Feb 20 1999 Jun Nishii <jun@flatout.org>
- updated to ver. 4.0.16

* Tue Feb 16 1999 Jun Nishii <jun@flatout.org>
- build ver. 4.0.14 for Vine Linux
