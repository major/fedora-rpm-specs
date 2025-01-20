Name:           perl-Locale-Maketext-Lexicon
Version:        1.00
Release:        35%{?dist}
Summary:        Extract translatable strings from source
License:        MIT

URL:            https://metacpan.org/release/Locale-Maketext-Lexicon
Source0:        https://cpan.metacpan.org/authors/id/D/DR/DRTECH/Locale-Maketext-Lexicon-%{version}.tar.gz

Requires:       perl(Encode)
Requires:       perl(File::Glob)
Requires:       perl(File::Spec)
Requires:       perl(FileHandle)
Requires:       perl(HTML::Parser) >= 3.56
Requires:       perl(Lingua::EN::Sentence) >= 0.25
Requires:       perl(Locale::Maketext) >= 1.17
Requires:       perl(PPI) >= 1.203
Requires:       perl(Template) >= 2.20
Requires:       perl(Template::Constants) >= 2.75
Requires:       perl(YAML::Loader) >= 0.66

BuildRequires:  coreutils
BuildRequires:  findutils
BuildRequires:  %{__make}
BuildRequires:  perl-interpreter
BuildRequires:  perl-generators
BuildRequires:  perl(ExtUtils::MakeMaker) > 6.76
BuildRequires:  perl(Carp)
BuildRequires:  perl(Config)
BuildRequires:  perl(Cwd)
BuildRequires:  perl(Encode)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(File::Basename)
BuildRequires:  perl(File::Find)
BuildRequires:  perl(File::Glob)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(File::Spec::Functions)
BuildRequires:  perl(FileHandle)
BuildRequires:  perl(Getopt::Long)
BuildRequires:  perl(HTML::Parser) >= 3.56
# I18N::Langinfo is optional
BuildRequires:  perl(Lingua::EN::Sentence) >= 0.25
BuildRequires:  perl(Locale::Maketext) >= 1.17
BuildRequires:  perl(PPI) >= 1.203
BuildRequires:  perl(Symbol)
BuildRequires:  perl(Template) >= 2.20
BuildRequires:  perl(Template::Constants) >= 2.75
BuildRequires:  perl(Template::Directive)
BuildRequires:  perl(Template::Parser)
BuildRequires:  perl(Text::Haml)
BuildRequires:  perl(YAML::Loader) >= 0.66
BuildRequires:  perl(base)
BuildRequires:  perl(constant)
BuildRequires:  perl(strict)
BuildRequires:  perl(vars)
BuildRequires:  perl(warnings)

# Required by the tests
BuildRequires:  /usr/bin/msgunfmt
BuildRequires:  perl(FindBin)
# HTML::Mason is optional
BuildRequires:  perl(lib)
# Mason is optional
BuildRequires:  perl(Test)
BuildRequires:  perl(Test::More)
# Test::Pod 1.41 not used
BuildRequires:  perl(Tie::Hash)
BuildRequires:  perl(YAML) >= 0.66

BuildArch: noarch

# Remove under-specified dependencies
%global __requires_exclude %{?__requires_exclude:%__requires_exclude|}^perl\\((PPI|Template::Constants|YAML::Loader)\\)$

%description
Locale::Maketext::Lexicon provides lexicon-handling backends for
Locale::Maketext to read from other localization formats, such as PO files,
MO files, or from databases via the "Tie" interface.

%prep
%setup -q -n Locale-Maketext-Lexicon-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1
%{make_build}

