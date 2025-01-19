%global _hardened_build 1

Summary: Mail delivery agent with filtering abilities
Name: maildrop
Version: 3.1.0
Release: 6%{?dist}
# Exception is explicit permission to link to OpenSSL
License: GPL-3.0-only WITH Classpath-exception-2.0
URL: http://www.courier-mta.org/maildrop/
Source0: https://downloads.sourceforge.net/project/courier/%{name}/%{version}/%{name}-%{version}.tar.bz2
Source1: https://downloads.sourceforge.net/project/courier/%{name}/%{version}/%{name}-%{version}.tar.bz2.sig
Source2: pubkey.maildrop

BuildRequires: automake, libtool, autoconf
BuildRequires: gcc-c++, gdbm-devel, libdb-devel, pcre2-devel
BuildRequires: gawk
BuildRequires: gnupg
BuildRequires: courier-unicode-devel >= 2.1
BuildRequires: libidn2-devel
BuildRequires: make
#Once this is available uncomment and rebuild
#BuildRequires: courier-authlib-devel

%description
maildrop is the mail filter/mail delivery agent that's used by the
Courier Mail Server. This is a standalone build of the maildrop mail
filter that can be used with other mail servers.

maildrop is a replacement for your local mail delivery agent. maildrop
reads a mail message from standard input, then delivers the message to
your mailbox. maildrop knows how to deliver mail to mbox-style
mailboxes, and maildirs.

maildrop optionally reads instructions from a file, which describe how
to filter incoming mail. These instructions can direct maildrop to
deliver the message to an alternate mailbox, or forward it somewhere
else. Unlike procmail, maildrop uses a structured filtering language.

maildrop is written in C++, and is significantly larger than
procmail. However, it uses resources much more efficiently. Unlike
procmail, maildrop will not read a 10 megabyte mail message into
memory. Large messages are saved in a temporary file, and are filtered
from the temporary file. If the standard input to maildrop is a file,
and not a pipe, a temporary file will not be necessary.

maildrop checks the mail delivery instruction syntax from the filter
file, before attempting to deliver a message. Unlike procmail, if the
filter file contains syntax errors, maildrop terminates without
delivering the message. The user can fix the typo without causing any
mail to be lost.

%prep
%{gpgverify} --keyring='%{SOURCE2}' --signature='%{SOURCE1}' --data='%{SOURCE0}'
%autosetup -p1

%build
%configure --disable-shared \
  --enable-use-flock=1 --with-locking-method=fcntl \
  --enable-use-dotlock=1 \
  --enable-syslog=1 \
  --enable-sendmail=%{_sbindir}/sendmail
# prevent 'install: will not overwrite just-created' error
# notification sent to courier-maildrop@lists.sourceforge.net on 2009/09/04
#sed -i 's|DELIVERQUOTAMAN = maildirquota.7 deliverquota.8|DELIVERQUOTAMAN =|' Makefile
%make_build

%install
rm -rf %{buildroot}
%make_install DESTDIR=%{buildroot} htmldir=%{_defaultdocdir}/%{name}
cp -pr COPYING COPYING.GPL AUTHORS %{buildroot}%{_defaultdocdir}/%{name}
cp -pr README README.postfix ChangeLog UPGRADE %{buildroot}%{_defaultdocdir}/%{name}

