Name:           perl-Config-Model-Tester
Version:        4.007
Release:        11%{?dist}
Summary:        Test framework for Config::Model
License:        LGPL-2.1-only
URL:            https://metacpan.org/release/Config-Model-Tester
Source0:        https://cpan.metacpan.org/authors/id/D/DD/DDUMONT/Config-Model-Tester-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  coreutils
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
BuildRequires:  perl(Module::Build)
# Run-time:
BuildRequires:  perl(:VERSION) >= 5.10.1
# Bootstrap to prevent circular dependency on perl-Config-Model
%if !%{defined perl_bootstrap}
BuildRequires:  perl(Config::Model)
BuildRequires:  perl(Config::Model::BackendMgr)
BuildRequires:  perl(Config::Model::Lister)
BuildRequires:  perl(Config::Model::Value)
%endif
BuildRequires:  perl(Exporter)
BuildRequires:  perl(File::Copy::Recursive)
BuildRequires:  perl(Getopt::Long)
BuildRequires:  perl(locale)
BuildRequires:  perl(Log::Log4perl) >= 1.11
BuildRequires:  perl(Path::Tiny)
BuildRequires:  perl(Test::Differences)
BuildRequires:  perl(Test::Exception)
BuildRequires:  perl(Test::File::Contents)
BuildRequires:  perl(Test::Log::Log4perl)
BuildRequires:  perl(Test::Memory::Cycle)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Test::Warn)
BuildRequires:  perl(utf8)
BuildRequires:  perl(vars)
# Tests:
BuildRequires:  perl(ExtUtils::testlib)
Requires:       perl(Test::Log::Log4perl)

%description
This class provides a way to test configuration models with tests files.
This class was designed to tests several models and several tests cases
per model.

%prep
%setup -q -n Config-Model-Tester-%{version}

%build
perl Build.PL installdirs=vendor
./Build

