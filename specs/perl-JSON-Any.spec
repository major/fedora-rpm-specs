Name:           perl-JSON-Any
Summary:        A meta-module to make working with JSON easier
Version:        1.40
Release:        5%{?dist}
License:        GPL-1.0-or-later OR Artistic-1.0-Perl

Source0:        https://cpan.metacpan.org/authors/id/E/ET/ETHER/JSON-Any-%{version}.tar.gz

URL:            https://metacpan.org/release/JSON-Any
BuildArch:      noarch

BuildRequires:  coreutils
BuildRequires:  findutils
BuildRequires:  make
BuildRequires:  perl-generators
BuildRequires:  perl(Carp)
BuildRequires:  perl(CPAN)
BuildRequires:  perl(Cpanel::JSON::XS)
BuildRequires:  perl(Data::Dumper)
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
BuildRequires:  perl(JSON)
# Not in Fedora
# BuildRequires:  perl(JSON::DWIW)
BuildRequires:  perl(JSON::MaybeXS)
BuildRequires:  perl(JSON::PP)
BuildRequires:  perl(JSON::Syck)
BuildRequires:  perl(JSON::XS) >= 1.52
BuildRequires:  perl(namespace::clean)
BuildRequires:  perl(Storable)
BuildRequires:  perl(Test::Fatal)
BuildRequires:  perl(Test::More) >= 0.42
BuildRequires:  perl(Test::Needs)
BuildRequires:  perl(Test::Requires)
BuildRequires:  perl(Test::Warnings)
BuildRequires:  perl(Test::Without::Module)

Requires:       perl(Carp)
Requires:       perl(JSON::XS) >= 1.52

%{?perl_default_filter}
%{?perl_default_subpackage_tests}

%description
JSON::Any provides a coherent API to bring together the various JSON modules
currently on CPAN.

%prep
%setup -q -n JSON-Any-%{version}
find .  -type f -exec chmod -c -x {} +

%build
/usr/bin/perl Makefile.PL NO_PACKLIST=1 NO_PERLLOCAL=1 INSTALLDIRS=vendor --default
%{make_build}

