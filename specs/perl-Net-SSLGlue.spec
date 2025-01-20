Name:           perl-Net-SSLGlue
Version:        1.058
Release:        26%{?dist}
Summary:        Add/extend SSL support for common perl modules
# Automatically converted from old format: GPL+ or Artistic - review is highly recommended.
License:        GPL-1.0-or-later OR Artistic-1.0-Perl

URL:            https://metacpan.org/release/Net-SSLGlue
Source0:        https://cpan.metacpan.org/authors/id/S/SU/SULLR/Net-SSLGlue-%{version}.tar.gz

# Remove interactive question
# Only minimal test which doesnt requires Internet connexion
Patch0:         perl-Net-SSLGlue-test.patch

BuildArch:      noarch
BuildRequires: make
BuildRequires:  perl-generators
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
BuildRequires:  perl(IO::Socket::SSL) >= 1.19
# Required to have tests effective
BuildRequires:  perl(LWP::Protocol::https)
BuildRequires:  perl(Net::LDAP)
BuildRequires:  perl(Net::SMTP)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)

Requires:       perl(LWP::UserAgent) >= 6.06
Requires:       perl(LWP::Protocol::https) >= 6.06
Requires:       perl(Net::FTP)
Requires:       perl(Net::FTP::dataconn)


%{?perl_default_filter}
%global __requires_exclude %{?__requires_exclude:%__requires_exclude|}^perl\\(IO::Socket::SSL\\)$
%global __requires_exclude %__requires_exclude|^perl\\(LWP::UserAgent\\)$


%description
Some commonly used perl modules don't have SSL support at all, even if the
protocol would support it. Others have SSL support, but most of them don't
do proper checking of the servers certificate.

The Net::SSLGlue::* modules try to add SSL support or proper certificate to
these modules. Currently is support for the following modules available:

- Net::SMTP - add SSL from beginning or using STARTTLS
- Net::LDAP - add proper certificate checking
- LWP - add proper certificate checking 


%prep
%setup -q -n Net-SSLGlue-%{version}
%patch -P0 -p0


%build
%{__perl} Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1
make %{?_smp_mflags}


%install
make pure_install DESTDIR=$RPM_BUILD_ROOT
%{_fixperms} $RPM_BUILD_ROOT/*


%check
make test


%files
%doc README Changes examples
%license COPYRIGHT
%{perl_vendorlib}/Net
%{_mandir}/man3/Net*


%changelog
* Sat Jan 18 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.058-26
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Tue Aug 06 2024 Miroslav Suchý <msuchy@redhat.com> - 1.058-25
- convert license to SPDX

* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.058-24
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.058-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.058-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.058-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.058-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.058-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed Jun 01 2022 Jitka Plesnikova <jplesnik@redhat.com> - 1.058-18
- Perl 5.36 rebuild

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.058-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.058-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri May 21 2021 Jitka Plesnikova <jplesnik@redhat.com> - 1.058-15
- Perl 5.34 rebuild

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.058-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.058-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jun 23 2020 Jitka Plesnikova <jplesnik@redhat.com> - 1.058-12
- Perl 5.32 rebuild

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.058-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.058-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri May 31 2019 Jitka Plesnikova <jplesnik@redhat.com> - 1.058-9
- Perl 5.30 rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.058-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.058-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Jun 29 2018 Jitka Plesnikova <jplesnik@redhat.com> - 1.058-6
- Perl 5.28 rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.058-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.058-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Mon Jun 05 2017 Jitka Plesnikova <jplesnik@redhat.com> - 1.058-3
- Perl 5.26 rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.058-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Sat Jun 18 2016 Emmanuel Seyman <emmanuel@seyman.fr> - 1.058-1
- Update to 1.058

* Mon May 16 2016 Jitka Plesnikova <jplesnik@redhat.com> - 1.057-2
- Perl 5.24 rebuild

* Tue Apr 05 2016 Emmanuel Seyman <emmanuel@seyman.fr> - 1.057-1
- Update to 1.057

* Mon Feb 29 2016 Emmanuel Seyman <emmanuel@seyman.fr> - 1.055-3
- Pass NO_PACKLIST to Makefile.PL
- Clean up spec file

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.055-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Oct 29 2015 Remi Collet <remi@fedoraproject.org> - 1.055-1
- update to 1.055

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.054-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Jun 06 2015 Jitka Plesnikova <jplesnik@redhat.com> - 1.054-2
- Perl 5.22 rebuild

* Tue Apr 28 2015 Jitka Plesnikova <jplesnik@redhat.com> - 1.054-1
- 1.054 bump; Update BRs/Rs

* Thu Aug 28 2014 Jitka Plesnikova <jplesnik@redhat.com> - 1.052-3
- Perl 5.20 rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.052-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Tue Jan 21 2014 Remi Collet <remi@fedoraproject.org> - 1.052-1
* Mon Aug  5 2013 Remi Collet <remi@fedoraproject.org> - 1.04-1
- update to 1.04

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.03-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Fri Aug 02 2013 Petr Pisar <ppisar@redhat.com> - 1.03-2
- Perl 5.18 rebuild

* Sat Jun 15 2013 Remi Collet <remi@fedoraproject.org> - 1.03-1
- update to 1.03

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.01-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.01-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sat Jun 16 2012 Petr Pisar <ppisar@redhat.com> - 1.01-2
- Perl 5.16 rebuild

* Tue Feb 21 2012 Remi Collet <remi@fedoraproject.org> - 1.01-1
- update to 1.01
- add Requires perl(LWP::Protocol::https)

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.8-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Sun Jul 31 2011 Remi Collet <Fedora@famillecollet.com> - 0.8-1
- update to 0.8

* Tue Jul 19 2011 Petr Sabata <contyk@redhat.com> - 0.7-2
- Perl mass rebuild

* Wed Jun 01 2011 Remi Collet <Fedora@famillecollet.com> - 0.7-1
- update to 0.7

* Tue May 10 2011 Remi Collet <Fedora@famillecollet.com> - 0.6-1
- update to 0.6 (doc fix only)

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Fri Feb 04 2011 Remi Collet <Fedora@famillecollet.com> - 0.5-1
- update to 0.5 (doc fix only)
- fix description

* Tue Dec 21 2010 Marcela Maslanova <mmaslano@redhat.com> - 0.4-2
- 661697 rebuild for fixing problems with vendorach/lib

* Sat Jun 19 2010 Remi Collet <Fedora@famillecollet.com> - 0.4-1
- update to 0.4
- add Changes and examples in docs

* Tue May 04 2010 Marcela Maslanova <mmaslano@redhat.com> - 0.2-2
- Mass rebuild with perl-5.12.0

* Sun Feb 21 2010 Remi Collet <Fedora@famillecollet.com> - 0.2-1
- Specfile autogenerated by cpanspec 1.78
- initial RPM + cleanups
- from review (#567107) perl_default_filter + DESTDIR

