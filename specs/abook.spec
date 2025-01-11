Name: abook
Version: 0.6.1
Release: 28%{?dist}
# GPL-2.0-or-later, except:
# getopt.[ch]: LGPL-2.0-or-later
# getopt1.c: LGPL-2.0-or-later
License: GPL-2.0-or-later AND LGPL-2.0-or-later
URL: http://abook.sourceforge.net/
Summary: Text-based addressbook program for mutt
Source0: http://abook.sourceforge.net/devel/abook-%{version}.tar.gz
# preserve all fields by default
Patch0: %{name}-preserve.patch
# 0618ad6 fixed bug #6 (https://sourceforge.net/p/abook/bugs/6/)
Patch1: 0001-fixed-bug-6.patch
# 02ac0ce doc: manpage mention of the -f option + fix for bug #8 (https://sourceforge.net/p/abook/bugs/8/)
Patch2: 0002-doc-manpage-mention-of-the-f-option-fix-for-bug-8.patch
# fix compilation when used with GCC -std=gnu99 or -std=gnu11
Patch3: abook-extern-inline.patch
# Fix detection of wcwidth()
Patch4: abook-wcwidth.patch
BuildRequires: autoconf
BuildRequires: automake
BuildRequires: gettext-devel
BuildRequires: make
BuildRequires: ncurses-devel
BuildRequires: readline-devel
BuildRequires: gcc
Requires: webclient

%description
Abook is a small and powerful text-based addressbook program
designed for use with the mutt mail client.

%prep
%autosetup -p1
autoreconf -vif

%build
%configure
%make_build

%install
%make_install
# generate localized files list
%find_lang %{name}

%files -f %{name}.lang
%license COPYING
%doc AUTHORS BUGS ChangeLog FAQ README RELEASE_NOTES THANKS TODO sample.abookrc
%{_bindir}/abook
%{_mandir}/man1/abook.*
%{_mandir}/man5/abookrc.*

%changelog
* Thu Jan 09 2025 Dominik Mierzejewski <dominik@greysector.net> - 0.6.1-28
- fix FTBFS with GCC15 (resolves: rhbz#2336029)
- switch to autosetup macro
- correct license tag

* Thu Jul 25 2024 Miroslav Suchý <msuchy@redhat.com> - 0.6.1-27
- convert license to SPDX

* Wed Jul 17 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.1-26
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.1-25
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.1-24
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.1-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Wed Jan 18 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.1-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Wed Jul 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.1-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed Jan 19 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.1-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.1-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Mon Jan 25 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.1-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Dec 14 2020 Dominik Mierzejewski <rpm@greysector.net> 0.6.1-17
- add explicit BR on make
- use modern macros
- mark license text accordingly

* Fri Jul 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.1-16
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.1-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.1-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.1-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Feb 17 2019 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.6.1-12
- Rebuild for readline 8.0

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.1-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.1-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Mon Feb 19 2018 Itamar Reis Peixoto <itamar@ispbrasil.com.br> - 0.6.1-9
- add gcc into buildrequires

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.1-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Tue Sep 19 2017 Dominik Mierzejewski <rpm@greysector.net> 0.6.1-7
- backport fixes from upstream git repo

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Jan 12 2017 Igor Gnatenko <ignatenko@redhat.com> - 0.6.1-3
- Rebuild for readline 7.x

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Sat Nov 07 2015 Dominik Mierzejewski <rpm@greysector.net> 0.6.1-1
- update to 0.6.1
- fix build with automake <> 1.14 by running autoreconf

* Tue Jun 16 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6.0-0.17.20141128git6e550af
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Wed Feb 11 2015 Dominik Mierzejewski <rpm@greysector.net> 0.6.0-0.16.20141128git6e550af
- update to the latest git snapshot
- fix build with gcc-5.0

* Fri Aug 15 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6.0-0.15.20140116git5840fce
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Fri Jun 06 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6.0-0.14.20140116git5840fce
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Thu Feb 27 2014 Dominik Mierzejewski <rpm@greysector.net> 0.6.0-0.13.20140116git5840fceb
- update to the latest git snapshot
- drop obsolete patch
- add comment explaining the preserve patch
- drop some more obsolete specfile parts

* Thu Feb 27 2014 Dominik Mierzejewski <rpm@greysector.net> 0.6.0-0.12.pre2
- fix build on aarch64
- drop obsolete specfile parts
- fix bad date in changelog

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6.0-0.11.pre2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6.0-0.10.pre2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Wed Jul 18 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6.0-0.9.pre2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Thu Jan 12 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6.0-0.8.pre2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Mon Feb 07 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6.0-0.7.pre2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Sat Dec 04 2010 Dominik Mierzejewski <rpm@greysector.net> 0.6.0-0.6.pre2
- preserve all fields by default (bug #365701), fix based on patch by Stephen Beahm

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6.0-0.5.pre2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Mon Feb 23 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6.0-0.4.pre2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Tue Feb 19 2008 Fedora Release Engineering <rel-eng@fedoraproject.org> - 0.6.0-0.3.pre2
- Autorebuild for GCC 4.3

* Sat Aug 25 2007 Dominik Mierzejewski <rpm@greysector.net> 0.6.0-0.2.pre2
- rebuild for BuildID
- update license tag

* Sun Apr 29 2007 Dominik Mierzejewski <rpm@greysector.net> 0.6.0-0.1.pre2
- latest devel version
- specfile cleanups

* Mon Aug 28 2006 Dominik Mierzejewski <rpm@greysector.net> 0.5.6-3
- mass rebuild

* Tue Aug 15 2006 Dominik Mierzejewski <rpm@greysector.net> 0.5.6-2
- fix macro usage in changelog
- clean buildroot before install

* Mon Jul 31 2006 Dominik Mierzejewski <rpm@greysector.net> 0.5.6-1
- updated to 0.5.6
- fix 64bit build

* Sun Apr 02 2006 Dominik Mierzejewski <rpm@greysector.net> 0.5.5-2
- more FE compliance fixes

* Fri Jan 06 2006 Dominik Mierzejewski <rpm@greysector.net> 0.5.5-1
- updated to 0.5.5
- applied upstream post-0.5.5 patches
- added locales

* Sun Oct 02 2005 Dominik Mierzejewski <rpm@greysector.net> 0.5.4-1
- updated to 0.5.4
- spec cleanups

* Sun Apr 10 2005 Dominik Mierzejewski <rpm@greysector.net> 0.5.3-2
- add missing readline-devel BR

* Sun Oct 10 2004 Dominik Mierzejewski <rpm@greysector.net> 0.5.3-1
- updated to 0.5.3

* Tue May 13 2003 Dominik Mierzejewski <rpm@greysector.net> 0.4.18-2
- rebuilt for RH7.3

* Tue Nov 05 2002 Aleksandr Blokhin 'Sass' <sass@altlinux.ru> 0.4.18-alt0.1.cvs20021008
- daily cvs snapshot
- %%rlz1 logic is going back ;)

* Wed Oct 16 2002 Stanislav Ievlev <inger@altlinux.ru> 0.4.17-alt2
- rebuild with gcc3
- I had to remove %%rlz1 logic. See changelogs below ;)))
- removed extra translations

