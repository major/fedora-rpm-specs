Name:		perl-Module-Extract-VERSION
Version:	1.118
Release:	1%{?dist}
Summary:	Extract a module version without running code
License:	Artistic-2.0
URL:		https://metacpan.org/release/Module-Extract-VERSION
Source0:	https://cpan.metacpan.org/modules/by-module/Module/Module-Extract-VERSION-%{version}.tar.gz
BuildArch:	noarch
# Module Build
BuildRequires:	coreutils
BuildRequires:	findutils
BuildRequires:	make
BuildRequires:	perl-generators
BuildRequires:	perl-interpreter
BuildRequires:	perl(:VERSION) >= 5.10.0
BuildRequires:	perl(ExtUtils::MakeMaker) >= 6.64
BuildRequires:	perl(File::Spec)
BuildRequires:	perl(File::Spec::Functions)
# Module Runtime
BuildRequires:	perl(Carp)
BuildRequires:	perl(Safe)
BuildRequires:	perl(strict)
BuildRequires:	perl(version)
BuildRequires:	perl(warnings)
# Test Suite
BuildRequires:	perl(Test::More) >= 1
# Optional Tests
BuildRequires:	perl(Test::Manifest) >= 1.21
BuildRequires:	perl(Test::Pod) >= 1.00
BuildRequires:	perl(Test::Pod::Coverage) >= 1.00
# Dependencies
Requires:	perl(Safe)
Requires:	perl(version)

%description
This module lets you pull out of module source code the version number for the
module. It assumes that there is only one $VERSION in the file.

%prep
%setup -q -n Module-Extract-VERSION-%{version}

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
%doc Changes README.pod SECURITY.md
%{perl_vendorlib}/Module/
%{_mandir}/man3/Module::Extract::VERSION.3*

%changelog
* Wed Jan 22 2025 Paul Howarth <paul@city-fan.org> - 1.118-1
- Update to 1.118
  - Refresh dist
- Package new SECURITY.md file

* Sat Jan 18 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.117-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.117-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Sun Feb 11 2024 Paul Howarth <paul@city-fan.org> - 1.117-1
- Update to 1.117
  - Refresh distro, update email address, move to BRIANDFOY

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.116-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.116-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.116-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.116-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Tue Oct 25 2022 Paul Howarth <paul@city-fan.org> - 1.116-1
- Update to 1.116
  - Fix problem with Safe compartment: don't import version:: since Safe
    already does that (GH#16)
- Use SPDX-format license tag

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.115-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Tue May 31 2022 Jitka Plesnikova <jplesnik@redhat.com> - 1.115-3
- Perl 5.36 rebuild

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.115-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Sun Jan  9 2022 Paul Howarth <paul@city-fan.org> - 1.115-1
- Update to 1.115
  - Fix link in README.pod

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.114-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri May 21 2021 Jitka Plesnikova <jplesnik@redhat.com> - 1.114-3
- Perl 5.34 rebuild

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.114-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Thu Jan 21 2021 Paul Howarth <paul@city-fan.org> - 1.114-1
- Update to 1.114
  - Freshen distro, dump Travis CI, add GitHub Actions

* Tue Jan  5 2021 Paul Howarth <paul@city-fan.org> - 1.113-14
- Use author-independent source URL

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.113-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jun 23 2020 Jitka Plesnikova <jplesnik@redhat.com> - 1.113-12
- Perl 5.32 rebuild

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.113-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.113-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri May 31 2019 Jitka Plesnikova <jplesnik@redhat.com> - 1.113-9
- Perl 5.30 rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.113-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.113-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Jun 28 2018 Jitka Plesnikova <jplesnik@redhat.com> - 1.113-6
- Perl 5.28 rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.113-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.113-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Mon Jun 05 2017 Jitka Plesnikova <jplesnik@redhat.com> - 1.113-3
- Perl 5.26 rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.113-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Dec  7 2016 Paul Howarth <paul@city-fan.org> - 1.113-1
- Update to 1.113
  - Fix a Perl 5.8 issue with Makefile.PL, even though the module requires
    Perl 5.10

* Tue Dec  6 2016 Paul Howarth <paul@city-fan.org> - 1.112-1
- Update to 1.112
  - Remove prereq.t test; upstream will do that locally
  - Hide some packages from PAUSE
- License changed to Artistic 2.0

* Tue Oct 18 2016 Paul Howarth <paul@city-fan.org> - 1.111-1
- Update to 1.111
  - Use a safe compartment
  - Require Perl 5.10 so named captures can be used
  - Support v5.12 and v5.14 PACKAGE NAMESPACE VERSION BLOCK
- Modernize spec since requirements not available on old distributions
- Drop now-redundant provides filter

* Fri Jul 22 2016 Petr Pisar <ppisar@redhat.com> - 1.01-17
- Adjust RPM version detection to SRPM build root without perl

* Sun May 15 2016 Jitka Plesnikova <jplesnik@redhat.com> - 1.01-16
- Perl 5.24 rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.01-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Sun Jan  3 2016 Paul Howarth <paul@city-fan.org> - 1.01-14
- Get rid of %%define
- Drop %%defattr, redundant since rpm 4.4
- Use %%license where possible
- Classify buildreqs by usage
- Don't need to remove empty directories from the buildroot
- Use DESTDIR rather than PERL_INSTALL_ROOT

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.01-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Fri Jun 12 2015 Jitka Plesnikova <jplesnik@redhat.com> - 1.01-12
- Perl 5.22 rebuild

* Thu Aug 28 2014 Jitka Plesnikova <jplesnik@redhat.com> - 1.01-11
- Perl 5.20 rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.01-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.01-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Sun Jul 21 2013 Petr Pisar <ppisar@redhat.com> - 1.01-8
- Perl 5.18 rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.01-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.01-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Wed Jun 13 2012 Petr Pisar <ppisar@redhat.com> - 1.01-5
- Perl 5.16 rebuild

* Thu Jan 12 2012 Paul Howarth <paul@city-fan.org> - 1.01-4
- BR: perl(Carp)

* Fri Aug 12 2011 Paul Howarth <paul@city-fan.org> - 1.01-3
- Filter bogus provide for perl(ExtUtils::MakeMaker::_version) (#728286)

* Thu Aug  4 2011 Paul Howarth <paul@city-fan.org> - 1.01-2
- Sanitize for Fedora submission

* Wed Aug  3 2011 Paul Howarth <paul@city-fan.org> - 1.01-1
- Initial RPM version
