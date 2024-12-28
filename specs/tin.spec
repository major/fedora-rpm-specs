Name: tin
Version: 2.6.4
Release: 1%{?dist}
Summary: Basic Internet news reader
# all sources built into binaries are BSD-3-Clause except
# src/parsdate.{c,y} which are Public Domain
License: BSD-3-Clause AND LicenseRef-Fedora-Public-Domain
URL: http://www.tin.org/
Source0: ftp://ftp.tin.org/pub/news/clients/tin/stable/tin-%{version}.tar.xz
Source1: ftp://ftp.tin.org/pub/news/clients/tin/stable/tin-%{version}.tar.xz.sign
Source2: tin-pgp-key-0x5A49550EB490B4D1.txt
BuildRequires: aspell
BuildRequires: byacc
BuildRequires: gcc-c++
BuildRequires: gettext
BuildRequires: gnupg1
BuildRequires: gnupg2
BuildRequires: libcanlock-devel
BuildRequires: make
BuildRequires: ncurses-devel
BuildRequires: openssl-devel
BuildRequires: pcre2-devel
BuildRequires: perl-generators
BuildRequires: libgsasl-devel
BuildRequires: libicu-devel
BuildRequires: libidn-devel
BuildRequires: zlib-devel

%description
Tin is a basic, easy to use Internet news reader.  Tin can read news
locally or remotely via an NNTP (Network News Transport Protocol)
server.

Install tin if you need a basic news reader.

%prep
workdir=$(mktemp --directory)
workring=${workdir}/keyring.gpg
gpg1 --homedir=${workdir} --pgp2 --yes --output="${workring}" --dearmor %{S:2}
gpg1 --homedir=${workdir} --pgp2 --verify --keyring="${workring}" %{S:1} %{S:0}
rm -r ${workdir}
%autosetup -p1
rm -rv libcanlock pcre

%build
%configure \
	--with-libdir=/var/lib/news \
	--with-spooldir=/var/spool/news/articles \
	--enable-cancel-locks \
	--enable-long-article-numbers \
	--enable-nntp \
	--enable-prototypes \
	--disable-echo \
	--disable-mime-strict-charset \
	--with-screen=ncursesw \
	--with-gpg=%{_bindir}/gpg2 \
	--with-mime-default-charset=UTF-8 \
	--with-nntps=openssl \
	--with-pcre2-config=/usr/bin/pcre2-config \
	--with-zlib \

sed -i -e 's/@\$(INSTALL) -s/@\$(INSTALL)/g' -e 's/@\$(CC)/\$(CC)/g' -e  's/@\$(CPP)/\$(CPP)/g' src/Makefile

%make_build

%install
%make_install

install -Dpm644 -t %{buildroot}%{_mandir}/man3 doc/wildmat.3

%find_lang %{name}

