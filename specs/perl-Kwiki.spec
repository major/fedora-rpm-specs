Name:           perl-Kwiki
Version:        0.39
Release:        54%{?dist}
Summary:        Kwiki Wiki Building Framework
# Automatically converted from old format: GPL+ or Artistic - review is highly recommended.
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Kwiki
Source0:        https://cpan.metacpan.org/authors/id/I/IN/INGY/Kwiki-%{version}.tar.gz
Patch0:         Kwiki-0.39-Fix-building-on-Perl-without-dot-in-INC.patch
BuildArch:      noarch
# Build
BuildRequires: make
BuildRequires:  perl-interpreter
BuildRequires:  perl-generators
BuildRequires:  perl(Config)
BuildRequires:  perl(Cwd)
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
BuildRequires:  perl(ExtUtils::MM_Unix)
BuildRequires:  perl(File::Basename)
BuildRequires:  perl(File::Find)
BuildRequires:  perl(File::Path)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(strict)
BuildRequires:  perl(vars)
# Runtime
BuildRequires:  perl(base)
# XXX: BuildRequires:  perl(CPAN)
BuildRequires:  perl(HTTP::BrowserDetect)
# This is actually Spiffy::mixin, the namespace is loaded via Spoon::Config
# XXX: BuildRequires:  perl(mixin)
BuildRequires:  perl(Spoon) >= 0.22
BuildRequires:  perl(Spoon::Base)
BuildRequires:  perl(Spoon::CGI)
BuildRequires:  perl(Spoon::Command)
BuildRequires:  perl(Spoon::Config)
BuildRequires:  perl(Spoon::ContentObject)
BuildRequires:  perl(Spoon::Cookie)
BuildRequires:  perl(Spoon::Formatter)
BuildRequires:  perl(Spoon::Formatter::Block)
BuildRequires:  perl(Spoon::Formatter::Container)
BuildRequires:  perl(Spoon::Formatter::Phrase)
BuildRequires:  perl(Spoon::Formatter::Unit)
BuildRequires:  perl(Spoon::Hub)
BuildRequires:  perl(Spoon::Installer)
BuildRequires:  perl(Spoon::MetadataObject)
BuildRequires:  perl(Spoon::Plugin)
BuildRequires:  perl(Spoon::Registry)
BuildRequires:  perl(Spoon::Template)
BuildRequires:  perl(Spoon::Template::TT2)
BuildRequires:  perl(warnings)
# Tests only
BuildRequires:  perl(IO::All)
BuildRequires:  perl(lib)
BuildRequires:  perl(Spiffy)
BuildRequires:  perl(Test::More)
# Optional tests only
BuildRequires:  perl(Test::Memory::Cycle)
Requires:       perl(CPAN)
Requires:       perl(Cwd)

# This is actually Spiffy::mixin; it's all rather obscure
%global __requires_exclude %{?__requires_exclude:__requires_exclude|}^perl\\(mixin\\)$

%description
A Wiki is a website that allows its users to add pages, and edit any
existing pages. It is one of the most popular forms of web collaboration.
If you are new to wiki, visit http://c2.com/cgi/wiki?WelcomeVisitors
which is possibly the oldest wiki, and has lots of information about how
wikis work.

Kwiki is a Perl wiki implementation based on the Spoon application
architecture and using the Spiffy object orientation model. The major goals
of Kwiki are that it be easy to install, maintain and extend.

All the features of a Kwiki wiki come from plugin modules. The base
installation comes with the bare minimum plugins to make a working Kwiki.
To make a really nice Kwiki installation you need to install additional
plugins. Which plugins you pick is entirely up to you. Another goal of
Kwiki is that every installation will be unique. When there are hundreds of
plugins available, this will hopefully be the case.

%prep
%setup -q -n Kwiki-%{version}
%patch -P0 -p1

%build
perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1
make %{?_smp_mflags}

