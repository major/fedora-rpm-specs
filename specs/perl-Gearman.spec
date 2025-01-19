Name:           perl-Gearman
Version:        2.004.015
Release:        24%{?dist}
Summary:        Perl interface for Gearman distributed job system
# Automatically converted from old format: GPL+ or Artistic - review is highly recommended.
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            http://danga.com/gearman/
Source0:        https://cpan.metacpan.org/authors/id/P/PA/PALIK/Gearman-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  make
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
# Run-time:
BuildRequires:  perl(base)
BuildRequires:  perl(Carp)
BuildRequires:  perl(constant)
BuildRequires:  perl(fields)
BuildRequires:  perl(IO::Select)
BuildRequires:  perl(IO::Socket::IP)
BuildRequires:  perl(IO::Socket::SSL)
BuildRequires:  perl(List::MoreUtils)
BuildRequires:  perl(POSIX)
BuildRequires:  perl(Scalar::Util)
BuildRequires:  perl(Socket)
BuildRequires:  perl(Storable)
BuildRequires:  perl(String::CRC32)
BuildRequires:  perl(Time::HiRes)
BuildRequires:  perl(version) >= 0.77
# Tests:
BuildRequires:  perl(Exporter)
BuildRequires:  perl(File::Which)
BuildRequires:  perl(lib)
BuildRequires:  perl(List::Util)
BuildRequires:  perl(Net::EmptyPort)
BuildRequires:  perl(Perl::OSType)
BuildRequires:  perl(Proc::Guard)
BuildRequires:  perl(Test::Exception)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Test::TCP)
BuildRequires:  perl(Test::Timer)
BuildRequires:  perl(vars)
# Optional tests:
%if !%{defined perl_bootstrap}
# Break build cycle: perl-Gearman → perl-Gearman-Server → perl-Gearman
# perl-Gearman-Server for %%{_bindir}/gearmand
BuildRequires:  perl-Gearman-Server
%endif
# Devel::Gladiator not yet packaged
Requires:       perl(version) >= 0.77

# Remove under-specifed dependencies
%global __requires_exclude %{?__requires_exclude:%{__requires_exclude}|}^perl\\(version\\)$

%description
Gearman provides a generic application framework to farm out work to other
machines or processes that are better suited to do the work. It allows you
to do work in parallel, to load balance processing, and to call functions
between languages. 

%prep
%setup -q -n Gearman-%{version}

%build
perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1
make %{?_smp_mflags}

