Name:           perl-Starlet
Version:        0.31
Release:        26%{?dist}
Summary:        Simple, high-performance PSGI/Plack HTTP server
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Starlet
Source0:        https://cpan.metacpan.org/authors/id/K/KA/KAZUHO/Starlet-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  %{__perl}
BuildRequires:  %{__make}
BuildRequires:  /usr/bin/start_server
BuildRequires:  perl-generators
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.59

BuildRequires:  perl(base)
BuildRequires:  perl(Carp)
BuildRequires:  perl(constant)
BuildRequires:  perl(Fcntl)
BuildRequires:  perl(File::Basename)
BuildRequires:  perl(File::Temp)
BuildRequires:  perl(HTTP::Date)
BuildRequires:  perl(HTTP::Status)
BuildRequires:  perl(IO::Socket::INET)
BuildRequires:  perl(List::Util)
BuildRequires:  perl(LWP::UserAgent) >= 5.8
BuildRequires:  perl(Net::EmptyPort)
BuildRequires:  perl(Parallel::Prefork) >= 0.17
BuildRequires:  perl(Plack) >= 0.992
BuildRequires:  perl(Plack::HTTPParser)
BuildRequires:  perl(Plack::Loader)
BuildRequires:  perl(Plack::TempBuffer)
BuildRequires:  perl(Plack::Test)
BuildRequires:  perl(Plack::Util)
BuildRequires:  perl(POSIX)
BuildRequires:  perl(Server::Starter) >= 0.06
BuildRequires:  perl(Socket)
BuildRequires:  perl(strict)
BuildRequires:  perl(Test::More) >= 0.88
BuildRequires:  perl(Test::TCP) >= 2.1
BuildRequires:  perl(Time::HiRes)
BuildRequires:  perl(Try::Tiny)
BuildRequires:  perl(warnings)

# Eliminate inc/*
BuildRequires:  perl(inc::Module::Install)
BuildRequires:  perl(Module::Install::ReadmeFromPod)


%description
Starlet is a standalone HTTP/1.0 server with support for keep-alive, prefork,
graceful shutdown, hot deploy, fast HTTP processing, and is suitable for
running HTTP application servers behind a reverse proxy.

%prep
%setup -q -n Starlet-%{version}
rm -r inc/
sed -i -e '/^inc\/.*$/d' MANIFEST

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1
%{make_build}

%install
%{make_install}
%{_fixperms} $RPM_BUILD_ROOT/*

%check
%{__make} test

%files
%doc Changes README
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
* Sat Jan 18 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.31-26
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.31-25
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.31-24
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.31-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.31-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.31-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Mon Nov 28 2022 Ralf Corsépius <corsepiu@fedoraproject.org> - 0.31-20
- Modernize spec.
- Convert license to SPDX.

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.31-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed Jun 01 2022 Jitka Plesnikova <jplesnik@redhat.com> - 0.31-18
- Perl 5.36 rebuild

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.31-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.31-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Sat May 22 2021 Jitka Plesnikova <jplesnik@redhat.com> - 0.31-15
- Perl 5.34 rebuild

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.31-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.31-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Jun 25 2020 Jitka Plesnikova <jplesnik@redhat.com> - 0.31-12
- Perl 5.32 rebuild

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.31-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.31-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri May 31 2019 Jitka Plesnikova <jplesnik@redhat.com> - 0.31-9
- Perl 5.30 rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.31-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.31-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Sat Jun 30 2018 Jitka Plesnikova <jplesnik@redhat.com> - 0.31-6
- Perl 5.28 rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.31-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.31-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Tue Jun 06 2017 Jitka Plesnikova <jplesnik@redhat.com> - 0.31-3
- Perl 5.26 rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.31-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Dec 12 2016 Ralf Corsépius <corsepiu@fedoraproject.org> - 0.31-1
- Update to 0.31.

* Tue Jun 14 2016 Ralf Corsépius <corsepiu@fedoraproject.org> - 0.30-1
- Update to 0.30.

* Tue May 17 2016 Jitka Plesnikova <jplesnik@redhat.com> - 0.29-2
- Perl 5.24 rebuild

* Fri Feb 26 2016 Ralf Corsépius <corsepiu@fedoraproject.org> - 0.29-1
- Update to 0.29.
- Expand BRs.

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.28-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Sun Jan 31 2016 Ralf Corsépius <corsepiu@fedoraproject.org> - 0.28-2
- Modernize spec.

* Wed Nov 18 2015 Ralf Corsépius <corsepiu@fedoraproject.org> - 0.28-1
- Upstream update.
- Update BRs.
- Eliminate inc/*

* Tue Oct 13 2015 Ralf Corsépius <corsepiu@fedoraproject.org> - 0.26-1
- Upstream update.

* Mon Jul 13 2015 Ralf Corsépius <corsepiu@fedoraproject.org> - 0.25-1
- Upstream update.
- Update deps.

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.24-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Mon Jun 08 2015 Jitka Plesnikova <jplesnik@redhat.com> - 0.24-4
- Perl 5.22 rebuild

* Mon Sep 01 2014 Jitka Plesnikova <jplesnik@redhat.com> - 0.24-3
- Perl 5.20 rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.24-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Tue May 27 2014 Ralf Corsépius <corsepiu@fedoraproject.org> - 0.24-1
- Upstream update.

* Thu Apr 24 2014 Ralf Corsépius <corsepiu@fedoraproject.org> - 0.23-1
- Upstream update.

* Mon Apr 14 2014 Ralf Corsépius <corsepiu@fedoraproject.org> - 0.22-1
- Upstream update.

* Wed Apr 09 2014 Ralf Corsépius <corsepiu@fedoraproject.org> - 0.21-2
- Add BR: perl(Plack::Test) (RHBZ#1085230).
- Minor spec file modernization.

* Thu Dec 26 2013 Ralf Corsépius <corsepiu@fedoraproject.org> - 0.21-1
- Upstream update.

* Wed Aug 28 2013 Ralf Corsépius <corsepiu@fedoraproject.org> - 0.20-1
- Upstream update.

* Mon Aug 05 2013 Petr Pisar <ppisar@redhat.com> - 0.19-3
- Perl 5.18 rebuild

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.19-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Mon Jul 08 2013 Ralf Corsépius <corsepiu@fedoraproject.org> - 0.19-1
- Upstream update.
- BR: perl(LWP::UserAgent).

* Thu Mar 21 2013 Ralf Corsépius <corsepiu@fedoraproject.org> - 0.18-1
- Upstream update.

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.16-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Mon Sep 17 2012 Ralf Corsépius <corsepiu@fedoraproject.org> - 0.16-1
- Upstream update.

* Tue Aug 14 2012 Ralf Corsépius <corsepiu@fedoraproject.org> - 0.15-1
- Upstream update.

* Sat Nov 26 2011 Ralf Corsépius <corsepiu@fedoraproject.org> 0.14-1
- Spec file cleanup.
- Abandon fedora < 15.
- Upstream update.

* Tue Jul 19 2011 Petr Sabata <contyk@redhat.com> - 0.13-3
- Perl mass rebuild

* Sun Feb 27 2011 Ralf Corsépius <corsepiu@fedoraproject.org> 0.13-2
- Add Requires: Fedora < 15's rpm misses.
- Add package reviewer's package description.
- Cosmetic spec cleanups.

* Wed Dec 22 2010 Ralf Corsépius <corsepiu@fedoraproject.org> 0.13-1
- Initial Fedora package.
