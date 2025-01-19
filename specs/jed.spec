Summary: Fast, compact editor based on the S-Lang screen library
Name: jed
Version: 0.99.19
Release: 32%{?dist}
License: GPL-1.0-or-later
Source0: ftp://space.mit.edu/pub/davis/jed/v0.99/jed-0.99-19.tar.bz2
Patch1: jed-0.99.12-xkeys.patch
URL: http://www.jedsoft.org/jed/
Patch2: jed-etc.patch
Patch3: jed-multilib-newauto.patch
Patch4: jed-selinux.patch
Source1: selinux.c
Obsoletes: jed-common jed-xjed
Provides: jed-common jed-xjed
Requires: slang-slsh
BuildRequires:  gcc
BuildRequires: slang-devel >= 2.0, autoconf, libselinux-devel, procps
BuildRequires: make

%description
Jed is a fast, compact editor based on the S-lang screen library.  Jed
features include emulation of the Emacs, EDT, WordStar and Brief
editors; support for extensive customization with slang macros,
colors, keybindings; and a variety of programming modes with syntax
highlighting.

You should install jed if you've used it before and you like it, or if
you haven't used any text editors before and you're still deciding
what you'd like to use.

%prep
%setup -q -n jed-0.99-19
%patch -P1 -p1 -b .xkeys
%patch -P2 -p1
%if "%{_lib}" == "lib64"
%patch -P3 -p1
%endif
%patch -P4 -p1 -b .selinux
cp -p %{SOURCE1} src/

find doc -type f -exec chmod a-x {} \;

cd autoconf
autoconf
mv configure ..
cd ..

%build
export JED_ROOT="%{_datadir}/jed"
%configure
make

%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT

JED_ROOT=$RPM_BUILD_ROOT%{_datadir}/jed $RPM_BUILD_ROOT%{_bindir}/jed -batch -n -l preparse.sl </dev/null

# wait till jed finishes
while ps -C jed > /dev/null; do sleep 1; done

rm -f $RPM_BUILD_ROOT%{_mandir}/man*/rgrep*

rm -rf $RPM_BUILD_ROOT%{_datadir}/jed/doc/{txt,manual,README}
rm -rf $RPM_BUILD_ROOT%{_datadir}/jed/bin $RPM_BUILD_ROOT%{_datadir}/jed/info

sed -i "s|JED_ROOT|%{_datadir}/jed|g" $RPM_BUILD_ROOT/%{_mandir}/man1/jed.1