%install
make pure_install DESTDIR=$RPM_BUILD_ROOT
%{_fixperms} $RPM_BUILD_ROOT/*

%check
unset AUTHOR_TESTING
make test

%files
%doc CHANGES README TODO
%{perl_vendorlib}/Gearman
%{_mandir}/man3/Gearman::*.*

%changelog
* Sat Jan 18 2025 Fedora Release Engineering <releng@fedoraproject.org> - 2.004.015-24
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Tue Aug 06 2024 Miroslav Suchý <msuchy@redhat.com> - 2.004.015-23
- convert license to SPDX

* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.004.015-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.004.015-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.004.015-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.004.015-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.004.015-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.004.015-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Fri Jun 03 2022 Jitka Plesnikova <jplesnik@redhat.com> - 2.004.015-16
- Perl 5.36 re-rebuild of bootstrapped packages

* Wed Jun 01 2022 Jitka Plesnikova <jplesnik@redhat.com> - 2.004.015-15
- Perl 5.36 rebuild

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.004.015-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.004.015-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Mon May 24 2021 Jitka Plesnikova <jplesnik@redhat.com> - 2.004.015-12
- Perl 5.34 re-rebuild of bootstrapped packages

* Fri May 21 2021 Jitka Plesnikova <jplesnik@redhat.com> - 2.004.015-11
- Perl 5.34 rebuild

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.004.015-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.004.015-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Jun 26 2020 Jitka Plesnikova <jplesnik@redhat.com> - 2.004.015-8
- Perl 5.32 re-rebuild of bootstrapped packages

* Tue Jun 23 2020 Jitka Plesnikova <jplesnik@redhat.com> - 2.004.015-7
- Perl 5.32 rebuild

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.004.015-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.004.015-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Jun 02 2019 Jitka Plesnikova <jplesnik@redhat.com> - 2.004.015-4
- Perl 5.30 re-rebuild of bootstrapped packages

* Fri May 31 2019 Jitka Plesnikova <jplesnik@redhat.com> - 2.004.015-3
- Perl 5.30 rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.004.015-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Tue Aug 28 2018 Petr Pisar <ppisar@redhat.com> - 2.004.015-1
- 2.004.015 bump

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.004.014-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Sat Jun 30 2018 Jitka Plesnikova <jplesnik@redhat.com> - 2.004.014-3
- Perl 5.28 re-rebuild of bootstrapped packages

* Fri Jun 29 2018 Jitka Plesnikova <jplesnik@redhat.com> - 2.004.014-2
- Perl 5.28 rebuild

* Wed Mar 14 2018 Petr Pisar <ppisar@redhat.com> - 2.004.014-1
- 2.004.014 bump

* Tue Feb 06 2018 Petr Pisar <ppisar@redhat.com> - 2.004.0013-1
- 2.004.0013 bump (bug #1540220)

* Thu Jan 04 2018 Petr Pisar <ppisar@redhat.com> - 2.004.012-1
- 2.004.012 bump

* Tue Jan 02 2018 Petr Pisar <ppisar@redhat.com> - 2.004.011-1
- 2.004.011 bump

* Wed Nov 22 2017 Petr Pisar <ppisar@redhat.com> - 2.004.010-1
- 2.004.010 bump

* Thu Oct 12 2017 Jitka Plesnikova <jplesnik@redhat.com> - 2.004.009-1
- 2.004.009 bump

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.004.008-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Wed Jun 14 2017 Petr Pisar <ppisar@redhat.com> - 2.004.008-1
- 2.004.008 bump

* Wed Jun 07 2017 Jitka Plesnikova <jplesnik@redhat.com> - 2.004.007-3
- Perl 5.26 re-rebuild of bootstrapped packages

* Tue Jun 06 2017 Jitka Plesnikova <jplesnik@redhat.com> - 2.004.007-2
- Perl 5.26 rebuild

* Tue May 30 2017 Petr Pisar <ppisar@redhat.com> - 2.004.007-1
- 2.004.007 bump

* Fri May 26 2017 Petr Pisar <ppisar@redhat.com> - 2.004.006-1
- 2.004.006 bump

* Tue May 09 2017 Petr Pisar <ppisar@redhat.com> - 2.004.004-1
- 2.004.004 bump

* Tue Apr 18 2017 Petr Pisar <ppisar@redhat.com> - 2.004.003-1
- 2.004.003 bump

* Wed Apr 12 2017 Petr Pisar <ppisar@redhat.com> - 2.004.002-1
- 2.004.002 bump

* Wed Apr 12 2017 Petr Pisar <ppisar@redhat.com> - 2.004.001-1
- 2.004.001 bump

* Thu Apr 06 2017 Petr Pisar <ppisar@redhat.com> - 2.003.002-1
- 2.003.002 bump

* Tue Mar 14 2017 Petr Pisar <ppisar@redhat.com> - 2.003.001-1
- 2.003.001 bump (bug #1425088)

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.002.004-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Tue Dec 06 2016 Petr Pisar <ppisar@redhat.com> - 2.002.004-1
- 2.002.004 bump

* Mon Dec 05 2016 Petr Pisar <ppisar@redhat.com> - 2.002.003-1
- 2.002.003 bump

* Mon Aug 08 2016 Jitka Plesnikova <jplesnik@redhat.com> - 1.130.004-1
- 1.130.004 bump

* Mon Jun 06 2016 Petr Pisar <ppisar@redhat.com> - 1.12.009-1
- 1.12.009 bump

* Fri Jun 03 2016 Petr Pisar <ppisar@redhat.com> - 1.12.008-1
- 1.12.008 bump
- Enable tests against server

* Wed Jun 01 2016 Petr Pisar <ppisar@redhat.com> - 1.12.007-1
- 1.12.007 bump

* Sun May 15 2016 Jitka Plesnikova <jplesnik@redhat.com> - 1.12-5
- Perl 5.24 rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.12-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.12-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Thu Jun 04 2015 Jitka Plesnikova <jplesnik@redhat.com> - 1.12-2
- Perl 5.22 rebuild

* Thu Dec 18 2014 Jitka Plesnikova <jplesnik@redhat.com> - 1.12-1
- 1.12 bump
- Modernize spec file

* Wed Aug 27 2014 Jitka Plesnikova <jplesnik@redhat.com> - 1.11-12
- Perl 5.20 rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.11-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.11-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Jul 18 2013 Petr Pisar <ppisar@redhat.com> - 1.11-9
- Perl 5.18 rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.11-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.11-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Mon Jun 11 2012 Petr Pisar <ppisar@redhat.com> - 1.11-6
- Perl 5.16 rebuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.11-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Mon Jun 20 2011 Marcela Mašláňová <mmaslano@redhat.com> - 1.11-4
- Perl mass rebuild

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.11-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Thu Dec 16 2010 Marcela Maslanova <mmaslano@redhat.com> - 1.11-2
- 661697 rebuild for fixing problems with vendorach/lib

* Thu Jun 24 2010 Ruben Kerkhof <ruben@rubenkerkhof.com> 1.11-1
- Upstream released new version

* Sun May 02 2010 Marcela Maslanova <mmaslano@redhat.com> - 1.09-6
- Mass rebuild with perl-5.12.0

* Fri Dec  4 2009 Stepan Kasal <skasal@redhat.com> - 1.09-5
- rebuild against perl 5.10.1

* Sat Jul 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.09-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Thu Feb 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.09-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Thu Feb  7 2008 Tom "spot" Callaway <tcallawa@redhat.com> 1.09-2
- rebuild for new per

* Sat Jun 30 2007 Ruben Kerkhof <ruben@rubenkerkhof.com> 1.09-1
- Upstream released new version
- New version now includes license information
- Filter out just one of the two Provides for Gearman::Client
* Thu Jun 28 2007 Ruben Kerkhof <ruben@rubenkerkhof.com> 1.08-2
- Filter out double Provides for Gearman::Client
- Change Source0 url
* Mon May 21 2007 Ruben Kerkhof <ruben@rubenkerkhof.com> 1.08-1
- Initial import

