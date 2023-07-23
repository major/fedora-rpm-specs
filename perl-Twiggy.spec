# Do not check any files in docdir for requires
%global __requires_exclude_from ^%{_docdir}/.*$

Name:           perl-Twiggy
Version:        0.1026
Release:        9%{?dist}
Summary:        AnyEvent HTTP server for PSGI (like Thin)
License:        GPL+ or Artistic
URL:            https://metacpan.org/release/Twiggy
Source0:        https://cpan.metacpan.org/authors/id/M/MI/MIYAGAWA/Twiggy-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  perl-interpreter >= 1:5.8.1
BuildRequires:  /usr/bin/dos2unix
BuildRequires:  findutils
BuildRequires:  make

BuildRequires:  perl-interpreter
BuildRequires:  perl-generators
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
# requires and recommends from Makefile.PL
BuildRequires:  perl(AnyEvent)
BuildRequires:  perl(HTTP::Parser::XS)
BuildRequires:  perl(HTTP::Status)
BuildRequires:  perl(Plack) >= 0.99
BuildRequires:  perl(Try::Tiny)
# all runtime requires
BuildRequires:  perl(AnyEvent::Handle)
BuildRequires:  perl(AnyEvent::Socket)
BuildRequires:  perl(AnyEvent::Util)
BuildRequires:  perl(base)
BuildRequires:  perl(Carp)
BuildRequires:  perl(Errno)
BuildRequires:  perl(IO::Handle)
BuildRequires:  perl(Plack::HTTPParser)
BuildRequires:  perl(Plack::Runner)
BuildRequires:  perl(Plack::Util)
BuildRequires:  perl(Scalar::Util)
BuildRequires:  perl(Server::Starter)
BuildRequires:  perl(Socket)
BuildRequires:  perl(constant)
BuildRequires:  perl(parent)
BuildRequires:  perl(warnings)
# optinal runtime requires
BuildRequires:  perl(AnyEvent::AIO)
BuildRequires:  perl(IO::AIO)
# other required for tests
BuildRequires:  perl(AnyEvent::HTTP)
BuildRequires:  perl(blib)
BuildRequires:  perl(FindBin)
BuildRequires:  perl(HTTP::Request)
BuildRequires:  perl(HTTP::Request::Common)
BuildRequires:  perl(HTTP::Response)
BuildRequires:  perl(IO::Socket::INET)
BuildRequires:  perl(IO::Uncompress::Gunzip)
BuildRequires:  perl(LWP::UserAgent)
BuildRequires:  perl(Plack::App::File)
BuildRequires:  perl(Plack::Loader)
BuildRequires:  perl(Plack::Middleware::Deflater)
BuildRequires:  perl(Plack::Request)
BuildRequires:  perl(Plack::Test::Suite)
BuildRequires:  perl(POSIX)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Test::Pod)
BuildRequires:  perl(Test::Requires)
BuildRequires:  perl(Test::TCP)
BuildRequires:  perl(Time::HiRes)

# requires and recommends from Makefile.PL
Requires:       perl(HTTP::Parser::XS)
Requires:       perl(Plack) >= 0.99
# optional runtime requires
Requires:       perl(AnyEvent::AIO)
Requires:       perl(IO::AIO)

%description
Twiggy is a lightweight and fast HTTP server based on AnyEvent and can run any
PSGI applications.

%prep
%setup -q -n Twiggy-%{version}
chmod -x eg/chat-websocket/static/jquery.oembed.js
dos2unix eg/chat-websocket/static/jquery.oembed.js

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
make %{?_smp_mflags}

%install
make pure_install DESTDIR=$RPM_BUILD_ROOT

find $RPM_BUILD_ROOT -type f -name .packlist -delete

%{_fixperms} $RPM_BUILD_ROOT/*

%check
TEST_SLOW=1 make test 

%files
%license LICENSE
%doc Changes eg/
%{perl_vendorlib}/*
%{_bindir}/*
%{_mandir}/man3/*
%{_mandir}/man1/*

%changelog
* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.1026-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.1026-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.1026-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed Jun 01 2022 Jitka Plesnikova <jplesnik@redhat.com> - 0.1026-6
- Perl 5.36 rebuild

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.1026-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Tue Jul 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.1026-4
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Sun May 23 2021 Jitka Plesnikova <jplesnik@redhat.com> - 0.1026-3
- Perl 5.34 rebuild

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.1026-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Thu Jan 21 2021 Fedora Release Monitoring <release-monitoring@fedoraproject.org> - 0.1026-1
- Update to 0.1026 (#1918607)

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.1025-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Jun 25 2020 Jitka Plesnikova <jplesnik@redhat.com> - 0.1025-15
- Perl 5.32 rebuild

* Tue Mar 17 2020 Jitka Plesnikova <jplesnik@redhat.com> - 0.1025-14
- Add BR: perl(blib)

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.1025-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.1025-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri May 31 2019 Jitka Plesnikova <jplesnik@redhat.com> - 0.1025-11
- Perl 5.30 rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.1025-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.1025-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Sat Jun 30 2018 Jitka Plesnikova <jplesnik@redhat.com> - 0.1025-8
- Perl 5.28 rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.1025-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.1025-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Tue Jun 06 2017 Jitka Plesnikova <jplesnik@redhat.com> - 0.1025-5
- Perl 5.26 rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.1025-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Tue May 17 2016 Jitka Plesnikova <jplesnik@redhat.com> - 0.1025-3
- Perl 5.24 rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.1025-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Mon Jun 22 2015 Jitka Plesnikova <jplesnik@redhat.com> - 0.1025-1
- 0.1025 bump

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1024-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Mon Jun 08 2015 Jitka Plesnikova <jplesnik@redhat.com> - 0.1024-4
- Perl 5.22 rebuild

* Mon Sep 01 2014 Jitka Plesnikova <jplesnik@redhat.com> - 0.1024-3
- Perl 5.20 rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1024-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Wed Nov 13 2013 Robin Lee <cheeselee@fedoraproject.org> - 0.1024-1
- Update to 0.1024

* Fri Aug  9 2013 Robin Lee <cheeselee@fedoraproject.org> - 0.1023-1
- Update to 0.1023

* Mon Aug 05 2013 Petr Pisar <ppisar@redhat.com> - 0.1021-5
- Perl 5.18 rebuild

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1021-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Fri May  3 2013 Robin Lee <cheeselee@fedoraproject.org> - 0.1021-3
- Remove duplicated BR

* Fri May  3 2013 Robin Lee <cheeselee@fedoraproject.org> - 0.1021-2
- Revise BuildRequires and Requires
- Include the eg directory to %%doc

* Tue Apr 09 2013 Robin Lee <cheeselee@fedoraproject.org> 0.1021-1
- Specfile autogenerated by cpanspec 1.78.
