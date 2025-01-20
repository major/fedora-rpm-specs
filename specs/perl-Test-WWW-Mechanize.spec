Name:           perl-Test-WWW-Mechanize
Version:        1.60
Release:        7%{?dist}
Summary:        Testing-specific WWW::Mechanize subclass

License:        Artistic-2.0
URL:            https://metacpan.org/release/Test-WWW-Mechanize
Source0:        https://cpan.metacpan.org/authors/id/P/PE/PETDANCE/Test-WWW-Mechanize-%{version}.tar.gz

BuildArch:      noarch

BuildRequires:  %{__perl}
BuildRequires:  %{__make}

BuildRequires:  perl(:VERSION) >= 5.10.0

BuildRequires:  perl-generators
BuildRequires:  perl(Carp)
BuildRequires:  perl(Carp::Assert::More) >= 1.16
BuildRequires:  perl(CGI)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(HTML::Lint)
BuildRequires:  perl(HTML::TokeParser)
# N/A in Fedora
# BuildRequires:  perl(HTML::Tidy5) >= 1.00
BuildRequires:  perl(HTTP::Message) >= 6.29
BuildRequires:  perl(HTTP::Server::Simple) >= 0.42
BuildRequires:  perl(HTTP::Server::Simple::CGI)
BuildRequires:  perl(LWP) >= 6.02
BuildRequires:  perl(Test::Builder)
BuildRequires:  perl(Test::Builder::Tester) >= 1.09
BuildRequires:  perl(Test::LongString) >= 0.15
BuildRequires:  perl(Test::More) >= 0.96
BuildRequires:  perl(Test::Pod) >= 0.08
BuildRequires:  perl(Test::Pod::Coverage) >= 1.00
BuildRequires:  perl(URI::file)
BuildRequires:  perl(WWW::Mechanize) >= 1.68
BuildRequires:  perl(parent)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)

Requires:       perl(WWW::Mechanize) >= 1.68
%global __requires_exclude %{?__requires_exclude:%__requires_exclude|}^perl\\(WWW::Mechanize\\)

%description
Test::WWW::Mechanize is a subclass of WWW::Mechanize that incorporates
features for web application testing.


%prep
%setup -q -n Test-WWW-Mechanize-%{version}

# Propagate build-time requirement Carp::Assert::More >= 1.16 to run-time
sed -i -e 's|use Carp::Assert::More|use Carp::Assert::More 1.16|' Mechanize.pm

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1
%{make_build}

