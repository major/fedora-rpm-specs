Name:           isync
Version:        1.5.0
Release:        3%{?dist}
Summary:        Tool to synchronize IMAP4 and Maildir mailboxes

# Automatically converted from old format: GPLv2+ - review is highly recommended.
License:        GPL-2.0-or-later
URL:            http://isync.sourceforge.net/
Source0:        https://downloads.sourceforge.net/%{name}/%{name}-%{version}.tar.gz
Source1:        https://downloads.sourceforge.net/%{name}/%{name}-%{version}.tar.gz.asc
# needs manual removal of leftover html elements
Source2:        https://keyserver.ubuntu.com/pks/lookup?op=get&search=0x63bfd037cad71e8dff3aea3ac17714f08d1bdbba#./%{name}.keyring
# https://sourceforge.net/p/isync/patches/19/
Patch0:         v2-0001-fix-compile-with-fno-lto.patch
Patch1:         0001-fix-initial-build-from-git.patch
Patch2:         0002-fix-IMAP-INBOX-case-normalization.patch
Patch3:         0003-add-missing-trailing-newlines-in-error-calls.patch
Patch4:         0004-fix-typos.patch
Patch5:         0005-improve-reporting-of-failure-to-open-previously-pres.patch
Patch6:         0006-fix-implicit-listing-of-Maildir-INBOX-under-Path.patch

BuildRequires:  perl
BuildRequires:  libdb-devel
BuildRequires:  openssl-devel
BuildRequires:  cyrus-sasl-devel
BuildRequires:  automake
BuildRequires:  gnupg2

Requires:       cyrus-sasl

%description
mbsync is a command line application which synchronizes mailboxes. Currently
Maildir and IMAP4 mailboxes are supported. New messages, message deletions
and flag changes can be propagated both ways. mbsync is suitable for use in
IMAP-disconnected mode.

%prep
%{gpgverify} --keyring='%{SOURCE2}' --signature='%{SOURCE1}' --data='%{SOURCE0}'
%autosetup -p1
# Convert to utf-8
for file in ChangeLog; do
    mv $file timestamp
    iconv -f ISO-8859-1 -t UTF-8 -o $file timestamp
    touch -r timestamp $file
done

%build
%configure
%make_build

%install
%make_install
# Remove copy of documentation files installed by package's buildsystem.
# Preverred over patching Makefile.am an regenerating Makefile.in due
# to robustness.
rm -r %{buildroot}%{_defaultdocdir}

