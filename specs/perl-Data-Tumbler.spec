Name:		perl-Data-Tumbler
Version:	0.010
Release:	30%{?dist}
Summary:	Dynamic generation of nested combinations
License:	GPL-1.0-or-later OR Artistic-1.0-Perl
URL:		https://metacpan.org/release/Data-Tumbler
Source0:	https://cpan.metacpan.org/modules/by-module/Data/Data-Tumbler-%{version}.tar.gz
BuildArch:	noarch
# Build
BuildRequires:	coreutils
BuildRequires:	findutils
BuildRequires:	make
BuildRequires:	perl-generators
BuildRequires:	perl-interpreter
BuildRequires:	perl(ExtUtils::MakeMaker)
# Module
BuildRequires:	perl(Carp)
BuildRequires:	perl(Storable)
BuildRequires:	perl(strict)
BuildRequires:	perl(warnings)
# Test Suite (upstream wants Test::Most ≥ 0.33 but test suite works fine with Test::Most 0.11)
BuildRequires:	perl(Data::Dumper)
BuildRequires:	perl(List::Util)
BuildRequires:	perl(Test::More) >= 0.88
BuildRequires:	perl(Test::Most) >= 0.11
BuildRequires:	perl(Time::HiRes)

%description
The tumble() method calls a sequence of 'provider' code references, each of
which returns a hash. The first provider is called and then, for each hash item
it returns, the tumble() method recurses to call the next provider. The
recursion continues until there are no more providers to call, at which point
the consumer code reference is called. Effectively the providers create a tree
of combinations and the consumer is called at the leaves of the tree. If a
provider returns no items then that part of the tree is pruned. Further
providers, if any, are not called and the consumer is not called.

During a call to tumble() three values are passed down through the tree and
into the consumer: path, context, and payload. The path and context are derived
from the names and values of the hashes returned by the providers. Typically
the path defines the current "path" through the tree of combinations. The
providers are passed the current path, context, and payload. The payload is
cloned at each level of recursion so that any changes made to it by providers
are only visible within the scope of the generated sub-tree.

%prep
%setup -q -n Data-Tumbler-%{version}

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
%license ARTISTIC-1.0 GPL-1 LICENSE
%doc Changes README
%{perl_vendorlib}/Data/
%{_mandir}/man3/Data::Tumbler.3*

%changelog
* Sat Jan 18 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.010-30
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.010-29
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.010-28
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.010-27
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.010-26
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.010-25
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.010-24
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Tue May 31 2022 Jitka Plesnikova <jplesnik@redhat.com> - 0.010-23
- Perl 5.36 rebuild

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.010-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.010-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri May 21 2021 Jitka Plesnikova <jplesnik@redhat.com> - 0.010-20
- Perl 5.34 rebuild

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.010-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Fri Jan  8 2021 Paul Howarth <paul@city-fan.org> - 0.010-18
- Spec tidy-up
  - Specify all build dependencies
  - Use author-independent source URL
  - Simplify find command using -delete
  - Fix permissions verbosely
  - Use %%license unconditionally

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.010-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jun 23 2020 Jitka Plesnikova <jplesnik@redhat.com> - 0.010-16
- Perl 5.32 rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.010-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.010-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri May 31 2019 Jitka Plesnikova <jplesnik@redhat.com> - 0.010-13
- Perl 5.30 rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.010-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.010-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Jun 28 2018 Jitka Plesnikova <jplesnik@redhat.com> - 0.010-10
- Perl 5.28 rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.010-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.010-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Mon Jun 05 2017 Jitka Plesnikova <jplesnik@redhat.com> - 0.010-7
- Perl 5.26 rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.010-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon May 16 2016 Jitka Plesnikova <jplesnik@redhat.com> - 0.010-5
- Perl 5.24 rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.010-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.010-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Jun 06 2015 Jitka Plesnikova <jplesnik@redhat.com> - 0.010-2
- Perl 5.22 rebuild

* Fri Mar 27 2015 Paul Howarth <paul@city-fan.org> - 0.010-1
- Update to 0.010
  - Relax minimum perl to 5.6 since it runs fine in LMU on 5.6
  - Add POD sections for author, support, copyright, ...
  - Fix tests for $] < 5.008

* Tue Jan  6 2015 Paul Howarth <paul@city-fan.org> - 0.008-1
- Update to 0.008
  - Reflect CPAN RT#100805 recommendation in LICENSE

* Mon Dec 15 2014 Paul Howarth <paul@city-fan.org> - 0.007-1
- Update to 0.007
  - Add GPL-1 license text as it's fulfilling basic requirements

* Tue Dec  9 2014 Paul Howarth <paul@city-fan.org> - 0.006-1
- Update to 0.006
  - Improve Kwalitee
  - Deploy correct licenses
  - Rewrite Changes according to CPAN::Changes::Spec
  - Add rough documentation in Pod
- This release by REHSACK → update source URL

* Thu Aug 28 2014 Jitka Plesnikova <jplesnik@redhat.com> - 0.005-4
- Perl 5.20 rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.005-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Mon Apr  7 2014 Paul Howarth <paul@city-fan.org> - 0.005-2
- Sanitize for Fedora submission

* Mon Mar 24 2014 Paul Howarth <paul@city-fan.org> - 0.005-1
- Update to 0.005
  - Make a test from more detailed example in 0.004
- Package upstream's new README file
- BR: perl(List::Util) for new test
- Update patch for building with Test::More < 0.88

* Sun Mar 23 2014 Paul Howarth <paul@city-fan.org> - 0.004-1
- Update to 0.004
  - Improve the docs with a more detailed example

* Fri Mar 21 2014 Paul Howarth <paul@city-fan.org> - 0.003-1
- Initial RPM version
