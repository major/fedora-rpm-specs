Name:           Perlbal
Version:        1.80
Release:        61%{?dist}
Summary:        Reverse-proxy load balance and web-server
# Automatically converted from old format: GPL+ or Artistic - review is highly recommended.
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Perlbal
Source0:        http://www.laqee.unal.edu.co/CPAN/authors/id/D/DO/DORMANDO/Perlbal-1.80.tar.gz
Source1:        perlbal.service
BuildArch:      noarch

BuildRequires:  coreutils
BuildRequires:  findutils
BuildRequires:  make
BuildRequires:  perl-interpreter
BuildRequires:  perl-generators
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  systemd
# Run-time:
BuildRequires:  perl(base)
BuildRequires:  perl(Carp)
BuildRequires:  perl(constant)
BuildRequires:  perl(Danga::Socket) >= 1.59
BuildRequires:  perl(Digest::MD5)
BuildRequires:  perl(Errno)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(Fcntl)
BuildRequires:  perl(fields)
BuildRequires:  perl(File::Path)
BuildRequires:  perl(File::Temp)
BuildRequires:  perl(Getopt::Long)
BuildRequires:  perl(HTTP::Date)
BuildRequires:  perl(HTTP::Request)
BuildRequires:  perl(HTTP::Response)
BuildRequires:  perl(IO::File)
BuildRequires:  perl(IO::Handle)
BuildRequires:  perl(IO::Select)
BuildRequires:  perl(IO::Socket)
BuildRequires:  perl(IO::Socket::INET)
# IO::Socket::SSL 0.98 not used at tests
# lib not used at tests
BuildRequires:  perl(List::Util)
BuildRequires:  perl(LWP::UserAgent)
# Net::CIDR::Lite not used at tests
BuildRequires:  perl(POSIX)
BuildRequires:  perl(Scalar::Util)
BuildRequires:  perl(Socket)
BuildRequires:  perl(strict)
# Symbol not used at tests
BuildRequires:  perl(Sys::Syscall)
BuildRequires:  perl(Time::HiRes)
# URI not used at tests
# URI::QueryParam not used at tests
BuildRequires:  perl(vars)
BuildRequires:  perl(warnings)
# Optional run-time:
# Cache::Memcached::Async not used at tests
BuildRequires:  perl(BSD::Resource)
BuildRequires:  perl(IO::AIO) >= 1.6
# IO::Socket::INET6 not used at tests
BuildRequires:  perl(Net::Netmask)
%if !%{defined perl_bootstrap}
BuildRequires:  perl(Perlbal::XS::HTTPHeaders) >= 0.20
%endif
BuildRequires:  perl(Sys::Syslog)
# Tests:
BuildRequires:  perl(FindBin)
BuildRequires:  perl(Hash::Util)
BuildRequires:  perl(lib)
BuildRequires:  perl(Test::More) >= 0.94
# Optional tests:
BuildRequires:  perl(Benchmark)

Requires:       perl(File::Temp)
Requires:       perl(IO::Select)
Requires:       perl(LWP::UserAgent)
Requires:       perl(Net::CIDR::Lite)
# Optional run-time:
Requires:       perl(BSD::Resource)
Requires:       perl(IO::AIO) >= 1.6
%if !%{defined perl_bootstrap}
Requires:       perl(Perlbal::XS::HTTPHeaders) >= 0.20
%endif

Requires(post):     systemd
Requires(preun):    systemd
Requires(postun):   systemd


%description
Perlbal is a single-threaded event-based server supporting HTTP load 
balancing, web serving, and a mix of the two. Perlbal can act as either a web 
server or a reverse proxy. 

One of the defining things about Perlbal is that almost everything can be 
configured or reconfigured on the fly without needing to restart the software. 
A basic configuration file containing a management port enables you to easily 
perform operations on a running instance of Perlbal. 

Perlbal can also be extended by means of per-service (and global) plugins that 
can override many parts of request handling and behavior.

%prep
%setup -q

%build
perl Makefile.PL INSTALLDIRS=vendor
make %{?_smp_mflags}

%install
make pure_install PERL_INSTALL_ROOT=%{buildroot}

find %{buildroot} -type f -name .packlist -exec rm -f {} \;
find %{buildroot} -depth -type d -exec rmdir {} 2>/dev/null \;

