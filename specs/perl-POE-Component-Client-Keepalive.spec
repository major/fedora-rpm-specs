Name:           perl-POE-Component-Client-Keepalive
%global real_ver 0.272
# Keep four digits to stay above the unfortunate 0.0901,
# so that epoch need not be changed.
Version:        %{real_ver}0
Release:        32%{?dist}
Summary:        Manages and keeps alive client connections
# Automatically converted from old format: GPL+ or Artistic - review is highly recommended.
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/POE-Component-Client-Keepalive
Source0:        https://cpan.metacpan.org/authors/id/R/RC/RCAPUTO/POE-Component-Client-Keepalive-%{real_ver}.tar.gz
# Fix a race in t/10_resolver.t, bug #1136851, CPAN RT#98644
Patch0:         POE-Component-Client-Keepalive-0.272-Fix-a-race-in-t-10_resolver.t.patch
BuildArch:      noarch
# Build
BuildRequires: make
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(Config)
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
# Runtime
BuildRequires:  perl(bytes)
BuildRequires:  perl(Carp)
BuildRequires:  perl(constant)
BuildRequires:  perl(Errno)
BuildRequires:  perl(Net::IP::Minimal) >= 0.02
BuildRequires:  perl(POE) >= 1.311
BuildRequires:  perl(POE::Component::Resolver) >= 0.917
BuildRequires:  perl(POE::Component::Server::TCP)
# Unused BuildRequires:  perl(POE::Component::SSLify)
BuildRequires:  perl(POE::Wheel::ReadWrite)
BuildRequires:  perl(POE::Wheel::SocketFactory)
BuildRequires:  perl(Socket)
# Tests
BuildRequires:  perl(IO::Socket::INET)
BuildRequires:  perl(lib)
BuildRequires:  perl(Scalar::Util)
BuildRequires:  perl(Test::More) >= 0.94
Requires:       perl(Net::IP::Minimal) >= 0.02
Requires:       perl(POE) >= 1.311
Requires:       perl(POE::Component::Resolver) >= 0.917
# Satisfy automaticly generated requires that want this module >= 0.0901
# (So the package has this provide in two versions, oh well.)
Provides:       perl(POE::Component::Client::Keepalive) = %{version}

%{?perl_default_filter}
%global __requires_exclude %{?__requires_exclude:__requires_exclude|^}perl\\(Net::IP::Minimal\\)$
%global __requires_exclude %__requires_exclude|^perl\\(POE\\)$
%global __requires_exclude %__requires_exclude|^perl\\(POE::Component::Resolver\\)$

%description
POE::Component::Client::Keepalive creates and manages connections for other
components. It maintains a cache of kept-alive connections for quick reuse. It
is written specifically for clients that can benefit from kept-alive
connections, such as HTTP clients. Using it for one-shot connections would
probably be silly.

