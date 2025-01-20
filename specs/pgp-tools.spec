%global tarballname signing-party

Name:           pgp-tools
Version:        2.10
Release:        15%{?dist}
Summary:        Collection of several utilities related to OpenPGP
# Automatically converted from old format: BSD and GPLv2+ - review is highly recommended.
License:        LicenseRef-Callaway-BSD AND GPL-2.0-or-later
URL:            https://salsa.debian.org/stappers/pgp-tools
Source0:        http://ftp.debian.org/debian/pool/main/s/%{tarballname}/%{tarballname}_%{version}.orig.tar.gz
Patch0:         0001-pgpring-port-to-OpenSSL.patch
Patch1:         gpgwrap_makefile.diff
BuildRequires: make
BuildRequires:  gcc
# for gpgring
BuildRequires:  openssl-devel
BuildRequires:  %{_bindir}/autoreconf
BuildRequires:  %{_bindir}/aclocal
# for gpgdir test suite
BuildRequires:  perl-generators
BuildRequires:  perl(Digest::MD5)
BuildRequires:  perl(GnuPG::Interface)
BuildRequires:  perl(Term::ReadKey)
# Building man pages
BuildRequires:  %{_bindir}/pod2man
Requires:       %{_bindir}/gpg
Recommends:     %{_sbindir}/sendmail
# for gpg-key2ps
Recommends:     %{_bindir}/paperconf

%description
This is a collection of several projects relating to OpenPGP.

* caff: CA - Fire and Forget signs and mails a key
* pgp-clean: removes all non-self signatures from key
* pgp-fixkey: removes broken packets from keys
* gpg-mailkeys: simply mail out a signed key to its owner
* gpg-key2ps: generate PostScript file with fingerprint paper slips
* gpgdir: recursive directory encryption tool
* gpglist: show who signed which of your UIDs
* gpgsigs: annotates list of GnuPG keys with already done signatures
* gpgparticipants: create list of party participants for the organiser
* gpgwrap: a passphrase wrapper
* keyanalyze: minimum signing distance (MSD) analysis on keyrings
* keylookup: ncurses wrapper around gpg --search
* sig2dot: converts a list of GnuPG signatures to a .dot file
* springgraph: creates a graph from a .dot file
* keyart: creates a random ASCII art of a PGP key file
* gpg-key2latex: generate LaTeX file with fingerprint paper slips

For more information on each of these tools, please see their respective
manpages. Please note that each individual project has its own license,
consult the licensing information in the subdirectories.

%prep
%setup -q -n %{tarballname}-%{version}
# fix gpgdir library path lookup as we're using system-provided libraries
sed -i -e "s,/usr/lib/gpgdir,," gpgdir/gpgdir
%patch -P0 -p1
%patch -P1 -p1

%build
%make_build \
    CFLAGS="$RPM_OPT_FLAGS" LDFLAGS="$RPM_LD_FLAGS" STRIP=: CC=%{__cc}

%install
%make_install
# apps with no 'make install'
for f in caff/{caff,pgp-clean,pgp-fixkey} \
         gpglist/gpglist \
         gpg-key2ps/gpg-key2ps \
         gpg-key2latex/gpg-key2latex \
         gpg-mailkeys/gpg-mailkeys \
         gpgparticipants/gpgparticipants{,-prefill} \
         gpgdir/gpgdir \
         gpgwrap/bin/gpgwrap \
         keyanalyze/pgpring/pgpring
do
  %{__install} -Dpm0755 -t %{buildroot}%{_bindir} $f
done

