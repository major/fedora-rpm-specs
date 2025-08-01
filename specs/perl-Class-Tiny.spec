# Run optional test
%if ! (0%{?rhel})
%bcond_without perl_Class_Tiny_enables_optional_test
%else
%bcond_with perl_Class_Tiny_enables_optional_test
%endif

Name:           perl-Class-Tiny
Version:        1.008
Release:        14%{?dist}
Summary:        Minimalist class construction
License:        Apache-2.0
URL:            https://metacpan.org/release/Class-Tiny
Source0:        https://cpan.metacpan.org/authors/id/D/DA/DAGOLDEN/Class-Tiny-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  coreutils
BuildRequires:  make
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(:VERSION) >= 5.6
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
# Run-time
BuildRequires:  perl(Carp)
# Devel::GlobalDestruction not needed on Perl >= 5.14
# mro on Perl >= 5.10
BuildRequires:  perl(mro)
# Tests
BuildRequires:  perl(base)
# CPAN::Meta 2.120900 not helpful
BuildRequires:  perl(Exporter)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(lib)
BuildRequires:  perl(subs)
BuildRequires:  perl(Test::More) >= 0.96
%if %{with perl_Class_Tiny_enables_optional_test}
# Optional test
BuildRequires:  perl(Test::FailWarnings)
%endif
# Devel::GlobalDestruction not needed on Perl >= 5.14
# mro on Perl >= 5.10
Requires:       perl(mro)

# Filter from requires
# Devel::GlobalDestruction not needed on Perl >= 5.14
%global __requires_exclude %{?__requires_exclude:%__requires_exclude|}^perl\\(Devel::GlobalDestruction\\)

%description
This module offers a minimalist class construction kit in around 120 lines
of code. Here is a list of features:

* defines attributes via import arguments
* generates read-write accessors
* supports lazy attribute defaults
* supports custom accessors
* superclass provides a standard new constructor
* new takes a hash reference or list of key/value pairs
* new has heuristics to catch constructor attribute typos
* new calls BUILD for each class from parent to child
* superclass provides a DESTROY method
* DESTROY calls DEMOLISH for each class from child to parent


%prep
%setup -q -n Class-Tiny-%{version}

%build
perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1
%{make_build}

%install
%{make_install}
%{_fixperms} $RPM_BUILD_ROOT/*

%check
make test

%files
%license LICENSE
%doc Changes CONTRIBUTING.mkdn README
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
* Fri Jul 25 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.008-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_43_Mass_Rebuild

* Sat Jan 18 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.008-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.008-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.008-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.008-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.008-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.008-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.008-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Tue May 31 2022 Jitka Plesnikova <jplesnik@redhat.com> - 1.008-6
- Perl 5.36 rebuild

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.008-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.008-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri May 21 2021 Jitka Plesnikova <jplesnik@redhat.com> - 1.008-3
- Perl 5.34 rebuild

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.008-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Sep 07 2020 Jitka Plesnikova <jplesnik@redhat.com> - 1.008-1
- 1.008 bump

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.006-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jun 23 2020 Jitka Plesnikova <jplesnik@redhat.com> - 1.006-13
- Perl 5.32 rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.006-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.006-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri May 31 2019 Jitka Plesnikova <jplesnik@redhat.com> - 1.006-10
- Perl 5.30 rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.006-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.006-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Jun 28 2018 Jitka Plesnikova <jplesnik@redhat.com> - 1.006-7
- Perl 5.28 rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.006-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Dec 07 2017 Petr Pisar <ppisar@redhat.com> - 1.006-5
- Modernize spec file

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.006-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sun Jun 04 2017 Jitka Plesnikova <jplesnik@redhat.com> - 1.006-3
- Perl 5.26 rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.006-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Sep 12 2016 Jitka Plesnikova <jplesnik@redhat.com> - 1.006-1
- 1.006 bump

* Sun May 15 2016 Jitka Plesnikova <jplesnik@redhat.com> - 1.004-3
- Perl 5.24 rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.004-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Mon Nov 02 2015 Jitka Plesnikova <jplesnik@redhat.com> - 1.004-1
- 1.004 bump

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.001-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Thu Jun 04 2015 Jitka Plesnikova <jplesnik@redhat.com> - 1.001-2
- Perl 5.22 rebuild

* Tue Feb 10 2015 Jitka Plesnikova <jplesnik@redhat.com> - 1.001-1
- 1.001 bump

* Wed Aug 27 2014 Jitka Plesnikova <jplesnik@redhat.com> - 1.000-2
- Perl 5.20 rebuild

* Tue Jul 29 2014 Jitka Plesnikova <jplesnik@redhat.com> - 1.000-1
- 1.000 bump

* Wed Jul 16 2014 Jitka Plesnikova <jplesnik@redhat.com> - 0.015-1
- 0.015 bump

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.014-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Fri Nov 29 2013 Jitka Plesnikova <jplesnik@redhat.com> - 0.014-1
- 0.014 bump

* Thu Nov 28 2013 Jitka Plesnikova <jplesnik@redhat.com> - 0.013-1
- 0.013 bump

* Sun Nov 03 2013 Jitka Plesnikova <jplesnik@redhat.com> - 0.012-1
- 0.012 bump

* Thu Sep 26 2013 Jitka Plesnikova <jplesnik@redhat.com> - 0.011-1
- 0.011 bump

* Thu Sep 19 2013 Jitka Plesnikova <jplesnik@redhat.com> - 0.010-1
- 0.010 bump

* Tue Sep 17 2013 Jitka Plesnikova <jplesnik@redhat.com> - 0.009-1
- 0.009 bump

* Mon Sep 16 2013 Jitka Plesnikova <jplesnik@redhat.com> - 0.008-1
- Specfile autogenerated by cpanspec 1.78.
