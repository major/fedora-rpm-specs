Name:           perl-Test-Moose-More
Version:        0.050
Release:        23%{?dist}
Summary:        More tools for testing Moose packages
# Automatically converted from old format: LGPLv2+ - review is highly recommended.
License:        LicenseRef-Callaway-LGPLv2+
URL:            https://metacpan.org/release/Test-Moose-More
Source0:        https://cpan.metacpan.org/authors/id/R/RS/RSRCHBOY/Test-Moose-More-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  make
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
# Run-time:
BuildRequires:  perl(Carp)
BuildRequires:  perl(Data::OptList)
BuildRequires:  perl(List::MoreUtils)
BuildRequires:  perl(List::Util) >= 1.45
BuildRequires:  perl(Moose::Util)
BuildRequires:  perl(Moose::Util::TypeConstraints)
BuildRequires:  perl(Scalar::Util)
BuildRequires:  perl(Sub::Exporter::Progressive)
BuildRequires:  perl(Syntax::Keyword::Junction)
BuildRequires:  perl(Test::Builder)
BuildRequires:  perl(Test::Moose)
BuildRequires:  perl(Test::More) >= 0.94
# Tests only:
BuildRequires:  perl(blib)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(IO::Handle)
BuildRequires:  perl(IPC::Open3)
BuildRequires:  perl(Moose)
BuildRequires:  perl(Moose::Deprecated)
BuildRequires:  perl(Moose::Meta::Attribute)
BuildRequires:  perl(Moose::Role)
BuildRequires:  perl(Moose::Util::MetaRole)
BuildRequires:  perl(namespace::autoclean)
BuildRequires:  perl(TAP::SimpleOutput) >= 0.009
BuildRequires:  perl(Test::Builder::Tester)
BuildRequires:  perl(Test::CheckDeps) >= 0.010
Requires:       perl(Test::More) >= 0.94

# Removed under-specified dependencies
%global __requires_exclude %{?__requires_exclude:%__requires_exclude|}^perl\\(Test::More\\)$

%description
This package contains a number of additional tests that can be employed
against Moose classes/roles. It is intended to replace Test::Moose.

%prep
%setup -q -n Test-Moose-More-%{version}

%build
perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1
make %{?_smp_mflags}

