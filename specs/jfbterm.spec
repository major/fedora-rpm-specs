# Don't provide any font Provides
%global	__fontconfig_provides	%{nil}
# ... and it seems that the above method no longer works
# on F-15 (bug 677760)
%global	__font_provides	%{nil}

Summary:   Japanese Console for Linux Frame Buffer Device
Name:      jfbterm
Version:   0.4.7
Release:   59%{?dist}
# COPYING		BSD-2-Clause
# SPDX confirmed
License:   BSD-2-Clause
Source0:   http://downloads.sourceforge.jp/jfbterm/13501/jfbterm-%{version}.tar.gz
Patch0:    jfbterm-0.4.6-conf.patch
#Patch1:    jfbterm-0.4.6-Makefile.patch
Patch1:    jfbterm-0.4.7-remove-sticky.patch
#Patch2:   jfbterm-0.4.6-x86_64.patch
Patch3:    jfbterm-0.4.7-infinite_loop.patch
# What is patch4 for??
#Patch4:    jfbterm-0.4.7-configure-header.patch
Patch5:    jfbterm-0.4.7-userspace.patch
Patch10:   jfbterm-0.4.7-remove-warning.patch
Patch11:   jfbterm-0.4.7-mmap-newkernel.patch
Patch12:   jfbterm-0.4.7-hang-onexit.patch
Patch13:   jfbterm-0.4.7-pagemask_userspace.patch
# Some people see jfbterm hang or segv with invalid ut_id
# (bug 698532)
Patch15:   jfbterm-0.4.7-hang-on-utmp-refresh-with-invalid-utid.patch
Patch16:   jfbterm-0.4.7-wrong-inline-gcc5.patch
Patch17:   jfbterm-configure-c99.patch

URL:         http://jfbterm.sourceforge.jp/

BuildRequires:   gcc
BuildRequires:   gzip
# BuildRequires:   autoconf
# for tic
BuildRequires:   ncurses
# Now efont-unicode-bdf is split.
BuildRequires:   efont-unicode-bdf
BuildRequires:   xorg-x11-fonts-misc
BuildRequires:   japanese-bitmap-fonts
BuildRequires:   jisksp16-1990-fonts
BuildRequires:   make
# Now fonts are symlinks so really these rpms are required.
#Requires:   efont-unicode-bdf
#Requires:   xorg-x11-fonts-base
#Requires:   xorg-x11-fonts-misc
#Requires:   japanese-bitmap-fonts

%description
JFBTERM/ME takes advantages of framebuffer device that is 
supported since linux kernel 2.2.x (at least on ix86 architecture) 
and make it enable to display multilingual text on console. 
It is developed on ix86 architecture, and it will works on 
other architectures such as linux/ppc.

Features:
   * It works with framebuffer device instead of VGA.
   * It supports pcf format font
   * It is not so fast because it doesn't take any advantages 
     of accelaration.
   * It also support coding systems other than ISO-2022, 
     such as SHIFT-JIS by using iconv(3).
   * It is userland program.

%prep
%setup -q
%patch -P0 -p1 -b .conf
%patch -P1 -p1 -b .remove_sticky
%patch -P5 -p1 -b .userspace
%patch -P3 -p1 -b .infinite_loop
# ???
#%%patch4 -p1 -b .conf_header
%patch -P10 -p1 -b .remove_warn
%patch -P11 -p1 -b .nmap_newkernel
%patch -P12 -p1 -b .hang_onexit
%patch -P13 -p1 -b .pagemask
%patch -P15 -p1 -b .utid_with_refresh
%patch -P16 -p1 -b .inline_gcc5
%patch -P17 -p1

#autoconf
touch Makefile.in aclocal.m4 config.h.in configure stamp-h.in

%build
# Copy fonts for a moment.
cp -p %{_datadir}/fonts/japanese/efont-unicode-bdf/b16.pcf.gz fonts/

%configure --enable-direct-color
touch stamp-h
%{__make} %{?_smp_mflags}

tic -C terminfo.jfbterm > jfbterm.termcap

%install
%{__rm} -rf %{buildroot}

%{__mkdir_p} %{buildroot}%{_sysconfdir}
%{__mkdir_p} %{buildroot}%{_datadir}/fonts/jfbterm

%{__make} DESTDIR=%{buildroot} install

%{__mv} %{buildroot}%{_sysconfdir}/jfbterm.conf.sample \
   %{buildroot}%{_sysconfdir}/jfbterm.conf

%{__mkdir_p} %{buildroot}%{_mandir}/man1
%{__mkdir_p} %{buildroot}%{_mandir}/man5
%{__install} -m 644 jfbterm.1 %{buildroot}%{_mandir}/man1
%{__install} -m 644 jfbterm.conf.5 %{buildroot}%{_mandir}/man5

