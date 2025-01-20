Name:           perl-Module-Starter-Plugin-CGIApp
Version:        0.44
Release:        30%{?dist}
Summary:        Template based module starter for CGI apps
# Automatically converted from old format: GPL+ or Artistic - review is highly recommended.
License:        GPL-1.0-or-later OR Artistic-1.0-Perl

URL:            https://metacpan.org/release/Module-Starter-Plugin-CGIApp
Source0:        https://cpan.metacpan.org/authors/id/J/JA/JALDHAR/Module-Starter-Plugin-CGIApp-%{version}.tar.gz
# https://github.com/jaldhar/Module-Starter-Plugin-CGIApp/pull/3
Patch0:         Module-Starter-Plugin-CGIApp-0.44-starter.patch
BuildArch:      noarch
buildrequires:  findutils
buildrequires:  perl-generators
buildrequires:  perl-interpreter
BuildRequires:  perl(base)
BuildRequires:  perl(blib)
BuildRequires:  perl(Carp)
BuildRequires:  perl(Cwd)
BuildRequires:  perl(English)
BuildRequires:  perl(File::Copy::Recursive)
BuildRequires:  perl(File::DirCompare)
BuildRequires:  perl(File::Find)
BuildRequires:  perl(File::Path)
BuildRequires:  perl(File::ShareDir)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(HTML::Template)
BuildRequires:  perl(Module::Build)
BuildRequires:  perl(Module::Signature)
BuildRequires:  perl(Module::Starter) >= 1.71
BuildRequires:  perl(Module::Starter::App)
BuildRequires:  perl(Pod::Coverage) >= 0.18
BuildRequires:  perl(strict)
BuildRequires:  perl(Test::Builder)
BuildRequires:  perl(Test::MockTime)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Test::Pod) >= 1.22
BuildRequires:  perl(Test::Pod::Coverage)
BuildRequires:  perl(Test::WWW::Mechanize::CGIApp)
BuildRequires:  perl(Time::Piece)
BuildRequires:  perl(Titanium)
BuildRequires:  perl(vars)
BuildRequires:  perl(warnings)
Requires:       perl(Module::Starter) >= 1.71

%{?perl_default_filter}
# Remove under-specified dependencies:
%global __requires_exclude %{?__requires_exclude:%__requires_exclude|}^perl\\(Module::Starter\\)$

%description
This is a plugin for Module::Starter that builds you a skeleton
CGI::Application module with all the extra files needed to package it for
CPAN. You can customize the output using HTML::Template.

%prep
%setup -q -n Module-Starter-Plugin-CGIApp-%{version}
%patch -P0 -p1


%build
%{__perl} Build.PL installdirs=vendor
./Build

%install
./Build install --destdir $RPM_BUILD_ROOT  create_packlist=0
find $RPM_BUILD_ROOT -depth -type d -exec rmdir {} 2>/dev/null \;