%install
make pure_install DESTDIR=$RPM_BUILD_ROOT
%{_fixperms} $RPM_BUILD_ROOT/*

%check
make test

%files
%license LICENSE
%doc Changes README
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
* Sat Jan 18 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.050-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Wed Sep 04 2024 Miroslav Suchý <msuchy@redhat.com> - 0.050-22
- convert license to SPDX

* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.050-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.050-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.050-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.050-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.050-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.050-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed Jun 01 2022 Jitka Plesnikova <jplesnik@redhat.com> - 0.050-15
- Perl 5.36 rebuild

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.050-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.050-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Sun May 23 2021 Jitka Plesnikova <jplesnik@redhat.com> - 0.050-12
- Perl 5.34 rebuild

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.050-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.050-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jun 23 2020 Jitka Plesnikova <jplesnik@redhat.com> - 0.050-9
- Perl 5.32 rebuild

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.050-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.050-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri May 31 2019 Jitka Plesnikova <jplesnik@redhat.com> - 0.050-6
- Perl 5.30 rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.050-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.050-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Jun 29 2018 Jitka Plesnikova <jplesnik@redhat.com> - 0.050-3
- Perl 5.28 rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.050-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Fri Sep 22 2017 Petr Pisar <ppisar@redhat.com> - 0.050-1
- 0.050 bump

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.048-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Mon Jun 19 2017 Petr Pisar <ppisar@redhat.com> - 0.048-1
- 0.048 bump

* Tue Jun 06 2017 Jitka Plesnikova <jplesnik@redhat.com> - 0.047-2
- Perl 5.26 rebuild

* Wed Apr 26 2017 Petr Pisar <ppisar@redhat.com> - 0.047-1
- 0.047 bump

* Tue Apr 18 2017 Petr Pisar <ppisar@redhat.com> - 0.046-1
- 0.046 bump

* Thu Apr 06 2017 Petr Pisar <ppisar@redhat.com> - 0.045-1
- 0.045 bump

* Wed Feb 15 2017 Petr Pisar <ppisar@redhat.com> - 0.043-1
- 0.043 bump

* Tue Feb 14 2017 Petr Pisar <ppisar@redhat.com> - 0.042-1
- 0.042 bump

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.038-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Jun 23 2016 Petr Pisar <ppisar@redhat.com> - 0.038-1
- 0.038 bump

* Mon May 16 2016 Jitka Plesnikova <jplesnik@redhat.com> - 0.037-3
- Perl 5.24 rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.037-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Mon Feb 01 2016 Petr Pisar <ppisar@redhat.com> - 0.037-1
- 0.037 bump

* Thu Aug 27 2015 Petr Pisar <ppisar@redhat.com> - 0.035-1
- 0.035 bump

* Thu Jul 30 2015 Petr Pisar <ppisar@redhat.com> - 0.033-1
- 0.033 bump

* Mon Jul 13 2015 Petr Pisar <ppisar@redhat.com> - 0.032-1
- 0.032 bump

* Wed Jul 01 2015 Petr Pisar <ppisar@redhat.com> - 0.031-1
- 0.031 bump

* Mon Jun 29 2015 Petr Pisar <ppisar@redhat.com> - 0.030-1
- 0.030 bump

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.029-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Mon Jun 08 2015 Jitka Plesnikova <jplesnik@redhat.com> - 0.029-2
- Perl 5.22 rebuild

* Tue Mar 31 2015 Petr Pisar <ppisar@redhat.com> - 0.029-1
- 0.029 bump

* Fri Mar 13 2015 Petr Pisar <ppisar@redhat.com> - 0.028-1
- 0.028 bump

* Fri Mar 13 2015 Petr Pisar <ppisar@redhat.com> - 0.027-1
- 0.027 bump

* Mon Feb 02 2015 Petr Pisar <ppisar@redhat.com> - 0.026-1
- 0.026 bump

* Tue Nov 25 2014 Petr Pisar <ppisar@redhat.com> - 0.025-1
- 0.025 bump

* Mon Sep 01 2014 Jitka Plesnikova <jplesnik@redhat.com> - 0.024-3
- Perl 5.20 rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.024-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Mon May 26 2014 Petr Pisar <ppisar@redhat.com> - 0.024-1
- 0.024 bump

* Thu Jan 23 2014 Petr Pisar <ppisar@redhat.com> - 0.023-1
- 0.023 bump

* Mon Nov 18 2013 Petr Pisar <ppisar@redhat.com> - 0.022-1
- 0.022 bump

* Sat Aug 03 2013 Petr Pisar <ppisar@redhat.com> - 0.020-1
- 0.020 bump

* Sat Aug 03 2013 Petr Pisar <ppisar@redhat.com> - 0.019-2
- Perl 5.18 rebuild

* Fri Jan 25 2013 Petr Pisar <ppisar@redhat.com> - 0.019-1
- 0.019 bump

* Thu Jan 10 2013 Petr Pisar <ppisar@redhat.com> - 0.018-1
- 0.018 bump

* Mon Oct 29 2012 Petr Pisar <ppisar@redhat.com> - 0.017-1
- 0.017 bump

* Mon Oct 22 2012 Petr Pisar <ppisar@redhat.com> - 0.016-1
- 0.016 bump

* Mon Aug 27 2012 Petr Pisar <ppisar@redhat.com> - 0.011-1
- 0.011 bump

* Mon Aug 27 2012 Petr Pisar <ppisar@redhat.com> - 0.010-1
- 0.010 bump

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.009-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jun 22 2012 Petr Pisar <ppisar@redhat.com> - 0.009-2
- Perl 5.16 rebuild

* Fri Apr 27 2012 Petr Pisar <ppisar@redhat.com> - 0.009-1
- 0.009 bump

* Mon Apr 16 2012 Petr Pisar <ppisar@redhat.com> - 0.008-1
- 0.008 bump

* Thu Apr 12 2012 Petr Pisar <ppisar@redhat.com> - 0.007-1
- 0.007 bump

* Tue Apr 10 2012 Petr Pisar <ppisar@redhat.com> - 0.006-1
- 0.006 bump

* Wed Feb 29 2012 Petr Pisar <ppisar@redhat.com> 0.005-1
- Specfile autogenerated by cpanspec 1.78.