%{__mkdir_p} %{buildroot}%{_datadir}/terminfo/j
tic -o %{buildroot}%{_datadir}/terminfo terminfo.jfbterm

# install fonts by symlink
# for fc5 and above, X11R6 directory is no longer used.
#%%{__rm} -rf %{buildroot}%{_datadir}/fonts/jfbterm/*

cp -p \
   %{_datadir}/fonts/japanese/efont-unicode-bdf/b16.pcf.gz \
   %{buildroot}%{_datadir}/fonts/jfbterm/

# For hanglg16, see https://bugzilla.redhat.com/show_bug.cgi?id=1952723
for font in \
   shnm8x16r.pcf.gz shnmk16.pcf.gz jisksp16-1990.pcf.gz \
   8x16.pcf.gz gb16fs.pcf.gz \
%if 0%{?fedora} < 34
   hanglg16.pcf.gz \
%endif
   ; do
   status=1
   for path in \
      %{_datadir}/fonts/japanese-bitmap-fonts \
      %{_datadir}/fonts/{japanese,ja}/misc \
      %{_datadir}/fonts/jisksp16-1990-fonts \
      %{_datadir}/fonts/jisksp16-1990 \
      %{_datadir}/fonts/japanese-bitmap \
      %{_datadir}/X11/fonts/misc \
       ; do
      if [ -f $path/$font -a $status = 1 ] ; then
         cp -p $path/$font %{buildroot}%{_datadir}/fonts/jfbterm/
         status=0
         break
      fi
   done
   if [ $status = 1 ] ; then exit 1 ; fi
done

status=1
for num in `seq 1 15` ; do
   font=8x13-ISO8859-${num}.pcf.gz
   path=%{_datadir}/X11/fonts/misc
   if [ -f $path/$font ] ; then
    cp -p $path/$font %{buildroot}%{_datadir}/fonts/jfbterm/
    status=0
   fi
done
if [ $status = 1 ] ; then exit 1 ; fi

%{__cat} > 60-jfbterm.perms <<EOF
# permission definitions
<console> 0660 /dev/tty0    0660 root
<console> 0600 /dev/console 0600 root
EOF

%{__mkdir_p} -m 755 %{buildroot}%{_sysconfdir}/security/console.perms.d
%{__install} -m 644 60-jfbterm.perms \
   %{buildroot}%{_sysconfdir}/security/console.perms.d/

# Change documents' fonts to UTF-8
%{__sed} -i -e 's|\r||' AUTHORS

for f in AUTHORS ChangeLog ; do
   %{__mv} ${f} ${f}.orig
   iconv -f ISO-2022-JP -t UTF8 ${f}.orig > ${f} && \
   %{__rm} -f ${f}.orig || %{__mv} ${f}.orig ${f}
done
%{__mv} README.ja README.ja.orig
iconv -f EUCJP -t UTF8 README.ja.orig > README.ja && \
   %{__rm} -f README.ja.orig || %{__mv} README.ja.orig README.ja

# Remove terminfo from FC-7
%{__rm} -rf %{buildroot}%{_datadir}/terminfo/

%files
%doc AUTHORS
%license COPYING
%doc ChangeLog
%doc NEWS
%doc README*
%doc jfbterm.termcap
%{_bindir}/jfbterm
%config(noreplace) %{_sysconfdir}/jfbterm.conf
%config(noreplace) %{_sysconfdir}/security/console.perms.d/60-jfbterm.perms
%{_datadir}/fonts/jfbterm
%dir %{_datadir}/fonts
%{_mandir}/man1/jfbterm.1*
%{_mandir}/man5/jfbterm.conf.5*

%changelog
* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.7-59
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.7-58
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Fri Feb 23 2024 Mamoru TASAKA <mtasaka@fedoraproject.org> - 0.4.7-57
- SPDX migration

* Wed Jan 24 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.7-56
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sat Jan 20 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.7-55
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.7-54
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Sun Apr 16 2023 Florian Weimer <fweimer@redhat.com> - 0.4.7-53
- Port configure script to C99

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.7-52
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Wed Nov 02 2022 Akira TAGOH <tagoh@redhat.com> - 0.4.7-51
- Replace old BR of fonts-japanese to japanese-bitmap-fonts.

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.7-50
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.7-49
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Mamoru TASAKA <mtasaka@fedoraproject.org> - 0.4.7-48
- Drop hanglg16 support for now (ref: bug 1952723)

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.7-47
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Mar 02 2021 Peter Hutterer <peter.hutterer@redhat.com> 0.4.7-46
- Drop BuildRequires for xorg-x11-fonts-base, it's the same package as
  xorg-x11-fonts-misc

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.7-45
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.7-44
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.7-43
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.7-42
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.7-41
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.7-40
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.4.7-39
- Escape macros in %%changelog

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.7-38
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.7-37
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.7-36
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.7-35
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.7-34
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4.7-33
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Mon Feb  9 2015 Mamoru Tasaka <mtasaka@fedoraproject.org> - 0.4.7-32
- Fix wrong usage of inline, which makes build failure with gcc5

