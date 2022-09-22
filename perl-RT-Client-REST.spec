Name:       perl-RT-Client-REST 
Version:    0.60
Release:    9%{?dist}
License:    GPL+ or Artistic
Summary:    Talk to RT using REST protocol 
Url:        https://metacpan.org/release/RT-Client-REST
Source:     https://cpan.metacpan.org/authors/id/D/DJ/DJZORT/RT-Client-REST-%{version}.tar.gz
BuildArch:  noarch
BuildRequires:  make
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(:VERSION) >= 5.4
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
# Run-time
BuildRequires:  perl(base)
BuildRequires:  perl(constant)
BuildRequires:  perl(DateTime)
BuildRequires:  perl(DateTime::Format::DateParse)
BuildRequires:  perl(Error)
BuildRequires:  perl(Exception::Class)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(HTTP::Cookies)
BuildRequires:  perl(HTTP::Request::Common)
BuildRequires:  perl(LWP::UserAgent)
BuildRequires:  perl(Params::Validate)
BuildRequires:  perl(vars)
# Tests
BuildRequires:  perl(blib)
BuildRequires:  perl(Data::Dumper)
BuildRequires:  perl(Encode)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(File::Spec::Functions)
BuildRequires:  perl(File::Temp)
BuildRequires:  perl(HTTP::Response)
BuildRequires:  perl(HTTP::Server::Simple) >= 0.44
BuildRequires:  perl(HTTP::Server::Simple::CGI)
BuildRequires:  perl(IO::File)
BuildRequires:  perl(IO::Handle)
BuildRequires:  perl(IO::Pipe)
BuildRequires:  perl(IO::Socket)
BuildRequires:  perl(IPC::Open3)
# Pod::Coverage::TrustPod not used
# Pod::Wordlist not used
BuildRequires:  perl(Socket)
# Test::CPAN::Meta not used
# Test::EOF not used
# Test::EOL not used
BuildRequires:  perl(Test::Exception)
# Test::Legal not used
# Test::NoBreakpoints 0.15 not used
# Test::NoTabs not used
# Test::Kwalitee::Extra not used
BuildRequires:  perl(Test::More)
# Test::Perl::Critic not used
# Test::PAUSE::Permissions not used
# Test::Pod 1.41 not used
# Test::Pod::Coverage 1.08 not used
# Test::Pod::No404s not used
# Test::Portability::Files not used
# Test::Spelling 0.12 not used
# Test::Vars not used
# Optional tests:
# CPAN::Meta not helpful
# CPAN::Meta::Prereqs not helpful
Requires:       perl(:MODULE_COMPAT_%(eval "`perl -V:version`"; echo $version))

%description
RT::Client::REST is a set of object-oriented Perl modules designed to make
communicating with RT using REST protocol easy. Most of the features have been
implemented and tested with rt 3.6.0 and later.

%prep
%setup -q -n RT-Client-REST-%{version}

%build
perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1
%{make_build}