%files
%doc COPYING COPYRIGHT doc INSTALL INSTALL.unx README changes.txt
%{_bindir}/*
%{_mandir}/man1/jed.*
%{_datadir}/jed

%changelog
* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.99.19-32
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.99.19-31
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Mon Jun 17 2024 Miroslav Suchý <msuchy@redhat.com> - 0.99.19-30
- convert license to SPDX

* Wed Jan 24 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.99.19-29
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sat Jan 20 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.99.19-28
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.99.19-27
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Mon Jan 23 2023 Florian Weimer <fweimer@redhat.com> - 0.99.19-26
- Avoid implicit function declarations in selinux.c

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.99.19-25
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.99.19-24
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.99.19-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.99.19-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.99.19-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.99.19-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.99.19-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.99.19-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.99.19-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.99.19-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.99.19-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.99.19-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.99.19-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.99.19-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.99.19-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.99.19-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Aug 16 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.99.19-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.99.19-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.99.19-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.99.19-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.99.19-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.99.19-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.99.19-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Tue Dec 28 2010 Rakesh Pandit <rakesh@fedoraproject.org> - 0.99.19-2
- Added slang-slsh as require

* Sat Jan 16 2010 Rakesh Pandit <rakesh@fedoraproject.org> - 0.99.19-1
- Updated to latest 0.99.19
- Rebased all patches
- Included selinux.c in Makefile.in
- Fixed %%install jed command failure

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.99.18-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.99.18-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Mon Jun  2 2008 Bill Nottingham <notting@redhat.com> - 0.99.18-8
- fix for new autoconf (#449580)

* Thu Feb 14 2008 Bill Nottingham <notting@redhat.com> - 0.99.18-7
- rebuild for gcc-4.3

* Wed Oct 10 2007 Bill Nottingham <notting@redhat.com> - 0.99.18-6
- rebuild for buildid

* Fri Aug  3 2007 Bill Nottingham <notting@redhat.com>
- tweak license tag

* Tue Sep  5 2006 Bill Nottingham <notting@redhat.com> - 0.99.18-5
- rebuild!

* Mon Jun  5 2006 Bill Nottingham <notting@redhat.com> - 0.99.18-4
- get rid of rpath on x86_64
- remove install-info prereq
- add provides for things obsoleted

* Fri Jun  2 2006 Bill Nottingham <notting@redhat.com> - 0.99.18-3
- various spec cleanups (#189374)

* Tue May  9 2006 Bill Nottingham <notting@redhat.com> - 0.99.18-2
- don't do all the installation by hand
- get help files installed
- fix JED_ROOT references in man page
- make /etc/jed.rc (as specified in man page) work

* Tue Apr 18 2006 Bill Nottingham <notting@redhat.com> - 0.99.18-1
- update to 0.99.18

* Mon Feb 13 2006 Bill Nottingham <notting@redhat.com> - 0.99.17-0.pre135.3
- bump for rebuild

* Mon May  9 2005 Bill Nottingham <notting@redhat.com> 0.99.16-10
- don't forcibly strip binary, fixes debuginfo generation

* Fri Mar  4 2005 Bill Nottingham <notting@redhat.com> 0.99.16-8
- bump release

* Sun Feb 27 2005 Florian La Roche <laroche@redhat.com>
- Copyright: -> License

* Sat Sep 25 2004 Bill Nottingham <notting@redhat.com> 0.99.16-6
- add SELinux support

* Tue Jun 15 2004 Elliot Lee <sopwith@redhat.com>
- rebuilt

* Tue May  4 2004 Bill Nottingham <notting@redhat.com> 0.99.16-4
- remove info page (#115826)

* Fri Feb 13 2004 Elliot Lee <sopwith@redhat.com>
- rebuilt

* Wed Jun 04 2003 Elliot Lee <sopwith@redhat.com>
- rebuilt

* Thu May 22 2003 Bill Nottingham <notting@redhat.com> 0.99.16-1
- update to 0.99.16

* Wed Jan 22 2003 Tim Powers <timp@redhat.com>
- rebuilt

* Thu Dec 12 2002 Tim Powers <timp@redhat.com> 0.99.15-4
- rebuild on all arches

* Thu Jul 25 2002 Bill Nottingham <notting@redhat.com> 0.99.15-3
- obsolete xjed subpackage to help upgrades (ick)

* Wed Jul 24 2002 Bill Nottingham <notting@redhat.com> 0.99.15-2
- remove xjed subpackage, collapse -common into main package

* Mon Jun 24 2002 Bill Nottingham <notting@redhat.com> 0.99.15-1
- update to 0.99.15

* Fri Jun 21 2002 Tim Powers <timp@redhat.com>
- automated rebuild

* Fri Jun 14 2002 Bill Nottingham <notting@redhat.com> 0.99.14-5
- rebuild against new slang

* Thu May 23 2002 Tim Powers <timp@redhat.com>
- automated rebuild

* Wed Jan 09 2002 Tim Powers <timp@redhat.com>
- automated rebuild

* Fri Jul 20 2001 Bill Nottingham <notting@redhat.com>
- add buildprereq (#49505)

* Thu Jun 21 2001 Bill Nottingham <notting@redhat.com>
- update to 0.99.14

* Mon May 14 2001 Preston Brown <pbrown@redhat.com>
- rgrep is obsolete, package removed.

* Thu Dec 28 2000 Bill Nottingham <notting@redhat.com>
- do the long-needed update to 0.99 series

* Thu Jul 13 2000 Prospector <bugzilla@redhat.com>
- automatic rebuild

* Sat Jun 10 2000 Bill Nottingham <notting@redhat.com>
- rebuild, move the man pages, etc.

* Mon Feb 07 2000 Preston Brown <pbrown@redhat.com>
- wmconfig -> desktop

* Sat Feb 05 2000 Cristian Gafton <gafton@redhat.com>
- add info entry

* Thu Feb  3 2000 Bill Nottingham <notting@redhat.com>
- handle compressed man pages
- add install-info scripts

* Sun Mar 21 1999 Cristian Gafton <gafton@redhat.com>
- auto rebuild in the new build environment (release 2)

* Thu Oct 29 1998 Bill Nottingham <notting@redhat.com>
- update to 0.98.7 for Raw Hide
- split off lib stuff into jed-common

* Mon Oct  5 1998 Jeff Johnson <jbj@redhat.com>
- change rgep group tag, same as grep.

* Sat Aug 15 1998 Jeff Johnson <jbj@redhat.com>
- build root

* Thu May 07 1998 Prospector System <bugs@redhat.com>
- translations modified for de, fr, tr

* Wed Apr 15 1998 Erik Troan <ewt@redhat.com>
- built against new ncurses

* Mon Nov  3 1997 Michael Fulbright <msf@redhat.com>
- added wmconfig entry for xjed

* Tue Oct 21 1997 Michael Fulbright <msf@redhat.com>
- updated to 0.98.4
- included man pages in file lists

* Thu Jul 10 1997 Erik Troan <ewt@redhat.com>
- built against glibc
