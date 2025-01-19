Name:       perl-Archive-RPM
Version:    0.07
Release:    38%{?dist}
Summary:    Work with a RPM
# lib/Archive/RPM.pm -> LGPL-2.1-or-later
# lib/Archive/RPM/ChangeLogEntry.pm -> LGPL-2.1-or-later
License:    LGPL-2.1-or-later
Url:        https://metacpan.org/release/Archive-RPM
Source:     https://cpan.metacpan.org/authors/id/R/RS/RSRCHBOY/Archive-RPM-%{version}.tar.gz
# Restore compatibility with Moose > 2.1005, bug #1168859, CPAN RT#100701
Patch0:     Archive-RPM-0.07-Inject-RPM2-Headers-into-INC-for-Moose-2.1005.patch
# Adjust method delegation filter to Moose-2.1900, bug #1420330, CPAN RT#120270
Patch1:     Archive-RPM-0.07-Adjust-to-Moose-2.1900.patch
BuildArch:  noarch
BuildRequires:  coreutils
BuildRequires:  findutils
BuildRequires:  make
BuildRequires:  perl-interpreter
BuildRequires:  perl-generators
BuildRequires:  perl(inc::Module::Install)
BuildRequires:  perl(Module::Install::AutoInstall)
BuildRequires:  perl(Module::Install::External)
# Module::Install::ExtraTests not helpful
BuildRequires:  perl(Module::Install::GithubMeta)
BuildRequires:  perl(Module::Install::Metadata)
BuildRequires:  perl(Module::Install::ReadmeFromPod)
BuildRequires:  perl(Module::Install::ReadmeMarkdownFromPod)
BuildRequires:  perl(Module::Install::WriteAll)
BuildRequires:  sed
# Run-time:
BuildRequires:  cpio
BuildRequires:  perl(DateTime)
BuildRequires:  perl(English)
BuildRequires:  perl(File::Temp)
BuildRequires:  perl(Moose)
BuildRequires:  perl(MooseX::AttributeHelpers)
BuildRequires:  perl(MooseX::MarkAsMethods)
BuildRequires:  perl(MooseX::Traits)
BuildRequires:  perl(MooseX::Types::DateTimeX)
BuildRequires:  perl(MooseX::Types::Path::Class)
BuildRequires:  perl(overload)
BuildRequires:  perl(Path::Class)
BuildRequires:  perl(RPM2) >= 0.67
BuildRequires:  rpm
# Tests:
BuildRequires:  perl(FindBin)
BuildRequires:  perl(strict)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(warnings)
Requires:       cpio
Requires:       perl(MooseX::Traits)
Requires:       rpm
Obsoletes:      perl-Archive-RPM-tests < 0.07-9

%{?perl_default_filter}

%description
Archive::RPM provides a more complete method of accessing an RPM's meta-
and actual data. We access this information by leveraging RPM2 where we
can, and by "exploding" the rpm with rpm2cpio and cpio when we need
information we can't get through RPM2.

%prep
%setup -q -n Archive-RPM-%{version}
%patch -P0 -p1
%patch -P1 -p1
# Remove bundled modules
rm -r ./inc
sed -i -e '/^inc\//d' MANIFEST
# Remove useless dependency, CPAN RT#100703
sed -i -e "/^requires 'MooseX::Types::DateTime';\$/d" Makefile.PL
# Disable authors tests
sed -i -e '/^extra_tests;$/d' Makefile.PL

%build
perl Makefile.PL INSTALLDIRS=vendor
make %{?_smp_mflags}

