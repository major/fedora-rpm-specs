Summary: A chat program for multiple users
Name: ytalk
Version: 3.3.0
Release: 42%{?dist}
License: GPLv2+
URL: http://www.impul.se/ytalk/
Source: http://www.impul.se/ytalk/%{name}-%{version}.tar.bz2
Source1: ytalkrc
Patch1: ytalk-c99.patch
BuildRequires: make
BuildRequires:  gcc
BuildRequires: ncurses-devel

%description
The YTalk program is essentially a chat program for multiple users.
YTalk works just like the UNIX talk program and even communicates with
the same talk daemon(s), but YTalk allows for multiple connections
(unlike UNIX talk).  YTalk also supports redirection of program output
to other users as well as an easy-to-use menu of commands.

%prep
%autosetup

%build
%configure
make %{?_smp_mflags}

%install
#%makeinstall
make install DESTDIR=%{buildroot}
%files
%doc COPYING AUTHORS README
%{_bindir}/*
%{_mandir}/*/*
%config(noreplace) /etc/ytalkrc

%changelog
* Sat Jul 22 2023 Fedora Release Engineering <releng@fedoraproject.org> - 3.3.0-42
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Sat Jan 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 3.3.0-41
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 3.3.0-40
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Sat Jan 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 3.3.0-39
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 3.3.0-38
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Thu Jan 28 2021 Fedora Release Engineering <releng@fedoraproject.org> - 3.3.0-37
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.3.0-36
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Jan 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.3.0-35
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Mon Sep  9 2019 Florian Weimer <fweimer@redhat.com> - 3.3.0-34
- Fix building in C99 mode

* Sat Jul 27 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.3.0-33
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.3.0-32
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.3.0-31
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.3.0-30
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.3.0-29
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.3.0-28
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.3.0-27
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri Feb 05 2016 Fedora Release Engineering <releng@fedoraproject.org> - 3.3.0-26
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Jun 19 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.3.0-25
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Mon Aug 18 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.3.0-24
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.3.0-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.3.0-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Fri Feb 15 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.3.0-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sun Jul 22 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.3.0-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.3.0-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.3.0-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Tue Aug 11 2009 Ville Skyttä <ville.skytta@iki.fi> - 3.3.0-17
- Use bzipped upstream tarball.

* Mon Jul 27 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.3.0-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Tue Jun 30 2009 Mike McGrath <mmcgrath@redhat.com> 3.3.9-15
- Release bump for test build 

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.3.0-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Tue Feb 12 2008 Mike McGrath <mmcgrath@redhat.com> 3.3.9-12
- Rebuild for gcc43

* Thu Jan 24 2008 Mike McGrath <mmcgrath@redhat.com> - 3.3.9-11
- Release bump for rebuild (koji test)

* Thu Dec 13 2007 Mike McGrath <mmcgrath@redhat.com> - 3.3.9-10
- Release bump for rebuild (koji test)

* Wed Aug 22 2007 Mike McGrath <mmcgrath@redhat.com> - 3.3.0-9
- Release bump for rebuild for ppc32

* Wed Jul 25 2007 Jeremy Katz <katzj@redhat.com> - 3.3.0-8
- rebuild for toolchain bug

* Tue Jul 24 2007 Mike McGrath <mmcgrath@redhat.com> 3.3.0-7
- release bump and rebuild

* Sun Sep 10 2006 Mike McGrath <imlinux@gmail.com> 3.3.0-6
- Rebuild

* Sat May 20 2006 Mike McGrath <imlinux@gmail.com> 3.3.0-5
- Removed macros from 3.3.0-4 changelog

* Fri May 19 2006 Mike McGrath <imlinux@gmail.com> 3.3.0-4
- Changed makeinstall-strip to make install DESTDIR={buildroot}

* Wed Dec 21 2005 Mike McGrath <imlinux@gmail.com> 3.3.0-3
- Updated to version 3.3.0
- Upstream maintainer changed (from http://www.metawire.org/) 

* Mon Sep 13 2004 Tim Waugh <twaugh@redhat.com> 3.1.2-1
- 3.1.2 (bug #131845).

* Tue Jun 15 2004 Elliot Lee <sopwith@redhat.com>
- rebuilt

* Fri Feb 13 2004 Elliot Lee <sopwith@redhat.com>
- rebuilt

* Tue Jun 17 2003 Tim Waugh <twaugh@redhat.com> 3.1.1-14
- Rebuilt.

* Wed Jun 04 2003 Elliot Lee <sopwith@redhat.com>
- rebuilt

* Wed Jan 22 2003 Tim Powers <timp@redhat.com>
- rebuilt

* Tue Jan 21 2003 Tim Waugh <twaugh@redhat.com>
- Fix URL (bug #82342).

* Wed Nov 20 2002 Tim Powers <timp@redhat.com>
- rebuild in current collinst

* Fri Jun 21 2002 Tim Powers <timp@redhat.com>
- automated rebuild

* Thu May 23 2002 Tim Powers <timp@redhat.com>
- automated rebuild

* Wed Jan 09 2002 Tim Powers <timp@redhat.com>
- automated rebuild

* Tue Jul 24 2001 Tim Waugh <twaugh@redhat.com>
- Change Copyright: to License:.
- Build requires ncurses-devel (bug #49768).

* Thu May  3 2001 Tim Waugh <twaugh@redhat.com>
- Add URL tag (bug #35439).
- Synchronise description with specspo.

* Tue Feb 27 2001 Preston Brown <pbrown@redhat.com>
- don't own manpage dir

* Thu Jul 13 2000 Prospector <bugzilla@redhat.com>
- automatic rebuild

* Sun Jun 18 2000 Than Ngo <than@redhat.de>
- rebuilt in the new build environment
- FHS packaging.

* Sat May 27 2000 Ngo Than <than@redhat.de>
- update to 3.1.1
- put man pages to correct place
- cleanup specfile

* Wed Apr  5 2000 Bill Nottingham <notting@redhat.com>
- rebuild against current ncurses/readline

* Mon Feb 07 2000 Preston Brown <pbrown@redhat.com>
- rebuild to gzip man page

* Thu Sep 09 1999 Cristian Gafton <gafton@redhat.com>
- rebuild for 6.1 to get rod of bswap polution for i386

* Sun Mar 21 1999 Cristian Gafton <gafton@redhat.com> 
- auto rebuild in the new build environment (release 3)

* Wed Feb 24 1999 Preston Brown <pbrown@redhat.com>
- Injected new description and group.

* Sun Nov 22 1998 Preston Brown <pbrown@redhat.com>
- upgrade to ytalk 3.1

* Sat Oct 10 1998 Cristian Gafton <gafton@redhat.com>
- strip binary

* Sun Aug 16 1998 Jeff Johnson <jbj@redhat.com>
- build root

* Fri Apr 24 1998 Prospector System <bugs@redhat.com>
- translations modified for de, fr, tr

* Wed Apr 15 1998 Erik Troan <ewt@redhat.com>
- built against new ncurses

* Thu Jul 31 1997 Erik Troan <ewt@redhat.com>
- built against glibc