* Sat Aug 16 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4.7-31
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4.7-30
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4.7-29
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4.7-28
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4.7-27
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Thu Jan  5 2012 Mamoru Tasaka <mtasaka@fedoraproject.org> - 0.4.7-26
- F-17: rebuild against gcc47

* Sat Apr 30 2011 Mamoru Tasaka <mtasaka@fedoraproject.org> - 0.4.7-25
- Attempt to fix hang or segv with invalid ut_id on wtmp refresh
  (bug 698532)

* Fri Feb 18 2011 Mamoru Tasaka <mtasaka@fedoraproject.org> - 0.4.7-24
- Change the method to kill virtual Provides related to font
  on F-15 (bug 677760)

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4.7-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Sat Jul 25 2009 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp> - 0.4.7-22
- F-12: Mass rebuild

* Sat Mar 28 2009 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp> - 0.4.7-21
- Font path again changed (on japanese-bitmap-fonts) ......

* Fri Mar 27 2009 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp> - 0.4.7-20
- F-11: rebuild, with suppressing font Provides (related to bug 491964)

* Tue Feb 24 2009 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp> - 0.4.7-19
- Again own %%{_datadir}/fonts on F-11+

* Mon Jul 28 2008 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp> - 0.4.7-18
- Fix Japanese font search path (F-10+: fonts-japanese renamed to 
  japanese-bitmap-fonts)
- %%{_datadir}/fonts is owned by filesystem (F-9+)

* Tue Apr  1 2008 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp> - 0.4.7-16
- Remove asm/page.h include, replaced by using sysconf

* Sat Feb  9 2008 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp>
- Rebuild against gcc43

* Mon Dec 17 2007 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp> - 0.4.7-15
- Supress gcc warning on 64 bits

* Sun Dec 16 2007 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp> - 0.4.7-14
- Remove previous workaround patch for glibc >= 2.7.90
- Remove unneeded autoconf call

* Mon Dec  3 2007 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp> - 0.4.7-13
- Add BR: jisksp16-1990-fonts due to fonts-japanese split
- Workarround for bug 408731

* Wed Aug 22 2007 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp> - 0.4.7-12
- Use sysconf instead of kernel-private PAGE_SIZE macro

* Wed Aug 22 2007 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp> - 0.4.7-10.dist.2
- Mass rebuild (buildID or binutils issue)

* Sun Dec 24 2006 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp> 0.4.7-10
- Properly own directories to remove ncurses dependency
- Remove terminfo on FC7+ (bug 220193)

* Mon Aug 28 2006 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp> 0.4.7-9
- Really copy font files, not use symlink to get rid of X requirement.
  (This package is aimed for CUI use, so X requirement is
   unwilling)

* Mon Aug 28 2006 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp> 0.4.7-8.1
- Rebuild for mass rebuild and kernel-headers
  (glibc-kernheaders removed).

* Sun Aug 20 2006 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp> 0.4.7-7
- Fix compilation problem on ppc.

* Sun Aug 20 2006 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp> 0.4.7-6
- Really require fonts as they are symlinks.

* Sun Aug 20 2006 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp> 0.4.7-5
- Install fonts required by relative symlinks.

* Thu Aug 15 2006 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp> 0.4.7-4
- Change the font search path.

* Thu Aug 10 2006 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp> 0.4.7-3
- Another attempt to remove sticky bit.
- Move the entry where we copy fonts needed.

* Thu Aug 10 2006 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp> 0.4.7-2
- Fix man page entry.

* Thu Aug 10 2006 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp> 0.4.7-1
- Strict dist to fc5 and above.
- Split efont-unicode-bdf to another rpm.

* Tue Aug  1 2006 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp> 0.4.7-0.15
- Clean up spec file and make some cosmetic change.
- Specify the correct licence.

* Tue Jul 25 2006 MACHIDA Hideki <h-machida@jc-c.co.jp> 0.4.7-0.9.1
- FIX: fc1 - fc3 font pathes.
- add console.perms file for not use sticky bit (fc4 or later).

* Tue Jul 25 2006 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp> 0.4.7-0.9
- Remove gcc compilation warning.
- Suppress mmap warning for linux >= 2.6.12 (this code is dead, perhaps?)
- Workarround for occasional hang on exit.
- Change Japanese documents coding to UTF-8.