%install
%{make_install}
chmod -R u+w ${RPM_BUILD_ROOT}/*

%check
%{__make} test

%files
%doc AUTHORS Changes README
%doc docs
%{_bindir}/*
%{_mandir}/man1/*
%{perl_vendorlib}/Locale
%{_mandir}/man3/*

%changelog
* Sat Jan 18 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.00-35
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.00-34
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.00-33
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.00-32
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.00-31
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.00-30
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Mon Nov 28 2022 Ralf Corsépius <corsepiu@fedoraproject.org> - 1.00-29
- Modernize spec.
- Update sources to sha512.

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.00-28
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed Jun 01 2022 Jitka Plesnikova <jplesnik@redhat.com> - 1.00-27
- Perl 5.36 rebuild

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.00-26
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.00-25
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Sun May 23 2021 Jitka Plesnikova <jplesnik@redhat.com> - 1.00-24
- Perl 5.34 rebuild

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.00-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.00-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jun 23 2020 Jitka Plesnikova <jplesnik@redhat.com> - 1.00-21
- Perl 5.32 rebuild

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.00-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.00-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri May 31 2019 Jitka Plesnikova <jplesnik@redhat.com> - 1.00-18
- Perl 5.30 rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.00-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sun Nov 25 2018 Emmanuel Seyman <emmanuel@seyman.fr> - 1.00-16
- Replace tabs with spaces in the spec file
- Drop the Group tag
- Replace PERL_INSTALL_ROOT with DESTDIR

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.00-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Jun 29 2018 Jitka Plesnikova <jplesnik@redhat.com> - 1.00-14
- Perl 5.28 rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.00-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.00-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Mon Jun 05 2017 Jitka Plesnikova <jplesnik@redhat.com> - 1.00-11
- Perl 5.26 rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.00-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon May 16 2016 Jitka Plesnikova <jplesnik@redhat.com> - 1.00-9
- Perl 5.24 rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.00-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Sat Jan 30 2016 Ralf Corsépius <corsepiu@fedoraproject.org> - 1.00-7
- Modernize spec.

* Tue Oct 13 2015 Petr Pisar <ppisar@redhat.com> - 1.00-6
- Specify all dependencies

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.00-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Jun 06 2015 Jitka Plesnikova <jplesnik@redhat.com> - 1.00-4
- Perl 5.22 rebuild

* Fri Aug 29 2014 Jitka Plesnikova <jplesnik@redhat.com> - 1.00-3
- Perl 5.20 rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.00-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Fri Mar 07 2014 Ralf Corsépius <corsepiu@fedoraproject.org> - 1.00-1
- Upstream update.

* Tue Feb 04 2014 Ralf Corsépius <corsepiu@fedoraproject.org> - 0.99-1
- Upstream update.
- Remove redundant explicit R: perl(YAML::Loader).
- Extend BR:'s.

* Mon Jan 27 2014 Ralf Corsépius <corsepiu@fedoraproject.org> - 0.98-2
- Reflect Text::Haml having made it into Fedora.

* Sun Jan 26 2014 Ralf Corsépius <corsepiu@fedoraproject.org> - 0.98-1
- Upstream update.

* Wed Jan 22 2014 Ralf Corsépius <corsepiu@fedoraproject.org> - 0.97-2
- Reflect Lingua::EN::Sentence having made it into Fedora.

* Fri Jan 17 2014 Ralf Corsépius <corsepiu@fedoraproject.org> - 0.97-1
- Upstream update.
- Modernize spec-file.

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.96-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Sat Jul 27 2013 Petr Pisar <ppisar@redhat.com> - 0.96-2
- Perl 5.18 rebuild

* Fri Jul 12 2013 Ralf Corsépius <corsepiu@fedoraproject.org> - 0.96-1
- Upstream update.

* Tue May 07 2013 Ralf Corsépius <corsepiu@fedoraproject.org> - 0.94-1
- Upstream update.
- Modernize spec.
- Filter perl(Text::Haml).

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.91-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.91-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Thu Jun 21 2012 Petr Pisar <ppisar@redhat.com> - 0.91-3
- Perl 5.16 rebuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.91-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Sep 06 2011 Ralf Corsépius <corsepiu@fedoraproject.org> - 0.91-1
- Upstream update.

* Fri Aug 19 2011 Ralf Corsépius <corsepiu@fedoraproject.org> - 0.86-1
- Upstream update.

* Wed Jul 20 2011 Petr Sabata <contyk@redhat.com> - 0.84-3
- Perl mass rebuild

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.84-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Mon Jan 17 2011 Ralf Corsépius <corsepiu@fedoraproject.org> - 0.84-1
- Upstream update.
- Replace custom filters with perl_default_filter.

* Mon Dec 20 2010 Marcela Maslanova <mmaslano@redhat.com> - 0.82-3
- 661697 rebuild for fixing problems with vendorach/lib

* Wed Jun 23 2010 Ralf Corsépius <corsepiu@fedoraproject.org> - 0.82-2
- Rebuild for perl-5.12.1.

* Thu May 06 2010 Ralf Corsépius <corsepiu@fedoraproject.org> - 0.82-1
- Upstream update.

* Mon May 03 2010 Marcela Maslanova <mmaslano@redhat.com> - 0.79-2
- Mass rebuild with perl-5.12.0

* Wed Mar 03 2010 Ralf Corsépius <corsepiu@fedoraproject.org> - 0.79-1
- Upstream update.

* Tue Mar 02 2010 Ralf Corsépius <corsepiu@fedoraproject.org> - 0.78-1
- Upstream update.

* Mon Dec  7 2009 Stepan Kasal <skasal@redhat.com> - 0.77-5
- rebuild against perl 5.10.1

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.77-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Thu Feb 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.77-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Thu Feb 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.77-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Fri Jan 02 2009 Ralf Corsépius <corsepiu@fedoraproject.org> - 0.77-1
- Upstream update.

* Sat Dec 20 2008 Ralf Corsépius <corsepiu@fedoraproject.org> - 0.76-1
- Upstream update.

* Sat Nov 29 2008 Ralf Corsépius <corsepiu@fedoraproject.org> - 0.75-1
- Upstream update.
- Reflect upstream maintainer having changed.
- BR: perl(Template), BR: perl(Test::Pod).

* Fri Oct 10 2008 Ralf Corsépius <corsepiu@fedoraproject.org> - 0.71-1
- Upstream update.
- Spec cleanup.
- Add spec hacks to work around rpm bugs.

* Thu Aug 28 2008 Ralf Corsépius <corsepiu@fedoraproject.org> - 0.68-2
- Filter out bogus requires.

* Tue Aug 26 2008 Ralf Corsépius <corsepiu@fedoraproject.org> - 0.68-1
- Upstream update.
- Reflect new Source0-URL.

* Wed Feb 27 2008 Tom "spot" Callaway <tcallawa@redhat.com> - 0.66-2
- Rebuild for perl 5.10 (again)

* Thu Feb 14 2008 Ralf Corsépius <rc040203@freenet.de> - 0.66-1
- Upstream update.

* Tue Feb  5 2008 Tom "spot" Callaway <tcallawa@redhat.com> - 0.65-2
- rebuild for new perl

* Fri Dec 28 2007 Ralf Corsépius <rc040203@freenet.de> - 0.65-1
- Upstream update.

* Tue Sep 04 2007 Ralf Corsépius <rc040203@freenet.de> - 0.64-2
- Update license tag.
- BR: perl(ExtUtils::MakeMaker).

* Mon Jun 11 2007 Ralf Corsépius <rc040203@freenet.de> - 0.64-1
- Upgrade to 0.64.
- Reflect source-url having changed.

* Fri Feb 16 2007 Ralf Corsépius <rc040203@freenet.de> - 0.62-1
- Upgrade to 0.62.
- Reflect licence change from Artistic/GPL to MIT.
- BR: /usr/bin/msgunfmt.

* Tue Sep 05 2006 Ralf Corsépius <rc040203@freenet.de> - 0.60-2
- Mass rebuild.

* Sat Apr 22 2006 Ralf Corsépius <rc040203@freenet.de> - 0.60-1
- Upstream update.

* Sun Mar 19 2006 Ralf Corsépius <rc040203@freenet.de> - 0.54-1
- Upstream update.

* Wed Mar 01 2006 Ralf Corsépius <rc040203@freenet.de> - 0.53-2
- Rebuild for perl-5.8.8.

* Mon Dec 05 2005 Ralf Corsepius <rc040203@freenet.de> - 0.53-1
- Upstream update.