%files
%doc %{_defaultdocdir}/%{name}
%attr(555,root,mail) %{_bindir}/maildrop
%attr(555,root,mail) %{_bindir}/lockmail
%{_bindir}/deliverquota
%{_bindir}/mailbot
%{_bindir}/maildirmake
%{_bindir}/makemime
%{_bindir}/reformail
%{_bindir}/reformime
%{_bindir}/makedat
%{_bindir}/makedatprog
%{_bindir}/maildirwatch
%{_bindir}/maildirkw
%{_mandir}/man1/*.1*
%{_mandir}/man5/*.5*
%{_mandir}/man7/*.7*
%{_mandir}/man8/*.8*

%changelog
* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Mon Jan 30 2023 Brian C. Lane <bcl@redhat.com> - 3.1.0-1
- New upstream v3.1.0
- drop default suid/sgid bits on maildrop and lockmail
- SPDX migration and license change

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.8-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.8-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Fri Jun 03 2022 Brian C. Lane <bcl@redhat.com> - 3.0.8-1
- New upstream v3.0.8

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Dec 01 2020 Brian C. Lane <bcl@redhat.com> - 3.0.1-2
- Add make to BuildRequires

* Mon Aug 03 2020 Brian C. Lane <bcl@redhat.com> - 3.0.1-1
- New upstreamv3.0.1
- Use %%make_build and %%make_install macros
- Switch Build Requirement from libdb4-devel to libdb-devel

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.0-4
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Nov 22 2019 Brian C. Lane <bcl@redhat.com> - 3.0.0-1
- New upstream v3.0.0 (Georg Sauthoff)
  Drop included patch for SIGSEGV fix

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.9.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.9.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Wed Aug 08 2018 Brian C. Lane <bcl@redhat.com> - 2.9.3-2
- Fix SIGSEGV in reformime (#1613761)

* Tue Jul 24 2018 Brian C. Lane <bcl@redhat.com> - 2.9.3-1
- Upstream 2.9.3

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.9.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.9.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Tue Jan 16 2018 Brian C. Lane <bcl@redhat.com> - 2.9.1-2
- Rebuild for ABI incompatible gdbm 1.14

* Tue Sep 26 2017 Brian C. Lane <bcl@redhat.com> - 2.9.1-1
- Upstream 2.9.1

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.8.3.20151220-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.8.3.20151220-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.8.3.20151220-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Brian C. Lane <bcl@redhat.com> 2.8.3.20151220-1
- Upstream 2.8.3.20151220
  Requires new courier-unicode v1.4 or greater

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 2.8.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.8.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat May 02 2015 Kalev Lember <kalevlember@gmail.com> - 2.8.1-2
- Rebuilt for GCC 5 C++11 ABI change

* Tue Feb 17 2015 Brian C. Lane <bcl@redhat.com> 2.8.1-1
- Update to 2.8.1
- Add courier-unicode requirement

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.7.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.7.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Fri Jan 10 2014 Brian C. Lane <bcl@redhat.com> 2.7.1-1
- Update to 2.7.1

* Thu Sep 26 2013 Brian C. Lane <bcl@redhat.com> 2.6.0-4
- Remove version from the doc directory name (#993910)

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.6.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Sat May 25 2013 Bruno Wolff III <bruno@wolff.to> 2.6.0-2
- Build with global hardening as maildrop has setuid binaries and reads untrusted input

* Sat Mar 16 2013 Brian C. Lane <bcl@redhat.com> 2.6.0-1
- Update to  2.6.0

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.5.0-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.5.0-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Feb 10 2012 Petr Pisar <ppisar@redhat.com> - 2.5.0-16
- Rebuild against PCRE 8.30

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.5.0-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.5.0-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Mon Jul  5 2010 Axel Thimm <Axel.Thimm@ATrpms.net> - 2.5.0-13
- Update to 2.5.0.

* Sun Feb 14 2010 Axel Thimm <Axel.Thimm@ATrpms.net> - 2.4.0-12
- Update to 2.4.0.
- Fixes CVE-2010-0301.

* Fri Sep  4 2009 Milos Jakubicek <xjakub@fi.muni.cz> - 2.0.4-11
- Fix FTBFS: prevent 'install: will not overwrite just-created' error

* Wed May 21 2008 Tom "spot" Callaway <tcallawa@redhat.com> - 2.0.4-7
- fix license tag

* Sat Mar  8 2008 Axel Thimm <Axel.Thimm@ATrpms.net> - 2.0.4-6
- Try a better license tag.
- Remove all devel parts - this is not upstream-ready yet.
- Make the build verbose.

* Sun Jan 13 2008 Axel Thimm <Axel.Thimm@ATrpms.net> - 2.0.4-5
- Go static.

* Wed Oct 24 2007 Axel Thimm <Axel.Thimm@ATrpms.net> - 2.0.4-4
- Add gawk to build dependencies.

* Sat Aug  4 2007 Axel Thimm <Axel.Thimm@ATrpms.net> - 2.0.4-3
- Update to 2.0.4.

* Sun Mar 25 2007 Axel Thimm <Axel.Thimm@ATrpms.net> - 2.0.3-2
- Initial build.

