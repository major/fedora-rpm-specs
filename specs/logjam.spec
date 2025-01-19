%global use_xmms 0

Name:		logjam
Version:	4.6.2
Release:	36%{?dist}
Epoch:		1
Summary:	GTK2 client for LiveJournal
License:	GPL-2.0-or-later
URL:		http://logjam.danga.com/
Source0:	http://andy-shev.github.com/LogJam/download/%{name}-%{version}.tar.bz2
# Alternately, we sometimes get source from git
# git clone git://github.com/martine/LogJam.git logjam-git
# find logjam-git -depth -name .git -type d -exec rm -rf {} \;
# tar cvfj logjam-git-20090824.tar.bz2 logjam-git/
# Source0:	logjam-git-20090824.tar.bz2
Requires:	curl >= 7.9, gtkspell
%if %{use_xmms}
BuildRequires:	xmms-devel
%endif
BuildRequires:	curl-devel, gtk2-devel, gtkspell-devel
# This is now a GTK3 component and we cannot use that.
# BuildRequires:	gtkhtml3-devel
BuildRequires:	gettext, desktop-file-utils, aspell-devel, librsvg2-devel
BuildRequires:	libsoup-devel, sqlite-devel, gnutls-devel, libgcrypt-devel
BuildRequires:	autoconf, automake, libtool, intltool, popt-devel, m4
BuildRequires:	dbus-devel, dbus-glib-devel, perl(YAML)
# These are long long ghosts
# Obsoletes:	loserjabber, logjam-gnome
Patch1:		logjam-4.4.1-fedora-desktop.patch
Patch2:		logjam-4.6.2-format-security-fix.patch
Patch3:		logjam-4.6.2-gcc10.patch
Patch4:		logjam-c99.patch
Patch5:		logjam-4.6.2-fix-verify-path-call.patch

