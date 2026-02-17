Name:           global
Version:        6.6.14
Release:        1%{?dist}
Summary:        Source code tag system
# The entire source code is GPL-3.0-or-later except:
# LGPL-2.0-or-later
#   libglibc/fnmatch.{c,h}
#   libglibc/regex.{c,h}
#   libglibc/snprintf.c
#   libltdl/*.{c,h}
# LGPL-2.1-or-later
#   libglibc/getopt{.c,1.c,.h,_int.h}
#   libglibc/hash-string.{c,h}
#   libglibc/obstack.{c,h}
# BSD-3-Clause
#   gtags-cscope/*.{c,h}
#   libdb/bt_*.c
#   libdb/{db,mpool}.{c,h}
#   libdb/{btree,compat,extern,queue}.h
# MIT
#   htags/jquery
# LicenseRef-Fedora-Public-Domain
#   htags/icons/
#   htags-refkit/htags_path2url.c
#   plugin-factory/uctags-scheme.c
# blessing
#   libdb/sqlite3.{c,h}
# GFDL-1.2-or-later
#   doc/global.{info,texi}
License:        GPL-3.0-or-later and LGPL-2.0-or-later and LGPL-2.1-or-later and BSD-3-Clause and MIT and LicenseRef-Fedora-Public-Domain and blessing and GFDL-1.2-or-later
URL:            https://www.gnu.org/software/global
Source:         https://ftp.gnu.org/pub/gnu/global/global-%{version}.tar.gz
BuildRequires:  gcc
BuildRequires:  ncurses-devel
BuildRequires:  libtool-ltdl-devel
BuildRequires:  python3-devel
BuildRequires:  emacs
%if 0%{?fedora} < 36
BuildRequires:  xemacs
%endif
BuildRequires:  sqlite-devel
BuildRequires:  make
Requires:       emacs-filesystem >= %{_emacs_version}
%if 0%{?fedora} < 36
Requires:       xemacs-filesystem >= %{_xemacs_version}
%endif
Obsoletes:      emacs-global <= 6.5.1-1
Obsoletes:      emacs-global-el <= 6.5.1-1
Provides:       emacs-global = %{version}-%{release}
Provides:       emacs-global-el = %{version}-%{release}

Patch0100:      libdb-dbpanic-function-pointers.patch

%description
GNU GLOBAL is a source code tag system that works the same way across
diverse environments. It supports C, C++, Yacc, Java, PHP and
assembler source code.

%package        ctags
Summary:        Integration of Universal Ctags and Pygments with GLOBAL
License:        GPL-3.0-or-later
Requires:       %{name} = %{version}-%{release}, python3-pygments

%description    ctags
This package contains plug-ins that provides support for more languages
through Pygments and Universal Ctags.

%prep
%autosetup -p1
touch -r configure.ac configure aclocal.m4 Makefile.in

%build
%configure --with-posix-sort=/usr/bin/sort --with-universal-ctags=/usr/bin/ctags \
           --localstatedir=/var/tmp/ --without-included-ltdl --with-sqlite3 \
           --with-python-interpreter=%{python3} --disable-static
%make_build

%install
%make_install

# Remove empty useless directory
rm -f %{buildroot}%{_infodir}/dir

rm -f %{buildroot}%{_libdir}/gtags/*.*a
rm -f %{buildroot}%{_libdir}/gtags/user-custom.*

rm %{buildroot}/%{_datadir}/gtags/{gtags.el,gtags.conf}
rm %{buildroot}/%{_datadir}/gtags/{AUTHORS,COPYING,ChangeLog,DONORS,FAQ,INSTALL,LICENSE,NEWS,README,THANKS}

# fix rpmlint error
chmod +x %{buildroot}/%{_datadir}/gtags/{global,completion}.cgi

mkdir -p %{buildroot}%{_sysconfdir}
install gtags.conf -t %{buildroot}%{_sysconfdir}

mkdir -p %{buildroot}%{_emacs_sitelispdir}
install gtags.el -p -t %{buildroot}%{_emacs_sitelispdir}
%{_emacs_bytecompile} %{buildroot}%{_emacs_sitelispdir}/gtags.el
chmod -x %{buildroot}%{_emacs_sitelispdir}/gtags.el
%if 0%{?fedora} < 36
mkdir -p %{buildroot}%{_xemacs_sitelispdir}
install gtags.el -p -t %{buildroot}%{_xemacs_sitelispdir}
%{_xemacs_bytecompile} %{buildroot}%{_xemacs_sitelispdir}/gtags.el
chmod -x %{buildroot}%{_xemacs_sitelispdir}/gtags.el
%endif

## Remove executable flag
chmod -x %{buildroot}/%{_sysconfdir}/gtags.conf

%files
%doc README THANKS AUTHORS FAQ NEWS
%doc DONORS ChangeLog
%license LICENSE COPYING
%config(noreplace) %{_sysconfdir}/gtags.conf
%{_bindir}/*
%{_infodir}/global.info*
%{_mandir}/man*/*
%{_datadir}/gtags
%{_emacs_sitelispdir}/gtags.el*
%if 0%{?fedora} < 36
%{_xemacs_sitelispdir}/gtags.el*
%endif


