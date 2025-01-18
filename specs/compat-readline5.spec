Summary: A library for editing typed command lines
Name: compat-readline5
Version: 5.2
Release: 50%{?dist}
License: GPL-2.0-or-later
URL: http://cnswww.cns.cwru.edu/php/chet/readline/rltop.html
Source: ftp://ftp.gnu.org/gnu/readline/readline-%{version}.tar.gz
Patch1: ftp://ftp.gnu.org/gnu/readline/readline-5.2-patches/readline52-001
Patch2: ftp://ftp.gnu.org/gnu/readline/readline-5.2-patches/readline52-002
Patch3: ftp://ftp.gnu.org/gnu/readline/readline-5.2-patches/readline52-003
Patch4: ftp://ftp.gnu.org/gnu/readline/readline-5.2-patches/readline52-004
Patch5: ftp://ftp.gnu.org/gnu/readline/readline-5.2-patches/readline52-005
Patch6: ftp://ftp.gnu.org/gnu/readline/readline-5.2-patches/readline52-006
Patch7: ftp://ftp.gnu.org/gnu/readline/readline-5.2-patches/readline52-007
Patch8: ftp://ftp.gnu.org/gnu/readline/readline-5.2-patches/readline52-008
Patch9: ftp://ftp.gnu.org/gnu/readline/readline-5.2-patches/readline52-009
Patch10: ftp://ftp.gnu.org/gnu/readline/readline-5.2-patches/readline52-010
Patch11: ftp://ftp.gnu.org/gnu/readline/readline-5.2-patches/readline52-011
Patch12: ftp://ftp.gnu.org/gnu/readline/readline-5.2-patches/readline52-013
Patch13: ftp://ftp.gnu.org/gnu/readline/readline-5.2-patches/readline52-014
# fix file permissions, remove RPATH, use CFLAGS
Patch20: readline-5.2-shlib.patch
# fixed in readline-6.0
Patch21: readline-5.2-redisplay-sigint.patch
Patch22: readline-5.2-config.patch
Patch23: compat-readline5-wcwidth.patch
Patch24: compat-readline5-configure-c99.patch
BuildRequires: gcc ncurses-devel
BuildRequires: make

%description
The Readline library provides a set of functions that allow users to
edit command lines. Both Emacs and vi editing modes are available. The
Readline library includes additional functions for maintaining a list
of previously-entered command lines for recalling or editing those
lines, and for performing csh-like history expansion on previous
commands.

%package devel
Summary: Files needed to develop programs which use the readline library
Requires: %{name} = %{version}-%{release}
Requires: ncurses-devel

%description devel
The Readline library provides a set of functions that allow users to
edit typed command lines. If you want to develop programs that will
use the readline library, you need to have the readline-devel package
installed. You also need to have the readline package installed.

%package static
Summary: Static libraries for the readline library
Requires: %{name}-devel = %{version}-%{release}

%description static
The readline-static package contains the static version of the readline
library.

%prep
%setup -q -n readline-%{version}
%patch -P1 -p0 -b .001
%patch -P2 -p0 -b .002
%patch -P3 -p0 -b .003
%patch -P4 -p0 -b .004
%patch -P5 -p0 -b .005
%patch -P6 -p0 -b .006
%patch -P7 -p0 -b .007
%patch -P8 -p0 -b .008
%patch -P9 -p0 -b .009
%patch -P10 -p0 -b .010
%patch -P11 -p0 -b .011
%patch -P12 -p0 -b .013
%patch -P13 -p0 -b .014
%patch -P20 -p1 -b .shlib
%patch -P21 -p1 -b .redisplay-sigint
%patch -P22 -p1
%patch -P23 -p1
%patch -P24 -p1

%build
export CPPFLAGS="-I%{_includedir}/ncurses"
%configure
%make_build

%install
%make_install

mkdir -p $RPM_BUILD_ROOT{/%{_lib},%{_libdir}/readline5}
mv $RPM_BUILD_ROOT%{_libdir}/libreadline.so.* $RPM_BUILD_ROOT/%{_lib}
mv $RPM_BUILD_ROOT%{_libdir}/lib*.a $RPM_BUILD_ROOT%{_libdir}/readline5

