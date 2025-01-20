Name:           perl-Text-Kakasi
Version:        2.04
Release:        59%{?dist}
Summary:        Kakasi library module for perl

License:        GPL-2.0-or-later
Url:            https://metacpan.org/release/Text-Kakasi
Source0:        https://cpan.metacpan.org/authors/id/D/DA/DANKOGAI/Text-Kakasi-2.04.tar.gz
Patch:          Text-Kakasi-1.04-perl580.diff

BuildRequires: make
BuildRequires:  perl-interpreter >= 2:5.8.0
BuildRequires:  perl-devel
BuildRequires:  perl-generators
BuildRequires:  kakasi-devel >= 2.3.1, kakasi-dict
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  gcc
Requires:       kakasi >= 2.3.1

%description
This module provides libkakasi interface for perl. libkakasi is a part
of KAKASI.  KAKASI is the language processing filter to convert Kanji
characters to Hiragana, Katakana or Romaji and may be helpful to read
Japanese documents.
More information about KAKASI is available at <http://kakasi.namazu.org/>.


%prep
%autosetup -n Text-Kakasi-%{version}

%build
CFLAGS="$RPM_OPT_FLAGS" %{__perl} Makefile.PL INSTALLDIRS=vendor
make OPTIMIZE="$RPM_OPT_FLAGS"