%install
./Build install destdir=$RPM_BUILD_ROOT create_packlist=0
%{_fixperms} $RPM_BUILD_ROOT/*

%check
./Build test

%files
%license LICENSE
%doc Changes
%{perl_vendorlib}/Config*
%{_mandir}/man3/Config::Model::Tester*

%changelog
* Sat Jan 18 2025 Fedora Release Engineering <releng@fedoraproject.org> - 4.007-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 4.007-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 4.007-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 4.007-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 4.007-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 4.007-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 4.007-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Fri Jun 03 2022 Jitka Plesnikova <jplesnik@redhat.com> - 4.007-4
- Perl 5.36 re-rebuild of bootstrapped packages

* Wed Jun 01 2022 Jitka Plesnikova <jplesnik@redhat.com> - 4.007-3
- Perl 5.36 rebuild

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 4.007-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Tue Oct 26 2021 Jitka Plesnikova <jplesnik@redhat.com> - 4.007-1
- 4.007 bump

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 4.006-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Mon May 24 2021 Jitka Plesnikova <jplesnik@redhat.com> - 4.006-5
- Perl 5.34 re-rebuild of bootstrapped packages

* Sat May 22 2021 Jitka Plesnikova <jplesnik@redhat.com> - 4.006-4
- Perl 5.34 rebuild

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 4.006-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Aug 04 2020 Jitka Plesnikova <jplesnik@redhat.com> - 4.006-2
- Added Test::Log::Log4perl to run-require

* Wed Jul 29 2020 Jitka Plesnikova <jplesnik@redhat.com> - 4.006-1
- 4.006 bump

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 4.005-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Jun 26 2020 Jitka Plesnikova <jplesnik@redhat.com> - 4.005-4
- Perl 5.32 re-rebuild of bootstrapped packages

* Thu Jun 25 2020 Jitka Plesnikova <jplesnik@redhat.com> - 4.005-3
- Perl 5.32 rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 4.005-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Tue Dec 10 2019 Jitka Plesnikova <jplesnik@redhat.com> - 4.005-1
- 4.005 bump

* Mon Nov 11 2019 Jitka Plesnikova <jplesnik@redhat.com> - 4.004-1
- 4.004 bump

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 4.003-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Jun 02 2019 Jitka Plesnikova <jplesnik@redhat.com> - 4.003-3
- Perl 5.30 re-rebuild of bootstrapped packages

* Fri May 31 2019 Jitka Plesnikova <jplesnik@redhat.com> - 4.003-2
- Perl 5.30 rebuild

* Fri May 10 2019 Jitka Plesnikova <jplesnik@redhat.com> - 4.003-1
- 4.003 bump

* Thu May 02 2019 Jitka Plesnikova <jplesnik@redhat.com> - 4.002-1
- 4.002 bump

* Tue Apr 30 2019 Jitka Plesnikova <jplesnik@redhat.com> - 4.001-1
- 4.001 bump

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.007-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Mon Jan 14 2019 Jitka Plesnikova <jplesnik@redhat.com> - 3.007-1
- 3.007 bump

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.006-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Sun Jul 01 2018 Jitka Plesnikova <jplesnik@redhat.com> - 3.006-3
- Perl 5.28 re-rebuild of bootstrapped packages

* Sat Jun 30 2018 Jitka Plesnikova <jplesnik@redhat.com> - 3.006-2
- Perl 5.28 rebuild

* Mon Apr 16 2018 Jitka Plesnikova <jplesnik@redhat.com> - 3.006-1
- 3.006 bump

* Tue Apr 03 2018 Jitka Plesnikova <jplesnik@redhat.com> - 3.005-1
- 3.005 bump

* Thu Mar 29 2018 Petr Pisar <ppisar@redhat.com> - 3.004-1
- 3.004 bump

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.003-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Mon Nov 06 2017 Jitka Plesnikova <jplesnik@redhat.com> - 3.003-1
- 3.003 bump

* Wed Aug 23 2017 Jitka Plesnikova <jplesnik@redhat.com> - 3.002-1
- 3.002 bump

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.001-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Thu Jun 08 2017 Jitka Plesnikova <jplesnik@redhat.com> - 3.001-1
- 3.001 bump

* Wed Jun 07 2017 Jitka Plesnikova <jplesnik@redhat.com> - 2.061-3
- Perl 5.26 re-rebuild of bootstrapped packages

* Tue Jun 06 2017 Jitka Plesnikova <jplesnik@redhat.com> - 2.061-2
- Perl 5.26 rebuild

* Thu Jun 01 2017 Jitka Plesnikova <jplesnik@redhat.com> - 2.061-1
- 2.061 bump

* Mon Mar 06 2017 Jitka Plesnikova <jplesnik@redhat.com> - 2.060-1
- 2.060 bump

* Mon Feb 13 2017 Jitka Plesnikova <jplesnik@redhat.com> - 2.059-1
- 2.059 bump

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.058-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Tue Dec 06 2016 Jitka Plesnikova <jplesnik@redhat.com> - 2.058-1
- 2.058 bump

* Mon Sep 05 2016 Jitka Plesnikova <jplesnik@redhat.com> - 2.057-1
- 2.057 bump

* Fri May 27 2016 Jitka Plesnikova <jplesnik@redhat.com> - 2.055-1
- 2.055 bump

* Wed May 18 2016 Jitka Plesnikova <jplesnik@redhat.com> - 2.054-3
- Perl 5.24 re-rebuild of bootstrapped packages

* Tue May 17 2016 Jitka Plesnikova <jplesnik@redhat.com> - 2.054-2
- Perl 5.24 rebuild

* Mon Apr 18 2016 Jitka Plesnikova <jplesnik@redhat.com> - 2.054-1
- 2.054 bump

* Mon Apr 04 2016 Jitka Plesnikova <jplesnik@redhat.com> - 2.053-1
- 2.053 bump

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 2.052-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Mon Oct 19 2015 Jitka Plesnikova <jplesnik@redhat.com> - 2.052-1
- 2.052 bump

* Wed Jun 24 2015 Jitka Plesnikova <jplesnik@redhat.com> - 2.051-2
- Remove local definition of bootstrap macro

* Mon Jun 22 2015 Jitka Plesnikova <jplesnik@redhat.com> - 2.051-1
- Specfile autogenerated by cpanspec 1.78.
