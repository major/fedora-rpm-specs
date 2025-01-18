Name: cadaver
Version: 0.26
Release: 2%{?dist}
Summary: Command-line WebDAV client
# Automatically converted from old format: GPLv2+ - review is highly recommended.
License: GPL-2.0-or-later
Source: https://notroj.github.io/cadaver/%{name}-%{version}.tar.gz
URL: http://www.webdav.org/cadaver/
BuildRequires: gcc, make
BuildRequires: neon-devel >= 0.27.0, readline-devel, ncurses-devel, gettext

%description
cadaver is a command-line WebDAV client, with support for file upload, 
download, on-screen display, in-place editing, namespace operations
(move/copy), collection creation and deletion, property manipulation, 
and resource locking.

%prep
%setup -q

%build
%configure --with-neon=%{_prefix}
make %{?_smp_mflags}

%install
make install DESTDIR=$RPM_BUILD_ROOT

# broken in 0.24
%find_lang %{name}

%files -f %{name}.lang
%doc NEWS FAQ THANKS TODO COPYING README.md
%{_bindir}/*
%{_mandir}/*/*

%changelog
* Thu Jan 16 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.26-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Wed Nov 27 2024 Joe Orton <jorton@redhat.com> - 0.26-1
- update to 0.26 (#2300583)
- enable NLS again

* Thu Jul  25 2024 Miroslav Suchý <msuchy@redhat.com> - 0.24-7
- convert license to SPDX

* Wed Jul 17 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.24-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Tue Jan 23 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.24-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.24-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.24-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Wed Jan 18 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.24-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Mon Oct 31 2022 Joe Orton <jorton@redhat.com> - 0.24-1
- update to 0.24

* Wed Jul 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.23.3-28
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed Jan 26 2022 Joe Orton <jorton@redhat.com> - 0.23.3-27
- update for neon 0.32.x (#2045239)

* Wed Jan 19 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.23.3-26
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.23.3-25
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.23.3-24
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.23.3-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jun  3 2020 Joe Orton <jorton@redhat.com> - 0.23.3-22
- rebuild to support neon 0.31

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.23.3-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.23.3-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Feb 17 2019 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.23.3-19
- Rebuild for readline 8.0

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.23.3-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.23.3-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.23.3-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.23.3-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.23.3-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.23.3-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Jan 12 2017 Igor Gnatenko <ignatenko@redhat.com> - 0.23.3-12
- Rebuild for readline 7.x

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.23.3-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.23.3-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Fri Aug 15 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.23.3-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Thu Jun 19 2014 Yaakov Selkowitz <yselkowi@redhat.com> - 0.23.3-8
- Fix FTBFS with neon-0.30 (#992037, #1106029)

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.23.3-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.23.3-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.23.3-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Wed Jul 18 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.23.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Thu Jan 12 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.23.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.23.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Tue Dec 15 2009 Joe Orton <jorton@redhat.com> - 0.23.3-1
- update to 0.23.3

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.23.2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Mon Feb 23 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.23.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Sat Mar 29 2008 Joe Orton <jorton@redhat.com> 0.23.2-4
- build with -fPIE not -fpie, might fix the SPARC build

* Mon Feb 11 2008 Joe Orton <jorton@redhat.com> 0.23.2-3
- BuildRequire gettext

* Mon Feb 11 2008 Joe Orton <jorton@redhat.com> 0.23.2-2
- update to 0.23.2

* Mon Feb 11 2008 Joe Orton <jorton@redhat.com> 0.23.1-2
- update to 0.23.1

* Fri Sep  7 2007 Joe Orton <jorton@redhat.com> 0.23.0-2
- spec file cleanup (#225634)

* Wed Aug 22 2007 Joe Orton <jorton@redhat.com> 0.23.0-1
- update to 0.23.0

* Mon Aug 20 2007 Joe Orton <jorton@redhat.com> 0.22.5-3
- fix License

* Fri Mar 23 2007 Joe Orton <jorton@redhat.com> 0.22.5-2
- update to 0.22.5
- use approved BuildRoot

* Fri Dec  1 2006 Joe Orton <jorton@redhat.com> 0.22.3-6
- BR ncurses-devel, fix readline support

* Wed Nov 22 2006 Joe Orton <jorton@redhat.com> 0.22.3-5
- rebuild

* Mon Jul 17 2006 Joe Orton <jorton@redhat.com> 0.22.3-4
- rebuild

* Tue May 16 2006 Karsten Hopp <karsten@redhat.de> 0.22.3-3
- buildrequires readline-devel

* Fri Feb 10 2006 Jesse Keating <jkeating@redhat.com> - 0.22.3-2.2
- bump again for double-long bug on ppc(64)

* Tue Feb 07 2006 Jesse Keating <jkeating@redhat.com> - 0.22.3-2.1
- rebuilt for new gcc4.1 snapshot and glibc changes

* Tue Jan 31 2006 Joe Orton <jorton@redhat.com> 0.22.3-2
- rebuild for neon 0.25.x

* Fri Jan  6 2006 Joe Orton <jorton@redhat.com> 0.22.3-1
- update to 0.22.3

* Fri Dec 09 2005 Jesse Keating <jkeating@redhat.com>
- rebuilt

* Tue Nov  8 2005 Tomas Mraz <tmraz@redhat.com> 0.22.2-3
- rebuilt with new openssl

* Wed Mar  2 2005 Joe Orton <jorton@redhat.com> 0.22.2-2
- rebuild

* Wed Jan 12 2005 Joe Orton <jorton@redhat.com> 0.22.2-1
- update to 0.22.2

* Wed Jan 12 2005 Tim Waugh <twaugh@redhat.com> 0.22.1-4
- Rebuild for new readline.

* Tue Jun 15 2004 Elliot Lee <sopwith@redhat.com>
- rebuilt

* Wed May 12 2004 Joe Orton <jorton@redhat.com> 0.22.1-2
- build as PIE

* Tue Apr 20 2004 Joe Orton <jorton@redhat.com> 0.22.1-1
- update to 0.22.1

* Fri Feb 13 2004 Elliot Lee <sopwith@redhat.com>
- rebuilt

* Fri Oct  3 2003 Joe Orton <jorton@redhat.com> 0.22.0-1
- update to 0.22.0; use system neon

* Tue Jul 22 2003 Nalin Dahyabhai <nalin@redhat.com> 0.21.0-2
- rebuild

* Mon Jul 21 2003 Joe Orton <jorton@redhat.com> 0.21.0-1
- update to 0.21.0

* Wed Jun 04 2003 Elliot Lee <sopwith@redhat.com>
- rebuilt

* Wed Jan 22 2003 Tim Powers <timp@redhat.com>
- rebuilt

* Tue Jan  7 2003 Nalin Dahyabhai <nalin@redhat.com> 0.20.5-5
- rebuild

* Fri Nov 22 2002 Joe Orton <jorton@redhat.com> 0.20.5-4
- force use of bundled neon (#78260)

* Mon Nov  4 2002 Joe Orton <jorton@redhat.com> 0.20.5-3
- rebuild in new environment

* Fri Aug 30 2002 Joe Orton <jorton@redhat.com> 0.20.5-2
- update to 0.20.5; many bug fixes, minor security-related
 fixes, much improved SSL support, a few new features.

* Thu Aug 22 2002 Joe Orton <jorton@redhat.com> 0.20.4-1
- add --with-force-ssl

* Wed May  1 2002 Joe Orton <joe@manyfish.co.uk>
- add man page

* Sat Jan 19 2002 Joe Orton <joe@manyfish.co.uk>
- updated description

* Mon Nov 19 2001 Joe Orton <joe@manyfish.co.uk>
- Merge changes from Nalin Dahyabhai <nalin@redhat.com>.

* Fri Feb 11 2000 Joe Orton <joe@orton.demon.co.uk>
- Text descriptions modified

* Thu Feb 10 2000 Lee Mallabone <lee0@callnetuk.com>
- Initial creation.