%files -f %name.lang
%doc README
%doc doc/{CHANGES{,.old},CREDITS,TODO,WHATSNEW}
%doc doc/{config-anomalies,filtering,good-netkeeping-seal}
%doc doc/*.{sample,txt}
%doc doc/tin.defaults
%{_bindir}/tin
%{_bindir}/rtin
%{_bindir}/metamutt
%{_bindir}/opt-case.pl
%{_bindir}/w2r.pl
%{_bindir}/url_handler.pl
%{_bindir}/tinews.pl
%{_mandir}/man1/opt-case.pl.1*
%{_mandir}/man1/rtin.1*
%{_mandir}/man1/tin.1*
%{_mandir}/man1/tinews.pl.1*
%{_mandir}/man1/url_handler.pl.1*
%{_mandir}/man1/w2r.pl.1.gz
%{_mandir}/man3/wildmat.3*
%{_mandir}/man5/mbox.5*
%{_mandir}/man5/mmdf.5*
%{_mandir}/man5/rtin.5*
%{_mandir}/man5/tin.5*

%changelog
* Thu Dec 26 2024 Dominik Mierzejewski <dominik@greysector.net> 2.6.4-1
- update to 2.6.4 (rhbz#2333917)

* Sun Dec 08 2024 Dominik Mierzejewski <dominik@greysector.net> 2.6.3-6
- enable Cancel-Locks support
- enable zlib compression support

* Sat Jul 20 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.6.3-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Tue Mar 05 2024 Dominik Mierzejewski <dominik@greysector.net> 2.6.3-4
- enable long article number support
- drop obsolete/redundant configure options
- switch to package names in BuildRequires and sort alphabetically
- use modern macros and drop __foo macro usage
- more explicit file list to avoid duplicates
- add missing files

* Wed Jan 31 2024 Pete Walter <pwalter@fedoraproject.org> - 2.6.3-3
- Rebuild for ICU 74

* Sat Jan 27 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.6.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Dec 27 2023 Dominik Mierzejewski <dominik@greysector.net> 2.6.3-1
- update to 2.6.3 (#2255732)
- drop obsolete patch
- use SPDX identifiers in License field

* Fri Dec 15 2023 Florian Weimer <fweimer@redhat.com> - 2.6.2-6
- Further C compatibility fixes for the configure script

* Sat Jul 22 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.6.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Tue Jul 11 2023 František Zatloukal <fzatlouk@redhat.com> - 2.6.2-4
- Rebuilt for ICU 73.2

* Sat Jan 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.6.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Sat Dec 31 2022 Pete Walter <pwalter@fedoraproject.org> - 2.6.2-2
- Rebuild for ICU 72

* Wed Dec 28 2022 Dominik Mierzejewski <dominik@greysector.net> 2.6.2-1
- update to 2.6.2 (#2156181)
- enable NNTPS support using OpenSSL
- use pcre2 instead of the deprecated pcre (#2128388)

* Sat Jan 22 2022 Fedora Release Engineering <releng@fedoraproject.org> 2.6.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jan 13 2022 Dominik Mierzejewski <dominik@greysector.net> 2.6.1-1
- update to 2.6.1 (#2035661)

* Fri Nov 05 2021 Dominik 'Rathann' Mierzejewski <dominik@greysector.net> 2.6.0-4
- work around libusb missing dependency on libusb1

* Fri Nov 05 2021 Dominik 'Rathann' Mierzejewski <dominik@greysector.net> 2.6.0-3
- Revert "Remove gunpg 1 based verification as it does not work anymore"

* Tue Oct 05 2021 Adrian Reber <adrian@lisas.de> 2.6.0-2
- Remove gunpg 1 based verification as it does not work anymore

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.5-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Thu May 20 2021 Pete Walter <pwalter@fedoraproject.org> - 2.4.5-5
- Rebuild for ICU 69

* Wed May 19 2021 Pete Walter <pwalter@fedoraproject.org> - 2.4.5-4
- Rebuild for ICU 69

* Mon Feb 01 2021 Dominik Mierzejewski <rpm@greysector.net> - 2.4.5-3
- fix segfault when clicking past the end of topic list in xterm (#1921096)

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Jan 04 2021 Adrian Reber <adrian@lisas.de> - 2.4.5-1
- updated to 2.4.5 (#1910747)

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.4-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri May 15 2020 Pete Walter <pwalter@fedoraproject.org> - 2.4.4-3
- Rebuild for ICU 67

* Fri Jan 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Tue Dec 24 2019 Dominik Mierzejewski <rpm@greysector.net> - 2.4.4-1
- updated to 2.4.4
- enable SASL authentication support
- drop pcre CFLAGS workaround
- specify path to gpg2 to enable GPG support
- set UTF-8 as the default charset
- make build more verbose
- enable spell-checking support
- verify source tarball PGP-2 signature
- add missing build dependencies

* Sat Jul 27 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Sat Dec 30 2017 Adrian Reber <adrian@lisas.de> - 2.4.2-1
- updated to 2.4.2

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Sat Jan 07 2017 Adrian Reber <adrian@lisas.de> - 2.4.1-1
- updated to 2.4.1

* Tue Aug 30 2016 Adrian Reber <adrian@lisas.de> - 2.4.0-1
- updated to 2.4.0

* Fri Feb 05 2016 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Jun 19 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.2.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Mon Aug 18 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.2.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.2.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Thu May 08 2014 Adrian Reber <adrian@lisas.de> - 2.2.1-1
- updated to 2.2.1

* Fri Dec 27 2013 Adrian Reber <adrian@lisas.de> - 2.2.0-1
- updated to 2.2.0
- spec cleanup

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Jul 17 2013 Petr Pisar <ppisar@redhat.com> - 2.0.1-5
- Perl 5.18 rebuild

* Fri Feb 15 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Thu Jan 10 2013 Adrian Reber <adrian@lisas.de> - 2.0.1-3
- Add configure option '--with-screen=ncursesw' (fixes #890764)

* Fri Jul 27 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Mon Mar 19 2012 Adrian Reber <adrian@lisas.de> - 2.0.1-1
- updated to 2.0.1

* Fri Feb 10 2012 Petr Pisar <ppisar@redhat.com> - 2.0.0-4
- Rebuild against PCRE 8.30

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Wed Oct 26 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0.0-2
- Rebuilt for glibc bug#747377

* Wed Sep 14 2011 Adrian Reber <adrian@lisas.de> - 2.0.0-1
- updated to 2.0.0

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.8.3-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Tue Apr 13 2010 Adrian Reber <adrian@lisas.de> - 1.8.3-7
- added BR on gnupg2 (bz #574976)
- use the %%find_lang macro
- remove binary stripping from Makefile with sed instead of perl

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.8.3-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.8.3-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Mon Feb 18 2008 Fedora Release Engineering <rel-eng@fedoraproject.org> - 1.8.3-4
- Autorebuild for GCC 4.3

* Fri Aug 24 2007 Adrian Reber <adrian@lisas.de> - 1.8.3-3
- license updated

* Fri Aug 24 2007 Adrian Reber <adrian@lisas.de> - 1.8.3-2
- rebuilt

* Wed Jun 20 2007 Adrian Reber <adrian@lisas.de> - 1.8.3-1
- updated to 1.8.3
- removed desktop file (bz #241463)

* Fri Sep 15 2006 Adrian Reber <adrian@lisas.de> - 1.8.2-1
- updated to 1.8.2

* Mon Mar 13 2006 Adrian Reber <adrian@lisas.de> - 1.8.1-1
- updated to 1.8.1

* Sun May 22 2005 Jeremy Katz <katzj@redhat.com> - 1.6.2-4
- rebuild on all arches

* Thu Apr  7 2005 Michael Schwendt <mschwendt[AT]users.sf.net>
- rebuilt

* Thu Jun 24 2004 Adrian Reber <adrian@lisas.de> - 0:1.6.2-0.fdr.2
- changed BuildRequires from bison to byacc
- added pcre-devel as BuildRequires
- replaced all commands with rpmmacros
- made make use RPM_OPT_FLAGS

* Sun Nov 23 2003 Adrian Reber <adrian@lisas.de> - 0:1.6.2-0.fdr.1
- updated to 1.6.2

* Fri Jun 06 2003 Adrian Reber <adrian@lisas.de> - 0:1.4.7-0.fdr.2
- remove stripping from Makefile; let rpm strip the binaries
- moved the documentation from docdir/doc to docdir

* Sat May 31 2003 Adrian Reber <adrian@lisas.de> - 0:1.4.7-0.fdr.1
- updated to 1.4.7
- Source now macroless
- BuildRoot changed to the format from the fedora spec template
- added smp_mflags to the makes
- more fedorafication

* Thu May 01 2003 Adrian Reber <adrian@lisas.de> - 0:1.4.6-0.fdr.3
- Added BuildRequires: bison, desktop-files-utils
- removed --verbose and --mandir from configure
- s/X-Red-Hat-Extra/X-Fedora/ in desktop-file-install
- added release macro to BuildRoot

* Tue Feb 25 2003 Adrian Reber <adrian@lisas.de> - 1.4.6-1.fedora.1
- applied fedora naming conventions

* Tue Aug 22 2000 Than Ngo <than@redhat.com>
- add applink file (Bug #16568)

* Mon Aug 07 2000 Preston Brown <pbrown@redhat.com>
- 1.4.4 fixes buffer overflow, memory leaks.

* Wed Jul 12 2000 Prospector <bugzilla@redhat.com>
- automatic rebuild

* Fri Jun 02 2000 Preston Brown <pbrown@redhat.com>
- fix spooldir to be /var/spool/news/articles not /var/spool/news

* Fri Mar 24 2000 Bernhard Rosenkraenzer <bero@redhat.com>
- rebuild with current ncurses

* Thu Feb 17 2000 Preston Brown <pbrown@redhat.com>
- rebuild with new vi in the buildroots so it finds the right default editor

* Thu Feb 10 2000 Preston Brown <pbrown@redhat.com>
- bump epoch

* Mon Feb 07 2000 Preston Brown <pbrown@redhat.com>
- upgrade to 1.4.2 (stable)

* Mon May 31 1999 Jeff Johnson <jbj@redhat.com>
- update to tinpre-1.4-19990517.
- fix libdir=/var/lib/news (#7).
- fix spooldir=/var/spool/news.

* Sun Mar 21 1999 Cristian Gafton <gafton@redhat.com>
- auto rebuild in the new build environment (release 3)

* Tue Mar 09 1999 Preston Brown <pbrown@redhat.com>
- upgraded to latest dev version snapshot.

* Wed Feb 24 1999 Preston Brown <pbrown@redhat.com>
- Injected new description and group.

* Tue Dec 22 1998 Preston Brown <pbrown@redhat.com>
- upgraded again to latest snapshot.

* Fri Nov 06 1998 Preston Brown <pbrown@redhat.com>
- Alan is right; 1.22 is full of bugs and ANCIENT. Moved to latest tin.

* Tue Aug  4 1998 Jeff Johnson <jbj@redhat.com>
- build root

* Wed Jun 24 1998 Alan Cox <alan@redhat.com>
- turned on DONT_LOG_USER - get rid of the silly file in /tmp. We probably
  ought to move to a newer tin soon.

* Fri Apr 24 1998 Prospector System <bugs@redhat.com>
- translations modified for de, fr, tr

* Wed Apr 15 1998 Erik Troan <ewt@redhat.com>
- built against new ncurses

* Mon Nov 3 1997 Erik Troan <ewt@redhat.com>
- hacked to use just termios, not a motley mix of termios and termio

* Fri Jul 18 1997 Erik Troan <ewt@redhat.com>
- built against glibc
