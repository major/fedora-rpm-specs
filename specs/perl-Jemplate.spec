%global cpan_version 0.30

Name:       perl-Jemplate 
# Keep 3-digit version for history
Version:    %{cpan_version}0
Release:    29%{?dist}
# lib/Jemplate.pm -> GPL+ or Artistic
# lib/Jemplate/Directive.pm -> GPL+ or Artistic
# lib/Jemplate/Parser.pm -> GPL+ or Artistic
# lib/Jemplate/Runtime.pm -> GPL+ or Artistic
# lib/Jemplate/Runtime/Compact.pm -> GPL+ or Artistic
License:    GPL-1.0-or-later OR Artistic-1.0-Perl
Summary:    JavaScript Templating with Template Toolkit 
Source:     https://cpan.metacpan.org/authors/id/I/IN/INGY/Jemplate-%{cpan_version}.tar.gz 
# Do not prune INC, CPAN RT#87546
Patch0:     Jemplate-0.27-Do-not-prune-INC.patch
Url:        https://metacpan.org/release/Jemplate
BuildArch:  noarch

BuildRequires: make
BuildRequires: perl-interpreter
BuildRequires: perl-generators
BuildRequires: perl(ExtUtils::MakeMaker) >= 6.30
BuildRequires: perl(strict)
# Run-time:
BuildRequires: perl(base)
BuildRequires: perl(bytes)
BuildRequires: perl(Carp)
BuildRequires: perl(Config)
BuildRequires: perl(constant)
BuildRequires: perl(Encode)
BuildRequires: perl(Exporter)
BuildRequires: perl(File::Basename)
BuildRequires: perl(File::Find)
# File::Find::Rule is bundled
BuildRequires: perl(File::Find::Rule) >= 0.33
BuildRequires: perl(File::Path)
BuildRequires: perl(File::Spec)
BuildRequires: perl(File::Temp)
BuildRequires: perl(FindBin)
BuildRequires: perl(Getopt::Long)
# Number::Compare is bundled
BuildRequires: perl(overload)
BuildRequires: perl(Scalar::Util)
BuildRequires: perl(Template) >= 2.25
# Template is bundled
# Template::Base is bundled
# Template::Config is bundled
# Template::Constants is bundled
# Template::Directive is bundled
# Template::Document is bundled
# Template::Exception is bundled
# Template::Grammar is bundled
# Template::Parser is bundled
# Template::Provider is bundled
# Template::Service is bundled
# Template::TieString is bundled
# Text::Glob is bundled
BuildRequires: perl(vars)
BuildRequires: perl(warnings)
# Tests
BuildRequires: perl(HTTP::Daemon)
BuildRequires: perl(HTTP::Response)
BuildRequires: perl(HTTP::Status)
BuildRequires: perl(IO::All)
BuildRequires: perl(JSON)
BuildRequires: perl(lib)
BuildRequires: perl(LWP::MediaTypes)
BuildRequires: perl(Path::Class)
BuildRequires: perl(Pod::Usage)
BuildRequires: perl(Test::Base)
BuildRequires: perl(Test::Base::Filter)
BuildRequires: perl(Test::More)
BuildRequires: perl(YAML)
# Optional tests
#BuildRequires: perl(JavaScript::V8x::TestMoreish)

Requires:   perl(File::Find::Rule) >= 0.33

%description
Jemplate is a templating framework for JavaScript that is built over
Perl's Template Toolkit (TT2). Jemplate parses TT2 templates using the
TT2 Perl framework, but with a twist. Instead of compiling the templates
into Perl code, it compiles them into JavaScript. Jemplate then provides
a JavaScript run-time module for processing the template code. Presto, we
have full featured JavaScript templating language!

%prep
%setup -q -n Jemplate-%{cpan_version}
%patch -P0 -p1
rm -rf inc
sed -i -e '/^inc\//d' MANIFEST

cat doc/text/Jemplate.text | iconv -f iso-8859-1 -t utf-8 > foo
cat foo > doc/text/Jemplate.text
rm foo

%build
perl Makefile.PL INSTALLDIRS=vendor
make %{?_smp_mflags}

