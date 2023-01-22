Name:           perl-Net-GitHub
Summary:        Perl interface for github.com
Version:        1.05
Release:        2%{?dist}
License:        GPL+ or Artistic
Source0:        https://cpan.metacpan.org/authors/id/F/FA/FAYLAND/Net-GitHub-%{version}.tar.gz
URL:            https://metacpan.org/release/Net-GitHub
BuildArch:      noarch
# Build
BuildRequires:  make
BuildRequires:  perl-interpreter
BuildRequires:  perl-generators
BuildRequires:  perl(Config)
BuildRequires:  perl(CPAN)
BuildRequires:  perl(Cwd)
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
BuildRequires:  perl(ExtUtils::MM_Unix)
BuildRequires:  perl(Fcntl)
BuildRequires:  perl(File::Find)
BuildRequires:  perl(File::Path)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(strict)
BuildRequires:  perl(vars)
# Runtime
BuildRequires:  perl(Cache::LRU)
BuildRequires:  perl(Carp)
BuildRequires:  perl(HTTP::Request)
BuildRequires:  perl(HTTP::Request::Common)
BuildRequires:  perl(JSON::MaybeXS)
BuildRequires:  perl(LWP::UserAgent)
BuildRequires:  perl(LWP::Protocol::https)
BuildRequires:  perl(MIME::Base64)
BuildRequires:  perl(Moo)
BuildRequires:  perl(Moo::Role)
BuildRequires:  perl(Types::Standard)
BuildRequires:  perl(URI)
BuildRequires:  perl(URI::Escape)
BuildRequires:  perl(warnings)
# Tests only
BuildRequires:  perl(Test::More)
Requires:       perl(LWP::Protocol::https)
Obsoletes:      %{name}-tests <= 0.50

%{?perl_default_filter}