%install
rm -rf $RPM_BUILD_ROOT
make pure_install PERL_INSTALL_ROOT=$RPM_BUILD_ROOT
find $RPM_BUILD_ROOT -type f -name .packlist -exec rm -f {} ';'
find $RPM_BUILD_ROOT -type f -name '*.bs' -a -size 0 -exec rm -f {} ';'
find $RPM_BUILD_ROOT -type d -depth -exec rmdir {} 2>/dev/null ';'
chmod -R u+w $RPM_BUILD_ROOT/*

file=$RPM_BUILD_ROOT%{_mandir}/man3/Text::Kakasi.3pm
iconv -f euc-jp -t utf-8 < "$file" > "${file}_"
mv -f "${file}_" "$file"

%check
make test


%files
%license COPYING
%{perl_vendorarch}/Text/
%{perl_vendorarch}/auto/Text/
%{_mandir}/man3/*.3*


%changelog
* Sat Jan 18 2025 Fedora Release Engineering <releng@fedoraproject.org> - 2.04-59
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.04-58
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Mon Jun 10 2024 Jitka Plesnikova <jplesnik@redhat.com> - 2.04-57
- Perl 5.40 rebuild

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.04-56
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.04-55
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.04-54
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Tue Jul 11 2023 Jitka Plesnikova <jplesnik@redhat.com> - 2.04-53
- Perl 5.38 rebuild

* Tue May 30 2023 Akira TAGOH <tagoh@redhat.com> - 2.04-52
- Fix %%patchN deprecation.
  Resolves: rhbz#2210972

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.04-51
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Mon Dec  5 2022 Akira TAGOH <tagoh@redhat.com> - 2.04-50
- Convert License tag to SPDX.

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.04-49
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon May 30 2022 Jitka Plesnikova <jplesnik@redhat.com> - 2.04-48
- Perl 5.36 rebuild

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.04-47
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.04-46
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri May 21 2021 Jitka Plesnikova <jplesnik@redhat.com> - 2.04-45
- Perl 5.34 rebuild

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.04-44
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.04-43
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Jun 22 2020 Jitka Plesnikova <jplesnik@redhat.com> - 2.04-42
- Perl 5.32 rebuild

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.04-41
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.04-40
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu May 30 2019 Jitka Plesnikova <jplesnik@redhat.com> - 2.04-39
- Perl 5.30 rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.04-38
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.04-37
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Jun 27 2018 Jitka Plesnikova <jplesnik@redhat.com> - 2.04-36
- Perl 5.28 rebuild

* Mon Feb 19 2018 Akira TAGOH <tagoh@redhat.com> - 2.04-35
- Add BR: gcc

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.04-34
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.04-33
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.04-32
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sun Jun 04 2017 Jitka Plesnikova <jplesnik@redhat.com> - 2.04-31
- Perl 5.26 rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.04-30
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Sat May 14 2016 Jitka Plesnikova <jplesnik@redhat.com> - 2.04-29
- Perl 5.24 rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 2.04-28
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.04-27
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Wed Jun 03 2015 Jitka Plesnikova <jplesnik@redhat.com> - 2.04-26
- Perl 5.22 rebuild

* Wed Aug 27 2014 Jitka Plesnikova <jplesnik@redhat.com> - 2.04-25
- Perl 5.20 rebuild

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.04-24
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.04-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.04-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Jul 17 2013 Petr Pisar <ppisar@redhat.com> - 2.04-21
- Perl 5.18 rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.04-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.04-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jun 08 2012 Petr Pisar <ppisar@redhat.com> - 2.04-18
- Perl 5.16 rebuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.04-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Fri Jun 17 2011 Marcela Mašláňová <mmaslano@redhat.com> - 2.04-16
- Perl mass rebuild

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.04-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Thu Dec 23 2010 Marcela Maslanova <mmaslano@redhat.com> - 2.04-14
- 661697 rebuild for fixing problems with vendorach/lib

* Fri May 07 2010 Marcela Maslanova <mmaslano@redhat.com> - 2.04-13
- Mass rebuild with perl-5.12.0

* Fri Dec  4 2009 Stepan Kasal <skasal@redhat.com> - 2.04-12
- rebuild against perl 5.10.1

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.04-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Thu Feb 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.04-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Tue Jun  3 2008 Akira TAGOH <tagoh@redhat.com> - 2.04-9
- Fix FTFBS. (#449405)

* Thu Mar 06 2008 Tom "spot" Callaway <tcallawa@redhat.com> - 2.04-8
Rebuild for new perl

* Tue Feb 12 2008 Akira TAGOH <tagoh@redhat.com> - 2.04-7
- Rebuild for gcc-4.3.

* Tue Oct 16 2007 Akira TAGOH <tagoh@redhat.com> - 2.04-6
- Add BR perl(ExtUtils::MakeMaker)

* Thu Aug 23 2007 Akira TAGOH <tagoh@redhat.com> - 2.04-5
- Rebuild

* Fri Aug 10 2007 Akira TAGOH <tagoh@redhat.com> - 2.04-4
- Update License tag.

* Mon Sep 11 2006 Akira TAGOH <tagoh@redhat.com> - 2.04-3
- rebuilt

* Thu Mar  2 2006 Akira TAGOH <tagoh@redhat.com> - 2.04-2
- rebuilt.

* Mon May 30 2005 Akira TAGOH <tagoh@redhat.com> - 2.04-1
- Updates to 2.04.
- import to Extras.

* Sat Apr 30 2005 Jose Pedro Oliveira <jpo at di.uminho.pt> - 1.05-13
- Added missing build requirement: kakasi-dict. (#156479)
- Bring up to date with current Fedora.Extras perl spec template.

* Thu Nov 25 2004 Miloslav Trmac <mitr@redhat.com> - 1.05-12
- Convert man page to UTF-8

* Tue Jun 15 2004 Elliot Lee <sopwith@redhat.com>
- rebuilt

* Tue Mar 02 2004 Elliot Lee <sopwith@redhat.com>
- rebuilt

* Fri Feb 13 2004 Elliot Lee <sopwith@redhat.com>
- rebuilt

* Wed Jun 04 2003 Elliot Lee <sopwith@redhat.com>
- rebuilt

* Mon Jun 02 2003 Akira TAGOH <tagoh@redhat.com> 1.05-7
- don't specify rpath. (#66120)
- removed Kakasi.bs.

* Thu May 22 2003 Jeremy Katz <katzj@redhat.com> 1.05-6
- fix rebuilding

* Wed Jan 22 2003 Tim Powers <timp@redhat.com>
- rebuilt

* Sat Dec 14 2002 Tim Powers <timp@redhat.com> 1.05-4
- don't use rpms internal dep generator

* Wed Nov 20 2002 Tim Powers <timp@redhat.com>
- rebuild in current collinst

* Thu Aug 15 2002 Tim Powers <timp@redhat.com>
- clean up file list so that we pick up the man page from the correct place

* Thu Jul 18 2002 Akira TAGOH <tagoh@redhat.com> 1.05-1
- New upstream release.
- add the owned directory.
- clean up for spec.
- moved site_perl to vendor_perl

* Tue Jun 25 2002 Yukihiro Nakai <ynakai@redhat.com>
- Delete Japanese description
- Fix for perl 5.8.0 (#67002)

* Thu May 23 2002 Tim Powers <timp@redhat.com>
- automated rebuild

* Wed Jan 09 2002 Tim Powers <timp@redhat.com>
- automated rebuild

* Wed Jul 25 2001 Tim Powers <timp@redhat.com>
- remove perl temp files

* Sun Jun 24 2001 Elliot Lee <sopwith@redhat.com>
- Bump release + rebuild.

* Mon Dec 11 2000 Akira Tagoh <tagoh@redhat.com>
- Rebuild for 7.1

* Mon Aug 07 2000 Yukihiro Nakai <ynakai@redhat.com>
- Rebuild for 7.0J

* Mon Apr 10 2000 Ryuji Abe <raeva@t3.rim.or.jp>
- version 1.04.

* Thu Apr 06 2000 Ryuji Abe <raeva@t3.rim.or.jp>
- version 1.02.

* Tue Feb 08 2000 Ryuji Abe <raeva@t3.rim.or.jp>
- Changed group (Utilities/Text -> Applications/Text).

* Sat Dec 11 1999 Ryuji Abe <raeva@t3.rim.or.jp>
- Rebuild for RHL-6.1.

* Fri Dec 03 1999 Ryuji Abe <raeva@t3.rim.or.jp>
- version 1.01.

* Wed Dec 01 1999 Ryuji Abe <raeva@t3.rim.or.jp>
- First build.