%files
%doc AUTHORS NEWS README TODO ChangeLog src/mbsyncrc.sample
%license COPYING
%{_bindir}/mbsync
%{_bindir}/mdconvert
%{_bindir}/mbsync-get-cert
%{_mandir}/man1/*

%changelog
* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Thu Sep 26 2024 Charles R. Anderson <cra@alum.wpi.edu> - 1.5.0-2
- Apply post-1.5.0 fixes from master branch:
- fix implicit listing of Maildir INBOX under Path
- improve reporting of failure to open previously present mailbox
- fix typos
- add missing trailing newlines in error() calls
- fix IMAP INBOX case normalization (rhbz#2314719)
- fix initial build from git

* Mon Aug 19 2024 Fabio Alessandro Locati <fale@fedoraproject.org> - 1.5.0-1
- Update to 1.5.0, fixes rhbz#2302484
- Fix crash caused by LTO, fixes rhbz#2302132

* Fri Jul 26 2024 Miroslav Suchý <msuchy@redhat.com> - 1.4.4-10
- convert license to SPDX

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.4-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Wed Jan 24 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.4-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sat Jan 20 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.4-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.4-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.4-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Mon Jan 09 2023 Jakub Kadlcik <frostyx@email.cz> - 1.4.4-4
- Apply OpenSSL EOF patch

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Dec  3 2021 Dan Čermák <dan.cermak@cgc-instruments.com> - 1.4.4-1
- New upstream release 1.4.4
- Fixes rhbz#2028810
- Fixes CVE-2021-3657
- Fixes CVE-2021-44143

* Tue Sep 14 2021 Sahana Prasad <sahana@redhat.com> - 1.4.3-2
- Rebuilt with OpenSSL 3.0.0

* Thu Aug 26 2021 Fabian Affolter <mail@fabian-affolter.ch> - 1.4.3-1
- Update to latest upstream release 1.4.3 (rhbz#1987273)

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Mon Jun  7 2021 Dan Čermák <dan.cermak@cgc-instruments.com> - 1.4.2-1
- New upstream release 1.4.2
- Fixes CVE-2021-3578
- Fixes rhbz#1968431

* Mon Feb 22 2021 Fabian Affolter <mail@fabian-affolter.ch> - 1.4.1-1
- Update to latest upstream release 1.4.1 (#1931574)
- Fix CVE-2021-20247 (#1931597, #1931598)

* Thu Feb 04 2021 Fabian Affolter <mail@fabian-affolter.ch> - 1.4.0-1
- Update to latest upstream release 1.4.0 (#1924724)

* Wed Feb 03 2021 Fabian Affolter <mail@fabian-affolter.ch> - 1.3.4-1
- Update to latest upstream release 1.3.4 (#1924724)

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Thu Aug 06 2020 Fabian Affolter <mail@fabian-affolter.ch> - 1.3.3-1
- Update to latest upstream release 1.3.3 (#1865992)

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Jul 10 2020 Fabian Affolter <mail@fabian-affolter.ch> - 1.3.2-1
- Update to latest upstream release 1.3.2 (#1854842)

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Wed May 29 2019 Fabian Affolter <mail@fabian-affolter.ch> - 1.3.1-1
- Support for SNI (#1632958)
- Update to new upstream version 1.3.1 (#1714679)

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Sun Jan 07 2018 Michael J Gruber <mjg@fedoraproject.org> - 1.3.0-1
- Update to new upstream version 1.3.0 (rhbz#1497574)

* Sun Oct 01 2017 Fabian Affolter <mail@fabian-affolter.ch> - 1.2.3-1
- Update to new upstream version 1.2.3 (rhbz#1497526)

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Mar 25 2017 Fabian Affolter <mail@fabian-affolter.ch> - 1.2.1-4
- Fix FTBFS (rhbz#1423747)

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Tue Nov 10 2015 Fabian Affolter <mail@fabian-affolter.ch> - 1.2.1-1
- Update to new upstream version 1.2.0 (rhbz#1279883)

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Tue Apr 07 2015 Ralph Bean <rbean@redhat.com> - 1.2.0-2
- Build against cyrus-sasl-devel

* Sun Apr 05 2015 Fabian Affolter <mail@fabian-affolter.ch> - 1.2.0-1
- Update to new upstream version 1.2.0 (rhbz#1208851, rhbz#1193063)

* Fri Jan 23 2015 Fabian Affolter <mail@fabian-affolter.ch> - 1.1.2-1
- Update to new upstream version 1.1.2 (rhbz#1183529)

* Sat Aug 16 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Thu Jun 05 2014 Fabian Affolter <mail@fabian-affolter.ch> - 1.1.1-1
- Update to new upstream version 1.1.1

* Sat Dec 21 2013 Fabian Affolter <mail@fabian-affolter.ch> - 1.1.0-1
- Update to new upstream version 1.1.0

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Feb 20 2013 Fabian Affolter <mail@fabian-affolter.ch> 1.0.6-1
- Update to new upstream version 1.0.6

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.5-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sat Aug 04 2012 Parag Nemade <paragn AT fedoraproject DOT org> - 1.0.5-3
- Change BR: db4-devel to libdb-devel

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sun Apr 29 2012 Fabian Affolter <mail@fabian-affolter.ch> 1.0.5-1
- Update to new upstream version 1.0.5

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.4-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.4-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Fri Aug 21 2009 Tomas Mraz <tmraz@redhat.com> - 1.0.4-6
- Rebuilt with new openssl

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.4-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.4-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Mon Jan 19 2009 Fabian Affolter <mail@fabian-affolter.ch> 1.0.4-3
- Preserve time stamps
- Fixe encoding error

* Sat Jan 17 2009 Tomas Mraz <tmraz@redhat.com> 1.0.4-2
- Rebuild with new openssl

* Sat Feb 23 2008 Lubomir Kundrak <lkundrak@redhat.com> 1.0.4-1
- Update to 1.0.4
- Drop upstreamed patches (all!)

* Tue Feb 19 2008 Fedora Release Engineering <rel-eng@fedoraproject.org> - 1.0.3-7
- Autorebuild for GCC 4.3

* Mon Dec 17 2007 Lubomir Kundrak <lkundrak@redhat.com> 1.0.3-6
- gmail returns SEARCH with no argument (#420721)

* Sun Dec 16 2007 Lubomir Kundrak <lkundrak@redhat.com> 1.0.3-5
- mbsync was ignoring option letters from last argument (#425838)

* Sun Sep 09 2007 Lubomir Kundrak <lkundrak@redhat.com> 1.0.3-3
- Fix code for the case where open() is a macro. (thanks to Marek Mahut)
- Cosmetic fixes. (#282261) (thanks to Till Maas)

* Fri Sep 07 2007 Lubomir Kundrak <lkundrak@redhat.com> 1.0.3-2
- Added dependency on OpenSSL for SSL/TLS support

* Fri Sep 07 2007 Lubomir Kundrak <lkundrak@redhat.com> 1.0.3-1
- Initial package