%install
%{make_install}
%{_fixperms} %{buildroot}/*

%check
unset AUTHOR_TESTING RELEASE_TESTING
make test

%files
%license LICENSE
%doc CHANGES CONTRIBUTORS examples README TODO
%{perl_vendorlib}/*
%{_mandir}/man3/*.3*

%changelog
* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.60-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed Jun 01 2022 Jitka Plesnikova <jplesnik@redhat.com> - 0.60-8
- Perl 5.36 rebuild

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.60-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.60-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Sun May 23 2021 Jitka Plesnikova <jplesnik@redhat.com> - 0.60-5
- Perl 5.34 rebuild

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.60-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.60-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jun 23 2020 Jitka Plesnikova <jplesnik@redhat.com> - 0.60-2
- Perl 5.32 rebuild

* Thu May 07 2020 Petr Pisar <ppisar@redhat.com> - 0.60-1
- 0.60 bump

* Tue May 05 2020 Petr Pisar <ppisar@redhat.com> - 0.59-1
- 0.59 bump

* Fri May 01 2020 Petr Pisar <ppisar@redhat.com> - 0.58-1
- 0.58 bump

* Wed Apr 29 2020 Petr Pisar <ppisar@redhat.com> - 0.57-1
- 0.57 bump

* Tue Mar 17 2020 Jitka Plesnikova <jplesnik@redhat.com> - 0.56-6
- Add perl(blib) for tests

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.56-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.56-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri May 31 2019 Jitka Plesnikova <jplesnik@redhat.com> - 0.56-3
- Perl 5.30 rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.56-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Jan 03 2019 Petr Pisar <ppisar@redhat.com> - 0.56-1
- 0.56 bump

* Tue Dec 11 2018 Petr Pisar <ppisar@redhat.com> - 0.55-1
- 0.55 bump

* Mon Nov 12 2018 Petr Pisar <ppisar@redhat.com> - 0.54-1
- 0.54 bump

* Tue Nov 06 2018 Petr Pisar <ppisar@redhat.com> - 0.53-1
- 0.53 bump

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.52-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Jun 29 2018 Jitka Plesnikova <jplesnik@redhat.com> - 0.52-2
- Perl 5.28 rebuild

* Mon Apr 09 2018 Petr Pisar <ppisar@redhat.com> - 0.52-1
- 0.52 bump

* Wed Feb 28 2018 Petr Pisar <ppisar@redhat.com> - 0.51-1
- 0.51 bump

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.50-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.50-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Tue Jun 06 2017 Jitka Plesnikova <jplesnik@redhat.com> - 0.50-5
- Perl 5.26 rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.50-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon May 16 2016 Jitka Plesnikova <jplesnik@redhat.com> - 0.50-3
- Perl 5.24 rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.50-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Mon Dec 14 2015 Petr Pisar <ppisar@redhat.com> - 0.50-1
- 0.50 bump

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.49-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Jun 06 2015 Jitka Plesnikova <jplesnik@redhat.com> - 0.49-4
- Perl 5.22 rebuild

* Fri Aug 29 2014 Jitka Plesnikova <jplesnik@redhat.com> - 0.49-3
- Perl 5.20 rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.49-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Mon May 26 2014 Petr Pisar <ppisar@redhat.com> - 0.49-1
- 0.49 bump
- License changed from (GPLv2) to (GPL+ or Artistic)

* Fri May 02 2014 Petr Pisar <ppisar@redhat.com> - 0.48-1
- 0.48 bump

* Mon Apr 28 2014 Petr Pisar <ppisar@redhat.com> - 0.46-1
- 0.46 bump

* Mon Nov 18 2013 Petr Pisar <ppisar@redhat.com> - 0.45-1
- 0.45 bump

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.43-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Fri Aug 02 2013 Petr Pisar <ppisar@redhat.com> - 0.43-6
- Perl 5.18 rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.43-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.43-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sat Jun 23 2012 Petr Pisar <ppisar@redhat.com> - 0.43-3
- Perl 5.16 rebuild

* Mon Feb 06 2012 Petr Pisar <ppisar@redhat.com> - 0.43-2
- Enable Test::Kwalitee tests (bug #786849)

* Thu Feb 02 2012 Petr Pisar <ppisar@redhat.com> - 0.43-1
- 0.43 bump
- Disable bogus Test::Kwalitee tests (bug #786849)

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.37-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Thu Jul 21 2011 Petr Sabata <contyk@redhat.com> - 0.37-8
- Perl mass rebuild

* Thu Jul 21 2011 Petr Sabata <contyk@redhat.com> - 0.37-7
- Perl mass rebuild

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.37-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Tue Dec 21 2010 Marcela Maslanova <mmaslano@redhat.com> - 0.37-5
- 661697 rebuild for fixing problems with vendorach/lib

* Thu May 06 2010 Marcela Maslanova <mmaslano@redhat.com> - 0.37-4
- Mass rebuild with perl-5.12.0

* Mon Dec  7 2009 Stepan Kasal <skasal@redhat.com> - 0.37-3
- rebuild against perl 5.10.1

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.37-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Mon Apr 20 2009 Chris Weyl <cweyl@alumni.drew.edu> 0.37-1
- submission

* Sat Apr 18 2009 Chris Weyl <cweyl@alumni.drew.edu> 0.37-0
- initial RPM packaging
- generated with cpan2dist (CPANPLUS::Dist::RPM version 0.0.8)