rm -f $RPM_BUILD_ROOT%{_libdir}/lib*.so
ln -sf ../../../%{_lib}/libreadline.so.5 $RPM_BUILD_ROOT%{_libdir}/readline5/libreadline.so
ln -sf ../libhistory.so.5 $RPM_BUILD_ROOT%{_libdir}/readline5/libhistory.so

mkdir $RPM_BUILD_ROOT%{_includedir}/readline5
mv $RPM_BUILD_ROOT%{_includedir}/readline{,5}

rm -rf $RPM_BUILD_ROOT%{_infodir}
rm -rf $RPM_BUILD_ROOT%{_mandir}

%ldconfig_scriptlets

%files
%doc CHANGES COPYING NEWS README USAGE
/%{_lib}/libreadline*.so.*
%{_libdir}/libhistory*.so.*

%files devel
%{_includedir}/readline5
%dir %{_libdir}/readline5
%{_libdir}/readline5/lib*.so

%files static
%{_libdir}/readline5/lib*.a

%changelog
* Thu Jan 16 2025 Fedora Release Engineering <releng@fedoraproject.org> - 5.2-50
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Wed Jul 17 2024 Fedora Release Engineering <releng@fedoraproject.org> - 5.2-49
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Wed Jan 24 2024 Fedora Release Engineering <releng@fedoraproject.org> - 5.2-48
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 5.2-47
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 5.2-46
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Mon Mar 13 2023 Tomas Korbar <tkorbar@redhat.com> - 5.2-45
- Change the License tag to the SPDX format

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 5.2-44
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Mon Nov 21 2022 Florian Weimer <fweimer@redhat.com> - 5.2-43
- Avoid C89isms in configure and the source code

