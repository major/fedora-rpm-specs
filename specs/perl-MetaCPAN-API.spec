Name:           perl-MetaCPAN-API
Version:        0.51
Release:        23%{?dist}
Summary:        A comprehensive, DWIM-featured API to MetaCPAN
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/MetaCPAN-API
Source0:        https://cpan.metacpan.org/authors/id/H/HA/HAARG/MetaCPAN-API-%{version}.tar.gz
BuildArch:      noarch
# Build
BuildRequires:  coreutils
BuildRequires:  findutils
BuildRequires:  make
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(ExtUtils::MakeMaker)
# Module
BuildRequires:  perl(Carp)
BuildRequires:  perl(HTTP::Tiny) >= 0.014
BuildRequires:  perl(IO::Socket::SSL)
BuildRequires:  perl(JSON::MaybeXS) >= 1.001000
BuildRequires:  perl(Moo) >= 1.000001
BuildRequires:  perl(Moo::Role)
BuildRequires:  perl(namespace::autoclean)
BuildRequires:  perl(strict)
BuildRequires:  perl(Try::Tiny)
BuildRequires:  perl(Types::Standard)
BuildRequires:  perl(warnings)
# Test suite
BuildRequires:  perl(Exporter)
BuildRequires:  perl(lib)
BuildRequires:  perl(Test::Fatal)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Test::RequiresInternet)
BuildRequires:  perl(Test::TinyMocker)
# Dependencies
Requires:       perl(IO::Socket::SSL)

%description
This is a hopefully-complete API-compliant interface to MetaCPAN
(https://metacpan.org/) with DWIM capabilities, to make your life easier.

However, it has been completely rewritten to address a multitude of problems,
and is now available under the new official name: MetaCPAN::Client.

Please do not use this module.

%prep
%setup -q -n MetaCPAN-API-%{version}

%build
perl Makefile.PL INSTALLDIRS=vendor
make %{?_smp_mflags}

%install
make pure_install DESTDIR=%{buildroot}
find %{buildroot} -type f -name .packlist -delete
%{_fixperms} -c %{buildroot}

%check
make test

%files
%license LICENSE
%doc Changes README
%{perl_vendorlib}/MetaCPAN/
%{_mandir}/man3/MetaCPAN::API.3*
%{_mandir}/man3/MetaCPAN::API::Author.3*
%{_mandir}/man3/MetaCPAN::API::Autocomplete.3*
%{_mandir}/man3/MetaCPAN::API::Distribution.3*
%{_mandir}/man3/MetaCPAN::API::Favorite.3*
%{_mandir}/man3/MetaCPAN::API::File.3*
%{_mandir}/man3/MetaCPAN::API::Module.3*
%{_mandir}/man3/MetaCPAN::API::Rating.3*
%{_mandir}/man3/MetaCPAN::API::POD.3*
%{_mandir}/man3/MetaCPAN::API::Release.3*
%{_mandir}/man3/MetaCPAN::API::Source.3*

%changelog
* Sat Jan 18 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.51-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.51-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.51-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.51-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.51-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.51-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.51-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed Jun 01 2022 Jitka Plesnikova <jplesnik@redhat.com> - 0.51-16
- Perl 5.36 rebuild

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.51-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.51-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Sun May 23 2021 Jitka Plesnikova <jplesnik@redhat.com> - 0.51-13
- Perl 5.34 rebuild

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.51-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.51-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jun 23 2020 Jitka Plesnikova <jplesnik@redhat.com> - 0.51-10
- Perl 5.32 rebuild

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.51-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.51-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri May 31 2019 Jitka Plesnikova <jplesnik@redhat.com> - 0.51-7
- Perl 5.30 rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.51-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.51-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Sat Jun 30 2018 Jitka Plesnikova <jplesnik@redhat.com> - 0.51-4
- Perl 5.28 rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.51-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.51-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sun Jun 18 2017 Paul Howarth <paul@city-fan.org> - 0.51-1
- Update to 0.51
  - Switch to v1 API
    - Old complex query forms may stop working with new API
  - Stop relying on . being in @INC
  - Drop URI::Escape prereq
  - Switch from JSON to JSON::MaybeXS
  - Test clean-ups
- This release by HAARG → update source URL
- Make %%files list more explicit
- Drop redundant Group: tag and %%{?perl_default_filter}

* Tue Jun 06 2017 Jitka Plesnikova <jplesnik@redhat.com> - 0.50-7
- Perl 5.26 rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.50-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon May 16 2016 Jitka Plesnikova <jplesnik@redhat.com> - 0.50-5
- Perl 5.24 rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.50-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.50-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Mon Jun 08 2015 Jitka Plesnikova <jplesnik@redhat.com> - 0.50-2
- Perl 5.22 rebuild

* Mon Jan 26 2015 Paul Howarth <paul@city-fan.org> - 0.50-1
- Update to 0.50
  - Convert to Moo
  - Use Types::Standard
  - Remove Module::Build
  - Deprecate using x_deprecate meta-data
- Classify buildreqs by usage
- Use %%license where possible
- No longer need to avoid network tests as they're skipped automatically in
  koji
- Switch to ExtUtils::MakeMaker flow

* Mon Sep 01 2014 Jitka Plesnikova <jplesnik@redhat.com> - 0.44-3
- Perl 5.20 rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.44-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Mon Apr 28 2014 Paul Howarth <paul@city-fan.org> - 0.44-1
- Update to 0.44
  - This module is deprecated; please use MetaCPAN::Client instead
- Account for new tests that require network access

* Sun Aug 04 2013 Petr Pisar <ppisar@redhat.com> - 0.43-6
- Perl 5.18 rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.43-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.43-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.43-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jun 22 2012 Petr Pisar <ppisar@redhat.com> - 0.43-2
- Perl 5.16 rebuild

* Thu Apr 19 2012 Iain Arnell <iarnell@gmail.com> 0.43-1
- update to latest upstream version
- enable author/release tests

* Sun Apr 01 2012 Iain Arnell <iarnell@gmail.com> 0.42-1
- Specfile autogenerated by cpanspec 1.79.
- skip tests that require network access in koji