* Tue Jul 25 2006 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp> 0.4.7-0.1
- Initial package for fc6 and fc5, based on srpm by Hideki Machida, initially
  by momonga linux project.

* Fri Mar 24 2006 MACHIDA Hideki <h@matchy.net> 0.4.7-matchy4
- for FedoraCore-5

* Tue Jun 14 2005 MACHIDA Hideki <h@matchy.net> 0.4.7-matchy3
- for FedoraCore-4

* Wed May 18 2005 MACHIDA Hideki <h@matchy.net> 0.4.7-matchy2
- add jfbterm-0.4.6-x86_64.patch and jfbterm-0.4.7-infinite_loop.patch
- from 0.4.7-1m (momonga-linux).

* Thu Feb 25 2005 MACHIDA Hideki <h@matchy.net> 0.4.7-matchy1
- update to 0.4.7.

* Thu Jan 27 2005 MACHIDA Hideki <h@matchy.net> 0.4.6-matchy6
- for release.

* Wed Jan 19 2005 MACHIDA Hideki <h@matchy.net> 0.4.6-matchy5.2
- add BuildPreReq: automake14, autoconf.

* Wed Jan 19 2005 MACHIDA Hideki <h@matchy.net> 0.4.6-matchy5
- use %%dist macro.

* Wed Jan 19 2005 MACHIDA Hideki <h@matchy.net> 0.4.6-matchy4
- add BuildPreReqs jisksp16-1990.

* Fri Dec 31 2004 MACHIDA Hideki <h@matchy.net> 0.4.6-matchy3
- fix debug package (Makefile patch).

* Wed Dec 29 2004 MACHIDA Hideki <h@matchy.net> 0.4.6-matchy2
- fix Packager and ChangeLog (^-^;)

* Tue Dec 28 2004 MACHIDA Hideki <h@matchy.net> 0.4.6-matchy1
- for FedoraCore-3 (from momonga-linux)
- add efont-unicode
- use tic.

* Wed Dec 15 2004 TAKAHASHI Tamotsu <tamo>
- (0.4.6-1m)

* Tue Apr  6 2004 Toru Hoshina <t@momonga-linux.org>
- (0.4.3-2m)
- not enumerate all of font file name.

* Tue Sep 16 2003 Kazuhiko <kazuhiko@fdiary.net>
- (0.4.3-1m)
- bugfixes

* Mon Sep 15 2003 Kazuhiko <kazuhiko@fdiary.net>
- (0.4.2-1m)
- include font files

* Thu May 29 2003 Shingo Akagaki <droa@kitty.dnsalias.org>
- (0.3.12-1m)
- version 0.3.12

* Fri Feb 15 2002 Tsutomu Yasuda <tom@kondara.org>
- (0.3.10-20k)
- update Source0 URL

* Tue May 22 2001 Toru Hoshina <toru@df-usa.com>
- (0.3.10-18k)

* Tue May  8 2001 MATSUDA, Daiki <dyky@df-usa.com>
- (0.3.10-16k)
- add termcap to PreReq tag

* Sun May  6 2001 MATSUDA, Daiki <dyky@df-usa.com>
- (0.3.10-14k)
- add PreReq tag for %%post section

* Tue Apr 17 2001 Tsutomu Yasuda <tom@digitalfactory.co.jp>
- applied gcc296 patch

* Sun Apr 15 2001 Toru Hoshina <toru@df-usa.com>
- revised spec file.
- add ppc support.
* Fri Oct 20 2000 Toru Hoshina <toru@df-usa.com>
- *Req*:tag never use ABS path

* Wed Jul 05 2000 Toru Hoshina <t@kondara.org>
- rebuild against glibc-2.1.90, X-4.0, rpm-3.0.5.

* Tue Apr 25 2000 Kenzi Cano <kc@furukawa.ch.kagu.sut.ac.jp>
- up to 0.3.10

* Wed Dec 01 1999 Motonobu Ichimura <famao@kondara.org>
- up to 0.3.7 

* Wed Nov 17 1999 Motonobu Ichimura <famao@kondara.org>
- up to 0.2.3

* Fri Nov 12 1999 Motonobu Ichimura <famao@kondara.org>
- up to 0.2.2

* Mon Nov 08 1999 Toru Hoshina <t@kondara.org>
- be a NoSrc :-P

* Sat Oct 23 1999 Motonobu Ichimura <famao@kondara.org>
- removed termcap and some changes added.
- not use terminfo.kon but terminfo.jfbterm

* Sat Oct 02 1999 Motonobu Ichimura <g95j0116@mn.waseda.ac.jp>
- first release
