# Run optional test
%bcond_without perl_Function_Parameters_enables_optional_test

Name:           perl-Function-Parameters
%global cpan_version 2.001003
Version:        2.1.3
Release:        16%{?dist}
Summary:        Subroutine definitions with parameter lists
License:        GPL+ or Artistic
URL:            https://metacpan.org/release/Function-Parameters
Source0:        https://cpan.metacpan.org/authors/id/M/MA/MAUKE/Function-Parameters-%{cpan_version}.tar.gz
BuildRequires:  findutils
BuildRequires:  gcc
BuildRequires:  make
BuildRequires:  perl-interpreter
BuildRequires:  perl-devel
BuildRequires:  perl-generators
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
BuildRequires:  perl(File::Find)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(Moose)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
# Run-time:
BuildRequires:  perl(Carp)
BuildRequires:  perl(Moose::Util::TypeConstraints)
BuildRequires:  perl(overload)
BuildRequires:  perl(Scalar::Util)
BuildRequires:  perl(XSLoader)
# Tests:
BuildRequires:  perl(aliased)
BuildRequires:  perl(attributes)
BuildRequires:  perl(constant)
BuildRequires:  perl(Dir::Self)
BuildRequires:  perl(feature)
BuildRequires:  perl(Hash::Util) >= 0.07
BuildRequires:  perl(integer)
BuildRequires:  perl(lib)
BuildRequires:  perl(Moose::Util)
BuildRequires:  perl(MooseX::Types)
BuildRequires:  perl(MooseX::Types::Moose)
BuildRequires:  perl(Sub::Name)
BuildRequires:  perl(Test::Deep)
BuildRequires:  perl(Test::Fatal)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(utf8)
BuildRequires:  perl(vars)
%if %{with perl_Function_Parameters_enables_optional_test}
# Optional tests:
BuildRequires:  perl(threads)
BuildRequires:  perl(threads::shared)
%endif
Requires:       perl(Moose::Util::TypeConstraints)

%description
This module extends Perl with keywords that let you define functions with
parameter lists. It uses Perl's keyword plugin API, so it works reliably
and doesn't require a source filter.

%prep
%setup -q -n Function-Parameters-%{cpan_version}

%build
perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 OPTIMIZE="$RPM_OPT_FLAGS"
make %{?_smp_mflags}

%install
make pure_install DESTDIR=$RPM_BUILD_ROOT
find $RPM_BUILD_ROOT -type f -name '*.bs' -size 0 -delete
%{_fixperms} $RPM_BUILD_ROOT/*

%check
make test

%files
%doc Changes README
%{perl_vendorarch}/auto/*
%{perl_vendorarch}/Function*
%{_mandir}/man3/*

%changelog
* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.3-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed Jun 01 2022 Jitka Plesnikova <jplesnik@redhat.com> - 2.1.3-15
- Perl 5.36 rebuild

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.3-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.3-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Sat May 22 2021 Jitka Plesnikova <jplesnik@redhat.com> - 2.1.3-12
- Perl 5.34 rebuild

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.3-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.3-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jun 23 2020 Jitka Plesnikova <jplesnik@redhat.com> - 2.1.3-9
- Perl 5.32 rebuild

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.3-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.3-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri May 31 2019 Jitka Plesnikova <jplesnik@redhat.com> - 2.1.3-6
- Perl 5.30 rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.3-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Jun 29 2018 Jitka Plesnikova <jplesnik@redhat.com> - 2.1.3-3
- Perl 5.28 rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Mon Nov 13 2017 Petr Pisar <ppisar@redhat.com> - 2.1.3-1
- 2.001003 bump

* Thu Nov 09 2017 Petr Pisar <ppisar@redhat.com> - 2.1.2-1
- 2.001002 bump

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Mon Jul 03 2017 Petr Pisar <ppisar@redhat.com> - 2.1.1-1
- 2.001001 bump

* Tue Jun 06 2017 Jitka Plesnikova <jplesnik@redhat.com> - 2.0.7-2
- Perl 5.26 rebuild

* Tue May 16 2017 Petr Pisar <ppisar@redhat.com> - 2.0.7-1
- 2.000007 bump

* Tue Apr 18 2017 Petr Pisar <ppisar@redhat.com> - 2.0.6-2
- 2.000006 bump

* Mon Apr 03 2017 Petr Pisar <ppisar@redhat.com> - 2.0.3-1
- 2.000003 bump

* Tue Mar 28 2017 Petr Pisar <ppisar@redhat.com> - 2.0.2-1
- 2.000002 bump

* Fri Mar 17 2017 Petr Pisar <ppisar@redhat.com> - 1.0706-1
- 1.0706 bump

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0705-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Jun 15 2016 Petr Pisar <ppisar@redhat.com> - 1.0705-1
- 1.0705 bump

* Mon May 16 2016 Jitka Plesnikova <jplesnik@redhat.com> - 1.0704-2
- Perl 5.24 rebuild

* Mon Feb 15 2016 Petr Pisar <ppisar@redhat.com> - 1.0704-1
- 1.0704 bump

* Thu Feb 04 2016 Petr Pisar <ppisar@redhat.com> 1.0703-1
- Specfile autogenerated by cpanspec 1.78.
- Address mistakes found by review