%{_fixperms} %{buildroot}/*

install -D -p -m 0644 conf/webserver.conf %{buildroot}%{_sysconfdir}/perlbal/perlbal.conf
install -D -p -m 0755 %{SOURCE1} %{buildroot}%{_unitdir}/perlbal.service
mkdir -p doc/examples
mv conf/* doc/examples

%check
make test

%post
%systemd_post perlbal.service

%preun
%systemd_preun perlbal.service

%postun
%systemd_postun_with_restart perlbal.service

%files
%dir %{_sysconfdir}/perlbal
%config(noreplace) %{_sysconfdir}/perlbal/perlbal.conf
%{_unitdir}/perlbal.service
%doc CHANGES README doc/*
%{perl_vendorlib}/*
%{_bindir}/perlbal
%{_mandir}/man1/*
%{_mandir}/man3/*


%changelog
* Thu Jan 16 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.80-61
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Mon Aug 05 2024 Miroslav Suchý <msuchy@redhat.com> - 1.80-60
- convert license to SPDX

* Wed Jul 17 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.80-59
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Wed Jun 12 2024 Jitka Plesnikova <jplesnik@redhat.com> - 1.80-58
- Perl 5.40 re-rebuild of bootstrapped packages

* Mon Jun 10 2024 Jitka Plesnikova <jplesnik@redhat.com> - 1.80-57
- Perl 5.40 rebuild

* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.80-56
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.80-55
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.80-54
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Wed Jul 12 2023 Jitka Plesnikova <jplesnik@redhat.com> - 1.80-53
- Perl 5.38 re-rebuild of bootstrapped packages

* Tue Jul 11 2023 Jitka Plesnikova <jplesnik@redhat.com> - 1.80-52
- Perl 5.38 rebuild

* Wed Jan 18 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.80-51
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Wed Jul 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.80-50
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Fri Jun 03 2022 Jitka Plesnikova <jplesnik@redhat.com> - 1.80-49
- Perl 5.36 re-rebuild of bootstrapped packages

* Wed Jun 01 2022 Jitka Plesnikova <jplesnik@redhat.com> - 1.80-48
- Perl 5.36 rebuild

* Wed Jan 19 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.80-47
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.80-46
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Mon May 24 2021 Jitka Plesnikova <jplesnik@redhat.com> - 1.80-45
- Perl 5.34 re-rebuild of bootstrapped packages

* Fri May 21 2021 Jitka Plesnikova <jplesnik@redhat.com> - 1.80-44
- Perl 5.34 rebuild

* Tue Mar 02 2021 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 1.80-43
- Rebuilt for updated systemd-rpm-macros
  See https://pagure.io/fesco/issue/2583.

* Mon Jan 25 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.80-42
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.80-41
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Jun 26 2020 Jitka Plesnikova <jplesnik@redhat.com> - 1.80-40
- Perl 5.32 re-rebuild of bootstrapped packages

* Tue Jun 23 2020 Jitka Plesnikova <jplesnik@redhat.com> - 1.80-39
- Perl 5.32 rebuild

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.80-38
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.80-37
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Jun 02 2019 Jitka Plesnikova <jplesnik@redhat.com> - 1.80-36
- Perl 5.30 re-rebuild of bootstrapped packages

* Fri May 31 2019 Jitka Plesnikova <jplesnik@redhat.com> - 1.80-35
- Perl 5.30 rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.80-34
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.80-33
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Sun Jul 01 2018 Jitka Plesnikova <jplesnik@redhat.com> - 1.80-32
- Perl 5.28 re-rebuild of bootstrapped packages

* Thu Jun 28 2018 Jitka Plesnikova <jplesnik@redhat.com> - 1.80-31
- Perl 5.28 rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.80-30
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.80-29
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Wed Jun 07 2017 Jitka Plesnikova <jplesnik@redhat.com> - 1.80-28
- Perl 5.26 re-rebuild of bootstrapped packages

* Mon Jun 05 2017 Jitka Plesnikova <jplesnik@redhat.com> - 1.80-27
- Perl 5.26 rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.80-26
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Nov 10 2016 Petr Pisar <ppisar@redhat.com> - 1.80-25
- Finish bootstrap on PowerPC

* Thu Nov 10 2016 Petr Pisar <ppisar@redhat.com> - 1.80-24
- Bootstrap on PowerPC

* Mon Sep 12 2016 Petr Pisar <ppisar@redhat.com> - 1.80-23
- Finish bootstrap on aarch64

* Mon Sep 12 2016 Petr Pisar <ppisar@redhat.com> - 1.80-22
- Bootstrap on aarch64

* Wed May 18 2016 Jitka Plesnikova <jplesnik@redhat.com> - 1.80-21
- Perl 5.24 re-rebuild of bootstrapped packages

* Mon May 16 2016 Jitka Plesnikova <jplesnik@redhat.com> - 1.80-20
- Perl 5.24 rebuild

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.80-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Oct 30 2015 Petr Pisar <ppisar@redhat.com> - 1.80-18
- Migrate from System V init script to systemd
- Specify all dependencies

* Tue Jun 16 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.80-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Wed Jun 10 2015 Jitka Plesnikova <jplesnik@redhat.com> - 1.80-16
- Perl 5.22 re-rebuild of bootstrapped packages

* Sat Jun 06 2015 Jitka Plesnikova <jplesnik@redhat.com> - 1.80-15
- Perl 5.22 rebuild

* Sun Sep 07 2014 Jitka Plesnikova <jplesnik@redhat.com> - 1.80-14
- Perl 5.20 re-rebuild of bootstrapped packages

* Thu Aug 28 2014 Jitka Plesnikova <jplesnik@redhat.com> - 1.80-13
- Perl 5.20 rebuild

* Fri Jun 06 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.80-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Thu Feb 27 2014 Luis Bazan <lbazan@fedoraproject.org> - 1.80-11
- remove buildrequire

* Thu Feb 27 2014 Luis Bazan <lbazan@fedoraproject.org> - 1.80-10
- fix BZ#1068711

* Wed Aug 14 2013 Jitka Plesnikova <jplesnik@redhat.com> - 1.80-9
- Perl 5.18 re-rebuild of bootstrapped packages

* Fri Aug 02 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.80-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Jul 24 2013 Petr Pisar <ppisar@redhat.com> - 1.80-7
- Perl 5.18 rebuild

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.80-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Wed Aug 01 2012 Luis Bazan <lbazan@fedoraproject.org> - 1.80-5
- Add readme to docs

* Wed Jul 18 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.80-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Tue Jul 10 2012 Petr Pisar <ppisar@redhat.com> - 1.80-3
- Perl 5.16 re-rebuild of bootstrapped packages

* Thu Jun 28 2012 Petr Pisar <ppisar@redhat.com> - 1.80-2
- Perl 5.16 rebuild

* Fri Jun 22 2012 Luis Bazan <lbazan@fedoraproject.org> - 1.80-1
- New upstream Version

* Fri Jun 15 2012 Petr Pisar <ppisar@redhat.com> - 1.79-6
- Perl 5.16 rebuild

* Thu Jan 12 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.79-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Wed Jul 27 2011 Petr Pisar <ppisar@redhat.com> - 1.79-4
- Disable 5.14 perl_bootstrap

* Tue Jul 26 2011 Petr Pisar <ppisar@redhat.com> - 1.79-3
- Disable XS implementation to bootstrap

* Thu Jul 21 2011 Petr Sabata <contyk@redhat.com> - 1.79-2
- Perl mass rebuild

* Wed Jul 13 2011 Luis Bazan <bazanluis20@gmail.com> 1.79-1
- Upstream released new version: http://cpansearch.perl.org/src/DORMANDO/Perlbal-1.79/CHANGES

* Wed Feb 09 2011 Ruben Kerkhof <ruben@rubenkerkhof.com> 1.78-1
- Upstream released new version:
  http://cpansearch.perl.org/src/DORMANDO/Perlbal-1.78/CHANGES

* Mon Feb 07 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.76-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Tue Jun 22 2010 Ruben Kerkhof <ruben@rubenkerkhof.com> 1.76-1
- Upstream released new version: http://cpansearch.perl.org/src/DORMANDO/Perlbal-1.76/CHANGES
- Minor spec and initscript cleanup

* Tue Jun 01 2010 Marcela Maslanova <mmaslano@redhat.com> - 1.75-2
- Mass rebuild with perl-5.12.0

* Tue Apr 06 2010 Ruben Kerkhof <ruben@rubenkerkhof.com> 1.75-1
- Upstream released new version

* Mon Dec  7 2009 Stepan Kasal <skasal@redhat.com> - 1.70-5
- rebuild against perl 5.10.1

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.70-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Mon Feb 23 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.70-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Sun Oct 19 2008 Ruben Kerkhof <ruben@rubenkerkhof.com> 1.70-2
- Use Perlbal::XS::HTTPHeaders to speed up header parsing

* Sun Mar 09 2008 Tom "spot" Callaway <tcallawa@redhat.com> 1.70-1
- 1.70 (fixes build for perl 5.10.0)

* Thu Feb 07 2008 Tom "spot" Callaway <tcallawa@redhat.com> 1.60-2
- don't need patch, merged with 1.60

* Thu Feb 07 2008 Tom "spot" Callaway <tcallawa@redhat.com> 1.60-1
- 1.60

* Thu Feb 07 2008 Tom "spot" Callaway <tcallawa@redhat.com> 1.59-2
- rebuild for new perl

* Wed Jun 20 2007 Ruben Kerkhof <ruben@rubenkerkhof.com> 1.59-1
- Upstream released new version
- Received patch from upstream for failing buffered upload test (240693)
* Sat May 12 2007 Ruben Kerkhof <ruben@rubenkerkhof.com> 1.58-1
- Initial import

