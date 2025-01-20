Name:           perl-Net-Twitter
Version:        4.01043
Release:        24%{?dist}
Summary:        Perl interface to the Twitter API
# Automatically converted from old format: GPL+ or Artistic - review is highly recommended.
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Net-Twitter
Source0:        https://cpan.metacpan.org/authors/id/M/MM/MMIMS/Net-Twitter-%{version}.tar.gz
BuildArch:      noarch
BuildRequires: make
BuildRequires:  perl-interpreter
BuildRequires:  perl-generators
BuildRequires:  perl(ExtUtils::MakeMaker) >= 7.12
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
# Run-time:
BuildRequires:  perl(Carp::Clan)
BuildRequires:  perl(Class::Load)
BuildRequires:  perl(Data::Visitor::Callback)
BuildRequires:  perl(DateTime)
BuildRequires:  perl(DateTime::Format::Strptime)
BuildRequires:  perl(Devel::StackTrace)
BuildRequires:  perl(Digest::SHA)
BuildRequires:  perl(Encode)
BuildRequires:  perl(HTML::Entities)
BuildRequires:  perl(HTTP::Request::Common)
BuildRequires:  perl(JSON)
BuildRequires:  perl(JSON::MaybeXS)
BuildRequires:  perl(List::Util)
# LWP::Protocol::https to support HTTPS protocol
# LWP::Protocol::https not used at tests
BuildRequires:  perl(Moose)
BuildRequires:  perl(Moose::Exporter)
BuildRequires:  perl(Moose::Meta::Method)
BuildRequires:  perl(Moose::Role)
BuildRequires:  perl(Moose::Util::TypeConstraints)
BuildRequires:  perl(MooseX::Role::Parameterized)
BuildRequires:  perl(namespace::autoclean)
BuildRequires:  perl(Net::Netrc)
BuildRequires:  perl(Net::OAuth)
BuildRequires:  perl(overload)
BuildRequires:  perl(Scalar::Util)
BuildRequires:  perl(Time::HiRes)
BuildRequires:  perl(Try::Tiny)
BuildRequires:  perl(URI)
BuildRequires:  perl(URI::Escape)
# Tests:
BuildRequires:  perl(base)
BuildRequires:  perl(blib)
BuildRequires:  perl(Carp)
BuildRequires:  perl(Encode)
BuildRequires:  perl(File::Find)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(File::Temp)
BuildRequires:  perl(HTTP::Response)
BuildRequires:  perl(lib)
BuildRequires:  perl(LWP::UserAgent) >= 5.819
BuildRequires:  perl(Net::OAuth::Message)
BuildRequires:  perl(Test::Fatal)
BuildRequires:  perl(Test::More) >= 0.88
BuildRequires:  perl(Test::Warn)
BuildRequires:  perl(utf8)
# Optional tests:
# Test::Pod::Coverage 1.04 not used
BuildRequires:  perl(Test::Deep)
# Test::Pod 1.41 not used
# Test::Spelling 0.11 not used
Requires:       perl(Moose::Meta::Method)
# LWP::Protocol::https to support HTTPS protocol
Requires:       perl(LWP::Protocol::https)
Requires:       perl(Net::Netrc)

%description
This module provides a Perl interface to the Twitter APIs. See
http://dev.twitter.com/doc for a full description of the Twitter APIs.

%prep
%setup -q -n Net-Twitter-%{version}

%build
perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1
make %{?_smp_mflags}