%install
make pure_install DESTDIR=%{buildroot}
find %{buildroot} -type f -name .packlist -exec rm -f {} ';'
%{_fixperms} %{buildroot}/*

%check
make test

%files
%doc Changes LICENSE README doc/ examples/ 
%{perl_vendorlib}/*
%{_mandir}/man3/*.3*
%{_bindir}/jemplate
%{_mandir}/man1/jemplate.1.gz

%changelog
* Sat Jan 18 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.300-29
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.300-28
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.300-27
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.300-26
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.300-25
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.300-24
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.300-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed Jun 01 2022 Jitka Plesnikova <jplesnik@redhat.com> - 0.300-22
- Perl 5.36 rebuild

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.300-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.300-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Sat May 22 2021 Jitka Plesnikova <jplesnik@redhat.com> - 0.300-19
- Perl 5.34 rebuild

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.300-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.300-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jun 23 2020 Jitka Plesnikova <jplesnik@redhat.com> - 0.300-16
- Perl 5.32 rebuild

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.300-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.300-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri May 31 2019 Jitka Plesnikova <jplesnik@redhat.com> - 0.300-13
- Perl 5.30 rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.300-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.300-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Jun 29 2018 Jitka Plesnikova <jplesnik@redhat.com> - 0.300-10
- Perl 5.28 rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.300-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.300-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Mon Jun 05 2017 Jitka Plesnikova <jplesnik@redhat.com> - 0.300-7
- Perl 5.26 rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.300-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon May 16 2016 Jitka Plesnikova <jplesnik@redhat.com> - 0.300-5
- Perl 5.24 rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.300-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.300-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Jun 06 2015 Jitka Plesnikova <jplesnik@redhat.com> - 0.300-2
- Perl 5.22 rebuild

* Fri Nov 14 2014 Jitka Plesnikova <jplesnik@redhat.com> - 0.300-1
- 0.30 bump

* Fri Aug 29 2014 Jitka Plesnikova <jplesnik@redhat.com> - 0.270-4
- Perl 5.20 rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.270-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Fri Aug 30 2013 Jitka Plesnikova <jplesnik@redhat.com> - 0.270-2
- Fix the macro.t to work with new Template::Parser

* Fri Aug 02 2013 Petr Pisar <ppisar@redhat.com> - 0.270-1
- 0.27 bump

* Fri Aug 02 2013 Petr Pisar <ppisar@redhat.com> - 0.262-5
- Perl 5.18 rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.262-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.262-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jun 22 2012 Petr Pisar <ppisar@redhat.com> - 0.262-2
- Perl 5.16 rebuild

* Wed Mar 14 2012 Petr Pisar <ppisar@redhat.com> - 0.262-1
- 0.262 bump

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.261-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Wed Jul 20 2011 Petr Sabata <contyk@redhat.com> - 0.261-4
- Perl mass rebuild

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.261-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Mon Dec 20 2010 Marcela Maslanova <mmaslano@redhat.com> - 0.261-2
- 661697 rebuild for fixing problems with vendorach/lib

* Fri Aug  6 2010 Marcela Maslanova <mmaslano@redhat.com> - 0.261-1
- update

* Sun May 02 2010 Marcela Maslanova <mmaslano@redhat.com> - 0.23-6
- Mass rebuild with perl-5.12.0

* Fri Jan 15 2010 Tom "spot" Callaway <tcallawa@redhat.com> - 0.23-5
- fix quoted test to work with newer Template::Toolkit behavior

* Mon Dec  7 2009 Stepan Kasal <skasal@redhat.com> - 0.23-4
- rebuild against perl 5.10.1

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.23-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Sat Mar 28 2009 Chris Weyl <cweyl@alumni.drew.edu> 0.23-2
- apply a partial patch to Jemplate.pm from 0.23_01, to resolve issues with
  this release and Catalyst::View::Jemplate

* Tue Mar 24 2009 Chris Weyl <cweyl@alumni.drew.edu> 0.23-1
- touch-up

* Tue Mar 24 2009 Chris Weyl <cweyl@alumni.drew.edu> 0.23-0
- initial RPM packaging
- generated with cpan2dist (CPANPLUS::Dist::RPM version 0.0.8)

