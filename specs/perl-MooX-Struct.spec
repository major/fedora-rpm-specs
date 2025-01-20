# Run optional tests
%{bcond_without perl_MooX_Struct_enables_optional_test}

Name:           perl-MooX-Struct
Version:        0.020
Release:        15%{?dist}
Summary:        Record structure-like Moo classes
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/MooX-Struct
Source0:        https://cpan.metacpan.org/authors/id/T/TO/TOBYINK/MooX-Struct-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  make
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
BuildRequires:  perl(strict)
# Run-time:
BuildRequires:  perl(:VERSION) >= 5.8
BuildRequires:  perl(B::Deparse)
BuildRequires:  perl(B::Hooks::EndOfScope)
BuildRequires:  perl(Carp)
BuildRequires:  perl(Data::Dumper)
BuildRequires:  perl(Data::Printer::Filter)
BuildRequires:  perl(Exporter::Tiny) >= 0.044
BuildRequires:  perl(IO::Handle)
# Moo 1.006 for tests from META
BuildRequires:  perl(Moo) >= 1.006
BuildRequires:  perl(Moo::Role)
BuildRequires:  perl(namespace::autoclean) >= 0.19
BuildRequires:  perl(namespace::clean)
BuildRequires:  perl(Object::ID)
BuildRequires:  perl(overload)
BuildRequires:  perl(Scalar::Util)
BuildRequires:  perl(Term::ANSIColor)
BuildRequires:  perl(Types::Standard) >= 1.000
BuildRequires:  perl(Types::TypeTiny) >= 1.000
BuildRequires:  perl(utf8)
BuildRequires:  perl(warnings)
# Tests:
BuildRequires:  perl(if)
BuildRequires:  perl(Test::More) >= 0.61
%if %{with perl_MooX_Struct_enables_optional_test}
# Optional tests:
BuildRequires:  perl(Data::Printer) >= 0.36
%endif
Requires:       perl(B::Deparse)
Requires:       perl(Data::Dumper)
Requires:       perl(Data::Printer) >= 0.36
Requires:       perl(Data::Printer::Filter)
Requires:       perl(Exporter::Tiny) >= 0.044
Requires:       perl(IO::Handle)
Requires:       perl(Moo::Role)
Requires:       perl(namespace::autoclean) >= 0.19
Requires:       perl(Object::ID)
Requires:       perl(Term::ANSIColor)

%description
MooX::Struct allows you to create cheap struct-like classes for your data
using Moo.

# Remove under-specified dependencies
%global __requires_exclude %{?__requires_exclude:%{__requires_exclude}|}^perl\\((Exporter::Tiny|namespace::autoclean)\\)$

%prep
%setup -q -n MooX-Struct-%{version}

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
%doc Changes COPYRIGHT CREDITS NEWS README
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
* Sat Jan 18 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.020-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.020-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.020-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.020-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.020-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.020-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.020-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed Jun 01 2022 Jitka Plesnikova <jplesnik@redhat.com> - 0.020-8
- Perl 5.36 rebuild

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.020-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.020-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Sat May 22 2021 Jitka Plesnikova <jplesnik@redhat.com> - 0.020-5
- Perl 5.34 rebuild

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.020-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.020-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jun 23 2020 Jitka Plesnikova <jplesnik@redhat.com> - 0.020-2
- Perl 5.32 rebuild

* Thu Feb 27 2020 Petr Pisar <ppisar@redhat.com> - 0.020-1
- 0.020 bump

* Tue Feb 25 2020 Petr Pisar <ppisar@redhat.com> - 0.019-1
- 0.019 bump

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.017-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.017-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri May 31 2019 Jitka Plesnikova <jplesnik@redhat.com> - 0.017-5
- Perl 5.30 rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.017-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.017-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Sat Jun 30 2018 Jitka Plesnikova <jplesnik@redhat.com> - 0.017-2
- Perl 5.28 rebuild

* Mon Jun 11 2018 Petr Pisar <ppisar@redhat.com> - 0.017-1
- 0.017 bump

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.016-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.016-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Tue Jun 06 2017 Jitka Plesnikova <jplesnik@redhat.com> - 0.016-2
- Perl 5.26 rebuild

* Tue May 23 2017 Petr Pisar <ppisar@redhat.com> - 0.016-1
- 0.016 bump

* Fri May 12 2017 Petr Pisar <ppisar@redhat.com> - 0.015-1
- 0.015 bump

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.014-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Feb 01 2017 Jitka Plesnikova <jplesnik@redhat.com> - 0.014-1
- 0.014 bump

* Thu Jun 23 2016 Petr Pisar <ppisar@redhat.com> 0.013-1
- Specfile autogenerated by cpanspec 1.78.