%install
%{make_install} DESTDIR="$RPM_BUILD_ROOT"
%{_fixperms} $RPM_BUILD_ROOT/*


%check
%{__make} test

%files
%doc Changes README*
%{perl_vendorlib}/Test
%{_mandir}/man3/*.3pm*


%changelog
* Sat Jan 18 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.60-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.60-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.60-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.60-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.60-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.60-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Sat Dec 17 2022 Ralf Corsépius <corsepiu@fedoraproject.org> - 1.60-1
- Update to 1.60.

* Mon Nov 28 2022 Ralf Corsépius <corsepiu@fedoraproject.org> - 1.58-5
- Convert license to SPDX.

* Wed Jul 27 2022 Ralf Corsépius <corsepiu@fedoraproject.org> - 1.58-4
- Add 0001-Fix-Odd-number-of-elements-in-hash-assignment-warnin.patch (RHBZ#2111408).

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.58-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed Jun 01 2022 Jitka Plesnikova <jplesnik@redhat.com> - 1.58-2
- Perl 5.36 rebuild

* Thu May 19 2022 Ralf Corsépius <corsepiu@fedoraproject.org> - 1.58-1
- Update to 1.58.

* Thu Apr 28 2022 Ralf Corsépius <corsepiu@fedoraproject.org> - 1.56-1
- Update to 1.56.
- Modernize spec.

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.54-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.54-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Sat May 22 2021 Jitka Plesnikova <jplesnik@redhat.com> - 1.54-3
- Perl 5.34 rebuild

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.54-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Dec 15 2020 Ralf Corsépius <corsepiu@fedoraproject.org> - 1.54-1
- Update to 1.54.

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.52-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jun 23 2020 Jitka Plesnikova <jplesnik@redhat.com> - 1.52-6
- Perl 5.32 rebuild

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.52-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.52-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri May 31 2019 Jitka Plesnikova <jplesnik@redhat.com> - 1.52-3
- Perl 5.30 rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.52-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Dec 07 2018 Ralf Corsépius <corsepiu@fedoraproject.org> - 1.52-1
- Update to 1.52.

* Mon Aug 13 2018 Ralf Corsépius <corsepiu@fedoraproject.org> - 1.50-1
- Update to 1.50.

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.48-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Jun 29 2018 Jitka Plesnikova <jplesnik@redhat.com> - 1.48-6
- Perl 5.28 rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.48-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.48-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Tue Jun 06 2017 Jitka Plesnikova <jplesnik@redhat.com> - 1.48-3
- Perl 5.26 rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.48-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Sun Jan 08 2017 Ralf Corsépius <corsepiu@fedoraproject.org> - 1.48-1
- Update to 1.48.

* Tue Aug 02 2016 Ralf Corsépius <corsepiu@fedoraproject.org> - 1.46-1
- Upstream update.
- Add BR: perl(HTML::TokeParser).

* Mon May 16 2016 Jitka Plesnikova <jplesnik@redhat.com> - 1.44-12
- Perl 5.24 rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.44-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Sat Jan 30 2016 Ralf Corsépius <corsepiu@fedoraproject.org> - 1.44-10
- Modernize spec.

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.44-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Jun 06 2015 Jitka Plesnikova <jplesnik@redhat.com> - 1.44-8
- Perl 5.22 rebuild

* Fri Aug 29 2014 Jitka Plesnikova <jplesnik@redhat.com> - 1.44-7
- Perl 5.20 rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.44-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Petr Pisar <ppisar@redhat.com> - 1.44-5
- Perl 5.18 rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.44-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.44-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Wed Jul 11 2012 Petr Pisar <ppisar@redhat.com> - 1.44-2
- Perl 5.16 rebuild

* Tue Jul 10 2012 Ralf Corsépius <corsepiu@fedoraproject.org> - 1.44-1
- Upstream update.

* Thu Jun 28 2012 Petr Pisar <ppisar@redhat.com> - 1.42-2
- Perl 5.16 rebuild

* Wed Jun 27 2012 Ralf Corsépius <corsepiu@fedoraproject.org> - 1.42-1
- Upstream update.

* Thu Jun 21 2012 Petr Pisar <ppisar@redhat.com> - 1.40-2
- Perl 5.16 rebuild

* Mon Apr 30 2012 Ralf Corsépius <corsepiu@fedoraproject.org> - 1.40-1
- Upstream update.

* Sat Jan 14 2012 Ralf Corsépius <corsepiu@fedoraproject.org> - 1.38-1
- Upstream update.
- Add rpm-4.9 filter.

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.34-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Sun Oct 02 2011 Iain Arnell <iarnell@gmail.com> 1.34-1
- update to latest upstream version
- license change again - Artistic 2.0 only

* Wed Jul 20 2011 Petr Sabata <contyk@redhat.com> - 1.32-2
- Perl mass rebuild

* Sat May 14 2011 Iain Arnell <iarnell@gmail.com> 1.32-1
- update to latest upstream and drop patches
- fix license tag: GPL+ or Artistic 2.0

* Mon Apr 11 2011 Ralf Corsépius <corsepiu@fedoraproject.org> - 1.30-3
- Add Test-WWW-Mechanize-1.30-svn.r712.diff (Fix FTBS on f13/f14/f15).
- Add Test-WWW-Mechanize-1.30-Test-LongString.diff (Fix FTBS on f16).
- Spec file cleanup.

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.30-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Mon Dec 20 2010 Ralf Corsépius <corsepiu@fedoraproject.org> - 1.30-1
- Upstream update.
- BR: perl(HTML::TreeBuilder).

* Wed Dec 08 2010 Ralf Corsépius <corsepiu@fedoraproject.org> - 1.28-2
- Add BR: perl(CGI) (Fix FTBFS: BZ 661092).

* Thu May 13 2010 Petr Pisar <ppisar@redhat.com> - 1.28-1
- Version bump
- Sort dependencies

* Fri May 07 2010 Marcela Maslanova <mmaslano@redhat.com> - 1.24-6
- Mass rebuild with perl-5.12.0

* Fri Dec  4 2009 Stepan Kasal <skasal@redhat.com> - 1.24-5
- rebuild against perl 5.10.1

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.24-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Thu Feb 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.24-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Sat Feb 21 2009 Ralf Corsepius <corsepiu@fedoraproject.org> - 1.24-2
- Add BR: perl(HTML::Lint).

* Fri Feb 20 2009 Ralf Corsepius <corsepiu@fedoraproject.org> - 1.24-1
- Upstream update.

* Wed Jun 25 2008 Chris Weyl <cweyl@alumni.drew.edu> 1.20-1
- update to 1.20
- update BR's

* Wed Mar  5 2008 Tom "spot" Callaway <tcallawa@redhat.com> - 1.14-2
- rebuild for new perl

* Thu Jun  7 2007 Jose Pedro Oliveira <jpo at di.uminho.pt> - 1.14-1
- Update to 1.14.

* Fri Jul  7 2006 Jose Pedro Oliveira <jpo at di.uminho.pt> - 1.12-1
- Update to 1.12.

* Mon Jun 19 2006 Jose Pedro Oliveira <jpo at di.uminho.pt> - 1.10-1
- Update to 1.10.

* Thu Mar  2 2006 Jose Pedro Oliveira <jpo at di.uminho.pt> - 1.08-2
- Rebuild for FC5 (perl 5.8.8).

* Tue Nov 22 2005 Jose Pedro Oliveira <jpo at di.uminho.pt> - 1.08-1
- Update to 1.08.

* Thu Aug 11 2005 Jose Pedro Oliveira <jpo at di.uminho.pt> - 1.06-1
- Update to 1.06.

* Tue Mar 22 2005 Jose Pedro Oliveira <jpo at di.uminho.pt> - 1.04-1
- First build.