%files ctags
%dir %{_libdir}/gtags
%{_libdir}/gtags/*

%changelog
* Sat Feb 14 2026 Matthew Krupcale <mkrupcale@gmail.com> - 6.6.14-1
- Update to v6.6.14

* Fri Jan 16 2026 Fedora Release Engineering <releng@fedoraproject.org> - 6.6.5-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_44_Mass_Rebuild

* Wed Jul 23 2025 Fedora Release Engineering <releng@fedoraproject.org> - 6.6.5-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_43_Mass_Rebuild

* Thu Jan 16 2025 Fedora Release Engineering <releng@fedoraproject.org> - 6.6.5-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Thu Jul 25 2024 Miroslav Suchý <msuchy@redhat.com> - 6.6.5-15
- convert license to SPDX

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 6.6.5-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Wed Jan 24 2024 Fedora Release Engineering <releng@fedoraproject.org> - 6.6.5-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 6.6.5-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 07 2024 Pavel Zhukov <landgraf@fedoraproject.org> - 6.6.5-11
- Fix pathfix usage

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 6.6.5-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Fri Mar  3 2023 DJ Delorie <dj@redhat.com> - 6.6.5-9
- Port configure script to C99

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 6.6.5-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 6.6.5-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 6.6.5-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Tue Nov  9 2021 Jerry James <loganjerry@gmail.com> - 6.6.5-5
- Drop XEmacs support in F36 and later

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 6.6.5-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Mar 23 2021 Pavel Zhukov ov <pzhukov@redhat.com> - 6.6.5-3
- Drop ctags-etags dependency

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 6.6.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Sep 14 2020 Pavel Zhukov <pzhukov@redhat.com> - 6.6.5-1
- New version v6.6.5 (#1875256)

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 6.6.4-3
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 6.6.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Feb 11 2020 Pavel Zhukov <pzhukov@redhat.com> - 6.6.4-1
- New version 6.6.4 (#1786393)

* Tue Feb 11 2020 Pavel Zhukov <pzhukov@redhat.com> - 6.6.3-4
- Fix build with -fno-common

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 6.6.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 6.6.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu May 23 2019 Pavel Zhukov <pzhukov@redhat.com> - 6.6.3-1
- New release v6.6.3

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 6.6.2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Aug 09 2018 Gregory Shimansky <gshimansky@gmail.com> - 6.5.7-6
- Added support for sqlite3

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 6.6.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 6.6.2-3
- Rebuilt for Python 3.7

* Mon Jun 18 2018 Pavel Zhukov <pzhukov@redhat.com> - 6.6.2-2
- Delete install-info according to packaging guidelines

* Mon Feb 12 2018 Pavel Zhukov <pzhukov@redhat.com> - 6.6.2-1
- New version 6.6.2 (#1543839)

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 6.6.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Mon Dec 18 2017 Pavel Zhukov <pzhukov@redhat.com> - 6.6.1-1
- New release 6.6.1 (#1524996)

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 6.5.7-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 6.5.7-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Thu May 25 2017 Pavel Zhukov <pzhukov@redhat.com> - 6.5.7-1
- Update to 6.5.7

* Wed Mar  1 2017 Robin Lee <cheeselee@fedoraproject.org> - 6.5.6-1
- Update to 6.5.6

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 6.5.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Dec 19 2016 Miro Hrončok <mhroncok@redhat.com> - 6.5.2-2
- Rebuild for Python 3.6

* Fri Mar 11 2016 Robin Lee <cheeselee@fedoraproject.org> - 6.5.2-1
- Update to 6.5.2
- Explicitly use Python3
- Use system ltdl

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 6.5.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Nov 12 2015 Robin Lee <cheeselee@fedoraproject.org> - 6.5.1-1
- Update 6.5.1
- Dropped global-6.3.3-format-security.patch
- Fix plug-ins' paths (BZ#1268763)
- Dropped emacs subpackages (BZ#1234559)
- Include elisp addon also for XEmacs
- Fix some rpmlint errors
- Revised summary and description for ctags subpackage
- Revised license tags and use %%license to install LICENSE and COPYING

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 6.3.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Wed Nov 26 2014  Pavel Zhukov <landgraf@fedoraproject.org> - 6.3.3-1
- New version

* Sat Aug 16 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 6.2.12-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Fri Aug 08 2014 Yaakov Selkowitz <yselkowi@redhat.com> - 6.2.12-3
- Fix FTBFS with -Werror=format-security (#1106647)

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 6.2.12-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat May 17 2014 Pavel Zhukov <landgraf@fedoraproject.org> - 6.2.12-1
- New release 

* Wed Oct 30 2013 Sjoerd Mullender <sjoerd@acm.org> - 6.2.9-4
- Install exuberant-ctags.so (#801562).

* Tue Oct 08 2013 Pavel Zhukov <landgraf@fedoraproject.org> - 6.2.9-3
- Remove deprecated defattr
- Cosmetic changes after review

* Mon Oct 07 2013 Pavel Zhukov <landgraf@fedoraproject.org> - 6.2.9-1
- Unorphan package
- New release 6.2.9

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 5.9.3-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 5.9.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 5.9.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Wed Dec  8 2010 Karel Klic <kklic@redhat.com> - 5.9.3-2
- Added --with-posix-sort=/bin/sort to %%configure to speed up
  indexing.

* Wed Dec  8 2010 Karel Klic <kklic@redhat.com> - 5.9.3-1
- Newest upstream release.

* Wed Dec  8 2010 Karel Klic <kklic@redhat.com> - 5.7.5-2
- Build gtags.elc and package it in the new emacs-global package.
- Package gtags.el in the new emacs-global-el package.
- Removed docs from /usr/share/gtags.
- Added more docs to %%doc.
- Install default gtags.conf into /etc.
- Removed deprecated %%clean section.
- Removed unused BuildRoot tag.

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 5.7.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Tue Jun 16 2009 Gerard Milmeister <gemi@bluewin.ch> - 5.7.5-1
- new release 5.7.5

* Fri Nov 21 2008 Gerard Milmeister <gemi@bluewin.ch> - 5.7.3-1
- new release 5.7.3

* Sun Oct 19 2008 Gerard Milmeister <gemi@bluewin.ch> - 5.7.2-1
- new release 5.7.2

* Sat Aug  2 2008 Gerard Milmeister <gemi@bluewin.ch> - 5.7.1-1
- new release 5.7.1

* Mon Jul 21 2008 Tom "spot" Callaway <tcallawa@redhat.com> - 5.4-3
- fix license tag

* Mon Feb 18 2008 Fedora Release Engineering <rel-eng@fedoraproject.org> - 5.4-2
- Autorebuild for GCC 4.3

* Sat Feb 24 2007 Gerard Milmeister <gemi@bluewin.ch> - 5.4-1
- new version 5.4

* Sat Dec  2 2006 Gerard Milmeister <gemi@bluewin.ch> - 5.3-1
- new version 5.3

* Wed Aug 30 2006 Gerard Milmeister <gemi@bluewin.ch> - 5.2-1
- new version 5.2

* Mon Aug 28 2006 Gerard Milmeister <gemi@bluewin.ch> - 5.0-2
- Rebuild for FE6

* Sun Apr 30 2006 Gerard Milmeister <gemi@bluewin.ch> - 5.0-1
- new version 5.0

* Fri Feb 17 2006 Gerard Milmeister <gemi@bluewin.ch> - 4.8.7-3
- Rebuild for Fedora Extras 5

* Wed Oct  5 2005 Gerard Milmeister <gemi@bluewin.ch> - 4.8.7-2
- Remove dir in /usr/share/info

* Sat Oct  1 2005 Gerard Milmeister <gemi@bluewin.ch> - 4.8.7-1
- New Version 4.8.7

* Tue Jul  5 2005 Gerard Milmeister <gemi@bluewin.ch> - 4.8.6-1
- New Version 4.8.6

* Wed May 25 2005 Jeremy Katz <katzj@redhat.com> - 4.8.4-4
- fix build with gcc4 (#156212)

* Sun May 22 2005 Jeremy Katz <katzj@redhat.com> - 4.8.4-3
- rebuild on all arches

* Thu Apr 07 2005 Michael Schwendt <mschwendt[AT]users.sf.net>
- rebuilt

* Mon Mar  7 2005 Gerard Milmeister <gemi@bluewin.ch> - 4.8.4-1
- New Version 4.8.4

* Mon Dec 27 2004 Gerard Milmeister <gemi@bluewin.ch> - 0:4.8.2-0.fdr.1
- New Version 4.8.2

* Sat Oct 23 2004 Gerard Milmeister <gemi@bluewin.ch> - 0:4.8.1-0.fdr.1
- New Version 4.8.1

* Sat Jul 17 2004 Gerard Milmeister <gemi@bluewin.ch> - 0:4.7.2-0.fdr.1
- New Version 4.7.2

* Fri Mar 19 2004 Gerard Milmeister <gemi@bluewin.ch> - 0:4.7-0.fdr.1
- New Version 4.7

* Thu Nov 27 2003 Gerard Milmeister <gemi@bluewin.ch> - 0:4.6.1-0.fdr.1
- First Fedora release