# find all manpages wherever they are hiding
%{__install} -Dpm0644 -t %{buildroot}%{_mandir}/man1 */*.1 */*/*.1

mv %{buildroot}%{_docdir}/{signing-party,%{expand:%{_docdir_fmt}}}

for f in $(find -type f \( -iname COPYING -o -iname LICENSE \))
do
  mv $f $(basename $f).$(basename $(dirname $f))
done

%check
pushd gpgdir/test
  ./gpgdir_test.pl
popd

%files
%license COPYING.* LICENSE.*
%{_pkgdocdir}
%{_bindir}/*
%{_mandir}/man1/*.1*

%changelog
* Sat Jan 18 2025 Fedora Release Engineering <releng@fedoraproject.org> - 2.10-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Wed Sep 04 2024 Miroslav Suchý <msuchy@redhat.com> - 2.10-14
- convert license to SPDX

* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.10-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.10-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.10-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.10-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.10-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.10-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.10-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Tue Sep 14 2021 Sahana Prasad <sahana@redhat.com> - 2.10-6
- Rebuilt with OpenSSL 3.0.0

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.10-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.10-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.10-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.10-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Tue Sep 17 2019 Lubomir Rintel <lkundrak@v3.sk> - 2.10-1
- Unbreak the build
- Update to 2.10
- Bring back pgpring
- Turn sendmail dependency into a weak one

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.7-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.7-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.7-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.7-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Sun Feb 04 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 2.7-1
- Update to 2.7

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.4-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.4-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Tue Jun 06 2017 Jitka Plesnikova <jplesnik@redhat.com> - 2.4-3
- Perl 5.26 rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Tue Sep 06 2016 Fabio Alessandro Locati <fale@redhat.com> - 2.4-1
- Update to 2.4

* Mon May 16 2016 Jitka Plesnikova <jplesnik@redhat.com> - 2.2-3
- Perl 5.24 rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 2.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Mon Jan 25 2016 Jochen Schmitt <Jochen herr-schmitt de> - 2.2-1
- New upstream release

* Thu Aug 13 2015 Jochen Schmitt <Jochen herr-schmitt de> - 2.1-1
- New upstram release
- remove spcial handling of testsuite R generation

* Thu Jul 30 2015 Jochen Schmitt <Jochen herr-schmitt de> - 1.1.12-7
- Rebuilt to fix dep. issues

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.12-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Mon Jun 08 2015 Jitka Plesnikova <jplesnik@redhat.com> - 1.1.12-5
- Perl 5.22 rebuild

* Sun Feb 15 2015 Jochen Schmitt <Jochen herr-schmitt de> - 1.1.12-4
- Fix chnagelog entry

* Wed Feb 11 2015 Jochen Schmitt <Jochen herr-schmitt de> - 1.1.12-3
 - Using of  $RPM_OPT_cFLOAGS and $RPM_LD_FLAGS to buid (#1185529) 

* Wed Feb  4 2015 Jochen Schmitt <Jochen herr-schmitt de> - 1.1.12-2
- New upstream release

* Wed Jan 21 2015 Jochen Schmitt <Jochen herr-schmitt de> - 1.1.10-2
- Fix dependency issue agains perl(for) (#1184547)

* Sat Jan 10 2015 Jochen Schmitt <Jochen herr-schmitt de> - 1.1.10-1
- New upstream release

* Sun Dec  7 2014 Jochen Schmitt <Jochen herr-schmitt de> - 1.1.5-7
- Add reference to 'signing-party' in the package description (#1171393)

* Wed Sep 10 2014 Jochen Schmitt <Jochen herr-schmitt de> - 1.1.5-6
- Fix Unicode-issue (#1139704)

* Tue Sep 02 2014 Jitka Plesnikova <jplesnik@redhat.com> - 1.1.5-5
- Perl 5.20 rebuild

* Sat Aug 23 2014 Jochen Schmitt <Jochen herr-schmitt de> - 1.1.5-4
- Fix error in gpg-key2ps (#1121353)

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.5-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Thu Mar  6 2014 Jochen Schmitt <Jochen herr-schmitt de> - 1.1.5-1
- New upstream release, fix caff <keyid> issue (#10734121)

* Sun Aug 04 2013 Petr Pisar <ppisar@redhat.com> - 1.1.4-3
- Perl 5.18 rebuild

* Sat Aug  3 2013 Jochen Schmitt <Jochen herr-schmitt de> - 1.1.4-2
- Rebuilt for perl-5.18.0

* Sun Jun 16 2013 Jochen Schmitt <Jochen herr-schmitt de> - 1.4.1-1
- New upstream release
- Add Req libpaper for gpg-key2ps
- Fix local issue with the paper size (#831211)

* Sun Feb 17 2013 Jochen Schmitt <Jochen herr-schmitt de> - 1.1.3-11
- Add perl-podlators as a BR
- Remove BuildRoot definition

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.3-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.3-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jun 22 2012 Petr Pisar <ppisar@redhat.com> - 1.1.3-8
- Perl 5.16 rebuild

* Mon Apr 30 2012 Paul Howarth <paul@city-fan.org> - 1.1.3-7
- Fix dependency declaration for Digest::MD5

* Mon Apr 30 2012 Peter Robinson <pbrobinson@fedoraproject.org> - 1.1.3-6
- Add missing perl module to fix FTBFS

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.3-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Thu Jul 21 2011 Petr Sabata <contyk@redhat.com> - 1.1.3-4
- Perl mass rebuild

* Tue Jul 19 2011 Petr Sabata <contyk@redhat.com> - 1.1.3-3
- Perl mass rebuild

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Tue Sep  7 2010 Jochen Schmitt <Jochen herr-schmitt de> - 1.1.3-1
- New upstream release
- Get Source from http://ftp.debian.org
- Upstream tarball contains verbain license text

* Tue Jun 01 2010 Marcela Maslanova <mmaslano@redhat.com> - 1.1-5
- Mass rebuild with perl-5.12.0

* Mon Dec  7 2009 Stepan Kasal <skasal@redhat.com> - 1.1-4
- rebuild against perl 5.10.1

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Fri Apr 17 2009 Matt Domsch <mdomsch@fedoraproject.org> - 1.1-2
- add BRs so %%check succeeds
- drop upstream's outdated copy of pgpring. mutt provides a newer
  version, so require mutt.

* Fri Apr 17 2009 Matt Domsch <mdomsch@fedoraproject.org> - 1.1-1
- update to 1.1
  adds gpgdir, gpgwrap, keyanalyze

* Thu Feb 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Tue May 20 2008 Matt Domsch <Matt_Domsch@dell.com> 1.0-1
- upgrade to 1.0-1
  - gpgsigs: Implement support for LaTeX output and photo ids.
    (Closes: debian #412433, #430607)
  - gpg-key2ps: Mention http://www.debian.org/events/materials/business-cards/
    as an alternative. (Closes: debian #439510)
  - add sig2dot and springgraph

* Tue Feb  5 2008 Tom "spot" Callaway <tcallawa@redhat.com> 0.4.12-2
- rebuild for new perl (and fix license tag)

* Wed Sep 19 2007 Matt Domsch <Matt_Domsch@dell.com> 0.4.12-1
- upgrade to 0.4.12
- cleanup doc installation (BZ#246433)

* Thu Nov 02 2006 Matt Domsch <Matt_Domsch@dell.com> 0.4.9-1
- upgrade to 0.4.9
  - Fix a bug with checking if we have exactly one or more keys that failed downloading.
  - Mention in manpage that keyserver-options is a useful setting in
    .caff/gnupghome/gpg.conf (Closes: debian #392811).
  - q-p-encode From: header (Closes: debian #366745).

* Sat Oct 07 2006 Matt Domsch <Matt_Domsch@dell.com> 0.4.8-1
- upgrade to 0.4.8
  - gpglist: do not die with with-fingerprint (Closes: debian #382019).
  - gpg-key2ps: add --list-key to gpg call (works around debian #382794).
  - caff: when set, use $ENV{'GNUPGHOME'} to find secring.gpg. Suggested by
    Gerfried Fuchs.

* Mon Jul 10 2006 Matt Domsch <Matt_Domsch@dell.com> 0.4.7-1
- upgrade to latest upstream
  - gpg-mailkeys: use right content-type for attached key,
    thanks Wesley Landaker (Closes: debian #370566).
  - upstream releasing tarballs now, so use those

* Thu May 25 2006 Matt Domsch <Matt_Domsch@dell.com> 0.4.6-1.20060525svn
- upgrade to lastest upstream

* Sun Feb 12 2006 Matt Domsch <Matt_Domsch@dell.com> 0.4.4-3.20060212svn
- upgrade to lastest upstream
- rebuild for FC5

* Tue Nov 29 2005 Matt Domsch <Matt_Domsch@dell.com> 0.4.4-3.20051123svn
- require perl(Locale::Recode) for gpgsigs

* Mon Nov 28 2005 Matt Domsch <Matt_Domsch@dell.com> 0.4.4-2.20051123svn
- cleanups based on feedback from dmitry@butskoy.name

* Thu Nov 10 2005 Matt Domsch <Matt_Domsch@dell.com> 0.4.4-1
- initial release