* Wed Jul 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 5.2-42
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed Jan 19 2022 Fedora Release Engineering <releng@fedoraproject.org> - 5.2-41
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 5.2-40
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 5.2-39
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Thu Aug 13 2020 Tomas Korbar <tkorbar@redhat.com> - 5.2-38
- Use make macros
- https://fedoraproject.org/wiki/Changes/UseMakeBuildInstallMacro

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 5.2-37
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 5.2-36
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jan 17 2020 Jeff Law <law@redhat.com> - 5.2-35
- Fix configure test for MUST_REINSTALL_SIGLHANDLERS
  compromised by LTO

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 5.2-34
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 5.2-33
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 5.2-32
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue May 22 2018 Miroslav Lichvar <mlichvar@redhat.com> 5.2-31
- Use macro for ldconfig scriptlets
- Add gcc to build requirements
- Remove obsolete macros
- Fix bogus date in changelog

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 5.2-30
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 5.2-29
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 5.2-28
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 5.2-27
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 5.2-26
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 5.2-25
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Aug 16 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 5.2-24
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 5.2-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 5.2-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 5.2-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Wed Jul 18 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 5.2-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Thu Jan 12 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 5.2-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 5.2-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 5.2-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Wed Jul 08 2009 Miroslav Lichvar <mlichvar@redhat.com> 5.2-16
- review fixes (#510022)

* Tue Jul 07 2009 Miroslav Lichvar <mlichvar@redhat.com> 5.2-15
- make compat package
- include upstream patches 013, 014

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 5.2-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Sun Mar 23 2008 Jan Kratochvil <jan.kratochvil@redhat.com> - 5.2-13
- Fix the previous %%changelog entry authorship.

* Sun Mar 23 2008 Jan Kratochvil <jan.kratochvil@redhat.com> - 5.2-12
- Fix excessive prompts on CTRL-C abort while the prompt is being printed.

* Tue Feb 19 2008 Fedora Release Engineering <rel-eng@fedoraproject.org> - 5.2-11
- Autorebuild for GCC 4.3

* Fri Jan 18 2008 Miroslav Lichvar <mlichvar@redhat.com> 5.2-10
- move libreadline to /lib

* Thu Jan 03 2008 Miroslav Lichvar <mlichvar@redhat.com> 5.2-9
- include upstream patches 008-011

* Mon Nov 05 2007 Miroslav Lichvar <mlichvar@redhat.com> 5.2-8
- fix cursor position when prompt has one invisible character (#358231)
- merge review fixes (#226361)
- fix source URL

* Mon Aug 27 2007 Miroslav Lichvar <mlichvar@redhat.com> 5.2-7
- include patches 005, 006, 007

* Wed Aug 22 2007 Miroslav Lichvar <mlichvar@redhat.com> 5.2-6
- update license tag

* Tue May 29 2007 Miroslav Lichvar <mlichvar@redhat.com> 5.2-5
- include patches 5.2-003, 5.2-004

* Thu Mar 22 2007 Miroslav Lichvar <mlichvar@redhat.com> 5.2-4
- apply 5.2-002 patch

* Thu Mar 15 2007 Miroslav Lichvar <mlichvar@redhat.com> 5.2-3
- link libreadline with libtinfo (#232277)
- include upstream 5.2-001 patch
- move static libraries to -static subpackage, spec cleanup

* Thu Nov 30 2006 Miroslav Lichvar <mlichvar@redhat.com> 5.2-2
- require ncurses-devel instead of libtermcap-devel

* Mon Nov 13 2006 Miroslav Lichvar <mlichvar@redhat.com> 5.2-1
- update to 5.2 (#213795)
- use CFLAGS when linking (#199374)
- package docs and examples (#172497)
- spec cleanup

* Wed Jul 12 2006 Jesse Keating <jkeating@redhat.com> - 5.1-1.1
- rebuild

* Mon Jul 10 2006 Jindrich Novy <jnovy@redhat.com> 5.1-1
- update to readline-5.1
- apply new proposed upstream patches for 5.1 (001-004)
- drop "read -e" patch, applied upstream

* Fri Feb 10 2006 Jesse Keating <jkeating@redhat.com> - 5.0-3.2.1
- bump again for double-long bug on ppc(64)

* Tue Feb 07 2006 Jesse Keating <jkeating@redhat.com> - 5.0-3.2
- rebuilt for new gcc4.1 snapshot and glibc changes

* Fri Dec 09 2005 Jesse Keating <jkeating@redhat.com>
- rebuilt

* Wed Mar  2 2005 Tim Waugh <twaugh@redhat.com> 5.0-3
- Rebuild for new GCC.

* Tue Jan 18 2005 Tim Waugh <twaugh@redhat.com> 5.0-2
- Fix line-wrapping (bug #145329).
- Apply "read -e" patch from bash package.

* Wed Jan 12 2005 Tim Waugh <twaugh@redhat.com> 5.0-1
- 5.0 (bug #144835).

* Mon Nov 29 2004 Tim Waugh <twaugh@redhat.com> 4.3-14
- Added URL tag (bug #141106).

* Thu Sep  2 2004 Jeremy Katz <katzj@redhat.com> - 4.3-13
- rebuild so that static linking against readline will work on ppc64 
  without dot symbols

* Mon Jun 28 2004 Tim Waugh <twaugh@redhat.com> 4.3-12
- Build requires libtool (bug #126589).

* Tue Jun 15 2004 Elliot Lee <sopwith@redhat.com>
- rebuilt

* Tue Mar 02 2004 Elliot Lee <sopwith@redhat.com>
- rebuilt

* Fri Feb 13 2004 Elliot Lee <sopwith@redhat.com>
- rebuilt

* Fri Nov 28 2003 Thomas Woerner <twoerner@redhat.com> 4.3-9
- removed rpath

* Thu Nov  6 2003 Tim Waugh <twaugh@redhat.com> 4.3-8
- Apply upstream patches (bug #109240 among others).

* Wed Jun 25 2003 Tim Waugh <twaugh@redhat.com>
- devel package requires libtermcap-devel (bug #98015).

* Wed Jun 25 2003 Tim Waugh <twaugh@redhat.com> 4.3-7
- Fixed recursion loop (bug #92372).

* Wed Jun 04 2003 Elliot Lee <sopwith@redhat.com>
- rebuilt

* Wed Jan 22 2003 Tim Powers <timp@redhat.com>
- rebuilt

* Wed Nov 20 2002 Tim Powers <timp@redhat.com>
- rebuild in current collinst
- BuildRequires autoconf only

* Wed Aug 07 2002 Phil Knirsch <pknirsch@redhat.com> 4.3-3
- Fixed Esc-O-M stack overflow bug.

* Mon Jul 22 2002 Phil Knirsch <pknirsch@redhat.com> 4.3-1
- Updated to latest readline release 4.3

* Thu Jul 11 2002 Phil Knirsch <pknirsch@redhat.com> 4.2a-7
- Fixed problem with alpha build.

* Wed Jul 10 2002 Phil Knirsch <pknirsch@redhat.com>
- Fixed utf8 problem (originally observed in bash).

* Fri Jun 21 2002 Tim Powers <timp@redhat.com> 4.2a-6
- automated rebuild

* Thu May 23 2002 Tim Powers <timp@redhat.com> 4.2a-5
- automated rebuild

* Wed Mar 20 2002 Trond Eivind Glomsrød <teg@redhat.com> 4.2a-4
- Use autoconf 2.53, not 2.52

* Mon Mar  4 2002 Bernhard Rosenkraenzer <bero@redhat.com> 4.2a-3
- Rebuild

* Mon Nov 26 2001 Matt Wilson <msw@redhat.com> 4.2a-2
- removed the manual symlinking of .so, readline handles this by itself
- call only %%makeinstall, not %%makeinstall install install-shared as
  this makes bogus .old files in the buildroot

* Tue Nov 20 2001 Bernhard Rosenkraenzer <bero@redhat.com> 4.2a-1
- 4.2a

* Tue Oct  2 2001 Bernhard Rosenkraenzer <bero@redhat.com> 4.2-4
- Work around autoconf bug

* Mon Oct  1 2001 Bernhard Rosenkraenzer <bero@redhat.com> 4.2-3
- Don't use readline's internal re-implementation of strpbrk on systems
  that have strpbrk - the system implementation is faster and better maintained.

* Tue Aug  7 2001 Bernhard Rosenkraenzer <bero@redhat.com> 4.2-2
- Make sure headers can be included from C++ applications (#51131)
  (Patch based on Debian's with the bugs removed ;) )

* Wed May 09 2001 Florian La Roche <Florian.LaRoche@redhat.de>
- update to 4.2 and adapt patches

* Fri Apr  6 2001 Nalin Dahyabhai <nalin@redhat.com>
- change the paths listed for the header files in the man page to reflect
  the location changes from previous versions (#35073)
- note that "on" is acceptable instead of "On" in the man page (#21327)

* Thu Mar  8 2001 Preston Brown <pbrown@redhat.com>
- fix reading of end key termcap value (@7 is correct, was kH) (#30884)

* Tue Jan 30 2001 Nalin Dahyabhai <nalin@redhat.com>
- mark the man page as currently out-of-date (#25294)

* Thu Sep  7 2000 Jeff Johnson <jbj@redhat.com>
- FHS packaging (64bit systems need to use libdir).

* Thu Aug 17 2000 Jeff Johnson <jbj@redhat.com>
- summaries from specspo.

* Wed Aug  2 2000 Florian La Roche <Florian.LaRoche@redhat.com>
- use "rm -f" in specfile

* Wed Jul 12 2000 Prospector <bugzilla@redhat.com>
- automatic rebuild

* Mon Jun  5 2000 Jeff Johnson <jbj@redhat.com>
- FHS packaging.

* Tue Mar 21 2000 Bernhard Rosenkraenzer <bero@redhat.com>
- 4.1

* Thu Feb 03 2000 Nalin Dahyabhai <nalin@redhat.com>
- update to 4.0

* Fri Apr 09 1999 Michael K. Johnson <johnsonm@redhat.com>
- added guard patch from Taneli Huuskonen <huuskone@cc.helsinki.fi>

* Sun Mar 21 1999 Cristian Gafton <gafton@redhat.com> 
- auto rebuild in the new build environment (release 4)

* Sun Jul 26 1998 Jeff Johnson <jbj@redhat.com>
- updated to 2.2.1

* Wed May 06 1998 Prospector System <bugs@redhat.com>
- translations modified for de, fr, tr

* Wed May 06 1998 Cristian Gafton <gafton@redhat.com>
- don't package /usr/info/dir

* Thu Apr 30 1998 Cristian Gafton <gafton@redhat.com>
- devel package moved to Development/Libraries

* Tue Apr 21 1998 Cristian Gafton <gafton@redhat.com>
- updated to 2.2

* Tue Oct 14 1997 Donnie Barnes <djb@redhat.com>
- spec file cleanups

* Fri Oct 10 1997 Erik Troan <ewt@redhat.com>
- added proper sonames

* Tue Jul 08 1997 Erik Troan <ewt@redhat.com>
- updated to readline 2.1

* Tue Jun 03 1997 Erik Troan <ewt@redhat.com>
- built against glibc