%{_fixperms} $RPM_BUILD_ROOT/*

%check
%{?!_with_signature_test:rm t/00-signature.t}
./Build test

%files
%doc Changes README
%{perl_vendorlib}/*
%{_bindir}/cgiapp-starter
%{_bindir}/titanium-starter
%{_mandir}/man1/cgiapp-starter.1.gz
%{_mandir}/man1/titanium-starter.1.gz
%{_mandir}/man3/*

%changelog
* Sat Jan 18 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.44-30
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Tue Aug 06 2024 Miroslav Suchý <msuchy@redhat.com> - 0.44-29
- convert license to SPDX

* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.44-28
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.44-27
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.44-26
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.44-25
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.44-24
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.44-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed Jun 01 2022 Jitka Plesnikova <jplesnik@redhat.com> - 0.44-22
- Perl 5.36 rebuild

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.44-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.44-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Sun May 23 2021 Jitka Plesnikova <jplesnik@redhat.com> - 0.44-19
- Perl 5.34 rebuild

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.44-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.44-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Jun 25 2020 Jitka Plesnikova <jplesnik@redhat.com> - 0.44-16
- Perl 5.32 rebuild

* Wed Mar 18 2020 Jitka Plesnikova <jplesnik@redhat.com> - 0.44-15
- Specify all dependencies

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.44-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.44-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri May 31 2019 Jitka Plesnikova <jplesnik@redhat.com> - 0.44-12
- Perl 5.30 rebuild

* Sun Mar 24 2019 Emmanuel Seyman <emmanuel@seyman.fr> - 0.44-11
- Add patch by ppisar to adapt to changes in Module-Starter-1.76 (#1690313)

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.44-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.44-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Sat Jun 30 2018 Jitka Plesnikova <jplesnik@redhat.com> - 0.44-8
- Perl 5.28 rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.44-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.44-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Tue Jun 06 2017 Jitka Plesnikova <jplesnik@redhat.com> - 0.44-5
- Perl 5.26 rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.44-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Tue May 17 2016 Jitka Plesnikova <jplesnik@redhat.com> - 0.44-3
- Perl 5.24 rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.44-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Sun Sep 27 2015 Emmanuel Seyman <emmanuel@seyman.fr> - 0.44-1
- Update to 0.44
- Remove partially-upstreamed patch

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.42-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Mon Jun 08 2015 Jitka Plesnikova <jplesnik@redhat.com> - 0.42-10
- Perl 5.22 rebuild

* Thu May 07 2015 Petr Pisar <ppisar@redhat.com> - 0.42-9
- Adapt to changes in Module-Starter-1.71 (bug #1189463)

* Mon Sep 01 2014 Jitka Plesnikova <jplesnik@redhat.com> - 0.42-8
- Perl 5.20 rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.42-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Thu Aug 08 2013 Petr Pisar <ppisar@redhat.com> - 0.42-6
- Perl 5.18 rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.42-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.42-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.42-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Mon Jul 02 2012 Petr Pisar <ppisar@redhat.com> - 0.42-2
- Perl 5.16 rebuild

* Thu May 17 2012 Emmanuel Seyman <emmanuel.seyman@club-internet.fr> - 0.42-1
- Update to 0.42

* Sat May 12 2012 Emmanuel Seyman <emmanuel.seyman@club-internet.fr> - 0.41-1
- Update to 0.41
- Clean up spec file
- Add perl default filter

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.30-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Jul 19 2011 Petr Sabata <contyk@redhat.com> - 0.30-6
- Perl mass rebuild

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.30-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Mon Dec 20 2010 Marcela Maslanova <mmaslano@redhat.com> - 0.30-4
- 661697 rebuild for fixing problems with vendorach/lib

* Thu Dec 09 2010 Ralf Corsépius <corsepiu@fedoraproject.org> - 0.30-3
- Pass vendordirs to Build.PL (Fix FTBFS: BZ 661044).

* Mon Jul 26 2010 Emmanuel Seyman <emmanuel.seyman@club-internet.fr> - 0.30-2
- Re-enable tests

* Tue May 11 2010 Emmanuel Seyman <emmanuel.seyman@club-internet.fr> - 0.30-1
- Update to 0.30.
- Disable tests due to incompatibility with rpmlint.
- Switch to Build.PL

* Mon May 03 2010 Marcela Maslanova <mmaslano@redhat.com> - 0.10-5
- Mass rebuild with perl-5.12.0

* Mon Feb 15 2010 Emmanuel Seyman <emmanuel.seyman@club-internet.fr> - 0.10-4
- Add missing Build-Requires
- Fix build instructions so they actually work (#555507)

* Mon Dec  7 2009 Stepan Kasal <skasal@redhat.com> - 0.10-3
- rebuild against perl 5.10.1

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.10-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Mon Jun 15 2009 Emmanuel Seyman <emmanuel.seyman@club-internet.fr> 0.10-1
- Specfile autogenerated by cpanspec 1.77.