%install
%{make_install}
%{_fixperms} %{buildroot}/*

%check
%{make_build} test

%files
%doc Changes README
%{perl_vendorlib}/JSON*
%{_mandir}/man3/JSON*

%changelog
* Sat Jan 18 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.40-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.40-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.40-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.40-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Mon Sep 11 2023 Emmanuel Seyman <emmanuel@seyman.fr> - 1.40-1
- Update to 1.40
- migrated to SPDX license
- Remove patches (no longer needed)
- Use /usr/bin/perl instead of %%{__perl}
- Use %%{make_build} and %%{make_install} where appropriate

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.39-25
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.39-24
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.39-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed Jun 01 2022 Jitka Plesnikova <jplesnik@redhat.com> - 1.39-22
- Perl 5.36 rebuild

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.39-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.39-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri May 21 2021 Jitka Plesnikova <jplesnik@redhat.com> - 1.39-19
- Perl 5.34 rebuild

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.39-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.39-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jun 23 2020 Jitka Plesnikova <jplesnik@redhat.com> - 1.39-16
- Perl 5.32 rebuild

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.39-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.39-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri May 31 2019 Jitka Plesnikova <jplesnik@redhat.com> - 1.39-13
- Perl 5.30 rebuild

* Mon Feb 04 2019 Petr Pisar <ppisar@redhat.com> - 1.39-12
- Adapt to changes in JSON-XS-4.0 (CPAN RT#127753)

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.39-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.39-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Jun 29 2018 Jitka Plesnikova <jplesnik@redhat.com> - 1.39-9
- Perl 5.28 rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.39-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.39-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Mon Jun 05 2017 Jitka Plesnikova <jplesnik@redhat.com> - 1.39-6
- Perl 5.26 rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.39-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon May 16 2016 Jitka Plesnikova <jplesnik@redhat.com> - 1.39-4
- Perl 5.24 rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.39-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.39-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Fri Jun 12 2015 Emmanuel Seyman <emmanuel@seyman.fr> - 1.39-1
- Update to 1.39
- Tighten file listing
- Tidy up spec file

* Sat Jun 06 2015 Jitka Plesnikova <jplesnik@redhat.com> - 1.38-2
- Perl 5.22 rebuild

* Sun Oct 05 2014 Emmanuel Seyman <emmanuel@seyman.fr> - 1.38-1
- Update to 1.38

* Wed Sep 03 2014 Jitka Plesnikova <jplesnik@redhat.com> - 1.36-2
- Perl 5.20 rebuild

* Sun Aug 31 2014 Emmanuel Seyman <emmanuel@seyman.fr> - 1.36-1
- Update to 1.36

* Fri Aug 29 2014 Jitka Plesnikova <jplesnik@redhat.com> - 1.35-2
- Perl 5.20 rebuild

* Sun Aug 17 2014 Emmanuel Seyman <emmanuel@seyman.fr> - 1.35-1
- Update to 1.35
- Drop Group (no longer used)

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.34-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Jun 01 2014 Emmanuel Seyman <emmanuel@seyman.fr> - 1.34-1
- Update to 1.34

* Sun Apr 20 2014 Emmanuel Seyman <emmanuel@seyman.fr> - 1.33-1
- Update to 1.33

* Sun Nov 10 2013 Emmanuel Seyman <emmanuel@seyman.fr> - 1.32-1
- Update to 1.32

* Sat Aug 03 2013 Petr Pisar <ppisar@redhat.com> - 1.30-2
- Perl 5.18 rebuild

* Sun Jun 16 2013 Emmanuel Seyman <emmanuel@seyman.fr> - 1.30-1
- Update to 1.30

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.29-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.29-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Wed Jun 20 2012 Petr Pisar <ppisar@redhat.com> - 1.29-2
- Perl 5.16 rebuild
- Specify all dependencies

* Thu Jan 12 2012 Emmanuel Seyman <emmanuel.seyman@club-internet.fr> - 1.29-1
- Update to 1.29
- Remove the defattr macro (no longer used)

* Wed Jul 20 2011 Petr Sabata <contyk@redhat.com> - 1.25-3
- Perl mass rebuild

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.25-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Sun Nov 21 2010 Iain Arnell <iarnell@gmail.com> 1.25-1
- update to latest upstream version
- clean up spec for modern rpmbuild
- restore JSON and JSON::Syck BRs for tests

* Sun May 02 2010 Marcela Maslanova <mmaslano@redhat.com> - 1.22-2
- Mass rebuild with perl-5.12.0

* Tue Feb 23 2010 Chris Weyl <cweyl@alumni.drew.edu> 1.22-1
- update by Fedora::App::MaintainerTools 0.003
- PERL_INSTALL_ROOT => DESTDIR
- dropped old BR on perl(JSON)
- dropped old BR on perl(JSON::Syck)

* Mon Dec  7 2009 Stepan Kasal <skasal@redhat.com> - 1.21-2
- rebuild against perl 5.10.1

* Tue Aug 11 2009 Chris Weyl <cweyl@alumni.drew.edu> 1.21-1
- auto-update to 1.21 (by cpan-spec-update 0.01)
- altered br on perl(ExtUtils::MakeMaker) (0 => 6.42)
- altered br on perl(Test::More) (0.62 => 0.42)
- added a new br on CPAN (inc::Module::AutoInstall found)
- added a new req on perl(Carp) (version 0)

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.19-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Thu Feb 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.19-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Thu Feb 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.19-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Wed Feb 11 2009 Chris Weyl <cweyl@alumni.drew.edu> 1.19-1
- update to 1.19

* Sun Sep 21 2008 Ville Skyttä <ville.skytta at iki.fi> - 1.16-4
- Fix Patch:/%%patch0 mismatch.

* Sat Mar 22 2008 Chris Weyl <cweyl@alumni.drew.edu> 1.16-3
- patch to allow utf8 to work properly with JSON::XS earlier than version 2
- patch to skip JSON when JSON is earlier than version 2

* Wed Mar 12 2008 Chris Weyl <cweyl@alumni.drew.edu> 1.16-2
- bump

* Sun Mar 09 2008 Chris Weyl <cweyl@alumni.drew.edu> 1.16-1
- Specfile autogenerated by cpanspec 1.74.