%install
make pure_install DESTDIR=$RPM_BUILD_ROOT
%{_fixperms} $RPM_BUILD_ROOT/*

%check
make test

%files
%doc Changes README
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
* Sat Jan 18 2025 Fedora Release Engineering <releng@fedoraproject.org> - 4.01043-24
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Tue Aug 06 2024 Miroslav Suchý <msuchy@redhat.com> - 4.01043-23
- convert license to SPDX

* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 4.01043-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 4.01043-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 4.01043-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 4.01043-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 4.01043-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 4.01043-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed Jun 01 2022 Jitka Plesnikova <jplesnik@redhat.com> - 4.01043-16
- Perl 5.36 rebuild

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 4.01043-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 4.01043-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Sun May 23 2021 Jitka Plesnikova <jplesnik@redhat.com> - 4.01043-13
- Perl 5.34 rebuild

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 4.01043-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 4.01043-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jun 23 2020 Jitka Plesnikova <jplesnik@redhat.com> - 4.01043-10
- Perl 5.32 rebuild

* Wed Mar 18 2020 Jitka Plesnikova <jplesnik@redhat.com> - 4.01043-9
- Add perl(blib) for tests

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 4.01043-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 4.01043-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri May 31 2019 Jitka Plesnikova <jplesnik@redhat.com> - 4.01043-6
- Perl 5.30 rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 4.01043-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 4.01043-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Jun 29 2018 Jitka Plesnikova <jplesnik@redhat.com> - 4.01043-3
- Perl 5.28 rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 4.01043-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jan 18 2018 Julian C. Dunn <jdunn@aquezada.com> - 4.01043-1
- Update to 4.01043 (bz#1535738)

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 4.01042-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Tue Jun 06 2017 Jitka Plesnikova <jplesnik@redhat.com> - 4.01042-2
- Perl 5.26 rebuild

* Fri Feb 17 2017 Jitka Plesnikova <jplesnik@redhat.com> - 4.01042-1
- 4.01042 bump

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 4.01041-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri Dec 09 2016 Jitka Plesnikova <jplesnik@redhat.com> - 4.01041-1
- 4.01041 bump

* Mon May 16 2016 Jitka Plesnikova <jplesnik@redhat.com> - 4.01020-2
- Perl 5.24 rebuild

* Fri May 06 2016 Julian C. Dunn <jdunn@aquezada.com> - 4.01020-1
- Upgrade to 4.01020 (bz#1323532)

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 4.01010-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Jun 25 2015 Petr Pisar <ppisar@redhat.com> - 4.01010-1
- 4.01010 bump

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.01008-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Mon Jun 08 2015 Jitka Plesnikova <jplesnik@redhat.com> - 4.01008-3
- Perl 5.22 rebuild

* Sat Feb 07 2015 Ralf Corsépius <corsepiu@fedoraproject.org> - 4.01008-2
- Rebuild w/ perl-generators-1.03 to get rid of bogus deps.

* Thu Jan 22 2015 Julian C. Dunn <jdunn@aquezada.com> - 4.01008-1
- Upgrade to 4.01008 (bz#1166391)

* Wed Sep 03 2014 Jitka Plesnikova <jplesnik@redhat.com> - 4.01005-2
- Perl 5.20 rebuild

* Mon Sep 01 2014 Julian C. Dunn <jdunn@aquezada.com> - 4.01005-1
- Upgrade to 4.01005 (bz#1130048)

* Mon Sep 01 2014 Jitka Plesnikova <jplesnik@redhat.com> - 4.01004-3
- Perl 5.20 rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.01004-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Mon Apr 14 2014 Julian C. Dunn <jdunn@aquezada.com> - 4.01004-1
- Upgrade to 4.01004 (bz#1087334)

* Sat Mar 15 2014 Julian C. Dunn <jdunn@aquezada.com> - 4.01003-1
- Upgrade to 4.01003 (bz#1076563)

* Sun Jan 19 2014 Julian C. Dunn <jdunn@aquezada.com> - 4.01002-1
- Upgrade to 4.01002 (bz#1055295)

* Thu Nov 21 2013 Julian C. Dunn <jdunn@aquezada.com> - 4.01000-1
- Upgrade to 4.01000 (bz#1032571)

* Thu Aug 22 2013 Julian C. Dunn <jdunn@aquezada.com> - 4.00007-1
- Upgrade to 4.00007 (bz#996455)

* Sun Aug 04 2013 Petr Pisar <ppisar@redhat.com> - 4.00006-3
- Perl 5.18 rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.00006-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Fri Jun 14 2013 Julian C. Dunn <jdunn@aquezada.com> - 4.00006-1
- Upgrade to 4.00006 (bz#914316)

* Wed Mar 13 2013 Julian C. Dunn <jdunn@aquezada.com> - 4.00004-1
- Upgrade to 4.00004 (bz#914316)

* Fri Mar 08 2013 Julian C. Dunn <jdunn@aquezada.com> - 4.00003-1
- Upgrade to 4.00003 (bz#914316)

* Sun Feb 24 2013 Julian C. Dunn <jdunn@aquezada.com> - 4.00002-1
- Upgrade to 4.00002 (bz#914316)

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> 
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Tue Oct 16 2012 Julian C. Dunn <jdunn@aquezada.com> - 3.18004-1
- Upgrade to 3.18004 (bz#866878)

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.18003-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Mon Jul 09 2012 Petr Pisar <ppisar@redhat.com> - 3.18003-2
- Perl 5.16 rebuild

* Mon Jul 02 2012 Julian C. Dunn <jdunn@aquezada.com> - 3.18003-1
- Upgrade to 3.18003

* Mon Jun 25 2012 Petr Pisar <ppisar@redhat.com> - 3.18002-2
- Perl 5.16 rebuild

* Wed Apr 25 2012 Julian C. Dunn <jdunn@aquezada.com> 3.18002-1
- Upgrade to 3.18002

* Tue Mar 27 2012 Julian C. Dunn <jdunn@aquezada.com> 3.18001-1
- Initial release.