%install
make pure_install DESTDIR=%{buildroot}
find %{buildroot} -type f -name .packlist -delete
%{_fixperms} %{buildroot}/*

%check
make test

%files
%doc Changes README
%{perl_vendorlib}/*
%{_mandir}/man3/*.3*

%changelog
* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.07-38
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.07-37
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.07-36
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.07-35
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.07-34
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.07-33
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.07-32
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed Jun 01 2022 Jitka Plesnikova <jplesnik@redhat.com> - 0.07-31
- Perl 5.36 rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.07-30
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.07-29
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Sat May 22 2021 Jitka Plesnikova <jplesnik@redhat.com> - 0.07-28
- Perl 5.34 rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.07-27
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.07-26
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jun 23 2020 Jitka Plesnikova <jplesnik@redhat.com> - 0.07-25
- Perl 5.32 rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.07-24
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.07-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri May 31 2019 Jitka Plesnikova <jplesnik@redhat.com> - 0.07-22
- Perl 5.30 rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.07-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.07-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Sat Jun 30 2018 Jitka Plesnikova <jplesnik@redhat.com> - 0.07-19
- Perl 5.28 rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.07-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.07-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Tue Jun 06 2017 Jitka Plesnikova <jplesnik@redhat.com> - 0.07-16
- Perl 5.26 rebuild

* Thu Feb 16 2017 Petr Pisar <ppisar@redhat.com> - 0.07-15
- Adjust method delegation filter to Moose-2.1900 (bug #1420330)

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.07-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon May 16 2016 Jitka Plesnikova <jplesnik@redhat.com> - 0.07-13
- Perl 5.24 rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.07-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.07-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Mon Jun 08 2015 Jitka Plesnikova <jplesnik@redhat.com> - 0.07-10
- Perl 5.22 rebuild

* Thu Dec 04 2014 Petr Pisar <ppisar@redhat.com> - 0.07-9
- Restore compatibility with Moose > 2.1005 (bug #1168859)
- Specify all dependencies
- Disable tests sub-package

* Mon Sep 01 2014 Jitka Plesnikova <jplesnik@redhat.com> - 0.07-8
- Perl 5.20 rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.07-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Mon Aug 05 2013 Petr Pisar <ppisar@redhat.com> - 0.07-6
- Perl 5.18 rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.07-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.07-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.07-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sat Jun 23 2012 Petr Pisar <ppisar@redhat.com> - 0.07-2
- Perl 5.16 rebuild

* Mon Jan 30 2012 Petr Šabata <contyk@redhat.com> - 0.07-1
- 0.07 bump

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.06-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Thu Jul 21 2011 Petr Sabata <contyk@redhat.com> - 0.06-5
- Perl mass rebuild

* Tue Jul 19 2011 Petr Sabata <contyk@redhat.com> - 0.06-4
- Perl mass rebuild

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.06-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Wed Dec 15 2010 Marcela Maslanova <mmaslano@redhat.com> - 0.06-2
- 661697 rebuild for fixing problems with vendorach/lib

* Fri Jun 18 2010 Petr Pisar <ppisar@redhat.com> - 0.06-1
- Update dependencies (bug #599859)
- Reorder spec headers

* Thu Apr 29 2010 Marcela Maslanova <mmaslano@redhat.com> - 0.05-2
- Mass rebuild with perl-5.12.0

* Sat Feb 13 2010 Chris Weyl <cweyl@alumni.drew.edu> 0.05-1
- update to 0.05

* Sat Feb 13 2010 Chris Weyl <cweyl@alumni.drew.edu> 0.04-5
- PERL_INSTALL_ROOT => DESTDIR
- add perl_default_subpackage_tests

* Wed Jan 20 2010 Chris Weyl <cweyl@alumni.drew.edu> 0.04-4
- auto-update to 0.04 (by cpan-spec-update 0.01)
- added a new br on CPAN (inc::Module::AutoInstall found)
- added a new req on perl(DateTime) (version 0)
- added a new req on perl(Moose) (version 0)
- added a new req on perl(MooseX::AttributeHelpers) (version 0)
- added a new req on perl(MooseX::Types::DateTime) (version 0)
- added a new req on perl(MooseX::Types::Path::Class) (version 0)
- added a new req on perl(Path::Class) (version 0)
- added a new req on perl(RPM2) (version 0.67)
- added a new req on perl(namespace::clean) (version 0)

* Mon Dec  7 2009 Stepan Kasal <skasal@redhat.com> - 0.04-3
- rebuild against perl 5.10.1

* Sat Jul 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.04-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Sun Apr 26 2009 Chris Weyl <cweyl@alumni.drew.edu> 0.04-1
- update to 0.04

* Sun Mar 08 2009 Chris Weyl <cweyl@alumni.drew.edu> 0.03-1
- submission

* Sun Mar 08 2009 Chris Weyl <cweyl@alumni.drew.edu> 0.03-0
- initial RPM packaging
- generated with cpan2dist (CPANPLUS::Dist::RPM version 0.0.8)
