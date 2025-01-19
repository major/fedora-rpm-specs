# Run optional tests
%bcond_without perl_BSON_enables_optional_test

Name:           perl-BSON
Version:        1.12.2
Release:        16%{?dist}
Summary:        BSON serialization and deserialization
# Automatically converted from old format: ASL 2.0 - review is highly recommended.
License:        Apache-2.0
URL:            https://metacpan.org/release/BSON
Source0:        https://cpan.metacpan.org/authors/id/M/MO/MONGODB/BSON-v%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  coreutils
BuildRequires:  findutils
BuildRequires:  make
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(:VERSION) >= 5.10.1
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
# Run-time:
BuildRequires:  perl(B)
BuildRequires:  perl(base)
BuildRequires:  perl(boolean) >= 0.45
BuildRequires:  perl(Carp)
BuildRequires:  perl(Config)
BuildRequires:  perl(constant)
BuildRequires:  perl(Crypt::URandom)
BuildRequires:  perl(DateTime)
BuildRequires:  perl(DateTime::Tiny)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(if)
BuildRequires:  perl(List::Util)
# Mango::BSON::Time not yet packaged
# Math::BigFloat not used because our perl has use64bitint=1
BuildRequires:  perl(Math::BigInt)
BuildRequires:  perl(MIME::Base64)
BuildRequires:  perl(Moo) >= 2.002004
BuildRequires:  perl(mro)
BuildRequires:  perl(namespace::clean)
BuildRequires:  perl(overload)
BuildRequires:  perl(re)
BuildRequires:  perl(Scalar::Util)
BuildRequires:  perl(Sys::Hostname)
BuildRequires:  perl(threads::shared)
BuildRequires:  perl(Tie::IxHash)
BuildRequires:  perl(Time::HiRes)
BuildRequires:  perl(Time::Local)
BuildRequires:  perl(Time::Moment)
BuildRequires:  perl(version)
# Tests:
BuildRequires:  perl(Data::Dumper)
BuildRequires:  perl(Devel::Peek)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(JSON::MaybeXS)
BuildRequires:  perl(JSON::PP) >= 2.97001
BuildRequires:  perl(lib)
BuildRequires:  perl(Path::Tiny) >= 0.054
BuildRequires:  perl(Test::Deep)
BuildRequires:  perl(Test::Fatal)
BuildRequires:  perl(Test::More) >= 0.96
# threads not used
BuildRequires:  perl(utf8)
%if %{with perl_BSON_enables_optional_test}
# Optional tests:
BuildRequires:  perl(Math::Int64)
%if !%{defined perl_bootstrap}
# Build cycle: perl-MongoDB → perl-BSON
BuildRequires:  perl(MongoDB)
BuildRequires:  perl(MongoDB::BSON::Binary)
BuildRequires:  perl(MongoDB::BSON::Regexp)
BuildRequires:  perl(MongoDB::Code)
BuildRequires:  perl(MongoDB::DBRef) >= 1.0.0
BuildRequires:  perl(MongoDB::OID)
BuildRequires:  perl(MongoDB::Timestamp)
%endif
BuildRequires:  perl(Test::Exception)
%endif
Requires:       perl(DateTime)
Requires:       perl(DateTime::Tiny)
# Keep Mango::BSON::Time optional. It's yet another MongoDB client
# implementation and BSON calls it only as a handy convertor into Mango object.
Suggests:       perl(Mango::BSON::Time)
Requires:       perl(re)
Requires:       perl(Time::Local)
Requires:       perl(Time::Moment)

%description
This Perl class implements a BSON encoder and decoder. It consumes
documents (typically hash references) and emits BSON strings and vice
versa in accordance with the BSON specification <http://bsonspec.org/>.

Upstream claims it will stop supporting this code on 2020-08-13.

%prep
%setup -q -n BSON-v%{version}

%build
perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1
%{make_build}