%description
GitHub (http://github.com) is a popular git host; this package is a Perl API
for working with GitHub users and repositories.

%prep
%setup -q -n Net-GitHub-%{version}

%build
perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1
make %{?_smp_mflags}

%install
make pure_install DESTDIR=%{buildroot}
%{_fixperms} %{buildroot}/*

%check
make test

%files
%doc Changes
%{perl_vendorlib}/*
%{_mandir}/man3/*.3*

%changelog
* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.05-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Tue Oct 04 2022 Jan Pazdziora <jpazdziora@redhat.com> - 1.05-1
- 2131644 - Rebase to upstream version 1.05.

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.03-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed Jun 01 2022 Jitka Plesnikova <jplesnik@redhat.com> - 1.03-2
- Perl 5.36 rebuild

* Fri Apr 22 2022 Jan Pazdziora <jpazdziora@redhat.com> - 1.03-1
- 2076017 - Rebase to upstream version 1.03.

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.02-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Sep 08 2021 Jan Pazdziora <jpazdziora@redhat.com> - 1.02-1
- 2002160 - Rebase to upstream version 1.02.

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.01-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Sun May 23 2021 Jitka Plesnikova <jplesnik@redhat.com> - 1.01-5
- Perl 5.34 rebuild

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.01-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.01-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jun 23 2020 Jitka Plesnikova <jplesnik@redhat.com> - 1.01-2
- Perl 5.32 rebuild

* Mon Apr 27 2020 Jan Pazdziora <jpazdziora@redhat.com> - 1.01-1
- 1826569 - Rebase to upstream version 1.01.

* Mon Mar 30 2020 Jan Pazdziora <jpazdziora@redhat.com> - 0.99-1
- 1814917 - Rebase to upstream version 0.99.

* Wed Mar 18 2020 Jan Pazdziora <jpazdziora@redhat.com> - 0.97-1
- 1814482 - Rebase to upstream version 0.97.

* Fri Mar 06 2020 Jan Pazdziora <jpazdziora@redhat.com> - 0.96-1
- 1810919 - Rebase to upstream version 0.96.

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.95-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.95-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri May 31 2019 Jitka Plesnikova <jplesnik@redhat.com> - 0.95-5
- Perl 5.30 rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.95-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.95-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Sat Jun 30 2018 Jitka Plesnikova <jplesnik@redhat.com> - 0.95-2
- Perl 5.28 rebuild

* Tue Apr 03 2018 Jan Pazdziora <jpazdziora@redhat.com> - 0.95-1
- 1562374 - Rebase to upstream version 0.95.

* Mon Feb 26 2018 Jan Pazdziora <jpazdziora@redhat.com> - 0.94-1
- 1548611 - Rebase to upstream version 0.94.

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.93-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Fri Jan 12 2018 Jan Pazdziora <jpazdziora@redhat.com> - 0.93-1
- 1531885 - Rebase to upstream version 0.93.

* Mon Dec 18 2017 Jan Pazdziora <jpazdziora@redhat.com> - 0.91-1
- 1524390 - Rebase to upstream version 0.91.

* Mon Sep 04 2017 Jan Pazdziora <jpazdziora@redhat.com> - 0.90-1
- 1484857 - Rebase to upstream version 0.90.

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.89-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Mon Jul 24 2017 Jan Pazdziora <jpazdziora@redhat.com> - 0.89-1
- 1473922 - Rebase to upstream version 0.89.

* Tue Jun 06 2017 Jitka Plesnikova <jplesnik@redhat.com> - 0.87-2
- Perl 5.26 rebuild

* Tue May 23 2017 Jan Pazdziora <jpazdziora@redhat.com> - 0.87-1
- 1454749 - Rebase to upstream version 0.87.

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.86-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Dec 05 2016 Jan Pazdziora <jpazdziora@redhat.com> - 0.86-1
- 1401295 - Rebase to upstream version 0.86.

* Thu Sep 01 2016 Jan Pazdziora <jpazdziora@redhat.com> - 0.85-1
- 1372321 - Rebase to upstream version 0.85.

* Mon May 16 2016 Jitka Plesnikova <jplesnik@redhat.com> - 0.83-3
- Perl 5.24 rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.83-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Mon Feb 01 2016 Petr Šabata <contyk@redhat.com> - 0.83-1
- 0.83 bump

* Tue Jan 12 2016 Petr Šabata <contyk@redhat.com> - 0.82-1
- 0.82 bump

* Mon Jan 04 2016 Petr Šabata <contyk@redhat.com> - 0.81-1
- 0.81 bump

* Mon Nov 02 2015 Jitka Plesnikova <jplesnik@redhat.com> - 0.80-1
- 0.80 bump

* Thu Oct 29 2015 Jitka Plesnikova <jplesnik@redhat.com> - 0.79-1
- 0.79 bump

* Thu Sep 24 2015 Petr Šabata <contyk@redhat.com> - 0.78-1
- 0.78 bump

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.77-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Mon Jun 08 2015 Jitka Plesnikova <jplesnik@redhat.com> - 0.77-2
- Perl 5.22 rebuild

* Mon Jun 08 2015 Petr Šabata <contyk@redhat.com> - 0.77-1
- 0.77 bump

* Thu Mar 26 2015 Petr Šabata <contyk@redhat.com> - 0.75-1
- 0.75 bump

* Wed Mar 18 2015 Petr Šabata <contyk@redhat.com> - 0.74-1
- 0.74 bump, fix a regression introduced in 0.73

* Fri Mar 06 2015 Petr Šabata <contyk@redhat.com> - 0.73-1
- 0.73 bump

* Tue Feb 10 2015 Petr Šabata <contyk@redhat.com> - 0.72-1
- 0.72 bump

* Tue Feb 03 2015 Petr Šabata <contyk@redhat.com> - 0.71-1
- 0.71 bump

* Thu Sep 18 2014 Petr Šabata <contyk@redhat.com> - 0.69-1
- 0.69 bump

* Wed Sep 10 2014 Petr Šabata <contyk@redhat.com> - 0.68-1
- 0.68 bump

* Mon Sep 01 2014 Jitka Plesnikova <jplesnik@redhat.com> - 0.66-2
- Perl 5.20 rebuild

* Fri Aug 01 2014 Petr Šabata <contyk@redhat.com> - 0.66-1
- 0.66 bump

* Mon Jun 30 2014 Petr Šabata <contyk@redhat.com> - 0.65-1
- 0.65 bump

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.63-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Mon Jun 02 2014 Petr Šabata <contyk@redhat.com> - 0.63-1
- 0.63 bump

* Mon May 26 2014 Petr Šabata <contyk@redhat.com> - 0.60-1
- 0.60 bump

* Tue Apr 01 2014 Petr Šabata <contyk@redhat.com> - 0.59-1
- 0.59 bump

* Fri Mar 28 2014 Petr Šabata <contyk@redhat.com> - 0.57-1
- 0.57, POD fixes

* Tue Feb 25 2014 Petr Šabata <contyk@redhat.com> - 0.56-1
- 0.56 bump

* Fri Jan 17 2014 Petr Šabata <contyk@redhat.com> - 0.55-1
- 0.55 bump, no code changes

* Wed Sep 25 2013 Petr Pisar <ppisar@redhat.com> - 0.54-1
- 0.54 bump

* Mon Sep 02 2013 Petr Šabata <contyk@redhat.com> - 0.53-1
- 0.53 bump

* Sun Aug 04 2013 Petr Pisar <ppisar@redhat.com> - 0.52-3
- Perl 5.18 rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.52-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Mar 28 2013 Petr Šabata <contyk@redhat.com> - 0.52-1
- 0.52 bugfix bump

* Thu Mar 14 2013 Petr Šabata <contyk@redhat.com> - 0.51-1
- 0.51 bump

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.50-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Thu Nov 29 2012 Petr Šabata <contyk@redhat.com> - 0.50-1
- 0.50 bump, dropping V2 support
- Drop the tests subpackage

* Mon Nov 26 2012 Petr Šabata <contyk@redhat.com> - 0.48-1
- 0.48 bump

* Wed Nov 07 2012 Petr Šabata <contyk@redhat.com> - 0.47-1
- 0.47 bump

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.46-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Mon Jun 25 2012 Petr Pisar <ppisar@redhat.com> - 0.46-2
- Perl 5.16 rebuild

* Fri May 11 2012 Petr Šabata <contyk@redhat.com> - 0.46-1
- 0.46 bump, authors' contacts updated

* Thu May 03 2012 Petr Šabata <contyk@redhat.com> - 0.45-1
- 0.45 bump

* Fri Apr 13 2012 Petr Šabata <contyk@redhat.com> - 0.44-1
- 0.44 bump
- Github is removing support of v1 and v2 API on May 1, 2012
  This version makes v3 the default

* Fri Mar 23 2012 Petr Šabata <contyk@redhat.com> - 0.42-1
- 0.42 bump
- Remove trailing newlines

* Thu Mar 22 2012 Petr Šabata <contyk@redhat.com> - 0.41-1
- 0.41 bump, switching to v3 API
- Remove command macros
- Upstream no longer ships examples

* Tue Jan 17 2012 Petr Šabata <contyk@redhat.com> - 0.30-1
- 0.30 bump
- Spec cleanup

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.28-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Thu Jul 21 2011 Petr Sabata <contyk@redhat.com> - 0.28-3
- Perl mass rebuild

* Wed Jul 20 2011 Petr Sabata <contyk@redhat.com> - 0.28-2
- Perl mass rebuild

* Fri Mar 18 2011 Iain Arnell <iarnell@gmail.com> 0.28-1
- update to latest upstream version
- add examples as doc

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.23-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Tue Dec 21 2010 Marcela Maslanova <mmaslano@redhat.com> - 0.23-2
- 661697 rebuild for fixing problems with vendorach/lib

* Sat Dec 18 2010 Iain Arnell <iarnell@gmail.com> 0.23-1
- update to latest upstream version
- clean up spec for modern rpmbuild

* Fri Jun  4 2010 Petr Pisar <ppisar@redhat.com> - 0.22-1
- 0.22 bump
- Update Source0 URL

* Tue May 04 2010 Marcela Maslanova <mmaslano@redhat.com> - 0.20-2
- Mass rebuild with perl-5.12.0

* Sun Mar 14 2010 Chris Weyl <cweyl@alumni.drew.edu> 0.20-1
- update by Fedora::App::MaintainerTools 0.006
- PERL_INSTALL_ROOT => DESTDIR
- updating to latest GA CPAN version (0.20)
- dropped old BR on perl(Test::Pod)
- added a new req on perl(Any::Moose) (version 0)
- added a new req on perl(Crypt::SSLeay) (version 0)
- added a new req on perl(HTML::TreeBuilder) (version 0)
- added a new req on perl(JSON::Any) (version 0)
- added a new req on perl(URI::Escape) (version 0)
- added a new req on perl(WWW::Mechanize::GZip) (version 0)

* Mon Dec  7 2009 Stepan Kasal <skasal@redhat.com> - 0.19-3
- rebuild against perl 5.10.1

* Tue Oct 13 2009 Chris Weyl <cweyl@alumni.drew.edu> 0.19-2
- add br on CPAN (M::I)

* Sat Sep 26 2009 Chris Weyl <cweyl@alumni.drew.edu> 0.19-1
- update filtering
- submission

* Sat Sep 26 2009 Chris Weyl <cweyl@alumni.drew.edu> 0.19-0
- initial RPM packaging
- generated with cpan2dist (CPANPLUS::Dist::RPM version 0.0.8)
