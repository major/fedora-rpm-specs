Name:           perl-Mail-IMAPClient
Version:        3.43
Release:        13%{?dist}
Summary:        An IMAP Client API
# Automatically converted from old format: GPL+ or Artistic - review is highly recommended.
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Mail-IMAPClient
Source0:        https://cpan.metacpan.org/authors/id/P/PL/PLOBBES/Mail-IMAPClient-%{version}.tar.gz
BuildRequires: make
BuildRequires:  perl-generators
BuildRequires:  perl(ExtUtils::MakeMaker), perl(IO::Socket), perl(constant), perl(Socket)
BuildRequires:  perl(IO::File), perl(IO::Select), perl(Fcntl), perl(Errno), perl(Carp)
BuildRequires:  perl(Data::Dumper), perl(Parse::RecDescent), perl(Test::More)
BuildRequires:	perl(Authen::SASL), perl(Test::Pod)
BuildArch:      noarch

%description
This module provides perl routines that simplify a sockets connection
to and an IMAP conversation with an IMAP server.

%prep
%setup -q -n Mail-IMAPClient-%{version}
sed -i 's#/usr/local/bin/perl#/usr/bin/perl#' examples/*.pl

# Turn off exec bits in examples to avoid docfile dependencies
chmod -c -x examples/*.pl

# Fix character encoding in documentation
iconv -f iso-8859-1 -t utf-8 < Changes > Changes.utf8
mv Changes.utf8 Changes

%build
# the extended tests cannot be run without an IMAP server
yes n | %{__perl} Makefile.PL INSTALLDIRS=vendor
make

%install
rm -rf $RPM_BUILD_ROOT
make pure_install PERL_INSTALL_ROOT=$RPM_BUILD_ROOT
find $RPM_BUILD_ROOT -type f -name .packlist -exec rm -f {} ';'
chmod -R u+w $RPM_BUILD_ROOT/*

%check
make test

%files
%doc Changes README examples/
%{perl_vendorlib}/Mail/
%{_mandir}/man3/*.3*

%changelog
* Sat Jan 18 2025 Fedora Release Engineering <releng@fedoraproject.org> - 3.43-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Tue Aug 06 2024 Miroslav Suchý <msuchy@redhat.com> - 3.43-12
- convert license to SPDX

* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 3.43-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 3.43-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 3.43-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 3.43-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 3.43-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 3.43-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed Jun 01 2022 Jitka Plesnikova <jplesnik@redhat.com> - 3.43-5
- Perl 5.36 rebuild

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 3.43-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 3.43-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri May 21 2021 Jitka Plesnikova <jplesnik@redhat.com> - 3.43-2
- Perl 5.34 rebuild

* Tue Feb 16 2021 Tom Callaway <spot@fedoraproject.org> - 3.43-1
- update to 3.43

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 3.42-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.42-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jun 23 2020 Jitka Plesnikova <jplesnik@redhat.com> - 3.42-5
- Perl 5.32 rebuild

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.42-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.42-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri May 31 2019 Jitka Plesnikova <jplesnik@redhat.com> - 3.42-2
- Perl 5.30 rebuild

* Thu Feb 28 2019 Tom Callaway <spot@fedoraproject.org> - 3.42-1
- update to 3.42

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.40-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Dec  6 2018 Tom Callaway <spot@fedoraproject.org> - 3.40-1
- update to 3.40

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.39-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Jun 28 2018 Jitka Plesnikova <jplesnik@redhat.com> - 3.39-5
- Perl 5.28 rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.39-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.39-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Mon Jun 05 2017 Jitka Plesnikova <jplesnik@redhat.com> - 3.39-2
- Perl 5.26 rebuild

* Tue Feb  7 2017 Tom Callaway <spot@fedoraproject.org> - 3.39-1
- update to 3.39

* Sun May 15 2016 Jitka Plesnikova <jplesnik@redhat.com> - 3.38-2
- Perl 5.24 rebuild

* Thu Feb 11 2016 Tom Callaway <spot@fedoraproject.org> - 3.38-1
- update to 3.38

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 3.37-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Sep 24 2015 Tom Callaway <spot@fedoraproject.org> - 3.37-1
- update to 3.37

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.35-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Fri Jun 05 2015 Jitka Plesnikova <jplesnik@redhat.com> - 3.35-4
- Perl 5.22 rebuild

* Thu Aug 28 2014 Jitka Plesnikova <jplesnik@redhat.com> - 3.35-3
- Perl 5.20 rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.35-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Thu Mar 13 2014 Nick Bebout <nb@fedoraproject.org> - 3.35-1
- Upgrade to 3.35

* Thu Oct 17 2013 Nick Bebout <nb@fedoraproject.org> - 3.34-1
- Upgrade to 3.34

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.33-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Mon Jul 22 2013 Petr Pisar <ppisar@redhat.com> - 3.33-2
- Perl 5.18 rebuild

* Tue May 21 2013 Nick Bebout <nb@fedoraproject.org> - 3.33-1
- Upgrade to 3.33

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.32-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Tue Sep 11 2012 Nick Bebout <nb@fedoraproject.org> - 3.32-1
- Upgrade to 3.32

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.31-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sat Jun 16 2012 Petr Pisar <ppisar@redhat.com> - 3.31-2
- Perl 5.16 rebuild

* Mon Apr 16 2012 Nick Bebout <nb@fedoraproject.org> - 3.31-1
- Upgrade to 3.31

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.30-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Dec 13 2011 Nick Bebout <nb@fedoraproject.org> - 3.30-1
- Upgrade to 3.30

* Mon Jun 20 2011 Marcela Mašláňová <mmaslano@redhat.com> - 3.28-2
- Perl mass rebuild

* Wed Mar 16 2011 Nick Bebout <nb@fedoraproject.org> - 3.28-1
- Upgrade to 3.28

* Mon Feb 21 2011 Nick Bebout <nb@fedoraproject.org> - 3.27-1
- Upgrade to 3.27

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.25-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Sat Oct  2 2010 Paul Howarth <paul@city-fan.org> - 3.25-2
- turn off exec bits on examples to avoid docfile dependencies (#639523)
- fix character encoding in documentation

* Mon Jul 12 2010 Tom "spot" Callaway <tcallawa@redhat.com> - 3.25-1
- update to 3.25

* Mon May 03 2010 Marcela Maslanova <mmaslano@redhat.com> - 3.21-3
- Mass rebuild with perl-5.12.0

* Mon Dec  7 2009 Stepan Kasal <skasal@redhat.com> - 3.21-2
- rebuild against perl 5.10.1

* Fri Sep 25 2009 Stepan Kasal <skasal@redhat.com> - 3.21-1
- new upstream source

* Sat Sep  5 2009 Stepan Kasal <skasal@redhat.com> - 3.20-1
- new upstream source

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.14-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Fri Mar 13 2009 Tom "spot" Callaway <tcallawa@redhat.com> - 3.14-1
- update to 3.14

* Thu Feb 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.08-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Mon Jul 21 2008 Tom "spot" Callaway <tcallawa@redhat.com> - 3.08-1
- 3.08

* Tue Mar 11 2008 Tom "spot" Callaway <tcallawa@redhat.com> - 3.05-1
- 3.05

* Wed Feb 27 2008 Tom "spot" Callaway <tcallawa@redhat.com> - 2.2.9-6
- Rebuild for perl 5.10 (again)

* Mon Jan 28 2008 Tom "spot" Callaway <tcallawa@redhat.com> - 2.2.9-5
- rebuild for new perl

* Sun Aug 26 2007 Tom "spot" Callaway <tcallawa@redhat.com> - 2.2.9-4
- license tag fix

* Mon Apr  9 2007 Tom "spot" Callaway <tcallawa@redhat.com> - 2.2.9-3
- set examples as non-exec, fix intepreter

* Wed Apr  4 2007 Tom "spot" Callaway <tcallawa@redhat.com> - 2.2.9-2
- add docs/ and examples/ as %%doc

* Mon Apr  2 2007 Tom "spot" Callaway <tcallawa@redhat.com> - 2.2.9-1
- Initial package for Fedora