%description
This is the new GTK2 client for LiveJournal (http://www.livejournal.com).

%if %{use_xmms}
%package xmms
Summary:	LogJam helper binary
Requires:	logjam, xmms
BuildRequires:	xmms-devel
BuildRequires: make

%description xmms
This is a helper binary for LogJam which is used to get the
current music from XMMS.
%endif

%prep
%setup -q
%patch -P1 -p1 -b .desktop
%patch -P2 -p1 -b .format-security
%patch -P3 -p1 -b .gcc10
%patch -P4 -p1
%patch -P5 -p1 -b .fix-verify-path-call

%build
touch NEWS README AUTHORS
%configure --with-sqlite3 \
%if %{use_xmms}
	--with-xmms
%else
	--without-xmms
%endif
make

%install
mkdir -p $RPM_BUILD_ROOT
make DESTDIR=$RPM_BUILD_ROOT install
# Rename locale dir, bugzilla 210206
if [ -d $RPM_BUILD_ROOT%{_datadir}/locale/en_US.UTF-8 ]; then
	mv $RPM_BUILD_ROOT%{_datadir}/locale/en_US.UTF-8 $RPM_BUILD_ROOT%{_datadir}/locale/en_US
fi
%find_lang %{name}
desktop-file-install \
  --dir $RPM_BUILD_ROOT%{_datadir}/applications         \
  --add-category X-Fedora                               \
  --delete-original					\
  $RPM_BUILD_ROOT/%{_datadir}/applications/logjam.desktop

%files -f %{name}.lang
%doc doc/README doc/TODO
%license COPYING
%{_bindir}/logjam
%{_mandir}/man1/logjam.1.gz
%{_datadir}/applications/*.desktop
%{_datadir}/pixmaps/logjam*

%if %{use_xmms}
%files xmms
%{_bindir}/logjam-xmms-client
%endif

%changelog
* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1:4.6.2-36
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1:4.6.2-35
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Sat Feb 10 2024 Tom Callaway <spot@fedoraproject.org> - 1:4.6.2-34
- fix license tag
- fix verify_path() call causing FTBFS

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1:4.6.2-33
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1:4.6.2-32
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1:4.6.2-31
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Apr 06 2023 Florian Weimer <fweimer@redhat.com> - 1:4.6.2-30
- Port to C99

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1:4.6.2-29
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1:4.6.2-28
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1:4.6.2-27
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1:4.6.2-26
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jun  1 2021 Tom Callaway <spot@fedoraproject.org> - 1:4.6.2-26
- disable xmms support
- remove gtkhtml3-devel BuildRequire, it was not being detected by configure anyway

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1:4.6.2-25
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1:4.6.2-24
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Jan 31 2020 Tom Callaway <spot@fedoraproject.org> - 1:4.6.2-23
- fix FTBFS

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1:4.6.2-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1:4.6.2-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1:4.6.2-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1:4.6.2-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 1:4.6.2-18
- Escape macros in %%changelog

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1:4.6.2-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1:4.6.2-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1:4.6.2-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1:4.6.2-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1:4.6.2-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Tue Jan 19 2016 Tom Callaway <spot@fedoraproject.org> - 1:4.6.2-12
- spec file cleanups

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1:4.6.2-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1:4.6.2-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1:4.6.2-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Wed Dec 04 2013 Tom Callaway <spot@fedoraproject.org> - 1:4.6.2-8
- fix format-security issues

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1:4.6.2-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Fri Apr 26 2013 Jon Ciesla <limburgher@gmail.com> - 1:4.6.2-6
- Drop desktop vendor tag.

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1:4.6.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1:4.6.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1:4.6.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Dec 06 2011 Adam Jackson <ajax@redhat.com> - 1:4.6.2-2
- Rebuild for new libpng

* Tue Jun  7 2011 Tom Callaway <spot@fedoraproject.org> - 1:4.6.2-1
- update to 4.6.2

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1:4.6.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Fri Feb  4 2011 Tom Callaway <spot@fedoraproject.org> - 1:4.6.1-1
- update to 4.6.1

* Mon Nov 29 2010 Tom "spot" Callaway <tcallawa@redhat.com> - 1:4.6.0-1
- update to 4.6.0

* Fri Jul  9 2010 Tom "spot" Callaway <tcallawa@redhat.com> - 1:4.5.3-39
- clean up MusicSource list, add banshee detection (Andy Shevchenko) (bz 574254)
- fix situation where outdated information is in logjam when 'last login' 
  dialogue is off (Andy Shevchenko) (bz 590291)
- update URL openers (Andy & spot) (bz 597705)
- add ability to refer to twitter account (Andy) (bz 597708)

* Thu Feb 18 2010 Tom "spot" Callaway <tcallawa@redhat.com> - 1:4.5.3-38
- dbus-glib-devel as BuildRequires in Fedora 13+

* Thu Feb 18 2010 Tom "spot" Callaway <tcallawa@redhat.com> - 1:4.5.3-37
- update Patch2, Patch12, Patch16 (Andy Shevchenko) (bz 556971)
- fix implicit DSO linking issue (bz 565012)

* Mon Aug 24 2009 Tom "spot" Callaway <tcallawa@redhat.com> - 1:4.5.3-36
- use properly formed user-agent string (Andy Shevchenko) (bz 518757)
- rebase to git master (bz 518758)
- Add Location support (Andy Shevchenko, from Ubuntu)
- Add link-by-nickname support (Andy Shevchenko, from FreeBSD)
- clean out merged patches

* Mon Aug 10 2009 Ville Skyttä <ville.skytta@iki.fi> - 1:4.5.3-35
- Convert specfile to UTF-8.

* Sat Jul 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1:4.5.3-34
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Mon Apr 27 2009 Tom "spot" Callaway <tcallawa@redhat.com> - 4.5.3-33
- conditionalize libtool fun for F10+

* Mon Apr 27 2009 Tom "spot" Callaway <tcallawa@redhat.com> - 4.5.3-32
- only move broken locale dir if it gets created

* Mon Apr 27 2009 Tom "spot" Callaway <tcallawa@redhat.com> - 4.5.3-31
- conditionalize libtool fun for F11+

* Mon Apr 27 2009 Tom "spot" Callaway <tcallawa@redhat.com> - 4.5.3-30
- rebuild with all patches in place

* Mon Apr 27 2009 Tom "spot" Callaway <tcallawa@redhat.com> - 4.5.3-29
- add support for lj-embed tags
- add support for MPRIS music detection (Andy Shevchenko)
- improve tag handling (Andy Shevchenko)

* Thu Apr  2 2009 Tom "spot" Callaway <tcallawa@redhat.com> - 4.5.3-28
- add patch to enable "keep drafts" functionality
  see: http://community.livejournal.com/logjam_dev/37274.html

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1:4.5.3-27
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Mon Feb 16 2009 Tom "spot" Callaway <tcallawa@redhat.com> - 4.5.3-26
- libtoolize to support newer libtool
- intltoolize so we get translations

* Mon Jul 28 2008 Tom "spot" Callaway <tcallawa@redhat.com> - 4.5.3-25
- fix docked behavior again (bz 447146)
- fix config option to start in dock again (bz 445998)
- fix patch8 to apply with fuzz=0
- add patch to enable/disable "logged in since" history popup as config option

* Tue Jul  1 2008 Tom "spot" Callaway <tcallawa@redhat.com> - 4.5.3-24
- fix ukranian translation (bz 447145)
- fix docked behavior (bz 447146)
- add close when send option (bz 447147)
- fix image resize sigsegv (bz 452170)

* Tue May 13 2008 Tom "spot" Callaway <tcallawa@redhat.com> - 4.5.3-23
- add explicit without-xmms conditional (bz 445996)
- add configuration option to start in dock (bz 445998)

* Tue Mar 18 2008 Tom "spot" Callaway <tcallawa@redhat.com> - 4.5.3-22
- re-enable threading where we really need it only

* Tue Mar 18 2008 Tom "spot" Callaway <tcallawa@redhat.com> - 4.5.3-21
- disable more threading

* Tue Mar 18 2008 Tom "spot" Callaway <tcallawa@redhat.com> - 4.5.3-20
- revert disable-threading patch

* Tue Mar 11 2008 Tom "spot" Callaway <tcallawa@redhat.com> - 4.5.3-19
- i'm going to beat autoconf

* Tue Mar 11 2008 Tom "spot" Callaway <tcallawa@redhat.com> - 4.5.3-18
- seriously, this is getting old now. added libtool to BR.

* Tue Mar 11 2008 Tom "spot" Callaway <tcallawa@redhat.com> - 4.5.3-17
- properly autotool

* Tue Mar 11 2008 Tom "spot" Callaway <tcallawa@redhat.com> - 4.5.3-16
- add Makefile.in bits to tags patch

* Tue Mar 11 2008 Tom "spot" Callaway <tcallawa@redhat.com> - 4.5.3-15
- fix tags patch

* Tue Mar 11 2008 Tom "spot" Callaway <tcallawa@redhat.com> - 4.5.3-14 
- missed one patch

* Tue Mar 11 2008 Tom "spot" Callaway <tcallawa@redhat.com> - 4.5.3-13
- disable unused threading on linux, resolves bz 435124
- enable tags support (bz 434754)
- add support for titles to links and images and links for images (bz 434754)
- set default spellcheck lang to en_US (en was the old default, but didn't work)

* Sat Feb 16 2008 Jesse Keating <jkeating@redhat.com> - 4.5.3-12
- Rebuild for new libsoup

* Wed Jan 30 2008 Tom "spot" Callaway <tcallawa@redhat.com> 1:4.5.3-11
- apply patch for new libsoup from bz 430966

* Tue Jan 29 2008 Tom "spot" Callaway <tcallawa@redhat.com> 1:4.5.3-10
- rebuild for new libsoup

* Thu Aug 23 2007 Tom "spot" Callaway <tcallawa@redhat.com> 1:4.5.3-9.2
- rebuild for BuildID, license fix (GPLv2+)

* Mon Mar 19 2007 Tom "spot" Callaway <tcallawa@redhat.com> 1:4.5.3-9.1
- rebuild for new gtkhtml, new patch to detect it

* Thu Jan 18 2007 Tom "spot" Callaway <tcallawa@redhat.com> 1:4.5.3-8
- Rename a locale directory to resolve bugzilla 210206

* Thu Jan 18 2007 Tom "spot" Callaway <tcallawa@redhat.com> 1:4.5.3-7
- fix rhythmbox music detection

* Mon Sep 11 2006 Tom "spot" Callaway <tcallawa@redhat.com> 1:4.5.3-5
- add docklet context menu patch
- fix BR: autoconf, intltool

* Fri Jun 16 2006 Tom "spot" Callaway <tcallawa@redhat.com> 1:4.5.3-4
- bump for gnutls change in devel

* Thu Apr  6 2006 Tom "spot" Callaway <tcallawa@redhat.com> 1:4.5.3-3
- fix gtkspell language settings, bz 186906

* Tue Mar  7 2006 Tom "spot" Callaway <tcallawa@redhat.com> 1:4.5.3-2
- update russian translations, bz 183619

* Tue Feb 28 2006 Tom "spot" Callaway <tcallawa@redhat.com> 1:4.5.3-1
- bump to 4.5.3

* Thu Jan  5 2006 Tom "spot" Callaway <tcallawa@redhat.com> 1:4.5.2-1
- bump to 4.5.2

* Tue Sep  6 2005 Tom "spot" Callaway <tcallawa@redhat.com> 1:4.5.1-5
- add BR: libgcrypt-devel

* Tue Sep  6 2005 Tom "spot" Callaway <tcallawa@redhat.com> 1:4.5.1-4
- add BR: gnutls-devel

* Tue Sep  6 2005 Tom "spot" Callaway <tcallawa@redhat.com> 1:4.5.1-3
- fc3 branch missing another patch

* Tue Sep  6 2005 Tom "spot" Callaway <tcallawa@redhat.com> 1:4.5.1-2
- fc3 branch missing a patch

* Tue Sep  6 2005 Tom "spot" Callaway <tcallawa@redhat.com> 1:4.5.1-1
- bump to 4.5.1

* Mon Jul 11 2005 Tom "spot" Callaway <tcallawa@redhat.com> 4.5-0.1patch8
- bump to patch8

* Thu Apr 14 2005 Tom "spot" Callaway <tcallawa@redhat.com> 4.4.1-8
- actually apply patch. :P

* Thu Apr 14 2005 Tom "spot" Callaway <tcallawa@redhat.com> 4.4.1-7
- touch up package included .desktop file and use it.

* Wed Apr  6 2005 Tom "spot" Callaway <tcallawa@redhat.com> 4.4.1-6
- Fix dual .desktop file issue

* Fri Mar 13 2005 Tom "spot" Callaway <tcallawa@redhat.com> 4.4.1-5
- Cleanups for compiler errors brought to light in Bugzilla 149865
- Change X-Fedora-Extras to X-Fedora

* Fri Feb 25 2005 Tom "spot" Callaway <tcallawa@redhat.com> 4.4.1-4
- Rebuilt for FC4/devel
- Replace Gtkhtml 3.1 patch with Gtkhtml 3.6 patch

* Thu Feb 10 2005 Tom "spot" Callaway <tcallawa@redhat.com> 4.4.1-3
- Bump to current version
- Compile fix patch is obsoleted
- Gtkhtml 3.1 patch changed for 4.4.1
- Adopt some changes from Kir Kolyshkin's package
  - Make xmms subpackage, with use_xmms conditional
  - Fix a segfault triggered by pressing "Copy URL" button in offline browser
  - Fix Russian localization
  - Adds support for Backdated: yes option in an offline logjam post file.
- BuildRequires: gettext, not gettext-devel

* Wed Feb  9 2005 Tom "spot" Callaway <tcallawa@redhat.com> 4.4.0-4
- use make, not %%__make
- no need to export CFLAGS first
- BuildRequires aspell-devel, desktop-file-utils
- change PreReq to Requires
- delete $RPM_BUILD_ROOT first
- use desktop-file-install to install logjam.desktop
- nuke Vendor and Packager lines
- add patch to look for gtkhtml3.1
- modify logjam.desktop to refer to X-Fedora-Extras
- add Comment and GenericName to logjam.desktop
- change Group to User Interface/Desktops

* Thu Feb  3 2005 Tom "spot" Callaway <tcallawa@redhat.com>
- fc3 cleanup

* Tue May 11 2004 Justin M. Forbes <64bit_fedora@comcast.net>
- bump to 4.4.0

* Tue Mar  9 2004 Tom "spot" Callaway <tcallawa@redhat.com>
- bump to 4.3.2
- install gtkhtml3-devel (whoops!)
- remove old xmms configure option

* Thu Feb  5 2004 Tom "spot" Callaway <tcallawa@redhat.com>
- bump to 4.3.0pre2
- Revert dash naming workaround

* Mon Feb  2 2004 Tom "spot" Callaway <tcallawa@redhat.com>
- bump to 4.3.0-pre1
- Workaround dash naming

* Wed Aug  6 2003 Tom "spot" Callaway <tcallawa@redhat.com>
- bump to 4.2.3
- Kylie Minogue does not approve.

* Wed Jun 11 2003 Tom "spot" Callaway <tcallawa@redhat.com>
- spec changes make sense once explained. :)
- bump to 4.2.0
- all old patches obsoleted
- added logjam desktop entry from Adam Konkle (modified slightly)

* Mon May 26 2003 Tom "spot" Callaway <tcallawa@redhat.com>
- added patches for a compilation fix and russian support
- modified spec. i still think its pointless, but whatever.

* Tue Apr 29 2003 Tom "spot" Callaway <tcallawa@redhat.com>
- bump to 4.1.2
- and i follow the tracks that lead me down, i'll never follow whats right

* Sat Apr 12 2003 Tom "spot" Callaway <tcallawa@redhat.com>
- bump to 4.1.1
- black velvet with that slow southern style

* Mon Apr  7 2003 Tom "spot" Callaway <tcallawa@redhat.com>
- bump to 4.1.0
- rebuilt against gtkspell 2.0.4

* Fri Dec  6 2002 Tom "spot" Callaway <tcallawa@redhat.com>
- bump to 4.0.1

* Tue Nov 19 2002 Tom "spot" Callaway <tcallawa@redhat.com>
- rebuilt against gtkspell 2.0.3
* Tue Oct 29 2002 Tom "spot" Callaway <tcallawa@redhat.com>
 - 4.0.0 official release
* Tue Oct 15 2002 Tom "spot" Callaway <tcallawa@redhat.com>
 - 3.1cvs20021015 release, removed patch0,1,3
* Sun May 26 2002 Tom "spot" Callaway <tcallawa@redhat.com>
 - 3.1cvs20020526 release, spec rewrite, lots of patching
* Mon Jan 07 2002 Tom "spot" Callaway <tcallawa@redhat.com>
 - 3.0.2 release, spec cleanups
* Mon Nov 12 2001 Tom "spot" Callaway <tcallawa@redhat.com>
 - 3.0.1 release, lots of new features/bugfixes.
* Fri Sep 07 2001 Tom "spot" Callaway <tcallawa@redhat.com>
 - Rebuild without ssl for compat. :~(
* Thu Sep 06 2001 Tom "spot" Callaway <tcallawa@redhat.com>
 - Removed curl-devel from the Prereq: to BuildRequires:
* Sat Jul 14 2001 Tom "spot" Callaway <tcallawa@redhat.com>
 - Point release, out of CVS finally
* Wed Jun 27 2001 Tom "spot" Callaway <tcallawa@redhat.com>
 - Compilation fixes. Window geometry saving patch (decklin). Autologin
 - Check for libcurl in configure. Fixed GtkSpell and position of metadata.
* Mon Jun 11 2001 Tom "spot" Callaway <tcallawa@redhat.com>
 - Timmay! Timmay! Gobbles! (Evan cleanups)
* Mon Jun 04 2001 Tom "spot" Callaway <tcallawa@redhat.com>
 - Client renamed to logjam, this adds some prereqs and needs more spec fixes.
* Tue May 15 2001 Tom "spot" Callaway <tcallawa@redhat.com>
 - Patch stripped. all livejournal.com urls removed in anticipation of rename
* Tue May 15 2001 Tom "spot" Callaway <tcallawa@redhat.com>
 - Many fixes, specific patch to fix proxy.
* Sun Mar 25 2001 Tom "spot" Callaway <tcallawa@redhat.com>
 - Added fix for James Manning, Web Links browser launch
* Tue Feb 13 2001 Tom "spot" Callaway <tcallawa@redhat.com>
 - Upgraded to add GNOME build option.
* Sun Oct 08 2000 Alexander Gräfe <nachtfalke@retrogra.de>
 - inital version of the RPM.