%install
%{make_install}
%{_fixperms} $RPM_BUILD_ROOT/*

%check
unset AUTHOR_TESTING AUTOMATED_TESTING BSON_EXTJSON BSON_EXTJSON_RELAXED \
    BSON_TEST_SORT_HASH HARNESS_PERL_SWITCHES PERL_BSON_BACKEND \
    PERL_MONGO_NO_DEP_WARNINGS
make test

%files
%license LICENSE
# devel directory contains obsoleted or not yet valid documentation
%doc Changes CONTRIBUTING.mkdn README
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.12.2-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Wed Jul 24 2024 Miroslav Suchý <msuchy@redhat.com> - 1.12.2-15
- convert license to SPDX

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.12.2-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.12.2-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.12.2-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.12.2-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.12.2-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.12.2-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Fri Jun 03 2022 Jitka Plesnikova <jplesnik@redhat.com> - 1.12.2-8
- Perl 5.36 re-rebuild of bootstrapped packages

* Wed Jun 01 2022 Jitka Plesnikova <jplesnik@redhat.com> - 1.12.2-7
- Perl 5.36 rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.12.2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.12.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Mon May 24 2021 Jitka Plesnikova <jplesnik@redhat.com> - 1.12.2-4
- Perl 5.34 re-rebuild of bootstrapped packages

* Sun May 23 2021 Jitka Plesnikova <jplesnik@redhat.com> - 1.12.2-3
- Perl 5.34 rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.12.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Aug 18 2020 Petr Pisar <ppisar@redhat.com> - 1.12.2-1
- 1.12.2 bump

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.12.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Jun 26 2020 Jitka Plesnikova <jplesnik@redhat.com> - 1.12.1-4
- Perl 5.32 re-rebuild of bootstrapped packages

* Tue Jun 23 2020 Jitka Plesnikova <jplesnik@redhat.com> - 1.12.1-3
- Perl 5.32 rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.12.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Aug 14 2019 Petr Pisar <ppisar@redhat.com> - 1.12.1-1
- 1.12.1 bump

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.12.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Mon Jul 15 2019 Petr Pisar <ppisar@redhat.com> - 1.12.0-1
- 1.12.0 bump

* Sun Jun 02 2019 Jitka Plesnikova <jplesnik@redhat.com> - 1.10.2-4
- Perl 5.30 re-rebuild of bootstrapped packages

* Fri May 31 2019 Jitka Plesnikova <jplesnik@redhat.com> - 1.10.2-3
- Perl 5.30 rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.10.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Mon Dec 10 2018 Petr Pisar <ppisar@redhat.com> - 1.10.2-1
- 1.10.2 bump

* Fri Nov 30 2018 Petr Pisar <ppisar@redhat.com> - 1.10.1-1
- 1.10.1 bump

* Wed Oct 03 2018 Jitka Plesnikova <jplesnik@redhat.com> - 1.8.1-1
- 1.8.1 bump

* Fri Sep 14 2018 Petr Pisar <ppisar@redhat.com> - 1.8.0-1
- 1.8.0 bump

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.7-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Jul 11 2018 Petr Pisar <ppisar@redhat.com> - 1.6.7-1
- 1.6.7 bump

* Sat Jun 30 2018 Jitka Plesnikova <jplesnik@redhat.com> - 1.6.6-4
- Perl 5.28 re-rebuild of bootstrapped packages

* Fri Jun 29 2018 Jitka Plesnikova <jplesnik@redhat.com> - 1.6.6-3
- Perl 5.28 rebuild

* Fri Jun 29 2018 Petr Pisar <ppisar@redhat.com> - 1.6.6-2
- Adapt to changes in MongoDB-v2.0.0

* Mon Jun 25 2018 Petr Pisar <ppisar@redhat.com> - 1.6.6-1
- 1.6.6 bump

* Wed Jun 20 2018 Petr Pisar <ppisar@redhat.com> - 1.6.5-1
- 1.6.5 bump

* Thu Jun 14 2018 Petr Pisar <ppisar@redhat.com> - 1.6.4-1
- 1.6.4 bump

* Mon May 28 2018 Petr Pisar <ppisar@redhat.com> - 1.6.3-1
- 1.6.3 bump

* Fri May 25 2018 Petr Pisar <ppisar@redhat.com> - 1.6.2-1
- 1.6.2 bump

* Mon May 21 2018 Jitka Plesnikova <jplesnik@redhat.com> - 1.6.1-1
- 1.6.1 bump

* Wed May 16 2018 Jitka Plesnikova <jplesnik@redhat.com> - 1.6.0-1
- 1.6.0 bump

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Wed Jun 07 2017 Jitka Plesnikova <jplesnik@redhat.com> - 1.4.0-3
- Perl 5.26 re-rebuild of bootstrapped packages

* Tue Jun 06 2017 Jitka Plesnikova <jplesnik@redhat.com> - 1.4.0-2
- Perl 5.26 rebuild

* Fri Mar 17 2017 Petr Pisar <ppisar@redhat.com> - 1.4.0-1
- 1.4.0 bump

* Fri Feb 24 2017 Petr Pisar <ppisar@redhat.com> - 1.2.2-3
- Fix constructing BSON::Time objects on 32-bit perl (bug #1401448)

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Dec 01 2016 Petr Pisar <ppisar@redhat.com> 1.2.2-1
- Specfile autogenerated by cpanspec 1.78.