%install
make pure_install DESTDIR=%{buildroot}
%{_fixperms} %{buildroot}/*

%check
make test

%files
%doc Changes README
%{perl_vendorlib}/*
%{_bindir}/*
%{_mandir}/man1/*
%{_mandir}/man3/*

%changelog
* Sat Jan 18 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.39-54
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Tue Aug 06 2024 Miroslav Suchý <msuchy@redhat.com> - 0.39-53
- convert license to SPDX

* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.39-52
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.39-51
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.39-50
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.39-49
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.39-48
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.39-47
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed Jun 01 2022 Jitka Plesnikova <jplesnik@redhat.com> - 0.39-46
- Perl 5.36 rebuild

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.39-45
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.39-44
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Sat May 22 2021 Jitka Plesnikova <jplesnik@redhat.com> - 0.39-43
- Perl 5.34 rebuild

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.39-42
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.39-41
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jun 23 2020 Jitka Plesnikova <jplesnik@redhat.com> - 0.39-40
- Perl 5.32 rebuild

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.39-39
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.39-38
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri May 31 2019 Jitka Plesnikova <jplesnik@redhat.com> - 0.39-37
- Perl 5.30 rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.39-36
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.39-35
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Jun 29 2018 Jitka Plesnikova <jplesnik@redhat.com> - 0.39-34
- Perl 5.28 rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.39-33
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.39-32
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Tue Jun 06 2017 Jitka Plesnikova <jplesnik@redhat.com> - 0.39-31
- Perl 5.26 rebuild

* Thu May 18 2017 Jitka Plesnikova <jplesnik@redhat.com> - 0.39-30
- Fix building on Perl without '.' in @INC

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.39-29
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon May 16 2016 Jitka Plesnikova <jplesnik@redhat.com> - 0.39-28
- Perl 5.24 rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.39-27
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.39-26
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Jun 06 2015 Jitka Plesnikova <jplesnik@redhat.com> - 0.39-25
- Perl 5.22 rebuild

* Wed Apr 01 2015 Petr Šabata <contyk@redhat.com> - 0.39-24
- Drop the erroneous dependency; CPAN::Config isn't a real package

* Tue Mar 31 2015 Petr Šabata <contyk@redhat.com> - 0.39-23
- Modernize the spec and correct the dep list

* Fri Aug 29 2014 Jitka Plesnikova <jplesnik@redhat.com> - 0.39-22
- Perl 5.20 rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.39-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.39-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Tue Jul 30 2013 Petr Pisar <ppisar@redhat.com> - 0.39-19
- Perl 5.18 rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.39-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.39-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Thu Jun 21 2012 Petr Pisar <ppisar@redhat.com> - 0.39-16
- Perl 5.16 rebuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.39-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Fri Jul 22 2011 Petr Sabata <contyk@redhat.com> - 0.39-14
- RPM 4.9 dependency filtering added
- BuildRequire IO::All

* Tue Jul 19 2011 Petr Sabata <contyk@redhat.com> - 0.39-13
- Perl mass rebuild

* Wed Feb 16 2011 Ralf Corsépius <corsepiu@fedoraproject.org> - 0.39-12
- Revert temporary hack "BR: perl-IO-All" (Not required anymore).

* Tue Feb 15 2011 Ralf Corsépius <corsepiu@fedoraproject.org> - 0.39-11
- Switch to using perl-filters/Abandon filter-requires.sh
  (Work around broken deps caused by rpm dep-tracker changes).
- BR: perl-IO-All, to assure getting the right perl(IO::All)
  (was bogusly provided by perl-Spoon-0.24-9).

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.39-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Mon Dec 20 2010 Marcela Maslanova <mmaslano@redhat.com> - 0.39-9
- 661697 rebuild for fixing problems with vendorach/lib

* Sun May 02 2010 Marcela Maslanova <mmaslano@redhat.com> - 0.39-8
- Mass rebuild with perl-5.12.0

* Mon Dec  7 2009 Stepan Kasal <skasal@redhat.com> - 0.39-7
- rebuild against perl 5.10.1

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.39-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Thu Feb 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.39-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Thu Feb 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.39-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Wed Mar 05 2008 Tom "spot" Callaway <tcallawa@redhat.com> 0.39-3
- rebuild for new perl

* Fri Jan 04 2008 Ralf Corsépius <rc040203@freenet.de> 0.39-2
- Update License-tag.
- BR: perl(Test::Memory::Cycle).
- BR: perl(Test::More) (BZ 419631).

* Tue Mar 13 2007 Steven Pritchard <steve@kspei.com> 0.39-1
- Update to 0.39.
- Use fixperms macro instead of our own chmod incantation.
- BR ExtUtils::MakeMaker.

* Mon Sep 04 2006 Steven Pritchard <steve@kspei.com> 0.38-4
- Cleanup to more closely resemble current cpanspec output.
- kwiki is a program, not documentation.

* Fri Mar 10 2006 Steven Pritchard <steve@kspei.com> 0.38-3
- Improve Summary.
- Fix up dependency filtering.

* Mon Feb 27 2006 Steven Pritchard <steve@kspei.com> 0.38-2
- Drop explicit BR: perl.
- Filter perl(mixin) dependency.

* Wed Dec 28 2005 Steven Pritchard <steve@kspei.com> 0.38-1
- Specfile autogenerated.