* Sun Apr 07 2002 Aleksandr Blohin <sass@altlinux.ru> 0.4.17-%%rlz1
- 0.4.17

* Fri Mar 15 2002 Aleksandr Blohin <sass@altlinux.ru> 0.4.16-%%rlz1
- 0.4.16

* Fri Mar 01 2002 Aleksandr Blohin <sass@altlinux.ru> 0.4.15-%%rlz1
- updates in spec

* Tue Jan 08 2002 Aleksandr Blohin <sass@altlinux.ru> 0.4.15-alt3
- added Summary & description in CP1251 encoding

* Mon Dec 24 2001 Aleksandr Blohin <sass@altlinux.ru> 0.4.15-alt2
- updated spec
- updated to rpm-4.0.3

* Wed Nov 7 2001 Aleksandr Blohin <sass@altlinux.ru> 0.4.15-alt1
- 0.4.15 final
- spec cleanup

* Sat Oct 27 2001 Aleksandr Blohin <sass@altlinux.ru> 0.4.15-alt0.pre2
- 0.4.15pre2
- spec cleanup

* Fri Oct 5 2001 Aleksandr Blohin <sass@altlinux.ru> 0.4.14-alt1
- 0.4.14

* Thu Jun 28 2001 Stanislav Ievlev <inger@altlinux.ru> 0.4.13-alt1
- 0.4.13

* Thu Apr 26 2001 Stanislav Ievlev <inger@altlinux.ru> 0.4.12-alt1
- 0.4.12

* Tue Jan 09 2001 Dmitry V. Levin <ldv@fandra.org> 0.4.11-ipl1mdk
- 0.4.11

* Sun Dec 17 2000 Dmitry V. Levin <ldv@fandra.org> 0.4.10-ipl1mdk
- RE adaptions.

* Sat Dec 16 2000 Vincent Danen <vdanen@mandrakesoft.com> 0.4.10-1mdk
- first mandrake version

* Wed Sep 20 2000 Gustavo Niemeyer <niemeyer@conectiva.com>
- First package.