%prep
%setup -q -n POE-Component-Client-Keepalive-%{real_ver}
%patch -P0 -p1
chmod -c -x mylib/* t/*
for test in t/release-pod-syntax.t \
            t/release-pod-coverage.t \
            t/000-report-versions.t; do
    perl -MConfig -i -pe 's/#!perl/$Config{startperl}/' ${test}
done

%build
perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1
%{make_build}

%install
%{make_install}
%{_fixperms} %{buildroot}/*

%check
# I'm leaving all tests active for now, even though 09_timeout.t runs a test
# which is _supposed_ to timeout against google.com.  This may or may not
# work inside the buildsys; if it doesn't the cure should be as easy as nixing
# this one test.
unset RELEASE_TESTING
make test

%files
%license LICENSE
%doc CHANGES README
%{perl_vendorlib}/*
%{_mandir}/man3/*.3*

%changelog
* Sat Jan 18 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.2720-32
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Tue Aug 06 2024 Miroslav Suchý <msuchy@redhat.com> - 0.2720-31
- convert license to SPDX

* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.2720-30
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.2720-29
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.2720-28
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.2720-27
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.2720-26
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.2720-25
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed Jun 01 2022 Jitka Plesnikova <jplesnik@redhat.com> - 0.2720-24
- Perl 5.36 rebuild

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.2720-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.2720-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri May 21 2021 Jitka Plesnikova <jplesnik@redhat.com> - 0.2720-21
- Perl 5.34 rebuild

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.2720-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.2720-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jun 23 2020 Jitka Plesnikova <jplesnik@redhat.com> - 0.2720-18
- Perl 5.32 rebuild

* Thu Feb 06 2020 Petr Pisar <ppisar@redhat.com> - 0.2720-17
- Modernize a spec file

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.2720-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.2720-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri May 31 2019 Jitka Plesnikova <jplesnik@redhat.com> - 0.2720-14
- Perl 5.30 rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.2720-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.2720-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Jun 28 2018 Jitka Plesnikova <jplesnik@redhat.com> - 0.2720-11
- Perl 5.28 rebuild

* Fri Feb 09 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.2720-10
- Escape macros in %%changelog

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.2720-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.2720-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Mon Jun 05 2017 Jitka Plesnikova <jplesnik@redhat.com> - 0.2720-7
- Perl 5.26 rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.2720-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Sun May 15 2016 Jitka Plesnikova <jplesnik@redhat.com> - 0.2720-5
- Perl 5.24 rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.2720-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2720-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Jun 06 2015 Jitka Plesnikova <jplesnik@redhat.com> - 0.2720-2
- Perl 5.22 rebuild

* Mon Dec 08 2014 Petr Šabata <contyk@redhat.com> - 0.2720-1
- 0.272 bump

* Sun Sep 07 2014 Jitka Plesnikova <jplesnik@redhat.com> - 0.2710-11
- Perl 5.20 rebuild

* Fri Sep 05 2014 Petr Pisar <ppisar@redhat.com> - 0.2710-10
- Fix a race in t/10_resolver.t (bug #1136851)

* Fri Aug 29 2014 Jitka Plesnikova <jplesnik@redhat.com> - 0.2710-9
- Perl 5.20 rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2710-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2710-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Mon Jul 29 2013 Petr Pisar <ppisar@redhat.com> - 0.2710-6
- Perl 5.18 rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2710-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2710-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jun 15 2012 Petr Pisar <ppisar@redhat.com> - 0.2710-3
- Perl 5.16 rebuild

* Tue May 15 2012 Petr Šabata <contyk@redhat.com> - 0.2710-2
- Fix the Resolver runtime dependency

* Tue May 15 2012 Petr Šabata <contyk@redhat.com> - 0.2710-1
- 0.271 bump

* Tue Mar 27 2012 Petr Šabata <contyk@redhat.com> - 0.2690-1
- 0.269 bump
- Drop command macros

* Thu Jan 19 2012 Petr Šabata <contyk@redhat.com> - 0.2680-1
- 0.268 bump
- Spec cleanup

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2620-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Jul 19 2011 Petr Sabata <contyk@redhat.com> - 0.2620-4
- Perl mass rebuild

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2620-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Tue Dec 21 2010 Marcela Maslanova <mmaslano@redhat.com> - 0.2620-2
- 661697 rebuild for fixing problems with vendorach/lib

* Tue Jun  8 2010 Petr Pisar <ppisar@redhat.com> - 0.2620-1
- 0.262 bump
- Escape per-cent sign in spec changelog

* Thu May 06 2010 Marcela Maslanova <mmaslano@redhat.com> - 0.2600-5
- Mass rebuild with perl-5.12.0

* Mon Dec  7 2009 Stepan Kasal <skasal@redhat.com> - 0.2600-4
- rebuild against perl 5.10.1

* Wed Sep 30 2009 Stepan Kasal <skasal@redhat.com> 0.2600-3
- keep the version aligned to 0.xxxx to maintain upgrade path

* Tue Sep 29 2009 Chris Weyl <cweyl@alumni.drew.edu> 0.260-2
- fix provides version (for perl-POE-Component-Client-HTTP)

* Sun Sep 27 2009 Chris Weyl <cweyl@alumni.drew.edu> 0.260-1
- update filtering
- auto-update to 0.260 (by cpan-spec-update 0.01)
- added a new br on perl(Net::IP) (version 1.25)
- altered br on perl(POE) (0.31 => 1.007)
- altered br on perl(POE::Component::Client::DNS) (1.01 => 1.04)
- added a new req on perl(Net::IP) (version 1.25)
- added a new req on perl(POE) (version 1.007)
- added a new req on perl(POE::Component::Client::DNS) (version 1.04)

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2500-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Mon Jun 15 2009 Stepan Kasal <skasal@redhat.com> 0.2500-2
- add an explicite perl(POE::Component::Client::Keepalive) = 0.25, sigh

* Sat Jun 13 2009 Stepan Kasal <skasal@redhat.com> 0.2500-1
- work around the broken versioning

* Thu May 21 2009 Chris Weyl <cweyl@alumni.drew.edu> 0.25-1
- auto-update to 0.25 (by cpan-spec-update 0.01)
- altered br on perl(POE::Component::Client::DNS) (0 => 1.01)

* Thu Feb 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1000-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Tue Mar  4 2008 Tom "spot" Callaway <tcallawa@redhat.com> 0.1000-2
- rebuild for new perl

* Sun May 13 2007 Chris Weyl <cweyl@alumni.drew.edu> 0.1000-1
- update to 0.1000
- add t/ to %%doc
- perl splittage BR tweaks

* Tue Oct 03 2006 Chris Weyl <cweyl@alumni.drew.edu> 0.0901-1
- update to 0.0901
- minor spec tweaks

* Thu Aug 31 2006 Chris Weyl <cweyl@alumni.drew.edu> 0.0801-3
- bump for mass rebuild

* Tue Jul 25 2006 Chris Weyl <cweyl@alumni.drew.edu> 0.0801-2
- import, bump & build for devel

* Thu Jul 20 2006 Chris Weyl <cweyl@alumni.drew.edu> 0.0801-1
- bits snipped

* Fri Jul 14 2006 Chris Weyl <cweyl@alumni.drew.edu> 0.0801-0
- Initial spec file for F-E
