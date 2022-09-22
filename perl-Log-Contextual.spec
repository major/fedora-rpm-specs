Name:           perl-Log-Contextual
Version:        0.008001
Release:        16%{?dist}
Summary:        Simple logging interface with a contextual log
License:        GPL+ or Artistic
URL:            https://metacpan.org/release/Log-Contextual
Source0:        https://cpan.metacpan.org/authors/id/F/FR/FREW/Log-Contextual-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  findutils
BuildRequires:  make
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
# Run-time:
BuildRequires:  perl(B)
BuildRequires:  perl(base)
BuildRequires:  perl(Carp)
BuildRequires:  perl(Data::Dumper::Concise)
BuildRequires:  perl(Exporter::Declare) >= 0.111
BuildRequires:  perl(Exporter::Declare::Export::Generator)
BuildRequires:  perl(Moo) >= 1.003000
BuildRequires:  perl(Moo::Role)
BuildRequires:  perl(Scalar::Util)
# Optional run-time:
BuildRequires:  perl(Log::Log4perl) >= 1.29
# Tests:
BuildRequires:  perl(File::Temp)
BuildRequires:  perl(FindBin)
BuildRequires:  perl(lib)
BuildRequires:  perl(Test::Fatal)
BuildRequires:  perl(Test::More)
# Test::PerlTidy not used
# Test::Pod 1.41 not used
Requires:       perl(Exporter::Declare) >= 0.111
Requires:       perl(Moo) >= 1.003000
Requires:       perl(:MODULE_COMPAT_%(eval "`perl -V:version`"; echo $version))

# Filter under-specified depenedencies
%global __requires_exclude %{?__requires_exclude:%__requires_exclude|}^perl\\(Exporter::Declare\\)\\s*$
%global __requires_exclude %{?__requires_exclude:%__requires_exclude|}^perl\\(Moo\\)\\s*$

%description
This module is a simple interface to extensible logging. It is bundled with
a really basic logger, Log::Contextual::SimpleLogger, but in general you
should use a real logger instead of that. For something more serious but
not overly complicated, try Log::Dispatchouli.

%prep
%setup -q -n Log-Contextual-%{version}

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
* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.008001-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed Jun 01 2022 Jitka Plesnikova <jplesnik@redhat.com> - 0.008001-15
- Perl 5.36 rebuild

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.008001-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.008001-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Sun May 23 2021 Jitka Plesnikova <jplesnik@redhat.com> - 0.008001-12
- Perl 5.34 rebuild

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.008001-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.008001-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Jun 25 2020 Jitka Plesnikova <jplesnik@redhat.com> - 0.008001-9
- Perl 5.32 rebuild

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.008001-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.008001-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri May 31 2019 Jitka Plesnikova <jplesnik@redhat.com> - 0.008001-6
- Perl 5.30 rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.008001-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.008001-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Sat Jun 30 2018 Jitka Plesnikova <jplesnik@redhat.com> - 0.008001-3
- Perl 5.28 rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.008001-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Mon Jan 22 2018 Jitka Plesnikova <jplesnik@redhat.com> - 0.008001-1
- 0.008001 bump

* Wed Nov 29 2017 Jitka Plesnikova <jplesnik@redhat.com> - 0.008000-1
- 0.008000 bump

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.007001-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Tue Jun 06 2017 Jitka Plesnikova <jplesnik@redhat.com> - 0.007001-2
- Perl 5.26 rebuild

* Mon May 22 2017 Jitka Plesnikova <jplesnik@redhat.com> - 0.007001-1
- 0.007001 bump

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.007000-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Jun 06 2016 Petr Pisar <ppisar@redhat.com> - 0.007000-1
- 0.007000 bump

* Tue May 17 2016 Jitka Plesnikova <jplesnik@redhat.com> - 0.006005-5
- Perl 5.24 rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.006005-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.006005-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Mon Jun 08 2015 Jitka Plesnikova <jplesnik@redhat.com> - 0.006005-2
- Perl 5.22 rebuild

* Mon Mar 16 2015 Jitka Plesnikova <jplesnik@redhat.com> - 0.006005-1
- 0.006005 bump

* Fri Aug 29 2014 Jitka Plesnikova <jplesnik@redhat.com> - 0.006004-2
- Perl 5.20 rebuild

* Wed Jul 16 2014 Jitka Plesnikova <jplesnik@redhat.com> - 0.006004-1
- 0.006004 bump

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.006003-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Wed Feb 26 2014 Petr Pisar <ppisar@redhat.com> - 0.006003-1
- 0.006003 bump

* Fri Feb 21 2014 Jitka Plesnikova <jplesnik@redhat.com> - 0.006002-1
- 0.006002 bump

* Tue Sep 10 2013 Jitka Plesnikova <jplesnik@redhat.com> - 0.006000-1
- 0.006000 bump

* Fri Aug 09 2013 Jitka Plesnikova <jplesnik@redhat.com> - 0.005005-1
- 0.005005 bump

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.005003-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Fri Mar 22 2013 Petr Šabata <contyk@redhat.com> - 0.005003-1
- 0.005003 bump

* Mon Feb 18 2013 Jitka Plesnikova <jplesnik@redhat.com> - 0.005002-1
- 0.005002 bump

* Mon Feb 11 2013 Jitka Plesnikova <jplesnik@redhat.com> - 0.005001-1
- 0.005001 bump

* Wed Jan 30 2013 Jitka Plesnikova <jplesnik@redhat.com> - 0.004300-1
- 0.004300 bump
- Update BRs.
- Replace PERL_INSTALL_ROOT with DESTDIR.

* Tue Jul 24 2012 Jitka Plesnikova <jplesnik@redhat.com> - 0.004201-1
- Specfile autogenerated by cpanspec 1.78.
