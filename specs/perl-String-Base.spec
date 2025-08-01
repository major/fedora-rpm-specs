Name:           perl-String-Base
Version:        0.003
Release:        27%{?dist}
Summary:        String index offsetting
# Automatically converted from old format: GPL+ or Artistic - review is highly recommended.
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/String-Base
Source0:        https://cpan.metacpan.org/authors/id/Z/ZE/ZEFRAM/String-Base-%{version}.tar.gz
BuildRequires:  findutils
BuildRequires:  gcc
BuildRequires:  perl-devel
BuildRequires:  perl-generators
BuildRequires:  perl(Module::Build)
BuildRequires:  perl(ExtUtils::CBuilder) >= 0.15
# Run-Time:
BuildRequires:  perl(Lexical::SealRequireHints) >= 0.006
BuildRequires:  perl(XSLoader)
# Tests:
BuildRequires:  perl(Test::More)
# Optional tests:
BuildRequires:  perl(Test::Pod) >= 1.00
BuildRequires:  perl(Test::Pod::Coverage)
Conflicts:      perl(B::Hooks::OP::Check) < 0.19

%{?perl_default_filter}

%description
This module implements automatic offsetting of string indices. In normal
Perl, the first character of a string has index 0, the second character has
index 1, and so on. This module allows string indexes to start at some
other value. Most commonly it is used to give the first character of a
string the index 1 (and the second 2, and so on), to imitate the indexing
behavior of FORTRAN and many other languages. It is usually considered
poor style to do this.

%prep
%setup -q -n String-Base-%{version}

%build
perl Build.PL installdirs=vendor optimize="$RPM_OPT_FLAGS"
./Build

%install
./Build install destdir=$RPM_BUILD_ROOT create_packlist=0
find $RPM_BUILD_ROOT -type f -name '*.bs' -size 0 -delete
%{_fixperms} $RPM_BUILD_ROOT/*

%check
./Build test

%files
%doc Changes README
%{perl_vendorarch}/auto/*
%{perl_vendorarch}/String*
%{_mandir}/man3/*

%changelog
* Fri Jul 25 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.003-27
- Rebuilt for https://fedoraproject.org/wiki/Fedora_43_Mass_Rebuild

* Mon Jul 07 2025 Jitka Plesnikova <jplesnik@redhat.com> - 0.003-26
- Perl 5.42 rebuild

* Sat Jan 18 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.003-25
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Tue Aug 06 2024 Miroslav Suchý <msuchy@redhat.com> - 0.003-24
- convert license to SPDX

* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.003-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Tue Jun 11 2024 Jitka Plesnikova <jplesnik@redhat.com> - 0.003-22
- Perl 5.40 rebuild

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.003-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.003-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.003-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Tue Jul 11 2023 Jitka Plesnikova <jplesnik@redhat.com> - 0.003-18
- Perl 5.38 rebuild

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.003-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.003-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Tue May 31 2022 Jitka Plesnikova <jplesnik@redhat.com> - 0.003-15
- Perl 5.36 rebuild

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.003-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.003-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri May 21 2021 Jitka Plesnikova <jplesnik@redhat.com> - 0.003-12
- Perl 5.34 rebuild

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.003-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.003-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jun 23 2020 Jitka Plesnikova <jplesnik@redhat.com> - 0.003-9
- Perl 5.32 rebuild

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.003-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.003-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri May 31 2019 Jitka Plesnikova <jplesnik@redhat.com> - 0.003-6
- Perl 5.30 rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.003-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.003-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Jun 28 2018 Jitka Plesnikova <jplesnik@redhat.com> - 0.003-3
- Perl 5.28 rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.003-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Mon Jul 31 2017 Petr Pisar <ppisar@redhat.com> - 0.003-1
- 0.003 bump

* Fri Jul 28 2017 Petr Pisar <ppisar@redhat.com> - 0.002-1
- 0.002 bump

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.001-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Mon Jun 05 2017 Jitka Plesnikova <jplesnik@redhat.com> - 0.001-16
- Perl 5.26 rebuild

* Fri May 19 2017 Petr Pisar <ppisar@redhat.com> - 0.001-15
- Restore compatibility with Perl 5.26.0 (CPAN RT#117410)

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.001-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Sun May 15 2016 Jitka Plesnikova <jplesnik@redhat.com> - 0.001-13
- Perl 5.24 rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.001-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.001-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Fri Jun 05 2015 Jitka Plesnikova <jplesnik@redhat.com> - 0.001-10
- Perl 5.22 rebuild

* Thu Aug 28 2014 Jitka Plesnikova <jplesnik@redhat.com> - 0.001-9
- Perl 5.20 rebuild

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.001-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.001-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.001-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Sun Jul 21 2013 Petr Pisar <ppisar@redhat.com> - 0.001-5
- Perl 5.18 rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.001-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.001-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Wed Jun 13 2012 Petr Pisar <ppisar@redhat.com> - 0.001-2
- Perl 5.16 rebuild

* Fri Jun 08 2012 Petr Pisar <ppisar@redhat.com> 0.001-1
- Specfile autogenerated by cpanspec 1.78.
